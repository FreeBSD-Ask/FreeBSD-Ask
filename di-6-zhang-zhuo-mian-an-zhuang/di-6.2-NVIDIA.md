# 6.2 NVIDIA 显卡驱动

## NVIDIA 显卡驱动概述

对于台式机，注意若 CPU 是英特尔处理器，且型号以 F（如 [i5-9400F](https://www.intel.cn/content/www/cn/zh/products/sku/190883/intel-core-i59400f-processor-9m-cache-up-to-4-10-ghz/specifications.html) [备份](https://web.archive.org/web/20260120221551/https://www.intel.cn/content/www/cn/zh/products/sku/190883/intel-core-i59400f-processor-9m-cache-up-to-4-10-ghz/specifications.html)）或者 KF（如 [i5-12600KF](https://www.intel.cn/content/www/cn/zh/products/sku/134590/intel-core-i512600kf-processor-20m-cache-up-to-4-90-ghz/specifications.html) [备份](https://web.archive.org/web/20260121072407/https://www.intel.cn/content/www/cn/zh/products/sku/134590/intel-core-i512600kf-processor-20m-cache-up-to-4-90-ghz/specifications.html)）结尾的型号，是没有核芯显卡的，不需要处理核显相关配置。

若你已拥有独立显卡，且你的视频输出（DP 或 HDMI）是直接插入的独立显卡。那么通常来说，你同样无需对核显进行任何配置，仅处理独显本身的驱动即可。

对于没有显卡直通能力的笔记本，必须先按照其他章节内容先安装配置英特尔核显驱动（相关 DRM）再参照下文进行配置！

## 加入 video 组

将指定用户添加到 video 组，以便访问显卡设备：

```sh
# pw groupmod video -m 你的用户名
```

## 安装显卡驱动

使用 pkg 安装：

```sh
# pkg install nvidia-drm-kmod nvidia-settings
```

或者使用 Ports 安装：

```sh
# cd /usr/ports/graphics/nvidia-drm-kmod/ && make install clean
# cd /usr/ports/x11/nvidia-settings/ && make install clean
```

列出已经安装的 NVIDIA 相关软件：

```sh
# pkg info -q | grep -i nvidia
```


## 配置 NVIDIA 显卡

### 启动 NVIDIA 相关内核模块

```sh
# echo 'hw.nvidiadrm.modeset="1"' >> /boot/loader.conf  # 启用 NVIDIA DRM 模式设置
# sysrc -f /etc/rc.conf kld_list+=nvidia-modeset       # 添加 nvidia-modeset 内核模块以便启动时加载
```

>**警告**
>
>不要试图加载 `nvidia-drm.ko`，会导致系统宕机。

### 生成 X11 配置文件

注意，若可正常显示，则无需执行此节！

```sh
# Xorg -configure                     # 自动生成 Xorg 配置文件
# cp /root/xorg.conf.new /etc/X11/xorg.conf  # 将生成的配置文件复制到 /etc/X11/xorg.conf
```

>**警告**
>
>不要试图安装和使用 Port `x11/nvidia-xconfig`。没有用且会卡死。


## 硬件加速和解码器

安装 VDPAU 驱动及相关库以支持视频硬件加速。

- 使用 pkg 安装：

```sh
# pkg install libva-vdpau-driver libvdpau libvdpau-va-gl
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/multimedia/libva-vdpau-driver/ && make install clean
# cd /usr/ports/multimedia/libvdpau/ && make install clean
# cd /usr/ports/multimedia/libvdpau-va-gl/ && make install clean
```

然后重新启动后即可正常使用 NVIDIA 驱动。

## 查看 NVIDIA 驱动状态

- 列出所有 NVIDIA GPU 及其详细信息

```sh
$ nvidia-smi 
```

`nvidia-smi` 示例输出：

```sh
# nvidia-smi
Mon Jan 19 19:06:59 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.126.09             Driver Version: 580.126.09     CUDA Version: N/A      |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 3060 Ti     Off |   00000000:01:00.0  On |                  N/A |
|  0%   39C    P8             12W /  225W |     409MiB /   8192MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

- 查看 KDE 系统信息：

![](../.gitbook/assets/nvi2.png)

- 用 MPV 打开一部电影，可以看到显存使用量明显上升（我是从 3 MB 上升到了数百兆），也可以用 SMPlayer 观看。

![](../.gitbook/assets/nvi1.jpg)

## 参考文献

- [关于我们的最新处理器和命名更新的简要指南](https://www.intel.cn/content/www/cn/zh/processors/processor-numbers.html) [备份](https://web.archive.org/web/20260121102640/https://www.intel.cn/content/www/cn/zh/processors/processor-numbers.html)。英特尔官方关于 CPU 代号的说明。

## 故障排除

### nvidia-smi 命令报错“mismatch”

![](../.gitbook/assets/no-version-vo.jpg)

当执行 nvidia-smi 命令时会出现错误提示“API mismatch”等字样。直译是 API 不匹配，提及不匹配，首先会想到是版本不匹配，即问题可能出现在 NVIDIA 本身的版本不匹配、NVIDIA 驱动本身与其他 NVIDIA 软件包版本不匹配、NVIDIA 和现有 FreeBSD 基本系统不匹配。

因此建议将所有 NVIDIA 软件包全部卸载，随后将 FreeBSD 基本系统更新到最新，再重新执行驱动安装流程。

### 如何卸载既有 NVIDIA 相关软件包

如果提示版本不符，需要先卸载所有安装的 NVIDIA 相关软件包，然后按本文进行配置：

```sh
# pkg delete *nvidia*
```

### 如何阻止驱动更新

把 `pkg info -q | grep -i nvidia` 输出的相关软件包都逐个使用 `pkg lock`命令锁定即可。

形如

```sh
# pkg lock nvidia-drm-kmod
# pkg lock nvidia-settings
```

但是如果运行 `freebsd-update` 命令，或者执行 pkgbase 对系统打补丁或更新补丁也可能会影响驱动。

因此需要读者自行平衡安全与日常。

