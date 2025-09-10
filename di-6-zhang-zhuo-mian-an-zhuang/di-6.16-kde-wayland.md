# 6.16 KDE6（Wayland）

## 环境准备

由于 issue [Request to restore support for vboxvideo and vmwgfx DRM drivers #356](https://github.com/freebsd/drm-kmod/issues/356) 未得到解决，故在任何 VMware、Virtual Box 或基于 Virtio 的虚拟机上均无法复现此教程。

NVIDIA 卡未经测试。本文使用 12 代处理器（i7-1260P）的核显进行测试。

请参照其他章节内容自行安装 drm、KDE 6、Fcitx 5、火狐浏览器等软件包。

并配置 drm。其余软件包暂不需进行任何配置，仅安装即可。

## seatd 相关

### 安装 seatd

seatd 是一种会话管理器。~~我也不知道它是干什么用的，但是就是需要~~

- 使用 pkg 安装：
  
```sh
# pkg ins seatd
```

- 通过 Ports：

```sh
# cd /usr/ports/sysutils/seatd/ 
# make install clean
``

### 配置 seatd 服务

设置服务项：

```sh
# service dbus enable
# service seatd enable
```

## 启动桌面

经测试，无法通过 SDDM 的 Wayland 选项启动 KDE6，按回车键登录后会自动回退到 SDDM 界面。

经测试，需要 root 账户权限才能启动，普通用户报错类似虚拟机（找不到 xxx）。

- 在 `/root` 下新建一脚本 `kde.sh`：

```sh
#! /bin/sh
export LANG=zh_CN.UTF-8 # 设置中文，Fcitx 需要
export LANGUAGE=zh_CN.UTF-8 # 设置中文，Fcitx 需要
export LC_ALL=zh_CN.UTF-8 # 设置中文，Fcitx 需要
export XMODIFIERS='@im=fcitx' # Fcitx 需要
/usr/local/bin/ck-launch-session /usr/local/lib/libexec/plasma-dbus-run-session-if-needed /usr/local/bin/startplasma-wayland # 启动桌面的命令
```

- 赋予可执行权限：

```sh
# chmod 755 /root/kde.sh
```

>**注意**
>
>你必须停止 SDDM 服务才能使用该脚本。请现在就检查 `/etc/rc.conf` 是有否 `sddm_enable="YES"` 字样，如有请删除。并按快捷键 ctrl + alt + f2 进入 TTY，登录 root 后输入 `service sddm stop` 停止 SDDM 服务。

- 进入 KDE

```sh
# sh /root/kde.sh
```

