# 第三节 FreeBSD 13.0 安装——基于 Vmware Workstation Pro 15

## 视频教程（一共4节，完整版本请点击去 bilibili 观看）

{% embed url="https://www.bilibili.com/video/BV14i4y137mh" %}

镜像下载地址：[_https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/13.0/FreeBSD-13.0-RELEASE-amd64-disc1.iso_](https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/13.0/FreeBSD-13.0-RELEASE-amd64-disc1.iso)__

## 故障排除

vmware 自动缩放屏幕请安装 x11-drivers/xf86-video-vmware：&#x20;

`# pkg install xf86-video-vmware`

**由于 BUG，FreeBSD 11/12 可能在 Vmware 的 UEFI 环境下无法启动。13.0 经测试正常启动。**
