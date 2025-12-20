# 4.11 系统目录结构

为了方便说明，仅列出三级目录和重要文件：

```sh
\
├── COPYRIGHT FreeBSD 版权信息
├── boot 操作系统引导过程中使用的程序和配置文件。
│   ├── fonts 终端字体
│   ├── device.hints 用于控制驱动程序的内核变量，参见 device.hints(5)
│   ├── uboot 空目录
│   ├── firmware pkg kmod 会安装至此，同 fwget
│   ├── loader.conf.d loader 配置文件的子项
│   ├── lua 启动加载器的 lua 脚本，包含启动时显示的 ASCII 艺术字（图）等，参见 loader_lua(8) 
│   ├── zfs 存放 ZFS 存储池（Zpool）的缓存文件 zpool.cache，参见 zpool(8)
│   ├── kernel 内核及内核模块
│   ├── images 启动时显示的 FreeBSD Logo 等
│   ├── modules 旧时 pkg kmod 会安装至此，如 drm-kmod
│   ├── efi EFI 挂载至此
│   ├── dtb 非 ARM 应为空，设备树 DTB 文件
│   └── defaults 存放默认内核的默认引导配置文件，是个详细的示例说明文件，参见 loader.conf(5)  
├── media 媒体文件挂载点，如 U 盘，光盘
├── mnt 用作临时挂载点的空目录
├── tmp 临时文件
├── root root 的家目录
├── proc 现代 FreeBSD 不使用 procfs，该目录无意义
├── zroot 同 ZFS 池的名称，我也不知道干什么用的，看起来是空的
├── var 多种用途的日志、临时、瞬态、缓存文件
│   ├── db 存放系统和应用程序的数据文件，如 pkg 的数据库等
│   ├── games 存放与游戏相关的数据文件，默认为空
│   ├── yp NIS 的配置等文件
│   ├── mail 存放系统邮件
│   ├── empty 默认为空，提供一个始终保持空白的目录供特定程序使用①
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
├── rescue 静态链接的系统工具，紧急模式时用，参见 rescue(8)
├── dev 存放设备文件和特殊文件，参见 devfs(5)
│   ├── reroot reboot -r 用
│   ├── input 存放输入设备相关的设备文件
│   ├── nvd0 NVMe 第一块固态硬盘
│   ├── nvd0p1 第一块固态硬盘的第一个分区
│   ├── mmcsd0 第一张存储卡
│   ├── dri 显卡字节设备节点，参见 drm(7)
│   ├── drm 显卡节点，参见 drm(7)
│   ├── fd 用于访问当前进程的文件描述符。目录下 0、1、2 对应标准输入、标准输出和标准错误，参见 fdescfs(5)
│   ├── usb USB 设备相关的设备节点
│   ├── gpt GPT 硬盘的设备节点，参见 gpt(8)
│   ├── iso9660  ISO 9660 文件系统的设备节点，如光盘
│   └── pts 伪终端设备，参见 pts(4)
├── etc 基本系统配置文件和脚本
│   ├── auto_master autofs 配置文件，参见 automount(8)
│   ├── crontab root 的 crontab 文件
│   ├── devfs.conf 启动时的设备参数
│   ├── freebsd-update.conf 基本系统更新工具 freebsd-update 的配置文件，参见 freebsd-update(8)
│   ├── fstab 文件分区表，参见 fstab(5)
│   ├── hosts hosts 文件，优先于 DNS 的本地 IP 域名映射表
│   ├── inetd.conf 配置 BSD inetd，参见 inetd(8)
│   ├── localtime 本地时区文件，参见 ctime(3)。在我的系统中，localtime 链接到了 /usr/share/zoneinfo/Asia/Shanghai
│   ├── login.conf ​登录类功能数据库，参见 login.conf(5)
│   ├── machine-id 系统的 UUID，dbus 用
│   ├── motd.template tty 登录后显示的信息，参见 motd(5)
│   ├── ntp.conf NTP 客户端配置文件，参见 ntpd(8)
│   ├── pf.conf PF 防火墙配置文件，参见 pf(4)
│   ├── rc.conf 系统 RC，参见 rc.conf(5)
│   ├── resolv.conf DNS 解析，参见 resolv.conf(5)
│   ├── sysctl.conf 内核状态默认值，参见 sysctl.conf(5)
│   ├── syslog.conf 系统日志配置文件
│   ├── ttys 创建 tty 的规则文件，参见 getty(8)
│   ├── wpa_supplicant.conf 连接 WiFi 的配置文件，参见 wpa_supplicant.conf(5)
│   ├── dma DMA 邮件代理相关，参见 dma(8)
│   ├── pam.d 可插拔认证模块（PAM）相关的配置文件，参见 pam.d(5)
│   ├── ssl 存储与 SSL/TLS 相关的文件，如证书、密钥
│   ├── X11 X11 相关，如 XRDP
│   ├── rc.conf.d 存放特定服务的配置文件，默认为空
│   ├── cron.d 存放系统级的定时任务配置文件，参见 crontab(1)、cron(8)
│   ├── profile.d 存放脚本文件，这些脚本在用户登录时由 shell 执行。但不会自动加载。
│   ├── ppp PPP 相关配置，参见 ppp(8)
│   ├── defaults 存放了一组默认配置文件，如 rc.conf、periodic.conf。
│   ├── zfs ZFS 相关配置文件，参见 zfs(8)
│   ├── rc.d 用于启动和管理系统服务的 RC 脚本
│   ├── devd 存放设备管理器（devd）的配置文件，如监控蓝牙、鼠标插拔
│   ├── ssh SSH 和 SSHD 相关配置文件
│   ├── autofs 存放自动挂载相关的配置文件，参见 autofs(5)
│   ├── gss GSSAPI 相关文件、含 Kerberos 5
│   ├── periodic 存放定期执行的维护脚本，由 cron 调用。参见 periodic.conf(5)
│   ├── mail Sendmail 相关文件
│   │    ├── aliases 用于投递系统邮件的地址
│   │    └── mailer.conf mailwrapper(8) 配置文件
│   ├── kyua Kyua 测试框架的全局配置文件。参见 kyua(1)、kyua.conf(5)
│   ├── unbound Unbound 配置文件
│   ├── ntp NTP 相关，参见 ntp.conf(5)、ntpd(8) 
│   ├── mtree 用于系统的初始化和验证过程，可用于系统审计，参见 mtree(8)
│   ├── bluetooth 蓝牙相关
│   ├── authpf 用于认证网关用户的 shell 配置文件，参见 authpf(8)，默认为空
│   ├── sysctl.kld.d 特定内核模块的配置文件，默认为空，参见 https://reviews.freebsd.org/D40886
│   ├── pkg PKG 相关配置文件，参见 pkg(7)
│   ├── jail.conf.d 旨在实现对 jail 配置的模块化管理，默认为空。参见 jail.conf(5)
│   ├── syslog.d syslogd 的配置文件，参见 syslog(3)
│   ├── newsyslog.conf.d newsyslog 的配置文件，参见 newsyslog.conf(5)
│   └── security OpenBSM 审计配置文件
├── libexec 系统级的可执行文件
│   └── resolvconf 管理 DNS 解析配置的程序，参见 resolvconf.conf(5)
├── net NFS 共享挂载点，参见 auto_master(5)
├── home 普通用户家目录
│   └── ykla 普通用户 ykla
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
│   ├── src FreeBSD 源代码，参见 ports(7)
│   ├── ports FreeBSD Ports
│   │    └── distfiles 下载的源码包存放的地方
│   ├── lib 用户库文件
│   └── sbin 用户系统管理实用程序
├── lib /bin、/sbin 的库文件
│   ├── geom GEOM 库，参见 geom(8)
│   └── nvmecontrol NVME 用，参见 nvmecontrol(8)
└── sbin 基本的 BSD 系统管理工具
```

①：目录 `/var/empty` 加注了 schg 权限，即系统不可变标志：

```sh
dr-xr-xr-x   2 root    wheel   schg,uarch  2 Feb 21 10:26 empty
```


## 参考文献

- 手册页 [hier(7)](https://man.freebsd.org/cgi/man.cgi?query=hier&sektion=7&manpath=freebsd-release-ports)
