# 第三节 IPFW

## （一）介绍说明：

IPFIREWALL (IPFW) 是一个由 FreeBSD 发起的防火墙应用软件， 它由 FreeBSD 的志愿者成员编写和维护。

在 FreeBSD 12 中，ipfw 已经默认被编译进内核了，它默认会有一条规则，规则号为 `65536`，是不可以删除的，这条规则会把所有流量都切断，所以还没配置好之前，千万不要随意启动 ipfw，否则就会面临无法连上远程 FreeBSD 的问题。

## （二）配置ipfw：

1. 执行以下命令：

```
# sysrc firewall_enable="YES"  # 允许防火墙开机自启
# sysrc firewall_type="open"  # 让系统把流量通过，这样就可以使用防火墙
# sysrc firewall_script="/etc/ipfw.rules"  # 制定ipfw规则的路径，我们待会儿在这里编辑规则
# sysrc firewall_logging="YES"  # 这样ipfw就可以打日志
# sysrc firewall_logif="YES"  # 把日志打到 `ipfw0` 这个设备里
```

2. 编辑 `/etc/ipfw.rules` 文件：

```
# ee /etc/ipfw.rules 

IPF="ipfw -q add"
ipfw -q -f flush

# loopback 
$IPF 10 allow all from any to any via lo0
$IPF 20 deny all from any to 127.0.0.0/8
$IPF 30 deny all from 127.0.0.0/8 to any
$IPF 40 deny tcp from any to any frag

# statefull
$IPF 50 check-state
$IPF 60 allow tcp from any to any established
$IPF 70 allow all from any to any out keep-state
$IPF 80 allow icmp from any to any

# open port for ssh
$IPF 110 allow tcp from any to any 22 out
$IPF 120 allow tcp from any to any 22 in

# open port for samba
$IPF 130 allow tcp from any to any 139 out
$IPF 140 allow tcp from any to any 139 in
$IPF 150 allow tcp from any to any 445 out
$IPF 160 allow tcp from any to any 445 in
$IPF 170 allow udp from any to any 137 out
$IPF 180 allow udp from any to any 137 in
$IPF 190 allow udp from any to any 138 out
$IPF 200 allow udp from any to any 138 in


# deny and log everything 
$IPF 500 deny log all from any to any
```

额外说明： samba 开放 tcp/139,445 端口，udp/137,138 端口

3. 启动 ipfw：

```
# service ipfw start

Firewall rules loaded.
Firewall logging enabled.
ifconfig: interface ipfw0 already exists
Firewall logging pseudo-interface (ipfw0) created.
```

4. 查看 ipfw 状态：

```
# service ipfw status

ipfw is enabled
```

5. 查看 ipfw 规则条目

```
# ipfw list

00010 allow ip from any to any via lo0
00020 deny ip from any to 127.0.0.0/8
00030 deny ip from 127.0.0.0/8 to any
00040 deny tcp from any to any frag
00050 check-state :default
00060 allow tcp from any to any established
00070 allow ip from any to any out keep-state :default
00080 allow icmp from any to any
00110 allow tcp from any to any 22 out
00120 allow tcp from any to any 22 in
00500 deny log ip from any to any
65535 deny ip from any to any
```
