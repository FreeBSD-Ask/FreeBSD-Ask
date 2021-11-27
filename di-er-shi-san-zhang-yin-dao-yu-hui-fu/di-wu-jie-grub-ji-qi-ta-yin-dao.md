# 第五节 Grub 及其他引导

根据 FreeBSD 开发者介绍由于 grub 的 ZFS 模块不采用 BSD 而是自己开发的，导致 grub 无法直接引导 FreeBSD 的内核从而启动系统。只能采取 chainlain+1 的方式间接引导。
