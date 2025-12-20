# 3.6 基于 Apple M1 & Parallels Desktop 20 安装 FreeBSD


本文基于 Apple M1（macOS 14.7）及 Parallels Desktop 20.1.3-55743 环境。

在 Parallels Desktop 20 中，FreeBSD 15.0-CURRENT 的图形界面（不支持自动缩放）、键盘和鼠标均可正常工作。

>**注意**
>
>由于补丁 [acpi_ged: Handle events directly](https://reviews.freebsd.org/D42158) 未合入 FreeBSD 14，因此版本 14 无法安装，会在安装界面报错（参见 [Virtualizing FreeBSD 14 CURRENT on macOS M2 via Parallels 19](https://forums.freebsd.org/threads/virtualizing-freebsd-14-current-on-macos-m2-via-parallels-19.93266/)），故只能安装 15 及以上版本。

## 安装

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/pd1.png)

选择“通过映像文件安装 Windows、Linux 或 macOS”，然后点击“继续”。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/pd2.png)

点击“手动选择”，然后继续。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/pd3.png)

点击“选择文件……”。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/pd4.png)

选中 FreeBSD 镜像。

>**警告**
>
>本文基于 Apple M1，故你选择的 FreeBSD 架构应该是 aarch64！

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/pd5.png)

界面会提示“未能检测操作系统”，可忽略此提示，直接点击“继续”。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/pd6.png)

在操作系统类型中选择“其他”。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/pd7.png)

>**技巧**
>
>Parallels Desktop 20 的默认设置通常已足够，且默认使用 UEFI 引导，一般无需调整硬件配置。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/pd8.png)

开始安装 FreeBSD 系统。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/pd9.png)

开机后进入 FreeBSD。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/pd10.png)

手动安装桌面环境后，桌面显示正常运行。

## 故障排除与未竟事项

### 鼠标不能移动的问题

若在 Parallels Desktop 中遇到 FreeBSD 鼠标无法移动的问题，可在 `/boot/loader.conf` 中添加如下配置：


```sh
ums_load="YES"
```


### 参考文献

[Issue(s) booting FreeBSD 12.2 aarch64 on Parallels Desktop on Apple Silicon](https://forums.freebsd.org/threads/issue-s-booting-freebsd-12-2-aarch64-on-parallels-desktop-on-apple-silicon.78654/)

## 虚拟机工具

安装：

```sh
# pkg install parallels-tools
```

若提示找不到软件包，可通过 Ports 编译安装：

```sh
# cd /usr/ports/emulators/parallels-tools/ 
# make install clean
```

>**注意**
>
>若通过 Ports 编译安装，需确保当前系统的源代码位于 `/usr/src` 目录下。


### 故障排除与未尽事宜

备注：该虚拟机工具似乎长期未更新，且其提供的功能效果不甚明显。其主要用途是增强虚拟机与宿主机之间的集成体验，例如改善剪贴板共享、文件拖放以及屏幕分辨率自适应等。

### 参考文献

- [parallels-tools Parallels Desktop Tools for FreeBSD](https://www.freshports.org/emulators/parallels-tools/)
