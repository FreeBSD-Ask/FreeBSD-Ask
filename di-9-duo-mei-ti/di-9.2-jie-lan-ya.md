# 9.2 蓝牙


## 无线蓝牙鼠标的设置

本文使用罗技 M337 蓝牙鼠标。

### 服务管理

```sh
# service hcsecd enable  # 启用 hcsecd 服务，用于管理蓝牙设备的链路密钥和 PIN 码
# service bthidd enable  # 启用 bthidd 服务，用于支持 Bluetooth HID 设备
# service hcsecd start   # 立即启动 hcsecd 服务
# service bthidd start   # 立即启动 bthidd 服务
```

### 蓝牙鼠标配对

将蓝牙鼠标切换到配对模式。

使用 root 权限运行 `bluetooth-config scan`，扫描可用的蓝牙设备，并按提示信息完成添加：

```sh
# bluetooth-config scan
Scanning for new Bluetooth devices (Attempt 1 of 5) ... done.
Found 1 new bluetooth device (now scanning for names):
[ 1] 34:88:5d:12:34:56  "Bluetooth Mouse M336/M337/M535" (Logitech-M337)
Select device to pair with [1, or 0 to rescan]: 1

This device provides human interface device services.
Set it up? [yes]:
```

## 附录：英特尔蓝牙


由 iwm 驱动的网卡可以通过安装 `comms/iwmbt-firmware` 包来启用蓝牙功能：


- 使用 pkg 安装：

```sh
# pkg install iwmbt-firmware
```

- 使用 Ports 安装：

```sh
# cd /usr/ports/comms/iwmbt-firmware/ 
# make install clean
```

蓝牙设备通过 USB 总线连接，可使用 `usbconfig` 查看所有 USB 设备（包括蓝牙设备）。例如，若蓝牙设备标识为 `ugen1.5`，则可执行：`iwmbtfw -d ugen1.5`。

## 故障排除与未竟事宜

### Logitech M337 配对连接后会自动断开

解决方案：删除 `/var/db/bthidd.hids` 文件中对应鼠标的 `bd_addr` 行（形如 `xx:xx:xx:xx:xx:xx`），然后重启 `bthidd` 服务：

```sh
# service bthidd restart
```


