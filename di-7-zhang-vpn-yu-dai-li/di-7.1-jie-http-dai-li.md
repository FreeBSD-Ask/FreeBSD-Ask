# 第 7.1 节 HTTP 代理

示例：V2ray 或 clash 开启允许局域网连接。然后按照具体配置可能如下：

首先查看使用的 shell
```shell-session
$ echo $SHELL
```

>**注意**
>
>**本文中的 `192.168.X.X:7890` 均非实际参数，以实际为准，复制粘贴是不会生效的！**

## HTTP_PROXY 代理

- 如果使用的是 `sh`, `bash`, `zsh`
  
**环境变量 HTTP_PROXY 一定要是大写！小写不生效！**
  
设置：
```shell-session
# export HTTP_PROXY=http://192.168.X.X:7890
```

取消：
```shell-session
# unset HTTP_PROXY
```


- 如果使用的是 `csh`

设置：
```shell-session
# setenv http_proxy http://192.168.X.X:7890
```

取消：
```shell-session
# unsetenv http_proxy
```
## Git 代理

- 如果使用的是 `sh`, `bash`, `zsh`：

设置：
```shell-session
# git config --global http.proxy http://192.168.X.X:7890
# git config --global https.proxy http://192.168.X.X:7890
```
取消：

```shell-session
# git config --global --unset http.proxy
# git config --global --unset https.proxy
```

## 浏览器配置代理

chromium 本身并没有在例如 `~/.config` 下的配置文件这种东西。亦没有可添加环境变量参数用于指定默认代理服务器。不过可以添加启动参数（Options）。

如：

```shell-session
--proxy-server="<IP地址>:<端口>"
```

例：

```shell-session
$ chrome --proxy-server="127.0.0.1:1234" (终端启动)
```

默认是 http 协议，如果你的代理程序使用 sock:

```shell-session
--proxy-server="socks://<IP地址>:<端口>"
```

socksv4:

```shell-session
--proxy-server="socksv4://<IP地址>:<端口>"
```

- 在图形界面下让 chromium 默认使用代理打开：

找到你的桌面环境为 chromium 创建的 desktop 文件，一般在 `~/.local/share/applications/` 这个位置。

```shell-session
$ ee chromium-browser.desktop # 使用你喜欢的编辑器打开上述目录下的 chromium desktop 文件
```

找到 `Exec=chrome %U` 这行 在其后加入上列你需要的参数。

```shell-session
Comment[zh_CN]=Google web browser based on WebKit
Comment=Google web browser based on WebKit
Encoding=UTF-8
Exec=chrome %U
GenericName[zh_CN]=
......
```

例:

```shell-session
Exec=chrome %U --proxy-server="192.168.2.163:20172"
```

### 单独为 Firefox 配置代理

因 Firefox 在 Windows GNU/linux Macos 以及 BSD 的所有客户端的浏览器设置页面>网络设置选项卡中均有 GUI 配置代理的模块，故此节不再赘述。

![FF-Porxy](../.gitbook/assets/FF-Proxy.png)

### 参考资料

- [FreeBSD Manual Pages: Chromium](https://man.freebsd.org/cgi/man.cgi?query=chrome&apropos=0&sektion=0&manpath=FreeBSD+13.2-RELEASE+and+Ports&arch=default&format=html)
- [FreeBSD Forums: chromium proxy settings page doesn't exist](https://forums.freebsd.org/threads/chromium-proxy-settings-page-doesnt-exist.31927/)
