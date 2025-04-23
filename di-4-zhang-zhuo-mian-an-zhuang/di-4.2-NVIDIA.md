# 第 4.2 节 显卡驱动（NVIDIA）


>**警告**
>
>当前页面的 N 卡驱动部分仍存在问题。可能无法使用。请帮助测试并将结果发送至 yklaxds@gmail.com，并说明显卡型号、机器参数等重要信息。

>**警告**
>
>对于没有持 **显卡直通** 的笔记本，必须安装英特尔核显驱动（相关 drm）！

## 笔记本核显 + Nvidia 独显（此节仍存在问题！需要你 PR 帮助改进或报告测试情况！）

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

## N 卡独显直连/台式机（仍存在问题！不要用）


### 安装驱动

安装几个 nvidia 相关的包：

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

查看驱动信息：

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
>在默认情况下，通过 pkg 安装的 nvidia-driver 是包含 Linux 兼容层支持的，如果要使用 Linux 兼容层，需要执行以下命令；如果不需要，则无需执行：
>
>```sh
># sysrc linux_enable="YES"
>```

当然，如果使用官方的 pkg 软件包，安装好驱动重启后：

```sh
$ kldstat
```

会发现系统自动加载了 `linux.ko` 模块。如果觉得太臃肿，不需要 Linux 兼容层，可以自己通过 ports 编译 `nvidia-driver`，去掉 `linux compatibility support`。




>**警告**
>
>除 N 卡外，应该尽量避免试图手动生成 `xorg.conf` 这个文件。你打不开桌面很大概率不是因为这个文件的配置有问题！你应该去检查显卡驱动或者桌面本身的问题。Xorg 是几乎不会出问题的！
