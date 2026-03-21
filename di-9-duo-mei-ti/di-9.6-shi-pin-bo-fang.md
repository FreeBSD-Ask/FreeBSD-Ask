# 9.6 视频播放器

FreeBSD 操作系统提供了多种视频播放器选择，本节将介绍几款常用视频播放器的安装配置和使用方法。

## VLC

### 安装 VLC

- 使用 pkg 二进制包管理器安装：
  
```sh
# pkg install vlc
```

- 或者使用 Ports 源码编译安装：

```sh
# cd /usr/ports/multimedia/vlc/ 
# make install clean
```

### VLC 视频播放测试

经实际测试，视频 A 和 B 均能在 VLC 播放器中正常播放。

![](../.gitbook/assets/vlc1.png)

![](../.gitbook/assets/vlc2.png)

## SMPlayer

SMPlayer 是 MPlayer（一款功能强大的纯命令行视频播放器）的 Qt 图形前端，在用户友好性和功能丰富度方面表现优秀，推荐使用。

### 安装 SMPlayer

- 使用 pkg 二进制包管理器安装：

```sh
# pkg install smplayer
```

- 或者使用 Ports 源码编译安装：

```sh
# cd /usr/ports/multimedia/smplayer/ 
# make install clean
```

### SMPlayer 视频播放测试

经实际测试，视频 A、B 均能在 SMPlayer 播放器中正常播放。

![SMPlayer](../.gitbook/assets/smplayer1.png)

![SMPlayer](../.gitbook/assets/smplayer2.png)

![SMPlayer](../.gitbook/assets/smplayer3.png)

## Kodi

Kodi 是一款知名的开源媒体中心软件，其曾用名为 XBMC（Xbox Media Center）。

### 安装 Kodi

- 使用 pkg 二进制包管理器安装：
  
```sh
# pkg install kodi
```

- 或者使用 Ports 源码编译安装：
  
```sh
# cd /usr/ports/multimedia/kodi/ 
# make install clean
```

### Kodi 设置中文

首先打开 Kodi 主界面中的 `interface`（界面）设置选项：

![](../.gitbook/assets/kodi1.png)

点击 `Skin`（皮肤）选项，然后点击界面左下角的设置级别按钮，将当前的 `Basic`（简单）级别改为 `Expert`（专家）或 `Standard`（标准）级别，否则无法看到 `Fonts`（字体）等高级设置选项。随后将 `Fonts`（字体）设置为 `Arial based`，否则中文可能出现乱码显示问题。

![](../.gitbook/assets/kodi3.png)

返回上一级菜单后，依次选择 `Regional`（区域）→ `Language`（语言）→ `Chinese (Simplified)`（简体中文）选项以完成语言切换。

![](../.gitbook/assets/kodi2.png)

中文界面设置完成后的效果如下：

![](../.gitbook/assets/kodi5.png)

### Kodi 播放视频测试

经实际测试，视频 A 和 B 均能在 Kodi 媒体中心中正常播放。

![](../.gitbook/assets/kodi4.png)

## 附录：直接在 TTY 播放视频（mpv）

可以直接在 Linux/FreeBSD 的 TTY（Teletypewriter，电传打字机，即纯文本终端）环境中使用 mpv 命令播放视频文件。

- 使用 pkg 二进制包管理器安装：

```sh
# pkg install mpv
```

- 还可以通过 Ports 源码编译安装：

```sh
# cd /usr/ports/multimedia/mpv/ 
# make install clean
```

切换到 TTY 终端环境后，使用 MPV 播放器播放视频文件 `1.mp4`：

```sh
$ mpv 1.mp4
```

请读者自行尝试上述操作步骤。

>**注意**
>
>此功能依赖 DRM（Direct Rendering Manager，直接渲染管理器）图形子系统，在虚拟机环境中可能无法正常使用。

## 附录：音量调节

可以使用系统自带的命令行工具 `mixer` 调整系统音量。

例如以下命令可将系统音量提高 5%：

```sh
$ mixer vol=+5%  # 将音量增加 5%
```
