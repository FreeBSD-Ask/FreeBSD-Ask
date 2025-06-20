# 7.2 蓝牙

由 iwm 驱动的网卡可以安装 `comms/iwmbt-firmware` 这个包来驱动蓝牙：

- 使用 pkg 安装：

```sh
# pkg install iwmbt-firmware
```

- 使用 Ports 安装：

```sh
# cd /usr/ports/comms/iwmbt-firmware/ 
# make install clean
```

---

蓝牙走 USB 总线，使用 `usbconfig` 可查看所有设备，包括蓝牙，如 `ugen1.5` 是蓝牙，则： `iwmbtfw -d ugen1.5`。

## 无线蓝牙鼠标的设置

本文基于 FreeBSD 13.0，罗技 m337。

```sh
# service hcsecd enable
# service bthidd enable
# service hcsecd start
# service bthidd start
```

使用 `bluetooth-config` 工具添加蓝牙设备即可。

蓝牙鼠标调到配对模式，运行 `# bluetooth-config scan`，按提示信息进行添加：

```sh
#  bluetooth-config scan
Scanning for new Bluetooth devices (Attempt 1 of 5) ... done.
Found 1 new bluetooth device (now scanning for names):
[ 1] 34:88:5d:12:34:56  "Bluetooth Mouse M336/M337/M535" (Logitech-M337)
Select device to pair with [1, or 0 to rescan]: 1

This device provides human interface device services.
Set it up? [yes]:
```

## 故障排除与未竟事宜

- logitech m337 配对连接后会自动断开。

解决方案：删除 `/var/db/bthidd.hids` 文件中对应鼠标的 `bd_addr` 行 `xx:xx:xx:xx:xx`。重启 `bthidd` 服务 `# service bthidd restart`。


