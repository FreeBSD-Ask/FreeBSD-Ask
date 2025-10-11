# 6.1 Intel 和 AMD 显卡驱动

>**警告**
>
>请勿使用 `sysutils/desktop-installer`，会引发不必要的错误和问题。

## 故障排除与未竟事宜

![没安装驱动](../.gitbook/assets/noqudong.png)

未安装显卡驱动。

## 显卡支持情况

FreeBSD 的 i915、AMD 显卡驱动和与基本系统是分离的。目前是移植的 LTS 版本 Linux kernel 的 drm 驱动，作为 Port 来提供的。面向不同的系统版本，能支持的 Linux 内核版本也是不同的。


>**警告**
>
>这种移植并不覆盖 Linux 现有的全部 drm GPU 驱动，目前仅有 i915 amd 和 radeon，其他 vmwgfx、xe、virtio 等等都是未进行移植的！

>**注意**
>
>DG2 Arc 显卡尚不受支持（截止 drm 6.10 版本），参见 [Intel Arc A770: Kernel panic on kldload i915kms.ko #315](https://github.com/freebsd/drm-kmod/issues/315)。可能需要等到 6.12 的移植才能受支持。

>根据笔记本和桌面项目反馈，“在使用 drm-kmod 6.1 及更高版本的桌面系统（搭载 RX 570、580 等 AMD GPU）在运行数分钟或数小时后会逐渐出现严重卡顿，最终会导致桌面完全不可用。”该问题预计会在今年 12 月初前得到解决。参见 <https://github.com/FreeBSDFoundation/proj-laptop/issues/89>

| **FreeBSD 版本**         | **对应 DRM 驱动版本**                   | **GPU 支持范围（AMD / Intel）**    | **备注**             |
| :--------------------------: | :--------------------------------- | :---------------------------- | :------------------- |
| **FreeBSD 14.3-RELEASE**<br> | **drm-61-kmod（基于 Linux 6.1 DRM）** | - **AMD：** <br>**GCN 1（Southern Islands）** <br>**GCN 5（Polaris / Vega）** <br> **RDNA 1 / RDNA 2 / RDNA 3（Radeon RX 7000 系列）**<br>- **Intel：** <br>**Gen 4（GMA X3000 / 965）**<br>**Gen 5（Iron Lake）**<br>**Gen 6（Sandy Bridge）**<br>**Gen 7（Ivy / Haswell）**<br>**Gen 8（Broadwell）**<br>**Gen 9（Skylake / Kaby Lake / Coffee Lake）**<br>**Gen 10（Cannon Lake – 已废弃）**<br>**Gen 11（Ice Lake / Jasper Lake）**<br>**Gen 12（Tiger Lake / Alder Lake）**                                         | <br>理论支持 Intel 3 ～ 12 代 GPU。|
| **FreeBSD 15.0/16.0-CURRENT**                                        | **drm-66-kmod（基于 Linux 6.6 DRM）** | - **AMD：** 自 **GCN 1** 起至 **RDNA 3（Radeon RX 7000 系列）**，并包含 **Instinct MI300 加速卡** 支持。<br>- **Intel：** <br> • **Gen 4–8：** 旧核显（GMA、HD Graphics 4000 等）<br> • **Gen 9：** Skylake / Kaby Lake / Coffee Lake<br> • **Gen 10：** Cannon Lake （已废弃）<br> • **Gen 11：** Ice Lake / Jasper Lake<br> • **Gen 12：** Tiger Lake / Alder Lake <br> • **Gen 13：** Raptor Lake （基本兼容 Alder Lake 驱动）<br> • **Gen 14：** Meteor Lake （实验性，已合入 drm-66） | 实测 **Intel Alder Lake-N (N100)、i7-i260p** 显卡驱动加载正常，显示与视频加速功能稳定；<br><br>理论支持 **Intel 3 ～ 14 代 GPU**（含 Meteor Lake），但 13 代及以后缺乏充分实测；       |

- 非 LTS 版本（Port graphics/drm-latest-kmod/，仅 15.0/16.0，目前 6.9）：
  - Intel：Meteor Lake 图形在 6.7 后默认启用；6.9 包含实验性 Xe 驱动 ，用于 Gen 12+ GPU （Arc、Meteor Lake 等），为后续 Xe2 / Lunar Lake 做准备。i915 仍为默认。
  - AMD：引入对 **RDNA 3+ / RDNA 4** 的初步支持 。覆盖 GCN 到 RDNA 3 全部架构，并预置 RDNA 4 驱动。

- 后续目标版本（待移植）：6.12（LTS）：
  - Intel：Xe 驱动成熟，新增 Xe2 (Lunar Lake 核显) 与 Battlemage 独显支持 。加入 Arrow Lake (15 代) 代码。Meteor Lake 完全支持。i915 仍默认，Xe 面向 Gen12+ 新平台。
  - AMD：RDNA 4 官方支持 ，面向 RX 8000 系列。延续 GCN 至 RDNA 3 所有架构。

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
>每次点版本或大版本升级时，可能需要重新获取新系统源代码，重新编译安装显卡驱动模块方可顺利完成升级，而不是卡在黑屏的地方：或者你使用“模块源”。


DRM 即“Direct Rendering Manager”（直接渲染管理器），DRM 是 Linux 内核的子系统，负责与现代显卡的 GPU 进行交互。FreeBSD 在内核实现了 Linux 内核编程接口（LinuxKPI），并移植了 Linux DRM，类似的还有一些无线网卡驱动。


## 加入 Video 组

```sh
# pw groupmod video -m 你的用户名
```

>**警告**
>
>即使加入了 `wheel` 组，也应再加入 `video` 组，否则：硬解显示会出问题、Wayland 下普通用户将无权限调用显卡。

## 安装 Intel 核显/AMD 显卡驱动

>**注意**
>
> 在使用 Gnome 时，如果自动锁屏/息屏，可能无法再次进入桌面。见 [Bug 255049 - x11/gdm doesn't show the login screen](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=255049)。

>**注意**
>
>在使用 Ports 时，drm 需要在 `/usr/src` 中有一份当前版本系统源代码，可参考系统更新章节。如果你是参考的本书其他章节进行的安装，那么你的系统中很可能已经有一份源码了，无需再获取源码。


### FreeBSD 14.X

>**技巧**
>
>若要使用 pkg 安装，请参照本书其他章节配置 kernel modules（kmods）内核模块源。

```sh
# cd /usr/ports/graphics/drm-61-kmod
# make BATCH=yes install clean
```

或者（如有问题请使用 Ports）

```sh
# pkg install drm-61-kmod
```

### FreeBSD 15.0

```sh
# cd /usr/ports/graphics/drm-66-kmod
# make BATCH=yes install clean
```

>**注意**
>
> 像英特尔三代处理器的 HD 4000 这种比较古老的显卡，他在传统的 BIOS 模式下无需额外安装显卡驱动，但是 UEFI 下有可能会花屏（FreeBSD 13.0 及以后无此问题），且需要安装此 DRM 显卡驱动。

## 配置 Intel 核显/AMD 显卡

请按如下进行操作：

### Intel 核芯显卡

  ```sh
  # sysrc -f /etc/rc.conf kld_list+=i915kms
  ```

### AMD

- 如果是 HD7000 以后的 AMD 显卡，添加 `amdgpu`（大部分人应该使用这个，如果没用再换 `radeonkms`）

    ```sh
    # sysrc -f /etc/rc.conf kld_list+=amdgpu
    ```

- 如果是 HD7000 以前的 AMD 显卡，添加 `kld_list="radeonkms"`（这是十多年前的显卡了）

    ```sh
    # sysrc -f /etc/rc.conf kld_list+=radeonkms
    ```

### 故障排除与未竟事宜

>**注意**
>
>遇到任何问题时，请先使用 Ports 重新编译安装。尤其是在版本升级时。

- `KLD XXX.ko depends on kernel - not available or version mismatch.`

提示内核版本不符，请先升级系统或使用 ports 编译安装。14.3-RELEASE 及以上版本可以用内置的内核模块源（参见其他章节），应该不会出现类似问题。

![](../.gitbook/assets/amd_error.png)

## 视频硬解

### Intel 视频硬解

如果不配置此节，blender 等软件将无法运行！直接“段错误”。

- 使用 pkg 安装：

```sh
# pkg install libva-intel-media-driver
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/multimedia/libva-intel-media-driver/ 
# make install clean
```

### AMD 视频硬解

- 使用 pkg 安装

```sh
# pkg ins mesa-gallium-va mesa-gallium-vdpau
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/graphics/mesa-gallium-va/ && make install clean
# cd /usr/ports/graphics/mesa-gallium-vdpau/ && make install clean
```

---

可能还需要这么做：

将以下内容写入 `/usr/local/etc/X11/xorg.conf.d/20-amdgpu-tearfree.conf`（请自行创建）

```ini
Section "Device"
  Identifier "AMDgpu"
  Driver "amdgpu"
  Option "TearFree" "on"
EndSection
```

然后就可以用 `mpv --hwdec xxx.mp4` 来测试了。请自行安装 mpv。

## 亮度调节

### 通用

- 对于一般计算机：

```sh
# sysrc -f /boot/loader.conf  acpi_video="YES"
```

- 对于 Thinkpad：

```sh
# sysrc -f /boot/loader.conf  acpi_ibm_load="YES"
# sysrc -f /boot/loader.conf  acpi_video="YES"
```

### 英特尔/AMD

`backlight` 自 FreeBSD 13 引入。

```sh
# backlight          # 打印当前亮度
# backlight decr 20  # 降低 20% 亮度
# backlight +        # 默认调整亮度增加 10%
# backlight -        # 默认调整亮度减少 10%
```

如果上述操作不起作用，请检查路径 `/dev/backlight` 下都有哪些设备。

- 示例（照抄不会起作用的，自己 `ls /dev/backlight` 看看）：

```sh
# backlight -f /dev/backlight/amdgpu_bl00 - 10
# backlight -f /dev/backlight/backlight0 - 10  
```

### 参考文献

- [backlight -- configure backlight	hardware](https://man.freebsd.org/cgi/man.cgi?backlight)
- 经过测试，此部分教程适用于 renoir 显卡：

## 检查状态

如何判断是否成功驱动显卡：

```sh
$ ls -al /dev/dri/card0
lrwxr-xr-x  1 root wheel 8 Jul  2 19:39 /dev/dri/card0 -> ../drm/0

$ ls -al /dev/backlight/backlight0 
crw-rw---- 1 root video 1, 177 2025年 8月22日 /dev/backlight/backlight0 # 台式机 HDMI 等输出可能没有
```

你会发现你多了一个设备，名字是  `card0`（一般是数字是 `0`，如果有第二块显卡，名字会是  `card1` ），同时多出一个名为 `backlight0` 的设备（HDMI 下不会存在该设备）。

## 故障排除与未竟事宜

- 如果显卡使用驱动有问题请直接联系作者：[https://github.com/freebsd/drm-kmod/issues](https://github.com/freebsd/drm-kmod/issues)
- 如果笔记本出现了唤醒时屏幕点不亮的问题，可以在 `/boot/loader.conf` 中添加 `hw.acpi.reset_video="1"` 以在唤醒时重置显示适配器。
- 普通用户若非 `wheel` 组成员，那么请加入 `video` 组。如果普通用户没有被加入到 video 组（wheel 还不够），那么 KDE 的设置，关于此系统中的显卡驱动将永远显示为 llvmpipe 。会影响 Wayland 下普通用户的显示或硬解调用。

## 参考文献

- 显卡详细支持情况可以看 [wiki/Graphics](https://wiki.freebsd.org/Graphics)
