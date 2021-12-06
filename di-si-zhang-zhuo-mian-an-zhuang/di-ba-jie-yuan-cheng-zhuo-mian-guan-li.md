# 第八节 远程桌面管理

启用 VNC 服务 

FreeBSD 操作系统的 VNC 服务可以使用 TigerVNC Server，在终端下执行命令 

```
# pkg install -y tigervnc-server 进行安装。安装之后，还要做一些设置： 
```

1.在终端执行命令 vncpasswd，设置访问密码。vnc 的访问密码居然是与用户无关的？ 

2.创建~/.vnc/xstartup 文件，内容如下： 
```
#!/bin/sh unset SESSION_MANAGER unset DBUS_SESSION_BUS_ADDRESS [ -x /etc/X11/xinit/xinitrc ] && exec /etc/X11/xinit/xinitrc [ -f /etc/X11/xinit/xinitrc ] && exec sh /etc/X11/xinit/xinitrc xsetroot -solid grey $command & #$command 
```
在不同桌面下需要替换，Gnome 用 `gnome-session`，KDE 用 `startplasma-x11`， MATE 用 `mate-session`，Xfce 用 `xfce4-session`。

保存后执行命令 `# chmod 755 ~/.vnc/xstartup`。

3.接下来在终端执行命令 `vncserver` 或 `vncserver :1`。

其中“:1”相当于 DISPLAY=:1，即 
指定桌面显示的通信端口为 1，对应 VNC 服务的通信端口为 5901。尽管桌面显示通信端口 是从 0 开始，但该端口已被当前桌面占用，因此 VNC 服务默认端口虽为 5900，但实际执行往往从 5901 开始。

如果启动服务时不指定通信端口，则系统根据使用情况自动指定。

关闭服务请用命令 `# vncserver -kill :1`，这里通信端口必须指定。 

4.如果启用了防火墙，那么此时还需要开通防火墙，以 ipfw 为例，在终端输入命令： 

```
# ipfw add allow tcp from any to me 5900-5910 in keep-state #表示开通 5900-5910 的端口，即 DISPLAY 的 0-10 端口，通常情况下，即便需要开启很多桌面，10 个端口也足够了。最后别忘了将指令加入规则集文件，否则操作系统重启后会佚失。
```
---------------------------------------
Linux/BSD 等一系列操作系统的远程桌面服务都是基于 VNC 协议的，唯独 MS Windows 有自己的一套做法。那么 BSD 下要如何访问 Windows 远程桌面呢？

这里介绍一款软件 rdesktop。 安装命令：

```
# pkg install -y rdesktop 
```
但 rdesktop 安装后不会在系统中生成菜单，因此要在终端输入命令： 
```
# rdesktop windows 设备 ip 
```
首次登陆设备会有安全提示，输入 yes，回车后远程桌面窗口就会弹出：
