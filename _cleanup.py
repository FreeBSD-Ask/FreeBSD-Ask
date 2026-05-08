import os

BASE = r"c:\Users\ykla\Documents\FreeBSD-Ask"
SKIP_DIRS = {".git", ".github", ".gitbook", "node_modules", "__pycache__"}

def find_md():
    md = []
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in files:
            if fn.endswith(".md"):
                md.append(os.path.join(root, fn))
    return sorted(md)

cleaned_files = []
failed_files = []

for fpath in find_md():
    rel = os.path.relpath(fpath, BASE)
    try:
        with open(fpath, "rb") as f:
            raw = f.read()
    except:
        continue
    if not raw:
        continue

    try:
        content = raw.decode("utf-8")
    except:
        continue

    lines = content.split("\n")
    # Strip CR
    lines = [l.rstrip("\r") for l in lines]

    modified = False

    # 1. Strip trailing whitespace
    for i in range(len(lines)):
        old = lines[i]
        new = old.rstrip()
        if old != new:
            lines[i] = new
            modified = True

    # 2. Collapse excessive empty lines (>2 consecutive) outside code blocks
    in_code = False
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("```"):
            in_code = not in_code
            i += 1
            continue
        if in_code:
            i += 1
            continue
        if s == "":
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith("```") and lines[j].strip() == "":
                j += 1
            excess = j - i - 2
            if excess > 0:
                del lines[i: i + excess]
                modified = True
            i += 1
        else:
            i += 1

    if modified:
        new_content = "\n".join(lines)
        tmp = fpath + ".tmp"
        try:
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(new_content)
            os.replace(tmp, fpath)
            cleaned_files.append(rel)
        except PermissionError:
            failed_files.append(rel)
            try:
                os.remove(tmp)
            except:
                pass
        except Exception as e:
            failed_files.append(f"{rel}: {e}")
            try:
                os.remove(tmp)
            except:
                pass

print(f"已清理: {len(cleaned_files)} 个文件")
if cleaned_files:
    for f in cleaned_files:
        print(f"  {f}")

if failed_files:
    print(f"\n失败 (被锁定): {len(failed_files)} 个文件")
    for f in failed_files:
        print(f"  {f}")

if not cleaned_files and not failed_files:
    print("无需清理")
