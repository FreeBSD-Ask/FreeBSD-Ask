# 第三节 音视频剪辑

## 音频剪辑

- Audacity : `# pkg install audacity`

## 视频剪辑

### 扣图

Unix 系统下相关软件有很多，这里我们简单介绍一下矢量制图程序 **Inkscape** 的使用方法

- [ ] 安装方式： `# pkg install inkscape`

1. `Ctrl  O（拉丁字母）` 打开图片
2. 点击图片
3. `Alt  i` 改为矢量模式
4. `Shift  F6` 贝塞尔和直线模式
5. `Ctrl  A` 全选
6. 选择 **路径** --> **交集**，实现扣图

想了解更多，可查阅 Inscape [官方教程](https://inkscape.org/zh-hans/learn/tutorials/)


### 剪辑

- Olive 视频编辑器：`# pkg install olive-video-editor`

## 编辑字幕

- Aegisub：`# pkg install aegisub`

## 压缩字幕

- ffmpeg : `# pkg install ffmpeg`

`$ ffmpeg -i 视频文件.mp4 -vf subtitles=对应字幕.ass 输出视频.mp4`
