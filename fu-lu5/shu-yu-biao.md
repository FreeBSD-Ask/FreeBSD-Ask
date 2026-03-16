# 术语表

|术语 | 中文 | 说明|
|:---|:---|:---|
|Berkeley Software Distribution, BSD |伯克利软件套件|直译应为“伯克利软件发行版”，这是加利福尼亚大学伯克利分校的计算机系统研究小组（CSRG）对其针对 AT&T 的 UNIX v7 进行改进和修改的成果命名。FreeBSD 正是 CSRG 这一工作的延续 |
|Port|/|单个软件的移植|
|Ports|/|所有 Port 的集合|
|Ports Collection|/|Ports 技术体系的整体|
|Jail|/|一种在 Chroot 基础上发展而来的操作系统级隔离技术|
|copyleft|著佐权|copyleft 指通过类似 GPL 的许可证条款，对衍生作品施加版权约束，例如要求源代码公开|
|Base System|基本系统 | 内核与用户空间（在 FreeBSD 中称为 world）的组合，即所有来自 src 源码树的组件|
|CURRENT|/|对应一般项目中的 head 或 main 开发分支|
|MFC（Merge From Head）| 合并自 main|将 CURRENT 或 main 分支中的更改向稳定分支回溯|
|XX.0-STABLE|/|仅表示 ABI 稳定性保证，仍属于开发中的不稳定分支|
|RELEASE|稳定版|适用于生产环境的正式发布版本|
|ABI|应用程序二进制接口|Application Binary Interface，应用程序与操作系统之间的二进制接口标准|
|Unix|/|最初由 AT&T 贝尔实验室开发的操作系统，现为一种标准规范和法律商标|
|UNIX 哲学|/|源于 UNIX 操作系统的开发实践，强调大道至简、小即美、一个程序只做一件事等原则|
|ZFS|/|Zettabyte File System，一款集成了文件系统和逻辑卷管理器的系统，具有强大的数据完整性保护与高效的数据压缩功能|
|OpenZFS|/|ZFS 的开源社区版本，统一了 ZFS 的开源开发|
|CDDL|通用开发及发行许可|Common Development and Distribution License，ZFS 采用的开源许可证|
|PF|包过滤器|Packet Filter，源自 OpenBSD 的防火墙，提供了丰富功能，包括 ALTQ 等|
|IPFW|/|ipfirewall，FreeBSD 内置的防火墙，采用首次匹配规则|
|IPF|/|IPFilter，一款防火墙软件|
|pkg|/|FreeBSD 的二进制包管理器，旧称 pkgng|
|PkgBase|/|FreeBSD 项目试图使用 pkg 来实现用户空间和内核更新的方案|
|Poudriere|/|通过 jail 测试 port，并构建 FreeBSD 镜像的工具|
|freebsd-update|/|FreeBSD 基本系统更新工具，用于获取安全更新和系统升级|
|rc.conf|/|FreeBSD 系统主要配置文件，用于设置系统服务和参数|
|loader.conf|/|系统启动配置文件，位于 /boot/loader.conf，用于指定要启动的内核、传递给内核的参数以及需要加载的附加模块|
|Chroot|/|Change Root，一种将进程及其子进程的根目录更改到文件系统中另一个位置的操作|
|bhyve|/|FreeBSD 内置的虚拟机管理程序|
|kqueue|/|FreeBSD 的事件通知接口，取代了 select/poll|
|DTrace|/|动态跟踪框架，可用于实时调试生产系统中的内核和应用程序问题|
|Capsicum|/|轻量级的操作系统能力和沙盒框架，用于应用程序沙盒化|
|GEOM|/|FreeBSD 的磁盘 I/O 请求转换框架，提供了磁盘分区、加密、镜像等功能|
|UFS|/|Unix File System，FreeBSD 的传统文件系统|
|GPT|/|GUID Partition Table，全局唯一标识分区表，一种磁盘分区表标准|
|MBR|/|Master Boot Record，主引导记录，传统的磁盘分区表|
|UEFI|/|Unified Extensible Firmware Interface，统一可扩展固件接口，现代计算机的引导标准|
|BIOS|/|Basic Input/Output System，基本输入输出系统，传统计算机的引导标准|
|Wayland|/|一种显示服务器协议，旨在替代 X11|
|X11|/|X Window System，一种图形用户界面的窗口系统|
|KDE|/|K Desktop Environment，一款流行的桌面环境|
|GNOME|/|GNU Network Object Model Environment，一款流行的桌面环境|
|Xfce|/|一款轻量级桌面环境|
|MATE|/|GNOME 2 的复刻版本，一款桌面环境|
|Cinnamon|/|一款桌面环境，由 Linux Mint 开发|
|LXQt|/|一款轻量级桌面环境|
|Hyprland|/|一款 Wayland 合成器，提供动态窗口管理|
|i3wm|/|一款平铺式窗口管理器|
|bspwm|/|一款平铺式窗口管理器|
|IceWM|/|一款轻量级窗口管理器|
|CDE|/|Common Desktop Environment，一款经典的 UNIX 桌面环境|
|LXDE|/|Lightweight X11 Desktop Environment，一款轻量级桌面环境|
|OpenBSD|/|一款注重安全的 BSD 操作系统|
|NetBSD|/|一款注重可移植性的 BSD 操作系统|
|DragonFly BSD|/|一款从 FreeBSD 分叉出来的 BSD 操作系统|
|GNU|/|GNU's Not Unix，自由软件基金会发起的操作系统项目|
|GPL|/|GNU General Public License，GNU 通用公共许可证，一种强 copyleft 许可证|
|BSD 许可证|/|一种宽松的开源许可证，允许商业使用和闭源衍生|
|LLVM|/|Low Level Virtual Machine，一组模块化和可重用的编译器和工具链技术|
|Clang|/|LLVM 项目的 C 语言前端和工具基础设施|
|KDE Plasma|/|KDE 桌面环境的最新版本|
|GDM|/|GNOME Display Manager，GNOME 桌面的显示管理器|
|SDDM|/|Simple Desktop Display Manager，一款简单的显示管理器|
|Sudo|/|一种特权提升工具，允许用户以其他用户的身份执行命令|
|Doas|/|OpenBSD 的特权提升工具，也可用于 FreeBSD|
|wheel|/|FreeBSD 中用于管理超级用户权限的用户组|
|devfs|/|设备文件系统，用于管理 /dev 目录下的设备节点|
|procfs|/|进程文件系统，现代 FreeBSD 默认不使用|
|fdescfs|/|文件描述符文件系统，用于访问当前进程的文件描述符|
|tmpfs|/|临时文件系统，将文件存储在内存中|
|NFS|/|Network File System，网络文件系统|
|SMB|/|Server Message Block，一种用于文件共享的协议|
|Samba|/|实现 SMB 协议的开源软件，用于文件共享|
|Apache|/|一款流行的 Web 服务器软件|
|Nginx|/|一款高性能的 Web 服务器和反向代理软件|
|PHP|/|PHP: Hypertext Preprocessor，一种广泛使用的服务器端脚本语言|
|PostgreSQL|/|一款功能强大的开源关系型数据库管理系统|
|MySQL|/|一款流行的开源关系型数据库管理系统|
|MongoDB|/|一款流行的 NoSQL 数据库|
|Nextcloud|/|一款开源的云存储和协作平台|
|Zabbix|/|一款开源的企业级监控系统|
|Prometheus|/|一款开源的系统监控和警报工具|
|Grafana|/|一款开源的数据可视化和监控平台|
|Tomcat|/|Apache 软件基金会的 Java Servlet 容器|
|Caddy|/|一款支持自动 HTTPS 的 Web 服务器|
|OnlyOffice|/|一款开源的办公套件|
|AList|/|一款支持多种存储的文件列表程序|
|Fail2Ban|/|一款入侵防御软件，用于保护服务器免受暴力攻击|
|TCP BBR|/|TCP Bottleneck Bandwidth and RTT，一种 TCP 拥塞控制算法|
|Wi-Fi|/|Wireless Fidelity，无线局域网技术|
|USB RNDIS|/|USB Remote Network Driver Interface Specification，USB 网络共享技术|
|Linux 兼容层|/|FreeBSD 的功能，允许运行 Linux 二进制程序|
|OpenHarmony|/|开放鸿蒙，华为开发的开源操作系统|
|RISC-V|/|一种开源的指令集架构|
|树莓派|/|Raspberry Pi，一款流行的单板计算机|
|Beastie|/|BSD 的吉祥物，一个红色的小恶魔形象|
|FreeBSD 基金会|/|美国科罗拉多州博尔德县的一家 501(c)3 非营利机构，负责支持 FreeBSD 项目|
|FreeBSD 核心小组|/|FreeBSD 项目的最高领导机构，共 9 人，采取集体领导制度|
|提交者|/|有权力直接写入 FreeBSD 存储库的人|
|CSRG|/|Computer Systems Research Group，加州大学伯克利分校的计算机系统研究小组|
|Multics|/|多路复用信息和计算服务，一个早期的操作系统项目|
|OpenSolaris|/|Sun Microsystems 开源的 Solaris 操作系统|
|illumos|/|OpenSolaris 社区管理委员会解散后，主要社区开发力量迁移到的新分支|
|Oracle Solaris|/|Oracle 收购 Sun 后，Solaris 项目进入闭源开发模式后的名称|
|LLNL|/|Lawrence Livermore National Laboratory，美国劳伦斯利弗莫尔国家实验室，OpenZFS 代码提交量的首位成员所属机构|
|ALTQ|/|Alternate Queuing，交错队列，PF 防火墙的功能|
|NAT|/|Network Address Translation，网络地址转换|
|ICMP|/|Internet Control Message Protocol，互联网控制报文协议|
|UDP|/|User Datagram Protocol，用户数据报协议|
|TCP|/|Transmission Control Protocol，传输控制协议|
|DNS|/|Domain Name System，域名系统|
|DHCP|/|Dynamic Host Configuration Protocol，动态主机配置协议|
|HTTP|/|HyperText Transfer Protocol，超文本传输协议|
|HTTPS|/|HyperText Transfer Protocol Secure，安全超文本传输协议|
|SSH|/|Secure Shell，安全外壳协议，用于安全远程登录|
|SSHD|/|SSH Daemon，SSH 守护进程|
|Changelog|/|变更日志，记录项目版本变更的文件|
|Readme|/|说明文件，通常包含项目的基本信息|
|Code of Conduct|/|行为准则，规定社区成员行为规范的文件|
|Contributing|/|贡献指南，说明如何为项目做贡献的文件|
|Security|/|安全说明，关于项目安全问题的说明文件|
|PR|/|Pull Request，拉取请求，在 Git 中提交代码变更的方式|
|CVS|/|Concurrent Versions System，并发版本系统，FreeBSD 早期使用的版本控制工具|
|SVN|/|Subversion，FreeBSD 中期使用的版本控制工具|
|Git|/|FreeBSD 目前使用的版本控制工具|
|CIS|/|Center for Internet Security，互联网安全中心，提供安全基准|
|SBOM|/|Software Bill of Materials，软件物料清单|
|SSDF|/|Secure Software Development Framework，安全软件开发框架|
|NIST|/|National Institute of Standards and Technology，美国国家标准及技术研究所|
|W^X|/|Write XOR Execute，写异或执行，一种安全策略|
|PIE|/|Position Independent Executable，位置无关可执行文件，一种安全缓解技术|
|ASLR|/|Address Space Layout Randomization，地址空间布局随机化，一种安全缓解技术|
|MAC|/|Mandatory Access Control，强制访问控制，TrustedBSD 的安全框架|
|DAC|/|Discretionary Access Control，自主访问控制，标准 Unix 安全模型|
|ACL|/|Access Control List，访问控制列表|
|TrustedBSD|/|FreeBSD 的安全扩展项目，基于 POSIX.1e 草案|
|Schg|/|系统不可变标志，FreeBSD 的文件系统标志之一|
|chflags|/|更改文件系统标志的命令|
|pw|/|FreeBSD 的用户和组管理命令|
|pwd_mkdb|/|生成密码数据库的命令|
|jls|/|列出当前运行中的 jail 信息的命令|
|jexec|/|在 jail 环境中执行命令的命令|
|pfctl|/|PF 防火墙的管理命令|
|kldload|/|加载内核模块的命令|
|kldunload|/|卸载内核模块的命令|
|sysctl|/|查看和设置内核状态的命令|
|sysrc|/|管理 rc.conf 配置的命令|
|service|/|管理系统服务的命令|
|make|/|构建工具，常用于编译 Ports|
|tar|/|归档工具，用于打包和解压文件|
|fetch|/|FreeBSD 的下载工具|
|certctl|/|管理证书的命令|
|ntpdate|/|同步时间的命令|
|gop|/|Graphics Output Protocol，图形输出协议，用于设置 UEFI 引导分辨率|
|VESA|/|Video Electronics Standards Association，视频电子标准协会，用于设置 BIOS 引导分辨率|
|autoboot_delay|/|自动启动延迟，loader.conf 中的配置项|
|boot_mute|/|静默启动，loader.conf 中的配置项|
|beastie_disable|/|禁用小恶魔启动菜单，loader.conf 中的配置项|
|loader_logo|/|设置启动 Logo，loader.conf 中的配置项|
|efi_max_resolution|/|设置 EFI 引导下的最大分辨率，loader.conf 中的配置项|
|vbe_max_resolution|/|设置 BIOS 引导下的最大分辨率，loader.conf 中的配置项|
|console|/|控制台，loader.conf 中的配置项，指定系统控制台|
|kernel|/|内核，loader.conf 中的配置项，指定要启动的内核|
|zfs_enable|/|启用 ZFS，loader.conf 中的配置项|
|kern.geom.label.disk_ident.enable|/|禁用 disk_ident 标签，loader.conf 中的配置项|
|kern.geom.label.gptid.enable|/|禁用基于磁盘序列号生成的设备名，loader.conf 中的配置项|
|rc.conf.d|/|rc.conf 的子目录，用于存放特定服务的配置文件|
|loader.conf.d|/|loader.conf 的子目录，用于存放用户定义设置|
|device.hints|/|设备资源提示文件，用于控制驱动程序的内核变量|
|motd|/|Message of the Day，今日信息，登录后显示的信息|
|fstab|/|文件系统表，用于配置文件系统挂载|
|hosts|/|本地 IP 域名映射表，优先于 DNS|
|resolv.conf|/|DNS 解析配置文件|
|ntp.conf|/|NTP 客户端配置文件|
|pf.conf|/|PF 防火墙配置文件|
|sysctl.conf|/|内核状态默认配置文件|
|syslog.conf|/|系统日志配置文件|
|ttys|/|创建 TTY 的规则文件|
|wpa_supplicant.conf|/|连接 WiFi 的配置文件|
|login.conf|/|登录类功能数据库|
|crontab|/|cron 定时任务文件|
|periodic.conf|/|定期执行的维护脚本配置文件|
|jail.conf|/|jail 配置文件|
|csh|/|C Shell，一种 shell|
|sh|/|Bourne Shell，FreeBSD 的默认 shell|
|tcsh|/|Tenex C Shell，csh 的增强版本|
|bash|/|Bourne Again Shell，GNU 的 shell|
|zsh|/|Z Shell，一种功能强大的 shell|
|vi|/|一款经典的文本编辑器|
|Vim|/|Vi IMproved，vi 的增强版本|
|Emacs|/|一款功能强大的文本编辑器|
|Neovim|/|Vim 的重构版本|
|gcc|/|GNU Compiler Collection，GNU 编译器集合|
|clang|/|LLVM 的 C/C++/Objective-C 编译器|
|gdb|/|GNU Debugger，GNU 调试器|
|IDA Pro|/|Interactive Disassembler Professional，一款专业的反汇编和调试工具|
|Java|/|一种编程语言和计算平台|
|Python|/|一种高级编程语言|
|Rust|/|一种系统编程语言，注重安全和性能|
|Go|/|Golang，Google 开发的编程语言|
|Qt|/|一款跨平台的应用程序开发框架|
|Node.js|/|一个基于 Chrome V8 引擎的 JavaScript 运行时|
|Code Server|/|在浏览器中运行 VS Code 的工具|
|Clangd|/|Clang 的语言服务器，提供代码补全等功能|
|Ren'Py|/|一款视觉小说引擎|
|Godot|/|一款开源的游戏引擎|
|Minecraft|/|一款沙盒游戏|
|Steam|/|Valve 开发的游戏平台|
|Audacious|/|一款音频播放器|
|Krita|/|一款数字绘画软件|
|Blender|/|一款 3D 建模和动画软件|
|MuseScore|/|一款音乐制谱软件|
|GeoGebra|/|一款数学软件|
|GPeriodic|/|一款元素周期表软件|
|Fcitx|/|一款输入法框架|
|IBus|/|Intelligent Input Bus，一款输入法框架|
|Firefox|/|一款开源的 Web 浏览器|
|Chromium|/|一款开源的 Web 浏览器|
|Wine|/|一款在类 Unix 系统上运行 Windows 程序的兼容层|
|Termius|/|一款 SSH 客户端|
|MobaXterm|/|一款 Windows 下的 SSH 客户端和 X11 服务器|
|AnyDesk|/|一款远程桌面软件|
|VirtualBox|/|一款虚拟机软件|
|VMware|/|一款虚拟机软件|
|Hyper-V|/|Microsoft 的虚拟机技术|
|Parallels Desktop|/|一款 macOS 下的虚拟机软件|
|UTM|/|一款 macOS 和 iOS 下的虚拟机软件|
|KVM|/|Kernel-based Virtual Machine，Linux 的内核虚拟机|
|QEMU|/|一款开源的机器模拟器和虚拟机|
|Ventoy|/|一款多合一启动盘制作工具|
|rEFInd|/|一款 UEFI 引导管理器|
|Xrdp|/|一款开源的 RDP 服务器|
|FreeRDP|/|一款开源的 RDP 客户端|
|Dsbmd|/|一款 FreeBSD 的设备挂载守护进程|
|Dsbmc|/|dsbmd 的图形化客户端|
|GParted|/|一款图形化的磁盘分区工具|
|GIMP|/|GNU Image Manipulation Program，一款图像编辑软件|
|LibreOffice|/|一款开源的办公套件|
|Calibre|/|一款电子书管理软件|
|VLC|/|一款开源的媒体播放器|
|MPV|/|一款开源的媒体播放器|
|Kodi|/|一款开源的媒体中心软件|
|Radxa|/|瑞芯微，一家中国的半导体公司，开发 Radxa 系列开发板|
|树莓派|Raspberry Pi|一款流行的单板计算机|
|昉·星光 2|VisionFive 2|一款 RISC-V 开发板|
|TwinCAT/BSD|/|倍福自动化控制系统的操作系统|
|GhostBSD|/|一款基于 FreeBSD 的桌面发行版|
|MidnightBSD|/|一款基于 FreeBSD 的操作系统|
|NomadBSD|/|一款基于 FreeBSD 的 Live USB 发行版|
|HelloSystem|/|一款基于 FreeBSD 的桌面操作系统，设计风格类似 macOS|
|MfsBSD|/|一款基于 FreeBSD 的内存文件系统发行版|
|AbsoluteBSD|/|一款基于 FreeBSD 的发行版|
|FuryBSD|/|一款基于 FreeBSD 的桌面发行版（已停止维护）|
|TrueOS|/|一款基于 FreeBSD 的服务器和桌面发行版（已停止维护）|
|PC-BSD|/|一款基于 FreeBSD 的桌面发行版（已停止维护，后更名为 TrueOS）|
|DragonFly BSD|/|一款从 FreeBSD 分叉出来的 BSD 操作系统|
|OpenBSD|/|一款注重安全的 BSD 操作系统|
|NetBSD|/|一款注重可移植性的 BSD 操作系统|
|FreeBSD 中文社区|/|FreeBSD 的中文用户和开发者社区|
|FreeBSD 日|/|每年 6 月 19 日，FreeBSD 基金会和社区庆祝 FreeBSD 生日的日子|
|EuroBSDCon|/|欧洲 BSD 大会|
|AsiaBSDCon|/|亚洲 BSD 大会|
|BSDCan|/|加拿大 BSD 大会|
|FreeBSDCon|/|FreeBSD 大会，首届于 1999 年举行|
|FreeBSD 期刊|/|FreeBSD 社区的期刊，跟进 FreeBSD 最新发布版本和新进展|
|谷歌编程之夏|/|Google Summer of Code，一个为学生提供参与开源项目机会的项目|
|FreeBSD 手册|/|FreeBSD 官方文档，提供详细的使用指南和参考|
|FreshPorts|/|一个 FreeBSD Ports 的搜索引擎和信息网站|
|BSDCan|/|加拿大 BSD 大会|
|TrustedBSD|/|FreeBSD 的安全扩展项目|
|OpenBSM|/|Open Basic Security Module，FreeBSD 的安全审计系统|
|Capsicum|/|FreeBSD 的轻量级能力和沙盒框架|
|CHERI|/|Capability Hardware Enhanced RISC Instructions，基于 Capsicum 项目发展而来的 CPU 架构扩展|
|JEMALLOC|/|Jason Evans 开发的内存分配器，集成在 FreeBSD 的 libc 中|
|KTRACE|/|FreeBSD 的内核跟踪设施|
|DDB|/|FreeBSD 的内核调试器|
|GDB|/|GNU Debugger，也可用于调试 FreeBSD 内核|
|KDB|/|FreeBSD 的内核调试框架|
|KGDB|/|用于远程调试 FreeBSD 内核的 GDB|
|CTF|/|Compact C Type Format，FreeBSD 内核调试信息格式|
|DWARF|/|一种调试信息格式，也用于 FreeBSD|
|ELF|/|Executable and Linkable Format，可执行和可链接格式，FreeBSD 使用的二进制文件格式|
|a.out|/|一种旧的二进制文件格式，FreeBSD 早期使用|
|COFF|/|Common Object File Format，一种旧的二进制文件格式|
|Mach-O|/|Mach Object，macOS 使用的二进制文件格式|
|PE|/|Portable Executable，Windows 使用的二进制文件格式|
|libc|/|C 标准库，FreeBSD 的标准 C 库|
|libm|/|数学库，FreeBSD 的数学函数库|
|libthr|/|线程库，FreeBSD 的 POSIX 线程库|
|libkvm|/|内核虚拟机库，用于访问内核内存|
|libgeom|/|GEOM 库，用于与 GEOM 存储框架交互|
|libarchive|/|归档库，提供对多种存档格式的流式访问功能|
|libfetch|/|下载库，FreeBSD 的文件下载库|
|libssl|/|SSL/TLS 库，OpenSSL 的 SSL/TLS 库|
|libcrypto|/|加密库，OpenSSL 的加密库|
|Linuxism|/|Linux 主义/Linux 歧视，指软件过分依赖 Linux 特有特性而难以移植到其他类 Unix 操作系统的现象|
|最小惊讶原则|/|Principle of Least Astonishment，POLA，一种设计原则，指设计必须符合用户的习惯、期望和心智能力|
|大教堂与市集|/|一种软件开发模型的比喻，大教堂指集中式开发，市集指分布式开发|
|KISS 原则|/|Keep It Simple, Stupid，一种设计原则，强调保持简单|
|UNIX 哲学|/|源于 UNIX 操作系统的开发实践，强调小即美、一个程序只做一件事、原型先行、可移植性先于高效率性等原则|
|忒修斯之船|/|一个哲学悖论，用于探讨事物的同一性问题|
|谷堆悖论|/|一个哲学悖论，探讨量变引起质变的问题|
|秃头悖论|/|一个哲学悖论，探讨量变引起质变的问题|
|同一时间的同一性|/|Identity Over Time，哲学中探讨事物在时间中保持同一性的问题|
|单一 UNIX 规范|/|Single UNIX Specification，SUS，UNIX 操作系统的标准规范|
|The Open Group|/|负责管理 UNIX 商标和单一 UNIX 规范的组织|
|501(c)3|/|美国税法中的一种非营利组织类型，可接受免税捐赠|
|LLNL|/|Lawrence Livermore National Laboratory，美国劳伦斯利弗莫尔国家实验室|
|Delphix|/|一家公司，OpenZFS 新功能的主要开发商|
|Perforce Software|/|一家软件公司，2024 年 2 月收购了 Delphix|
|Sun Microsystems|/|太阳计算机系统公司，ZFS 和 Solaris 的原开发商，2009 年被 Oracle 收购|
|Oracle|/|甲骨文公司，收购了 Sun Microsystems|
|AT&T|/|美国电话电报公司，UNIX 的原开发商|
|贝尔实验室|/|Bell Labs，AT&T 的研究实验室，UNIX 的诞生地|
|加州大学伯克利分校|/|University of California, Berkeley，BSD 的诞生地|
|CSRG|/|Computer Systems Research Group，加州大学伯克利分校的计算机系统研究小组|
|Bill Joy|/|Sun Microsystems 的创始人之一，也是 BSD Unix 的关键开发者|
|Ken Thompson|/|UNIX 的主要开发者之一|
|Dennis Ritchie|/|UNIX 的主要开发者之一，C 语言的发明者|
|Marshall Kirk McKusick|/|FreeBSD 的重要开发者，《FreeBSD 操作系统设计与实现》的作者之一|
|George Neville-Neil|/|《FreeBSD 操作系统设计与实现》的作者之一|
|Robert N.M. Watson|/|《FreeBSD 操作系统设计与实现》的作者之一|
|Jordan Hubbard|/|FreeBSD 的创始人之一，Ports 系统的创建者|
|Justin Gibbs|/|FreeBSD 基金会的创始人之一|
|Deb Goodkin|/|FreeBSD 基金会的首位执行董事|
|Jan Koum|/|WhatsApp 的原 CEO 及创始人，FreeBSD 的重要捐赠者|
|Eric S. Raymond|/|开源运动的重要人物，《大教堂与集市》和《UNIX 编程艺术》的作者|
|Henry Spencer|/|UNIX 社区的重要人物，有著名言论：“那些不懂 Unix 的人注定要再造一个四不像式 Unix”|
|Linus Torvalds|/|Linux 内核的创始人|
|Richard M. Stallman|/|自由软件基金会的创始人，GNU 项目的发起者|
|Theo de Raadt|/|OpenBSD 的创始人|
|Matt Dillon|/|DragonFly BSD 的创始人|
|Red Hat|/|红帽公司，一家重要的 Linux 发行商，控制着许多主流 Linux 项目|
|Netflix|/|奈飞公司，几乎所有网络活动都使用 FreeBSD 设备进行|
|Sony|/|索尼公司，PlayStation 系列游戏机使用基于 FreeBSD 的操作系统|
|Dell EMC|/|戴尔 EMC，Isilon NAS 存储设备使用基于 FreeBSD 的 OneFS 操作系统|
|Beckhoff|/|倍福公司，TwinCAT/BSD 自动化控制系统使用 FreeBSD|
|容器|/|Container，一种轻量级的虚拟化技术|
|CI/CD|/|Continuous Integration/Continuous Deployment，持续集成/持续部署|
|Git|/|一种分布式版本控制系统|
|GitHub Actions|/|GitHub 的持续集成和持续部署服务|
|GitHub|/|一个代码托管平台|
|Git|/|一种分布式版本控制系统|
|SVN|/|Subversion，一种集中式版本控制系统|
|CVS|/|Concurrent Versions System，一种早期的版本控制系统|
|DevSummit|/|FreeBSD 的开发者峰会|
|BSDCan|/|加拿大 BSD 大会|
|EuroBSDCon|/|欧洲 BSD 大会|
|FreeBSD 中文社区|/|FreeBSD 的中文用户和开发者社区|
|FreeBSD 日|/|每年 6 月 19 日，FreeBSD 基金会和社区庆祝 FreeBSD 生日的日子|
|AsiaBSDCon|/|亚洲 BSD 大会|
|FreeBSDCon|/|FreeBSD 大会，首届于 1999 年举行|
|FreeBSD 期刊|/|FreeBSD 社区的期刊，跟进 FreeBSD 最新发布版本和新进展|
|谷歌编程之夏|/|Google Summer of Code，一个为学生提供参与开源项目机会的项目|
|FreeBSD 手册|/|FreeBSD 官方文档，提供详细的使用指南和参考|
|FreshPorts|/|一个 FreeBSD Ports 的搜索引擎和信息网站|