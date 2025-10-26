#!/usr/bin/env bash
set -euo pipefail

README="README.md"
MARKER_START="<!-- commit-progress-start -->"
MARKER_END="<!-- commit-progress-end -->"
PER=3533

# 如果不存在标记则初始化
if ! grep -qF "$MARKER_START" "$README"; then
  echo -e "\n$MARKER_START\n$MARKER_END" >> "$README"
fi

# 获取总提交数
commits=$(git rev-list --count HEAD)

# 计算版本号和进度
version=$(( commits / PER ))
progress_commits=$(( commits % PER ))
# 计算百分比并四舍五入到最接近的 0.05%
percent=$(awk "BEGIN {printf \"%.4f\", ($progress_commits*100)/$PER}")  # 精度保留 4 位
percent_rounded=$(awk "BEGIN {printf \"%.2f\", (int(($percent+0.025)/0.05)*0.05)}")
to_next=$(( PER - progress_commits ))

# 红黄绿渐变颜色
if awk "BEGIN{exit !($percent_rounded < 50)}"; then
  ratio=$(awk "BEGIN {printf \"%.4f\", $percent_rounded/50}")
  r=255
  g=$(awk "BEGIN {printf \"%d\", 255 * $ratio}")
  b=0
else
  ratio=$(awk "BEGIN {printf \"%.4f\", ($percent_rounded-50)/50}")
  r=$(awk "BEGIN {printf \"%d\", 255 - 255 * $ratio}")
  g=255
  b=0
fi

hex=$(printf "%02X%02X%02X" "$r" "$g" "$b")
badge_url="https://img.shields.io/badge/进度-${percent_rounded}%25-%23${hex}?style=for-the-badge"

# 构造替换内容
replacement=$(cat <<EOF
$MARKER_START
**第三版进度:** v$version  （草稿提交数: $progress_commits）  

![进度徽章]($badge_url) 

距离第三版还需提交: $to_next 次
$MARKER_END
EOF
)

# 替换 README 中标记内容
awk -v start="$MARKER_START" -v end="$MARKER_END" -v repl="$replacement" '
BEGIN {inside=0}
{
  if($0 == start) { print repl; inside=1; next }
  if(inside==1 && $0 == end) { inside=0; next }
  if(inside==0) print
}' "$README" > "${README}.tmp"

# 若无变化则退出
if cmp -s "$README" "${README}.tmp"; then
  echo "无变化（进度 <0.1%），无需提交。"
  rm "${README}.tmp"
  exit 0
fi

mv "${README}.tmp" "$README"
echo "README 已更新：版本 ${version}，进度 ${percent_rounded}%"

# 自动提交并推送
if [ -n "$(git status --porcelain)" ]; then
  git config user.name "github-actions[bot]"
  git config user.email "github-actions[bot]@users.noreply.github.com"
  git add "$README"
  git commit -m "CI: 更新提交进度徽章"
  git push
fi
