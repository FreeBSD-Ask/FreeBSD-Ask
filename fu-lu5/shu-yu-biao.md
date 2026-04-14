# 术语表

本术语表系统收录了本书第 1—27 章所涉及的专业术语，涵盖操作系统原理、网络技术、安全机制、开源许可证、文件系统、虚拟化等多个领域。按在正文中首次出现的顺序排列。

| 术语 | 中文 | 说明 |
| :--- | :--- | :--- |
| 操作系统 | / | 管理计算机硬件与软件资源的系统软件，为计算机程序提供公共服务，是用户与计算机硬件之间的接口 |
| 分时系统 | / | 允许多个用户同时使用一台计算机的操作系统，通过将 CPU 时间划分为时间片轮流为各用户服务 |
| 内核 | / | 操作系统中常驻内存的核心部分，负责管理系统的进程、内存、设备驱动程序、文件和网络系统等 |
| 微内核 | / | 一种操作系统内核架构，仅将最基本的服务放入内核态运行，其他服务以用户态进程的形式实现 |
| 宏内核 | / | 一种操作系统内核架构，将进程管理、内存管理、文件系统、设备驱动等所有核心服务集成在内核空间中运行。又称单内核 |
| UNIX 哲学 | / | 源于 UNIX 操作系统的开发实践，是一套经过长期演化的软件工程方法论体系，传统上强调小即美、一个程序只做一件事、原型先行、可移植性先于高效率性等核心设计原则 |
| 可移植性 | / | 软件从一种硬件平台或操作系统环境转移到另一种环境时能够正常运行的难易程度 |
| 自由软件 | / | 赋予用户运行、复制、分发、研究、修改和改进软件自由的软件 |
| copyleft | 著佐权 | 通过类似 GPL 的许可证条款，对衍生作品施加版权约束，例如要求源代码公开 |
| 开源软件 | / | 源代码公开、允许用户自由使用、修改和分发的软件 |
| GNU | / | GNU's Not Unix，自由软件基金会发起的操作系统项目 |
| GPL | / | GNU General Public License，GNU 通用公共许可证，一种强 copyleft 许可证 |
| BSD 许可证 | / | 一种宽松的开源许可证，允许商业使用和闭源衍生 |
| BSD | 伯克利软件发行版 | Berkeley Software Distribution，加利福尼亚大学伯克利分校计算机系统研究小组（CSRG）对 UNIX v7 进行改进和修改的成果命名，是 UNIX 技术演化史上的重要分支 |
| 类 Unix | / | Unix-like，行为类似 UNIX 但不一定通过 SUS 认证的操作系统 |
| 发行版 | / | Distribution，基于内核及配套软件集合打包发布的完整操作系统 |
| 内核模块 | / | 可在运行时动态加载到内核中或从中卸载的代码段，无需重新编译内核即可扩展内核功能 |
| Base System | 基本系统 | 内核与用户空间（在 FreeBSD 中称为 world）的组合，即所有来自 src 源码树的组件 |
| 用户空间 | / | Userland / Userspace，操作系统中非内核部分的运行环境，应用程序在此空间中执行 |
| ABI | 应用程序二进制接口 | Application Binary Interface，应用程序与操作系统之间的二进制接口标准 |
| RELEASE | 稳定版 | 适用于生产环境的正式发布版本 |
| STABLE | / | FreeBSD 的固定开发分支，提供 ABI 稳定性保证，但仍处于开发阶段 |
| CURRENT | / | FreeBSD 的主要开发分支，对应一般项目中的 head 或 main 分支，包含最新的代码变更但可能不稳定 |
| MFC | 合并自 Head | Merge From CURRENT，FreeBSD 开发流程中将 CURRENT 分支的更改合并到稳定分支的过程 |
| Jail | / | 一种在 Chroot 基础上发展而来的操作系统级隔离技术，通过命名空间隔离、资源限制等机制实现轻量级虚拟化，是现代容器技术的重要早期实践之一 |
| ZFS | / | Zettabyte File System，一种集成了文件系统和逻辑卷管理器的先进存储系统，采用写时复制事务模型，具有强大的数据完整性保护机制、高效的数据压缩功能与可扩展存储架构 |
| OpenZFS | / | ZFS 的开源社区版本，统一了 ZFS 的开源开发 |
| bhyve | / | FreeBSD 内置的虚拟机管理程序（hypervisor） |
| DTrace | / | Dynamic Tracing，动态跟踪框架，可用于实时调试生产系统中的内核和应用程序问题 |
| Capsicum | / | 轻量级的操作系统能力和沙盒框架，用于应用程序沙盒化 |
| PF | 包过滤器 | Packet Filter，源自 OpenBSD 的防火墙软件，在 FreeBSD 中作为可选防火墙提供，支持 ALTQ 流量整形等功能 |
| Netgraph | / | FreeBSD 的网络图框架，提供内核级网络节点的图状抽象与可编程互联 |
| GEOM | / | FreeBSD 的磁盘 I/O 请求转换框架，提供了磁盘分区、加密、镜像等功能 |
| UFS | Unix 文件系统 | Unix File System，FreeBSD 的传统文件系统 |
| Port | / | FreeBSD 系统中单个软件的源代码包，包含编译和安装该软件所需的配置文件和脚本 |
| Ports | / | FreeBSD 的软件包管理系统，包含所有 Port 的集合，用于从源代码编译和安装软件 |
| Ports Collection | / | Ports 系统的完整集合，包含软件分类目录、构建工具和依赖管理机制 |
| pkg | / | FreeBSD 的二进制包管理器，用于安装、更新和管理预编译的软件包，旧称 pkgng |
| PkgBase | / | FreeBSD 项目方案，尝试使用 pkg 包管理器来实现用户空间和内核的更新 |
| freebsd-update | / | FreeBSD 基本系统更新工具，用于获取安全更新和执行系统版本升级 |
| Poudriere | / | FreeBSD 工具，通过 Jail 环境测试 port 并构建 FreeBSD 软件包镜像 |
| 安全启动 | / | Secure Boot，基于 UEFI 固件的安全机制，通过数字签名验证引导加载程序和操作系统内核的完整性 |
| Linuxism | / | 指软件过分依赖 Linux 特有特性而难以移植到其他类 Unix 操作系统的现象 |
| POLA | 最小惊讶原则 | Principle of Least Astonishment，一种设计原则，指设计必须符合用户的习惯、期望和心智能力 |
| Unix | / | 最初由 AT&T 贝尔实验室开发的操作系统，现为一种标准规范和法律商标 |
| Single UNIX Specification | 单一 UNIX 规范 | SUS，UNIX 操作系统的标准规范 |
| CDDL | 通用开发及发行许可 | Common Development and Distribution License，ZFS 采用的开源许可证，允许商业使用和修改 |
| TCP/IP | 传输控制协议/网际协议 | Transmission Control Protocol/Internet Protocol，互联网的基础协议族 |
| 校验和 | / | Checksum，通过对数据序列进行特定算法运算得到的固定长度值，用于检测数据在传输或存储过程中是否发生错误 |
| UEFI | 统一可扩展固件接口 | Unified Extensible Firmware Interface，现代计算机的固件接口标准 |
| BIOS | 基本输入输出系统 | Basic Input/Output System，传统计算机的固件接口标准 |
| GPT | 全局唯一标识分区表 | GUID Partition Table，一种磁盘分区表标准 |
| MBR | 主引导记录 | Master Boot Record，传统的磁盘分区表标准 |
| 引导加载程序 | / | Bootloader，计算机启动时执行的程序，负责初始化硬件设备并将操作系统内核加载到内存中执行 |
| 分区 | / | Partition，将物理磁盘划分为若干逻辑存储区域的操作 |
| 交换 | / | Swap，操作系统将内存中暂时不使用的页面写入磁盘交换区以释放物理内存的机制 |
| 挂载 | / | Mount，将文件系统与目录树中的某个目录关联，使其内容可被访问的操作 |
| DHCP | 动态主机配置协议 | Dynamic Host Configuration Protocol，自动为主机分配 IP 地址等网络配置的协议 |
| SSH | 安全外壳协议 | Secure Shell，用于安全远程登录的协议 |
| DNS | 域名系统 | Domain Name System，将域名映射为 IP 地址的分布式命名系统 |
| 虚拟化 | / | Virtualization，将计算机物理资源抽象为逻辑资源的技术，使多个操作系统或应用程序可在同一物理硬件上独立运行 |
| 虚拟机 | / | Virtual Machine，通过虚拟化技术模拟的完整计算机系统 |
| VirtIO | / | 虚拟化 I/O 框架，为虚拟机提供标准化的高性能 I/O 接口 |
| 串口控制台 | / | Serial Console，通过串行端口进行系统管理和调试的接口 |
| Chroot | / | Change Root，一种将进程及其子进程的根目录更改到文件系统中另一个位置的操作 |
| TTY | / | Teletypewriter，电传打字机，引申为文本终端设备 |
| 虚拟控制台 | / | Virtual Console，在物理终端上模拟的多个独立逻辑终端 |
| Shell | / | 操作系统中提供用户界面的程序，是用户与内核交互的接口，负责解释和执行用户输入的命令 |
| POSIX | / | Portable Operating System Interface，可移植操作系统接口，IEEE 和 The Open Group 制定的操作系统标准 |
| 进程 | / | Process，程序在计算机上的一次执行活动，是操作系统进行资源分配和调度的基本单位 |
| 守护进程 | / | Daemon，在后台运行的系统进程，不与任何控制终端关联，通常负责监听网络请求或执行系统维护任务 |
| 信号 | / | Signal，操作系统中用于通知进程发生事件的软件中断机制 |
| 文件系统 | / | File System，操作系统中负责管理和存取文件信息的软件机构 |
| 符号链接 | / | Symbolic Link，一种特殊类型的文件，其内容为指向另一个文件或目录的路径名。又称软链接 |
| 硬链接 | / | Hard Link，文件系统中指向同一索引节点的多个目录项，与原始文件共享相同的数据块 |
| 权限提升 | / | Privilege Escalation，获取超出授权范围的更高权限的行为 |
| SUID | 设置用户 ID | Set User ID，一种文件权限位，使执行该文件的用户临时获得文件属主的权限 |
| SGID | 设置组 ID | Set Group ID，一种文件权限位，使执行该文件的用户临时获得文件属组的权限 |
| 设备文件 | / | Device File，操作系统中代表硬件设备或虚拟设备的特殊文件 |
| procfs | / | Process File System，进程文件系统，以文件系统形式呈现内核进程信息 |
| devfs | / | Device File System，设备文件系统，自动管理 /dev 目录下的设备节点 |
| fdescfs | / | File Descriptor File System，文件描述符文件系统，提供对进程文件描述符的文件系统访问 |
| 伪终端 | / | Pseudo-Terminal，在软件中模拟的终端设备，用于远程登录和窗口系统中的终端模拟 |
| PAM | 可插拔认证模块 | Pluggable Authentication Modules，一种灵活的系统认证框架 |
| Kerberos | / | 一种网络认证协议，使用密钥分发中心（KDC）和票据机制实现安全的身份验证 |
| NIS | 网络信息服务 | Network Information Service，一种集中管理网络中用户和主机信息的系统 |
| NTP | 网络时间协议 | Network Time Protocol，用于在计算机网络中同步各节点时钟的协议 |
| syslog | / | 系统日志协议和工具，用于记录系统消息和事件 |
| OpenBSM | / | Open Basic Security Module，FreeBSD 的安全审计系统 |
| 审计 | / | Audit，对系统安全相关事件进行记录、检查和分析的过程 |
| inetd | 互联网超级服务器 | Internet Super Server，统一管理多个网络服务的守护进程 |
| IPFW | / | ipfirewall，FreeBSD 内置的防火墙系统，采用首次匹配规则 |
| IPF | / | IPFilter，一种防火墙软件，在 FreeBSD 中曾作为可选防火墙组件 |
| ALTQ | 交错队列 | Alternate Queuing，PF 防火墙的流量整形和队列管理功能 |
| 二进制包 | / | Binary Package，预编译的软件包，可直接安装而无需从源代码构建 |
| 依赖 | / | Dependency，软件之间存在的引用关系，一个软件的正常运行需要另一个软件的存在 |
| 启动环境 | / | Boot Environment，ZFS 上的可引导文件系统快照，支持系统版本回退 |
| 数据集 | / | Dataset，ZFS 中的管理单元，类似于传统文件系统中的独立分区 |
| 存储池 | / | Storage Pool / zpool，ZFS 中由一个或多个虚拟设备组成的存储空间 |
| 快照 | / | Snapshot，文件系统或存储系统在某一特定时间点的只读副本 |
| 写时复制 | / | Copy-on-Write (COW)，一种优化策略，在修改数据时先复制再写入，保证数据一致性 |
| etcupdate | / | FreeBSD 工具，用于在系统升级后合并配置文件的变更 |
| buildworld | / | FreeBSD 源代码构建过程之一，编译完整的用户空间 |
| buildkernel | / | FreeBSD 源代码构建过程之一，编译内核 |
| installworld | / | FreeBSD 源代码构建过程之一，安装编译好的用户空间 |
| releng | / | Release Engineering，FreeBSD 的发布工程分支 |
| Linux 兼容层 | / | FreeBSD 系统功能，可在 FreeBSD 上运行 Linux 二进制程序，提供应用程序兼容性 |
| Linuxulator | / | FreeBSD 内核中的 Linux 系统调用转换层，实现 Linux 二进制兼容性 |
| RISC-V | / | 开源指令集架构，FreeBSD 支持 RISC-V 架构的硬件平台 |
| kqueue | / | FreeBSD 的事件通知接口，取代了 select/poll |
| TrustedBSD | / | FreeBSD 的安全扩展项目，基于 POSIX.1e 草案 |
| W^X | 写异或执行 | Write XOR Execute，一种安全策略，内存页不可同时具有写入和执行权限 |
| PIE | 位置无关可执行程序 | Position Independent Executable，一种安全缓解技术，可执行文件可加载到任意地址 |
| ASLR | 地址空间布局随机化 | Address Space Layout Randomization，一种安全缓解技术，通过随机化进程的内存布局增加攻击难度 |
| DAC | 自主访问控制 | Discretionary Access Control，标准 Unix 安全模型，资源属主可自主决定访问权限 |
| ACL | 访问控制列表 | Access Control List，一种以对象为中心的访问控制机制，提供比传统 Unix 权限更细粒度的控制 |
| CHERI | / | Capability Hardware Enhanced RISC Instructions，基于 Capsicum 项目发展而来的 CPU 架构扩展 |
| Container | 容器 | 一种轻量级的操作系统级虚拟化技术，通过命名空间隔离和控制组等机制实现进程的隔离与资源限制 |
| NAT | 网络地址转换 | Network Address Translation，将 IP 数据包头部中的地址转换为另一个地址的技术 |
| ICMP | 互联网控制报文协议 | Internet Control Message Protocol，用于在 IP 网络中发送控制消息和错误报告的协议 |
| UDP | 用户数据报协议 | User Datagram Protocol，一种无连接的传输层协议 |
| TCP | 传输控制协议 | Transmission Control Protocol，一种面向连接的、可靠的传输层协议 |
| HTTP | 超文本传输协议 | HyperText Transfer Protocol，应用层协议，是万维网数据通信的基础 |
| HTTPS | 超文本传输安全协议 | HyperText Transfer Protocol Secure，在 HTTP 基础上通过 TLS 加密的协议 |
| 拥塞控制 | / | Congestion Control，网络中防止过多数据注入导致网络拥塞的机制 |
| Wayland | / | 一种显示服务器协议，旨在替代 X11 |
| X11 | X 窗口系统 | X Window System，一种图形用户界面的窗口系统 |
| CDE | 通用桌面环境 | Common Desktop Environment，一款经典的 UNIX 桌面环境 |
| OpenBSD | / | 一款注重安全的 BSD 操作系统 |
| NetBSD | / | 一款注重可移植性的 BSD 操作系统 |
| DragonFly BSD | / | 一款从 FreeBSD 分叉出来的 BSD 操作系统 |
| LLVM | / | Low Level Virtual Machine，一组模块化和可重用的编译器和工具链技术 |
| Clang | / | LLVM 项目的 C/C++ 语言前端和工具基础设施 |
| NFS | 网络文件系统 | Network File System，一种分布式文件系统协议 |
| SMB | 服务器消息块 | Server Message Block，一种用于文件共享的协议 |
| 交叉编译 | / | Cross-compilation，在一种平台上编译生成另一种平台上可执行代码的编译过程 |
| 设备树 | / | Device Tree，描述硬件设备信息的数据结构，用于嵌入式系统的硬件发现 |
| 单板计算机 | / | Single-Board Computer，集成在单一电路板上的完整计算机 |
| 固件 | / | Firmware，嵌入在硬件设备中的软件，控制设备的基本操作 |
| 运行级别 | / | Runlevel，SysVinit 系统中定义系统运行状态的级别 |
| 伪静态 | / | URL Rewriting，通过服务器端规则将动态 URL 映射为静态 URL 的技术 |
| 反向代理 | / | Reverse Proxy，代理服务器接收客户端请求后转发给后端服务器，再将响应返回客户端 |
| 时序数据库 | / | Time Series Database，专门用于存储和查询时间序列数据的数据库 |
| ORDBMS | 对象关系型数据库管理系统 | Object-Relational Database Management System，支持对象、类和继承等特性的关系型数据库 |
| NoSQL | / | Not Only SQL，不严格遵循关系模型的数据库管理系统 |
| 文档型数据库 | / | Document-oriented Database，以文档为单位存储和检索数据的数据库 |
| SCRAM-SHA-256 | / | Salted Challenge Response Authentication Mechanism，一种基于 SHA-256 的认证机制 |
| ACID | / | Atomicity, Consistency, Isolation, Durability，数据库事务的四个基本特性：原子性、一致性、隔离性、持久性 |
| SSL/TLS | 安全套接层/传输层安全 | Secure Sockets Layer / Transport Layer Security，为网络通信提供安全及数据完整性的协议 |
| FastCGI | / | Fast Common Gateway Interface，一种改进的 CGI 协议，通过持久进程处理请求以提高性能 |
| JIT 编译器 | 即时编译器 | Just-In-Time Compiler，在程序运行时将字节码编译为机器码的编译器 |
| Java Servlet | / | Java 平台上用于处理 HTTP 请求的服务器端组件 |
| SPICE | / | Simple Protocol for Independent Computing Environments，一种远程显示协议 |
| VNC | 虚拟网络计算 | Virtual Network Computing，一种远程桌面协议 |
| RDP | 远程桌面协议 | Remote Desktop Protocol，Microsoft 开发的远程桌面协议 |
| FUSE | 用户空间文件系统 | Filesystem in Userspace，允许非特权用户在用户空间创建文件系统的框架 |
| autofs | / | Automatic File System，自动挂载文件系统框架 |
| fsck | / | File System Consistency Check，文件系统一致性检查和修复工具 |
| GELI | / | FreeBSD 的磁盘加密框架 |
| sysctl | / | System Control，FreeBSD 内核运行时参数的读取和设置接口 |
| securelevel | / | 安全级别，FreeBSD 内核的安全等级机制，级别越高限制越严格 |
| rctl | / | Resource Control，FreeBSD 的资源限制工具 |
| mac_bsdextended | / | FreeBSD 的强制访问控制（MAC）策略模块 |
| devd | / | Device Daemon，FreeBSD 的设备状态守护进程，响应硬件事件 |
| powerd | / | Power Daemon，FreeBSD 的电源管理守护进程 |
| cron | / | Command Run On，Unix 系统的定时任务执行守护进程 |
| DMA | / | DragonFly Mail Agent，FreeBSD 默认的邮件传输代理 |
| mtree | / | FreeBSD 的目录树规范和验证工具 |
| authpf | / | Authenticating Gateway Shell，PF 防火墙的认证网关 Shell |
| Unbound | / | 一种验证型递归 DNS 服务器 |
| Kyua | / | FreeBSD 的自动化测试框架 |
