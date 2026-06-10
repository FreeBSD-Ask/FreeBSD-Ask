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
| 第一层 | 网络接口层（Link Layer） | 负责在物理网络介质上发送和接收数据帧，处理硬件地址（MAC 地址）解析。该层对应 FreeBSD 中的网络接口驱动程序，其配置由 `ifconfig` 命令管理。以太网帧的发送和接收、地址解析（ARP，Address Resolution Protocol）均在该层完成 |
| 第二层 | 互联网层（Internet Layer） | 负责数据包的路由和转发，核心协议为 IP（Internet Protocol），同时处理逻辑寻址（IP 地址）、分片与重组、路由选择等功能。路由表管理和 `route` 命令操作均属于该层 |
| 第三层 | 传输层（Transport Layer） | 提供端到端的通信服务，主要协议为 TCP（Transmission Control Protocol）和 UDP（User Datagram Protocol）。TCP 提供可靠的面向连接传输，UDP 提供无连接的不可靠传输。FreeBSD 实现了多 TCP 栈共存架构，允许系统同时加载多个 TCP 协议栈实现 |
| 第四层 | 应用层（Application Layer） | 包含多种面向用户的网络应用协议，如 HTTP、SSH、DNS、SMTP 等。FreeBSD 通过 Ports 和 pkg 提供了大量网络服务软件 |

### 参考文献

- Kurose J F, Ross K W. 计算机网络：自顶向下方法（原书第 8 版）[M]. 陈鸣，译. 北京: 机械工业出版社, 2022. ISBN: 978-7-111-71236-7.

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

`@` 符号前的文本是控制该设备的驱动程序名称。在此示例中，分别是 em(4) 和 iwm(4)。

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

FreeBSD 采用驱动程序名称后接单元号的方式为网络接口命名。单元号表示适配器在启动时被检测到的顺序，或后续被检测到时的顺序。例如，`em0` 是系统中使用 em(4) 驱动程序的第一块网卡，`wlan0` 是使用 rtwn(4) 驱动创建的第一个无线接口。

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
| **inet**（IPv4 地址） | 有线接口 `em0` 的地址更新为 **192.168.5.22**；无线接口 `wlan0` 的地址为 **192.168.5.23** |
| **inet6**（IPv6 地址） | `em0` 当前拥有两个 IPv6 地址，分别是链路本地地址 `fe80::20c:29ff:fe84:f86%em0` 和全局动态地址 `240e:341:207:a600:2d60:b653:3a68:8605` |
| **netmask**（子网掩码） | `em0` 和 `wlan0` 的掩码均为 `0xffffff00`，这等同于标准的 **255.255.255.0** |
| **broadcast**（广播地址） | 两个接口当前所在网段的有效广播地址均为 **192.168.5.255** |
| **ether**（MAC 地址） | 有线接口 `em0` 的物理地址是 `00:0c:29:84:0f:86`；无线接口 `wlan0` 的物理地址是 `20:0d:b0:c4:ab:59` |
| **media**（物理媒体） | `em0` 显示为以太网自动选择模式（`Ethernet autoselect (1000baseT <full-duplex>)`）；`wlan0` 显示为无线高速模式（`IEEE 802.11 Wireless Ethernet VHT mode 11ac`） |
| **status**（链接状态） | `em0` 的状态为 `active`，说明网线已连接且载波信号正常；`wlan0` 的状态为 `associated`，说明已成功关联到无线基站（SSID 外部显示为 `test_5G`） |

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

## 网关和路由

**路由** 是系统寻找通往其他系统的网络路径的机制。每条路由由一对地址定义，分别表示“目标”和“网关”。路由表明：连接指定目标时，应经由指定网关发送数据包。目标分为三种类型：单台主机、子网和“默认”。“默认路由”在其他路由均不适用时生效。网关同样分为三种类型：单台主机、接口（也称为链路）和以太网硬件（MAC）地址。已知路由存储于路由表中。

### 路由基础

使用 netstat(1) 可查看 FreeBSD 系统的路由表。添加 `-n` 选项可避免反向 DNS 解析延迟，这在排查网络问题时尤为重要：

```sh
$ netstat -rn
Routing tables

Internet:	# IPv4
# 路径				网关			  标志			接口  过期时间
Destination        Gateway            Flags         Netif Expire
default            192.168.179.2      UGS             em0   # 默认路由，通过 em0 接口
localhost          link#3             UH              lo0   # 回环地址，使用 lo0 接口
192.168.5.0/24     link#2             U               em1   # 192.168.5.0/24
192.168.5.16       link#3             UHS             lo0   # 192.168.5.16
192.168.179.0/24   link#1             U               em0   # 192.168.179.0/24 子网
192.168.179.128    link#3             UHS             lo0   # 本地主机地址 192.168.179.128

Internet6:	# IPv6
Destination        Gateway            Flags         Netif Expire
::/96              link#3             URS             lo0   # IPv4 兼容 IPv6 地址块（已废弃，RFC 4291）
default            fe80::5%em1        UG              em1   # 默认 IPv6 路由，下一跳是链路本地地址 fe80::5，标志 UG 表示可达且为网关
localhost          link#3             UHS             lo0   # IPv6 本地回环地址 ::1
::ffff:0.0.0.0/96  link#3             URS             lo0   # IPv4 映射 IPv6 地址
240e:341:22b:ae00: link#2             U               em1   # 全球单播地址
240e:341:22b:ae00: link#3             UHS             lo0   # 本地主机路由
fe80::%lo0/10      link#3             URS             lo0   # 链路本地 IPv6 网络
fe80::%em0/64      link#1             U               em0   # em0 接口链路本地 IPv6 地址
fe80::20c:29ff:fe8 link#3             UHS             lo0   # 静态主机路由
fe80::%em1/64      link#2             U               em1   # em1 接口链路本地 IPv6 地址
fe80::20c:29ff:fe8 link#3             UHS             lo0   # 静态主机路由（与前条 fe80::20c:29ff:fe8 条目重复，属路由表缓存正常现象）
fe80::%lo0/64      link#3             U               lo0   # lo0 接口链路本地子网
fe80::1%lo0        link#3             UHS             lo0   # lo0 单一本地主机链路本地地址，静态主机路由
ff02::/16          link#3             URS             lo0   # IPv6 多播地址
```

该示例的条目如下：

- **default**：
  默认路由。本地系统需连接远程主机时，检查路由表以确定是否存在已知路径。如果远程主机匹配表中某条目，系统即检查能否通过该条目指定的接口完成连接。
  默认路由在无更具体前缀匹配时采用，不受其他路径状态的影响。对于局域网中的主机，默认路由的 `Gateway` 字段应设为可直接连接互联网的系统。读取该条目时，应确认 `Flags` 列指示网关可达（`UG`）。

  对于充当对外网关的主机，其默认路由指向与互联网服务提供商（ISP）相连的网关。

  IPv4 网络中，默认网关为 **192.168.179.2**，标记为 UGS（Up、Gateway、Static）。所有发往未知外部网络（如互联网）的 IPv4 流量均经 `em0` 接口发送至该路由器转发。

  IPv6 部分中，默认路由以链路本地地址 **fe80::5%em1** 指定下一跳，该下一跳通常为 ISP 提供的路由器。标志为 UG，所有未匹配的 IPv6 流量经 em1 接口发出。链路本地地址为 IPv6 特性，仅用于本地链路通信，不等同于公网可达地址。

  该机器具备双栈网络能力，IPv4 和 IPv6 出口分别依赖不同网卡（em0 和 em1）。

- **localhost**：第二条路由。`Netif` 列中为 `localhost` 指定的接口是 **lo0**，也称为回环设备。所有发往该目标的流量均保留于本机内部，不通过网络发送。

- **子网**

  IPv4 路由表显示该设备同时接入两个局域网：**192.168.5.0/24** 和 **192.168.179.0/24**。对应网关分别为 `link#2` 和 `link#1`，标志仅含 U（Up），表明二者均为“直连网络”。该机器与这两个网段内其他设备（如 `192.168.5.x` 范围内的计算机）通信时，数据包无须经由路由器，而是通过 ARP 解析目标 MAC 地址后，直接经 em1 和 em0 接口以链路层单播帧发送。

- **全球单播地址**

  IPv6 路由（Internet6）中，以 **240e:341:22b:ae00:** 为首的条目绑定于 em1 接口。该地址属于全球单播地址（Global Unicast Address），通常由运营商（如中国电信，以 240e 开头）分配，理论上可在互联网中路由，但实际访问能力取决于防护策略与服务配置。

- **标志**

  `Flags` 列展示各路由的属性。下表汇总了常见的路由表标志及其含义。

  **常见的路由表标志**

  | 标志 | 目的 |
  | ---- | ---- |
  | U | 路由可用 |
  | H | 路由目标是单个主机 |
  | G | 将此目的地的任何流量转发到此网关，由网关决定如何进一步转发 |
  | S | 该路由是静态配置的 |
  | M | 路由已被重定向修改 |
  | B | 黑洞路由：静默丢弃匹配的数据包 |
  | D | 由重定向动态创建 |
  | L | 链路层路由，涉及以太网硬件地址引用 |
  | R | 拒绝路由：目标主机或网络不可达 |
  | b | 路由表示广播地址 |

### 跟踪路由信息

地址空间分配给某网络后，服务提供商会配置自身路由表，确保所有流量均发往该站点链路。外部站点如何确定应将数据包发往该网络的 ISP？

互联网通过全球路由系统跟踪所有已分配地址空间，并界定其与互联网主干网（承载互联网流量的核心线路）的连接节点。每台主干路由器均保存一份主路由表，将特定网络的流量指向对应的主干运营商，再经由一系列服务提供商逐级传递至目标网络。

服务提供商必须向主干站点通告自身的连接点，使流量能够到达该网络。该过程称为路由传播。

路由传播偶尔出现故障，导致部分站点无法连通。此时，查找路由断点的常用命令是 `traceroute`（IPv6 使用 `traceroute6`），在 `ping` 失败时尤为有用。

使用 `traceroute` 必须提供远程主机的地址。输出将显示路径上的网关主机，最终抵达目标主机或因连接中断而终止。

以下为对 `freebsd.org` 域名的 IPv6 路径跟踪：

```sh
$ traceroute6 freebsd.org
traceroute6 to freebsd.org (2610:1c1:1:606c::50:15) from 240e:341:22b:ae00:f534:e5cb:2367:c033, 64 hops max, 28 byte packets
 1  * * *
 2  240e:c::201 (240e:c::201)  6.427 ms  5.508 ms  6.578 ms
 3  *
    240e:c:1:20e::2 (240e:c:1:20e::2)  6.229 ms  5.737 ms
 4  * * *
 5  240e::1:11:46:5c02 (240e::1:11:46:5c02)  10.729 ms * *
 6  240e::f:1:6601:503 (240e::f:1:6601:503)  13.093 ms *  11.332 ms
 7  240e:0:a::c9:360d (240e:0:a::c9:360d)  15.618 ms
    240e:0:a::c9:3649 (240e:0:a::c9:3649)  16.334 ms *
 8  * * *
 9  *
    zayo.ae10.mpr4.sjc7.us.zip.zayo.com (2001:438:ffff::407e:2f9)  180.002 ms  179.112 ms
10  ae34.mpr1.ewr4.us.zip.zayo.com (2001:438:ffff::407d:1455)  244.026 ms  243.263 ms *
11  2001:438:fffe::24ba (2001:438:fffe::24ba)  246.736 ms *  245.756 ms
12  cs89-cs80.nyinternet.net (2610:1c1::2502)  218.700 ms  218.396 ms  217.715 ms
13  2610:1c1::803 (2610:1c1::803)  228.099 ms  227.280 ms  226.003 ms
14  wfe0.nyi.freebsd.org (2610:1c1:1:606c::50:15)  214.724 ms  216.682 ms *
```

详细说明：

| 序号 | 节点 | 说明 |
| ---- | ---- | ---- |
| 1 | `*` | 本地网络第一跳无响应 |
| 2 | **240e:c::201 (240e:c::201)** | 运营商接入网关 |
| 3、4 | `*` | 骨干网前级节点无响应，可能丢弃了 ICMPv6 |
| 5 | **240e::1:11:46:5c02 (240e::1:11:46:5c02)** | 中国电信核心骨干路由器，国内长途汇聚节点 |
| 6 | **240e::f:1:6601:503 (240e::f:1:6601:503)** | 中国电信国际出口前的骨干节点，部分探测包丢失 |
| 7 | **240e:0:a::c9:360d (240e:0:a::c9:360d), 240e:0:a::c9:3649 (240e:0:a::c9:3649)** | 中国电信向海外出口的跨洲骨干路由器 |
| 8 | `*` | 无响应节点，可能丢弃了 ICMPv6 |
| 9 | **zayo.ae10.mpr4.sjc7.us.zip.zayo.com (2001:438:ffff::407e:2f9)** | Zayo 美国加州圣何塞骨干网（Zip Zayo）入口节点 |
| 10 | **ae34.mpr1.ewr4.us.zip.zayo.com (2001:438:ffff::407d:1455)** | Zayo 美国纽瓦克骨干网节点，负责东海岸流量汇聚 |
| 11 | **2001:438:fffe::24ba (2001:438:fffe::24ba)** | Zayo 美国骨干网最后一跳，接近 NYInternet 入口 |
| 12 | **cs89-cs80.nyinternet.net (2610:1c1::2502)** | NYInternet 美国运营商核心路由器，接入 freebsd.org 网络 |
| 13 | **2610:1c1::803 (2610:1c1::803)** | NYInternet 核心骨干节点，负责 freebsd.org 服务器的流量分发 |
| 14 | **wfe0.nyi.freebsd.org (2610:1c1:1:606c::50:15)** | freebsd.org 服务器终端节点，traceroute6 的目标 |
