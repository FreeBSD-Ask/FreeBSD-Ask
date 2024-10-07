# 第 4.1 节 安装显卡驱动及 Xorg（必看）

>**警告**
>
>当前页面的 N 卡驱动部分仍有待测试！可能存在问题。

>**警告**
>
>对于没有显卡直通的笔记本，必须安装英特尔 drm！

>**注意**
>
>虚拟机显卡驱动看前边的章节，不再赘述。

FreeBSD 已从 Linux 移植了显卡驱动，理论上，绝大部分英特尔核显、A 卡 N 卡均在 AMD64 架构上正常运行。

## 显卡支持情况

对于 FreeBSD 13.1，编译使用`drm-510-kmod`，支持情况同 Linux 5.10。AMD 可支持 R7 4750U。

FreeBSD 14.1-RELEASE、14-STABLE 1400508（即 2024 年 2 月 18 日后以的 STABLE 版本，Git 提交为 `2d120981e26dfef5c9cb9eb9936bb46cb6918136`）FreeBSD 15 CUEERNT，编译使用 `drm-61-kmod`，支持情况同 Linux 6.1。

>**技巧**
>
>1400508 指的是 OSVERSION。
>
>可以在 port 开发者手册中的最后一章中查询对应的版本和 Git 提交。
>
>查看本机 OSVERSION：
>
>```sh
>root@ykla:~ # uname -U
>1500019
>```


## 安装英特尔核显/AMD 独显驱动——简单版本（推荐）

首先切换到 latest 源，或使用 ports 安装：

```sh
# pkg install drm-kmod
```

或者

```sh
# cd /usr/ports/graphics/drm-kmod/
# make BATCH=yes install clean
```


>**注意**
>
>在使用 Ports 时，drm 需要在 `/usr/src` 中有一份系统源代码。

> **注意**
>
> `graphics/drm-kmod` 这个包并非真实存在，他只是帮助判断系统版本以安装对应的 port 的元包。
>
> 像英特尔三代处理器的 HD 4000 这种比较古老的显卡，他在传统的 BIOS 模式下无需额外安装显卡驱动，但是 UEFI 下有可能会花屏（FreeBSD 13.0 及以后无此问题），且需要安装此 DRM 显卡驱动。

### 故障排除

- `KLD XXX.ko depends on kernel - not available or version mismatch.`

提示内核版本不符，请先升级系统或使用 ports 编译安装。

![](../.gitbook/assets/amd_error.png)

- 提示 `/usr/ports/xxx no such xxx`
  
即找不到路径，请先获取 ports，请看前文。

## 安装英特尔核显/AMD 独显驱动——复杂版本

>**注意**
>
>如果要使用 `ports` 安装提示需要源码，请见其他章节。

- FreeBSD 13.X

```sh
# cd /usr/ports/graphics/drm-510-kmod/ 
# make BATCH=yes install clean
```

- FreeBSD 14.1 RELEASE、14-STABLE 1400508（即 2024 年 2 月 18 日以后的 STABLE 版本，Git 提交为 `2d120981e26dfef5c9cb9eb9936bb46cb6918136`）及 FreeBSD 15 CUEERNT

```sh
# cd /usr/ports/graphics/drm-61-kmod/ 
# make BATCH=yes install clean
```


## 配置、加载英特尔核显/AMD 独显

>**注意**
>
> 无论是使用以上哪种方法，都需要进行这一步配置。

打开 `/etc/rc.conf`:

- 如果为 intel 核芯显卡，添加 `kld_list="i915kms"`
- AMD
  - 如果为 HD7000 以后的 AMD 显卡，添加 `kld_list="amdgpu"` （大部分人应该使用这个，如果没用再去使用 `radeonkms`）
  - 如果为 HD7000 以前的 AMD 显卡，添加 `kld_list="radeonkms"` （这是十多年前的显卡了）

### 视频硬解

```sh
# pkg install xf86-video-intel libva-intel-driver
```

或者

```sh
# cd /usr/ports/x11-drivers/xf86-video-intel/ && make install clean
# cd /usr/ports/multimedia/libva-intel-driver && make install clean
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

#### 英特尔

backlight 自 FreeBSD 13 引入。

```sh
# backlight          #打印当前亮度
# backlight decr 20  #降低 20% 亮度
# backlight +        #默认调整亮度增加 10%
# backlight -        #默认调整亮度减少 10%
```

##### 参考文献

- [backlight -- configure backlight	hardware](https://man.freebsd.org/cgi/man.cgi?backlight)
- 经过测试，此部分教程适用于 renoir 显卡：


>**注意**
>
> 在使用 Gnome 时，如果自动锁屏或息屏，可能无法再次进入桌面。见 [Bug 255049 - x11/gdm doesn't show the login screen](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=255049)。


## 笔记本核显 + Nvidia 独显

**除非** 你的笔记本电脑支持 **显卡直通**，否则笔记本电脑一般请先按照上边的方法配置核显。

>**警告**
>
>笔记本电脑一般不能单独用 nvidia 打开 xorg。**除非** 你的笔记本电脑支持 **显卡直通**。

### 旧显卡

>**技巧**
>
>下面的 `390` 亦可换成 `340`、470。

- 340 驱动支持的显卡参考 [FreeBSD Display Driver – X64](https://www.nvidia.cn/Download/driverResults.aspx/156260/cn/)
- 390 驱动支持的显卡参考 [FreeBSD Display Driver – X64](https://www.nvidia.cn/download/driverResults.aspx/196293/cn/)
- 470 驱动支持的显卡参考 [FreeBSD Display Driver – X64](https://www.nvidia.cn/Download/driverResults.aspx/227125/cn/)


```sh
# pkg install nvidia-secondary-driver-390
```

或者：

```sh
# cd /usr/ports/x11/nvidia-secondary-driver-390/ 
# make install clean
```

其中：

  - x11/nvidia-hybrid-graphics-390   用于支持双显卡切换
  - x11/nvidia-secondary-driver-390  对应的显卡驱动


配置：

```sh
# sysrc kld_list+=nvidia-modeset
# sysrc nvidia_xorg_enable=YES
```


### 新显卡
  - 550 驱动驱动支持的显卡参考 [FreeBSD Display Driver – X64](https://www.nvidia.cn/Download/driverResults.aspx/220794/cn/)

```sh
# cd /usr/ports/graphics/nvidia-drm-kmod/ && make install clean
# cd /usr/ports/x11/nvidia-secondary-driver && make install clean
```

其中：

  - graphics/nvidia-drm-kmod    用于支持双显卡切换
  - x11/nvidia-secondary-driver 对应的显卡驱动

配置：

```sh
# sysrc kld_list+="nvidia-drm.ko"
# sysrc -f /boot/loader.conf  hw.nvidiadrm.modeset=1
```


### 查看显卡驱动状态

开机后在 kde 设置里查看显卡默认用的是 intel 核显，终端里 `nvidia-smi` 只有 `nvidia-xorg-service 8MB`。

然后在终端用这个命令调用 N 卡：

```sh
$ nvrun 程序名 # 默认无 GUI 运行
$ nvrun-vgl 程序名 # GUI 运行程序
```

`mesa-demos` 包含一些 opengl 示例，可用于测试驱动是否可用，非必要安装。

`kld_list` 中 `nvidia-modeset`  和 `i915kms` 需要同时存在。

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

工具->偏好设置->输入/编解码器->硬件加速解码：选择VDPAU 视频解码器

![](../.gitbook/assets/121233788899956.png)

用 `nvrun-vgl vlc` 启动 vlc，并播放视频


![](../.gitbook/assets/59022617586598.png)

显存使用上升，正在使用硬解

## 独显直连/台式机

注意，有多个版本的 N 卡驱动，不知道该用哪个的去看 FreeBSD 手册《X Window 系统》一节。

### 安装驱动

安装几个 nvidia 相关的包:

```sh
# pkg install nvidia-driver nvidia-settings nvidia-xconfig nvidia-drm-kmod
```


>**注意**
>
>如果 pkg 找不到 `graphics/nvidia-drm-kmod` 就编译安装，该包提供了 PRIME 等支持。


或者：

```sh
# cd /usr/ports/x11/nvidia-driver/ && make install clean
# cd /usr/ports/x11/nvidia-settings/ && make install clean
# cd /usr/ports/x11/nvidia-xconfig/ && make install clean
# cd /usr/ports/graphics/nvidia-drm-kmod/ && make install clean
```

```sh
# sysrc kld_list+="nvidia-drm.ko" #配置驱动
# sysrc -f /boot/loader.conf hw.nvidiadrm.modeset=1 
# reboot #重启
```


### 查看驱动状态

这时候应该已经可以驱动显卡了。

查看驱动信息:

```sh
$ nvidia-smi
```

如果发现系统没有使用 nvidia 驱动需要自动生成配置文件：

```sh
# Xorg -configure #生成配置文件。注意，这一步步骤并非必要！
# cp /root/xorg.conf.new /etc/X11/xorg.conf
```

然后重新启动就可以发现正常使用 nvidia 驱动了

>**注意**
>
>在默认情况下，通过 pkg 安装的 nvidia-driver 是包含 Linux 兼容层支持的, 如果要使用 Linux 软件，需要执行以下命令（实际上使用 linux 兼容层，以下命令是必须的） ，如果不需要使用 Linux 兼容层，则不需要执行。

```sh
# sysrc linux_enable="YES"
```

当然如果使用官方的 pkg 软件包，安装好驱动重启后：

```sh
$ kldstat
```

会发现系统自动加载了 `linux.ko` 模块。如果觉得太臃肿，不需要 Linux 兼容层可以自己通过 ports 编译 `nvidia-driver`,去掉 `linux compatibility support`。

## 附：拉取开发版 drm-kmod（仅限 FreeBSD-CURRENT）

> **警告**
>
> 此部分属于实验性内容且仅限 FreeBSD-CURRENT 使用，不建议新手操作。

>**注意**
>
> 请提前在 `/usr/src` 准备好一份系统源码。

拉取最新的 drm-kmod 并编译安装：

安装 git：

```sh
# pkg install git
```

或者：

```sh
# cd /usr/ports/devel/git/ 
# make install clean
```

然后：

```sh
$ git clone --depth=1 https://github.com/dumbbell/drm-kmod/
$ cd freebsd/drm-kmod
$ git checkout -b update-to-v5.17
$ make
…
# make install
===> linuxkpi (install)
install -T release -o root -g wheel -m 555   linuxkpi_gplv2.ko /boot/modules/
===> ttm (install)
install -T release -o root -g wheel -m 555   ttm.ko /boot/modules/
===> drm (install)
install -T release -o root -g wheel -m 555   drm.ko /boot/modules/
===> amd (install)
===> amd/amdgpu (install)
install -T release -o root -g wheel -m 555   amdgpu.ko /boot/modules/
===> radeon (install)
install -T release -o root -g wheel -m 555   radeonkms.ko /boot/modules/
===> i915 (install)
install -T release -o root -g wheel -m 555   i915kms.ko /boot/modules/
kldxref /boot/modules
```

参考资料

- [[drm ERROR :radeon_ttm_init] failed initializing buffer object driver(-22) – radeonkms no longer loads with drm-devel-kmod on AMD Thames [Radeon HD 7550M/7570M/7650M]](https://github.com/freebsd/drm-kmod/issues/93#issuecomment-962622626)

### 故障排除

- 如果显卡使用驱动有问题请直接联系作者：[https://github.com/freebsd/drm-kmod/issues](https://github.com/freebsd/drm-kmod/issues)
- 如果笔记本出现了唤醒时屏幕点不亮的问题，可以在 `/boot/loader.conf` 中添加 `hw.acpi.reset_video="1"` 以在唤醒时重置显示适配器。

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

>**警告**
>
>总有人试图手动生成 `xorg.conf` 这个文件，这是非常错误的行为！你打不开桌面很大概率不是因为这个文件的配置有问题！你应该去检查显卡驱动或者桌面本身的问题。Xorg 几乎是不会出问题的！

## 参考文献

- 详细情况可以看 [wiki/Graphics](https://wiki.freebsd.org/Graphics)
