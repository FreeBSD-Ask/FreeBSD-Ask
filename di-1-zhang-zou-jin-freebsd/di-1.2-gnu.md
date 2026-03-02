

## GNU 操作系统和自由软件运动

根据 Linux 内核文档 [1.5. Licensing](https://www.kernel.org/doc/html/latest/process/1.Intro.html)（另见 [Linux kernel licensing rules](https://www.kernel.org/doc/html/latest/process/license-rules.html)）：

>Code is contributed to the Linux kernel under a number of licenses, but all code must be compatible with version 2 of the GNU General Public License (GPLv2), which is the license covering the kernel distribution as a whole. In practice, that means that all code contributions are covered either by GPLv2 (with, optionally, language allowing distribution under later versions of the GPL) or the three-clause BSD license. Any contributions which are not covered by a compatible license will not be accepted into the kernel.（Linux 内核中的代码是在多种许可证之下被贡献的，但所有代码都必须与 GNU 通用公共许可证第 2 版（GPLv2）兼容，而该许可证覆盖了所有内核发行文件。实际上，这意味着所有对代码的贡献要么受 GPLv2 约束（可选地包含允许在 GPL 后续版本下发布的条款），要么受三条款 BSD 许可证约束。任何未被兼容许可证覆盖的贡献都不会被接纳进内核。）

我们有必要了解一下 GPL 背后的故事。

---

由于 Unix 在后期愈发封闭，许可证昂贵、受限制于商业公司等原因，RMS（Richard Matthew Stallman）就想创造一款自由且兼容 Unix 的操作系统。

- 1983 年，RMS 发表 [《GNU 宣言》](https://www.gnu.org/gnu/manifesto.html) [备份](https://web.archive.org/web/20260115033223/https://www.gnu.org/gnu/manifesto.html) ，其中 GNU 即 GNU is Not Unix（GNU 不是 Unix）。GNU 是一款操作系统——旨在完全替代 Unix。
- 1984 年，创建 [GNU 项目](https://www.gnu.org/) [备份](https://web.archive.org/web/20260115033101/https://www.gnu.org/)
- 1985 年，RMS 创建自由软件基金会（Free Software Foundation，FSF）
- 1989 年，FSF 发布 GPLv1
- 1991 年，FSF 发布 GPLv2
- 2007 年，FSF 发布 GPLv3

一开始，RMS 为 Unix 编写了许多实用程序（用户空间），然而 GNU 的目标操作系统始终缺乏稳定内核（即使到 2025 年，[GNU Hurd](https://hurd.gnu.org/) [备份](https://web.archive.org/web/20260116222211/https://www.gnu.org/software/hurd/)  仍未完成）。Linux 内核的诞生打破了这一困境。

作为由 Linux 内核和 GNU 软件组合而成的操作系统，Linux 不断地 GNU 化，形成了 GNU/Linux，其中 GNU 的贡献不可忽视，但很多人常忽略这一事实。这是因为：Linux 内核的开发由 Linus Torvalds 主导。Linus 本人对 FSF 和 RMS 的理念并不完全认同。因此，Linux 内核项目的理念与自由软件运动，甚至与严格的开源理念之间，存在一定的张力（例如，Linux 内核包含了不符合自由软件定义或严格开源定义的二进制固件模块，参见 [Linux-libre](https://www.fsfla.org/ikiwiki/selibre/linux-libre/) [备份](https://web.archive.org/web/20260115033255/https://www.fsfla.org/ikiwiki/selibre/linux-libre/) ）。并且 Linux 内核使用 GPLv2，而非 GNU 推荐的 GPLv3。事实是，Linus Torvalds 随意移除 Linux 项目的参与者，却未同时移除他们贡献的代码。——这无论同自由还是开源理念都是冲突的。

我们将 Linux 之前这段时间称作“自由软件运动”（代表人物 RMS）。Linux 的流行促成了另一种理念的兴起，即“开源运动”——代表人物有 Eric S. Raymond，OSI（Open Source Initiative，开放源代码促进会）的创始人，《UNIX 编程艺术》、《大教堂与集市》的作者；Bruce Perens，Debian 项目前领导人——想想下面有关开源的定义为什么是自 [Debian 的开源定义 DFSG](https://www.debian.org/social_contract#guidelines) [备份](https://web.archive.org/web/20260114070814/https://www.debian.org/social_contract#guidelines) 衍生而来？

自由软件运动并未停止，但人们对开源的误解却越来越重。

## 自由软件运动与开源运动之间的张力

需要注意的是，根据笔者与 RMS 的通讯，其强调的 GNU 与自由软件运动并不强调“开源”（甚至是反对开源），而是强调“Free”式自由。有些人可能认为现在的“开源”仅仅是由 [OSI 定义](https://opensource.org/osd)  的那样，这是一种极其片面的观点。

>致所有阅读我邮件的 NSA（美国国家安全局）和 FBI 特工：请考虑一下，捍卫美国宪法以抵御一切敌人，无论是外国的还是本国的，是否需要你效仿斯诺登的做法。
>
>>但是我有点困惑：GNU 项目是否强制要求开发必须开源？因为 GNU 通用公共许可证（GPL）强制开源。
>
>GNU 项目并不倡导“开源”。我们从不用这个词，除非是为了表达与它的分歧。我们代表的是自由软件（Free Software）——自由如同自由的言论。我们致力于在计算中为用户争取自由。
>
>请参见：<https://gnu.org/philosophy/free-software-even-more-important.html>
>
>“开源”这个词是一些反对自由软件运动的人发明的——他们与我们意见相左。他们想谈论同样的软件，却又掩盖自由的理念。
>
>关于自由软件与开源的区别，请参见：<https://gnu.org/philosophy/open-source-misses-the-point.html>
>
>另请阅读 Evgeny Morozov 的文章：<https://thebaffler.com/salvos/the-meme-hustler>，他在文中也探讨了这一点。
>
>所以请不要问我们关于“开源”或“开放”某些东西的问题。我们不是那样思考的。你真正应该问我们的是：我们如何以自由软件的方式做事情。
>
>>它属于 GNU 项目，那么 GNU 项目是否也会强制他人……
>
>我不太确定你所说的“强制”是什么意思，这里可能存在误解。通常我们会告诉人们我们认为什么是对的，什么是错的，但我们无法命令他们做什么。
>
>唯一的例外是他们使用了 GPL 许可的软件代码。在这种情况下，GNU GPL 本身是一种法律上的约束，规定了他们如何使用这些代码。它要求他们在再发布代码时，尊重其他用户的自由。
>
>这正是 copyleft（著佐权）的意义所在。
>
>如果你还有更多问题，请写信至 licensing@gnu.org。

此为私人通信引用，不涉及隐私话题。

## 附录：自由软件与开源软件语境下的典型误解与思想偏差探析

我们必须先给自由软件和开源协议分别下个定义，我们引用 [GNU 网站](https://www.gnu.org/philosophy/free-sw.zh-cn.html) [备份](https://web.archive.org/web/20260121155047/https://www.gnu.org/philosophy/free-sw.zh-cn.html)  的相关内容来定义什么是自由软件的自由。

### 厘清“营利”和“盈利”

这两个词语的含义不同，用法也不同。

- “盈利”：名词，扣除成本后获得的利润，也作赢利。《现代汉语词典》（ISBN：9787100124508，中国社会科学院语言研究所词典编辑室编，商务印书馆，第 7 版，第 1572 页）
- “营利”：动词，谋求利润。《现代汉语词典》（ISBN：9787100124508，中国社会科学院语言研究所词典编辑室编，商务印书馆，第 7 版，第 1572 页）

### 自由软件定义：四项基本自由

>如果一款软件是自由软件，那么它必须为用户提供以下四项基本自由：
>
>自由度 0：无论用户出于何种目的，必须可以按照用户意愿，自由地运行该软件。
>
>自由度 1：用户可以自由地学习并修改该软件，以此来帮助用户完成用户自己的计算。作为前提，用户必须可以访问到该软件的源代码。
>
>自由度 2：用户可以自由地分发该软件的拷贝，这样就可以助人。
>
>自由度 3：用户可以自由地分发该软件修改后的拷贝。借此，用户可以将改进后的软件分享给整个社区令他人也从中受益。作为前提，用户必须可以访问到该软件的源代码。

即：“用户可以自由地运行、拷贝、分发、学习、修改并改进该软件。”

推论 1：如果商业用户为了营利（自由度 0）而修改（自由度 1）再分发（自由度 2），只要修改后仍然开源（自由度 3），商业用户的行为是完全合规的，并说明他们完全有权自由使用、修改、分发及通过该软件营利。任何自由度均未限制 **营利** 行为。引证 1：[自由软件可以是商业软件](https://www.gnu.org/philosophy/free-sw.zh-cn.html#four-freedoms) [备份](https://web.archive.org/web/20260115033837/https://www.gnu.org/philosophy/free-sw.zh-cn.html#four-freedoms) ；

### 开源协议定义与开源软件定义

为了坚持开源定义 (OSD)，并防范开源运动原则的滥用而成立的开源促进会（OSI）对开源协议是这么定义的（基于 [Debian Free Software Guidelines](https://www.debian.org/social_contract#guidelines) [备份](https://web.archive.org/web/20260114070814/https://www.debian.org/social_contract#guidelines), DFSG），为了避免歧义，我们 [全文引用](https://opensource.org/osd)  如下：

>导言
>
>开源不仅仅意味着可以访问源代码。开源软件的分发条款必须符合以下标准
>
>1. 自由再分发
>
>许可证不得限制任何一方出售或赠送该软件，作为包含来自多个不同来源的程序的聚合软件分发包的组件。许可证不得要求对此类销售收取版税或其他费用。
>
>2. 源代码
>
>程序必须包含源代码，并且必须允许以源代码以及编译形式分发。如果某种形式的产品未与源代码一起分发，则必须有公开的方式来获取源代码，费用不得超过合理的复制成本，最好是通过互联网免费下载。源代码必须是程序员修改程序时的首选形式。故意混淆的源代码是不允许的。中间形式，例如预处理器或翻译器的输出，是不允许的。
>
>3. 衍生作品
>
>许可证必须允许修改和衍生作品，并且必须允许它们按照与原始软件许可证相同的条款进行分发。
>
>4. 作者源代码的完整性
>
>许可证可以限制以修改形式分发源代码，仅当许可证允许分发带有源代码的“补丁文件”，以便在构建时修改程序。许可证必须明确允许分发从修改后的源代码构建的软件。许可证可以要求衍生作品使用与原始软件不同的名称或版本号。
>
>5. 不得歧视个人或群体
>
>许可证不得歧视任何个人或群体。
>
>6. 不得歧视应用领域
>
>许可证不得限制任何人在特定应用领域中使用该程序。例如，它不得限制该程序在商业中使用，或用于基因研究。
>
>7. 许可证的分发
>
>附加到程序的权利必须适用于所有重新分发程序的人，而无需这些方执行额外的许可证。
>
>8. 许可证不得特定于产品
>
>附加到程序的权利不得取决于程序是否为特定软件分发包的一部分。如果程序从该分发包中提取出来，并在程序许可证的条款范围内使用或分发，则所有重新分发程序的一方都应享有与原始软件分发包授予的权利相同的权利。
>
>9. 许可证不得限制其他软件
>
>许可证不得对与许可软件一起分发的其他软件施加限制。例如，许可证不得坚持要求在同一介质上分发的所有其他程序都必须是开源软件。
>
>10. 许可证必须保持技术中立
>
>许可证的任何条款都不得基于任何个人技术或界面风格。

OSI（Open Source Initiative，开源促进会）基于开放软件定义（OSD）的开放认证许可证，已成为全球公认的开放软件判定标准，并通过国际组织、产业界与政府政策的采纳而确立其权威性。参见 [International Authority & Recognition](https://opensource.org/about/authority) 。

受 OSI 认可的开源协议有：[OSI Approved Licenses](https://opensource.org/licenses) ，严格意义上讲，只有列表中的许可证才属于开源许可证。

### 关于各种软件的定义

根据 [自由与非自由软件的分类](https://www.gnu.org/philosophy/categories.zh-cn.html) [备份](https://web.archive.org/web/20260117035802/https://www.gnu.org/philosophy/categories.zh-cn.html) ，我们定义如下：

- 自由软件：符合上述四项基本自由定义的软件即称为自由软件。推论：商业软件可以是自由软件，商业 ≠ 非自由。引证 1：[自由软件可以是商业软件](https://www.gnu.org/philosophy/free-sw.zh-cn.html#four-freedoms) [备份](https://web.archive.org/web/20260115033837/https://www.gnu.org/philosophy/free-sw.zh-cn.html#four-freedoms) ；引证 2：[Words to Avoid (or Use with Care) Because They Are Loaded or Confusing](https://www.gnu.org/philosophy/words-to-avoid.html) [备份](https://web.archive.org/web/20260120174001/https://www.gnu.org/philosophy/words-to-avoid.html) ,“Commercial”部分
- 开源软件：使用上述开源协议授权的软件。所有自由软件都是开源软件，但是所有开源软件不一定是自由软件。二者的定义和理念都有一定的差异。自由软件是开源软件的充分不必要条件
- 专有软件/私有软件（proprietary software）：即真正意义上的“非自由软件”，大部分商业软件属此类型。这是 GNU 宣言一开始真正的目标
- 免费软件：定义模糊。其他类别的软件均可能是“免费”的，但并不一定
- 商业软件：商业软件是由企业作为其业务的一部分所开发的软件

#### 推论

- 推论 1：商业软件可以是开源软件/自由软件。反之，开源软件/自由软件也同样可以是商业软件。
- 推论 2：商业软件形式的开源软件/自由软件可以营利（无论项目作者是不是参与此商业软件），且合规。比如我们常见的行为是淘宝商户拿开源许可的软件营利，遭到原作者的不忿。其实这种行为是合规的，只要其标注了原作者并愿意分发相应的源码（如许可证要求）。现实中对此类商家的指责，多源于公众对所采用的开源协议缺乏理解——不少人甚至未通读协议（含中文译本），从而产生误解。在遵守许可的前提下，此类营利可是合乎伦理的，尽管若只是简单搬运可能惹人不快；
- 推论 3：商业软件不一定是私有软件或专有软件。反之，私有软件或专有软件也不一定是商业软件（如将你的个人项目无营利目的地闭源分发给你的几位朋友）。

### 自由/开源软件与免费

根据“自由度 2：用户可以自由地分发该软件的拷贝”，事实上只要阅读过 GPL 2/3 等相关开源协议，就会知道协议并未限制开源软件的营利行为。从现实出发的红帽公司就是一个典型例子。

开源软件/自由软件 ≠ 免费。

### 开源 ≠ 无版权？协议不可撤销？

很多人会混淆开源与无版权，认为开源=无版权。这种想法在实际中存在逻辑问题：如果你不持有版权，凭什么要求他人遵守你的开源协议？（部分人会将版权转给 GNU 协会，但仍在事实上存在版权）

在司法实践中也存在矛盾，许多开源软件项目作者仍然被追究了法律责任，如果是无版权，那么应该追究谁的责任？

在各国版权法中，版权不可转让所有权利，只能让渡部分权利。让渡全部权利（包括人身权）既荒谬又存在逻辑问题。以《中华人民共和国著作权法》为例，只有“第（五）项至第（十七）项”是可以让渡的，发表权、署名权、修改权、保护作品完整权都是无法让渡的。

在实例中，作者永远不会受到开源协议本身的限制（除非他也引用了别人的项目），那是用来限制他人的，即使协议声称不可撤销，在司法实践中通常无效，并已有相关判例。

### CC-BY-NC（所有版本）、CC-BY-ND（所有版本）既不自由也不开源

根据 [各类许可证及其评论](https://www.gnu.org/philosophy/categories.zh-cn.html) [备份](https://web.archive.org/web/20260117035802/https://www.gnu.org/philosophy/categories.zh-cn.html) ，结合 [OSI Approved Licenses](https://opensource.org/licenses) ，CC-BY-NC（所有版本）、CC-BY-ND（所有版本）等均不属于开源软件许可证或自由软件许可证，因此在该许可证授权下的项目既非传统意义上的自由软件亦非开源软件。

原因很简单，上述协议都歧视商业用户，剥夺了商业用户的“自由”。

此外，前项 CC 协议也不符合自由软件精神，即要求冗长的署名与声明，这种广告条款增加了项目复用时的合规成本。

笔者注意到，不少项目虽然采用了前项 CC 协议进行授权，却依然自诩支持开源软件，拥护自由软件运动，甚至标榜自己是忠实拥趸。这一现象表明，尽管“自由软件”和“开源软件”的名号已广为人知，但其背后的理念却未必真正得到了理解与践行。

### 可以获取源代码 ≠ 开源 ≠ 自由

根据微软的 Enterprise Source Licensing Program: ESLP 协议（或者 Microsoft Reference Source License, Ms-RSL），商业用户只要购买了一定量的产品副本（并不要求多么离谱的数量或额度），即可获取其对应的源代码。

你可以获取源代码，并且微软的限制条件仍然在表面上看似符合“自由度 1”（自由修改参见 [神州网信](https://www.cmgos.com/) [备份](https://web.archive.org/web/20260115132700/https://www.cmgos.com/web/home/)  的 Windows 10 神州网信政府版）。

但是你很难说这种协议是一种开源协议，在某种意义上 CC-BY-NC（所有版本）、CC-BY-ND（所有版本）其实和这种许可协议没有什么本质区别。
