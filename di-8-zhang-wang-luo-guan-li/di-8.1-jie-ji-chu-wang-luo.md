# 8.1 基础网络

FreeBSD 是理想的互联网或内网服务器操作系统，能在极高负载下提供稳健的网络服务，并高效使用内存，在数千个并发用户进程下保持良好响应时间。

FreeBSD 网络配置涉及多个核心命令和配置文件：

- `ifconfig` 命令用于配置网络接口参数；
- `route` 命令用于手动操作网络路由表；
- **/etc/rc.conf** 是系统启动配置的核心文件，网络接口的持久化配置均存储在此文件中；
- **/etc/resolv.conf** 文件用于配置 DNS 解析器信息；
- **/etc/hosts** 文件提供本地主机名到 IP 地址的静态映射。

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

1. **UP** 表示接口已被管理员启用（处于 up 状态），当前 `em0` 和 `wlan0` 均已启用。
2. **inet**（IPv4 地址）：有线接口 `em0` 的地址更新为 `192.168.5.22`；无线接口 `wlan0` 的地址为 `192.168.5.23`。
3. **inet6**（IPv6 地址）：`em0` 当前拥有两个 IPv6 地址，分别是链路本地地址 `fe80::20c:29ff:fe84:f86%em0` 和全局动态地址 `240e:341:207:a600:2d60:b653:3a68:8605`。
4. **netmask**（子网掩码）：`em0` 和 `wlan0` 的掩码均为 `0xffffff00`，这等同于标准的 `255.255.255.0`。
5. **broadcast**（广播地址）：两个接口当前所在网段的有效广播地址均为 `192.168.5.255`。
6. **ether**（MAC 地址）：有线接口 `em0` 的物理地址是 `00:0c:29:84:0f:86`；无线接口 `wlan0` 的物理地址是 `20:0d:b0:c4:ab:59`。
7. **media**（物理媒体）：`em0` 显示为以太网自动选择模式（`Ethernet autoselect (1000baseT <full-duplex>)`）；`wlan0` 显示为无线高速模式（`IEEE 802.11 Wireless Ethernet VHT mode 11ac`）。
8. **status**（链接状态）：`em0` 的状态为 `active`，说明网线已插好且载波信号正常；`wlan0` 的状态为 `associated`，说明已成功关联到无线基站（SSID 外部显示为 `test_5G`）。

此外，`wlan0` 的关键指示项如下：

1. **ssid**（无线网络名称）：当前连接的 Wi-Fi 名称为 `test_5G`。
2. **channel**（工作信道与频率）：当前工作在 153 信道，频率为 5765 MHz（属于 5GHz 频段），且启用了 80MHz 的频宽（vht/80-）。
3. **bssid**（无线路由器 MAC 地址）：当前所连 Wi-Fi 热点的物理地址是 `e4:60:4d:97:00:e8`。
4. **country / regdomain**（国家区域代码与无线监管域）：当前遵从美国标准（country US）以及美国联邦通信委员会（regdomain FCC）的无线电法律法规。
5. **authmode / privacy**（认证与加密模式）：认证方式为 WPA2/802.11i（目前主流的安全无线认证标准），且隐私加密已开启（privacy ON），单播与传输密钥采用 AES-CCM (128-bit)。
6. **txpower**（发射功率）：当前无线的发射功率为 17 dBm。

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

## 配置 IPv4

### 配置动态 IPv4 地址

如果网络中有 DHCP 服务器，可使用 DHCP 动态获取 IP 地址。FreeBSD 使用 dhclient(8) 作为 DHCP 客户端，dhclient(8) 可自动获取 IP 地址、子网掩码和默认路由器。

> **注意**
>
> dhclient(8) **不支持 DHCPv6**（RFC 3315/RFC 8415），IPv6 动态地址需使用 rtsold(8)（SLAAC）或第三方 DHCPv6 客户端（如 `dhcp6c`）。

要使接口使用 DHCP，执行以下命令：

```sh
# sysrc ifconfig_em0="DHCP"
```

可以手动运行 dhclient(8)：

```sh
# dhclient em0
DHCPREQUEST on em0 to 255.255.255.255 port 67
DHCPACK from 192.168.1.1
bound to 192.168.1.19 -- renewal in 43200 seconds.
```

dhclient(8) 也可在后台启动。后台运行可能影响依赖网络的程序，但多数情况下能加快启动速度。

要在后台执行 dhclient(8)，执行以下命令：

```sh
# sysrc background_dhclient="YES"
```

随后重启网络接口：

```sh
# service netif restart
```

### 配置静态 IPv4 地址

也可在命令行通过 ifconfig(8) 配置网络接口卡，但如果不同时将这些配置添加到 **/etc/rc.conf** 文件，重启后配置将丢失。

可通过以下命令设置 IP 地址：

```sh
# ifconfig em0 inet 192.168.1.150/24
```

要使更改在重启后持久化，执行以下命令：

```sh
# sysrc ifconfig_em0="inet 192.168.1.150 netmask 255.255.255.0"
```

一次性设置默认路由：

```sh
# route add default 192.168.1.1
```

永久添加默认路由器：

```sh
# sysrc defaultrouter="192.168.1.1"
```

将 DNS 服务器地址添加到 **/etc/resolv.conf** 文件：

```ini
nameserver 223.5.5.5   # 指定首选 DNS 服务器为阿里云公共 DNS
nameserver 223.6.6.6   # 指定备用 DNS 服务器为阿里云公共 DNS 备选
```

随后重启网络接口和路由：

```sh
# service netif restart
# service routing restart
```

可使用 ping(8) 测试连接：

```sh
$ ping -c2 www.FreeBSD.org
PING www.FreeBSD.org (198.18.0.7): 56 data bytes
64 bytes from 198.18.0.7: icmp_seq=0 ttl=128 time=0.776 ms
64 bytes from 198.18.0.7: icmp_seq=1 ttl=128 time=0.635 ms

--- www.FreeBSD.org ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 0.635/0.705/0.776/0.071 ms
```

如能正常收到 ICMP 响应报文，表明网络已连通。

## IPv6 配置

IPv6 是 IP 协议的新版本，即 IPv4 的继任者。IPv6 相对于 IPv4 提供了多项优势和新功能：

- 其 128 位地址空间可容纳约 3.4×10^38 个地址，从而解决了 IPv4 地址短缺与耗尽问题。
- 路由器仅在路由表中存储网络聚合地址，通过地址聚合减少路由表条目，这与 IPv4 相比大幅降低了路由器的内存和 CPU 需求。
- 地址自动配置（RFC4862）。
- 以多播取代广播地址。
- 支持 IPsec（IP 安全），但非强制要求（RFC 6434 已将 IPv6 节点对 IPsec 的实现要求由 MUST 调整为 SHOULD，因此成为推荐而非必选）。
- 简化的头部结构。
- 对移动 IP 的支持。
- IPv6 到 IPv4 的过渡机制。

FreeBSD 集成了 [KAME](https://www.kame.net/) 项目 IPv6 参考实现，并附带 IPv6 所需的全部组件。

IPv6 地址有三种不同类型：

- **单播（Unicast）**：发送到单播地址的数据包到达属于该地址的接口。
- **任播（Anycast）**：这些地址在语法上与单播地址无法区分，但指向一组接口。发往任播地址的数据包将到达最近的接口。
- **多播（Multicast）**：这些地址标识一组接口。发往多播地址的数据包将到达属于多播组的所有接口。IPv4 广播地址（通常为 xxx.xxx.xxx.255）在 IPv6 中由多播地址表示。

读取 IPv6 地址时，规范形式表示为 `x:x:x:x:x:x:x:x`，其中每个 x 代表一个 16 位十六进制值。例如 **FEBC:A574:382B:23C1:AA49:4592:4EFE:9982**。

通常，地址会有很长的全零子字符串。`::`（双冒号）可用于替换每个地址中的一个子字符串。此外，每个十六进制值最多可省略三个前导零。例如，**fe80::1** 对应规范形式 **fe80:0000:0000:0000:0000:0000:0000:0001**。

一些 IPv6 地址是保留的：

| IPv6 地址 | 描述 | 说明 |
| --------- | ---- | ---- |
| **::/128** | 未指定地址 | 等同于 IPv4 中的 **0.0.0.0** |
| **::1/128** | 回环地址 | 等同于 IPv4 中的 **127.0.0.1** |
| **::ffff:0.0.0.0/96** | IPv4 映射的 IPv6 地址 | 低 32 位是 IPv4 地址 |
| **fe80::/10** | 链路本地单播 | 等同于 IPv4 中的 **169.254.0.0/16** |
| **fc00::/7** | 唯一本地 | 仅在协作站点集合内可路由 |
| **ff00::/8** | 多播 | — |
| **2000::/3** | 全局单播 | 所有全局单播地址从此池分配 |
| **2001:db8::/32** | 文档用途 | 用于文档中的 IPv6 地址前缀 |

### 配置动态 IPv6 地址

要使用 SLAAC 动态配置接口的 IPv6 地址：

```sh
# sysrc ifconfig_em0_ipv6="inet6 accept_rtadv"
# sysrc rtsold_enable="YES"
```

注意，启用 IPv6 数据包转发（即 `ipv6_gateway_enable=YES`）后，除非将 `net.inet6.ip6.rfc6204w3` sysctl(8) 变量设置为 1，否则系统不会配置 SLAAC 地址。

### 配置静态 IPv6 地址

要将 FreeBSD 系统配置为具有静态 IPv6 地址的 IPv6 客户端，需要设置 IPv6 地址：

```sh
# sysrc ifconfig_em0_ipv6="inet6 2001:db8:4672:6565:2026:5043:2d42:5344 prefixlen 64"
```

要分配默认路由器：

```sh
# sysrc ipv6_defaultrouter="2001:db8:4672:6565::1"
```

### 参考文献

- Li Q, Jinmei T, Shima K. IPv6 详解：卷 1，核心协议实现[M]. 陈涓，赵振平，译. 北京：人民邮电出版社，2009：846. ISBN: 978-7-115-18950-9 (英文影印版本 ISBN: 978-7-115-19551-7). 详解 IPv6 核心协议实现，基于 FreeBSD KAME 项目代码分析。
- Li Q, Jinmei T, Shima K. IPv6 详解：卷 2，高级协议实现[M]. 王嘉祯，等，译. 北京：人民邮电出版社，2009：869. ISBN: 978-7-115-20891-0 (英文影印版本 ISBN: 978-7-115-19519-7). 详解 IPv6 高级协议与扩展机制，包含移动 IPv6 等关键技术。

## 主机名

主机名代表主机在网络上的完全限定域名（FQDN，Fully Qualified Domain Name）。

检查当前主机名：

```sh
$ hostname
ykla
```

临时更改主机名：

```sh
root@ykla:/home/ykla # hostname f	# 将主机名由 ykla 临时修改为 f
root@f:/home/ykla #
```

更改主机名并使其在重启后持久化：

```sh
# sysrc hostname="f"
```

## DNS 配置详解

可将 DNS 类比作电话簿，其中 IP 地址与主机名相互对应。除非 **/etc/nsswitch.conf** 文件中另有说明，FreeBSD 将首先查看 **/etc/hosts** 文件中的地址，随后查看 **/etc/resolv.conf** 文件中的 DNS 信息。

相关文件结构：

```sh
/etc/
├── rc.conf             # 系统启动配置文件
├── resolv.conf          # DNS 解析服务器配置文件
└── resolvconf.conf      # resolvconf 服务配置文件
```

### 本地地址 hosts 文件

**/etc/hosts** 文件是一个简单的文本数据库，提供主机名到 IP 地址的映射。通过 LAN 连接的本地计算机条目可添加到此文件中，用于简单的主机名解析，无须设置 DNS 服务器。此外，**/etc/hosts** 文件可用于提供 Internet 名称的本地记录，减少对外部 DNS 服务器的查询需求。

例如，在本地环境中有 www/gitlab-ce 的本地实例，可以将如下行添加到 **/etc/hosts** 文件：

```ini
192.168.1.150 git.example.com git
```

### 配置 DNS 名称服务器

FreeBSD 系统访问 Internet 域名系统（DNS）的方式由 resolv.conf(5) 控制。**/etc/resolv.conf** 文件中最常见的条目是：

- **nameserver**：解析器应查询的名称服务器的 IP 地址。服务器按列出的顺序查询，最多三个。
- **search**：主机名查找的搜索列表。通常由本地主机名的域确定。
- **domain**：本地域名。

典型的 **/etc/resolv.conf** 文件如下：

```ini
search example.com
nameserver 223.5.5.5
nameserver 223.6.6.6
```

search 和 domain 选项只能使用其中一个。使用 DHCP 时，dhclient(8) 通常会用从 DHCP 服务器接收的信息重写 **/etc/resolv.conf** 文件。

由于动态主机配置协议（Dynamic Host Configuration Protocol，DHCP）客户端在获取网络配置时会通过 resolvconf 服务重写 /etc/resolv.conf，手动编辑该文件后，重启系统时可能被重置。

如果需要使用手动配置的 DNS 服务器而不希望系统自动更新覆盖，可禁用 resolvconf 服务。编辑 **/etc/resolvconf.conf** 文件（如不存在则创建），写入 `resolvconf=NO` 一行，该配置将禁用系统对 DNS 配置文件的自动更新。

### 参考文献

- FreeBSD Project. resolvconf[EB/OL]. [2026-03-26]. <https://man.freebsd.org/cgi/man.cgi?query=resolvconf&sektion=8>. man 手册，提供 resolvconf 工具的完整技术文档，为 DNS 配置管理提供重要参考。
- FreeBSD Forums. **8.8.8.8** or **1.1.1.1** if set in etc resolv conf doesn't stay as an entry in the file after a network restart[EB/OL]. [2026-03-26]. <https://forums.freebsd.org/threads/8-8-8-8-or-1-1-1-1-if-set-in-etc-resolv-conf-doesnt-stay-as-an-entry-in-the-file-after-a-network-restart.85951/>. 实际案例分析，提供防止覆写 DNS 配置的解决方案。

## 网络故障排除

首先检查以下基本要素：

- 电源连接是否正常？
- 路由器是否正常工作？
- 宽带或网络费用是否缴纳？
- 是否是区域性大规模网络中断事件？
- 计算机的时间是否正确？
- 网线是否插好？
- 网络服务是否正确配置？
- 防火墙是否正确配置？
- 网卡是否受 FreeBSD 支持？

如果网卡工作正常但性能不佳，可参阅 tuning(7)。不正确的网络设置可能导致连接缓慢，应同时检查网络配置。

“No route to host”消息表示系统无法将数据包路由到目标主机。这通常是因为未指定默认路由或网线未插入。可使用 `route get <目标地址>` 命令查看系统对特定目标的路由决策，再检查 `netstat -rn` 的输出，确保有到主机的有效路由。

“ping: sendto: Permission denied”错误消息通常由防火墙配置错误引起。如果直接加载了 IPFW 防火墙模块但未配置任何规则，IPFW 的默认规则 65535 会拒绝所有流量，甚至是 ping(8)。但通过 rc.conf 标准方式启用防火墙时，IPFW 默认 `firewall_type="open"` 会放行所有流量；PF 和 IPFilter 无规则时默认放行。

## 附录：/etc/rc.conf 网络配置示例

> **注意**：
>
> 修改 **/etc/rc.conf** 文件后，需重启系统或依次运行命令 `service netif restart` 与 `service routing restart` 来应用网络更改。

主机名（不能为空，否则无法使用 Xorg）：

```ini
hostname="ykla"
```

### 动态 DHCP 方式

动态 DHCP 方式：使网卡 igc0 使用 DHCP：

```ini
ifconfig_igc0="DHCP"
```

### 静态 IP 方式

静态 IP 方式：将网卡 igc0 的 IPv4 设置为 **192.168.5.77**，子网掩码为 **255.255.255.0**：

```ini
ifconfig_igc0="inet 192.168.5.77 netmask 255.255.255.0"  # 
```

默认网关/默认路由，通常为路由器 IP 地址：

```ini
defaultrouter="192.168.5.1"
```

为网卡 igc0 设置别名 IPv4 **192.168.5.12**，子网掩码为 **255.255.255.0** 从而拥有额外的 IPv4 地址：

```ini
ifconfig_igc0_alias0="inet 192.168.5.12 netmask 255.255.255.0"
```

> **注意**：
>
> 如果别名地址与主地址位于同一子网，必须将子网掩码设为 255.255.255.255（0xffffffff），否则会产生重复路由错误。不同子网的别名则使用该子网正常的子网掩码。

静态路由：

```ini
static_routes="static1 static2" # ①
```

① 在 **/etc/rc.conf** 文件中，如果需要一次性写入多个配置项，只能使用 `ABC_XYZ="xxx yyy ccc ddd"` 这种格式。如果写成以下形式是 **错误的**：

```ini
ABC_XYZ="xxx" # 第一行
ABC_XYZ="yyy"
ABC_XYZ="ccc"
ABC_XYZ="ddd"
```

因为在这种形式下，后续的 `ABC_XYZ` 配置行会覆盖前一行，因此只有最后一行会生效。

示例：如需访问 **192.168.50.0/24** 地址块（可用主机 IP 从 **192.168.50.1** 到 **192.168.50.254**），将数据包发送给 **192.168.1.1**，由其转发：

```ini
route_static1="-net 192.168.50.0/24 192.168.1.1"
```

示例：如果需访问网络 **10.88.200.0/24** 地址块（可用主机 IP 从 **10.88.200.1** 到 **10.88.200.254**），就将数据包发送给 10.10.10.254，由它来转发：

```ini
route_static2="-net 10.88.200.0/24 10.10.10.254"
```

## 查看网卡速率

如需实时监控网络接口的流量统计信息，可使用 `systat` 工具的网络接口视图。该命令以指定的刷新间隔显示各网络接口的接收和发送流量数据：

```sh
# systat -ifstat 2
```

其中 `-ifstat` 参数指定显示网络接口信息，数字 2 表示刷新间隔为 2 秒。

## 查看 FreeBSD 下载流量（bwm-ng）

如需查看更详细的网络流量统计，可安装 `bwm-ng` 工具，该工具提供多种流量显示格式和交互功能：

```sh
# pkg install bwm-ng  # 安装 bwm-ng
# bwm-ng
  bwm-ng v0.6.3 (probing every 0.500s), press 'h' for help
  input: getifaddrs type: rate
  /         iface                   Rx                   Tx                Total
  ==============================================================================
              em0:           2.04 MB/s            6.03 KB/s            2.05 MB/s
              lo0:           0.00  B/s            0.00  B/s            0.00  B/s
        vm-public:           2.04 MB/s            2.05 MB/s            4.09 MB/s
             tap0:           5.49 KB/s            2.04 MB/s            2.04 MB/s
  ------------------------------------------------------------------------------
            total:           4.09 MB/s            4.09 MB/s            8.18 MB/s
```

按字母 d 可切换流量显示格式，按 h 可查阅更多使用方法。

## 课后习题

1. 在 FreeBSD 系统上配置双静态 IP 地址，分别设置不同的 DNS 服务器，使用 `dig` 命令验证每个 DNS 服务器的解析行为，分析 **/etc/resolv.conf** 中多 DNS 服务器条目的查询顺序与容错机制。
2. 修改网络接口的 MTU（Maximum Transmission Unit）值为 9000（巨型帧），使用 `ping` 测试连通性，记录 MTU 变化对大包传输的影响，分析巨型帧在局域网与广域网中的适用场景。
3. 禁用 `resolvconf` 服务，手动修改 **/etc/resolv.conf** 文件并重启网络服务，验证配置是否持久化，分析 `resolvconf` 对 DNS 配置动态管理的机制。
