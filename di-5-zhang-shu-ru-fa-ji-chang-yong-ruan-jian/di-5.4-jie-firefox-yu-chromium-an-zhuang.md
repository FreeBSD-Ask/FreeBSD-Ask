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

 [Chromium Sync](https://www.learningtopi.com/sbc/chromium-sync/)

- 解决 chromium 出现未知错误时占用大量性能（加到图标的启动参数中）

```shell-session
chrome --disk-cache-size=0 --disable-gpu
```
