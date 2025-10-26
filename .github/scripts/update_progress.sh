#!/usr/bin/env bash
set -euo pipefail

README="README.md"
SVG_FILE="progress.svg"
MARKER_START="<!-- commit-progress-start -->"
MARKER_END="<!-- commit-progress-end -->"
PER=3533

# 如果不存在标记则初始化
if ! grep -qF "$MARKER_START" "$README"; then
  echo -e "\n$MARKER_START\n$MARKER_END" >> "$README"
fi

# 获取总提交数
commits=$(git rev-list --count HEAD)

# 获取上次 progress_commits（如果有）
last_progress=$(awk -F '草稿提交数: ' '/草稿提交数:/ {gsub(/[）]/,"",$2); print $2}' "$README" | tail -n1)
last_progress=${last_progress:-0}

# 获取上次提交作者
last_author=$(git log -1 --pretty=format:'%an' -- "$README")

# 如果进度只增加 1 且上次提交者是 github-actions[bot] 则跳过
progress_commits=$(( commits % PER ))
if [[ $((progress_commits - last_progress)) -eq 1 && "$last_author" == "github-actions[bot]" ]]; then
  echo "进度仅增加 1 且上次提交者为 github-actions[bot]，跳过更新。"
  exit 0
fi

# 计算版本号和百分比
version=3
percent=$(awk "BEGIN {printf \"%.4f\", ($progress_commits*100)/$PER}")
percent_rounded=$(awk "BEGIN {printf \"%.2f\", (int(($percent+0.025)/0.05)*0.05)}")
to_next=$(( PER - progress_commits ))

# SVG 进度条参数
WIDTH=400
HEIGHT=30
FILLED_WIDTH=$(awk "BEGIN {printf \"%d\", $WIDTH*$percent_rounded/100}")
UNFILLED_WIDTH=$((WIDTH - FILLED_WIDTH))

# 生成渐变颜色函数（红黄绿）
get_color() {
  local p=$1
  local r g b
  if (( $(awk "BEGIN{print ($p<50)}") )); then
    ratio=$(awk "BEGIN {printf \"%.4f\", $p/50}")
    r=255
    g=$(awk "BEGIN {printf \"%d\", 255*$ratio}")
    b=0
  else
    ratio=$(awk "BEGIN {printf \"%.4f\", ($p-50)/50}")
    r=$(awk "BEGIN {printf \"%d\", 255 - 255*$ratio}")
    g=255
    b=0
  fi
  printf "#%02X%02X%02X" "$r" "$g" "$b"
}

fill_color=$(get_color $percent_rounded)
bg_color="#CCCCCC"

# 生成 SVG
cat > "$SVG_FILE" <<EOF
<svg xmlns="http://www.w3.org/2000/svg" width="$WIDTH" height="$HEIGHT">
  <rect x="0" y="0" width="$WIDTH" height="$HEIGHT" fill="$bg_color" rx="5" ry="5"/>
  <rect x="0" y="0" width="$FILLED_WIDTH" height="$HEIGHT" fill="$fill_color" rx="5" ry="5"/>
  <text x="$((WIDTH/2))" y="$((HEIGHT/2 + 5))" font-size="16" text-anchor="middle" fill="#000000">
    $percent_rounded%
  </text>
</svg>
EOF

# 构造替换内容
replacement=$(cat <<EOF
$MARKER_START
**第三版进度:** v$version  （草稿提交数: $progress_commits）  

![进度徽章]($SVG_FILE) 

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
  git add "$README" "$SVG_FILE"
  git commit -m "CI: 更新提交进度徽章"
  git push
fi
