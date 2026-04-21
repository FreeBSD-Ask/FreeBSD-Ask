# OpenBSD 系统安装

本节将详细介绍 OpenBSD 系统的安装流程，涵盖镜像获取、系统安装及自定义分区配置等关键环节，为后续的系统管理与高级应用奠定技术基础。

## 下载镜像

以 OpenBSD 7.7、amd64 架构为例，访问 [https://cdn.openbsd.org/pub/OpenBSD/7.7/amd64](https://cdn.openbsd.org/pub/OpenBSD/7.7/amd64) 获取系统镜像

刻录 U 盘安装，请下载 `install77.img`（同时支持 UEFI 和 BIOS）；用于虚拟机体验，请下载 `install77.iso`。

ISO 镜像支持 UEFI 和 BIOS 启动。

> **警告**
>
> 截至 OpenBSD 7.7，请勿使用 Ventoy 1.x 版本引导实体机安装（如 1.1.05），否则会卡在文件集选择阶段。

## 安装过程（UEFI）

本节介绍在 UEFI 环境下安装 OpenBSD 系统的详细步骤。

> **技巧**
>
> OpenBSD 安装程序实际上调用的是位于 [distrib/miniroot/install.sub](https://github.com/openbsd/src/blob/master/distrib/miniroot/install.sub) 的脚本。该安装脚本高度耦合，截至写作时，有三千两百余行。

使用 `install77.iso`，并开启 VMware 虚拟机的 UEFI 功能。

```sh
Welcome to the OpenBSD/amd64 7.7 installation program.

(I)nstall, (U)pgrade, (A)utoinstall or (S)hell? i	# 此处的 i 是用户键入的，下同
```

输入 `i`，按 **回车键**，开始安装。

```sh
Choose your keyboard layout ('?', or 'L' for list) [default]?
```

选择键盘布局，按 **回车键**，选择默认的美国键盘。

```sh
System hostname? (short form, e.g. 'foo') ykla
```

系统主机名可以选择较短的名称，将来主机名会显示为 `ykla` 这样的形式。

```sh
Available network interfaces are: em0 vlan0.
```

上面列出系统识别的网卡。

```sh
Network interface to configure? (name, lladdr, '?' , or 'done ') [em0] # 此处按回车键

IPv4 address for em0? (or 'autoconf' or 'none')[autoconf] # 此处按回车键自动 DHCP IPv4

IPv6 address for em0? (or 'autoconf' or 'none')[none] # 此处按回车键不需要 IPv6

Available network interfaces are: em0 vlan0.

Network interface to configure? (name, lladdr, '?' , or 'done ') [done] # 此处按回车键，若设定错误，可输入 [em0] 退回到上面几步。
```

此步骤用于选择网络连接。为避免麻烦，尽量选择有线网络。可先输入 `?`，详细了解网络名称后再选择。如本例中 `em0` 为有线网络，`vlan0` 是虚拟 VLAN 接口。

后续配置均可直接按 **回车键** 确认。

```sh
Password for root account? (will not echo)
```

设置 root 账号密码，输入后回车确认（密码不会显示在屏幕上）。

```sh
Password for root account? (again)
```

再次输入 root 账号密码，按 **回车键** 确认。

```sh
Start sshd(8) by default? [yes]
```

按 **回车键** 确认，启用 SSH 服务。

```sh
Do you want the X Windows System to be started by xenodm(1)? [no] yes # 输入 yes，按回车键确认
```

启用 xenodm 以运行 X Window System。

```sh
Setup a user? (enter a lower-case loginname, or 'no') [no] ykla # 输入用户名，按回车键确认
```

设置普通用户的用户名。

```sh
Full user name for ykla?
```

用户全名，可随意输入或按 **回车键** 默认。

```sh
Password for ykla account? (will not echo)
```

为该账号设置密码（密码不会显示在屏幕上）。按 **回车键** 确认。

```sh
Password for ykla account? (again)
```

再次输入该用户名的密码。按 **回车键** 确认。

```sh
Allow root ssh login?(yes, no, prohibit-password)[no] yes
```

输入 `yes` 按 **回车键** 确认，以允许 root 登录 ssh。

```sh
What timezone are you in? ('?' for list) [GB] Asia
```

输入 `Asia`（亚洲），按 **回车键** 确认。

```sh
What sub-timezone of 'Asia' are you in? ('?' for list) Shanghai
```

输入 `Shanghai`（注意 `S` 为大写字母），按 **回车键** 确认。

```sh
Available disks are: sd0.

Encrypt the root disk? (disk,  'no' or '?' for details) [no]
```

按 **回车键**，不加密磁盘。

```sh
Available disks are: sd0

Which one is the root disk? (or 'done') [sd0] ?
```

输入 `?` 可查看硬盘：

```sh
Which disk is the root disk? ('?' for details) [sd0] ?
    sd0: NVMe, VMware Virtual N, 1.3 (50.0G)
Available disks are: sd0.
Which disk is the root disk? ('?' for details) [sd0]
```

这一步是选择要将系统安装在哪一块硬盘。按 `?` 列出识别的所有硬盘。请务必记住所有盘符，然后输入需要安装的位置。若选择 `sd0`，输入 `sd0` 并按回车键。

```sh
Use (W)hole disk MBR, whole disk (G)PT or (E)dit? [gpt]
```

回车，选择使用 GPT 分区表。

```sh
Use (A)uto layout, (E)dit auto layout, or create (C)ustom layout? [a]
```

这里直接按回车键，选择系统默认分区。

> **警告**
>
> 由于默认情况下，自动分区的存储空间分配不够合理，使用该方式时可能无法安装桌面环境。

> **技巧**
>
> 文末附有自定义分区设置，仅供参考。

```sh
Available disks are: sd0. Which disk do you wish to initialize? (or 'done') [done]  # 直接按回车键

Let's install the sets!

Location of sets? (cd0 disk ftp http or 'done') [cd0]  # 直接按回车键
```

直接按回车键，选择 `cd0`，即使用安装介质作为软件源。

```sh
Pathname to the sets? (or 'done') [7.7/amd64]	# 直接按回车键
```

直接按回车键。

```sh
Select sets by entering a set name, a file name pattern or 'all'. De-select
sets by prepending a '-', e.g.: '-game*'. Selected sets are labelled `[X]`

[X] bsd       [X] bsd.rd      [X] comp77.tgz   [X] game77.tgz  [X] xshare77.tgz [X] xserv77.tgz
[X] bsd.mp    [X] base77.tgz  [X] man77.tgz    [X] xbase77.tgz [X] xfont77.tgz


Set name(s)? (or 'abort' or 'done') [done] -game*
```

此处可输入 `-game*` 以取消选择 `game77.tgz`，其余保持选中状态；也可以直接按 **回车键**。

> **警告**
>
> 即使不使用桌面环境，也建议勾选 `xserv77.tgz`，否则部分软件可能无法正常运行。

```sh
Set name(s)? (or 'abort' or 'done') [done] -game*	# 输入 -game* 取消选择游戏文件集

[X] bsd       [X] bsd.rd      [X] comp77.tgz   [ ] game77.tgz  [X] xshare77.tgz [X] xserv77.tgz
[X] bsd.mp    [X] base77.tgz  [X] man77.tgz    [X] xbase77.tgz [X] xfont77.tgz

Set name(s)? (or 'abort' or 'done') [done] 	# 直接按回车键
Directory does not contain SHA256sig. Continue without verification? [no] yes	# 请输入 yes，然后直接按回车键
```

此后开始安装系统。约 5 分钟后，系统会显示如下提示：

```sh
Location of sets? (cd0 disk http nfs or 'done') [done]  # 直接按回车键
Time appears wrong.   Set to 'Mon Dec 16 22:43:37CST 2824' ? [yes]  # 直接按回车键
```

> **警告**
>
> 如果不希望在 `fw_update` 阶段卡住，请在按 **回车键** 前拔掉网线，断开网络连接。

```sh
CONGRATULATIONS! Your OpenBSD install has been successfully completed!

When you login to your new system the first time, please read your mail
using the 'mail' command.

Exit to (S)heLL, (H)alt or (R)eboot? [reboot]
# 按回车键重启进入新系统
```

系统已成功安装，重启后即可进入新系统。

> **警告**
>
> 如果不希望遇到报错 `ssh(fail): no hostkeys available, invalid format`，请在重启前恢复网络连接。

## 附录：自定义分区

本附录详细介绍 OpenBSD 的自动分区机制，并提供手动分区方法供参考。

### OpenBSD 自动分区的源代码分析

OpenBSD 默认的自动分区实际调用的是 [sbin/disklabel/editor.c](https://github.com/openbsd/src/blob/master/sbin/disklabel/editor.c) 文件中的相关函数。

```c
// 磁盘容量大于等于 11.25 GB（含）时执行下面的分区策略
struct space_allocation alloc_big[] = {
	{  MEG(150),         GIG(1),   5, "/"		},
	{   MEG(80),       MEG(256),  10, "swap"	},
	{  MEG(120),         GIG(4),   8, "/tmp"	},
	{   MEG(80),         GIG(4),  13, "/var"	},
	{ MEG(1500),        GIG(30),  10, "/usr"	},
	{  MEG(384),         GIG(1),   3, "/usr/X11R6"	},
	{    GIG(1),        GIG(20),  15, "/usr/local"	},
	{    GIG(2),         GIG(5),   2, "/usr/src"	},
	{    GIG(5),         GIG(6),   4, "/usr/obj"	},
	{    GIG(1),       GIG(300),  30, "/home"	}
	/* 除此之外的任何内容，留给用户自行决定 */
};


// 磁盘容量介于 2.38 GB（含）到 11.25 GB（不含）之间时执行下面的分区策略
struct space_allocation alloc_medium[] = {
	{  MEG(800),         GIG(2),   5, "/"		},
	{   MEG(80),       MEG(256),  10, "swap"	},
	{ MEG(1300),         GIG(3),  78, "/usr"	},
	{  MEG(256),         GIG(2),   7, "/home"	}
};


// 磁盘容量介于 700 M（含）到 2.38 GB（不含）之间时执行下面的分区策略
struct space_allocation alloc_small[] = {
	{  MEG(700),         GIG(4),  95, "/"		},
	{    MEG(1),       MEG(256),   5, "swap"	}
};


// 磁盘容量介于 1 MB 到 700 M（不含）之间时执行下面的分区策略
struct space_allocation alloc_stupid[] = {
	{    MEG(1),      MEG(2048), 100, "/"		}
};
```

根据 [sbin/disklabel/extern.h](https://github.com/openbsd/src/blob/master/sbin/disklabel/extern.h) 头文件中的宏：

```c
#define MEG(x)	((x) * 1024LL * (1024 / DEV_BSIZE))    // 实际上是 1 MB
#define GIG(x)  (MEG(x) * 1024LL)    // 实际上是 1 GB
```

再看结构体 `struct space_allocation`：

```c
{  MEG(150),         GIG(1),   5, "/"		},
```

若磁盘总大小满足，先依次按最小大小为所有指定分区进行初次分配，则在初次分配中，先将 `/` 分区指定 150 MB，然后按照权重 5% 对剩余磁盘空间进行二次分配，二次分配后的 `/` 不会超过最大大小限制 1 GB。即无论磁盘多大，`/` 大小的硬限制始终为 1 GB，上述代码最早可追溯到 2009 年。

```c
sa[alloc_table->sz - 1].rate = 100; /* 最后一个分区是贪婪分配的。 */
```

注意到，超过最大权重限制的剩余空间将分配给以下分区：

- 若磁盘总大小大于等于 2.38 GB（含）：`/home`
- 若磁盘总大小介于 700 M（含）到 2.38 GB 之间（不含）：swap

> **思考题**
>
> 在实际使用中，`/` 分区很快就会被填满，而 `/home` 几乎完全为空。并且原生的文件系统不支持磁盘的再分配，如缩减分区、调整顺序。
>
> 请问这种设计的根本缺陷在哪里？请尝试改正并通过邮件列表向 OpenBSD 项目提交改进建议。

实际执行计算的是同 [sbin/disklabel/editor.c](https://github.com/openbsd/src/blob/master/sbin/disklabel/editor.c) 文件内的函数 `allocate_space()`，其中 `if (xtrablks < sa[i].minsz)` 表明先验证磁盘总大小是否满足初次分配的最小要求。从结构体 `alloc_big[]`、`alloc_medium[]`、`alloc_small[]` 最后到 `alloc_stupid[]` 依次降级计算。

函数 `allocate_partition()` 执行实际写入。

> **思考题**
>
> 在 UEFI 下，OpenBSD 自动生成的 `EFI` 分区在哪个位置？

自动安装的分区如下：

```sh
# cat /etc/fstab    # 查看系统文件系统挂载配置文件内容
798e155a2c1de208.b none swap sw
798e155a2c1de208.a / ffs rw 1 1
798e155a2c1de208.l /home ffs rw,nodev,nosuid 1 2
798e155a2c1de208.d /tmp ffs rw,nodev,nosuid 1 2
798e155a2c1de208.f /usr ffs rw,nodev 1 2
798e155a2c1de208.g /usr/X11R6 ffs rw,nodev 1 2
798e155a2c1de208.h /usr/local ffs rw,wxallowed,nodev 1 2
798e155a2c1de208.k /usr/obj ffs rw,nodev,nosuid 1 2
798e155a2c1de208.j /usr/src ffs rw,nodev,nosuid 1 2
798e155a2c1de208.e /var ffs rw,nodev,nosuid 1 2
```

以人类可读格式显示 `sd0` 磁盘的磁盘标签信息：

```sh
# disklabel -h sd0
# /dev/rsd0c:
type: SCSI
disk: SCSI disk
label: VMware Virtual N
duid: 798e155a2c1de208
flags:
bytes/sector: 512
sectors/track: 63
tracks/cylinder: 255
sectors/cylinder: 16065
cylinders: 10443
total sectors: 167772160 # total bytes: 81920.0M
boundstart: 532544
boundend: 167772127

16 partitions:
#                size           offset  fstype [fsize bsize   cpg]
  a:          1024.0M           532544  4.2BSD   2048 16384 12960 # /
  b:          3343.4M          2629696    swap                    # none
  c:         81920.0M                0  unused
  d:          4096.0M          9477056  4.2BSD   2048 16384 12960 # /tmp
  e:          9268.1M         17865664  4.2BSD   2048 16384 12960 # /var
  f:          8567.8M         36846784  4.2BSD   2048 16384 12960 # /usr
  g:          1024.0M         54393600  4.2BSD   2048 16384 12960 # /usr/X11R6
  h:         11625.7M         56490752  4.2BSD   2048 16384 12960 # /usr/local
  i:           260.0M               64   MSDOS
  j:          2913.5M         80300160  4.2BSD   2048 16384 12960 # /usr/src
  k:          6144.0M         86267104  4.2BSD   2048 16384 12960 # /usr/obj
  l:         33653.4M         98850016  4.2BSD   2048 16384 12960 # /home
```

400 G 硬盘自动分区如下：

```sh
# df -h    # 以人类可读的格式显示各文件系统的磁盘使用情况
Filesystem     Size    Used   Avail Capacity  Mounted on
/dev/sd0a      986M    128M    809M    14%    /
/dev/sd0l      295G   36.0K    281G     1%    /home
/dev/sd0d      3.9G   12.0K    3.7G     1%    /tmp
/dev/sd0f     29.1G    1.4G   26.2G     6%    /usr
/dev/sd0g      986M    321M    615M    35%    /usr/X11R6
/dev/sd0h     19.4G    146K   18.4G     1%    /usr/local
/dev/sd0k      5.8G    2.0K    5.5G     1%    /usr/obj
/dev/sd0j      4.8G    2.0K    4.6G     1%    /usr/src
/dev/sd0e     11.5G    8.0M   11.0G     1%    /var
```

### 执行手动分区

了解自动分区的机制后，可以根据实际需求执行手动分区，以更合理地分配磁盘空间。

在系统分区阶段，选择 `C`（Custom），即“自定义设置”。

> `p m`（注意之间的空格）

输入 `p m`（注意之间的空格）来显示硬盘。其他选项如下：

| 代码 | 作用 |
| ---- | ---- |
| p m | 查看分区大小 |
| A | 自动分区 |
| a | 增加分区 |
| d | 删除分区 |
| z | 删除全部分区 |
| q | 确认分区 |

假设磁盘容量为 80 GB，可规划分区为：`EFI 260 MB`、`/` 75 GB、其余空间分配给 `swap`。

顺序不可动，否则无法启动！必须先分一个 /，再分 swap。基本思路：自动分区 → 删去 i 分区以外的分区 → 分 `/` → 分 `swap`。

使用 `d` 删除现有的分区，但会保留 `i` 分区这个 EFI 分区（OpenBSD 7.5 及以上版本，**7.5 以下版本请逐个删除除 MSDOS 以外的所有分区**）

查看当前分区状态：

```sh
键入 p m

OpenBSD area: 532544-167772127; size: 81660.0M; free: 81660.0M
#       size        offset    fstype [fsize bsize  cpg]
  c:    81920.0M          0    unused
  i:      260.0M         64    MSDOS
```

设置 75 GB 的 / 分区：

```sh
partition: [a]	# 此处键入 a

offset: [532544]	# 直接按回车键即可

size: [167239583] 75G # 此处键入 75G

FS type: [4.2BSD]	# 直接按回车键即可，表示使用 UFS 文件系统

mount point: [none] /	# 此处键入 /，代表设定根分区
```

设置交换分区，将剩余空间分配给交换分区：

```sh
partition: [b]	# 直接按回车键即可

offset: [157822560]	# 直接按回车键即可

size: [9949567]	# 直接按回车键即可

FS type: [swap]	# 直接按回车键即可
```

然后查看当前分区状态：

```sh
键入 p m

OpenBSD area: 532544-167772127; size: 81660.0M; free: 81660.0M
#             size            offset    fstype   [fsize bsize  cpg]
  a:      76801.8M           532544      4.2BSD    2048 16384    1  #   /
  b:       4858.2M        157822560        swap
  c:      81920.0M                0      unused
  i:        260.0M               64       MSDOS
```

需要注意的是，在 `size` 一栏中未输入具体数值而直接按 **回车键**，表示将上一步剩余的全部容量分配给该分区，即 `swap` 分区。

配置完毕，记得输入 `q` 确认。

```sh
键入 q

Write new label?: [y]
```

按回车键确认写入新的分区标签。

至此，分区配置完成。

## 从 release 升级到 stable 或 current

除了标准的 release 版本外，OpenBSD 还提供了 stable 和 current 版本供高级用户选择。本节介绍如何从 release 版本升级到这些版本。

OpenBSD 的版本分为三类：release、stable 和 current。release 是官方正式发布的稳定版本，每六个月发布一次；stable 是在 release 基础上应用安全补丁的版本；current 是开发版本，包含最新的功能但可能不稳定。

OpenBSD [不建议](https://www.openbsd.org/faq/current.html)从 release 升级到 current，建议直接使用 [快照版本](https://cdn.openbsd.org/pub/OpenBSD/snapshots/)（即预构建的 current）。这是因为 current 版本的 ABI 变动频繁，从 release 直接升级可能遇到兼容性问题。

经过测试，如果直接从 release 升级到 current 可能会遇到问题，例如：

```sh
===> sbin/shutdown
install -c -s  -o root -g _shutdown  -m 4550 shutdown /sbin/shutdown
install -c -o root -g bin -m 444  /usr/src/sbin/shutdown/shutdown.8 /usr/share/man/man8/shutdown.8
install: unknown group _shutdown
*** Error 1 in target 'realinstall'
*** Error 1 in sbin/shutdown (<bsd.prog.mk>:157 'realinstall')
*** Error 2 in sbin (<bsd.subdir.mk>:48 'realinstall')
*** Error 2 in . (<bsd.subdir.mk>:48 'realinstall')
*** Error 2 in . (Makefile:97 'do-build')
*** Error 2 in /usr/src (Makefile:74 'build'
```

获取 current 版本源代码的步骤：

```sh
$ cd /usr                                                      # 切换到 /usr 目录
$ cvs -qd anoncvs@anoncvs.jp.openbsd.org:/cvs checkout -P src       # 从 OpenBSD anoncvs 仓库检出 src 源代码树
$ cvs -qd anoncvs@anoncvs.jp.openbsd.org:/cvs checkout -P xenocara  # 从 OpenBSD anoncvs 仓库检出 xenocara（X Window 系统源代码）
$ cvs -qd anoncvs@anoncvs.jp.openbsd.org:/cvs checkout -P ports     # 从 OpenBSD anoncvs 仓库检出 Ports 树
```

获取 7.7 -stable 版本源代码的步骤：

```sh
$ cd /usr                                                                  # 切换到 /usr 目录
$ cvs -qd anoncvs@anoncvs.jp.openbsd.org:/cvs checkout -rOPENBSD_7_7 -P src       # 从 OpenBSD anoncvs 仓库检出 OPENBSD_7_7 版本的 src 源代码树
$ cvs -qd anoncvs@anoncvs.jp.openbsd.org:/cvs checkout -rOPENBSD_7_7 -P xenocara  # 从 OpenBSD anoncvs 仓库检出 OPENBSD_7_7 版本的 xenocara 源代码
$ cvs -qd anoncvs@anoncvs.jp.openbsd.org:/cvs checkout -rOPENBSD_7_7 -P ports     # 从 OpenBSD anoncvs 仓库检出 OPENBSD_7_7 版本的 Ports 树
```

从源代码编译和升级系统的步骤：

```sh
# cd /sys/arch/$(machine)/compile/GENERIC.MP      # 进入内核编译目录，该路径在 CVS 源代码拉取完成后才会存在
# make obj                                       # 创建内核编译所需的对象目录
# make config                                    # 生成内核配置相关文件
# make -j4 && make install                       # 使用 4 个并行任务编译并安装内核
# cd /usr/src                                   # 切换到基本系统源代码目录
# make obj && make -j4 build                     # 创建对象目录并使用 4 个并行任务编译基本系统
# sysmerge                                      # 合并系统配置文件的更新
# cd /dev && ./MAKEDEV all                       # 生成并更新所有设备节点
# cd /usr/xenocara                              # 切换到 xenocara（X Window 系统）源代码目录
# make bootstrap                                 # 构建 xenocara 所需的引导工具
# make obj                                       # 创建 xenocara 编译所需的对象目录
# make build                                     # 编译 Xorg（xenocara）
```

## 参考文献

- OpenBSD Project. Anonymous CVS[EB/OL]. (2024-03-25)[2026-03-25]. <https://www.openbsd.org/anoncvs.html>. OpenBSD 官方 CVS 匿名访问指南，提供代码仓库获取方法。
- OpenBSD Project. FAQ - Building the System from Source[EB/OL]. (2024-03-25)[2026-03-25]. <https://www.openbsd.org/faq/faq5.html>. 详细说明从源代码编译 OpenBSD 系统的步骤与配置。
- OpenBSD Project. release — building an OpenBSD release[EB/OL]. (2024-03-25)[2026-03-25]. <https://man.openbsd.org/release>. OpenBSD 官方手册页，介绍发布版本构建流程。
