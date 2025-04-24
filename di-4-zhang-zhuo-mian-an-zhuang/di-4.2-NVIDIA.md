# 第 4.2 节 显卡驱动（NVIDIA）

>**警告**
>
>对于没有持 **显卡直通** 的笔记本，必须安装英特尔核显驱动（相关 drm）！

## 安装显卡驱动


使用 pkg 安装：

```sh
# pkg install nvidia-drm-kmod nvidia-settings
```

或者使用 Ports 安装；

```sh
# cd /usr/ports/graphics/nvidia-drm-kmod/ && make install clean
# cd /usr/ports/x11/nvidia-settings/ && make install clean
```


## 配置 NVIDIA 显卡

- 启动内核模块

```sh
# echo 'hw.nvidiadrm.modeset="1"' >> /boot/loader.conf
# sysrc -f /etc/rc.conf kld_list+=nvidia-modeset
```
- 生成 X11 配置文件。注意，若正常显示无需这步及下步！

```sh
# Xorg -configure 
# cp /root/xorg.conf.new /etc/X11/xorg.conf
```

然后重新启动就可以发现正常使用 NVIDIA 驱动了。

## 使用 VLC 硬解

- 使用 pkg 安装 VLC：

```sh
pkg install libva-vdpau-driver libvdpau libvdpau-va-gl
```

- 或者使用 Ports 安装

```sh
# cd /usr/ports/multimedia/libva-vdpau-driver/ && make install clean
# cd /usr/ports/multimedia/libvdpau/ && make install clean
# cd /usr/ports/multimedia/libvdpau-va-gl/ && make install clean
```

---

工具->偏好设置->输入/编解码器->硬件加速解码：选择 VDPAU  视频解码器

![](../.gitbook/assets/121233788899956.png)


## 查看驱动状态

重启后，应该可以驱动显卡了。

- 要查看驱动信息（每秒刷新一次）：

```sh
$ nvidia-smi -L -1 
```

- 查看 KDE 系统参数：

![](../.gitbook/assets/nvi1.png)

- 打开一部 1.5G 左右的电影，可以看到显存明显上升（我是从 3M 上升到了数百兆）

![](../.gitbook/assets/nvi2.png)


