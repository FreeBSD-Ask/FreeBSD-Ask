import os
from pathlib import Path

# 配置目录
repo_root = os.getcwd()
assets_dir = os.path.join(repo_root, '.gitbook', 'assets')

# 收集所有 Markdown 文件
md_files = []
for root, _, files in os.walk(repo_root):
    for file in files:
        if file.lower().endswith('.md'):
            md_files.append(Path(root) / file)

def extract_image_targets(text):
    """提取 Markdown 图片目标；处理转义与平衡方括号，并要求闭合的右括号。"""
    targets = []
    i = 0
    n = len(text)
    while i < n:
        start = text.find("![", i)
        if start < 0:
            break
        j = start + 2
        depth = 1
        while j < n and depth > 0:
            ch = text[j]
            if ch == "\\":
                j += 2
                continue
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
            j += 1
        if depth != 0 or j >= n or text[j] != "(":
            i = start + 2
            continue
        k = j + 1
        while k < n and text[k] in " \t\r\n":
            k += 1
        if k < n and text[k] == "<":
            end = text.find(">", k + 1)
            if end < 0:
                i = start + 2
                continue
            target = text[k + 1:end].strip()
            close = text.find(")", end + 1)
        else:
            tstart = k
            while k < n and text[k] not in " \t\r\n)":
                if text[k] == "\\" and k + 1 < n:
                    k += 2
                    continue
                k += 1
            target = text[tstart:k]
            close = text.find(")", k)
        if close < 0 or not target:
            i = start + 2
            continue
        targets.append(target)
        i = close + 1
    return targets

# 收集所有使用的图片路径
used_images = set()

for md_file in md_files:
    md_path = Path(md_file)
    content = md_path.read_text(encoding='utf-8')

    for target in extract_image_targets(content):
        img_path = target.strip().replace('\\', '/')
        if any(img_path.startswith(p) for p in ('http://', 'https://', '//')):
            continue

        # 处理绝对路径和相对路径
        if img_path.startswith('/'):
            abs_path = Path(repo_root) / img_path[1:]
        else:
            abs_path = (md_path.parent / img_path).resolve()

        try:
            rel_path = abs_path.relative_to(repo_root).as_posix()
            used_images.add(rel_path)
        except ValueError:
            pass

# 收集实际存在的图片文件
existing_images = set()
for root, _, files in os.walk(assets_dir):
    for file in files:
        path = Path(root) / file
        rel_path = path.relative_to(repo_root).as_posix()
        existing_images.add(rel_path)
        
# 排除指定图片（如 CI 自动生成的 progress.svg）
used_images = {img for img in used_images if not img.endswith('progress.svg')}
existing_images = {img for img in existing_images if not img.endswith('progress.svg')}

# 计算差异
missing_images = sorted(used_images - existing_images)
unused_images = sorted(existing_images - used_images)

# 生成报告（仅在有问题时）
if missing_images or unused_images:
    report = ["# 图片引用检查报告\n"]
    if missing_images:
        report.append("## ❌ 缺失图片\n")
        report.extend(f"- `{img}`" for img in missing_images)
    if unused_images:
        report.append("\n## ⚠️ 未使用的图片\n")
        report.extend(f"- `{img}`" for img in unused_images)
    Path('image-report.md').write_text("\n".join(report), encoding='utf-8')
else:
    # 如果正常，确保之前生成的报告不会误留
    report_path = Path('image-report.md')
    if report_path.exists():
        report_path.unlink()
