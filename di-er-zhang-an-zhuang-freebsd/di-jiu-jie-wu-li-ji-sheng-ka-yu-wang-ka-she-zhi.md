# 第九节 声卡与网卡设置
## FreeBSD 声卡
### 声音设置

用以下命令查看当前声卡设备

```shell
$cat /dev/sndstat
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
后面带有default是oss默认设备。如果软件的音频使用的oss且输出是默认的，音频就会从这个设备输出。  
FreeBSD大部分软件的音频输出驱动为oss。有些默认是pulseaudio(比如firefox) ，这些软件的设置看最后的提示。

下列命令可以修改输出的设备。
最后的数字是对应的pcm后面的数字。

```shell
$sysctl hw.snd.default_unit=5
```
这里推荐几个oss mixer

kde5 audio/dsbmixer

gtk  audio/gtk-mixer

非图形化audio/mixertui

### 提示
但是oss有些缺点，使用obs-studio 无法录制oss输出。只能录oss输入。看官方论坛里，可以virtual_oss 模拟一个设备实现，这个没具体研究过  

但是obs-studio可以录pulseaudio 输出的音频。
所以有些软件可以使用pulseaudio作为输出。使用pulseaudio的软件的音频输出,不受上面的命令控制音频输出设备。pulseaudio 会根据自己的设置把音频送到对应设备  

所以需要使用pulseaudio混音器控制。
在kde5下面自带的音频控制器，切换设备就是控制的pulseaudio.
官方打包好的多媒体软件有些是支持pulseaudio但是这些软件中的大部分对应的编译选项没有打开。如果需要
录制软件的音频输出，可以自行打开编译选项自己编译。在软件中设置pulseaudio 作为音频驱动输出就可以了
