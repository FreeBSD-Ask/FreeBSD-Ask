# 第九节 物理机下显卡的配置

FreeBSD 已从 Linux 移植了显卡驱动，理论上，A 卡 N 卡均在 AMD64 架构上正常运行。

## 支持情况

对于 FreeBSD 11，支持情况同 Linux 内核 4.11；

对于 FreeBSD 12，支持情况同 Linux 内核 4.16；

对于 FreeBSD 13.1/14-current，编译使用`drm-510-kmod`，支持情况同 Linux 5.10，可以支持 Intel 第十二代处理器，AMD 可支持 R7 4750U。

详细情况可以看

<https://wiki.freebsd.org/Graphics>

## 英特尔核显 / AMD 独显

### 安装驱动

注意，如果要通过 `ports` 安装提示需要源码，请见第二十一章。

- FreeBSD 12.0: `#pkg install drm-fbsd12.0-kmod`

>**注意：除了 12.0，对于任意 12.X 均应该安装 `drm-fbsd12.0-kmod` ，但应该使用 port 在本地重新构建而不应该使用 pkg 进行安装，否则不会正常运行。**

- FreeBSD 13

>FreeBSD 13.0 可以使用二进制包进行安装`# pkg install drm-fbsd13-kmod` 或编译安装`drm-54-kmod`，配置方法同“加载显卡”。
>
>FreeBSD 13.1 需要通过 ports 编译安装`drm-510-kmod`。因为后者支持的显卡更多:`# cd /usr/ports/graphics/drm-510-kmod/ && make BATCH=yes install clean`

- FreeBSD 14：`# cd /usr/ports/graphics/drm-510-kmod/ && make BATCH=yes install clean`

>**故障排除：如果提示`/usr/ports/xxx no such xxx`找不到路径，请先获取 portsnap：`portsnap fetch extract`。portsnap 换源问题请看 第三章 第二节。**
>
> `graphics/drm-kmod` 这个包并不是真实存在的，他只是帮助判断系统版本以安装对应的 ports 包的元包。
### 加载显卡

打开`/etc/rc.conf`:

- 如果为 intel 核芯显卡，添加 `kld_list="i915kms"`
- 如果为 HD7000 以后的 AMD 显卡，添加 `kld_list="amdgpu"` （大部分人应该使用这个，如果没用再去使用`radeonkms`）
- 如果为 HD7000 以前的 AMD 显卡，添加 `kld_list="radeonkms"` （这是十余年前的显卡了）

### 视频硬解

`# pkg install xf86-video-intel libva-intel-driver`

### 亮度调节

#### 通用

一般计算机：
```
# sysrc -f /boot/loader.conf  acpi_video="YES"
```

对于 Thinkpad：

```
# sysrc -f /boot/loader.conf  acpi_ibm_load="YES"
# sysrc -f /boot/loader.conf  acpi_video="YES"
```

>仅限 FreeBSD 13

```
# backlight decr 20  #降低 20% 亮度
```

#### 英特尔
```
# pkg install intel-backlight
# intel-backlight 80 #调整为 80% 亮度
```

## 英伟达显卡

```
# pkg install nvidia-driver nvidia-settings nvidia-xconfig #安装几个 nvidia 相关的包
# sysrc kld_list+="nvidia-modeset" #配置驱动
# reboot #重启
```

这时候应该已经可以驱动显卡了。

```
# 查看驱动信息
$ nvidia-smi
```

如果发现系统没有使用 nvidia 驱动需要自动生成配置文件：

```
# Xorg -configure #生成配置文件。注意，该步骤不是必要！
# cp /root/xorg.conf.new /etc/X11/xorg.conf
```

然后重新启动就可以发现正常使用 nvidia 驱动了

**注意**： 默认情况下，通过 pkg 安装的 nvidia-driver 是包含 Linux 兼容层支持的, 如果要使用 Linux 软件，需要执行以下命令，（实际上使用 linux 兼容层，以下命令是必须的。） 如果不需要使用 Linux 兼容层，则不需要执行。

```
# sysrc linux_enable="YES"
```

当然如果使用官方的 pkg 包，安装好驱动重启后：

```
$ kldstat
```

会发现系统自动加载了 `linux.ko` 模块。如果觉得太臃肿，不需要 Linux 兼容层 可以自己通过 ports 编译 `nvidia-driver`,去掉 `linux compatibility support`。
