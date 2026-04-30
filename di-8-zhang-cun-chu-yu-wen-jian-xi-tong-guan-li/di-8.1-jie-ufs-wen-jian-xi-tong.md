# 8.1 UFS 文件系统

## 概述

UFS 全称为 Unix File System（UNIX 文件系统），FreeBSD 中使用的 UFS 实际上是伯克利快速文件系统（Berkeley Fast File System，FFS），由 Kirk McKusick、Bill Joy 等人于 1983 年随 4.2BSD 首次引入，其设计理念可追溯至更早的 Unix 文件系统。历史上，macOS 也曾使用该文件系统作为根文件系统。

需要明确区分，本节所述的 UFS 文件系统与手机等设备中使用的 UFS 存储属于完全不同的技术范畴。后者全称为 Universal Flash Storage（通用闪存存储），是一种硬件存储标准，目前已发展至 4.1 版本（FreeBSD 在 10.4 版本中支持 eMMC；FreeBSD 15.0 已通过 `ufshci` 驱动支持 UFS 存储）。

作为文件系统的 UFS，其当前版本号为 2。基于 Linux 的 Android 系统不支持 UFS 文件系统，此类设备的根文件系统通常为 ext4（部分新设备采用 F2FS），而 Linux 对 UFS 的读写支持尚不完整。

> **警告**
>
> UFS 文件系统只能扩大，不能缩小。

## 磁盘扩容操作

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

## 参考文献

- FreeBSD Project. ffs -- Berkeley fast file system[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?ffs(7)>. UFS/FFS 文件系统概述手册页，描述伯克利快速文件系统的设计与实现。
- FreeBSD Project. mount_ufs -- mount a UFS file system[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?mount_ufs(8)>. UFS 文件系统挂载命令手册页。
- FreeBSD Project. newfs -- install a UFS file system[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?newfs(8)>. UFS 文件系统创建工具手册页。
- FreeBSD Project. gpart -- control utility for the disk partitioning GEOM class[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?gpart(8)>. 磁盘分区管理工具手册页。
- FreeBSD Project. growfs -- expand a UFS file system[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?growfs(8)>. UFS 文件系统扩容工具手册页。
- FreeBSD Project. fsck_ffs -- file system consistency check and interactive repair[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?fsck_ffs(8)>. UFS 文件系统一致性检查与修复工具手册页。
- Jaeyoon Choi. Universal Flash Storage on FreeBSD[EB/OL]. [2026-04-16]. <https://freebsdfoundation.org/our-work/journal/browser-based-edition/freebsd-15-0/universal-flash-storage-on-freebsd/>。该文介绍了 FreeBSD UFS 驱动的开发过程及当前状态。
- McKusick M K. 4.4BSD 操作系统设计与实现[M]. 李善平，刘文峰，马天驰，译. 北京：机械工业出版社，2012. 该书第 7 章详细描述了 FFS 的设计与历史。
- McKusick M K, Joy W N, Leffler S J, et al. A Fast File System for UNIX[J]. ACM Transactions on Computer Systems，1984，2(3)：181-197. FFS 原始论文，首次系统阐述了伯克利快速文件系统的设计与实现。

## 课后习题

1. 在虚拟机环境中模拟 UFS2 分区扩容，先通过 gpart recover 恢复 GPT 分区表，再执行 gpart resize 和 growfs 操作，验证扩容前后的磁盘使用情况变化。

2. 分析 UFS2 文件系统为什么只能扩大而不能缩小，并尝试解决。

3. 对比使用 growfs 服务和手动执行 growfs 命令的差异，尝试不使用 service growfs onestart 而直接调用 growfs，验证其行为变化。
