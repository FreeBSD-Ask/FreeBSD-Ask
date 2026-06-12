# 5.4 基于 Apple M1 和 Parallels Desktop 20 安装 FreeBSD

基于 macOS 14.7 与 Parallels Desktop 20.1.3 环境，FreeBSD 15.0 的图形界面、键盘和鼠标均可正常运作。

## 安装

环境准备完成后，安装 FreeBSD。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/parallels-1.png)

选择“通过映像文件安装 Windows、Linux 或 macOS”，确认并继续。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/parallels-2.png)

选择“手动选择”并继续。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/parallels-3.png)

选择“选择文件……”。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/parallels-4.png)

选中 FreeBSD 镜像。

> **警告**
>
> 本节基于 Apple M1，故选择的 FreeBSD 架构应为 aarch64。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/parallels-5.png)

界面提示“未能检测操作系统”时，忽略该提示并继续。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/parallels-6.png)

在操作系统类型中选择“其他”。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/parallels-7.png)

> **技巧**
>
> Parallels Desktop 20 的默认设置通常已足够，且默认使用 UEFI 引导，无需调整硬件配置。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/parallels-8.png)

开始安装 FreeBSD 系统。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/parallels-9.png)

系统启动后进入 FreeBSD。

![Parallels Desktop 20 安装 FreeBSD 15.0](../.gitbook/assets/parallels-10.png)

安装桌面环境后，桌面即可正常运行。

## 鼠标无法移动

如果在 Parallels Desktop 中遇到 FreeBSD 鼠标无法移动的问题，可在 **/boot/loader.conf.local**（推荐使用本地配置扩展文件，避免直接修改系统默认配置 **/boot/loader.conf**）中添加如下配置：

```sh
ums_load="YES"
```

### 参考文献

- FreeBSD Forums. Issue(s) booting FreeBSD 12.2 aarch64 on Parallels Desktop on Apple Silicon[EB/OL]. (2021-01-30)[2026-03-26]. <https://forums.freebsd.org/threads/issue-s-booting-freebsd-12-2-aarch64-on-parallels-desktop-on-apple-silicon.78654/>. 提供了 Apple Silicon 上 Parallels Desktop 中 FreeBSD 启动问题的讨论与解决方案。

## 虚拟机工具

使用 pkg 安装虚拟机工具：

```sh
# pkg install parallels-tools
```

若提示找不到软件包，可通过 Ports 编译安装虚拟机工具：

```sh
# cd /usr/ports/emulators/parallels-tools/
# make install clean
```

> **注意**
>
> 如果通过 Ports 编译安装，需确保系统中已有源代码在 **/usr/src** 目录中。

### 参考文献

- FreshPorts. parallels-tools Parallels Desktop Tools for FreeBSD[EB/OL]. [2026-03-26]. <https://www.freshports.org/emulators/parallels-tools/>. 提供了 Parallels Desktop 虚拟机工具的 FreeBSD Port 信息与安装说明。
