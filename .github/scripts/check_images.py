import os
import re
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

# 正则表达式匹配图片引用（本地或网络）
# 解释：!\[alt\](url "title") 或者 ![alt](url)
image_pattern = re.compile(r'!\[.*?\]\(\s*([^\)\s]+)(?:\s+["\'].*?["\'])?\s*\)', re.IGNORECASE)

# 集合：本地引用、网络引用
used_local = set()
used_external = set()

for md_file in md_files:
    content = md_file.read_text(encoding='utf-8')
    for match in image_pattern.findall(content):
        img_path = match.strip().replace('\\', '/')
        # 网络图片判断
        if img_path.startswith(('http://', 'https://', '//')):
            used_external.add(img_path)
            continue

        # 本地图片路径解析
        if img_path.startswith('/'):
            abs_path = Path(repo_root) / img_path.lstrip('/')
        else:
            abs_path = (md_file.parent / img_path).resolve()
        try:
            rel_path = abs_path.relative_to(repo_root).as_posix()
            used_local.add(rel_path)
        except ValueError:
            # 非仓库内部路径视为外部引用
            used_external.add(img_path)

# 收集实际存在的本地图片文件
existing_images = set()
for root, _, files in os.walk(assets_dir):
    for file in files:
        path = Path(root) / file
        existing_images.add(path.relative_to(repo_root).as_posix())

# 计算差异
missing_images = sorted(used_local - existing_images)
unused_images = sorted(existing_images - used_local)

# 生成报告内容
lines = []
if missing_images:
    lines.append('## ❌ 缺失图片')
    lines += [f'- `{img}`' for img in missing_images]
if unused_images:
    lines.append('## ⚠️ 未使用的图片')
    lines += [f'- `{img}`' for img in unused_images]
if used_external:
    lines.append('## 🌐 网络图片引用')
    lines += [f'- `{url}`' for url in sorted(used_external)]

report = '# Image Reference Check Report\n\n'
report += '\n'.join(lines) if lines else '✅ 所有图片状态均正常！'

# 写入报告文件
Path('image-report.md').write_text(report, encoding='utf-8')
print('Report generated: image-report.md')
