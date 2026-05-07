# 6.2 高级网络管理

## 网关和路由

**路由** 是使系统能够找到通往另一个系统的网络路径的机制。**路由** 是一对定义的地址，分别表示“目标”和“网关”。路由表明，当尝试连接到指定的目标时，应该通过指定的网关发送数据包。有三种目标类型：单个主机、子网和“默认”。“默认路由”在没有其他路由适用时使用。网关也有三种类型：单个主机、接口（也叫做链路）和以太网硬件（MAC）地址。已知的路由会存储在路由表中。

本节提供了路由基础的概述。然后展示了如何将 FreeBSD 系统配置为路由器，并提供了一些故障排除技巧。

### 路由基础

可以使用 netstat(1) 查看 FreeBSD 系统的路由表：

```sh
$ netstat -r
Routing tables

Internet:	# IPv4
# 路径				网关			  标志			接口	TTL
Destination        Gateway            Flags         Netif Expire
default            192.168.179.2      UGS             em0   # 默认路由，通过 em0 接口
localhost          link#3             UH              lo0   # 回环地址，使用 lo0 接口
192.168.5.0/24     link#2             U               em1   # 192.168.5.0/24 子网
192.168.5.16       link#3             UHS             lo0   # 本地主机地址 192.168.5.16，回环接口 lo0
192.168.179.0/24   link#1             U               em0   # 192.168.179.0/24 子网
192.168.179.128    link#3             UHS             lo0   # 本地主机地址 192.168.179.128，回环接口 lo0

Internet6:	# IPv6
Destination        Gateway            Flags         Netif Expire
::/96              link#3             URS             lo0   # IPv4 映射 IPv6 地址块，回环接口 lo0
default            fe80::5%em1        UG              em1   # 默认 IPv6 路由，下一跳是链路本地地址 fe80::5，标志 UG 表示可达且为网关
localhost          link#3             UHS             lo0   # IPv6 本地回环地址 ::1
::ffff:0.0.0.0/96  link#3             URS             lo0   # IPv4 映射 IPv6 地址
240e:341:22b:ae00: link#2             U               em1   # 全球单播地址
240e:341:22b:ae00: link#3             UHS             lo0   # 本地主机路由
fe80::%lo0/10      link#3             URS             lo0   # 链路本地 IPv6 网络
fe80::%em0/64      link#1             U               em0   # em0 接口链路本地 IPv6 地址
fe80::20c:29ff:fe8 link#3             UHS             lo0   # lo0 接口链路本地 IPv6 地址，静态主机路由
fe80::%em1/64      link#2             U               em1   # em1 接口链路本地 IPv6 地址
fe80::20c:29ff:fe8 link#3             UHS             lo0   # lo0 接口链路本地 IPv6 地址重复条目，静态主机路由
fe80::%lo0/64      link#3             U               lo0   # lo0 接口链路本地子网
fe80::1%lo0        link#3             UHS             lo0   # lo0 单一本地主机链路本地地址，静态主机路由
ff02::/16          link#3             URS             lo0   # IPv6 多播地址
```

这个例子中的条目如下：

- **default**：
  指定了默认路由。当本地系统需要连接到远程主机时，它会检查路由表以确定是否有已知的路径。如果远程主机匹配表中的某个条目，系统将检查是否可以通过该条目中指定的接口连接。
  默认路由在没有更具体前缀匹配时使用，不依赖于其他路径失败。对于本地局域网上的主机，默认路由中的 `Gateway` 字段设置为具有直接互联网连接的系统。在读取此条目时，请确保 `Flags` 列指示网关是可用的（`UG`）。

  对于作为外部世界网关的机器，默认路由将是连接到互联网服务提供商（ISP）的网关机器。
  
  对于 IPv4 网络，默认网关是 `192.168.179.2`，带有 UGS 标志（Up、Gateway、Static），这意味着所有发往未知外部网络（比如互联网）的 IPv4 流量，都会从 `em0` 这个网络接口发送给这台路由器进行转发。
  
  在 IPv6 部分，默认路由通过链路本地地址 `fe80::5%em1` 指定下一跳，这个下一跳通常是 ISP 提供的路由器。标志为 UG，说明所有未匹配的 IPv6 流量将通过 em1 接口发出。链路本地地址是 IPv6 特性，仅用于本地链路通信，并不等同于公网可达地址。
  
  这表明此机器具有双栈网络能力，且 IPv4 和 IPv6 的出口依赖不同的网卡（分别是 em0 和 em1）。

- **localhost**：这是第二个路由。`Netif` 列中为 `localhost` 指定的接口是 **lo0**，也称为回环设备。这表明所有发送到此目标的流量应保持在内部，而不是通过网络发送。

- **子网**

  从 IPv4 路由表中可以看出，此设备同时连接着两个不同的局域网：`192.168.5.0/24` 和 `192.168.179.0/24`。它们的网关显示为 `link#2` 和 `link#1`，且标志只有 U（Up），代表这是“直连网络”。当这台机器需要与这两个网段内的其他设备（例如 `192.168.5.x` 范围内的电脑）通信时，数据包不需要经过路由器，而是直接分别通过 em1 和 em0 接口广播并发送过去。
  
- **全球单播地址**

  在 IPv6 路由（Internet6）中，有一个非常重要的条目是以 `240e:341:22b:ae00:` 开头的地址，它绑定在 em1 接口上。这是一个全球单播地址（Global Unicast Address），通常由运营商（如中国电信 240e 开头）分配，理论上可在互联网路由，但实际访问能力取决于防护策略和服务配置。  

- **标志**

  可以在 `Flags` 列中查看每个路由的各种属性。**常见的路由表标志** 总结了这些标志及其含义。

  **常见的路由表标志**

  | 标志 | 目的                                 |
  | ---- | ---- |
  | U  | 路由是活动的（启用）                       |
  | H  | 路由目标是单个主机                       |
  | G  | 将此目的地的任何流量转发到此网关，由网关决定如何进一步转发   |
  | S  | 该路由是静态配置的                      |
  | C  | 直接连接的本地网络或克隆路由 |
  | W  | 该路由是根据本地网络（克隆）路由自动配置的             |
  | L  | 路由涉及到以太网（链路）硬件的引用                 |
  | R |路由重定向，常见于 Mesh 网络和 BGP |


### 跟踪路由信息

当一个地址空间被分配给一个网络时，服务提供商会配置他们的路由表，以确保所有流量都被发送到该站点的链接。但是，外部站点如何知道将其数据包发送到网络的 ISP 呢？

有一个系统跟踪所有分配的地址空间，并定义它们与互联网主干网（或承载互联网流量的主干线路）连接的节点。每台主干机器都保存一份主路由表，该表将特定网络的流量指向一个特定的主干承运商，从那里通过一系列服务提供商直到到达特定网络。

服务提供商的任务是向主干站点通告他们是连接点，因此也是流量的进入路径。这个过程被称为路由传播。

有时，路由传播会出现问题，导致某些站点无法连接。最有用的命令之一用于查找路由问题的断点是 `traceroute`（IPV6 为 `traceroute6`），尤其是在 `ping` 失败时非常有用。

使用 `traceroute` 时，需要提供远程主机的地址。输出将显示路径上的网关主机，最终要么到达目标主机，要么因连接问题而终止。

以下是对 `freebsd.org` 域名的 IPv6 路径跟踪：

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
    zayo.ae10.mpr4.sjc7.us.zip.zayo.com (2001:438:ffff::407e:2f9)  180.002 ms  179.112ms
10  ae34.mpr1.ewr4.us.zip.zayo.com (2001:438:ffff::407d:1455)  244.026 ms  243.263 ms *
11  2001:438:fffe::24ba (2001:438:fffe::24ba)  246.736 ms *  245.756 ms
12  cs89-cs80.nyinternet.net (2610:1c1::2502)  218.700 ms  218.396 ms  217.715 ms
13  2610:1c1::803 (2610:1c1::803)  228.099 ms  227.280 ms  226.003 ms
14  wfe0.nyi.freebsd.org (2610:1c1:1:606c::50:15)  214.724 ms  216.682 ms *
```




## TCP/IP 协议栈

传输控制协议（Transmission Control Protocol，TCP）是互联网协议套件（Internet Protocol Suite）中的核心传输层协议，其软件实现体系称为 TCP 栈（因采用层次化结构组织，因此称为"栈"）。TCP 协议最初于 1974 年由 Vint Cerf 和 Bob Kahn 设计，规范定义于 RFC 793。

TCP 栈负责端到端的可靠数据传输、拥塞控制、流量控制等关键功能。

不同于其他主流操作系统，FreeBSD 创新性地实现了多 TCP 栈共存架构，该架构允许系统同时加载多个 TCP 协议栈实现，并可为不同的网络连接或系统全局选用不同的 TCP 栈。

当前主要开发与维护工作集中于 RACK 栈（RACK 算法最初由 Google 开发，FreeBSD 的 tcp_rack 栈实现由 Netflix 的 Randall Stewart 完成）和基础栈（基于 4.4BSD 经典栈实现演化而来）。

### 使用 RACK 栈

RACK（Recent ACKnowledgment）是一种基于时间戳的快速丢包检测算法，最初由 Google 的 Yuchung Cheng、Neal Cardwell 等人提出（标准化为 RFC 8985）。Netflix 的 Randall Stewart 将其实现为 FreeBSD 的 tcp_rack 栈，通过改进丢包恢复机制优化网络传输性能。与传统基于 4.4BSD 的 TCP 栈相比，RACK 在高延迟丢包时恢复速度更快，在现代网络环境中具有更好的性能表现。

如需启用 RACK 栈，需按以下步骤操作：

```sh
# echo "net.inet.tcp.functions_default=rack" >> /etc/sysctl.conf
# sysrc kld_list+="tcp_rack"
# kldload tcp_rack
# sysctl net.inet.tcp.functions_default=rack
```

第一条命令将系统默认 TCP 栈设置为 RACK 并写入 sysctl 配置文件，实现开机自动启用；第二条命令将 `tcp_rack` 模块添加到系统启动加载列表；第三条命令立即加载 `tcp_rack` 内核模块；第四条命令立即应用 RACK 栈设置。

重启系统或加载内核模块后，可通过以下命令显示系统中可用的 TCP 栈列表：

```sh
# sysctl net.inet.tcp.functions_available
net.inet.tcp.functions_available:
Stack                           D Alias                            PCB count
freebsd                           freebsd                          3
rack                            * rack                             0
```

输出中标记 `*` 的栈为当前系统默认使用的 TCP 协议栈。

### BBR 拥塞控制算法原理

TCP BBR（Bottleneck Bandwidth and Round-trip propagation time）是 Google 公司开发的一种基于模型的拥塞控制算法。与传统基于丢包的拥塞控制算法（如 CUBIC、NewReno）不同，BBR 通过主动探测网络路径的瓶颈带宽和往返传播时间构建网络性能模型，其核心优化目标包括：

- 充分利用可用网络带宽。
- 最小化网络传输延迟。

BBR 不再将丢包作为拥塞信号，而是根据探测到的带宽和延迟动态调整发送速率，在高带宽长延迟网络环境中表现更具优势。

### BBR 在 FreeBSD 中的实现与应用

FreeBSD 平台上的 TCP BBR 实现由 Netflix 技术团队完成，作为 `tcp_bbr` 拥塞控制模块提供。部分网络场景下（如长距离传输、高带宽链路），启用 TCP BBR 可提升网络传输性能。

无需编译内核，可直接将 `tcp_rack` 和 `tcp_bbr` 模块添加到系统启动加载列表，实现开机自动加载：

```sh
# sysrc kld_list+="tcp_rack tcp_bbr"
```

将系统默认 TCP 拥塞控制算法设置为 BBR 并写入 sysctl 配置文件，实现开机自动启用：

```sh
# echo 'net.inet.tcp.functions_default=bbr' >> /etc/sysctl.conf
```

完成上述配置后，重启系统或立即加载模块并应用配置：

```sh
# reboot
```

查看当前系统使用的默认 TCP 拥塞控制算法：

```sh
# sysctl net.inet.tcp.functions_default
```

如果输出结果为 `net.inet.tcp.functions_default: bbr`，则 TCP BBR 启用成功。

### 故障排除与未竟事宜

#### 性能差异分析与说明

使用 RACK 或 BBR 栈时可能遇到以下问题：

#### 局域网速度良好但互联网速度不佳

在测试环境中观察到，RACK 和 BBR 栈在局域网环境中的性能表现良好，均优于默认 TCP 栈；但在互联网环境中的性能表现存在一定局限性：测试数据显示，RACK 栈的互联网传输速度约为默认栈的三分之一，BBR 栈约为默认栈的六分之一。该测试在特定网络条件下完成，实际性能可能因网络环境、硬件配置和流量特征等因素而异。

该性能差异可能通过调整相关参数得到优化，具体的参数调优方法有待进一步研究与验证。

### 参考文献

- Netflix. netflix/tcplog_dumper[EB/OL]. [2026-03-26]. <https://github.com/netflix/tcplog_dumper>. Netflix 开源项目，提供 TCP 日志转储工具，为 TCP 协议分析提供实用工具。
- Cheng Y, Cardwell N, Dukkipati N, et al. The RACK-TLP Loss Detection Algorithm for TCP: RFC 8985[S/OL]. (2021-02)[2026-04-17]. <https://www.rfc-editor.org/rfc/rfc8985>. RACK-TLP 丢包检测算法的 IETF 标准文档，由 Google 的 Yuchung Cheng、Neal Cardwell 等人撰写。
- FreeBSD Project. tcp -- Internet Transmission Control Protocol[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?tcp(4)>. TCP 协议栈手册页，描述传输控制协议实现与套接字选项。
- FreeBSD Project. ip -- Internet Protocol[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?ip(4)>. IP 协议手册页，描述网际协议实现与套接字选项。
- FreeBSD Project. sysctl -- get or set kernel state[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?sysctl(8)>. 内核状态管理工具手册页，描述 MIB 变量的读取与设置。
- FreeBSD Project. sysctl.conf -- kernel state defaults[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?sysctl.conf(5)>. 内核状态默认配置文件格式手册页。
- FreeBSD Project. FreeBSD Handbook, Chapter 32: Advanced Networking[EB/OL]. [2026-04-14]. <https://docs.freebsd.org/en/books/handbook/advanced-networking/>. FreeBSD 手册中关于高级网络配置的指南。

## 课后习题

1. 依次启用 FreeBSD 默认栈、RACK 栈和 BBR 栈，使用 `iperf3` 在局域网和互联网环境中分别测试吞吐量和延迟，记录三种栈在不同网络场景下的性能差异，并从拥塞控制算法原理角度分析差异成因。
2. 查阅 `tcp_bbr` 模块的源代码，找出控制 BBR 算法行为的关键参数，修改其中两个参数并重新加载模块，记录参数变化对传输性能的影响。
3. 分析 FreeBSD 多 TCP 栈共存架构的实现机制，设计一个测试场景，在同一系统中为不同网络连接指定不同的 TCP 栈，记录配置方法与验证结果。
