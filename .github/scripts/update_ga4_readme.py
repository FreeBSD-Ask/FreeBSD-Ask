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
avg_session_duration_sec = float(row[3].value)

# 将平均互动时长转换为 分:秒
minutes = int(avg_session_duration_sec // 60)
seconds = int(avg_session_duration_sec % 60)
avg_session_duration_str = f"{minutes} 分 {seconds} 秒"
avg_session_duration_str2 = f"{minutes}min{seconds}s"

# 更新 ga-stats.json（保留秒数）
stats = {
    "totalUsers": total_users,
    "sessions": sessions,
    "pageViews": page_views,
    "avgSessionDuration": avg_session_duration_sec
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

# Markdown 表格（显示为分:秒）
stats_table = f"""
## 📈 统计信息

自 2022 年 6 月 1 日以降，本书的访问情况如下：

| 指标               | 统计       |
|:--------------------:|:------------:|
| 用户总数           | {total_users:,}  |
| 会话数             | {sessions:,}  |
| 浏览次数           | {page_views:,}  |
| 平均会话时长     | {avg_session_duration_str} |
"""

# 徽章 Markdown（保持原 JSON 秒数）
badges_md = f"""
![总用户数](https://img.shields.io/badge/总用户数-{total_users:,}-green)
![会话数](https://img.shields.io/badge/会话数-{sessions:,}-orange)
![浏览次数](https://img.shields.io/badge/浏览次数-{page_views:,}-blue)
![平均互动时长](https://img.shields.io/badge/每次会话的平均互动时长-{avg_session_duration_str2}-purple)
"""

# 替换 README 中的区块
content = replace_section(content, "<!-- GA_STATS:START -->", "<!-- GA_STATS:END -->", stats_table)
content = replace_section(content, "<!-- GA_BADGES:START -->", "<!-- GA_BADGES:END -->", badges_md)

# 写回 README.md
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
