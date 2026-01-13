#!/usr/bin/env bash
set -euo pipefail

README="README.md"
SVG_FILE=".gitbook/assets/progress.svg"
MARKER_START="<!-- commit-progress-start -->"
MARKER_END="<!-- commit-progress-end -->"

# 每一版 = 3533 次人工提交（唯一口径）
PER=3533
VERSION=3  # 当前目标版本（人工版本）

# 历史所有机器人作者（统一正则）
BOT_REGEX='(github-actions\[bot\]|dependabot\[bot\]|renovate\[bot\]|ImgBotApp|codecov\[bot\]|allcontributors\[bot\]|greenkeeper\[bot\])'

# 初始化 README 标记
if ! grep -qF "$MARKER_START" "$README"; then
  echo -e "\n$MARKER_START\n$MARKER_END" >> "$README"
fi

# ===== 统计（全部基于人工口径） =====

# 人工提交总数（历史全部）
human_commits=$(git log --perl-regexp \
  --author='^(?!.*'"$BOT_REGEX"').*$' \
  --pretty=oneline | wc -l | tr -d ' ')

# 机器人提交总数（仅展示）
bot_commits=$(git log --perl-regexp \
  --author="$BOT_REGEX" \
  --pretty=oneline | wc -l | tr -d ' ')

# 最近一次人工提交作者
last_author=$(git log --perl-regexp \
  --author='^(?!.*'"$BOT_REGEX"').*$' \
  -1 --pretty=format:'%an' | tr -d '\r\n' | xargs)

echo "最近人工提交者: [$last_author]"
echo "人工提交总数: $human_commits"
echo "机器人提交总数: $bot_commits"

# 无人工提交直接退出
if [[ -z "$last_author" || "$human_commits" -eq 0 ]]; then
  echo "未找到人工提交，跳过更新。"
  exit 0
fi

# ===== 版本计算（纯人工） =====

# 当前人工版本进度
current_progress=$(( human_commits - PER*(VERSION-1) ))
to_next=$(( PER*VERSION - human_commits ))

if (( to_next < 0 )); then
  VERSION=$((VERSION + 1))
  to_next=$(( PER*VERSION - human_commits ))
  msg="距离第 ${VERSION} 版还需提交: $to_next 次"
elif (( to_next == 0 )); then
  msg="第 ${VERSION} 版已完成"
elif (( to_next <= 100 )); then
  msg="第 ${VERSION} 版已近完成，还需提交"
else
  msg="距离第 ${VERSION} 版还需提交: $to_next 次"
fi

# 百分比（人工）
percent=$(awk "BEGIN {printf \"%.4f\", ($current_progress*100)/$PER}")
percent_rounded=$(awk "BEGIN {printf \"%.2f\", (int(($percent+0.025)/0.05)*0.05)}")

# ===== SVG =====

ORIG_WIDTH=400
WIDTH=$(awk "BEGIN {printf \"%d\", $ORIG_WIDTH*0.65}")
HEIGHT=30
FILLED_WIDTH=$(awk "BEGIN {w=$WIDTH*$percent_rounded/100; print (w>0 && w<1) ? 1 : int((w+0.999999))}")
bg_color="#CCCCCC"

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
  <text x="$(($FILLED_WIDTH/2<15?15:$FILLED_WIDTH/2))"
        y="$(($HEIGHT/2 + 5))"
        font-size="16"
        text-anchor="middle"
        fill="#000000">$percent_rounded%</text>
</svg>
EOF

# ===== README 替换 =====

replacement=$(cat <<EOF
$MARKER_START
**第 $VERSION 版编纂进度:**   （人工提交数: $current_progress / $PER）

![进度徽章]($SVG_FILE)

$msg

提交统计（历史）:
- 人工提交: $human_commits
- 机器人提交: $bot_commits
$MARKER_END
EOF
)

awk -v start="$MARKER_START" -v end="$MARKER_END" -v repl="$replacement" '
BEGIN {inside=0}
{
  if ($0 == start) { print repl; inside=1; next }
  if (inside==1 && $0 == end) { inside=0; next }
  if (inside==0) print
}' "$README" > "${README}.tmp"

if cmp -s "$README" "${README}.tmp"; then
  echo "无变化，无需提交。"
  rm "${README}.tmp"
  exit 0
fi

mv "${README}.tmp" "$README"
echo "README 已更新：第 ${VERSION} 版，人工进度 ${percent_rounded}%"

# ===== CI 提交 =====

if [ -n "$(git status --porcelain)" ]; then
  git config user.name "github-actions[bot]"
  git config user.email "github-actions[bot]@users.noreply.github.com"

  git add "$README" "$SVG_FILE"
  git commit -m "CI: 更新人工提交进度徽章

统计口径:
- 每版人工提交数: $PER
- 当前人工提交总数: $human_commits
- 机器人提交总数: $bot_commits
"

  git push
fi