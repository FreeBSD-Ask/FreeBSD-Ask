# 7.3 Mihomo 配置

Mihomo 是 Clash 系列的衍生版本，已在 FreeBSD 的 Ports 中提供。

本节将介绍 Mihomo 的安装与配置方法。

## 安装 Mihomo

使用 pkg 安装：

```sh
# pkg install net/mihomo
```

或者使用 Ports 安装：

```sh
# cd /usr/ports/net/mihomo/
# make install clean
```

## Mihomo 文件结构

Mihomo 的文件结构如下：

```sh
/usr/
├── ports/
│   └── net/
│       └── mihomo/ # Mihomo Ports 目录
├── local/
│   ├── bin/
│   │   └── mihomo # Mihomo 可执行文件
│   └── etc/
│       └── rc.d/
│           └── mihomo # Mihomo RC 服务脚本
└── etc/
    └── rc.conf # 系统服务配置文件
```

若认为配置较为复杂，也可在 Linux 兼容层中使用，FreeBSD 的网络同样可受其控制，这得益于 FreeBSD 强大的 Linux 二进制兼容能力。

## RC 脚本

已向 Ports 维护者发出请求合并（[Bug 291295 - net/mihomo: Add rc.conf and some Post-installation](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=291295)），该请求旨在为 Mihomo 添加系统服务管理支持，但目前尚未收到回应。在官方集成完成前，可使用下文提供的自定义 RC 脚本实现服务化管理。

### RC 脚本

为便于管理 Mihomo 服务，可以使用以下脚本。将以下脚本保存为名为 mihomo 的文件，并放置到路径 `/usr/local/etc/rc.d/` 下。使用 root 账户为该文件赋予可执行权限：`chmod +x /usr/local/etc/rc.d/mihomo`。

```sh
#!/bin/sh

. /etc/rc.subr   # 引入 rc.d 脚本框架，这是 FreeBSD 服务脚本的标准前置依赖

name="mihomo"    # 定义服务名，用于标识和管理该服务
desc="mihomo server"    # 服务描述，用于提供服务的简要说明
rcvar="mihomo_enable"    # 服务开关变量，控制服务是否开机自启

: ${mihomo_datadir:="/var/run/mihomo"}
: ${mihomo_user:="root"}    # 默认用户；如使用其他用户，请确保 /etc/mihomo 目录及 $pidfile 和 log 文件可写，这是权限安全的基本要求
: ${mihomo_extra_flags:=""}	# mihomo 的额外参数，用于传递自定义启动选项

procname="/usr/local/bin/mihomo"    # 与 pidfile 配合，用于检测服务进程，这是 rc.d 框架识别服务进程的关键
pidfile="${mihomo_datadir}/mihomo.pid"    # 用于检测服务进程，存储主进程的进程标识符（Process ID，PID）
logfile="${mihomo_datadir}/mihomo.log"
start_cmd="mihomo_start"    # 设置 start 命令调用 mihomo_start 函数，stop 等命令由 rc.d 框架默认实现，这种设计能自定义启动逻辑
extra_commands="init reconfig regeoip"    # 设置其他的自定义命令，扩展 rc.d 框架的标准命令集
reconfig_cmd="mihomo_reconfig"    # 指定 reconfig 命令调用 mihomo_reconfig 函数，用于下载 config.yaml 文件
regeoip_cmd="mihomo_regeoip"    # 指定 regeoip 命令调用 mihomo_regeoip 函数，用于下载 geoip.dat 文件，可通过 mihomo_extra_flags="-m" 指定使用该文件
init_cmd="mihomo_init"    # 指定 init 命令调用 mihomo_init 函数。创建数据文件目录，指定属主，避免普通用户身份执行时的读写权限问题

mihomo_start()
{    # 使用 daemon 启动 mihomo，指定 -p 参数使用 pidfile，使 mihomo 成为 daemon 的子进程，由 daemon 自动管理 pidfile，从而在 mihomo 进程退出时自动清理 pidfile，这是 Unix 守护进程管理的标准实践
	daemon -u ${mihomo_user} -p "$pidfile" -o "${logfile}" $procname -d "${mihomo_datadir}" -f "${mihomo_datadir}/config.yaml" ${mihomo_extra_flags}
}
mihomo_reconfig()
{
	startmsg "begin to refresh config.yaml"
	startmsg "config.yaml : ${mihomo_config}"
	if ( fetch -o ${mihomo_datadir}/config.yaml.new "${mihomo_config}" );then
		mv ${mihomo_datadir}/config.yaml.new ${mihomo_datadir}/config.yaml    # 下载成功将覆盖原有配置，下载失败保留原有配置，这种原子操作保证了配置更新的安全性
        startmsg "rename config.yaml.new to config.yaml"
	else
		err "fetch config.yaml failed! check $$mihomo_config!"
	fi
}
mihomo_regeoip()
{
	startmsg "begin to refresh geoip.dat"
	startmsg "geoip.dat : $mihomo_geoip"
	if ( fetch -o ${mihomo_datadir}/geoip.new "${mihomo_geoip}" );then
		mv ${mihomo_datadir}/geoip.new ${mihomo_datadir}/geoip.dat
        startmsg "rename geoip.new to geoip.dat"
	else
		err "fetch geoip.dat failed! check $$mihomo_geoip"
	fi
}
mihomo_init()
{
	startmsg "begin init"
	install -d -m 0700 -o ${mihomo_user} ${mihomo_datadir}
    startmsg "all data is in ${mihomo_datadir}"
    startmsg "remember reconfig/regeoip before start"
}

load_rc_config $name
run_rc_command "$1"
```

### 可用参数及选项

RC 脚本提供了多个命令行参数和配置选项，以下是一些常用参数。这些命令会直接将配置写入 `/etc/rc.conf` 文件，如配置有误，可直接修改对应行，`/etc/rc.conf` 文件是 FreeBSD 系统配置的核心文件。

- 启用 Mihomo 服务项及开机自启，将服务注册到系统启动流程中：

```sh
service mihomo enable
```

- 立即启用 Mihomo，启动服务进程：

```sh
service mihomo start
```

- 立即停用 Mihomo，终止服务进程：

```sh
service mihomo stop
```

- 查看 Mihomo 状态，检查服务运行状态：

```sh
service mihomo status
```

- 在此指定订阅链接地址（示例地址仅用于演示，需自行替换为有效链接），订阅链接是获取代理节点配置的标准方式：

```sh
sysrc mihomo_config="https://xxxx.yyy"
```

- 用于地理位置判断的 GeoIP 数据，主要用于根据 IP 地址的地理归属进行流量分流或规则匹配，这是实现智能分流的基础数据：

```sh
sysrc mihomo_geoip="https://ghfast.top/https://github.com/MetaCubeX/meta-rules-dat/releases/download/latest/geoip.dat" # 可选，但建议使用
```

- 指定其他 Mihomo 参数，用于传递额外的自定义选项：

```sh
sysrc mihomo_extra_flags="-m" # 可选，但建议使用
```

- `-m`：启用 geodata 模式，使 Mihomo 使用 geosite.dat 和 geoip.dat 文件进行规则匹配，而非默认的 site.dat 和 ip.dat。

- 指定调用 Mihomo 的用户，用于控制服务运行的身份，这是安全实践的重要组成部分：

```sh
sysrc mihomo_user="mihomo"  # 默认用户是 root
```

- 指定 Mihomo 的数据路径，配置服务运行时数据的存储位置：

```sh
sysrc mihomo_datadir="/var/run/mihomo"
```

相关文件结构：

```sh
/var/
└── run/
    └── mihomo/ # Mihomo 数据目录
        ├── mihomo.pid # 进程标识符（Process ID，PID）文件
        ├── mihomo.log # 日志文件
        ├── config.yaml # 配置文件
        └── geoip.dat # GeoIP 数据文件
```

- 初始化（创建）Mihomo 的数据目录，准备服务运行环境：

```sh
service mihomo init
```

- 更新订阅。`start` 前先更新即可使用最新的订阅信息，确保配置文件是最新版本：

```sh
service mihomo reconfig
```

- 更新 regeoip，更新地理位置数据库：

```sh
service mihomo regeoip # 首次启用时建议使用，但无需频繁更新，因为 IP 地理位置数据变化相对缓慢
```

### 最小 RC 示例

以下是一个最简配置示例，可在理解其含义并按需修改后写入 `/etc/rc.conf` 文件，这个示例展示了最小化的可用配置：

```ini
mihomo_config="https://xxx.yyy" # 实际订阅链接地址，请勿照抄，否则将不生效
mihomo_geoip="https://ghfast.top/https://github.com/MetaCubeX/meta-rules-dat/releases/download/latest/geoip.dat" # GeoIP 数据
mihomo_enable="YES" # 开机启用/服务项
```

可根据实际需求自行调整配置，通过组合上述参数实现个性化设置。

### 未竟事宜

以下是一些有待探索的问题，可自行研究解决方案，这些问题代表了该领域进一步探索的方向：

- 如何实现“直连”、“代理”、“全局”的分流？这三种模式是代理系统的基础功能模式。

- 如何实现 TUN 虚拟网卡代理（是否可能）？TUN 模式可以实现更底层的网络流量拦截。

- 如何根据订阅链接进行测速？测速功能对于选择最优代理节点具有重要意义。

- 如何指定订阅链接中代理组的某个代理？（比如仅使用位于美国的某个代理 A）这涉及代理节点的精细化选择。

## Clash for FreeBSD

### 环境准备

FreeBSD 默认登录 Shell 可能不是 `bash`，执行以下命令前请先切换到 `bash`：

```shell
$ bash
```

建议使用 `root` 权限账号。

```shell
# pkg update
# pkg install -y bash curl gtar gzip
```

说明：

- 当前脚本通过 `bash` 执行。
- `freebsd-rc` 后端依赖 `service` 与 `/usr/local/etc/rc.d`。

### 安装与初始化

```shell
$ git clone --branch master --depth 1 https://github.com/wenyinos/clash-freebsd.git
$ cd clash-freebsd
$ export KERNEL_TYPE=mihomo
# bash install.sh
```

首次配置：

```shell
$ clashctl add <订阅链接> <名称>
$ clashctl use
$ clashctl select
$ clashon
$ clashctl status
```

### FreeBSD 服务管理（rc.d）

系统安装默认使用 `freebsd-rc` 后端，服务名：`clash_freebsd`。

```shell
# service clash_freebsd status
# service clash_freebsd start
# service clash_freebsd stop
# service clash_freebsd restart
```

管理内核服务开机自启：

```shell
# clashctl autostart on
# clashctl autostart status
# clashctl autostart off
```

说明：

- `clashctl autostart on` 只影响 rc.d 服务是否随系统启动。
- `service` 与 `autostart` 命令需要 root 权限（请使用 root 或 `sudo`）。
- FreeBSD 自启配置文件：`/etc/rc.conf.d/clash_freebsd`。

### Tun 与路由诊断（FreeBSD）

Tun 设备通常为 `/dev/tun*`。

```shell
# clashctl tun on
# clashctl tun off
# clashctl tun doctor
$ route -n get default
$ netstat -rn -f inet
```

Tun 未生效时优先检查：

- `tun on/off` 需要 root 权限
- `ls -l /dev/tun*`
- 当前用户权限（建议 root）
- 默认路由是否已接管到 tun 接口

### 常用排障命令

```shell
$ clashctl doctor
$ clashctl logs
$ clashctl logs mihomo
$ clashctl config regen
```

### 卸载

```shell
# bash uninstall.sh
```

彻底清理运行时数据：

```shell
# bash uninstall.sh --purge-runtime
```

### 参考文献

- wenyinos. 一个更完整、更优雅的 FreeBSD Clash / Mihomo 运行平台[EB/OL]. [2026-04-26]. <https://github.com/wenyinos/clash-freebsd>. 提供了 FreeBSD 下 Clash 代理的完整部署方案，支持订阅链接管理。

### 未竟事宜

以下是 Clash  FreeBSD 项目有待改进的地方，这些改进方向有助于提高项目的通用性和易用性：

- 与 bash 解耦，支持默认的 sh，使其更符合 FreeBSD 的默认环境。

## 课后习题

1. 重构 Mihomo RC 脚本，将其与 bash 解耦并移植到 FreeBSD 默认的 sh 环境，验证功能完整性并对比与原脚本的差异。
