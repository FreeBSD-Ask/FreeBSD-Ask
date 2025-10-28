# 9.1 音频设备配置

>**警告**
>
>Port KDE 6 默认通过 PulseAudio 在全局占用音频，请勿手动切换到其他音频后端（如 PipeWire），以免造成不必要的麻烦。

## 声音设置

声卡驱动 `snd_hda` 可默认加载，当默认内核未包含时需手动加载对应内核模块。

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

后面带有 `default` 是 oss 默认设备。如果软件的音频使用的 oss 且输出是默认的，音频就会从这个设备输出。

可以通过调整内核参数，使上面命令输出更为详细的声卡信息：

```sh
# sysctl hw.snd.verbose=4
```

FreeBSD 大部分软件的音频输出驱动为 oss。有些默认是 pulseaudio（如 firefox），这些软件的设置看最后的提示。firefox 可以通过 `about:support` 页查看使用的音频后端。firefox 支持各种音频后端，能根据系统安装的后端自动按顺序选择，亦可手动选择。

下列命令可以修改输出的设备。最后的数字是对应 pcm 后面的数字。

```sh
# sysctl hw.snd.default_unit=5
```

上面 pcm6（“pcm6: <Realtek ALC892 (Rear Digital)> (play)”）是数字输出接口。一般集成声卡的模拟接口采样率最高 48kHz，数字接口最高采样率可以达到 192kHz。如果有数字输出，但面板上没有接口，而主板上有 S/PDIF 接口的插针，加个 S/PDIF 的挡板（十分便宜，一般是 S/PDIF 口和同轴口，两个输出口），接上线即可使用。


## man 示例

以下节选自 [man snd_hda](https://man.freebsd.org/cgi/man.cgi?snd_hda)。

均将相关行写入 `/boot/device.hints`。

>**注意**
>
>`cad0` 应以 `cat /dev/sndstat` 实际输出为准。

### 示例 1

```ini
hint.hdac.0.cad0.nid20.config="as=1"
hint.hdac.0.cad0.nid21.config="as=2"
```

这会交换 line-out（线路输出）和扬声器的功能。因此 **pcm0** 设备会把声音输出到线路输出和耳机插孔。当耳机插入时，线路输出会自动静音。

- **pcm0** 的录音输入来自两个外置麦克风和线路输入插孔。
- **pcm1** 的播放则会输出到内置扬声器。

### 示例 2

```ini
hint.hdac.0.cad0.nid20.config="as=1 seq=15 device=Headphones"
hint.hdac.0.cad0.nid27.config="as=2 seq=0"
hint.hdac.0.cad0.nid25.config="as=4 seq=0"
```

这样会把耳机和其中一个麦克风分离到独立的设备。

- **pcm0** 会把声音播放到内置扬声器和线路输出插孔，并且在耳机插入时自动静音扬声器。
- **pcm0** 的录音输入来自一个外部麦克风和线路输入插孔。
- **pcm1** 设备则完全用于前面板的耳机（耳机 + 麦克风）。


### 示例 3

```ini
hint.hdac.0.cad0.nid20.config="as=1 seq=0"
hint.hdac.0.cad0.nid26.config="as=2 seq=0"
hint.hdac.0.cad0.nid27.config="as=3 seq=0"
hint.hdac.0.cad0.nid25.config="as=4 seq=0"
hint.hdac.0.cad0.nid24.config="as=5 seq=0 device=Line-out"
hint.hdac.0.cad0.nid21.config="as=6 seq=0"
```

这样会得到 4 个独立设备：

* **pcm0**（线路输出和线路输入）
* **pcm1**（耳机和麦克风）
* **pcm2**（通过重新定义后置麦克风插孔作为额外线路输出）
* **pcm3**（内置扬声器）


### 示例 4


```ini
hint.hdac.0.cad0.nid20.config="as=1 seq=0"
hint.hdac.0.cad0.nid24.config="as=1 seq=1 device=Line-out"
hint.hdac.0.cad0.nid26.config="as=1 seq=2 device=Line-out"
hint.hdac.0.cad0.nid21.config="as=2 seq=0"
```

这样会得到 2 个设备：

* **pcm0**：用于 5.1 声道播放，通过 3 个后置接口（线路输出 + 重新定义的麦克风和线路输入），以及前面板的耳机（耳机 + 麦克风）。
* **pcm1**：用于内置扬声器播放。

当耳机插入时，后置接口会自动静音。


## 实例

```sh
# cat /dev/sndstat # 省略无用信息
pcm1: <Realtek ALC897 (Rear Analog Line-in)> at nid 26 on hdaa0
pcm0: <Realtek ALC897 (Analog)> at nid 27 and 26 on hdaa0
```

此设备不是 AUX 口（不是扬声器 + 麦克风二合一）。当前仅插入了一台音响。在默认情况下无声音。


可通过命令实时调试音频（均立刻生效，但重启失效）：

```sh
# sysctl dev.hdaa.0.nid26_config="as=1 seq=0"
# sysctl dev.hdaa.0.nid27_config="as=1 seq=15"
```

- `as=1`：把两者放到同一个关联里。
- `seq=0`：主输出（扬声器）。
- `seq=15`：耳机，插入耳机时会自动静音扬声器。

此时发现已经有声音了，编辑 `/boot/device.hints`，加入以下若干行，将其固化为永久设置：

```ini
hint.hdaa.0.nid26.config="as=1 seq=0"
hint.hdaa.0.nid27.config="as=1 seq=15"
```

## oss mixer

| GUI 环境 |      名称       |
| :------: | :-------------: |
|   kde5   | audio/dsbmixer  |
|   gtk    | audio/gtk-mixer |
| 非图形化 | audio/mixertui  |

## 故障排除与未竟事项

部分声卡需要自行编译内核，请参考 [Open Sound System for FreeBSD](http://www.opensound.com/freebsd.html)。

但是 oss 有些缺点，使用 `obs-studio` 无法录制 oss 输出。只能录制 oss 输入。看官方论坛里，可以用 `virtual_oss` 模拟一个设备实现（使用 `virtual_oss` 的参数 `-M` 进行声道路由，即把 oss 输出重定向到 oss 输入）。

但是 `obs-studio` 可以录制 pulseaudio 输出的音频。(默认的“桌面音频”这个输入源，没有说明应该是 pulseaudio 输出，故 oss 输出无法通过此录音）

所以有些软件可以使用 pulseaudio 作为输出。使用 pulseaudio 的软件的音频输出，不受上面的命令控制音频输出设备。pulseaudio 会根据自己的设置把音频送到对应设备，所以需要使用 pulseaudio 混音器控制。

在 kde5 下面自带的音频控制器，切换设备就是控制的 pulseaudio。

官方打包好的多媒体软件有些是支持 pulseaudio 但是这些软件中的大部分对应的编译选项没有打开。如果需要录制软件的音频输出，可以自行打开 ports 的编译选项自己编译。在软件中设置 pulseaudio 作为音频驱动输出就可以了。


## AMD CPU mode 2 reset

已知 APU 上使用 drm-kmod，打开空播放器可能会触发 mode 2 reset 报错即 driver reset，进而触发 Kernel Panic。

不要打开空的播放器窗口，或者打开空的音频播放器窗口。

音频文件要在终端里用命令行播放。

由于样本量不足，尚未进行 Bug 报告。
