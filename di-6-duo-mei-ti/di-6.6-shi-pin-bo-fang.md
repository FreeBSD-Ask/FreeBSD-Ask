# 第 6.6 节 视频播放器

## VLC

### 安装 VLC

- 使用 pkg 安装：
  
```sh
# pkg install vlc
```

- 或者使用 Ports：

```sh
# cd /usr/ports/multimedia/vlc/ 
# make install clean
```

### VLC 视频播放测试

视频 A、B 均正常

![](../.gitbook/assets/vlc1.png)

![](../.gitbook/assets/vlc2.png)

## SMPlayer

SMPlayer 是 MPlayer（纯命令行）的 QT 前端。推荐使用。

### 安装 SMPlayer

- 使用 pkg 安装：

```sh
# pkg install smplayer
```

- 或者使用 Ports：

```sh
# cd /usr/ports/multimedia/smplayer/ 
# make install clean
```

### SMPlayer 视频播放测试

视频 A、B 均正常

![SMPlayers](../.gitbook/assets/smplayer1.png)

![SMPlayer](../.gitbook/assets/smplayer2.png)

![SMPlayer](../.gitbook/assets/smplayer3.png)

## Kodi

Kodi 曾用名为 XBMC。

### 安装 Kodi

- 使用 pkg 安装：
  
```
# pkg install kodi
```

- 或者使用 Ports：
  
```sh
# cd /usr/ports/multimedia/kodi/ 
# make install clean
```

### Kodi 设置中文

打开 `interface`（界面）

![](../.gitbook/assets/kodi1.png)

点击 `Skin`（皮肤）。再点击左下角，把 `basic`（简单）改为 `expert`（专家）或 `Standard`（标准），否则你看不到 `fonts` 等选项！然后将 `fonts`（字体）改为 `Arial based`，否则中文会乱码！

![](../.gitbook/assets/kodi3.png)

返回，选择 `Regional`（区域）——> `Language`（语言）——> `Chinese (Simple)`（简体中文）。

![](../.gitbook/assets/kodi2.png)

中文设置完毕：

![](../.gitbook/assets/kodi5.png)

### Kodi 播放视频测试

视频 A、B 均正常

![](../.gitbook/assets/kodi4.png)

