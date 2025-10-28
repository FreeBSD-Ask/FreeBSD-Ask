#!/usr/bin/env bash
set -euo pipefail

README="README.md"
SVG_FILE="progress.svg"
MARKER_START="<!-- commit-progress-start -->"
MARKER_END="<!-- commit-progress-end -->"
PER=3533
VERSION=3  # 当前目标版本

# 如果不存在标记则初始化
if ! grep -qF "$MARKER_START" "$README"; then
  echo -e "\n$MARKER_START\n$MARKER_END" >> "$README"
fi

# 获取总提交数
commits=$(git rev-list --count HEAD)

# 获取最后一次提交者名称（去除多余空格和换行）
last_author=$(git log -1 --pretty=format:'%an' | tr -d '\r\n' | xargs)

echo "最近提交者: [$last_author]"

# 如果上次提交者是 github-actions[bot] 则跳过
if [[ "$last_author" == "github-actions[bot]" ]]; then
  echo "上次提交者是 github-actions[bot]，无变化，跳过更新。"
  exit 0
fi

# 当前草稿提交量
current_progress=$(( commits - PER*(VERSION-1) + 1 ))
# 距离目标版本还需提交
to_next=$(( PER*VERSION - commits - 1 ))

# 自动调整版本与提示文本
if (( to_next < 0 )); then
  msg="第 ${VERSION} 版已完成"
  VERSION=$((VERSION + 1))
  to_next=$(( PER*VERSION - commits - 1 ))
  msg="距离第 ${VERSION} 版还需提交: $to_next 次"
elif (( to_next == 0 )); then
  msg="第 ${VERSION} 版已完成"
elif (( to_next <= 100 )); then
  msg="第 ${VERSION} 版已近完成，还需提交"
else
  msg="距离第 ${VERSION} 版还需提交: $to_next 次"
fi

# 计算百分比和进度条
percent=$(awk "BEGIN {printf \"%.4f\", ($current_progress*100)/$PER}")
# 四舍五入到 0.05%
percent_rounded=$(awk "BEGIN {printf \"%.2f\", (int(($percent+0.025)/0.05)*0.05)}")

# SVG 进度条参数
ORIG_WIDTH=400
WIDTH=$(awk "BEGIN {printf \"%d\", $ORIG_WIDTH*0.65}")  # 减少 35%
HEIGHT=30
FILLED_WIDTH=$(awk "BEGIN {w=$WIDTH*$percent_rounded/100; print (w>0 && w<1) ? 1 : int((w+0.999999))}")
UNFILLED_WIDTH=$((WIDTH - FILLED_WIDTH))
bg_color="#CCCCCC"

# 生成渐变颜色（红→黄→绿）SVG
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

# 构造渐变 SVG
GRADIENT_ID="grad1"
cat > "$SVG_FILE" <<EOF
<svg xmlns="http://www.w3.org/2000/svg" width="$WIDTH" height="$HEIGHT">
  <defs>
    <linearGradient id="$GRADIENT_ID" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF0000"/>
      <stop offset="50%" stop-color="#FFFF00"/>
      <stop offset="100%" stop-color="#00FF00"/>
    </linearGradient>
  </defs>
    <!-- 背景灰色 -->
  <rect x="0" y="0" width="$WIDTH" height="$HEIGHT" fill="$bg_color" rx="5" ry="5"/>
  <rect x="0" y="0" width="$FILLED_WIDTH" height="$HEIGHT" fill="url(#$GRADIENT_ID)" rx="5" ry="5"/>
  <text x="$(($FILLED_WIDTH/2<15?15:$FILLED_WIDTH/2))" y="$(($HEIGHT/2 + 5))" font-size="16" text-anchor="middle" fill="#000000">$percent_rounded%</text>
</svg>
EOF

# 构造替换内容
replacement=$(cat <<EOF
$MARKER_START
**第 $VERSION 版进度:**   （草稿提交数: $current_progress）  

![进度徽章]($SVG_FILE) 

$msg
$MARKER_END
EOF
)

# 替换 README
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
echo "README 已更新：版本 ${VERSION}，进度 ${percent_rounded}%"

# 自动提交并推送
if [ -n "$(git status --porcelain)" ]; then
  git config user.name "github-actions[bot]"
  git config user.email "github-actions[bot]@users.noreply.github.com"
  
  git add "$README" "$SVG_FILE"
  git commit -m "CI: 更新提交进度徽章"

# 自动提交并推送
if [ -n "$(git status --porcelain)" ]; then
  git config user.name "github-actions[bot]"
  git config user.email "github-actions[bot]@users.noreply.github.com"
  
  git add "$README" "$SVG_FILE"
  git commit -m "CI: 更新提交进度徽章"

  git remote set-url origin git@github.com:${GITHUB_REPOSITORY}.git

  # 使用 SSH 推送（Deploy Key）
  GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=no" git push origin main
fi


