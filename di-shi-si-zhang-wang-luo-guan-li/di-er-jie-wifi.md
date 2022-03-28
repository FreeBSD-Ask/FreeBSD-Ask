# 第二节 WiFi

**英特尔 WIFI 5/6 芯片（AC 8265、AC 9260、AC 9560、AX200、AX201、AX210）驱动见最后一部分。**

**注意：如果安装 FreeBSD 的时候就不能识别出无线网卡，那么就是不支持你的无线网卡。请忽略下文。**

## 一般网卡驱动

首先运行 `# ifconfig`，看看能不能找到你的网卡，如果能，那么你可以跳过本节了。

运行 `# sysctl net.wlan.devices`，
他可以告诉你，找到的无线网卡，如果冒号输出后边没有东西，那就是识别不了。请更换无线网卡。

编辑 /boot/loader.conf 文件

加入

```
if_urtwn_load="YES" 
legal.realtek.license_ack=1
```

>**注意：这里只是示例，请添加自己所需的驱动。**

接下来，创建 wlan0

```
# ifconfig wlan0 create wlandev at0
```

`at0` 是你的网卡，具体看自己的,该命令是临时的，若需要永久开机生效，在 `rc.conf` 中，加入

```
# wlans_ath0 ="wlan0"
```

扫描 WiFi

```
# ifconfig wlan0 up scan
# ifconfig wlan0 ssid abc
```

连接 WiFi abc

```
# dhclient wlan0
```

获取地址

连接加密网络

创建 `/etc/wpa_supplicant.conf`：

```
network={ 
ssid="WIFI 名字（SSID）" 
psk="WIFI 密码"
}
```

在 `rc.conf` 里面加入

```
# ifconfig_wlan0="WPA SYNCDHCP"
```

然后重启电脑（因为命令有点问题，只能重启让rc.conf生效）

```
# wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
# wpa_cli -i wlan0 scan // 搜索附近wifi网络
# wpa_cli -i wlan0 scan_result // 打印搜索wifi网络结果
# wpa_cli -i wlan0 add_network // 添加一个网络连接
# wpa_cli -i wlan0 remove_network 1 // 删除一个网络连接
# wpa_cli -i wlan0 set_network 0 ssid ‘“name”‘
# wpa_cli -i wlan0 set_network 0 psk ‘“psk”‘
# wpa_cli -i wlan0 enable_network 0
```

保存连接

```
# wpa_cli -i wlan0 save_config
```

断开连接

```
# wpa_cli -i wlan0 disable_network 0
```

连接已有的连接

```
# wpa_cli -i wlan0 list_network 列举所有保存的连接
# wpa_cli -i wlan0 select_network 0 连接第1个保存的连接
# wpa_cli -i wlan0 enable_network 0 使能第1个保存的连接
```

断开 WiFi

```
# ifconfig wlan0 down
```

附配置详情：[https://segmentfault.com/a/1190000011579147](https://segmentfault.com/a/1190000011579147)

wpa 验证，静态 ip

```
# ifconfig_wlan0="WPA inet 192.168.1.100 netmask 255.255.255.0"

# ifconfig wlan0 inet 192.168.0.100 netmask 255.255.255.0
```

开启无线 ap，先确认下你的网卡是否支持 hostap

```
# ifconfig wlan0 list caps
```

先销毁

```
# ifconfig wlan0 destroy
```

再创建

```
# ifconfig wlan0 create wlandev ath0 wlanmode hostap

# ifconfig wlan0 inet 192.168.0.1 netmask 255.255.255.0 ssid freebsdap mode 11g channel 1
```

>如果连不上或者搜不到调试信道，尝试将 WiFi 区域码选 `Japan` ，然后选 `China`

### 简单版本

以螃蟹卡为例：

>
>```
># ee /boot/loader.conf 
>```
>
>加入
>
>```
>rtwn_usb_load="YES"
>legal.realtek.license_ack=1
>```
>
>在 `/etc/rc.conf` 中写入
>
>```
>wlans_rtwn0="wlan0"
>ifconfig_wlan0="WPA DHCP"
>```
>
>执行：
>
>```
># /etc/rc.d/netif start
>```

## 英特尔 WIFI 5/6 芯片

>以下部分仅适用于 FreeBSD 13.1、14.0。
>
>iwlwifi 驱动适用于`AC 8265、AC 9260、AC 9560、AX200、AX201、AX210` 以及旧的 iwm 驱动所包含的网卡，见 <https://www.intel.cn/content/www/cn/zh/support/articles/000005511/wireless.html>。
> 
>**该驱动仍不完善，不会自动加载（可以用命令`# sysctl net.wlan.devices`查看有无加载，如果没有显示`iwlwifi0`就没有加载），每次都需要手动加载。**

将以下部分写入`/etc/rc.conf`：

```
kld_list="if_iwlwifi"
wlans_iwlwifi0="wlan0"
wlandebug_wlan0="+state +crypto +node +auth +assoc +dot1xsm +wpa"
ifconfig_wlan0="WPA SYNCDHCP"
```

创建 `/etc/wpa_supplicant.conf`：

```
network={ 
ssid="WIFI 名字（SSID）" 
psk="WIFI 密码"
}
```

先加载驱动看一下：

```
# kldload if_iwlwifi
```

>**注意：以下部分每次开机都要执行一次方能联网。**


创建并链接：

```
# ifconfig wlan0 create wlandev iwlwifi0
# /etc/rc.d/netif start  wlan0
```

故障排除：<https://wiki.freebsd.org/WiFi/Iwlwifi>
