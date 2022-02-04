# 第二节 FreeBSD 13.0 安装——基于 Virtual Box

**注意：不推荐新手使用此虚拟机，因为需要踩的坑比较多。**

## VirtualBox 下载

点击“download” 即可下载：

{% embed url="https://www.virtualbox.org" %}

## VirtualBox 虚拟机 FreeBSD 配置

#### 安装设置

安装完成后请手动关机，卸载或删除安装光盘，否则还会进入安装界面。

#### 网络设置

网络设置比较复杂，为了达到使用宿主机（如 Windows10 ）控制虚拟机里的 FreeBSD 系统的目的，需要设置两块网卡——一块是NAT网络模式的网卡用来上网、另一块是仅主机模式的网卡用来互通宿主机。如图所示：

![](../.gitbook/assets/QQ图片20211231155133.png)

![](../.gitbook/assets/QQ图片20211231155139.png)

使用命令`# ifconfig`看一下，如果第二块网卡`em1`没有获取到 ip 地址,请手动 DHCP 获取一下: `# dhclient em1`即可(为了长期生效可在`/etc/rc.conf`中加入`ifconfig_em1="DHCP"`）

如果没有网络（互联网）请设置 DNS 为 `223.5.5.5`。如果不会，请看本章第四节。

#### 安装增强工具

`# pkg install virtualbox-ose-additions`

xorg 可以自动识别驱动，不需要手动配置`/usr/local/etc/X11/xorg.conf`（经过测试手动配置反而更卡，点一下要用 5 秒钟动一次……）。

显卡控制器用 `VBoxSVGA`即可。

编辑 `# ee etc/rc.conf`，增加以下內容：

```
vboxguest_enable="YES"
vboxservice_enable="YES"
```

启动服务，调整权限：

```
# service vboxguest restart #可能会提示找不到模块，但是不影响使用
# service vboxservice restart
# pw groupmod wheel -m <yourname> #sudo 权限
# pw groupmod opt -m <yourname>   #开机重启 权限
```
