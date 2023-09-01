# 第 2.7 节 ee 用法及网络配置


## ee 

### 基础入门

ee 的用法比 nano 还要简单上许多。是 FreeBSD 基本系统自带的文本编辑器。

比如

```shell-session
# ee a.txt
```

按 ESC 键，会显示提示框，按两次回车即可保存。

### 详细用法

编辑后按 `ESC` 会弹出提示框，输入 `a` 保存；

* \ 或 \[ 键 显示主选单。
* o 输入 ASCII code，例如输入 65 就会显示 A。
* u 跳到档案结尾。
* t 跳到档案开头。
* c 输入指令。在按了 Ctrl+c 后，上方选单会出现命令说明，例如你可以直接输入数字，表示将光标移到某一行。
* y 搜寻。按了 Ctrl+y 之后，你可以输入欲搜寻的字符串。如果要搜寻下一个该字符串，只要再按 Ctrl+x 即可。预设的搜寻是不分大小写的，如果要区分大小写，你可以按 Ctrl+c 并输入 case 即可。如果要取消只要再按 Ctrl+c 并输入 nocase。
* a 跳到行首。
* e 跳到行尾。
* d 删除光标所在位置的字符。
* j 贴上上一次所删除的字符。
* k 删除光标所在位置的一整行。
* l 贴上上一次删除的一整行内容。
* w 删除一个字。
* r 贴上上一次所删除的字。
* p 将光标移到上一行。
* n 将光标移到下一行。
* b 将光标移到上一个字，和方向键左键一样。
* f 将光标移到下一个字，和方向键右键一样。
* g 下一页。
* v 上一页。
* z 移到下一个字。
* 离开 ee。如果文件有修改过，它会问你是否要

### 网络配置

先 `ifconfig` 看看有没有网卡，没有那就不属于本节的范围之内了。请注意 `lo0` 并不是真实网卡，如果你只能看到这个说明你网卡没有被正确驱动。

示例输出：

```shell-session
root@ykla:~ # ifconfig
genet0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
	options=68000b<RXCSUM,TXCSUM,VLAN_MTU,LINKSTATE,RXCSUM_IPV6,TXCSUM_IPV6>
	ether dc:a6:1a:2e:f4:4t
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
root@ykla:~ #
```

以下内容同时适用于虚拟机和物理机。

默认情况下，FreeBSD 是正常联网的，如果不能可能是因为没有正确配置 DNS。

```shell-session
# ee /etc/resolv.conf
```

清空里面原有内容。添加以下内容.

```shell-session
nameserver 223.5.5.5 # 阿里 DNS，下同
nameserver 223.6.6.6
nameserver 8.8.8.8   # 谷歌 DNS，境外设备才用
```

之后重启一下网络配置

```shell-session
# /etc/netstart restart
```

尝试 ping 一下 163.com。（按下 ctrl + C 可中断）

示例输出：

```shell-session
root@ykla:~ # ping 163.com
PING 163.com (123.58.180.7): 56 data bytes
64 bytes from 123.58.180.7: icmp_seq=0 ttl=55 time=30.617 ms
64 bytes from 123.58.180.7: icmp_seq=1 ttl=55 time=30.608 ms
64 bytes from 123.58.180.7: icmp_seq=2 ttl=55 time=30.633 ms
^C
--- 163.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 30.608/30.619/30.633/0.010 ms
root@ykla:~ #
```

网络连通。



