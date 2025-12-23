# 9.1 音频设备配置

>**警告**
>
>KDE 6 Ports 默认通过 PulseAudio 在全局占用音频，请勿手动切换到其他音频后端（如 PipeWire），以免造成不必要的问题。

## 声音设置

声卡驱动 `snd_hda` 通常会默认加载；当默认内核未包含该驱动时，需要手动加载对应的内核模块。


用以下命令查看当前声卡设备：

```sh
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

后面标注为 `default` 的设备是 OSS 的默认音频设备。如果软件使用 OSS 作为音频输出接口且输出设备设置为默认值，音频就会从该设备输出。

可以通过调整内核参数，使上面命令输出更为详细的声卡信息：

```sh
# sysctl hw.snd.verbose=4  #  设置 FreeBSD 声卡驱动调试输出等级为 4
```

FreeBSD 中大部分软件的音频输出接口为 OSS。有些软件默认使用 PulseAudio（如 Firefox），这些软件的相关设置请参见后文提示。Firefox 可以通过 `about:support` 页面查看当前使用的音频后端。Firefox 支持多种音频后端，可根据系统中已安装的后端按优先顺序自动选择，也可以手动指定。

下列命令可以设置默认声卡设备单元号为 5。最后的数字是对应 pcm 后面的数字。

```sh
# sysctl hw.snd.default_unit=5
```

上文中的 `pcm6: <Realtek ALC892 (Rear Digital)> (play)` 为数字输出接口。一般集成声卡的模拟接口采样率最高 48kHz，数字接口最高采样率可以达到 192kHz。如果存在数字输出，但机箱面板上没有对应接口，而主板上提供了 S/PDIF 接口插针，可以安装一块 S/PDIF 挡板（通常包含 S/PDIF 光纤口和同轴口，价格较低），连接后即可使用。


## man 示例

以下节选自 [man snd_hda](https://man.freebsd.org/cgi/man.cgi?snd_hda)。

以下示例均需要将相关配置行写入 `/boot/device.hints` 文件中。

>**注意**
>
>`cad0` 应以 `cat /dev/sndstat` 实际输出为准。

### 示例 1

```ini
hint.hdac.0.cad0.nid20.config="as=1"   # 配置声卡节点 20 的音频流为通道 1
hint.hdac.0.cad0.nid21.config="as=2"   # 配置声卡节点 21 的音频流为通道 2
```

这样会交换 Line-out（线路输出）接口与扬声器的功能。因此 **pcm0** 设备会将声音输出到线路输出和耳机插孔。当耳机插入时，线路输出会自动静音。

- **pcm0** 的录音输入来自两个外置麦克风和线路输入插孔。
- **pcm1** 的播放则会输出到内置扬声器。

### 示例 2

```ini
hint.hdac.0.cad0.nid20.config="as=1 seq=15 device=Headphones"   # 配置声卡节点 20 的音频流为通道 1，序列号 15，输出设备为耳机
hint.hdac.0.cad0.nid27.config="as=2 seq=0"                       # 配置声卡节点 27 的音频流为通道 2，序列号 0
hint.hdac.0.cad0.nid25.config="as=4 seq=0"                       # 配置声卡节点 25 的音频流为通道 4，序列号 0
```

这样会将耳机和其中一个麦克风分离到独立的设备。

- **pcm0** 会将声音播放到内置扬声器和线路输出插孔，并且在耳机插入时自动静音扬声器。
- **pcm0** 的录音输入来自一个外部麦克风和线路输入插孔。
- **pcm1** 设备则完全用于前面板的耳机（耳机 + 麦克风）。


### 示例 3

```ini
hint.hdac.0.cad0.nid20.config="as=1 seq=0"                 # 配置声卡节点 20 的音频流为通道 1，序列号 0
hint.hdac.0.cad0.nid26.config="as=2 seq=0"                 # 配置声卡节点 26 的音频流为通道 2，序列号 0
hint.hdac.0.cad0.nid27.config="as=3 seq=0"                 # 配置声卡节点 27 的音频流为通道 3，序列号 0
hint.hdac.0.cad0.nid25.config="as=4 seq=0"                 # 配置声卡节点 25 的音频流为通道 4，序列号 0
hint.hdac.0.cad0.nid24.config="as=5 seq=0 device=Line-out" # 配置声卡节点 24 的音频流为通道 5，序列号 0，输出设备为 Line-out
hint.hdac.0.cad0.nid21.config="as=6 seq=0"                 # 配置声卡节点 21 的音频流为通道 6，序列号 0
```

这样会得到 4 个独立设备：

- **pcm0**（线路输出和线路输入）
- **pcm1**（耳机和麦克风）
- **pcm2**（通过重新定义后置麦克风插孔作为额外线路输出）
- **pcm3**（内置扬声器）


### 示例 4


```ini
hint.hdac.0.cad0.nid20.config="as=1 seq=0"                 # 配置声卡节点 20 的音频流为通道 1，序列号 0
hint.hdac.0.cad0.nid24.config="as=1 seq=1 device=Line-out" # 配置声卡节点 24 的音频流为通道 1，序列号 1，输出设备为 Line-out
hint.hdac.0.cad0.nid26.config="as=1 seq=2 device=Line-out" # 配置声卡节点 26 的音频流为通道 1，序列号 2，输出设备为 Line-out
hint.hdac.0.cad0.nid21.config="as=2 seq=0"                 # 配置声卡节点 21 的音频流为通道 2，序列号 0
```

这样会得到 2 个设备：

- **pcm0**：用于 5.1 声道播放，通过 3 个后置接口（线路输出 + 重新定义的麦克风和线路输入），以及前面板的耳机（耳机 + 麦克风）。
- **pcm1**：用于内置扬声器播放。

当耳机插入时，后置接口会自动静音。


## 实例

```sh
# cat /dev/sndstat # 省略无用信息
pcm1: <Realtek ALC897 (Rear Analog Line-in)> at nid 26 on hdaa0
pcm0: <Realtek ALC897 (Analog)> at nid 27 and 26 on hdaa0
```

该设备并非 AUX 接口（即非扬声器与麦克风的二合一接口），当前仅插入了一台音响。在默认配置下，该设备不会输出声音。

可以通过以下命令实时调试音频配置（命令立即生效，但在系统重启后失效）：

```sh
# sysctl dev.hdaa.0.nid26_config="as=1 seq=0"   # 设置 HDA 声卡节点 26 的音频流为通道 1，序列号 0
# sysctl dev.hdaa.0.nid27_config="as=1 seq=15"  # 设置 HDA 声卡节点 27 的音频流为通道 1，序列号 15
```

- `as=1`：将两者放到同一个关联里。
- `seq=0`：主输出（扬声器）。
- `seq=15`：耳机，插入耳机时会自动静音扬声器。

此时发现已经有声音了，编辑 `/boot/device.hints` 文件，加入以下若干行，将其固化为永久设置：

```ini
hint.hdaa.0.nid26.config="as=1 seq=0"    # 配置 HDA 声卡节点 26 的音频流为通道 1，序列号 0
hint.hdaa.0.nid27.config="as=1 seq=15"   # 配置 HDA 声卡节点 27 的音频流为通道 1，序列号 15
```

## oss mixer

| GUI 环境 |      名称       |
| :------: | :-------------: |
|   kde5   | audio/dsbmixer  |
|   gtk    | audio/gtk-mixer |
| 非图形化 | audio/mixertui  |

## 故障排除与未竟事项

部分声卡需要自行编译内核，请参考 [Open Sound System for FreeBSD](http://www.opensound.com/freebsd.html)。

但是 OSS 存在一定的限制，例如在使用 `obs-studio` 时无法录制 OSS 的输出音频。根据官方论坛的说明，可以使用 `virtual_oss` 模拟一个音频设备实现该功能（通过 `virtual_oss` 的 `-M` 参数进行声道路由，即将 OSS 输出重定向到 OSS 输入）。

但是 `obs-studio` 可以录制 PulseAudio 的输出音频（默认的“桌面音频”输入源实际对应的是 PulseAudio 输出，因此无法录制 OSS 的输出音频）。因此，有些软件可以配置为使用 PulseAudio 作为音频输出接口。使用 PulseAudio 的软件的音频输出，不受上面的命令控制音频输出设备。PulseAudio 会根据自己的设置将音频送到对应设备，所以需要使用 PulseAudio 混音器控制。

在 KDE 5 环境中，自带的音频控制器在切换设备时，实际上是在控制 PulseAudio 的配置。

官方打包的部分多媒体软件支持 PulseAudio，但其中大多数软件默认未启用对应的编译选项。如果需要录制软件的音频输出，可以在 Ports 中启用相应的编译选项并自行编译。在软件中设置 PulseAudio 作为音频驱动输出就可以了。

## AMD CPU mode 2 reset

已知在 APU 上使用 drm-kmod 时，打开空播放器窗口可能会触发 mode 2 reset 报错（即 driver reset），进而导致 Kernel Panic。

请避免打开未加载任何媒体内容的播放器窗口或音频播放器窗口。

音频文件应通过终端中的命令行方式进行播放。

由于样本数量不足，目前尚未提交相关 Bug 报告。
