# 6.6 QQ（Linux 版）


## 基于 RockyLinux（FreeBSD Port）

>**注意**
>
>请先参照本书其他章节先行安装 RockyLinux 兼容层（FreeBSD Port）

### 安装 rpm 工具

- 使用 pkg 安装

```sh
# pkg install rpm4
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/archivers/rpm4/ 
# make install clean
```

### 下载安装 QQ

- 下载 QQ，官方链接：[QQ Linux 版 - 轻松做自己](https://im.qq.com/linuxqq/index.shtml)

```sh
# fetch https://dldir1.qq.com/qqfile/qq/QQNT/Linux/QQ_3.2.17_250521_x86_64_01.rpm # 写作本文时链接如此，请自行获取最新链接
```

- 安装 QQ：

```sh
root@ykla:/ # cd /compat/linux/
root@ykla:/compat/linux # rpm2cpio < /home/ykla/QQ_3.2.17_250521_x86_64_01.rpm | cpio -id # 注意把 QQ 所在路径改成你自己的
./usr/share/icons/hicolor/512x512/apps/qq.png: Cannot extract through symlink usr/share/icons/hicolor/512x512/apps/qq.png
1055863 blocks
```

### 解决依赖库

- 查看依赖：

```sh
# /compat/linux/usr/bin/bash # 切换到兼容层的 shell
bash-5.1# ldd /opt/QQ/qq 
	linux-vdso.so.1 (0x00007fffffffe000)
	libffmpeg.so => /opt/QQ/libffmpeg.so (0x000000080c000000)
	....省略一部分...
```

可以看到 `ldd` 正常，无需解决依赖问题。

### 解决 fcitx 中文输入法在 QQ 中不能使用的问题

- 在兼容层中安装 `ibus-gtk3` 和 `ibus-libs`，下载后执行：

```
# fetch https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/i/ibus-gtk3-1.5.25-6.el9.x86_64.rpm
# fetch https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/i/ibus-libs-1.5.25-6.el9.x86_64.rpm
# cd /compat/linux 
# rpm2cpio < /home/ykla/ibus-gtk3-1.5.25-6.el9.x86_64.rpm | cpio -id
# rpm2cpio < /home/ykla/ibus-libs-1.5.25-6.el9.x86_64.rpm | cpio -id
```

- 接下来：

```sh
root@ykla:/compat/linux #  /compat/linux/usr/bin/bash # 切换到 Rockylinux 的 bash
bash-5.1# gtk-query-immodules-3.0-64 --update-cache   # 刷新缓存
```


### 启动 QQ

```sh
$ /compat/linux/opt/QQ/qq --no-sandbox  --in-process-gpu
```

>**注意**
>
>此处请务必以普通用户权限运行 QQ，否则可能无法使用输入法。

>**技巧**
>
>`--no-sandbox` 选项是关闭沙盒以允许 root 用户运行 QQ。
>
>`--in-process-gpu` 选项也是必要的，否则你退出 QQ 后就打不开了，除非重启。

![FreeBSD QQ](../.gitbook/assets/rlqq.png)

fcitx5 输入法正常：

![FreeBSD QQ](../.gitbook/assets/rlqq2.png)

## 基于 ArchLinux 兼容层

请看 Linux 兼容层的 ArchLinux 兼容层部分。  

```sh
# 自行将脚本创建为 arch.sh，请参看兼容层相关章节。
# sh arch.sh #运行脚本
# chroot /compat/arch/ /bin/bash #进入 Arch 兼容层
# passwd #为 Arch 的 root 设置一个密码
# passwd test #为 Arch 的 test 设置一个密码，上述脚本已经创建过该用户了！不设置密码无法正常使用 aur。

```

新开一个终端，输入 `reboot` 重启 FreeBSD，否则设置的密码可能会不识别。

```sh
# chroot /compat/arch/ /bin/bash #进入 Arch 兼容层
# su test # 此时位于 Arch 兼容层！切换到普通用户才能使用 aur
$ yay -S linuxqq # 此时位于 Arch 兼容层！此时用户为 test
$ exit # 此时位于 Arch 兼容层！退回到 root 用户
# # 此时位于 Arch 兼容层！此时用户恢复为 root
```

启动 QQ：

```sh
# /opt/QQ/qq --no-sandbox --in-process-gpu  # 此时位于 Arch 兼容层！
```

>**注意**
>
>此处你必须以 root 权限运行 QQ，否则会报错找不到 X11。

![FreeBSD QQ](../.gitbook/assets/rlqq3.png)

![FreeBSD QQ](../.gitbook/assets/rlqq4.png)

## 基于 Ubuntu 兼容层

请先构建 Ubuntu 兼容层。

```sh
# chroot /compat/ubuntu/ /bin/bash # 进入 Ubuntu 兼容层
# wget https://dldir1v6.qq.com/qqfile/qq/QQNT/Linux/QQ_3.2.18_250626_amd64_01.deb # 此时位于 Ubuntu 兼容层。下载 QQ
# apt install ./QQ*.deb  # 此时位于 Ubuntu 兼容层。安装 QQ
```

安装依赖文件：

```sh
# apt install libgbm-dev libasound2-dev #此时位于 Ubuntu 兼容层
# ldconfig # 此时位于 Ubuntu 兼容层。刷新动态链接库
```

启动 QQ：

```sh
# export LANG=zh_CN.UTF-8 #此时位于 Ubuntu 兼容层。设定环境变量
# export LC_ALL=zh_CN.UTF-8 #此时位于 Ubuntu 兼容层。设定环境变量
# /bin/qq --no-sandbox --in-process-gpu #此时位于 Ubuntu 兼容层
```

>**注意**
>
>设定环境变量是必要的，否则输入法无法正常使用。而且你必须以 root 用户运行 QQ。

![FreeBSD QQ](../.gitbook/assets/rlqq5.png)

## 故障排除

### 网络错误

如果你拥有多张网卡网卡，例如一块有线网卡、一块无线网卡。那么在打开 QQ 以后你可能会遇到网络错误的提示，此时需要给你的空闲网卡随机指派一个 IP。

参见《Linux 兼容层故障排除与未竟事宜》

### 中文输入法

>**注意**
>
>不应在兼容层内部安装输入法。这样不起任何作用。

若你自行构建兼容层，需要在启动 QQ 前，在兼容层内部，设定以下中文环境变量：

```sh
# export LANG=zh_CN.UTF-8 
# export LC_ALL=zh_CN.UTF-8 
```

如果设置失败请重启一次 FreeBSD 主机。

### QQ 闪退

在兼容层内部：

```sh
$ rm ~/.config/QQ/crash_files/*
$ chmod a-wx ~/.config/QQ/crash_files/
```

#### 参考文献

- [Linux 下新 QQ Bug＆Fix 一记（闪退相关）](https://zhuanlan.zhihu.com/p/645895811)
