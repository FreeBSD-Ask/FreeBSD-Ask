# FreeBSD 从入门到追忆（第三版：草稿）

FreeBSD 是真正自由（Liberty）的**操作系统**，在这波谲云诡的世界中仍然坚守 BSD UNIX 哲学——恪守古老的法则，追寻真正的自由。

请参与 [FreeBSD 中文社区 2025 年第二季度问卷调查](https://www.wjx.cn/vm/ebuJRkf.aspx#)（2025.6.26 停止收集）

## 关于

### 内容提要

本书旨在深入剖析 FreeBSD 操作系统，敉平从陌生人到研究者之间的鸿沟。

### 加入 FreeBSD 中文社区（CFC）

- **首要**联系方式为 **QQ 群**：[787969044](https://qm.qq.com/q/cX5mpJ36gg)（点击加群）
- 微信群：因微信封闭性，须先加 QQ 群再联系 QQ 群主
- Discord：<https://discord.gg/j7VhWrhp3e>（需要代理。可通过网页使用，无需安装软件）
- Telegram 群组：[https://t.me/oh_my_BSD](https://t.me/oh_my_BSD)（需要代理）

### 历史

《FreeBSD 从入门到追忆》肇始于 2021 年 3 月 14 日，其原型最早可追溯至 2020 年 12 月 31 日 ykla 发布的文章《FreeBSD 艺术科学哲学导论》。

### 意见反馈

由于编写者水平所限，书中缺点和谬误之处自不可免。

如遇问题：请发送邮件至 [yklaxds@gmail.com](mailto:yklaxds@gmail.com)（优先）或联系 QQ 群群主。欢迎通过在桌面端网页右下方或底部左下方有当前页面的 GitHub 提交 PR。

## 贡献指南与开放任务

详见 [贡献指南与开放任务](CONTRIBUTING.md)

我们观察到，由于：

- 手册与文章整体已与现实严重脱节。约三分之一内容已无参考价值，形式化冗余占据篇幅；
- 社区欠缺维护动力，几乎无新技术内容。手册年度提交量远低于合理维护水平，显示出严重停滞。（其一年的提交甚至都没有本书一天的提交量大）；
- 开发者拒绝采纳邮件列表或 Bug 报告中的改进建议，闭门造车，并称这是在讨论车棚问题。也不与社区讨论任何重大事项；
- 审阅机制形同虚设，外部贡献者难以参与；
- FreeBSD 基金会的不作为；
- 工具链陈旧复杂，至今大多数提交者本人都看不懂项目结构。至今搞不懂中文手册翻译流程。

### 为什么不去建设《FreeBSD 手册》

这正是本书诞生的主要原因之一。

上游文档目前存在船大难掉头的现状，试图从内部改革早已不现实。

笔者的多个 PR 均在 1-2 年后才被接受，提交者严重缺乏时间感，如此，何谈改进？

故，提出以下目标与方法用于改善社区现状，以期促进 FreeBSD 及 FreeBSD 中文社区发展。

### 现阶段总体目标

在各个方面全面地、彻底地取代 FreeBSD 上游的 [《FreeBSD 手册》](https://docs.freebsd.org/en/books/handbook/)的地位。在一定程度上让人们优先选择此书而不是上游手册。

### 方法

使之成为“一本书”，而不仅仅是本字典或手册：

- 避免引用和复制粘贴原文。在此基础上，对其章节内容进行重写。
- 使 BSD 中文文档协作方式现代化、简单化（工具链自动化、使用最简单的 Markdown 语法等），避免因为繁琐的语法、流程、繁苛的要求劝退可能存在的贡献者
- 使 BSD 中文文档技术选材、内容现代化
- 确保每个部分都是经过实际验证的，不仅要求来源可查，而且要求来源可信：
- 如果是原理性内容，要找出最原始的出处，具体到 FreeBSD 的哪段代码，哪次提交，哪个函数；
- 如果是可操作内容，必须自己试一试。
- 审视原有开发者的开发哲学与理念，是否合理，并进行评价并初步参与其项目。
- 指出上游社区官方手册的错误或过时内容
- 在编写完成后将之翻译为英文呈现

## 导出本书的 PDF 文档

可使用 [safreya](https://github.com/safreya) 编写的 [Python 脚本](https://github.com/FreeBSD-Ask/gitbook-pdf-export)来导出 PDF。

此外，每周都会通过 GitHub Action 导出 PDF 于 [releases](https://github.com/FreeBSD-Ask/FreeBSD-Ask/releases)（也许需要代理）。

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
