# 2.4 FreeBSD 简史

- 1961 年分时操作系统（Timesharing OS）

在 20 世纪 60 年代初，分时操作系统诞生。1961 年 11 月，麻省理工学院的 Fernando Corbató 在 IBM 709 上首次演示了兼容分时系统（CTSS），即最早的分时系统之一。同期，曼彻斯特大学设计的 Atlas 计算机上也实现了 Atlas 监控程序，该系统于 1962 年 12 月 7 日正式投入运行，首次将虚拟存储器投入实际使用——虚拟存储器的概念则由德国物理学家 Fritz-Rudolf Güntsch 于 1956 年在其博士论文中率先提出（参见：Denning P J. Virtual Memory[J]. ACM Computing Surveys, 1970, 2(3): 153-189）。在那个时代，分时共享系统意味着两个人共用同一台计算机，通常需要安排一张小时时间表来规划使用计算机的时间。

- 1964 年 MULTICS（**多路复用** 信息和计算服务）

Multics 最初的规划与开发始于 1964 年，地点位于马萨诸塞州的剑桥市。最初，Multics 是由麻省理工学院（Fernando Corbató 领导的 MAC 项目）主导的项目；1964 年 8 月，通用电气公司签约成为硬件供应商；同年 11 月，贝尔实验室加入，形成三方合作。Multics 在专为操作系统设计的通用电气 645 计算机上开发；GE 645 原型机于 1967 年 1 月交付给麻省理工学院，Multics 于同年 12 月在该硬件上首次启动。

- 1969 年 UNIX（UNIX 操作系统）

在贝尔实验室退出 Multics 项目前，Dennis Ritchie 和 Ken Thompson 已经意识到了 Multics 的潜力。1969 年，Ken Thompson 在一台闲置的 PDP-7 计算机上着手开发一款名为 Unics（Uniplexed Information and Computing Service，**单路复用** 信息和计算服务）的新程序。随后在 1970 年夏，他们以开发文字处理系统的名义从贝尔实验室法务部门获得资金，购买了一台 PDP-11/20 计算机，将 Unics 移植到了这台性能更强的机器上。

- 1973 年 UNIX 代码迁移到 C 语言

Dennis Ritchie 决定为 UNIX 开发一种高级语言，使其语句能编译成少数几条机器指令。这促使他开发了 C 编程语言。1973 年夏天，第四版研究 UNIX（Research Unix V4）使用 C 语言重写了内核（Thompson 曾在 1972 年做过尝试但放弃了）。这令 UNIX 具备了可移植性，从而改写了操作系统的历史。

- 1974 年加州大学伯克利分校引入 UNIX

1974 年，加州大学伯克利分校的 Bob Fabry 教授从 AT&T 获得了 UNIX 的源代码许可证。Bob Fabry 此前在 1973 年的国际计算机学会（Association for Computing Machinery，ACM）操作系统原理研讨会上见过 UNIX 第 4 版，并有意引入加州大学伯克利分校。该校的计算机系统研究小组（CSRG）开始修改和改进 AT&T Research Unix，并将修改后的版本称为“BSD Unix”或“BSD”。

- 1978 年 3 月 9 日 1BSD 发布

基于 UNIX 创建的伯克利软件发行版（1BSD）是 UNIX 第六版的一种附加组件，而非独立完整的操作系统。此版本发行了大约 30 份。

- 1979 年 5 月 10 日 2BSD 发布

第二款伯克利软件发行版（2BSD）发布于 1979 年 5 月。涉及 1BSD 的软件更新，以及由 Bill Joy 新开发的两个至今仍在 UNIX 系统上使用的程序：vi 文本编辑器（ex 的可视化版本）和 Csh。2BSD 是 Bill Joy 参与 PDP-11 相关工作的最后一个 BSD 版本，发行了约 75 份。

- 1980 年 4 月 DARPA 的赞助

在 1980 年初，美国国防高级研究计划局（DARPA, Defense Advanced Research Projects Agency）正在寻找一种有助于军事项目的操作系统。基于 3BSD 的成功，Bob Fabry 于 1979 年秋向 DARPA 提交了提案，建议伯克利为 DARPA 社区开发 3BSD 的增强版本。1980 年 4 月，DARPA 与伯克利签订了为期 18 个月的合同，开始赞助伯克利进行相关工作。

- 1983 年 8 月 4.2BSD 发布

在 Bill Joy 离开伯克利并与他人创建 Sun Microsystems（太阳计算机系统公司）（1982 年）之后，4.2BSD 于 1983 年 8 月正式发布，这是 Bill Joy 离开后的第一个版本。1984 年，USENIX 为 4.2BSD 出版的《Unix System Manager's Manual》封面首次使用了由 John Lasseter 绘制的 BSD 吉祥物形象，这一形象后来成为 BSD 最广为人知的标志。该版本发行了 1000 余份拷贝，意味着已有大量计算机在使用。

- 1988 年 6 月 4.3BSD-Tahoe

随着开发人员逐渐淘汰老旧的 VAX 平台，4.3BSD-Tahoe 发布了针对 Power 6/32 平台（TAHOE）的版本。该平台由 Computer Consoles Incorporated 开发，代号 Tahoe，虽商业上未获成功，但首次实现 BSD 向非 VAX 架构的移植，将机器相关代码与无关代码分离，为后续系统可移植性奠定基础。

- 1991 年 386BSD 和 Net/2

Keith Bostic 发起了一个项目，旨在不使用 AT&T 代码的前提下，重新实现大多数标准的 UNIX 软件。最终发布了 Networking Release 2（Net/2）——一种几乎完全可自由分发的操作系统。在 Net/2 的基础上，BSD 为英特尔 80386 架构分别移植了两个版本：由 William Jolitz 和 Lynne Jolitz 夫妇开发的免费的 386BSD、由 Berkeley Software Design（BSDi）开发的专有 BSD/386（后来更名为 BSD/OS）。386BSD 本身昙花一现，但成为不久后启动的 NetBSD 和 FreeBSD 项目的代码基础。

- 1992 年 USL 诉讼案

BSDi 很快就陷入了与 AT&T 的 UNIX System Laboratories（USL，UNIX 系统实验室）子公司的法律纠纷中，当时 USL 是 System V 版权和 UNIX 商标的所有者。USL 对 BSDi 的诉讼于 1992 年提起，并导致对 Net/2 的分发禁令。该诉讼于 1994 年 2 月达成和解。和解条件之一是加州大学伯克利分校承认 Net/2 中有三个文件属于“受限制代码”（encumbered code），因为这些代码归 Novell 所有（Novell 此前从 AT&T 处获得了这些权利），必须删除。作为交换，Novell“认可”了 4.4BSD-Lite 发布时将声明为不受限制的代码，并强烈建议所有现有的 Net/2 用户迁移至 4.4BSD-Lite。FreeBSD 也在此列，项目被要求在 1994 年 7 月底之前停止发布基于 Net/2 的产品。根据协议条款，项目被允许在截止日期前做最后一次发布，即 FreeBSD 1.1.5.1。在 BSD 的约 18,000 个文件中，仅需删除三个文件，并修改另外 70 个文件以添加 USL 的版权声明。本次和解为首个基于 4.4BSD-Lite 的 FreeBSD RELEASE 的发布铺平了道路。

- 1993 年 6 月 FreeBSD 项目成立

FreeBSD 项目起源于 1993 年初，部分源自非官方的 386BSD 补丁包的最后三位协调人的创意：Nate Williams，Rod Grimes 和 Jordan Hubbard。他们最初的目标是制作一个 386BSD 的中间快照，以解决一些补丁包机制无法解决的问题。该项目早期的工作名称是 386BSD 0.5 或 386BSD Interim，正体现了这一事实。386BSD 是 Bill Jolitz 开发的操作系统。当时该系统问世已将近一年，但一直被严重忽视。随着补丁包日益膨胀，臃肿不堪，他们决定通过提供 386BSD 过渡项目来帮助 Bill 走出困境。然而，在没有明确提供备选方案的情况下，Bill Jolitz 突然决定退出 386BSD 过渡项目，他们的计划被迫搁浅。三人认为，即使没有 Bill 的支持，这个项目也是值得的，因此他们采用了 David Greenman 创造的“FreeBSD”之名。为了改善 FreeBSD 的发行渠道，Jordan Hubbard 随后联系了 Walnut Creek CDROM。Walnut Creek CDROM 不仅支持在 CD 上发行 FreeBSD，还为此项目提供了一台工作用机和高速互联网连接。如果没有 Walnut Creek CDROM 对这一当时完全未知项目的近乎前所未有的信任，FreeBSD 很可能无法如此迅速地发展至今天的规模。1993 年 6 月 19 日，该项目正式命名为“FreeBSD”。首个 FreeBSD RELEASE（FreeBSD 1.0）发布于 1993 年 11 月，基于 4.3BSD Net/2（Networking Release 2）磁带，并包含 386BSD 和自由软件基金会提供的许多组件。

- 1994 年 8 月 FreeBSD Ports

FreeBSD 的 Ports 和软件包为用户和管理员提供了一种简便的安装应用程序的方式。Ports 目前提供了多达 37,000 个 port。它们首次现身于 1994 年，当时 Jordan Hubbard 将“port make macros”提交到 FreeBSD 的 CVS 存储库中，目的是给他的软件包安装套件 **Makefile** 打补丁。

- 1994 年 11 月 22 日 IPFW

ipfirewall（IPFW）随 FreeBSD 2.0-RELEASE 引入，这种采用“首次匹配（First Match）”规则的防火墙自此成为系统的重要组成部分。ipfw 曾作为 Mac OS X（10.0 至 10.6 版本）的内置数据包过滤防火墙。

- 1998 年 5 月软更新（Soft Updates）

1998 年 5 月，FreeBSD 采用了软更新依赖跟踪系统。软更新旨在通过跟踪并强制执行元数据更新之间的依赖关系来维护文件系统元数据的完整性，防止因崩溃或断电导致损坏。

- 1999 年 10 月 17 日首届 BSD 大会

首届 FreeBSD 大会（FreeBSDCon'99）在加利福尼亚州伯克利举行。来自世界各地的 350 多名开发者和用户参加了此次活动，标志着 FreeBSD 受欢迎度和影响力的重要里程碑。

- 2000 年 3 月 14 日 FreeBSD Jail

FreeBSD Jail 随 2000 年初发布的 FreeBSD 4.0 引入。Jail 是一种操作系统级虚拟化机制，允许管理员将 FreeBSD 系统划分为多个独立的子系统，各子系统之间相互隔离。

- 2000 年 3 月 28 日 FreeBSD 基金会成立

FreeBSD 基金会是一家总部位于美国的非营利组织，注册为 501(c)(3) 机构，致力于支持 FreeBSD 项目、其开发和社区。资金来自个人和企业的捐款，用于赞助开发人员进行特定活动、购买硬件和网络基础设施，并提供开发者峰会的差旅津贴。该基金会由 Justin Gibbs 等人于 2000 年 3 月 28 日创立。

- 2000 年 7 月 27 日 kqueue(2)

kqueue(2) 是取代 select/poll 的创新解决方案，于 2000 年 7 月 27 日随着 FreeBSD 4.1-RELEASE 引入。这一可扩展的事件通知接口与后来 Linux 内核中引入的 epoll 机制在目标和设计思路上具有相似性。

- 2000 年 9 月首次核心团队选举

尽管此前已存在自我推选产生的核心团队，但首次通过选举形式组建核心团队是在 2000 年 9 月。当时任命了由 9 名成员组成的团队，自此以后每两年举行一次选举。

- 2001 年 11 月 EuroBSDCon

EuroBSDCon 2001 于 2001 年 11 月 9 日至 11 日在英国布莱顿举行（EuroBSDCon. Short History of EuroBSDCon[EB/OL]. [2026-04-18]. <https://2024.eurobsdcon.org/history.html>.）。随着全球社区的不断扩大，EuroBSDCon 的目标是聚集在 BSD 操作系统家族及相关项目上工作的用户和开发者。

- 2004 年 1 月 12 日 5.2-RELEASE

在 5.1 版本实验性支持 amd64 架构后，5.2-RELEASE 正式提供了对 amd64 的支持。amd64 成为首个被列为一级（Tier 1）架构的 64 位平台。

- 2004 年 3 月首届 AsiaBSDCon；5 月首届 BSDCan

在 EuroBSDCon 获得成功之后，首届 AsiaBSDCon 于 2004 年 3 月 13 日至 15 日在台湾“中央研究院”举办，紧随其后的是 BSDCan，于 5 月 13 日至 16 日在加拿大渥太华举行。随着 FreeBSD 社区的不断壮大，全球范围内对以 BSD 为主题的会议需求也随之增长。

- 2004 年 11 月 6 日 5.3-RELEASE 移植 PF

PF（Packet Filter）最初设计用于 OpenBSD，于 2003 年 3 月移植到 FreeBSD，2004 年 2 月 26 日由 Max Laier 集成到基本系统，随 5.3-RELEASE 一同发布。

- 2004 年 11 月 6 日 Libarchive

Libarchive 最初是为 FreeBSD 5.3 开发的，随该版本一同发布。它是一种用 C 语言编写的程序库，提供对多种不同存档格式的流式访问功能。

- 2005 年谷歌编程之夏

FreeBSD 基金会在首年度的谷歌编程之夏就参与其中。谷歌编程之夏始于 2005 年，为新的开发者提供了一个机会，使其参与开源编程项目。在项目结束后，许多参与该项目的学生成为了 FreeBSD 的贡献者。

- 2005 年 8 月首位执行董事

Deb Goodkin 于 2005 年 8 月加入基金会，成为基金会首位雇员，后担任执行董事。她之前在数据存储设备的市场营销、销售和开发领域有着 20 余年的工作经验。

- 2005 年 10 月 31 日新的 FreeBSD Logo

项目举行了一项 Logo 设计大赛，由 Anton K. Gural 设计的 Logo 获胜（当前仍在使用）。

- 2005 年 jemalloc

Jason Evans 于 2004 年初开始构思 jemalloc，2005 年 9 月集成到 FreeBSD 的 libc 中，随 FreeBSD 7.0-RELEASE（2008 年 2 月 27 日）成为默认内存分配器，取代了原有的 phkmalloc。该工具改进了 FreeBSD 的可扩展性和碎片化行为。

- 2008 年 2 月 ZFS

ZFS 由 Sun Microsystems 自 2001 年起开始开发，作为一种集成了文件系统和逻辑卷管理器的系统。该系统具有良好的可扩展性，并提供强大的数据完整性保护与高效的数据压缩功能。OpenSolaris 版本的 ZFS 于 2007 年 4 月 6 日由 Pawel Jakub Dawidek 导入 FreeBSD 源代码树，随 2008 年 2 月 27 日发布的 FreeBSD 7.0-RELEASE 首次进入 FreeBSD 系统。

- 2009 年 1 月 4 日 DTrace

Sun Microsystems 开发了 DTrace，DTrace 可用于实时调试生产系统中的内核和应用程序问题。尽管该工具最初是为 Solaris 开发的，但它随 FreeBSD 7.1-RELEASE（2009 年 1 月 4 日发布）成为 FreeBSD 的标准组成部分，FreeBSD 为 DTrace 提供了全面支持。

- 2010 年 8 月 Capsicum

Capsicum 是一种轻量级的操作系统能力和沙盒框架，可用于应用程序沙盒化、将大型软件架构分解为隔离的组件，并限制软件漏洞的影响范围。Capsicum 最初由剑桥大学开发，于 2010 年 8 月在 USENIX Security 研讨会上首次发表论文，随后作为可选功能发布在 FreeBSD 9.0 中，后来成为 FreeBSD 10.0 中的默认功能。

- 2012 年 CHERI

CHERI（Capability Hardware Enhanced RISC Instructions）项目源于 DARPA 的 CRASH/CTSRD 计划，该计划于 2010 年 9 月启动，由剑桥大学与 SRI International 合作开展，主要研究者包括 Robert N. M. Watson 等（与 Capsicum 同一研究者）。2012 年 3 月，CHERI 首篇论文《CHERI: a research platform deconflating hardware virtualization and protection》在伦敦举行的 RESoLVE'12 研讨会上发表。CHERI 将混合能力模型引入 CPU 架构领域，实现在进程地址空间内的细粒度隔离，并支持当前软件设计。

- 2012 年 7 月 14 日完成 Ports 从 CVS 到 Subversion 的迁移

Ports 集合自 2012 年 7 月起进入 CVS 与 SVN 双轨运行期，项目于 2013 年 2 月 28 日正式关闭 CVS 访问，彻底完成了向 Subversion 的过渡。

- 2012 年 8 月 Poudriere

Poudriere 是一种通过 Jail 测试 port，并构建 FreeBSD 镜像的工具，由 Bryan Drewery 开发，于 2012 年 8 月首次发布。

- 2012 年 11 月 Clang/LLVM

LLVM 项目是一组模块化和可重用的编译程序和工具链技术。Clang 项目为 LLVM 项目提供了 C 语言前端基础设施。FreeBSD 于 2012 年 11 月将 Clang 设为 i386 和 amd64 架构的默认编译器，随 FreeBSD 10.0-RELEASE 正式交付。

- 2012 年 11 月 11 日黑客入侵

FreeBSD 项目集群检测到黑客入侵，攻击通过窃取开发者 SSH 密钥实现，影响第三方软件包构建系统，未涉及基础系统源代码。项目花费数月进行审计与还原。

- 2013 年 9 月 17 日 OpenZFS 项目启动

OpenZFS 项目衍生于 OpenSolaris。2013 年 9 月 17 日，ZFS 开源项目宣布 OpenZFS 成为 ZFS 的继任者，并创建了一个正式的社区来维持开发和支持。但此时 FreeBSD 依旧使用的是最早的 OpenSolaris ZFS。

- 2014 年 1 月 20 日 pkg 成为默认的软件包管理器

pkg 首次出现在 9.1-RELEASE 中。在 10.0-RELEASE 中，pkg 成为默认的软件包管理器，取代了 `pkg_*` 等一系列命令。

- 2014 年 1-2 月 FreeBSD 期刊创刊号

作为 FreeBSD 社区的声音，也是了解 FreeBSD 最新发布版本和新进展的重要途径，FreeBSD 期刊的创刊号是 2014 年 1/2 月刊，重点关注 FreeBSD 10。最初以付费订阅模式发行，直至 2019 年 1 月才将 FreeBSD 期刊转为免费出版物，随后同时在基金会网站上进行刊载（同时提供了 HTML 和 PDF）。

- 2017 年 6 月 19 日新设“FreeBSD 日”

国际 FreeBSD 日是每年一度的庆祝活动，以赞扬 FreeBSD 对技术的开创性和持续影响，并纪念其传承的价值。2017 年 6 月 15 日，National Day Calendar 注册官宣布每年 6 月 19 日为 National FreeBSD Day。

- 2018 年 FreeBSD 中文社区（CFC）成立

在千禧年代曾存在多个中文社区，但后来逐渐衰落。这些早期社区的部分核心成员虽仍活跃于 FreeBSD 项目，但已不再专注于中文社区事务，转而投身于个人事业与家庭。FreeBSD 中文社区（CFC）最早由百度贴吧 FreeBSD 吧发展而来。

- 2021 年 4 月 6 日从 Subversion 迁移到 Git

FreeBSD 项目从 Subversion 到 Git 的迁移始于 2019 年 5 月的 DevSummit，当时成立了一个 Git 工作小组。src 仓库于 2020 年 12 月迁移，ports 于 2021 年 4 月 6 日完成迁移。

- 2021 年 4 月 13 日由 OpenSolaris ZFS 切换到 OpenZFS

在 13.0-RELEASE 中，FreeBSD 将 ZFS 实现从基于 illumos 的代码库切换到了统一的 OpenZFS 2 代码库，使 FreeBSD 能够更快地获取 ZFS 上游改进。该迁移计划最早于 2018 年提出。

- 2024 年 8 月德国主权技术基金赞助 FreeBSD 项目实施基础设施现代化

该项目的主要目标是改进基本系统、Ports 和软件包的安全工具，更新项目基础设施以加快开发速度、增强构建安全性，并降低新开发者的参与门槛。项目于 2024 年 8 月启动，至 2025 年 12 月完成。

- 2024 年 10 月笔记本和桌面工作组 LDWG 成立

笔记本和桌面工作组（LDWG）如其名称所示，致力于通过一系列功能改进和新增，使 FreeBSD 在个人设备上实现“开箱即用”的体验。该工作计划为期 1 至 2 年。

- 2024—2025 Alpha-Omega 审计

Alpha-Omega 项目先后审计了 FreeBSD 的 bhyve 虚拟机监视器、Capsicum 沙盒框架以及基本系统中的第三方程序，以提升 FreeBSD 项目的安全性与合规性。

- 2025 年 12 月 2 日引入 pkgbase

历经十年岁月磨炼，FreeBSD 终于在 15.0-RELEASE 中新增了 pkgbase 安装方式，以通过软件包来管理基本系统。这种方式最初源于 TrueOS 项目。

## 参考文献

- OpenZFS. OpenZFS[EB/OL]. [2026-06-07]. <https://en.wikipedia.org/wiki/OpenZFS>.
- FreeBSD Foundation. Infrastructure Modernization[EB/OL]. (2025-12-19)[2026-06-07]. <https://freebsdfoundation.org/blog/infrastructure-modernization-commissioned-by-the-sovereign-tech-agency/>.
- FreeBSD Foundation. Contributing to FreeBSD Ports with Git[EB/OL]. [2026-06-07]. <https://freebsdfoundation.org/wp-content/uploads/2022/03/mingrone.pdf>.
- Watson R N M, et al. CHERI: A Research Platform Deconflating Hardware Virtualization and Protection[C]//RESoLVE'12 Workshop, London, UK, 2012-03.
- Gunkies. Power 6/32[EB/OL]. [2026-06-07]. <https://gunkies.org/wiki/Tahoe>.
- Laier M. Packet Filter (pf) An Extended Introduction[EB/OL]. (2004-10-21)[2026-06-07]. <https://people.freebsd.org/~mlaier/sucon.pdf>. PF 移植报告。
- Evans J. A Scalable Concurrent malloc(3) Implementation for FreeBSD[C]//BSDCan, 2006. 新型内存分配器的实现。
- Dawidek P J. Porting the Solaris ZFS file system to the FreeBSD operating system[C]//AsiaBSDCon, 2007. ZFS 移植报告。
- National Day Calendar. NEW DAY PROCLAMATION | NATIONAL FREEBSD DAY - June 19[EB/OL]. (2017-06-15)[2026-06-07]. <https://www.nationaldaycalendar.com/proclamations/new-day-proclamation-national-freebsd-day-june-19>. 美国国家日历。
- FreeBSD Project. FreeBSD.org intrusion announced November 17th 2012[EB/OL]. (2012-11-17)[2026-06-06]. <https://www.freebsd.org/news/2012-compromise/>. FreeBSD 2012 入侵事件。
- FreshPorts. ports-mgmt/poudriere-devel[EB/OL]. [2026-06-06]. <https://www.freshports.org/ports-mgmt/poudriere-devel/>. Port **poudriere** 添加日期为 2012-08-16
- FreeBSD Foundation. Development Project Update: Toolchain Modernization[EB/OL]. (202007)[2026-06-06]. <https://freebsdfoundation.org/wp-content/uploads/2020/07/Development-Project-Update-Toolchain-Modernization.pdf>.
- Ritchie D M. The Evolution of the Unix Time-sharing System[EB/OL]. (1984)[2026-06-07]. <https://www.read.seas.harvard.edu/~kohler/class/aosref/ritchie84evolution.pdf>. 记载“In early 1970 we proposed acquisition of a PDP-11”。
- Multicians. GE-635s at Project MAC and BTL[EB/OL]. [2026-06-07]. <https://dps8m.gitlab.io/w3/multicians.org/ge635.html>.
- FreeBSD Foundation. Timeline[EB/OL]. [2026-03-25]. <https://freebsdfoundation.org/freebsd/timeline/>. FreeBSD 发展历史时间线。
- McKusick M K, Neville-Neil G V, Watson R N M. FreeBSD 操作系统设计与实现[M]. 陈向群,郭立峰,叶顺平,译. 原书第 2 版. 北京: 机械工业出版社, 2021: VI. 记载“1995 年 OpenBSD 组从 NetBSD 组中分离出来”。
- FreeBSD Foundation. Staff[EB/OL]. [2026-04-16]. <https://freebsdfoundation.org/about-us/our-team/>. 记载 Deb Goodkin 于 2005 年 8 月加入基金会，为首位雇员。
- SeaGL. 25+ Years of FreeBSD and Why You Should Get Involved![EB/OL]. (2019-11-15)[2026-04-16]. <https://osem.seagl.org/conferences/seagl2019/program/proposals/611>. 记载 Deb Goodkin “joining as the first employee back in August 2005”。
- FreeBSD Wiki. Jails[EB/OL]. [2026-04-16]. <https://wiki.freebsd.org/Jails>. 记载“Jails were introduced by Poul-Henning Kamp in March 2000 with FreeBSD 4.0-RELEASE”。
- Watson R N M, et al. CHERI: A Hybrid Capability-System Architecture for Scalable Software Compartmentalization[C]//ISCA. 2015. CHERI 原始论文，阐述硬件能力架构扩展的设计与实现。
- ACM. Fernando J (“Corby”) Corbato[EB/OL]. [2026-04-17]. <https://amturing.acm.org/award_winners/corbato_1009471.cfm>. 记载 CTSS 于 1961 年 11 月在 IBM 709 上首次演示。
- Tom Van Vleck. The Multicians web site[EB/OL]. (2026-04-08)[2026-04-17]. <https://multicians.org/history.html>. 记载 Multics 项目历史，通用电气公司于 1964 年 8 月签约、贝尔实验室于 1964 年 11 月加入。
- FreeBSD Project. Core Bylaws[EB/OL]. [2026-04-17]. <https://www.freebsd.org/internal/bylaws/>. 记载首次核心团队选举于 2000 年 9 月举行。
- FreeBSD Foundation. Resolutions Document[EB/OL]. [2026-04-17]. <https://freebsdfoundation.org/wp-content/uploads/2015/12/ResolutionsDocument-1.pdf>. 记载 FreeBSD 基金会成立文件签署日期为 2000 年 3 月 28 日。
- FreeBSD Project. FreeBSD News Flash October 1999[EB/OL]. [2026-04-17]. <https://ftpmirror.your.org/pub/FreeBSD-CVS/www/data/news/1999/index.html>. 记载 FreeBSDCon'99 参会人数超过 350 人。
- USENIX. Announcing the USENIX AsiaBSDCon and Request for Papers[EB/OL]. (2003-10)[2026-04-17]. <https://web.archive.org/web/20041217153402/https://www.bsdnewsletter.com/2003/10/News107.html>. 记载首届 AsiaBSDCon 于 2004 年 3 月 13 日至 15 日在台湾“中央研究院”举办。
- IEEE Computer Society. Linus Torvalds[EB/OL]. [2026-04-17]. <https://www.computer.org/profiles/linus-torvalds/>. 记载 Linus Torvalds 于 1988 年入学赫尔辛基大学，后获得计算机科学硕士学位。
- Evans J. A Scalable Concurrent malloc(3) Implementation for FreeBSD[C]//BSDCan, 2006. 记载 jemalloc 的设计与实现，2005 年集成到 FreeBSD libc。
- Evans J. jemalloc Background[EB/OL]. [2026-04-17]. <https://github.com/jemalloc/jemalloc/wiki/Background>. 记载 jemalloc 最初构思于 2004 年初，2005 年 9 月集成到 FreeBSD。
- OpenZFS. History[EB/OL]. [2026-04-17]. <https://www.openzfs.org/wiki/History>. 记载 ZFS 开发始于 2001 年，2008 年随 FreeBSD 7.0 移植发布。
- FreeBSD Project. FreeBSD 7.0-RELEASE Announcement[EB/OL]. (2008-02-27)[2026-04-17]. <https://www.freebsd.org/releases/7.0R/announce/>. FreeBSD 7.0-RELEASE 发布日期为 2008 年 2 月 27 日。
- FreeBSD Project. FreeBSD 7.1-RELEASE Announcement[EB/OL]. (2009-01-04)[2026-04-17]. <https://www.freebsd.org/releases/7.1R/announce/>. FreeBSD 7.1-RELEASE 发布日期为 2009 年 1 月 4 日，DTrace 随此版本引入。
- Watson R N M, Neumann P G, Woodruff J, et al. CHERI: A Research Platform Deconflating Hardware Virtualization and Protection[C]//RESOLV'12 Workshop, London, UK, 2012-03. CHERI 首篇论文。
- SRI International. CTSRD Final Technical Report[EB/OL]. [2026-04-17]. <https://web.archive.org/web/20251122133531/https://www.csl.sri.com/~neumann/20191213-ctsrd-ftr-final.pdf>. 记载 CTSRD/CHERI 项目始于 2010 年 9 月 24 日。
- MCKUSICK M K. Twenty Years of Berkeley Unix: From AT&T-Owned to Freely Redistributable[M]//SALUS P H, ed. Open Sources: Voices from the Open Source Revolution. Sebastopol: O'Reilly, 1999. 记载 DARPA 合同始于 1980 年 4 月，为期 18 个月。
- FreeBSD Core Team. Change to FreeBSD release scheduling and support period[EB/OL]. (2024-07-10)[2026-04-18]. <https://lists.freebsd.org/archives/freebsd-announce/2024-July/000143.html>. 自 FreeBSD 15 起，稳定分支支持周期由 5 年缩短为 4 年。
- USL v. BSDi Settlement Agreement[EB/OL]. (1994-02-04)[2026-04-17]. <https://web.archive.org/web/20240613194116/https://www.bell-labs.com/usr/dmr/www/bsdi/USLsettlement.pdf>. 记载 Net/2 中仍残留 AT&T 代码，和解后 4.4BSD-Lite 方彻底移除。
- FreeBSD Foundation. Navigating FreeBSD's New Quarterly and Biennial Release Schedule[EB/OL]. (2024-07-16)[2026-04-17]. <https://freebsdfoundation.org/blog/navigating-freebsds-new-quarterly-and-biennial-release-schedule/>. 记载自 15.x 起维护周期从 5 年缩短至 4 年，大版本周期为每 2 年一次。
- FreeBSD Project. FreeBSD 5.2-RELEASE Announcement[EB/OL]. (2004-01-12)[2026-04-17]. <https://www.freebsd.org/releases/5.2R/announce/>. FreeBSD 5.2-RELEASE 发布日期为 2004 年 1 月 12 日，amd64 成为 Tier 1 架构。
- FreeBSD Project. FreeBSD 5.3-RELEASE Announcement[EB/OL]. (2004-11-06)[2026-04-17]. <https://www.freebsd.org/releases/5.3R/announce/>. FreeBSD 5.3-RELEASE 发布日期为 2004 年 11 月 6 日，PF 及 Libarchive 均随此版本发布。
- Libarchive Project. LibarchiveUsers[EB/OL]. [2026-04-17]. <https://github.com/libarchive/libarchive/wiki/LibarchiveUsers>. 记载“libarchive was originally developed for FreeBSD; it was first released with FreeBSD 5.3 in November 2004”。
- Max Laier. Packet Filter (pf) An Extended Introduction[EB/OL]. (2004-10-21)[2026-04-17]. <https://web.archive.org/web/20250503030531/https://people.freebsd.org/~mlaier/sucon.pdf>. PF 移植者 Max Laier 的演讲，PF 于 2003 年 3 月移植到 FreeBSD，2004 年 2 月 26 日集成到 FreeBSD 基本系统。

## 课后习题

1. 在 QEMU 中运行 FreeBSD 1.0 版本，记录启动过程中与当代 FreeBSD 的显著差异，分析这些差异反映出的系统设计演进。
