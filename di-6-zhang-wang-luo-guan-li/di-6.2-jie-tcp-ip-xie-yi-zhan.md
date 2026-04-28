# 6.2 TCP/IP 协议栈

传输控制协议（Transmission Control Protocol，TCP）是互联网协议套件（Internet Protocol Suite）中的核心传输层协议之一，其软件实现体系被称为 TCP 栈（因采用层次化结构组织，故称为“栈”）。TCP 协议最初由 Vint Cerf 和 Bob Kahn 于 1974 年设计，其规范定义于 RFC 793。

TCP 栈负责端到端的可靠数据传输、拥塞控制、流量控制等关键功能。

不同于其他主流操作系统，FreeBSD 创新性地实现了多 TCP 栈共存架构，该架构允许系统同时加载多个 TCP 协议栈实现，并允许为不同的网络连接或系统全局选择使用不同的 TCP 栈。

当前主要开发与维护工作集中于 RACK 栈（RACK 算法最初由 Google 开发，FreeBSD 的 tcp_rack 栈实现由 Netflix 的 Randall Stewart 完成）和基础栈（基于 4.4BSD 经典栈实现演化而来）。

## 使用 RACK 栈

RACK（Recent ACKnowledgment）是一种基于时间戳的快速丢包检测算法，最初由 Google 的 Yuchung Cheng、Neal Cardwell 等人提出（标准化为 RFC 8985），Netflix 的 Randall Stewart 将其实现为 FreeBSD 的 tcp_rack 栈，旨在通过改进丢包恢复机制优化网络传输性能。与传统基于 4.4BSD 的 TCP 栈相比，RACK 在高延迟丢包时恢复速度更快，在现代网络环境中具有更好的性能表现。

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

## BBR 拥塞控制算法原理

TCP BBR（Bottleneck Bandwidth and Round-trip propagation time）是 Google 公司开发的一种基于模型的拥塞控制算法。与传统基于丢包的拥塞控制算法（如 CUBIC、NewReno）不同，BBR 通过主动探测网络路径的瓶颈带宽和往返传播时间来构建网络性能模型，其核心优化目标包括：

- 充分利用可用网络带宽。
- 最小化网络传输延迟。

BBR 不再将丢包作为拥塞信号，而是根据探测到的带宽和延迟动态调整发送速率，在高带宽长延迟网络环境中表现更具优势。

## BBR 在 FreeBSD 中的实现与应用

FreeBSD 平台上的 TCP BBR 实现由 Netflix 技术团队完成，作为 `tcp_bbr` 拥塞控制模块提供。在部分网络场景下（如长距离传输、高带宽链路），启用 TCP BBR 可提升网络传输性能。

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

若输出结果为 `net.inet.tcp.functions_default: bbr`，则 TCP BBR 启用成功。

## 故障排除与未竟事宜

### 性能差异分析与说明

在使用 RACK 或 BBR 栈的过程中，可能会遇到一些需要注意的问题，以下是相关说明。

### 局域网速度良好但互联网速度不佳

在测试环境中观察到，RACK 和 BBR 栈在局域网环境中的性能表现良好，均优于默认 TCP 栈；但在互联网环境中的性能表现存在一定局限性：测试数据显示，RACK 栈的互联网传输速度约为默认栈的三分之一，BBR 栈则约为默认栈的六分之一。该测试在特定网络条件下完成，实际性能可能因网络环境、硬件配置和流量特征等因素而异。

该性能差异可能通过调整相关参数得到优化，具体的参数调优方法有待进一步研究与验证。

## 参考文献

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
