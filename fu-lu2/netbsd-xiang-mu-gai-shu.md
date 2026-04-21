# NetBSD 项目概述

在前述章节介绍 FreeBSD 系统的基础上，本附录转向 BSD 家族的另一重要成员 NetBSD。NetBSD 是一个开源、可移植的类 UNIX 操作系统，作为 BSD 家族的重要成员，它起源于 4.3BSD NET/2 和 386BSD，其首个版本 0.8 发布于 1993 年 4 月 19 日（此后也引入了 4.4BSD-Lite 的变更）。

NetBSD 的学术渊源可追溯至加州大学伯克利分校（UC Berkeley）的 Berkeley Software Distribution（BSD）项目，在操作系统可移植性研究领域具有重要地位。

本节系统介绍 NetBSD 的技术特性、生态系统及实践应用。

## 技术特性与生态系统

NetBSD 的[口号](https://www.netbsd.org/about/portability.html) 是“Of course it runs NetBSD”（意为“当然可以运行 NetBSD”），这一口号集中体现了其在跨平台兼容性方面的核心技术追求。

NetBSD 支持[多种架构](https://wiki.netbsd.org/ports/)。其中，一级架构（Tier I）为官方战略重点支持的平台，二级架构（Tier II）为社区自主演进维护的平台。目前 NetBSD 支持 9 个一级架构和 49 个二级架构，其架构支持广度在同类操作系统中处于领先地位。

NetBSD 主要面向技术爱好者和开发者，对于普通用户来说具有一定的学习曲线，开发者构成了该系统的核心用户群体。

NetBSD 开发的 [pkgsrc](https://www.pkgsrc.org/) 包管理器框架也支持 macOS、Linux 等多个操作系统。pkgsrc 通过可移植的构建脚本实现跨平台软件管理，体现了 NetBSD 在可移植性软件工程方面的设计理念。

NetBSD 提供 Linux 兼容层，可运行部分 Linux 二进制程序，主要支持命令行工具和基础图形应用。

在硬件驱动方面，NetBSD 自带 i915 显卡驱动和 AMD 相关驱动，并支持 UEFI 启动和 NVMe 存储设备。

NetBSD 对 NVIDIA 显卡大致支持到 Pascal 架构（GeForce GTX 10 系列）。相关信息可参考 [nouveau / NetBSD](https://nouveau.freedesktop.org/NetBSD.html) 和 [nouveau(4) - NetBSD Manual Pages](https://man.netbsd.org/nouveau.4)（具体硬件支持列表）。

## 项目支持渠道

为 NetBSD 项目提供支持，最简单的方式是通过 [GitHub Sponsors](https://github.com/sponsors/netbsd) 进行捐赠。~~还能获得一个 GitHub 徽章 [Public Sponsor](https://github.com/orgs/community/discussions/19916)。~~

> **技巧**
>
> 支付后支付方式将绑定，如需解除绑定，可联系 GitHub 客服 [提交工单](https://support.github.com/)，通常在一个工作日内即可处理。

还可通过 [Donate using Stripe](https://www.netbsd.org/stripe.html) 进行捐赠，该方式支持中国银联、Google Pay 等多种支付方式。

## NetBSD 上的 ZFS

ZFS（Zettabyte File System，泽字节文件系统）作为一个功能强大的企业级文件系统，在 NetBSD 上也有相应的实现。以下为相关资源：

- 手册页 [zfs(8) - NetBSD Manual Pages](https://man.netbsd.org/zfs.8)，提供 ZFS 文件系统的官方命令参考
- [Finish ZFS](https://wiki.netbsd.org/projects/project/zfs/)，ZFS 移植项目进展报告
- [Google 编程之夏 2007](https://developers.google.com/open-source/gsoc/2007?hl=zh-cn)，记录了 ZFS 引入计划的早期阶段
- [Google Summer of Code zfs-port project](https://blog.netbsd.org/tnf/entry/google_summer_of_code_zfs)，ZFS 移植项目的官方技术报告
- [Root On ZFS](https://wiki.netbsd.org/root_on_zfs/)，提供 ZFS 根分区安装指南
- [NetBSD zfs Wiki](https://wiki.netbsd.org/zfs/)，NetBSD ZFS 维基，记录 NetBSD 引入 ZFS 代码的过程——最初从 OpenSolaris 移植，后续部分代码取自 FreeBSD，目前仍基于 illumos ZFS 实现（illumos 是 OpenSolaris 的后继开源项目，与 OpenZFS 存在功能差异），未集成 OpenZFS 新特性

在 NetBSD 源代码中，最早可见的 ZFS 提交为 [Import Opensolaris source code used with zfs port. Zfs code si from date](https://github.com/NetBSD/src/commit/c1cb2cd89c023350f357f813e12b526f6f71002f)。从代码提交量分析，该 ZFS 移植项目长期缺乏维护和更新。

## 参考文献

- The NetBSD Foundation. Information about NetBSD 0.8[EB/OL]. [2026-04-14]. <https://www.netbsd.org/releases/formal-0.8/>. NetBSD 项目官方发行页面。该页面记载 NetBSD 0.8 发布于 1993 年 4 月 19 日。
- The NetBSD Foundation. NetBSD Portability[EB/OL]. [2026-04-14]. <https://www.netbsd.org/about/portability.html>. NetBSD 官方可移植性说明，阐述跨平台支持策略。
- The NetBSD Foundation. Platforms Supported by NetBSD[EB/OL]. [2026-04-18]. <https://wiki.netbsd.org/ports/>. NetBSD 官方架构支持页面，当前有 9 个一级架构（Tier I）和 49 个二级架构（Tier II）。
- The NetBSD Foundation. pkgsrc -- The NetBSD Packages Collection[EB/OL]. [2026-04-14]. <https://www.pkgsrc.org/>. pkgsrc 包管理器框架官方站点，提供跨平台软件管理方案。
- The NetBSD Foundation. zfs(8) -- NetBSD Manual Pages[EB/OL]. [2026-04-14]. <https://man.netbsd.org/zfs.8>. NetBSD 上 ZFS 文件系统命令参考手册页。
- The NetBSD Foundation. NetBSD ZFS Wiki[EB/OL]. [2026-04-14]. <https://wiki.netbsd.org/zfs/>. NetBSD ZFS 维基，记录 ZFS 移植进展与使用指南。
- Nouveau Wiki. Feature Matrix[EB/OL]. [2026-04-16]. <https://nouveau.freedesktop.org/FeatureMatrix.html>. Nouveau 驱动功能支持列表，列出了各 GPU 架构的功能比较。
- Nouveau Project. CodeNames[EB/OL]. [2025-04-17]. <https://nouveau.freedesktop.org/CodeNames.html>. nouveau GPU 架构与代号映射表。
