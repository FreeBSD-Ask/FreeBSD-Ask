# FreeBSD 从入门到追忆（第三版：草稿）

欢迎你来到 FreeBSD 的世界！

FreeBSD 是真正自由（Liberty）的**操作系统**，在这波谲云诡的世界中仍然坚守 BSD UNIX 哲学——恪守古老的法则，追寻真正的自由。

请参与 [FreeBSD 中文社区 2025 年第二季度问卷调查](https://www.wjx.cn/vm/ebuJRkf.aspx#)（将于 2025.6.26 停止收集）

## 导出电子文档

可使用 [safreya](https://github.com/safreya) 编写的 [Python 脚本](https://github.com/FreeBSD-Ask/gitbook-pdf-export)来导出 PDF/EPUB。

此外，每周都会通过 GitHub Action 导出 PDF/EPUB 于 [releases](https://github.com/FreeBSD-Ask/FreeBSD-Ask/releases)（也许需要代理）。

## 关于

本书是 FreeBSD 中文社区许多人不懈努力的成果。

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

### 为什么不去建设《FreeBSD 手册》

拿着旧地图，如何寻得到新道路？

我们意识到在现有框架内推动《FreeBSD 手册》的全面现代化改进存在较大困难。笔者提交的多个 PR 往往需要经历一年甚至更长时间才被接受，提交者普遍缺乏时间感和动力。在这样沉重的阻力下，传统路径难以奏效。

因此，我们决定探索一种更开放、高效的协作模式，创造一本更贴近用户需求、更新及时且易于维护的 FreeBSD 文档。这本书的出现，正是为了填补这一空白，服务更广泛的 FreeBSD 用户和社区。

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
