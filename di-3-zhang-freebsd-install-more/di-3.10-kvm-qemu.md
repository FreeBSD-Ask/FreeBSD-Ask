# 3.10 云服务器安装 FreeBSD（基于 KVM、QEMU 等平台）

> **警告**
> 
> 请注意数据安全，以下教程有一定危险性和要求你有一定的动手能力。
> 
> **安装前请在原有的 Linux 系统上看看自己的 IP 及 netmask，可以用命令 `ip addr` 及 `ip route show` 查看网关信息。因为有的服务器并不使用 DHCP 服务，而需要手动指定 IP。特别是小厂服务器。**

> **注意**
> 
> 不支持 OpenVZ、LXC 虚拟机，因为他们本质上不属于虚拟机，宿主机与客户机共享内核。内核都是 Linux 了，哪里还有 FreeBSD ？
> 
> 不支持 UEFI 引导模式，仅支持传统 MBR + BIOS (Legacy/CSM) 方式引导。MBR + GPT 分区表形式亦不支持。

## 概述

在各种以 KVM、QEMU 为虚拟架构的服务器厂商中，大部分都没有 FreeBSD 系统的支持，只能通过特殊的方法自己暴力安装。

最常见的用 KVM 虚拟化的厂商就是搬瓦工、Linode。它们虽说在部分机型上有提供 FreeBSD 系统镜像支持，但是这部分机型即使有镜像，支持都不完善，比如自带镜像默认都不支持 `BBR`，部分机型更是没有 FreeBSD 系统支持。

## 原理

通过 Grub 的 Memdisk 模式，直接从 mfsBSD 启动。

即直接将 mfsBSD 写入内存，然后再安装 FreeBSD。

内存不充裕可以使用 mfsBSD 的 mini 模式，请看下文。

本操作不同于 3.9 节操作，不需要 mfsLinux 作为介质通过 DD 方式安装。类似的，3.9 节的方法行不通也可以参考本文。

## 准备mfsBSD

mfsBSD 是一款完全载入内存的 FreeBSD 系统，类似于 Windows 的 PE 系统。

我们需要先下载下来，然后用 SCP、SFTP 等你熟悉的东西传入服务器。当然你也可以直接在服务器 wget/axel 下载。

> **注意**
>
> IPv6-Only 服务器不能直接 wget，因为下载地址不支持 IPv6 网络，注意踩坑。
>
> *此问题已给作者邮件沟通，但暂未得到回应。*

- 运行内存 <= 512 MB

    mfsBSD Mini 可能无法正常使用 `zfs` 作为文件系统。这种情况下你需要使用 `ufs` 。

    内存 <= 4G 建议不要使用 `zfs` 作为文件系统。

    下载：[mfsBSD Mini](https://mfsbsd.vx.sk/files/iso/14/amd64/mfsbsd-mini-14.1-RELEASE-amd64.iso)

    校验(官网的链接指向错误)：[checksums](https://mfsbsd.vx.sk/files/iso/14/amd64/mfsbsd-mini-14.1-RELEASE-amd64.iso.sums.txt)

- 运行内存 > 512 MB

    下载：[mfsBSD 完整版](https://mfsbsd.vx.sk/files/iso/14/amd64/mfsbsd-14.2-RELEASE-amd64.iso)

    校验：[checksums](https://mfsbsd.vx.sk/files/iso/14/amd64/mfsbsd-14.2-RELEASE-amd64.iso.sums.txt)

## 修改 Grub

> **警告**
> 
> GRUB2 的 `memdisk.mod` 模块不是 MEMDISK。
> 
> memdisk 需要由包管理器安装的 syslinux 提供。

我将会以 Debian 作为例子，在 Debian 中使用 memdisk 引导 mfsBSD.img ：

1. 安装 syslinux：
   ```sh
   # apt-get install syslinux
   ```
2. 准备 mfsBSD.img：将 mfsBSD.img 放在可访问路径，如 `/boot/mfsbsd.img`。
3. 复制 memdisk：从 syslinux 包中复制 memdisk 文件到 `/boot`：
   ```sh
   # cp /usr/lib/syslinux/memdisk /boot/
   ```
4. 取消隐藏的 GRUB 菜单
    现在大多数发行版的 grub 菜单都是默认隐藏的，需要在开机时按 **Esc** 才能进入，但是有时候会直接进入 BIOS。故，直接取消隐藏比较方便。
    ```sh
    # grub2-editenv - unset menu_auto_hide
    ```
5. 重启到 grub，进入命令行操作：
    ```sh
    ls # 显示磁盘
    ls (hd0,gpt2)/ # 显示磁盘 (hd0,gpt2) 下的内容，MBR 分区表可能为 (hd0,msdosx)。不一定是 (hd0,gpt2)，以实际为准
    linux16 (hd0,gpt2)/memdisk iso
    initrd (hd0,gpt2)/bsd.iso
    boot # 输入 boot 后回车即可继续启动
    ```

> **注意**：
> - 如果遇到问题，可尝试切换到串口控制台（`console=comconsole`）或检查镜像完整性。

在 Proxmox 中，可以直接按下菜单里的`xterm.js`按钮进入串口控制台进行问题排查

![选择xterm.js按钮](../.gitbook/assets/proxmox-choose-xtermjs.png)

![进入xterm.js排查](../.gitbook/assets/xtermjs-page.png)

## 重启进入mfsBSD，并配置网络

mfsBSD 的 `root` 密码默认是 `mfsroot`。

重启进入到 mfsBSD 后，按照以下方法配置网络，当然你也可以直接在支持 DHCP 的网络下直接运行 `bsdinstall` 配置。

以接口 `vtnet0` 举例，逐行配置 IPv4，下面的请换成你的 IP 地址和路由情况：

```sh
# ifconfig vtnet0 inet 192.0.2.123/24
# route add -inet default 192.0.2.1
```

检查：

```sh
# ifconfig vtnet0
# route -n show -inet6
```

## 开始安装

使用 `kldload zfs` 加载 zfs 模块，然后运行 `bsdinstall`。

这部分你可以参照 3.9 节的方法安装，重复的环节在这里省略。

## 故障排除与未尽事宜

- GPT 分区表下如何安装？

    也许可以参考：<https://unix.stackexchange.com/questions/563053/booting-mfsbsd-via-pxe-with-uefi>与<https://forums.freebsd.org/threads/booting-mfsbsd-via-ipxe-on-efi.66169/>采用 PXE 方式引导。

    [FreeBSD 下搭建 PXE 服务器](https://book.bsdcn.org/freebsd-shou-ce/di-34-zhang-gao-ji-wang-luo/34.10.-shi-yong-pxe-jin-hang-wu-pan-cao-zuo)

    待解决、待尝试。

- VMWare、VirtualBox 无法按照此方法安装

    鉴于 VirtualBox 可以选择虚拟化，选择为 `kvm` 可再次尝试。（笔者的机器无法引导，也许你能成功）

    ![VirtualBox 选择虚拟化](../.gitbook/assets/xtermjs-page.png)

    VMWare 上，可以参照 3.9 节的方式再次尝试。

- 待尝试的方案

    1. DD 写入 [VM-IMAGES 列表下的镜像](https://download.freebsd.org/releases/VM-IMAGES/14.3-RELEASE/amd64/Latest/)

    2. DD 写入 [FreeBSD-14.3-RELEASE-amd64-memstick](https://download.freebsd.org/releases/ISO-IMAGES/14.3/FreeBSD-14.3-RELEASE-amd64-memstick.img)

- QEMU平台上，尝试直接DD

    ![能进入 BootLoader，但启动失败](../.gitbook/assets/qemu-dd-mfsbsd.png)

    思路: 这个页面可以继续使用 `?` 查看磁盘信息，也许可以接着引导。

- 通过mfsLinux DD mfsBSD

    ![无法进入 BootLoader](../.gitbook/assets/mfslinux-dd-mfsbsd.png)

    待解决。
