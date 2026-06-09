# 8.1 计算机网络基础

FreeBSD 是理想的互联网或内网服务器操作系统，能在极高负载下提供稳健的网络服务，并高效使用内存，在数千个并发用户进程下保持良好响应时间。

FreeBSD 网络配置涉及多个核心命令和配置文件：

| 命令/文件 | 用途 |
| --------- | ---- |
| `ifconfig` | 配置网络接口参数 |
| `route` | 手动操作网络路由表 |
| **/etc/rc.conf** | 系统启动配置的核心文件，网络接口的持久化配置均存储在此文件中 |
| **/etc/resolv.conf** | 配置 DNS 解析器信息 |
| **/etc/hosts** | 提供本地主机名到 IP 地址的静态映射 |

## 网络模型基础

计算机网络是将地理位置不同、具有独立功能的多台计算机及其外部设备，通过通信线路连接起来的系统。在网络操作系统、网络管理软件及网络通信协议的管理和协调下，该网络实现资源共享和信息传递。

FreeBSD 网络子系统基于 TCP/IP 协议族实现，遵循互联网协议套件的分层架构。

TCP/IP 协议族采用四层模型组织网络功能：

| 层次 | 名称 | 功能说明 |
| ---- | ---- | -------- |
| 第一层 | 网络接口层（Link Layer） | 负责在物理网络介质上发送和接收数据帧，处理硬件地址（MAC 地址）解析。该层对应 FreeBSD 中的网络接口驱动程序和 `ifconfig` 命令管理的配置。以太网帧的发送和接收、地址解析（ARP，Address Resolution Protocol）均在该层完成 |
| 第二层 | 互联网层（Internet Layer） | 负责数据包的路由和转发，核心协议为 IP（Internet Protocol），同时处理逻辑寻址（IP 地址）、分片与重组、路由选择等功能。路由表管理和 `route` 命令操作均属于该层 |
| 第三层 | 传输层（Transport Layer） | 提供端到端的通信服务，主要协议为 TCP（Transmission Control Protocol）和 UDP（User Datagram Protocol）。TCP 提供可靠的面向连接传输，UDP 提供无连接的不可靠传输。FreeBSD 实现了一种多 TCP 栈共存架构，允许系统同时加载多个 TCP 协议栈实现 |
| 第四层 | 应用层（Application Layer） | 包含多种面向用户的网络应用协议，如 HTTP、SSH、DNS、SMTP 等。FreeBSD 通过 Ports 和 pkg 提供了大量网络服务软件 |

### 参考文献

- Kurose J F, Ross K W. 计算机网络：自顶向下方法（原书第 8 版）[M]. 陈鸣,译. 北京: 机械工业出版社, 2022. ISBN: 978-7-111-71236-7.

## 识别网络适配器

FreeBSD 支持多种有线和无线网络适配器。查看所用 FreeBSD 版本的硬件兼容性列表，确认网络适配器是否受支持。

### 通过 pciconf 命令识别网络适配器

要获取系统使用的网络适配器，执行以下命令：

```sh
% pciconf -lv | grep -A1 -B3 network
```

输出示例如下：

```sh
em0@pci0:2:1:0:	class=0x020000 rev=0x01 hdr=0x00 vendor=0x8086 device=0x100f subvendor=0x15ad subdevice=0x0750
    vendor     = 'Intel Corporation'
    device     = '82545EM Gigabit Ethernet Controller (Copper)'
    class      = network
    subclass   = ethernet

iwm0@pci0:3:0:0: class=0x028000 rev=0x00 hdr=0x00 vendor=0x8086 device=0x4237 subvendor=0x8086 subdevice=0x1211
    vendor     = 'Intel Corporation'
    device     = 'PRO/Wireless 5100 AGN [Shiloh] Network Connection'
    class      = network
```

`@` 符号前的文本是控制设备的驱动程序名称。在此示例中，分别是 em(4) 和 iwm(4)。

### 通过 ifconfig 命令识别网络适配器

使用 `ifconfig` 命令可查看系统中的网络接口列表及其状态。输出应类似于以下内容：

```sh
em0: flags=1008843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST,LOWER_UP> metric 0 mtu 1500
	options=4e504bb<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,JUMBO_MTU,VLAN_HWCSUM,LRO,VLAN_HWFILTER,VLAN_HWTSO,RXCSUM_IPV6,TXCSUM_IPV6,HWSTATS,MEXTPG>
	ether 00:0c:29:84:0f:86
	inet 192.168.5.22 netmask 0xffffff00 broadcast 192.168.5.255
	inet6 fe80::20c:29ff:fe84:f86%em0 prefixlen 64 scopeid 0x1
	inet6 240e:341:207:a600:2d60:b653:3a68:8605 prefixlen 64 autoconf pltime 101808 vltime 188208
	media: Ethernet autoselect (1000baseT <full-duplex>)
	status: active
	nd6 options=823<PERFORMNUD,ACCEPT_RTADV,AUTO_LINKLOCAL,STABLEADDR>
lo0: flags=1008049<UP,LOOPBACK,RUNNING,MULTICAST,LOWER_UP> metric 0 mtu 16384
	options=680003<RXCSUM,TXCSUM,LINKSTATE,RXCSUM_IPV6,TXCSUM_IPV6>
	inet 127.0.0.1 netmask 0xff000000
	inet6 ::1 prefixlen 128
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x2
	groups: lo
	nd6 options=21<PERFORMNUD,AUTO_LINKLOCAL>
wlan0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
	options=200001<RXCSUM,RXCSUM_IPV6>
	ether 20:0d:b0:c4:ab:59
	inet 192.168.5.23 netmask 0xffffff00 broadcast 192.168.5.255
	groups: wlan
	ssid test_5G channel 153 (5765 MHz 11a vht/80-) bssid e4:60:4d:97:00:e8
	regdomain FCC country US authmode WPA2/802.11i privacy ON
	deftxkey UNDEF AES-CCM 2:128-bit AES-CCM ucast:128-bit txpower 17
	bmiss 7 mcastrate 6 mgmtrate 6 scanvalid 60 ampdulimit 64k
	ampdudensity 2 shortgi -stbc -uapsd vht vht40 vht80 -vht160 -vht80p80
	wme roaming MANUAL
	parent interface: rtwn0
	media: IEEE 802.11 Wireless Ethernet VHT mode 11ac
	status: associated
	nd6 options=829<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL,STABLEADDR>
```

FreeBSD 采用驱动程序名称后接单元号的方式为网络接口命名。单元号表示适配器在启动时被检测到的顺序，或后续被发现时的顺序。例如，`em0` 是系统中使用 em(4) 驱动程序的第一块网卡，`wlan0` 是使用 rtwn(4) 驱动程序的第一块无线网卡。

该示例显示以下设备：

- `em0`：以太网接口。
- `lo0`：本地回环接口，用于本机内部通信，不属于物理网卡。可用于性能分析、软件测试与本地通信。
- `wlan0`：通用 WiFi 802.11 链路层接口，用于连接无线网络。

  > **技巧**
  >
  > 如果 `ifconfig` 输出中仅显示 `lo0` 接口，则表示系统未识别物理网卡，此时应检查网卡硬件连接和驱动加载状态。可通过 `dmesg | grep ether` 命令查看网卡驱动加载日志。

该示例显示 `em0`、`wlan0` 已启动且运行正常。

关键指示项：

| 指示项 | 说明 |
| ------ | ---- |
| **UP** | 表示接口已被管理员启用（处于 up 状态），当前 `em0` 和 `wlan0` 均已启用 |
| **inet**（IPv4 地址） | 有线接口 `em0` 的地址更新为 `192.168.5.22`；无线接口 `wlan0` 的地址为 `192.168.5.23` |
| **inet6**（IPv6 地址） | `em0` 当前拥有两个 IPv6 地址，分别是链路本地地址 `fe80::20c:29ff:fe84:f86%em0` 和全局动态地址 `240e:341:207:a600:2d60:b653:3a68:8605` |
| **netmask**（子网掩码） | `em0` 和 `wlan0` 的掩码均为 `0xffffff00`，这等同于标准的 `255.255.255.0` |
| **broadcast**（广播地址） | 两个接口当前所在网段的有效广播地址均为 `192.168.5.255` |
| **ether**（MAC 地址） | 有线接口 `em0` 的物理地址是 `00:0c:29:84:0f:86`；无线接口 `wlan0` 的物理地址是 `20:0d:b0:c4:ab:59` |
| **media**（物理媒体） | `em0` 显示为以太网自动选择模式（`Ethernet autoselect (1000baseT <full-duplex>)`）；`wlan0` 显示为无线高速模式（`IEEE 802.11 Wireless Ethernet VHT mode 11ac`） |
| **status**（链接状态） | `em0` 的状态为 `active`，说明网线已插好且载波信号正常；`wlan0` 的状态为 `associated`，说明已成功关联到无线基站（SSID 外部显示为 `test_5G`） |

此外，`wlan0` 的关键指示项如下：

| 指示项 | 说明 |
| ------ | ---- |
| **ssid**（无线网络名称） | 当前连接的 Wi-Fi 名称为 `test_5G` |
| **channel**（工作信道与频率） | 当前工作在 153 信道，频率为 5765 MHz（属于 5GHz 频段），且启用了 80MHz 的频宽（vht/80-） |
| **bssid**（无线路由器 MAC 地址） | 当前所连 Wi-Fi 热点的物理地址是 `e4:60:4d:97:00:e8` |
| **country / regdomain**（国家区域代码与无线监管域） | 当前遵从美国标准（country US）以及美国联邦通信委员会（regdomain FCC）的无线电法律法规 |
| **authmode / privacy**（认证与加密模式） | 认证方式为 WPA2/802.11i（目前主流的安全无线认证标准），且隐私加密已开启（privacy ON），单播与传输密钥采用 AES-CCM (128-bit) |
| **txpower**（发射功率） | 当前无线的发射功率为 17 dBm |

如果 ifconfig(8) 输出类似于以下内容，则表示网络接口待配置：

```sh
em0: flags=1008843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST,LOWER_UP> metric 0 mtu 1500
        options=4e504bb<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,JUMBO_MTU,VLAN_HWCSUM,L
RO,VLAN_HWFILTER,VLAN_HWTSO,RXCSUM_IPV6,TXCSUM_IPV6,HWSTATS,MEXTPG>
        ether 00:0c:29:84:0f:86
        inet6 fe80::20c:29ff:fe84:f86%em0 prefixlen 64 scopeid 0x1
        inet6 240e:341:207:a600:2d60:b653:3a68:8605 prefixlen 64 autoconf pltime 1018
08 vltime 188208
        media: Ethernet autoselect (1000baseT <full-duplex>)
        status: active
        nd6 options=823<PERFORMNUD,ACCEPT_RTADV,AUTO_LINKLOCAL,STABLEADDR>
lo0: flags=1008049<UP,LOOPBACK,RUNNING,MULTICAST,LOWER_UP> metric 0 mtu 16384
        options=680003<RXCSUM,TXCSUM,LINKSTATE,RXCSUM_IPV6,TXCSUM_IPV6>
        inet 127.0.0.1 netmask 0xff000000
        inet6 ::1 prefixlen 128
        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x2
        groups: lo
        nd6 options=21<PERFORMNUD,AUTO_LINKLOCAL>
```

