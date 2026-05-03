# 8.1 UFS 文件系统

UFS（Unix File System）是 FreeBSD 的原生文件系统，基于伯克利快速文件系统（FFS），由 Kirk McKusick 等人于 1983 年随 4.2BSD 引入，当前版本为 UFS2。本节涵盖磁盘扩容、快照创建与挂载及配额管理三类操作。

## 概述

UFS 全称为 Unix File System（UNIX 文件系统），FreeBSD 中使用的 UFS 实际上是伯克利快速文件系统（Berkeley Fast File System，FFS），由 Kirk McKusick、Bill Joy 等人于 1983 年随 4.2BSD 首次引入。历史上，macOS 也曾使用该文件系统作为根文件系统。

须明确区分，本节所述的 UFS 文件系统与手机等设备中使用的 UFS 存储属于完全不同的技术范畴。后者全称为 Universal Flash Storage（通用闪存存储），是一种硬件存储标准，目前已发展至 4.1 版本。FreeBSD 在 10.4 版本中支持 eMMC，FreeBSD 15.0 已通过 `ufshci` 驱动支持 UFS 存储。

作为文件系统的 UFS，其当前版本号为 2。基于 Linux 的 Android 系统不支持 UFS 文件系统，此类设备的根文件系统通常为 ext4，部分新设备采用 F2FS，而 Linux 对 UFS 的读写支持尚不完整。

> **警告**
>
> UFS 文件系统只能扩大，不能缩小。

## UFS 文件系统磁盘扩容

> **注意**
>
> 此方案仅适用于向后扩展；若 freebsd-ufs 分区前方存在空余空间，则无法使用此方法进行扩展。

首先，使用 `gpart show` 命令查看系统中所有磁盘的分区布局：

```sh
# gpart show
=>       3  41943035  da0  GPT  (20G)
         3       122    1  freebsd-boot  (61K)
       125     66584    2  efi  (33M)
     66709   2097152    3  freebsd-swap  (1.0G)
   2163861  10486633    4  freebsd-ufs  (5.0G)
  12650494  29292544       - free -  (14G)
```

系统盘初始大小为 5 GB，输出显示 `da0` 磁盘仅含一个 UFS 分区。

### 执行扩容命令序列

> **警告**
>
> 若使用的是 GPT 分区表，此处的扩容操作在虚拟机或云服务器环境中可能会破坏 GPT 分区表，原因是虚拟机或云平台在调整磁盘大小时可能未正确更新 GPT 分区表的备份副本，因此须首先恢复 `da0` 磁盘的分区表：
>
> ```sh
> # gpart recover da0
> ```
>
> 执行上述操作后，后续步骤保持一致。

调整 da0 磁盘上编号为 4 的 `freebsd-ufs` 分区大小：

```sh
# gpart resize -i 4 da0
da0p4 resized
```

选项 `-i` 用于指定待扩容的分区编号，此处用于扩展 `freebsd-ufs` 分区。

### 扩展文件系统

使用 growfs 服务扩展文件系统，该操作仅需执行一次，完成后无需重复运行：

```sh
# service growfs onestart
Growing root partition to fill device
da0 recovering is not needed
da0p4 resized
growfs: no room to allocate last cylinder group; leaving 7.7MB unused
super-block backups (for fsck_ffs -b #) at:
 11544384, 12827072, 14109760, 15392448, 16675136, 17957824, 19240512, 20523200, 21805888, 23088576, 24371264,
 25653952, 26936640, 28219328, 29502016, 30784704, 32067392, 33350080, 34632768, 35915456, 37198144, 38480832
```

growfs 是 FreeBSD 用于扩展 UFS 文件系统的工具，通过调整柱面组和超级块来利用新增的分区空间。

### 验证扩容结果

查看已挂载文件系统的磁盘使用情况：

```sh
# df -hl
Filesystem         Size    Used   Avail Capacity  Mounted on
/dev/gpt/rootfs     18G    4.8G     12G    29%    /
devfs              1.0K      0B    1.0K     0%    /dev
/dev/gpt/efiesp     32M    651K     31M     2%    /boot/efi
tmpfs               20M    4.0K     20M     0%    /tmp
tmpfs               32M    156K     32M     0%    /var
```

参数说明：

- `-h`：以人类可读格式显示，单位为 KB、MB、GB 等。
- `-l`：仅显示本地文件系统。

上述输出表明，分区扩展操作已完成，文件系统已成功调整至新的大小。

### 参考文献

- FreeBSD Project. ffs -- Berkeley fast file system[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?ffs(7)>. UFS/FFS 文件系统概述手册页，描述伯克利快速文件系统的设计与实现。
- FreeBSD Project. mount_ufs -- mount a UFS file system[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?mount_ufs(8)>. UFS 文件系统挂载命令手册页。
- FreeBSD Project. growfs -- expand a UFS file system[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?growfs(8)>. UFS 文件系统扩容工具手册页。
- FreeBSD Project. fsck_ffs -- file system consistency check and interactive repair[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?fsck_ffs(8)>. UFS 文件系统一致性检查与修复工具手册页。
- Jaeyoon Choi. Universal Flash Storage on FreeBSD[EB/OL]. [2026-04-16]. <https://freebsdfoundation.org/our-work/journal/browser-based-edition/freebsd-15-0/universal-flash-storage-on-freebsd/>。该文介绍了 FreeBSD UFS 驱动的开发过程及当前状态。
- McKusick M K. 4.4BSD 操作系统设计与实现[M]. 李善平，刘文峰，马天驰，译. 北京：机械工业出版社，2012. 该书第 7 章详细描述了 FFS 的设计与历史。
- McKusick M K, Joy W N, Leffler S J, et al. A Fast File System for UNIX[J]. ACM Transactions on Computer Systems，1984，2(3)：181-197. FFS 原始论文，首次系统阐述了伯克利快速文件系统的设计与实现。

## UFS 文件系统快照

FreeBSD 提供了一项与软更新（Soft Updates）结合使用的功能：文件系统快照。

UFS 快照允许用户创建指定文件系统的镜像，并将其作为文件处理。

快照文件必须创建在被快照的文件系统内，每个 UFS 文件系统最多可创建 20 个快照。活动快照会记录在超级块中，并在系统重启后仍然存在。当不再需要某个快照时，可使用 rm(1) 删除。尽管可以按任意顺序删除快照，但可能无法彻底回收所有已使用的空间，因为其他快照可能会占用部分已释放的块。

可使用 mksnap_ffs(8) 创建 `/` 的快照，并存储至 `/.snap/snap1`：

```sh
# mksnap_ffs /.snap/snap1
```

>**技巧**
>
>mksnap_ffs 会自动快照指定目录所在的文件系统，不支持指定文件系统。以上是 UFS 标准安装的系统，因此会对完整的根分区进行快照。

快照亦可通过 mount(8) 创建。若要将 **/** 的快照存入文件 **/home/ykla/snapshot/snap**，可使用以下命令：

```sh
# mkdir -p /home/ykla/snapshot/
# mount -u -o snapshot /home/ykla/snapshot/snap /
```

UFS 快照文件的大小等于其来源文件系统的大小，但实际占用空间与 ZFS 类似：

```sh
# ls -loh /home/ykla/snapshot/snap	# 逻辑占用存储
-r--------  1 root ykla snapshot   19G May  1 01:55 /home/ykla/snapshot/snap
# du -hl /home/ykla/snapshot/snap	# 真实占用存储
6.1M	/home/ykla/snapshot/snap
```

`snapshot` 文件标志（不可变标志）由 mksnap_ffs(8) 在快照文件初始创建时设置。

可使用 find(1) 查找文件系统中的快照文件，例如 **/**：

```sh
# find / -flags snapshot
/.snap/snap1
/home/ykla/snapshot/snap
```

快照可作为文件系统的冻结镜像挂载。若要以只读方式挂载快照 **/home/ykla/snapshot/snap**，可执行以下命令：

```sh
# mdconfig -a -t vnode -o readonly -f /home/ykla/snapshot/snap -u 4
# mount -r /dev/md4 /mnt
# ls /mnt/
.snap		dev		libexec		rescue		var
.sujournal	entropy		media		root
COPYRIGHT	etc		mnt		sbin
bin		home		net		tmp
boot		lib		proc		usr
```

选项说明：
  
| 参数 | 含义 |
| ---- | ---- |
| `-a` | 创建 md 设备 |
| `-t vnode` | 用文件作为磁盘 |
| `-o readonly` | 创建只读 vnode 磁盘设备 |
| `-f file` | 指定快照文件 |
| `-u 4` | 指定至 md4，防止冲突 |

挂载后，冻结的 **/** 即可通过 **/mnt** 访问，所有内容均保持快照创建时的状态。唯一的例外是，任何早期的快照将显示为空文件。卸载快照可执行：

```sh
# umount /mnt
# mdconfig -d -u 4
```

### 参考文献

- McKusick, M. McKusick.com[EB/OL]. [2026-04-30]. <http://www.mckusick.com/>. 有关 softupdates 和文件系统快照的更多信息，包括技术论文，可访问 Kirk McKusick 的网站：

## UFS 文件系统磁盘配额

磁盘配额可用于限制用户或用户组在每个 UFS 文件系统上可分配的磁盘空间或文件数量。以此防止某个用户或用户组消耗掉所有可用的磁盘空间。

FreeBSD 默认内核提供了对磁盘配额的支持，可运行以下命令进行验证：

```sh
$ sysctl kern.features.ufs_quota
kern.features.ufs_quota: 1
```

如果以上输出为 0，意味着当前可能正在使用自定义内核，未支持磁盘配额模块。应在内核配置文件中加入内核选项 `options QUOTA`，然后重新编译内核。

设置开机启用磁盘配额：

```sh
# service quota enable
```

立刻启用磁盘配额：

```sh
# service quota start
```

系统在启动时会通过 quotacheck(8) 检查每个文件系统的配额完整性。此程序确保配额数据库中的数据正确反映文件系统中的数据。此过程较为耗时，会显著影响系统的启动时间。要跳过此步骤，可在 **/etc/rc.conf** 中添加以下变量：

```ini
check_quotas="NO"
```

须在 **/etc/fstab** 中加入配额选项，以启用每个用户或每个用户组的磁盘配额。若要启用每个用户的配额，可在文件系统的 **/etc/fstab** 配置行的选项字段中添加 `userquota`。例如：

```ini
/dev/nda0p2     /               ufs     rw,userquota      1       1
```

若要启用组配额，可使用 `groupquota` 替代。若同时启用用户和组配额，可用逗号分隔选项：

```ini
/dev/nda0p2     /               ufs     rw,userquota,groupquota      1       1
```

配置完成后，重新启动系统，**/etc/rc** 将自动运行适当的命令，为 **/etc/fstab** 中启用的所有配额创建初始配额文件。

默认情况下，配额文件存储在文件系统的根目录中，名为 **quota.user** 和 **quota.group**。

```sh
-rw-r-----   1 root operator -                             64192 May  1 02:34 quota.group
-rw-r-----   1 root operator -                             64192 May  1 02:34 quota.user
```

### 设置配额限制

要验证配额是否已启用，可以运行以下命令：

```sh
$ quota -v
Disk quotas for user ykla (uid 1001):
Filesystem        usage    quota   limit   grace  files   quota  limit   grace
/                    32        0       0              9       0      0
```

系统至此已具备使用 `edquota` 设置配额限制的条件。

配额限制可基于磁盘空间（块配额）、文件数量（inode 配额）或两者的组合进行设定。每种限制进一步细分为两个类别：硬限制和软限制。

硬限制是不可超过的。当用户达到硬限制时，该用户在该文件系统上将无法再分配任何空间。例如，如果用户在文件系统上的硬限制为 500 KB，并且当前使用了 490 KB，则该用户只能分配额外的 10 KB。尝试分配额外的 11 KB 将失败。

软限制允许在一定时间内超出，该时间段称为宽限期，默认为一周。若用户超出软限制且宽限期已过，软限制将转变为硬限制，不再允许进一步分配。当用户重新降至软限制以下时，宽限期将重置。

在以下示例中，编辑 `ykla` 账户的配额。调用 `edquota` 时，将打开由环境变量 `EDITOR` 指定的编辑器以编辑配额限制，默认编辑器为 nvi。

```sh
# edquota -u ykla
Quotas for user ykla:
/: in use: 32k, limits (soft = 0k, hard = 0k)	# 块配额限制
        inodes in use: 9, limits (soft = 0, hard = 0)	# inode 配额限制
```

可以更改块配额和 inode 配额来配置配额限制。例如，要将 **/** 的块限制提高到软限制 `100` 和硬限制 `120`，将该行的值更改为：

```sh
/: in use: 32k, limits (soft = 100k, hard = 120k)
```

退出编辑器后，新配额限制将生效。用户只能检查自己的配额和自己所属组的配额。只有超级用户才能查看所有用户和组的配额。

```sh
# quota -v ykla
Disk quotas for user ykla (uid 1001):
Filesystem        usage    quota   limit   grace  files   quota  limit   grace
/                    32      100     120              9       0      0
```

通常，用户未使用任何磁盘空间的文件系统不会出现在 quota(1) 的输出中，即使该用户对该文件系统拥有配额。

某些场景下需要为一批用户设置相同的配额限制。可先为某个用户分配所需的配额限制，再使用 `-p` 选项将该配额复制到指定范围的用户 ID（UID）。以下命令将 UID `10000` 至 `19999` 的用户复制配额限制：

```sh
# edquota -p ykla 10000-19999
```

## 课后习题

1. 在虚拟机环境中模拟 UFS2 分区扩容，先通过 gpart recover 恢复 GPT 分区表，再执行 gpart resize 和 growfs 操作，验证扩容前后的磁盘使用情况变化。

2. 分析 UFS2 文件系统为什么只能扩大而不能缩小，并尝试解决。

3. 对比使用 growfs 服务和手动执行 growfs 命令的差异，尝试不使用 service growfs onestart 而直接调用 growfs，验证其行为变化。
