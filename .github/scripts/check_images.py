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

# 正则表达式匹配图片引用
image_pattern = re.compile(
    r'!\[.*?\]\(\s*([^\)\s]*)(?:\s+["'].*?["'])?\s*\)',
    re.IGNORECASE
)

# 集合：本地引用、网络引用
used_local = set()
used_external = set()

for md_file in md_files:
    content = md_file.read_text(encoding='utf-8')
    for match in image_pattern.findall(content):
        img_path = match.strip().replace('\\', '/')
        # 网络图片
        if any(img_path.startswith(p) for p in ('http://', 'https://', '//')):
            used_external.add(img_path)
            continue

        # 本地图片
        if img_path.startswith('/'):
            abs_path = Path(repo_root) / img_path[1:]
        else:
            abs_path = (md_file.parent / img_path).resolve()
        try:
            rel_path = abs_path.relative_to(repo_root).as_posix()
            used_local.add(rel_path)
        except ValueError:
            # 非仓库内路径
            used_external.add(img_path)

# 收集实际存在的本地图片文件
existing_images = set()
for root, _, files in os.walk(assets_dir):
    for file in files:
        path = Path(root) / file
        rel_path = path.relative_to(repo_root).as_posix()
        existing_images.add(rel_path)

# 计算差异
missing_images = sorted(used_local - existing_images)
unused_images = sorted(existing_images - used_local)

# 生成报告
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

report_content = '# Image Reference Check Report\n\n'
if lines:
    report_content += '\n'.join(lines)
else:
    report_content += '✅ 所有图片状态均正常！'

Path('image-report.md').write_text(report_content, encoding='utf-8')
print('Report generated: image-report.md')
