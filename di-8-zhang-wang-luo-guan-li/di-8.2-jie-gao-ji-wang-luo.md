# 8.2 高级网络

本节介绍路由基础知识与故障排除技巧。

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

## TCP/IP 协议栈

传输控制协议（Transmission Control Protocol，TCP）是互联网协议族（Internet Protocol Suite）中的核心传输层协议，软件实现体系称作 TCP 栈（采用层次化结构进行组织，因此称“栈”）。Vint Cerf 和 Bob Kahn 于 1974 年在论文《A Protocol for Packet Network Intercommunication》中首次提出 TCP 的核心思想（当时为传输与网络转发合一的单一协议），后经迭代，约在 1978 至 1979 年间决定将 TCP 与 IP 拆分为两个独立协议，并于 1981 年 9 月分别发布为 RFC 791（IP）和 RFC 793（TCP）。RFC 9293 已于 2022 年 8 月取代了 RFC 793，前者为当前 TCP 协议的最新标准规范。

TCP 栈提供端到端的可靠数据传输、拥塞控制、流量控制等关键功能。不同于其他主流操作系统，FreeBSD 创新性地实现了多 TCP 栈共存架构，该架构允许系统同时加载多个 TCP 协议栈实现，并可为不同的网络连接或系统全局选用不同的 TCP 栈。

当前主要开发与维护工作集中于 RACK 栈（RACK 算法最初出自 Google，FreeBSD 的 tcp_rack 栈实现出自 Netflix 的 Randall Stewart）和基础栈（基于 4.4BSD 经典栈实现演化而来）。

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

BBR 不以丢包为拥塞信号，而是根据探测到的带宽和延迟动态调整发送速率，在高带宽长延迟的网络环境中更具优势。

### BBR 在 FreeBSD 中的实现与应用

将 `tcp_rack` 和 `tcp_bbr` 添加到系统启动列表：

```sh
# sysrc kld_list+="tcp_rack tcp_bbr"
```

将系统默认 TCP 拥塞控制算法设置为 BBR：

```sh
# echo 'net.inet.tcp.functions_default=bbr' >> /etc/sysctl.conf
```

重启系统：

```sh
# reboot
```

查看当前系统使用的默认 TCP 拥塞控制算法：

```sh
# sysctl net.inet.tcp.functions_default
```

如果输出结果为 `net.inet.tcp.functions_default: bbr`，则 TCP BBR 启用成功。

### 故障排除与未竟事宜

在测试环境中，RACK 和 BBR 在局域网中表现良好，但在互联网环境下带宽显著下降：RACK 约为默认栈的三分之一，BBR 约为默认栈的六分之一。该测试在特定网络条件下完成（如高延迟跨境链路），实际性能可能因网络环境而异。需注意，RACK 与 BBR 的设计目标是提升而非降低吞吐量，上述结果可能源于特定丢包/延迟环境的系统性偏差，不代表这些栈在典型部署场景中的表现。

## 参考文献

- Netflix. netflix/tcplog_dumper[EB/OL]. [2026-03-26]. <https://github.com/netflix/tcplog_dumper>. Netflix 开源项目，提供 TCP 日志转储工具，为 TCP 协议分析提供实用工具。
- Cheng Y, Cardwell N, Dukkipati N, et al. The RACK-TLP Loss Detection Algorithm for TCP: RFC 8985[S/OL]. (2021-02)[2026-04-17]. <https://www.rfc-editor.org/rfc/rfc8985>. RACK-TLP 丢包检测算法的 IETF 标准文档，Google Yuchung Cheng、Neal Cardwell 等人撰写。
- FreeBSD Project. tcp -- Internet Transmission Control Protocol[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?query=tcp&sektion=4>. TCP 协议栈手册页，描述传输控制协议实现与套接字选项。
- FreeBSD Project. ip -- Internet Protocol[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?query=ip&sektion=4>. IP 协议手册页，描述网际协议实现与套接字选项。

## 课后习题

1. 依次启用 FreeBSD 默认栈、RACK 栈和 BBR 栈，使用 `iperf3` 在局域网和互联网环境中分别测试吞吐量和延迟，记录三种栈在不同网络场景下的性能差异，并从拥塞控制算法原理角度分析差异成因。
2. 查阅 `tcp_bbr` 模块的源代码，找出控制 BBR 算法行为的关键参数，修改其中两个参数并重新加载模块，记录参数变化对传输性能的影响。
3. 分析 FreeBSD 多 TCP 栈共存架构的实现机制，设计一个测试场景，在同一系统中为不同网络连接指定不同的 TCP 栈，记录配置方法与验证结果。
