# 9.4 ZFS 数据压缩

本节阐述 ZFS 内置数据压缩功能的技术原理与实践应用。ZFS 支持多种压缩算法。

不同压缩算法在压缩比、压缩速度与解压速度方面各有优劣，需根据工作负载特征进行选择。

本节介绍 ZFS 数据压缩功能的使用方法，包括查看和设置压缩属性。

首先查看各 ZFS 文件系统的数据压缩属性及其当前设置：

```sh
# zfs get compression
NAME                PROPERTY     VALUE           SOURCE
zroot               compression  lz4             local
zroot/ROOT          compression  lz4             inherited from zroot
zroot/ROOT/default  compression  lz4             inherited from zroot
zroot/home          compression  lz4             inherited from zroot
zroot/home/ykla     compression  lz4             inherited from zroot
zroot/tmp           compression  lz4             inherited from zroot
zroot/usr           compression  lz4             inherited from zroot
zroot/usr/ports     compression  lz4             inherited from zroot
zroot/usr/src       compression  lz4             inherited from zroot
zroot/var           compression  lz4             inherited from zroot
zroot/var/audit     compression  lz4             inherited from zroot
zroot/var/crash     compression  lz4             inherited from zroot
zroot/var/log       compression  lz4             inherited from zroot
zroot/var/mail      compression  lz4             inherited from zroot
zroot/var/tmp       compression  lz4             inherited from zroot
```

将 zroot 文件系统的数据压缩算法设置为 zstd-5 级别：

```sh
# zfs set compression=zstd-5 zroot
```

> **注意**
>
> 压缩属性变更立即生效，无需重启系统。但该属性仅对新写入的数据生效，不会自动压缩已有的数据。

再次列出各个 ZFS 文件系统的数据压缩属性及其当前设置：

```sh
# zfs get compression
NAME                PROPERTY     VALUE           SOURCE
zroot               compression  zstd-5          local
zroot/ROOT          compression  zstd-5          inherited from zroot
zroot/ROOT/default  compression  zstd-5          inherited from zroot
zroot/home          compression  zstd-5          inherited from zroot
zroot/home/ykla     compression  zstd-5          inherited from zroot
zroot/tmp           compression  zstd-5          inherited from zroot
zroot/usr           compression  zstd-5          inherited from zroot
zroot/usr/ports     compression  zstd-5          inherited from zroot
zroot/usr/src       compression  zstd-5          inherited from zroot
zroot/var           compression  zstd-5          inherited from zroot
zroot/var/audit     compression  zstd-5          inherited from zroot
zroot/var/crash     compression  zstd-5          inherited from zroot
zroot/var/log       compression  zstd-5          inherited from zroot
zroot/var/mail      compression  zstd-5          inherited from zroot
zroot/var/tmp       compression  zstd-5          inherited from zroot
```

查看各个 ZFS 文件系统的实际数据压缩比：

> **注意**
>
> `compressratio` 表示已压缩数据与未压缩数据的比值。例如 2.70x 表示数据被压缩到原始大小的约 37%。

```sh
# zfs get compressratio
NAME                PROPERTY       VALUE  SOURCE
zroot               compressratio  2.70x  -
zroot/ROOT          compressratio  2.68x  -
zroot/ROOT/default  compressratio  2.68x  -
zroot/home          compressratio  1.00x  -
zroot/home/ykla     compressratio  1.01x  -
zroot/tmp           compressratio  1.00x  -
zroot/usr           compressratio  2.73x  -
zroot/usr/ports     compressratio  1.00x  -
zroot/usr/src       compressratio  2.73x  -
zroot/var           compressratio  1.47x  -
zroot/var/audit     compressratio  1.00x  -
zroot/var/crash     compressratio  1.01x  -
zroot/var/log       compressratio  2.90x  -
zroot/var/mail      compressratio  1.00x  -
zroot/var/tmp       compressratio  1.00x  -
```

## 参考文献

- FreeBSD Project. zfs -- configures ZFS datasets[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?zfs(8)>. ZFS 数据集管理工具手册页，涵盖压缩属性设置。
- FreeBSD Project. zfsprops -- native and user-defined properties of ZFS datasets[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?zfsprops(7)>. ZFS 数据集属性手册页，定义 compression、compressratio 等属性。

## 课后习题

1. 在 FreeBSD 虚拟机中分别使用 lz4、zstd-1、zstd-9 三种压缩算法创建 ZFS 池，测试相同数据集在不同算法下的压缩比与读写性能差异。
2. 选取 ZFS 数据压缩的透明压缩机制，编写一个最小脚本测试不同工作负载下的压缩效果。
3. 修改 ZFS 压缩策略，将 /usr/ports 数据集设置为不压缩，将 /var/log 设置为 zstd-9 压缩，验证其压缩比与系统响应变化。
