# 第5.7节 安装 QQ

## Linux QQ 3.x（electron）【可选：基于 ArchLinux 兼容层】

前文请看 Linux 兼容层的 ArchLinux 兼容层部分。

```
# chroot /compat/arch/ /bin/bash #进入 Arch兼容层
# su test # 切换到普通用户才能使用 aur，前文已经创建该用户了！
$ yay -S linuxqq # 此时用户为 test
# exit #此时用户恢复为 root
````

```
# export LANG=zh_CN.UTF-8 # 此时位于 Arch 兼容层！
# export LC_ALL=zh_CN.UTF-8 # 如果不添加则中文输入法无法使用。如果设置失败请重启一次 FreeBSD 主机。此时位于 Arch 兼容层！
# /user/bin/qq --no-sandbox --no-zygote --in-process-gpu # 此时位于 Arch 兼容层！
```

## Linux QQ 3.x（electron）【可选：基于 Ubuntu 兼容层】

> 请先安装 CentOS 兼容层及 Ubuntu 兼容层，具体请看 第五章 第五节。

```
# chroot /compat/ubuntu/ /bin/bash #进入 Ubuntu 兼容层
# wget https://dldir1.qq.com/qqfile/qq/QQNT/64bd2578/linuxqq_3.0.0-565_amd64.deb #此时位于 Ubuntu 兼容层
```

```
# apt install ./linuxqq_3.0.0-565_amd64.deb  #此时位于 Ubuntu 兼容层
```

安装依赖文件和字体：

```
# apt install libgbm-dev libasound2-dev webcamoid-plugins fonts-wqy-microhei  fonts-wqy-zenhei language-pack-zh-hans #此时位于 Ubuntu 兼容层
# cp  /usr/lib/x86_64-linux-gnu/avkys/submodules/MultiSink/libffmpeg.so /usr/lib  #此时位于 Ubuntu 兼容层
# ldconfig #此时位于 Ubuntu 兼容层
```

启动 QQ：

```
# export LANG=zh_CN.UTF-8
# export LC_ALL=zh_CN.UTF-8 # 如果不添加则中文输入法无法使用。
# /bin/qq --no-sandbox --no-zygote --in-process-gpu #此时位于 Ubuntu 兼容层
```

![](../.gitbook/assets/qq3.0.jpg)


> **注意**
>
>**如果退出后进不去，请加参数 `--in-process-gpu` 执行之即可，即 `/bin/qq --in-process-gpu`**。



## Linux QQ 2.x （GTK2.0）

### **安装 Linux 兼容层：**

> 请先安装 Linux 兼容层，具体请看 第五章 第五节。

```
# pkg install linux-c7-gtk2 linux-c7-libxkbcommon
```

### 下载 Linux QQ

```
# mkdir /home/work
# fetch https://down.qq.com/qqweb/LinuxQQ/linuxqq_2.0.0-b2-1089_x86_64.rpm
```

安装 Linux QQ：

```
# pkg install archivers/rpm4
# cd /compat/linux
# rpm2cpio < /home/work/linuxqq_2.0.0-b2-1089_x86_64.rpm | cpio -id
```

### 下载并安装 Linux QQ 所需依赖

由于未知原因，安装的 Linux QQ 无法输入，需要安装以下依赖才可以输入文字，但是只摸索了 Fcitx 输入法框架下的依赖。

```
# cd /home/work
# fetch http://mirror.centos.org/centos/7/os/x86_64/Packages/gtk2-immodule-xim-2.24.31-1.el7.x86_64.rpm
# fetch https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/f/fcitx-gtk2-4.2.9.6-1.el7.x86_64.rpm
# fetch https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/f/fcitx-4.2.9.6-1.el7.x86_64.rpm
# fetch https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/f/fcitx-libs-4.2.9.6-1.el7.x86_64.rpm
```

然后分别安装以上 4 个包：

```
# cd /compat/linux
# rpm2cpio < /home/work/gtk2-immodule-xim-2.24.31-1.el7.x86_64.rpm | cpio -id
# rpm2cpio < /home/work/fcitx-gtk2-4.2.9.6-1.el7.x86_64.rpm | cpio -id
# rpm2cpio < /home/work/fcitx-4.2.9.6-1.el7.x86_64.rpm | cpio -id
# rpm2cpio < /home/work/fcitx-libs-4.2.9.6-1.el7.x86_64.rpm | cpio -id
```

~~注意：为了方便境内 FreeBSD 用户，可以使用境内的 gitee 同步下载以上 4 个文件；~~

> 经验与教训：
>
> **请远离境内诸如 gitee 等无良企业。**

Github：

[https://github.com/ykla/FreeBSD-Linux-QQ](https://github.com/ykla/FreeBSD-Linux-QQ)

### 刷新 gtk 缓存

`# /compat/linux/usr/bin/gtk-query-immodules-2.0-64 --update-cache`

### 运行 Linux QQ

`$ /compat/linux/usr/local/bin/qq`
