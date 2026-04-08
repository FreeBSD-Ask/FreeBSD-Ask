# 术语表

本术语表收录了本书所涉及的专业术语，涵盖操作系统、网络技术、开源社区等多个领域，为读者提供参考。

| 术语 | 中文 | 说明 |
| :--- | :--- | :--- |
| Berkeley Software Distribution, BSD | 伯克利软件发行版 | 伯克利软件发行版，是加利福尼亚大学伯克利分校的计算机系统研究小组（CSRG）对其针对 AT&T 的 UNIX v7 进行改进和修改的成果命名，是 UNIX 技术演化史上的重要分支。从技术演化角度，BSD 构成了现代类 Unix 操作系统的重要技术谱系之一，FreeBSD 正是 CSRG 这一工作的直接延续与发展。 |
| Port | / | FreeBSD 系统中单个软件的源代码包，包含编译和安装该软件所需的配置文件和脚本。 |
| Ports | / | FreeBSD 的软件包管理系统，包含所有 Port 的集合，用于从源代码编译和安装软件。 |
| Ports Collection | / | Ports 系统的完整集合，包含软件分类目录、构建工具和依赖管理机制。 |
| Jail | / | 一种在 Chroot 基础上发展而来的操作系统级隔离技术，通过命名空间隔离、资源限制等机制实现轻量级虚拟化，是现代容器技术的重要早期实践之一，为后续容器技术的发展奠定了技术基础。 |
| copyleft | 著佐权 | Copyleft 指通过类似 GPL 的许可证条款，对衍生作品施加版权约束，例如要求源代码公开。 |
| Base System | 基本系统 | 内核与用户空间（在 FreeBSD 中称为 world）的组合，即所有来自 src 源码树的组件。 |
| CURRENT | / | FreeBSD 的主要开发分支，对应一般项目中的 head 或 main 分支，包含最新的代码变更但可能不稳定。 |
| MFC（Merge From Head） | 合并自 Head | FreeBSD 开发流程，将 CURRENT 或 main 分支中的更改合并到稳定分支的过程。 |
| XX.0-STABLE | / | FreeBSD 的固定开发分支，提供应用程序二进制接口（ABI）稳定性保证，但仍处于开发阶段。 |
| RELEASE | 稳定版 | 适用于生产环境的正式发布版本。 |
| ABI | 应用程序二进制接口 | Application Binary Interface，应用程序与操作系统之间的二进制接口标准。 |
| Unix | / | 最初由 AT&T 贝尔实验室开发的操作系统，现为一种标准规范和法律商标。 |
| ZFS | / | Zettabyte File System，一种集成了文件系统和逻辑卷管理器的先进存储系统，采用 copy-on-write（写时复制）事务模型，具有强大的数据完整性保护机制、高效的数据压缩功能与可扩展存储架构，是现代存储技术的重要创新。 |
| OpenZFS | / | ZFS 的开源社区版本，统一了 ZFS 的开源开发。 |
| CDDL | 通用开发及发行许可 | Common Development and Distribution License，ZFS 采用的开源许可证，允许商业使用和修改。 |
| PF | 包过滤器 | Packet Filter，源自 OpenBSD 的防火墙软件，在 FreeBSD 中作为可选防火墙提供，支持 ALTQ 流量整形等功能。 |
| IPFW | / | ipfirewall，FreeBSD 内置的防火墙系统，采用首次匹配规则，提供基本的包过滤功能。 |
| IPF | / | IPFilter，一种防火墙软件，在 FreeBSD 历史版本中曾作为可选防火墙组件。 |
| pkg | / | FreeBSD 的二进制包管理器，用于安装、更新和管理预编译的软件包，旧称 pkgng。 |
| PkgBase | / | FreeBSD 项目方案，尝试使用 pkg 包管理器来实现用户空间和内核的更新。 |
| Poudriere | / | FreeBSD 工具，通过 jail 环境测试 port 并构建 FreeBSD 软件包镜像。 |
| freebsd-update | / | FreeBSD 基本系统更新工具，用于获取安全更新和执行系统版本升级。 |
| Chroot | / | Change Root，一种将进程及其子进程的根目录更改到文件系统中另一个位置的操作。 |
| bhyve | / | FreeBSD 内置的虚拟机管理程序。 |
| kqueue | / | FreeBSD 的事件通知接口，取代了 select/poll。 |
| DTrace | / | 动态跟踪框架，可用于实时调试生产系统中的内核和应用程序问题。 |
| Capsicum | / | 轻量级的操作系统能力和沙盒框架，用于应用程序沙盒化。 |
| GEOM | / | FreeBSD 的磁盘 I/O 请求转换框架，提供了磁盘分区、加密、镜像等功能。 |
| UFS | Unix 文件系统 | Unix File System，FreeBSD 的传统文件系统。 |
| GPT | 全局唯一标识分区表 | GUID Partition Table，一种磁盘分区表标准。 |
| MBR | 主引导记录 | Master Boot Record，传统的磁盘分区表。 |
| UEFI | 统一可扩展固件接口 | Unified Extensible Firmware Interface，现代计算机的引导标准。 |
| BIOS | 基本输入输出系统 | Basic Input/Output System，传统计算机的引导标准。 |
| Wayland | / | 一种显示服务器协议，旨在替代 X11。 |
| X11 | X 窗口系统 | X Window System，一种图形用户界面的窗口系统。 |
| CDE | 通用桌面环境 | Common Desktop Environment，一款经典的 UNIX 桌面环境。 |
| OpenBSD | / | 一款注重安全的 BSD 操作系统。 |
| NetBSD | / | 一款注重可移植性的 BSD 操作系统。 |
| DragonFly BSD | / | 一款从 FreeBSD 分叉出来的 BSD 操作系统。 |
| GNU | / | GNU's Not Unix，自由软件基金会发起的操作系统项目。 |
| GPL | / | GNU General Public License，GNU 通用公共许可证，一种强 copyleft 许可证。 |
| BSD 许可证 | / | 一种宽松的开源许可证，允许商业使用和闭源衍生。 |
| LLVM | / | Low Level Virtual Machine，一组模块化和可重用的编译器和工具链技术。 |
| Clang | / | LLVM 项目的 C 语言前端和工具基础设施。 |
| NFS | / | Network File System，网络文件系统。 |
| SMB | / | Server Message Block，一种用于文件共享的协议。 |
| Samba | / | 实现 SMB 协议的开源软件，用于文件共享。 |
| Apache | / | 一种流行的 Web 服务器软件。 |
| Nginx | / | 一种高性能的 Web 服务器和反向代理软件。 |
| PHP | / | PHP: Hypertext Preprocessor，一种广泛使用的服务器端脚本语言。 |
| PostgreSQL | / | 一种功能强大的开源关系型数据库管理系统。 |
| MySQL | / | 一种流行的开源关系型数据库管理系统。 |
| MongoDB | / | 一种流行的 NoSQL 数据库。 |
| Nextcloud | / | 一种开源的云存储和协作平台。 |
| Zabbix | / | 一种开源的企业级监控系统。 |
| Prometheus | / | 一种开源的系统监控和警报工具。 |
| Grafana | / | 一种开源的数据可视化和监控平台。 |
| Tomcat | / | Apache 软件基金会的 Java Servlet 容器。 |
| Caddy | / | 一种支持自动 HTTPS 的 Web 服务器。 |
| Fail2Ban | / | 一种入侵防御软件，用于保护服务器免受暴力攻击。 |
| TCP BBR | / | TCP Bottleneck Bandwidth and RTT，一种 TCP 拥塞控制算法。 |
| Wi-Fi | 无线局域网技术 | 一种无线局域网技术，Wi-Fi 是 Wi-Fi 联盟的注册商标，无正式全称。 |
| USB RNDIS | / | USB Remote Network Driver Interface Specification，USB 网络共享技术。 |
| Linux 兼容层 | / | FreeBSD 系统功能，可在 FreeBSD 上运行 Linux 二进制程序，提供应用程序兼容性。 |
| RISC-V | / | 开源指令集架构，FreeBSD 支持 RISC-V 架构的硬件平台。 |
| Beastie | / | BSD 操作系统家族的吉祥物，形象为红色小恶魔。 |
| FreeBSD 基金会 | / | 支持 FreeBSD 项目的非营利机构，位于美国科罗拉多州博尔德县，负责资金筹集和项目支持。 |
| FreeBSD 核心小组 | / | FreeBSD 项目的最高管理机构，由 9 名成员组成，负责项目战略决策和方向指导。 |
| 提交者 | / | FreeBSD 项目中有权限直接向代码仓库提交更改的开发者。 |
| CSRG | / | Computer Systems Research Group，加州大学伯克利分校的计算机系统研究小组，主要活动时间为 1980-1992 年。 |
| Multics | / | 多路复用信息和计算服务，一个早期的操作系统项目。 |
| OpenSolaris | / | Sun Microsystems 开源的 Solaris 操作系统版本，ZFS 和 DTrace 等技术的开源实现基础。 |
| illumos | / | OpenSolaris 社区分支，在 Oracle 收购 Sun 后由社区维护的开源操作系统项目。 |
| Oracle Solaris | / | Oracle 公司维护的 Solaris 操作系统商业版本，基于早期 OpenSolaris 代码。 |
| LLNL | 美国劳伦斯利弗莫尔国家实验室 | Lawrence Livermore National Laboratory，OpenZFS 项目的主要贡献机构之一。 |
| ALTQ | 交错队列 | Alternate Queuing，PF 防火墙的流量整形和队列管理功能。 |
| NAT | 网络地址转换 | Network Address Translation。 |
| ICMP | 互联网控制报文协议 | Internet Control Message Protocol。 |
| UDP | 用户数据报协议 | User Datagram Protocol。 |
| TCP | 传输控制协议 | Transmission Control Protocol。 |
| DNS | 域名系统 | Domain Name System。 |
| HTTP | 超文本传输协议 | HyperText Transfer Protocol。 |
| HTTPS | 安全超文本传输协议 | HyperText Transfer Protocol Secure。 |
| SSH | 安全外壳协议 | Secure Shell，用于安全远程登录。 |
| SSHD | SSH 守护进程 | SSH Daemon。 |
| PR | / | Pull Request，拉取请求，在 Git 中提交代码变更的方式；在 FreeBSD 中亦指 Bug 报告。 |
| CVS | / | Concurrent Versions System，并发版本系统，FreeBSD 早期使用的版本控制工具。 |
| SVN | / | Subversion，FreeBSD 中期使用的版本控制工具。 |
| CIS | 互联网安全中心 | Center for Internet Security，提供安全基准。 |
| SBOM | 软件物料清单 | Software Bill of Materials。 |
| SSDF | 安全软件开发框架 | Secure Software Development Framework。 |
| NIST | 美国国家标准及技术研究所 | National Institute of Standards and Technology。 |
| W^X | 写异或执行 | Write XOR Execute，一种安全策略。 |
| PIE | 位置无关可执行文件 | Position Independent Executable，一种安全缓解技术。 |
| ASLR | 地址空间布局随机化 | Address Space Layout Randomization，一种安全缓解技术。 |
| DAC | 自主访问控制 | Discretionary Access Control，标准 Unix 安全模型。 |
| ACL | 访问控制列表 | Access Control List。 |
| TrustedBSD | / | FreeBSD 的安全扩展项目，基于 POSIX.1e 草案。 |
| gop | / | Graphics Output Protocol，图形输出协议，用于设置 UEFI 引导分辨率。 |
| VESA | / | Video Electronics Standards Association，视频电子标准协会，用于设置 BIOS 引导分辨率。 |
| device.hints | / | 设备资源提示文件，用于控制驱动程序的内核变量。 |
| motd | / | Message of the Day，今日信息，登录后显示的信息。 |
| fstab | / | 文件系统表，用于配置文件系统挂载。 |
| hosts | / | 本地 IP 域名映射表，优先于 DNS。 |
| ttys | / | 创建 TTY 的规则文件。 |
| csh | / | C Shell，一种 shell。 |
| sh | / | Bourne Shell，FreeBSD 的默认 shell。 |
| tcsh | / | Tenex C Shell，csh 的增强版本。 |
| bash | / | Bourne Again Shell，GNU 的 shell。 |
| zsh | / | Z Shell，一种功能强大的 shell。 |
| vi | / | 一种经典的文本编辑器。 |
| Vim | / | Vi IMproved，vi 的增强版本。 |
| Emacs | / | 一种功能强大的文本编辑器。 |
| Neovim | / | Vim 的重构版本。 |
| gcc | / | GNU Compiler Collection，GNU 编译器集合。 |
| gdb | / | GNU Debugger，GNU 调试器。 |
| IDA Pro | / | Interactive Disassembler Professional，一种专业的反汇编和调试工具。 |
| Java | / | 一种编程语言和计算平台。 |
| Python | / | 一种高级编程语言。 |
| Rust | / | 一种系统编程语言，注重安全和性能。 |
| Go | / | Golang，Google 开发的编程语言。 |
| Qt | / | 一种跨平台的应用程序开发框架。 |
| Node.js | / | 一个基于 Chrome V8 引擎的 JavaScript 运行时。 |
| Code Server | / | 在浏览器中运行 VS Code 的工具。 |
| Clangd | / | Clang 的语言服务器，提供代码补全等功能。 |
| Ren'Py | / | 一种视觉小说引擎。 |
| Godot | / | 一种开源的游戏引擎。 |
| Minecraft | / | 一种沙盒游戏。 |
| Steam | / | Valve 开发的游戏平台。 |
| Fcitx | / | 一种输入法框架。 |
| IBus | / | Intelligent Input Bus，一种输入法框架。 |
| Chromium | / | 一种开源的 Web 浏览器。 |
| Wine | / | 一种在类 Unix 系统上运行 Windows 程序的兼容层。 |
| Termius | / | 一种 SSH 客户端。 |
| MobaXterm | / | 一种 Windows 下的 SSH 客户端和 X11 服务器。 |
| AnyDesk | / | 一种远程桌面软件。 |
| VirtualBox | / | 一种虚拟机软件。 |
| VMware | / | 一种虚拟机软件。 |
| Hyper-V | / | Microsoft 的虚拟机技术。 |
| Parallels Desktop | / | 一种 macOS 下的虚拟机软件。 |
| UTM | / | 一种 macOS 和 iOS 下的虚拟机软件。 |
| KVM | / | Kernel-based Virtual Machine，Linux 的内核虚拟机。 |
| QEMU | / | 一种开源的机器模拟器和虚拟机。 |
| Ventoy | / | 一种多合一启动盘制作工具。 |
| rEFInd | / | 一种 UEFI 引导管理器。 |
| Radxa | 瑞莎 | 一家中国的半导体公司，开发 Radxa 系列开发板。 |
| Raspberry Pi | 树莓派 | 一种流行的单板计算机。 |
| VisionFive 2 | 昉·星光 2 | 一种 RISC-V 开发板。 |
| TwinCAT/BSD | / | 倍福自动化控制系统的操作系统。 |
| GhostBSD | / | 一种基于 FreeBSD 的桌面发行版。 |
| MidnightBSD | / | 一种基于 FreeBSD 的操作系统。 |
| NomadBSD | / | 一种基于 FreeBSD 的 Live USB 发行版。 |
| HelloSystem | / | 一种基于 FreeBSD 的桌面操作系统，设计风格类似 macOS。 |
| MfsBSD | / | 一种基于 FreeBSD 的内存文件系统发行版。 |
| FreeBSD 中文社区 | / | FreeBSD 的中文用户和开发者社区。 |
| FreeBSD 日 | / | 每年 6 月 19 日，FreeBSD 基金会和社区庆祝 FreeBSD 生日的日子。 |
| EuroBSDCon | / | 欧洲 BSD 大会。 |
| AsiaBSDCon | / | 亚洲 BSD 大会。 |
| BSDCan | / | 加拿大 BSD 大会。 |
| FreeBSDCon | / | FreeBSD 大会，首届于 1999 年举行。 |
| FreeBSD 期刊 | / | FreeBSD 社区的期刊，跟进 FreeBSD 最新发布版本和新进展。 |
| Google Summer of Code | 谷歌编程之夏 | 一个为学生提供参与开源项目机会的项目。 |
| FreeBSD Handbook | / | FreeBSD 官方文档，提供详细的使用指南和参考。 |
| FreshPorts | / | 一个 FreeBSD Ports 的搜索引擎和信息网站。 |
| OpenBSM | / | Open Basic Security Module，FreeBSD 的安全审计系统。 |
| CHERI | / | Capability Hardware Enhanced RISC Instructions，基于 Capsicum 项目发展而来的 CPU 架构扩展。 |
| Linuxism | Linux 主义/Linux 歧视 | 指软件过分依赖 Linux 特有特性而难以移植到其他类 Unix 操作系统的现象。该术语有双重含义：既可描述技术上的 Linux 特性依赖，也可指对非 Linux 系统的歧视态度。 |
| POLA | 最小惊讶原则 | Principle of Least Astonishment，一种设计原则，指设计必须符合用户的习惯、期望和心智能力。 |
| 大教堂与集市 | / | 一种软件开发模型的比喻，大教堂指集中式开发，市集指分布式开发。 |
| KISS 原则 | / | Keep It Simple, Stupid，一种设计原则，强调保持简单。 |
| UNIX 哲学 | / | 源于 UNIX 操作系统的开发实践，是一套经过长期演化的软件工程方法论体系，传统上强调小即美、一个程序只做一件事、原型先行、可移植性先于高效率性等核心设计原则，对现代软件设计与系统架构产生了深远的范式性影响。 |
| Ship of Theseus | 忒修斯之船 | 哲学思想实验，探讨物体在部件逐步更换后是否保持同一性的问题。 |
| 谷堆悖论 | / | 连锁悖论，探讨模糊概念的边界问题，如多少粒谷子能构成一个谷堆。 |
| 秃头悖论 | / | 连锁悖论，探讨渐变过程中的分类问题，如掉多少根头发算秃头。 |
| 跨时间的同一性 | / | 哲学概念，探讨事物随时间变化如何保持自身同一性的问题。 |
| Single UNIX Specification | 单一 UNIX 规范 | SUS，UNIX 操作系统的标准规范。 |
| The Open Group | 开放组织 | 负责管理 UNIX 商标和单一 UNIX 规范的组织。 |
| 501(c)(3) | / | 美国税法中的一种非营利组织类型，可接受免税捐赠。 |
| Sun Microsystems | / | 太阳计算机系统公司，ZFS 和 Solaris 的原开发商，2009 年被 Oracle 收购。 |
| Oracle | 甲骨文公司 | 收购了 Sun Microsystems。 |
| AT&T | 美国电话电报公司 | UNIX 的原开发商。 |
| Bell Labs | 贝尔实验室 | AT&T 的研究实验室，UNIX 的诞生地。 |
| University of California, Berkeley | 加州大学伯克利分校 | BSD 的诞生地。 |
| Bill Joy | / | Sun Microsystems 的创始人之一，也是 BSD Unix 的关键开发者。 |
| Ken Thompson | / | UNIX 的主要开发者之一。 |
| Dennis Ritchie | / | UNIX 的主要开发者之一，C 语言的发明者。 |
| Marshall Kirk McKusick | / | FreeBSD 的重要开发者，《FreeBSD 操作系统设计与实现》的作者之一。 |
| Jordan Hubbard | / | FreeBSD 的创始人之一，Ports 系统的创建者。 |
| Justin Gibbs | / | FreeBSD 基金会的创始人之一。 |
| Deb Goodkin | / | FreeBSD 基金会的首位执行董事。 |
| Jan Koum | / | WhatsApp 的原 CEO 及创始人，FreeBSD 的重要捐赠者。 |
| Eric S. Raymond | / | 开源运动的重要人物，《大教堂与集市》和《UNIX 编程艺术》的作者。 |
| Henry Spencer | / | UNIX 社区的重要人物，有著名言论：“那些不懂 Unix 的人注定要再造一个四不像式 Unix”。 |
| Linus Torvalds | / | Linux 内核的创始人。 |
| Richard M. Stallman | / | 自由软件基金会的创始人，GNU 项目的发起者。 |
| Theo de Raadt | / | OpenBSD 的创始人。 |
| Matt Dillon | / | DragonFly BSD 的创始人。 |
| Red Hat | 红帽公司 | 一家重要的 Linux 发行商，控制着许多主流 Linux 项目。 |
| Netflix | 奈飞公司 | 几乎所有网络活动都使用 FreeBSD 设备进行。 |
| Sony | 索尼公司 | PlayStation 系列游戏机使用基于 FreeBSD 的操作系统。 |
| Dell EMC | 戴尔 EMC | Isilon NAS 存储设备使用基于 FreeBSD 的 OneFS 操作系统。 |
| Beckhoff | 倍福公司 | TwinCAT/BSD 自动化控制系统使用 FreeBSD。 |
| Container | 容器 | 一种轻量级的虚拟化技术。 |
| CI/CD | / | Continuous Integration/Continuous Deployment，持续集成/持续部署。 |
| GitHub Actions | / | GitHub 的持续集成和持续部署服务。 |
| GitHub | / | 一个代码托管平台。 |
| Git | / | 一种分布式版本控制系统。 |
| DevSummit | / | FreeBSD 的开发者峰会。 |
