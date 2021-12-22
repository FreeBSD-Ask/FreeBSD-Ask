# 第六节 物理机安装与硬件选配

## 物理机安装添加

物理机安装应该选用 **img** 结尾的镜像，例如

[_**https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/13.0/FreeBSD-13.0-RELEASE-amd64-memstick.img**_](https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/13.0/FreeBSD-13.0-RELEASE-amd64-memstick.img)

刻录工具 Windows 应该选用 Rufus，Linux 直接使用 `dd`命令即可。：

{% embed url="https://rufus.ie/zh" %}

**注意：使用 Handbook 推荐的 **_**win32diskimager**_** 亦可。如果安装后需要恢复 U 盘，请参考使用 Windows 的 **_**diskpart**_** 命令，也可以使用傲梅分区助手和 **_**diskgenius**_**。**

## 硬件选配（以下硬件均正常运行）

更多硬件请参考：

{% embed url="https://bsd-hardware.info/?d=FreeBSD" %}

1、小米笔记本 12.5 一代 ：处理器 6Y30 、显卡 HD515 、WIFI intel 8260AC、声卡 ALC 233（实际上是 235）、硬盘 NVME INTEL 600P。

2、联想 G400 ：处理器 i3-3110M/i5-3230M、显卡 HD4000、WIFI intel N135（联想 G400 网卡白名单支持三种网卡，如果是博通 BCM43142 建议更换为 N135，FUR 料号：04W3783）。注意：如果要使用 UEFI，必须使用 FreeBSD 13.0 及以上，否则启动会花屏……
