#!/usr/bin/env python3
import re
import sys
import os
import time
import json
import random
import hashlib
import requests
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from urllib.parse import urlparse
from tqdm import tqdm

# 禁用 HTTPS 警告
requests.packages.urllib3.disable_warnings()

# ================= 基本配置 =================

CACHE_FILE = "archive_cache.json"
MAX_WORKERS = 3 
THREAD_DELAY = (3, 7)

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
]

ARCHIVE_SERVICES = [
    {"name": "Wayback", "type": "wayback", "api": "https://web.archive.org/save/", "retries": 2, "timeout": 30},
    {"name": "Archive.ph", "type": "archive_ph", "domains": ["archive.is", "archive.today", "archive.ph"], "retries": 2, "timeout": 45},
    {"name": "Megalodon", "type": "megalodon", "api": "https://megalodon.jp/pc/get", "retries": 2, "timeout": 30}
]

SKIP_KEYWORDS = ["备份", "backup", "archive", "鱼拓", "mirror", "snapshot"]

SKIP_DOMAINS = {
    "bilibili.com",
    "www.bilibili.com",
    "freshports.org",
    "www.freshports.org",
    "man.freebsd.org",
    "bugs.freebsd.org",
    "analytics.google.com",
    "repobeats.axiom.co",
    "img.shields.io",
    "cajviewer.cnki.net",
    "web.archive.org",
    "qm.qq.com",
    "t.me",
    "play.google.com",
    "docs.bsdcn.org",
    "rewards.bing.com",
    "creativecommons.org",
    "contrib.nn.ci",
}

STOP_EVENT = threading.Event()
CACHE_LOCK = threading.Lock()
PRINT_LOCK = threading.Lock()
LIST_LOCK = threading.Lock()
TASK_LOCK = threading.Lock() 

ACTIVE_TASKS = {}
SESSION_SUCCESS = []
SESSION_FAILED = []
SESSION_UPDATED_FILES = [] 

# 新增：全局进度变量
TOTAL_FILES = 0
PROCESSED_FILES = 0

# ================= UI & 日志 =================

def safe_log(msg, color="0"):
    with PRINT_LOCK:
        tqdm.write(f"[{datetime.now().strftime('%H:%M:%S')}] \033[{color}m{msg}\033[0m")

def ui_monitor_thread():
    last_line_count = 0
    while not STOP_EVENT.is_set():
        with PRINT_LOCK:
            now = time.time()
            if last_line_count > 0:
                sys.stdout.write(f"\033[{last_line_count}A")

            lines = []
            lines.append(f"\033[1;36m┏━━ 备份进度监控 (线程: {MAX_WORKERS}) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

            # 1. 进度条板块 (新增)
            with LIST_LOCK:
                total = TOTAL_FILES
                done = PROCESSED_FILES
            
            percent = (done / total * 100) if total > 0 else 0
            bar_len = 30
            filled = int(bar_len * percent / 100)
            bar = "█" * filled + "░" * (bar_len - filled)
            
            lines.append(f"┃ 总进度: [{bar}] {percent:>5.1f}% ({done}/{total} 文件)")

            # 2. 活跃任务
            lines.append(f"\033[1;34m┣━━ 当前网络抓取 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            with TASK_LOCK:
                current_tasks = list(ACTIVE_TASKS.items())[:5]

            if not current_tasks:
                lines.append("┃ \033[90m暂无活跃抓取任务\033[0m")
            else:
                for task_item in current_tasks:
                    try:
                        t_id, t_info = task_item
                        t_elapsed = now - t_info.get("start_time", now)
                        t_url = t_info.get("url", "Unknown")
                        t_service = t_info.get("service", "Wait")
                        url_display = t_url[:50] + "..." if len(t_url) > 50 else t_url
                        lines.append(f"┃ [T{t_id:03}] {t_elapsed:>5.1f}s | {t_service:<10} | {url_display}")
                    except: continue

            # 3. 最新更新的文件
            lines.append(f"\033[1;32m┣━━ 最近更新的文件 (5) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            with LIST_LOCK:
                recent_files = SESSION_UPDATED_FILES[-5:]
            if not recent_files:
                lines.append("┃ \033[90m尚未写入任何文件\033[0m")
            else:
                for fname in reversed(recent_files):
                    lines.append(f"┃ ✔ {fname[:70]}")

            lines.append(f"\033[1;36m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

            out = "".join(f"\r\033[K{line}\n" for line in lines)
            sys.stdout.write(out)
            sys.stdout.flush()
            last_line_count = len(lines)
        time.sleep(0.5)

# ================= 核心逻辑 =================

def find_markdown_links(text):
    links = []
    pattern = re.compile(r'\[([^\]]+)\]\((https?://)') 
    for m in pattern.finditer(text):
        start, url_start, depth = m.start(), m.start(2), 1
        i = url_start
        while depth > 0 and i < len(text):
            if text[i] == '(': depth += 1
            elif text[i] == ')': depth -= 1
            i += 1
        if depth == 0:
            url = text[url_start:i - 1]
            links.append({"start": start, "end": i, "text": m.group(1), "url": url})
    return links

def should_skip_url(url):
    if not url or not url.startswith(('http://', 'https://')): return True
    try:
        host = urlparse(url).netloc.lower()
        return not host or "." not in host or host in SKIP_DOMAINS
    except: return True

def load_cache():
    with CACHE_LOCK:
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, "r", encoding="utf-8") as f: return json.load(f)
            except: pass
    return {}

def save_cache_item(url_hash, data):
    with CACHE_LOCK:
        cache = {}
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, "r", encoding="utf-8") as f: cache = json.load(f)
            except: pass
        cache[url_hash] = data
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, indent=2, ensure_ascii=False)

def request_archive(service, url, tid):
    last_err = "Err"
    for attempt in range(1, service["retries"] + 1):
        if STOP_EVENT.is_set(): return "Stopped"
        with TASK_LOCK:
            if tid in ACTIVE_TASKS: ACTIVE_TASKS[tid].update({"service": service["name"], "attempt": attempt})
        try:
            headers = {"User-Agent": random.choice(USER_AGENTS), "Referer": url}
            if service["type"] == "wayback":
                r = requests.get(service["api"] + url, headers=headers, timeout=service["timeout"], verify=False)
                if "web.archive.org/web/" in r.url: return r.url
            elif service["type"] == "archive_ph":
                r = requests.post(f"https://{random.choice(service['domains'])}/submit/", data={"url": url}, headers=headers, timeout=service["timeout"], verify=False)
                m = re.search(r'https?://(?:archive\.is|archive\.today|archive\.ph)/(?:[A-Za-z0-9]+|wb/\d+/)', r.text)
                if m: return m.group(0)
            elif service["type"] == "megalodon":
                r = requests.post(service["api"], data={"url": url, "agree": "1"}, headers=headers, timeout=service["timeout"], verify=False)
                if "megalodon.jp" in r.url and re.search(r'\d{4}-\d{4}', r.url): return r.url
        except Exception as e: last_err = type(e).__name__
        time.sleep(random.uniform(*THREAD_DELAY))
    return last_err

def process_url_task(url):
    if should_skip_url(url): return None
    tid = threading.get_ident() % 1000
    with TASK_LOCK: ACTIVE_TASKS[tid] = {"url": url, "start_time": time.time(), "service": "Wait"}
    try:
        h = hashlib.md5(url.encode()).hexdigest()
        cache = load_cache()
        if h in cache and cache[h].get("archive_url"):
            res = cache[h]["archive_url"]
            with LIST_LOCK: SESSION_SUCCESS.append((url, res))
            return res
        services = ARCHIVE_SERVICES[:]
        random.shuffle(services)
        for s in services:
            res = request_archive(s, url, tid)
            if isinstance(res, str) and res.startswith("http"):
                save_cache_item(h, {"archive_url": res, "service": s["name"]})
                with LIST_LOCK: SESSION_SUCCESS.append((url, res))
                return res
        with LIST_LOCK: SESSION_FAILED.append((url, "Fail"))
        return None
    finally:
        with TASK_LOCK: ACTIVE_TASKS.pop(tid, None)

def process_file(path):
    global PROCESSED_FILES
    try:
        with open(path, "r", encoding="utf-8") as f: content = f.read()
    except: 
        with LIST_LOCK: PROCESSED_FILES += 1
        return

    links = find_markdown_links(content)
    todo = [l for l in links if not any(k in l["text"].lower() for k in SKIP_KEYWORDS) 
            and "[备份](" not in content[l["end"]:l["end"]+40] and not should_skip_url(l["url"])]
    
    if not todo:
        with LIST_LOCK: PROCESSED_FILES += 1
        return

    urls = list(set(l["url"] for l in todo))
    results = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = {ex.submit(process_url_task, u): u for u in urls}
        for f in as_completed(futs): results[futs[f]] = f.result()

    new_content = content
    todo.sort(key=lambda x: x["start"], reverse=True)
    count = 0
    for l in todo:
        archived = results.get(l["url"])
        if archived:
            new_content = new_content[:l["end"]] + f" [备份]({archived})" + new_content[l["end"]:]
            count += 1

    if count > 0:
        with open(path, "w", encoding="utf-8") as f: f.write(new_content)
        with LIST_LOCK:
            SESSION_UPDATED_FILES.append(os.path.basename(path))
        safe_log(f"已更新: {os.path.basename(path)} (+{count})", "32")
    
    # 文件处理结束，增加进度计数
    with LIST_LOCK:
        PROCESSED_FILES += 1

# ================= 递归收集文件 =================

def collect_md_files(path):
    md_files = []
    if os.path.isfile(path) and path.endswith(".md"):
        md_files.append(path)
    elif os.path.isdir(path):
        for entry in os.scandir(path):
            md_files.extend(collect_md_files(entry.path))
    return md_files

# ================= 主函数 =================

def main():
    global TOTAL_FILES
    if len(sys.argv) != 2:
        print("用法: python link.py <文件或目录>")
        return

    target = sys.argv[1]
    
    # 递归收集文件
    all_files = collect_md_files(target)
    
    TOTAL_FILES = len(all_files)
    if TOTAL_FILES == 0:
        print("错误: 未找到任何 .md 文件。")
        return

    ui = threading.Thread(target=ui_monitor_thread, daemon=True)
    ui.start()

    try:
        for f_path in all_files:
            if STOP_EVENT.is_set(): break
            process_file(f_path)
    except KeyboardInterrupt:
        STOP_EVENT.set()
    finally:
        STOP_EVENT.set()
        time.sleep(1)
        print("\n" + "="*50)
        print(f"完成！共处理 {PROCESSED_FILES} 个文件。")

if __name__ == "__main__":
    main()
