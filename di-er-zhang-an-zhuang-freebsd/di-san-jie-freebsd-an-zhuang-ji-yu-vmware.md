# 第三节 FreeBSD 13.0 安装——基于 Vmware Workstation Pro 15

## 视频教程

[https://www.bilibili.com/video/BV14i4y137mh](https://www.bilibili.com/video/BV14i4y137mh)

## 故障排除

vmware 自动缩放屏幕请安装 x11-drivers/xf86-video-vmware：&#x20;

`#pkg install xf86-video-vmware`

**由于 BUG，FreeBSD 11/12 可能在 Vmware 的 UEFI 环境下无法启动。13.0 经测试正常启动。**
