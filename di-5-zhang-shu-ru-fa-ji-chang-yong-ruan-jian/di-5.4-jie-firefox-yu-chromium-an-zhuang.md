# 第 5.4 节 Firefox 与 Chromium 安装

## 火狐浏览器

### 安装普通版本（更新频繁）：

```shell-session
# pkg install firefox
```

或者

```shell-session
# cd /usr/ports/www/firefox
# make install clean
```

### 安装长期支持版本：

```shell-session
pkg install firefox-esr
```

或者

```shell-session
#cd /usr/ports/www/firefox-esr/ && make install clean
```

## Chromium（Chromium 不是 chrome，但是启动命令是 chrome）

```shell-session
# pkg install chromium 
```

或者

```shell-session
# cd /usr/ports/www/chromium
# make install clean
```

- Chromium 加入 Google 同步

 [Launch Chromium with API Keys on Mac OS X and Windows ](https://gist.github.com/cvan/44a6d60457b20133191bd7b104f9dcc4)

 - Chromium配置`HTTP`代理
  
chromium本身并没有在例如~/.config下的配置文件这种东西。亦没有可添加环境变量参数用于指定默认代理服务器。不过可以添加启动参数(Options)。

如： 

```  
--proxy-server="<IP地址>:<端口>"
```

例：

```
chrome --proxy-server="127.0.0.1:1234" (终端启动)
```
默认是http协议，如果你的代理程序使用sock:


```
--proxy-server="socks://<IP地址>:<端口>"
```
socksv4: 

```
--proxy-server="socksv4://<IP地址>:<端口>"
```

- 在图形界面下让chromium默认使用代理打开：

找到你的桌面环境为chromium创建的desktop文件，
一般在 `/usr/home/{你的用户名}/.local/share/applications/`这个位置。

```
vim/ee chromium-browser.desktop # 使用你喜欢的编辑器打开上述目录下的chromium desktop文件
```
找到 Exec=chrome %U 这行 在其后加入上列你需要的参数。
```
Comment[zh_CN]=Google web browser based on WebKit
Comment=Google web browser based on WebKit
Encoding=UTF-8
Exec=chrome %U 
GenericName[zh_CN]=
......
```

例:
```
Exec=chrome %U --proxy-server="192.168.2.163:20172"
```
#### 单独为Firefox配置代理
  
因Firefox在windows GNU/linux Macos以及bsd的所有客户端的浏览器设置页面>网络设置选项卡中均有gui配置代理的模块，故此节不再赘述。

<img decoding="async" src="https://i.mij.rip/2023/10/10/bffb29adb2fd30f0d3b7a008ac820a27.png" width="70%">

## 参考资料

- [FreeBSD Manual Pages: Chromium](https://man.freebsd.org/cgi/man.cgi?query=chrome&apropos=0&sektion=0&manpath=FreeBSD+13.2-RELEASE+and+Ports&arch=default&format=html)
- [FreeBSD Forums: chromium proxy settings page doesn't exist](https://forums.freebsd.org/threads/chromium-proxy-settings-page-doesnt-exist.31927/)
