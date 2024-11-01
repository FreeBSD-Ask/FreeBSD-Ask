# 第 3.7 节 通过 freebsd-update 更新 FreeBSD


> **前排提示**
>
> 阿里云云服务器用户升级到 13.x 请看第 2.1 节 “使用 virtio 技术半虚拟化的虚拟机” 部分。

> **注意：**
>
> 只有一级架构的 release 版本才提供该源。也就是说 current 和 stable 是没有的。 关于架构的支持等级说明请看： [https://www.freebsd.org/platforms](https://www.freebsd.org/platforms)
>
> 在 FreeBSD 15 的开发计划中，预计将使用 `pkgbase` 替代 `freebsd-update`。



## 更新 EFI 引导

>**警告**
>
>对于通过 EFI 引导的系统，EFI 系统分区（ESP）上有一个/多个引导加载程序的副本，用于固件来引导内核。如果根文件系统是 ZFS，则引导加载程序必须得支持读取 ZFS 引导文件系统。在系统升级后，且执行 `zpool upgrade` 前，必须更新 ESP 上的引导加载程序，否则系统可能无法引导。虽然不是强制性的，但在 UFS 作为根文件系统时亦应如此。可以使用命令 `efibootmgr -v` 来确定当前引导加载程序的位置。`BootCurrent` 显示的值是用于引导系统的当前引导配置的编号。输出的相应条目以 `+` 号开头，例如
>
>```
>+Boot0000* FreeBSD HD(1,GPT,f859c46d-19ee-4e40-8975-3ad1ab00ac09,0x800,0x82000)/File(\EFI\freebsd\loader.efi) nda0p1:/EFI/freebsd/loader.efi (null)
>```
>
>ESP 可能已经挂载到了 **/boot/efi**。如果没有，可以手动挂载分区，使用 `efibootmgr` 输出中列出的分区（本例为 `nda0p1`）：`mount_msdosfs /dev/nda0p1 /boot/efi`。有关另一则示例，请参阅 [ loader.efi(8)  ](https://man.freebsd.org/cgi/man.cgi?query=loader.efi&sektion=8&format=html)。
>
>在 `efibootmgr -v` 输出的 `File` 字段中的值，例如 `\EFI\freebsd\loader.efi`，是 EFI 上正在使用的引导加载程序的位置。如果挂载点是 **/boot/efi**，则此文件将变成为 `/boot/efi/efi/freebsd/loader.efi`。 （在 FAT32 文件系统上大小写不敏感；FreeBSD 使用小写）`File` 的另一个常见值可能是 `\EFI\boot\bootXXX.efi`，其中 `XXX` 是 amd64（即 `x64`）、aarch64（即 `aa64`）或 riscv64（即 `riscv64`）；如未配置，则为默认引导加载程序。应把 **/boot/loader.efi** 复制到 **/boot/efi** 上的正确路径来更新已配置及默认的引导加载程序。

——引自 FreeBSD 14.0 发行说明，有改动。

>**注意**
>
>ZFS 相关升级请参见 ZFS 章节

## 更新系统

FreeBSD 提供了实用工具 `freebsd-update` 来安装系统更新，包括升级到大版本。

## 环境准备

- 如果是 csh（14 以下 root 默认为 csh）：
```
# setenv EDITOR /usr/bin/ee # 切换 vi 为 ee，vi 不会用
# setenv VISUAL /usr/bin/ee # 切换 vi 为 ee，vi 不会用
```

- 如果是 bash、zsh 或 sh（14 及以上 root 默认为 sh）：

```sh
# export  EDITOR=/usr/bin/ee # 切换 vi 为 ee，vi 不会用
# export  VISUAL=/usr/bin/ee # 切换 vi 为 ee，vi 不会用
```



### 常规的安全更新：

```sh
# freebsd-update fetch
```

当出现类似于下列信息时：

```sh
usrlinclude/c++/vl/trllvector usrlinclude/c++/vl/trllversion usrlinclude/c++/v1/trl/wchar.h usr/include/c++/v1/tr1/wctype.h usrlinclude/c++/vllunwind-armh
usrlinclude/c++/v1/unwind-itaniumh usrlinclude/c++/vllunwindh
usr/include/crypto/ cryptodevh usrlinclude/crypto/cbcmac.h usr/include/crypto/deflate.h usrlinclude/crypto/gfmult.h usr/include/crypto/gmac.h
usr/include/crypto/rijndael.h usrlinclude/crypto/rmd160.h usr/include/crypto/xform.h
usr/include/crypto/xformauth.h usr/includecrypto/xformcomp.h usrlincludelcryptolxformenc.h
usr/include/crypto/xformpoly1305.h usrlincludelsys/ cscanatomic.h usrlincludelsys/ cscanbus.h usr/lib/clang/11.0.1
usr/lib/clang/11.0.1/include
:
```

你只需要输入`q`回车即可。然后：

```sh
# freebsd-update install
```

### 小版本或者大版本更新

> 例如 `13.2` 是要更新到的版本号：

```sh
# freebsd-update upgrade -r 13.2-RELEASE
```

**以 FreeBSD 13.1-RELEASE 升级 13.2-RELEASE 为例，设备为 i5-3230M 双核，内存 4G（以下均以此为基准）**

当出现类似于下列信息时：

```sh
root@ykla:/home/ykla # freebsd-update upgrade -r 13.2-RELEASE
src component not installed, skipped
Looking up update.FreeBSD.cn mirrors... none found.
Fetching public key from update.FreeBSD.cn... done.
Fetching metadata signature for 13.1-RELEASE from update.FreeBSD.cn... done.  #这里我使用了 FreeBSD.cn 镜像站，其实换不换这个源速度都差不多，因为都是零碎文件，如果你更新错误，建议换源看看
Fetching metadata index... done.
Fetching 2 metadata files... done.
Inspecting system... done.

The following components of FreeBSD seem to be installed:
kernel/generic kernel/generic-dbg world/base world/lib32

The following components of FreeBSD do not seem to be installed:
world/base-dbg world/lib32-dbg

Does this look reasonable (y/n)? y  #在这里输入 y 回车即可，在检查基本组件的安装情况。

Fetching metadata signature for 13.2-RELEASE from update.FreeBSD.cn... done.
Fetching metadata index... done.
Fetching 1 metadata patches. done.
Applying metadata patches... done.
Fetching 1 metadata files... done.
Inspecting system...    #这里在检查系统，需要等待约 10 分钟。
Fetching files from 13.1-RELEASE for merging... done.
Preparing to download files...    #这里在准备要下载的文件，需要等待约 15 分钟。
Fetching 5614   #这里需要等待约 3 分钟。注意，当跨版本更新时，有时候需要等待 5 小时会更长时间，都是正常的。
patches.....10....20....30....40....50....60....70....80....90....100....110....120....130....140....150....160....170....180....190....200....210....220....230....240....250....260....270....280....290....300....310....320....330....340....350....360....370....380....390....400....

…………以下省略………………

....5260....5270....5280....5290....5300....5310....5320....5330....5340....5350....5360....5370....5380....5390....5400....5410....5420....5430....5440....5450....5460....5470....5480....5490....5500....5510....5520....5530....5540....5550....5560....5570....5580....5590....5600....5610.. done.
Applying patches...    #应用补丁，需要等待约 10 分钟
Applying patches... done.
Fetching 494 files... ....10....20....30....40....50....60....70....80....90....100....110....120....130....140....150....160....170....180....190....200....210....220....230....240....250....260....270....280....290....300....310....320....330....340....350....360....370....380....390....400....410....420....430....440....450....460....470....480....490.. done.
Attempting to automatically merge changes in files... done.

The following changes, which occurred between FreeBSD 13.1-RELEASE and
FreeBSD 13.2-RELEASE have been merged into /etc/passwd:
--- current version
+++ new version
@@ -1,7 +1,5 @@
-# $FreeBSD$
-#
 root:*:0:0:Charlie &:/root:/bin/csh
 toor:*:0:0:Bourne-again Superuser:/root:
 daemon:*:1:1:Owner of many system processes:/root:/usr/sbin/nologin
 operator:*:2:5:System &:/:/usr/sbin/nologin
 bin:*:3:7:Binaries Commands and Source:/:/usr/sbin/nologin
Does this look reasonable (y/n)?  #输入 y 回车，这里在确认系统文件的变动。
The following files will be removed as part of updating to
13.2-RELEASE-p0:
/boot/kernel/iwlwifi-Qu-b0-hr-b0-68.ucode.ko
/boot/kernel/iwlwifi-Qu-b0-jf-b0-68.ucode.ko
/boot/kernel/iwlwifi-Qu-c0-hr-b0-68.ucode.ko
/boot/kernel/iwlwifi-Qu-c0-jf-b0-68.ucode.ko
/boot/kernel/iwlwifi-QuZ-a0-hr-b0-68.ucode.ko
/boot/kernel/iwlwifi-QuZ-a0-jf-b0-68.ucode.ko
/boot/kernel/iwlwifi-cc-a0-68.ucode.ko
/boot/kernel/iwlwifi-so-a0-gf-a0-68.ucode.ko
/boot/kernel/iwlwifi-so-a0-gf4-a0-68.ucode.ko
/boot/kernel/iwlwifi-so-a0-hr-b0-68.ucode.ko
/boot/kernel/iwlwifi-so-a0-jf-b0-68.ucode.ko
/boot/kernel/iwlwifi-ty-a0-gf-a0-68.ucode.ko
/usr/include/c++/v1/__function_like.h
/usr/include/c++/v1/__memory/pointer_safety.h
/usr/include/c++/v1/__utility/__decay_copy.h
/usr/lib/clang/13.0.0
/usr/lib/clang/13.0.0/include
/usr/lib/clang/13.0.0/include/__clang_cuda_builtin_vars.h
/usr/lib/clang/13.0.0/include/__clang_cuda_cmath.h
/usr/lib/clang/13.0.0/include/__clang_cuda_complex_builtins.h
/usr/lib/clang/13.0.0/include/__clang_cuda_device_functions.h
/usr/lib/clang/13.0.0/include/__clang_cuda_intrinsics.h
/usr/lib/clang/13.0.0/include/__clang_cuda_libdevice_declares.h
/usr/lib/clang/13.0.0/include/__clang_cuda_math.h
/usr/lib/clang/13.0.0/include/__clang_cuda_math_forward_declares.h
/usr/lib/clang/13.0.0/include/__clang_cuda_runtime_wrapper.h
/usr/lib/clang/13.0.0/include/__clang_hip_cmath.h
/usr/lib/clang/13.0.0/include/__clang_hip_libdevice_declares.h
/usr/lib/clang/13.0.0/include/__clang_hip_math.h
/usr/lib/clang/13.0.0/include/__clang_hip_runtime_wrapper.h
/usr/lib/clang/13.0.0/include/__stddef_max_align_t.h
/usr/lib/clang/13.0.0/include/__wmmintrin_aes.h
:   # 这里输入 q，确认变动，直至没有新内容出现
To install the downloaded upgrades, run "/usr/sbin/freebsd-update install".
```

运行 `freebsd-update install` 以安装更新：

```sh
root@ykla:/home/ykla # freebsd-update install
src component not installed, skipped
Creating snapshot of existing boot environment... done.
Installing updates...
Kernel updates have been installed.  Please reboot and run
"/usr/sbin/freebsd-update install" again to finish installing updates.
```

内核更新已经安装，系统要求重启后再运行 `freebsd-update install`。

```sh
root@ykla:/home/ykla # reboot
```

```sh
root@ykla:/home/ykla # freebsd-update install
src component not installed, skipped
Creating snapshot of existing boot environment... done.
Installing updates...Scanning //usr/share/certs/blacklisted for certificates... #需要等待约 15 分钟
Scanning //usr/share/certs/trusted for certificates...
Scanning //usr/local/share/certs for certificates...
 done.
```

检查第三方软件 ABI 变化：

```sh
root@ykla:/home/ykla # pkg upgrade
Updating FreeBSD repository catalogue...
FreeBSD repository is up to date.
All repositories are up to date.
Checking for upgrades (28 candidates): 100%
Processing candidates (28 candidates): 100%
The following 30 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
	gstreamer1-plugins-curl: 1.20.6
	gstreamer1-plugins-openh264: 1.20.6
	openh264: 2.3.0,2

Installed packages to be UPGRADED:
	curl: 7.87.0 -> 7.88.1
	dav1d: 1.0.0_3 -> 1.1.0
	gnutls: 3.7.8_1 -> 3.7.9
	gstreamer1: 1.20.5 -> 1.20.6
	gstreamer1-plugins: 1.20.5 -> 1.20.6
	gstreamer1-plugins-a52dec: 1.20.5 -> 1.20.6
	gstreamer1-plugins-bad: 1.20.5 -> 1.20.6
	gstreamer1-plugins-dts: 1.20.5 -> 1.20.6
	gstreamer1-plugins-dvdread: 1.20.5 -> 1.20.6
	gstreamer1-plugins-good: 1.20.5 -> 1.20.6
	gstreamer1-plugins-mpg123: 1.20.5 -> 1.20.6
	gstreamer1-plugins-ogg: 1.20.5 -> 1.20.6
	gstreamer1-plugins-pango: 1.20.5 -> 1.20.6
	gstreamer1-plugins-png: 1.20.5 -> 1.20.6
	gstreamer1-plugins-resindvd: 1.20.5 -> 1.20.6
	gstreamer1-plugins-theora: 1.20.5 -> 1.20.6
	gstreamer1-plugins-ugly: 1.20.5 -> 1.20.6
	gstreamer1-plugins-vorbis: 1.20.5 -> 1.20.6
	harfbuzz: 6.0.0 -> 7.0.1
	libass: 0.17.0 -> 0.17.1
	mesa-dri: 22.3.3_2 -> 22.3.6
	mesa-libs: 22.3.3_1 -> 22.3.6
	nss: 3.87 -> 3.88.1
	openexr: 3.1.5 -> 3.1.6_1
	plasma5-systemsettings: 5.24.7 -> 5.24.7_1
	sddm: 0.19.0_7 -> 0.19.0_8
	xwayland-devel: 21.0.99.1.386 -> 21.0.99.1.439

Number of packages to be installed: 3
Number of packages to be upgraded: 27

The process will require 5 MiB more space.
32 MiB to be downloaded.

Proceed with this action? [y/N]:    #这里输入 y 回车。

…………以下省略………………
```

找不到 .so：

```sh
# pkg bootstrap -f
```

以上，更新完毕。

## **故障排除**

### **FreeBSD 升级出错，没有 ntp 用户**

终端执行命令

```sh
# pw groupadd ntpd -g 123
# pw useradd ntpd -u 123 -g ntpd -h - -d /var/db/ntp -s /usr/sbin/nologin -c "NTP Daemon"
```

## 查看 FreeBSD 版本

> **注意：**
>
> 有时候补丁不涉及内核，内核版本就不会变，用 `uname -r` 看不出来，但是用户空间版本会变。所以你可能会看到两个版本，以高的为准。

### freebsd-version 命令

查看 FreeBSD 内核版本和补丁号：

```sh
ykla@ykla:~ % freebsd-version -k
13.1-RELEASE-p3
```

查看已安装的用户空间的版本和补丁程序级别：

```sh
ykla@ykla:~ % freebsd-version -u
13.1-RELEASE-p5
```

### uname 命令

```sh
ykla@ykla:~ % uname -a
FreeBSD ykla 13.1-RELEASE FreeBSD 13.1-RELEASE releng/13.1-n250148-fc952ac2212 GENERIC amd64
```

```sh
ykla@ykla:~ % uname -mrs
FreeBSD 13.1-RELEASE amd64
```


### 升级后 pkg 无法使用，或任何软件找不到 .so

```sh
# pkg bootstrap -f
```

或者使用 ports `make deinstall` 卸载 pkg 重装。



