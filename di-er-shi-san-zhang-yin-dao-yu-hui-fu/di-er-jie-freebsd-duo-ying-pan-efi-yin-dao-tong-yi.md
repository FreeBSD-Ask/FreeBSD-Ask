# 第二节 FreeBSD多硬盘EFI引导统一

何谓多硬盘 EFI 统一？就是说有两块硬盘，两块硬盘上分别都有EFI分区，一个分区里是 FreeBSD，另一个是Windows。现在只想保留一个分区，即想把EFI配置文件放到一块硬盘的EFI分区里统一管理。

设装有 Windows 的硬盘为 ada0，FreeBSD 的硬盘为 nvd0.首先关闭 Windows 的快速启动启动：命令为powercfg /h off，然后关机重启进入 FreeBSD，创建挂载点 mkdir /mnt/efi。检测 ada0p1（硬盘的第一个分区）是不是我们要挂载的 EFI 分区，输入命令 fstyp /dev/ada0p1，我的输出是 NTFS，可见不是我们想要的EFI 分区；fstyp /dev/ada0p2，输出 msdosfs，是我们的 Windows 磁盘上的 EFI 分区。

接下来挂载 ada0 磁盘上的EFI分区到 FreeBSD 的/mnt/efi: mount -t msdosfs /dev/ada0p2 /mnt/efi

为FreeBSD 引导性创建 EFI 路径下的目录: mkdir /mnt/efi/EFI/freebsd

然后复制启动文件到该路径 cp /boot/boot1.efi /mnt/efi/EFI/freebsd/bootx64.efi

最后生成启动项：efibootmgr -c -l /mnt/efi/EFI/freebsd/bootx64.efi -L “FreeBSD niu pi”

重启进入 Windows ，使用 easyuefi 激活 FreeBSD niu pi 这个启动项即可。如没有问题，可使用 DiskGenius 删除 nvd0 磁盘的 EFI 分区文件。
