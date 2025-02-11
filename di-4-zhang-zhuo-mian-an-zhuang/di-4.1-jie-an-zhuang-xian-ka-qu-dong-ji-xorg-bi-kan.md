# 第 4.1 节 桌面环境概述、安装显卡驱动&Xorg

## 桌面环境概述

所有 FreeBSD 安装介质默认均不包含图形界面（DVD 的包含部分桌面的软件包，但是安装了也无法使用），需要手动安装。

>**警告**
>
>请勿使用 `sysutils/desktop-installer`，会引发不必要的错误和问题。

执着于一定要让 FreeBSD 表现出如 Linux 甚至是 Windows 一般的桌面力是一种可望而不可即的奢求，FreeBSD 官方的口号是 `The power to serve`。但 FreeBSD 基金会在 2024 年收到了一笔赞助，并成立了笔记本和台式机小组。

GhostBSD 适合对 BSD 好奇的人体验。本质上还是 FreeBSD 的预配置版本。如果是使用三个月以上的 FreeBSD 用户，不推荐这个发行版。它的软件仓库和 FreeBSD 一样，但是自己的独立服务器在国内速度感人（虽然也可以替换成 FreeBSD 的源）。

本章内容并非是让大家把所有的桌面都安装一遍，而是尽可能多地提供选择。

安装桌面的基本步骤是：① 安装显卡驱动 -> ② 安装 Xorg -> ③ 安装 KDE5/Gnome/XFCE/MATE -> ④ 安装显示管理器 sddm/lightdm -> ⑤ 安装输入法等软件

Wayland 是 xorg 的替代品，但是目前 BSD 上的 Wayland 支持欠佳。

其中，Gnome 可省略第四步，因为其显示管理器 gdm 早就在第二步就进行了自动安装。

显示管理器推荐搭配是 ：

- KDE5 + sddm
- Xfce/Mate + lightdm

>**警告**
>
>由于 slim 的作者早在 2013 年就停止了开发，不推荐使用，会产生一些奇怪的 bug——比如 fcitx5 用不了，加载不了 dbus。

输入法框架目前推荐使用：

- fcitx（对于 KDE 5 桌面）
- ibus（对于其他基于 GTK 的桌面，如 gnome、xfce、mate 等等）。

>**警告**
>
>一般地，请勿使用 scim，作者早就跑路（大概已经距今 18 年了）。

>**技巧**
>
>对于不同的 SHELL，环境变量的配置方法是不一样的，FreeBSD 14 前默认使用 `csh`，14 及以后默认使用 `sh`。而且不同桌面加载环境变量的方法也是不一样的，所以针对不同桌面，不同 SHELL 的配置方法是不一样的，具体方法请看具体桌面。

## 故障排除

![没安装驱动](../.gitbook/assets/noqudong.png)

没有安装显卡驱动。

---

>**警告**
>
>当前页面的 N 卡驱动部分仍存在问题。无法使用。

>**警告**
>
>对于没有显卡直通的笔记本，必须安装英特尔 drm！

>**注意**
>
>虚拟机显卡驱动看前边的章节，不再赘述。

FreeBSD 已从 Linux 移植了显卡驱动，理论上，绝大部分英特尔核显、A 卡、N 卡均在 AMD64 架构上正常运行。

## 显卡支持情况

对于 FreeBSD 13.1，编译使用`drm-510-kmod`，支持情况同 Linux 5.10。AMD 可支持 R7 4750U。

FreeBSD 14.1-RELEASE、14-STABLE（OSVERSION >1400508）、FreeBSD 15 CUEERNT，编译使用 `drm-61-kmod`，支持情况同 Linux 6.1。经过实际测试，可支持第十二代 Alder Lake-N（如 N100）。十三代等后续版本暂无条件测试。

>**技巧**
>
>可以在 port 开发者手册中的最后一章中查询 OSVERSION 对应的版本和 Git 提交。
>
>查看本机 OSVERSION：
>
>```sh
>root@ykla:~ # uname -U
>1500019
>```

>**警告**
>
>每次点版本或大版本升级时，可能需要重新获取新系统源代码，重新编译安装显卡驱动模块方可顺利完成升级，而不是卡在黑屏的地方。

## 安装英特尔核显/AMD 显卡驱动


>**注意**
>
> 在使用 Gnome 时，如果自动锁屏/息屏，可能无法再次进入桌面。见 [Bug 255049 - x11/gdm doesn't show the login screen](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=255049)。

>**注意**
>
>在使用 Ports 时，drm 需要在 `/usr/src` 中有一份当前版本系统源代码，可参考系统更新章节。如果你是参考的本书其他章节进行的安装，那么你的系统中很可能已经有一份源码了，无需再获取源码。


- FreeBSD 13.X

```sh
# cd /usr/ports/graphics/drm-510-kmod
# make BATCH=yes install clean
```

或者（如有问题请使用 Ports）

```sh
# pkg install drm-510-kmod
```


- FreeBSD 14.1 RELEASE、14-STABLE 及 FreeBSD 15 CUEERNT

```sh
# cd /usr/ports/graphics/drm-61-kmod
# make BATCH=yes install clean
```

或者（如有问题请使用 Ports）

```sh
# pkg install drm-61-kmod
```

>**注意**
>
> 像英特尔三代处理器的 HD 4000 这种比较古老的显卡，他在传统的 BIOS 模式下无需额外安装显卡驱动，但是 UEFI 下有可能会花屏（FreeBSD 13.0 及以后无此问题），且需要安装此 DRM 显卡驱动。

### 配置英特尔核显/AMD 显卡驱动

打开 `/etc/rc.conf`:

- 如果为 intel 核芯显卡，添加 `kld_list="i915kms"`
- AMD
  - 如果是 HD7000 以后的 AMD 显卡，添加 `kld_list="amdgpu"`（大部分人应该使用这个，如果没用再换 `radeonkms`）
  - 如果是 HD7000 以前的 AMD 显卡，添加 `kld_list="radeonkms"`（这是十多年前的显卡了）

### 故障排除

>**注意**
>
>遇到任何问题时，请先使用 Ports 重新编译安装。尤其是在版本升级时。

- `KLD XXX.ko depends on kernel - not available or version mismatch.`

提示内核版本不符，请先升级系统或使用 ports 编译安装。

![](../.gitbook/assets/amd_error.png)

- `/usr/ports/xxx no such xxx`
  
即找不到路径，请先获取 ports，请看前文。


#### 视频硬解（重要）

如果不配置此节，blender 等软件将无法运行！直接段错误。

```sh
# pkg install xf86-video-intel libva-intel-media-driver
```

或者

```sh
# cd /usr/ports/x11-drivers/xf86-video-intel/ && make install clean
# cd /usr/ports/multimedia/libva-intel-media-driver/ && make install clean
```



### 亮度调节

#### 通用

对于一般计算机：

```sh
# sysrc -f /boot/loader.conf  acpi_video="YES"
```

对于 Thinkpad：

```sh
# sysrc -f /boot/loader.conf  acpi_ibm_load="YES"
# sysrc -f /boot/loader.conf  acpi_video="YES"
```

#### 英特尔/AMD

backlight 自 FreeBSD 13 引入。

```sh
# backlight          #打印当前亮度
# backlight decr 20  #降低 20% 亮度
# backlight +        #默认调整亮度增加 10%
# backlight -        #默认调整亮度减少 10%
```

如果上述操作不起作用，请检查路径 `/dev/backlight` 下都有哪些设备。

- 示例（照抄不会起作用的，自己 `ls /dev/backlight` 看看）：

```sh
# backlight -f /dev/backlight/amdgpu_bl00 - 10
# backlight -f /dev/backlight/backlight0 - 10  
```

##### 参考文献

- [backlight -- configure backlight	hardware](https://man.freebsd.org/cgi/man.cgi?backlight)
- 经过测试，此部分教程适用于 renoir 显卡：

## 笔记本核显 + Nvidia 独显（仍存在问题！不要用）


>**警告**
>
>笔记本电脑一般不能单独用 nvidia 打开 xorg。**除非** 你的笔记本电脑支持 **显卡直通**。否则请先按照上部分对核显进行配置。

  - 550 驱动驱动支持的显卡参考 [FreeBSD Display Driver – X64](https://www.nvidia.cn/Download/driverResults.aspx/220794/cn/)

安装：

```sh
# pkg install nvidia-drm-kmod
```

或者

```sh
# cd /usr/ports/graphics/nvidia-drm-kmod/ 
# make install clean
```

配置：

```sh
# sysrc kld_list+="nvidia-drm.ko"
# echo 'hw.nvidiadrm.modeset="1"' >> /boot/loader.conf
```

### 查看显卡驱动状态

开机后在 kde 设置里查看显卡，默认用的是 intel 核显，终端里 `nvidia-smi` 仅有 `nvidia-xorg-service 8MB`。

然后在终端用这个命令调用 N 卡：

```sh
$ nvrun 程序名 # 默认无 GUI 运行
$ nvrun-vgl 程序名 # GUI 运行程序
```

`mesa-demos` 包含一些 opengl 示例，可用于测试驱动是否可用，非必要安装。

安装包后，若 xorg 启动成功则无需额外配置；若失败，再用 `pciconf -lv` 查找显卡的 busid，例如

```sh
vgapci0@pci0:1:0:0:	class=0x030000 rev=0xa1 hdr=0x00 vendor=0x10de device=0x0df4 subvendor=0x1043 subdevice=0x15f2
    vendor     = 'NVIDIA Corporation'
    device     = 'GF108M [GeForce GT 540M]'
    class      = display
    subclass   = VGA
```

在 `/usr/local/etc/X11/xorg-nvidia-headless.conf` 找到 `Device` 一节，并对应修改 `BusID` ,上面为 ”pci0:1:0:0“：

```sh
Section "Device"
    Identifier     "Device0"
    Driver         "nvidia"
    BusID          "PCI:1:0:0"
EndSection
```

检验是否成功启用独显，可以用 mesa-demos 中的程序测试，运行 `bounce`，用 `nvidia-smi -l 1` 观察(每隔一秒刷新一次)。在未使用 nvidia 驱动时会使用 7M 显存，在启用程序时显存并没有变化。


![](../.gitbook/assets/418810292836709.png)

 运行 `nvrun-vgl bounce` 用 `nvidia-smi -l 1` 观察使用 nvidia 驱动时使用了 13M 显存。
 
![](../.gitbook/assets/380531501625801.png)
 
### 开启 vlc 硬解

安装：

```sh
pkg install libva-vdpau-driver libvdpau libvdpau-va-gl
```
或者

```sh
# cd /usr/ports/multimedia/libva-vdpau-driver/ && make install clean
# cd /usr/ports/multimedia/libvdpau/ && make install clean
# cd /usr/ports/multimedia/libvdpau-va-gl/ && make install clean
```

工具->偏好设置->输入/编解码器->硬件加速解码：选择 VDPAU  视频解码器

![](../.gitbook/assets/121233788899956.png)

用 `nvrun-vgl vlc` 启动 vlc，并播放视频


![](../.gitbook/assets/59022617586598.png)

显存使用上升，标志着正在使用硬解。

## 独显直连/台式机（仍存在问题！不要用）


### 安装驱动

安装几个 nvidia 相关的包:

```sh
# pkg install nvidia-drm-kmod nvidia-settings nvidia-xconfig
```
>**技巧**
>
>`nvidia-drm-kmod` 目前依赖安装的 `nvidia-driver` 默认为 550。

>**注意**
>
>如果 pkg 找不到 `graphics/nvidia-drm-kmod` 就编译安装，该包提供了 PRIME 等支持。


或者：

```sh
# cd /usr/ports/graphics/nvidia-drm-kmod/ && make install clean
# cd /usr/ports/x11/nvidia-settings/ && make install clean
# cd /usr/ports/x11/nvidia-xconfig/ && make install clean
```

```sh
# sysrc kld_list+="nvidia-drm.ko" #配置驱动
# echo 'hw.nvidiadrm.modeset="1"' >> /boot/loader.conf
# reboot #重启
```


### 查看驱动状态

这时候应该已经可以驱动显卡了。

查看驱动信息:

```sh
$ nvidia-smi
```

如果发现系统没有使用 nvidia 驱动，需要自动生成配置文件：

```sh
# Xorg -configure #生成配置文件。注意，若正常显示无需这步和下步！
# cp /root/xorg.conf.new /etc/X11/xorg.conf
```

然后重新启动就可以发现正常使用 nvidia 驱动了

>**技巧**
>
>在默认情况下，通过 pkg 安装的 nvidia-driver 是包含 Linux 兼容层支持的, 如果要使用 Linux 兼容层，需要执行以下命令；如果不需要，则无需执行：
>
>```sh
># sysrc linux_enable="YES"
>```

当然，如果使用官方的 pkg 软件包，安装好驱动重启后：

```sh
$ kldstat
```

会发现系统自动加载了 `linux.ko` 模块。如果觉得太臃肿，不需要 Linux 兼容层，可以自己通过 ports 编译 `nvidia-driver`,去掉 `linux compatibility support`。

## xorg

可选软件包：

xorg 完整包: xorg

xorg 最小化包: xorg-minimal（不建议）

### 安装

通过 pkg 安装

```sh
# pkg install xorg
```

通过 ports 安装

```sh
# cd /usr/ports/x11/xorg
# make install clean
```

### 故障排除

- 如果显卡使用驱动有问题请直接联系作者：[https://github.com/freebsd/drm-kmod/issues](https://github.com/freebsd/drm-kmod/issues)
- 如果笔记本出现了唤醒时屏幕点不亮的问题，可以在 `/boot/loader.conf` 中添加 `hw.acpi.reset_video="1"` 以在唤醒时重置显示适配器。
- 普通用户若非 `wheel` 组成员，那么请加入 `video` 组。

>**警告**
>
>应该尽量避免试图手动生成 `xorg.conf` 这个文件。你打不开桌面很大概率不是因为这个文件的配置有问题！你应该去检查显卡驱动或者桌面本身的问题。Xorg 几乎是不会出问题的！

## 参考文献

- 详细情况可以看 [wiki/Graphics](https://wiki.freebsd.org/Graphics)

---

> **小故事**
>
> sddm gdm lightdm slim 在系统里乱战：
>
> sddm：我背后是 kde
>
> gdm：我背后是 gnome
>
> lightdm：我背后可以是任何一个
>
> slim：怎么办？好慌，潜水太久，管理员要踢我了。
>
> FreeBSD：合着你们在我地盘上养蛊呢？
