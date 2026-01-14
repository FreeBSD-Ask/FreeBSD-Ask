# FreeBSD 从入门到跑路

![](.gitbook/assets/web-logo.png)

🎉 欢迎来到 BSD 的世界！

FreeBSD 是真正自由（Liberty）的 **操作系统**，在这波谲云诡的世界中仍然坚守 BSD UNIX 哲学——恪守古老的法则，追寻真正的自由。

“入门”本是一种快乐，“跑路”亦是一种豁达。“本乘兴而行，兴尽而反，何必 FreeBSD 邪！”（化用房玄龄.晋书·王羲之传附王徽之传 [M].中华书局，1974）

## 📄 内容提要

这是一本开源的 FreeBSD 操作系统研究书籍，还包含一些关于 OpenBSD、NetBSD 等 Berkeley Unix 家族系统的导论章节。

[~~FreeBSD 项目即将归档（Archived）~~，为了保护我们心爱的操作系统……我们能做的事情就是，写一本书！](https://www.bilibili.com/bangumi/media/md3068)（化用《Love Live! School Idol Project》中的经典口号）


## 🖋️ 作者

本书是 **FreeBSD 中文社区** 许多人共同努力的成果。

- FreeBSD 中文社区 **首要** 联系方式为 **QQ 群**：[787969044](https://qm.qq.com/q/cX5mpJ36gg)（点击加群）

![FreeBSD 中文社区 QQ 群](.gitbook/assets/2025-qq.png)

- 微信群：由于微信平台的限制，须先加入 QQ 群，再联系群主获取新鲜的入群二维码。
- Discord：<https://discord.gg/j7VhWrhp3e>（需代理，可通过网页使用）
- Telegram 群组：[https://t.me/oh_my_BSD](https://t.me/oh_my_BSD)（需代理）


## 📚 电子书

目前网站提供了 PDF 和 EPUB 格式的电子文档：

- PDF（适用于印刷及电脑端离线阅读）下载地址：<https://docs.bsdcn.org/bsdbook.pdf> ![](https://img.shields.io/website?url=https%3A%2F%2Fdocs.bsdcn.org%2Fbsdbook.pdf&up_message=%E6%96%87%E4%BB%B6%E5%8F%AF%E7%94%A8&down_message=%E6%96%87%E4%BB%B6%E4%B8%8D%E5%8F%AF%E7%94%A8&style=for-the-badge&label=%E6%96%87%E6%A1%A3%E7%8A%B6%E6%80%81)

- EPUB（适用于移动端离线阅读）下载地址：<https://docs.bsdcn.org/bsdbook.epub> ![](https://img.shields.io/website?url=https%3A%2F%2Fdocs.bsdcn.org%2Fbsdbook.epub&up_message=%E6%96%87%E4%BB%B6%E5%8F%AF%E7%94%A8&down_message=%E6%96%87%E4%BB%B6%E4%B8%8D%E5%8F%AF%E7%94%A8&style=for-the-badge&label=%E6%96%87%E6%A1%A3%E7%8A%B6%E6%80%81)


>**注意**
>
>上面的网址是 ***docs*** 开头的而不是 ***book*** ！

EPUB 格式文档在手机上可使用 [微信读书](https://play.google.com/store/apps/details?id=com.tencent.weread&hl=zh) 打开，其格式显示较为完整；在电脑上则可使用 [CAJViewer 9](https://cajviewer.cnki.net/download.html) 打开。

上述电子文档始终反映实时的网页内容，随 Git 提交而 **实时更新**（但其文件名不会发生变化）。

电子书的生成由 [safreya](https://github.com/safreya) 开发的 [GitBook PDF/EPUB 导出工具](https://github.com/FreeBSD-Ask/gitbook-pdf-export) 提供支持。

## 🌐 部署地址

本书目前部署了两个域名以供访问，分别使用不同的网站架构：

- <https://book.bsdcn.org>
- <https://docs.bsdcn.org>
- <https://doc.bsdcn.org>（境内访问速度较佳）

除此之外，FreeBSD 中文社区未对本书进行任何部署。我们唯一的域名只有 “bsdcn.org”。

## 💬 意见反馈

由于编者水平所限，书中缺点和谬误之处自不可免。

如遇本书相关问题或网站技术问题：请发送邮件至 ykla [yklaxds@gmail.com](mailto:yklaxds@gmail.com)。关于本书内容问题，欢迎通过在桌面端网页右下方（或底部左下方）当前页面的 GitHub 直接提交 PR。

除此外有关中文社区的问题烦请加入 QQ 群后再联系 QQ 群主。

为了建设一个友爱、希望与和平的社区环境，请确保您的行为符合 [FreeBSD 中文社区行为规范（CoC）](https://docs.bsdcn.org/CODE_OF_CONDUCT) 及其精神。

由于架构设计原因，您必须使用 GitHub 账户登录方可留言，并且您在 docs 上的评论将会公开到 GitHub 存储库 [Handbook-giscus-discussions](https://github.com/FreeBSD-Ask/Handbook-giscus-discussions) 的 Discussions 中，您可自行前往上述位置管理您的历史留言。

## 🧭 目标与方向

详见 [贡献指南与开放任务](CONTRIBUTING.md)。

## ☕ 捐赠

请优先捐赠 FreeBSD 基金会！

![](.gitbook/assets/proud_donor.png)

[点此捐赠 FreeBSD 基金会](https://freebsdfoundation.org/donate-to-freebsd-foundation/)

需要你持有 VISA 信用卡：请在捐赠页面下使用 Amazon Pay 或 Google Pay，经测试可用。

你还可以通过必应搜索的 Rewards 积分 [对 FreeBSD 基金会进行捐赠](https://rewards.bing.com/redeem/000999036000?causeId=840-841545163&&PC=EMMX01)。也可以用该方式 [捐赠 NetBSD 基金会](https://rewards.bing.com/redeem/000999036000?causeId=840-134134071&PC=EMMX01)。

## 🏗️ 贡献者

![贡献者](https://contrib.nn.ci/api?no_bot=true&repo=FreeBSD-Ask/FreeBSD-Ask)

## ⚖️ 授权协议与法律声明

本项目采用《CC BY 4.0 署名 4.0 协议国际版》，详见 [署名 4.0 协议国际版法律文本](https://creativecommons.org/licenses/by/4.0/legalcode.zh-hans)。

为识别目的，本作品中引用的第三方商标（如 ®）、商号、服务标志（如 ™）、商品外观及版权材料（如 ©）等所有商业标识与知识产权内容，其相关权利均由各自合法权利人独立持有并受法律保护。前述引用仅为说明与指称之目的，不构成任何商业性使用、关联背书或法律授权，亦不视为对相关权利的限制或影响。

本作品出于说明、评论或教学目的，可能合理引用（包括但不限于文字、图像、数据等）了来源于第三方的内容（例如官方网站及其他公开网站、出版物等）。此类引用的知识产权仍归属原始权利人所有。相关引用均出于善意，符合合理使用原则，并非意在侵犯原作者或权利人的合法权益。

作品中演示或提及的任何第三方软件、源代码及文档，其全部知识产权（包括但不限于著作权、专利、商标与商业秘密）均由原权利人完整保留。如果您相信您的作品以侵犯版权的方式被复制或粘贴在我们的项目中，请通过电子邮件地址 ykla [yklaxds@gmail.com](mailto:yklaxds@gmail.com) 进行联系。我们将妥善处理。

除特别注明外，本书中的文字、图表等内容依据 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 协议发布。

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-orange.svg)](https://creativecommons.org/licenses/by/4.0/)

书中所有代码示例依据 [BSD 2 条款许可](https://opensource.org/license/bsd-2-clause) 发布。

[![License: BSD 2 Clause](https://img.shields.io/badge/License-BSD--2--Clause-EB0028.svg)](https://opensource.org/license/bsd-2-clause)

## 📜 项目历史

《FreeBSD 从入门到跑路》肇始于 2021 年 3 月 14 日，其原型最早可追溯至 ykla 于 2020 年 12 月 31 日发表的文章《FreeBSD 艺术科学哲学导论》。

<!-- GA_STATS:START -->

## 📈 统计信息

自 2022 年 6 月 1 日以降，本书的访问情况如下：

| 指标           | 统计数据     |
|:---------------:|:-------------:|
| 用户总数       | 42,608 位  |
| 会话数         | 88,940 次 |
| 浏览次数       | 618,214 次 |
| 平均会话时长   | 8 分 53 秒 |

<!-- GA_STATS:END -->

<!-- GA_BADGES:START -->

![总用户数](https://img.shields.io/badge/总用户数-42,608-green)
![会话数](https://img.shields.io/badge/会话数-88,940-orange)
![浏览次数](https://img.shields.io/badge/浏览次数-618,214-blue)
![平均会话时长](https://img.shields.io/badge/平均会话时长-8min53s-purple)

<!-- GA_BADGES:END -->

以上统计信息由 [Google Analytics](https://analytics.google.com/) 提供。

---

![GitHub 存储库状态图](https://repobeats.axiom.co/api/embed/0268f0741b1257dd58a7489442bd7829d2670313.svg "Repobeats analytics image")

以上图表由 [Repobeats analytics image](https://repobeats.axiom.co/) 提供。

---

<!-- CHINESE_CHAR_COUNT_START -->
文档总字数：82.87 万字；

统计时间：2026-01-14 09:38:45（北京时间）

与上周相比：+2.34 万字（+2.90%）

与上月相比：数据暂缺

<!-- CHINESE_CHAR_COUNT_END -->


<!-- commit-progress-start -->
**第 3 版编纂进度:**   （人工提交数: 1239 / 3533）

![进度徽章](.gitbook/assets/progress.svg)

距离第 3 版还需提交: 2294 次

提交统计（历史）:
- 人工提交: 8305
- 机器人提交: 190
<!-- commit-progress-end -->

---

~~本书得到的 ⭐ 真是太少啦！~~ 若本书对你有帮助，欢迎给本书所在的 [GitHub 项目存储库](https://github.com/FreeBSD-Ask/FreeBSD-Ask) 加颗 ⭐。
