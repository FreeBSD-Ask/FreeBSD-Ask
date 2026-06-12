# 7.3 使用 pkg 管理二进制包

FreeBSD 的二进制包管理器目前是 pkg（旧称 pkgng），名称来源于英文单词“Package”，即软件包的简称。

## 安装 pkg 包管理器

> **技巧**
>
> 为了避免向后兼容问题，pkg(8) 工具不会预装在基本系统中。

基本系统默认不包含 pkg，需要先下载并安装 pkg：

```sh
# pkg # 输入 pkg 后按回车
The package management tool is not yet installed on your system. # pkg 尚未安装
Do you want to fetch and install it now? [y/N]: y # 输入 y 并回车确认安装
Bootstrapping pkg from pkg+https://pkg.FreeBSD.org/FreeBSD:14:amd64/quarterly, please wait... # 观察此处，可发现默认调用的是 quarterly 分支的源
Verifying signature with trusted certificate pkg.freebsd.org.2013102301... done
Installing pkg-1.21.3...
Extracting pkg-1.21.3: 100%
pkg: not enough arguments # 这里的报错提示缺少参数，但只是为了安装 pkg 本体，可以忽略
Usage: pkg [-v] [-d] [-l] [-N] [-j <jail name or id>|-c <chroot path>|-r <rootdir>] [-C <configuration file>] [-R <repo config dir>] [-o var=value] [-4|-6] <command> [<args>]

For more information on available commands and options see 'pkg help'.
```

> **技巧**
>
> 如果长时间停留在 `Bootstrapping pkg from ……, please wait...`，请按 **Ctrl + C** 中断这一过程，换境内源后再操作。

> **技巧**
>
> 如果提示 `00206176BC680000:error:0A000086:SSL routines:tls_post_process_server_certificate:certificate verify failed:/usr/src/crypto/openssl/ssl/statem/statem_clnt.c:1890:`（SSL 证书验证失败），请先校准时间。

> ```sh
> # ntpd -q -g pool.ntp.org # 使用 pool.ntp.org 同步系统时间
> ```
>
>> **思考题**
>>
>> 在 SSL 广泛应用的背景下，任何网络问题总是需要检查本机时间是否正确。而用户往往忽略这一点（有时候甚至是 CPU 中负责加密的模块损坏导致的），并且在大多数情况下报错也极不明确。请读者思考，如何解决这个问题？

## 使用 pkg 安装软件

> **技巧**
>
> 如果需要查询某个软件包在 FreeBSD 中的具体情况，可以使用搜索引擎搜索“freebsd ports 包名”，也可以直接在 [FreshPorts](https://www.freshports.org/) 查找。

以安装 Chromium 为例：

```sh
$ pkg ins chromium # 在普通用户权限下安装 chromium 浏览器
pkg: Insufficient privileges to install packages
```

“Insufficient privileges to install packages”即“权限不足，无法安装软件包”。

再试一次：

```sh
$ su # 提升权限到 root，要求此普通用户在 wheel 组中
Password: # 这里输入的是 root 账户密码！
# pkg ins chromium # 再次安装 chromium
Updating FreeBSD repository catalogue...
Fetching data.pkg: 100%   10 MiB 768.6kB/s    00:14
Processing entries: 100%
FreeBSD repository update completed. 36822 packages processed.
Updating FreeBSD-kmods repository catalogue...
Fetching data.pkg: 100%   31 KiB  32.3kB/s    00:01
Processing entries: 100%
FreeBSD-kmods repository update completed. 213 packages processed.
All repositories are up to date.
The following 6 package(s) will be affected (of 0 checked): # 有 6 个软件包将会受到影响

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

> **思考题**
>
>> [Add Concurrent Downloads of Multiple Packages](https://github.com/freebsd/pkg/issues/1628)
>
> 可见 pkg 既不支持并行下载也不支持并行安装。阅读源代码，尝试解决这个问题并提交 PR。

可能会遇到这种情况：

```sh
# pkg ins chromium  # 安装 Chromium 浏览器
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

“pkg: No packages available to install matching 'chromium' have been found in the repositories”即“pkg：在仓库中找不到与 chromium 匹配的可安装软件包”。

如果前面显示了“FreeBSD repository update completed. 36804 packages processed.”（FreeBSD 仓库更新完成。处理了 36804 个包），说明当前软件源是可用的，只是找不到 `chromium` 这个软件包而已。

这就是下文所述“原子更新”缺失的体现。

此外，即使系统已设置 i18n，pkg 的输出仍然是英文。

> **思考题**
>
>> [Is it possible to add i18n multilingual support using po files?](https://github.com/freebsd/pkg/issues/2421)
>>
>> FreeBSD 基本系统中没有 gettext，所以没有计划这样做，如果后续在 pkg 中出现可用的 libintl 套件，则可能会重新考虑。
>
> 阅读 pkg 源代码，定位问题源头，尝试解决这个问题，提交 PR 让 pkg 支持 i18n。

## pkg 更新软件

```sh
# pkg upgrade
```

出现错误：`You must upgrade the ports-mgmt/pkg port first`（必须先更新 pkg 本体）。

解决（优先使用 pkg 自身升级，或通过 Ports 编译）：

```sh
# pkg bootstrap -f      # 强制从远端仓库重装 pkg，无需经过 Ports
```

或：

```sh
# cd /usr/ports/ports-mgmt/pkg
# make deinstall
# make install
```

## 查看已安装的所有软件

```sh
# pkg info
```

## 卸载软件

`pkg delete` 默认会自动将依赖关系不满足的包一并加入删除列表，不会破坏依赖关系；仅当使用 `-f` 参数时才跳过依赖检查。如果需要清理不再被其他包依赖的“叶子”包，可安装 `pkg_rmleaves`，或使用内建命令 `pkg autoremove` 移除自动安装且已无依赖的包。

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
# pkg delete -fa # 如果带上参数 f，会将 pkg 包管理器本身也卸载，因为 pkg 也是用户最初自行安装的软件。
Checking integrity... done (0 conflicting)
Deinstallation has been requested for the following 87 packages (of 0 packages in the universe):

Installed packages to be REMOVED:
	alsa-lib: 1.2.12
	brotli: 1.1.0,1
	curl: 8.8.0
……省略一部分……
	pcre2: 10.43
	perl5: 5.36.3_1
	pkg: 1.21.3   # 如果带上参数 -f，会将 pkg 本身也删除，因为 pkg 也是用户最初自行安装的软件
	png: 1.6.43
	xorg-fonts-truetype: 7.7_1
	xorgproto: 2024.1
	zstd: 1.5.6

Number of packages to be removed: 87

The operation will free 825 MiB.

Proceed with deinstalling packages? [y/N]: # 输入 y 按回车键即可完成卸载
```

#### 参考文献

- FreeBSD Project. pkg delete -- deletes packages from the database and the system[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?query=pkg-delete&sektion=8>. 提供了 pkg 命令删除软件包的详细规范与参数说明。
- FreeBSD Project. pkg(7) -- a utility for manipulating packages[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=7>. FreeBSD 包管理工具手册页。

## 列出 pkg 包安装的文件

> **技巧**
>
> pkg 的下载路径是 **/var/cache/pkg/**。

```sh
/
└── var/
    └── cache/
        └── pkg/ # pkg 的下载路径
```

> **注意**
>
> 只能列出已安装软件包的文件，未安装的不能使用该命令。

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

## 查找缺少的 `.so` 文件（适用于 Linux 兼容层）

> **警告**
>
> 本节仅处理 Linux 兼容层缺少 `.so` 文件的问题。如果在 FreeBSD 上遇到此类问题，应首先更新系统，随后再更新软件源和软件。

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
```

目录结构：

```sh
/usr/local/
├── etc/
│   └── pkg.conf # pkg 配置文件
└── lib/
    └── pkg/ # pkg 插件目录
```

- 编辑 **/usr/local/etc/pkg.conf** 文件，找到空行，写入：

```ini
PKG_PLUGINS_DIR = "/usr/local/lib/pkg/";
PKG_ENABLE_PLUGINS = true;
PLUGINS [ provides ];
```

- 运行 `pkg plugins`：

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

### 在 pkg 中无法找到本书中提及的包

使用 pkg 安装教材中明确提及的软件包时若提示不存在，一般可将原因归纳为以下两种：

- 情况一：Ports 中确实不存在该 Port，可能的原因包括教材内容有误、该 Port 已从 Ports 集合中移除或已更名等。
- 情况二：Ports 中确实存在该 Port，但 FreeBSD 的 pkg 包是周期性构建的（与 Ports 自身的更新同步），因此时常出现暂时缺少对应 pkg 二进制包的情况。

具体原因建议查询 <https://www.freshports.org/>，上面会显示软件包的依赖情况和 pkg 包的构建情况。

本书中一般会同时列出 Ports 安装方式，例如要查 Port **x11/budgie**，操作方法如下：直接访问 <https://www.freshports.org/x11/budgie/>。

如果 Ports 中有该 Port，但 pkg 中暂时没有，等待 7–14 天通常即可（构建失败的包系统会自动向维护者报告错误）。如要立刻安装使用，请使用 Ports。

### `ld-elf.so.1: Shared object "libmd.so.6" not found, required by "pkg"`

该问题通常是由于软件源未及时同步基本系统 ABI 的变更。

对于一般 RELEASE，更新系统即可。对于 CURRENT/STABLE 系统，重新编译 `pkg` 即可。

#### RELEASE

请先切换到 latest 源，再使用软件源里的 pkg 包重装 pkg：

```sh
# pkg-static bootstrap -f  # 强制初始化 pkg 包管理器
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

### `pw: user 'package' disappeared during update`

问题示例：

```sh
[1/1] Installing package…
===> Creating groups.
Creating group 'package' with gid '000'.
===> Creating users
Creating user 'package' with uid '000'.
pw: user 'package' disappeared during update
pkg: PRE-INSTALL script failed
```

原因是用户数据库未同步。

根据 **/etc/master.passwd** 更新密码数据库：

```sh
# /usr/sbin/pwd_mkdb -p /etc/master.passwd
```

### `Shared object "x.so.x" not found, required by "xxx"`

出现该问题通常是由于 ABI 被破坏，更新即可解决。

使用 pkg 安装 `bsdadminscripts2`：

```sh
# pkg install bsdadminscripts2
```

或者使用 Ports 安装 `bsdadminscripts2`：

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

按照上述软件列表，使用 Ports 逐个重新编译即可（RELEASE 可以直接用 `pkg` 更新）。

#### 附录：`bsdadminscripts2` 扩展用法及参考文献

- lonkamikaze. BSD Administration Scripts II[EB/OL]. [2026-03-25]. <https://github.com/lonkamikaze/bsda2>. 提供 FreeBSD 系统管理辅助工具集，含包完整性检查等功能。

若使用了 PkgBase，`bsdadminscripts2` 可 **检查系统的完整性**，找出哪些系统文件遭到了篡改。

验证已安装软件包的完整性和一致性：

```sh
# pkg_validate
FreeBSD-pkg-bootstrap-15.snap20241004232339: checksum mismatch for /etc/pkg/FreeBSD.conf
FreeBSD-runtime-15.snap20241004232339: checksum mismatch for /etc/group
FreeBSD-runtime-15.snap20241004232339: checksum mismatch for /etc/master.passwd
```

- `bsdadminscripts2` 也可查找当前系统的过时软件：

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

这通常发生在已失去安全支持的系统或 CURRENT/STABLE 分支系统上，不影响使用，输入 `y` 即可。

如果要从根源上解决，需要卸载 pkg，从 Ports 安装 `ports-mgmt/pkg`；或者从源代码更新整个系统。

如果仅需屏蔽此提示，只需要按照提示将 `IGNORE_OSVERSION=yes` 写入 **/etc/make.conf** 文件中（如果文件不存在则新建）即可。

### `pkg: An error occurred while fetching package: No error`

以 root 权限执行 `certctl rehash` 刷新证书即可。

参见：pkg(8): “An error occurred while fetching package: No error”[EB/OL]. [2026-03-26]. <https://forums.freebsd.org/threads/pkg-8-an-error-occured-while-fetching-package-no-error.96761/>.

## 附录：FreeBSD 软件包原子更新的困难与现状分析

FreeBSD 镜像站的软件源（无论官方还是非官方）存在以下典型现象：

- 一旦某个 Port 发生更新，就会立即从软件源中撤销由该 Port 衍生的 pkg 二进制包，直到下次构建出新的 pkg 软件包，而非保留旧版本软件包；
- 只要开始一次新的构建，旧版本软件包就会立即从 pkg 软件源中删除，直到构建出新版本的 pkg 软件包。

一种可行的解决方案是：将软件包锁定在某一固定版本阶段（如季度分支），暂不更新，直接轮替版本。

问题在于 Port 更新是不定时的，复杂的依赖关系可能引发连锁问题。有能力者可尝试提出新的看法和建议，并反馈至下方或 [FreeBSD 论坛](https://forums.freebsd.org/)。

> **思考题**
>
> - 相关讨论 [the disappearing pkg issue](https://www.reddit.com/r/freebsd/comments/1nlnwtd/the_disappearing_pkg_issue/)
> - pkg 项目位于 [freebsd/pkg](https://github.com/freebsd/pkg)
> - pkg 软件包的构建系统位于 [Poudriere](https://github.com/freebsd/poudriere)
>
> 尝试：帮助 FreeBSD 项目实现 pkg 二进制软件包的原子更新？

## 课后习题

1. 阅读 pkg 源代码，定位其并行下载与安装的实现位置，尝试为其添加并行下载功能，并验证是否能显著提升安装速度。

2. 选取 pkg 的原子更新问题，设计一个实验方案，复现该问题，并提出一个可行的解决方案。

3. 为 pkg 新增 i18n 支持。
