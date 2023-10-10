# 第 6.1 节 UFS

UFS 全称是 Unix File System，即 UNIX 文件系统，基于 UNIX v7。过去，MACOS 也使用该文件系统作为 root 文件系统。目前 FreeBSD 在使用的是 UFS2。Linux 对 UFS 的读写支持也不完整。这个文件系统只能扩大不能被缩小。

> **注意**
>
> UFS 文件系统和手机等设备中使用的 UFS 存储完全不是一回事，那个 UFS 是 Universal Flash Storage（通用闪存存储）的缩写，已经出到 4.0 了。而作为文件系统的 UFS 版本号才是 2。而且手机内部的系统也不可能是 UFS 文件系统，因为基于 Linux 的安卓根本不支持 UFS 这个文件系统，这些设备一般的根文件系统是 ext4（一些新设备是 F2FS）。
