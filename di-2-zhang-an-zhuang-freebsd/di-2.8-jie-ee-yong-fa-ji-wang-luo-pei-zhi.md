# 第 2.8 节 ee 用法及网络配置

## ee 文本编辑器

### 基础入门

ee 的用法比 nano 还要简单上许多。是 FreeBSD 基本系统自带的文本编辑器。

比如

```shell-session
# ee a.txt
```

可以直接编辑，就和 nano 或记事本一样。

按 **ESC 键**，会显示提示框，按两次 **回车键** 即可保存。

### 详细用法（用不上，不用看系列）

编辑后按 `ESC` 会弹出提示框，按两次 **回车键** 即可保存；

要进行文本插入之外的任何操作，用户必须使用控制键（**Control** 键，用 "**Ctrl** +" 表示，与字母键一起按下，例如 **Ctrl** + a）和键盘上的功能键（如 **Next Page**、**Prev Page**、箭头键等）。由于并非所有终端都有功能键，*ee* 将基本的光标移动功能分配给控制键，同时也使用键盘上的更直观的按键（如果有）。例如，要向上移动光标，用户可以使用向上箭头键或 ****Ctrl** + u**。

- **Ctrl** +a         提示插入字符的十进制值。
- **Ctrl** +b         移动到文本底部。
- **Ctrl** +c         获取命令提示。
- **Ctrl** +d         向下移动光标。
- **Ctrl** +e         提示要搜索的字符串。
- **Ctrl** +f         恢复上次删除的字符。
- **Ctrl** +g         移动到行首。
- **Ctrl** +h         退格。
- **Ctrl** +i         制表符。
- **Ctrl** +j         插入新行。
- **Ctrl** +k         删除光标所在字符。
- **Ctrl** +l         向左移动光标。
- **Ctrl** +m         插入新行。
- **Ctrl** +n         移动到下一页。
- **Ctrl** +o         移动到行尾。
- **Ctrl** +p         移动到上一页。
- **Ctrl** +r         向右移动光标。
- **Ctrl** +t         移动到文本顶部。
- **Ctrl** +u         向上移动光标。
- **Ctrl** +v         恢复上次删除的单词。
- **Ctrl** +w         删除光标位置开始的单词。
- **Ctrl** +x         搜索。
- **Ctrl** +y         从光标位置删除到行尾。
- **Ctrl** +z         恢复上次删除的行。
- **Ctrl** +\[ (ESC)   弹出菜单。

## 网络配置

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
**Ctrl** +C
--- 163.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 30.608/30.619/30.633/0.010 ms
root@ykla:~ #
```

网络连通。


### 将网卡设为混杂模式

```shell-session
ifconfig_xxx="inet x.x.x.x netmask x.x.x.x promisc"
```
#### 参考文献

- [ifconfig(8)](https://man.freebsd.org/cgi/man.cgi?ifconfig(8))
- [ee(1)](https://man.freebsd.org/cgi/man.cgi?ee(1))

