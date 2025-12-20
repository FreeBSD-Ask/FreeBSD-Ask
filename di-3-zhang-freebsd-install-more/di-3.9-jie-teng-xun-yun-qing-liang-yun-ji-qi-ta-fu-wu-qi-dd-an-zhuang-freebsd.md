# 3.9 云服务器安装 FreeBSD（基于腾讯云轻量云、阿里云轻量应用服务器）

其实就是本地硬盘安装 FreeBSD。在不依赖额外介质的前提下借助已有的操作系统（Linux）完成 FreeBSD 的安装。

## 使用 virtio 技术半虚拟化的虚拟机

> **注意**
>
> 以下内容仅供参考，有待测试。如果你测试通过，请告知我们！

根据反馈，在 VMware ESXi 等半虚拟化平台上安装或升级 FreeBSD 会遇到故障（如阿里云 virtio-blk 驱动会出问题），需要在开机时按 **ESC** 键，然后输入 `set kern.maxphys=65536` 回车，再输入 `boot` 即可正常启动。安装好后需要在 `/boot/loader.conf` 加入 `kern.maxphys=65536` 即可避免每次开机重复操作。阿里云升级完成后可能会因为此类问题卡在引导界面，此时需要重启并进 VNC 再进行上述操作。

> **注意**
>
> **对于不再受安全支持的版本如 `9.2`，请参考本文并结合手动安装 FreeBSD 章节操作。**

>**警告**
>
>**安装前请在原有的 Linux 系统上看看自己的 IP 及 netmask，可以用命令 `ip addr` 及 `ip route show` 查看网关信息、最大传输单元（MTU）数值；注意子网和 CIDR。因为有的服务器并不使用 DHCP 服务，而需要手动指定 IP。**

## 视频教程

[08-腾讯云轻量云及其他服务器安装 FreeBSD](https://www.bilibili.com/video/BV1y8411d7pp)


视频与教程有一定出入，按哪个来都可以。SCP 命令可以用图形化的 WinSCP 替代。最后安装完毕建议按照其他章节来设置密钥登录，并禁止密码验证，以提高安全性。


## 概述

[腾讯云轻量应用服务器（即腾讯云轻量云）](https://cloud.tencent.com/product/lighthouse) 以及 [阿里云轻量应用服务器](https://www.aliyun.com/product/swas) 等机器都没有 FreeBSD 系统的支持，只能通过特殊的方法自己暴力安装。


>**警告**
>
>请注意数据安全，以下教程有一定危险性和要求你有一定的动手能力。

上述的服务器面板里没有 FreeBSD 镜像 IDC，所以要用变通的方法来安装。因为 FreeBSD 和 Linux 的内核不通用，可执行文件也不通用，所以无法通过 chroot 再删掉源系统的方法安装。安装的方法是先在内存盘中启动 FreeBSD 系统，即先安装 [mfsBSD](https://mfsbsd.vx.sk)，再格式化硬盘安装新系统。mfsBSD 是一款完全载入内存的 FreeBSD 系统，类似于 Windows 的 PE 系统。

我们需要下载 [img 格式的 mfsBSD 镜像](https://mfsbsd.vx.sk/files/images/14/amd64/mfsbsd-se-14.2-RELEASE-amd64.img)，可以提前下好，再使用 WinSCP 传入服务器，服务器直接下载可能需要两个小时。


## 取消隐藏的 GRUB 菜单

现在大多数发行版的 grub 菜单都是默认隐藏的，需要在开机时按 **Esc** 才能进入，但是有时候会直接进入 BIOS。故，直接取消隐藏比较方便。

```sh
# grub2-editenv - unset menu_auto_hide
```

## 使用 mfsLinux 写入 mfsBSD

如前所述，且因 FreeBSD 和一般的 Linux 是不同的生态，我们需要先进入 Linux 的内存盘，再在运行于内存中 Linux 里把 mfsBSD 写入硬盘，然后通过 `bsdinstall` 工具安装系统。

就在 mfsBSD 下载位置的下方，有 [mfsLinux](https://mfsbsd.vx.sk/files/iso/mfslinux/mfslinux-0.1.11-94b1466.iso)，它就是我们要用的 Linux。由于它只有 ISO 格式，无法直接在当前环境下启动，因其是纯 initrd 类型的，我们就把启动它的 initrd 和内核提取出来，放在硬盘里手动启动。

在一般的 Linux 系统中，initrd 是打包成内存盘的小而全的 Linux 根目录，里面可加载驱动，可挂载硬盘，并包含启动初始化程序的必要数据。开机时 Bootloader 加载内核与 initrd，由 initrd 中的脚本进行启动的准备工作，随后运行硬盘里的初始化程序。

我们先把从那个 ISO 提取出来的内核和 initrd 文件放在根目录下，然后重启机器进入 GRUB 的命令行界面（可在倒计时的时候按 `e` 进入编辑模式，删掉 `linux`、`initrd` 行原有内容，写完后按 `Ctrl X` 即可加载），手动启动指定的内核和 initrd（可以用 `Tab` 键补全路径）。然后输入 `boot` 后回车即可继续启动操作系统。或者按 `c` 进入“编辑模式“。

```sh
linux (hd0,msdos1)/vmlinuz
initrd (hd0,msdos1)/initramfs.igz
boot # 输入 boot 后回车即可继续启动
```

>**技巧**
>
>不一定是 **(hd0,msdos1)**，以实际为准，不要一下都删掉了看不出来了。

![](../.gitbook/assets/2.png)

这个特制的 initrd 启动之后并未加载硬盘上的原系统，而是自己连接了网络并打开 SSH 服务器。这样我们就获得了一款运行在内存中的 Linux 系统。

这个时候应该就可以使用 ssh 连接上服务器了，并且可以安全的格式化硬盘。

mfsBSD 和 mfsLinux 镜像的 `root` 密码默认均是 `mfsroot`

```sh
# cd /tmp # 切换到临时路径
# wget https://mfsbsd.vx.sk/files/images/14/amd64/mfsbsd-se-14.2-RELEASE-amd64.img # 下载 mfsbsd
# dd if=mfsbsd-se-14.2-RELEASE-amd64.img of=/dev/vda # 你可以看下你是不是 /dev/vda
# reboot # 重启
```

>**技巧**
>
>建议在此处使用服务器的“快照”功能对服务器进行备份，以防以下教程操作失误重来耽误时间。

## 安装 FreeBSD

ssh 连接服务器后，使用 `kldload zfs` 加载 zfs 模块，然后运行 `bsdinstall`，在出现以下图片时，点 `Other` 输入图中的指定镜像版本（地址里有即可，你可以自己改哦）：

示例：如 <https://mirrors.ustc.edu.cn/freebsd/releases/amd64/14.2-RELEASE/> 或 <https://mirrors.nju.edu.cn/freebsd/snapshots/amd64/15.0-CURRENT/>

![腾讯云轻量云及其他服务器安装 FreeBSD](../.gitbook/assets/installBSD1.png)

![腾讯云轻量云及其他服务器安装 FreeBSD](../.gitbook/assets/installBSD2.png)

![腾讯云轻量云及其他服务器安装 FreeBSD](../.gitbook/assets/installBSD3.png)


- 我们还可以手动下载 FreeBSD 的安装文件，以 `MANIFEST` 文件为例：

```sh
# mkdir -p /usr/freebsd-dist # 创建目录
# cd /usr/freebsd-dist # 切换目录
# fetch http://ftp.freebsd.org/pub/FreeBSD/releases/amd64/14.2-RELEASE/MANIFEST # 下载所需文件
```

## 故障排除与未尽事宜

### 为何不能直接 dd？（错误示范，仅供说明，请勿执行）

  在正常的 Linux 系统内直接把 mfsBSD 的 img dd 到硬盘里，重启之后虽然正常加载 bootloader，但是可能是因为系统又对硬盘进行了写入而无法正常挂载内存盘。

```sh
# wget https://mfsbsd.vx.sk/files/images/13/amd64/mfsbsd-se-13.1-RELEASE-amd64.img -O- | dd of=/dev/vda
```

解释：

- `|` 是管道的意思，将上一个命令的标准输出作为下一个命令的标准输入
- `-O-` 指把文件下载输出到标准输出，而 dd 在没有指定 if 时会自动从标准输入读取内容

直接 dd 会报错如图：

![](../.gitbook/assets/1.png)


### LVM 逻辑卷

如果有云服务器用 lvm 的话，需要把东西全都放到 `/boot` 里面，要不然无法识别。

### 腾讯云轻量应用可能无法获取 IPv6 地址

腾讯云的 IPv6 地址下发方式很不标准，他们有自己的子网。

腾讯云 IPv6 可能是由一个专有的服务提供的，待解决与确证。

### 失败的方案

#### 方案一

UEFI 下：

```sh
set iso=(hd0,gpt2)/bsd.iso
loopback loop $iso
set root=(loop)
chainloader /boot/loader.efi
boot # 输入 boot 后回车即可继续启动
```

失败，该挂载并非将镜像挂载为内存盘，可以引导，但是 FreeBSD 在启动过程中会报错找不到启动文件。

并且在 UEFI 下，grub2 不存在 linux16、kfreebsd 等命令。

#### 方案二

传统引导下。

- 安装 syslinux

- 需要安装 syslinux 以获得 memdisk 支持。

```bash
# dnf install syslinux
```

>**警告**
>
>GRUB2 的 `memdisk.mod` 模块不是 MEMDISK。你必须安装此包才有 memdisk。

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

上面的方法可能适用于 BIOS + MBR，但是 GPT 分区表下测试失败。

#### 方案三

缩小 Linux 的 / 分区，直接将 FreeBSD img dd 到新分区中。

不可行，因为 XFS 不支持在线缩小操作（红帽系列一般都是 XFS + 逻辑卷）。

#### 方案四

直接写入 EFI 分区。

不可行，EFI 分区的大小可能受限。

#### 方案五

grub 不支持把 ISO 挂载为内存盘，但是不一定其他引导做不到。

还没找到……

#### 方案六

对于那些可以在线调整分区的文件系统，可以压缩出一个 2G 的空余分区，将其格式化为 fat32，再 dd 写入 img。

为 grub 指定 chainloader +1 到 dd 后生成的 BSD esp。一般的云服务器会默认有个作为文件系统的 swap 吗？或者可以直接把 img dd 到 swap 。

对于那些无法压缩的，可以临时花几块钱挂载一块数据盘，dd 到数据盘。通过数据盘上的安装程序进行安装。安装后删除数据盘即可。

可能存在的问题是 img 也许会无法正确识别分区，也许需要手动指定 root。

有些发行版并不使用 grub，需要考虑是安装一个 grub 还是直接在 system-boot 上处理，并且可能性如何？

## 参考资料

- [Remote Installation of the FreeBSD Operating System Without a Remote Console](https://docs.freebsd.org/en/articles/remote-install/)
- [GRUB2 配置文件“grub.cfg”详解（GRUB2 实战手册）](https://www.jinbuguo.com/linux/grub.cfg.html)，作者：金步国。参数解释参见此处，有需要的读者请自行阅读。下同。
- [关于启动时不显示 grub 界面的问题](https://phorum.vbird.org/viewtopic.php?f=2&t=40587)
