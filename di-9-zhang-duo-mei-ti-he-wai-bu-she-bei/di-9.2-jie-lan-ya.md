# 9.2 蓝牙

## 无线蓝牙鼠标的设置

本节使用罗技（Logitech）M337 蓝牙鼠标作为示例设备进行配置说明。

### 服务管理

蓝牙功能的实现依赖于多个系统服务的协同工作。`hcsecd` 服务用于管理蓝牙设备的链路密钥和 PIN 码，负责蓝牙设备的安全认证；`bthidd` 服务用于支持 Bluetooth HID（Human Interface Device）设备，如蓝牙鼠标、键盘等。首先需要启用并启动相关服务：

```sh
# service hcsecd enable  # 启用 hcsecd 服务，用于管理蓝牙设备的链路密钥和 PIN 码
# service bthidd enable  # 启用 bthidd 服务，用于支持 Bluetooth HID 设备
# service hcsecd start   # 立即启动 hcsecd 服务
# service bthidd start   # 立即启动 bthidd 服务
```

### 蓝牙鼠标配对

以罗技 M337 鼠标为例，需长按鼠标底部的配对按钮直至指示灯快速闪烁，使其进入可被发现的配对模式。

使用 root（超级用户）权限运行 `bluetooth-config scan` 命令，扫描附近可用的蓝牙设备，并按提示信息完成设备配对与添加：

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

由 iwm 驱动的 Intel 无线网卡可通过安装 `comms/iwmbt-firmware` 固件包来启用蓝牙功能，该固件为蓝牙硬件提供必要的微码支持。

- 使用 pkg（二进制包管理器）安装：

```sh
# pkg install iwmbt-firmware
```

- 使用 Ports 安装：

```sh
# cd /usr/ports/comms/iwmbt-firmware/ 
# make install clean
```

蓝牙设备通过 USB 总线连接，可使用 `usbconfig` 工具查看所有 USB 设备（包括蓝牙设备）。若系统启动时固件未自动加载，可手动加载。例如，若蓝牙设备标识为 `ugen1.5`，则可执行：

```sh
# iwmbtfw -d ugen1.5
```

## 故障排除与未竟事项

### Logitech M337 配对连接后会自动断开

此问题可能是由于 bthidd 服务缓存的设备信息与实际设备状态不一致导致。解决方案：删除 `/var/db/bthidd.hids` 文件中对应鼠标的 `bd_addr` 行（该行包含设备的蓝牙地址，格式为 `xx:xx:xx:xx:xx:xx`），清除旧的配对信息。

完成上述操作后，重启蓝牙 HID 守护进程服务以使更改生效：

```sh
# service bthidd restart
```

## 课后习题

1. 查找蓝牙鼠标配对后自动断开问题的根源，阅读 bthidd 源代码，修改配对逻辑以避免频繁重连。

2. 选取蓝牙服务栈中的某组件（如 hcsecd），在 FreeBSD 中重构其最小实现。

3. 尝试使用蓝牙音频设备（如蓝牙耳机），查找并配置必要的服务和驱动，验证其能否正常工作。
