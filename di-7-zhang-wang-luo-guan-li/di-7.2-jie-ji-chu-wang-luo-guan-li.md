# 7.2 基础网络管理

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

也可在命令行通过 ifconfig(8) 配置网络接口，但若不同时将这些配置写入 **/etc/rc.conf** 文件，重启后配置将丢失。

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
nameserver 223.6.6.6   # 指定备用 DNS 服务器为阿里云公共 DNS
```

随后重启网络接口和路由：

```sh
# service netif restart
# service routing restart
```

可使用 ping(8) 测试连接：

```sh
$ ping -4c2 FreeBSD.org
PING FreeBSD.org (96.47.72.84): 56 data bytes
64 bytes from 96.47.72.84: icmp_seq=0 ttl=51 time=239.916 ms
64 bytes from 96.47.72.84: icmp_seq=1 ttl=51 time=236.443 ms

--- FreeBSD.org ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 236.443/238.179/239.916/1.737 ms
```

如能正常收到 ICMP 响应报文，表明网络已连通。

## 配置 IPv6

IPv6 是 IPv4 的后继协议。IPv6 相对于 IPv4 提供了多项优势和新功能：

- 其 128 位地址空间可容纳约 3.4×10^38 个地址，从而解决了 IPv4 地址短缺与耗尽问题。
- 路由器仅在路由表中存储网络聚合地址，通过地址聚合减少路由表条目，这与 IPv4 相比大幅降低了路由器的内存和 CPU 需求。
- 地址自动配置（RFC 4862）。
- 以多播取代广播地址。
- 支持 IPsec（IP 安全），但非强制要求（RFC 6434 已将 IPv6 节点对 IPsec 的实现要求由 MUST 调整为 SHOULD，因此成为推荐而非必选）。
- 简化的头部结构。
- 对移动 IP 的支持。
- IPv6 到 IPv4 的过渡机制。

FreeBSD 集成了 [KAME](https://www.kame.net/) 项目 IPv6 参考实现，并包含 IPv6 所需的全部组件。KAME 项目已于 2006 年结束，其代码由 FreeBSD 项目继续维护和演进。

IPv6 地址有三种不同类型：

| 类型 | 说明 |
| ---- | ---- |
| **单播（Unicast）** | 发送到单播地址的数据包到达属于该地址的接口 |
| **任播（Anycast）** | 地址在语法上与单播地址无法区分，但指向一组接口。发往任播地址的数据包将到达最近的接口 |
| **多播（Multicast）** | 地址标识一组接口。发往多播地址的数据包将到达属于多播组的所有接口。IPv4 广播地址（通常为 xxx.xxx.xxx.255）在 IPv6 中由多播地址表示 |

读取 IPv6 地址时，规范形式表示为 `x:x:x:x:x:x:x:x`，其中每个 x 代表一个 16 位十六进制值。例如 **FEBC:A574:382B:23C1:AA49:4592:4EFE:9982**。

IPv6 地址中常出现连续的全零字段。`::`（双冒号）可用于替换地址中一段连续的全零字段。此外，每个十六进制值最多可省略三个前导零。例如，**fe80::1** 对应规范形式 **fe80:0000:0000:0000:0000:0000:0000:0001**。

部分 IPv6 地址为保留地址：

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

要将 FreeBSD 系统配置为具有静态 IPv6 地址的 IPv6 客户端，需设置 IPv6 地址：

```sh
# sysrc ifconfig_em0_ipv6="inet6 2001:db8:4672:6565:2026:5043:2d42:5344 prefixlen 64"
```

要分配默认路由器：

```sh
# sysrc ipv6_defaultrouter="2001:db8:4672:6565::1"
```

可使用 ping(8) 测试连接：

```sh
$ ping -6c2 FreeBSD.org
PING(56=40+8+8 bytes) 240e:341:228:f400:cfbe:d56:7f75:26e0 --> 2610:1c1:1:606c::50:15
16 bytes from 2610:1c1:1:606c::50:15, icmp_seq=0 hlim=47 time=223.377 ms
16 bytes from 2610:1c1:1:606c::50:15, icmp_seq=1 hlim=47 time=223.348 ms

--- FreeBSD.org ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 223.348/223.362/223.377/0.014 ms
```

如能正常收到 ICMP 响应报文，表明网络已连通。

### 参考文献

- Li Q, Jinmei T, Shima K. IPv6 详解：卷 1，核心协议实现[M]. 陈涓，赵振平，译. 北京：人民邮电出版社，2009：846. ISBN: 978-7-115-18950-9 (英文影印版本 ISBN: 978-7-115-19551-7). 详解 IPv6 核心协议实现，基于 FreeBSD KAME 项目代码分析。
- Li Q, Jinmei T, Shima K. IPv6 详解：卷 2，高级协议实现[M]. 王嘉祯，等，译. 北京：人民邮电出版社，2009：869. ISBN: 978-7-115-20891-0 (英文影印版本 ISBN: 978-7-115-19519-7). 详解 IPv6 高级协议与扩展机制，包含移动 IPv6 等关键技术。

## 网卡别名

FreeBSD 的常见用途之一是虚拟站点托管，即一台服务器在网络中呈现为多台服务器。其实现方式是将多个网络地址分配给单个接口。

一个网络接口可配置一个主 IP 地址（Primary Address）以及任意数量的附加 IP 地址（Secondary Addresses），它们在底层网络通信中具有同等效力。

> **技巧**
>
> “别名”（alias）地址只是早期操作系统为了方便管理而沿用的传统称呼，对于物理网卡而言并无区别。实际上，IPv6 本身即支持多地址。

这些别名通常通过在 **/etc/rc.conf** 中添加别名条目来实现，如下所示：

```sh
# sysrc ifconfig_em0_alias0="inet xxx.xxx.xxx.xxx netmask xxx.xxx.xxx.xxx"
```

别名条目必须以 `alias0` 开头，使用递增的数字，如 `alias0`、`alias1`，依此类推。配置过程将在第一个缺失的数字处停止。

别名子网掩码的计算非常重要。对于给定的接口，必须有一个地址正确表示网络的子网掩码。任何其他属于该网络的地址必须使用全 `1` 的子网掩码，表示为 **255.255.255.255** 或 **0xffffffff**。

例如，假设以下情况：`em0` 接口连接到两个网络：

- **6.1.1.0**、子网掩码为 **255.255.255.0**；
- **202.0.75.16**、子网掩码为 **255.255.255.240**。

我们需要为系统配置两个网段的 IP 地址范围：**6.1.1.1** 到 **6.1.1.5**，以及 **202.0.75.17** 到 **202.0.75.20**。

只有给定网络范围中的第一个地址应具有实际的子网掩码。其余地址（**6.1.1.2** 到 **6.1.1.5** 和 **202.0.75.18** 到 **202.0.75.20**）必须配置为子网掩码为 **255.255.255.255**。

以下 **/etc/rc.conf** 条目将接口配置为适应此场景：

```sh
# sysrc ifconfig_em0="inet 6.1.1.1 netmask 255.255.255.0"
# sysrc ifconfig_em0_alias0="inet 6.1.1.2 netmask 255.255.255.255"
# sysrc ifconfig_em0_alias1="inet 6.1.1.3 netmask 255.255.255.255"
# sysrc ifconfig_em0_alias2="inet 6.1.1.4 netmask 255.255.255.255"
# sysrc ifconfig_em0_alias3="inet 6.1.1.5 netmask 255.255.255.255"
# sysrc ifconfig_em0_alias4="inet 202.0.75.17 netmask 255.255.255.240"
# sysrc ifconfig_em0_alias5="inet 202.0.75.18 netmask 255.255.255.255"
# sysrc ifconfig_em0_alias6="inet 202.0.75.19 netmask 255.255.255.255"
# sysrc ifconfig_em0_alias7="inet 202.0.75.20 netmask 255.255.255.255"
```

一种更简洁的表达方式是使用以空格分隔的 IP 地址范围。第一个地址将使用指定的子网掩码，而额外的地址将使用子网掩码 **255.255.255.255**。

```sh
# sysrc ifconfig_em0_aliases="inet 6.1.1.1-5/24 inet 202.0.75.17-20/28"
```

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

## DNS

可将 DNS 类比为电话簿，其中 IP 地址与主机名相互对应。除非 **/etc/nsswitch.conf** 文件中另有说明，FreeBSD 将首先查看 **/etc/hosts** 文件中的地址，随后查看 **/etc/resolv.conf** 文件中的 DNS 信息。

相关文件结构：

```sh
/etc/
├── rc.conf             # 系统启动配置文件
├── resolv.conf          # DNS 解析服务器配置文件
└── resolvconf.conf      # resolvconf 服务配置文件
```

### 本地地址 hosts 文件

**/etc/hosts** 文件是一个简单的文本数据库，提供主机名到 IP 地址的映射。通过 LAN 连接的本地计算机条目可添加到此文件中，用于简单的主机名解析，无须设置 DNS 服务器。此外，**/etc/hosts** 文件可提供互联网域名的本地记录，减少对外部 DNS 服务器的查询需求。

例如，在本地环境中有 www/gitlab-ce 的本地实例，可以将如下行添加到 **/etc/hosts** 文件：

```ini
192.168.1.150 git.example.com git
```

### 配置 DNS 名称服务器

FreeBSD 系统访问 Internet 域名系统（DNS）的方式由 resolv.conf(5) 控制。**/etc/resolv.conf** 文件中最常见的条目是：

| 条目 | 说明 |
| ---- | ---- |
| `nameserver` | 解析器应查询的名称服务器的 IP 地址。服务器按列出的顺序查询，最多三个 |
| `search` | 主机名查找的搜索列表。通常由本地主机名的域确定 |
| `domain` | 本地域名 |

典型的 **/etc/resolv.conf** 文件如下：

```ini
search example.com
nameserver 223.5.5.5
nameserver 223.6.6.6
```

search 和 domain 选项互斥；如果两者都指定，只有最后一个生效。使用 DHCP 时，dhclient(8) 通常会用从 DHCP 服务器接收的信息重写 **/etc/resolv.conf** 文件。

由于动态主机配置协议（Dynamic Host Configuration Protocol，DHCP）客户端在获取网络配置时会通过 resolvconf 服务重写 /etc/resolv.conf，手动编辑该文件后，系统重启时配置可能被覆盖。

如需使用手动配置的 DNS 服务器而不希望系统自动更新覆盖，可禁用 resolvconf 服务。编辑 **/etc/resolvconf.conf** 文件（如不存在则创建），写入 `resolvconf=NO` 一行，该配置将禁用系统对 DNS 配置文件的自动更新。

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
- 网线是否连接正常？
- 网络服务是否正确配置？
- 防火墙是否正确配置？
- 网卡是否受 FreeBSD 支持？

如果网卡工作正常但性能不佳，可参阅 tuning(7)。不正确的网络设置可能导致连接缓慢，应同时检查网络配置。

“No route to host”消息表示系统无法将数据包路由到目标主机。这通常是因为未指定默认路由或网线未连接。可使用 `route get <目标地址>` 命令查看系统对特定目标的路由决策，再检查 `netstat -rn` 的输出，确保有到主机的有效路由。

错误消息 `ping: sendto: Permission denied` 通常由防火墙配置错误引起。如果直接加载了 IPFW 防火墙模块但未配置任何规则，IPFW 的默认规则 65535 会拒绝所有流量，甚至是 ping(8)。

通过 rc.conf 启用防火墙时：

- `firewall_type` 的默认值为 `"UNKNOWN"`，此时不会添加任何放行规则，仅有默认规则 65535（deny all）生效
- 若将 `firewall_type` 显式设置为 `"open"`，则 IPFW 会在规则 65000 处添加放行规则，覆盖默认的拒绝行为。

PF 和 IPFilter 无规则时默认放行。

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

## 附录：/etc/rc.conf 网络配置示例

> **注意**：
>
> 修改 **/etc/rc.conf** 文件后，需重启系统或依次运行命令 `service netif restart` 与 `service routing restart` 来应用网络更改。

主机名（不得为空，否则无法使用 Xorg）：

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

为网卡 igc0 设置别名 IPv4 **192.168.5.12**，子网掩码为 **255.255.255.255**（与主地址同子网时必须使用全 1 掩码）从而拥有额外的 IPv4 地址：

```ini
ifconfig_igc0_alias0="inet 192.168.5.12 netmask 255.255.255.255"
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

示例：如需访问网络 **6.88.200.0/24** 地址块（可用主机 IP 从 **6.88.200.1** 到 **6.88.200.254**），则将数据包发送至 6.10.6.254，由其转发：

```ini
route_static2="-net 6.88.200.0/24 6.10.6.254"
```

## 课后习题

1. 在 FreeBSD 系统上配置双静态 IP 地址，分别设置不同的 DNS 服务器，使用 `dig` 命令验证每个 DNS 服务器的解析行为，分析 **/etc/resolv.conf** 中多 DNS 服务器条目的查询顺序与容错机制。
2. 修改网络接口的 MTU（Maximum Transmission Unit）值为 9000（巨型帧），使用 `ping` 测试连通性，记录 MTU 变化对大包传输的影响，分析巨型帧在局域网与广域网中的适用场景。
3. 禁用 `resolvconf` 服务，手动修改 **/etc/resolv.conf** 文件并重启网络服务，验证配置是否持久化，分析 `resolvconf` 对 DNS 配置动态管理的机制。
