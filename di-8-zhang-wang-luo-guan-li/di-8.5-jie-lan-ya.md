# 8.5 蓝牙

蓝牙是一种无线技术，用于在 2.4 GHz 免授权频段内创建个人网络，通常覆盖 10 米范围。此类网络通常由便携设备（如手机、手持设备和笔记本电脑）按需形成。与 Wi-Fi 不同，蓝牙提供更高级别的服务协议，例如 FTP 类文件服务器、文件推送、语音传输、串行线路仿真等。

本节介绍在 FreeBSD 系统上使用 USB 蓝牙适配器的方法，以及各种蓝牙协议和实用程序。

## 加载蓝牙支持

FreeBSD 蓝牙协议栈基于 Netgraph 框架实现。USB 蓝牙适配器需加载 `ng_ubt` 内核模块。若需开机自动加载，可将以下配置写入 **/boot/loader.conf**：

```ini
ng_ubt_load="YES"
```

蓝牙功能的实现依赖多个系统服务协同工作。需在 **/etc/rc.conf** 中添加以下配置（或使用 `service` 命令启用）：

```ini
hcsecd_enable="YES"
sdpd_enable="YES"
bthidd_enable="YES"
```

也可通过以下命令启用并启动相关服务：

```sh
# service hcsecd enable  # 启用 hcsecd 服务
# service sdpd enable    # 启用 sdpd 服务
# service bthidd enable  # 启用 bthidd 服务
# service hcsecd start   # 立即启动 hcsecd 服务
# service sdpd start     # 立即启动 sdpd 服务
# service bthidd start   # 立即启动 bthidd 服务
```

相关组件说明：

- `ng_ubt`：Netgraph USB 蓝牙驱动，为 USB 蓝牙适配器提供传输层支持，是蓝牙协议栈的基础驱动。
- `hcsecd`：管理蓝牙设备的链路密钥和 PIN 码，负责蓝牙设备的安全认证。
- `sdpd`：蓝牙服务发现协议（Service Discovery Protocol）守护进程，负责发现和通告蓝牙服务。
- `bthidd`：支持 Bluetooth HID（Human Interface Device）设备，如蓝牙鼠标、键盘等。
- `hccontrol`：通过 hccontrol(8) 可控制蓝牙 HCI 底层接口，包括查询设备状态、扫描附近设备、管理连接等操作，是蓝牙调试的核心工具。

## 蓝牙鼠标配对

以罗技 M337 鼠标为例，需长按鼠标底部的配对按钮直至指示灯快速闪烁，使其进入可被发现的配对模式。

使用 root 权限运行 `bluetooth-config scan` 命令，扫描附近可用的蓝牙设备，并按提示信息完成设备配对与添加：

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

由 iwm 及 iwlwifi 驱动的 Intel 无线网卡通常集成了蓝牙功能，可通过安装 **comms/iwmbt-firmware** 固件包来加载蓝牙硬件所需的微码。

- 使用 pkg（二进制包管理器）安装：

```sh
# pkg install iwmbt-firmware
```

- 使用 Ports 安装：

```sh
# cd /usr/ports/comms/iwmbt-firmware/
# make install clean
```

蓝牙设备通过 USB 总线连接，可使用 `usbconfig` 工具查看所有 USB 设备（包括蓝牙设备）。如果系统启动时固件未自动加载，可手动加载。例如，如果蓝牙设备标识为 `ugen1.5`，则可执行：

```sh
# iwmbtfw -d ugen1.5 -f /usr/local/share/iwmbt-firmware/
```

> **注意**
>
> FreeBSD 蓝牙协议栈初始化脚本（**/etc/rc.d/bluetooth**）可能在系统服务启动阶段（蓝牙 HID 守护进程尝试打开设备时）导致设备锁定。因此，必须在启动蓝牙协议栈之前先运行 `iwmbtfw` 加载固件，否则需执行完整的断电/重启或挂起/恢复周期才能解锁设备。

## 故障排除与未竟事宜

### 配对连接后自动断开

此问题可能由 bthidd 服务缓存的设备信息与实际设备状态不一致所致。解决方案：删除 **/var/db/bthidd.hids** 文件中对应鼠标的 `bd_addr` 行（该行包含设备的蓝牙地址，格式为 `xx:xx:xx:xx:xx:xx`，如 `34:88:5d:12:34:56`），清除旧的配对信息。

完成上述操作后，重启蓝牙 HID 守护进程服务使更改生效：

```sh
# service bthidd restart
```
