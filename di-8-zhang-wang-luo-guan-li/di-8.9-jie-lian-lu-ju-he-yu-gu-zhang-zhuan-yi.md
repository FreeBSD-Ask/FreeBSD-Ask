# 8.9 链路聚合与故障转移

FreeBSD 提供了 lagg(4) 接口，可以将多个网络接口聚合为一个虚拟接口，以提供故障转移和链路聚合。故障转移允许流量继续传输，只要至少一个聚合接口的链路有效。链路聚合在支持 LACP 的交换机上效果最佳，因为该协议双向分配流量，并能响应单个链路的故障。

lagg 接口支持的聚合协议决定了哪些端口用于发送流量以及是否允许特定端口接收流量。以下是 lagg(4) 支持的协议：

- **failover** 此模式仅通过主端口发送和接收流量。如果主端口不可用，则使用下一个活动端口。第一个添加到虚拟接口的接口为主端口，所有后续添加的接口将用作故障转移设备。如果发生故障转移到非主端口，则当原始端口恢复后，其将重新成为主端口。
- **loadbalance** 提供静态设置，不与对端协商聚合或交换帧来监控链路。如果交换机支持 LACP，应该使用 LACP 协议。
- **lacp** IEEE 802.3ad 链路聚合控制协议（LACP）与对端协商一组可聚合的链路，形成一个或多个链路聚合组（LAG）。每个 LAG 由相同速率、全双工操作的端口组成，并且流量会根据 LAG 的最大总速度在端口之间进行平衡。通常，只有一个 LAG 包含所有端口。在物理连接发生变化时，LACP 会快速收敛到新的配置。
  LACP 基于哈希的协议头信息平衡外发流量，并接受任何活动端口的入站流量。哈希包括以太网源和目标地址，若可用，还包括 VLAN 标签，以及 IPv4 或 IPv6 的源和目标地址。
- **roundrobin** 此模式通过所有活动端口使用轮询调度器分配外发流量，并接受任何活动端口的入站流量。由于此模式可能导致以太网帧乱序，因此应谨慎使用。
- **broadcast** 此模式将外发流量发送到配置在 lagg 接口上的所有端口，并从任何端口接收帧。

## 配置示例

本节演示如何配置交换机和 FreeBSD 系统以进行 LACP 负载均衡。随后介绍如何将两个以太网接口配置为故障转移模式，以及如何在以太网接口和无线接口之间配置故障转移模式。

### 示例 1. 使用交换机进行 LACP 聚合

本示例将 FreeBSD 机器上的两个 em4 以太网接口与交换机上的前两个以太网端口连接，作为一个负载均衡和故障容错链路。可以添加更多接口以增加吞吐量和容错能力。请将示例中的交换机端口、以太网设备和 IP 地址替换为实际配置。

以太网链路要求帧保持顺序，因此两个站点之间的同一流量始终通过同一物理链路，单条流量的最大速率受限于单个接口的带宽。传输算法会尽可能多地利用信息来区分不同的流量，并将流量均衡分配到可用的接口上。

在 FreeBSD 系统上，使用物理接口 **em0** 和 **em1** 创建 lagg(4) 接口，并为该接口分配 IP 地址 **10.0.0.3/24**：

```sh
# ifconfig em0 up
# ifconfig em1 up
# ifconfig lagg0 create
# ifconfig lagg0 up laggproto lacp laggport em0 laggport em1 10.0.0.3/24
```

接下来，验证虚拟接口的状态：

```sh
# ifconfig lagg0
lagg0: flags=1008843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST,LOWER_UP> metric 0 mtu 1500
        options=4e504bb<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,JUMBO_MTU,VLAN_HWCSUM,LRO,VLAN_HWFILTER,VLAN_HWTSO,RXCSUM_IPV6,TXCSUM_IPV6,HWSTATS,MEXTPG>
        ether 00:50:56:29:a9:45
        hwaddr 00:00:00:00:00:00
        inet 10.0.0.3 netmask 0xffffff00 broadcast 10.0.0.255
        laggproto lacp lagghash l2,l3,l4
        laggport: em0 flags=0<>
        laggport: em1 flags=0<>
        groups: lagg
        media: Ethernet autoselect
        status: active
        nd6 options=829<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL,STABLEADDR>
```

为确保此配置在重启后仍然生效，需在 FreeBSD 系统的 **/etc/rc.conf** 文件中添加以下条目：

```sh
ifconfig_em0="up"
ifconfig_em1="up"
cloned_interfaces="lagg0"
ifconfig_lagg0="laggproto lacp laggport em0 laggport em1 10.0.0.3/24"
```

### 示例 2. 故障转移模式

故障转移模式可用于在主接口的链路丢失时切换到备用接口。要配置故障转移，确保底层物理接口已启用，然后创建 lagg(4) 接口。在此示例中，**em0** 是主接口，**em1** 是备用接口，虚拟接口通过 DHCP 分配 IP 地址：

```sh
# ifconfig em0 up
# ifconfig em1 up
# ifconfig lagg0 create
# ifconfig lagg0 up laggproto failover laggport em0 laggport em1
# dhclient lagg0
```

虚拟接口的状态应如下所示：

```sh
# ifconfig lagg0
lagg0: flags=1008843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST,LOWER_UP> metric 0 mtu 1500
	options=4e504bb<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,JUMBO_MTU,VLAN_HWCSUM,LRO,VLAN_HWFILTER,VLAN_HWTSO,RXCSUM_IPV6,TXCSUM_IPV6,HWSTATS,MEXTPG>
	ether 00:50:56:29:a9:45
	hwaddr 00:00:00:00:00:00
	inet 192.168.5.5 netmask 0xffffff00 broadcast 192.168.5.255
	laggproto failover lagghash l2,l3,l4
	laggport: em0 flags=5<MASTER,ACTIVE>
	laggport: em1 flags=0<>
	groups: lagg
	media: Ethernet autoselect
	status: active
	nd6 options=829<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL,STABLEADDR>
```

流量将在 **em0** 上发送和接收。如果 **em0** 上的链路丢失，**em1** 将成为活动链路。如果主接口的链路恢复，它将重新成为活动链路。

为确保此配置在重启后仍然生效，需在 **/etc/rc.conf** 文件中添加以下条目：

```sh
ifconfig_em0="up"
ifconfig_em1="up"
cloned_interfaces="lagg0"
ifconfig_lagg0="laggproto failover laggport em0 laggport em1 DHCP"
```

### 示例 3. 以太网与无线接口之间的故障转移模式

对于笔记本电脑用户，通常希望将无线设备配置为备用接口，仅在以太网连接不可用时使用。使用 lagg(4) 可以配置故障转移模式，优先选择以太网连接，出于性能和安全性考虑，同时保持通过无线连接传输数据的能力。

此配置通过将以太网接口的 MAC 地址覆写为无线接口的 MAC 地址来实现。

> **注意**
>
> 理论上，以太网或无线 MAC 地址都可以更改以匹配对方。然而，一些常见的无线接口不支持覆盖 MAC 地址。因此，我们建议为此目的覆写以太网 MAC 地址。

> **注意**
>
> 请将无线接口的驱动程序添加到 `/etc/rc.conf` 的 `kld_list` 中以加载驱动程序，然后重启。否则在设置 lagg(4) 接口时驱动程序尚未加载会影响正常运行。

在此示例中，**em0** 是主接口，**wlan0** 是故障转移接口。**wlan0** 接口是由 **rtwn0** 物理无线接口创建的，并且以太网接口将配置为无线接口的 MAC 地址。首先，启用无线接口，请将 **rtwn0** 替换为系统的无线接口名称：

```sh
# ifconfig wlan0 create wlandev rtwn0
```

现在可以确定无线接口的 MAC 地址：

```sh
# ifconfig wlan0 ether
wlan0: flags=8802<BROADCAST,SIMPLEX,MULTICAST> metric 0 mtu 1500
	options=200001<RXCSUM,RXCSUM_IPV6>
	ether 20:0d:b0:c4:ab:59
```

`ether` 行将显示指定接口的 MAC 地址。现在，将以太网接口的 MAC 地址更改无线网卡的 MAC 地址：

```sh
# ifconfig em0 ether 20:0d:b0:c4:ab:59
```

确保 **em0** 接口已启用，然后创建 lagg(4) 接口，以 **em0** 作为主接口并故障转移到 **wlan0**：

```sh
# ifconfig em0 up
# ifconfig lagg0 create
# ifconfig lagg0 up laggproto failover laggport em0 laggport wlan0
```

然后，启动 DHCP 客户端以获取 IP 地址：

```sh
# dhclient lagg0
```

虚拟接口的状态应如下所示：

```sh
# ifconfig lagg0
lagg0: flags=1008843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST,LOWER_UP> metric 0 mtu 1500
	options=4e504bb<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,JUMBO_MTU,VLAN_HWCSUM,LRO,VLAN_HWFILTER,VLAN_HWTSO,RXCSUM_IPV6,TXCSUM_IPV6,HWSTATS,MEXTPG>
	ether 20:0d:b0:c4:ab:59
	hwaddr 00:00:00:00:00:00
	inet 192.168.5.7 netmask 0xffffff00 broadcast 192.168.5.255
	laggproto failover lagghash l2,l3,l4
	laggport: em0 flags=5<MASTER,ACTIVE>
	groups: lagg
	media: Ethernet autoselect
	status: active
	nd6 options=829<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL,STABLEADDR>
```

为确保此配置在重启后仍然生效，需在 **/etc/rc.conf** 文件中添加以下条目：

```sh
ifconfig_em0="ether 20:0d:b0:c4:ab:59"
wlans_rtwn0="wlan0"
ifconfig_wlan0="WPA"
cloned_interfaces="lagg0"
ifconfig_lagg0="up laggproto failover laggport em0 laggport wlan0 DHCP"
```
