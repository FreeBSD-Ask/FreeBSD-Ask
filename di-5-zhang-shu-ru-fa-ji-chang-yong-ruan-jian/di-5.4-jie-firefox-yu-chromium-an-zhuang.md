# 第 5.4 节 安装 Firefox 与 Chromium 

## 火狐浏览器

### 安装普通版本（更新频繁）

```sh
# pkg install firefox
```

或者

```sh
# cd /usr/ports/www/firefox
# make install clean
```

### 安装长期支持版本

```sh
pkg install firefox-esr
```

或者

```sh
#cd /usr/ports/www/firefox-esr/
# make install clean
```

## Chromium

Chromium 不是 chrome，但在 FreeBSD 中启动命令是 `chrome`。

```sh
# pkg install chromium 
```

或者

```sh
# cd /usr/ports/www/chromium
# make install clean
```

>**警告**
>
>要编译 Chromium，你必须拥有至少 12G 内存，或等量的交换分区 + 内存。

### 故障排除

- Chromium 加入 Google 同步

 [Chromium Sync](https://www.learningtopi.com/sbc/chromium-sync/)

- 解决 chromium 出现未知错误时占用大量性能（加到图标的启动参数中，图标是文本文件）

```sh
chrome --disk-cache-size=0 --disable-gpu
```
