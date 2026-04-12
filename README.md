# FreeBSD 从入门到跑路

![🎉 欢迎来到 BSD 的世界！](.gitbook/assets/web-logo.png)

🎉 欢迎来到 BSD 的世界！

FreeBSD 是一款真正自由（Liberty）的 **操作系统**，在这波谲云诡的世界中仍然坚守 BSD UNIX 哲学——**恪守古老的法则，追寻真正的自由**。

“入门”本是一种快乐，“跑路”亦是一种豁达。“本乘兴而行，兴尽而反，何必 FreeBSD 邪！”（化用晋书·王羲之传附王徽之传[M]//房玄龄.晋书.北京:中华书局,1974）

## 内容提要

>**注意**
>
>本书约有 60% 的章节尚未完成（详见下文），已有的章节虽经审阅和修订，但仍非最终版本。

本书是一本关于 FreeBSD 操作系统的开源研究著作，同时包含 OpenBSD、NetBSD 等 Berkeley Unix 家族系统的导论章节。

[~~FreeBSD 项目即将归档（Archived）~~，为了保护我们心爱的操作系统……我们能做的事情就是，写一本书！](https://www.bilibili.com/bangumi/media/md3068)（化用《Love Live! School Idol Project》中的经典口号）

## 关于作者

本书由 FreeBSD 中文社区多位成员共同编写完成。

![微信公众号](.gitbook/assets/wechatnew.png)

微信公众号：bsdcn2018

- FreeBSD 中文社区主要联系方式为 QQ 群：[787969044](https://qm.qq.com/q/cX5mpJ36gg)

![FreeBSD 中文社区 QQ 群](.gitbook/assets/2025-qq.png)

- 微信群：受微信平台限制，需先加入 QQ 群，再联系群主获取最新入群二维码。
- Discord：<https://discord.gg/j7VhWrhp3e>（需代理，可通过网页访问）
- Telegram 群组：[https://t.me/oh_my_BSD](https://t.me/oh_my_BSD)（需代理）

## 电子文档

本书提供 PDF 和 EPUB 两种格式的电子文档：

- PDF（适用于印刷及桌面端离线阅读）下载地址：<https://docs.bsdcn.org/bsdbook.pdf> ![PDF 文件状态](https://img.shields.io/website?url=https%3A%2F%2Fdocs.bsdcn.org%2Fbsdbook.pdf&up_message=%E6%96%87%E4%BB%B6%E5%8F%AF%E7%94%A8&down_message=%E6%96%87%E4%BB%B6%E4%B8%8D%E5%8F%AF%E7%94%A8&style=for-the-badge&label=%E6%96%87%E6%A1%A3%E7%8A%B6%E6%80%81)

- EPUB（适用于移动端离线阅读）下载地址：<https://docs.bsdcn.org/bsdbook.epub> ![EPUB 文件状态](https://img.shields.io/website?url=https%3A%2F%2Fdocs.bsdcn.org%2Fbsdbook.epub&up_message=%E6%96%87%E4%BB%B6%E5%8F%AF%E7%94%A8&down_message=%E6%96%87%E4%BB%B6%E4%B8%8D%E5%8F%AF%E7%94%A8&style=for-the-badge&label=%E6%96%87%E6%A1%A3%E7%8A%B6%E6%80%81)

>**注意**
>
>以上下载地址以 `docs.bsdcn.org` 域名开头，非 `book.bsdcn.org`。

EPUB 格式文档在移动端可使用 [微信读书](https://play.google.com/store/apps/details?id=com.tencent.weread&hl=zh) 打开，格式显示完整；在桌面端可使用 [CAJViewer 9](https://cajviewer.cnki.net/download.html) 打开。

电子文档内容与网页版实时同步，随 Git 提交更新，文件名保持不变。

电子书生成由 [safreya](https://github.com/safreya) 开发的 [GitBook PDF/EPUB 导出工具](https://github.com/FreeBSD-Ask/gitbook-pdf-export) 提供支持，该工具可将 GitBook 格式内容转换为 PDF 和 EPUB 格式。

## 部署地址

本书通过三个域名提供访问服务，各域名使用不同网站架构：

- <https://book.bsdcn.org>
- <https://docs.bsdcn.org>
- <https://doc.bsdcn.org>（境内访问速度较佳）

FreeBSD 中文社区未通过其他域名部署本书，唯一官方域名为 `bsdcn.org`。

## 意见反馈

受编者水平所限，书中难免存在疏漏与错误。

如遇内容问题或网站技术问题，请发送邮件至 ykla [yklaxds@gmail.com](mailto:yklaxds@gmail.com)。关于内容问题，欢迎通过 GitHub 提交 PR，入口位于桌面端网页当前页面的右下角或底部左下角。

社区相关问题请加入 QQ 群后联系群主。

请遵循 [FreeBSD 中文社区行为规范（CoC）](https://docs.bsdcn.org/CODE_OF_CONDUCT)。

留言功能需使用 GitHub 账户登录，评论将公开至 GitHub 存储库 [Handbook-giscus-discussions](https://github.com/FreeBSD-Ask/Handbook-giscus-discussions) 的 Discussions 板块，可前往该位置管理历史留言。

## 目标与方向

详见 [贡献指南与开放任务](CONTRIBUTING.md)。

## 捐赠

请优先考虑向 FreeBSD 基金会捐赠。

![捐赠 FreeBSD 基金会](.gitbook/assets/proud_donor.png)

[点此捐赠 FreeBSD 基金会](https://freebsdfoundation.org/donate-to-freebsd-foundation/)

支付方式支持：VISA 信用卡（可通过 Amazon Pay 或 Google Pay）、万事达品牌借记卡。

此外，可通过 Bing Rewards 积分 [对 FreeBSD 基金会进行捐赠](https://rewards.bing.com/redeem/000999036000?causeId=840-841545163&&PC=EMMX01)。Bing Rewards 是微软必应搜索提供的积分计划。同方式亦可 [捐赠 NetBSD 基金会](https://rewards.bing.com/redeem/000999036000?causeId=840-134134071&PC=EMMX01)。

## 贡献者

![贡献者](https://contrib.nn.ci/api?no_bot=true&repo=FreeBSD-Ask/FreeBSD-Ask)

## 授权协议与法律声明

本项目采用《CC BY 4.0 署名 4.0 协议国际版》，核心条款包括：署名——允许对作品进行复制、发行、修改、再创作，需保留原作者署名，详见 [署名 4.0 协议国际版法律文本](https://creativecommons.org/licenses/by/4.0/legalcode.zh-hans)。

本作品引用的第三方商标、商号、服务标志、商品外观及版权材料，其相关权利均由各自权利人持有。前述引用仅为说明与指称之目的。

为说明、评论或教学目的，本作品合理引用第三方内容（文字、图像、数据等），知识产权归属原始权利人。

作品中涉及的第三方软件、源代码及文档，知识产权由原权利人保留。如认为您的作品被侵权，请通过电子邮件 ykla [yklaxds@gmail.com](mailto:yklaxds@gmail.com) 联系。

除特别注明外，本书中的文字、图表等内容依据 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 协议发布。

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-orange.svg)](https://creativecommons.org/licenses/by/4.0/)

书中所有代码示例依据 [BSD 2 条款许可](https://opensource.org/license/bsd-2-clause) 发布。

[![License: BSD 2 Clause](https://img.shields.io/badge/License-BSD--2--Clause-EB0028.svg)](https://opensource.org/license/bsd-2-clause)

## 项目历史

《FreeBSD 从入门到跑路》始于 2021 年 3 月 14 日，其原型可追溯至 ykla 于 2020 年 12 月 31 日发表的文章《FreeBSD 艺术科学哲学导论》。

<!-- GA_STATS:START -->

## 统计信息

自 2022 年 6 月 1 日以降，本书的访问情况如下：

| 指标 | 统计数据 |
| ---- | -------- |
| 用户总数 | 45,606 位 |
| 会话数 | 93,941 次 |
| 浏览次数 | 639,565 次 |
| 平均会话时长 | 8 分 48 秒 |

<!-- GA_STATS:END -->

<!-- GA_BADGES:START -->

![总用户数](https://img.shields.io/badge/总用户数-45,606-green)
![会话数](https://img.shields.io/badge/会话数-93,941-orange)
![浏览次数](https://img.shields.io/badge/浏览次数-639,565-blue)
![平均会话时长](https://img.shields.io/badge/平均会话时长-8min48s-purple)

<!-- GA_BADGES:END -->

以上统计信息由 [Google Analytics](https://analytics.google.com/) 提供。

---

![GitHub 存储库状态图](https://repobeats.axiom.co/api/embed/0268f0741b1257dd58a7489442bd7829d2670313.svg "Repobeats analytics image")

以上图表由 [Repobeats analytics image](https://repobeats.axiom.co/) 提供。

---

<!-- CHINESE_CHAR_COUNT_START -->
文档总字数：99.44 万字；

统计时间：2026-04-12 14:00:04（北京时间）

与上周相比：−1058 字（−0.11%）

与上月相比：+6.24 万字（+6.69%）

<!-- CHINESE_CHAR_COUNT_END -->

<!-- commit-progress-start -->
**第 3 版编纂进度:** （人工提交数: 1433 / 3533）

![进度徽章](.gitbook/assets/progress.svg)

距离第 3 版还需提交: 2100 次

提交统计（历史）:
- 人工提交: 8499
- 机器人提交: 329
<!-- commit-progress-end -->

## ⭐ 图

![⭐ 图](https://api.star-history.com/image?repos=FreeBSD-Ask/FreeBSD-Ask&type=date&legend=top-left)

若本书对您有帮助，欢迎为 [GitHub 项目存储库](https://github.com/FreeBSD-Ask/FreeBSD-Ask) 加颗 ⭐。
