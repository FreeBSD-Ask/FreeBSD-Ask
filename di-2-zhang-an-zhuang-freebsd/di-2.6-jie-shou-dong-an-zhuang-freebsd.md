# 第 2.6 节 手动安装 FreeBSD

总是有人想用 [LFS](https://www.linuxfromscratch.org/lfs/) 的方式来安装 FreeBSD，但是 FreeBSD 基本系统是一个有机整体，不是由单个软件包构成的，因此我认为这难以实现，参考 [ghostBSD](https://github.com/GhostBSD) 的代码我也没有看出来他的裁剪方法。有能力者请反馈。

但是你可以不使用 FreeBSD 的安装工具—bsdinstall，自己手动安装 FreeBSD。

主要思想就是自己对磁盘进行分区，解压缩所需要的 txz 压缩文件，然后对其进行配置（如引导，创建用户，设置密码网络等等）。

所需要考虑的问题不止一个，例如如何使用 zfs（如果你想），不同的引导下 UEFI BIOS 的引导配置方法是不一样的。

手动安装需要你有极强的动手能力，起码自己安装过 Gentoo Linux。

参考文献：

- [How to manually install FreeBSD on a remote server (with UFS, ZFS, encryption...)](https://stanislas.blog/2018/12/how-to-install-freebsd-server/)
- [RootOnZFS/GPTZFSBoot](https://wiki.freebsd.org/RootOnZFS/GPTZFSBoot)

以上我仅测试过 UFS 相关。

