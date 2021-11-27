# 第七节 物理机下显卡的配置

FreeBSD 已从 Linux 移植了显卡驱动，理论上，A 卡 N 卡均可在 amd64 架构上正常运行。

## 支持情况

对于 FreeBSD 11，支持情况同 Linux 内核 4.11；

对于 FreeBSD 12，支持情况同 Linux 内核 4.16；

对于 FreeBSD 13，支持情况同 Linux 5.4，最高可以支持 Intel 第十二代处理器。

详细情况可以看&#x20;

{% embed url="https://wiki.freebsd.org/Graphics" %}

## 英特尔核显 / AMD 独显

### 安装驱动

* FreeBSD 12.0: `#pkg install drm-fbsd12.0-kmod`

注意：对于任意 12.X 均应该安装 `drm-fbsd12.0-kmod `，但应该使用 port 在本地重新构建而不应该使用 pkg 进行安装，否则不会正常运行。

* FreeBSD13：`#pkg install drm-fbsd13-kmod`

### 加载显卡

打开`/etc/rc.conf`:

* 如果为 intel 核心显卡，添加 `kld_list="i915kms"`
* 如果为 HD7000 以后的 AMD 显卡，添加` kld_list="amdgpu"`
* 如果为 HD7000 以前的 AMD 显卡，添加 `kld_list="radeonkms"`

### 视频硬解

`#pkg install xf86-video-intel libva-intel-driver`

## 英伟达显卡

```shell
#安装几个 nvidia 相关的包
#pkg install nvidia-driver nvidia-settings nvidia-xconfig
#配置驱动
#sysrc kld_list+="nvidia-modeset"
```

重启 这时候应该已经可以点亮图形界面了……

```shell
# 查看驱动信息
$nvidia-smi
```

如果发现系统没有使用 nvidia 驱动 需要自动生成配置文件

```shell
#Xorg -configure #生成配置文件。
#cp /root/xorg.conf.new /etc/X11/xorg.conf
```

然后重新启动就可以发现正常使用nvidia驱动了&#x20;

**注意**： 默认情况下，通过 pkg 安装的 nvidia-driver 是包含 linux compatibility support, 如果要使用 linux软件，需要执行以下命令，（实际上使用linux兼容层，以下命令是必须的。） 如果不需要使用 linux 兼容层，则不需要执行。

```shell
#sysrc linux_enable="YES"
```

当然如果使用官方的 pkg 包，安装好驱动重启后

```shell
$kldstat
```

会发现系统自动加载 linux.ko 模块。如果觉得太臃肿，不需要 Linux 兼容层 可以自己编译 nvidia-driver ports,去掉 linux compatibility support
