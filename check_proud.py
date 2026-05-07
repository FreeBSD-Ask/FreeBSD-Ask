import re
from pathlib import Path
BASE = Path(r"c:\Users\ykla\Documents\FreeBSD-Ask")

for md in sorted(BASE.rglob("*.md")):
    if md.name == "README.md": continue
    try:
        c = md.read_text("utf-8")
        for m in re.finditer(r'(?:!\[[^\]]*\])?\([^)]*?proud[^)]*?\)', c, re.I):
            rel = str(md.relative_to(BASE))
            if "proud" in m.group(0).lower():
                print(f"[{rel}] {m.group(0)[:120]}")
    except:
        pass

# also check what proud files exist
for f in sorted((BASE / ".gitbook" / "assets").rglob("proud*")):
    print(f"  EXISTS: {f.relative_to(BASE)}")
