# 9.7 多媒体处理工具

FreeBSD 支持多种多媒体处理工具，本节将介绍音频剪辑、视频剪辑、字幕压制以及图形图像处理等相关工具的使用方法。

## 音频剪辑

音频剪辑是多媒体处理中的常见需求，Audacity 是一款功能强大的开源音频编辑软件。

- Audacity：

使用 pkg 安装：

```sh
# pkg install audacity
```

或者使用 Ports 安装：

```sh
# cd /usr/ports/audio/audacity/ 
# make install clean
```

## 视频剪辑

视频剪辑是处理视频内容的重要环节，Olive 视频编辑器是一款开源的非线性视频编辑软件。

Olive 视频编辑器（Olive Video Editor）：

使用 pkg 安装：

```sh
# pkg install olive-video-editor
```

或者使用 Ports 安装：

```sh
# cd /usr/ports/multimedia/olive/ 
# make install clean
```

## 压制字幕

将字幕压制到视频中是常见的多媒体处理需求，FFmpeg 是一款功能强大的多媒体处理工具，可以完成此项任务。

FFmpeg：

使用 pkg 安装：

```sh
# pkg install ffmpeg
```

或者使用 Ports 安装：

```sh
# cd /usr/ports/multimedia/ffmpeg/ 
# make install clean
```

使用 FFmpeg 将 ASS 字幕压制到视频中：

```sh
$ ffmpeg -i 视频文件.mp4 -vf subtitles=对应字幕.ass 输出视频.mp4
```

## 抠图

抠图是图形图像处理中的常用操作，在 Unix 系统下可用的相关软件较多，这里简要介绍矢量制图程序 **Inkscape** 的使用方法。

### 安装 Inkscape

- 使用 pkg 安装：

```sh
# pkg install inkscape
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/graphics/inkscape/ 
# make install clean
```

### Inkscape 用法

1. `Ctrl O`（字母 `o`）打开图片
2. 点击图片
3. 按 `Alt I` 切换到矢量模式
4. `Shift F6` 贝塞尔和直线模式
5. `Ctrl A` 全选
6. 在菜单中选择 **路径** → **交集**，以实现抠图

### 参考文献

- Inkscape [官方教程](https://inkscape.org/zh-hans/learn/tutorials/) [备份](https://web.archive.org/web/20260121063653/https://inkscape.org/zh-hans/learn/tutorials/)
