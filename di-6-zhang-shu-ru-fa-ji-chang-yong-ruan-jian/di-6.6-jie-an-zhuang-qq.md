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
# exit # 此时位于 Arch 兼容层！此时用户恢复为 root
```

```sh
# export LANG=zh_CN.UTF-8 # 此时位于 Arch 兼容层！
# export LC_ALL=zh_CN.UTF-8 # 此时位于 Arch 兼容层！如果不添加环境变量，则中文输入法无法使用。如果设置失败请重启一次 FreeBSD 主机。此时位于 Arch 兼容层！
# /opt/QQ/qq --no-sandbox --in-process-gpu  # 此时位于 Arch 兼容层！
```

## 基于 Ubuntu 兼容层

请先安装 Ubuntu 兼容层。

```sh
# chroot /compat/ubuntu/ /bin/bash #进入 Ubuntu 兼容层
# wget https://dldir1.qq.com/qqfile/qq/QQNT/ad5b5393/linuxqq_3.1.2-13107_amd64.deb #此时位于 Ubuntu 兼容层
```

```sh
# apt install ./linuxqq_3.1.0-9572_amd64.deb  #此时位于 Ubuntu 兼容层
```

安装依赖文件和字体：

```sh
# apt install libgbm-dev libasound2-dev #此时位于 Ubuntu 兼容层
# ldconfig #此时位于 Ubuntu 兼容层
```

安装中文字体：用包管理器查找中文字体，例如 wqy

启动 QQ：

```sh
# export LANG=zh_CN.UTF-8 # 此时位于 Ubuntu 兼容层
# export LC_ALL=zh_CN.UTF-8 # 如果不添加则中文输入法无法使用。此时位于 Ubuntu 兼容层
# /bin/qq --no-sandbox --in-process-gpu #此时位于 Ubuntu 兼容层
```

> **注意**
>
> 如果你双网卡，例如一个有线一个无线，打开 QQ 以后可能会遇到网络错误的提示，需要给你的空闲网卡随便指派一个 IP。
>
> 参见《Linux 兼容层故障排除与未竟事宜》
>
> 如果退出后进不去，请加参数 `--in-process-gpu` 执行之即可，即 `/bin/qq  --no-sandbox --in-process-gpu`。

![FreeBSD QQ](../.gitbook/assets/qq3.0.png)

## 故障排除

### QQ 闪退

在兼容层内部：

```sh
$ rm ~/.config/QQ/crash_files/*
$ chmod a-wx ~/.config/QQ/crash_files/
```

#### 参考文献

- [Linux 下新 QQ Bug＆Fix 一记（闪退相关）](https://zhuanlan.zhihu.com/p/645895811)
