# 4.3 系统目录结构

## 目录结构概览

FreeBSD 的文件系统层次结构是理解系统整体架构的基础。根目录（/）是文件系统的最顶层目录，在系统启动时第一个被挂载，包含操作系统进入多用户模式所需的基本系统。根目录还包含其他文件系统的挂载点。挂载点是附加文件系统可以挂载到父文件系统（通常是根文件系统）上的目录。标准挂载点包括 `/usr/`、`/var/`、`/tmp/`、`/mnt/` 和 `/media/`。完整的文件系统层次结构描述参见 hier(7)。

## 文件系统层次结构的设计哲学

类 UNIX 操作系统的目录结构设计遵循若干核心原则，这些原则源于 UNIX 早期开发实践并经长期演化而成：

- **单一根目录原则**：与 Windows 等系统采用多根（多盘符）的设计不同，UNIX 系统采用单一根目录（`/`）作为整个文件系统的起点。所有存储设备、分区和网络文件系统均以挂载（mount）的方式接入统一的目录树中。这一设计使得文件路径具有全局唯一性，避免了盘符分配的不确定性。文件系统最好被可视化为以 `/` 为根的树形结构，`/dev`、`/usr` 等目录是根目录的分支，这些分支还可以拥有自己的分支。

- **功能分离原则**：将不同功能的文件分配到不同的目录中，使得各文件系统可以独立管理、挂载和备份。例如，将系统二进制文件（`/bin`、`/sbin`）与用户应用程序（`/usr/local`）分离，将配置文件（`/etc`）与日志数据（`/var/log`）分离。将 `/var` 与 `/` 分离是有利的，因为 `/var` 包含日志目录、假脱机目录和多种临时文件，可能会被填满，而填满根文件系统是不当的做法。

- **基本系统与第三方软件分离原则**：FreeBSD 将基本系统（base system）与第三方软件严格分离。基本系统的组件安装在 `/bin`、`/sbin`、`/usr/bin`、`/usr/sbin`、`/usr/lib` 等目录中，而通过 Ports 或 pkg 安装的第三方软件则统一安装到 `/usr/local/` 下的对应子目录中（如 `/usr/local/bin`、`/usr/local/lib`、`/usr/local/etc`）。这种分离确保了基本系统的独立性和完整性，使得系统升级不会影响第三方软件，反之亦然。

- **静态与动态数据分离原则**：静态数据（如二进制文件、库文件、文档）与动态数据（如日志、临时文件、运行时数据）分别存储于不同的目录树中。`/usr` 主要存放静态的只读数据，`/var` 则存放可变的运行时数据，`/tmp` 存放临时文件。

## FHS 与 FreeBSD 目录结构

文件系统层次标准（Filesystem Hierarchy Standard，FHS）由 Linux 基金会维护，旨在定义类 UNIX 操作系统中目录结构和目录内容的规范。FHS 的目标是使软件开发者能够预测已安装文件和目录的位置，从而编写更具可移植性的软件。当前版本为 FHS 3.0，发布于 2015 年。

FreeBSD 的目录结构遵循了 FHS 的核心设计理念，但并非 FHS 的严格实现。FreeBSD 的目录层次由 `hier(7)` 手册页定义，是 FreeBSD 项目的权威规范。与 Linux 发行版相比，FreeBSD 的目录结构存在若干显著差异：

| 项目 | FHS（文件系统层次标准） | FreeBSD |
| ---- | ----------------------- | ------- |
| `/usr/local` 的角色 | 保留给系统管理员本地安装软件 | Ports 与 pkg 安装第三方软件的默认目标路径；用于本地可执行文件与库 |
| 配置文件位置 | 通常位于 `/etc` 或 `/etc/opt`（第三方软件） | 第三方软件配置位于 `/usr/local/etc`；系统配置位于 `/etc`，严格分离 |
| `/libexec` 目录 | 非标准或不强制规定 | 用于存放系统级辅助可执行程序 |
| `/rescue` 目录 | 不存在标准定义 | 存放静态链接的紧急修复工具，用于系统恢复 |

为便于说明，仅列出前三级目录及重要文件。

```sh
/
├── COPYRIGHT FreeBSD 版权信息文件
├── bin 基本的 BSD 用户工具，参见 intro(1)
├── boot 操作系统引导过程中使用的程序和配置文件，参见 boot(8)
│   ├── defaults 存放默认内核的默认引导配置文件
│   │   └── loader.conf 详细的示例说明文件，参见 loader.conf(5)
│   ├── device.hints 用于控制驱动程序的内核变量，参见 device.hints(5)
│   ├── dtb 编译的扁平化设备树（FDT）文件，参见 fdt(4) 和 dtc(1)；x86 架构下应为空
│   │   └── overlays 编译的 FDT 覆盖层，参见 loader.conf(5) 中的 fdt_overlays
│   ├── efi EFI 系统分区（ESP）挂载点，参见 uefi(8)
│   ├── firmware 可加载的二进制固件内核模块；pkg kmod 会安装至此，以及通过 fwget 下载的固件
│   ├── fonts 二进制位图控制台字体，参见 loader.conf(5) 和 vtfontcvt(8)
│   ├── images 启动时显示的 FreeBSD Logo 等，参见 loader_lua(8)
│   ├── kernel 内核及内核模块，参见 kldstat(8)
│   ├── kernel.old 备用内核及内核模块
│   ├── loader.conf loader 配置文件，参见 loader.conf(5)
│   ├── loader.conf.d loader 配置文件的子项，参见 loader.conf(5)
│   ├── lua 引导加载程序的 Lua 脚本，包含启动时显示的 ASCII 艺术字（图）等，参见 loader_lua(8)
│   ├── modules 第三方可加载内核模块，如通过 pkg(8) 或 ports(7) 安装的模块
│   ├── uboot 空目录
│   └── zfs 存放 ZFS 存储池（Zpool）的缓存文件，参见 zpool(8)
│       └── zpool.cache 硬编码的磁盘驱动器路径，参见 zpool(8)
├── compat 支持与其他操作系统二进制兼容的文件
│   └── linux Linux 兼容层运行时的默认位置，参见 linux(4)
├── dev 存放设备文件和特殊文件，参见 intro(4) 和 devfs(5)
│   ├── ada0 第一块 ATA 存储设备
│   ├── ada0p1 第一块 ATA 存储设备的第一个分区
│   ├── cd0 第一块光盘驱动器
│   ├── cuaU0 第一个 USB 串口，参见 cu(1)
│   ├── da0 第一块 SCSI 存储设备
│   ├── da0s1 第一块 SCSI 存储设备的第一个分区
│   ├── dri 显卡字符设备节点，参见 drm(7)
│   ├── drm 显卡特殊文件节点，参见 drm(7)
│   ├── fd 文件描述符文件，参见 fd(4)；目录下 0、1、2 对应标准输入、标准输出和标准错误
│   ├── fd0 第一块软盘驱动器
│   ├── gpt 按 GPT 标签划分的存储分区，参见 gpt(8)
│   ├── input 存放输入设备相关的设备文件
│   ├── iso9660 ISO 9660 文件系统的设备节点，如光盘
│   ├── mmcsd0 第一张 SD 存储卡
│   ├── mmcsd0s1 第一张 SD 存储卡的第一个分区
│   ├── nda0 第一块 NVMe 存储设备（通过 cam(3) 连接）
│   ├── nda0p1 第一块 NVMe 存储设备的第一个分区
│   ├── null 无限循环设备，接受任何输入但不包含任何内容
│   ├── nvd0 第一块 NVMe 存储设备（使用 NVMe 命名空间）
│   ├── pts 伪终端设备，参见 pts(4)
│   ├── random 弱随机性来源，参见 random(4)
│   ├── reroot reboot -r 使用
│   ├── sa0 第一块磁带驱动器
│   ├── usb USB 总线
│   ├── vmm 活跃的 bhyve(8) 虚拟机
│   └── zvol ZFS 卷，参见 zfs(8)
├── entropy 为随机数生成器提供初始状态，参见 save-entropy(8)
├── etc 基本系统配置文件和脚本，参见 intro(5)
│   ├── auto_master autofs 配置文件，参见 automount(8)
│   ├── autofs 存放自动挂载相关的配置文件，参见 autofs(5)
│   ├── bluetooth 蓝牙相关配置文件
│   ├── cron.d 存放系统级的定时任务配置文件，参见 crontab(5)
│   ├── crontab root 用户的 crontab 文件
│   ├── defaults 存放了一组默认配置文件，如 rc.conf、periodic.conf，参见 rc(8)
│   ├── devd 存放设备管理器（devd）的配置文件，如监控蓝牙、鼠标插拔，参见 devd(8)
│   ├── devfs.conf 启动时的 devfs 设备规则配置
│   ├── dma DMA 邮件代理相关，参见 dma(8)
│   ├── freebsd-update.conf 基本系统更新工具 freebsd-update 的配置文件，参见 freebsd-update(8)
│   ├── fstab 文件分区表，参见 fstab(5)
│   ├── gss GSSAPI 相关文件、含 Kerberos 5
│   ├── hosts hosts 文件，优先于 DNS 的本地 IP 域名映射表
│   ├── inetd.conf 配置 BSD inetd，参见 inetd(8)
│   ├── jail.conf.d 旨在实现对 jail 配置的模块化管理，默认为空（jail.conf(5)）
│   ├── kyua Kyua 测试框架的全局配置文件（kyua(1)、kyua.conf(5)）
│   ├── localtime 本地时区文件，参见 ctime(3)。在测试系统中，localtime 被链接到了 /usr/share/zoneinfo/Asia/Shanghai
│   ├── login.conf 登录类功能数据库，参见 login.conf(5)
│   ├── machine-id 系统的 UUID，D-Bus 用
│   ├── mail Sendmail 相关文件，参见 sendmail(8)
│   │   ├── aliases 用于投递系统邮件的地址
│   │   └── mailer.conf mailwrapper(8) 配置文件
│   ├── motd.template TTY 登录后显示的信息，参见 motd(5)
│   ├── mtree 用于系统的初始化和验证过程，可用于系统审计，参见 mtree(8)
│   ├── newsyslog.conf.d newsyslog 的配置文件，参见 newsyslog.conf(5)
│   ├── ntp NTP 相关，参见 ntp.conf(5)、ntpd(8)
│   ├── ntp.conf NTP 客户端配置文件，参见 ntpd(8)
│   ├── pam.d 可插拔认证模块（PAM）相关的配置文件，参见 pam(3)
│   ├── periodic 存放定期执行的维护脚本，由 cron 调用，参见 periodic(8)
│   ├── pf.conf PF 防火墙配置文件，参见 pf(4)
│   ├── pkg PKG 相关配置文件，参见 pkg(8)
│   ├── ppp PPP 相关配置，参见 ppp(8)
│   ├── profile.d 存放脚本文件，这些脚本可在用户登录时由 Shell 执行，但不会自动加载
│   ├── rc.conf 系统 RC，参见 rc.conf(5)
│   ├── rc.conf.d 存放特定服务的配置文件，默认为空
│   ├── rc.d 用于启动和管理系统服务的 RC 脚本，参见 rc(8)
│   ├── resolv.conf DNS 解析配置文件，参见 resolv.conf(5)
│   ├── resolvconf.conf DNS 配置管理器配置，通常由 local-unbound 生成，参见 local-unbound(8) 或 resolvconf(8)
│   ├── security OpenBSM 审计配置文件，参见 audit(8)
│   ├── ssh SSH 和 SSHD 相关配置文件，参见 ssh(1)
│   ├── ssl 存储与 SSL/TLS 相关的文件，如证书、密钥
│   │   ├── cert.pem 系统信任库的捆绑形式，参见 certctl(8)
│   │   ├── certs 系统信任库的 OpenSSL 哈希目录形式，参见 certctl(8)
│   │   ├── openssl.cnf OpenSSL 配置文件，参见 openssl.cnf(5)
│   │   └── untrusted 明确不信任的证书，参见 certctl(8)
│   ├── sysctl.conf 内核状态默认值，参见 sysctl.conf(5)
│   ├── sysctl.kld.d 特定内核模块的配置文件，默认为空，参见：D40886[EB/OL]. [2026-03-26]. <https://reviews.freebsd.org/D40886>.
│   ├── syslog.conf 系统日志配置文件
│   ├── syslog.d syslogd 的配置文件，参见 syslog(3)
│   ├── ttys 创建 TTY 的规则文件，参见 getty(8)
│   ├── unbound Unbound 配置文件
│   ├── wpa_supplicant.conf 连接 WiFi 的配置文件，参见 wpa_supplicant.conf(5)
│   ├── X11 X11 相关，如 XRDP
│   └── zfs ZFS 相关配置文件，参见 zfs(8)
├── home 普通用户家目录；典型用户 beastie 的家目录为 /home/beastie/
│   └── ykla 普通用户 ykla 的家目录
├── lib /bin、/sbin 的库文件，对 /bin 和 /sbin 中的二进制文件至关重要的系统库
│   ├── geom GEOM 库，参见 geom(8)
│   └── nvmecontrol NVMe 相关工具，参见 nvmecontrol(8)
├── libexec 系统级辅助可执行程序，对 /bin 和 /sbin 中的二进制文件至关重要的系统实用程序
│   └── resolvconf 管理 DNS 解析配置的程序，参见 resolvconf.conf(5)
├── media 媒体文件挂载点，如 U 盘、光盘；参见 automount(8)，或使用桌面环境时参见 bsdisks(8)
├── mnt 用作临时挂载点的空目录
├── net NFS 共享挂载点，参见 auto_master(5)
├── nonexistent 不存在的目录；按照惯例，作为不需要家目录的用户账户的家目录；参见 /var/empty/
├── proc 现代 FreeBSD 默认不使用 procfs，该目录通常为空；参见 procfs(4)
├── rescue 静态链接的系统工具，紧急模式时使用，参见 rescue(8)
├── root root 的家目录
├── sbin 基本的 BSD 系统管理工具，参见 intro(8)
├── tmp 通常在系统重启后仍会保留的临时文件；参见 rc.conf(5) 中的 clear_tmp_enable
├── usr 包含大多数用户实用程序和应用程序
│   ├── bin 用户实用程序、编程工具和应用程序，参见 intro(1)
│   ├── freebsd-dist 发行文件（如 base.txz），参见 release(7) 和 bsdinstall(8)
│   ├── include 标准 C 头文件
│   ├── lib 共享库和 ar(1) 类型库，参见 intro(3)
│   │   ├── clang 系统编译器 clang(1) 的共享库
│   │   ├── compat 兼容性共享库
│   │   ├── debug 内核和基本系统库及二进制文件的独立调试数据
│   │   ├── dtrace dtrace(1) 库脚本
│   │   ├── engines OpenSSL（加密/SSL 工具包）动态可加载引擎
│   │   ├── flua FreeBSD Lua 共享库
│   │   └── i18n 国际化共享库
│   ├── lib32 32 位兼容库
│   ├── libdata 杂项实用数据文件
│   │   ├── ldscripts 链接器脚本，参见 ld(1)
│   │   └── pkgconfig 编译器和链接器标志集合，用于 pkgconf(1) 开发工具
│   ├── libexec 由程序执行的系统守护进程和实用程序
│   │   ├── bsdconfig ncurses FreeBSD 配置向导调用的实用程序
│   │   ├── bsdinstall bsdinstall(8) 的实用程序
│   │   ├── dwatch dwatch(1) 的配置文件
│   │   ├── fwget fwget(8) 调用的实用程序
│   │   ├── hyperv 与 Hyper-V 虚拟机管理程序通信的脚本
│   │   ├── lpr 行式打印机系统的实用程序和过滤器，参见 lpr(1)
│   │   ├── sendmail sendmail(8) 二进制文件，参见 mailwrapper(8)
│   │   ├── sm.bin sendmail(8) 的受限 Shell，参见 smrsh(8)
│   │   └── zfs Z 文件系统实用程序
│   ├── local 本地可执行文件、库等，由 pkg(7) 或 ports(7) 安装
│   │   ├── bin 本地用户实用程序，参见 intro(1)
│   │   ├── etc 本地程序配置文件
│   │   ├── include 本地库头文件
│   │   ├── lib 本地库文件
│   │   ├── lib32 本地 32 位兼容库
│   │   ├── libdata 本地实用数据文件
│   │   ├── libexec 本地实用程序调用的实用程序
│   │   ├── sbin 本地管理实用程序
│   │   ├── share 本地架构无关文件
│   │   ├── share/doc 本地文档
│   │   ├── share/doc/freebsd/ FreeBSD 项目的文章、书籍、FAQ 和手册
│   │   └── share/man 本地手册页，参见 man(1)
│   ├── obj 架构特定的目标树，用于从源代码构建 FreeBSD，参见 build(7)
│   ├── ports FreeBSD Ports，参见 ports(7)
│   │   └── distfiles 下载的源代码包的存放位置
│   ├── sbin 系统守护进程和面向用户执行的管理实用程序，参见 intro(8)
│   ├── share 架构无关文件
│   │   ├── atf 自动化测试框架脚本，参见 ATF(7)
│   │   ├── bhyve bhyve(8) 键盘映射
│   │   ├── calendar 系统级日历文件，参见 calendar(1)
│   │   ├── certs openssl(1) 的 TLS 证书
│   │   ├── dict 词表，参见 look(1)
│   │   │   ├── freebsd FreeBSD 特有的术语、专有名词和行话
│   │   │   └── web2 韦氏第二版国际词典的词汇
│   │   ├── doc 杂项文档
│   │   ├── dtrace 动态跟踪编译器脚本，参见 dtrace(1)
│   │   ├── examples 用户和程序员的各种示例
│   │   ├── firmware 用户态程序加载的固件映像
│   │   ├── games BSD 传统游戏使用的 ASCII 文本文件，参见 intro(6)
│   │   ├── keys 已知可信和已撤销的密钥
│   │   │   └── pkg pkg(7) 和 pkg(8) 的指纹
│   │   ├── locale 本地化文件，参见 setlocale(3)
│   │   ├── man 系统手册页，参见 man(1)
│   │   ├── misc 杂项系统级文件
│   │   │   ├── ascii ASCII 码表
│   │   │   ├── flowers 花语含义
│   │   │   ├── magic file(1) 使用的魔术数字
│   │   │   └── termcap 终端特性数据库，参见 termcap(5)
│   │   ├── mk make 模板，参见 make(1)
│   │   ├── nls 国家语言支持文件
│   │   ├── security 安全策略数据文件，如 mac_lomac(4)
│   │   ├── sendmail sendmail(8) 配置文件
│   │   ├── skel 新账户的示例点文件
│   │   ├── snmp SNMP 守护进程的 MIB、示例文件和树定义
│   │   │   ├── defs 用于 gensnmptree(1) 的树定义文件
│   │   │   └── mibs 管理信息库（MIB）文件
│   │   ├── syscons syscons(4) 文件
│   │   │   ├── fonts 控制台字体，参见 vidcontrol(1) 和 vidfont(1)
│   │   │   ├── keymaps 控制台键盘映射，参见 kbdcontrol(1) 和 kbdmap(1)
│   │   │   └── scrnmaps 控制台屏幕映射
│   │   ├── sysroot -sysroot 编译器/链接器参数构建非本机二进制文件所需的文件
│   │   │   └── VERSION FreeBSD 发行版 VERSION 的文件；"VERSION" 匹配 uname(1) -r
│   │   │       └── MACHINE.MACHINE_ARCH 表示这些文件的二进制 ABI；"MACHINE" 匹配 uname(1) -m；"MACHINE_ARCH" 匹配 uname(1) -p
│   │   ├── tabset 各种终端的制表符描述文件，用于 termcap 文件，参见 termcap(5)
│   │   ├── vi vi(1) 编辑器的本地化支持和实用程序
│   │   ├── vt 系统控制台使用的文件，参见 vt(4)
│   │   │   ├── fonts 控制台字体，参见 vidcontrol(1)、vidfont(1) 和 vtfontcvt(8)
│   │   │   └── keymaps 控制台键盘映射，参见 kbdcontrol(1) 和 kbdmap(1)
│   │   └── zoneinfo 时区配置信息，参见 tzfile(5)
│   ├── src FreeBSD 源代码，参见 development(7)；源代码树的布局由顶层 README.md 文件描述
│   └── tests FreeBSD 测试套件，参见 tests(7)
├── var 多种用途的日志、临时、瞬态、缓存文件
│   ├── account 默认为空，系统审计用，参见 accton(8)
│   │   └── acct 执行审计文件，参见 acct(5)
│   ├── at 存放 at 命令调度的任务文件，参见 at(1)
│   │   ├── jobs 作业文件
│   │   └── spool 输出假脱机文件
│   ├── audit 存储安全审计日志文件，属于 audit 组，参见 audit(8)
│   ├── authpf 用于认证网关用户的 Shell，参见 authpf(8)，默认为空
│   ├── backups 用于存放系统的备份文件，如用户名和密钥、pkg 数据库。由 /etc/periodic/daily 下的 200、210 等文件生成
│   ├── cache 缓存文件
│   │   ├── cups CUPS 的缓存打印机，参见 cups(1)
│   │   └── pkg pkg(8) 的缓存包
│   ├── crash 存放崩溃转储文件，参见 crash(8) 和 savecore(8)
│   ├── cron 存放 cron 定时任务相关文件，参见 cron(8)
│   │   └── tabs crontab 文件，参见 crontab(5)
│   ├── db 自动生成的系统特定数据库文件
│   │   ├── etcupdate etcupdate(8) 的临时文件和日志
│   │   ├── freebsd-update freebsd-update(8) 的下载和临时文件
│   │   └── pkg 包数据库
│   ├── empty 默认为空，旨在提供一个始终保持为空的目录供特定程序使用①
│   ├── games 存放与游戏相关的数据文件，默认为空
│   ├── heimdal Kerberos 5 用，默认为空，参见 kdc(8)
│   ├── lib 移植的 Linux 应用程序的状态信息
│   ├── log 各种系统日志文件
│   │   ├── Xorg.0.log X 服务器日志（若安装了 X(7)），轮替为 Xorg.0.log.old
│   │   ├── aculog 串行线路访问日志，参见 cu(1)
│   │   ├── auth.log 系统认证日志
│   │   ├── bsdinstall_log 系统安装日志
│   │   ├── cron 定时任务日志，参见 cron(8)
│   │   ├── cups CUPS 日志，参见 cups(1)
│   │   ├── daemon.log 系统守护进程的默认日志
│   │   ├── debug.log 未丢弃的调试 syslog 消息
│   │   ├── devd.log 设备状态变更守护进程的默认日志
│   │   ├── dmesg.today 系统消息缓冲区日志，轮替为 dmesg.yesterday
│   │   ├── lpd-errs 行式打印机假脱机守护进程日志，参见 lpd(8)
│   │   ├── maillog sendmail(8) 日志，轮替并压缩为 maillog.0.bz2
│   │   ├── messages 通用系统日志，参见 syslogd(8)
│   │   ├── mount.today 当前加载的 fstab(5)，轮替为 mount.yesterday
│   │   ├── pf.today 包过滤防火墙日志，参见 pf(4)
│   │   ├── pflog pflogd(8) 捕获的已保存数据包
│   │   ├── ppp.log 参见 ppp(8)
│   │   ├── security 标记有安全标志的事件转录
│   │   ├── setuid.today 以提升权限运行的可执行文件列表，轮替为 setuid.yesterday
│   │   ├── userlog 用户或组变更日志
│   │   ├── utx.lastlogin 最后登录日志，参见 getutxent(3)
│   │   └── utx.log 登录/注销日志，参见 getutxent(3)
│   ├── mail 系统邮件，用户邮箱文件
│   ├── msgs 用于存放系统消息文件，参见 msgs(1)
│   ├── preserve 用于存放编辑器（如 vi）在异常关闭后保存的文件，已不再使用，默认为空
│   ├── quotas UFS 配额信息文件
│   ├── run 用来存放 PID 文件和运行时数据，包含自系统启动以来的操作系统信息
│   │   ├── bhyve bhyve(8) 虚拟机的 unix(4) 域套接字
│   │   ├── ppp 可由 "network" 组写入的命令连接套接字，参见 ppp(8)
│   │   ├── utx.active 当前用户数据库，参见 getutxent(3)
│   │   └── wpa_supplicant IEEE 802.11 WiFi 运行时文件
│   ├── rwho 存储由 rwhod 收集的网络中其他计算机的用户登录信息，参见 rwhod(8)。默认为空
│   ├── spool 存放等待处理的任务文件，如待打印机打印的文件
│   │   ├── clientmqueue 未投递的提交邮件队列，参见 sendmail(8)
│   │   ├── cups CUPS 的打印作业和临时文件，参见 cups(1)
│   │   ├── dma DragonFly 邮件代理的未投递邮件队列，参见 dma(8)
│   │   ├── lock 串行设备锁，参见 uucplock(3)
│   │   ├── lpd 行式打印机假脱机守护进程的假脱机
│   │   ├── mqueue sendmail(8) 的未投递邮件队列
│   │   └── output 行式打印机假脱机目录
│   ├── tmp 通常会在系统重启后保留的临时文件
│   │   └── vi.recover vi(1) 编辑器的恢复文件
│   ├── unbound Unbound 服务器的相关文件和配置，参见 unbound(8)
│   └── yp NIS 的配置等文件，参见 yp(8)
└── zroot 与 ZFS 池同名的目录，通常为空，功能尚不明确
```

①：目录 `/var/empty` 设置了 schg 标志，即系统不可变标志。

```sh
# ls -lod /var/empty
dr-xr-xr-x   2 root    wheel   schg  2 Apr 13 12:38 /var/empty
```

参数解释：在长格式（`-l`）输出中包含文件标志（`-o`），且将目录视为普通文件列出而不递归（`-d`）。

> **技巧**
>
> OpenSSH 使用特权分离（privilege separation）架构，预认证阶段的 chroot 目录为 `/var/empty`，该目录必须为空且仅 root 可写。

## 设备与设备节点

设备是系统中主要用于与硬件相关活动的术语，包括磁盘、打印机、显卡和键盘。

每个设备都有一个设备名称和编号。例如，`ada0` 是第一块 SATA 硬盘，而 `kbd0` 代表键盘。

FreeBSD 中的大多数设备必须通过称为设备节点的特殊文件访问，这些文件位于 `/dev` 目录中。

在 FreeBSD 中，设备节点由 devfs(5) 文件系统自动管理。devfs 是一个虚拟文件系统，在系统启动时由内核自动挂载到 `/dev`，并根据当前系统中存在的硬件设备动态创建和删除设备节点。这与传统 UNIX 系统需要手动使用 `mknod` 命令创建设备节点的做法不同。devfs 确保了 `/dev` 目录中只包含当前系统实际存在的设备节点，避免了设备节点的冗余。

设备节点分为两种类型：字符设备（character device）和块设备（block device）。字符设备以字节流方式访问数据，如终端（`/dev/ttyv0`）和串口；块设备以固定大小的块为单位访问数据，如磁盘（`/dev/ada0`）。在 `ls -l` 的输出中，字符设备的类型标识为 `c`，块设备的类型标识为 `b`。

设备命名遵循一定的约定：SATA 硬盘以 `ada` 开头（如 `ada0`、`ada1`），SCSI 硬盘和 USB 存储设备以 `da` 开头（如 `da0`），NVMe 存储以 `nvd` 或 `nda` 开头，CD-ROM 驱动器以 `cd` 开头。编号从 0 开始。GPT 分区在设备名后附加 `p` 加分区号（如 `ada0p1`），MBR 切片附加 `s` 加切片号（如 `ada0s1`）。

## 启动消息 dmesg

当 FreeBSD 启动时，大多数启动消息都与正在检测的设备有关。启动消息的副本保存在 `/var/run/dmesg.boot` 中。

以下示例是 Radxa X4 16G 128G eMMC 款在 15.0-CURRENT 下完整的启动消息内容。

```sh
---<<BOOT>>---
Copyright (c) 1992-2025 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
	The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
# FreeBSD 的版权信息

FreeBSD 15.0-CURRENT #0 main-n275588-045a4c108fcf: Fri Feb 21 02:25:56 UTC 2025
    root@releng3.nyi.freebsd.org:/usr/obj/usr/src/amd64.amd64/sys/GENERIC amd64
# 当前系统版本

FreeBSD clang version 19.1.7 (https://github.com/llvm/llvm-project.git llvmorg-19.1.7-0-gcd708029e0b2)
# Clang 版本

WARNING: WITNESS option enabled, expect reduced performance.
# CURRENT 系统内核默认启用了若干调试功能

VT(efifb): resolution 800x600
# EFI TTY 分辨率

CPU: Intel(R) N100 (806.40-MHz K8-class CPU)
  Origin="GenuineIntel"  Id=0xb06e0  Family=0x6  Model=0xbe  Stepping=0
  Features=0xbfebfbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,DTS,ACPI,MMX,FXSR,SSE,SSE2,SS,HTT,TM,PBE>
  Features2=0x7ffafbbf<SSE3,PCLMULQDQ,DTES64,MON,DS_CPL,VMX,EST,TM2,SSSE3,SDBG,FMA,CX16,xTPR,PDCM,PCID,SSE4.1,SSE4.2,x2APIC,MOVBE,POPCNT,TSCDLT,AESNI,XSAVE,OSXSAVE,AVX,F16C,RDRAND>
  AMD Features=0x2c100800<SYSCALL,NX,Page1GB,RDTSCP,LM>
  AMD Features2=0x121<LAHF,ABM,Prefetch>
  Structured Extended Features=0x239ca7eb<FSGSBASE,TSCADJ,BMI1,AVX2,FDPEXC,SMEP,BMI2,ERMS,INVPCID,NFPUSG,PQE,RDSEED,ADX,SMAP,CLFLUSHOPT,CLWB,PROCTRACE,SHA>
  Structured Extended Features2=0x98c007bc<UMIP,PKU,OSPKE,WAITPKG,GFNI,VAES,VPCLMULQDQ,RDPID,MOVDIRI,MOVDIR64B>
  Structured Extended Features3=0xfc184410<FSRM,MD_CLEAR,IBT,IBPB,STIBP,L1DFL,ARCH_CAP,CORE_CAP,SSBD>
  XSAVE Features=0xf<XSAVEOPT,XSAVEC,XINUSE,XSAVES>
  IA32_ARCH_CAPS=0x180fd6b<RDCL_NO,IBRS_ALL,SKIP_L1DFL_VME,MDS_NO,TAA_NO>
  VT-x: PAT,HLT,MTF,PAUSE,EPT,UG,VPID,VID,PostIntr
  TSC: P-state invariant, performance statistics
# CPU 相关信息

real memory  = 17179869184 (16384 MB)
avail memory = 16318308352 (15562 MB)
# 内存相关信息

Event timer "LAPIC" quality 600
# 事件计时器

ACPI APIC Table: <ALASKA A M I >
WARNING: L3 data cache covers more APIC IDs than a package (7 > 3)
# ACPI 相关信息

FreeBSD/SMP: Multiprocessor System Detected: 4 CPUs
FreeBSD/SMP: 1 package(s) x 4 core(s)
# 处理器 SMP 信息

random: registering fast source Intel Secure Key RNG
random: fast provider: "Intel Secure Key RNG"
random: unblocking device.
# 随机数生成器

ioapic0 <Version 2.0> irqs 0-119
Launching APs: 2 1 3
random: entropy device external interface
kbd0 at kbdmux0
efirtc0: <EFI Realtime Clock>
efirtc0: registered as a time-of-day clock, resolution 1.000000s
# RTC 时钟

smbios0: <System Management BIOS> at iomem 0x75ca6000-0x75ca6017
smbios0: Version: 3.6
aesni0: <AES-CBC,AES-CCM,AES-GCM,AES-ICM,AES-XTS,SHA1,SHA256>
acpi0: <ALASKA A M I >
Firmware Error (ACPI): Could not resolve symbol [\134_SB.PC00.TXHC.RHUB.SS01], AE_NOT_FOUND (20241212/dswload2-315)
ACPI Error: AE_NOT_FOUND, During name lookup/catalog (20241212/psobject-372)
Firmware Error (ACPI): Could not resolve symbol [\134_SB.PC00.TXHC.RHUB.SS02], AE_NOT_FOUND (20241212/dswload2-315)
ACPI Error: AE_NOT_FOUND, During name lookup/catalog (20241212/psobject-372)
acpi0: Power Button (fixed)
hpet0: <High Precision Event Timer> iomem 0xfed00000-0xfed003ff on acpi0
Timecounter "HPET" frequency 19200000 Hz quality 950
Event timer "HPET" frequency 19200000 Hz quality 550
Event timer "HPET1" frequency 19200000 Hz quality 440
Event timer "HPET2" frequency 19200000 Hz quality 440
Event timer "HPET3" frequency 19200000 Hz quality 440
Event timer "HPET4" frequency 19200000 Hz quality 440
atrtc1: <AT realtime clock> on acpi0
atrtc1: Warning: Couldn't map I/O.
atrtc1: registered as a time-of-day clock, resolution 1.000000s
Event timer "RTC" frequency 32768 Hz quality 0
attimer0: <AT timer> port 0x40-0x43,0x50-0x53 irq 0 on acpi0
Timecounter "i8254" frequency 1193182 Hz quality 0
Event timer "i8254" frequency 1193182 Hz quality 100
Timecounter "ACPI-fast" frequency 3579545 Hz quality 900
acpi_timer0: <24-bit timer at 3.579545MHz> port 0x1808-0x180b on acpi0
pcib0: <ACPI Host-PCI bridge> port 0xcf8-0xcff on acpi0
pci0: <ACPI PCI bus> on pcib0
vgapci0: <VGA-compatible display> port 0x4000-0x403f mem 0x6000000000-0x6000ffffff,0x4000000000-0x400fffffff at device 2.0 on pci0
vgapci0: Boot video device
xhci0: <XHCI (generic) USB 3.0 controller> mem 0x6001120000-0x600112ffff at device 13.0 on pci0
xhci0: 32 bytes context size, 64-bit DMA
usbus0 on xhci0
usbus0: 5.0Gbps Super Speed USB v3.0
pci0: <simple comms, UART> at device 18.0 (no driver attached)
xhci1: <XHCI (generic) USB 3.0 controller> mem 0x6001100000-0x600110ffff at device 20.0 on pci0
xhci1: 32 bytes context size, 64-bit DMA
usbus1 on xhci1
usbus1: 5.0Gbps Super Speed USB v3.0
pci0: <memory, RAM> at device 20.2 (no driver attached)
pci0: <simple comms> at device 22.0 (no driver attached)
sdhci_pci0: <Generic SD HCI> mem 0x6001149000-0x6001149fff at device 26.0 on pci0
sdhci_pci0: 1 slot(s) allocated
uma_zalloc_debug: zone "malloc-16" with the following non-sleepable locks held:
exclusive sleep mutex SD slot mtx (sdhci) r = 0 (0xfffff80001ad9020) locked @ /usr/src/sys/dev/sdhci/sdhci.c:688
stack backtrace:
#0 0xffffffff80bcc76c at witness_debugger+0x6c
#1 0xffffffff80bcd980 at witness_warn+0x430
#2 0xffffffff80f05784 at uma_zalloc_debug+0x34
#3 0xffffffff80f052d7 at uma_zalloc_arg+0x27
#4 0xffffffff80b27bdd at malloc+0x7d
#5 0xffffffff80b28592 at reallocf+0x12
#6 0xffffffff80b9367d at devclass_add_device+0x1cd
#7 0xffffffff80b91c2b at make_device+0x10b
#8 0xffffffff80b91a6d at device_add_child_ordered+0x2d
#9 0xffffffff8086f42c at sdhci_card_task+0x1fc
#10 0xffffffff80875021 at sdhci_pci_attach+0x491
#11 0xffffffff80b93e8b at device_attach+0x45b
#12 0xffffffff80b951fa at bus_attach_children+0x4a
#13 0xffffffff8082ba77 at pci_attach+0xd7
#14 0xffffffff80f52775 at acpi_pci_attach+0x15
#15 0xffffffff80b93e8b at device_attach+0x45b
#16 0xffffffff80b951fa at bus_attach_children+0x4a
#17 0xffffffff80f55ad8 at acpi_pcib_acpi_attach+0x428
mmc0: <MMC/SD bus> on sdhci_pci0
pcib1: <ACPI PCI-PCI bridge> at device 28.0 on pci0
pci1: <ACPI PCI bus> on pcib1
pci1: <network> at device 0.0 (no driver attached)
pcib2: <ACPI PCI-PCI bridge> at device 28.6 on pci0
pci2: <ACPI PCI bus> on pcib2
igc0: <Intel(R) Ethernet Controller I226-V> mem 0x80500000-0x805fffff,0x80600000-0x80603fff at device 0.0 on pci2
igc0: EEPROM V2.17-0 eTrack 0x80000303
igc0: Using 1024 TX descriptors and 1024 RX descriptors
igc0: Using 4 RX queues 4 TX queues
igc0: Using MSI-X interrupts with 5 vectors
igc0: Ethernet address: 10:02:b5:86:0e:f9
igc0: netmap queues/slots: TX 4/1024, RX 4/1024
pcib3: <ACPI PCI-PCI bridge> at device 29.0 on pci0
pci3: <ACPI PCI bus> on pcib3
nvme0: <Generic NVMe Device> mem 0x80700000-0x80703fff at device 0.0 on pci3
isab0: <PCI-ISA bridge> at device 31.0 on pci0
isa0: <ISA bus> on isab0
hdac0: <Intel Alder Lake-N HDA Controller> mem 0x6001140000-0x6001143fff,0x6001000000-0x60010fffff at device 31.3 on pci0
pci0: <serial bus> at device 31.5 (no driver attached)
acpi_button0: <Sleep Button> on acpi0
cpu0: <ACPI CPU> on acpi0
acpi_button1: <Power Button> on acpi0
acpi_tz0: <Thermal Zone> on acpi0
acpi_syscontainer0: <System Container> on acpi0
acpi_syscontainer1: <System Container> on acpi0
atrtc0: <AT realtime clock> at port 0x70 irq 8 on isa0
atrtc0: Warning: Couldn't map I/O.
atrtc0: registered as a time-of-day clock, resolution 1.000000s
atrtc0: Can't map interrupt.
atrtc0: non-PNP ISA device will be removed from GENERIC in FreeBSD 15.
hwpstate_intel0: <Intel Speed Shift> on cpu0
cpufreq0: <CPU frequency control> on cpu0
hwpstate_intel1: <Intel Speed Shift> on cpu1
cpufreq1: <CPU frequency control> on cpu1
hwpstate_intel2: <Intel Speed Shift> on cpu2
cpufreq2: <CPU frequency control> on cpu2
hwpstate_intel3: <Intel Speed Shift> on cpu3
cpufreq3: <CPU frequency control> on cpu3
Timecounter "TSC" frequency 806401362 Hz quality 1000
Timecounters tick every 1.000 msec
ugen1.1: <Intel XHCI root HUB> at usbus1
ugen0.1: <Intel XHCI root HUB> at usbus0
uhub0 on usbus1
uhub0: <Intel XHCI root HUB, class 9/0, rev 3.00/1.00, addr 1> on usbus1
uhub1 on usbus0
uhub1: <Intel XHCI root HUB, class 9/0, rev 3.00/1.00, addr 1> on usbus0
ZFS filesystem version: 5
ZFS storage pool version: features support (5000)
mmcsd0: 125GB <MMCHC Y2P128 0.0 SN F034273C MFG 04/2023 by 155 0x0000> at mmc0 200.0MHz/8bit/8192-block
mmcsd0boot0: 4MB partition 1 at mmcsd0
mmcsd0boot1: 4MB partition 2 at mmcsd0
mmcsd0rpmb: 17MB partition 3 at mmcsd0
uhub1: 2 ports with 2 removable, self powered
nvme0: Allocated 16MB host memory buffer
hdacc0: <Realtek ALC269 HDA CODEC> at cad 0 on hdac0
hdaa0: <Realtek ALC269 Audio Function Group> at nid 1 on hdacc0
pcm0: <Realtek ALC269 (Right Analog)> at nid 21 and 24 on hdaa0
nda0 at nvme0 bus 0 scbus0 target 0 lun 1
nda0: <Fanxiang S530Q 500GB SN14243 FX240960178>
nda0: Serial Number FX240960178
nda0: nvme version 1.4
nda0: 476940MB (976773168 512 byte sectors)
Trying to mount root from zfs:zroot/ROOT/default []...
WARNING: WITNESS option enabled, expect reduced performance.
uhub0: 16 ports with 16 removable, self powered
Root mount waiting for: usbus1
ugen1.2: <Realtek Bluetooth Radio> at usbus1
ichsmb0: <Intel Alder Lake SMBus controller> port 0xefa0-0xefbf mem 0x6001148000-0x60011480ff at device 31.4 on pci0
smbus0: <System Management Bus> on ichsmb0
rtw890: <rtw89_8852be> port 0x3000-0x30ff mem 0x80800000-0x808fffff at device 0.0 on pci1
rtw890: successfully loaded firmware image 'rtw89/rtw8852b_fw-1.bin'
rtw890: loaded firmware rtw89/rtw8852b_fw-1.bin
rtw890: Firmware version 0.29.29.5 (da87cccd), cmd version 0, type 5
rtw890: Firmware version 0.29.29.5 (da87cccd), cmd version 0, type 3
rtw890: chip rfe_type is 5
acpi_wmi0: <ACPI-WMI mapping> on acpi0
acpi_wmi0: cannot find EC device
acpi_wmi0: Embedded MOF found
ACPI: \134_SB.WFDE.WQCC: 1 arguments were passed to a non-method ACPI object (Buffer) (20241212/nsarguments-361)
acpi_wmi1: <ACPI-WMI mapping> on acpi0
acpi_wmi1: cannot find EC device
acpi_wmi1: Embedded MOF found
ACPI: \134_SB.WFTE.WQCC: 1 arguments were passed to a non-method ACPI object (Buffer) (20241212/nsarguments-361)
lo0: link state changed to UP
igc0: link state changed to UP
ubt0 on uhub0
ubt0: <Realtek Bluetooth Radio, class 224/1, rev 1.00/0.00, addr 1> on usbus1
Security policy loaded: MAC/ntpd (mac_ntpd)
```

## 参考文献

- Linux Foundation. Filesystem Hierarchy Standard 3.0[EB/OL]. (2015-06-03)[2026-04-23]. <https://refspecs.linuxfoundation.org/fhs.shtml>.
- FreeBSD Project. hier(7)[EB/OL]. [2026-03-26]. <https://man.freebsd.org/cgi/man.cgi?query=hier&sektion=7&manpath=freebsd-release-ports>. 系统阐述 FreeBSD 文件系统层次结构。
- FreeBSD Project. chflags(1)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=chflags>.
- FreeBSD Project. ls(1)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=ls>.

## 课后习题

1. 使用 `tree` 或 `find` 命令遍历 FreeBSD 的目录树结构，与 Ubuntu 最新 LTS 版本在 `/etc`、`/usr`、`/var` 三个目录的组织方式上进行对比分析。
2. 查阅 FreeBSD 源代码中 `hier(7)` 的定义，分析其目录结构设计所遵循的层次化原则。
3. 修改 `/tmp` 目录的默认权限配置（如将权限从 `1777` 改为 `1755`），记录修改后对临时文件创建和系统服务运行的影响。
