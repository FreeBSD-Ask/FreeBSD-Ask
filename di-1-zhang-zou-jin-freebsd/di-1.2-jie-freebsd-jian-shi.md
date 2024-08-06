# 第 1.2 节 FreeBSD 简史

## 什么是 FreeBSD？

问：如何定义 FreeBSD？答：一款开源的类 UNIX 操作系统。

BSD 最初是由加州大学伯克利分校（University of California, Berkeley）所开发的，意为 `Berkeley Software Distribution`（伯克利软件套件）。

值得注意地是，Berkeley 伯克利之名来自著名的近代经验论哲学家乔治·贝克莱（George Berkeley，1685－1753，音译问题，原词是一致的），伯克利市和伯克利大学都是来源他的名字。

贝克莱主教通过他的形而上学（反对牛顿绝对时空观等）启发了 20 世纪一众科学家，例如爱因斯坦，在某种意义上指导了现代科技革命。并且引发了数学史上关于无穷小量的数学哲学讨论。

> esse est percipi, to be is to be perceived（存在就是被感知）。——【英】乔治·贝克莱

![](../.gitbook/assets/图片3.png)

**FreeBSD 不是 Linux，亦不是 UNIX，是类 UNIX**

UNIX -> Networking Release 1->Networking Release 2 ->386BSD -> FreeBSD 1.0

386BSD -> 诉讼（1991-1994） -> 4.4 BSD-Lite -> FreeBSD 2.0

“I have never even checked 386BSD out; when I started on Linux it wast available”——Linus

![](../.gitbook/assets/图片2.png)

> 图片来源：https://github.com/freebsd/freebsd-src/blob/main/share/misc/bsd-family-tree

## 时间表

### 1962 年 分时操作系统（Timesharing OS）

在 20 世纪 60 年代初出现了分时操作系统，其中一个最早的系统是由英国曼彻斯特计划设计的 Atlas 品牌计算机上的 Atlas 监控程序。在那个时代，分时共享系统意味着两个人共享同一台计算机，往往需要设定一个小时时间表来安排他们使用计算机的时间。

### 1964 年 MULTICS（多任务信息与计算系统）

Multics 的最初规划和开发始于 1964 年，地点位于马萨诸塞州的剑桥。最初，这是由麻省理工学院（Fernando Corbató 领导的 MAC 计划）与通用电气公司和贝尔实验室合作的项目。它是在专门为该操作系统设计的通用电气 645 计算机上开发的；第一个完整系统于 1967 年 1 月交付给麻省理工学院。

### 1969 年 UNIX（UNIX 操作系统）

在贝尔实验室退出 Multics 项目之前，Dennis Ritchie 和 Ken Thompson 对 Multics 的潜力有所了解。他们从贝尔实验室法务部门获得了资金，购买了一台更强大的 PDP-11/20 机器。在 1969 年，Ken Thompson、Dennis Ritchie 和其他人开始着手开发一款利用更强大计算机全部功能的新程序。这个程序被称为 Unics（Uniplexed Information and Computing Service，即没路信息计算系统）。

### 1972 年 UNIX 代码迁移到 C 语言

Dennis Ritchie 决定为 UNIX 开发一种高级汇编语言，其中的语句可以翻译成两到三条指令。这促使他开发了 C 编程语言。第四个研究版的 UNIX 被重新编写成 C 语言。这使得 UNIX 具备了可移植性，从而改写了操作系统的历史。

### 1974 年 UNIX 被引入加州大学伯克利分校

1974 年，加州大学伯克利分校的 Bob Fabry 教授从 AT&T 获得了 UNIX 的源代码许可。Bob Fabry 此前在 1973 年的 ACM 操作系统原理研讨会（Association for Computing Machinery）上见过 UNIX 4，并有意将其引入该大学。计算机系统研究小组（CSRG）开始修改和改进 AT&T Research Unix。他们将这个修改后的版本称为“BSD Unix”或“BSD”。

### 1978 年 3 月 9 日 1BSD 发布

基于 UNIX 创建的伯克利软件发行版（1BSD）是 UNIX 第六版的一个附加组件，而非独立的完整操作系统。此版本大约发行了 30 份副本。

### 1979 年 5 月 10 日 2BSD 发布

第二个伯克利软件发行版（2BSD）于 1979 年 5 月发布，包括 1BSD 软件的更新，以及由 Bill Joy 新开发的两个至今在 Unix 系统上仍在使用的程序：vi 文本编辑器（ex 的可视化版本）和 Csh。这是 Bill Joy 为 PDP-11 工作的最后一个 BSD 版本。大约发行了 75 份副本。

### 1980 年 6 月 DARPA 资助

在 1980 年初，DARPA 正在寻找一种能够帮助当前军事项目的操作系统。Bill Joy 关于 UNIX 系统（特别是 BSD）能力的一篇论文引起了他们的注意。他们在 1980 年 6 月开始资助伯克利进行相关工作。

### 1983 年 8 月 4.2BSD 发布

4.2BSD 的正式发布是在 1983 年 8 月。值得注意的是，这是在 1982 年 Bill Joy 离开后共同创建的 Sun Microsystems 的第一个版本。它也标志着 BSD 的吉祥物首次出现在 John Lasseter 的画作中，并出现在 USENIX 发行的印刷手册的封面上。这次发布有了超过 1000 个发行版本，代表了大量的计算机。

### 1988 年 6 月 4.3BSD-Tahoe

随着开发人员逐渐远离老旧的 VAX 平台，4.3BSD-Tahoe 发布了针对 Power 6/32 平台（TAHOE）的版本。这个发布非常有价值，因为它将 BSD 中的机器相关代码与机器无关代码分离开来，从而提高了系统的未来可移植性。

### 1991 年 386BSD 和 Net/2

Keith Bostic 启动了一个项目，重新实现大部分标准的 Unix 实用程序，且不使用 AT&T 的代码。最终发布了 Networking Release 2（Net/2），一个几乎完整的可自由分发的操作系统。Net/2 成为两个独立的 BSD 到 Intel 80386 架构的移植的基础：由 William Jolitz 开发的免费的 386BSD 和由 Berkeley Software Design（BSDi）开发的专有 BSD/386（后来更名为 BSD/OS）。386BSD 本身存活时间不长，但成为随后不久开始的 NetBSD 和 FreeBSD 项目的初始代码基础。

### 1992 年 USL 诉讼

BSDi 很快就陷入了与 AT&T 的 Unix System Laboratories（USL）子公司的法律纠纷中，当时 USL 是 System V 版权和 Unix 商标的所有者。USL 对 BSDi 的诉讼于 1992 年提起，并导致对 Net/2 的发布禁令。该诉讼于 1994 年 1 月达成和解。在伯克利发布的 18,000 个文件中，只有三个文件需要移除，并对 70 个文件进行修改以显示 USL 的版权声明。这个和解为首个 FreeBSD 版本的发布铺平了道路。

### 1993 年 6 月 FreeBSD 的创建

386BSD 的开发进展缓慢，在一段时间的忽视后，一群 386BSD 用户决定自己复刻出去，并创建 FreeBSD，以便他们能够使操作系统保持最新状态。1993 年 6 月 19 日，项目选择了名为 FreeBSD 的名称。第一个 FreeBSD 的版本于 1993 年 11 月 发布。

### 1994 年 8 月 FreeBSD Ports

FreeBSD 的 Ports 和软件包为用户和管理员提供了一种简单的安装应用程序的方式。Ports 现在提供了超过 34,000 个 port，它们首次现身于 1994 年，当时 Jordan Hubbard 将“port make macros”提交到 FreeBSD 的 CVS 仓库中，以补充他的软件包安装套件“Makefile”。

### 1994 年 11 月 22 日 IPFW（IP 防火墙）

ipfirewall（IP 防火墙）是在 FreeBSD 2.0-RELEASE 中被引入的，这种“首次匹配”防火墙自此成为操作系统的重要组成部分。ipfw 曾作为 Mac OS X 的内置防火墙而广泛使用。

### 1996 年 8 月 FreeBSD 2.1.5

FreeBSD 2.1.5 于 1996 年 8 月发布，迅速在互联网服务提供商（ISP）和商业社区中广受欢迎。这个版本对于 FreeBSD 来说是一个巨大的成功。

### 1998 年 5 月 软更新（Soft Updates）

软更新依赖跟踪系统于 1998 年 5 月被 FreeBSD 采用。软更新旨在通过跟踪和执行更新之间的依赖关系，保持文件系统元数据的完整性，以防发生崩溃或停电。

### 1998 年 10 月 16 日 FreeBSD 3.0-RELEASE

FreeBSD 3.0-RELEASE 于 1998 年 10 月 16 日宣布发布，为 i386 带来了最初的对称多处理（SMP）支持。3.0-RELEASE 还默认使用了 SCSI 通用访问方法（CAM）。

### 1998 年 11 月 29 日 FreeBSD 2.2.8-RELEASE

FreeBSD 2.2.8-RELEASE 于 1998 年 11 月 29 日发布（在 FreeBSD 3 发布后一个月）。FreeBSD 2 的最终分支包括 sendfile 和 dummynet 两个关键特性，这些特性在后续的 FreeBSD 版本中得到了进一步的发展。

### 1999 年 10 月 17 日 首届 BSD 大会

首届 FreeBSD 大会（FreeBSDCon'99）在加利福尼亚州伯克利举行。来自世界各地的 300 多名开发者和用户参加了此次活动，标志着这个操作系统在受欢迎度和影响力上的一个重要里程碑。

### 2000 年 3 月 14 日 FreeBSD 4.0-RELEASE

于 2000 年 3 月 14 日宣布发布的 FreeBSD 4.0-RELEASE 带来了大量的新功能和工具。该版本包括早期的 IPv6 支持和 IPsec，两者都依赖于 KAME 代码，还有 OpenSSH、 `accept()`过滤器以及具备基本的 802.11b WiFi 支持的 wi(4)。

### 2000 年 3 月 14 日 FreeBSD Jail

FreeBSD Jail 是在 2000 年初发布的 FreeBSD 4.0 中被引入的。Jail 机制是操作系统级别的虚拟化实现，允许系统管理员将一个 FreeBSD 系统分割为多个独立的小系统或"Jail"。这使得系统管理员能够更好地保护和优化他们的 FreeBSD 系统。

### 2000 年 3 月 15 日 FreeBSD 基金会成立

FreeBSD 基金会是一个总部位于美国的非营利组织，注册为 501(c)(3) 机构，致力于支持 FreeBSD 项目、其开发和社区。资金来自个人和企业的捐款，用于赞助开发人员进行特定活动、购买硬件和网络基础设施，并提供开发者峰会的差旅津贴。该基金会由 Justin Gibbs 于 2000 年 3 月 15 日创立。

### 2000 年 7 月 27 日 kqueue(2)

kqueue(2) 是取代 select/poll 的创新解决方案，于 2000 年 7 月 27 日随着 FreeBSD 4.1-RELEASE 引入。这个可扩展的事件通知接口启发了 Linux 的 epoll() 机制。

### 2000 年 10 月 17 日 首次核心团队选举

尽管此前已经存在一个自我选定的核心团队，但首次核心团队选举是在 2000 年 9 月举行的。当时任命了一个由 9 名成员组成的团队，并自那以后每两年举行一次选举。

### 2001 年 9 月 EuroBSDCon

EuroBSDCon 2001 于 2001 年尾在英国布赖顿举行。随着全球社区的不断扩大，EuroBSDCon 的目标是聚集在 BSD 操作系统家族及相关项目上工作的用户和开发者。

### 2003 年 1 月 19 日 FreeBSD 5.0-RELEASE

FreeBSD 5.0-RELEASE 经历了近 3 年的开发，由于引入了先进的多线程内核，提供更好的 SMP 支持，因此备受期待。

### 2004 年 1 月 9 日 AMD64 磁盘镜像

在实验性版本的 5.1 中包含后，5.2-RELEASE 正式支持了 amd64，amd64 成为第一个一级 64 位平台。

### 2004 年 3 月 12 日 首届 AsiaBSDCon 和 BSDCan

在 EuroBSDCon 获得成功之后，首届 AsiaBSDCon 于 2004 年 3 月 12 日启动，紧随其后的是 BSDCan，于 5 月 13 日举行。随着 FreeBSD 社区的不断发展壮大，全球范围内对于以 BSD 为重点的会议的需求也随之增长。

### 2004 年 5 月 1 日 谷歌代码之夏

FreeBSD 基金会在首个年度的谷歌代码之夏中就开始参与。谷歌代码之夏为新开发者提供了一个机会，让他们参与当前的开源编码项目。许多参与该项目的学生在项目结束后成为了 FreeBSD 的贡献者。

### 2004 年 11 月 3 日 移植 PF

在 2006 年，原本设计用于 OpenBSD 的 Packet Filter（简称 PF）被移植到了 FreeBSD，与 5.3-RELEASE 一同发布。

### 2004 年 11 月 17 日 Libarchive

Libarchive 最初是为 FreeBSD 5.3 开发的，该版本于 2004 年末发布。它是一个用 C 语言编写的程序库，提供对多种不同存档格式的流式访问功能。

### 2005 年 8 月 首位执行董事

Deb Goodkin 于 2005 年加入基金会，成为首位执行董事。她之前在数据存储设备的市场营销、销售和开发领域有超过 20 年的工作经验。

### 2005 年 10 月 8 日 新的 FreeBSD Logo

举行了一个标志设计竞赛，由 Anton K. Gural 设计的当前还在使用的标志获胜。

### 2005 年 11 月 4 日 FREEBSD 6.0-RELEASE

FreeBSD 6.0-RELEASE 于 2005 年 11 月 4 日发布。FreeBSD 6.0 标志着 sys/arm/arm 中首次提交的 32 位 Arm 支持，802.11 WiFi 支持得到升级以包括高级功能，并通过添加 libthr(3) 和进一步的内核改进实现了 1:1 用户级线程。

### 2007 年 JEMALLOC

Jason Evans 于 2005 年开发了 jemalloc，这是一个内存分配器。与此同时，FreeBSD 需要一个可扩展的多处理器内存分配器，因此 Evans 将 jemalloc 集成到 FreeBSD 的 libc 中，并改进了其可扩展性和碎片化行为。

### 2008 年 2 月 27 日 FREEBSD 7.0-RELEASE

因为担心 ULE 调度程序是否准备就绪，FreeBSD 7.0-RELEASE 在发布时作为内核可选参数搭载了它，它在下一个稳定版本中成为了默认调度程序。FreeBSD 7.0 还添加了 SCTP 协议以及与网络、音频和多处理器性能相关的重大更新。

### 2008 年 3 月 ZFS

在 2005 年，Sun Microsystems 在开发一种新的文件系统，最终产物是 ZFS，这是一个集成了文件系统和逻辑卷管理器的系统。该系统具有可扩展性，并提供了广泛的数据完整性保护和高效的数据压缩功能。ZFS 于 2008 年初添加到 FreeBSD 代码中。

### 2009 年 1 月 6 日 DTrace

Sun Microsystems 开发了 DTrace，DTrace 可用于实时调试生产系统中的内核和应用程序问题。尽管该程序最初是为 Solaris 开发的，但它成为 FreeBSD 的标准组成部分，并为 DTrace 提供了全面支持。

### 2009 年 11 月 25 日 FreeBSD 8.0-RELEASE

FreeBSD 8.0-RELEASE 于 2009 年 11 月 25 日宣布发布，其中包含了 XEN domU 支持、VNET、透明超级页、改进的 ZFS 支持以及新的 USB 堆栈，包括了 USB 3.0 支持。

### 2010 年 8 月 Capsicum

Capsicum 是一个轻量级的操作系统能力和沙盒框架。它可以用于应用程序分隔、将较大的软件体系分解为隔离的组件，并限制软件漏洞的影响。Capsicum 最初由剑桥大学开发，并首次作为可选功能在 FreeBSD 9.0 中发布，后来成为 FreeBSD 10.0 中的默认功能。

### 2012 年 CHERI

在 2012 年，剑桥大学开始开发了 Capability Hardware Enhanced RISC Instructions (CHERI)，这是基于之前的 Capsicum 项目的发展而来。CHERI 将 Capsicum 的混合能力模型转移到 CPU 架构领域，实现在进程地址空间内的细粒度隔离，并支持当前软件设计。

### 2012 年 POUDRIERE

Poudriere 是一个利用 jail 来测试 port 并后续构建 FreeBSD 镜像的工具，它被添加到了 ports 中。

### 2012 年 1 月 12 日 FREEBSD 9.0-RELEASE

FreeBSD 9.0-RELEASE 于 2012 年 1 月 12 日发布，其中包括了全新的安装程序 bsdinstall。其他主要特性包括软更新日志（SUJ）、NFS 版本 4 和模块化拥塞控制。FreeBSD 9 是索尼用于开发 PlayStation 4 操作系统（Obris OS）所使用的版本。

### 2012 年 4 月 12 日 CLANG/LLVM

LLVM 项目是一组模块化和可重用的编译器和工具链技术。Clang 项目为 LLVM 项目提供了 C 语言前端和工具基础设施。这些程序目前是 FreeBSD 的编译基础设施。

### 2013 年 2 月 28 日 从 CVS 迁移到 Subversion

由于大多数 port 已经在 Subversion 中进行开发，于 2013 年 2 月 28 日正式完成了从 CVS 到 Subversion 的迁移。在此之后，FreeBSD ports 不再使用 CVS。

### 2013 年 9 月 17 日 开源 ZFS 项目启动

开源 ZFS 项目是 OpenSolaris 的一个衍生项目。于 2013 年 9 月 17 日，开源 ZFS 项目宣布 OpenZFS 作为 ZFS 的继任者，并创建了一个正式的社区来继续开发和支持。

### 2014 年 1 月 20 日 FreeBSD 10.0-RELEASE

于 2014 年 1 月 20 日宣布发布 FreeBSD 10.0-RELEASE，带来了大量的新功能和工具。10.0 版本配备了 pkg(7) 并切换到 pkgng，这个新的软件包管理工具允许用户跳过手动编译 ports 的过程。该发布还包括 FUSE 实现、高级 iSCSI 支持（包括目标（服务器）和发起者（客户端））、VirtIO 驱动程序、bhyve 虚拟化技术和 amd64 架构上的 UEFI 支持。

### 2016 年 10 月 10 日 FREEBSD 11.0-RELEASE

于 2016 年 10 月 10 日宣布发布 FreeBSD 11.0-RELEASE。该版本包含了对无线网络的多项改进以及对 UDP-lite 的集成。最重要的是，FreeBSD 11 还包括了对 aarch64（arm64）的支持，最初被分类为二级架构。

### 2017 年 6 月 19 日 首个"FreeBSD Day"

国际 FreeBSD 日是每年一度的庆祝活动，旨在赞扬 FreeBSD 对技术的开创性和持续影响，并纪念其传承的价值。

### 2018 年 12 月 11 日 FREEBSD 12.0-RELEASE

2018 年 12 月 11 日发布的 FreeBSD 12.0 版本增强了对 AMD CPU 的支持，并显著提升了对现代显卡的支持。此外，还新增了开放指令集架构（ISA）RISC-V 的支持。

### 2021 年 4 月 6 日 Git 迁移完成

于 2021 年 4 月 6 日 完成了从 Subversion 到 Git 的迁移。此过程始于 2019 年 5 月的 DevSummit，在当时成立了一个 Git 工作小组。

### 2021 年 4 月 13 日 FREEBSD 13.0-RELEASE

FreeBSD 13.0-RELEASE 于 2021 年 4 月 13 日发布。尽管 AArch64 从 FreeBSD 11 开始就得到了支持，但它在 FreeBSD 13.0-RELEASE 中才被提升为一级平台，成为第一个非 x86 架构的一级平台。13.0 还包括内核 TLS 卸载、对 clang 和 LLVM 的升级以及移除了弃用的库和工具。

原文地址：https://freebsdfoundation.org/freebsd/timeline/




