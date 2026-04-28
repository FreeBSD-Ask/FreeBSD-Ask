# 6.1 网络基础配置

FreeBSD 是一款理想的互联网或内网服务器操作系统，能够在最重的负载下提供稳健的网络服务，并高效使用内存以维持数千个并发用户进程的良好响应时间。

FreeBSD 网络配置涉及多个核心命令和配置文件：

- `ifconfig` 命令用于配置网络接口参数；
- `route` 命令用于手动操作网络路由表；
- `/etc/rc.conf` 是系统启动配置的核心文件，网络接口的持久化配置均存储于此；
- `/etc/resolv.conf` 文件用于配置 DNS 解析器信息；
- `/etc/hosts` 文件提供本地主机名到 IP 地址的静态映射。

## 网络模型基础

计算机网络是将地理位置不同、具有独立功能的多台计算机及其外部设备，通过通信线路连接起来，在网络操作系统、网络管理软件及网络通信协议的管理和协调下，实现资源共享和信息传递的系统。

FreeBSD 的网络子系统基于 TCP/IP 协议族实现，该协议族遵循互联网协议套件的分层架构。理解网络分层模型有助于把握 FreeBSD 网络配置的内在逻辑。

TCP/IP 协议族采用四层模型组织网络功能：

- **网络接口层（Link Layer）**：负责在物理网络介质上发送和接收数据帧，处理硬件地址（MAC 地址）解析。在 FreeBSD 中，该层对应网络接口驱动程序和 `ifconfig` 命令管理的配置。以太网帧的发送与接收、ARP（Address Resolution Protocol）地址解析均在此层完成。
- **互联网层（Internet Layer）**：负责数据包的路由和转发，核心协议为 IP（Internet Protocol）。该层处理逻辑寻址（IP 地址）、分片与重组、路由选择等功能。在 FreeBSD 中，路由表管理和 `route` 命令操作属于此层范畴。
- **传输层（Transport Layer）**：提供端到端的通信服务，主要协议为 TCP（Transmission Control Protocol）和 UDP（User Datagram Protocol）。TCP 提供可靠的面向连接的传输，UDP 提供无连接的不可靠传输。FreeBSD 创新性地实现了多 TCP 栈共存架构，允许系统同时加载多个 TCP 协议栈实现。
- **应用层（Application Layer）**：包含各种面向用户的网络应用协议，如 HTTP、SSH、DNS、SMTP 等。FreeBSD 通过 Ports 和 pkg 提供了丰富的网络服务软件。

### 参考文献

- Kurose J F, Ross K W. 计算机网络：自顶向下方法（原书第 8 版）[M]. 陈鸣，译. 北京：机械工业出版社，2022. ISBN 978-7-111-71236-7.

## 识别网络适配器

FreeBSD 支持多种有线和无线网络适配器。查看所用 FreeBSD 版本的硬件兼容性列表，确认网络适配器是否受支持。

### 识别网络适配器方法一

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

### 识别网络适配器方法二

使用 `ifconfig` 命令可查看系统中的网络接口列表及其状态。

示例输出：

```sh
# ifconfig
genet0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
	options=68000b<RXCSUM,TXCSUM,VLAN_MTU,LINKSTATE,RXCSUM_IPV6,TXCSUM_IPV6>
	ether dc:a6:1a:2e:f4:4f
	inet 192.168.123.157 netmask 0xffffff00 broadcast 192.168.123.255
	media: Ethernet autoselect (1000baseT <full-duplex>)
	status: active
	nd6 options=29<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL>
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384
	options=680003<RXCSUM,TXCSUM,LINKSTATE,RXCSUM_IPV6,TXCSUM_IPV6>
	inet6 ::1 prefixlen 128
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x2
	inet 127.0.0.1 netmask 0xff000000
	groups: lo
	nd6 options=21<PERFORMNUD,AUTO_LINKLOCAL>
```

`lo0` 是本地回环接口，用于本机内部通信，不属于物理网卡。如 `ifconfig` 输出中仅包含 `lo0` 接口，说明系统未识别物理网卡，此时需检查网卡硬件连接和驱动加载情况。可通过 `dmesg | grep ether` 命令查看网卡驱动加载日志。

## 配置 IPv4

### 配置动态 IPv4 地址

如果网络有 DHCP 服务器，配置网络接口使用 DHCP 较为简便。FreeBSD 使用 dhclient(8) 作为 DHCP 客户端。dhclient(8) 将自动提供 IP 地址、子网掩码和默认路由器。

>**注意**
>
> dhclient(8) **不支持 DHCPv6**（RFC 3315/RFC 8415），IPv6 动态地址需使用 `rtsold(8)`（SLAAC）或第三方 DHCPv6 客户端（如 `dhcp6c`）。

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

可在后台启动 dhclient(8) 客户端。这可能导致依赖网络的程序出现问题，但在许多情况下可提供更快的启动速度。

要在后台执行 dhclient(8)，执行以下命令：

```sh
# sysrc background_dhclient="YES"
```

然后重启网络接口：

```sh
# service netif restart
```

### 配置静态 IPv4 地址

也可在命令行通过 ifconfig(8) 执行网络接口卡配置。然而，除非同时将这些配置添加到 `/etc/rc.conf` 文件，否则重启后配置将丢失。

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

永久性添加默认路由器：

```sh
# sysrc defaultrouter="192.168.1.1"
```

将 DNS 记录添加到 `/etc/resolv.conf` 文件：

```ini
nameserver 223.5.5.5   # 指定首选 DNS 服务器为阿里云公共 DNS
nameserver 223.6.6.6   # 指定备用 DNS 服务器为阿里云公共 DNS 备选
```

然后重启网络接口和路由：

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

如能正常收到 ICMP 响应报文，则说明网络已连通。

>**注意**
>
>Jail 内默认不允许使用 ping（需设置 sysctl `allow.raw_sockets`）。

## IPv6 配置

IPv6 是 IP 协议的新版本，也称为 IPv4 的后继。IPv6 相对于 IPv4 提供了多项优势和新功能：

- 其 128 位地址空间允许 340,282,366,920,938,463,463,374,607,431,768,211,456 个地址。这解决了 IPv4 地址短缺和最终的 IPv4 地址耗尽问题。
- 路由器仅在路由表中存储网络聚合地址，从而将路由表的平均空间减少到 8192 个条目。
- 地址自动配置（RFC4862）。
- 强制多播地址。
- 内置 IPsec（IP 安全）。
- 简化的头部结构。
- 对移动 IP 的支持。
- IPv6 到 IPv4 的过渡机制。

FreeBSD 包括 KAME 项目 IPv6 参考实现，并附带 IPv6 所需的全部组件。

IPv6 地址有三种不同类型：

- **单播（Unicast）**：发送到单播地址的数据包到达属于该地址的接口。
- **任播（Anycast）**：这些地址在语法上与单播地址无法区分，但它们寻址一组接口。发往任播地址的数据包将到达最近的接口。
- **多播（Multicast）**：这些地址标识一组接口。发往多播地址的数据包将到达属于多播组的所有接口。IPv4 广播地址（通常为 xxx.xxx.xxx.255）在 IPv6 中由多播地址表示。

读取 IPv6 地址时，规范形式表示为 `x:x:x:x:x:x:x:x`，其中每个 x 代表一个 16 位十六进制值。例如 `FEBC:A574:382B:23C1:AA49:4592:4EFE:9982`。

通常，地址会有很长的全零子字符串。`::`（双冒号）可用于替换每个地址中的一个子字符串。此外，每个十六进制值最多可省略三个前导零。例如，`fe80::1` 对应规范形式 `fe80:0000:0000:0000:0000:0000:0000:0001`。

一些 IPv6 地址是保留的：

| IPv6 地址 | 描述 | 说明 |
| --------- | ---- | ---- |
| `::/128` | 未指定地址 | 等同于 IPv4 中的 0.0.0.0 |
| `::1/128` | 回环地址 | 等同于 IPv4 中的 127.0.0.1 |
| `::ffff:0.0.0.0/96` | IPv4 映射的 IPv6 地址 | 低 32 位是 IPv4 地址 |
| `fe80::/10` | 链路本地单播 | 等同于 IPv4 中的 169.254.0.0/16 |
| `fc00::/7` | 唯一本地 | 仅在协作站点集合内可路由 |
| `ff00::/8` | 多播 | — |
| `2000::/3` | 全局单播 | 所有全局单播地址从此池分配 |
| `2001:db8::/32` | 文档用途 | 用于文档中的 IPv6 地址前缀 |

### 配置动态 IPv6 地址

要使用 SLAAC 动态配置接口的 IPv6 地址：

```sh
# sysrc ifconfig_em0_ipv6="inet6 accept_rtadv"
# sysrc rtsold_enable="YES"
```

注意，当启用 IPv6 数据包转发（即 `ipv6_gateway_enable=YES`）时，除非将 `net.inet6.ip6.rfc6204w3` sysctl(8) 变量设置为 1，否则系统不会配置 SLAAC 地址。

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

主机名代表主机在网络上的完全限定域名（FQDN）。

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

可将 DNS 理解为电话簿，其中 IP 地址与主机名相互对应。除非 `/etc/nsswitch.conf` 文件中另有说明，FreeBSD 将首先查看 `/etc/hosts` 文件中的地址，然后查看 `/etc/resolv.conf` 文件中的 DNS 信息。

相关文件结构：

```sh
/etc/
├── rc.conf             # 系统启动配置文件
├── resolv.conf          # DNS 解析服务器配置文件
└── resolvconf.conf      # resolvconf 服务配置文件
```

### 本地地址 hosts 文件

`/etc/hosts` 文件是一个简单的文本数据库，提供主机名到 IP 地址的映射。通过 LAN 连接的本地计算机条目可添加至此文件中，用于简单的命名目的，而无须设置 DNS 服务器。此外，`/etc/hosts` 文件可用于提供 Internet 名称的本地记录，减少对外部 DNS 服务器的查询需求。

例如，在本地环境中有 www/gitlab-ce 的本地实例，可以如下行添加到 `/etc/hosts` 文件：

```ini
192.168.1.150 git.example.com git
```

### 配置 DNS 名称服务器

FreeBSD 系统访问 Internet 域名系统（DNS）的方式由 resolv.conf(5) 控制。`/etc/resolv.conf` 文件中最常见的条目是：

- **nameserver**：解析器应查询的名称服务器的 IP 地址。服务器按列出的顺序查询，最多三个。
- **search**：主机名查找的搜索列表。通常由本地主机名的域确定。
- **domain**：本地域名。

典型的 `/etc/resolv.conf` 文件如下：

```ini
search example.com
nameserver 223.5.5.5
nameserver 223.6.6.6
```

search 和 domain 选项只能使用其中一个。使用 DHCP 时，dhclient(8) 通常会用从 DHCP 服务器接收的信息重写 `/etc/resolv.conf` 文件。

手动编辑 `/etc/resolv.conf` 文件后，重启系统时该文件可能被重置，因为动态主机配置协议（Dynamic Host Configuration Protocol，DHCP）客户端在获取网络配置时会通过 resolvconf 服务重写该文件。

如需使用手动配置的 DNS 服务器而不被系统自动更新覆盖，可通过禁用 resolvconf 服务实现。编辑 `/etc/resolvconf.conf` 文件（如不存在则创建），写入 `resolvconf=NO` 一行，该配置将禁用系统对 DNS 配置文件的自动更新功能。

### 参考文献

- FreeBSD Project. resolvconf[EB/OL]. [2026-03-26]. <https://man.freebsd.org/cgi/man.cgi?query=resolvconf>. man 手册，提供 resolvconf 工具的完整技术文档，为 DNS 配置管理提供重要参考。
- FreeBSD Forums. 8.8.8.8 or 1.1.1.1 if set in etc resolv conf doesn't stay as an entry in the file after a network restart[EB/OL]. [2026-03-26]. <https://forums.freebsd.org/threads/8-8-8-8-or-1-1-1-1-if-set-in-etc-resolv-conf-doesnt-stay-as-an-entry-in-the-file-after-a-network-restart.85951/>. 实际案例分析，提供防止覆写 DNS 配置的解决方案。

## 网络故障排除

在排除硬件和软件配置故障时，首先检查基本要素：

- 网线是否插好？
- 网络服务是否正确配置？
- 防火墙是否正确配置？
- 网卡是否受 FreeBSD 支持？
- 路由器是否正常工作？

如果网卡工作正常但性能不佳，可参阅 tuning(7)。同时检查网络配置，因不正确的网络设置可能导致连接缓慢。

“No route to host”消息发生在系统无法将数据包路由到目标主机时。这可能由于未指定默认路由或网线未插入所致。检查 `netstat -rn` 的输出，确保有到主机的有效路由。

“ping: sendto: Permission denied”错误消息通常由防火墙配置错误引起。如果在 FreeBSD 上启用了防火墙但未定义规则，默认策略是拒绝所有流量，甚至是 ping(8)。

## 附录：网络配置 rc.conf 示例

> **注意**：
>
> 修改 `/etc/rc.conf` 文件后，需重启系统或运行命令 `/etc/rc.d/netif restart` 来应用网络更改。

```ini
hostname="ykla"  # 主机名，不能为空，否则无法使用 Xorg
ifconfig_igc0="DHCP"  # 使网卡 igc0 使用 DHCP
ifconfig_igc0="inet 192.168.31.77 netmask 255.255.255.0"  # 设置网卡 igc0 的 IPv4 为 192.168.31.77，子网掩码为 255.255.255.0（静态 IP）
defaultrouter="192.168.31.1"  # 默认网关/默认路由，通常为路由器 IP 地址
ifconfig_igc0_alias0="inet 192.168.1.33 netmask 255.255.255.0"  # 设置网卡 igc0 别名 IPv4 192.168.1.33，子网掩码为 255.255.255.0 即拥有额外的 IPv4 地址
static_routes="static1 static2"  # 静态路由，需结合下文使用①
route_static1="-net 10.0.10.0/24 10.0.1.1"  # 如果要访问 10.0.10.0/24 这个网络（10.0.10.1 到 10.0.10.254），就将数据包发送给 10.0.1.1，由它来转发
route_static2="-net 172.16.30.0/24 172.16.1.254"  # 如果要访问 172.16.30.0/24 这个网络（172.16.30.1 到 172.16.30.254），就将数据包发送给 172.16.1.254，由它来转发
```

① 在 `/etc/rc.conf` 文件中，如果需要一次性写入多个配置项，只能使用 `ABC_XYZ="xxx yyy ccc ddd"` 这种格式。

如果在 `/etc/rc.conf` 文件中写成以下形式：

```ini
ABC_XYZ="xxx"	# 第一行
ABC_XYZ="yyy"
ABC_XYZ="ccc"
ABC_XYZ="ddd"
```

这种形式下，后续的 `ABC_XYZ` 配置行会覆盖前一行，因此只有最后一行会生效。

## 查看网卡速率

如需实时监控网络接口的流量统计信息，可使用 `systat` 工具的网络接口视图。该命令以指定的刷新间隔显示各网络接口的接收和发送流量数据：

```sh
# systat -if 2
```

其中 `-if` 参数指定显示网络接口信息，数字 2 表示刷新间隔为 2 秒。

## 查看 FreeBSD 下载流量（bwm-ng）

如需查看更详细的网络流量统计，可安装 `bwm-ng` 工具，该工具提供了多种流量显示格式和交互功能：

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

1. 在 FreeBSD 系统上配置双静态 IP 地址，分别设置不同的 DNS 服务器，然后使用 `dig` 命令验证每个 DNS 服务器的解析行为，分析为什么系统允许同时配置多个 DNS 服务器而不产生冲突。

2. 修改网络接口的 MTU 值为 9000（巨型帧），并使用命令测试连通性。

3. 禁用 `resolvconf` 服务，然后手动修改 `/etc/resolv.conf` 文件并重启网络服务，验证配置是否持久化。
