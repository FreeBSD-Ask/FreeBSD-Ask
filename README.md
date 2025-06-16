# FreeBSD 从入门到追忆（第三版：草稿）

欢迎你来到 FreeBSD 的世界！

FreeBSD 是真正自由（Liberty）的**操作系统**，在这波谲云诡的世界中仍然坚守 BSD UNIX 哲学——恪守古老的法则，追寻真正的自由。

请参与 [FreeBSD 中文社区 2025 年第二季度问卷调查](https://www.wjx.cn/vm/ebuJRkf.aspx#)（将于 2025.6.26 停止收集）

## 导出电子文档

可使用 [safreya](https://github.com/safreya) 编写的 [Python 脚本](https://github.com/FreeBSD-Ask/gitbook-pdf-export)来导出 PDF/EPUB。

此外，每周都会通过 GitHub Action 导出 PDF/EPUB 于 [releases](https://github.com/FreeBSD-Ask/FreeBSD-Ask/releases)（也许需要代理）。

## 关于

本书是 FreeBSD 开源社区许多人不懈努力的成果。

### 内容提要

本书涉及了 FreeBSD 14.3-RELEASE 和 13.5-RELEASE 的安装和日常使用，还包含一些 15.0-CURRENT 的内容。

### 加入 FreeBSD 中文社区（CFC）

- **首要**联系方式为 **QQ 群**：[787969044](https://qm.qq.com/q/cX5mpJ36gg)（点击加群）
- 微信群：因微信封闭性，须先加 QQ 群再联系 QQ 群主
- Discord：<https://discord.gg/j7VhWrhp3e>（需要代理。可通过网页使用）
- Telegram 群组：[https://t.me/oh_my_BSD](https://t.me/oh_my_BSD)（需要代理）

### 历史

《FreeBSD 从入门到追忆》肇始于 2021 年 3 月 14 日，其原型最早可追溯至 2020 年 12 月 31 日 ykla 发布的文章《FreeBSD 艺术科学哲学导论》。

### 意见反馈

由于编写者水平所限，书中缺点和谬误之处自不可免。

如遇问题：请发送邮件至 [yklaxds@gmail.com](mailto:yklaxds@gmail.com)（优先）或联系 QQ 群群主。欢迎通过在桌面端网页右下方或底部左下方有当前页面的 GitHub 提交 PR。

## 目标与方向

详见 [贡献指南与开放任务](CONTRIBUTING.md)

我们观察到 FreeBSD 上游文档项目当前面临一些挑战：

- FreeBSD 手册与文章整体已与现实情况严重脱节，形式化内容占据了过多篇幅。
- 文档项目的整体维护动力和技术更新显得匮乏，提交频率远低于一个活跃开源项目的预期水平；
- 开发者长期忽视来自邮件列表与 Bugzilla 的社区反馈，普遍拒绝采纳改进建议，甚至以“车棚问题”（bikeshedding）为由，对文档质量的系统性讨论未能被有效采纳或讨论。邮件列表缺乏实质性协商；
- 文档审阅机制几乎陷入瘫痪，存在大量无人处理的提交与修订请求。维护者与审阅者的工作流程有待优化。
- FreeBSD 基金会的协调作用在文档领域体现不足，其资源（如会议支持）主要集中于欧美地区，对亚洲、南美等地区的实际用户及语言翻译社区的支持力度有待加强，相关法务支持也显不足。
- 文档构建工具链复杂而落后，缺乏现代化编辑体验，项目结构混乱，提交者本人往往也难以掌握。中文翻译流程未有公开清晰文档，参与门槛高，导致翻译项目处于停滞状态。
- 无论是成为文档贡献者还是获得提交权限，流程的透明度、指导的充分性以及审核的及时性都有较大提升空间，影响了新人的参与热情和社区活力。

### 为什么不去建设《FreeBSD 手册》

正是基于上述观察到的挑战，我们意识到在现有框架内推动《FreeBSD 手册》的全面现代化更新存在较大困难（例如，笔者提交的多个 PR 经历了 1-2 年才被接受），因此我们决定探索新的路径。这本书的诞生，正是为了尝试一种更高效、更开放的协作模式，以期为 FreeBSD 用户和社区提供更及时、更易用的高质量文档。

### 现阶段总体目标

创建现代化、易用且社区驱动的 FreeBSD 文档体系，以有效补充和适应当前的用户需求，并积极促进 FreeBSD 开源社区的整体发展。

即在各个方面全面地、彻底地取代 FreeBSD 上游社区[《FreeBSD 手册》](https://docs.freebsd.org/en/books/handbook/)的地位。

### 方法论

使之成为“一本书”，而不仅仅是本字典或手册：

- 避免引用和复制粘贴原文。在此基础上，对其章节内容进行重写。
- 使 BSD 中文文档协作方式现代化、简单化（工具链自动化、使用最简单的 Markdown 语法等），避免因为繁琐的语法、流程、繁苛的要求劝退可能存在的贡献者
- 使 BSD 中文文档技术选材、内容现代化
- 确保每个部分都是经过实际验证的，不仅要求来源可查，而且要求来源可信：
- 如果是原理性内容，要找出最原始的出处，具体到 FreeBSD 的哪段代码，哪次提交，哪个函数；
- 如果是可操作内容，必须自己试一试。
- 审视原有开发者的开发哲学与理念，是否合理，并进行评价并初步参与其项目。
- 指出上游社区官方手册的错误或过时内容
- 在本书编写完成后，我们会将其翻译为英文，分享给全球社区，以期成为国际用户的重要参考。

## 捐赠

请优先捐赠 FreeBSD 基金会！

若本书对你有帮助，也欢迎给此 [GitHub 项目](https://github.com/FreeBSD-Ask/FreeBSD-Ask)加颗 ⭐。

![](.gitbook/assets/proud_donor.png)

[点此捐赠 FreeBSD 基金会](https://freebsdfoundation.org/donate)

需要持有 VISA 信用卡：请在捐赠页面“Click & Pledge”下使用 `Amazon Pay`，测试可用。

## 贡献者

![贡献者](https://contrib.nn.ci/api?repo=FreeBSD-Ask/FreeBSD-Ask)

## 授权协议

本项目采用《CC BY 4.0 署名 4.0 协议国际版》，详见[署名 4.0 协议国际版法律文本](https://creativecommons.org/licenses/by/4.0/legalcode.zh-hans)。

![CC BY](.gitbook/assets/by.png)
