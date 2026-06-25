# 3.5 DragonFly BSD 概论

DragonFly BSD（蜻蜓 BSD）是一种基于 FreeBSD 4.8 衍生而来的类 UNIX 系统。该项目由 Matthew Dillon（20 世纪 80 年代末至 90 年代初的 Amiga 开发者，1994 至 2003 年间的 FreeBSD 开发者）于 2003 年 6 月启动，并于 2003 年 7 月正式发布于 [FreeBSD 邮件列表](https://lists.freebsd.org/pipermail/freebsd-current/2003-July/006889.html)。

Dillon 启动 DragonFly BSD 项目，是因为他对 FreeBSD 5 采用的 SMP（对称多处理）并行计算架构有不同判断。SMP 是指多个处理器共享同一内存空间的架构设计，他认为该设计可能引入不必要的性能开销。这一技术分歧导致与 FreeBSD 核心开发团队的讨论，最终促成了独立项目。尽管存在技术路径差异，DragonFly BSD 与 FreeBSD 项目在错误修复和驱动程序更新等领域仍保持协作关系。

DragonFly BSD 继承了 FreeBSD 4 的技术路线，同时在多个关键系统层面做了创新设计，包括轻量级内核线程实现机制和 HAMMER/HAMMER2 文件系统等核心组件。DragonFly BSD 的部分设计理念受到了 AmigaOS 架构的启发。

截至 2026 年 6 月，DragonFly BSD 的最新版本为 6.4.2（2025 年 5 月发布）。6.4 系列新增了对第二类管理程序（Type-2 Hypervisor）的 NVMM 支持、amdgpu 显卡驱动，以及远程挂载 HAMMER2 卷的实验性功能。

从硬件支持现状来看，DragonFly BSD 自带 i915 显卡驱动，架构仅支持 x86-64 平台，未提供 Linux 兼容层。其 DPorts 软件包系统与 FreeBSD Ports 基本保持兼容，当前版本基于 FreeBSD Ports 2024Q3 分支，正在向 2025Q2 推进。需注意 DragonFly BSD 的驱动支持相对滞后，特别是显卡驱动的更新节奏相对较慢。

捐赠 DragonFly BSD：[Sponsoring projects](https://www.dragonflybsd.org/donations/)，目前仅支持国际 PayPal。

> DragonFly BSD 的文档相对陈旧，但这并不反映其实际开发进度。DragonFly BSD 的开发仍然活跃，不应因官方文档陈旧而放弃使用。

### 附录：其他专注于安全的 BSD 系统

#### HardenedBSD

专注于安全的 BSD 操作系统不仅有 OpenBSD，还可以尝试 2014 年从 FreeBSD 复刻而来的[HardenedBSD](https://hardenedbsd.org/)。

其官网称“我们的主要目标是对 Grsecurity 补丁集（增强 Linux 内核安全的内核补丁集）中已公开文档的部分，进行净室开发。”

> Grsecurity 为 Linux 内核提供的补丁集是垃圾。
>
> ——Linus Torvalds（Linux 创始人）

#### CheriBSD

[CheriBSD 官网](https://www.cheribsd.org/)

CheriBSD 基于 FreeBSD 实现了 Capability（能力式指针），提供内存保护和软件隔离功能。CheriBSD 主要面向 ARM 和 RISC-V 架构，由国际斯坦福研究所（SRI International）和英国剑桥大学（University of Cambridge）联合开发。

#### FuguIta

[FuguIta 官网](https://fuguita.org/)

FuguIta 是一种基于 OpenBSD 开发的 Live 系统，同时支持部分型号的树莓派（树莓派 3/4/5, arm64 架构）。
