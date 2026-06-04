# 9.3 AMD 显卡驱动

本节涵盖 AMD 显卡驱动的安装与配置。请先阅读显卡驱动概述。

## 安装 AMD 显卡驱动

> **注意**
>
> 在使用 GNOME 时，如果自动锁屏/熄屏，可能无法再次进入桌面。相关技术问题可参见：Bug 255049 - x11/gdm doesn't show the login screen[EB/OL]. [2026-03-26]. <https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=255049>。

> **注意**
>
> 使用 Ports 安装时，drm 驱动需要在 **/usr/src** 中有一份当前版本的系统源代码，具体可参考系统更新章节。如果已参考本书其他章节安装，系统中通常已有一份源代码，无需再次获取。

### FreeBSD 14.x

```sh
# cd /usr/ports/graphics/drm-61-kmod
# make BATCH=yes install clean
```

或者使用 pkg 安装（如 Ports 安装有问题则使用此方法）：

```sh
# pkg install drm-61-kmod
```

### FreeBSD 15.0

使用 Ports 安装：

```sh
# cd /usr/ports/graphics/drm-66-kmod
# make BATCH=yes install clean
```

## AMD 显卡配置

- HD 7000 以后的 AMD 显卡，在 **/etc/rc.conf** 文件中添加 `amdgpu` 内核模块到 `kld_list`，以便系统启动时加载（多数用户应使用此驱动，如未生效，再修改为 `radeonkms`）：

```sh
# sysrc -f /etc/rc.conf kld_list+=amdgpu
```

- HD 7000 以前的 AMD 显卡，在 **/etc/rc.conf** 文件中添加 `radeonkms` 内核模块到 `kld_list`：

```sh
# sysrc -f /etc/rc.conf kld_list+=radeonkms
```

## AMD 显卡视频硬解

> **警告**
>
> 如果忽略此部分，Blender 等软件将无法运行，并会直接产生“段错误”。

### 安装 Mesa 的 Gallium VA-API 和 VDPAU 支持包

- 使用 pkg 安装：

```sh
# pkg install mesa-gallium-va mesa-gallium-vdpau
```

- 或使用 Ports 安装：

```sh
# cd /usr/ports/graphics/mesa-gallium-va/ && make install clean
# cd /usr/ports/graphics/mesa-gallium-vdpau/ && make install clean
```

### 附录：X11 设置

如果上述配置未生效，可能还需要配置 X11。

将以下内容写入 **/usr/local/etc/X11/xorg.conf.d/20-amdgpu-tearfree.conf** 文件（请自行创建该文件）：

```ini
Section "Device"
  Identifier "AMDgpu"          # 设置设备标识符为 AMDgpu
  Driver "amdgpu"              # 使用 amdgpu 驱动
  Option "TearFree" "on"       # 启用 TearFree 功能以防止屏幕撕裂
EndSection
```

配置完成后，可使用命令 `mpv --hwdec=auto xxx.mp4` 测试。需自行安装 mpv。

## 参考文献

- FreeBSD Project. Graphics[EB/OL]. [2026-03-25]. <https://wiki.freebsd.org/Graphics>. FreeBSD 官方维基，是图形硬件兼容性详细列表与配置指南。

## 课后习题

1. 尝试自动化 FreeBSD 上的 DRM 移植流程。
2. 尝试从 OpenBSD 重新移植 DRM 实现。
