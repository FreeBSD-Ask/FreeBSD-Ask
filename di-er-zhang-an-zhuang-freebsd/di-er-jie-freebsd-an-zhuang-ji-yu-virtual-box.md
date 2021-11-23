# 第二节 FreeBSD 13.0 安装——基于 Virtual Box

## VirtualBOX 虚拟机 FreeBSD配置

`#pkg install virtualbox-ose-additions`

　　再将
```
Section “Device”
Identifier “Card0”
Driver “vboxvideo”
VendorName “InnoTek Systemberatung GmbH”
BoardName “VirtualBox Graphics Adapter”
EndSection`
```
　　写到 /usr/local/etc/X11/ xorg.conf

　　显卡控制器用 VBoxSVGA
