# 4.3 系统目录结构

FreeBSD 遵循 hier(7) 规范组织文件系统层次结构，根目录 / 在系统启动时首个被挂载，包含进入多用户模式所需的基本系统。本节逐级解释根目录下各子目录的功能与设计原则。

## 目录结构概览

根目录（/）是文件系统的最顶层目录，在系统启动时第一个被挂载，包含操作系统进入多用户模式所需的基本系统。根目录还包含其他文件系统的挂载点。挂载点是附加文件系统可以挂载到父文件系统（通常是根文件系统）上的目录。标准挂载点包括 `/usr/`、`/var/`、`/tmp/`、`/mnt/` 和 `/media/`。完整的文件系统层次结构描述参见 hier(7)。

## FreeBSD 目录结构的设计原则

FreeBSD 的目录结构设计遵循以下原则：

- **单一根目录原则**：与 Windows 等系统采用多根（多盘符）的设计不同，UNIX 系统采用单一根目录（`/`）作为整个文件系统的起点。所有存储设备、分区和网络文件系统均以挂载的方式接入统一的目录树中。

- **功能分离原则**：将不同功能的文件分配到不同的目录中，各文件系统可独立管理、挂载和备份。例如，将系统二进制文件（`/bin`、`/sbin`）与用户应用程序（`/usr/local`）分离，将配置文件（`/etc`）与日志数据（`/var/log`）分离。`/var` 包含日志目录、假脱机目录和临时文件，可能被填满，因此应与 `/` 分离。

- **基本系统与第三方软件分离原则**：FreeBSD 将基本系统与第三方软件严格分离。基本系统组件安装在 `/bin`、`/sbin`、`/usr/bin`、`/usr/sbin`、`/usr/lib` 等目录中，通过 Ports 或 pkg 安装的第三方软件统一安装到 `/usr/local/` 下的对应子目录中（如 `/usr/local/bin`、`/usr/local/lib`、`/usr/local/etc`）。

- **静态与动态数据分离原则**：静态数据（如二进制文件、库文件、文档）与动态数据（如日志、临时文件、运行时数据）分别存储于不同的目录树中。`/usr` 主要存放静态的只读数据，`/var` 则存放可变的运行时数据，`/tmp` 存放临时文件。

## FHS 与 FreeBSD 目录结构

文件系统层次标准（FHS）由 Linux 基金会 Linux 标准基础工作组（Linux Standard Base, LSB）维护，定义了类 UNIX 操作系统中目录结构和目录内容的规范，当前版本为 FHS 3.0，发布于 2015 年。

FreeBSD 的目录层次由 `hier(7)` 手册页定义。与 FHS 相比，FreeBSD 的目录结构存在以下差异：

| 项目 | FHS | FreeBSD |
| ---- | --- | ------- |
| `/usr/local` | 供管理员本地安装软件时使用，初始为空 | pkg/ports 安装第三方软件默认路径 |
| 配置文件 | 第三方 `/etc/opt`，建议使用子目录 | 第三方 `/usr/local/etc`，系统 `/etc` |
| `/bin`、`/sbin`、`/lib` | 独立目录，与 `/usr` 分离 | 独立目录，与 `/usr` 分离 |
| `/libexec` | 可选，与 `/usr/lib` 二选一，存放内部二进制 | `/` 和 `/usr` 下均有，系统辅助程序 |
| `/rescue` | 未定义 | 静态链接紧急修复工具 |
| `/srv` | 系统提供的服务数据（ftp、www 等） | 未定义 |
| `/opt` | `/opt/<package>` | 未定义，统一用 `/usr/local` |
| `/media` | 可移动介质挂载点 | 由 automount(8) 或 bsdisks(8) 管理 |
| `/mnt` | 临时挂载点 | 临时挂载点 |
| `/run` | 必选（3.0），PID 文件及 UNIX 域套接字 | 无，沿用 `/var/run` |
| `/sys` | Linux sysfs（§6.1.7） | 无，用 sysctl(8) |
| `/proc` | Linux procfs（§6.1.5） | procfs(4) 已废弃，仅出于兼容目的保留，默认不使用 |
| 共享库 | `/lib` 关键库，`/usr/lib` 非关键及编程库，`/lib<qual>` 兼容 | `/lib` 关键库，`/usr/lib` 共享/ar 库，`/usr/lib32` |
| 内核 | `/` 或 `/boot` | `/boot/kernel/`，备用 `/boot/kernel.old/` |
| `/home` | 可选，用户家目录 | 用户家目录 |
| `/var/empty` | 未定义 | 由 sshd(8) 特权分离 chroot 使用 |
| `/nonexistent` | 未定义 | 无家目录账户的占位符 |

FHS 按可共享/不可共享、静态/可变两个维度将文件分层：`/usr` 可共享只读，`/var` 可变，根文件系统仅需满足引导、恢复、修复的最低需求。FreeBSD 遵循此原则，基本系统限定在 `hier(7)` 定义目录，第三方软件限定在 `/usr/local`。

POSIX（IEEE 1003.1）/SUS（UNIX 03）对目录结构无类似要求。POSIX.1-2008 明确删除了 `/bin`、`/usr/bin`、`/lib`、`/usr/lib` 等描述——理由是对应用程序没有用处。POSIX 仅要求 `/`、`/dev`（含 `/dev/null`、`/dev/tty`、`/dev/console`）、`/tmp` 存在，临时文件建议通过 `TMPDIR` 环境变量定位。FHS 仅在个别条目中注明与 POSIX 一致（如 `/tmp` 行为、`[`/`test` 路径、手册页 locale 命名），其余目录规范均属 FHS 自身定义，不在 POSIX 范围内。

为便于说明，仅列出前三级目录及重要文件。

```sh
/
├── COPYRIGHT FreeBSD 版权信息文件
├── bin 基本的 BSD 用户工具，参见 intro(1)
├── boot 操作系统引导过程中使用的程序和配置文件，参见 boot(8)
│   ├── defaults 存放默认引导配置文件，参见 loader.conf(5)
│   │   └── loader.conf 引导加载程序配置文件，参见 loader.conf(5)
│   ├── device.hints 用于控制驱动程序的内核变量，参见 device.hints(5)
│   ├── dtb 编译的扁平化设备树（FDT）文件，参见 fdt(4) 和 dtc(1)；x86 架构下应为空
│   │   └── overlays 编译的 FDT 覆盖层，参见 loader.conf(5) 中的 fdt_overlays
│   ├── efi EFI 系统分区（ESP）挂载点，参见 uefi(8)
│   ├── firmware 可加载的二进制固件内核模块；pkg kmod 会安装至此，以及通过 fwget 下载的固件
│   ├── fonts 二进制位图控制台字体，参见 loader.conf(5) 和 vtfontcvt(8)
│   ├── images beastie 启动菜单图像，参见 loader_lua(8)
│   ├── kernel 内核及内核模块，参见 kldstat(8)
│   ├── kernel.old 备用内核及内核模块
│   ├── loader.conf loader 配置文件，参见 loader.conf(5)
│   ├── loader.conf.d loader 补充配置目录，参见 loader.conf(5)
│   ├── lua 引导加载程序的 Lua 脚本，包含启动时显示的 ASCII 艺术字（图）等，参见 loader_lua(8)
│   ├── modules 第三方可加载内核模块，如通过 pkg(8) 或 ports(7) 安装的模块
│   ├── uboot 空目录
│   └── zfs 存放 ZFS 存储池（Zpool）的缓存文件，参见 zpool(8)
│       └── zpool.cache 硬编码的磁盘驱动器路径，参见 zpool(8)
├── compat 支持与其他操作系统二进制兼容的文件
│   └── linux Linux 兼容层运行时的默认位置，参见 linux(4)
├── dev 设备文件和特殊文件，参见 intro(4) 和 devfs(4)
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
│   ├── reroot `reboot -r` 使用的重引导设备
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
│   ├── devfs.conf 启动时 devfs 设备规则配置，参见 devfs.conf(5)
│   ├── dma DMA 邮件代理相关，参见 dma(8)
│   ├── freebsd-update.conf 基本系统更新工具 freebsd-update 的配置文件，参见 freebsd-update(8)
│   ├── fstab 文件分区表，参见 fstab(5)
│   ├── gss GSSAPI 相关文件、含 Kerberos 5
│   ├── hosts hosts 文件，优先于 DNS 的本地 IP 域名映射表
│   ├── inetd.conf 配置 BSD inetd，参见 inetd(8)
│   ├── jail.conf.d 用于 jail 配置的模块化管理，默认为空（jail.conf(5)）
│   ├── kyua Kyua 测试框架的全局配置文件（kyua(1)、kyua.conf(5)）
│   ├── localtime 本地时区文件，参见 ctime(3)。在测试系统中，localtime 被链接到了 /usr/share/zoneinfo/Asia/Shanghai
│   ├── login.conf 登录类功能数据库，参见 login.conf(5)
│   ├── machine-id 系统的 UUID，供 D-Bus 使用
│   ├── mail Sendmail 相关文件，参见 sendmail(8)
│   │   ├── aliases 用于投递系统邮件的地址
│   │   └── mailer.conf mailwrapper(8) 配置文件
│   ├── motd.template TTY 登录后显示的信息，参见 motd(5)
│   ├── mtree 系统初始化与验证，可用于系统审计，参见 mtree(8)
│   ├── newsyslog.conf.d newsyslog 的配置文件，参见 newsyslog.conf(5)
│   ├── ntp NTP 相关，参见 ntp.conf(5)、ntpd(8)
│   ├── ntp.conf NTP 客户端配置文件，参见 ntpd(8)
│   ├── pam.d 可插拔认证模块（PAM）相关的配置文件，参见 pam(3)
│   ├── periodic 存放定期执行的维护脚本，由 cron 调用，参见 periodic(8)
│   ├── pf.conf PF 防火墙配置文件，参见 pf(4)
│   ├── pkg PKG 相关配置文件，参见 pkg(8)
│   ├── ppp PPP 相关配置，参见 ppp(8)
│   ├── profile.d 存放用户登录时可执行的 Shell 脚本，不会自动加载
│   ├── rc.conf 系统启动配置文件，参见 rc.conf(5)
│   ├── rc.conf.d 存放特定服务的配置文件，默认为空
│   ├── rc.d 用于启动和管理系统服务的 RC 脚本，参见 rc(8)
│   ├── resolv.conf DNS 解析配置文件，参见 resolv.conf(5)
│   ├── resolvconf.conf DNS 配置管理器配置，通常由 local-unbound 生成，参见 local-unbound(8) 或 resolvconf(8)
│   ├── security OpenBSM 审计配置文件，参见 audit(8)
│   ├── ssh SSH 和 SSHD 相关配置文件，参见 ssh(1)
│   ├── ssl SSL/TLS 证书、密钥等
│   │   ├── cert.pem 系统信任库的捆绑形式，参见 certctl(8)
│   │   ├── certs 系统信任库的 OpenSSL 哈希目录形式，参见 certctl(8)
│   │   ├── openssl.cnf OpenSSL 配置文件，参见 openssl.cnf(5)
│   │   └── untrusted 明确不信任的证书，参见 certctl(8)
│   ├── sysctl.conf 内核状态默认值，参见 sysctl.conf(5)
│   ├── sysctl.kld.d 特定内核模块的配置文件，默认为空，参见：D40886[EB/OL]. [2026-03-26]. <https://reviews.freebsd.org/D40886>.
│   ├── syslog.conf 系统日志配置文件
│   ├── syslog.d syslogd 的配置文件，参见 syslogd(8)
│   ├── ttys 创建 TTY 的规则文件，参见 getty(8)
│   ├── unbound Unbound 配置文件
│   ├── wpa_supplicant.conf 连接 WiFi 的配置文件，参见 wpa_supplicant.conf(5)
│   ├── X11 X11 相关，如 XRDP
│   └── zfs ZFS 相关配置文件，参见 zfs(8)
├── home 普通用户家目录；典型用户 beastie 的家目录为 /home/beastie/
│   └── ykla 普通用户 ykla 的家目录
├── lib /bin、/sbin 所需的关键库文件
│   ├── geom GEOM 库，参见 geom(8)
│   └── nvmecontrol NVMe 相关工具，参见 nvmecontrol(8)
├── libexec 系统辅助程序，供 /bin、/sbin 中的二进制文件调用
│   └── resolvconf 管理 DNS 解析配置的程序，参见 resolvconf.conf(5)
├── media 媒体文件挂载点，如 U 盘、光盘；参见 automount(8)，或使用桌面环境时参见 bsdisks(8)
├── mnt 用作临时挂载点的空目录
├── net NFS 共享挂载点，参见 auto_master(5)
├── nonexistent 不存在的目录；按照惯例，作为不需要家目录的用户账户的家目录；参见 /var/empty/。守护进程账户（如 www、nobody、bind）的家目录通常设为此路径，表示这些账户不需要可写的家目录
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
│   │   ├── Xorg.0.log X 服务器日志（若安装 X(7)），轮替为 Xorg.0.log.old
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
│   │   ├── security 安全事件日志
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
└── zroot 由 ZFS 在创建名为 "zroot" 的存储池时自动生成的挂载点目录；`zroot` 是 FreeBSD 安装程序默认的根池名称（参见 zpool(8) 和 zfs(8) 的 `mountpoint` 属性）。该目录自身通常为空，其子文件系统（如 zroot/ROOT、zroot/usr、zroot/var 等）分别挂载到对应路径；仅当直接在 zpool 根数据集下创建文件时，内容才会出现在此目录中
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

在 FreeBSD 中，设备节点由 devfs(5) 文件系统自动管理。devfs 是一个虚拟文件系统，在系统启动时由内核自动挂载到 `/dev`，并根据当前系统中存在的硬件设备动态创建和删除设备节点。这与传统 UNIX 系统需要手动使用 `mknod` 命令创建设备节点的做法不同。devfs 确保了 `/dev` 目录中只包含当前系统实际存在的设备节点。

设备节点分为两种类型：字符设备（character device）和块设备（block device）。字符设备以字节流方式访问数据，如终端（`/dev/ttyv0`）和串口；块设备以固定大小的块为单位访问数据，如磁盘（`/dev/ada0`）。在 `ls -l` 的输出中，字符设备的类型标识为 `c`，块设备的类型标识为 `b`。

设备命名遵循一定的约定：SATA 硬盘以 `ada` 开头（如 `ada0`、`ada1`），SCSI 硬盘和 USB 存储设备以 `da` 开头（如 `da0`），NVMe 存储以 `nvd` 或 `nda` 开头，CD-ROM 驱动器以 `cd` 开头。编号从 0 开始。GPT 分区在设备名后附加 `p` 加分区号（如 `ada0p1`），MBR 切片附加 `s` 加切片号（如 `ada0s1`）。

## 启动消息 dmesg

当 FreeBSD 启动时，大多数启动消息都与正在检测的设备有关。启动消息的副本保存在 `/var/run/dmesg.boot` 中。

以下示例是 Radxa X4 16G 128G eMMC 款在 15.0-CURRENT 下完整的启动消息内容。

```sh
# ----- 内核启动标记 -----
---<<BOOT>>---
# 此行标记内核开始输出启动消息。此前的引导加载程序（loader）输出不会出现在 dmesg 缓冲区中，
# 因为 dmesg 缓冲区由内核在初始化时创建。引导加载程序消息（启动菜单）只能通过串口控制台或屏幕查看。

# ----- 版权声明 -----
Copyright (c) 1992-2025 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
	The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
# 第一行声明 FreeBSD 项目的版权（FreeBSD 独有的代码，始于 1992 年）。
# 第二行声明加州大学董事会（The Regents）的版权——这是 4.3BSD Net/2 及之前 BSD 版本的版权持有者。
# 年份跨度 1979-1994 代表了 BSD 从 3BSD 到 4.4BSD-Lite2 的完整历史。
# 第三行声明 FreeBSD Foundation 持有“FreeBSD”注册商标。

# ----- 内核版本标识 -----
FreeBSD 15.0-CURRENT #0 main-n275588-045a4c108fcf: Fri Feb 21 02:25:56 UTC 2025
    root@releng3.nyi.freebsd.org:/usr/obj/usr/src/amd64.amd64/sys/GENERIC amd64
# 格式：<系统名称> <版本>-<分支> #<构建号> <Git 提交哈希>: <构建日期时间>
# 15.0-CURRENT：开发分支（非正式发行版）。
# #0：该内核配置的第 0 次构建（config(8) 构建计数）。
# main-n275588-045a4c108fcf：Git main 分支的快照标识。
# 第二行：构建主机（root@releng3.nyi.freebsd.org）、构建目录路径、内核配置文件（GENERIC）、目标架构（amd64）。

# ----- 编译器信息 -----
FreeBSD clang version 19.1.7 (https://github.com/llvm/llvm-project.git llvmorg-19.1.7-0-gcd708029e0b2)
# FreeBSD 基本系统编译器版本。FreeBSD 当前版本的内核由 Clang 19.1.7 编译。
# FreeBSD 从 10.0 起将 Clang 作为默认系统编译器，替代了 GCC。

# ----- 调试选项警告 -----
WARNING: WITNESS option enabled, expect reduced performance.
# WITNESS 是内核死锁检测和锁顺序验证机制。启用后会令每次锁获取都进行验证，
# 带来显著的性能开销（通常 10%-30% 的吞吐量损失）。CURRENT 分支内核默认启用，
# 用于在开发过程中捕获锁顺序错误（lock order reversal）。RELEASE/STABLE 版本禁用此选项。

# ----- 控制台与显示设备 -----
VT(efifb): resolution 800x600
# VT（Virtual Terminal，Newcons）：FreeBSD 新一代系统控制台驱动（替代了 syscons）。
# efifb：通过 EFI 固件提供的帧缓冲区（framebuffer）驱动来显示。
# UEFI 固件默认将显示分辨率设为 800x600。若 drm（Direct Rendering Manager）驱动加载后，分辨率可升至显示器原生分辨率。

# ===== CPU 检测与特性枚举 =====
CPU: Intel(R) N100 (806.40-MHz K8-class CPU)
# CPU 型号名称。Intel N100 是 Alder Lake-N 架构的低功耗处理器。
# 806.40 MHz 是启动时 CPU 的基础频率（base frequency），加载 hwpstate_intel(4) 
# 后内核会通过 Intel Speed Shift 动态调整频率（N100 最高睿频可达 ~3.4 GHz）。
# "K8-class" 表示该 CPU 支持 AMD64 指令集（AMD K8 是首个 x86-64 处理器）；
# 内核代码以 AMD K8 为 AMD64 功能基线进行分类。

  Origin="GenuineIntel"  Id=0xb06e0  Family=0x6  Model=0xbe  Stepping=0
# Origin：CPU 厂商字符串，GenuineIntel = Intel。Family/Model/Stepping 用于微码更新匹配。

  Features=0xbfebfbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,DTS,ACPI,MMX,FXSR,SSE,SSE2,SS,HTT,TM,PBE>
# 基础 x86 特性（CPUID 叶子 1 的 EDX 寄存器）。涵盖 32 位时代的全部标准特性：
# FPU（x87 浮点）、VME（虚拟 8086 模式增强）、TSC（时间戳计数器）、APIC 等。
# SSE/SSE2：Streaming SIMD Extensions，Intel P4 时代引入的 128 位 SIMD。

  Features2=0x7ffafbbf<SSE3,PCLMULQDQ,DTES64,MON,DS_CPL,VMX,EST,TM2,SSSE3,SDBG,FMA,CX16,xTPR,PDCM,PCID,SSE4.1,SSE4.2,x2APIC,MOVBE,POPCNT,TSCDLT,AESNI,XSAVE,OSXSAVE,AVX,F16C,RDRAND>
# ECX 扩展特性（CPUID 叶子 1 的 ECX 寄存器）：
# VMX：Intel 虚拟化技术（VT-x），bhyve(8) 依赖此特性。
# AESNI：AES 指令集，加速加密操作（OpenSSL/ZFS 加密均可受益）。
# AVX：256 位 SIMD，浮点运算密集场景的加速指令。
# RDRAND：硬件随机数生成器，为 random(4) 提供熵源。

  AMD Features=0x2c100800<SYSCALL,NX,Page1GB,RDTSCP,LM>
  AMD Features2=0x121<LAHF,ABM,Prefetch>
# AMD 扩展特性（Intel 实现 AMD64 后也报告这些位）：
# SYSCALL：快速系统调用指令（AMD64 ABI 的核心）。NX：不可执行页位（W^X 安全机制）。
# LM（Long Mode）：64 位支持。Page1GB：1GB 大页支持。

  Structured Extended Features=0x239ca7eb<FSGSBASE,TSCADJ,BMI1,AVX2,FDPEXC,SMEP,BMI2,ERMS,INVPCID,NFPUSG,PQE,RDSEED,ADX,SMAP,CLFLUSHOPT,CLWB,PROCTRACE,SHA>
# 结构化扩展特性（CPUID 叶子 7、子叶 0 的 EBX）：
# SMEP（Supervisor Mode Execution Protection）：内核态阻止执行用户态代码——关键安全特性。
# SMAP（Supervisor Mode Access Prevention）：内核态阻止访问用户态内存。
# AVX2：256 位整数 SIMD 扩展，提升媒体处理/加解密性能。
# RDSEED：与 RDRAND 互补的更强随机数指令（通过熵源直接生成而非增强后输出）。

  Structured Extended Features2=0x98c007bc<UMIP,PKU,OSPKE,WAITPKG,GFNI,VAES,VPCLMULQDQ,RDPID,MOVDIRI,MOVDIR64B>
# 结构化扩展特性 2（叶子 7、子叶 0 的 ECX）：
# UMIP/OSPKE：内存保护增强。WAITPKG：Intel 用户态等待指令包，用于自旋等待优化。
# GFNI/VAES/VPCLMULQDQ：Intel 10nm+ 引入的 Galois Field/AES 加速指令，显著加速加密操作。

  Structured Extended Features3=0xfc184410<FSRM,MD_CLEAR,IBT,IBPB,STIBP,L1DFL,ARCH_CAP,CORE_CAP,SSBD>
# 结构化扩展特性 3（叶子 7、子叶 0 的 EDX）：
# MD_CLEAR：支持 VERW 指令清除微架构缓冲区（MDS 缓解）。
# IBPB/STIBP/SSBD：Spectre/Meltdown 系列侧信道漏洞的硬件缓解控制位。
# FSRM：快速短 REP MOVSB（memcpy 加速），配合 ERMS 使用。

  XSAVE Features=0xf<XSAVEOPT,XSAVEC,XINUSE,XSAVES>
# XSAVE：x86 上下文保存/恢复扩展（CPUID 叶子 D、子叶 1 的 EAX）。
# XSAVEOPT/XSAVES：优化的状态保存，减少上下文切换开销。

  IA32_ARCH_CAPS=0x180fd6b<RDCL_NO,IBRS_ALL,SKIP_L1DFL_VME,MDS_NO,TAA_NO>
# IA32_ARCH_CAPABILITIES（MSR 0x10A）：Intel 架构能力 MSR，硬件报告自身安全特性。
# RDCL_NO：不受 RIDL / MDS 漏洞影响。MDS_NO/TAA_NO：不受微架构数据采样攻击影响。
# 这些标志位影响系统安全评估——它们表示该 CPU 不需要对应安全缓解措施。

  VT-x: PAT,HLT,MTF,PAUSE,EPT,UG,VPID,VID,PostIntr
# VT-x（Intel 虚拟化技术）子特性集：
# EPT（Extended Page Tables）：二级地址转换（SLAT），bhyve 的核心依赖，大幅提升虚拟机内存性能。
# VPID（Virtual Processor Identifier）：TLB 标记，避免 VM 切换时刷新 TLB。
# VID（Virtual Interrupt Delivery）：硬件直通中断分发。PostIntr：Posted Interrupt 支持。

  TSC: P-state invariant, performance statistics
# TSC（时间戳计数器）特性：Invariant TSC 意味着不受 P-state（频率调节）和 C-state（休眠）影响，内核可将其用作高精度单调时钟源（timecounter）。

# ===== 物理内存检测 =====
real memory  = 17179869184 (16384 MB)
# 硬件实际提供的物理内存总量（16 GB）。

avail memory = 16318308352 (15562 MB)
# 内核可用的物理内存。差值（约 822 MB）包括：
# 1) 内核代码与静态数据段占用的内存。2) 内核内存分配器（kmem）预保留的内存。
# 3) BIOS/UEFI 固件内存映射中标记为保留（reserved）的内存区域。
# 4) 某些 PCI 设备 MMIO 区域映射所占用的地址空间。

# ===== 事件计时器 =====
Event timer "LAPIC" quality 600
# LAPIC（Local APIC）计时器质量评分。内核维护多个计时器源，quality 值越高优先级越大。
# 600 分相对较高（HPET 为 550（Event）/950（Timecounter），TSC 为 1000（最高优先级））。
# 内核启动时会遍历所有计时器并按 quality 降序选择最佳可用源。

# ===== ACPI 子系统 =====
ACPI APIC Table: <ALASKA A M I >
# ACPI APIC（MADT）表供应商信息。"ALASKA A M I" 表明 BIOS 由 AMI（American Megatrends Inc.）
# 提供，主板厂商为 ASRock（Alaska 是其产品线内部代号）。

WARNING: L3 data cache covers more APIC IDs than a package (7 > 3)
# L3 缓存共享 APIC ID 范围与 BSP（Bootstrap Processor）报告值不一致，
# 可能是 BIOS/Firmware ACPI 表存在小问题，不影响正常使用。此问题常见于低功耗平台。

# ===== SMP（对称多处理）初始化 =====
FreeBSD/SMP: Multiprocessor System Detected: 4 CPUs
FreeBSD/SMP: 1 package(s) x 4 core(s)
# SMP 检测结果。1 个物理插槽（package）× 4 个核心（core）。
# Intel N100 为 4 核 4 线程（不支持超线程），因此逻辑 CPU 数 = 物理核心数。

# ===== 随机数子系统初始化 =====
random: registering fast source Intel Secure Key RNG
random: fast provider: "Intel Secure Key RNG"
random: unblocking device.
# FreeBSD 随机数子系统（random(4)）初始化流程：
# 1) 注册快速的 Intel Secure Key RNG（RDRAND 指令）作为硬件熵源。
# 2) 标记 fast provider（快速提供者）为 "Intel Secure Key RNG"。
# 3) unblocking device：当内核收集到足够早期熵后，/dev/random 解除阻塞，
#    用户态程序从此可正常读取随机数。CURRENT 版本使用 FenestrasX 算法。

# ===== I/O APIC 与 AP 启动 =====
ioapic0 <Version 2.0> irqs 0-119
# I/O APIC（高级可编程中断控制器）版本 2.0，支持 120 条 IRQ 线（0-119），
# 负责将 PCI 设备中断请求分发至对应 CPU 核心（LAPIC）。

Launching APs: 2 1 3
# AP（Application Processor，应用处理器）启动顺序。BSP（Bootstrap Processor）为 CPU 0，
# 在 AP 启动前已经运行，后续逐核启动：CPU 2 → CPU 1 → CPU 3。
# 启动顺序由 APIC ID 和拓扑算法决定，通常先启动与 BSP 不在同一物理核心的 AP。

random: entropy device external interface
# random(4) 外部熵接口注册完毕。用户态程序可以开始读取 /dev/random。

# ===== 键盘多路复用器 =====
kbd0 at kbdmux0
# kbd0 连接到键盘多路复用器 kbdmux0(4)。kbdmux 允许多个键盘同时作为单一键盘设备工作
#（AT 键盘 + USB 键盘同时可用），输入被透明合并。

# ===== EFI 实时时钟 =====
efirtc0: <EFI Realtime Clock>
efirtc0: registered as a time-of-day clock, resolution 1.000000s
# efiRTC：通过 EFI 运行时服务（Runtime Services）获取/设置时间的时钟驱动。
# "time-of-day clock"：系统时间的硬件时钟源注册。1s 粒度说明 EFI RTC 只能精确到秒级，
# 在启动早期为内核提供初始时间基准。后续会使用更高精度的 TSC/HPET 作为 timecounter。

# ===== SMBIOS =====
smbios0: <System Management BIOS> at iomem 0x75ca6000-0x75ca6017
smbios0: Version: 3.6
# SMBIOS（DMI）提供主板、BIOS、系统序列号等硬件描述信息，驱动映射到内存地址处。

# ===== AES-NI 加速引擎 =====
aesni0: <AES-CBC,AES-CCM,AES-GCM,AES-ICM,AES-XTS,SHA1,SHA256>
# aesni(4) 驱动加载，提供 AES 各模式（CBC/CCM/GCM等）以及 SHA1/SHA256 硬件加速。
# GELI 全盘加密、ZFS 原生加密、IPsec、OpenSSL 等都可利用此驱动实现线速加密。

# ===== ACPI 根设备 -----
acpi0: <ALASKA A M I>
# ACPI 根设备（插槽/主板的ACPI命名空间），OEM ID = ALASKA（ASRock/N100DC-ITX 主板）。

# ----- ACPI 固件错误（非致命）-----
Firmware Error (ACPI): Could not resolve symbol [\134_SB.PC00.TXHC.RHUB.SS01], AE_NOT_FOUND (20241212/dswload2-315)
ACPI Error: AE_NOT_FOUND, During name lookup/catalog (20241212/psobject-372)
Firmware Error (ACPI): Could not resolve symbol [\134_SB.PC00.TXHC.RHUB.SS02], AE_NOT_FOUND (20241212/dswload2-315)
ACPI Error: AE_NOT_FOUND, During name lookup/catalog (20241212/psobject-372)
# BIOS/UEFI 固件 ACPI DSDT/SSDT 表中引用了不存在的 USB SuperSpeed（SS）端口符号：
# \134 是反斜杠 ACPI 名称路径转义（ACPI namespace root \），RHUB.SS01/SS02 
# 是 xHCI 的 Root Hub 下的 SuperSpeed 端口对象。AE_NOT_FOUND 表明找不到。
# 这通常是固件（BIOS/UEFI）编写的 Bug：定义了 USB 3.0 控制器的 SS 端口引用，
# 但实际的 DSDT/SSDT 表中并未声明对应设备节点。
# 影响：这两个 USB SS 端口无法使用（该平台物理上可能仅支持 USB 2.0 或无对应 USB 3.0 插槽）。

acpi0: Power Button (fixed)
# ACPI 的固定硬件电源按钮，由 acpi_button(4) 管理。

# ===== 高精度事件计时器（HPET）=====
hpet0: <High Precision Event Timer> iomem 0xfed00000-0xfed003ff on acpi0
# HPET 内存映射 I/O 地址范围。HPET 是 x86 平台替代传统 PIT/RTC 的高精度计时器。

Timecounter "HPET" frequency 19200000 Hz quality 950
# HPET 的 timecounter（时间计数器）频率 19.2 MHz，quality 950（仅次于 TSC 的 1000）。
# timecounter 用于 gettimeofday(2)/clock_gettime(2) 等精确时间获取。

Event timer "HPET" frequency 19200000 Hz quality 550
Event timer "HPET1" frequency 19200000 Hz quality 440
Event timer "HPET2" frequency 19200000 Hz quality 440
Event timer "HPET3" frequency 19200000 Hz quality 440
Event timer "HPET4" frequency 19200000 Hz quality 440
# HPET 的内部比较器（Comparator）作为 event timer（事件计时器/定时器）：
# 1 个主计时器（quality 550）+ 4 个从计时器（quality 440）。
# event timer 用于内核的 hardclock/statclock 等周期性和一次性定时中断。
# HPET1-4 的 quality 440 低于主计时器的 550，内核会优先使用主计时器，
# 仅在多 CPU 绑核（CPU binding）场景下才后续启用备用计时器。

# ===== AT 实时时钟（传统 RTC）=====
atrtc1: <AT realtime clock> on acpi0
atrtc1: Warning: Couldn't map I/O.
atrtc1: registered as a time-of-day clock, resolution 1.000000s
# 传统的 AT RTC（Motorola MC146818A 兼容），提供 date/time 设置/获取。
# Warning 表明无法映射 I/O 端口（可能 UEFI 模式下固件未分配 I/O 空间），但无实际影响。
# 现代 UEFI 平台更推荐使用 efiRTC；计划在 FreeBSD 15 中从 GENERIC 移除 AT RTC 。

Event timer "RTC" frequency 32768 Hz quality 0
# RTC 的周期性中断频率 32768 Hz（2^15 Hz），quality 0（最低优先级，仅做最后备选）。

# ===== 传统 AT 定时器（i8254 PIT）=====
attimer0: <AT timer> port 0x40-0x43,0x50-0x53 irq 0 on acpi0
# i8254 可编程间隔定时器（Programmable Interval Timer, PIT）。端口 0x40-0x43 
# 为 PIT 数据/命令端口，irq 0 为 PIT 中断。

Timecounter "i8254" frequency 1193182 Hz quality 0
# i8254 频率 = 1.193182 MHz（NTSC 彩色副载波频率 / 3，历史遗留值）。
# quality 0 = 最低优先级，仅在没有任何更高 priority timecounter 可用时使用。

Event timer "i8254" frequency 1193182 Hz quality 100
# 作为 event timer 时 quality 100，高于 RTC（0），但在现代平台上仍不如 LAPIC/HPET。

# ===== ACPI 快速计时器（ACPI PM Timer）=====
Timecounter "ACPI-fast" frequency 3579545 Hz quality 900
acpi_timer0: <24-bit timer at 3.579545MHz> port 0x1808-0x180b on acpi0
# ACPI Power Management Timer（PM Timer），频率 3.579545 MHz。24 位计数器意味着
# 约 4.7 秒计数器溢出回绕一次（2^24 / 3579545 ≈ 4.69 s），内核需在溢出前读值并累积，
# 方可作为高精度 timecounter 使用。quality 900，为中等偏高的时间计数器选择。

# ===== PCI 总线枚举 =====
pcib0: <ACPI Host-PCI bridge> port 0xcf8-0xcff on acpi0
# ACPI Host-PCI 桥（PCI 配置空间的端口映射方式，0xCF8=地址寄存器，0xCFC=数据寄存器）。

pci0: <ACPI PCI bus> on pcib0
# PCI 总线 0 绑定在 Host-PCI 桥上。内核随后枚举所有 PCI 设备并尝试匹配驱动。

# ----- 显卡 -----
vgapci0: <VGA-compatible display> port 0x4000-0x403f mem 0x6000000000-0x6000ffffff,0x4000000000-0x400fffffff at device 2.0 on pci0
# Intel N100 的集成 UHD 显卡（Alder Lake-N 内建 GPU）。device 2.0 = PCI BDF（Bus 0, Device 2, Function 0）。

vgapci0: Boot video device
# 此设备被标记为引导视频设备。UEFI GOP（Graphics Output Protocol）在此之前已将帧缓冲区
# 设置为 800x600（参见上面 VT(efifb) 行），此标记传递到内核 drm-kmod 驱动后可用作主显示输出。

# ----- USB 3.0 xHCI 控制器 0 -----
xhci0: <XHCI (generic) USB 3.0 controller> mem 0x6001120000-0x600112ffff at device 13.0 on pci0
xhci0: 32 bytes context size, 64-bit DMA
# xHCI（USB 3.0 主控制器，PCI Function 13.0）。context size=32 B 为 xHCI 数据结构大小，
# 64-bit DMA 表示支持 64 位总线地址——兼容 4GB 以上的物理内存。

usbus0 on xhci0
# usbus0（USB 总线实例）绑定在 xhci0 上。USB 核心通过此总线管理连接的 USB 设备。

usbus0: 5.0Gbps Super Speed USB v3.0
# 速率 5.0 Gbps = SuperSpeed USB 3.0 Gen1。

# ----- 未匹配驱动的设备 -----
pci0: <simple comms, UART> at device 18.0 (no driver attached)
# PCI Serial/UART 控制器未绑定驱动。可能为 Intel Trace Hub 或串口。
# "(no driver attached)" 指内核没有为此 PCI 设备 ID 匹配的驱动程序（支持表中无此 VID/DID）。

# ----- USB 3.0 xHCI 控制器 1 -----
xhci1: <XHCI (generic) USB 3.0 controller> mem 0x6001100000-0x600110ffff at device 20.0 on pci0
xhci1: 32 bytes context size, 64-bit DMA
usbus1 on xhci1
usbus1: 5.0Gbps Super Speed USB v3.0
# 第二个 xHCI 控制器（Alder Lake-N 支持多个 USB 控制器）。usbus1 独立于 usbus0。

# ----- 未匹配驱动的其他 PCI 设备 -----
pci0: <memory, RAM> at device 20.2 (no driver attached)
# 可能为 Intel 电源管理/热监控所用的 MMIO RAM 区域，不需要专用驱动。

pci0: <simple comms> at device 22.0 (no driver attached)
# 可能为 Intel Management Engine Interface（MEI/HECI）。FreeBSD 无 MEI 驱动（大部分 MEI 功能
# 是管理引擎交互（多见于服务器/工作站）。

# ----- SD/MMC 控制器 -----
sdhci_pci0: <Generic SD HCI> mem 0x6001149000-0x6001149fff at device 26.0 on pci0
sdhci_pci0: 1 slot(s) allocated
# SD/MMC 主控制器驱动（sdhci(4)），检测到 1 个 SD 卡槽。

# ----- WITNESS 调试报告（非致命）-----
uma_zalloc_debug: zone "malloc-16" with the following non-sleepable locks held:
exclusive sleep mutex SD slot mtx (sdhci) r = 0 (0xfffff80001ad9020) locked @ /usr/src/sys/dev/sdhci/sdhci.c:688
# WITNESS 检测到在持有非可睡眠锁（sleep mutex）"SD slot mtx"的情况下，
# 内核内存分配器 UMA 试图从 zone "malloc-16" 分配内存且可能挂起（sleepable）——
# 这是一个潜在的锁顺序问题（lock order reversal, LOR）。
# r = 0 = 递归计数为 0，表示非递归锁的单次获取。

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
# 调用栈 (stack backtrace) 从上到下依次为调用顺序：
# witness_debugger：WITNESS 进入调试输出。
# witness_warn：WARN 级别——非严重的锁顺序警告（非死锁）。
# uma_zalloc_debug → uma_zalloc_arg → malloc → reallocf：内存分配器检测路径。
# devclass_add_device → make_device：设备类中添加新设备实例。
# sdhci_card_task：SD 卡检测任务（在 sdhci(4) attach 上下文内执行）。
# sdhci_pci_attach → device_attach：设备驱动 attach 入口。
# bus_attach_children → ... → acpi_pcib_acpi_attach：遍历总线子设备的递归 attach 调用链，层层向上经ACPI层回到PCI桥顶的ACPI attach入口。
# 此 LOR 不影响 SD 卡正常读写，仅为 CURRENT 调试用途。

mmc0: <MMC/SD bus> on sdhci_pci0
# mmc0 总线绑定在 sd/mmc 主控制器上，后续可识别 eMMC 或 SD 卡设备。

# ===== PCI-PCI 桥与子总线 =====
# ----- PCIe 根端口 1 -----
pcib1: <ACPI PCI-PCI bridge> at device 28.0 on pci0
pci1: <ACPI PCI bus> on pcib1
pci1: <network> at device 0.0 (no driver attached)
# PCIe 桥 28.0（PCIe Root Port #1）后方连接网络设备（无线网卡），
# 此时驱动尚未加载（驱动在启动后期通过 kldload 或 devmatch 才会加载）。

# ----- PCIe 根端口 6 -----
pcib2: <ACPI PCI-PCI bridge> at device 28.6 on pci0
pci2: <ACPI PCI bus> on pcib2

# ----- Intel I226-V 有线网卡 -----
igc0: <Intel(R) Ethernet Controller I226-V> mem 0x80500000-0x805fffff,0x80600000-0x80603fff at device 0.0 on pci2
# igc(4) 驱动为 Intel I225/I226 系列 2.5 Gbps 以太网控制器。

igc0: EEPROM V2.17-0 eTrack 0x80000303
# 网卡 EEPROM 版本及 Intel 内部版本追踪号。EEPROM 存储 MAC 地址和 PHY 校准数据。

igc0: Using 1024 TX descriptors and 1024 RX descriptors
# TX/RX 描述符环形缓冲区（ring descriptor）大小。描述符是硬件 DMA 传输的元数据结构，
# 每个描述符对应一个待发送/接收的数据包缓冲区。1024 个描述符 → 最多 1024 个未处理的数据包。

igc0: Using 4 RX queues 4 TX queues
# 多队列（multi-queue）RSS 配置：4 个 CPU 对应 4 个队列，每个 CPU 独立处理自己的数据包流。

igc0: Using MSI-X interrupts with 5 vectors
# MSI-X（Message Signaled Interrupts Extended）：每队列 1 个中断向量 + 1 个管理向量 = 5。
# 相比传统 pin-based INTx 中断，MSI-X 无中断共享、无优先级冲突、可绑定至特定 CPU。

igc0: Ethernet address: 10:02:b5:86:0e:f9
# MAC 地址。永久存储在 EEPROM 中，系统启动时由 igc(4) 读出。

igc0: netmap queues/slots: TX 4/1024, RX 4/1024
# netmap(4) 高性能零拷贝网络框架兼容信息：支持 4 个硬件队列，每队列 1024 个缓冲区槽位。

# ----- PCIe 根端口 7 -----
pcib3: <ACPI PCI-PCI bridge> at device 29.0 on pci0
pci3: <ACPI PCI bus> on pcib3

# ----- NVMe SSD -----
nvme0: <Generic NVMe Device> mem 0x80700000-0x80703fff at device 0.0 on pci3
# NVMe 控制器（PCIe 设备 0.0），通过 nda(4) CAM 层驱动或 nvd(4) 直接映射驱动管理。

# ===== PCI-ISA 桥与 ISA 总线 =====
isab0: <PCI-ISA bridge> at device 31.0 on pci0
isa0: <ISA bus> on isab0
# LPC（Low Pin Count）桥在软件上表现为 PCI-ISA 桥。ISA 总线是传统 x86 接口，
# 供 atrtc(4)、atkbd(4)、uart(4) 等以 ISA 方式访问的遗留设备使用。

# ===== Intel 高保真音频控制器 =====
hdac0: <Intel Alder Lake-N HDA Controller> mem 0x6001140000-0x6001143fff,0x6001000000-0x60010fffff at device 31.3 on pci0
# Intel HDA (High Definition Audio) 控制器，挂载在 PCI Function 31.3。

pci0: <serial bus> at device 31.5 (no driver attached)
# 可能是 I2C 串行总线控制器，当前无驱动匹配。

# ===== ACPI 固定特性 =====
acpi_button0: <Sleep Button> on acpi0
# ACPI 睡眠按钮（通常在笔记本上）。

cpu0: <ACPI CPU> on acpi0
# CPU 0 的 ACPI 处理器对象（用于 _PSS/_PCT/_CST 等电源管理对象）。

acpi_button1: <Power Button> on acpi0
# ACPI 电源按钮——与前面的 fixed Power Button 的区别在于：
# "fixed" = ACPI FADT 固定硬件事件，"acpi_button1" = ACPI 命名空间中的控制方法（Control Method）电源设备。

acpi_tz0: <Thermal Zone> on acpi0
# ACPI 温控区域（temperature sensor），用于 CPU/主板的温度监测与风扇调速。

acpi_syscontainer0: <System Container> on acpi0
acpi_syscontainer1: <System Container> on acpi0
# ACPI 系统容器设备，是 NUMA/多节点系统的拓扑容器。

# ===== AT RTC (ISA 侧) =====
atrtc0: <AT realtime clock> at port 0x70 irq 8 on isa0
atrtc0: Warning: Couldn't map I/O.
atrtc0: registered as a time-of-day clock, resolution 1.000000s
atrtc0: Can't map interrupt.
atrtc0: non-PNP ISA device will be removed from GENERIC in FreeBSD 15.
# atrtc(4) 在 ISA 总线侧的探测。两个 Warning 不影响系统运行——ISA I/O 和中断在 UEFI 平台上通常不可映射。
# FreeBSD 15 计划将 atrtc 从 GENERIC 内核配置中移除（以 efirtc 和 ACPI 时钟替代）。

# ===== Intel Speed Shift (HWP) =====
hwpstate_intel0: <Intel Speed Shift> on cpu0
cpufreq0: <CPU frequency control> on cpu0
hwpstate_intel1: <Intel Speed Shift> on cpu1
cpufreq1: <CPU frequency control> on cpu1
hwpstate_intel2: <Intel Speed Shift> on cpu2
cpufreq2: <CPU frequency control> on cpu2
hwpstate_intel3: <Intel Speed Shift> on cpu3
cpufreq3: <CPU frequency control> on cpu3
# Intel Speed Shift（HWP = Hardware P-state）——Intel 从 Skylake 起引入的 
# CPU 自动频率调节机制：CPU 自身硬件根据负载实时调整核心频率，
# 无需操作系统干预。传统方式（cpufreq）需要 OS 通过 ACPI _PSS 表选择 P-state（被动调速）。
# HWP 的延迟和粒度优于传统 cpufreq，是 FreeBSD 供电管理和性能的重要组成。

# ===== 最终 Timecounter 选择 =====
Timecounter "TSC" frequency 806401362 Hz quality 1000
# Time Stamp Counter（TSC）频率 = 806.4 MHz = N100 CPU 基础频率（base clock）。
# quality 1000 是最高优先级——内核最终选择 TSC 为系统主 timecounter。
# TSC 在每个 CPU 时钟（base clock）递增一次，是最细粒度的时间源。
# 该 CPU 的 TSC 为 Invariant（不随 P-state/C-state 变化），可作为可靠的单调时钟源。

Timecounters tick every 1.000 msec
# 内核 timecounter 子系统以 1ms（1000 Hz）的频率更新系统时间基准。

# ===== USB 根集线器发现 =====
ugen1.1: <Intel XHCI root HUB> at usbus1
ugen0.1: <Intel XHCI root HUB> at usbus0
# USB generic 设备节点。ugenX.Y 中 X=USB 总线号，Y=设备地址（根集线器固定为 1）。

uhub0 on usbus1
uhub0: <Intel XHCI root HUB, class 9/0, rev 3.00/1.00, addr 1> on usbus1
# uhub(4)——USB 集线器驱动。class 9 = Hub 类。rev 3.00 = USB 3.0。

uhub1 on usbus0
uhub1: <Intel XHCI root HUB, class 9/0, rev 3.00/1.00, addr 1> on usbus0

# ===== ZFS 版本信息 =====
ZFS filesystem version: 5
ZFS storage pool version: features support (5000)
# ZFS 版本信息：文件系统层版本 5，存储池版本 5000（OpenZFS 2.x/3.x 原生功能标志支持）。
# "features support" 意味着每个 pool 有一个功能标志（feature flags）集合，
# 而非固定的版本号——不同的 pool 可独立启用不同的功能（如压缩、去重等）。

# ===== eMMC 存储设备 =====
mmcsd0: 125GB <MMCHC Y2P128 0.0 SN F034273C MFG 04/2023 by 155 0x0000> at mmc0 200.0MHz/8bit/8192-block
# Radxa X4 板载 128 GB eMMC 存储。通信速率 200.0 MHz，8 bit 数据宽度（HS400 模式）。

mmcsd0boot0: 4MB partition 1 at mmcsd0
mmcsd0boot1: 4MB partition 2 at mmcsd0
# eMMC 内置的两个引导分区（boot partitions）—— 通常存放 BootROM/UEFI 固件。
# Linux 内核通常用它们存放 U-Boot SPL。

mmcsd0rpmb: 17MB partition 3 at mmcsd0
# eMMC RPMB（Replay Protected Memory Block）—— 受重放保护的安全存储分区，
# 用于防回滚密钥存储等安全用途。大小 17 MB。

uhub1: 2 ports with 2 removable, self powered
# uhub1 具有 2 个可移除（external-facing）端口，自供电（意味着不从上游端口取电）。

# ===== NVMe 控制器初始化 =====
nvme0: Allocated 16MB host memory buffer
# NVMe 规范的主机内存缓冲区（Host Memory Buffer, HMB）——SSD 可使用主机系统内存
# 作为映射表（FTL mapping table）的缓存，减少 SSD 本地 DRAM 需求或增加缓存容量。

# ===== HD Audio Codec 探测 =====
hdacc0: <Realtek ALC269 HDA CODEC> at cad 0 on hdac0
# HD Audio Codec（Realtek ALC269）位于 codec address 0。ALC269 常见于笔记本电脑与小主机。

hdaa0: <Realtek ALC269 Audio Function Group> at nid 1 on hdacc0
# AFG（Audio Function Group），HDA 规范术语——包含 DAC/ADC/混音/插孔等功能节点。

pcm0: <Realtek ALC269 (Right Analog)> at nid 21 and 24 on hdaa0
# pcm(4) 音频设备实例。nid 21（Pin Complex）/ nid 24（Pin Complex）代表 
# 右声道模拟输出引脚——可能是 3.5mm 耳机/音箱输出。系统至此具备音频输出能力。

# ===== NVMe 磁盘设备（nda/CAM 路径）=====
nda0 at nvme0 bus 0 scbus0 target 0 lun 1
# nda(4)：通过 CAM(4) 框架连接的 NVMe 磁盘设备。
# nda0：500GB 梵想 S530Q NVMe SSD。
# scbus0 target 0 lun 1：SCSI 中层总线的模拟寻址。
# （FreeBSD 的 CAM 层统一了 nvme(4)→nda(4) 和 ahci(4)→ada(4) 等不同传输协议）

nda0: <Fanxiang S530Q 500GB SN14243 FX240960178>
nda0: Serial Number FX240960178
nda0: nvme version 1.4
nda0: 476940MB (976773168 512 byte sectors)
# NVMe 规范版本 1.4。476940 MB = 500 GB × 1000 / 1024 ≈ 476.9 GiB。
# 976773168 × 512 B = 500.107 GB（多出 107 MB 用于固件/bad block 映射）。

# ===== 挂载根文件系统 =====
Trying to mount root from zfs:zroot/ROOT/default []...
# 内核尝试从 ZFS 池 "zroot" 的数据集 "zroot/ROOT/default" 挂载根文件系统。
# [] 中是传递给 mountroot 的可选参数（通常有 "rw" 或 "ro"），CURRENT 启动为空。
# 这是引导过程的最后一个内核阶段——根系统挂载成功后内核执行 init(8)。

WARNING: WITNESS option enabled, expect reduced performance.
# WITNESS 第二次提醒（重复告警）。这是在挂载 root 且即将进入多用户模式前的最终提醒。

uhub0: 16 ports with 16 removable, self powered
# uhub0 具有 16 个端口（全部可移除、自供电），对应 xHCI 1 号控制器。

Root mount waiting for: usbus1
# 根挂载挂起等待 usbus1（2 号 xHCI 控制器）的 USB 总线枚举完成。
# 因为键盘或驱动等可能在 USB 总线上，必须先让 USB 准备好才能继续启动。

ugen1.2: <Realtek Bluetooth Radio> at usbus1
# 蓝牙适配器（Realtek）。ugen 节点创建标志着蓝牙硬件可用，启动后可加载 ubt(4) 驱动。

# ===== SMBus 控制器（后期枚举）=====
ichsmb0: <Intel Alder Lake SMBus controller> port 0xefa0-0xefbf mem 0x6001148000-0x60011480ff at device 31.4 on pci0
smbus0: <System Management Bus> on ichsmb0
# Intel PCH SMBus（系统管理总线）控制器，用于与 SPD（内存条 EEPROM）、
# 温度传感器、电压监控器等低速设备通信，通过 smbus(4) 框架访问。

# ===== Realtek 8852BE WiFi 6 网卡 =====
rtw890: <rtw89_8852be> port 0x3000-0x30ff mem 0x80800000-0x808fffff at device 0.0 on pci1
# rtw89(4) 驱动为 Realtek 8852BE WiFi 6 无线网卡。驱动以 firmware 方式加载闭源固件。

rtw890: successfully loaded firmware image 'rtw89/rtw8852b_fw-1.bin'
rtw890: loaded firmware rtw89/rtw8852b_fw-1.bin
rtw890: Firmware version 0.29.29.5 (da87cccd), cmd version 0, type 5
rtw890: Firmware version 0.29.29.5 (da87cccd), cmd version 0, type 3
# 固件加载流程：首先加载固件映像文件 .bin，然后验证固件版本。
# 固件版本 0.29.29.5（GIT 提交 da87cccd），cmd version = 0（命令接口版本），
# type 5 和 type 3 分别是 WiFi MAC 层固件和 Bluetooth 共存/PHY 子固件。
# 大部分现代 WiFi 芯片都需要运行时加载闭源固件——卡本身是无固件的 ROM+通用 DSP。

rtw890: chip rfe_type is 5
# RFE（RF Front-End）类型 = 5。前端类型决定了驱动如何进行射频校准和天线选择。

# ===== ACPI WMI（Windows Management Instrumentation）=====
acpi_wmi0: <ACPI-WMI mapping> on acpi0
acpi_wmi0: Embedded MOF found
# acpi_wmi(4)：ACPI WMI 映射驱动。WMI 提供 ACPI 至 Windows 驱动的接口，
# FreeBSD 通过此驱动读取 ACPI WMI 中内嵌的 MOF（Managed Object Format）元数据。
# WMI 接口常被用于笔记本热键、RF kill 开关、风扇控制等——但 x86 小主机平台可能无实际功能。

acpi_wmi0: cannot find EC device
# 未发现 Embedded Controller（EC）——许多 WMI 事件需要 EC 传递键盘/ACPI 通知，
# 没有 EC 说明该平台 WMI 仅提供基础信息（如 BIOS 型号）而无实际控制功能。

ACPI: \134_SB.WFDE.WQCC: 1 arguments were passed to a non-method ACPI object (Buffer) (20241212/nsarguments-361)
# ACPI namespace 的 WMI 事件数据对象（_SB.WFDE.WQCC）被内核解析时发现传入了参数
# 给一个非方法对象（Buffer 数据类型）——BIOS Bug，无影响功能。

acpi_wmi1: <ACPI-WMI mapping> on acpi0
acpi_wmi1: cannot find EC device
acpi_wmi1: Embedded MOF found
ACPI: \134_SB.WFTE.WQCC: 1 arguments were passed to a non-method ACPI object (Buffer) (20241212/nsarguments-361)
# 第二个 ACPI WMI 映射实例。某些主板通过两个 WMI GUID 提供不同类别的功能。
# 此处类似，无 EC 设备导致无法处理 WMI 事件。

# ===== 网络接口就绪 =====
lo0: link state changed to UP
# lo0（loopback 127.0.0.1）接口链路状态变为 UP。loopback 永远在线。

igc0: link state changed to UP
# Intel I226-V 有线网卡链路状态 UP。物理电缆插入且链路协商正常。

# ===== 蓝牙设备最终挂载 =====
ubt0 on uhub0
ubt0: <Realtek Bluetooth Radio, class 224/1, rev 1.00/0.00, addr 1> on usbus1
# ubt(4) 蓝牙 USB 设备驱动已经绑定。蓝牙为 USB class 224（Wireless），
# subclass 1（RF Controller = Bluetooth），protocol 1（BR/EDR+LE）。

# ===== MAC 安全策略加载 =====
Security policy loaded: MAC/ntpd (mac_ntpd)
# mac_ntpd(4)：MAC（强制访问控制/TrustedBSD）框架的 ntpd 隔离策略。
# 授予 ntpd 用户（uid 123）调节系统时钟和绑定 NTP 端口（123）的权限，
# 使 ntpd 能够以非 root 用户身份运行。这是 FreeBSD 默认安全策略之一。
```

## 参考文献

- Linux Foundation. Filesystem Hierarchy Standard 3.0[EB/OL]. (2015-06-03)[2026-04-23]. <https://refspecs.linuxfoundation.org/fhs.shtml>. Filesystem Hierarchy Standard, 文件层次标准包含一套关于类 UNIX 操作系统文件和目录放置的要求和指南。这些指南旨在支持应用程序、系统管理工具、开发工具和脚本之间的互操作性，增强上述系统文档的一致性。
- FreeBSD Project. hier(7)[EB/OL]. [2026-03-26]. <https://man.freebsd.org/cgi/man.cgi?query=hier&sektion=7&manpath=freebsd-release-ports>. 系统阐述 FreeBSD 文件系统层次结构。
- FreeBSD Project. chflags(1)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=chflags>.
- FreeBSD Project. ls(1)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=ls>.

## 课后习题

1. 使用 `tree` 或 `find` 命令遍历 FreeBSD 的目录树结构，与 Ubuntu 最新 LTS 版本在 `/etc`、`/usr`、`/var` 三个目录的组织方式上进行对比分析。
2. 查阅 FreeBSD 源代码中 `hier(7)` 的定义，分析其目录结构设计所遵循的层次化原则。
3. 修改 `/tmp` 目录的默认权限配置（如将权限从 `1777` 改为 `1755`），记录修改后对临时文件创建和系统服务运行的影响。
