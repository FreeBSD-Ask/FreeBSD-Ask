# 第 2.12 节 安装 FreeBSD——基于 Apple M1&VMware Fusion Pro

本文基于 macOS 15.3.1，VMware Fusion Pro 13.6.2,FreeBSD 15.0，UEFI（默认）。

## 下载 VMware Fusion Pro

博通直链：<https://softwareupdate.vmware.com/cds/vmw-desktop/fusion/>

可以在 [fusion-arm64.xml](https://softwareupdate.vmware.com/cds/vmw-desktop/#:~:text=Files-,fusion%2Darm64.xml,-fusion%2Duniversal.xml) 找到 arm 架构的 VMware Fusion Pro。若没有最新版本，则下载后更新即可。

## 下载 FreeBSD

由于苹果 M1 是 arm 架构，请下载带有 `aarch64` 字样的镜像。**不要**下成 `amd64`。

## 配置虚拟机

![](../.gitbook/assets/Fusion1.png)

![](../.gitbook/assets/Fusion2.png)

![](../.gitbook/assets/Fusion3.png)

![](../.gitbook/assets/Fusion4.png)

## 开始安装

![](../.gitbook/assets/Fusion5.png)

![](../.gitbook/assets/Fusion6.png)


## 配置桌面

无需安装任何虚拟机增强工具。

![](../.gitbook/assets/Fusion7.png)

![](../.gitbook/assets/Fusion8.png)

![](../.gitbook/assets/Fusion9.png)

桌面不能抻拉。

## 故障排除

### 解决鼠标不能移动的问题

编辑 `/boot/loader.conf`，加入：

```sh
hw.usb.usbhid.enable="1"
usbhid_load="YES"
```

即可。

#### 参考文献

- [Mouse does not work in VMWARE Fusion and Freebsd 14.2](https://forums.freebsd.org/threads/mouse-does-not-work-in-vmware-fusion-and-freebsd-14-2.96563/)