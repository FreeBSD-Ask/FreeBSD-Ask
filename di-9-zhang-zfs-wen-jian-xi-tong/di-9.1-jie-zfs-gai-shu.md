# 9.1 ZFS 概述

ZFS 源于 Sun Solaris，2005 年以 CDDL 许可证开源，2007 年导入 FreeBSD。Oracle 收购 Sun 后 ZFS 转为闭源开发，开源社区于 2013 年发起 OpenZFS 项目延续其发展。2020 年 OpenZFS 2.0 统一了 FreeBSD 与 Linux 的 ZFS 代码库，提供写时复制、快照、端到端校验与自愈等存储特性。

## ZFS 发展历程：从 Solaris 到 OpenZFS

ZFS 最早由 Sun 公司开发，旨在取代 Solaris（早期曾用名 SunOS）上的 UFS 文件系统。SunOS 和 BSD Unix 的关键开发者之一是 Bill Joy，他同时也是 Sun 的创始人之一。SunOS 早期基于 BSD Unix 开发，随后转向 SVR4（Unix System V Release 4，即与 AT&T 合作开发）。

ZFS 源代码于 2005 年 10 月 31 日集成到 Solaris 开发主干（revision 789），随后于 2005 年 11 月 16 日作为 OpenSolaris build 27 以 CDDL（Common Development and Distribution License，通用开发及发行许可）开源发布。

ZFS 于 2007 年导入 FreeBSD 源代码树，在 FreeBSD 7.0-RELEASE（2008 年 2 月，pool v6）中以实验状态发布；在 FreeBSD 8.0-RELEASE（2009 年 11 月，pool v13）中宣布为生产就绪状态。

2009 年 4 月 Oracle 宣布收购 Sun（2010 年 1 月收购完成）之后，Solaris 项目（易名为 Oracle Solaris）及 ZFS（易名为 Oracle Solaris ZFS）进入闭源开发模式，OpenSolaris 社区管理委员会于 2010 年 8 月自行解散（revision 13149，在解散时 ZFS pool 为 [v28](https://github.com/freebsd/freebsd-src/commit/572e285762521df27fe5b026f409ba1a21abb7ac)）。OpenSolaris 的主要社区开发力量迁移到了新分支 [illumos 项目](https://github.com/illumos/illumos-gate)。从此以后（v28），Oracle Solaris ZFS 与社区版本开始分道扬镳。

目前 illumos 采用类似 Linux 内核的开发模式，衍生出 OpenIndiana、OmniOS 等十余款发行版。但其年平均代码提交量约 150 次，开发活跃度已显著降低。

2011 年 2 月，FreeBSD 采用了 ZFS pool v15，这是 2009 年 10 月随 Solaris 10 update 8（Solaris 10 10/09）分发的版本。

2011 年 11 月，Oracle Solaris 11 发布，ZFS pool 升级至 v31。

2012 年 1 月 12 日，FreeBSD 9.0-RELEASE 支持了 ZFS pool v28。参见：Finally... Import the latest open-source ZFS version - (SPA) 28[EB/OL]. [2026-03-26]. <https://github.com/freebsd/freebsd-src/commit/10b9d77bf1ccf2f3affafa6261692cb92cf7e992>。

在 OpenSolaris 关停 3 年后（2013 年），OpenZFS 项目正式成立，统一了 ZFS 的开源开发（此前 ZFS on Linux 原生内核模块项目已于 2010 年启动，而基于 FUSE 的 ZFS-FUSE 项目则始于 2008 年）。由于 Oracle Solaris ZFS 的闭源开发，OpenZFS 很难再兼容 Oracle Solaris ZFS。

“时来天地皆同力，运去英雄不自由。”（[唐] 罗隐《筹笔驿》）OpenZFS 新功能的主要开发商 Delphix 公司（Delphix 于 2024 年 3 月被 Perforce Software 收购）将其设备的操作系统从 illumos 迁移到了 Linux，基本上放弃了对前者的投入。其理由是几乎所有云平台厂商和虚拟机平台仅支持 Linux，因此 illumos 几乎再难得到支持。甚至 Oracle Solaris 本身也进入了维护模式（版本 11.4 的生命周期可延续至 2037 年）。Oracle ZFS 迁移到了企业级存储解决方案 [Oracle 存储](https://www.oracle.com/cn/storage/#zfs-storage-appliance)。

illumos 版本的 ZFS（其主要开发仍由 OpenZFS 推动）得到的功能更新日趋减少，FreeBSD 对该版本 ZFS 的维护难度也不断上升，当 ZFS 出现新功能时，通常要先等待其合并到 illumos，再回溯到 FreeBSD 中。但 illumos 的开发已基本停滞。2018 年 8 月，FreeBSD 项目开始研究如何将 FreeBSD ZFS 由 illumos 迁移到直接上游 OpenZFS。

OpenZFS 于 2020 年 8 月合入 FreeBSD-CURRENT，随 FreeBSD 13.0-RELEASE（2021 年 4 月）正式发布，“ZFS 的实现目前由 OpenZFS 提供。[9e5787d2284e](https://cgit.freebsd.org/src/commit/?id=9e5787d2284e)（由 iXsystems 赞助）”取代了 OpenSolaris/illumos 版本的 ZFS。这一迁移使 FreeBSD 与主流 ZFS 开源生态重新接轨。

目前 OpenZFS 代码提交量的首位成员来自美国劳伦斯利弗莫尔国家实验室（LLNL，Lawrence Livermore National Laboratory），OpenZFS 的开发由多家组织共同推动，主要贡献者包括 LLNL、Klara Systems、iXsystems、Delphix 等。LLNL 的核心职责是确保美国国家核威慑的安全、可靠和有效。

Sun 原意是太阳，太阳虽有西落，但同时也在地球的另一侧东升。这一隐喻恰当地概括了 ZFS 从 Sun 生态向更广泛的开源生态迁移的历史进程。

### 参考文献

- FreeBSD Foundation. The Future of ZFS in FreeBSD[EB/OL]. [2026-04-02]. <https://staging.freebsdfoundation.org/wp-content/uploads/2015/12/2011-FOSDEM-ZFS-in-Open-Source-Operating-Systems.pdf>. Oracle 闭源后的 FreeBSD 项目报告，记录关键时间节点与开发人员。
- FreeBSD Project. Comprehensive changes for vendored openzfs[EB/OL]. (2020-07-29)[2026-04-02]. <https://reviews.freebsd.org/D25872>. 切换至 OpenZFS 的代码审查过程文档。
- FreeBSD Project. 9e5787d2284e[EB/OL]. [2026-04-02]. <https://github.com/freebsd/freebsd-src/commit/9e5787d2284e187abb5b654d924394a65772e004>. GitHub 上的迁移提交记录。
- OpenZFS Project. History[EB/OL]. [2026-04-02]. <https://openzfs.org/wiki/History>. OpenZFS 项目官方历史记录。
- OpenZFS Project. Add support for FreeBSD[EB/OL]. [2026-04-02]. <https://github.com/openzfs/zfs/pull/8987>. 向 OpenZFS 提交的 FreeBSD 支持 PR。
- Dimitropoulos S. Debugging ZFS: From Illumos to Linux[EB/OL]. [2026-04-02]. <https://www.youtube.com/watch?v=uDDJnzSb-2w>. Delphix 迁移使 ZFS 开发集中于 Linux 平台。
- 红帽. 红帽与实验室携手打造全球性能最强的超级计算机[EB/OL]. [2026-04-02]. <https://www.redhat.com/zh-cn/success-stories/LLNL>. LLNL 与红帽合作及大规模使用 Linux 的介绍。
- Oracle. Oracle and Sun System Software and Operating Systems Oracle Lifetime Support Policy[EB/OL]. [2026-04-02]. <https://www.oracle.com/us/assets/lifetime-support-hardware-301321.pdf>. Oracle 产品支持周期文档，第 41 页为 Solaris。
- OpenZFS Project. Announcement[EB/OL]. (2015-04-15)[2026-04-16]. <https://www.openzfs.org/wiki/Announcement>. 记载 OpenZFS 项目于 2013 年 9 月 17 日正式成立：“Today we announce OpenZFS: the truly open source successor to the ZFS project.”
- Burt J. Oracle Completes Sun Acquisition[EB/OL]. (2010-01-27)[2026-04-16]. <https://www.eweek.com/storage/oracle-completes-sun-acquisition/>. 记载 Oracle 于 2010 年 1 月 27 日完成对 Sun 的收购。
- NERA Economic Consulting. US DOJ and DG Comp Clear Oracle's Acquisition of Sun Microsystems[EB/OL]. [2026-04-16]. <https://www.nera.com/experience/2010/us-doj-and-dg-comp-clear-oracles-acquis.html>. 记载“On 20 April 2009, Oracle and Sun announced that Oracle would acquire Sun”及“On 27 January 2010, Oracle completed its acquisition of Sun”。
- Perforce Software. Perforce Software Completes Acquisition of Delphix[EB/OL]. (2024-03-25)[2026-04-17]. <https://www.perforce.com/press-releases/perforce-completes-delphix-acquisition>. 记载 Perforce 于 2024 年 3 月 25 日完成对 Delphix 的收购。
- Jude A. The History and Future of OpenZFS[EB/OL]. (2020-03)[2026-04-17]. <http://www.allanjude.com/bsd/asiabsdcon2020_history_and_future_of_zfs.pdf>. AsiABSDCon 2020 演示文稿，明确区分 ZFS-FUSE（2008 年基于 FUSE 的用户态实现，由 LLNL 启动）与 ZFS on Linux 原生内核模块项目（2010 年由 LLNL 启动）。LLNL, Lawrence Livermore National Laboratory, 劳伦斯利弗莫尔国家实验室。

## 许可证兼容性分析

从知识产权与开源许可的角度分析，ZFS 未能直接纳入 Linux 内核树的核心原因在于许可证兼容性问题。Linux 内核采用 GPLv2（GNU General Public License version 2）许可，这是一种强 copyleft 许可证，要求衍生作品也必须以相同许可发布；而 ZFS 采用 CDDL（Common Development and Distribution License）许可，同样包含 copyleft 条款，但传染范围仅限于 CDDL 许可的代码文件。两者在 copyleft 传染范围与权利义务要求上存在实质性冲突，导致无法通过双许可证方式解决兼容性问题，因此 ZFS 未被接受进入 Linux 主内核树。

> **思考题**
>
> 阅读 GPLv2 和 CDDL 许可证的原文或译文。
>
> 1. 解释为什么二者存在冲突？
> 2. 如果仅从许可来看，自由软件基金会称任何树外模块都是不合规的 ~~当然最后要看法院的意见~~，Ubuntu ZFS 模块即是一例。那么，这是否能反证整个 Linux 内核都是以 GPLv2 授权的？

## 技术潜能与现实困境

ZFS 的性能优势与高级特性通常需要针对性的参数调优才能充分发挥，调优策略具有高度环境依赖性，需结合具体存储硬件、工作负载特征与使用场景进行个性化配置，主要调优方向包括 ARC 缓存大小、记录大小、压缩算法选择等。ZFS 不属于典型的开箱即用型文件系统。

### 文档生态现状分析

目前可用的 ZFS 文档包括：

- [Oracle Solaris 管理：ZFS 文件系统](https://docs.oracle.com/cd/E26926_01/html/E25826/index.html)：该文档撰写于 OpenZFS 项目启动之前，不包含 OpenZFS 近十五年来的开发进展。
- *FreeBSD Mastery: ZFS* 与 *FreeBSD Mastery: Advanced ZFS*
- 《FreeBSD 操作系统设计与实现（第二版）》：包含 ZFS 原理性描述

OpenZFS 项目的官方文档可作为参考来源。

> **技巧**
>
> ZFS 有多种实现，其功能差异对比表参见：Feature Flags[EB/OL]. [2026-03-26]. <https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Feature%20Flags.html>。

## 附录：ZFS 与传统文件系统挂载方式的差异

ZFS 并不使用 **/etc/fstab** 管理文件系统挂载，而是通过 `zfs mount` 命令和 ZFS 数据集的 `mountpoint` 属性进行管理。但 EFI 系统分区和 swap 分区仍然需要使用 **/etc/fstab**。

## 课后习题

1. 查找 OpenZFS 2.4.0 的源代码仓库，编译并在 FreeBSD 14.3 中安装，对比原生 ZFS 在编译时间和内存占用上的差异。
2. 选取 ZFS 从 illumos 迁移到 OpenZFS 的关键提交 9e5787d2284e，重构其最小兼容层。
3. 修改当前系统的 ZFS 功能集配置，禁用 3 个你认为不必要的特性，验证系统启动与运行状态。
4. 为 ZFS 添加国际化支持。
