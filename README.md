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

由于：

- FreeBSD 文档项目（FreeBSD Documentation Project），已经完全失效
- 上游社区缺乏行动力，维护者不足且引入的新维护者欠缺维护意愿
- 一意孤行不听取社区邮件列表建议
- 旁人难于参与（无人审阅、缺乏时间感等）
- 其一年的提交甚至都没有本书一天的提交量大（对于上游社区这种技术性文档，这绝不意味着“稳定”，只能是“过时”）。

故，提出以下目标与方法用于改善社区现状，以期促进 FreeBSD 发展。

### 现阶段总体目标

- 使 BSD 中文文档协作方式现代化（工具链自动化、使用最简单的 Markdown 语法等）
- 使 BSD 中文文档技术选材、内容现代化
- 在各个方面全面地、彻底地取代 FreeBSD 上游的 *[FreeBSD 手册](https://docs.freebsd.org/en/books/handbook/)*。尽量在不引用其原文的条件下对其章节内容进行重写。
- 在一定程度上（人们会优先选择此书）取代本书其他 BSD 的官方上游社区的手册

### 方法

使之成为“一本书”，而不仅仅是本字典或手册：

- 确保每个部分都是经过实际验证的，不仅要求来源可查，而且要求来源可信：
- 如果是原理性内容，要找出最原始的出处；
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
