# 4.3 系统目录结构

## 目录结构概览

FreeBSD 的文件系统层次结构是理解系统整体架构的基础。根目录（/）是文件系统的最顶层目录，在系统启动时第一个被挂载，包含操作系统进入多用户模式所需的基本系统。根目录还包含其他文件系统的挂载点。挂载点是附加文件系统可以嫁接到父文件系统（通常是根文件系统）上的目录。标准挂载点包括 `/usr/`、`/var/`、`/tmp/`、`/mnt/` 和 `/media/`。完整的文件系统层次结构描述参见 hier(7)。

## 文件系统层次结构的设计哲学

类 UNIX 操作系统的目录结构设计遵循若干核心原则，这些原则源于 UNIX 早期开发实践并经长期演化而成：

- **单一根目录原则**：与 Windows 等系统采用多根（多盘符）的设计不同，UNIX 系统采用单一根目录（`/`）作为整个文件系统的起点。所有存储设备、分区和网络文件系统均以挂载（mount）的方式接入统一的目录树中。这一设计使得文件路径具有全局唯一性，避免了盘符分配的不确定性。文件系统最好被可视化为以 `/` 为根的树形结构，`/dev`、`/usr` 等目录是根目录的分支，这些分支还可以拥有自己的分支。

- **功能分离原则**：将不同功能的文件分配到不同的目录中，使得各文件系统可以独立管理、挂载和备份。例如，将系统二进制文件（`/bin`、`/sbin`）与用户应用程序（`/usr/local`）分离，将配置文件（`/etc`）与日志数据（`/var/log`）分离。将 `/var` 与 `/` 分离是有利的，因为 `/var` 包含日志目录、假脱机目录和各种临时文件，可能会被填满，而填满根文件系统是不好的做法。

- **基本系统与第三方软件分离原则**：FreeBSD 将基本系统（base system）与第三方软件严格分离。基本系统的组件安装在 `/bin`、`/sbin`、`/usr/bin`、`/usr/sbin`、`/usr/lib` 等目录中，而通过 Ports 或 pkg 安装的第三方软件则统一安装到 `/usr/local/` 下的对应子目录中（如 `/usr/local/bin`、`/usr/local/lib`、`/usr/local/etc`）。这种分离确保了基本系统的独立性和完整性，使得系统升级不会影响第三方软件，反之亦然。

- **静态与动态数据分离原则**：静态数据（如二进制文件、库文件、文档）与动态数据（如日志、临时文件、运行时数据）分别存储于不同的目录树中。`/usr` 主要存放静态的只读数据，`/var` 则存放可变的运行时数据，`/tmp` 存放临时文件。

## 设备与设备节点

设备是系统中主要用于与硬件相关活动的术语，包括磁盘、打印机、显卡和键盘。当 FreeBSD 启动时，大多数启动消息都与正在检测的设备有关。启动消息的副本保存在 `/var/run/dmesg.boot` 中。

每个设备都有一个设备名称和编号。例如，`ada0` 是第一个 SATA 硬盘，而 `kbd0` 代表键盘。

FreeBSD 中的大多数设备必须通过称为设备节点的特殊文件访问，这些文件位于 `/dev` 目录中。

在 FreeBSD 中，设备节点由 devfs(5) 文件系统自动管理。devfs 是一个虚拟文件系统，在系统启动时由内核自动挂载到 `/dev`，并根据当前系统中存在的硬件设备动态创建和删除设备节点。这与传统 UNIX 系统需要手动使用 `mknod` 命令创建设备节点的做法不同。devfs 确保了 `/dev` 目录中只包含当前系统实际存在的设备节点，避免了设备节点的冗余。

设备节点分为两种类型：字符设备（character device）和块设备（block device）。字符设备以字节流方式访问数据，如终端（`/dev/ttyv0`）和串口；块设备以固定大小的块为单位访问数据，如磁盘（`/dev/ada0`）。在 `ls -l` 的输出中，字符设备的类型标识为 `c`，块设备的类型标识为 `b`。

设备命名遵循一定的约定：SATA 硬盘以 `ada` 开头（如 `ada0`、`ada1`），SCSI 硬盘和 USB 存储设备以 `da` 开头（如 `da0`），NVMe 存储以 `nvd` 或 `nda` 开头，CD-ROM 驱动器以 `cd` 开头。编号从 0 开始。GPT 分区在设备名后附加 `p` 加分区号（如 `ada0p1`），MBR 切片附加 `s` 加切片号（如 `ada0s1`）。

## FHS 与 FreeBSD 目录结构

文件系统层次标准（Filesystem Hierarchy Standard，FHS）由 Linux 基金会维护，旨在定义类 UNIX 操作系统中目录结构和目录内容的规范。FHS 的目标是使软件开发者能够预测已安装文件和目录的位置，从而编写更具可移植性的软件。当前版本为 FHS 3.0，发布于 2015 年（来源：Linux Foundation. Filesystem Hierarchy Standard 3.0[EB/OL]. (2015-06-03)[2026-04-23]. <https://refspecs.linuxfoundation.org/fhs.shtml>.）

FreeBSD 的目录结构遵循了 FHS 的核心设计理念，但并非 FHS 的严格实现。FreeBSD 的目录层次由 `hier(7)` 手册页定义，是 FreeBSD 项目的权威规范。与 Linux 发行版相比，FreeBSD 的目录结构存在若干显著差异：

| 项目 | FHS（文件系统层次标准） | FreeBSD |
| ---- | ----------------------- | ------- |
| `/usr/local` 的角色 | 保留给系统管理员本地安装软件 | Ports 与 pkg 安装第三方软件的默认目标路径；用于本地可执行文件与库 |
| 配置文件位置 | 通常位于 `/etc` 或 `/etc/opt`（第三方软件） | 第三方软件配置位于 `/usr/local/etc`；系统配置位于 `/etc`，严格分离 |
| `/libexec` 目录 | 非标准或不强制规定 | 用于存放系统级辅助可执行程序 |
| `/rescue` 目录 | 不存在标准定义 | 存放静态链接的紧急修复工具，用于系统恢复 |

为便于说明，仅列出三级目录和重要文件。

```sh
/
├── COPYRIGHT FreeBSD 版权信息文件
├── boot 操作系统引导过程中使用的程序和配置文件
│   ├── fonts 终端字体
│   ├── device.hints 用于控制驱动程序的内核变量，参见 device.hints(5)
│   ├── uboot 空目录
│   ├── firmware pkg kmod 会安装至此，以及通过 fwget 下载的固件
│   ├── loader.conf loader 配置文件
│   ├── loader.conf.d loader 配置文件的子项
│   ├── lua 引导加载程序的 lua 脚本，包含启动时显示的 ASCII 艺术字（图）等，参见 loader_lua(8)
│   ├── zfs 存放 ZFS 存储池（Zpool）的缓存文件
│   │    └── zpool.cache，硬编码的磁盘驱动器路径，参见 zpool(8)
│   ├── kernel 内核及内核模块
│   ├── images 启动时显示的 FreeBSD Logo 等
│   ├── modules 旧时 pkg kmod 会安装至此，如 drm-kmod
│   ├── efi EFI 系统分区挂载至此
│   ├── dtb 设备树 DTB 文件，x86 架构下应为空
│   └── defaults 存放默认内核的默认引导配置文件
│       └── loader.conf 详细的示例说明文件，参见 loader.conf(5)
├── media 媒体文件挂载点，如 U 盘，光盘
├── mnt 用作临时挂载点的空目录
├── tmp 通常在系统重启后仍会保留的临时文件
├── root root 的家目录
├── proc 现代 FreeBSD 默认不使用 procfs，该目录通常为空
├── zroot 与 ZFS 池同名的目录，通常为空，作用未知
├── var 多种用途的日志、临时、瞬态、缓存文件
│   ├── db 存放系统和应用程序的数据文件，如 pkg 的数据库等
│   ├── games 存放与游戏相关的数据文件，默认为空
│   ├── yp NIS 的配置等文件
│   ├── mail 系统邮件
│   ├── empty 默认为空，旨在提供一个始终保持空白的目录供特定程序使用①
│   ├── preserve 用于存放编辑器（如 vi）在异常关闭后保存的文件，已不再使用，默认为空
│   ├── heimdal Kerberos 5 用，默认为空
│   ├── run 用来存放 PID 文件和运行时数据
│   ├── authpf 用于认证网关用户的 shell，参见 authpf(8)，默认为空
│   ├── msgs 用于存放系统消息文件，参见 msgs(1)
│   ├── at 存放 at 命令调度的任务文件，参见 at(1)
│   ├── cache 缓存文件，如 pkg 下载的二进制文件缓存在 cache/pkg
│   ├── backups 用于存放系统的备份文件，如用户名和密钥、pkg 数据库。由 /etc/periodic/daily 下的 200、210 等文件生成
│   ├── spool 存放等待处理的任务文件，如待打印机打印的文件
│   ├── cron 存放 cron 定时任务相关文件，参见 cron(8)
│   ├── crash 存放崩溃转储文件
│   ├── rwho 存储由 rwhod 收集的网络中其他计算机的用户登录信息，参见 rwhod(8)。默认为空
│   ├── log 各种系统日志文件
│   ├── unbound Unbound 服务器的相关文件
│   ├── audit 存储安全审计日志文件，属于 audit 组
│   ├── account 默认为空，系统审计用，参见 accton(8)
│   └── tmp 通常会在系统重启后保留的临时文件
├── rescue 静态链接的系统工具，紧急模式时使用，参见 rescue(8)
├── dev 存放设备文件和特殊文件，参见 devfs(5)
│   ├── reroot reboot -r 使用
│   ├── input 存放输入设备相关的设备文件
│   ├── nda0 NVMe 第一块固态硬盘
│   ├── nda0p1 第一块固态硬盘的第一个分区
│   ├── mmcsd0 第一张存储卡
│   ├── dri 显卡字符设备节点，参见 drm(7)
│   ├── drm 显卡节点，参见 drm(7)
│   ├── fd 用于访问当前进程的文件描述符。目录下 0、1、2 对应标准输入、标准输出和标准错误，参见 fdescfs(5)
│   ├── usb USB 设备相关的设备节点
│   ├── gpt GPT 硬盘的设备节点，参见 gpt(8)
│   ├── iso9660 ISO 9660 文件系统的设备节点，如光盘
│   └── pts 伪终端设备，参见 pts(4)
├── etc 基本系统配置文件和脚本
│   ├── auto_master autofs 配置文件，参见 automount(8)
│   ├── crontab root 用户的 crontab 文件
│   ├── devfs.conf 启动时的 devfs 设备规则配置
│   ├── freebsd-update.conf 基本系统更新工具 freebsd-update 的配置文件，参见 freebsd-update(8)
│   ├── fstab 文件分区表，参见 fstab(5)
│   ├── hosts hosts 文件，优先于 DNS 的本地 IP 域名映射表
│   ├── inetd.conf 配置 BSD inetd，参见 inetd(8)
│   ├── localtime 本地时区文件，参见 ctime(3)。在测试系统中，localtime 被链接到了 /usr/share/zoneinfo/Asia/Shanghai
│   ├── login.conf 登录类功能数据库，参见 login.conf(5)
│   ├── machine-id 系统的 UUID，dbus 用
│   ├── motd.template TTY 登录后显示的信息，参见 motd(5)
│   ├── ntp.conf NTP 客户端配置文件，参见 ntpd(8)
│   ├── pf.conf PF 防火墙配置文件，参见 pf(4)
│   ├── rc.conf 系统 RC，参见 rc.conf(5)
│   ├── resolv.conf DNS 解析配置文件，参见 resolv.conf(5)
│   ├── sysctl.conf 内核状态默认值，参见 sysctl.conf(5)
│   ├── syslog.conf 系统日志配置文件
│   ├── ttys 创建 TTY 的规则文件，参见 getty(8)
│   ├── wpa_supplicant.conf 连接 WiFi 的配置文件，参见 wpa_supplicant.conf(5)
│   ├── dma DMA 邮件代理相关，参见 dma(8)
│   ├── pam.d 可插拔认证模块（PAM）相关的配置文件，参见 pam.d(5)
│   ├── ssl 存储与 SSL/TLS 相关的文件，如证书、密钥
│   ├── X11 X11 相关，如 XRDP
│   ├── rc.conf.d 存放特定服务的配置文件，默认为空
│   ├── cron.d 存放系统级的定时任务配置文件，参见 crontab(1)、cron(8)
│   ├── profile.d 存放脚本文件，这些脚本可在用户登录时由 shell 执行，但不会自动加载
│   ├── ppp PPP 相关配置，参见 ppp(8)
│   ├── defaults 存放了一组默认配置文件，如 rc.conf、periodic.conf。
│   ├── zfs ZFS 相关配置文件，参见 zfs(8)
│   ├── rc.d 用于启动和管理系统服务的 RC 脚本
│   ├── devd 存放设备管理器（devd）的配置文件，如监控蓝牙、鼠标插拔
│   ├── ssh SSH 和 SSHD 相关配置文件
│   ├── autofs 存放自动挂载相关的配置文件，参见 autofs(5)
│   ├── gss GSSAPI 相关文件、含 Kerberos 5
│   ├── periodic 存放定期执行的维护脚本，由 cron 调用（periodic.conf(5)）
│   ├── mail Sendmail 相关文件
│   │    ├── aliases 用于投递系统邮件的地址
│   │    └── mailer.conf mailwrapper(8) 配置文件
│   ├── kyua Kyua 测试框架的全局配置文件（kyua(1)、kyua.conf(5)）
│   ├── unbound Unbound 配置文件
│   ├── ntp NTP 相关，参见 ntp.conf(5)、ntpd(8)
│   ├── mtree 用于系统的初始化和验证过程，可用于系统审计，参见 mtree(8)
│   ├── bluetooth 蓝牙相关
│   ├── authpf 用于认证网关用户的 shell 配置文件，参见 authpf(8)，默认为空
│   ├── sysctl.kld.d 特定内核模块的配置文件，默认为空，参见：D40886[EB/OL]. [2026-03-26]. <https://reviews.freebsd.org/D40886>.
│   ├── pkg PKG 相关配置文件，参见 pkg(7)
│   ├── jail.conf.d 旨在实现对 jail 配置的模块化管理，默认为空（jail.conf(5)）
│   ├── syslog.d syslogd 的配置文件，参见 syslog(3)
│   ├── newsyslog.conf.d newsyslog 的配置文件，参见 newsyslog.conf(5)
│   └── security OpenBSM 审计配置文件
├── libexec 系统级辅助可执行程序
│   └── resolvconf 管理 DNS 解析配置的程序，参见 resolvconf.conf(5)
├── net NFS 共享挂载点，参见 auto_master(5)
├── home 普通用户家目录
│   └── ykla 普通用户 ykla 的家目录
├── bin 基本的 BSD 用户工具，参见 intro(1)
├── sys 链接到 /usr/src/sys
├── usr 用户工具与程序
│   ├── share 架构无关文件
│   ├── local 用户安装的软件，通常是通过 ports(7) 或 pkg(7) 安装的
│   ├── lib32 用户的 32 位兼容库
│   ├── include 用户库文件、头文件
│   ├── obj 架构特定的目标树，用于从源代码构建 FreeBSD
│   ├── libexec 用户执行的系统守护进程和实用程序
│   ├── bin 用户实用程序
│   ├── tests FreeBSD 测试套件，参见 tests(7)
│   ├── libdata 杂项实用数据文件
│   ├── src FreeBSD 源代码，参见 src(1)
│   ├── ports FreeBSD Ports
│   │    └── distfiles 下载的源代码包存放的地方
│   ├── lib 用户库文件
│   └── sbin 用户系统管理实用程序
├── lib /bin、/sbin 的库文件
│   ├── geom GEOM 库，参见 geom(8)
│   └── nvmecontrol NVMe 相关工具，参见 nvmecontrol(8)
└── sbin 基本的 BSD 系统管理工具
```

①：目录 `/var/empty` 加注了 schg 权限，即系统不可变标志。

```sh
# ls -lod /var/empty
dr-xr-xr-x   2 root    wheel   schg  2 Apr 13 12:38 /var/empty
```

参数解释：在长格式（`-l`）输出中包含文件标志（`-o`），并且将目录视为普通文件列出而不递归（`-d`）。

FreeBSD ls 与 GNU ls 比较：

| 参数 | FreeBSD `ls` 行为 | GNU `ls` 行为 |
| ---- | ----------------- | ------------- |
| `-o` | 显示长格式 + 文件 flags（文件标志） | 等同 `-l`，但不显示属组（group） |
| `-l` | 长格式（权限 / 属主 / 属组 / 时间等） | 长格式（权限 / 属主 / 属组 / 时间等） |
| `-G` | 启用彩色输出 | 不支持该参数 |
| `--color` | 不支持 | 启用彩色输出 |
| `--group-directories-first` | 不支持 | 目录优先排序（目录排在文件前） |
| 文件 flags（flags） | 支持（如 `schg`, `uchg` 等） | 不支持 |

## 参考文献

- FreeBSD Project. hier(7)[EB/OL]. [2026-03-26]. <https://man.freebsd.org/cgi/man.cgi?query=hier&sektion=7&manpath=freebsd-release-ports>. 系统阐述 FreeBSD 文件系统层次结构。
- FreeBSD Project. chflags(1)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=chflags>.
- FreeBSD Project. ls(1)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=ls>.

## 课后习题

1. 在 FreeBSD 中遍历整个目录树结构，并与 Ubuntu 最新 LTS 版本进行比较。
2. 分析 FreeBSD 源代码中有关文件结构的设计。
3. 修改 FreeBSD 中 `/tmp` 目录的默认权限配置，验证其行为变化。
