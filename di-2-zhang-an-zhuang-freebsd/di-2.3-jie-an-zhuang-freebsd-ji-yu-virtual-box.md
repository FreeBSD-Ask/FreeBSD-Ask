# 第 2.3 节 安装 FreeBSD——基于 Virtual Box


## 下载 VirtualBox

进入网页点击 `Download` 即可下载：

[https://www.virtualbox.org](https://www.virtualbox.org)

## 安装设置



以下演示基于 VirtualBox 7.1.4 和 Windows11 24H2。

![](../.gitbook/assets/vb1.png)

选择“新建”。

![](../.gitbook/assets/vb2.png)


名称输入“FreeBSD”，最下面几个选项会自动补全。

![](../.gitbook/assets/vb3.png)

设置内存大小，CPU 数量，并开启 EFI。

>**技巧**
>
>UEFI 下显卡也可以正常驱动。——2023.1.14 测试
>
> ```sh
> # efibootmgr # 无需安装，自带
> Boot to FW : false
> BootCurrent: 0004
> Timeout    : 0 seconds
> BootOrder  : 0004, 0000, 0001, 0002, 0003
> +Boot0004* FreeBSD
> Boot0000* UiApp
> Boot0001* UEFI VBOX CD-ROM VB2-01700376
> Boot0002* UEFI VBOX HARDDISK VB7aff22ad-deb533d3
> Boot0003* EFI Internal Shell
> ```

![](../.gitbook/assets/vb4.png)

调整硬盘大小。

![](../.gitbook/assets/vb4.5.png)

打开设置。

![](../.gitbook/assets/vb5.png)

显卡控制器用 `VBoxSVGA` 即可。

>**警告**
>
>不要试图勾选下方的 3D，这会在实际上放弃选定 `VBoxSVGA`。

![](../.gitbook/assets/vb5.5.png)

开始安装！

![](../.gitbook/assets/vb6.png)

![](../.gitbook/assets/vb7.png)

![](../.gitbook/assets/vb8.png)

>**注意**
>
>较低版本的 VirtualBox 安装 FreeBSD 完成后请手动关机，卸载/删除安装光盘，否则还会再次进入安装界面。

安装后的系统：

![](../.gitbook/assets/vb9.png)




## 网络设置

### 方法 ① 桥接

桥接是最简单的互通主机与虚拟机的方法，并且可以获取一个和宿主机在同一个 IP 段的 IP 地址，如主机是 192.168.31.123，则虚拟机的地址为 192.168.31.x。

![](../.gitbook/assets/VBbridge.png)

设置后 `# dhclient em0` 即可（为了长期生效可在 `/etc/rc.conf` 中加入 `ifconfig_em0="DHCP"`）。

如果没有网络（互联网）请设置 DNS 为 `223.5.5.5`。如果不会，请看本章其他章节。

### 方法 ② NAT

网络设置比较复杂，有时桥接不一定可以生效。为了达到使用宿主机（如 Windows10 ）控制虚拟机里的 FreeBSD 系统的目的，需要设置两块网卡——一块是 NAT 网络模式的网卡用来上网、另一块是仅主机模式的网卡用来互通宿主机。如图所示：

![](../.gitbook/assets/vbnat1.png)

![](../.gitbook/assets/vbnat2.png)

使用命令 `# ifconfig` 看一下，如果第二块网卡 `em1` 没有获取到 ip 地址,请手动 DHCP 获取一下: `# dhclient em1` 即可（为了长期生效可在 `/etc/rc.conf` 中加入 `ifconfig_em1="DHCP"`）。

如果没有网络（互联网）请设置 DNS 为 `223.5.5.5`。如果不会，请看本章其他章节。

## 显卡驱动与增强工具

```sh
# pkg install virtualbox-ose-additions
```

或者

```sh
# cd /usr/ports/emulators/virtualbox-ose-additions/
# make install clean
```

查看安装说明：

```sh
root@ykla:/home/ykla # pkg info -D virtualbox-ose-additions
virtualbox-ose-additions-6.1.50.1401000:
On install:
VirtualBox Guest Additions are installed.

To enable and start the required services:

# sysrc vboxguest_enable="YES"
# sysrc vboxservice_enable="YES"

To start the services, restart the system.

In some situations, a panic will occur when the kernel module loads.
Having no more than one virtual CPU might mitigate the issue.

For features such as window scaling and clipboard sharing, membership of
the wheel group is required. With username "jerry" as an example:

# pw groupmod wheel -m jerry

The settings dialogue for FreeBSD guests encourages use of the VMSVGA
graphics controller. Whilst this might suit installations of FreeBSD
without a desktop environment (a common use case), it is not appropriate
where Guest Additions are installed.

Where Guest Additions are installed:

1. prefer VBoxSVGA

2. do not enable 3D acceleration (doing so will invisibly
   lose the preference for VBoxSVGA)

You may ignore the yellow alert that encourages use of VMSVGA.

```

xorg 可以自动识别驱动，**不需要** 手动配置 `/usr/local/etc/X11/xorg.conf`（经过测试手动配置反而更卡，点一下要用 5 秒钟……）。



启动服务：

```sh
# sysrc vboxguest_enable="YES"
# sysrc vboxservice_enable="YES"
```

启动服务，调整权限（以普通用户 ykla 为例）：

```sh
# service vboxguest restart # 可能会提示找不到模块，但是不影响使用
# service vboxservice restart
# pw groupmod wheel -m ykla # 管理员权限
```

## 故障排除

### EFI 下无法正常关机

添加

```sh
hw.efi.poweroff=0
```

到 `/etc/sysctl.conf`，然后再重启，再关机就正常了。

#### 参考文献

- [12.0-U8.1 -> 13.0-U2 poweroff problem & solution](https://www.truenas.com/community/threads/12-0-u8-1-13-0-u2-poweroff-problem-solution.104813/)
- [EFI: VirtualBox computer non-stop after successful shutdown of FreeBSD](https://forums.freebsd.org/threads/efi-virtualbox-computer-non-stop-after-successful-shutdown-of-freebsd.84856/)

### 鼠标进去了出不来

请先按一下右边的 `ctrl`（正常键盘左右各有一个 `ctrl`，为默认设置）；如果自动缩放屏幕需要还原或者找不到菜单栏了请按 `home`+ 右 `ctrl`。

>**技巧**
>
>在 108 键盘上，`Home` 键位于 `Scroll Lock` 的下方。

### UEFI 固件设置

开机反复按 `Esc` 即可进入 VB 虚拟机的 UEFI 固件设置。

