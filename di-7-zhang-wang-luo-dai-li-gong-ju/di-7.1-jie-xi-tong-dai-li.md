# 7.1 系统代理

代理（Proxy）技术是计算机网络中的基础概念，其核心思想是在客户端与目标服务器之间引入中间节点，由中间节点代为转发请求和响应。代理协议主要分为两类：HTTP 代理（定义于 RFC 7230/7231，工作在应用层）和 SOCKS 代理（定义于 RFC 1928，工作在会话层）。HTTP 代理仅支持 HTTP/HTTPS 协议的转发，而 SOCKS5 代理可转发任意 TCP 连接，适用范围更广。

在 FreeBSD 系统中，系统级代理通常通过 `HTTP_PROXY`、`HTTPS_PROXY`、`FTP_PROXY` 和 `ALL_PROXY` 等环境变量实现，这些变量被 pkg(8)、fetch(1) 等基本系统工具和多数第三方应用程序所识别。

## 代理工作原理

从网络通信的理论视角来看，代理的工作流程可概括为：客户端发起请求 → 请求被重定向至代理服务器 → 代理服务器将请求转发至目标服务器 → 目标服务器响应代理服务器 → 代理服务器将响应返回客户端。在此过程中，目标服务器看到的是代理服务器的地址，而非客户端的真实地址。

代理按部署模式可分为三类：

- **正向代理（Forward Proxy）**：客户端显式配置代理地址，代理代表客户端向外部服务器发起请求。本节讨论的系统代理即属于正向代理。正向代理的典型用途包括突破网络访问限制和缓存加速。
- **反向代理（Reverse Proxy）**：代理代表服务器接收客户端请求，客户端不知道真实服务器的地址。反向代理的典型用途包括负载均衡、SSL 终结和静态内容缓存。
- **透明代理（Transparent Proxy）**：客户端无需配置，网络设备（如路由器）将流量重定向至代理。透明代理的典型用途包括企业网络的内容过滤和流量监控。

FreeBSD 的环境变量代理机制属于正向代理范畴。应用程序在发起网络请求时，会检查 `HTTP_PROXY` 等环境变量，若已设置，则将请求发送至指定的代理服务器而非目标服务器。此机制由 fetch(3) 库函数实现，pkg(8) 和多数 Ports 软件均依赖此库。

在 V2Ray 或 Clash 等代理软件开启局域网连接功能后，便可按照下文进行配置。

在配置系统代理前，需要查看当前用户正在使用的 Shell 类型，因不同 Shell 对环境变量的设置方式存在差异。执行以下命令可查看当前 Shell：

```sh
$ echo $SHELL
```

## 配置 HTTP_PROXY 代理

本节介绍通过环境变量配置系统代理的方法。多数命令行工具会读取 HTTP_PROXY、HTTPS_PROXY、ALL_PROXY 等环境变量来确定是否使用代理。

### 若使用 sh、bash 或 zsh

在 sh、bash 或 zsh 中配置代理时，需注意以下事项。

> **注意**
>
> 在 sh、bash 或 zsh 中，环境变量 `HTTP_PROXY` 通常使用大写形式。部分应用程序（如 curl、wget）也会识别小写形式 `http_proxy`，但不同程序的行为不一致，建议统一使用大写形式以确保兼容性。

设置 HTTP 代理环境变量，该变量将被当前 Shell 及其子进程继承：

```sh
# export HTTP_PROXY=http://192.168.X.X:7890
```

> **警告**
>
> 示例中的 IP 地址和端口号 192.168.X.X:7890 需替换为实际的代理服务端点。

取消已设置的 HTTP 代理环境变量：

```sh
# unset HTTP_PROXY
```

### 若使用 csh

在 csh 或 tcsh 中配置代理时，需注意以下事项。

> **注意**
>
> 在 csh 或 tcsh 中，环境变量 `http_proxy` 必须使用小写形式，大写形式不会生效。

在 csh 或 tcsh 中设置 HTTP 代理环境变量，需使用该 Shell 特有的 `setenv` 命令：

```sh
# setenv http_proxy http://192.168.X.X:7890
```

在 csh 或 tcsh 中取消已设置的 HTTP 代理环境变量，使用对应的 `unsetenv` 命令：

```sh
# unsetenv http_proxy
```

## 配置 Git 代理

Git 的代理配置方法，请参见本书其他章节。

## 为浏览器配置代理

本节介绍 Chromium 和 Firefox 浏览器的代理配置方法。

### chrome 命令选项

[chromium](https://www.chromium.org/) 是 Google Chrome 浏览器的开源版本，支持多种命令行参数。

Chromium 浏览器在 `~/.config` 等目录下并无专门的代理配置文件，也不支持通过环境变量指定默认代理服务器，但可通过启动参数设置代理。

为支持此参数的应用程序指定代理服务器和端口：

```sh
--proxy-server="<IP 地址>:<端口>"
```

启动 Chrome 并使用指定的本地代理服务器：

```sh
$ chrome --proxy-server="127.0.0.1:1234"
```

默认使用 HTTP 协议，为支持此参数的应用程序指定 SOCKS 代理服务器和端口：

```sh
--proxy-server="socks://<IP 地址>:<端口>"
```

为支持此参数的应用程序指定 SOCKS4 代理服务器和端口：

```sh
--proxy-server="socks4://<IP 地址>:<端口>"
```

在图形界面下使 Chromium 默认使用代理打开，可通过修改桌面启动文件实现持久化配置。

找到桌面环境为 Chromium 创建的桌面（desktop）文件，通常位于 `~/.local/share/applications/` 目录下：

```sh
~/
└── .local/
    └── share/
        └── applications/
            └── chromium-browser.desktop # Chromium 桌面启动文件
```

使用编辑器打开上述目录下的 Chromium desktop 文件 `chromium-browser.desktop`，找到 `Exec=chrome %U` 这一行，并在其后添加所需参数：

```ini
Comment[zh_CN]=Google web browser based on WebKit
Comment=Google web browser based on WebKit
Encoding=UTF-8
Exec=chrome %U
GenericName[zh_CN]=
......
```

启动 Chromium 并使用指定的代理服务器：

```sh
Exec=chrome %U --proxy-server="192.168.2.163:20172"
```

### 为 Firefox 单独配置代理

Firefox 浏览器在设置页面的网络设置选项卡中提供了图形化代理配置模块。

![Firefox 代理设置](../.gitbook/assets/FF-Proxy.png)

### 参考文献

- The Chromium team. chromium(1) USER COMMANDS chromium(1) NAME chromium - the web browser from Google[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?query=chrome>. 阐述 Chromium 命令行代理参数配置，为本章节提供技术依据。
- Owynn, graudeejs, rjohn, olli@, Sevendogsbsd, kpedersen. chromium proxy settings page doesn't exist[EB/OL]. [2026-03-25]. <https://forums.freebsd.org/threads/chromium-proxy-settings-page-doesnt-exist.31927/>. 提供了 FreeBSD 下 Chromium 代理配置的实践解决方案。

## 课后习题

1. 修改 Chromium 的 desktop 文件，使其默认使用 SOCKS5 代理启动，验证其 DNS 查询是否也通过代理转发，并将方法贡献至本节。

2. 为 csh 编写一个代理开关脚本，在设置代理后验证 git、fetch 等命令的实际网络流量路径，思考为何不同 Shell 对环境变量大小写有不同约定，究竟是哪个文件规定的。

3. 为 Firefox 编写一个 shell 脚本，通过修改其配置文件实现代理自动切换，并对比与 Chromium 参数配置方式在用户可控性上的差异。最终尝试将其贡献到 Firefox 项目。
