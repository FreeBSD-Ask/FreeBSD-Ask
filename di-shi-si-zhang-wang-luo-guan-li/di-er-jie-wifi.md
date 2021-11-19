# 第二节 WIFI

首先运行ifconfig，看看能不能找到你的网卡，如果能，那么你可以走了\
﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉\
运行sysctl net.wlan.devices，他可以告诉你，找到的无线网卡\
编辑/boot/loader.conf文件\
加入

if\_urtwn\_load =“是” legal.realtek.license\_ack = 1\
这里只是示例，请添加自己所需的\
接下来，创建wlan0

ifconfig wlan0 create wlandev at0

at0是你的网卡，具体看自己的\
，该命令是临时的，需要永久开机生效，在rc.conf中，加入\
wlans\_ath0 =“ wlan0”\
ifconfig wlan0 up scan\
扫描wifi\
ifconfig wlan0 ssid abc\
连接wifi abc\
dhclient wlan0\
获取地址\
连接加密网络\
创建wpa\_supplicant.conf

network={\
scan\_ssid=1\
如果是隐藏wifi加入这个，不是就不要加了\
ssid=”abc”\
wifi名字\
psk=”1234”\
密码\
}\
在rc.conf里面加入\
ifconfig\_wlan0 =“ WPA SYNCDHCP”\
然后重启电脑（因为命令有点问题，只能重启让rc.conf生效）\
wpa\_supplicant -B -i wlan0 -c /etc/wpa\_supplicant.conf\
wpa\_cli -i wlan0 scan // 搜索附近wifi网络\
$ wpa\_cli -i wlan0 scan\_result // 打印搜索wifi网络结果\
$ wpa\_cli -i wlan0 add\_network // 添加一个网络连接\
$ wpa\_cli -i wlan0 remove\_network 1 // 删除一个网络连接

$ wpa\_cli -i wlan0 set\_network 0 ssid ‘“name”‘\
$ wpa\_cli -i wlan0 set\_network 0 psk ‘“psk”‘\
$ wpa\_cli -i wlan0 enable\_network 0

保存连接

$ wpa\_cli -i wlan0 save\_config

断开连接

$ wpa\_cli -i wlan0 disable\_network 0

连接已有的连接

$ wpa\_cli -i wlan0 list\_network 列举所有保存的连接\
$ wpa\_cli -i wlan0 select\_network 0 连接第1个保存的连接\
$ wpa\_cli -i wlan0 enable\_network 0 使能第1个保存的连接

断开wifi

$ ifconfig wlan0 down\
附配置详情：[https://segmentfault.com/a/1190000011579147](https://segmentfault.com/a/1190000011579147)

wpa验证，静态ip\
ifconfig\_wlan0 =“WPA inet 192.168.1.100netmask 255.255.255.0”\
ifconfig wlan0 inet 192.168.0.100 netmask 255.255.255.0\
开启无线ap，，先确认下你的网卡是否支持hostap\
ifconfig wlan0 list caps\
先销毁\
ifconfig wlan0 destroy\
在创建\
ifconfig wlan0 create wlandev ath0 wlanmode hostap

\#ifconfig wlan0 inet 192.168.0.1 netmask 255.255.255.0 ssid freebsdap mode 11g channel 1

如果连不上或者搜不到调试信道或者WIFI区域码区域码选japan 然后china

## 简单版本

ee /boot/ loader.conf 　　

ee是个编辑器

中写入 rtwn\_usb\_load=”YES”

legal.realtek.license\_ack=1

在 /etc/ rc.conf 中写入

wlans\_rtwn0=”wlan0”

ifconfig\_wlan0=”WPA DHCP”
