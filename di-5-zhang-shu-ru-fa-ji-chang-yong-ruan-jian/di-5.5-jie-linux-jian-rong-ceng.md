# 第5.5节 Linux 兼容层

**注意：一个常见误解就是把 FreeBSD 的 Linux 兼容层当做 Wine，认为这样做会降低软件的运行效率。实际情况是不仅不会慢，而且有些软件的运行速度还会比在 Linux 中更快，运行效率更高。因为他不是模拟器，也不是转译，而是 Linux ABI 实现。**

## CentOS 兼容层（原生）

### 安装基本系统

```
# sysrc linux_enable="YES"
# sysrc kld_list+="linux linux64"
# kldload linux64
# pkg install emulators/linux-c7 dbus
# service linux start
# sysrc dbus_enable="YES" #一般桌面已经配置
# service dbus start #一般桌面已经配置
# dbus-uuidgen > /compat/linux/etc/machine-id
# reboot
```

### 配置 fstab

以下写入 `/etc/fstab`:

```
linprocfs   /compat/linux/proc	linprocfs	rw	0	0
linsysfs    /compat/linux/sys	linsysfs	rw	0	0
tmpfs    /compat/linux/dev/shm	tmpfs	rw,mode=1777	0	0
```

检查挂载有无报错：

```
# mount -al
```

```
# reboot
```

## Ubuntu 兼容层

<figure><img src="../.gitbook/assets/UbuntuonBSD.png" alt=""><figcaption></figcaption></figure>

> **以下教程仅在 FreeBSD 13.1-release 测试通过。构建的是 Ubuntu 22.04 LTS（18.04\20.04 亦可）。兼容层使用技术实际上是 Linux jail，并非 chroot。**
>
> 类似的方法可以构建 Debian 兼容层。

**需要先配置好原生的 CentOS 兼容层。**

**更多其他系统请看`/usr/local/share/debootstrap/scripts/`**


### 开始构建

```
# pkg install debootstrap
# chmod 0755 /usr/local/sbin/debootstrap # 见 https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=268205
# debootstrap jammy /compat/ubuntu http://mirrors.ustc.edu.cn/ubuntu/
# reboot
```

### 挂载文件系统

将 `nullfs_load="YES"` 写入 `/boot/loader.conf`。

将以下行写入 `/etc/fstab`：

```
# Device        Mountpoint              FStype          Options                      Dump    Pass#
devfs           /compat/ubuntu/dev      devfs           rw,late                      0       0
tmpfs           /compat/ubuntu/dev/shm  tmpfs           rw,late,size=1g,mode=1777    0       0
fdescfs         /compat/ubuntu/dev/fd   fdescfs         rw,late,linrdlnk             0       0
linprocfs       /compat/ubuntu/proc     linprocfs       rw,late                      0       0
linsysfs        /compat/ubuntu/sys      linsysfs        rw,late                      0       0
/tmp            /compat/ubuntu/tmp      nullfs          rw,late                      0       0
/home           /compat/ubuntu/home     nullfs          rw,late                      0       0
```

检查挂载有无报错：

```
# mount -al
```

如果提示没有 home 文件夹，请新建之:

```
# mkdir /compat/ubuntu/home
```

重启：

```
# reboot
```

### 进入 Ubuntu 兼容层

首先 chroot 进去 Ubuntu，移除会报错的软件：

```
# chroot /compat/ubuntu /bin/bash 
# apt remove rsyslog # 此时已经位于 Ubuntu 兼容层了。
```

### 换源

在卸载 rsyslog 之后，换源，由于 SSL 证书没有更新，所以还不能用 https 源：

```
# ee /compat/ubuntu/etc/apt/sources.list #此时处于 FreeBSD 系统！因为 Ubuntu 兼容层还没有文本编辑器。
```

写入：

```
deb http://mirrors.ustc.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
```

进入 Ubuntu 兼容层，开始更新系统，安装常用软件：

```
# LANG=C #设定字符集，防止错误
# apt update && apt upgrade && apt install nano wget # 此时已经位于 Ubuntu 兼容层了。
```

安装 Windows 11 字体【可选。自制包，打包同时兼容与低版本 Ubuntu】

```
apt install git
git clone https://github.com/ykla/ttf-mswin11-zh-deb
cd ttf-mswin11-zh-deb
dpkg -i ttf-ms-win11-*.deb
```

### 运行 X11 软件

```
# xhost +local：#此时处于 FreeBSD 系统！
```

#### 不知道程序的命令行启动命令是什么？

请按以下方法依次查找(以 `gedit` 为例)：

* 直接执行软件包名 `# gedit`；
* `whereis 软件包名`，定位后执行。`whereis gedit`；
* 通过软件图标定位，找到路径 `/usr/share/applications`,根据软件包名找到软件，用文本编辑器（如 `ee`、`nano`）打开。（软件图标本质上是一个文本文件，不是软连接或者图片），找到程序运行的命令复制到终端运行即可；
* 通过 `find` 命令全局查找 `# find / —name 软件包名`，`# find / —name gedit`。

> 如何查找软件？
>
> ```
> #apt search --names-only XXX
> ```
>
> 把 XXX 换成想要搜索的软件名即可。

#### 缺失 .so 文件

* 首先看看缺失哪些 .so 文件，一般不会只缺失一个。

```
root@ykla:/# ldd /usr/bin/qq 
	linux_vdso.so.1 (0x00007ffffffff000)
	libffmpeg.so => not found
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x0000000801061000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x0000000801066000)
…………………………以下省略……………………………………
```

可以看到 `libffmpeg.so => not found`，缺“libffmpeg.so”。

* 安装工具

```
# apt install apt-file
# apt-file update
```

* 查看 `libffmpeg.so` 属于哪个包：

```
root@ykla:/# apt-file search libffmpeg.so
qmmp: /usr/lib/qmmp/plugins/Input/libffmpeg.so
webcamoid-plugins: /usr/lib/x86_64-linux-gnu/avkys/submodules/MultiSink/libffmpeg.so
webcamoid-plugins: /usr/lib/x86_64-linux-gnu/avkys/submodules/MultiSrc/libffmpeg.so
webcamoid-plugins: /usr/lib/x86_64-linux-gnu/avkys/submodules/VideoCapture/libffmpeg.so
root@ykla:/# 
```

可以看到多个包都提供了这个 so 文件，随便安装一个：

```
# apt install webcamoid-plugins
```

* 按照上述路径复制文件，并刷新 ldd 缓存：

```
# cp  /usr/lib/x86_64-linux-gnu/avkys/submodules/MultiSink/libffmpeg.so /usr/lib #复制到系统的 lib 中
# ldconfig
```

* 查看：

```
root@ykla:/# ldd /usr/bin/qq 
	linux_vdso.so.1 (0x00007ffffffff000)
	libffmpeg.so => /lib/libffmpeg.so (0x0000000801063000)
…………………………以下省略……………………………………
```

### 示例：运行 Chrome

```
# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb # 无需代理软件，可以直连。此时已经位于 Ubuntu 兼容层了。
# apt install ./google-chrome-stable_current_amd64.deb # 此时已经位于 Ubuntu 兼容层了。
```

```
# /usr/bin/google-chrome-stable --no-sandbox --no-zygote --in-process-gpu  # 此时已经位于 Ubuntu 兼容层了。
```

> Systemd 不可用，但可以用`server xxx start`。
>
> 导入过 [https://github.com/zq1997/deepin-wine](https://github.com/zq1997/deepin-wine) 源以安装 deepin-qq，deepin-wechat 等软件，但都提示`段错误`。所有 Wine 程序都无法正常运行。如果你能解决这个问题，请提出 issue 或者 pull。

## ArchLinux 兼容层

<figure><img src="../.gitbook/assets/Arch.jpg" alt=""><figcaption></figcaption></figure>

>注:ArchLinux 兼容层看上去占用略大于 Ubuntu 兼容层是因为后方运行的谷歌 Chrome 浏览器。

> 以下部分参考 [从现有 Linux 发行版安装 Arch Linux](https://wiki.archlinuxcn.org/wiki/%E4%BB%8E%E7%8E%B0%E6%9C%89\_Linux\_%E5%8F%91%E8%A1%8C%E7%89%88%E5%AE%89%E8%A3%85\_Arch\_Linux)。
>
> **需要先配置好原生的 CentOS 兼容层。**

由于 Linux 兼容层默认内核是 3.17，太低了。直接构建的话，Arch 兼容层会在 chroot 的时候报错 `FATAL: kernel too old`。需要把 Linux 兼容层的内核版本改为 6.0.0（或其他较高版本）才可以：

```
# echo "compat.linux.osrelease=6.0.0" >> /etc/sysctl.conf
```

即可永久生效。

### 构建基本系统

```
# cd /home/ykla
# wget http://mirrors.cqu.edu.cn/archlinux/iso/2023.01.01/archlinux-bootstrap-x86_64.tar.gz # 该链接为动态更新。
# tar xpvf archlinux-bootstrap-x86_64.tar.gz -C /compat --numeric-owner # 若有报错 exit 请无视之。
# mv /compat/root.x86_64 /compat/arch # 重命名 /
```

### 挂载文件系统

将 `nullfs_load="YES"` 写入 `/boot/loader.conf`。

将以下行写入`/etc/fstab`：

```
# Device        Mountpoint            FStype          Options                      Dump    Pass#
devfs           /compat/arch/dev      devfs           rw,late                      0       0
tmpfs           /compat/arch/dev/shm  tmpfs           rw,late,size=1g,mode=1777    0       0
fdescfs         /compat/arch/dev/fd   fdescfs         rw,late,linrdlnk             0       0
linprocfs       /compat/arch/proc     linprocfs       rw,late                      0       0
linsysfs        /compat/arch/sys      linsysfs        rw,late                      0       0
/tmp            /compat/arch/tmp      nullfs          rw,late                      0       0
/home           /compat/arch/home     nullfs          rw,late                      0       0
```

检查挂载有无报错：

```
# mount -al
```

如果提示没有 home 文件夹，请新建之:

```
# mkdir /compat/arch/home
```

重启：

```
# reboot
```

### 基本配置

#### 初始化 pacman 密匙环

```
# cp /etc/resolv.conf /compat/arch/etc/ # 此时位于 FreeBSD！复制 DNS 解析。
# chroot /compat/arch /bin/bash # 此时已经是 Arch 兼容层了！
# pacman-key --init
# pacman-key --populate archlinux
```

#### 换源

由于新安装的 Arch 没有任何文本管理器，所以我们需要在 FreeBSD 中编辑相关文件：

```
# ee /compat/arch/etc/pacman.d/mirrorlist # 此时位于 FreeBSD！将下行添加至文件顶部。

Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch
```

安装一些基本软件:

```
# pacman -S base base-devel nano yay wqy-zenhei
```

#### archlinuxcn 源配置

```
# nano /etc/pacman.conf # 将下两行添加至文件底部。

[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
```
导入密钥：

```
# pacman -S archlinuxcn-keyring
```
**提示：若卡在 `Locally signing trusted keys in keyring` 超过五分钟，就 `ctrl`+`c` 中断了重来。**

由于 yay 及类似安装 aur 的软件均禁止直接 root，故需要在 chroot 中创建一个普通权限的用户（经测试 FreeBSD 中原有的普通用户不可用）：

```
# useradd -G wheel -m test
```

编辑 sudo 配置文件（若有红色警告请无视之）：

```
# nano /etc/sudoers

将 `%wheel ALL=(ALL) ALL` 前面的 `#` 删掉。
将 `%sudo ALL=(ALL:ALL) ALL` 前面的 `#` 删掉。
```

卸载 fakeroot 更改为 fakeroot-tcp，否则无法使用 aur：

> 该 Bug 见 <https://archlinuxarm.org/forum/viewtopic.php?t=14466>

```
# pacman -S fakeroot-tcp #会询问是否卸载 fakeroot，请确认并卸载。
```

#### 区域设置

> **提示：如果不设置则无法在 ArchLinux 的图形化程序中使用中文输入法。**

编辑 `/etc/locale.gen`，把 `zh_CN.UTF-8 UTF-8` 前面的注释 `#` 删掉。

重新生成区域文件：

```
# locale-gen
```

## Gentoo Linux 兼容层（portage 尚不可用）


```
# wget https://mirrors.ustc.edu.cn/gentoo/releases/amd64/autobuilds/20230101T164658Z/stage3-amd64-openrc-20230101T164658Z.tar.xz
# mkdir -p /compat/gentoo
# tar xpvf stage3-amd64-openrc-20230101T164658Z.tar.xz -C /compat/gentoo --numeric-owner
```

编辑 `ee /etc/fstab`，加入：

```
# Device        Mountpoint              FStype          Options                      Dump    Pass#
devfs           /compat/gentoo/dev      devfs           rw,late                      0       0
tmpfs           /compat/gentoo/dev/shm  tmpfs           rw,late,size=1g,mode=1777    0       0
fdescfs         /compat/gentoo/dev/fd   fdescfs         rw,late,linrdlnk             0       0
linprocfs       /compat/gentoo/proc     linprocfs       rw,late                      0       0
linsysfs        /compat/gentoo/sys      linsysfs        rw,late                      0       0
/tmp            /compat/gentoo/tmp      nullfs          rw,late                      0       0
/home           /compat/gentoo/home     nullfs          rw,late                      0       0
```

编辑：

`ee /compat/gentoo/etc/portage/make.conf`

加入：

```
MAKEOPTS="-j2"
GENTOO_MIRRORS="https://mirrors.ustc.edu.cn/gentoo"
```

进行常见配置：

```
# mkdir -p /compat/gentoo/etc/portage/repos.conf # 此时位于 FreeBSD！
# cp /compat/gentoo/usr/share/portage/config/repos.conf /compat/gentoo/etc/portage/repos.conf/gentoo.conf # 此时位于 FreeBSD！
# cp /etc/resolv.conf /compat/gentoo/etc/ # 此时位于 FreeBSD！复制 DNS 解析。
```

### 换源

```
# ee /compat/gentoo/etc/portage/repos.conf/gentoo.conf # 此处位于 FreeBSD！
```

把`sync-uri = rsync://rsync.gentoo.org/gentoo-portage` 修改为 `sync-uri = rsync://mirrors.163.com/gentoo-portage`

```
# chroot /compat/gentoo /bin/bash # 此处位于 Gentoo!
```

获取 Gentoo ebuild 数据库快照

```
# emerge --sync # 请无视 `Cannot change mode to rwxr-xr-x: Bad file descriptor` 权限错误。此处位于 Gentoo!
# chmod -R 755 /var/db/repos/gentoo #修正权限。此处位于 Gentoo!
# export FEATURES="-ipc-sandbox -mount-sandbox -network-sandbox -pid-sandbox -sandbox -usersandbox -xattr" # 禁用 jail 不支持的标志。此处位于 Gentoo!
```

测试安装 screenfetch：

```
ykla / # emerge --ask screenfetch
setlocale: unsupported locale setting
setlocale: unsupported locale setting

 * IMPORTANT: 10 news items need reading for repository 'gentoo'.
 * Use eselect news read to view new items.


These are the packages that would be merged, in order:

Calculating dependencies... done!
[ebuild  N     ] app-misc/screenfetch-3.9.1  USE="-X -curl" 

Would you like to merge these packages? [Yes/No] y

>>> Verifying ebuild manifests

>>> Emerging (1 of 1) app-misc/screenfetch-3.9.1::gentoo
 * screenfetch-3.9.1.tar.gz BLAKE2B SHA512 size ;-) ...                                                      [ ok ]
>>> Unpacking source...
>>> Unpacking screenfetch-3.9.1.tar.gz to /var/tmp/portage/app-misc/screenfetch-3.9.1/work
>>> Source unpacked in /var/tmp/portage/app-misc/screenfetch-3.9.1/work
>>> Preparing source in /var/tmp/portage/app-misc/screenfetch-3.9.1/work/screenFetch-3.9.1 ...
>>> Source prepared.
>>> Configuring source in /var/tmp/portage/app-misc/screenfetch-3.9.1/work/screenFetch-3.9.1 ...
>>> Source configured.
>>> Compiling source in /var/tmp/portage/app-misc/screenfetch-3.9.1/work/screenFetch-3.9.1 ...
>>> Source compiled.
>>> Test phase [not enabled]: app-misc/screenfetch-3.9.1

>>> Install app-misc/screenfetch-3.9.1 into /var/tmp/portage/app-misc/screenfetch-3.9.1/image
>>> Completed installing app-misc/screenfetch-3.9.1 into /var/tmp/portage/app-misc/screenfetch-3.9.1/image

 * Final size of build directory: 166 KiB
 * Final size of installed tree:    5 KiB

mkfifo: cannot set permissions of '/var/tmp/portage/app-misc/screenfetch-3.9.1/temp/multijob.rbwYPC': Bad file descriptor
 * ERROR: app-misc/screenfetch-3.9.1::gentoo failed:
 *   (no error message)
 * 
 * If you need support, post the output of `emerge --info '=app-misc/screenfetch-3.9.1::gentoo'`,
 * the complete build log and the output of `emerge -pqv '=app-misc/screenfetch-3.9.1::gentoo'`.
 * The complete build log is located at '/var/tmp/portage/app-misc/screenfetch-3.9.1/temp/build.log'.
 * The ebuild environment file is located at '/var/tmp/portage/app-misc/screenfetch-3.9.1/temp/environment'.
 * Working directory: '/var/tmp/portage/app-misc/screenfetch-3.9.1/image'
 * S: '/var/tmp/portage/app-misc/screenfetch-3.9.1/work/screenFetch-3.9.1'
!!! post install failed; exiting.

>>> Failed to emerge app-misc/screenfetch-3.9.1, Log file:

>>>  '/var/tmp/portage/app-misc/screenfetch-3.9.1/temp/build.log'

 * Messages for package app-misc/screenfetch-3.9.1:

 * ERROR: app-misc/screenfetch-3.9.1::gentoo failed:
 *   (no error message)
 * 
 * If you need support, post the output of `emerge --info '=app-misc/screenfetch-3.9.1::gentoo'`,
 * the complete build log and the output of `emerge -pqv '=app-misc/screenfetch-3.9.1::gentoo'`.
 * The complete build log is located at '/var/tmp/portage/app-misc/screenfetch-3.9.1/temp/build.log'.
 * The ebuild environment file is located at '/var/tmp/portage/app-misc/screenfetch-3.9.1/temp/environment'.
 * Working directory: '/var/tmp/portage/app-misc/screenfetch-3.9.1/image'
 * S: '/var/tmp/portage/app-misc/screenfetch-3.9.1/work/screenFetch-3.9.1'
```

测试**失败**，权限看上去还是有些问题，如果有人能解决请报告。


## 参考资料

> 其他更多可以运行的软件及方法见 [https://wiki.freebsd.org/LinuxApps](https://wiki.freebsd.org/LinuxApps)。


网站：

* [https://handbook.bsdcn.org/di-11-zhang-linux-er-jin-zhi-jian-rong-ceng/11.2.-pei-zhi-linux-er-jin-zhi-jian-rong-ceng.html](https://handbook.bsdcn.org/di-11-zhang-linux-er-jin-zhi-jian-rong-ceng/11.2.-pei-zhi-linux-er-jin-zhi-jian-rong-ceng.html)
* [https://www.freebsd.org/cgi/man.cgi?linux](https://www.freebsd.org/cgi/man.cgi?linux)
* [https://wiki.freebsd.org/LinuxJails](https://wiki.freebsd.org/LinuxJails)
* [https://handbook.bsdcn.org/di-11-zhang-linux-er-jin-zhi-jian-rong-ceng/11.4.-shi-yong-debootstrap8-gou-jian-debian-ubuntu-ji-ben-xi-tong.html](https://handbook.bsdcn.org/di-11-zhang-linux-er-jin-zhi-jian-rong-ceng/11.4.-shi-yong-debootstrap8-gou-jian-debian-ubuntu-ji-ben-xi-tong.html)
