# 1.2 GNU 操作系统和自由软件运动

GNU 项目于 1983 年由理查德·斯托曼发起，目标是创建一款完全自由的、与 UNIX 兼容的操作系统。

## GNU 操作系统与自由软件运动的缘起

GNU 项目与自由软件运动的渊源，可从 Linux 内核文档入手理解。根据 Linux Kernel Documentation 的相关说明（参见 Linux Kernel Documentation. 1. Introduction — The Linux Kernel documentation[EB/OL]. [2026-03-26]. <https://www.kernel.org/doc/html/latest/process/1.Intro.html> 及 Linux Kernel Documentation. Linux kernel licensing rules — The Linux Kernel documentation[EB/OL]. [2026-03-26]. <https://www.kernel.org/doc/html/latest/process/license-rules.html>）：

> Code is contributed to the Linux kernel under a number of licenses, but all code must be compatible with version 2 of the GNU General Public License (GPLv2), which is the license covering the kernel distribution as a whole. In practice, that means that all code contributions are covered either by GPLv2 (with, optionally, language allowing distribution under later versions of the GPL) or the three-clause BSD license. Any contributions which are not covered by a compatible license will not be accepted into the kernel.（Linux 内核中贡献的代码是由多种许可证授权的，但所有代码都必须与 GNU 通用公共许可证第 2 版（GPLv2）兼容，因为 GPLv2 捆绑了所有内核发行文件。实际上这意味着，一切贡献的代码要么受 GPLv2 约束（可选地包含允许在 GPL 后续版本下发布的条款），要么受三条款 BSD 许可证约束。那些由非兼容许可证授权的贡献都不会被内核接纳）

UNIX 在后期发展中渐趋封闭，由最初开放的研究项目（受当时美国法律要求）转变为商业产品。普通用户无法自由获取和修改其源代码，许可证价格高昂，使用权受商业公司严格限制。理查德·马修·斯托曼（Richard Matthew Stallman，RMS）希望创造一款自由且与 UNIX 兼容的操作系统，这一愿景直接推动了自由软件运动的兴起。

- 1983 年，理查德·马修·斯托曼发表了 GNU 项目初始公告；其中 GNU 即“GNU's Not Unix”（GNU 不是 UNIX）的递归缩写。GNU 是一款旨在完全替代 UNIX 的操作系统。
- 1984 年，理查德·马修·斯托曼正式创建了 [GNU 项目](https://www.gnu.org/)。
- 1985 年，理查德·马修·斯托曼撰写了 GNU 宣言（Stallman R. The GNU Manifesto[EB/OL]. [2026-03-26]. <https://www.gnu.org/gnu/manifesto.html>）；同年创建了自由软件基金会（Free Software Foundation，FSF）。
- 1989 年，自由软件基金会发布了 GNU General Public License V1.0 (GPLv1, GNU 通用公共许可证第 1 版)。
- 1991 年，理查德·马修·斯托曼发布了 GNU General Public License V2.0 (GPLv2, GNU 通用公共许可证第 2 版)。
- 2007 年，自由软件基金会发布 GNU General Public License V3.0 (GPLv3, GNU 通用公共许可证第 3 版)。

在 GNU 项目初期，理查德·马修·斯托曼为 UNIX 开发了大量实用程序（用户空间组件），然而 GNU 始终未能产出稳定的内核。[**GNU Hurd**](https://hurd.gnu.org/) 是 GNU 项目的内核，采用微内核架构设计，其开发始于 1990 年。尽管 GNU Hurd 已于 2025 年随 Debian GNU/Hurd 发布，但其硬件支持和软件生态仍不成熟。Linux 内核的诞生打破了这一技术僵局。

Linux 由 Linux 内核与 GNU 软件组合而成，在发展过程中不断融入 GNU 理念，最终形成 GNU/Linux 操作系统。尽管 GNU 的贡献巨大，其作用却常被低估。这一现象的部分原因在于 Linux 内核的开发由林纳斯·托瓦兹（Linus Torvalds）主导，而托瓦兹对自由软件基金会及理查德·马修·斯托曼的理念并不完全认同。Linux 内核项目与自由软件运动乃至严格的开源理念之间，存在一定的分歧（例如，Linux 内核包含了一些不符合自由软件或严格开源定义的二进制固件模块，参见 **Linux-libre**，一款由拉丁美洲自由软件基金会（FSFLA）维护的去除所有二进制固件的 Linux 内核变体 Linux-libre[EB/OL]. [2026-03-26]. <https://www.fsfla.org/ikiwiki/selibre/linux-libre/>.）此外，Linux 内核采用的是 GPLv2 许可证，而非 GNU 所推荐的 GPLv3。

在 Linux 诞生之前，软件自由领域的代表性运动是“自由软件运动”（代表人物为理查德·马修·斯托曼）。Linux 的流行促成了另一种理念的兴起，即“开源运动”，代表人物包括开放源代码促进会（Open Source Initiative，OSI）的创始人、《UNIX 编程艺术》与《大教堂与集市》的作者埃里克·斯蒂芬·雷蒙德（Eric S. Raymond），以及 Debian 项目前领导人布鲁斯·佩伦斯（Bruce Perens）。OSI 所定义的开源标准源于 Debian 自由软件指导方针（Debian Free Software Guidelines，DFSG）。

自由软件运动与开源运动之间的理念分歧，至今仍是软件许可领域的核心分歧之一。

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
>与 GPL 许可证的“著佐权”（Copyleft）机制不同，FreeBSD 项目采用 BSD 许可证，这是一种更为宽松的许可证模式。FreeBSD 项目的源代码中包含部分受 GNU 通用公共许可证（GPL）和 GNU 宽通用公共许可证（LGPL）授权的软件，这些许可证通过著佐权（Copyleft）条款对源代码的再发布附加了更严格的限制。然而，由于 GPL 软件在商业使用中可能带来额外复杂性，在合理可行的情况下，FreeBSD 项目更倾向于接受 BSD 许可证的软件提交。这一许可证选择的差异，是 FreeBSD 与 Linux 在软件生态治理上的核心区别。

### 参考文献

- Debian Project. Debian GNU/Hurd[EB/OL]. [2026-04-17]. <https://www.debian.org/ports/hurd/>. Debian GNU/Hurd 官方页面，2025 年随 Debian Trixie 发布了正式版本。
- GNU Project. What is the Hurd?[EB/OL]. [2026-04-17]. <https://www.gnu.org/software/hurd/hurd/what_is_the_gnu_hurd.html>. GNU Hurd 项目介绍，阐述其微内核架构设计理念。

## 附录：自由软件与开源软件的常见误解辨析

自由软件与开源软件的概念常被混淆。本附录从“营利”与“盈利”的词语辨析入手，梳理自由软件的四项基本自由与 OSI 开源协议十条标准，辨析自由软件与开源软件的关系，并厘清 CC-BY-NC/ND 等非开源许可证的边界。

### 厘清“营利”和“盈利”

这两个词语在含义和用法上均不相同。

- “盈利”：名词，扣除成本后获得的利润，也作赢利。引自中国社会科学院语言研究所词典编辑室，编. 现代汉语词典[M]. 第7版. 北京：商务印书馆，2016：1572. ISBN: 978-7-100-12450-8.
- “营利”：动词，谋求利润。引自中国社会科学院语言研究所词典编辑室，编. 现代汉语词典[M]. 第7版. 北京：商务印书馆，2016：1572. ISBN: 978-7-100-12450-8.

### 自由软件定义：四项基本自由

> 如果一款软件是自由软件，那么它必须为用户提供以下四项基本自由：
>
> 自由度 0：无论用户出于何种目的，必须可以按照用户意愿，自由地运行该软件。
>
> 自由度 1：用户可以自由地学习并修改该软件，以此来帮助用户完成用户自己的计算。作为前提，用户必须可以访问到该软件的源代码。
>
> 自由度 2：用户可以自由地分发该软件的拷贝，以便帮助他人。
>
> 自由度 3：用户可以自由地分发该软件修改后的拷贝。借此，用户可以将改进后的软件分享给整个社区，令他人也从中受益。作为前提，用户必须可以访问到该软件的源代码。

即：“用户可以自由地运行、复制、分发、学习、修改并改进该软件。”

推论 1：如果商业用户为了营利（自由度 0）而修改（自由度 1）再分发（自由度 2），只要修改后仍然开源（自由度 3），商业用户的行为是完全合规的。这表明商业用户完全有权自由使用、修改、分发及通过该软件营利。任何自由度均未限制 **营利** 行为。引证 1：[自由软件可以是商业软件](https://www.gnu.org/philosophy/free-sw.zh-cn.html#four-freedoms)。

### 开源协议定义与开源软件定义

开放源代码促进会（OSI）旨在坚持开源定义（Open Source Definition，OSD）并防范开源运动原则的滥用，其对开源协议的定义如下——开源软件的分发条款必须符合以下核心标准：

1. **自由再分发**：许可证不得限制任何一方出售或赠送该软件，不得要求对此类销售收取版税或其他费用。
2. **源代码**：程序必须包含源代码，并允许以源代码以及编译形式分发。
3. **衍生作品**：许可证必须允许修改和衍生作品，并允许按照与原始软件许可证相同的条款进行分发。
4. **作者源代码的完整性**：许可证可以限制以修改形式分发源代码，仅当允许分发带有源代码的“补丁文件”。
5. **不得歧视个人或群体**：许可证不得歧视任何个人或群体。
6. **不得歧视应用领域**：许可证不得限制任何人在特定应用领域中使用该程序。
7. **许可证的分发**：附加到程序的权利必须适用于所有重新分发程序的人。
8. **许可证不得特定于产品**：附加到程序的权利不得取决于程序是否为特定软件分发包的一部分。
9. **许可证不得限制其他软件**：许可证不得对与许可软件一起分发的其他软件施加限制。
10. **许可证必须保持技术中立**：许可证的任何条款都不得基于任何单一技术或界面风格。

OSI 基于开源定义（OSD）的开放认证许可证，已成为全球公认的开放软件判定标准，并因国际组织、产业界与政府政策的采纳而确立了权威性。

经 OSI 认证的开源许可证参见 [OSI 官方许可证列表](https://opensource.org/licenses)。严格意义上，仅该列表中的许可证属于开源许可证。

### 关于各种软件的定义

根据自由软件基金会. 自由与非自由软件的分类[EB/OL]. (2025-12-28)[2026-03-26]. <https://www.gnu.org/philosophy/categories.zh-cn.html>. 定义如下：

- 自由软件：符合上述四项基本自由定义的软件即称为自由软件。推论：商业软件可以是自由软件，商业不等于非自由。引证 1：自由软件基金会. 什么是自由软件？[EB/OL]. [2026-03-26]. <https://www.gnu.org/philosophy/free-sw.zh-cn.html>. 引证 2：Free Software Foundation. Words to Avoid (or Use with Care) Because They Are Loaded or Confusing[EB/OL]. [2026-03-26]. <https://www.gnu.org/philosophy/words-to-avoid.html>.“Commercial”部分。
- 开源软件：使用上述开源协议授权的软件。所有自由软件都是开源软件，但并非所有开源软件都是自由软件。二者的定义与理念均存在差异。自由软件是开源软件的充分不必要条件。
- 专有软件/私有软件（Proprietary Software）：即真正意义上的“非自由软件”，大部分商业软件属此类型。这是 GNU 宣言最初的目标。
- 免费软件：界定标准不一。前述各类软件均可能免费分发，但免费本身不构成其性质的判定依据。
- 商业软件：商业软件是由企业作为其业务的一部分所开发的软件。

#### 推论

- 推论 1：商业软件可以是开源软件或自由软件。反之，开源软件或自由软件也可以是商业软件。
- 推论 2：商业软件形式的开源软件或自由软件可以营利（无论项目作者是否参与此商业软件），且合规。例如，典型情形为电商平台商户利用开源许可的软件营利。在遵守许可的前提下，此类营利是合乎伦理的。现实中对此类商家的指责，多源于公众对所采用的开源协议缺乏理解。
- 推论 3：商业软件不一定是私有软件或专有软件。反之，私有软件或专有软件也不一定是商业软件（如将个人项目无营利目的地闭源分发给朋友）。

### 自由/开源软件与免费

依据“自由度 2：用户可以自由地分发该软件的拷贝”及 GPLv2/v3 等相关开源协议的条款，上述协议并未限制开源软件的营利行为。红帽公司（Red Hat）就是一个典型的例子。

开源软件/自由软件不等于免费。

### 开源不等于无版权

部分公众会混淆开源与无版权，认为开源即无版权。该观点在实际中存在逻辑问题：如果不持有版权，便无法要求他人遵守开源协议。部分人会将版权转交给自由软件基金会，但版权在事实上依然存在。

在司法实践中，许多开源软件项目作者仍被依法追究法律责任。如果是无版权，则无法确定责任主体。

在各国版权法中，版权的所有权利通常不可完全转让，只能让渡部分权利。以《中华人民共和国著作权法》为例，发表权、署名权、修改权、保护作品完整权等权利是无法让渡的。

在实践中，作者通常不受开源协议本身的限制（除非引用了他人的项目），协议旨在约束第三方。

### CC-BY-NC 与 CC-BY-ND 既不自由也不开源

根据各类许可证及其评论，知识共享署名-非商业性使用协议（Creative Commons Attribution-NonCommercial，CC-BY-NC）与知识共享署名-禁止演绎协议（Creative Commons Attribution-NoDerivs，CC-BY-ND）等均不属于开源软件许可证或自由软件许可证。

原因在于，上述协议限制了商业用户的使用，剥夺了商业用户的“自由”。前述 CC 协议也不符合自由软件精神，其要求的冗长署名与声明增加了项目复用时的合规成本。

### 可以获取源代码不等于开源或自由

根据微软（Microsoft）的企业源代码许可计划（Enterprise Source Licensing Program，ESLP）或微软参考源代码许可证（Microsoft Reference Source License，Ms-RSL），商业用户在满足一定条件后即可获取对应的源代码。

虽然可以获取源代码，且在某些情况下允许修改（如神州网信政府版 Windows 10），但此类协议并不属于开源协议。本质上，CC-BY-NC 与 CC-BY-ND 与此类许可协议并无根本区别。

### 参考文献

- 自由软件基金会. 自由与非自由软件的分类[EB/OL]. [2026-03-26]. <https://www.gnu.org/philosophy/categories.zh-cn.html>.
- Open Source Initiative. Licenses - Open Source Initiative[EB/OL]. [2026-03-26]. <https://opensource.org/licenses>.
- Open Source Initiative. International Authority & Recognition - Open Source Initiative[EB/OL]. (2025-06-03)[2026-03-26]. <https://opensource.org/about/authority>.
- 基于 Debian. Debian Social Contract[EB/OL]. (2022-10-01)[2026-03-26]. <https://www.debian.org/social_contract#guidelines>. DFSG。
- 自由软件基金会. 什么是自由软件？[EB/OL]. [2026-03-26]. <https://www.gnu.org/philosophy/free-sw.zh-cn.html>. 引用自由软件基金会相关内容来定义自由软件的自由。

## 课后习题

1. 查阅理论文献，分析 Linux 发行版（Debian、Ubuntu、Fedora、Arch Linux 等）与 GNU 项目及 GNU GPL 许可证之间的技术、法律与社区关系，绘制三者互动关系图。
2. 选定一个 Linux 发行版，研究其系统核心组件与 GNU 项目之间的依赖关系。该发行版中哪些关键组件来自 GNU 项目？其内核（Linux 内核）与 GNU 工具链如何协同工作？查阅相关技术文档和架构资料，撰写技术分析报告。
3. 阅读 GNU GPLv2 许可证原文，归纳 copyleft 机制的核心条款，与 BSD 2 条款许可证在再分发限制方面逐条对比。
