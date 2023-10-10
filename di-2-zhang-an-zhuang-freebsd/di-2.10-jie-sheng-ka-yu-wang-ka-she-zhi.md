# 第 2.10 节 声卡与网卡设置

## FreeBSD 声卡

### 声音设置

声卡驱动 snd_hda 默认即加载。默认内核没有包含时要手动加载对应内核模块。

用以下命令查看当前声卡设备：

```shell-session
$ cat /dev/sndstat
Installed devices:
pcm0: <NVIDIA (0x0083) (HDMI/DP 8ch)> (play)
pcm1: <NVIDIA (0x0083) (HDMI/DP 8ch)> (play)
pcm2: <NVIDIA (0x0083) (HDMI/DP 8ch)> (play)
pcm3: <NVIDIA (0x0083) (HDMI/DP 8ch)> (play)
pcm4: <Realtek ALC892 (Rear Analog 5.1/2.0)> (play/rec) default
pcm5: <Realtek ALC892 (Front Analog)> (play/rec)
pcm6: <Realtek ALC892 (Rear Digital)> (play)
No devices installed from userspace.
```

后面带有 default 是 oss 默认设备。如果软件的音频使用的 oss 且输出是默认的，音频就会从这个设备输出。

FreeBSD 大部分软件的音频输出驱动为 oss。有些默认是 pulseaudio(比如 firefox)，这些软件的设置看最后的提示。

下列命令可以修改输出的设备。最后的数字是对应的 pcm 后面的数字。

```shell-session
$ sysctl hw.snd.default_unit=5
```

此处推荐几个 oss mixer：

| GUI 环境 |      名称       |
| :------: | :-------------: |
|   kde5   | audio/dsbmixer  |
|   gtk    | audio/gtk-mixer |
| 非图形化 | audio/mixertui  |

### 提示

部分声卡需要自行编译内核，请参考 [Open Sound System for FreeBSD](http://www.opensound.com/freebsd.html)。

但是 oss 有些缺点，使用 `obs-studio` 无法录制 oss 输出。只能录制 oss 输入。看官方论坛里，可以 `virtual_oss` 模拟一个设备实现。

但是 `obs-studio` 可以录制 pulseaudio 输出的音频。

所以有些软件可以使用 pulseaudio 作为输出。使用 pulseaudio 的软件的音频输出，不受上面的命令控制音频输出设备。pulseaudio 会根据自己的设置把音频送到对应设备，所以需要使用 pulseaudio 混音器控制。

在 kde5 下面自带的音频控制器，切换设备就是控制的 pulseaudio。

官方打包好的多媒体软件有些是支持 pulseaudio 但是这些软件中的大部分对应的编译选项没有打开。如果需要录制软件的音频输出，可以自行打开 ports 的编译选项自己编译。在软件中设置 pulseaudio 作为音频驱动输出就可以了。

