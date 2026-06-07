# 4.6 KVM、QEMU 等平台安装 FreeBSD（传统引导和 MBR 分区表）

在 KVM/QEMU 等硬件辅助虚拟化平台上，通过传统 BIOS + MBR 方式安装 FreeBSD 适用于不直接提供 FreeBSD 镜像的云服务环境。此方法不支持 UEFI 引导，也不适用于 OpenVZ、LXC 等容器化平台。

> **注意**
>
> 因为容器化技术本质上不属于完整的虚拟化解决方案，宿主机与客户机共享内核，此方法不支持 OpenVZ、LXC 等容器化技术。内核已经是 Linux，无法运行 FreeBSD 系统。
>
> 此方法不支持 UEFI 引导模式（BIOS + GPT 分区表同样不支持），仅支持传统 BIOS + MBR 引导方式，请确保环境符合要求。

> **警告**
>
> 请注意数据安全，以下教程具有一定风险，且要求操作者具备相应的操作能力与系统管理知识。

## 概述

本节介绍在 KVM、QEMU 等平台上安装 FreeBSD 的方法。多数采用 KVM、QEMU 虚拟化架构的服务商未直接提供 FreeBSD 系统支持，需通过特殊方法手动安装。

部分服务商虽在某些机型上提供 FreeBSD 系统镜像，但支持尚不完善，例如默认镜像未启用 `BBR`，某些机型则完全不提供 FreeBSD 支持。

本方法无需使用 mfsLinux 作为安装介质，亦无需通过 `dd` 命令安装。

mfsBSD 是一款完全载入内存的 FreeBSD 系统，类似于 Windows PE（Preinstallation Environment）。

本节通过 GRUB2 借助 MEMDISK 模块将 mfsBSD 载入内存，并从中启动，随后通过 mfsBSD 中的 `bsdinstall` 命令安装 FreeBSD。

## 获取现有网络配置

部分服务器可能未启用 DHCP 服务，需手动指定 IP，多见于小型服务商。

安装前，请在原 Linux 系统中确认 IP 地址和子网掩码，可使用命令 `ip addr` 和 `ip route show` 查看网关信息。

## 准备 mfsBSD

下载 mfsBSD。可下载至本地计算机后通过 SCP、SFTP 或 WinSCP 等工具上传至服务器；亦可直接使用命令行在服务器上下载。

> **注意**
>
> 因 mfsBSD 的下载站点不支持 IPv6 网络，仅支持 IPv6 的服务器无法通过命令行下载。

针对此问题，已通过邮件与作者沟通，截至发稿时尚未收到回复。

### 内存 ≤ 512 MB

下载 mfsBSD Mini 14.1-RELEASE ISO 镜像：

```sh
# wget https://mfsbsd.vx.sk/files/iso/14/amd64/mfsbsd-mini-14.1-RELEASE-amd64.iso
```

校验和（官网链接指向错误，已反馈但未获回复）：[checksums](https://mfsbsd.vx.sk/files/iso/14/amd64/mfsbsd-mini-14.1-RELEASE-amd64.iso.sums.txt)

> **注意**
>
> 内存小于或等于 4 GB 的机器不建议使用 ZFS 文件系统。
>
> mfsBSD Mini 使用 Dropbear SSH 替代 OpenSSH，但仍包含 `zfs` 内核模块，支持 ZFS 文件系统。

### 内存 > 512 MB

下载 mfsBSD 14.2-RELEASE AMD64 ISO 镜像：

```sh
# wget https://mfsbsd.vx.sk/files/iso/14/amd64/mfsbsd-14.2-RELEASE-amd64.iso
```

校验和：[checksums](https://mfsbsd.vx.sk/files/iso/14/amd64/mfsbsd-14.2-RELEASE-amd64.iso.sums.txt)

### 准备 mfsBSD.iso

将下载的 mfsBSD 重命名为 `mfsbsd.iso` 并放置于 **/boot** 目录中（若放置于其他目录，可能因 LVM 导致无法识别硬盘分区）。

## 获取 memdisk

memdisk 是 syslinux 提供的工具，用于将 ISO 镜像加载到内存中。

> **警告**
>
> GRUB2 自带的 `memdisk.mod` 模块并非此处所需的 MEMDISK。
>
> memdisk 须通过包管理器安装的 syslinux 提供。

### 安装 syslinux

不同 Linux 发行版安装 syslinux 的命令有所差异。

- Debian/Ubuntu

```bash
# apt install syslinux
```

- Rocky Linux

```bash
# dnf install syslinux
```

### 提取 memdisk

从已安装的 syslinux 包中提取 memdisk 文件到 **/boot**：

- Debian/Ubuntu

```sh
# cp /usr/lib/syslinux/memdisk /boot/
```

- Rocky Linux

```sh
# cp /usr/share/syslinux/memdisk /boot/
```

## 取消隐藏的 GRUB 菜单

取消 GRUB2 菜单的自动隐藏设置：

```bash
# grub2-editenv - unset menu_auto_hide
```

## 启动 mfsBSD

重启并进入 GRUB 菜单后，按 `c` 键进入命令行模式：

![在此界面按 C](../.gitbook/assets/grub-boot-menu-1.png)

![Grub 命令行界面](../.gitbook/assets/grub-boot-menu-2.png)

```sh
ls # 显示磁盘。如果显示的磁盘为 (hd0,gptxxx)，说明该平台不支持本节方法。
ls (hd0,msdos2)/
linux16 (hd0,msdos2)/memdisk iso
initrd16 (hd0,msdos2)/mfsbsd.iso
boot # 输入 boot 后按回车从 mfsBSD 继续启动
```

> **技巧**
>
> 如果遇到问题，可尝试切换到串口控制台（`console=comconsole`），或检查镜像完整性。

在 Proxmox 中，可直接点击界面上的 `xterm.js` 按钮进入串口控制台排查问题。

![选择 xterm.js 按钮](../.gitbook/assets/proxmox-choose-xtermjs.png)

![进入 xterm.js 排查](../.gitbook/assets/xtermjs-page.png)

## 为 mfsBSD 配置网络

mfsBSD 的 `root` 默认密码为 `mfsroot`。可以使用 SSH 工具连接后安装。

> **技巧**
>
> 如果平台支持 DHCP 自动获取网络配置，可跳过本节。

重启进入 mfsBSD 后，配置网络。

以接口 `vtnet0` 为例，配置 IPv4：

> **警告**
>
> 请将下面的示例替换为实际 IP 地址和路由信息。

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

使用 `kldload zfs` 加载 ZFS 模块，随后运行 `bsdinstall`。

该步骤可参照其他章节的方法安装。

## 故障排除与未竟事宜

### GPT 分区表下如何安装？

可参考以下资料：

- Konstantin Kelemen. Booting mfsBSD via PXE with UEFI[EB/OL]. (2019-10-24)[2026-03-29]. <https://unix.stackexchange.com/questions/563053/booting-mfsbsd-via-pxe-with-uefi>.
- FreeBSD Forums. Booting mfsBSD via iPXE on EFI[EB/OL]. (2018-10-05)[2026-03-29]. <https://forums.freebsd.org/threads/booting-mfsbsd-via-ipxe-on-efi.66169/>.

此问题有待进一步研究。

### VMware、VirtualBox 无法按照此方法安装

VirtualBox 用户可尝试将虚拟化引擎选择为“KVM”后再次引导，但可能因环境而异（测试环境未能成功引导）。

![VirtualBox 选择虚拟化](../.gitbook/assets/virtualbox-choose-vm.png)

### 待尝试的方案

以下方案尚未经过验证，供读者参考尝试。

- `dd` 写入 [VM-IMAGES 列表下的镜像](https://download.freebsd.org/releases/VM-IMAGES/14.3-RELEASE/amd64/Latest/)
- `dd` 写入 [FreeBSD-14.3-RELEASE-amd64-memstick](https://download.freebsd.org/releases/ISO-IMAGES/14.3/FreeBSD-14.3-RELEASE-amd64-memstick.img)
- 在 QEMU 平台上，尝试直接使用 `dd`

![能进入 BootLoader，但启动失败](../.gitbook/assets/qemu-dd-mfsbsd-result.png)

思路：在该界面可使用 `?` 命令查看磁盘信息，有望继续完成引导。

- 通过 mfsLinux `dd` mfsBSD

![无法进入 BootLoader](../.gitbook/assets/mfslinux-dd-mfsbsd-result.png)

此问题尚待验证。

## 参考文献

- mfsBSD. mfsBSD — minimalistic FreeBSD distribution[EB/OL]. [2026-04-17]. <https://mfsbsd.vx.sk/>. mfsBSD 项目主页，提供完全载入内存的 FreeBSD 系统镜像。
- syslinux Wiki. MEMDISK[EB/OL]. [2026-04-17]. <https://wiki.syslinux.org/wiki/index.php?title=MEMDISK>. MEMDISK 模块说明，用于将 ISO 镜像加载到内存中作为虚拟磁盘使用。
