# 9.4 ZFS 数据压缩

ZFS 支持多种压缩算法。

不同压缩算法在压缩比、压缩速度与解压速度方面各有优劣，需根据工作负载特征进行选择。

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

## Zstandard 压缩算法深度解析

Zstandard（简称 Zstd）由 LZ4 的原始作者 Yann Collet 创建，目的是提供类似于 gzip 的压缩比，但速度与 LZ4 相当。Zstd 提供了多种压缩级别（1-19，以及“快速”1-9、“快速”10-100 以 10 为增量），允许存储管理员在性能和压缩比之间进行相对精细的控制。

### 压缩算法演进

最初，ZFS 支持的压缩算法较少：LZJB（一种由 Jeff Bonwick 创建的改进型 Lempel–Ziv 变体，速度适中，但压缩比率较低）、ZLE（零长度编码，仅压缩零的连续序列）以及九个级别的 gzip。用户因此常常会竭尽全力将应压缩的数据与已经压缩的数据分开，以避免 ZFS 尝试重新压缩已压缩的数据。由于各种历史原因，压缩在新创建的 ZFS 存储池中仍默认“关闭”。

在 2013 年，ZFS 新增了 LZ4 压缩算法，它比 LZJB 提供了更高的速度和更好的压缩比。2015 年，当用户启用压缩而未指定算法时，LZ4 取代了 LZJB 成为默认算法。通过这一新的高速压缩器，加上“早期中止”功能，全局启用压缩变得可行——无法压缩的数据会被快速检测并跳过，从而避免影响性能。早期中止功能通过限制压缩算法输出缓冲区的大小，使其比输入缓冲区小八分之一。如果压缩算法无法将输出数据放入更小的缓冲区，它将失败并返回错误。

### Zstd 的优势

Zstd 的主要优势之一是解压速度与压缩级别无关。对于那些写入一次但多次读取的数据，Zstd 允许使用最高的压缩级别而不会产生性能损失。在写入大量数据时，ZFS 会单独压缩每个记录，因此能够充分利用现代系统上多个处理器核心的优势。

最大的优势之一来自于压缩 ARC 功能——ZFS 的自适应替换缓存（ARC）现在会将数据的压缩版本缓存到 RAM 中，并在每次请求时进行解压。这使得相同数量的缓存能够存储更多的逻辑数据和元数据，从而增加缓存命中率，并提高访问频繁或最近访问的数据的性能。如果从 LZ4 升级到 Zstd 增加了磁盘上的压缩比，这些增益会直接放大压缩 ARC 中每个字节的效能。

使用更大的 ZFS 记录大小（recordsize）可以实现更高的压缩比。原因在于 ZFS 独立地压缩每个记录，因此记录大小对压缩增益有很大影响；记录越大，压缩字典就越优化。

需要注意的一点是，如果压缩带来的节省不足以节省至少一个磁盘扇区，ZFS 将不会存储压缩后的块。例如，在典型的数据库文件系统中，如果记录大小为 16 KB，且压缩比为 1.32x，最终块的大小为 12.1 KB，那么仍然需要存储四个 4 KB 的扇区，因此直接存储未压缩的数据反而会更有效。然而，如果压缩比为 1.34x，所需的存储空间为 11.9 KB，这可以通过三个 4 KB 的扇区来实现，因此 ZFS 会使用压缩版本。

### Zstd 的磁盘格式集成

在 ZFS 的磁盘格式中，压缩类型存储在每个块指针的 8 位字段中。Zstd 补丁引入了 41 个额外的压缩级别，但解压函数对所有 Zstd 级别都是相同的。Zstd 压缩块使用了比 LZ4 更大的头部，除了大小外，还存储了 Zstd 的版本和压缩级别。存储 Zstd 的版本使得在将来更容易升级 Zstd 的版本，使系统能够包括多个版本的 Zstd 压缩函数，从而在需要时始终能够重新创建一个块。这对于“NOPwrite”功能最为实用：当一个块需要被覆盖时，ZFS 可以比较新块的校验和，如果它与旧块相同，则无需重新写入数据。

## 参考文献

- FreeBSD Project. zfs -- configures ZFS datasets[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?zfs(8)>. ZFS 数据集管理工具手册页，涵盖压缩属性设置。
- FreeBSD Project. zfsprops -- native and user-defined properties of ZFS datasets[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?zfsprops(7)>. ZFS 数据集属性手册页，定义 compression、compressratio 等属性。

## 课后习题

1. 在 FreeBSD 虚拟机中分别使用 lz4、zstd-1、zstd-9 三种压缩算法创建 ZFS 池，测试相同数据集在不同算法下的压缩比与读写性能差异。
2. 选取 ZFS 数据压缩的透明压缩机制，编写一个最小脚本测试不同工作负载下的压缩效果。
3. 修改 ZFS 压缩策略，将 /usr/ports 数据集设置为不压缩，将 /var/log 设置为 zstd-9 压缩，验证其压缩比与系统响应变化。
