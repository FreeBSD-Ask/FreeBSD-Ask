# 6.16 KDE6（Wayland）

## 环境准备

由于 issue [Request to restore support for vboxvideo and vmwgfx DRM drivers #356](https://github.com/freebsd/drm-kmod/issues/356) 未得到解决，故在任何 VMware、Virtual Box 或基于 Virtio 的虚拟机上均无法复现此教程。你需要在真实的物理机上进行参照。

NVIDIA 卡未经测试。本文使用 Intel 12 代处理器（i7-1260P）的核显进行测试。

目前，右键正常，在任意位置按快捷键 Crtl + C 亦不会退回到 TTY。

请参照其他章节内容自行 **安装** drm、KDE 6、Fcitx 5、火狐浏览器等软件包。**并配置 drm 显卡驱动。** 其余软件包暂且 **不要** 进行任何配置，**仅安装** 即可。

## seatd 相关

### 安装 seatd

seatd 是一种会话管理器。~~我也不知道它是干什么用的，但是就是需要~~

- 使用 pkg 安装：
  
```sh
# pkg ins seatd
```

- 通过 Ports：

```sh
# cd /usr/ports/sysutils/seatd/ 
# make install clean
```

### 配置 seatd 服务

设置服务项：

```sh
# service dbus enable
# service seatd enable
```

## 启动 KDE 6

经测试，无法通过 SDDM 的 Wayland 选项启动 KDE6，按回车键登录后会自动回退到 SDDM 界面。

经测试，需要 root 账户权限才能启动，普通用户报错类似虚拟机（找不到 xxx）。

- 在 `/root` 下新建一脚本 `kde.sh`：

```sh
#! /bin/sh
export LANG=zh_CN.UTF-8 # 设置中文，Fcitx 需要
export LANGUAGE=zh_CN.UTF-8 # 设置中文，Fcitx 需要
export LC_ALL=zh_CN.UTF-8 # 设置中文，Fcitx 需要
export XMODIFIERS='@im=fcitx' # Fcitx 需要
/usr/local/bin/ck-launch-session /usr/local/lib/libexec/plasma-dbus-run-session-if-needed /usr/local/bin/startplasma-wayland # 启动桌面的命令
```

- 赋予可执行权限：

```sh
# chmod 755 /root/kde.sh
```

>**注意**
>
>你必须停止 SDDM 服务才能使用该脚本。请现在就检查 `/etc/rc.conf` 是有否 `sddm_enable="YES"` 字样，如有请删除。并按快捷键 ctrl + alt + f2 进入 TTY，登录 root 后输入 `service sddm stop` 停止 SDDM 服务。

- 进入 KDE

此时，你应位于 TTY 界面，并登录到了 root，并且不存在任何 X11 会话（如有，请禁用相关服务并重启再来）。

```sh
# sh /root/kde.sh
```

![在 FreeBSD 上通过 Wayland 运行 KDE6](../.gitbook/assets/kde-Wayland1.png)

>**技巧**
>
>上图之所以显示为“Intel UHD Graphics”显卡而非“Iris Xe Graphics”，是因为笔者无力购买第二根 DDR5 内存条。参见 [Intel® Iris® Xe Graphics Shows As Intel® UHD Graphics in the Intel® Graphics Command Center and Device Manager](https://www.intel.com/content/www/us/en/support/articles/000059744/graphics.html)（网站对应页面的中文翻译不正确）。

- 检查是否是 Wayland：

![检查当前是否位于 Wayland](../.gitbook/assets/kde-Wayland2.png)

```sh
# echo $XDG_SESSION_TYPE
```

## 配置 Fcitx 5

>**技巧**
>
>经测试 IBus 亦可用，且无需配置。

配置 Fcitx 自动启动：

```sh
# mkdir -p /root/.config/autostart/ # 创建自启动目录
# cp /usr/local/share/applications/org.fcitx.Fcitx5.desktop /root/.config/autostart/ # 自动启动 fcitx
```

当你初次进入 KDE Wayland 桌面时，KDE 会在右下角提示你要在设置的虚拟键盘中进行配置才能启用输入法。请留意该提示。若未设置，将无法切换输入法且无法输入中文。方法：

打开 KDE 系统设置：找到“键盘”——>虚拟键盘

![](../.gitbook/assets/kde-Wayland3-1.png)

请选择“Fcitx 6 Wayland 启动器（实验性）”

![](../.gitbook/assets/kde-Wayland5.png)

经测试，在终端 Konsole、火狐浏览器和 Chromium（启动命令为 `chrome --no-sandbox`）中均可输入中文。

![](../.gitbook/assets/kde-Wayland4.png)

## 声音

>**注意**
>
>在 root 下，PulseAudio 不会自动加载。经测试写入其他位置（如脚本中）无效。

打开 KDE 设置，找到“自动启动”，点击右上角“+ 添加”，点击“应用程序”。

在弹出窗口中输入 `pulseaudio`，并打开底部的选项“终端选项”，勾选“在终端中运行”和“命令退出时不关闭终端”两项重启系统即可。

![](../.gitbook/assets/kde-Wayland7.png)

![](../.gitbook/assets/kde-Wayland8.png)

![](../.gitbook/assets/kde-Wayland6.png)

设置可执行权限：

![](../.gitbook/assets/kde-Wayland7-1.png)

视频播放测试：

![](../.gitbook/assets/kde-Wayland9.png)

## 故障排除与未竟事宜

### 通过 SDDM 的 Wayland 会话启动 KDE

有反馈称 APU 核显可直接通过 SDDM 的 Wayland 会话启动 KDE，不需要上述 Shell 文件。需更多反馈。

### 使用 root 登录图形界面

这是不建议也是不安全的做法，但是普通用户似乎无法调用。待解决。

### 切换到 PipeWire

待解决。

## 参考文献

- [KDE Plasma 6 Wayland on FreeBSD](https://euroquis.nl/kde/2025/09/07/wayland.html)，此处提示需要 `seatd`。
