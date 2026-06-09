# 8.2 基础网络管理

本节介绍网络管理基础知识与故障排除技巧。

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

| 类型 | 说明 |
| ---- | ---- |
| **单播（Unicast）** | 发送到单播地址的数据包到达属于该地址的接口 |
| **任播（Anycast）** | 地址在语法上与单播地址无法区分，但指向一组接口。发往任播地址的数据包将到达最近的接口 |
| **多播（Multicast）** | 地址标识一组接口。发往多播地址的数据包将到达属于多播组的所有接口。IPv4 广播地址（通常为 xxx.xxx.xxx.255）在 IPv6 中由多播地址表示 |

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
ifconfig_igc0="inet 192.168.5.77 netmask 255.255.255.0"
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
fe80::20c:29ff:fe8 link#3             UHS             lo0   # 静态主机路由（与第37行重复，属路由表缓存正常现象）
fe80::%lo0/64      link#3             U               lo0   # lo0 接口链路本地子网
fe80::1%lo0        link#3             UHS             lo0   # lo0 单一本地主机链路本地地址，静态主机路由
ff02::/16          link#3             URS             lo0   # IPv6 多播地址
```

该示例的条目如下：

- **default**：
  默认路由。本地系统需要连接远程主机时，检查路由表以确定是否存在已知路径。如果远程主机匹配表中某条目，系统即检查可否通过该条目指定的接口完成连接。
  默认路由在无更具体前缀匹配时采用，不依赖其他路径的成败。对于局域网中的主机，默认路由的 `Gateway` 字段应设为可直接连接互联网的系统。读取该条目时，应确认 `Flags` 列指示网关可达（`UG`）。

  作为对外网关的机器，默认路由指向与互联网服务提供商（ISP）相连的网关。

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

服务提供商必须向主干站点通告自身连接点身份，成为流量进入路径。该过程称为路由传播。

路由传播偶有故障，导致部分站点无法连通。此时，查找路由断点的常用命令是 `traceroute`（IPv6 使用 `traceroute6`），`ping` 失败时尤其有用。

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

## 网卡别名

FreeBSD 的常见用途之一是虚拟站点托管，其中一台服务器在网络中表现为多个服务器。这是通过将多个网络地址分配给单个接口来实现的。

一个网络接口可以配置一个主 IP 地址（Primary Address）以及任意数量的附加 IP 地址（Secondary Addresses），它们在底层网络通信中具有相同的有效性。

> **技巧**
>
> “别名”（alias）地址只是早期操作系统为了方便管理而沿用的传统称呼，对于物理网卡而已并无区别。实际上，IPv6 天然地拥有多个地址特征。

这些别名通常通过在 **/etc/rc.conf** 中添加别名条目来实现，如下所示：

```sh
# sysrc ifconfig_em0_alias0="inet xxx.xxx.xxx.xxx netmask xxx.xxx.xxx.xxx"
```

别名条目必须以 `alias0` 开头，使用递增的数字，如 `alias0`、`alias1`，依此类推。配置过程将在第一个缺失的数字处停止。

别名子网掩码的计算非常重要。对于给定的接口，必须有一个地址正确表示网络的子网掩码。任何其他属于该网络的地址必须使用全 `1` 的子网掩码，表示为 **255.255.255.255** 或 **0xffffffff**。

例如，假设以下情况：`em0` 接口连接到两个网络：

- **10.1.1.0**、子网掩码为 **255.255.255.0**；
- **202.0.75.16**、子网掩码为 **255.255.255.240**。

我们需要为系统配置两个网段的 IP 地址范围：**10.1.1.1** 到 **10.1.1.5**，以及 **202.0.75.17** 到 **202.0.75.20**。

只有给定网络范围中的第一个地址应具有实际的子网掩码。其余地址（**10.1.1.2** 到 **10.1.1.5** 和 **202.0.75.18** 到 **202.0.75.20**）必须配置为子网掩码为 **255.255.255.255**。

以下 **/etc/rc.conf** 条目将接口配置为适应此场景：

```sh
# sysrc ifconfig_em0="inet 10.1.1.1 netmask 255.255.255.0"
# sysrc ifconfig_em0_alias0="inet 10.1.1.2 netmask 255.255.255.255"
# sysrc ifconfig_em0_alias1="inet 10.1.1.3 netmask 255.255.255.255"
# sysrc ifconfig_em0_alias2="inet 10.1.1.4 netmask 255.255.255.255"
# sysrc ifconfig_em0_alias3="inet 10.1.1.5 netmask 255.255.255.255"
# sysrc ifconfig_em0_alias4="inet 202.0.75.17 netmask 255.255.255.240"
# sysrc ifconfig_em0_alias5="inet 202.0.75.18 netmask 255.255.255.255"
# sysrc ifconfig_em0_alias6="inet 202.0.75.19 netmask 255.255.255.255"
# sysrc ifconfig_em0_alias7="inet 202.0.75.20 netmask 255.255.255.255"
```

一种更简洁的表达方式是使用以空格分隔的 IP 地址范围。第一个地址将使用指定的子网掩码，而额外的地址将使用子网掩码 **255.255.255.255**。

```sh
# sysrc ifconfig_em0_aliases="inet 10.1.1.1-5/24 inet 202.0.75.17-20/28"
```

## TCP/IP 协议栈

传输控制协议（Transmission Control Protocol，TCP）是互联网协议族（Internet Protocol Suite）中的核心传输层协议，软件实现体系称作 TCP 栈（采用层次化结构进行组织，因此称“栈”）。Vint Cerf 和 Bob Kahn 于 1974 年在论文《A Protocol for Packet Network Intercommunication》中首次提出 TCP 的核心思想（当时为传输与网络转发合一的单一协议），后经迭代，约在 1978 至 1979 年间决定将 TCP 与 IP 拆分为两个独立协议，并于 1981 年 9 月分别发布为 RFC 791（IP）和 RFC 793（TCP）。RFC 9293 已于 2022 年 8 月取代了 RFC 793，前者为当前 TCP 协议的最新标准规范。

TCP 栈提供端到端的可靠数据传输、拥塞控制、流量控制等关键功能。不同于其他主流操作系统，FreeBSD 创新性地实现了多 TCP 栈共存架构，该架构允许系统同时加载多个 TCP 协议栈实现，并可为不同的网络连接或系统全局选用不同的 TCP 栈。

当前主要开发与维护工作集中于 RACK 栈（RACK 算法最初出自 Google，FreeBSD 的 tcp_rack 栈实现出自 Netflix 的 Randall Stewart）和基础栈（基于 4.4BSD 经典栈实现演化而来，默认拥塞控制算法为 CUBIC）。

### 使用 RACK 栈

如需启用 RACK 栈：

```sh
# echo "net.inet.tcp.functions_default=rack" >> /etc/sysctl.conf
# sysrc kld_list+="tcp_rack"
# kldload tcp_rack
# sysctl net.inet.tcp.functions_default=rack
```

重启系统或加载内核模块后，用以下命令显示系统中可用 TCP 栈列表：

```sh
# sysctl net.inet.tcp.functions_available
net.inet.tcp.functions_available:
Stack                           D Alias                            PCB count
freebsd                           freebsd                          3
rack                            * rack                             0
```

输出中标记 `*` 的栈为当前系统默认使用的 TCP 协议栈。

### BBR 拥塞控制算法

- 充分利用可用网络带宽。
- 最小化网络传输延迟。

BBR（Bottleneck Bandwidth and Round-trip propagation time，瓶颈带宽与往返传播时间）不以丢包为拥塞信号，而是根据探测到的带宽和延迟动态调整发送速率，在高带宽长延迟的网络环境中更具优势。

### BBR 在 FreeBSD 中的实现与应用

将 `tcp_rack` 和 `tcp_bbr` 添加到系统启动列表：

```sh
# sysrc kld_list+="tcp_rack tcp_bbr"
```

将系统默认 TCP 拥塞控制算法设置为 BBR：

```sh
# echo 'net.inet.tcp.functions_default=bbr' >> /etc/sysctl.conf
```

重启系统后，查看当前系统使用的默认 TCP 拥塞控制算法：

```sh
# sysctl net.inet.tcp.functions_default
```

如果输出结果为 `net.inet.tcp.functions_default: bbr`，则 TCP BBR 启用成功。

### 故障排除与未竟事宜

在测试环境中，RACK 和 BBR 在局域网中表现良好，但在互联网环境下带宽显著下降：RACK 约为默认栈的三分之一，BBR 约为默认栈的六分之一。该测试在特定网络条件下完成（如高延迟跨境链路），实际性能可能因网络环境而异。需注意，RACK 与 BBR 的设计目标是提升而非降低吞吐量，上述结果可能源于特定丢包/延迟环境的系统性偏差，不代表这些栈在典型部署场景中的表现。

### 参考文献

- Netflix. netflix/tcplog_dumper[EB/OL]. [2026-03-26]. <https://github.com/netflix/tcplog_dumper>. Netflix 开源项目，提供 TCP 日志转储工具，为 TCP 协议分析提供实用工具。
- Cheng Y, Cardwell N, Dukkipati N, et al. The RACK-TLP Loss Detection Algorithm for TCP: RFC 8985[S/OL]. (2021-02)[2026-04-17]. <https://www.rfc-editor.org/rfc/rfc8985>. RACK-TLP 丢包检测算法的 IETF 标准文档，Google Yuchung Cheng、Neal Cardwell 等人撰写。

## 课后习题

1. 依次启用 FreeBSD 默认栈、RACK 栈和 BBR 栈，使用 `iperf3` 在局域网和互联网环境中分别测试吞吐量和延迟，记录三种栈在不同网络场景下的性能差异，并从拥塞控制算法原理角度分析差异成因。
2. 查阅 `tcp_bbr` 模块的源代码，找出控制 BBR 算法行为的关键参数，修改其中两个参数并重新加载模块，记录参数变化对传输性能的影响。
3. 分析 FreeBSD 多 TCP 栈共存架构的实现机制，设计一个测试场景，在同一系统中为不同网络连接指定不同的 TCP 栈，记录配置方法与验证结果。
