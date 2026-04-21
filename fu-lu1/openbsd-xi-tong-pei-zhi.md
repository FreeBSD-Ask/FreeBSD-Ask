# OpenBSD 系统配置

完成 OpenBSD 系统安装后，本节将介绍初次配置、硬件驱动获取、系统更新与升级等关键配置步骤，为系统的安全稳定运行提供技术支撑。

## 初次进入系统后获取驱动

系统安装完成后，首次进入 OpenBSD 时需要进行基本配置。本节介绍如何获取硬件驱动程序。

第一次进入系统后，OpenBSD 会自动检测 Wi-Fi、显卡和声卡，并下载相关驱动。请静待几分钟，待其自动更新。由于境外网站连接可能不稳定，若等待时间过长，可按 `Ctrl+C` 取消（安装系统过程中请不要执行此操作，建议断开网络），系统启动后可运行 `fw_update` 重新获取驱动。

`fw_update` 是 OpenBSD 用于获取和更新固件的工具，它会从官方固件服务器下载硬件所需的非开源固件文件。

由于各种原因，新版本在下载驱动时可能会遇到超时错误，可多次尝试下载。运行 `fw_update` 后，如有驱动下载失败，可记录其名称，然后直接访问 [OpenBSD 官方固件网站](http://firmware.openbsd.org/firmware/)手动获取，并注意匹配版本。解压驱动包，将内部驱动文件复制到 `/etc/firmware/` 目录下，然后重启系统。

例如，`inteldrm-firmware-xxx.tgz` 是 Intel 显卡驱动，解压后在驱动的 firmware 目录下会看到 i915 目录，可执行以下操作：

```sh
# mkdir -p /etc/firmware/i915                         # 创建 i915 固件存放目录
# cp -r inteldrm-firmware-xxx/firmware/i915/* /etc/firmware/i915/  # 复制 Intel i915 DRM 固件文件到系统目录
```

同理，`amdgpu-firmware-xxx.tgz` 是 AMD 显卡驱动，解压后在驱动的 firmware 目录下会看到 amdgpu 目录，可执行以下操作：

```sh
# mkdir -p /etc/firmware/amdgpu                         # 创建 amdgpu 固件存放目录
# cp -r amdgpu-firmware-xxx/firmware/amdgpu/* /etc/firmware/amdgpu/  # 复制 AMD GPU 固件文件到系统目录
```

固件目录结构：

```sh
/etc/
└── firmware/
    ├── i915/
    └── amdgpu/
```

其他驱动的操作方法与此类似。

## 配置 doas 以使用管理员权限

在 OpenBSD 中，doas 是默认用于获取管理员权限的工具。本节介绍如何配置 doas。

doas 是 OpenBSD 项目开发的 sudo 替代品，设计目标是更简单、更安全。与 sudo 相比，doas 的配置语法更加简洁。

以 root 账号登录系统。执行命令将 doas 示例配置文件复制到 `/etc` 目录：

```sh
# cp /etc/examples/doas.conf /etc/
```

从模板复制的 `/etc/doas.conf` 文件默认应包含 `permit keepenv :wheel` 这一行。wheel 是一个特殊的用户组，该组的用户可以使用管理员权限。`keepenv` 表示保留当前用户的环境变量。

如需 doas 免密码，应修改为 `permit nopass keepenv :wheel`。

若希望仅允许单个用户免密码使用 doas，可使用 `permit nopass keepenv 用户名 as root`，其中将“用户名”替换为实际用户名。

## 更新与升级

为确保系统安全和稳定，需要定期更新 OpenBSD 系统和软件包。本节介绍常用的更新和升级命令。

OpenBSD 提供了多个工具用于系统和软件的更新：

- `syspatch`：获取并应用 OpenBSD 官方发布的安全补丁
- `sysupgrade`：执行 OpenBSD 系统升级操作
- `fw_update`：下载并更新系统固件文件
- `pkg_add -u`：更新系统中已安装的软件包到最新版本

获取并应用 OpenBSD 官方发布的安全补丁：

```sh
# syspatch
```

执行 OpenBSD 系统升级操作：

```sh
# sysupgrade
```

下载并更新系统固件文件：

```sh
# fw_update
```

更新系统中已安装的软件包到最新版本：

```sh
# pkg_add -u
```

将指定用户的默认登录 shell 修改为 bash：

```sh
# chsh -s /usr/local/bin/bash 用户名
```

## 挂载可移动磁盘

本节将详细介绍在 OpenBSD 中使用可移动磁盘的相关操作步骤。

### 新建挂载点

在挂载可移动磁盘前，需要先创建挂载点目录。

创建多个 U 盘挂载目录，如目录不存在则一并创建：

```sh
# mkdir -p /media/usb1 /media/usb2 /media/usb3 /media/usb4  # 可根据需要创建更多目录
```

挂载点目录结构：

```sh
/media/
├── usb1/
├── usb2/
├── usb3/
├── usb4/
└── mtp/
```

### 查看盘符

挂载点创建完成后，需要查看新插入的磁盘设备名称，以便确定正确的挂载路径。

使用 `dmesg | tail` 命令来查看新插入的盘符。例如，格式为 FAT32 的 U 盘在 OpenBSD 系统里盘符可能为 `sd1`。

### 检查分区

确定磁盘盘符后，需要进一步查看其分区信息，以找到正确的分区进行挂载。

如果插入的盘符为 `sd1`，则输入 `disklabel sd1` 查看 `sd1` 磁盘的分区信息，结果如下：

```sh
# disklabel sd1
                size           offset  fstype [fsize bsize   cpg]
 c:         60062500                0  unused
 i:         60062244              256   MSDOS
```

### 挂载

了解分区信息后，就可以执行具体的挂载操作了。

由上可知分区为 `i`，使用以下命令将 `sd1i` 分区挂载到目录 `/media/usb1`：

```sh
# mount /dev/sd1i /media/usb1
```

### 其他文件系统

OpenBSD 还支持挂载其他多种文件系统格式。

OpenBSD 可以挂载的外接存储格式包括 NTFS（内核自带只读挂载，需读写挂载则安装软件包 `ntfs_3g`）、ext2/ext3 以及 CD-ROM，具体命令如下：

```sh
# mount /dev/sd3i /media/usb1       # 将 FAT32 分区 sd3i 挂载到 /media/usb1
# mount_ntfs /dev/sd2k /media/usb2  # 将 NTFS 分区 sd2k 以只读方式挂载到 /media/usb2
# ntfs-3g /dev/sd2k /media/usb2     # 将 NTFS 分区 sd2k 以读写方式挂载（需安装 ntfs_3g）
# mount /dev/sd1l /media/usb3       # 将 ext2/ext3 分区 sd1l 挂载到 /media/usb3
# mount /dev/cd0a /media/usb4       # 将 CD-ROM 设备 cd0a 挂载到 /media/usb4
```

### 卸载磁盘

使用完可移动磁盘后，需要正确卸载以避免数据丢失。

卸载挂载在 /media/usb1 的文件系统：

```sh
# umount /media/usb1
```

注意：卸载前请确保没有进程正在使用挂载点，以免数据损坏。

### 挂载 Android 设备

除了传统的 U 盘和移动硬盘外，OpenBSD 也可以挂载 Android 设备的存储。

新近的 Android 系统的存储设备通常采用 MTP 协议映射，需要相应的 MTP 软件来管理手机文件。MTP（Media Transfer Protocol，媒体传输协议）是一种用于在设备之间传输媒体文件的协议。与 Linux 不同，OpenBSD 上可用的软件较少，此处使用 `simple-mtpfs` 完成挂载操作。

安装 `simple-mtpfs` 软件包，用于挂载 MTP 设备：

```sh
# pkg_add simple-mtpfs
```

挂载 Android 设备的流程：

```sh
# pkg_add simple-mtpfs                        # 安装 simple-mtpfs，用于挂载 MTP 设备
# mkdir -p /media/mtp                          # 创建 MTP 设备挂载目录
# chmod 755 /media/mtp                          # 设置挂载目录权限，允许用户访问
# simple-mtpfs -o allow_other /media/mtp       # 将 MTP 设备挂载到 /media/mtp，允许其他用户访问
# umount /media/mtp                             # 卸载挂载的 MTP 设备
```

除了 Android 手机，Android 电纸书等设备也可以使用上述方法挂载。

## Wi-Fi

本节介绍在 OpenBSD 中配置 Wi-Fi 的方法。

在 OpenBSD 中，Wi-Fi 网络的配置文件通常为 `hostname.if`，其中 `if` 为 Wi-Fi 驱动名称加序号。例如，一台笔记本 Wi-Fi 型号为 rtl8188cu，OpenBSD 下的驱动为 rtwn，序号从 0 开始。为了让系统自动连接 Wi-Fi，可编辑 `/etc/hostname.rtwn0` 文件，并添加以下内容：

```ini
dhcp                                # 通过 DHCP 自动获取网络配置
join WiFi名称 wpakey WiFi密码        # 连接指定的 WiFi，无线网络名称为 WiFi名称，密钥为 WiFi密码
```

保存文件后即可生效。

## 加载触摸板

对于使用笔记本电脑的用户，通常需要启用触摸板的轻点点击功能以提升使用体验。

wsconsctl 是 OpenBSD 用于控制控制台和输入设备的工具。编辑 `/etc/wsconsctl.conf` 文件，添加一行：

```ini
mouse.tp.tapping=1
```

可启用触摸板轻点击（Tap-to-Click）功能。

## 启用超线程

OpenBSD 默认禁用超线程以提高安全性，但用户可以根据需要手动启用。

超线程（Simultaneous Multithreading，SMT）是一种通过在单个物理核心上执行多个线程来提高性能的技术。OpenBSD 项目认为超线程机制可能带来潜在的安全风险，因此默认将其禁用。

编辑 `/etc/sysctl.conf` 文件，添加一行 `hw.smt=1` 以启用 CPU 超线程。

```sh
# sysctl hw.smt=1  # 立刻生效但非永久化设置
hw.smt: 0 -> 1
```

查看当前在线的 CPU 核心数量：

```sh
# sysctl hw.ncpuonline
hw.ncpuonline=4
```

## 关机

本节介绍 OpenBSD 中的关机命令。

OpenBSD 系统推荐使用 `halt -p` 命令来关闭系统并切断电源，`poweroff` 命令同样可用（等同于 `halt -p`）。

要关闭系统并切断电源，请执行命令：

```sh
# halt -p
```

或者使用命令立即关闭系统并停止所有服务：

```sh
# shutdown -h now
```

## HTTP 代理

在网络环境受限的情况下，可能需要配置 HTTP 代理以访问外部资源。

系统配置文件结构：

```sh
/etc/
├── examples/
│   └── doas.conf
├── doas.conf
├── installurl
├── hostname.rtwn0
├── wsconsctl.conf
└── sysctl.conf
```

设置 HTTP 代理地址和端口：

```sh
$ export http_proxy=http://192.168.X.X:7890
$ export https_proxy=http://192.168.X.X:7890
$ export no_proxy=localhost,127.0.0.1
```

> **注意**
>
> 此处的环境变量 `http_proxy` 必须为小写，使用大写名称将不会生效。同样，`https_proxy` 和 `no_proxy` 也应使用小写。

## 相关资料

- OpenBSD Project. OpenBSD FAQ[EB/OL]. (2024-03-25)[2026-03-25]. <https://www.openbsd.org/faq/>. 官方系统配置与使用指南，提供完整参考。
- Lucas M W. Absolute OpenBSD, 2nd Edition: Unix for the Practical Paranoid[M]. San Francisco: No Starch Press, 2013. OpenBSD 技术参考书，讲解 OpenBSD 系统基础。
- K58. Installing OpenBSD 7.3 on your laptop is really hard (not)[EB/OL]. (2024-03-25)[2026-03-25]. <https://www.k58.uk/openbsd.html>. 笔记本电脑安装 OpenBSD 的实践指南。
