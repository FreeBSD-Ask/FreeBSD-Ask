# 第六节 物理机下显卡的配置

## N卡

注意：检查是否开启 linux 兼容层

```shell
#安装几个nvidia相关的包以及xorg。
pkg install nvidia-driver nvidia-settings nvidia-xconfig xorg dbus
#启用相关服务。
sysrc kld_list="nvidia nvidia-modeset linux"
sysrc dbus_enable="YES"
sysrc linux_enable="YES"
echo 'linux_enable="YES"' >> /boot/loader.conf
```

这时候应该已经可以点亮图形界面了……

```shell
nvidia-xconfig #生成配置文件。
startx 
```
