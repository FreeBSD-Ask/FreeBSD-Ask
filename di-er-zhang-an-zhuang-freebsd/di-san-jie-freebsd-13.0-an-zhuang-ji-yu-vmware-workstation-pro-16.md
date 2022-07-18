# 第三节 FreeBSD 13.0 安装——基于 Vmware Workstation Pro 16

## 视频教程（一共4节，完整版本请点击去 bilibili 观看）

https://www.bilibili.com/video/BV14i4y137mh

Release 正式版 镜像下载地址：<https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/13.0/FreeBSD-13.0-RELEASE-amd64-disc1.iso>

Current 测试版（仅限专业用户，对于该版本来说，无法启动，环境变量错误都是正常的事情！） 镜像下载地址（北京交通大学开源镜像站）: <https://mirror.bjtu.edu.cn/freebsd/snapshots/ISO-IMAGES/14.0/>

FreeBSD 旧版本下载地址: [http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/old-releases/amd64/ISO-IMAGES/](http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/old-releases/amd64/ISO-IMAGES/)

## VMware Workstation Pro 下载

VMware Workstation Pro 是免费试用下载的，请勿从第三方站点下载，否则会造成一些苦难哲学的后果。点击 Download NOW 即可。左边是 Windows 系统使用，右侧是 Linux 系统使用。该软件虽是收费的，但是授权码并不难获得。

<https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html>

### VMware Workstation 16 Player 下载

VMware Workstation 16 Player 是个人免费使用的，你也可以选择此版本。

<https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html>

## 网络设置

请使用 NAT 模式，如果不能与宿主机（物理机）互通，请打开 VMware 编辑-虚拟网络管理器，移除第一项“桥接”。移除后重启虚拟机应该就可以了。

如果没有网络请设置 DNS 为`223.5.5.5`。请看本章第四节。

## 显卡驱动以及虚拟机增强工具

### 显卡驱动

VMware 自动缩放屏幕请安装显卡驱动和虚拟机增强工具，即：

```
# pkg install xf86-video-vmware open-vm-tools
```

安装完毕后无需任何多余配置即可实现屏幕自动缩放。

>请勿做多余配置，比如去修改创建 `xorg.conf`，这会造成虚拟机卡死等问题。

> wayland 下也需要安装该驱动。即使 wayland 暂不可用。

> 如果屏幕显示不正常（过大），请尝试：编辑虚拟机设置——>硬件、设备——>显示器——>监视器、指定监视器设置——>任意监视器的最大分辨率，设置为主机的分辨率或者略低于主机分辨率均可。


### 虚拟机增强工具

如果有桌面

```
# pkg install open-vm-tools
```

如果没有桌面：

```
# pkg install open-vm-tools-nox11
```

具体配置

编辑 `/boot/loader.conf`

写入

```
fusefs_load="YES"
```

### 共享文件夹

请先安装虚拟机增强工具。

```
# mount -t .host:/ /mnt/hgfs
```

查看共享文件夹

```
# ls /mnt/hgfs
```

**注意：由于 BUG，FreeBSD 11/12 可能在 VmMare 的 UEFI 环境下无法启动。经测试 13.0 正常启动。**

>**提示**
>
>在使用 Windows 远程桌面或者其他 XRDP 工具远程另一台 Windows 桌面，并使用其上面运行的 Vmware 虚拟机操作 FreeBSD 时，鼠标通常会变得难以控制。
