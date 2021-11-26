# 第六节 物理机下显卡的配置

FreeBSD 已从 Linux 移植了显卡驱动，理论上，A 卡 N 卡均可在 amd64 架构上正常运行。


## 英特尔核显 / AMD 独显

### 安装驱动

- FreeBSD12.X: `#pkg install drm-fbsd12.0-kmod`
- FreeBSD13：`#pkg install drm-fbsd13-kmod`

### 加载显卡

打开`/etc/rc.conf`:

- 如果为 intel 核心显卡，添加 kld_list="i915kms"

- 如果为 HD7000 以后的 AMD 显卡，添加kld_list="amdgpu"

- 如果为 HD7000 以前的 AMD 显卡，添加kld_list="radeonkms"


### 视频硬解

`#pkg install xf86-video-intel libva-intel-driver`


## 英伟达显卡

```shell
#安装几个nvidia相关的包
#pkg install nvidia-driver nvidia-settings nvidia-xconfig
#配置驱动
#sysrc kld_list+="nvidia-modeset"

```
重启
这时候应该已经可以点亮图形界面了……
```shell
# 查看驱动信息
$nvidia-smi
```

如果发现系统没有使用nvidia驱动
需要自动生成配置文件
```shell
#Xorg -configure #生成配置文件。
#cp /root/xorg.conf.new /etc/X11/xorg.conf
```
然后重新启动就可以发现正常使用nvidia驱动了
