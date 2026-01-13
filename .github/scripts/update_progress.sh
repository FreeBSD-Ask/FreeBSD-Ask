#!/usr/bin/env bash
set -euo pipefail

README="README.md"
SVG_FILE=".gitbook/assets/progress.svg"
MARKER_START="<!-- commit-progress-start -->"
MARKER_END="<!-- commit-progress-end -->"
PER=3533
VERSION=3  # 当前目标版本

# 机器人账号列表
BOT_AUTHORS=(
  "github-actions\\[bot\\]"
  "dependabot\\[bot\\]"
  "renovate\\[bot\\]"
  "ImgBotApp"
  "codecov\\[bot\\]"
  "allcontributors\\[bot\\]"
  "greenkeeper\\[bot\\]"
)

# 如果不存在标记则初始化
if ! grep -qF "$MARKER_START" "$README"; then
  echo -e "\n$MARKER_START\n$MARKER_END" >> "$README"
fi

# 构建排除机器人参数
EXCLUDE_BOTS_OPTIONS=()
for bot in "${BOT_AUTHORS[@]}"; do
  EXCLUDE_BOTS_OPTIONS+=( --invert-grep --author="$bot" )
done

# 非机器人提交总数
commits=$(git rev-list --count HEAD "${EXCLUDE_BOTS_OPTIONS[@]}")

# 最近一次非机器人提交者
last_author=$(git log -1 --pretty=format:'%an' "${EXCLUDE_BOTS_OPTIONS[@]}" | tr -d '\r\n' | xargs)

echo "最近非机器人提交者: [$last_author]"
echo "非机器人提交总数: $commits"

# 没有非机器人提交则退出
if [[ -z "$last_author" ]]; then
  echo "未找到非机器人提交，跳过更新。"
  exit 0
fi

# 当前草稿提交量
current_progress=$(( commits - PER*(VERSION-1) + 1 ))
# 距离目标版本还需提交
to_next=$(( PER*VERSION - commits - 1 ))

# 自动调整版本与提示文本
if (( to_next < 0 )); then
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

# 百分比
percent=$(awk "BEGIN {printf \"%.4f\", ($current_progress*100)/$PER}")
percent_rounded=$(awk "BEGIN {printf \"%.2f\", (int(($percent+0.025)/0.05)*0.05)}")

# SVG 参数
ORIG_WIDTH=400
WIDTH=$(awk "BEGIN {printf \"%d\", $ORIG_WIDTH*0.65}")
HEIGHT=30
FILLED_WIDTH=$(awk "BEGIN {w=$WIDTH*$percent_rounded/100; print (w>0 && w<1) ? 1 : int((w+0.999999))}")
bg_color="#CCCCCC"

# 生成 SVG
cat > "$SVG_FILE" <<EOF
<svg xmlns="http://www.w3.org/2000/svg" width="$WIDTH" height="$HEIGHT">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF0000"/>
      <stop offset="50%" stop-color="#FFFF00"/>
      <stop offset="100%" stop-color="#00FF00"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="$WIDTH" height="$HEIGHT" fill="$bg_color" rx="5" ry="5"/>
  <rect x="0" y="0" width="$FILLED_WIDTH" height="$HEIGHT" fill="url(#grad1)" rx="5" ry="5"/>
  <text x="$(($FILLED_WIDTH/2<15?15:$FILLED_WIDTH/2))" y="$(($HEIGHT/2 + 5))"
        font-size="16" text-anchor="middle" fill="#000000">$percent_rounded%</text>
</svg>
EOF

# README 替换块
replacement=$(cat <<EOF
$MARKER_START
**第 $VERSION 版编纂进度:**   （草稿提交数: $current_progress）

![进度徽章]($SVG_FILE)

$msg
$MARKER_END
EOF
)

awk -v start="$MARKER_START" -v end="$MARKER_END" -v repl="$replacement" '
BEGIN {inside=0}
{
  if($0 == start) { print repl; inside=1; next }
  if(inside==1 && $0 == end) { inside=0; next }
  if(inside==0) print
}' "$README" > "${README}.tmp"

if cmp -s "$README" "${README}.tmp"; then
  echo "无变化，无需提交。"
  rm "${README}.tmp"
  exit 0
fi

mv "${README}.tmp" "$README"
echo "README 已更新：版本 ${VERSION}，进度 ${percent_rounded}%"

if [ -n "$(git status --porcelain)" ]; then
  git config user.name "github-actions[bot]"
  git config user.email "github-actions[bot]@users.noreply.github.com"
  git add "$README" "$SVG_FILE"
  git commit -m "CI: 更新提交进度徽章（排除机器人提交）"
  git push origin main
fi