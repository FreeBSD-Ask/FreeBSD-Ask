# 第三节 FreeBSD 13.0 安装——基于 Vmware Workstation Pro 16

## 视频教程（一共4节，完整版本请点击去 bilibili 观看）

{% embed url="https://www.bilibili.com/video/BV14i4y137mh" %}

Release 正式版 镜像下载地址：[_https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/13.0/FreeBSD-13.0-RELEASE-amd64-disc1.iso_](https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/13.0/FreeBSD-13.0-RELEASE-amd64-disc1.iso)

FreeBSD 旧版本下载地址: [http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/old-releases/amd64/ISO-IMAGES/](http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/old-releases/amd64/ISO-IMAGES/)

## VMware Workstation Pro 下载

VMware Workstation Pro 是免费试用下载的，请勿从第三方站点下载，否则会造成一些苦难哲学的后果。点击 Download NOW 即可。左边是 Windows 系统使用，右侧是 Linux 系统使用。该软件虽是收费的，但是授权码并不难获得。

{% embed url="https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html" %}

### VMware Workstation 16 Player 下载

VMware Workstation 16 Player 是个人免费使用的，你也可以选择此版本。

{% embed url="https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html" %}

## 网络设置

请使用 NAT 模式，如果不能与宿主机（物理机）互通，请打开 Vmware 编辑-虚拟网络管理器，移除第一项“桥接”。移除后重启虚拟机应该就可以了。

如果没有网络请设置 DNS 为223.5.5.5。请看本章第四节。

## 虚拟机增强工具以及显卡驱动

### 虚拟机增强工具

如果没有桌面：

```
# pkg install open-vm-tools-nox11
```

如果有桌面

```
# pkg install open-vm-tools
```

具体配置

将下面几行加入 `/etc/rc.conf`

```
vmware_guest_vmblock_enable="YES"
vmware_guest_vmhgfs_enable="YES"
vmware_guest_vmmemctl_enable="YES"
vmware_guest_vmxnet_enable="YES" 
vmware_guestd_enable="YES"
```

编辑 `/boot/loader.conf`

写入

```
fusefs_load="YES"
```

### 显卡驱动

vmware 自动缩放屏幕请安装显卡驱动，即：

`# pkg install xf86-video-vmware`

>wayland 下也需要安装该驱动。

### 共享文件夹

请先安装虚拟机增强工具。

```
# mount -t .host:/ /mnt/hgfs
```

查看共享文件夹

```
# ls /mnt/hgfs
```

**注意：由于 BUG，FreeBSD 11/12 可能在 Vmware 的 UEFI 环境下无法启动。经测试 13.0 正常启动。**
