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

 