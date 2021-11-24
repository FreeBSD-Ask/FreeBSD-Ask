# 第二节 FreeBSD 13.0 安装——基于 Virtual Box

## VirtualBOX 虚拟机 FreeBSD配置

`#pkg install virtualbox-ose-additions`

　　再将

```
Section "Device"
Identifier "Card0"
Driver "vboxvideo"
VendorName "InnoTek Systemberatung GmbH"
BoardName "VirtualBox Graphics Adapter"
EndSection
```

　　写到 `/usr/local/etc/X11/ xorg.conf`

　　显卡控制器用 VBoxSVGA

編輯 `#ee etc/rc.conf`，增加以下內容：

```
vboxguest_enable="YES"
vboxservice_enable="YES"
```

启动服务，调整权限：

```
#service vboxguest restart
#service vboxservice restart
#pw groupmod wheel -m <yourname> #sudo 权限
#pw groupmod opt -m <yourname>   #开机重启 权限
```

