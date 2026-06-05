# 2.3 FreeBSD 开发模型

FreeBSD 的版本发布遵循 CURRENT → ALPHA → BETA → RC → RELEASE 的迭代周期，STABLE 分支的 ABI 则保持固定，各有明确的适用场景。

## FreeBSD 版本概述

FreeBSD 的版本管理体系包含两个开发分支（CURRENT 与 STABLE）和四个版本阶段（ALPHA → BETA → RC → RELEASE），其中 ALPHA 为 STABLE 分支创建后的预发布快照。

具体流程：CURRENT → 分出 STABLE 分支 → ALPHA → BETA → RC → RELEASE。

RELEASE 版本经过完整的 BETA→RC 测试周期，发布后仅接受安全与稳定性修复，适用于生产环境。

![FreeBSD 版本更迭](../.gitbook/assets/bsd-release-versions.png)

> **注意**
>
> 该图展示的版本更迭关系较为简化，实际流程中 X.0-RELEASE 来自 X-STABLE 分支，而 X-STABLE 由 main 分支（即 X.CURRENT）分出。

> **注意**
>
> 只有 ALPHA、BETA、RC 和 RELEASE（[且必须为一级架构](https://www.freebsd.org/platforms/)）才能使用命令 `freebsd-update` 更新系统，其余版本需通过源代码编译或使用二进制的 pkgbase 更新。

## CURRENT 分支

FreeBSD-CURRENT 是 FreeBSD 最前沿的源代码，包含正在进行的工作、实验性变更和可能出现在下一个正式版本中的过渡机制。虽然许多 FreeBSD 开发人员每天都会编译 FreeBSD-CURRENT 的源代码，但有时会出现源代码无法编译的情况。这些问题会尽快得到解决，但 FreeBSD-CURRENT 所带来的究竟是灾难还是新功能，取决于同步的源代码版本。

FreeBSD-CURRENT 主要面向三个兴趣群体：

- 积极参与某部分源代码树的 FreeBSD 社区成员。

- 积极的测试者，他们愿意花时间解决问题，提出关于变更和 FreeBSD 整体方向的建议，并提交补丁。

- 想要关注 FreeBSD 状态，使用当前源代码作为参考，或偶尔发表评论或贡献代码的用户。

预发布功能尚未经过充分测试，且很可能存在缺陷，FreeBSD-CURRENT 不应视为提前获取新功能的捷径。其他提交同样有可能引入新缺陷，而不是修复既有缺陷，因此它也不是获取缺陷修复的捷径。FreeBSD-CURRENT 并未得到“正式支持”。

使用 -CURRENT 的用户应跟踪 FreeBSD-CURRENT：

1. 加入 [FreeBSD-CURRENT 邮件列表](https://lists.freebsd.org/subscription/freebsd-current) 和 [源代码仓库主分支提交信息列表](https://lists.freebsd.org/subscription/dev-commits-src-main)。这是 **必需** 的，以便了解人们对系统当前状态的评论，并接收有关 FreeBSD-CURRENT 当前状态的重要公告。[源代码仓库主分支提交信息列表](https://lists.freebsd.org/subscription/dev-commits-src-main) 会记录每个变更的提交日志条目，以及关于可能副作用的相关信息。

   要加入这些列表，请访问 [FreeBSD 列表服务器](https://lists.freebsd.org/)，点击要订阅的列表，并按照说明进行操作。如果要跟踪整个源代码树的变更，而不仅是 FreeBSD-CURRENT 的变更，订阅 [所有分支的源代码仓库提交信息列表](https://lists.freebsd.org/subscription/dev-commits-src-all)。
2. 与 FreeBSD-CURRENT 源代码同步。通常使用 git 从 FreeBSD Git 仓库的 `main` 分支检出 -CURRENT 代码。
3. 由于仓库体积较大，有些用户选择仅同步他们感兴趣的部分源代码或他们正在贡献补丁的部分。但计划从源代码编译操作系统的用户必须下载 **所有** 的 FreeBSD-CURRENT，而不仅是选定的部分。请阅读 [FreeBSD-CURRENT 邮件列表](https://lists.freebsd.org/subscription/freebsd-current) 和 **/usr/src/UPDATING** 以保持更新，了解有时会成为必要的启动过程。
4. 积极参与！建议 FreeBSD-CURRENT 用户提交增强功能或缺陷修复。附带代码的方案始终受到欢迎。

## STABLE 分支

FreeBSD-STABLE 是用于发布主要版本的开发分支。

与一般 Linux 发行版中的“稳定版”概念不同，其名称中的“稳定”指的是该分支的 ABI（Application Binary Interface，应用程序二进制接口）保持稳定，而非指系统整体稳定性，也可以理解为“固定”。在没有充分测试的开发或测试环境中，不应将任何生产服务器更新到 FreeBSD-STABLE。应使用 FreeBSD 的最新正式版本，即 RELEASE。

CURRENT 分支中的代码在经过充分测试后（需满足 MFC 最短三天的要求，MFC 指 `Merge From CURRENT`，类似于 `backporting` 即向后移植）会推送到 STABLE 分支，但这并不保证两个分支都没有重大缺陷。尽管 FreeBSD-STABLE 分支应该始终能够编译并运行，但这并无保证。

STABLE 仍然是一个开发分支，任何时候，FreeBSD-STABLE 的源代码都可能不适合普遍使用。它只是另一条工程开发轨道，并非面向终端用户。

更多用户运行 FreeBSD-STABLE 而非 FreeBSD-CURRENT，某些在 FreeBSD-CURRENT 中未发现的缺陷和极端情况会在 FreeBSD-STABLE 中暴露，因此不能盲目地跟踪 FreeBSD-STABLE。

希望跟踪或参与 FreeBSD 开发过程，特别是与下一个 FreeBSD 发布相关的开发者，应该考虑跟踪 FreeBSD-STABLE。

要跟踪 FreeBSD-STABLE：

1. 加入 [FreeBSD-STABLE 邮件列表](https://lists.freebsd.org/subscription/freebsd-stable)，以便及时了解 FreeBSD-STABLE 中可能出现的构建依赖或其他需要特别注意的问题。开发人员在此邮件列表中也会宣布他们正在考虑的有争议的修复或更新，用户可以在此期间回应并提出意见。

   加入相关的 git 列表以跟踪所选分支。例如，跟踪 15-STABLE 分支的用户应该加入 [稳定分支提交信息列表](https://lists.freebsd.org/subscription/dev-commits-src-branches)。该列表记录每个变更的提交日志条目，以及任何可能副作用的相关信息。

   要加入这些列表，请访问 [FreeBSD 列表服务器](https://lists.freebsd.org/)，点击要订阅的列表并按照说明进行操作。如果要跟踪整个源代码树的变更，订阅 [所有分支的源代码仓库提交信息列表](https://lists.freebsd.org/subscription/dev-commits-src-all)。
2. 安装新的 FreeBSD-STABLE 系统，可以从 FreeBSD 镜像站安装最新的 FreeBSD-STABLE 发布版本，或使用基于 FreeBSD-STABLE 的月度快照。
   如果要编译或升级现有的 FreeBSD 系统到 FreeBSD-STABLE，请使用 git 检出所需分支的源代码。分支名称（如 **stable/15**）在 <https://www.freebsd.org/releng> 上列出。
3. 在编译或升级到 FreeBSD-STABLE 之前，请仔细阅读 **/usr/src/Makefile** 和 [FreeBSD-STABLE 邮件列表](https://lists.freebsd.org/subscription/freebsd-stable) 和 **/usr/src/UPDATING** 以保持更新，了解有时在向下一个发布版本过渡过程中所需的其他启动过程。

## 课后习题

1. 分析 FreeBSD 的版本变更历史。
