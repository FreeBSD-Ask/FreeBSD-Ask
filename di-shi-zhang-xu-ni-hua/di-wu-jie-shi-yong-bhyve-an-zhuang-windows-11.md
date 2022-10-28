# 第五节 使用 bhyve 安装 Windows 11

**以下部分内容翻译自 <https://github.com/churchers/vm-bhyve/wiki>，未经测试，谨慎参考，成功者可向我报告。**

## 基本思路

首先，完全可行，已经有人实现（见参考资料）。其次，Windows 11 与 Windows 10 的不同之处在于前者对硬件的设备的要求更高，要求强制的 TPM 模块（受信任的平台）。并且强制要求使用 UEFI GPT。所以需要对镜像做一些额外的修改才可以加载使用（参考资料似乎不需要这些）。最后，其他的应该和 Windows 10 是相同的。

## 安装固件与软件

如果你打算运行 Windows，强烈建议你运行 FreeBSD 11 + 并启用 UEFI 图形支持。

首先，你需要确保你有 UEFI 固件与  vm-bhyve，如果还没有安装的话。

```
# pkg install bhyve-firmware vm-bhyve
```

## 客户机配置

使用 Windows 模板创建一个客户机。这个客户机默认为 2 个 CPU 和 2GB 的内存。它还使用了一个"e1000"英特尔网络适配器，它被 Windows 开箱即用所支持。如果你想改变配置选项，可以使用 `vm configure guest` 命令。

> 注意，如果你运行的是比 Windows 10 更早的 Windows 版本，你将需要使用 `disk0_opts="sectorsize=512"` 选项将磁盘扇区大小设置为 512。
当你想在 Windows 系统上安装 Microsoft SQL Server 时，你也必须将磁盘扇区大小设置为 512。

```
# vm create -t windows winguest
```

## 安装系统

通过指定 Windows iso 文件开始正常的安装。当在安装模式下运行时，`vm-bhyve` 将等待，直到 VNC 客户端连接后再启动客户机。这允许你抓住 Windows 可能显示的“从 CD/DVD 启动“选项。你可以在 `vm list` 中看到，在这一点上，客户机将显示为锁定：

```
# vm install winguest Windows-Installer.iso
```

一旦与 VNC 客户端连接，就可以像平常一样完成 Windows 的安装。

## 添加 VirtIO 网络驱动

虽然“e1000”网络适配器开箱即用，允许访客获得网络访问，但建议尽可能使用“virtio-net”设备。有几种安装这些驱动程序的方法。

* 如果机器可以通过 e1000 设备访问互联网，你可以直接在客户机中下载并安装 virtio 驱动。安装完毕后，关闭客户机，在客户机配置中改变设备并重新启动。
* 可以在安装模式下启动客户机，但要指定 VirtIO ISO 文件。

```
# vm install winguest virtio-installer.iso
```
    
* 可以添加 CD 设备到客户机上，并指向 ISO 文件

```
disk1_type="ahci-cd"
disk1_dev="custom"
disk1_name="/full/path/to/virtio-installer.iso"
```

## 关于 CPU

某些版本的 Windows（大多数桌面版本）不支持一个以上的物理 CPU。默认情况下，bhyve 配置单个虚拟 CPU 和单核心。

可以修改 sysctl `hw.vmm.topology.cores_per_package` 以告诉 bhyve 为每个 CPU 创建多核心，而不是单核心。例如，将这个 sysctl 设置为 4 将配置一个有 8 个 vCPU 的客户机，有 2  x 4 个核心。

必须在 /boot/loader.conf 中设置（并重新启动才能生效）`hw.vmm.topology.cores_per_package`。

当在 FreeBSD 12 上，使用 vm-bhyve 1.3 时，可以使用配置选项来控制每个客户的 CPU 拓扑结构：

```
cpu=8
cpu_sockets=2
cpu_cores=4
cpu_threads=1
```

## 关于 NVMe 支持

如同 FreeBSD 12.1R，bhyve 支持 NVMe 仿真。对于 vm-bhyve 配置，请遵循以下选项：

```
disk0_type="nvme"
disk0_name="disk0.img"
disk0_opts="maxq=16,qsz=8,ioslots=1,sectsz=512,ser=ABCDEFGH"
```

你甚至可以在没有虚拟磁盘的情况下将客户机安装到物理 NVMe 磁盘上。以下是一个例子：

```
loader="uefi"
graphics="yes"
xhci_mouse="yes"
cpu=2
ram=8G
network0_type="e1000"
network0_switch="public"
utctime="no"
passthru0="4/0/0"
```

`4/0/0` 是一个 passthru NVMe SSD。

目前，NVMe 启动支持 Windows 8.1 及更新的 Windows 操作系统，如果你想从 NVMe 磁盘启动 Windows 7，请按照以下步骤进行。

* 使用 ahci-HD 控制器安装 Windows 7 客户机，就像正常程序一样。
* 安装后，用 nvme 控制器附加一个额外的 disk1.img。
* 安装微软的 nvme 补丁，即 ``Windows6.1-KB2990941-v3-x64.msu`` 和 ``Windows6.1-KB3087873-v2-x64.msu``，确保 nvme 控制器和磁盘 1 出现在 windows7 客户的设备管理器中。
* 关闭客户机电源，交换客户机配置中的 disk0.img 和 disk1.img。再次启动。
* 关闭客户机电源，删除 ahci 控制器和 disk1.img。留下 nvme 控制器和 disk0.img，再次启动。

现在 Windows 7 客户机设备管理器中只有 nvme 控制器，没有 ahci 控制器。

## 从 VNC 访问 GUI

从 5 月 27 日开始，bhyve UEFI 支持帧缓冲设备，并可以用 VNC 访问。

### VNC 链接

#### 更新 vm-bhyve

确保你至少在运行 vm-bhyve 1.1。

#### 使用支持的 FreeBSD 版本

如果从源码编译，目前在 12-CURRENT 和 11-STABLE 中有图形支持。如果您喜欢使用二进制版本，可以使用 11.0 候选版本。

我们不支持在任何低于 11 的版本上运行图形界面。

#### 获取最新的UEFI固件

`pkg install sysutils/bhyve-firmware` 现在将 `edk2-bhyve` 和 `uefi-edk2-bhyve-csm` 作为依赖项安装。无需安装且也不存在 `uefi-edk2-bhyve`。

如果你正在运行 vm-bhyve 1.1-p3 或更高版本，只需安装这个 port/软件包就足够了。因为我们会自动在正确的地方寻找固件。如果你正在使用以前的版本，你仍然需要把固件从 `/usr/local/share/uefi-firmware` 复制到 `/my/vm/dir/.config/`。

#### 更新客户机配置

以下已在一个已经使用以前的 UEFI 固件的 Windows 虚拟机上进行了测试。

需要添加以下选项到配置文件中：

```
graphics="yes"
```

在启动客户机时，应该添加一个 800x600 的帧缓冲设备到客户机中。我们尝试动态地分配一个可用的端口给 vnc 服务器来监听。你可以在 `vm list` 输出中看到分配的端口（或者在控制台-端口下的 `vm info guest`）。

#### 其他配置选项

默认情况下，在客户机中创建一个 PS2 鼠标。这是旧版本的 Windows/FreeBSD 唯一支持的鼠标。新版本支持 XHCI 鼠标，它的效果要好得多。可以通过添加以下配置来启用改进的鼠标：

```
xhci_mouse="yes"
```

为了在 13.0 之后的 FreeBSD 宿主机中正确使用 xhci 鼠标，应该使用 hms(4) 驱动程序，要启用它，请在 `/boot/loader.conf` 中添加这个：

```
hw.usb.usbhid.enable=1
usbhid_load="YES"
```

早于  FreeBSD 13.0 的系统请使用 <https://github.com/wulf7/utouch>（port `misc/utouch-kmod`）。

如果你想让 VNC 监听一个特定的主机 IP 地址，请指定以下选项：

```
graphics_listen="1.2.3.4"
```

你也可以选择一个 5900 以外的端口。显然，如果你有多个客户机，需要为每个客户机使用不同的端口号。如果没有指定，我们会自动选择一个可用的端口，从 5900 开始：

```
graphics_port="5901"
```

默认情况下，屏幕分辨率被设置为 `800x600`。要指定一个不同的分辨率，请使用以下选项：

```
graphics_res="1600x900"
```

请注意，目前只支持以下分辨率：

```
1920x1200
1920x1080
1600x1200
1600x900
1280x1024
1280x720
1024x768
800x600
640x480
```

下面的选项将使 bhyve 暂停启动，直到有客户端连接到 VNC 会话。当在启动过程中需要按一个键时，这对安装客户机很有用。默认情况下，它被设置为“auto”，这使得 vm-bhyve 在安装模式下运行时，在第一次启动时等待。设置为“no”将导致客户永远不等待，即使在安装模式下：

```
graphics_wait="yes"
```


## 参考资料

 - <https://github.com/churchers/vm-bhyve/wiki/Running-Windows>
 - <https://twitter.com/bhyve_dev/status/1446404943020056581>
 - <https://forums.freebsd.org/threads/windows-11-on-bhyve.82371/>
 - <https://dadv.livejournal.com/209650.html>
 - <https://wiki.freebsd.org/bhyve/Windows>
 - <https://github.com/churchers/vm-bhyve/wiki>

