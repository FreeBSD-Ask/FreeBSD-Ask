# 第2.2节 FreeBSD 13.1 安装——基于 Virtual Box

## 下载 VirtualBox

进入网页点击 `download` 即可下载：

[https://www.virtualbox.org](https://www.virtualbox.org)

## 安装设置

安装完成后请手动关机，卸载或删除安装光盘，否则还会进入安装界面。

## 网络设置

### 方法① 桥接

桥接是最简单的互通主机与虚拟机的方法，并且可以获取一个和宿主机在同一个 IP 段的 IP 地址，如主机是 192.168.31.123，则虚拟机的地址为 192.168.31.x。

![](../.gitbook/assets/VBbridge.png)

设置后 `# dhclient em0` 即可（为了长期生效可在 `/etc/rc.conf` 中加入 `ifconfig_em0="DHCP"`）。

如果没有网络（互联网）请设置 DNS 为 `223.5.5.5`。如果不会，请看本章其他章节。

### 方法② NAT

网络设置比较复杂，有时桥接不一定可以生效。为了达到使用宿主机（如 Windows10 ）控制虚拟机里的 FreeBSD 系统的目的，需要设置两块网卡——一块是 NAT 网络模式的网卡用来上网、另一块是仅主机模式的网卡用来互通宿主机。如图所示：

![](../.gitbook/assets/QQ图片20211231155133.png)

![](../.gitbook/assets/QQ图片20211231155139.png)

使用命令 `# ifconfig` 看一下，如果第二块网卡 `em1` 没有获取到 ip 地址,请手动 DHCP 获取一下: `# dhclient em1` 即可（为了长期生效可在 `/etc/rc.conf` 中加入 `ifconfig_em1="DHCP"`）。

如果没有网络（互联网）请设置 DNS 为 `223.5.5.5`。如果不会，请看本章其他章节。

## 显卡驱动与增强工具

> **UEFI 下显卡无法驱动。**

```
# pkg install virtualbox-ose-additions
```

xorg 可以自动识别驱动，**不需要** 手动配置 `/usr/local/etc/X11/xorg.conf`（经过测试手动配置反而更卡，点一下要用 5 秒钟……）。

显卡控制器用 `VBoxSVGA` 即可。

编辑 `# ee /etc/rc.conf`，增加以下內容：

```
vboxguest_enable="YES"
vboxservice_enable="YES"
```

启动服务，调整权限（以普通用户 ykla 为例）：

```
# service vboxguest restart # 可能会提示找不到模块，但是不影响使用
# service vboxservice restart
# pw groupmod wheel -m ykla # sudo 权限
# pw groupmod opt -m ykla # 开机重启 权限
```

## 故障排除

如果鼠标进去了出不来，请先按一下右边的 `ctrl`（键盘左右各有一个 `ctrl`，为默认设置）；如果自动缩放屏幕需要还原或者找不到菜单栏了请按 `home`+ 右 `ctrl`（提示：`Home` 键在 108 键盘上位于 `Scroll Lock` 的下边。）
