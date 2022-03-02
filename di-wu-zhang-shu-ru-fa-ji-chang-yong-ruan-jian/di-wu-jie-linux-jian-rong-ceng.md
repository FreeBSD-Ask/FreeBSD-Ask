# 第五节 Linux 兼容层

**注意：一个常见误解就是把 FreeBSD 的 Linux 兼容层当做 Wine，认为这样做会降低软件的运行效率。实际情况是不仅不会慢，而且速度还会比在 Linux 中更快，运行效率更高。**

## 系统自带；

以下参考

<https://handbook.freebsdcn.org/di-10-zhang-linux-er-jin-zhi-jian-rong-ceng/10.1.-gai-shu>

### 开启服务

```
# sysrc linux_enable="YES"
# sysrc kld_list+="linux linux64"
# kldload linux64
# pkg install emulators/linux-c7 dbus
# service linux start
# sysrc dbus_enable="YES"
# service dbus start
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
```
# reboot
```
## 自己构建 Ubuntu 兼容层

>**以下教程仅在 FreeBSD 13.0 测试通过。构建的是 Ubuntu 20.04 LTS。兼容层使用技术实际上是 Linux jail，并非 chroot。**

**需要先按照“系统自带”的方法配置好原生的 CentOS 兼容层。**

将`nullfs_load="YES"`写入`/boot/loader.conf`

### 开始构建

```
# pkg install debootstrap
# debootstrap focal /compat/ubuntu http://mirror.bjtu.edu.cn/ubuntu/
# reboot
```
### 挂载文件系统
将以下行写入`/etc/fstab`：
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

如果提示没有home文件夹，请新建:
```
# mkdir /home
```
### Jail

首先 chroot 进去 Ubuntu，移除会报错的软件：
```
# chroot /compat/ubuntu /bin/bash 
# apt remove rsyslog # 此时已经位于 Ubuntu 兼容层了。
```

### 换源

在卸载 rsyslog 之后，换源,由于 SSL 证书没有更新，所以还不能用 https：

```
# ee /compat/ubuntu/etc/apt/sources.list #此时处于 FreeBSD 系统！因为 Ubuntu 兼容层还没有文本编辑器。
```
写入：
```
deb http://mirror.bjtu.edu.cn/ubuntu/ focal main restricted universe multiverse
deb-src http://mirror.bjtu.edu.cn/ubuntu/ focal main restricted universe multiverse
deb http://mirror.bjtu.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirror.bjtu.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirror.bjtu.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirror.bjtu.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb http://mirror.bjtu.edu.cn/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirror.bjtu.edu.cn/ubuntu/ focal-security main restricted universe multiverse
```
进入 Ubuntu 兼容层，开始更新系统，安装常用软件：

```
# apt update && apt upgrade && apt install nano wget # 此时已经位于 Ubuntu 兼容层了。
```

### 运行 X11 软件

```
# xhost +local：#此时处于 FreeBSD 系统！
```
### 示例：运行 Chrome

```
# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb # 无需代理软件，可以直连。此时已经位于 Ubuntu 兼容层了。
# apt install ./google-chrome-stable_current_amd64.deb # 此时已经位于 Ubuntu 兼容层了。
```

```
# /usr/bin/google-chrome-stable --no-sandbox --no-zygote --in-process-gpu  # 此时已经位于 Ubuntu 兼容层了。
```

>Systemd 不可用，但可以用`server xxx start`。其他更多可以运行的软件见 <https://wiki.freebsd.org/LinuxApps> 。
>
>参考文献 <https://wiki.freebsd.org/LinuxJails> 、<https://handbook.freebsdcn.org/di-10-zhang-linux-er-jin-zhi-jian-rong-ceng/10.4.-shi-yong-debootstrap8-gou-jian-debian-ubuntu-ji-ben-xi-tong> 。
>
>类似的方法可以构建 Debian、Arch 兼容层（经测试会提示 内核太老，旧版本则强制升级无法使用）。Gentoo 兼容层则提示 bash so 文件错误，即使静态编译了 zsh。
>
>导入过 <https://github.com/zq1997/deepin-wine> 源以安装 deepin-qq，deepin-wechat 等软件，但都提示段错误。所有 Wine 程序都无法正常运行。如果你能解决这个问题，请提出 issue 或者 pull。
