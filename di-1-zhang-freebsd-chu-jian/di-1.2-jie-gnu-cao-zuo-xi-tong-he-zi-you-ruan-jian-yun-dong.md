# 1.2 GNU 操作系统和自由软件运动

GNU 项目由理查德·斯托曼于 1983 年发起，目标是创建一款完全自由的、与 UNIX 兼容的操作系统。本节梳理从 GNU 项目初始公告、自由软件基金会成立到 GPL 许可证体系建立的关键节点，并说明 GNU 用户空间与 Linux 内核如何结合为 GNU/Linux。

## GNU 操作系统与自由软件运动的缘起

GNU 项目与自由软件运动的渊源，可从 Linux 内核文档切入理解。根据 Linux Kernel Documentation 的相关说明（参见 Linux Kernel Documentation. 1. Introduction — The Linux Kernel documentation[EB/OL]. [2026-03-26]. <https://www.kernel.org/doc/html/latest/process/1.Intro.html> 及 Linux Kernel Documentation. Linux kernel licensing rules — The Linux Kernel documentation[EB/OL]. [2026-03-26]. <https://www.kernel.org/doc/html/latest/process/license-rules.html>）：

> Code is contributed to the Linux kernel under a number of licenses, but all code must be compatible with version 2 of the GNU General Public License (GPLv2), which is the license covering the kernel distribution as a whole. In practice, that means that all code contributions are covered either by GPLv2 (with, optionally, language allowing distribution under later versions of the GPL) or the three-clause BSD license. Any contributions which are not covered by a compatible license will not be accepted into the kernel.（Linux 内核中贡献的代码是由多种许可证授权的，但所有代码都必须与 GNU 通用公共许可证第 2 版（GPLv2）兼容，因为 GPLv2 捆绑了所有内核发行文件。实际上这意味着，一切贡献的代码要么受 GPLv2 约束（可选地包含允许在 GPL 后续版本下发布的条款），要么受三条款 BSD 许可证约束。那些由非兼容许可证授权的贡献都不会被内核接纳）

UNIX 在后期发展中逐渐呈现封闭化趋势，从最初开放的研究项目（受当时美国法律要求）转变为商业产品。普通用户无法自由获取和修改其源代码，许可证价格高昂且使用权受到商业公司严格限制。理查德·马修·斯托曼（Richard Matthew Stallman，RMS）希望创造一款自由且与 UNIX 兼容的操作系统，这一愿景直接推动了自由软件运动的兴起。

- 1983 年，理查德·马修·斯托曼发表了 GNU 项目初始公告；其中 GNU 即“GNU's Not Unix”（GNU 不是 UNIX）的递归缩写。GNU 是一款旨在完全替代 UNIX 的操作系统。
- 1984 年，理查德·马修·斯托曼正式创建了 [GNU 项目](https://www.gnu.org/)。
- 1985 年，理查德·马修·斯托曼撰写了 GNU 宣言（Stallman R. The GNU Manifesto[EB/OL]. [2026-03-26]. <https://www.gnu.org/gnu/manifesto.html>）；同年创建了自由软件基金会（Free Software Foundation，FSF）。
- 1989 年，自由软件基金会发布了 GNU General Public License V1.0 (GPLv1, GNU 通用公共许可证第 1 版)。
- 1991 年，理查德·马修·斯托曼发布了 GNU General Public License V2.0 (GPLv2, GNU 通用公共许可证第 2 版)。
- 2007 年，自由软件基金会发布 GNU General Public License V3.0 (GPLv3, GNU 通用公共许可证第 3 版)。

在 GNU 项目初期，理查德·马修·斯托曼为 UNIX 开发了大量实用程序（用户空间组件），然而 GNU 的目标操作系统始终未能形成稳定的内核。[**GNU Hurd**](https://hurd.gnu.org/) 是 GNU 项目的内核，采用微内核架构设计，其开发始于 1990 年。尽管 GNU Hurd 已于 2025 年随 Debian GNU/Hurd 发布，但其硬件支持和软件生态仍远未达到生产就绪水平。Linux 内核的诞生打破了这一技术僵局。

Linux 由 Linux 内核与 GNU 软件组合而成，在发展过程中不断融入 GNU 理念，最终形成 GNU/Linux 操作系统。尽管 GNU 的贡献巨大，其作用却常被低估。这一现象的部分原因在于 Linux 内核的开发由林纳斯·托瓦兹（Linus Torvalds）主导，而托瓦兹对自由软件基金会及理查德·马修·斯托曼的理念并不完全认同。Linux 内核项目与自由软件运动乃至严格的开源理念之间，存在一定的分歧（例如，Linux 内核包含了一些不符合自由软件或严格开源定义的二进制固件模块，参见 **Linux-libre**，一款由拉丁美洲自由软件基金会（FSFLA）维护的去除所有二进制固件的 Linux 内核变体 Linux-libre[EB/OL]. [2026-03-26]. <https://www.fsfla.org/ikiwiki/selibre/linux-libre/>.）此外，Linux 内核采用的是 GPLv2 许可证，而非 GNU 所推荐的 GPLv3。

在 Linux 诞生之前，软件自由领域的代表性运动是"自由软件运动"（代表人物为理查德·马修·斯托曼）。Linux 的流行促成了另一种理念的兴起，即"开源运动"，代表人物包括开放源代码促进会（Open Source Initiative，OSI）的创始人、《UNIX 编程艺术》与《大教堂与集市》的作者埃里克·斯蒂芬·雷蒙德（Eric S. Raymond），以及 Debian 项目前领导人布鲁斯·佩伦斯（Bruce Perens）。OSI 所定义的开源标准源于 Debian 自由软件指导方针（Debian Free Software Guidelines，DFSG）。

自由软件运动与开源运动之间的理念分歧，至今仍是软件许可领域的重要议题。

## 自由软件运动与开源运动的张力

自由软件运动与开源运动之间存在一定的理念差异。理查德·马修·斯托曼在私人通信中强调，GNU 与自由软件运动并不强调“开源”（甚至是反对使用这一术语），而是强调“Free”所代表的自由。部分观点认为“开源”仅仅是 OSI 所定义（Open Source Initiative. The Open Source Definition[EB/OL]. (2024-02-16)[2026-03-26]. <https://opensource.org/osd>.）的那样，这是一种片面的观点。

以下引用自理查德·马修·斯托曼的私人通信，内容不涉及隐私信息。

> 致所有阅读我邮件的美国国家安全局（National Security Agency，NSA）和联邦调查局（Federal Bureau of Investigation，FBI）特工：请考虑一下，捍卫美国宪法以抵御一切敌人，无论是外国的还是本国的，是否需要你效仿爱德华·斯诺登（Edward Snowden）的做法。
>
>> 但是我有点困惑：GNU 项目是否强制要求开发必须开源？因为 GNU 通用公共许可证（GPL）强制开源。
>
> GNU 项目并不倡导“开源”。我们从不用这个词，除非是为了表达与它的分歧。我们代表的是自由软件（Free Software）——自由如同自由的言论。我们致力于在计算中为用户争取自由。
>
> 请参见：free-software-even-more-important[EB/OL]. [2026-03-26]. <https://gnu.org/philosophy/free-software-even-more-important.html>.
>
> “开源”这个词是一些反对自由软件运动的人发明的——他们与我们意见相左。他们想谈论同样的软件，却又掩盖自由的理念。
>
> 关于自由软件与开源的区别，请参见：open-source-misses-the-point[EB/OL]. [2026-03-26]. <https://gnu.org/philosophy/open-source-misses-the-point.html>.
>
> 另请阅读叶夫根尼·莫罗佐夫（Evgeny Morozov）的文章：<https://thebaffler.com/salvos/the-meme-hustler>，他在文中也探讨了这一点。
>
> 所以请不要问我们关于“开源”或“开放”某些东西的问题。我们不是那样思考的。你真正应该问我们的是：我们如何以自由软件的方式做事情。
>
>> 它属于 GNU 项目，那么 GNU 项目是否也会强制他人……
>
> 我不太确定你所说的“强制”是什么意思，这里可能存在误解。通常我们会告诉人们我们认为什么是对的，什么是错的，但我们无法命令他们做什么。
>
> 唯一的例外是他们使用了 GPL 许可的软件代码。在这种情况下，GNU GPL 本身是一种法律上的约束，规定了他们如何使用这些代码。它要求他们在再发布代码时，尊重其他用户的自由。
>
> 这正是著佐权（Copyleft）的意义所在。
>
> 如果你还有更多问题，请写信至 <licensing@gnu.org>。

> **技巧**
>
>与 GPL 许可证的“著佐权”（Copyleft）机制不同，FreeBSD 项目采用 BSD 许可证，这是一种更为宽松的许可证模式。FreeBSD 项目的源代码中包含部分受 GNU 通用公共许可证（GPL）和 GNU 宽通用公共许可证（LGPL）授权的软件，这些许可证附带更多限制条件，尽管至少在强制开放获取方面如此。然而，由于 GPL 软件在商业使用中可能产生额外的复杂性，在合理可行的情况下，FreeBSD 项目更倾向于接受采用限制更少的 BSD 许可证的软件提交。这一许可证选择的差异，构成了 FreeBSD 与 Linux 在软件生态治理上的根本分歧。

## 参考文献

- Debian Project. Debian GNU/Hurd[EB/OL]. [2026-04-17]. <https://www.debian.org/ports/hurd/>. Debian GNU/Hurd 官方页面，2025 年随 Debian Trixie 发布了正式版本。
- GNU Project. What is the Hurd?[EB/OL]. [2026-04-17]. <https://www.gnu.org/software/hurd/hurd/what_is_the_gnu_hurd.html>. GNU Hurd 项目介绍，阐述其微内核架构设计理念。

## 课后习题

1. 查阅 GNU Hurd 项目的源代码与构建指南，在 QEMU 中启动一个基本的 GNU Hurd 系统，记录其微内核架构与传统宏内核在启动流程上的差异。
2. 阅读 GNU 通用公共许可证第二版（GPLv2）原文，归纳其 copyleft 机制的核心条款，并与 BSD 2 条款许可证在再分发限制方面进行逐条对比。
3. 统计 FreeBSD 基本系统中 BSD 许可证与 GPL 许可证组件的数量及占比。
