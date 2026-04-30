# 8.1 UFS 文件系统

## 概述

UFS 全称为 Unix File System（UNIX 文件系统），FreeBSD 中使用的 UFS 实际上是伯克利快速文件系统（Berkeley Fast File System，FFS），由 Kirk McKusick、Bill Joy 等人于 1983 年随 4.2BSD 首次引入，其设计理念可追溯至更早的 Unix 文件系统。历史上，macOS 也曾使用该文件系统作为根文件系统。

需要明确区分，本节所述的 UFS 文件系统与手机等设备中使用的 UFS 存储属于完全不同的技术范畴。后者全称为 Universal Flash Storage（通用闪存存储），是一种硬件存储标准，目前已发展至 4.1 版本（FreeBSD 在 10.4 版本中支持 eMMC；FreeBSD 15.0 已通过 `ufshci` 驱动支持 UFS 存储）。

作为文件系统的 UFS，其当前版本号为 2。基于 Linux 的 Android 系统不支持 UFS 文件系统，此类设备的根文件系统通常为 ext4（部分新设备采用 F2FS），而 Linux 对 UFS 的读写支持尚不完整。

> **警告**
>
> UFS 文件系统只能扩大，不能缩小。

## UFS 文件系统磁盘扩容

> **注意**
>
> 此方案仅适用于向后扩展；若 freebsd-ufs 分区前方存在空余空间，则无法使用此方法进行扩展。

首先，使用 `gpart show` 命令显示系统中所有磁盘的分区布局：

```sh
# gpart show
=>       3  41943035  da0  GPT  (20G)
         3       122    1  freebsd-boot  (61K)
       125     66584    2  efi  (33M)
     66709   2097152    3  freebsd-swap  (1.0G)
   2163861  10486633    4  freebsd-ufs  (5.0G)
  12650494  29292544       - free -  (14G)
```

系统盘初始大小为 5 GB，输出显示 `da0` 磁盘仅包含一个 UFS 分区。

### 执行扩容命令序列

> **警告**
>
> 若使用的是 GPT 分区表，此处的扩容操作在虚拟机或云服务器环境中可能会破坏 GPT 分区表，原因是虚拟机或云平台在调整磁盘大小时可能未正确更新 GPT 分区表的备份副本，因此需首先恢复 `da0` 磁盘的分区表：
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

选项 `-i` 用于指定要扩容的分区编号，此处用于扩展 `freebsd-ufs` 分区。

### 扩展文件系统

使用 growfs 服务扩展文件系统（该操作仅需执行一次，完成后无需重复运行）：

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

growfs 是 FreeBSD 用于扩展 UFS 文件系统的工具，它通过调整文件系统的柱面组和超级块，使文件系统能够利用新增加的分区空间。

### 验证扩容结果

显示已挂载文件系统的磁盘使用情况：

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

- `-h`：以人类可读格式显示（单位为 KB、MB、GB 等）
- `-l`：仅显示本地文件系统

上述输出表明，分区扩展操作已完成，且文件系统已成功调整至新的大小。

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

UFS 快照可以使用户创建指定文件系统的镜像，并将其作为文件处理。

必须在执行操作的文件系统中创建快照文件，每个 UFS 文件系统最多可以创建 20 个快照。活动快照会记录在超级块中，因此它们在卸载和重新挂载操作以及系统重启后会保持持久性。当不再需要某个快照时，可以使用 [rm(1)](https://man.freebsd.org/cgi/man.cgi?query=rm&sektion=1&format=html) 删除它。尽管可以按任意顺序删除快照，但可能无法彻底回收所有使用的空间，因为其他快照可能会占用一些已释放的块。

可以使用 [mksnap_ffs(8)](https://man.freebsd.org/cgi/man.cgi?query=mksnap_ffs&sektion=8&format=html) 创建 `/` 的快照，并存储到 `/.snap/snap1`：

```sh
# mksnap_ffs /.snap/snap1
```

>**技巧**
>
>mksnap_ffs 会自动快照指定目录所在的文件系统，不支持指定文件系统。上面是 UFS 标准安装的系统，因此会对完整的根分区进行快照。

快照是通过 [mount(8)](https://man.freebsd.org/cgi/man.cgi?query=mount&sektion=8&format=html) 创建的。要将 **/** 的快照放入文件 **/home/ykla/snapshot/snap** 中，请使用以下命令：

```sh
# mkdir -p /home/ykla/snapshot/
# mount -u -o snapshot /home/ykla/snapshot/snap /
```

UFS 快照文件的大小等于其来源文件系统的大小，但是实际上与 ZFS 类似：

```sh
# ls -loh /home/ykla/snapshot/snap	# 逻辑占用存储
-r--------  1 root ykla snapshot   19G May  1 01:55 /home/ykla/snapshot/snap
# du -hl /home/ykla/snapshot/snap	# 真实占用存储
6.1M	/home/ykla/snapshot/snap
```

不可更改的 `snapshot` 文件标志由 [mksnap_ffs(8)](https://man.freebsd.org/cgi/man.cgi?query=mksnap_ffs&sektion=8&format=html) 在快照文件初始创建时设置。

可以使用 [find(1)](https://man.freebsd.org/cgi/man.cgi?query=find&sektion=1&format=html) 查找文件系统中的快照文件，例如 **/**：

```sh
# find / -flags snapshot
/.snap/snap1
/home/ykla/snapshot/snap
```


可以作为文件系统的冻结镜像挂载快照。要只读挂载快照 **/home/ykla/snapshot/snap**，可以执行以下命令：

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
  
| 参数            | 含义       |
| ------------- | -------- |
| `-a`          | 创建 md 设备 |
| `-t vnode`    | 用文件作为磁盘  |
| `-o readonly` | 只读挂载     |
| `-f file`     | 指定快照文件   |
| `-u 4`        | 指定至 md4，防止冲突   |


现在，冻结的 **/var** 可以通过 **/mnt** 访问。一切都会保持快照创建时的状态。唯一的例外是，任何早期的快照将显示为空文件。要卸载快照，请执行：

```sh
# umount /mnt
# mdconfig -d -u 4
```

### 参考文献


- McKusick, M. McKusick.com[EB/OL]. [2026-04-30]. <http://www.mckusick.com/>. 有关 softupdates 和文件系统快照的更多信息，包括技术论文，请访问 Marshall Kirk McKusick 的网站。

## 课后习题

1. 在虚拟机环境中模拟 UFS2 分区扩容，先通过 gpart recover 恢复 GPT 分区表，再执行 gpart resize 和 growfs 操作，验证扩容前后的磁盘使用情况变化。

2. 分析 UFS2 文件系统为什么只能扩大而不能缩小，并尝试解决。

3. 对比使用 growfs 服务和手动执行 growfs 命令的差异，尝试不使用 service growfs onestart 而直接调用 growfs，验证其行为变化。
