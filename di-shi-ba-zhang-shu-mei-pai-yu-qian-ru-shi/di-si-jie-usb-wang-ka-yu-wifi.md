# 第四节 USB 网卡与 WIFI

　树莓派 3B+是目前配置比较高的型号，由于 FreeBSD 的 SDIO 驱动并未完全支持，所以板载的蓝牙和 WIFI 均无法使用（可购买无线网卡，推荐 16 块钱的 COMFAST CF-WU810N ）。

　如果你购买了上述无线网卡，想实现开机自动连接 wifi 的功能，那也非常简单。

　　方法：

　　/boot/loader.conf

　　中写入

```
　　rtwn_usb_load="YES"
　　legal.realtek.license_ack=1
```

　　在 /etc/rc.conf 中写入

```
　　wlans_rtwn0="wlan0"
　　ifconfig_wlan0="WPA DHCP"
```

　　注意在 /etc/wpa\_supplicant.conf 文件中（没有就自己通 touch 命令新建一个）写入

　　network={ ssid=”wifi 名字，别搞什么中文” psk=”密码” }

　　保存重启即可。能够实现开机自动连接 wifi 。
