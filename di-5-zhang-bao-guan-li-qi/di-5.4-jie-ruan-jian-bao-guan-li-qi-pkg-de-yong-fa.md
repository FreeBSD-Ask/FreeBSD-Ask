# 5.4 使用 pkg 管理二进制包

FreeBSD 的二进制包管理器目前是 pkg（旧称 pkgng），即“Package”，意为软件包。

`pkg install` 可以缩写成 `pkg ins`，其他命令亦类似。

> **注意**
>
> pkg 只能管理第三方软件包，并不能起到升级系统，获取安全更新的作用。这是因为 FreeBSD 项目是将内核与用户空间作为一个整体来进行维护的，而不是像 Linux 那样 Linus Torvalds 负责维护内核，各个发行版的人负责维护 GNU 工具（他们这些软件实际上被设计为单个软件包，因此可以用包管理器更新与升级系统）。
>
>FreeBSD 现在也正 [试图使用 pkg 来实现用户空间和内核的更新](https://wiki.freebsd.org/PkgBase) ，以期解决上述问题。
>
> FreeBSD 使用 `freebsd-update` 来升级系统，获取安全补丁。<https://pkg-status.freebsd.org/> 可以查看当前的 pkg 编译状态。
>
>
> 偏好图形化的用户可以安装并使用 `ports-mgmt/octopkg`，该工具是 pkg 的图形化前端，由 GhostBSD 开发。


>**技巧**
>
>如果需要查询某个软件包在 FreeBSD 中的具体情况，可以这样做：使用 Google 或 Bing（Bing 很多时候搜索不出来）搜索“freebsd ports 包名”。如果无法使用，可以直接在网站里搜索包名 [https://www.freshports.org/](https://www.freshports.org/)。

## 如何从 Port 构建出 pkg

![pkg 构建流程图](../.gitbook/assets/portstopkg.png)

### 书里明确写有某个包，但是 pkg 安装的时候却提示没有

这个问题一般来说有两种情况：

- ① 在 Ports 中的确没有这个 Port：书里写错了、从 Ports 中移除了/改名了等
- ② Ports 中的确有这个 Port：FreeBSD 的 pkg 包是周期性构建的（因为 Ports 本身在更新），因此经常会出现暂时没有对应 pkg 包的情况

具体是哪个问题造成的，建议查询 <https://www.freshports.org>，上面会显示软件包的依赖情况和 pkg 包的构建情况。

本书中一般会同时列出 Ports 安装方式，比如要查 Port `x11/budgie`，你可以这么做：直接访问 <https://www.freshports.org/x11/budgie/>。

一般来说，如果 Ports 中有该 Port，但 pkg 中暂时没有，等待 7–14 天通常即可（构建失败的包系统会自动向维护者报告错误）。如要立刻安装使用，请使用 Ports。

### 附录：FreeBSD 软件包原子更新的困难与现状

你会经常观察到 FreeBSD 的镜像站（无论是官方的还是非官方的）源存在这样几种情况：

- 一旦 Port 发生更新，就会立刻从软件源撤销该 Port 衍生的 pkg 软件包，直到下次构建出新的 pkg 软件包，而不是保留旧的软件包；
- 只要开始一次新的构建，旧的软件包不是被临时保留，而是被立刻从 pkg 软件包软件源中删除，直到构建出新版本的 pkg 软件包。

理论上的解决方案是：保持软件包处于某一固定版本阶段（季度分支），不进行更新，然后直接轮替。

问题在于 Port 更新是不定时的。复杂的依赖会破坏一切。有能力者可尝试提出新的看法和建议，并反馈至下方或 [FreeBSD 论坛](https://forums.freebsd.org/)。

>**思考题**
>
>- 相关讨论 [the disappearing pkg issue](https://www.reddit.com/r/freebsd/comments/1nlnwtd/the_disappearing_pkg_issue/)
>- pkg 项目位于 [freebsd/pkg](https://github.com/freebsd/pkg)
>- pkg 软件包的构建系统位于 [Poudriere](https://github.com/freebsd/poudriere)。
>
>试一试：帮助 FreeBSD 项目实现 pkg 二进制软件包的原子更新？


## 安装 pkg 包管理器本体

>**技巧**
>
>根据 man [pkg(7)](https://man.freebsd.org/cgi/man.cgi?query=pkg) 页面解释：
>
>>为了避免出现向后兼容问题，实际的 `pkg(8)` 工具不会预装在基本系统中。

基本系统默认不包含 pkg，需要先下载并安装 pkg：

```sh
# pkg # 输入 pkg 后按回车
The package management tool is not yet installed on your system. # pkg 尚未安装
Do you want to fetch and install it now? [y/N]: y # “你想下载安装吗？”请在这里输入 y 再按回车键即可安装
Bootstrapping pkg from pkg+https://pkg.FreeBSD.org/FreeBSD:14:amd64/quarterly, please wait... # 观察此处，可发现默认调用的是 quarterly 分支的源
Verifying signature with trusted certificate pkg.freebsd.org.2013102301... done
Installing pkg-1.21.3...
Extracting pkg-1.21.3: 100%
pkg: not enough arguments # 这里的报错提示缺少参数，但只是为了安装 pkg 本体，可以忽略
Usage: pkg [-v] [-d] [-l] [-N] [-j <jail name or id>|-c <chroot path>|-r <rootdir>] [-C <configuration file>] [-R <repo config dir>] [-o var=value] [-4|-6] <command> [<args>]

For more information on available commands and options see 'pkg help'.
```

>**技巧**
>
>如果长时间卡在 `Bootstrapping pkg from ……, please wait...`，请按 **Ctrl + C** 中断这一过程，换境内源后再进行。

>**技巧**
>
>如果提示 `00206176BC680000:error:0A000086:SSL routines:tls_post_process_server_certificate:certificate verify failed:/usr/src/crypto/openssl/ssl/statem/statem_clnt.c:1890:`（SSL 证书验证失败），请先校准时间。
>
>```sh
># ntpdate -u pool.ntp.org	#  使用 pool.ntp.org 同步系统时间
>```
>
>>**思考题**
>>
>>在 SSL 大行其是的年代里，任何网络问题总是要看看自己机器的时间是否正确。而一般人总会忽略这一点（有时候甚至是 CPU 中负责加密的模块损坏导致的），并且大多数情况下报错也极不明确。你认为应该如何解决这个问题？


## 使用 pkg 安装软件

以安装 chromium 为例：

```sh
$ pkg ins chromium # 在普通用户权限下安装 chromium 浏览器看看
pkg: Insufficient privileges to install packages
```

“Insufficient privileges to install packages”即“没有足够的权限来安装软件包”。

再试一次：

```sh
$ su # 提升权限到 root，要求此普通用户在 wheel 组中
Password: # 这里输入的是 root 账户密码！
# pkg ins chromium # 再安装 chromium 试试看！
Updating FreeBSD repository catalogue...
Fetching data.pkg: 100%   10 MiB 768.6kB/s    00:14    
Processing entries: 100%
FreeBSD repository update completed. 36822 packages processed.
Updating FreeBSD-kmods repository catalogue...
Fetching data.pkg: 100%   31 KiB  32.3kB/s    00:01    
Processing entries: 100%
FreeBSD-kmods repository update completed. 213 packages processed.
All repositories are up to date.
The following 6 package(s) will be affected (of 0 checked): # 有 6 个软件包将会受影响

New packages to be INSTALLED:
        chromium: 142.0.7444.162 [FreeBSD]
        dconf: 0.49.0 [FreeBSD]
        harfbuzz-icu: 10.3.0 [FreeBSD]
        jsoncpp: 1.9.6_1 [FreeBSD]
        sndio: 1.10.0_1 [FreeBSD]
        speex: 1.2.1_1,1 [FreeBSD]

Number of packages to be installed: 6

The process will require 463 MiB more space.
127 MiB to be downloaded.

Proceed with this action? [y/N]: # 此处输入 y 再按回车键即可安装
```

>**思考题**
>
>>[Add Concurrent Downloads of Multiple Packages](https://github.com/freebsd/pkg/issues/1628)
>
>你会发现 pkg 既不支持并行下载也不支持并行安装，阅读源代码，尝试解决提交 PR 这个问题。

你极有可能会遇到这种情况：

```sh
# pkg ins chromium	# 安装 Chromium 浏览器
Updating FreeBSD repository catalogue.
Fetching meta.conf: 100%    179 B   0.2kB/s    00:01    
Fetching data.pkg: 100%   10 MiB   2.7MB/s    00:04    
Processing entries: 100%
FreeBSD repository update completed. 36804 packages processed.
Updating FreeBSD-kmods repository catalogue...
FreeBSD-kmods repository is up to date.
All repositories are up to date.
pkg: No packages available to install matching 'chromium' have been found in the repositories
```

“pkg: No packages available to install matching 'chromium' have been found in the repositories”即“pkg：在仓库中找不到 与“chromium”匹配、可供安装的软件包”。

如果你前面显示了“FreeBSD repository update completed. 36804 packages processed.”（FreeBSD 仓库更新完成。处理了 36804 个包），说明当前软件源是可用的，只是找不到 `chromium` 这个软件包而已。

这就是上面所述的缺乏“原子更新”的表现。

还会发现，即使系统已设置 i18n，pkg 的输出仍然是英文。

>**思考题**
>
>>[Is it possible to add i18n multilingual support using po files?](https://github.com/freebsd/pkg/issues/2421)
>>
>>FreeBSD 基本系统里没有 gettext，所以没有计划这样做，如果后续在 pkg 中出现可用的 libintl 套件，则可能会重新考虑。
>
>阅读 pkg 源代码，定位问题所在源头，尝试解决这个问题，提交 PR 让 pkg 支持 i18n。


## pkg 更新软件

```sh
# pkg upgrade
```

错误：`You must upgrade the ports-mgmt/pkg port first`（必须先更新 pkg 本体）

解决：

```sh
# cd /usr/ports/ports-mgmt/pkg
# make deinstall
# make install
```

## 查看已经安装的所有软件

```sh
# pkg info
```

## 卸载软件

直接使用 `pkg delete` 可能破坏依赖关系，应尽量避免使用（Ports 的 `make deinstall` 亦然），建议改用 `pkg_rmleaves` 命令，该命令所属的软件需要自行安装。


```sh
# pkg install pkg_rmleaves
```

或者

```sh
# cd /usr/ports/ports-mgmt/pkg_rmleaves/
# make install
```

### 如何卸载所有自行安装的第三方软件？

```sh
# pkg delete -fa # 如果带上参数 f，会将 pkg 自己也删掉，因为 pkg 也是用户一开始自行安装的软件。
Checking integrity... done (0 conflicting)
Deinstallation has been requested for the following 87 packages (of 0 packages in the universe):

Installed packages to be REMOVED:
	alsa-lib: 1.2.12
	brotli: 1.1.0,1
	curl: 8.8.0
……省略一部分……
	pcre2: 10.43
	perl5: 5.36.3_1
	pkg: 1.21.3   # 如果带上参数 `-f`，会将 pkg 本身也删除，因为 pkg 也是用户最初自行安装的软件
	png: 1.6.43
	xorg-fonts-truetype: 7.7_1
	xorgproto: 2024.1
	zstd: 1.5.6

Number of packages to be removed: 87

The operation will free 825 MiB.

Proceed with deinstalling packages? [y/N]: # 输入 y 按回车键就卸载了
```

#### 参考文献

- [pkg delete -- deletes packages from the database	and the	system](https://man.freebsd.org/cgi/man.cgi?query=pkg-delete&sektion=8&n=1)

## 列出 pkg 包安装的文件

>**技巧**
>
>pkg 的下载路径是 `/var/cache/pkg/`。

>**注意**
>
>只能列出已安装的包的文件，未安装的不能用这个命令。

```sh
# pkg info -l xrdp
xrdp-0.10.2_2,1:
	/usr/local/bin/xrdp-dis
	/usr/local/bin/xrdp-dumpfv1
	/usr/local/bin/xrdp-genkeymap
	/usr/local/bin/xrdp-keygen
	/usr/local/bin/xrdp-sesadmin
	/usr/local/bin/xrdp-sesrun
	/usr/local/etc/pam.d/xrdp-sesman
	/usr/local/etc/rc.d/xrdp
	……省略一部分……
```


## 查找缺少的 `.so`（适用于 Linux 兼容层）

>**警告**
>
>本节仅针对 Linux 兼容层缺少 `.so` 文件的问题。如果你是在 FreeBSD 中遇到了此类问题，应首先更新系统。然后再更新软件源和软件。

### 安装 pkg-provides

```sh
# pkg install pkg-provides
```

或者：

```sh
# cd /usr/ports/ports-mgmt/pkg-provides/ 
# make install clean
```

### 配置使用 pkg-provides

- 查看配置说明：

```sh
# pkg info -D pkg-provides
pkg-provides-0.7.4:
On install:
In order to use the pkg-provides plugin you need to enable plugins in pkg.
# 要使用 pkg-provides 插件，必须先在 pkg 中启用插件功能。

To do this, uncomment the following lines in /usr/local/etc/pkg.conf file
and add pkg-provides to the supported plugin list:
# 方法是在 /usr/local/etc/pkg.conf 文件中取消以下行的注释，并将 pkg-provides 添加到支持的插件列表中：

PKG_PLUGINS_DIR = "/usr/local/lib/pkg/";
PKG_ENABLE_PLUGINS = true;
PLUGINS [ provides ];
# 插件配置示例，其中 provides 表示启用 pkg-provides 插件。

After that run `pkg plugins' to see the plugins handled by pkg.
# 设置完成后，运行 `pkg plugins` 查看已启用的插件。

On upgrade:
# 升级说明：

To update the provides database run `pkg provides -u`.
# 要更新 provides 数据库，运行 `pkg provides -u`。
```

- 编辑 `/usr/local/etc/pkg.conf`，找到空行，写入：


```ini
PKG_PLUGINS_DIR = "/usr/local/lib/pkg/";
PKG_ENABLE_PLUGINS = true;
PLUGINS [ provides ];
```

- 运行：`pkg plugins`：

```sh
# pkg plugins
NAME       DESC                                          VERSION   
provides   A plugin for querying which package provides a particular file 0.7.4     
```

- 刷新数据库：

```sh
# pkg provides -u
Fetching provides database: 100%   19 MiB   6.6MB/s    00:03    
Extracting database....success
```

### 示例：查找 `libxcb-icccm.so.4`

```sh
# pkg provides libxcb-icccm.so.4
Name    : xcb-util-wm-0.4.2
Comment : Framework for window manager implementation
Repo    : FreeBSD
Filename: usr/local/lib/libxcb-icccm.so.4.0.0
          usr/local/lib/libxcb-icccm.so.4
```

## 故障排除与未竟事宜

### `ld-elf.so.1: Shared object "libmd.so.6" not found, required by "pkg"`

该问题通常是由于软件源未及时同步基本系统 ABI 的变更所致。

对于一般 RELEASE，更新系统即可。对于 CURRENT/STABLE 系统，重新编译 `pkg` 即可。


#### RELEASE

请先切换到 latest 源，再使用软件源里的 pkg 包重装 pkg：

```sh
# pkg-static bootstrap -f	# # 强制初始化 pkg 包管理器
```

若无效，则再：

```sh
# freebsd-update fetch        # 下载可用的 FreeBSD 更新
# freebsd-update install      # 安装下载的 FreeBSD 更新
# pkg-static update -f        # 强制更新本地软件包仓库索引
# pkg-static upgrade -f pkg   # 强制升级 pkg 工具本体
```

#### CURRENT/STABLE

```sh
# pkg-static delete -f pkg # 强制卸载当前的 pkg
# cd /usr/ports/ports-mgmt/pkg # 切换目录
# make BATCH=yes install clean # 使用 Ports 重新安装 pkg
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

问题原因在于用户数据库未同步。

根据 `/etc/master.passwd` 更新密码数据库：

```sh
# /usr/sbin/pwd_mkdb -p /etc/master.passwd
```

### `Shared object "x.so.x" not found, required by "xxx"`

出现该问题通常是由于 ABI 发生破坏，更新即可解决。

使用 pkg 安装 `bsdadminscripts2`：

```sh
# pkg install bsdadminscripts2
```

或者使用 ports 安装 `bsdadminscripts2`：

```sh
# cd /usr/ports/ports-mgmt/bsdadminscripts2/ 
# make install clean
```

检查已安装软件包的动态库依赖是否完整：

```sh
# pkg_libchk
doxygen-1.9.6_1,2: /usr/local/bin/doxygen misses libmd.so.6
jbig2dec-0.20_1: /usr/local/bin/jbig2dec misses libmd.so.6
jbig2dec-0.20_1: /usr/local/lib/libjbig2dec.so misses libmd.so.6
```

按照上述软件列表，使用 Ports 逐个重新编译即可（RELEASE 可以直接 `pkg` 更新。）。


#### 附录：`bsdadminscripts2` 扩展用法及参考文献


- [BSD Administration Scripts II](https://github.com/lonkamikaze/bsda2)，项目地址，含详细使用说明

- 若使用了 pkgbase，`bsdadminscripts2` 可 **检查系统的完整性**，找出哪些系统文件是被窜改过的。

验证已安装软件包的完整性和一致性：

```sh
# pkg_validate
FreeBSD-pkg-bootstrap-15.snap20241004232339: checksum mismatch for /etc/pkg/FreeBSD.conf
FreeBSD-runtime-15.snap20241004232339: checksum mismatch for /etc/group
FreeBSD-runtime-15.snap20241004232339: checksum mismatch for /etc/master.passwd
```

- `bsdadminscripts2` 亦可查找当前系统的过时软件：

```sh
# pkg_version -ql\<
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

这通常发生在已失去安全支持的系统，或 CURRENT/STABLE 分支系统上，不影响使用，输入 `y` 即可。

如果想要从根源上解决，需要自己卸载 pkg，从 ports 安装 `ports-mgmt/pkg`；或者从源代码更新整个系统。

如果只是不想看到这个提示：只需要按照提示将 `IGNORE_OSVERSION=yes` 写到 `/etc/make.conf` 里面（没有就新建）就行。

### `pkg: An error occurred while fetching package: No error`

以 root 权限执行 `certctl rehash` 刷新证书即可。

参见 [pkg(8): "An error occured while fetching package: No error"](https://forums.freebsd.org/threads/pkg-8-an-error-occured-while-fetching-package-no-error.96761/)


