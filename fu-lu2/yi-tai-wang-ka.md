# FreeBSD 兼容的网络适配器

## 以太网卡

### Realtek（螃蟹卡）

#### Realtek RTL8125 2.5 G

常见 2.5 G 的网卡都是这个，即螃蟹卡。可以在 Windows 的设备管理器中查看，以下示例就是这个卡：

![Realtek RTL8125 2.5 G](../.gitbook/assets/rtl8125.png)

>**技巧**
>
>RTL8125 在 FreeBSD 下默认是没有驱动的，需要手动安装。最简单的办法是使用通过手机 USB 共享网络临时上网，方法见本手册其余部分。安装了网卡重启即可。

安装方法同下。

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

#### 安装方法

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

配置：

```sh
# ee /boot/loader.conf # 写入以下两行
if_re_load="YES"
if_re_name="/boot/modules/if_re.ko"
```

默认情况下已经开启巨型帧，要关闭（影响网速，如网速过慢可关闭之）：

```sh
# echo hw.re.max_rx_mbuf_sz="2048" >> /boot/loader.conf
```

要启用 WOL 唤醒：

```sh
# echo hw.re.s5wol="1"  >> /boot/loader.conf
# echo hw.re.s0_magic_packet="1"  >> /boot/loader.conf
```

以上设置完毕后均需重启。

参考文献：

* [realtek-re-kmod Kernel driver for Realtek PCIe Ethernet Controllers](https://www.freshports.org/net/realtek-re-kmod)

### Intel 网卡

#### 2.5 G

英特尔 i225-V、i226-V 2.5G 网卡默认可驱动，亦无需配置。已测试（I226-V rev04）。由 `igc` 驱动。网卡显示为 `igc0` 样式。

支持列表：

* I225-LM（商业端产品线，服务器用）
* I225-V（桌面端产品线，常见于家用台式机）
* I225-IT
* I225-K

参考文献：

* [igc -- Intel Ethernet Controller	I225 driver](https://man.freebsd.org/cgi/man.cgi?query=igc)

#### 千兆和百兆及其他以太网卡

i210、i211 由 em 驱动。默认应该就能驱动，无需配置，但未测试。

支持列表及更多参见：

* [em, lem,	igb -- Intel(R)	PRO/1000 Gigabit Ethernet adapter driver](https://man.freebsd.org/cgi/man.cgi?query=igc)


## USB 网卡推荐

> **警告**
>
> 千兆和 2.5G 网卡 **在 15.0 CURRENT 以前都有时断时续的故障。** 如果你有更好的推荐（稳定不掉网）请联系我们。
>
> 对于 2.5G USB 网卡，似乎只有 RTL 8156 和 RTL 8156B 可选。

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

**经过在树莓派 5 上的测试，AX88179A 和 RTL8156B 均可连续正常工作不断流，并维持 72 小时以上。**

**如果随便按芯片组来买网卡，FreeBSD 大概率未支持其 `VendorID` 和 `ProductID`——比如“DOREWIN 达而稳”。这种情况下要联系开发者将你的硬件写入驱动，然后重新编译内核才可以。**

>相关 Bug：
>
> * [Bug 166724 - if_re(4): watchdog timeout](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=166724)
>
> * [Bug 267514 - AXGE(4) ASIX AX88179A ue0: link state changed to DOWN](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=267514)
