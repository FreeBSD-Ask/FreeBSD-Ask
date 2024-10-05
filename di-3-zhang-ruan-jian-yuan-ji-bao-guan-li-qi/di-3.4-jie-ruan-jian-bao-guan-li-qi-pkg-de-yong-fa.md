# 第 3.4 节 软件包管理器 pkg 的用法

包管理器目前是 pkgng，其命令是 pkg。`pkg install` 可以缩写成 `pkg ins`，其他类似。

> **请注意**
>
> ~~pkg 只能管理第三方软件包，并不能起到升级系统，获取安全更新的作用。这是因为 FreeBSD 项目是把内核与用户空间作为一个整体来进行维护的，而不是像 Linux 那样 linus torvalds 负责维护内核，各个发行版的人负责维护 GNU 工具（他们这些软件实际上被设计为单个软件包，因此可以用包管理器更新与升级系统）。~~
>
>FreeBSD 现在也正[试图使用 pkg 来实现用户空间和内核的更新](https://wiki.freebsd.org/PkgBase)。解决上述问题。
>
> FreeBSD 使用 `freebsd-update` 来升级系统，获取安全补丁。<https://pkg-status.freebsd.org/> 可以查看当前的 pkg 编译状态。
>
>
> 偏好图形化的用户可以安装使用 `ports-mgmt/octopkg`，该工具是 pkg 的图形化前端，由 ghostbsd 开发。

## 如何用 pkg 安装软件

基本系统默认没有 pkg，需要先下载一下 pkg：

```sh
# pkg
```

回车即可输入 `y` 确认下载

pkg 使用 https，先安装 ssl 证书：

```sh
# pkg install ca_root_nss
```
或者

```sh
# cd /usr/ports/security/ca_root_nss/
# make install clean
```

然后把 repo.conf 里的 pkg+http 改成 pkg+https 即可。

最后刷新 pkg 数据库：

```sh
# pkg update -f
```

安装 python 3：


```sh
# pkg install python
```

或

```sh
# cd /usr/ports/lang/python/
# make install clean
```

pkg 升级：

```sh
# pkg upgrade
```

错误：`You must upgrade the ports-mgmt/pkg port first`

解决：

```sh
# cd /usr/ports/ports-mgmt/pkg
# make deinstall reinstall
```

查看已经安装的所有软件：

```sh
# pkg info
```

## 如何卸载软件

**来源请求** ~~直接使用 `pkg delete` 会破坏正常的依赖关系，应该尽量避免使用（ports 的 `make deinstall` 也一样），转而使用 `pkg-rmleaf` 命令，该命令属于的软件需要自行安装。~~ [FreeBSD 15 不再可用](https://github.com/bsdelf/pkg-rmleaf/issues/2)，同时该包已近 6 年未经维护。

```sh
# pkg install pkg-rmleaf
```

或者
```sh
# cd /usr/ports/ports-mgmt/pkg-rmleaf/
# make install clean
```

### 如何卸载所有自行安装的第三方软件？

```sh
root@ykla:~ # pkg delete -fa # 如果带上参数 f，会把 pkg 自己也删掉，因为 pkg 也是用户一开始自行安装的软件。
Checking integrity... done (0 conflicting)
Deinstallation has been requested for the following 87 packages (of 0 packages in the universe):

Installed packages to be REMOVED:
	alsa-lib: 1.2.12
	brotli: 1.1.0,1
	curl: 8.8.0
	dejavu: 2.37_3
	encodings: 1.1.0,1
	expat: 2.6.2
	font-bh-ttf: 1.0.3_5
	font-misc-ethiopic: 1.0.4
	font-misc-meltho: 1.0.3_5
	fontconfig: 2.15.0_2,1
	freetype2: 2.13.2
	gettext-runtime: 0.22.5
	giflib: 5.2.2
	git: 2.45.2_1
	glib: 2.80.3,2
	graphite2: 1.3.14
	harfbuzz: 8.5.0
	htop: 3.3.0_2
	indexinfo: 0.3.1
	javavmwrapper: 2.7.10
	jbigkit: 2.1_3
	jpeg-turbo: 3.0.3
	lcms2: 2.16_2
	lerc: 4.0.0
	libICE: 1.1.1,1
	libSM: 1.2.3_1,1
	libX11: 1.8.9,1
	libXau: 1.0.9_1
	libXdmcp: 1.1.5
	libXext: 1.3.6,1
	libXfixes: 6.0.0_1
	libXi: 1.8_1,1
	libXrandr: 1.5.2_1
	libXrender: 0.9.10_2
	libXt: 1.3.0,1
	libXtst: 1.2.3_3
	libdeflate: 1.20
	libffi: 3.4.6
	libfontenc: 1.1.8
	libiconv: 1.17_1
	libidn2: 2.3.7
	liblz4: 1.9.4_1,1
	libnghttp2: 1.62.1
	libpci: 3.12.0
	libpsl: 0.21.5_1
	libssh2: 1.11.0_1,3
	libunistring: 1.2
	libxcb: 1.17.0
	mkfontscale: 1.2.3
	mpdecimal: 4.0.0
	openjdk21: 21.0.3+9.1
	p5-Authen-SASL: 2.17
	p5-CGI: 4.66
	p5-Clone: 0.46
	p5-Digest-HMAC: 1.04
	p5-Encode-Locale: 1.05
	p5-Error: 0.17029
	p5-GSSAPI: 0.28_2
	p5-HTML-Parser: 3.82
	p5-HTML-Tagset: 3.24
	p5-HTTP-Date: 6.06
	p5-HTTP-Message: 6.46
	p5-IO-HTML: 1.004
	p5-IO-Socket-IP: 0.42
	p5-IO-Socket-SSL: 2.088
	p5-LWP-MediaTypes: 6.04
	p5-Mozilla-CA: 20240313
	p5-Net-SSLeay: 1.94
	p5-TimeDate: 2.33,1
	p5-URI: 5.28
	pciids: 20240531
	pciutils: 3.12.0
	pcre2: 10.43
	perl5: 5.36.3_1
	pkg: 1.21.3   # 如果带上参数 f，就会把 pkg 自己也删掉，因为这个 pkg 也是用户一开始自行安装的软件。
	png: 1.6.43
	py311-packaging: 24.1
	python311: 3.11.9
	readline: 8.2.10
	screen: 4.9.1_3
	tiff: 4.6.0
	usbhid-dump: 1.4
	usbids: 20240318
	usbutils: 0.91
	xorg-fonts-truetype: 7.7_1
	xorgproto: 2024.1
	zstd: 1.5.6

Number of packages to be removed: 87

The operation will free 825 MiB.

Proceed with deinstalling packages? [y/N]: 
```

## 故障排除

###  `ld-elf.so.1: Shared object "libmd.so.6" not found, required by "pkg"`

该问题一般是由于软件源未及时同步基本系统 ABI 的变更。

对于一般 RELEASE，更新系统即可。对于 CURRENT/STABLE 系统，重新编译 `pkg` 即可。


- RELEASE

请先切换到 latest 源。
  
```sh
# freebsd-update fetch
# freebsd-update install
# pkg-static update -f
# pkg-static upgrade -f pkg
```

- CURRENT/STABLE

```sh
# pkg-static delete -f pkg #强制卸载当前的 pkg
# cd /usr/ports/ports-mgmt/pkg #切换目录
# make BATCH=yes install clean #使用 Ports 重新安装 pkg
```

### `pw: user ‘package’ disappeared during update`

问题示例：

```sh
[1/1] Installing package…
===> Creating groups.
Creating group ‘package’ with gid ‘000’.
===> Creating users
Creating user ‘package’ with uid ‘000’.
pw: user ‘package’ disappeared during update
pkg: PRE-INSTALL script failed
```

问题在于数据库未同步。

刷新数据库：

```sh
# /usr/sbin/pwd_mkdb -p /etc/master.passwd
```

### `Shared object "x.so.x" not found, required by "xxx"`

出现该问题一般是由于 ABI 破坏，更新即可。

安装 `bsdadminscripts2`：

```sh
# pkg install bsdadminscripts2
```
或者

```sh
# cd /usr/ports/ports-mgmt/bsdadminscripts2/ 
# make install clean
```

```sh
# pkg_libchk
doxygen-1.9.6_1,2: /usr/local/bin/doxygen misses libmd.so.6
jbig2dec-0.20_1: /usr/local/bin/jbig2dec misses libmd.so.6
jbig2dec-0.20_1: /usr/local/lib/libjbig2dec.so misses libmd.so.6
jbig2dec-0.20_1: /usr/local/lib/libjbig2dec.so.0 misses libmd.so.6
jbig2dec-0.20_1: /usr/local/lib/libjbig2dec.so.0.0.0 misses libmd.so.6
x265-3.5_3: /usr/local/bin/x265 misses libmd.so.6
x265-3.5_3: /usr/local/lib/libx265.so misses libmd.so.6
x265-3.5_3: /usr/local/lib/libx265.so.200 misses libmd.so.6
xorg-server-21.1.13,1: /usr/local/libexec/Xorg misses libmd.so.6
xwayland-24.1.2,1: /usr/local/bin/Xwayland misses libmd.so.6
root@ykla:/usr/ports/chinese/fcitx # 
```

按照上述软件列表，使用 Ports 逐个重新编译即可（RELEASE 可以直接 `pkg` 更新。）。



#### `bsdadminscripts2` 扩展用法及参考文献


- [BSD Administration Scripts II](https://github.com/lonkamikaze/bsda2)，项目地址，含详细使用说明

- 若使用了 pkgbase，`bsdadminscripts2` 可 **检查系统的完整性**，找出哪些系统文件是被窜改过的：

```sh
root@ykla:/ # pkg_validate
FreeBSD-pkg-bootstrap-15.snap20241004232339: checksum mismatch for /etc/pkg/FreeBSD.conf
FreeBSD-runtime-15.snap20241004232339: checksum mismatch for /etc/group
FreeBSD-runtime-15.snap20241004232339: checksum mismatch for /etc/master.passwd
FreeBSD-runtime-15.snap20241004232339: checksum mismatch for /etc/shells
FreeBSD-runtime-15.snap20241004232339: checksum mismatch for /etc/sysctl.conf
FreeBSD-ssh-15.snap20241004232339: checksum mismatch for /etc/ssh/sshd_config
PackageKit-1.2.8: checksum mismatch for /var/lib/PackageKit/transactions.db
```

- `bsdadminscripts2` 亦可查找当前系统的过时软件：

```sh
@ykla:/usr/ports # pkg_version -ql\<
akonadi-23.08.5_1
build2-0.17.0
chromium-128.0.6613.137
```

### `Newer FreeBSD version for package pkg`

问题示例：

```sh
Newer FreeBSD version for package pkg:
To ignore this error set IGNORE_OSVERSION=yes
- package: 1402843
- running kernel: 1400042
Ignore the mismatch and continue? [y/N]:
```

这通常发生在失去安全支持的或者在 CURRENT/STABLE 版本的系统上，不影响使用，输入 `y` 即可。

如果想要从根源上解决，需要自己卸载 pkg，从 ports 安装 `ports-mgmt/pkg`；或者从源代码更新整个系统。

如果只是不想看到这个提示：只需要按照提示将 `IGNORE_OSVERSION=yes` 写到 `/etc/make.conf` 里面（没有就新建）就行。

## 参考文献

- [pkg delete -- deletes packages from the database	and the	system](https://man.freebsd.org/cgi/man.cgi?query=pkg-delete&sektion=8&n=1)
