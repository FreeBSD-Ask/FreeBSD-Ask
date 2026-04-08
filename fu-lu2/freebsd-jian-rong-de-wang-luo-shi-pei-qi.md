# FreeBSD 兼容的网络适配器

下面介绍 FreeBSD 兼容的网络适配器相关信息。

## 以太网卡

以太网卡是最常见的网络适配器类型，FreeBSD 对多种以太网卡提供了良好的支持。

### Realtek（螃蟹卡）

#### Realtek RTL8125 2.5 G

Realtek RTL8125 是一款常见的 2.5 G 以太网卡。在消费级市场中，常见的 2.5 G 网卡多采用该型号芯片。在安装 FreeBSD 前，可以在 Windows 设备管理器中查看硬件标识，确认网卡型号是否为 RTL8125。

![Realtek RTL8125 2.5 G](../.gitbook/assets/rtl8125.png)

> **技巧**
>
> RTL8125 在 FreeBSD 下默认没有驱动，需要手动安装。最简单的方法是通过手机 USB 共享网络临时上网，具体方法见本手册其他部分。安装网卡驱动后需重启系统。

安装方法如下。

### Realtek（螃蟹卡）网卡通用安装方法

除了特定型号的安装方法外，Realtek 网卡还有通用的安装方式。下面介绍 Realtek 网卡的通用安装方法。

#### 支持列表

在安装驱动之前，需要确认当前网卡型号是否在支持列表中。

- 5 G 网卡
  - RTL8126
- 2.5 G 网卡
  - RTL8125 / RTL8125B(G)
- 10/100/1000M 网卡
  - RTL8111B / RTL8111C / RTL8111D / RTL8111E / RTL8111F / RTL8111G
    RTL8111H / RTL8118(A) / RTL8119I / RTL8111L / RTL8111K
  - RTL8168B / RTL8168E / RTL8168H
  - RTL8111DP / RTL8111EP(P) / RTL8111FP
  - RTL8411 / RTL8411B
- 10/100 M 网卡
  - RTL8101E / RTL8102E / RTL8103E / RTL8105E / RTL8106E / RTL8107E
  - rtl8401 / rtl8402

#### Realtek 以太网卡驱动安装方法

确认网卡型号在支持列表中后，即可开始安装驱动。

- 使用 pkg 安装：

```sh
pkg install realtek-re-kmod
```

- 使用 Ports 安装：

```sh
# cd /usr/ports/net/realtek-re-kmod/ 
# make install clean
```

在编译安装时，需要有一份源代码在 `/usr/src`。

```sh
/usr/
├── ports/
│   └── net/
│       └── realtek-re-kmod/  # Realtek 网卡驱动 Ports 目录
└── src/                      # 系统源代码目录（编译驱动时需要）
```

> **技巧**
>
> 如果 Realtek 网卡仍存在断流、时有时无等情况，可以试试 net/realtek-re-kmod198[EB/OL]. [2026-03-26]. <https://www.freshports.org/net/realtek-re-kmod198/>，参见：Bug 275882 - net/realtek-re-kmod: Problem with checksum offload since +199.00[EB/OL]. [2026-03-26]. <https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=275882>。

---

相关文件结构：

```sh
/boot/
├── loader.conf        # 系统启动加载器配置文件
└── modules/
    └── if_re.ko       # re 网卡驱动内核模块
```

编辑 `/boot/loader.conf` 文件，写入以下两行：

```ini
if_re_load="YES"                 # 设置开机自动加载 re 网卡驱动模块
if_re_name="/boot/modules/if_re.ko"   # 指定 re 网卡驱动模块路径
```

默认情况下已启用巨型帧。巨型帧是指大于标准以太网帧（1500 字节）的帧，通常为 9000 字节。巨型帧可以减少网络开销，提高传输效率，但在某些网络环境下可能导致兼容性问题。如需关闭以优化网速（例如网速过慢时），可以执行以下操作：

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

- realtek-re-kmod Kernel driver for Realtek PCIe Ethernet Controllers[EB/OL]. [2026-03-25]. <https://www.freshports.org/net/realtek-re-kmod>. FreshPorts 上的 Realtek 网卡驱动页面，提供安装信息与版本更新。

### Intel 网卡

Intel 网卡也是常见的网络适配器类型，FreeBSD 对其有良好的支持。

#### 2.5 G

英特尔 i225-V 和 i226-V 2.5 G 网卡默认可驱动，无需额外配置。已在 I226-V rev04 型号上测试通过，使用 `igc` 驱动，网卡显示为 `igc0` 样式。

支持列表：

- I225-LM（商业端产品线，服务器用）
- I225-V（桌面端产品线，常见于家用台式机）
- I225-IT
- I225-K

参考文献：

- igc -- Intel Ethernet Controller I225 driver[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?query=igc>. 手册页，详述了 Intel i225 网卡驱动的使用方法。

#### 千兆和百兆及其他以太网卡

除了 2.5 G 网卡外，Intel 还有其他多种型号的以太网卡。i210 和 i211 网卡由 em 驱动，通常无需额外配置即可使用，但尚未进行测试。

支持列表及更多参见：

- em, lem, igb -- Intel(R) PRO/1000 Gigabit Ethernet adapter driver[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?query=igc>. 手册页，涵盖 Intel PRO/1000 系列千兆网卡驱动说明。

## USB 网卡推荐

USB 网卡具有便携性强、使用方便的特点，适合临时使用或设备没有内置网卡的情况。下面介绍 USB 网卡的相关推荐。

> **警告**
>
> 千兆和 2.5 G 网卡在 15.0-RELEASE 以前都有时断时续的故障。如果有更好的推荐（稳定不掉线）请提交 PR。
>
> 对于 2.5 G USB 网卡，目前可选的型号似乎仅有 RTL8156 和 RTL8156B。

| 类型 | 品牌/型号 | 芯片组/参数 | 售价（¥） | 备注 |
| ---- | --------- | ----------- | --------- | ---- |
| USB 以太网卡 | 绿联 USB 百兆网卡 CR110 | AX88772A 100M | 40 | / |
| USB 以太网卡 | 绿联 USB 千兆网卡 CM209 | AX88179A 1000M | 79 | 在 15.0-RELEASE 以前断流 |
| Type-C 以太网卡 | 绿联 Type-C 转百兆网卡 30287 | AX88772A 100M | 59 | / |
| Type-C 以太网卡 | 绿联 Type-C 转千兆网卡 CM199 | AX88179A 1000M | 99 | 在 15.0-RELEASE 以前断流。在树莓派 5 上的测试表明，目前 15.0-RELEASE 下的 AX88179A 和 RTL8156B 网卡均可持续稳定运行，不会断流，最长连续运行时间超过 72 小时 |
| USB 无线网卡 | COMFAST CF-WU810N（已停产） | RTL8188EUS 150 M 2.4 G 150 M | 20 | 由 rtwn 驱动 |
| USB 无线网卡 | COMFAST CF-912AC | RTL8812AU 2.4 G & 5 G 1200 M | 60 | 由 rtwn 驱动 |
| USB 无线网卡 | COMFAST CF-915AC | RTL8811AU 2.4 G & 5 G 600 M | 49 | 由 rtwn 驱动，理论上支持，未经实际测试，无论是否支持，都请提交 issue |
| USB 无线网卡 | 绿联 N300 M | RTL8192EU 2.4 G 300 M | 30 | 由 rtwn 驱动，理论上支持，未经实际测试，无论是否支持，都请提交 issue |
| USB 无线网卡 | 绿联 AC 1300 M-双频 | RTL8812AU 2.4 G & 5 G 1300 M | 129 | 由 rtwn 驱动，理论上支持，未经实际测试，无论是否支持，都请提交 issue |
| USB 以太网卡 | 绿联 USB 2.5 G 网卡 CM275 | RTL8156 2.5 G | 189 | 在 15.0-RELEASE 以前断流 |
| Type-C 以太网卡 | 绿联 Type-C 转 2.5 G 网卡 | RTL8156 2.5 G | 199 | 在 15.0-RELEASE 以前断流 |

VendorID（厂商标识）和 ProductID（产品标识）是 USB/PCI 设备的两个标准标识符，驱动程序通过这两个 ID 来识别和匹配硬件。

相同芯片组的硬件可能由不同厂商生产，使用不同的 VendorID/ProductID。

如果仅根据芯片组随意购买网卡，FreeBSD 很可能不支持其 `VendorID` 和 `ProductID`，例如 DOREWIN 达而稳。

在这种情况下，需要联系驱动开发者将硬件信息加入驱动，并重新编译内核才能使用。

相关 Bug 反馈：

- Bug 166724 - if_re(4): watchdog timeout[EB/OL]. [2026-03-25]. <https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=166724>. 记载了 Realtek 网卡驱动看门狗超时问题的历史 Bug 报告。
- Bug 267514 - AXGE(4) ASIX AX88179A ue0: link state changed to DOWN[EB/OL]. [2026-03-25]. <https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=267514>. 记载了 ASIX USB 千兆网卡连接不稳定问题的 Bug 报告。

## 课后习题

1. 在 FreeBSD 系统中查找 realtek-re-kmod 驱动源代码，分析该驱动如何处理巨型帧，修改 hw.re.max_rx_mbuf_sz 参数并验证网络性能变化。

2. 尝试使用 pciconf 或 usbconfig 工具查看某 USB 网卡的 VendorID 和 ProductID，查找该网卡在 FreeBSD 中的驱动支持情况，分析为什么某些厂商硬件虽然使用相同芯片组却不被系统默认支持。
