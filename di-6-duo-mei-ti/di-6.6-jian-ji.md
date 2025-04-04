# 第 6.6 节 音频图形图像处理

## 音频剪辑

- Audacity :

安装：

```sh
# pkg install audacity
```

或者

```sh
# cd /usr/ports/audio/audacity/ 
# make install clean
```


## 视频剪辑

- Olive 视频编辑器：

安装：

```sh
# pkg install olive-video-editor
```

或者：

```sh
# cd /usr/ports/multimedia/olive/ 
# make install clean
```


## 压缩字幕

- ffmpeg :

```
# pkg install ffmpeg
```

或者：

```sh
# cd /usr/ports/multimedia/ffmpeg/ 
# make install clean
```

处理：

```sh
$ ffmpeg -i 视频文件.mp4 -vf subtitles=对应字幕.ass 输出视频.mp4
```

## 扣图

Unix 系统下相关软件有很多，这里我们简单介绍一下矢量制图程序 **Inkscape** 的使用方法

### 安装 inkscape

- 使用 pkg 安装：

```sh
# pkg install inkscape
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/graphics/inkscape/ 
# make install clean
```

### inkscape 用法

1. `Ctrl O`（字母 `o`）打开图片
2. 点击图片
3. `Alt i` 改为矢量模式
4. `Shift F6` 贝塞尔和直线模式
5. `Ctrl A` 全选
6. 选择 **路径** --> **交集**，实现扣图

### 参考文献

- Inscape [官方教程](https://inkscape.org/zh-hans/learn/tutorials/)


