# 第 3.4 节 软件包管理器 pkg 的用法

包管理器目前是 pkgng，其命令是 pkg。

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

```
# pkg
```

回车即可输入 `y` 确认下载

pkg 使用 https，先安装 ssl 证书：

```
# pkg install ca_root_nss
```

然后把 repo.conf 里的 pkg+http 改成 pkg+https 即可。

最后刷新 pkg 数据库：

```
# pkg update -f
```

安装 python 3：


```
# pkg install python
```

pkg 升级：

```
# pkg upgrade
```

错误：`You must upgrade the ports-mgmt/pkg port first`

解决：

```shell-session
# cd /usr/ports/ports-mgmt/pkg
# make deinstall reinstall
```

查看已经安装的所有软件：

```shell-session
# pkg info
```

## 如何卸载软件

**来源请求** 直接使用 `pkg delete` 会破坏正常的依赖关系，应该尽量避免使用（ports 的 `make deinstall` 也一样），转而使用 `pkg-rmleaf` 命令，该命令属于的软件需要自行安装：

`# pkg install pkg-rmleaf`

### 如何卸载所有自行安装的第三方软件？

```shell-session
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

### FreeBSD pkg 安装软件时出现创建用户失败解决

问题示例：

```shell-session
[1/1] Installing package…
===> Creating groups.
Creating group ‘package’ with gid ‘000’.
===> Creating users
Creating user ‘package’ with uid ‘000’.
pw: user ‘package’ disappeared during update
pkg: PRE-INSTALL script failed
```

问题解析：数据库未同步

问题解决：

```shell-session
# /usr/sbin/pwd_mkdb -p /etc/master.passwd
```

### Shared object "x.so.x" not found, required by "xxx"

出现该问题一般是由于 ABI 破坏，更新即可。

```shell-session
# pkg  install bsdadminscripts
# pkg_libchk
# port-rebuild
```

### Newer FreeBSD version for package pkg

问题示例：

```shell-session
Neuer FreeBSD version for package pkg:
To ignore this error set IGNORE_OSVERSION=yes
- package: 1402843
- running kernel: 1400042
Ignore the mismatch and continue? [y/N]:
```

这通常发生在失去安全支持的或者在 Current 版本的系统上，不影响使用，输入 `y` 即可。

如果想要从根源上解决，需要自己卸载 pkg，从 ports 安装 `ports-mgmt/pkg`；或者从源代码更新整个系统。

如果只是不想看到这个提示：只需要按照提示将 `IGNORE_OSVERSION=yes` 写到 `/etc/make.conf` 里面（没有就新建）就行。

## 参考文献

- [pkg delete -- deletes packages from the database	and the	system](https://man.freebsd.org/cgi/man.cgi?query=pkg-delete&sektion=8&n=1)
