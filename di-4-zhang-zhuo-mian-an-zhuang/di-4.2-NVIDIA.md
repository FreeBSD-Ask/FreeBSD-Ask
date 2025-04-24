# 第 4.2 节 显卡驱动（NVIDIA）


>**警告**
>
>当前页面的 N 卡驱动部分仍存在问题。可能无法使用。请帮助测试并将结果发送至 yklaxds@gmail.com，并说明显卡型号、机器参数等重要信息。

>**警告**
>
>对于没有持 **显卡直通** 的笔记本，必须安装英特尔核显驱动（相关 drm）！

## 笔记本核显 + Nvidia 独显（此节仍存在问题！需要你 PR 帮助改进或报告测试情况！）


使用 pkg 安装：

```sh
# pkg install nvidia-drm-kmod
```

或者使用 Ports 安装；

```sh
# cd /usr/ports/graphics/nvidia-drm-kmod/ 
# make install clean
```

---

配置：

```sh
# echo 'hw.nvidiadrm.modeset="1"' >> /boot/loader.conf
# sysrc -f /etc/rc.conf kld_list+=nvidia-modeset
```


### 使用 VLC 硬解

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


## N 卡独显直连/台式机

### 安装驱动

安装几个 nvidia 相关的包：

```sh
# pkg install nvidia-drm-kmod nvidia-settings nvidia-xconfig
```

或者用 Ports 安装：

```sh
# cd /usr/ports/graphics/nvidia-drm-kmod/ && make install clean
# cd /usr/ports/x11/nvidia-settings/ && make install clean
# cd /usr/ports/x11/nvidia-xconfig/ && make install clean
```

```sh
# echo 'hw.nvidiadrm.modeset="1"' >> /boot/loader.conf
# sysrc -f /etc/rc.conf kld_list+=nvidia-modeset
```


## 查看驱动状态

重启后，应该可以驱动显卡了。要查看驱动信息：

```sh
$ nvidia-smi
```

如果发现系统没有使用 nvidia 驱动，需要自动生成配置文件：

```sh
# Xorg -configure #生成配置文件。注意，若正常显示无需这步和下步！
# cp /root/xorg.conf.new /etc/X11/xorg.conf
```

然后重新启动就可以发现正常使用 nvidia 驱动了。
