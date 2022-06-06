# 第五节 Grub 及其他引导

注意，本书所有 `grub` 均为 `grub2`。

根据 FreeBSD 开发者介绍由于 `grub` 的 ZFS 模块不采用 BSD 提供的，而是自己开发的，导致 `grub` 无法直接引导 FreeBSD 的内核从而启动系统。只能采取 `chainlain+1` 的方式间接引导。

```
menuentry "FreeBSD-13.0 Release" {
set root='(hd0,gpt1)'  # 请自己检查
chainloader /boot/boot1.efi
}
```
