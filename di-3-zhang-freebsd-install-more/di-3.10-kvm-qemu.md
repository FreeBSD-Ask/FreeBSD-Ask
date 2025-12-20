# 3.10 云服务器安装 FreeBSD（基于 KVM、QEMU 等平台）

> **注意**
>
> 不支持 OpenVZ、LXC 虚拟机，因为它们本质上不属于虚拟机，宿主机与客户机共享内核。内核已经是 Linux，自然无法运行 FreeBSD。
> 
> 不支持 UEFI 引导模式（BIOS + GPT 分区表同样不支持），仅支持传统 BIOS + MBR 引导方式。

> **警告**
>
> 请注意数据安全，以下教程具有一定风险，并且要求具备一定的动手能力。

## 概述

在各种采用 KVM、QEMU 虚拟化架构的服务商中，大部分不直接提供 FreeBSD 系统支持，只能通过特殊方法手动安装。

它们虽然在部分机型上提供 FreeBSD 系统镜像，但支持并不完善，例如自带镜像默认未启用 `BBR`，而部分机型则完全不提供 FreeBSD 支持。

本方法无需使用 mfsLinux 作为介质并通过 `dd` 命令进行安装。

mfsBSD 是一款完全载入内存的 FreeBSD 系统，类似于 Windows 的 PE 系统。

本文通过 GRUB2 借助 MEMDISK 模块将 mfsBSD 载入为内存盘，并从中启动。然后再通过 mfsBSD 中的 `bsdinstall` 命令安装 FreeBSD。

## 获取现有网络配置

有的服务器可能不使用 DHCP 服务，而需要手动指定 IP，这种情况多见于小厂服务器。

安装前，请在原 Linux 系统中确认 IP 地址及子网掩码。

可以用命令 `ip addr` 及 `ip route show` 查看网关信息。

## 准备 mfsBSD

我们需要下载 mfsBSD。你可以下载到本地计算机，再通过 SCP、SFTP 或 WinSCP 等工具上传至服务器；也可以直接在服务器上使用命令行下载。

> **注意**
>
> 仅支持 IPv6 的服务器无法通过命令行下载，因为 mfsBSD 的下载地址不支持 IPv6 网络。
>
> 针对该问题，笔者已通过邮件与作者沟通，但截至发文时尚未收到回应。

### 内存 <= 512 MB

下载 mfsBSD Mini：

```sh
# wget https://mfsbsd.vx.sk/files/iso/14/amd64/mfsbsd-mini-14.1-RELEASE-amd64.iso
```

校验码（官网链接指向错误，已反馈但未收到回复）：[checksums](https://mfsbsd.vx.sk/files/iso/14/amd64/mfsbsd-mini-14.1-RELEASE-amd64.iso.sums.txt)

>**技巧**
>
>内存小于或等于 4 GB 的机器不建议使用 ZFS 文件系统。
>
>同时，mfsBSD Mini 可能无法正常加载 `zfs` 内核模块。
>
>这种情况下你只能使用 `ufs` 文件系统。

### 内存 > 512 MB

下载 mfsBSD 完整版：

```sh
# wget https://mfsbsd.vx.sk/files/iso/14/amd64/mfsbsd-14.2-RELEASE-amd64.iso
```

检验码：[checksums](https://mfsbsd.vx.sk/files/iso/14/amd64/mfsbsd-14.2-RELEASE-amd64.iso.sums.txt)

### 准备 mfsBSD.iso

将下载的 mfsBSD 重命名为 `mfsbsd.iso`，并放置在 `/boot` 目录下（否则可能因 LVM 导致硬盘分区无法识别）。

## 获取 memdisk

> **警告**
>
> 请注意，GRUB2 自带的 `memdisk.mod` 模块并非此处所需的 MEMDISK。
>
> memdisk 需要由通过包管理器安装的 syslinux 软件提供。

### 安装 syslinux

- Debian/Ubuntu

```bash
# apt install syslinux
```

- Rocky Linux

```bash
# dnf install syslinux
```

### 提取 memdisk

从已安装的 syslinux 包中提取 memdisk 文件到 `/boot`

```sh
# cp /usr/lib/syslinux/memdisk /boot/
```

## 取消隐藏的 GRUB 菜单

目前大多数发行版的 GRUB 菜单默认处于隐藏状态，需要在开机时按 **Esc** 才能进入，但有时会直接进入 BIOS，因此直接取消隐藏会更为方便。

```sh
# grub2-editenv - unset menu_auto_hide
```

## 启动 mfsBSD

重启并进入 GRUB 菜单后，按 `c` 键进入命令行模式：

![在此界面按 C](../.gitbook/assets/grub21.png)

![Grub 命令行界面](../.gitbook/assets/grub22.png)

```sh
ls # 显示磁盘。如果显示的磁盘为 (hd0,gptxxx)，说明该平台不支持本教程。
ls (hd0,msdos2)/
linux16 (hd0,msdos2)/memdisk iso
initrd (hd0,msdos2)/mfsbsd.iso
boot # 输入 boot 后回车即可从 mfsBSD 继续启动
```

> **注意**：
>
> 如果遇到问题，可尝试切换到串口控制台（`console=comconsole`），或检查镜像完整性。

在 Proxmox 中，可直接点击界面上的 `xterm.js` 按钮进入串口控制台排查问题。

![选择 xterm.js 按钮](../.gitbook/assets/proxmox-choose-xtermjs.png)

![进入 xterm.js 排查](../.gitbook/assets/xtermjs-page.png)

## 为 mfsBSD 配置网络

mfsBSD 的 `root` 默认密码为 `mfsroot`。你可以使用 SSH 工具连接后进行安装。

>**技巧**
>
>如果平台支持 DHCP 自动获取网络配置，可跳过本节。

重启进入到 mfsBSD 后，配置网络。

以接口 `vtnet0` 举例，配置 IPv4：

>**警告**
>
>请将下面的示例替换为你的实际 IP 地址和路由信息。

```sh
# ifconfig vtnet0 inet 192.0.2.123/24 # 为网卡 vtnet0 设置 IPv4
# route add -inet default 192.0.2.1 # 设置默认网关/路由
```

检查网络配置：

```sh
# ifconfig vtnet0 # 显示网卡接口 vtnet0 的网络信息
# route -n show -inet6 # 显示 IPv6 的路由表
```

## 开始安装

使用 `kldload zfs` 加载 zfs 模块，然后运行 `bsdinstall`。

这部分你可以参照其他章节的方法安装。

## 故障排除与未尽事宜

### GPT 分区表下如何安装？

也许可以参考：

- [Booting mfsBSD via PXE with UEFI](https://unix.stackexchange.com/questions/563053/booting-mfsbsd-via-pxe-with-uefi) 与 [Booting mfsBSD via iPXE on EFI](https://forums.freebsd.org/threads/booting-mfsbsd-via-ipxe-on-efi.66169/) 采用 PXE 方式引导。
- [FreeBSD 下搭建 PXE 服务器](https://book.bsdcn.org/freebsd-shou-ce/di-34-zhang-gao-ji-wang-luo/34.10.-shi-yong-pxe-jin-hang-wu-pan-cao-zuo)

待解决、待尝试。

### VMware、VirtualBox 无法按照此方法安装

对于 VirtualBox，可尝试将虚拟化引擎选择为“KVM”后再次引导（笔者的机器未能成功引导，结果可能因环境而异）。

![VirtualBox 选择虚拟化](../.gitbook/assets/virtualbox-choose-vm.png)

### 待尝试的方案

- `dd` 写入 [VM-IMAGES 列表下的镜像](https://download.freebsd.org/releases/VM-IMAGES/14.3-RELEASE/amd64/Latest/)
- `dd` 写入 [FreeBSD-14.3-RELEASE-amd64-memstick](https://download.freebsd.org/releases/ISO-IMAGES/14.3/FreeBSD-14.3-RELEASE-amd64-memstick.img)
- 在 QEMU 平台上，尝试直接 `dd`

![能进入 BootLoader，但启动失败](../.gitbook/assets/qemu-dd-mfsbsd.png)

思路：在该界面可使用 `?` 命令查看磁盘信息，或许可以继续完成引导。

- 通过 mfsLinux `dd` mfsBSD

![无法进入 BootLoader](../.gitbook/assets/mfslinux-dd-mfsbsd.png)

（此问题）尚待解决与验证。
