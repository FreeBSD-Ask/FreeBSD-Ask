# FreeBSD 兼容的网络适配器

## 以太网卡

### Realtek（螃蟹卡）

#### Realtek RTL8125 2.5 G

常见的 2.5 G 网卡多为该型号，即螃蟹卡。可以在 Windows 设备管理器中查看，以下示例显示的即为该型号网卡：

![Realtek RTL8125 2.5 G](../.gitbook/assets/rtl8125.png)

>**技巧**
>
>RTL8125 在 FreeBSD 下默认没有驱动，需要手动安装。最简单的方法是通过手机 USB 共享网络临时上网，具体方法见本手册其他部分。安装网卡驱动后需重启系统。

安装方法如下所示。

### Realtek（螃蟹卡）网卡通用安装方法

#### 支持列表

* 5G 网卡
  * RTL8126
* 2.5G 网卡
  * RTL8125 / RTL8125B(G)
* 10/100/1000M 网卡
  * RTL8111B / RTL8111C / RTL8111D / RTL8111E / RTL8111F / RTL8111G
    RTL8111H / RTL8118(A) / RTL8119i / RTL8111L / RTL8111K
  * RTL8168B / RTL8168E / RTL8168H
  * RTL8111DP / RTL8111EP(P) / RTL8111FP
  * RTL8411 / RTL8411B
* 10/100M 网卡
  * RTL8101E / RTL8102E / RTL8103E / RTL8105E / RTL8106E / RTL8107E
  * rtl8401 / rtl8402

#### Realtek 以太网卡驱动安装方法

* 使用 pkg 安装：
  
```
pkg install realtek-re-kmod
```

* 使用 Ports 安装：

```sh
# cd /usr/ports/net/realtek-re-kmod/ 
# make install clean
```

>**注意**
>
>编译安装时，需要有一份源代码在 `/usr/src`。


>**技巧**
>
>如果你的 realtek 网卡仍存在断流，时有时无等情况，可以试试 [net/realtek-re-kmod198](https://www.freshports.org/net/realtek-re-kmod198/)，参见 [Bug 275882 - net/realtek-re-kmod: Problem with checksum offload since +199.00](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=275882)。

---

编辑 `/boot/loader.conf` 文件写入以下两行：

```ini
if_re_load="YES"                 # 设置开机自动加载 re 网卡驱动模块
if_re_name="/boot/modules/if_re.ko"   # 指定 re 网卡驱动模块路径
```

默认情况下已经启用巨型帧，如需关闭以优化网速（例如网速过慢时），可以执行以下操作：

```sh
# echo hw.re.max_rx_mbuf_sz="2048" >> /boot/loader.conf # 设置 re 网卡接收缓冲区最大尺寸为 2048，以优化网络性能
```

要启用 WOL 唤醒：

```sh
# echo hw.re.s5wol="1" >> /boot/loader.conf          # 启用 re 网卡的 S5 唤醒功能（支持休眠唤醒）
# echo hw.re.s0_magic_packet="1" >> /boot/loader.conf  # 启用 re 网卡的魔术包唤醒功能（Magic Packet Wake-on-LAN）
```

完成以上设置后，需要重启系统使其生效。

参考文献：

* [realtek-re-kmod Kernel driver for Realtek PCIe Ethernet Controllers](https://www.freshports.org/net/realtek-re-kmod)

### Intel 网卡

#### 2.5 G

英特尔 i225-V 和 i226-V 2.5G 网卡默认可驱动，无需额外配置。已在 I226-V rev04 型号上测试通过，使用 `igc` 驱动，网卡显示为 `igc0` 样式。


支持列表：

* I225-LM（商业端产品线，服务器用）
* I225-V（桌面端产品线，常见于家用台式机）
* I225-IT
* I225-K

参考文献：

* [igc -- Intel Ethernet Controller	I225 driver](https://man.freebsd.org/cgi/man.cgi?query=igc)

#### 千兆和百兆及其他以太网卡

i210 和 i211 网卡由 em 驱动，通常无需额外配置即可使用，但尚未进行测试。

支持列表及更多参见：

* [em, lem,	igb -- Intel(R)	PRO/1000 Gigabit Ethernet adapter driver](https://man.freebsd.org/cgi/man.cgi?query=igc)


## USB 网卡推荐

> **警告**
>
> 千兆和 2.5G 网卡 **在 15.0 CURRENT 以前都有时断时续的故障。** 如果你有更好的推荐（稳定不掉网）请联系我们。
>
>对于 2.5G USB 网卡，目前可选的型号似乎仅有 RTL8156 和 RTL8156B。

|      类型     |         品牌/型号         |           芯片组/参数          | 售价（¥） |                          备注                          |
| :---------: | :-------------------: | :-----------------------: | :---: | :--------------------------------------------------: |
|   USB 无线网卡  |   COMFAST CF-WU810N（已停产）   | RTL8188EUS 150M 2.4G 150M |   20  |                       由 rtwn 驱动                      |
|   USB 无线网卡  |    COMFAST CF-912AC   | RTL8812AU 2.4G & 5G 1200M |   60  |                       由 rtwn 驱动                      |
|   USB 无线网卡  |    COMFAST CF-915AC   |  RTL8811AU 2.4G & 5G 600M |   49  | 由 rtwn 驱动，套壳的，该型号为理论上支持，我没有实际测试过，如果不支持/支持，都请提交 issue |
|   USB 无线网卡  |        绿联 N300M       |    RTL8192EU 2.4G 300M    |   30  |   由 rtwn 驱动，该型号为理论上支持，我没有实际测试过，如果不支持/支持，都请提交 issue   |
|   USB 无线网卡  |     绿联 AC 1300M-双频    | RTL8812AU 2.4G & 5G 1300M |  129  |   由 rtwn 驱动，该型号为理论上支持，我没有实际测试过，如果不支持/支持，都请提交 issue   |
|   USB 以太网卡  |   绿联 USB 百兆网卡 CR110   |       AX88772A 100M       |   40  |                                                      |
|   USB 以太网卡  |   绿联 USB 千兆网卡 CM209   |       AX88179A 1000M      |   79  |                       **在 15.0 CURRENT 以前断流**                     |
|   USB 以太网卡  |  绿联 USB 2.5G 网卡 CM275 |        RTL8156 2.5G       |  189  |                         **在 15.0 CURRENT 以前断流**                               |
| Type-C 以太网卡 | 绿联 Type-C 转百兆网卡 30287 |       AX88772A 100M       |   59  |                                                      |
| Type-C 以太网卡 | 绿联 Type-C 转千兆网卡 CM199 |       AX88179A 1000M      |   99  |                       **在 15.0 CURRENT 以前断流**                                   |
| Type-C 以太网卡 |  绿联 Type-C 转 2.5G 网卡  |        RTL8156 2.5G       |  199  |                         **在 15.0 CURRENT 以前断流**                                 |

根据在树莓派 5 上的测试，AX88179A 和 RTL8156B 均可持续稳定运行，不会断流，最长连续运行时间超过 72 小时。

如果仅根据芯片组随意购买网卡，FreeBSD 很可能不支持其 `VendorID` 和 `ProductID`——例如 DOREWIN 达而稳。在这种情况下，需要联系驱动开发者将硬件信息加入驱动，并重新编译内核才能使用。

相关 Bug：

* [Bug 166724 - if_re(4): watchdog timeout](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=166724)
* [Bug 267514 - AXGE(4) ASIX AX88179A ue0: link state changed to DOWN](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=267514)
