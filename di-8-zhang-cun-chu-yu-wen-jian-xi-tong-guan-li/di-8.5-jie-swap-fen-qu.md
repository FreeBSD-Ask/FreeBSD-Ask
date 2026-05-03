# 8.5 swap 分区

swap 空间是操作系统中内存管理的组成部分。

在 FreeBSD 中，swap 可通过传统分区、交换文件或 ZFS 卷（ZVOL）等多种方式实现。本节重点阐述在系统安装后如何添加 swap 空间的技术方案。

若在系统安装阶段未配置 swap（交换分区），则仅能通过 dd 命令创建交换文件或 ZFS 卷的方式实现，这是因为 UFS 及 ZFS 文件系统均不支持分区收缩操作。

## 目录结构

```sh
/
├── usr
│   └── swap0                       # 交换文件
├── etc
│   ├── rc.conf                      # 系统启动配置文件
│   └── fstab                        # 持久化挂载配置文件
└── dev
    ├── md0                          # 内存磁盘（用于交换文件）
    ├── nda0p3                       # 交换分区
    └── zvol
        └── zroot
            └── swap                 # ZFS 交换卷
```

## 基于 dd 命令的传统交换文件方案

创建一个大小为 8 GB（1 GB = 1024 MB，如需更大容量，请读者进行简单的容量计算）的交换文件 `/usr/swap0`：

```sh
# dd if=/dev/zero of=/usr/swap0 bs=1M count=8192 status=progress  # bs=1M 表示使用 1MB 块写入零；status=progress 用于显示写入进度
  8416919552 bytes (8417 MB, 8027 MiB) transferred 4.011s, 2098 MB/s # 该输出为实时刷新信息
8192+0 records in
8192+0 records out
8589934592 bytes transferred in 4.071005 secs (2110028088 bytes/sec)
```

设置交换文件的访问权限，仅允许所有者进行读写操作：

```sh
# chmod 0600 /usr/swap0
```

若要立即启用，需将交换文件通过 mdconfig 配置为内存磁盘设备，再使用 swapon 激活交换空间，其中 mdconfig 用于将文件映射为内存磁盘，swapon 用于激活交换设备：

```sh
# mdconfig -a -t vnode -f /usr/swap0 -u 0 && swapon /dev/md0
```

若要在系统重启后仍能生效，还需在 `/etc/rc.conf` 配置文件中添加以下内容：

```ini
swapfile="/usr/swap0"
```

该配置用于定义交换文件的路径。

## 使用 ZFS 卷作为 swap 空间

> **警告**
>
> 本节所述操作可能会影响系统崩溃转储功能。

> **警告**
>
> 根据 OpenZFS Project. OpenZFS 文档[EB/OL]. [2026-03-26]. <https://openzfs.github.io/openzfs-docs/Getting%20Started/Ubuntu/Ubuntu%2022.04%20Root%20on%20ZFS.html> 所述，在内存压力极高的系统上，无论 swap 空间剩余多少，使用 zvol 作为 swap 设备都可能导致系统锁死。参见：OpenZFS Project. Swap deadlock in 0.7.9[EB/OL]. [2026-03-26]. <https://github.com/openzfs/zfs/issues/7734>。而将 swap 放置在其他分区上又可能会影响 ZFS 对 swap 的数据校验，因此上游文档建议弃用 swap。需要注意的是，swap 对于系统休眠功能至关重要，若需要该功能，需至少保证 swap 的容量不小于系统内存容量。

在 ZFS 池 zroot 下创建大小为 8 GB 的 zvol（ZFS 块设备卷）用作交换空间：

```sh
# zfs create -V 8G -b $(getconf PAGESIZE) -o logbias=throughput -o sync=always -o primarycache=metadata -o com.sun:auto-snapshot=false zroot/swap
```

对上述命令的参数说明如下：

- `$(getconf PAGESIZE)`：可返回系统页面大小（固态硬盘通常返回值为 `4096`），从而使 swap 卷与系统页面对齐，以期提高性能
- `-o`：用于指定选项（option），语法为 `-o 属性名=属性值`
- `-o logbias=throughput`：ZFS 将优化同步操作，提高池的全局吞吐量并有效利用资源，可提升文件写入性能
- `-o sync=always`：强制所有写入操作实时同步
- `-o primarycache=metadata`：控制 ARC 的缓存策略，仅缓存元数据，不缓存实际数据块，避免 ARC 将 swap 数据缓存到内存
- `-o com.sun:auto-snapshot=false`：禁用自动快照功能，因为通常无需对 swap 进行快照
- 参数 `-V`：用于创建 ZFS 卷（zvol）而非 ZFS 文件系统
- 在 FreeBSD 中，ZFS 默认的池名称为 `zroot`
- 本次创建的卷名称为 `swap`

启用 ZFS zvol 作为交换空间：

```sh
# swapon /dev/zvol/zroot/swap
```

在 `/etc/fstab` 文件中添加 ZFS zvol 交换分区的挂载项，以实现开机时自动挂载：

```ini
/dev/zvol/zroot/swap none swap sw 0 0
```

写入配置后，可使用命令 `swapon -a` 进行检查（`-a` 表示激活 `/etc/fstab` 中所有 swap 条目），确保无错误输出。

### 参考文献

- OpenZFS Project. FAQ[EB/OL]. [2026-03-25]. <https://openzfs.github.io/openzfs-docs/Project%20and%20Community/FAQ.html>. OpenZFS 官方常见问题解答，提供 ZFS 卷配置的最佳实践。
- Oracle. Oracle Solaris ZFS 管理指南[EB/OL]. [2026-03-25]. <https://docs.oracle.com/cd/E19253-01/819-7065/givdo/index.html>. Oracle 官方 ZFS 技术文档，系统阐述 ZFS 存储管理方法。
- FreeBSD Project. swapon(8) -- specify additional devices for paging and swapping[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=swapon&sektion=8>. 交换空间管理工具手册页。
- FreeBSD Project. swapinfo(8) -- display system swap space usage[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=swapinfo&sektion=8>. 交换空间使用信息查询工具手册页。

## 查看 swap 使用量

以更易读的单位显示系统交换空间信息：

```sh
# swapinfo -h
Device              Size     Used    Avail Capacity
/dev/nda0p3         2.0G       0B     2.0G     0%
```

选项 `-h` 表示以人类可读格式（human-readable）输出。参见 FreeBSD Project. man swapinfo(8)[EB/OL]. [2026-03-26]. <https://man.freebsd.org/cgi/man.cgi?swapinfo(8)>。

从输出可知，`/dev/nda0p3` 为交换分区，其大小为 2 GB，当前已使用量为 0。

## 课后习题

1. 使用 dd 命令创建一个 4 GB 的交换文件，配置 `/etc/rc.conf` 文件实现开机自动启用，重启后使用 swapinfo 验证交换空间是否正常工作。

2. 对比传统交换文件和 ZFS 卷作为 swap 的实现机制，重构一个最小化的 swap 配置脚本，分析两者在性能、可靠性和系统崩溃转储支持上的权衡。

3. 修改 ZFS 卷作为 swap 的参数配置，尝试调整 logbias、sync 或 primarycache 选项，验证参数变化对系统行为的影响。
