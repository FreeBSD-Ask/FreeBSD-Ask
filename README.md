# FreeBSD 从入门到跑路（第三版：草稿）

欢迎你来到 FreeBSD 的世界！

FreeBSD 是真正自由（Liberty）的**操作系统**，在这波谲云诡的世界中仍然坚守 BSD UNIX 哲学——恪守古老的法则，追寻真正的自由。

## 加入 FreeBSD 中文社区（CFC）

本书是 FreeBSD 中文社区许多人不懈努力的成果。

- **首要**联系方式为 **QQ 群**：[787969044](https://qm.qq.com/q/cX5mpJ36gg)（点击加群）
- 微信群：因微信封闭性，须先加 QQ 群，再联系 QQ 群主获取新鲜二维码
- Discord：<https://discord.gg/j7VhWrhp3e>（需代理，可通过网页使用）
- Telegram 群组：[https://t.me/oh_my_BSD](https://t.me/oh_my_BSD)（需代理）

## 内容提要

本书涉及了 FreeBSD 14.3-RELEASE 和 13.5-RELEASE 的安装和日常使用，还包含一些 15.0-CURRENT 的内容。

## 历史

《FreeBSD 从入门到跑路》肇始于 2021 年 3 月 14 日，其原型最早可追溯至 2020 年 12 月 31 日 ykla 发布的文章《FreeBSD 艺术科学哲学导论》。

## 意见反馈

由于编写者水平所限，书中缺点和谬误之处自不可免。

如遇问题：请发送邮件至 [yklaxds@gmail.com](mailto:yklaxds@gmail.com)（优先）或联系 QQ 群群主。欢迎通过在桌面端网页右下方或底部左下方有当前页面的 GitHub 提交 PR。

## 目标与方向

构建能够在实践中逐步替代上游[《FreeBSD 手册》](https://docs.freebsd.org/en/books/handbook/)的现代化文档体系。

详见 [贡献指南与开放任务](CONTRIBUTING.md)

### 为什么不去建设《FreeBSD 手册》

我们意识到在现有框架内推动《FreeBSD 手册》的全面现代化改进存在较大困难。笔者提交的多个 PR 往往需要经历一年甚至更长时间才被接受，提交者普遍缺乏时间感和动力。在这样沉重的阻力下，传统路径难以奏效。

因此，我们决定探索一种更开放、高效的协作模式，创造一本更贴近用户需求、更新及时且易于维护的 FreeBSD 文档。这本书的出现，正是为了填补这一空白，服务更广泛的 FreeBSD 用户和社区。

### 方法论

使之成为“一本书”，而不仅仅是本字典或手册：

- 如果某一技术在最新版本被移除，则应及时移除其在本书的对应位置内容
- 使全书语气温柔而坚定
- 在最大化减少原文引用的前提下，重写各章节内容，删除冗余。
- 现代化、简化 BSD 中文文档协作方式：
  - 自动化（CI 检查、预览、生成 HTML/PDF）
  - 仅用最基础的 Markdown 语法，避免复杂扩展和繁琐流程
  - 技术和选材与时俱进，确保内容现代化。
- 严格验证每一部分：
  - 参考文献：不仅要求来源可查，而且要求来源可信：
  - 原理性内容：
    - 追溯到具体 FreeBSD 源码文件、提交记录或函数；
    - 具体到相关标准、规范、法律文件等
    - 分析其设计哲学与开发思路
  - 操作性内容：在 FreeBSD 环境中亲自试验，确保可复现
- 审视原作者的开发哲学与理念，评价其合理性，并尝试简单参与相关项目。
- 指出并修正上游官方手册中的错误或已过时内容。
- 生成英文版本

## 捐赠

请优先捐赠 FreeBSD 基金会！

![](.gitbook/assets/proud_donor.png)

[点此捐赠 FreeBSD 基金会](https://freebsdfoundation.org/donate)

需要持有 VISA 信用卡：请在捐赠页面“Click & Pledge”下使用 `Amazon Pay`，测试可用。

## 贡献者

![贡献者](https://contrib.nn.ci/api?repo=FreeBSD-Ask/FreeBSD-Ask)

## 电子书

可使用 [safreya](https://github.com/safreya) 编写的 [Python 脚本](https://github.com/FreeBSD-Ask/gitbook-pdf-export)来导出 PDF/EPUB。

此外，每周都会通过 GitHub Action 导出 PDF/EPUB 于 [releases](https://github.com/FreeBSD-Ask/FreeBSD-Ask/releases)（也许需要代理）。

## 授权协议

本项目采用《CC BY 4.0 署名 4.0 协议国际版》，详见[署名 4.0 协议国际版法律文本](https://creativecommons.org/licenses/by/4.0/legalcode.zh-hans)。

![CC BY](.gitbook/assets/by.png)

## Star 历史

若本书对你有帮助，也欢迎给此 [GitHub 项目](https://github.com/FreeBSD-Ask/FreeBSD-Ask)加颗 ⭐。

![⭐ 图](https://api.star-history.com/svg?repos=FreeBSD-Ask/FreeBSD-Ask&type=Date)
