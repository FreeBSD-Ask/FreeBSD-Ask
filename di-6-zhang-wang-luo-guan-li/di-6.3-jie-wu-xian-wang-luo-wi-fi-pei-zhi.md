# 6.3 无线网络（Wi-Fi）配置

FreeBSD 支持多种无线网卡和认证方式。

> **技巧**
>
> Wi-Fi 并不是任何单词的缩写。该词仅为 [Wi-Fi 联盟](https://www.wi-fi.org/)（Wi-Fi Alliance）持有的注册商标，并无任何引申义，如“Wireless Fidelity”。（Doctorow C. WiFi isn’t short for “Wireless Fidelity”[EB/OL]. (2005-11-08)[2026-04-21]. <https://boingboing.net/2005/11/08/wifi-isnt-short-for.html>.）

## 快速连接（基于 COMFAST CF-912AC 1200M 802.11AC）

### 无线网络配置

基本的无线网络由多个站点组成，这些站点通过在 2.4GHz、5GHz 或 6GHz 频段广播的无线电通信。配置无线网络包含三个基本步骤：

1. 扫描并选择接入点
2. 认证站点
3. 配置 IP 地址或使用 DHCP

### 示例网卡

本节以 COMFAST CF-912AC 1200M 802.11AC 无线网卡为例，介绍一般无线网卡的驱动配置方法。该网卡采用 Realtek 芯片组。其他采用 Realtek 芯片的网卡配置方法类似。

### 识别无线网卡

在配置无线网络前，需要确认系统是否能够识别无线网卡。可通过查询内核无线设备列表来确认硬件识别状态，该命令会显示系统中可用的无线网络接口设备：

```sh
# sysctl net.wlan.devices
net.wlan.devices: rtwn0
```

上述输出中的 `rtwn0` 是示例网卡（COMFAST CF-912AC）的设备名称，实际输出可能因硬件而异。如果输出中冒号 `:` 后没有内容，则说明无线网卡未被识别，此时可能需要检查硬件连接或更换兼容性更好的无线网卡。

### 虚拟无线接口机制

在 FreeBSD 中，无线网络采用分层架构设计，需要创建一个虚拟的无线接口 `wlan0`，并将其绑定到物理无线网卡上才能使用。

创建一个新的无线接口 `wlan0`，并将其绑定到物理设备 `rtwn0`：

```sh
# ifconfig wlan0 create wlandev rtwn0
```

上述命令中，`rtwn0` 为 `sysctl net.wlan.devices` 输出中的物理网卡名称，需根据实际硬件进行替换（~~除非也使用 COMFAST CF-912AC 1200M 802.11AC~~）。

创建完成后，可使用 `ifconfig` 命令查看接口状态（以下输出已省略以太网卡和 `lo0` 接口）：

```sh
# ifconfig

……此处省略一部分……

wlan0: flags=8802<BROADCAST,SIMPLEX,MULTICAST> metric 0 mtu 1500
	options=200001<RXCSUM,RXCSUM_IPV6>
	ether 20:0d:b0:c4:ab:59
	groups: wlan
	ssid "" channel 1 (2412 MHz 11b)
	regdomain FCC country US authmode OPEN privacy OFF txpower 30 bmiss 7
	scanvalid 60 wme bintval 0
	parent interface: rtwn0
	media: IEEE 802.11 Wireless Ethernet autoselect (autoselect)
	status: no carrier
	nd6 options=29<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL>
```

在正常情况下，输出中应包含 `wlan0` 接口。

### 扫描无线网络

在连接到无线网络之前，需要先扫描周围可用的无线网络。可使用 ifconfig(8) 扫描可用的无线网络：

```sh
# ifconfig wlan0 up scan
SSID/MESH ID                      BSSID              CHAN RATE    S:N     INT CAPS

……此处省略一部分……

test_5G                           50:d6:c5:93:d7:64   36   54M  -78:-95   100 EP   APCHANREP WPA RSN WPS BSSLOAD HTCAP VHTCAP VHTOPMODE WME
```

参数说明：

- **SSID/MESH ID** 标识网络名称。
- **BSSID** 标识接入点的 MAC 地址。
- **CHAN** 信道。
- **RATE** 速率。
- **S:N** 信号强度和质量。
- **INT** 信标间隔。
- **CAPS** 字段标识每个网络的类型和运行站点的功能。

扫描结果会显示可用的无线网络列表。

### SSID 的定义与作用

服务集标识符（Service Set Identifier，SSID）是无线网络的名称标识，用于区分不同的无线网络。

将 `wlan0` 接口连接到 SSID 为 `test_5G` 的无线网络（适用于无密码的开放网络）：

```sh
# ifconfig wlan0 ssid test_5G
```

上述命令中，`test_5G` 为示例 Wi-Fi 名称（SSID），需替换为实际网络名称。

若无法扫描到 Wi-Fi 网络，可能需要修改无线区域设置或路由器信道。此时可按以下步骤重新配置：

```sh
# ifconfig wlan0 destroy
# ifconfig wlan0 create wlandev rtwn0
# ifconfig wlan0 country HR regdomain ETSI
```

第一条命令销毁现有 `wlan0` 接口并释放其占用的资源，避免出现 `ifconfig: SIOCS80211: Device busy` 错误；第二条命令重新创建无线接口并绑定到物理设备；第三条命令设置无线国家码为 HR 并使用 ETSI 无线频段规范，当目标网络使用大于 48 的信道（DFS 信道）时需要进行此设置，如信道小于 48，可省略该步骤。

完成上述配置后，重启网络服务以接入 Wi-Fi：

```sh
# service netif restart
# dhclient wlan0
```

第一条命令重启网络接口服务，第二条命令为 `wlan0` 接口获取动态 IP 地址。

### 使用 WPA2 认证

对于加密的无线网络，需要使用 Wi-Fi 保护访问（Wi-Fi Protected Access，WPA）配置文件进行连接。WPA2/3 是目前主流的无线网络安全协议，提供了数据加密与身份认证功能。

无线网络中的认证过程由 wpa_supplicant(8) 管理。创建 **/etc/wpa_supplicant.conf** 配置文件，内容如下：

```ini
ctrl_interface=/var/run/wpa_supplicant   # 可选，控制接口路径，用于 wpa_supplicant 与 wpa_cli 等工具通信
fast_reauth=1                             # 可选，启用快速重新认证，加快已认证网络的重连速度
network={
ssid="test_5G"
psk="freebsdcn"
}
```

配置说明：

- `ssid` 指定要连接的无线网络 SSID（Wi-Fi 名称），此处示例为 `test_5G`
- `psk` 指定无线网络的密码，此处示例为 `freebsdcn`

若无法获取无线网络的服务集标识符（SSID）和预共享密钥（PSK，Pre-Shared Key），可联系网络管理员或重置网络设备以获取凭据。

下一步在 **/etc/rc.conf** 文件中配置无线连接。使用动态地址：

```sh
# sysrc ifconfig_wlan0="WPA DHCP"
```

然后重启网络：

```sh
# service netif restart
```

如果网络连接正常，再行永久性配置。在 **/etc/rc.conf** 文件中添加或修改相关配置条目：

```ini
wlans_rtwn0="wlan0"                      # 将物理无线设备 rtwn0 绑定到 wlan0 接口
ifconfig_wlan0="WPA SYNCDHCP"           # 配置 wlan0 使用 WPA 并通过 DHCP 自动获取 IP 地址
create_args_wlan0="country HR regdomain ETSI"  # 创建 wlan0 接口时设置无线国家码为 HR，并使用 ETSI 频段规范；如果信道大于 48（DFS），则需进行此设置。如信道小于 48，可以不设置
```

### 无线网络配置文件结构

FreeBSD 无线网络涉及以下配置文件。

```sh
/etc/
├── rc.conf              # 系统启动配置文件
└── wpa_supplicant.conf  # WPA 无线网络配置文件
```

完成上述配置后，重启系统或者网络服务以使所有配置生效。

重启后，使用 `ifconfig` 查看连接情况，在正常情况下可看到已成功连接（示例输出中 IP 为 192.168.31.178）：

```sh
……省略一部分输出……

wlan0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
	options=200001<RXCSUM,RXCSUM_IPV6>
	ether 11:7c:e8:c4:ab:58
	inet 192.168.31.178 netmask 0xffffff00 broadcast 192.168.31.255
	groups: wlan
	ssid test_5G channel 36 (5180 MHz 11a ht/20) bssid 50:d6:c5:93:d7:64
	regdomain NONE country CN authmode WPA2/802.11i privacy ON
	deftxkey UNDEF TKIP 2:128-bit txpower 17 bmiss 7 mcastrate 6
	mgmtrate 6 scanvalid 60 ht20 ampdulimit 64k ampdudensity 4 shortgi
	-stbc -uapsd wme roaming MANUAL
	parent interface: rtwn0
	media: IEEE 802.11 Wireless Ethernet MCS mode 11na
	status: associated
	nd6 options=29<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL>
```

## 英特尔无线网卡驱动概况

英特尔（Intel）网卡是目前使用广泛的无线网卡之一。iwlwifi 驱动 [适用于](https://wiki.freebsd.org/WiFi/Iwlwifi/Chipsets) `AC 8265、AC 9260、AC 9560、AX200、AX201、AX210、AX211`，iwm 驱动 [适用于](https://wiki.freebsd.org/WiFi/Iwm) `AC 3160、AC 3165、AC 3168、AC 7260、AC 7265、AC 8260、AC 8265、AC 9260、AC 9270、AC 946X` 等型号。两者覆盖的芯片范围有部分重叠但不完全包含，见 [英特尔 ® 无线适配器的 Linux* 支持](https://www.intel.cn/content/www/cn/zh/support/articles/000005511/wireless.html)。

在 **/etc/rc.conf** 文件中添加以下配置：

```ini
wlans_iwlwifi0="wlan0"        # 将物理无线设备 iwlwifi0 绑定到 wlan0 接口
ifconfig_wlan0="WPA SYNCDHCP"  # 配置 wlan0 使用 WPA 并通过 DHCP 自动获取 IP 地址
```

创建 **/etc/wpa_supplicant.conf** 配置文件：

```sh
network={
ssid="WIFI 名称（SSID）"
psk="WIFI 密码"
}
```

完成配置后，执行以下命令启动 Wi-Fi 进行测试：

```sh
# ifconfig wlan0 create wlandev iwlwifi0
# /etc/rc.d/netif start wlan0
```

第一条命令创建 `wlan0` 接口并绑定到物理无线设备 `iwlwifi0`，第二条命令启动 `wlan0` 接口。

故障排除与未竟事宜请参考：[wiki/WiFi/Iwlwifi](https://wiki.freebsd.org/WiFi/Iwlwifi)

### 参考文献

- FreeBSD Project. iwm(4) -- Intel IEEE 802.11ac wireless network driver[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=iwm(4)>. Intel 无线网卡驱动技术文档。
- FreeBSD Project. iwlwifi(4) -- Intel IEEE 802.11a/b/g/n/ac/ax/be wireless network driver[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=iwlwifi(4)>. Intel 无线网卡驱动技术文档。

## 博通（Broadcom）网卡驱动

博通（Broadcom）是另一家常用的无线网卡厂商。FreeBSD 内置的 Broadcom（博通）网卡驱动主要有两种：`bwi` 和 `bwn`，`bwi` 支持较旧型号，`bwn` 支持较新型号。两者的支持范围部分重叠，但 `bwn` 对硬件的兼容性更好。

关于驱动选择的详细信息，请参考 Fuller L. Broadcom WiFi Improvements for FreeBSD[EB/OL]. (2018-01-22)[2026-04-05]. <https://web.archive.org/web/20240203102135/https://www.landonf.org/code/freebsd/Broadcom_WiFi_Improvements.20180122.html>.

### 示例：BCM4301、BCM4303、BCM4306 rev 2

根据参考文献，上述型号的网卡只能使用 `bwi` 驱动。

首先，在 **/boot/loader.conf** 文件中添加以下配置，设置系统在启动时加载 `bwi` 驱动：

```sh
if_bwi_load="YES"
```

然后使用 Ports 安装 Broadcom 无线设备的固件（该固件未提供二进制包）：

```sh
# cd /usr/ports/net/bwi-firmware-kmod/
# make install clean
```

可先通过 USB 或以太网共享网络安装，也可以提前将所需依赖下载到指定目录。

在 **/etc/rc.conf** 文件中添加以下配置，将物理无线设备 `bwi0` 绑定到 `wlan0` 接口：

```ini
wlans_bwi0="wlan0"
```

完成上述配置后，重启系统。

### 示例：配置 bwn 驱动

安装 Broadcom 无线设备的固件：

```sh
# cd /usr/ports/net/bwn-firmware-kmod/
# make install clean
```

### 博通网卡驱动相关的文件结构

博通网卡驱动涉及以下文件。

```sh
/
├── boot/
│   └── loader.conf        # 系统启动加载配置文件
├── usr/
│   ├── ports/
│   │   └── net/
│   │       ├── bwi-firmware-kmod/   # Broadcom bwi 固件 Port
│   │       └── bwn-firmware-kmod/   # Broadcom bwn 固件 Port
│   └── src/
│       └── sys/
│           └── amd64/
│               └── conf/              # 内核配置文件目录
└── home/
    └── ykla/
        └── wifi-firmware-iwlwifi-kmod-20241017.1403000_2.pkg  # 英特尔无线网卡固件包
```

编辑 **/boot/loader.conf** 文件添加以下配置，设置系统在启动时加载 `bwn` 驱动：

```ini
if_bwn_load="YES"
```

在 **/etc/rc.conf** 文件中添加以下配置，将物理无线设备 `bwn0` 绑定到 `wlan0` 接口：

```ini
wlans_bwn0="wlan0"
```

## 无线网络故障排除

如果扫描时未列出接入点，可尝试切换路由器的信道，或者将协议降级到 Wi-Fi 4。

如果设备无法与接入点关联，验证配置是否与接入点上的设置匹配。这包括认证方案和任何安全协议。尽可能简化配置。如果使用 WPA2 或 WPA 等安全协议，将接入点配置为开放认证和无安全性，以验证流量是否可以通过。

如果系统可以与接入点关联，使用 ping(8) 等工具诊断网络配置。

## 附录：更新系统版本后无法使用无线网络

### 固件与系统更新的兼容性问题

在 FreeBSD 中，固件（Firmware）是硬件设备正常工作所需的底层软件，它提供了硬件设备与操作系统内核之间的通信接口。固件接口可能随内核版本更新而发生变化。

### 固件重新获取方法

如果在更新系统版本后无法使用无线网络，需要重新获取与当前内核版本兼容的固件。FreeBSD 提供了 `fwget` 工具用于自动获取和安装所需固件：

```sh
# fwget
```

如果当前系统没有网络连接，可以通过 USB 网络共享等方式临时获得网络连接后再执行上述命令；也可手动从 [https://mirrors.ustc.edu.cn/freebsd-pkg/FreeBSD%3A14%3Aamd64/kmods_latest_3/All/](https://mirrors.ustc.edu.cn/freebsd-pkg/FreeBSD%3A14%3Aamd64/kmods_latest_3/All/) 等镜像站点下载所需固件包，然后使用以下命令进行安装：

```sh
# pkg add /path/to/firmware.pkg
```

## 附录：特殊型号需要编译内核

对于特殊型号的博通无线网卡，可能需要重新编译内核才能获得完整支持。

在 FULLER L. FreeBSD Broadcom Wi-Fi Improvements[EB/OL]. [2026-03-26]. <https://web.archive.org/web/20240203102135/https://www.landonf.org/code/freebsd/Broadcom_WiFi_Improvements.20180122.html>. 中列出的部分型号带有 `$` 注释：`The optional bwn(4) PHY driver is derived from b43 GPL code, and must be explicitly enabled.`，表示需要使用基于 GNU 通用公共许可证（GNU General Public License，GPL）协议的代码。由于 FreeBSD 基本系统及内核默认不包含 GPL 许可证下的代码，因此需要重新编译内核以启用该选项。

```sh
# cd /usr/src/  # 此处是 FreeBSD 内核源代码安装目录
# cd sys/amd64/conf/  # 切换到 FreeBSD 内核配置文件目录。注意架构！
# cp GENERIC MYKERNEL  # 复制默认内核配置文件 GENERIC 为自定义内核 MYKERNEL
# echo "options BWN_GPL_PHY" >> MYKERNEL  # 向 MYKERNEL 内核配置文件添加 BWN_GPL_PHY 选项
# cd /usr/src  # 此处是 FreeBSD 内核源代码安装目录
# make -j4 buildkernel KERNCONF=MYKERNEL  # 使用 MYKERNEL 配置并启用 4 个并行任务编译内核
# make -j4 installkernel KERNCONF=MYKERNEL  # 安装使用 MYKERNEL 配置编译的内核，并启用 4 个并行任务
```

上述命令中，**/usr/src/** 为 FreeBSD 内核源代码安装目录，需注意根据实际架构选择相应的配置文件目录。

然后在 **/boot/loader.conf** 文件中添加以下配置：

```ini
hw.bwn_pci.preferred="1"        # 设置首选使用 BWN PCI 无线设备
if_bwn_pci_load="YES"           # 在启动时加载 bwn_pci 驱动
bwn_v4_ucode_load="YES"         # 加载 BWN V4 无线固件
bwn_v4_n_ucode_load="YES"       # 加载 BWN V4 N 模式无线固件
bwn_v4_lp_ucode_load="YES"      # 加载 BWN V4 低功耗模式无线固件
```

完成后重启系统，使用 `ifconfig` 检查是否存在 `wlan0` 接口，然后按照前文所述方法进行配置。

### 参考文献

- FreeBSD Foundation. Broadcom Wi-Fi Modernization[EB/OL]. [2026-03-26]. <https://freebsdfoundation.org/project/broadcom-wi-fi-modernization/>. FreeBSD 基金会资助的博通 Wi-Fi 驱动现代化项目概述。
- FreeBSD Project. Revision 326841[EB/OL]. [2026-03-26]. <https://svnweb.freebsd.org/base?view=revision&revision=326841>. 将博通无线驱动纳入 FreeBSD 基本系统的代码提交记录。
- FreeBSD Forums. Installing Broadcom BCM43236 WiFi on 11.3 missing firmware error[EB/OL]. [2026-03-26]. <https://forums.freebsd.org/threads/installing-broadcom-bcm43236-wifi-on-11-3-missing-firmware-error.76470/>. 博通无线网卡固件缺失导致无法使用的论坛讨论。
- helloSystem. ISO[EB/OL]. [2026-03-26]. <https://github.com/helloSystem/ISO/issues/78>. helloSystem 项目中关于 Wi-Fi 支持问题的反馈。

## 故障排除概述

### 若无法连接或无法搜索到特定信道

无线网络的区域码设置会影响可用的信道列表。可以尝试调整无线区域码设置。

在 **/etc/rc.conf** 文件中添加以下配置：

```ini
create_args_wlan0="country CN regdomain NONE"
```

该配置在创建 `wlan0` 接口时设置无线国家码为 CN，使用无特定无线频段限制。

完成配置后，重启系统。

### 断开 Wi-Fi

禁用 `wlan0` 接口：

```sh
# ifconfig wlan0 down
```

### WPA 验证

在 **/etc/rc.conf** 文件中配置 `wlan0` 接口使用 WPA，并设置静态 IP 地址和子网掩码：

```ini
ifconfig_wlan0="WPA inet 192.168.1.100 netmask 255.255.255.0"
```

### 设置静态 IP

为 `wlan0` 接口配置静态 IPv4 地址和子网掩码：

```sh
# ifconfig wlan0 inet 192.168.0.100 netmask 255.255.255.0
```

### 开启无线热点

配置无线热点前，需要确认网卡是否支持 hostap 模式。可通过以下命令列出 `wlan0` 接口支持的无线功能和能力：

```sh
# ifconfig wlan0 list caps
drivercaps=591c541<STA,FF,IBSS,HOSTAP,SHSLOT,SHPREAMBLE,MONITOR,WPA1,WPA2,WME>
cryptocaps=b<WEP,TKIP,AES_CCM>
htcaps=207002d<LDPC,SHORTGI20>
```

若输出中包含 `HOSTAP`，则表明该网卡支持 hostap 功能。

确认网卡支持后，销毁现有 `wlan0` 接口并释放其占用的资源：

```sh
# ifconfig wlan0 destroy
```

重新创建 `wlan0` 接口并配置为热点模式：

```sh
# ifconfig wlan0 create wlandev rtwn0 wlanmode hostap
# ifconfig wlan0 inet 192.168.0.1 netmask 255.255.255.0 ssid freebsdap mode 11g channel 1
```

第一条命令创建 `wlan0` 接口，绑定到 `rtwn0` 并设置为 Host AP 模式；第二条命令配置 `wlan0` 的 IP 地址、SSID、无线模式和信道。

![创建无线热点](../.gitbook/assets/wifi-hotspot.png)

## 附录：图形化网络配置工具

FreeBSD 提供了图形化网络管理工具，功能类似于 Linux 的 Plasma NetworkManager 或 NetworkManager。

使用 pkg 安装：

```sh
# pkg install net-mgmt/networkmgr
```

或者使用 Ports 安装：

```sh
# cd /usr/ports/net-mgmt/networkmgr/
# make install clean
```

## 课后习题

1. 使用两种不同厂商的无线网卡（如 Realtek 和 Intel），分别在 FreeBSD 上创建虚拟无线接口并连接同一 AP，使用 `systat -if` 监控两者的吞吐量与延迟差异，分析驱动实现差异对性能的影响。
2. 配置 FreeBSD 为无线热点（Host AP 模式），修改默认信道和发射功率参数，使用另一设备连接并测试信号强度与吞吐量变化，分析 Host AP 模式下的信道选择策略。
3. 查阅 FreeBSD 源代码中 `wlan` 接口的创建逻辑，分析系统采用“物理网卡 + 虚拟接口”分层架构而非直接管理物理设备的设计考量。
