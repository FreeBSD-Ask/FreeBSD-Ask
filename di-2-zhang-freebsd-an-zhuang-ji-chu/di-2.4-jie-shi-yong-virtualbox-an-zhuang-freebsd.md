# 2.4 使用 VirtualBox 安装 FreeBSD

Oracle VirtualBox 是 Type-2 虚拟机监视器（Hypervisor），通过虚拟设备模拟（device emulation）和半虚拟化（paravirtualization）技术为虚拟机提供计算、存储和网络资源。VirtualBox 支持多种虚拟磁盘镜像格式，默认使用 VDI（Virtual Disk Image），也兼容 VMDK（VMware）、VHD（Microsoft）等格式。该虚拟化软件可在大多数常见操作系统上运行，包括 FreeBSD 本身。

FreeBSD 在 VirtualBox 中作为虚拟机运行效果良好。以下演示基于 VirtualBox 7.2.8 和 Windows 11 25H2。

## 下载 VirtualBox

下载并安装 VirtualBox 虚拟机软件。

访问官方网站，点击页面右侧的 `Download` 按钮下载对应版本的安装程序。

[https://www.virtualbox.org](https://www.virtualbox.org)

## 安装设置

VirtualBox 安装完成后，创建并配置虚拟机。

![VirtualBox 主界面](../.gitbook/assets/virtualbox-1.png)

选择“新建”。

![新建虚拟机](../.gitbook/assets/virtualbox-2.png)

名称输入“FreeBSD”，下方的相关选项会自动补全。

![虚拟机名称设置](../.gitbook/assets/virtualbox-3.png)

设置内存大小与 CPU 数量，并开启 EFI 支持选项。

> **技巧**
>
> 请使用 UEFI，Xorg 可以自动识别驱动，**无需** 手动配置 **/usr/local/etc/X11/xorg.conf**；

![硬件设置](../.gitbook/assets/virtualbox-4.png)

调整硬盘大小。

![硬盘大小设置](../.gitbook/assets/virtualbox-4-5.png)

打开设置。

![虚拟机设置](../.gitbook/assets/virtualbox-5.png)

显卡控制器使用 `VBoxSVGA`。

> **警告**
>
> **请勿** 勾选下方的“启用 3D 加速”选项，否则将导致无法使用 `VBoxSVGA` 控制器，无法驱动显卡。

![显示设置](../.gitbook/assets/virtualbox-5-5.png)

也可以切换到 NVme 硬盘（非必须）：

![NVme 硬盘](../.gitbook/assets/virtualbox-5-6.png)

点击“启动”开始安装 FreeBSD 虚拟机。

![FreeBSD 安装界面](../.gitbook/assets/virtualbox-6.png)

![FreeBSD 安装界面](../.gitbook/assets/virtualbox-7.png)

![FreeBSD 安装界面](../.gitbook/assets/virtualbox-8.png)

FreeBSD 安装完成后，请手动关机并卸载或删除安装光盘（询问是否强制释放时同意释放），否则仍会再次进入安装界面。

![安装完成后弹出光盘](../.gitbook/assets/virtualbox-removecd.png)

安装后的 FreeBSD 虚拟机系统：

![FreeBSD 系统界面](../.gitbook/assets/virtualbox-9.png)

## 解决 EFI 下无法正常关机

编辑 **/etc/sysctl.conf** 文件，添加以下内容：

```ini
hw.efi.poweroff=0
```

然后重启系统，再执行关机即可恢复正常，即禁用 EFI 电源关闭功能，使系统通过 ACPI 正常关机。

### 参考文献

- mib. 12.0-U8.1 -> 13.0-U2 poweroff problem & solution[EB/OL]. (2022-12-23)[2026-03-26]. <https://www.truenas.com/community/threads/12-0-u8-1-13-0-u2-poweroff-problem-solution.104813/>. 提供了 EFI 环境下 FreeBSD 关机问题的解决方案。
- FreeBSD Forums. EFI: VirtualBox computer non-stop after successful shutdown of FreeBSD[EB/OL]. (2022-04-28)[2026-03-26]. <https://forums.freebsd.org/threads/efi-virtualbox-computer-non-stop-after-successful-shutdown-of-freebsd.84856/>. 详细分析了 VirtualBox 中 FreeBSD 关机异常的技术原因与修复方法。

## 网络设置

在虚拟网络方面，VirtualBox 提供 NAT、桥接（Bridged）、内部网络（Internal）、仅主机（Host-Only）等多种网络模式，每种模式对应不同的网络拓扑和连通性。

### 桥接模式

> **技巧**
>
> VirtualBox 中的桥接模式可以使各方向的网络互通。

桥接是实现宿主机与虚拟机互通的简单方法，虚拟机可以获得一个与宿主机在同一网段的 IP 地址。例如，若宿主机 IP 为 **192.168.5.123**，则虚拟机 IP 应为 **192.168.5.x**。

![桥接网络设置](../.gitbook/assets/virtualbox-bridge-network.png)

请确保上图中“名称(N)”选择的网卡（本例中是一块以太网卡“Realtek Gaming 2.5GbE Family Controller”）是当前正在使用的网卡，否则虚拟机网卡也不会拥有网络。

设置后执行 `dhclient em0` 立即获取 IP 地址，为了长期生效可在 **/etc/rc.conf** 文件中加入 `ifconfig_em0="DHCP"`。

如果无法访问互联网，请将 DNS 设置为 **223.5.5.5**。如果不熟悉相关操作，请参阅本章其他部分。

### NAT 与仅主机模式

与 VMware 不同，VirtualBox 的默认 NAT 模式下，宿主机和虚拟机无法直接互通。虚拟机可以访问宿主机的特殊地址 **10.0.2.2** 及其上运行的服务，但宿主机无法访问虚拟机的端口，各虚拟机之间网络也相互隔离。

网络设置较为复杂，桥接模式未必能够生效。如果要通过宿主机（如 Windows 11）控制虚拟机中的 FreeBSD 系统，需设置两块网卡：一块为 NAT 网络模式的网卡用于连接互联网，另一块为仅主机模式的网卡用于与宿主机互通。

首先设置网络地址转换（NAT）下的网卡，用于互联网。

![双网卡设置](../.gitbook/assets/virtualbox-dual-nic-1.png)

网卡类型下拉列表中，“网络地址转换（NAT）”与“NAT 网络”选项类似。主要区别在于：“NAT 网络”模式下的虚拟机之间可以互通，而“网络地址转换（NAT）”模式下的虚拟机网络则是相互隔离的。

然后设置第二块网卡，仅主机（Host-only）网络下的网卡，用于局域网：

![仅主机模式设置](../.gitbook/assets/virtualbox-dual-nic-2.png)

使用命令 `ifconfig` 查看状态，如果第二块网卡 `em1` 没有获取到 IP 地址，请手动通过 DHCP 临时获取：`dhclient em1`。为了长期生效，可在 **/etc/rc.conf** 文件中加入 `ifconfig_em1="DHCP"`。

![NAT 与仅主机模式](../.gitbook/assets/virtualbox-dual-nic-3.png)

```sh
# netstat -rn -f inet | egrep 'default|10\.0\.2\.0/24|192\.168\.56\.0/24'
default            10.0.2.2           UGS             em0 # 网络地址转换(NAT)网卡，默认网关，
10.0.2.0/24        link#1             U               em0
192.168.56.0/24    link#2             U               em1 # 仅主机(Host-only)网络网卡，用于与宿主机互通
```

按这种方式设定的网络，虚拟机与宿主机所在的局域网无法互通。应通过 em1 的 IP 地址进行 SSH 连接，通常为 `192.168.56.X`，而 **不是** `10.0.2.X`。

### 参考文献

- Oracle. Network Address Translation (NAT)[EB/OL]. [2026-03-26]. <https://www.virtualbox.org/manual/topics/networkingdetails.html#network_nat>. 也可以按照手册中的端口转发来连通网络。
-  Oracle Corporation. 6.3. Network Address Translation (NAT)[EB/OL]. [2026-04-04]. <https://www.virtualbox.org/manual/topics/networkingdetails.html#network_nat>. “网络地址转换（NAT）”与“NAT 网络”选项的区别。

## 虚拟机增强工具

VirtualBox 的虚拟机增强工具（Guest Additions）是一组运行在虚拟机内部的驱动程序和系统服务，提供以下支持：

- 共享剪贴板。
- 集成鼠标指针。
- 宿主时间同步。
- 窗口缩放。
- 无缝模式。

> **注意**
>
> 以下命令在 FreeBSD 虚拟机中执行。

### 安装增强工具工具

- 使用 pkg 安装：

```sh
# pkg install virtualbox-ose-additions-72
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/emulators/virtualbox-ose-additions-72/
# make install clean
```

- 安装完成后，可通过以下命令查看增强工具的配置说明：

```sh
# pkg info -D virtualbox-ose-additions-72
```

### 服务管理

安装增强工具后，需启用相关服务并设置开机自启。

启用 VirtualBox 虚拟机增强驱动：

```sh
# service vboxguest enable
```

启用 VirtualBox 服务：

```sh
# service vboxservice enable
```

将普通用户 ykla 添加到 wheel 组以获得管理权限：

```sh
# pw groupmod wheel -m ykla
```

如果使用了 ntpd(8) 时间服务，应禁用宿主时间同步，在 **/etc/rc.conf** 中添加以下内容：：

```ini
vboxservice_flags="--disable-timesync"
```

### 桌面预览

Wayland 下，缺少对应的 DRM/KMS 驱动支持，暂时无法使用。在虚拟机中安装启动 X11 下的 KDE：

![FreeBSD 系统界面](../.gitbook/assets/virtualbox-kde.png)

窗口缩放、鼠标无缝切换等功能均正常。

![FreeBSD 系统界面](../.gitbook/assets/virtualbox-kde2.png)

可以比较流畅地播放网络视频，音量偏低，可以提高最大音量。

### 共享文件夹

在宿主机和虚拟机之间传输文件的共享文件夹，可通过 `mount_vboxvfs` 挂载访问。可以使用 VirtualBox 图形界面创建共享文件夹。例如，要为虚拟机创建共享文件夹 **C:\Users\ykla\\**，并将其挂载到 **/mnt/bsdboxshare**，请执行：

![编辑共享文件夹](../.gitbook/assets/virtualbox-file.png)

注意，“文件夹名称”是操作系统（FreeBSD 虚拟机）将看到的文件名，不得包含空格。

在 FreeBSD 虚拟机中查看待挂载的文件夹：

```sh
$ dmesg | grep -i VBOXVFS
VBOXVFS[1]: sfprov_mount: path: [ykla]
```

在 FreeBSD 虚拟机中挂载共享文件夹的命令如下：

```sh
# mkdir -p /mnt/bsdboxshare # 创建上面指定的挂载点
# mount_vboxvfs -w ykla /mnt/bsdboxshare # 挂载共享文件夹 ykla，-w 为可写挂载
```

列出共享文件夹内容：

```sh
# ls /mnt/bsdboxshare/

……省略其他输出……

/mnt/bsdboxshare/SendTo/
/mnt/bsdboxshare/SiYuan/
/mnt/bsdboxshare/Templates/
```

## 故障排除与未竟事宜

### 鼠标捕获在虚拟机窗口内，无法移出

请先按右侧的 `Ctrl` 键（默认设置下键盘左右各有一个 `Ctrl`），如果因自动缩放需要还原屏幕或找不到菜单栏，请按 `Home` + 右侧 `Ctrl`。

> **技巧**
>
> 标准 108 键键盘上，`Home` 键位于 `Scroll Lock` 键的下方。

### UEFI 固件设置

开机时反复按 `Esc` 键即可进入 VirtualBox 虚拟机的 UEFI 固件设置。
