# 第五节 IPFILTER (IPF)

IPF是一款开源软件，作者 Darren Reed。

如果想启用 ipf，可以执行以下命令： 
```
#ipfilter 

# cp /usr/share/examples/ipfilter/ipf.conf.sample /etc/ipf.rules #复制示例文件作为默认配置规则集文件， 否则 ipfilter 启动后会没有规则。示例文件自带的规则不会影响使用 

# service ipfilter enable #设置 ipfilter 开机启动，也可以通过 bsdconfig 设置 ipfilter_enable 

# service ipfilter start #启动 ipfilter #ipnat sudo cp /usr/share/examples/ipfilter/ipnat.conf.sample /etc/ipnat.rules #复制示例文件作为默认配置规则集文件，否则 ipnat 无法启动 

# service ipnat enable #设置 ipnat 开机启动，也可以通过 bsdconfig 设置 ipnat_enable 

# service ipnat start #启动 ipnat。注意，ipfilter 服务重启后，ipnat 也需要重启 ipf 的管理命令主要用 ipf、ipfstat 和 ipnat，常用操作示例如下： 
```
```
# ipf -E #启动 ipfilter，相当于 service ipfilter start 

# ipf -D #停止 ipfilter，相当于 server ipfilter stop 

# ipf -f /etc/ipf.rules #加载规则集文件中的规则 ipfstat #查看所有规则 

# ipfstat -iohn #查看规则，i 表示输入规则，o 表示输出规则，h 表示通过该规则的流量，n 表示记录编号

# ipfstat -t #进入监控模式，按 Q 退出 

# ipf -Fa #清理已加载的规则 

# ipnat -f /etc/ipnat.rules #加载规则集文件中的 nat 规则 

# ipnat -s #汇总并显示 nat 状态 ipnat -lh #列表显示 nat 规则，加 h 表示同时显示通过该规则的流量 

# ipnat -CF #清理已加载的 nat 规则 不过以上操作并没有对规则的管理，因此还需要修改规则集文件，常用示例如下：block all # #拒绝所有访问。ipfilter 是默认明示禁止的防火墙，因此需要通过下列规则禁止所有访问 block in all #block 是动作，block 表示拒绝，pass 表示通过；in 为数据方向，in 为入，out 为出，在 ipfilter 里数据方向是必须的；all 是 from any to any 的简写，表示从源地址到目标地址，地址通常用网段(如 192.168.1.0/24)或 IP 地址(如 192.168.1.100)，any 是特殊词，表示任何地址 

block out all #放开回环接口的访问权限，回环接口不对外部 

pass in quick on lo0 all #quick 关键字表示若规则匹配，就停止执行，不会再执行后续规则 

pass out quick on lo0 all #增加 TCP 协议访问 80 端口的规则 

pass in quick proto tcp from any to 192.168.1.184 port = 80 #允许任何设备以 TCP 协议访问本机 80 端口。 其中 proto tcp 是访问协议，常用值有 tcp、udp、tcp/udp、icmp，不写则表示支持所有协议；port = 80 是 端口，写在目标地址之后为目标端口，源地址之后未写，表示从源地址的任何端口发起访问 

pass out quick proto tcp from 192.168.1.184 to any #允许回显信息给任何访问的设备 #增加 80 端口到 8080 端口流量转发的规则 

pass in quick proto tcp from any to 192.168.1.184 port = 80 #首先放开 ipfilter 的访问限制 rdr em0 192.168.1.184 port 80 -> 192.168.1.184 port 8080 #由于测试机只有一块网卡，因此转发仅限本机 

pass out quick proto icmp from 192.168.1.184 to any icmp-type 8 keep state #允许本机 ping 任何外部设备。 其中 ICMP type 8 是查询请求；keep state 表示维持状态。如与下例合并，会完全放开 ping 的功能 

pass in quick proto icmp from any to 192.168.1.184 icmp-type 8 keep state #允许任何外部设备 ping 本机 

pass out quick proto icmp from 192.168.1.184 to any icmp-type 0 #允许 traceroute 命令以 ICMP 协议执行 

pass out quick proto udp from 192.168.1.184 to any port 33434 >< 34500 keep state #traceroute 默认协议 UDP， 端口号从 33434 开始，每转发一次端口号加 1 
```

下面根据我的操作系统整理规则集文件/etc/ipf.rules 如下：

```
block in all

block out all 

pass in quick on lo0 all 

pass out quick on lo0 all #设置任何设备可以访问服务器的 22、80、443、4200、10000 端口 

pass in quick proto tcp from any to 192.168.1.184 port = { 22,80,443,4200,10000 } 

pass out quick proto tcp from 192.168.1.184 port = { 22,80,443,4200,10000 } to any pass out quick proto tcp from 192.168.1.184 to any port = { 80,443 } keep state #设置服务器访问任何网络设 备的 80、443 端口 

pass out quick proto udp from any to any port = 53 keep state #设置访问 DNS 服务器 

pass out quick proto udp from any to any port = 67 keep state #设置访问 DHCP 服务器 

pass out quick proto icmp from 192.168.1.184 to any icmp-type 8 keep state

pass in quick proto icmp from any to 192.168.1.184 icmp-type 8 keep state 

pass out quick proto icmp from 192.168.1.184 to any icmp-type 0 

pass out quick proto udp from 192.168.1.184 to any port 33434 >< 34500 keep state

pass in quick proto tcp from any to 192.168.1.184 port = 8080 #数据转发前要放开相应端口 
```

然后再整理 NAT 规则集文件/etc/ipnat.rules 如下： 

```
# rdr em0 192.168.1.184 port 8080 -> 192.168.1.184 port 80 #设置本机 8080 到 80 端口的映射 
```
保存文件，接下来在终端执行命令： 

```
# ipf -Fa -f /etc/ipf.rules #加载规则集文件中的规则

# ipnat -CF -f /etc/ipnat.rules #加载规则集文件中的 nat 规则就可以看到效果了。
```
