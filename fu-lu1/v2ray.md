# V2Ray

V2Ray 是一款支持多种代理协议（VMess、Shadowsocks 等）和流量路由功能的代理软件。路由模块可根据目标地址、端口等条件将流量分发至不同的出站代理，实现灵活的流量分流。FreeBSD 系统中，V2Ray 可通过 pkg(8) 或 Ports 安装。

Xray-core 是 V2Ray 的分支，在保持核心功能的基础上优化了性能并扩展了功能。两者配置基本兼容，Xray 可参照 V2Ray 的配置方法。相较于 Xray，V2Ray 对部分新协议支持更新较慢。注意：VLESS 协议在 V2Ray 中已被弃用（官方文档标注“VLESS 已被弃用并且可能被移除”），其活跃开发（包括 XTLS、REALITY 等增强）在 Xray-core 中进行。

## 安装 V2Ray

### 安装 V2Ray

- 使用 pkg 安装：

```sh
# pkg install v2ray
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/net/v2ray/
# make install clean
```

### 安装 Xray-core

使用 pkg 安装 Xray-core：

```sh
# pkg install xray-core
```

或者使用 Ports 安装 Xray-core：

```sh
# cd /usr/ports/security/xray-core/
# make install clean
```

## 启动代理软件

安装完成后需启动代理软件。如果已在其他平台（如 Windows）上使用 V2RayN 等客户端配置了代理节点，可将配置导出为 config.json 文件并复制到 FreeBSD 系统中。

使用指定的配置文件启动 V2Ray：

```sh
# v2ray run -c /path/to/config.json
```

使用指定的配置文件启动 Xray：

```sh
# xray run -c /path/to/config.json
```

此时，代理软件应已成功启动，可通过日志或进程状态验证。

## 配置代理参数

Xray 配置文件与 V2Ray 基本兼容，但部分高级功能的配置方式有所不同。

代理软件启动后，需配置相关软件的代理参数。V2Ray/Xray 采用入站（inbounds）和出站（outbounds）的架构设计：inbounds 定义代理软件如何接收流量，outbounds 定义代理软件如何转发流量。

编辑 config.json 文件，找到对应的 inbounds 属性。inbounds 是一个数组，其中的每个元素表示一项入站接口配置，包括监听地址、端口号和代理协议类型。在需要使用代理的软件中，将代理服务器地址和端口号设置为此处对应的值。

### 配置浏览器使用代理（以 Firefox 为例）

#### 查找端口

打开配置文件 config.json，在 inbounds 字段下确认端口号。通常 Windows 导出的配置中，SOCKS5 端口为 10808，HTTP 端口为 10809。

例如，其中一个入站接口的 `protocol` 为 `http`、`listen` 为 **127.0.0.1**、`port` 为 10809。即该入站接口在本地回环地址的 10809 端口监听 HTTP 代理请求。

#### Firefox 设置

- 打开设置 → 网络设置 → 代理服务器。
- 选择“手动代理配置”。
- 对于 HTTP 代理：将地址设置为 **127.0.0.1**，端口设置为 10809。
- 对于 SOCKS 代理：将 SOCKS 主机填写为 **127.0.0.1**，端口填写为 10808。

> **重要**
>
> 勾选底部的“使用 SOCKS v5 时代理 DNS”（Proxy DNS when using SOCKS v5），将域名解析请求也通过代理服务器转发，以绕过 DNS 污染。

### 配置终端命令行程序

大多数终端命令会读取环境变量 `HTTP_PROXY`、`HTTPS_PROXY` 和 `ALL_PROXY`，并根据其取值自动使用相应的代理。

下面的命令适用于 sh、Bash、Zsh（临时设置，仅当前会话生效）：

```sh
$ export HTTP_PROXY="http://127.0.0.1:10809" # 设置 HTTP 代理
$ export HTTPS_PROXY="http://127.0.0.1:10809" # 设置 HTTPS 代理
$ export ALL_PROXY="socks5://127.0.0.1:10808" # 设置 SOCKS5 代理
```

若需持久化配置，应使用用户分级方法。

设置完成后，在 Firefox 浏览器中访问网页并观察 V2Ray 日志，可确认浏览器流量已通过代理转发。终端中的命令行程序同样通过代理访问网络，但部分命令对环境变量的支持方式不同，需要根据具体软件查阅其代理配置方法。

## 代理流量分流

部分网址无须通过代理服务器访问，例如境内网站或本地网络资源，需要分流处理。

打开 config.json 文件，找到 routing 属性。其中的 rules 子属性用于配置流量分流规则，每条规则通常包含 ip 或 domain 等匹配条件。IP 或域名匹配到某条规则时，V2Ray 根据 outboundTag 将流量转发至对应的出站配置（如 proxy 表示代理、direct 表示直连、block 表示拦截）。将需要分流的域名或 IP 配置至相应规则即可，相关细节可参考 [V2Ray 官方文档](https://www.v2fly.org/)。通过 V2Ray 客户端导出的配置文件通常已包含默认的分流规则。

V2Ray 还预置了 geosite.dat 和 geoip.dat 两个资源文件：geosite.dat 按分类保存各类域名信息，geoip.dat 按分类保存各类 IP 地址信息。资源文件路径可通过设置环境变量 `V2RAY_LOCATION_ASSET` 指定，V2Ray 会自动在该路径下查找 geosite.dat 和 geoip.dat 文件。对于 Xray，则使用 `XRAY_LOCATION_ASSET` 环境变量指定资源文件路径。注意：如果使用 Xray，请确保正确设置 `XRAY_LOCATION_ASSET` 环境变量，否则可能导致资源文件加载失败。

例如，在直连规则中可以配置 geosite 中的 cn 域名走直连：

```json
      {
        "domain": [
          "geosite:cn"
        ],
        "outboundTag": "direct",
        "type": "field"
      },
```

V2Ray 社区提供的 cn 域名直连规则可根据实际需求扩展。也可在 GitHub 上查找由社区维护的 geosite 和 geoip 文件（如 [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat)），其中通常对“白名单模式”和“黑名单模式”的配置方式有较为详细的说明。

## 故障排除与未竟事宜

### Xray 资源文件加载失败（geosite.dat/geoip.dat）

相关目录文件结构：

```sh
/usr/local/
├── bin/
│   ├── v2ray # V2Ray 可执行文件
│   └── xray # Xray 可执行文件
├── etc/
│   └── xray-core/
│       └── config.json # Xray 配置文件
└── share/
    └── xray-core/
        ├── geosite.dat # 域名分类资源文件
        └── geoip.dat # IP 地址分类资源文件
```

使用 Xray 时可能遇到资源文件加载失败的问题。FreeBSD 中，xray-core 的 pkg 安装资源文件位于 **/usr/local/share/xray-core/**，但程序默认在可执行文件同级目录 **/usr/local/bin/** 查找。如果启动时报 `open /usr/local/bin/geosite.dat: no such file or directory` 错误，可采用以下两种方案：

#### 终端临时运行或用户分级方案

**临时运行**

通过环境变量指定资源路径，这种方式适用于单次运行或测试场景：

```sh
# env XRAY_LOCATION_ASSET=/usr/local/share/xray-core/ xray run -c /path/to/config.json
```

> **技巧**
>
> 如果需要在后台运行，可在命令末尾添加 `&` 符号。但此方式不能使进程脱离当前终端会话；如果需要关闭终端后进程仍持续运行，请使用 `nohup` 或 `disown`。

**持久化配置**

通过用户分级方法持久化配置，使环境变量在每次登录时自动生效，且与 Shell 类型无关。编辑 **~/.login_conf** 文件：

```ini
me:\
	:setenv=XRAY_LOCATION_ASSET=/usr/local/share/xray-core/:
```

编辑后，需要执行以下命令来更新登录能力数据库：

```sh
$ cap_mkdb ~/.login_conf
```

配置完成后，应重新登录使更改生效。对于系统服务运行方式（如 rc.conf），因为系统服务通过 sysrc 注入环境变量，无需此配置。

建立软链接，使 Xray 无论从何处启动都能找到资源文件：

```sh
# ln -s /usr/local/share/xray-core/geosite.dat /usr/local/bin/geosite.dat
# ln -s /usr/local/share/xray-core/geoip.dat /usr/local/bin/geoip.dat
```

#### 系统服务运行方案

**放置配置文件：**

首先，将配置移至系统默认目录并修正权限：

```sh
# cp /path/to/config.json /usr/local/etc/xray-core/config.json
# chown -R v2ray:v2ray /usr/local/etc/xray-core/      # 将 /usr/local/etc/xray-core/ 目录（及 config.json 等文件）的所有权递归修改为 v2ray 用户和组。
```

- FreeBSD 的 `security/xray-core` 没有创建独立的 `xray` 用户/组，而是沿用 `net/v2ray` 的 `v2ray:v2ray`，这是为了保持用户权限管理的一致性。

如果 **/usr/local/etc/xray-core/** 目录下存在其他 `.json` 样例文件，因 Xray 可能扫描目录下的所有 JSON 文件，应将其移除，避免配置冲突。

**配置 rc.conf 文件：**

执行以下命令开启服务并注入环境变量：

```sh
# sysrc xray_enable="YES"
# sysrc xray_config="/usr/local/etc/xray-core"      # 指向 xray-core 的代理配置目录，该目录在安装 xray-core 时自动生成
# sysrc xray_env="XRAY_LOCATION_ASSET=/usr/local/share/xray-core"      # 指向的是 xray-core 的资源文件目录
```

**服务管理：**

- 启动：`service xray start`
- 停止：`service xray stop`
- 重新启用自启动：使用 `service xray enable`
