# 9.6 视频播放器

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

视频 A 和 B 均能正常播放。

![](../.gitbook/assets/vlc1.png)

![](../.gitbook/assets/vlc2.png)

## SMPlayer

SMPlayer 是 MPlayer（纯命令行播放器）的 Qt 前端，推荐使用。

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

![SMPlayer](../.gitbook/assets/smplayer1.png)

![SMPlayer](../.gitbook/assets/smplayer2.png)

![SMPlayer](../.gitbook/assets/smplayer3.png)

## Kodi

Kodi 曾用名为 XBMC。

### 安装 Kodi

- 使用 pkg 安装：
  
```sh
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

点击 `Skin`（皮肤），然后点击左下角，将 `Basic`（简单）改为 `Expert`（专家）或 `Standard`（标准），否则无法看到 `Fonts`（字体）等选项。随后将 `Fonts`（字体）改为 `Arial based`，否则中文可能出现乱码。

![](../.gitbook/assets/kodi3.png)

返回后，依次选择 `Regional`（区域）→ `Language`（语言）→ `Chinese (Simplified)`（简体中文）。

![](../.gitbook/assets/kodi2.png)

中文设置完毕：

![](../.gitbook/assets/kodi5.png)

### Kodi 播放视频测试

视频 A 和 B 均能正常播放

![](../.gitbook/assets/kodi4.png)

## 附录：直接在 TTY 播放视频（mpv）

可以直接在 TTY 中使用 mpv 命令播放视频。

- 使用 pkg 安装：

```sh
# pkg ins mpv
```

- 还可以通过 Ports 安装：

```sh
# cd /usr/ports/multimedia/mpv/ 
# make install clean
```

切换到 TTY，使用 MPV 播放器播放视频文件 `1.mp4`：

```sh
$ mpv 1.mp4
```

请读者自行尝试操作。

>**注意**
>
>此功能依赖 DRM，虚拟机环境可能无法正常使用。

## 附录：音量调节

可以使用命令行工具 `mixer` 调整音量。

例如以下命令可将音量提高 5%：

```sh
$ mixer vol=+5%  # 将音量增加 5%
```
