import os
import json
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Metric, RunReportRequest

# GA4 Property ID
PROPERTY_ID = "317797940"

# 写入服务账户 JSON 文件
key_json = os.environ["GA4_SERVICE_KEY"]
with open("ga4_key.json", "w", encoding="utf-8") as f:
    f.write(key_json)

# 初始化 GA4 客户端
client = BetaAnalyticsDataClient.from_service_account_file("ga4_key.json")

# 请求自 2022-06-01 起累计数据
request = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    metrics=[
        Metric(name="totalUsers"),
        Metric(name="sessions"),
        Metric(name="screenPageViews"),
        Metric(name="averageSessionDuration"),
    ],
    date_ranges=[DateRange(start_date="2022-06-01", end_date="today")],
)

response = client.run_report(request)

# 提取指标值
row = response.rows[0].metric_values
total_users = int(row[0].value)
sessions = int(row[1].value)
page_views = int(row[2].value)
avg_session_duration = float(row[3].value)

# 更新 ga-stats.json
stats = {
    "totalUsers": total_users,
    "sessions": sessions,
    "pageViews": page_views,
    "avgSessionDuration": avg_session_duration
}
with open("ga-stats.json", "w", encoding="utf-8") as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)

# 更新 README 表格和徽章
readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

def replace_section(content, start, end, new_text):
    if start in content and end in content:
        before = content.split(start)[0]
        after = content.split(end)[1]
        return before + start + "\n" + new_text + "\n" + end + after
    return content

# Markdown 表格
stats_table = f"""
## 📊 GA4 数据（自 2022-06-01 起）

| 指标               | 数值       |
|--------------------|------------|
| 总用户数           | {total_users:,} |
| 会话数             | {sessions:,}   |
| 浏览次数           | {page_views:,} |
| 平均互动时长（秒） | {avg_session_duration:.2f} |
"""

# 徽章 Markdown（使用 Shields.io JSON endpoint 示例）
badges_md = f"""
![总用户数](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/FreeBSD-Ask/FreeBSD-Ask/main/ga-stats.json&label=总用户数&value=totalUsers)
![会话数](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/FreeBSD-Ask/FreeBSD-Ask/main/ga-stats.json&label=会话数&value=sessions)
![浏览次数](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/FreeBSD-Ask/FreeBSD-Ask/main/ga-stats.json&label=浏览次数&value=pageViews)
![平均互动时长](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/FreeBSD-Ask/FreeBSD-Ask/main/ga-stats.json&label=平均互动时长&value=avgSessionDuration)
"""

content = replace_section(content, "<!-- GA_STATS:START -->", "<!-- GA_STATS:END -->", stats_table)
content = replace_section(content, "<!-- GA_BADGES:START -->", "<!-- GA_BADGES:END -->", badges_md)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

# 自动提交并推送（只提交 README.md）
if [ -n "$(git status --porcelain "$README")" ]; then
  git config user.name "github-actions[bot]"
  git config user.email "github-actions[bot]@users.noreply.github.com"
  
  git add "$README"
  git commit -m "CI: 更新谷歌分析"
  git push origin main
fi
