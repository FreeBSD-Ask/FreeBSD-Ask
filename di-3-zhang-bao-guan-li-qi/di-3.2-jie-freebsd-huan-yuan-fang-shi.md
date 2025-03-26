# 第 3.2 节 FreeBSD 换源方式



## FreeBSD 包管理器设计理念

熟悉 Linux 的人也许会发现，FreeBSD 的包管理方案实际上大约等于以下两大 Linux 发行版包管理器的完美合体：

Arch Linux: Pacman，对应 pkg（同样秉持 KISS 的理念）

Gentoo Linux: Portage，对应 Ports（Portage 本身就是 Ports 的仿制品）

FreeBSD 传统上有四类源：FreeBSD 之所以有这么多源是因为其既可以使用 pkg 通过二进制包安装软件，亦可通过 Ports 使用源代码编译安装软件。pkg 自然需要一类源；索引源代码模板 Ports 也需要一类源，而通过 Ports 下载指定的源代码压缩包也需要一类源；由于基本系统的设计，系统更新也需要一类源。

>**技巧**
>
> 如果需要查询一个软件包在 FreeBSD 中的具体情况可以这样用：谷歌或者必应（必应很多时候搜索不出来）搜索“freebsd ports 包名”。如果无法使用，可以直接在网站里搜索包名 [https://www.freshports.org/](https://www.freshports.org/)。

### FreeBSD 传统上有四类源：pkg、ports、~~portsnap~~、update、kernel modules 源

|源 | 说明 | 备注|
|:---:|:---|:---|
|pkg|类似于传统 Linux 的包管理器，用于安装二进制软件包 | 不需要二进制方式安装软件可以不配置，默认未安装 `pkg`，输入 `pkg` 回车会提示安装|
|~~portsnap~~|拉取 Ports 的源代码模板（本身不含源代码，只是一些描述文件和补丁集）。换言之，这个源类似 Gentoo 的 [ebuild 数据库](https://mirrors.ustc.edu.cn/help/gentoo.html)|**已在 FreeBSD 14 中废弃，无需配置，后续版本亦不再使用，** 改用 `git`、`gitup` 和压缩包 `ports.tar.gz` 等方式获取。|
|ports|Gentoo 的包管理器 Portage（命令为 `emerge`）即是源于此。用于帮助用户从源代码编译安装软件。换言之，等同于 Gentoo 的 [Distfiles 源](https://mirrors.ustc.edu.cn/help/gentoo.html)|不需要源代码方式编译软件可以不配置。|
|update|用于更新系统工具和系统本身 | 预计在 FreeBSD 15 或 16 中废弃，转而使用 [pkgbase](https://wiki.freebsd.org/PkgBase) 代替之|
|kernel modules（kmods）| 内核模块源，为解决小版本间可能存在的 ABI 不兼容问题 | 参见 [Possible solution to the drm-kmod kernel mismatch after upgrade from Bapt](https://forums.freebsd.org/threads/possible-solution-to-the-drm-kmod-kernel-mismatch-after-upgrade-from-bapt.96058/#post-682984)、[CFT: repository for kernel modules](https://lists.freebsd.org/archives/freebsd-ports/2024-December/006997.html)|

> 注意：
>
> `portsnap` 在 FreeBSD 14 中已经弃用，改为使用 `gitup`（请参考第 3.3 节）：
>
> ````sh
> 20230422:
> 	Remove portsnap(8).  Users are encouraged to obtain the ports tree
> 	using git instead.
> ````



对于失去安全支持的版本，请参考最后本文一节。

**本文对于一个源列出了多个镜像站，无须全部配置，只需选择其一即可。**

目前境内没有官方镜像站，以下均为非官方镜像站。

## pkg 源：pkg 源提供了二进制软件包

FreeBSD 中 pkg 源分为系统级和用户级两个配置文件。**不建议**直接修改 `/etc/pkg/FreeBSD.conf` ~~但是太麻烦啦，一般我都是直接改这个文件的~~，因为该文件会随着基本系统的更新而发生改变。

**故障排除**

> **并非所有源都有 `quarterly` 和 `latest`，具体请看 <https://pkg.freebsd.org/> 。**
>
> **若要获取滚动更新的包，请将 `quarterly` 修改为 `latest`。二者区别见 FreeBSD 手册。请注意，`CURRENT` 版本只有 `latest`：**
>
>>使用命令修改系统级 pkg 源使用 latest：
>>
> > ```sh
> > # sed -i '' 's/quarterly/latest/g' /etc/pkg/FreeBSD.conf
> > ```
>
> **若要使用 https，请先安装 `security/ca_root_nss`（FreeBSD 14.1 及以后不需要），并将 `http` 修改为 `https`，最后使用命令 `# pkg update -f` 刷新缓存即可，下同。**

>**注意**
>
>[NJU](https://github.com/nju-lug/NJU-Mirror-Issue/issues/54) 和 163 均同步自 USTC 而非 FreeBSD 直接上游。

### 中国科学技术大学开源软件镜像站（USTC）

>**技巧**
>
>视频教程见 [005-FreeBSD14.2 更换 pkg 源为 USTC 镜像站](https://www.bilibili.com/video/BV13ji2YLEkV)

创建用户级源目录和文件：

```sh
# mkdir -p /usr/local/etc/pkg/repos
# ee /usr/local/etc/pkg/repos/ustc.conf
```

写入以下内容：

```sh
ustc: {
url: "http://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/quarterly",
}
FreeBSD: { enabled: no }
```

### 南京大学开源镜像站

创建用户级源目录和文件：

```sh
# mkdir -p /usr/local/etc/pkg/repos
# ee /usr/local/etc/pkg/repos/nju.conf
```

写入以下内容：

```sh
nju: {
url: "http://mirrors.nju.edu.cn/freebsd-pkg/${ABI}/quarterly",
}
FreeBSD: { enabled: no }
```

### 网易开源镜像站

创建用户级源目录和文件：

```sh
# mkdir -p /usr/local/etc/pkg/repos
# ee /usr/local/etc/pkg/repos/163.conf
```

写入以下内容：

```sh
163: {
url: "http://mirrors.163.com/freebsd-pkg/${ABI}/quarterly",
}
FreeBSD: { enabled: no }
```


## ports 源：以源代码方式编译安装软件的包管理器

### 下载 ports

这个源是下载 ports 本身的源。等同于以前的 `portsnap`。



#### Git 方法

须提前安装 git：

```sh
# pkg install git
```

或

```sh
# cd /usr/ports/devel/git
# make install clean
```

然后：

```sh
# git clone  --filter=tree:0 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git /usr/ports
```

>**注意**
>
>`--depth 1` 会给服务器带来较大计算压力，请尽量使用参数  `--filter=tree:0`。

#### 下载压缩文件的方法

>**警告**
>
>通过下载 Port 的压缩文件来使用 Ports，是一次性的：Ports 后续无法更新，建议你优先采用 Git 方法。


```sh
# fetch https://mirrors.nju.edu.cn/freebsd-ports/ports.tar.gz
```

或者

```sh
# fetch https://mirrors.ustc.edu.cn/freebsd-ports/ports.tar.gz
```

然后

```sh
# tar -zxvf ports.tar.gz -C /usr/ #解压至路径
# rm ports.tar.gz #删除存档
```

### ports 源

这个源是下载 ports 中的软件的源。


> **警告**
>
> ports 源可能并不完整。其余的大概只镜像了不到十分之一。见 <https://github.com/ustclug/discussions/issues/408>。

#### 南京大学开源镜像站

创建或修改文件 :

```sh
# ee /etc/make.conf
```

写入以下内容：

```sh
MASTER_SITE_OVERRIDE?=http://mirrors.nju.edu.cn/freebsd-ports/distfiles/${DIST_SUBDIR}/
```

#### 网易开源镜像站

创建或修改文件：

```sh
# ee /etc/make.conf
```

写入以下内容：

```sh
MASTER_SITE_OVERRIDE?=http://mirrors.163.com/freebsd-ports/distfiles/${DIST_SUBDIR}/
```

#### 中国科学技术大学开源软件镜像站

创建或修改文件：

```sh
# ee /etc/make.conf
```

写入以下内容：

```sh
MASTER_SITE_OVERRIDE?=http://mirrors.ustc.edu.cn/freebsd-ports/distfiles/${DIST_SUBDIR}/
```

## portsnap 源：打包的 ports 文件（FreeBSD 14.0 及以后不可用）

> **警告**
>
> FreeBSD 关于弃用 portsnap 的说明：[[HEADS UP] Planned deprecation of portsnap](https://marc.info/?l=freebsd-ports&m=159656662608767&w=2)。

**获取 portsnap 更新**

```sh
# portsnap auto #同时支持命令行和 cron
```

或

```sh
# portsnap fetch extract
```

**故障排除**

```sh
Snapshot appears to have been created more than one day into the future!
(Is the system clock correct?)
Cowardly refusing to proceed any further.
```

需要同步时间。

```sh
ntpdate ntp.api.bz
```

## freebsd-update 源：提供基本系统更新

注意：只有一级架构的 release 版本才提供该源。也就是说 current 和 stable 是没有的（可选择使用后续文章中的 pkgbase 进行更新）。关于架构的支持等级说明请看：

[Supported Platforms](https://www.freebsd.org/platforms)

**例：从 FreeBSD 12 升级到 13.0**

```sh
# freebsd-update -r 13.0-RELEASE upgrade
```

## kernel modules（kmods）内核模块源：面向 FreeBSD 14.2 及更高版本（不含 15.0-CURRENT）

### FreeBSD 官方源

新建文件夹 `/usr/local/etc/pkg/repos`（即 `mkdir -p /usr/local/etc/pkg/repos`），再新建文件 `/usr/local/etc/pkg/repos/FreeBSD-kmods.conf`：

写入：

#### quarterly 分支

```sh
FreeBSD-kmods {
	url: pkg+https://pkg.freebsd.org/${ABI}/kmods_quarterly_${VERSION_VERSION}
	signature_type: "fingerprints"
	fingerprints: "/usr/share/keys/pkg"
	mirror_type: "srv"
	enabled: yes
}
```

#### latest 分支

```sh
FreeBSD-kmods {
	url: pkg+https://pkg.freebsd.org/${ABI}/kmods_latest_${VERSION_VERSION}
	signature_type: "fingerprints"
	fingerprints: "/usr/share/keys/pkg"
	mirror_type: "srv"
	enabled: yes
}
```

### 中国科学技术大学开源软件镜像站

新建文件夹 `/usr/local/etc/pkg/repos`（即 `mkdir -p /usr/local/etc/pkg/repos`），再新建文件 `/usr/local/etc/pkg/repos/FreeBSD-kmods.conf`：

写入：

#### quarterly 分支

```sh
FreeBSD-kmods {
	url: https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_quarterly_${VERSION_VERSION}
	enabled: yes
}
```

#### latest 分支

```sh
FreeBSD-kmods {
	url: https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_latest_${VERSION_VERSION}
	enabled: yes
}
```



## 不受安全支持的版本（请酌情使用）

>**技巧**
>
>网易开源镜像站还提供了 FreeBSD 11、12 等过期版本的 pkg 二进制源。可自行配置使用。

不受安全支持的版本也是可以使用二进制源的。

> 以下，以 `FreeBSD 9.2` 为例：

首先切换成可以用的二进制源

```sh
# setenv PACKAGESITE http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest
```

如果 shell 不是 csh，那么：

```sh
# export PACKAGESITE=http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest
```

安装示例：现在安装 `bsdinfo`。

```sh
root@ykla:~ # pkg_add -r bsdinfo
Fetching http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest/bsdinfo.tbz... Done.
```

**pkg 是不可用的，会提示找不到 `digests.txz` 和 `repo.txz`，因为当时 pkgng 还没有被官方所支持，仍然仅支持使用 `pkg_*` 命令。**

## 参考文献

- [FreeBSD ports](https://mirrors.ustc.edu.cn/help/freebsd-ports.html)，USTC Mirrors 换源帮助
- [FreeBSD pkg](https://mirrors.ustc.edu.cn/help/freebsd-pkg.html)，USTC Mirrors 换源帮助
