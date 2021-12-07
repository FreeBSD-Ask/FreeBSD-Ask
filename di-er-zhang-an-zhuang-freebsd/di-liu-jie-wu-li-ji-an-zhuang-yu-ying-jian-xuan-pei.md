# 第六节 物理机安装与硬件选配

物理机安装应该选用 **img** 结尾的镜像，例如

__[_https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/13.0/FreeBSD-13.0-RELEASE-amd64-memstick.img_](https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/13.0/FreeBSD-13.0-RELEASE-amd64-memstick.img)__

刻录工具 Windows 应该选用 Rufus，Linux 直接使用 dd 命令即可。：

{% embed url="https://rufus.ie/zh" %}

**注意：**使用 Handbook 推荐的 _win32diskimager_ 亦可。如果安装后需要恢复 U 盘，请参考使用 Windows 的 _diskpart_ 命令，也可以使用傲梅分区助手和 _diskgenius_。

## 硬件选配（以下硬件均正常运行）

更多硬件请参考：

{% embed url="https://bsd-hardware.info/?d=FreeBSD" %}

1、小米笔记本 12.5  一代 ：处理器 6Y30 、显卡 HD515 、WIFI 8260AC、声卡 ACL233（实际上是 233）、硬盘 NVME INTEL 600P.
