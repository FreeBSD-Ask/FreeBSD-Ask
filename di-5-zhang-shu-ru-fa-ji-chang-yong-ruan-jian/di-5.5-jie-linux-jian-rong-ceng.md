# 第5.5节 Linux 兼容层

**注意：一个常见误解就是把 FreeBSD 的 Linux 兼容层当做 Wine，认为这样做会降低软件的运行效率。实际情况是不仅不会慢，而且有些软件的运行速度还会比在 Linux 中更快，运行效率更高。因为他不是模拟器。**

## 系统自带

以下参考

<https://handbook.bsdcn.org/di-11-zhang-linux-er-jin-zhi-jian-rong-ceng/11.2.-pei-zhi-linux-er-jin-zhi-jian-rong-ceng.html>

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

检查挂载有无报错：

```
# mount -al
```

```
# reboot
```

## 自己构建 Ubuntu 兼容层

> **以下教程仅在 FreeBSD 13.0 测试通过。构建的是 Ubuntu 22.04 LTS（18.04\20.04 亦可）。兼容层使用技术实际上是 Linux jail，并非 chroot。**

**需要先按照“系统自带”的方法配置好原生的 CentOS 兼容层。**

**更多其他系统请看`/usr/local/share/debootstrap/scripts/`**

将`nullfs_load="YES"`写入`/boot/loader.conf`

### 开始构建

```
# pkg install debootstrap
# chmod 0755 /usr/local/sbin/debootstrap # 见 https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=268205
# debootstrap jammy /compat/ubuntu http://mirrors.163.com/ubuntu/
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

如果提示没有 home 文件夹，请新建:

```
# mkdir /compat/ubuntu/home
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
deb http://mirrors.163.com/ubuntu/ jammy main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ jammy main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ jammy-updates main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ jammy-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ jammy-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ jammy-backports main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ jammy-security main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ jammy-security main restricted universe multiverse
```

进入 Ubuntu 兼容层，开始更新系统，安装常用软件：

```
# LANG=C #设定字符集，防止错误
# apt update && apt upgrade && apt install nano wget # 此时已经位于 Ubuntu 兼容层了。
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

*首先看看缺失哪些 .so 文件，一般不会只缺失一个。

```
root@ykla:/# ldd /usr/bin/qq 
	linux_vdso.so.1 (0x00007ffffffff000)
	libffmpeg.so => not found
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x0000000801061000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x0000000801066000)
	libglib-2.0.so.0 => /lib/x86_64-linux-gnu/libglib-2.0.so.0 (0x000000080106b000)
	libgobject-2.0.so.0 => /lib/x86_64-linux-gnu/libgobject-2.0.so.0 (0x000000080a5b9000)
	libgio-2.0.so.0 => /lib/x86_64-linux-gnu/libgio-2.0.so.0 (0x000000080a619000)
	libnss3.so => /lib/x86_64-linux-gnu/libnss3.so (0x000000080a7f1000)
	libnssutil3.so => /lib/x86_64-linux-gnu/libnssutil3.so (0x00000008011a7000)
	libsmime3.so => /lib/x86_64-linux-gnu/libsmime3.so (0x000000080a91e000)
	libnspr4.so => /lib/x86_64-linux-gnu/libnspr4.so (0x000000080a948000)
	libatk-1.0.so.0 => /lib/x86_64-linux-gnu/libatk-1.0.so.0 (0x000000080a988000)
	libatk-bridge-2.0.so.0 => /lib/x86_64-linux-gnu/libatk-bridge-2.0.so.0 (0x000000080a9b2000)
	libcups.so.2 => /lib/x86_64-linux-gnu/libcups.so.2 (0x000000080a9ea000)
	libdbus-1.so.3 => /lib/x86_64-linux-gnu/libdbus-1.so.3 (0x000000080aa88000)
	libdrm.so.2 => /lib/x86_64-linux-gnu/libdrm.so.2 (0x00000008011db000)
	libgtk-3.so.0 => /lib/x86_64-linux-gnu/libgtk-3.so.0 (0x000000080ac00000)
	libpango-1.0.so.0 => /lib/x86_64-linux-gnu/libpango-1.0.so.0 (0x000000080aad6000)
	libcairo.so.2 => /lib/x86_64-linux-gnu/libcairo.so.2 (0x000000080b429000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x000000080b551000)
	libX11.so.6 => /lib/x86_64-linux-gnu/libX11.so.6 (0x000000080b638000)
	libXcomposite.so.1 => /lib/x86_64-linux-gnu/libXcomposite.so.1 (0x00000008011f3000)
	libXdamage.so.1 => /lib/x86_64-linux-gnu/libXdamage.so.1 (0x00000008011f8000)
	libXext.so.6 => /lib/x86_64-linux-gnu/libXext.so.6 (0x000000080ab3d000)
	libXfixes.so.3 => /lib/x86_64-linux-gnu/libXfixes.so.3 (0x000000080ab52000)
	libXrandr.so.2 => /lib/x86_64-linux-gnu/libXrandr.so.2 (0x000000080ab5a000)
	libgbm.so.1 => /lib/x86_64-linux-gnu/libgbm.so.1 (0x000000080ab67000)
	libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1 (0x000000080ab78000)
	libxcb.so.1 => /lib/x86_64-linux-gnu/libxcb.so.1 (0x000000080aba9000)
	libxkbcommon.so.0 => /lib/x86_64-linux-gnu/libxkbcommon.so.0 (0x000000080b778000)
	libasound.so.2 => /lib/x86_64-linux-gnu/libasound.so.2 (0x000000080b7bf000)
	libatspi.so.0 => /lib/x86_64-linux-gnu/libatspi.so.0 (0x000000080b8c2000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x000000080abd5000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x000000080ba00000)
	/lib64/ld-linux-x86-64.so.2 (0x0000000001021000)
	libpcre.so.3 => /lib/x86_64-linux-gnu/libpcre.so.3 (0x000000080b8fc000)
	libffi.so.8 => /lib/x86_64-linux-gnu/libffi.so.8 (0x000000080b972000)
	libgmodule-2.0.so.0 => /lib/x86_64-linux-gnu/libgmodule-2.0.so.0 (0x000000080abf7000)
	libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x000000080b97f000)
	libmount.so.1 => /lib/x86_64-linux-gnu/libmount.so.1 (0x000000080b99b000)
	libselinux.so.1 => /lib/x86_64-linux-gnu/libselinux.so.1 (0x000000080bc28000)
	libplc4.so => /lib/x86_64-linux-gnu/libplc4.so (0x000000080b9df000)
	libplds4.so => /lib/x86_64-linux-gnu/libplds4.so (0x000000080b9e6000)
	libgssapi_krb5.so.2 => /lib/x86_64-linux-gnu/libgssapi_krb5.so.2 (0x000000080bc54000)
	libavahi-common.so.3 => /lib/x86_64-linux-gnu/libavahi-common.so.3 (0x000000080b9eb000)
	libavahi-client.so.3 => /lib/x86_64-linux-gnu/libavahi-client.so.3 (0x000000080bca8000)
	libgnutls.so.30 => /lib/x86_64-linux-gnu/libgnutls.so.30 (0x000000080bcbc000)
	libsystemd.so.0 => /lib/x86_64-linux-gnu/libsystemd.so.0 (0x000000080bea7000)
	libgdk-3.so.0 => /lib/x86_64-linux-gnu/libgdk-3.so.0 (0x000000080bf6e000)
	libpangocairo-1.0.so.0 => /lib/x86_64-linux-gnu/libpangocairo-1.0.so.0 (0x000000080c075000)
	libXi.so.6 => /lib/x86_64-linux-gnu/libXi.so.6 (0x000000080c087000)
	libcairo-gobject.so.2 => /lib/x86_64-linux-gnu/libcairo-gobject.so.2 (0x000000080c09b000)
	libgdk_pixbuf-2.0.so.0 => /lib/x86_64-linux-gnu/libgdk_pixbuf-2.0.so.0 (0x000000080c0a7000)
	libepoxy.so.0 => /lib/x86_64-linux-gnu/libepoxy.so.0 (0x000000080c0d7000)
	libfribidi.so.0 => /lib/x86_64-linux-gnu/libfribidi.so.0 (0x000000080c20c000)
	libpangoft2-1.0.so.0 => /lib/x86_64-linux-gnu/libpangoft2-1.0.so.0 (0x000000080c228000)
	libharfbuzz.so.0 => /lib/x86_64-linux-gnu/libharfbuzz.so.0 (0x000000080c243000)
	libfontconfig.so.1 => /lib/x86_64-linux-gnu/libfontconfig.so.1 (0x000000080c312000)
	libthai.so.0 => /lib/x86_64-linux-gnu/libthai.so.0 (0x000000080c35c000)
	libpixman-1.so.0 => /lib/x86_64-linux-gnu/libpixman-1.so.0 (0x000000080c367000)
	libfreetype.so.6 => /lib/x86_64-linux-gnu/libfreetype.so.6 (0x000000080c412000)
	libpng16.so.16 => /lib/x86_64-linux-gnu/libpng16.so.16 (0x000000080c4da000)
	libxcb-shm.so.0 => /lib/x86_64-linux-gnu/libxcb-shm.so.0 (0x000000080c515000)
	libxcb-render.so.0 => /lib/x86_64-linux-gnu/libxcb-render.so.0 (0x000000080c51a000)
	libXrender.so.1 => /lib/x86_64-linux-gnu/libXrender.so.1 (0x000000080c529000)
	libwayland-server.so.0 => /lib/x86_64-linux-gnu/libwayland-server.so.0 (0x000000080c538000)
	libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x000000080c600000)
	libXau.so.6 => /lib/x86_64-linux-gnu/libXau.so.6 (0x000000080c54e000)
	libXdmcp.so.6 => /lib/x86_64-linux-gnu/libXdmcp.so.6 (0x000000080c554000)
	libblkid.so.1 => /lib/x86_64-linux-gnu/libblkid.so.1 (0x000000080c55c000)
	libpcre2-8.so.0 => /lib/x86_64-linux-gnu/libpcre2-8.so.0 (0x000000080c82a000)
	libkrb5.so.3 => /lib/x86_64-linux-gnu/libkrb5.so.3 (0x000000080c8c1000)
	libk5crypto.so.3 => /lib/x86_64-linux-gnu/libk5crypto.so.3 (0x000000080c595000)
	libcom_err.so.2 => /lib/x86_64-linux-gnu/libcom_err.so.2 (0x000000080c5c4000)
	libkrb5support.so.0 => /lib/x86_64-linux-gnu/libkrb5support.so.0 (0x000000080c5ca000)
	libp11-kit.so.0 => /lib/x86_64-linux-gnu/libp11-kit.so.0 (0x000000080c98c000)
	libidn2.so.0 => /lib/x86_64-linux-gnu/libidn2.so.0 (0x000000080c5da000)
	libunistring.so.2 => /lib/x86_64-linux-gnu/libunistring.so.2 (0x000000080cac7000)
	libtasn1.so.6 => /lib/x86_64-linux-gnu/libtasn1.so.6 (0x000000080cc71000)
	libnettle.so.8 => /lib/x86_64-linux-gnu/libnettle.so.8 (0x000000080cc89000)
	libhogweed.so.6 => /lib/x86_64-linux-gnu/libhogweed.so.6 (0x000000080cccf000)
	libgmp.so.10 => /lib/x86_64-linux-gnu/libgmp.so.10 (0x000000080cd17000)
	liblzma.so.5 => /lib/x86_64-linux-gnu/liblzma.so.5 (0x000000080cd99000)
	libzstd.so.1 => /lib/x86_64-linux-gnu/libzstd.so.1 (0x000000080cdc4000)
	liblz4.so.1 => /lib/x86_64-linux-gnu/liblz4.so.1 (0x000000080ce93000)
	libcap.so.2 => /lib/x86_64-linux-gnu/libcap.so.2 (0x000000080ceb3000)
	libgcrypt.so.20 => /lib/x86_64-linux-gnu/libgcrypt.so.20 (0x000000080cebe000)
	libXinerama.so.1 => /lib/x86_64-linux-gnu/libXinerama.so.1 (0x000000080cffc000)
	libXcursor.so.1 => /lib/x86_64-linux-gnu/libXcursor.so.1 (0x000000080d001000)
	libwayland-cursor.so.0 => /lib/x86_64-linux-gnu/libwayland-cursor.so.0 (0x000000080d00d000)
	libwayland-egl.so.1 => /lib/x86_64-linux-gnu/libwayland-egl.so.1 (0x000000080d017000)
	libwayland-client.so.0 => /lib/x86_64-linux-gnu/libwayland-client.so.0 (0x000000080d01c000)
	libjpeg.so.8 => /lib/x86_64-linux-gnu/libjpeg.so.8 (0x000000080d02f000)
	libgraphite2.so.3 => /lib/x86_64-linux-gnu/libgraphite2.so.3 (0x000000080d0b0000)
	libuuid.so.1 => /lib/x86_64-linux-gnu/libuuid.so.1 (0x000000080d0d7000)
	libdatrie.so.1 => /lib/x86_64-linux-gnu/libdatrie.so.1 (0x000000080d0e0000)
	libbrotlidec.so.1 => /lib/x86_64-linux-gnu/libbrotlidec.so.1 (0x000000080d0e9000)
	libbsd.so.0 => /lib/x86_64-linux-gnu/libbsd.so.0 (0x000000080d0f9000)
	libkeyutils.so.1 => /lib/x86_64-linux-gnu/libkeyutils.so.1 (0x000000080d111000)
	libresolv.so.2 => /lib/x86_64-linux-gnu/libresolv.so.2 (0x000000080d118000)
	libgpg-error.so.0 => /lib/x86_64-linux-gnu/libgpg-error.so.0 (0x000000080d12c000)
	libbrotlicommon.so.1 => /lib/x86_64-linux-gnu/libbrotlicommon.so.1 (0x000000080d154000)
	libmd.so.0 => /lib/x86_64-linux-gnu/libmd.so.0 (0x000000080d177000)
root@ykla:/# 
```

可以看到 `libffmpeg.so => not found`，缺“libffmpeg.so”。

安装工具：

```
# apt install apt-file
# apt-file update
```

查看 `libffmpeg.so` 属于哪个包：

```
root@ykla:/# apt-file search libffmpeg.so
qmmp: /usr/lib/qmmp/plugins/Input/libffmpeg.so
webcamoid-plugins: /usr/lib/x86_64-linux-gnu/avkys/submodules/MultiSink/libffmpeg.so
webcamoid-plugins: /usr/lib/x86_64-linux-gnu/avkys/submodules/MultiSrc/libffmpeg.so
webcamoid-plugins: /usr/lib/x86_64-linux-gnu/avkys/submodules/VideoCapture/libffmpeg.so
root@ykla:/# 
```

可以看到多个包都提供了这个 so  文件，随便安装一个：

```
# apt install qmmp
```

刷新 ldd 缓存：

```
# ldconfig
```


### 示例：运行 Chrome

```
# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb # 无需代理软件，可以直连。此时已经位于 Ubuntu 兼容层了。
# apt install ./google-chrome-stable_current_amd64.deb # 此时已经位于 Ubuntu 兼容层了。
```

```
# /usr/bin/google-chrome-stable --no-sandbox --no-zygote --in-process-gpu  # 此时已经位于 Ubuntu 兼容层了。
```

> Systemd 不可用，但可以用`server xxx start`。其他更多可以运行的软件见 [https://wiki.freebsd.org/LinuxApps](https://wiki.freebsd.org/LinuxApps)。
>
> 参考文献 [https://wiki.freebsd.org/LinuxJails](https://wiki.freebsd.org/LinuxJails) 、<https://handbook.bsdcn.org/di-11-zhang-linux-er-jin-zhi-jian-rong-ceng/11.4.-shi-yong-debootstrap8-gou-jian-debian-ubuntu-ji-ben-xi-tong.html>。
>
> 类似的方法可以构建 Debian、Arch 兼容层（经测试会提示 内核太老，旧版本则强制升级无法使用）。Gentoo 兼容层则提示 bash so 文件错误，即使静态编译了 zsh。
>
> 导入过 [https://github.com/zq1997/deepin-wine](https://github.com/zq1997/deepin-wine) 源以安装 deepin-qq，deepin-wechat 等软件，但都提示段错误。所有 Wine 程序都无法正常运行。如果你能解决这个问题，请提出 issue 或者 pull。
