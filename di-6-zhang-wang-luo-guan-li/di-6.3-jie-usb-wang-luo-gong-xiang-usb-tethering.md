# 6.3 USB 网络共享（USB tethering）

## 概述

USB 网络共享（USB tethering）是一种通过通用串行总线（Universal Serial Bus，USB）物理层将移动设备（如智能手机、平板电脑）的广域网（WAN）连接共享给计算机系统的技术。该技术实现了移动设备网络连接的复用，为缺乏独立网络接入的计算设备提供了临时网络连接方案。

本节介绍 FreeBSD 操作系统中 USB 网络共享的配置方法，该教程已在红米手机（红米 Note 12 5G）上完成测试验证，从技术原理上可同时支持 Android 和 iOS 设备。

### WiFi 共享的流量特性

对于大多数新款 Android 手机，可以实现在开启 WiFi 关闭流量的同时共享网络给 FreeBSD。该功能通过将手机已建立的 WiFi 连接通过 USB 接口转发给 FreeBSD 实现，不会消耗移动数据流量。

![USB 网络共享](../.gitbook/assets/tethering.png)

对于已获取 root 权限的 Android 设备，还可以通过数据线共享手机的 VPN 连接给 FreeBSD 设备。相关软件可参考 [VPN 热点](https://github.com/mygod/vpnhotspot)，使用方法可参考 [通过创建 Wifi 热点来共享 V2ray 代理](https://www.sainnhe.dev/post/v2ray-hotspot/)。

## 加载内核模块

首先需要加载相应的内核模块，以便系统能够识别 USB 网络共享设备（若默认情况下未生效）。内核模块为系统提供了与特定硬件设备通信的能力。

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

### 其他 Android 设备驱动

Android 设备使用通信设备类以太网控制模型/网络控制模型（Communication Device Class Ethernet Control Model/Network Control Model，CDC ECM/NCM）协议，需加载以下内核模块：

```sh
# kldload if_cdce
```

该命令加载 USB CDC ECM/Ethernet 网络驱动，使系统能够识别使用 CDC ECM/NCM 协议的 Android 设备。加载成功后，系统通常会创建类似 `ue0` 的网络接口。

## 持久化驱动加载机制

若需要系统启动时自动加载上述模块，可根据设备类型选择相应条目写入到 `/boot/loader.conf` 文件：

```ini
if_urndis_load="YES"  # 设置系统启动时自动加载 USB RNDIS 网络驱动
if_cdce_load="YES"    # 设置系统启动时自动加载 USB CDC ECM/Ethernet 网络驱动
if_ipheth_load="YES"  # 设置系统启动时自动加载 iPhone/iPad 以太网驱动
```

编辑完成后，保存文件并重启系统以使更改生效。

## 物理连接与网络共享启用

加载所需内核模块后，将 USB 数据线连接到 FreeBSD 系统与移动设备之间，然后在移动设备上开启 USB 网络共享功能。具体开启方式因设备品牌和系统版本而异，通常可在移动设备的“设置”、“网络”或“个人热点”菜单中找到相关选项。请注意，某些设备可能需要先启用 USB 调试（对于 Android 设备）或信任此计算机（对于 iOS 设备）才能正常工作。

## 获取 IP 地址

移动设备开启 USB 网络共享后，FreeBSD 系统会自动创建相应的网络接口，通常接口名称为 `ue0`，可通过 `ifconfig` 命令确认实际接口名称。确认接口名称后，通过 DHCP 为该接口获取 IP 地址：

```sh
# dhclient ue0
```

该命令为 `ue0` 接口发送 DHCP 请求，从移动设备获取 IP 地址、子网掩码、默认网关和 DNS 服务器等网络配置参数。获取成功后，可以使用 `ifconfig ue0` 命令查看分配的 IP 地址。

## 参考文献

- FreeBSD Project. if_urndis -- USB Remote NDIS Ethernet device[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?if_urndis(4)>. USB RNDIS 网络设备驱动手册页，用于 Android USB 网络共享。
- FreeBSD Project. if_cdce -- Communication Device Class Ethernet device[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?if_cdce(4)>. USB CDC Ethernet 设备驱动手册页。
- FreeBSD Project. if_ipheth -- Apple iPhone USB Ethernet device[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?if_ipheth(4)>. iPhone USB 网络共享驱动手册页。
- FreeBSD Project. dhclient -- Dynamic Host Configuration Protocol client[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?dhclient(8)>. DHCP 客户端手册页，描述自动获取 IP 地址配置。
- FreeBSD Project. ifconfig -- configure network interface parameters[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?ifconfig(8)>. 网络接口配置工具手册页。
- FreeBSD Project. loader.conf -- kernel and module configuration[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?loader.conf(5)>. 内核模块加载配置文件格式手册页。
- FreeBSD Project. FreeBSD Handbook, Chapter 32: Advanced Networking[EB/OL]. [2026-04-14]. <https://docs.freebsd.org/en/books/handbook/advanced-networking/>. FreeBSD 手册中关于高级网络配置的指南。

## 课后习题

1. 同时加载 `if_urndis` 和 `if_cdce` 模块，连接两部不同的 Android 手机，观察系统创建的网络接口命名规则，分析 FreeBSD 如何处理多个同类 USB 网络设备的资源分配。

2. 将 USB 网络共享接口 `ue0` 配置为静态 IP 并设置为默认网关，使用另一设备通过该接口上网。

3. 查阅 `if_urndis` 驱动源代码，构建其最小可加载版本，分析为什么 USB 网络共享需要特定的内核模块支持而非作为用户空间程序实现。
