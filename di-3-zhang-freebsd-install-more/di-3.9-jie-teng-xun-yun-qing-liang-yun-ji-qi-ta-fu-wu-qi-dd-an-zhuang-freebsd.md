# 3.9 云服务器安装 FreeBSD（基于腾讯云轻量云、阿里云轻量应用服务器）

这实质上是通过本地硬盘安装 FreeBSD。即在不依赖额外介质的前提下，借助已有的操作系统（Linux）完成 FreeBSD 的安装。

## 使用基于 VirtIO 半虚拟化技术的虚拟机

> **注意**
>
> 以下内容仅供参考，有待测试。如果你测试通过，请告知我们！

根据反馈，在 VMware ESXi 等半虚拟化平台上安装或升级 FreeBSD 时可能遇到故障（例如阿里云的 VirtIO-BLK 驱动问题）。需在开机时按 **ESC** 键，输入 `set kern.maxphys=65536` 并按回车，再输入 `boot` 才能正常启动。安装完成后，在 `/boot/loader.conf` 中加入 `kern.maxphys=65536` 即可避免每次开机重复此操作。阿里云升级后可能会因此类问题卡在引导界面，此时需通过 VNC 连接并执行上述操作。

> **注意**
>
> 对于已停止安全支持的版本（如 9.2），请参考本文内容，并结合“手动安装 FreeBSD”章节进行操作。

>**警告**
>
>安装前，请在原有的 Linux 系统中查看 IP 地址及子网掩码。可使用命令 `ip addr` 和 `ip route show` 查看网关信息及最大传输单元（MTU）数值；同时请注意子网和 CIDR 表示法。因为部分服务器未启用 DHCP 服务，因此需要手动配置 IP。


## 视频教程

[08-腾讯云轻量云及其他服务器安装 FreeBSD](https://www.bilibili.com/video/BV1y8411d7pp)

视频内容与文字教程可能存在差异，任选其一操作即可。SCP 命令可以使用图形化工具 WinSCP 替代。安装完成后，建议按照其他章节设置密钥登录并禁用密码验证，以提升安全性。

## 概述

[腾讯云轻量应用服务器（即腾讯云轻量云）](https://cloud.tencent.com/product/lighthouse) 以及 [阿里云轻量应用服务器](https://www.aliyun.com/product/swas) 均未提供 FreeBSD 系统支持，只能通过特殊方法手动安装。

>**警告**
>
>请注意数据安全。本教程操作具有一定风险，并要求你具备一定的动手能力。

上述服务器的管理面板未提供 FreeBSD 镜像，因此需要采用变通方法进行安装。由于 FreeBSD 与 Linux 在内核及可执行文件格式上不兼容，因此无法通过 `chroot` 后删除原系统的方式进行安装。安装方法为：首先在内存盘中启动 FreeBSD 系统（即先引导 [mfsBSD](https://mfsbsd.vx.sk)），然后格式化硬盘并安装新系统。mfsBSD 是一款完全载入内存的 FreeBSD 系统，类似于 Windows PE 环境。


我们需要下载 [img 格式的 mfsBSD 镜像](https://mfsbsd.vx.sk/files/images/14/amd64/mfsbsd-se-14.2-RELEASE-amd64.img)，可提前下载后通过 WinSCP 上传至服务器；若直接在服务器上下载，可能耗时较长（约两小时）。


## 取消隐藏的 GRUB 菜单

目前大多数 Linux 发行版的 GRUB 菜单默认处于隐藏状态，需在开机时按 Esc 键唤出，但该操作有时会直接进入 BIOS 设置界面。因此，直接取消隐藏菜单更为方便。

```sh
# grub2-editenv - unset menu_auto_hide
```

## 使用 mfsLinux 写入 mfsBSD

如前所述，由于 FreeBSD 与 Linux 生态不同，需要先引导至一个运行在内存中的 Linux 环境，在该环境中将 mfsBSD 写入硬盘，最后通过 `bsdinstall` 工具完成系统安装。

在 mfsBSD 下载页面的下方，可找到 [mfsLinux](https://mfsbsd.vx.sk/files/iso/mfslinux/mfslinux-0.1.11-94b1466.iso)，这正是我们所需的 Linux 环境。由于它仅提供 ISO 格式，无法在当前环境下直接启动。由于其基于纯 initrd 架构，需要从中提取内核和 initrd 文件，存放于硬盘并进行手动引导。

在典型的 Linux 系统中，initrd 是一个被打包为内存盘的精简根文件系统，内含驱动程序、挂载工具以及启动初始化程序所必需的数据。开机时，引导加载程序（Bootloader）加载内核与 initrd，由 initrd 中的脚本执行启动准备，随后移交控制权给硬盘上的初始化程序。

首先，将从该 ISO 中提取出的内核和 initrd 文件放置于根目录。重启机器并进入 GRUB 命令行界面（可在引导倒计时时按 `e` 键进入编辑模式，删除原有 `linux` 和 `initrd` 行的内容并修改，完成后按 `Ctrl+X` 启动）。手动指定启动的内核与 initrd（可使用 `Tab` 键补全路径）。输入 `boot` 并按回车即可继续启动。或按 `c` 键进入 GRUB 命令行模式。

```sh
linux (hd0,msdos1)/vmlinuz
initrd (hd0,msdos1)/initramfs.igz
boot # 输入 boot 后回车即可继续启动
```

>**技巧**
>
>分区标识不一定是 `(hd0,msdos1)`，请以实际情况为准。注意不要误删过多内容导致无法辨识。

![](../.gitbook/assets/2.png)

这个特制的 initrd 启动后，不会加载硬盘上的原系统，而是自行配置网络并启动 SSH 服务器。由此，我们获得了一个运行在内存中的 Linux 系统。

此时应可以通过 SSH 连接到服务器，并安全地对硬盘进行格式化操作。

mfsBSD 和 mfsLinux 镜像的默认 `root` 密码均为 `mfsroot`。

```sh
# cd /tmp # 切换至临时目录
# wget https://mfsbsd.vx.sk/files/images/14/amd64/mfsbsd-se-14.2-RELEASE-amd64.img # 下载 mfsBSD 镜像
# dd if=mfsbsd-se-14.2-RELEASE-amd64.img of=/dev/vda # 请确认你的硬盘设备是否为 /dev/vda
# reboot # 重启系统
```

>**技巧**
>
>建议在此处使用服务器的“快照”功能进行备份，以防后续操作失误导致重装，耽误时间。

## 安装 FreeBSD

通过 SSH 连接服务器后，执行 `kldload zfs` 加载 ZFS 模块，然后运行 `bsdinstall`。在出现图示界面时，选择 `Other` 并输入指定的镜像地址（地址中包含相应版本即可，可自行更改）：

示例：例如 <https://mirrors.ustc.edu.cn/freebsd/releases/amd64/14.2-RELEASE/> 或 <https://mirrors.nju.edu.cn/freebsd/snapshots/amd64/15.0-CURRENT/>

![腾讯云轻量云及其他服务器安装 FreeBSD](../.gitbook/assets/installBSD1.png)

![腾讯云轻量云及其他服务器安装 FreeBSD](../.gitbook/assets/installBSD2.png)

![腾讯云轻量云及其他服务器安装 FreeBSD](../.gitbook/assets/installBSD3.png)


- 我们也可以手动下载 FreeBSD 的安装文件，以 `MANIFEST` 文件为例：

```sh
# mkdir -p /usr/freebsd-dist # 创建目标目录
# cd /usr/freebsd-dist # 进入该目录
# fetch http://ftp.freebsd.org/pub/FreeBSD/releases/amd64/14.2-RELEASE/MANIFEST # 下载 MANIFEST 文件
```

## 故障排除与未尽事宜

### 为何不能直接使用 dd？（错误示范，仅供说明，请勿执行）

在正常的 Linux 系统中，若直接将 mfsBSD 的 img 镜像通过 `dd` 写入硬盘，重启后虽能正常加载引导程序，但可能因系统对硬盘的后续写入操作而导致无法正常挂载内存盘。

```sh
# wget https://mfsbsd.vx.sk/files/images/13/amd64/mfsbsd-se-13.1-RELEASE-amd64.img -O- | dd of=/dev/vda
```

解释：

- `|` 是管道符号，将上一个命令的标准输出作为下一个命令的标准输入。
- `-O-` 选项指示 wget 将文件下载并输出到标准输出；`dd` 在未指定 `if` 参数时会自动从标准输入读取数据。

直接执行此 `dd` 命令会报错，如图所示：


![](../.gitbook/assets/1.png)


### LVM 逻辑卷

如果云服务器使用了 LVM，需要将所有与引导相关的文件放置于 `/boot` 分区内，否则可能无法被正确识别。

### 腾讯云轻量应用可能无法获取 IPv6 地址

腾讯云 IPv6 地址的分配方式并非标准实现，其采用了自定义的子网方案。

腾讯云 IPv6 可能由专有服务提供，此问题尚待解决与确认。

### 失败的方案

#### 方案一

在 UEFI 模式下：

```sh
set iso=(hd0,gpt2)/bsd.iso
loopback loop $iso
set root=(loop)
chainloader /boot/loader.efi
boot # 输入 boot 后回车即可继续启动
```

此方法失败。该操作并非将镜像挂载为内存盘，虽可引导，但 FreeBSD 在启动过程中会报错，无法找到启动文件。

此外，在 UEFI 模式下，GRUB2 不提供 `linux16`、`kfreebsd` 等命令。


#### 方案二

在传统 BIOS 引导方式下。

- 安装 syslinux

- 需安装 syslinux 软件包以获得 MEMDISK 支持。

```bash
# dnf install syslinux
```

>**警告**
>
>GRUB2 自带的 `memdisk.mod` 模块并非 MEMDISK。必须安装 syslinux 包才能获得 MEMDISK 工具。

- 复制到 `/boot`

```sh
# cp /usr/share/syslinux/memdisk /boot/
```

```sh
ls # 显示磁盘
ls (hd0,gpt2)/ # 显示磁盘 (hd0,gpt2) 下的内容，MBR 分区表可能为 (hd0,msdosx)。不一定是 (hd0,gpt2)，以实际为准
linux16 (hd0,gpt2)/memdisk iso
initrd (hd0,gpt2)/bsd.iso
boot # 输入 boot 后回车即可继续启动
```

上述方法可能适用于 BIOS 搭配 MBR 分区表，但在 GPT 分区表下测试失败。

#### 方案三

缩小 Linux 的根分区（`/`），直接将 FreeBSD 的 img 镜像通过 `dd` 写入新分区。

此方案不可行，因为 XFS 文件系统不支持在线缩小（红帽系列发行版通常采用 XFS 搭配逻辑卷管理）。

#### 方案四

直接写入 EFI 分区。

此方案不可行，EFI 系统分区（ESP）的大小通常有限制。

#### 方案五

GRUB 不支持将 ISO 镜像挂载为内存盘，但其他引导程序或许可以实现这一功能。

目前尚未找到可行方案。

#### 方案六

对于支持在线调整的文件系统，可压缩出约 2 GB 的未分配空间，创建一个 FAT32 分区，再将 img 镜像 `dd` 写入该分区。

在 GRUB 中，使用 `chainloader +1` 指向 `dd` 操作后生成的 BSD EFI 系统分区。需注意，一般的云服务器默认可能使用文件作为交换空间（swapfile）？或者，也可以尝试直接将 img 镜像 `dd` 到交换分区。

对于无法压缩分区的情况，可以临时购买并挂载一块数据盘，将镜像 `dd` 到数据盘。然后通过数据盘上的安装程序进行系统安装。安装完成后卸载并删除数据盘即可。

潜在的问题在于 img 镜像可能无法正确识别分区，可能需要手动指定根文件系统。

部分发行版并不使用 GRUB，此时需要考虑是安装 GRUB，还是直接在 systemd-boot 等引导程序上处理，以及其可行性如何。

## 参考资料

- [Remote Installation of the FreeBSD Operating System Without a Remote Console](https://docs.freebsd.org/en/articles/remote-install/)
- [GRUB2 配置文件“grub.cfg”详解（GRUB2 实战手册）](https://www.jinbuguo.com/linux/grub.cfg.html)，作者：金步国。参数解释参见此处，有需要的读者请自行阅读。下同。
- [关于启动时不显示 grub 界面的问题](https://phorum.vbird.org/viewtopic.php?f=2&t=40587)
