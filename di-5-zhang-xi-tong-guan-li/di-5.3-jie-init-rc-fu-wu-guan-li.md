# 5.3 init.rc 服务管理

## 概述

FreeBSD 使用传统的 BSD init（初始化系统）来管理系统服务。与 systemd 等现代初始化系统不同，BSD init 采用基于脚本的服务管理方式。所有其他进程都是由 init 直接或间接启动的。

FreeBSD 提供了两个核心的服务管理命令：`service` 命令用于控制 rc.d 系统中的服务启动脚本，支持 `start`、`stop`、`restart`、`status` 等操作，并可列出可用服务。

`sysrc` 命令用于安全地修改 rc.conf(5) 中的系统配置值，自动处理 `/etc/rc.conf`、`/etc/rc.conf.local` 和 `/etc/defaults/rc.conf` 之间的优先级关系，避免手动编辑可能导致的语法错误。

## 服务管理配置文件与目录结构

```sh
/
├── etc/  # 参见 rc.conf(5)
│   ├── defaults/
│   │   ├── rc.conf         # 系统默认 rc 配置
│   │   └── vendor.conf     # 厂商默认配置（默认不存在）
│   ├── rc                  # 系统启动主脚本
│   ├── rc.conf             # 用户主配置文件
│   ├── rc.conf.local       # 本地自定义配置（默认不存在），用于开机时自定义配置
│   ├── rc.conf.d/          # 分散的用户自定义配置文件目录（默认为空）
│   ├── rc.d/               # 基本系统的服务脚本，参见 rc.d(8)
│   ├── rc.firewall         # 防火墙启动脚本
│   ├── rc.local            # 本地自定义启动脚本（默认不存在）
│   ├── rc.shutdown         # 系统关机执行脚本
│   ├── rc.suspend          # 系统挂起前执行的脚本
│   └── rc.subr             # rc 脚本公共函数库
├── var/
│   └── run/
│       └── dmesg.boot      # 启动时 dmesg(8) 输出
└── usr/
    └── local/
        └── etc/
            └── rc.d/       # 第三方应用的服务脚本
```

在 FreeBSD 源代码中，上述文件主要位于 [libexec/rc](https://github.com/freebsd/freebsd-src/tree/main/libexec/rc) 路径下。

默认 rc 配置位于 `/etc/defaults/rc.conf`。**此文件仅供查阅，不应直接修改。** 如需修改，应编辑 `/etc/rc.conf` 文件来覆盖默认的设置。`/etc/rc.conf` 文件是用户自定义的 rc 配置文件。如需系统自动启动 sshd、apache、pf 等服务，就需要修改该文件。

> **注意**
>
>`/etc/rc.conf` 文件的优先级高于 `/etc/defaults/rc.conf` 文件。也就是说，`/etc/rc.conf` 文件将覆盖 `/etc/defaults/rc.conf` 文件中的同名配置项。

## 系统服务管理常用命令集

BSD init 系统提供了 `service` 命令作为服务管理的统一接口，配合 `sysrc` 命令实现服务的启动、停止和开机自启动配置。以下是常用命令集。

启动服务：

```sh
# service xxx start
```

停止服务：

```sh
# service xxx stop
```

临时启动服务（即使未在 rc.conf 文件中启用）：

```sh
# service XXX onestart
```

临时停止服务（即使未在 rc.conf 文件中启用）：

```sh
# service XXX onestop
```

重启服务：

```sh
# service xxx restart
```

添加服务并设置开机自启：

```sh
# service xxx enable
# sysrc xxx_enable="YES"
```

> **注意**
>
>`service xxx enable` 命令并非适用于所有服务，仍有局限，参见：FreeBSD Project. rc keywords: enable, disable, delete cannot manage certain built-in rc startup items.[EB/OL]. [2026-03-26]. <https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=285543>. 下同。

禁用开机启动：

```sh
# service xxx disable
# sysrc xxx_enable="NO"
```

删除启动项：

```sh
# service xxx delete
```

> **注意**
>
> 关键字 `enable`、`disable`、`delete` 最早出现在 13.0-RELEASE，参见：FreeBSD Project. Add new rc keywords: enable, disable, delete[EB/OL]. [2026-03-26]. <https://reviews.freebsd.org/D17113>.

系统服务安装后默认未启用，上述命令无法直接执行，需先启用服务。

编辑 `/etc/rc.conf` 文件，在文件中添加一行：`XXX_enable="YES"`，其中 `XXX` 表示服务名称（例如 `nginx`、`samba` 等），这是固定格式。

```ini
# 启用 XXX 服务或功能（将 XXX 替换为具体服务名称），以下格式类似
XXX_enable="YES"
```

> **技巧**
>
>```sh
> # sysrc XXX_enable="YES"
>```
>
> 上述命令中的 `"YES"` 的双引号可省略，系统会自动添加（FreeBSD 15.0-RELEASE 起如此）。`"NO"` 亦同理。

基本系统服务的脚本路径为 `/etc/rc.d/`，第三方应用服务的脚本路径为 `/usr/local/etc/rc.d/`。可直接调用这两个目录下的脚本。

重新加载服务配置：

```sh
# /usr/local/etc/rc.d/XXX reload
```

停止服务：

```sh
# /usr/local/etc/rc.d/XXX stop
```

## 默认 rc.conf 配置文件的内容与结构

默认 rc.conf 配置文件的源代码位于 [libexec/rc/rc.conf](https://github.com/freebsd/freebsd-src/blob/main/libexec/rc/rc.conf)，对应提交为 [Set virtual_oss_enable="NO" in /etc/defaults/rc.conf](https://github.com/freebsd/freebsd-src/commit/1b2d495a24c36d81b14178a2f898025946bff2d8)。

```sh
#!/bin/sh

# 这是 rc.conf 文件 —— 包含许多可用变量，可用于修改系统的默认启动行为。不应直接编辑此文件！
# 应将那些覆盖配置放入 ${rc_conf_files}（即 /etc/rc.conf、/etc/rc.conf.local）中，这样就可以在不污染原生配置信息的情况下，
# 在以后更新系统默认值时仍然保留自定义设置。
#
# ${rc_conf_files} 文件中应仅包含那些覆盖本文件中设置的值。
# 这样在默认值变动或新增功能时，升级路径会更简单。
#
# 所有参数必须用双引号或单引号括起来。
#
# 如需更详细的 rc.conf 变量说明，请参阅 rc.conf(5) 手册页。

##############################################################
###  重要的启动时初始选项                   ####################
##############################################################

# 如果之前未设置 _localbase，则设置默认值
# 尝试从 sysctl 获取 user.localbase 的值，参见 getlocalbase(3)
# 此处设置的是本地软件第三方目录的基础路径
: ${_localbase:="$(/sbin/sysctl -n user.localbase 2> /dev/null)"}
# 如果获取不到，则默认使用 /usr/local
: ${_localbase:="/usr/local"}


# 不能在此处设置 rc_debug，否则会干扰在设置 kenv 变量 rc.debug 时的 rc.subr 操作
#rc_debug="NO"        # 设置为 YES 可启用 rc.d 的调试输出
rc_info="NO"           # 启用启动时的信息消息显示
rc_startmsgs="YES"     # 启动时显示 "Starting foo:" 消息
rcshutdown_timeout="90" # 在终止 rc.shutdown 前等待的秒数
precious_machine="NO"  # 设置为 YES 可对误操作的 shutdown(8) 命令提供一定保护
early_late_divider="FILESYSTEMS" # 分隔启动过程早期/晚期阶段的脚本，修改前请确保了解其影响，详见 rc.conf(5)
always_force_depends="NO"        # 设置为 YES 可在启动过程中检查依赖服务是否已启动（可能增加启动时间）


apm_enable="NO"        # 设置为 YES 可启用 BIOS 功能 APM（高级电源管理），否则禁用
apmd_enable="NO"       # 启动 apmd 来处理用户空间的 APM 事件
apmd_flags=""          # 在启用 apmd 时额外传递的标志
ddb_enable="NO"        # 设置为 YES 将在启动时加载 ddb 脚本
ddb_config="/etc/ddb.conf"  # ddb(8) 配置文件路径
devd_enable="YES"      # 启动 devd，用于在设备树变化时触发程序
devd_flags=""          # devd(8) 的额外标志
devmatch_enable="YES"   # 根据设备 ID 按需加载内核模块
devmatch_blocklist=""  # 排除 devmatch 加载的模块列表（不加后缀名 .ko）
#kld_list=""           # 本地磁盘挂载后要加载的内核模块
kldxref_enable="YES"   # 使用 kldxref(8) 构建 linker.hints 文件
kldxref_clobber="NO"   # 启动时是否覆盖旧的 linker.hints
kldxref_module_path="" # 覆盖 kern.module_path；以分号 ';' 分隔的列表
powerd_enable="NO"     # 启动 powerd(8) 降低功耗，系统电源控制管理
powerd_flags=""        # 启用 powerd(8) 时传递的标志
tmpmfs="AUTO"          # 设置为 YES 始终创建 mfs /tmp，NO 表示从不创建
tmpsize="20m"          # 创建 mfs /tmp 时的大小
tmpmfs_flags="-S"      # mfs /tmp 的额外 mdmfs 选项
utx_enable="YES"       # 启用用户账户管理
varmfs="AUTO"          # 设置为 YES 始终创建 mfs /var，NO 表示从不创建
varsize="32m"          # 创建 mfs /var 时的大小
varmfs_flags="-S"      # mfs /var 的额外挂载选项
mfs_type="auto"        # 可选 "md", "tmpfs", "auto"，优先 tmpfs，md 作为回退
populate_var="AUTO"    # 设置为 YES 始终（重新）填充 /var，NO 表示从不填充
cleanvar_enable="YES"  # 清理 /var 目录
var_run_enable="YES"   # 在关机/重启时保存/恢复 /var/run 结构
var_run_autosave="YES" # 仅在关机/重启时恢复 /var/run 结构，用户可通过 service var_run save 手动保存
var_run_mtree="/var/db/mtree/BSD.var-run.mtree"  # 保存 /var/run mtree 的路径
local_startup="${_localbase}/etc/rc.d"         # 启动脚本目录
script_name_sep=" "      # 如果启动脚本名包含空格，可修改此分隔符
rc_conf_files="/etc/rc.conf /etc/rc.conf.local" # 要加载的 rc.conf 文件列表

# ZFS 支持
zfs_enable="NO"             # 设置为 YES 将自动挂载 ZFS 文件系统
zfskeys_enable="NO"         # 设置为 YES 将自动加载 ZFS 加密密钥
zfs_bootonce_activate="NO"  # 设置为 YES，使成功的 bootonce ZFS 启动环境永久生效
zpool_reguid=""              # 指定首次启动时要替换 GUID 的 zpool
zpool_upgrade=""             # 指定首次启动时要升级版本的 zpool

# ZFSD 支持
zfsd_enable="NO"            # 设置为 YES 自动启动 ZFS 故障管理守护进程

gptboot_enable="YES"        # GPT 引导成功/失败报告

# GELI 磁盘加密配置
geli_devices=""             # 除 /etc/fstab 中的 GELI 设备外，自动附加的设备列表
geli_groups=""              # 自动附加同一组设备，使用相同密钥或口令
geli_tries=""               # 尝试附加 geli 设备的次数；为空时使用 kern.geom.eli.tries
geli_default_flags=""       # geli(8) 的默认标志
geli_autodetach="YES"       # 在最后一次关闭时自动分离。在所有文件系统挂载后，提供者将被标记为可自动分离

# 示例用法
#geli_devices="da1 mirror/home"                  # 指定要自动附加的 GELI 加密设备列表
#geli_da1_flags="-p -k /etc/geli/da1.keys"      # 为 da1 设备设置附加标志和密钥文件路径
#geli_da1_autodetach="NO"                        # 设置 da1 设备在最后关闭时是否自动分离（NO 表示不自动分离）
#geli_mirror_home_flags="-k /etc/geli/home.keys" # 为 mirror/home 设备设置密钥文件
#geli_groups="storage backup"                    # 定义设备组，用于按组自动附加
#geli_storage_flags="-k /etc/geli/storage.keys" # 为 storage 组的设备设置密钥文件
#geli_storage_devices="ada0 ada1"               # storage 组中包含的物理设备
#geli_backup_flags="-j /etc/geli/backup.passfile -k /etc/geli/backup.keys" # 为 backup 组的设备设置口令文件和密钥文件
#geli_backup_devices="ada2 ada3"                # backup 组中包含的物理设备

## 磁盘相关选项
root_rw_mount="YES"           # 设置为 YES 表示允许将根文件系统重新挂载为可读写；NO 表示禁止重新挂载为可读写
root_hold_delay="30"           # 在释放根文件系统挂载保持锁之前等待的时间（秒）
fsck_flags="-p"                # fsck 的默认标志，-p 表示自动修复可修复的错误；可改为 -f 或 -f -y 强制完全检查
fsck_y_enable="NO"             # 设置为 YES，如果初次预检（preen）失败，则自动执行 fsck -y
fsck_y_flags="-T ffs:-R -T ufs:-R"  # fsck -y 的额外标志
background_fsck="YES"          # 尝试在后台执行 fsck（如果可能）
background_fsck_delay="60"     # 启动后台 fsck 前等待的时间（秒）
growfs_enable="NO"             # 设置为 YES 在启动时尝试扩展根文件系统
growfs_swap_size=""             # 指定 growfs 扩展 swap 大小，0 表示禁用，"" 表示使用默认大小（单位为字节）
netfs_types="nfs:NFS smbfs:SMB"  # 网络文件系统类型映射
extra_netfs_types="NO"         # 启动时延迟挂载的额外网络文件系统类型列表，或 NO 表示不使用

##############################################################
###  网络配置小节                        ######################
##############################################################

### 基本网络与防火墙/安全选项: ###

hostname=""                          # 请设置主机名！
hostid_enable="YES"                  # 启用主机 UUID
hostid_file="/etc/hostid"            # 存放 hostuuid 的文件
hostid_uuidgen_flags="-r"            # uuidgen 命令的标志
machine_id_file="/etc/machine-id"    # 存放 machine-id 的文件
nisdomainname="NO"                   # 如果使用 NIS，设置 NIS 域名，否则 NO
dhclient_program="/sbin/dhclient"    # DHCP 客户端程序路径
dhclient_flags=""                     # 传递给 DHCP 客户端的额外参数
#dhclient_flags_em0=""                # 仅为 em0 接口传递额外 dhclient 参数
background_dhclient="NO"             # 在后台启动 DHCP 客户端
#background_dhclient_em0="YES"       # 在后台启动 em0 接口的 DHCP 客户端
dhclient_arpwait="YES"               # 等待 ARP 解析完成
synchronous_dhclient="NO"            # 在启动时直接在配置的接口上启动 dhclient
defaultroute_delay="30"              # 等待 DHCP 接口默认路由的时间（秒）
defaultroute_carrier_delay="5"       # 等待链路信号的时间（秒）
netif_enable="YES"                    # 启用网络接口初始化
netif_ipexpand_max="2048"             # IP 范围规格中允许的最大 IP 数量
wpa_supplicant_program="/usr/sbin/wpa_supplicant"  # WPA supplicant 程序路径
wpa_supplicant_flags="-s"             # 传递给 wpa_supplicant 的额外参数
wpa_supplicant_conf_file="/etc/wpa_supplicant.conf" # WPA supplicant 配置文件

# IPFW 防火墙
firewall_enable="NO"             # 设置为 YES 启用防火墙（IPFW）功能
firewall_script="/etc/rc.firewall"  # 设置启动防火墙时执行的脚本
firewall_type="UNKNOWN"           # 防火墙类型（参见 /etc/rc.firewall）
firewall_quiet="NO"               # 设置为 YES 可禁止显示防火墙规则
firewall_logging="NO"             # 设置为 YES 启用防火墙事件日志
firewall_flags=""                  # 当类型为文件时，传递给 ipfw 的标志
firewall_coscripts=""              # 防火墙启动/停止后要执行的可执行文件或脚本列表

firewall_client_net="192.0.2.0/24"       # “client” 防火墙的 IPv4 网络地址
#firewall_client_net_ipv6="2001:db8:2:1::/64" # “client” 防火墙的 IPv6 网络前缀

firewall_simple_iif="em1"          # “simple” 防火墙的内部网络接口
firewall_simple_inet="192.0.2.16/28" # “simple” 防火墙的内部网络地址
firewall_simple_oif="em0"          # “simple” 防火墙的外部网络接口
firewall_simple_onet="192.0.2.0/28" # “simple” 防火墙的外部网络地址
#firewall_simple_iif_ipv6="em1"       # “simple” 防火墙的内部 IPv6 网络接口
#firewall_simple_inet_ipv6="2001:db8:2:800::/56" # “simple” 防火墙的内部 IPv6 网络前缀
#firewall_simple_oif_ipv6="em0"       # “simple” 防火墙的外部 IPv6 网络接口
#firewall_simple_onet_ipv6="2001:db8:2:0::/56" # “simple” 防火墙的外部 IPv6 网络前缀

firewall_myservices=""             # 本机为“workstation”防火墙提供服务的端口/协议列表
firewall_allowservices=""          # 允许访问 $firewall_myservices 的 IP 列表
firewall_trusted=""                # 对本机具有完全访问权限的受信任 IP 列表
firewall_logdeny="NO"              # 设置为 YES 记录被拒绝的默认入站数据包
firewall_nologports="135-139,445 1026,1027 1433,1434" # 对这些端口的被拒绝数据包不记录日志
firewall_nat_enable="NO"       # 启用内核 NAT（前提是 firewall_enable 为 YES）
firewall_nat_interface=""       # 用于 NAT 的公共接口或 IP 地址
firewall_nat_flags=""           # 额外配置参数
firewall_nat64_enable="NO"     # 启用内核 NAT64 模块
firewall_nptv6_enable="NO"     # 启用内核 NPTv6 模块
firewall_pmod_enable="NO"      # 启用内核协议修改模块
dummynet_enable="NO"           # 加载 dummynet(4) 模块
ipfw_netflow_enable="NO"       # 通过 ng_netflow 启用 netflow 日志
ip_portrange_first="NO"        # 设置动态分配端口的起始端口
ip_portrange_last="NO"         # 设置动态分配端口的结束端口

ike_enable="NO"                # 启用 IKE 守护进程（通常是 racoon 或 isakmpd）
ike_program="${_localbase}/sbin/isakmpd" # IKE 守护进程路径
ike_flags=""                    # IKE 守护进程额外标志

ipsec_enable="NO"               # 设置为 YES 时，使用 setkey 加载 ipsec_file
ipsec_file="/etc/ipsec.conf"    # setkey 的配置文件名称

natd_program="/sbin/natd"       # natd 程序路径
natd_enable="NO"                # 启用 natd（前提是 firewall_enable 为 YES）
natd_interface=""               # 公共接口或 IP 地址
natd_flags=""                   # natd 额外标志

ipfilter_enable="NO"            # 设置为 YES 启用 ipfilter 功能
ipfilter_program="/sbin/ipf"    # ipfilter 程序路径
ipfilter_rules="/etc/ipf.rules" # ipfilter 规则文件（示例见 /usr/src/share/examples/ipfilter）
ipfilter_flags=""               # ipfilter 额外标志
ipfilter_optionlist=""          # ipf(8) 的 optionlist

ippool_enable="NO"              # 设置为 YES 启用 ip filter pool
ippool_program="/sbin/ippool"   # ippool 程序路径
ippool_rules="/etc/ippool.tables" # ippool 规则文件
ippool_flags=""                 # ippool 额外标志

ipnat_enable="NO"               # 设置为 YES 启用 ipnat 功能
ipnat_program="/sbin/ipnat"     # ipnat 程序路径
ipnat_rules="/etc/ipnat.rules"  # ipnat 规则文件
ipnat_flags=""                  # ipnat 额外标志

ipmon_enable="NO"               # 设置为 YES 启用 ipmon；需要 ipfilter 或 ipnat
ipmon_program="/sbin/ipmon"     # ipfilter 监控程序路径
ipmon_flags="-Ds"               # 通常为 "-Ds" 或 "-D /var/log/ipflog"

ipfs_enable="NO"                # 设置为 YES 启用在关机和启动时保存/恢复状态表
ipfs_program="/sbin/ipfs"       # ipfs 程序路径
ipfs_flags=""                   # ipfs 额外标志

pf_enable="NO"                  # 设置为 YES 启用 packet filter (pf)
pf_rules="/etc/pf.conf"         # pf 规则文件（默认不存在）
pf_program="/sbin/pfctl"        # pfctl 程序路径
pf_flags=""                     # pfctl 额外标志
pf_fallback_rules_enable="NO"   # 如果规则集加载失败则使用备用规则
pf_fallback_rules="block drop log all" # 规则集加载失败时使用的规则
#pf_fallback_rules="block drop log all
#pass quick on em4"             # 多规则示例
pf_fallback_rules_file="/etc/pf-fallback.conf" # 规则集失败时使用的文件

pflog_enable="NO"               # 设置为 YES 启用 pf 日志
pflog_logfile="/var/log/pflog"  # pflogd 日志存放路径
pflog_program="/sbin/pflogd"    # pflogd 程序路径
pflog_flags=""                  # pflogd 额外标志

dnctl_enable="NO"               # 启用 dnctl（pf 状态管理工具）
dnctl_program="/sbin/dnctl"     # dnctl 程序路径
dnctl_rules="/etc/dnctl.conf"   # dnctl 规则文件

ftpproxy_enable="NO"            # 设置为 YES 启用 pf 的 ftp-proxy(8)
ftpproxy_flags=""               # ftp-proxy 额外标志

pfsync_enable="NO"              # 向其他主机同步 pf 状态
pfsync_syncdev=""               # pfsync 使用的接口
pfsync_syncpeer=""              # pfsync 对端主机 IP
pfsync_ifconfig=""              # pfsync 的额外 ifconfig(8) 选项

tcp_extensions="YES"            # 设置为 NO 关闭 RFC1323 TCP 高性能扩展
log_in_vain="0"                 # >=1 时记录连接到无监听端口的日志
tcp_keepalive="YES"             # 启用 TCP 空闲连接超时检测（或 NO）
tcp_drop_synfin="NO"            # 设置为 YES 丢弃 SYN+FIN 的 TCP 包
                                # 注意：违反 TCP 协议规范
icmp_drop_redirect="auto"       # 设置为 YES 忽略 ICMP REDIRECT 包
icmp_log_redirect="NO"          # 设置为 YES 记录 ICMP REDIRECT 包

network_interfaces="auto"       # 网络接口列表，或使用 "auto" 自动检测
cloned_interfaces=""            # 要创建的克隆网络接口列表
#cloned_interfaces="gif0 gif1 gif2 gif3"	# 预先克隆 GENERIC 配置的虚拟接口
#ifconfig_lo0="inet 127.0.0.1/8" # 默认回环设备配置，用于本地通信
#ifconfig_lo0_alias0="inet 127.0.0.254/32"	# 回环设备别名示例，用于绑定额外 IPv4 地址
#ifconfig_em0_ipv6="inet6 2001:db8:1::1 prefixlen 64"	# 为 em0 配置主 IPv6 地址，前缀长度 64
#ifconfig_em0_alias0="inet6 2001:db8:2::1 prefixlen 64"	# em0 的 IPv6 别名，用于多地址配置
#ifconfig_em0_name="net0"	# 将物理接口 em0 重命名为 net0，便于管理
#vlans_em0="101 vlan0"	# 在 em0 上创建 VLAN 101，并命名为 vlan0
#create_args_vlan0="vlan 102"	# 为 vlan0 配置二级 VLAN tag 102
#wlans_ath0="wlan0"	# 将 ath0 无线接口配置为 wlan0
#wlandebug_wlan0="scan+auth+assoc"	# 使用 wlandebug(8) 设置 WLAN 调试标志，包括扫描、认证和关联过程
#ipv4_addrs_em0="192.168.0.1/24 192.168.1.1-5/28"	# 为 em0 配置多个 IPv4 地址：192.168.0.1/24 和 192.168.1.1 到 192.168.1.5/28 的连续范围
#
#autobridge_interfaces="bridge0"    # 要检查的桥接接口列表
#autobridge_bridge0="tap* vlan0"    # 自动添加到桥接的接口 glob

# 用户 PPP 配置
ppp_enable="NO"                     # 启动用户 PPP（或 NO）
ppp_program="/usr/sbin/ppp"         # 用户 PPP 程序路径
ppp_mode="auto"                      # 模式选择：auto、ddial、direct 或 dedicated，默认 auto
ppp_nat="YES"                        # 使用 PPP 内部 NAT（或 NO）
ppp_profile="papchap"                # 使用配置文件 /etc/ppp/ppp.conf
ppp_user="root"                      # PPP 运行用户

# 启动多个 PPP 实例
#ppp_profile="profile1 profile2 profile3" # 要使用的 PPP 配置文件
#ppp_profile1_mode="ddial"             # 覆盖 profile1 的 PPP 模式
#ppp_profile2_nat="NO"                 # 覆盖 profile2 的 NAT 模式
# profile3 使用默认 ppp_mode 和 ppp_nat

### 网络守护进程（杂项） ###
hostapd_program="/usr/sbin/hostapd"
hostapd_enable="NO"           # 启动 hostap 守护进程

syslogd_enable="YES"          # 启动 syslog 守护进程（或 NO）
syslogd_program="/usr/sbin/syslogd" # syslogd 程序路径（可替换）
syslogd_flags="-s"            # syslogd 启动参数
syslogd_oomprotect="YES"      # 当交换空间耗尽时，不杀死 syslogd

altlog_proglist=""            # /var 下 chroot 应用程序列表

inetd_enable="NO"             # 启动网络守护进程调度器（YES/NO）
inetd_program="/usr/sbin/inetd"   # inetd 程序路径（可替换）
inetd_flags="-wW -C 60"       # inetd 可选启动参数

iscsid_enable="NO"            # iSCSI 发起端守护进程
iscsictl_enable="NO"          # iSCSI 发起端自动启动
iscsictl_flags="-Aa"          # iscsictl 可选参数

hastd_enable="NO"             # 启动 HAST 守护进程（YES/NO）
hastd_program="/sbin/hastd"   # hastd 程序路径（可替换）
hastd_flags=""                # hastd 可选参数

ggated_enable="NO"            # 启动 ggate 守护进程（YES/NO）
ggated_config="/etc/gg.exports"   # ggated(8) 导出文件
ggated_flags=""               # 额外参数，例如绑定端口

ctld_enable="NO"              # CAM Target Layer / iSCSI 目标守护进程

local_unbound_enable="NO"     # 本地缓存 DNS 解析器
local_unbound_oomprotect="YES" # 交换空间耗尽时不杀死 local_unbound
local_unbound_tls="NO"        # 使用 DNS over TLS

blacklistd_enable="NO"        # 已重命名为 blocklistd_enable
blacklistd_flags=""           # 已重命名为 blocklistd_flags
blocklistd_enable="NO"        # 启动 blocklistd 守护进程（YES/NO）
blocklistd_flags=""           # blocklistd(8) 可选参数

resolv_enable="YES"           # 启用 resolv / resolvconf

#
# Kerberos。请勿在从属服务器上运行管理守护进程
#
kdc_enable="NO"             # 启动 Kerberos 5 KDC（或 NO）
kdc_program=""              # Kerberos 5 KDC 程序路径
kdc_flags=""                # Kerberos 5 KDC 额外参数
kdc_restart="NO"            # KDC 异常终止时自动重启
kdc_restart_delay=""        # 自动重启延迟时间（秒）

kadmind_enable="NO"         # 启动 kadmind（或 NO）
kadmind_program="/usr/libexec/kadmind" # kadmind 程序路径

kpasswdd_enable="NO"        # 启动 kpasswdd（或 NO）
kpasswdd_program="/usr/libexec/kpasswdd" # kpasswdd 程序路径

kfd_enable="NO"             # 启动 kfd（或 NO）
kfd_program="/usr/libexec/kfd" # Kerberos 5 kfd 守护进程路径
kfd_flags=""                # kfd 额外参数

ipropd_master_enable="NO"   # 启动 Heimdal 增量同步守护进程（主节点）
ipropd_master_program="/usr/libexec/ipropd-master"
ipropd_master_flags=""      # ipropd-master 参数
ipropd_master_keytab="/etc/krb5.keytab"  # 主节点 keytab
ipropd_master_slaves=""     # /var/heimdal/slaves 中使用的从节点名列表

ipropd_slave_enable="NO"    # 启动 Heimdal 增量同步守护进程（从节点）
ipropd_slave_program="/usr/libexec/ipropd-slave"
ipropd_slave_flags=""       # ipropd-slave 参数
ipropd_slave_keytab="/etc/krb5.keytab"   # 从节点 keytab
ipropd_slave_master=""      # 主节点名

gssd_enable="NO"            # 启动 gssd 守护进程（或 NO）
gssd_program="/usr/sbin/gssd" # gssd 程序路径
gssd_flags=""               # gssd 参数
rwhod_enable="NO"           # 启动 rwho 守护进程（或 NO）
rwhod_flags=""               # rwhod 参数
rarpd_enable="NO"            # 启动 rarpd（或 NO）
rarpd_flags="-a"             # rarpd 参数
bootparamd_enable="NO"       # 启动 bootparamd（或 NO）
bootparamd_flags=""          # bootparamd 参数

pppoed_enable="NO"           # 启动 PPP over Ethernet 守护进程
pppoed_provider="*"          # PPPoE 提供者和 ppp(8) 配置文件条目
pppoed_flags="-P /var/run/pppoed.pid" # PPPoE 参数（如果启用）
pppoed_interface="em0"       # PPPoE 运行的接口

sshd_enable="NO"             # 启用 sshd
sshd_oomprotect="YES"        # 当交换空间耗尽时不杀死 sshd
sshd_program="/usr/sbin/sshd" # sshd 程序路径
sshd_flags=""                # sshd 额外参数

### 网络守护进程（NFS）：所有需 rpcbind_enable="YES" ###
autofs_enable="NO"           # 启动 autofs 守护进程
automount_flags=""           # automount(8) 参数（如果启用 autofs）
automountd_flags=""          # automountd(8) 参数（如果启用 autofs）
autounmountd_flags=""        # autounmountd(8) 参数（如果启用 autofs）

nfs_client_enable="NO"       # 本机作为 NFS 客户端（或 NO）
nfs_access_cache="60"        # 客户端缓存超时时间（秒）
nfs_server_enable="NO"       # 本机作为 NFS 服务器（或 NO）
nfs_server_flags="-u -t"     # nfsd 参数（如果启用）
nfs_server_managegids="NO"   # NFS 服务器是否映射 AUTH_SYS 的 gids（或 NO）
nfs_server_maxio="131072"    # nfsd 最大 I/O 大小
mountd_enable="NO"           # 启动 mountd（或 NO）
mountd_flags="-r -S"         # mountd 参数（如果启用 NFS 服务器）
weak_mountd_authentication="NO" # 允许非 root 挂载请求
nfs_reserved_port_only="YES" # 仅在安全端口提供 NFS（或 NO）
nfs_bufpackets=""            # 客户端 bufspace（以包计）

rpc_lockd_enable="NO"        # 启动 NFS rpc.lockd（客户端/服务器需要）
rpc_lockd_flags=""            # rpc.lockd 参数（如果启用）
rpc_statd_enable="NO"        # 启动 NFS rpc.statd（客户端/服务器需要）
rpc_statd_flags=""            # rpc.statd 参数（如果启用）
rpcbind_enable="NO"           # 启动端口映射服务（YES/NO）
rpcbind_program="/usr/sbin/rpcbind" # rpcbind 程序路径
rpcbind_flags=""             # rpcbind 参数（如果启用）

rpc_ypupdated_enable="NO"    # 如果是 NIS 主节点且启用 SecureRPC
nfsv4_server_enable="NO"     # 启用 NFSv4 支持
nfsv4_server_only="NO"       # 设置 NFS 服务器仅支持 NFSv4
nfscbd_enable="NO"           # NFSv4 客户端回调守护进程
nfscbd_flags=""               # nfscbd 参数
nfsuserd_enable="NO"         # NFSv4 用户/组名称映射守护进程
nfsuserd_flags=""             # nfsuserd 参数
tlsclntd_enable="NO"         # 启动 rpc.tlsclntd（NFS-over-TLS 挂载需要）
tlsclntd_flags=""             # rpc.tlsclntd 参数
tlsservd_enable="NO"         # 启动 rpc.tlsservd（NFS-over-TLS nfsd 需要）
tlsservd_flags=""             # rpc.tlsservd 参数

### 网络时间服务选项 ###
ntpdate_enable="NO"               # 启动 ntpdate 在开机时同步时间（或 NO）
ntpdate_program="/usr/sbin/ntpdate" # ntpdate 程序路径（可自定义）
ntpdate_flags="-b"                # ntpdate 参数（如果启用）
ntpdate_config="/etc/ntp.conf"    # ntpdate(8) 配置文件
ntpdate_hosts=""                   # ntpdate(8) 服务器列表，用空格分隔

ntpd_enable="NO"                   # 启动 ntpd 网络时间协议守护进程（或 NO）
ntpd_program="/usr/sbin/ntpd"      # ntpd 程序路径（可自定义）
ntpd_config="/etc/ntp.conf"        # ntpd(8) 配置文件
ntpd_sync_on_start="NO"            # 启动 ntpd 时是否立即同步时间（即使偏移大）
ntpd_flags=""                       # ntpd 额外参数

ntp_src_leapfile="/etc/ntp/leap-seconds"          # ntpd leapfile 的初始来源
ntp_db_leapfile="/var/db/ntpd.leap-seconds.list" # 获取闰秒的标准位置
ntp_leapfile_sources="https://hpiers.obspm.fr/iers/bul/bulc/ntp/leap-seconds.list https://data.iana.org/time-zones/tzdb/leap-seconds.list"  #  leapfile 的获取来源
ntp_leapfile_fetch_opts="-mq"       # 获取 NTP leapfile 时使用的选项，例如 --no-verify-peer
ntp_leapfile_expiry_days=30         # 在到期前 30 天检查新的 leapfile
ntp_leapfile_fetch_verbose="NO"     # 获取 NTP leapfile 时是否输出详细信息

# 网络信息服务 (NIS) 选项：全部都依赖 rpcbind_enable="YES" ###
nis_client_enable="NO"        # 是 NIS 客户端（或 NO）
nis_client_flags=""            # ypbind 的参数（如果启用）
nis_ypset_enable="NO"         # 开机时运行 ypset（或 NO）
nis_ypset_flags=""             # ypset 参数（如果启用）
nis_server_enable="NO"        # 是 NIS 服务器（或 NO）
nis_server_flags=""            # ypserv 参数（如果启用）
nis_ypxfrd_enable="NO"        # 开机时运行 rpc.ypxfrd（或 NO）
nis_ypxfrd_flags=""            # rpc.ypxfrd 参数（如果启用）
nis_yppasswdd_enable="NO"     # 开机时运行 rpc.yppasswdd（或 NO）
nis_yppasswdd_flags=""         # rpc.yppasswdd 参数（如果启用）
nis_ypldap_enable="NO"         # 开机时运行 ypldap（或 NO）
nis_ypldap_flags=""             # ypldap 参数（如果启用）

### SNMP 守护进程 ###
# 确保理解在网络中运行 SNMP v1/v2 的安全隐患
bsnmpd_enable="NO"            # 启动 SNMP 守护进程（或 NO）
bsnmpd_flags=""                # bsnmpd 参数

### 网络路由选项: ###
defaultrouter="NO"            # 设置默认网关（或 NO）
#defaultrouter_fibN="192.0.2.1" # 使用此形式为 FIB N 设置网关
static_arp_pairs=""            # 设置静态 ARP 列表（或留空）
static_ndp_pairs=""            # 设置静态 NDP 列表（或留空）
static_routes=""               # 设置静态路由列表（或留空）
gateway_enable="NO"            # 如果此主机将作为网关，则设置为 YES
routed_enable="NO"             # 启用路由守护进程则设置为 YES
routed_program="/sbin/routed"  # 启用时使用的路由守护进程
routed_flags="-q"              # 路由守护进程参数
arpproxy_all="NO"              # 替代过时的内核选项 ARP_PROXYALL
forward_sourceroute="NO"       # 执行源路由（仅当 gateway_enable 设置为 YES 时）
accept_sourceroute="NO"        # 接受发往本机的源路由数据包

### 蓝牙 ###
hcsecd_enable="NO"               # 启用 hcsecd(8)（或 NO）
hcsecd_config="/etc/bluetooth/hcsecd.conf"  # hcsecd(8) 配置文件

sdpd_enable="NO"                 # 启用 sdpd(8)（或 NO）
sdpd_control="/var/run/sdp"      # sdpd(8) 控制套接字
sdpd_groupname="nobody"          # 初始化后设置 sdpd(8) 运行的用户组
sdpd_username="nobody"           # 初始化后设置 sdpd(8) 运行的用户名

bthidd_enable="NO"               # 启用 bthidd(8)（或 NO）
bthidd_config="/etc/bluetooth/bthidd.conf"  # bthidd(8) 配置文件
bthidd_hids="/var/db/bthidd.hids"          # bthidd(8) 已知 HID 设备文件
bthidd_evdev_support="AUTO"      # AUTO 取决于 EVDEV_SUPPORT 内核选项

rfcomm_pppd_server_enable="NO"   # 以服务器模式启用 rfcomm_pppd(8)（或 NO）
rfcomm_pppd_server_profile="one two"  # 使用 /etc/ppp/ppp.conf 中的配置文件

#rfcomm_pppd_server_one_bdaddr=""   # 为 'one' 覆盖本地 bdaddr
rfcomm_pppd_server_one_channel="1"  # 为 'one' 覆盖本地通道
#rfcomm_pppd_server_one_register_sp="NO"  # 为 'one' 覆盖 SP 和 DUN 注册
#rfcomm_pppd_server_one_register_dun="NO" # 为 'one'

#rfcomm_pppd_server_two_bdaddr=""   # 为 'two' 覆盖本地 bdaddr
rfcomm_pppd_server_two_channel="3"  # 为 'two' 覆盖本地通道
#rfcomm_pppd_server_two_register_sp="NO"  # 为 'two' 覆盖 SP 和 DUN 注册
#rfcomm_pppd_server_two_register_dun="NO" # 为 'two'

ubthidhci_enable="NO"            # 将存在的 USB 蓝牙控制器从 HID 模式切换到 HCI 模式
#ubthidhci_busnum="3"             # 总线号 3
#ubthidhci_addr="2"               # 地址 2，使用 usbconfig 列表检查系统的正确编号

### 网络连接/可用性验证选项 ###
netwait_enable="NO"           # 启用 rc.d/netwait（或 NO）
#netwait_ip=""                # 等待此列表中任意 IP 的 ping 响应
netwait_timeout="60"           # 执行 ping 的总秒数
#netwait_if=""                # 等待此列表中每个接口的活动链路
netwait_if_timeout="30"        # 监控链路状态的总秒数
netwait_dad="NO"               # 等待 DAD 完成
netwait_dad_timeout=""         # 等待 DAD 的总秒数，0 或未设置表示自动检测

### 杂项网络选项 ###
icmp_bmcastecho="NO"           # 响应广播 ping 数据包

### IPv6 选项 ###
ipv6_network_interfaces="auto"         # IPv6 网络接口列表（或 "auto" 或 "none"）
ipv6_activate_all_interfaces="NO"     # 如果 NO，没有对应 $ifconfig_IF_ipv6 的接口会被标记为 IFDISABLED（出于安全原因）
ipv6_defaultrouter="NO"               # 设置 IPv6 默认网关（或 NO）
#ipv6_defaultrouter="2002:c058:6301::"  # 用于 6to4（RFC 3068）
#ipv6_defaultrouter_fibN="2001:db8::"   # 设置 FIB N 的网关
ipv6_static_routes=""                  # 静态路由列表（或留空）
#ipv6_static_routes="xxx"              # 示例：设置 fec0:0000:0000:0006::/64 路由到回环接口
#ipv6_route_xxx="fec0:0000:0000:0006:: -prefixlen 64 ::1"
ipv6_gateway_enable="NO"               # 如果此主机作为网关则设置为 YES
ipv6_cpe_wanif="NO"                    # 如果此节点作为路由器转发 IPv6 包，设置上游接口名
ipv6_privacy="NO"                      # 在接收 RA 的接口上使用隐私地址（RFC 4941）

route6d_enable="NO"               # 设置为 YES 启用 IPv6 路由守护进程
route6d_program="/usr/sbin/route6d"  # IPv6 路由守护进程名称
route6d_flags=""                   # IPv6 路由守护进程参数
#route6d_flags="-l"               # 仅监听本地链路 IPv6 地址。（路由器示例）
#route6d_flags="-q"               # 静默模式，关闭路由通告。示例：终端节点运行路由守护进程时应停止通告
# 示例：为路由器或终端节点配置静态 IPv6
#ipv6_network_interfaces="em0 em1"  # 指定启用 IPv6 的网络接口 em0 和 em1（路由器示例）
#ipv6_prefix_em0="fec0:0000:0000:0001 fec0:0000:0000:0002"  # 为 em0 接口分配静态 IPv6 前缀/地址（路由器示例），此处分配了 2 个 IPv6 地址
#ipv6_prefix_em1="fec0:0000:0000:0003 fec0:0000:0000:0004"  # 为 em1 接口分配静态 IPv6 前缀/地址（路由器示例），此处分配了 2 个 IPv6 地址
ipv6_default_interface="NO"       # 默认输出接口（仅在 ipv6_gateway_enable="NO" 时生效）
rtsol_flags="-i"                  # IPv6 路由器请求标志
rtsold_enable="NO"                # 设置为 YES 启用 IPv6 路由器请求守护进程
rtsold_flags="-a -i"              # IPv6 路由器请求守护进程参数
rtadvd_enable="NO"                # 设置为 YES 启用 IPv6 路由器通告守护进程
rtadvd_flags=""                   # IPv6 路由器通告守护进程参数
rtadvd_interfaces=""              # rtadvd 发送 RA 数据包的接口
stf_interface_ipv4addr=""         # 6to4 IPv6 over IPv4 隧道接口的本地 IPv4 地址
stf_interface_ipv4plen="0"        # 6to4 IPv4 地址前缀长度，有效值 0-31
stf_interface_ipv6_ifid="0:0:0:1" # stf0 的 IPv6 接口 ID，可设置为 AUTO
stf_interface_ipv6_slaid="0000"   # stf0 的 IPv6 Site Level Aggregator
ipv6_ipv4mapping="NO"             # 设置为 YES 启用 IPv4 映射 IPv6 地址通信 (::ffff:a.b.c.d)
ip6addrctl_enable="YES"           # 启用默认 IPv6 地址选择
ip6addrctl_verbose="NO"           # 启用详细配置消息
ip6addrctl_policy="AUTO"          # 预定义地址选择策略（ipv4_prefer, ipv6_prefer, 或 AUTO）

##############################################################
###  系统控制台选项           #################################
##############################################################

keyboard=""                # 使用的键盘设备（默认 /dev/kbd0）
keymap="NO"                # /usr/share/{syscons,vt}/keymaps/* 中的键盘映射（或 NO）
keyrate="NO"               # 键盘速率：slow, normal, fast（或 NO）
keybell="NO"               # kbdcontrol(1) 中选项，使用 "off" 禁用
keychange="NO"             # 功能键默认值（或 NO）
cursor="NO"                # 光标类型 {normal 普通光标|blink 闪烁光标|destructive 反显光标}（或 NO）
scrnmap="NO"               # /usr/share/syscons/scrnmaps/* 中的屏幕映射（或 NO）
font8x16="NO"              # /usr/share/{syscons,vt}/fonts/* 中 8x16 字体（或 NO）
font8x14="NO"              # /usr/share/{syscons,vt}/fonts/* 中 8x14 字体（或 NO）
font8x8="NO"               # /usr/share/{syscons,vt}/fonts/* 中 8x8 字体（或 NO）
blanktime="300"            # 空屏时间（秒），或 "NO" 禁用
saver="NO"                 # 屏幕保护：使用 /boot/kernel/${saver}_saver.ko
moused_nondefault_enable="YES" # 除非在 rc.conf(5) 中明确覆盖，否则非默认鼠标视为启用
moused_enable="NO"          # 运行鼠标守护进程
moused_type="evdev"         # 可用设置见 rc.conf(5) 手册
moused_port="/dev/psm0"     # 鼠标端口设置
moused_flags=""             # moused 的附加参数
mousechar_start="NO"        # 如果 0xd0-0xd3 默认范围被占用，可指定其他起始范围，如 mousechar_start=3
msconvd_enable="NO"         # 运行鼠标协议转换守护进程
msconvd_type="auto"         # 可用 moused_type 类型见 rc.conf(5)
msconvd_ports=""            # msconvd 端口列表
msconvd_flags=""            # msconvd 的附加参数
allscreens_flags=""         # 为所有虚拟屏幕设置 vidcontrol 模式
allscreens_kbdflags=""      # 为所有虚拟屏幕设置 kbdcontrol 模式

##############################################################
###  邮件传输代理（MTA）选项              ######################
##############################################################

# /etc/rc.d/sendmail 设置：
sendmail_enable="NONE"              # 运行 sendmail 收件守护进程（YES/NO/NONE）
                                    # 如果为 NONE，则不启动任何 sendmail 进程
sendmail_pidfile="/var/run/sendmail.pid"  # sendmail PID 文件
sendmail_procname="/usr/sbin/sendmail"   # sendmail 进程名称
sendmail_flags="-L sm-mta -bd -q30m"     # 作为服务器运行 sendmail 的参数
sendmail_cert_create="YES"          # 如果没有证书则创建服务器证书（YES/NO）
#sendmail_cert_cn="CN"              # 生成证书的 CN（Common Name，共用名）
sendmail_submit_enable="YES"        # 启动仅本地主机的 MTA 用于邮件提交
sendmail_submit_flags="-L sm-mta -bd -q30m -ODaemonPortOptions=Addr=localhost"
                                    # 本地主机 MTA 的参数
sendmail_outbound_enable="YES"      # 出队滞留邮件（YES/NO）
sendmail_outbound_flags="-L sm-queue -q30m"  # 出站 sendmail 参数
sendmail_msp_queue_enable="YES"     # 出队滞留 clientmqueue 邮件（YES/NO）
sendmail_msp_queue_flags="-L sm-msp-queue -Ac -q30m"  # sendmail_msp_queue 守护进程参数
sendmail_rebuild_aliases="NO"       # 如有必要运行 newaliases（YES/NO）


##############################################################
###  杂项管理选项                           ###################
##############################################################

auditd_enable="NO"	# 运行审计守护进程
auditd_program="/usr/sbin/auditd"	# 审计守护进程路径
auditd_flags=""		# 传递给审计守护进程的选项
auditdistd_enable="NO"	# 运行分布式审计守护进程
auditdistd_program="/usr/sbin/auditdistd"	# auditdistd 守护进程路径
auditdistd_flags=""	# 传递给 auditdistd 守护进程的选项
cron_enable="YES"	# 运行定期任务守护进程
cron_program="/usr/sbin/cron"	# 启用时使用的 cron 可执行文件路径
cron_dst="YES"		# 智能处理夏令时转换（YES/NO）
cron_flags=""		# 传递给 cron 守护进程的选项
cfumass_enable="NO"	# 为 cfumass(4) 创建默认 LUN
cfumass_dir="/var/cfumass"	# LUN 内容文件所在目录
cfumass_image="/var/tmp/cfumass.img"	# LUN 支撑文件路径
lpd_enable="NO"		# 运行行打印守护进程
lpd_program="/usr/sbin/lpd"	# lpd 可执行文件路径
lpd_flags=""		# 传递给 lpd 的选项
nscd_enable="NO"	# 运行 NSS 缓存守护进程
chkprintcap_enable="NO"	# 在运行 lpd 之前运行 chkprintcap(8)
chkprintcap_flags="-d"	# 默认创建缺失的目录
dumpdev="AUTO"		# 崩溃转储设备（设备名、AUTO 或 NO）；稳定分支建议注释此项以遵循 kenv
dumpon_flags=""		# 传递给 dumpon(8) 的选项，紧随 dumpdev
dumpdir="/var/crash"	# 存放崩溃转储的目录
savecore_enable="YES"	# 如果存在转储设备，从中提取核心转储
savecore_flags="-m 10"	# 如果启用了 dumpdev 且存在，则使用。默认仅保存最近 10 个内核转储

service_delete_empty="NO"	# 让 'service delete' 删除空的 rc.conf.d 文件
crashinfo_enable="YES"		# 自动生成崩溃转储摘要
crashinfo_program="/usr/sbin/crashinfo"	# 生成崩溃转储摘要的脚本
quota_enable="NO"		# 启动时启用磁盘配额（或 NO）
check_quotas="YES"		# 启动时检查配额（或 NO）
quotaon_flags="-a"		# 启用所有文件系统的配额（如果启用）
quotaoff_flags="-a"		# 关机时关闭所有文件系统的配额。
quotacheck_flags="-a"		# 检查所有文件系统的配额（如果启用）
accounting_enable="NO"		# 启用进程记账（或 NO）
firstboot_sentinel="/firstboot"	# 如果此文件存在，运行带 "firstboot" 关键字的脚本。应位于可读写文件系统，以便启动完成后可删除
sysvipc_enable="NO"		# 启动时加载 System V IPC 原语（或 NO）
linux_enable="NO"		# 启动时加载 Linux 二进制兼容性（或 NO）
linux_mounts_enable="YES"	# 如果 linux_enable 为 YES，启动时挂载 Linux 特定文件系统
clear_tmp_enable="NO"		# 启动时清空 /tmp
clear_tmp_X="YES" 		# 清空并重新创建 /tmp 中的 X11 相关目录
ldconfig_insecure="NO"		# 设置为 YES 以禁用 ldconfig 安全检查
ldconfig_paths="/usr/lib/compat ${_localbase}/lib ${_localbase}/lib/compat/pkg"  # 共享库搜索路径
ldconfig32_paths="/usr/lib32/compat"  # 32 位兼容共享库搜索路径
ldconfig_local_dirs="${_localbase}/libdata/ldconfig"  # 带 ldconfig 配置文件的本地目录
ldconfig_local32_dirs="${_localbase}/libdata/ldconfig32"  # 带 32 位兼容 ldconfig 配置文件的本地目录
kern_securelevel_enable="NO"	# 内核安全级别（参见 security(7)）
kern_securelevel="-1"		# 范围：-1..3；-1 最不安全。注意：将 securelevel 设置为 0 会导致系统以安全等级 1 启动，因为 init(8) 会在 rc(8) 完成后提升级别
update_motd="YES"		# 更新 /var/run/motd 中的版本信息（或 NO）
entropy_boot_file="/boot/entropy"  # 设置为 NO 以禁用非常早期（启动早期）通过重启缓存熵
entropy_file="/entropy"  # 设置为 NO 以禁用晚期（多用户模式）通过重启缓存熵。如果 / 不可用，推荐使用 /var/db/entropy-file
entropy_dir="/var/db/entropy"  # 设置为 NO 以禁用通过 cron 缓存熵
entropy_save_sz="4096"		# 熵缓存文件大小
entropy_save_num="8"		# 要保存的熵缓存文件数量
harvest_mask="4607"		# 熵设备收集除最侵入性来源外的所有来源。（参见 'sysctl kern.random.harvest' 和 random(4)）
osrelease_enable="YES"		# 启动时更新 /var/run/os-release（或 NO）
osrelease_file="/var/run/os-release"	# 用于更新 os-release 的文件
osrelease_perms="444"		# os-release 文件的默认权限
osrelease_home_url="https://FreeBSD.org"	# /var/run/os-release 中的 HOME_URL
osrelease_documentation_url="https://docs.FreeBSD.org"	# /var/run/os-release 中的 DOCUMENTATION_URL
osrelease_support_url="https://www.FreeBSD.org/support"	# /var/run/os-release 中的 SUPPORT_URL
osrelease_bug_report_url="https://bugs.FreeBSD.org"	# /var/run/os-release 中的 BUG_REPORT_URL
dmesg_enable="YES"		# 将 dmesg(8) 保存到 /var/run/dmesg.boot
dmesg_umask="022"		# /var/run/dmesg.boot 文件的默认 umask
watchdogd_enable="NO"		# 启动软件看门狗守护进程
watchdogd_flags=""		# watchdogd 的参数（如果启用）
watchdogd_timeout=""		# watchdogd 超时，覆盖 watchdogd_flags 中的 -t
watchdogd_shutdown_timeout=""	# 停止 watchdogd 后使用的超时，仅对系统关机有效，覆盖 watchdogd_flags 中的 -x 选项
devfs_rulesets="/etc/defaults/devfs.rules /etc/devfs.rules"  # 包含 devfs(8) 规则的文件
devfs_system_ruleset=""		# 要应用于 /dev 的规则集名称（非编号）
devfs_set_rulesets=""		# 要应用的 /mount/dev=ruleset_name 列表（必须已挂载，即 fstab(5)）
devfs_load_rulesets="YES"	# 始终加载默认规则集
performance_cx_lowest="NONE"	# 在线 CPU 空闲状态
performance_cpu_freq="NONE"	# 在线 CPU 频率
economy_cx_lowest="Cmax"	# 离线 CPU 空闲状态
economy_cpu_freq="NONE"		# 离线 CPU 频率
virecover_enable="YES"		# 为 vi(1) 编辑器执行维护操作
ugidfw_enable="NO"		# 启动时加载 mac_bsdextended(4) 规则
bsdextended_script="/etc/rc.bsdextended"	# 默认 mac_bsdextended(4) 规则文件
newsyslog_enable="YES"		# 启动时运行 newsyslog
newsyslog_flags="-CN"		# newsyslog 参数，用于创建标记文件
mixer_enable="YES"		# 运行音量混合器
opensm_enable="NO"		# 启动 infiniband 设备的 Opensm(8)，默认关闭
nuageinit_enable="NO"		# 启动时运行 nuageinit
virtual_oss_enable="NO"		# 启动时运行 virtual_oss
rctl_enable="YES"		# 启动时加载 rctl(8) 规则
rctl_rules="/etc/rctl.conf"	# rctl(8) 规则文件，参见 rctl.conf(5)
iovctl_files=""			# iovctl(8) 的配置文件

##############################################################
### Jail 配置（参见 rc.conf(5) 手册页）               ##########
##############################################################
jail_enable="NO"		# 设置为 NO 禁止启动任何 jail
jail_conf="/etc/jail.conf"	# jail(8) 的配置文件
jail_confwarn="YES"		# 防止关于过时的每个 jail 配置的警告
jail_parallel_start="NO"	# 后台启动 jail
jail_list=""			# 用空格分隔的 jail 名称列表
jail_reverse_stop="NO"		# 以逆序停止 jail

##############################################################
### 定义 source_rc_confs                                   ###
### 这是 /etc/rc.* 脚本用于安全引用 rc_conf_files 覆盖的机制  ###
##############################################################

# 如果 source_rc_confs 尚未定义，则定义之
if [ -z "${source_rc_confs_defined}" ]; then
	source_rc_confs_defined=yes

	# 定义 source_rc_confs 函数，用于安全地加载 rc_conf_files 中列出的配置文件
	source_rc_confs() {
		local i sourced_files

		# 遍历 rc_conf_files 列表
		for i in ${rc_conf_files}; do
			case ${sourced_files} in
			*:$i:*)  # 如果已加载过该文件，则跳过
				;;
			*)
				# 将当前文件标记为已加载
				sourced_files="${sourced_files}:$i:"
				# 如果文件可读，则加载它
				if [ -r $i ]; then
					. $i
				fi
				;;
			esac
		done

		# 再次遍历 rc_conf_files，处理可能在第一次加载中被重新定义的新文件
		for i in ${rc_conf_files}; do
			case ${sourced_files} in
			*:$i:*)  # 如果已加载过该文件，则跳过
				;;
			*)
				sourced_files="${sourced_files}:$i:"
				if [ -r $i ]; then
					. $i
				fi
				;;
			esac
		done
	}
fi

# 允许厂商在 /etc/default/rc.conf 中覆盖 FreeBSD 默认设置，
# 而无需手动管理 /etc/rc.conf。
if [ -r /etc/defaults/vendor.conf ]; then
	. /etc/defaults/vendor.conf
fi
```

## 课后习题

1. 创建一个自定义服务脚本放入 `/usr/local/etc/rc.d/` 目录，分析 `rc.subr` 中依赖关系检查的实现逻辑，评估其与 systemd unit 依赖模型的差异。
2. 修改 `rc_debug` 为 YES，追踪一次服务启动的完整流程，对比正常启动与调试启动的输出差异，分析调试输出中各阶段的执行顺序。
3. 禁用 `rc_startmsgs` 并修改关键服务的启动顺序（通过 `REQUIRE` 和 `BEFORE` 关键字），记录系统启动行为的变化。
