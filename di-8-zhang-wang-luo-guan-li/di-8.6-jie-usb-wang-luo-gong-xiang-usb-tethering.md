# 8.6 USB 网络共享（USB tethering）

## 概述

USB 网络共享（USB tethering）是通过通用串行总线（USB）物理层将移动设备（如智能手机、平板电脑）的广域网（WAN）连接共享给计算机系统的技术。

以下配置方法已在红米 Note 12 5G 上完成测试验证，可支持 Android 设备和 iPhone 13 及更早型号的 iOS 设备（iPhone 14 及更新型号因 NCM 协议兼容性问题暂不可用，详见下文 Apple 设备驱动部分说明）。

### Wi-Fi 共享的流量特性

部分 Android 手机（如 Google Pixel 3 及更新机型）开启 Wi-Fi 并关闭移动数据后，可将网络共享给 FreeBSD。该功能通过将手机已建立的 Wi-Fi 连接经由 USB 接口转发给 FreeBSD 实现，不产生移动数据流量。

![USB 网络共享](../.gitbook/assets/tethering.png)

已获取 root 权限的 Android 设备，还可通过数据线将手机的 VPN 连接共享给 FreeBSD 设备。相关软件可参考 [VPN 热点](https://github.com/mygod/vpnhotspot)，使用方法可参考 [通过创建 Wifi 热点来共享 V2ray 代理](https://www.sainnhe.dev/post/v2ray-hotspot/)。

## 加载内核模块

首先需加载相应内核模块，使系统能识别 USB 网络共享设备（若默认未加载）。

### 通用 Android 设备驱动

一般 Android 设备使用远程网络驱动接口规范（Remote Network Driver Interface Specification，RNDIS）协议，需加载以下内核模块：

```sh
# kldload if_urndis
```

该命令加载 USB RNDIS 网络驱动，使系统能够识别使用 RNDIS 协议的 Android 设备。

### Apple 设备驱动

Apple iPhone/iPad 设备需加载以下内核模块：

```sh
# kldload if_ipheth
```

该命令加载 iPhone/iPad 以太网网络驱动，使系统能够识别 iOS 设备的 USB 网络共享功能。加载成功后，系统通常会创建类似 `ue0` 的网络接口。

> **注意**
>
> 自 iPhone 14 系列起，Apple 已将 USB 网络共享协议从传统 IP-over-USB 切换为 NCM 协议。FreeBSD 的 if_ipheth 驱动目前不支持 NCM 模式，if_cdce 驱动对 Apple 的 NCM 实现也存在兼容性问题（Apple 的 NCM 实现不完全符合标准），可能导致连接不可用。截至 2025 年末，此问题尚无完善的解决方案。

### 较新 Android 设备驱动（CDC NCM）

自 Google Pixel 6 系列（2021 年）起，Google 已将 Android 原生 USB 网络共享协议从 RNDIS 切换为网络控制模型（Network Control Model，NCM），其他部分厂商的新款设备也逐步跟进。此类设备需加载以下内核模块：

```sh
# kldload if_cdce
```

该命令加载 USB CDC ECM/NCM 网络驱动，使系统能够识别使用 NCM 协议的 Android 设备。加载成功后，系统通常会创建类似 `ue0` 的网络接口。

## 持久化驱动加载机制

如果需要系统启动时自动加载上述模块，可根据设备类型选择相应条目写入 **/boot/loader.conf** 文件：

```ini
if_urndis_load="YES"  # 设置系统启动时自动加载 USB RNDIS 网络驱动
if_cdce_load="YES"    # 设置系统启动时自动加载 USB CDC ECM/NCM 网络驱动
if_ipheth_load="YES"  # 设置系统启动时自动加载 iPhone/iPad 以太网驱动
```

编辑完成后，保存文件并重启系统使更改生效。

## 物理连接与网络共享启用

加载所需内核模块后，将 USB 数据线连接到 FreeBSD 系统与移动设备之间，随后在移动设备上开启 USB 网络共享功能。具体开启方式因设备品牌和系统版本而异，通常可在移动设备的“设置”、“网络”或“个人热点”菜单中找到相关选项。需注意，部分 Android 设备可能需要先启用 USB 调试才能识别 USB 网络共享设备（大多数现代 Android 设备无需此步骤）；iOS 设备可能需要在弹出的对话框中确认信任该计算机方可正常工作。

## 获取 IP 地址

移动设备开启 USB 网络共享后，FreeBSD 系统会自动创建相应的网络接口，通常接口名称为 `ue0`，可通过 `ifconfig` 命令确认实际接口名称。确认接口名称后，通过 DHCP 为该接口获取 IP 地址：

```sh
# dhclient ue0
```

该命令为 `ue0` 接口发送 DHCP 请求，从移动设备获取 IP 地址、子网掩码、默认网关和 DNS 服务器等网络配置参数。获取成功后，可使用 `ifconfig ue0` 命令查看分配的 IP 地址。

## 参考文献

- FreeBSD Project. if_urndis -- USB Remote NDIS Ethernet device[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?query=if_urndis&sektion=4>. USB RNDIS 网络设备驱动手册页，用于 Android USB 网络共享。
- FreeBSD Project. if_cdce -- Communication Device Class Ethernet device[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?query=if_cdce&sektion=4>. USB CDC Ethernet 设备驱动手册页。
- FreeBSD Project. if_ipheth -- Apple iPhone USB Ethernet device[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?query=if_ipheth&sektion=4>. iPhone USB 网络共享驱动手册页。
- FreeBSD Project. dhclient -- Dynamic Host Configuration Protocol client[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?query=dhclient&sektion=8>. DHCP 客户端手册页，描述自动获取 IP 地址配置。
- FreeBSD Project. ifconfig -- configure network interface parameters[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?query=ifconfig&sektion=8>. 网络接口配置工具手册页。
- FreeBSD Project. loader.conf -- kernel and module configuration[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?query=loader.conf&sektion=5>. 内核模块加载配置文件格式手册页。
