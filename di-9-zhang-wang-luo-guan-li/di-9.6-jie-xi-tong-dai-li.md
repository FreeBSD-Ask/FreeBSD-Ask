# 9.6 系统代理

代理（Proxy）技术是计算机网络中的基础概念，其核心原理是在客户端与目标服务器之间引入中间节点，由中间节点代为转发请求和响应。

## 代理工作原理

代理的工作流程可概括为：客户端发起请求 → 请求重定向至代理服务器 → 代理服务器将请求转发至目标服务器 → 目标服务器响应代理服务器 → 代理服务器将响应返回客户端。在此过程中，目标服务器获知的是代理服务器的地址，而非客户端的真实地址。

代理按部署模式可分为三类：

| 类型 | 说明 | 典型用途 |
| ---- | ---- | -------- |
| **正向代理（Forward Proxy）** | 客户端显式配置代理地址，代理代表客户端向外部服务器发起请求 | 突破网络访问限制和缓存加速 |
| **反向代理（Reverse Proxy）** | 代理代表服务器接收客户端请求，客户端不知道真实服务器的地址 | 负载均衡、SSL 终结和静态内容缓存 |
| **透明代理（Transparent Proxy）** | 客户端无需配置，网络设备（如路由器）将流量重定向至代理 | 企业网络的内容过滤和流量监控 |

三种代理模式的数据流对比：

```sh
代理模式对比

  正向代理（Forward Proxy）
  客户端 ──→ 代理服务器 ──→ 目标服务器
  (已知代理)  (代表客户端)  (只看到代理 IP)

  反向代理（Reverse Proxy）
  客户端 ──→ 代理服务器 ──→ 真实服务器
  (不知真实服务器)  (代表服务器)  (隐藏在后端)

  透明代理（Transparent Proxy）
  客户端 ──→ 网关/路由器 ──→ 代理 ──→ 目标服务器
  (无感知)    (流量重定向)   (透明拦截)
```

配置系统代理前，需了解 FreeBSD 提供的环境变量配置方式。

## 配置 HTTP_PROXY 代理

通过设置 HTTP_PROXY、HTTPS_PROXY、ALL_PROXY 等环境变量，可使多数命令行工具通过代理转发流量。以下为配置方法。

### 临时设置

在当前 shell 会话中临时设置代理环境变量：

```sh
$ export HTTP_PROXY=http://192.168.X.X:7890
```

> **警告**
>
> 示例中的 IP 地址和端口号 **192.168.X.X:7890** 需替换为实际的代理服务端点。

取消已设置的 HTTP 代理环境变量：

```sh
$ unset HTTP_PROXY
```

### 持久化配置（用户分级方法）

通过用户分级方法持久化配置，使代理环境变量在每次登录时自动生效，且与 Shell 类型无关。编辑 **~/.login_conf** 文件：

```ini
me:\
	:setenv=HTTP_PROXY=http://192.168.X.X:7890,HTTPS_PROXY=http://192.168.X.X:7890:
```

编辑后，需要执行以下命令来更新登录能力数据库：

```sh
$ cap_mkdb ~/.login_conf
```

重新登录后生效。

## 配置 Git 代理

Git 支持通过 `http.proxy` 和 `core.gitProxy` 等配置项设置代理。

## 为浏览器配置代理

### Chrome 命令选项

[chromium](https://www.chromium.org/) 是 Google Chrome 浏览器的开源版本，支持多种命令行参数。

Chromium 浏览器在 **~/.config** 等目录下并无独立的代理配置界面，但支持通过 `http_proxy`/`https_proxy` 环境变量（非 Gnome/KDE 环境下）及启动参数设置代理。

可按以下格式指定代理服务器和端口：

```sh
--proxy-server="<IP 地址>:<端口>"
```

启动 Chrome 并使用指定的本地代理服务器：

```sh
$ chrome --proxy-server="127.0.0.1:1234"
```

默认使用 HTTP 协议。指定 SOCKS 代理服务器和端口：

```sh
--proxy-server="socks://<IP 地址>:<端口>"
```

指定 SOCKS4 代理服务器和端口：

```sh
--proxy-server="socks4://<IP 地址>:<端口>"
```

要使 Chromium 在图形界面中默认通过代理启动，可修改桌面启动文件以实现持久化配置。

找到桌面环境为 Chromium 创建的 desktop 文件，通常位于 **~/.local/share/applications/** 目录：

使用编辑器打开 Chromium desktop 文件 `chromium-browser.desktop`，找到 `Exec=chrome %U` 一行并在其后添加所需参数：

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

> **技巧**
>
> 上述示例中的 **192.168.2.163**、`20172` 为占位符，须替换为实际的值。

### 为 Firefox 单独配置代理

Firefox 浏览器的设置页面中，网络设置选项卡提供了图形化代理配置模块。

![Firefox 代理设置](../.gitbook/assets/firefox-proxy.png)

### 参考文献

- Owynn, graudeejs, rjohn, olli@, Sevendogsbsd, kpedersen. chromium proxy settings page doesn't exist[EB/OL]. [2026-03-25]. <https://forums.freebsd.org/threads/chromium-proxy-settings-page-doesnt-exist.31927/>. 提供了 FreeBSD 下 Chromium 代理配置的实践解决方案。

## 课后习题

1. 修改 Chromium 的 desktop 文件，使其默认使用 SOCKS5 代理启动，验证其 DNS 查询是否通过代理转发，分析 `--proxy-server` 参数对 DNS 解析路径的影响。
2. 为 csh 和 sh 分别编写代理开关脚本，设置代理后使用 `tcpdump` 验证 git、fetch 等命令的实际网络流量路径，分析不同 shell 对环境变量大小写约定的差异及其规范来源。
3. 为 Firefox 编写一个 shell 脚本，通过修改其 `prefs.js` 配置文件实现代理自动切换，对比 Firefox 配置文件方式与 Chromium 命令行参数方式在用户可控性上的差异。
