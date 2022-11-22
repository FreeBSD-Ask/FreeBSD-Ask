# 第5.4节 Firefox 与 Chromium 安装

## 火狐浏览器

### 安装普通版本（更新频繁）：

```
# pkg install firefox
```

或者

```
# cd /usr/ports/www/firefox
# make install clean 
```

### 安装长期支持版本：

```
pkg install firefox-esr
```

或者

```
#cd /usr/ports/www/firefox-esr/ && make install clean
```

## Chromium（Chromium 不是 chrome，但是启动命令是 chrome）

```
# pkg install chromium
```

或者

```
# cd /usr/ports/www/chromium
# make install clean
```
