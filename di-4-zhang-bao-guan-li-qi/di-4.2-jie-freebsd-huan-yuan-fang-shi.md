# 第 3.2 节 FreeBSD 换源方式

## FreeBSD 包管理器设计理念

熟悉 Linux 的人也许会发现，FreeBSD 的包管理方案实际上大约等于以下两大 Linux 发行版包管理器的完美合体：

- Arch Linux：Pacman，对应 pkg（同样秉持 KISS 的理念）
- Gentoo Linux：Portage，对应 Ports（Portage 本身就是 Ports 的仿制品）

|源 | 说明 | 备注|
|:---:|:---|:---|
|pkg|类似于传统 Linux 的包管理器，用于安装二进制软件包 | 不需要二进制方式安装软件可以不配置，默认未安装 `pkg`，输入 `pkg` 回车会提示安装|
|~~portsnap~~|拉取 Ports 的源代码模板（本身不含源代码，只是一些描述文件和补丁集）。换言之，这个源类似 Gentoo 的 [ebuild 数据库](https://mirrors.ustc.edu.cn/help/gentoo.html)|**已于 FreeBSD 14 及后续版本废弃，无需配置** 改用 `git`、`gitup` 和压缩包 `ports.tar.gz` 等方式获取。|
|ports|Gentoo 的包管理器 Portage（命令为 `emerge`）即是源于此。用于帮助用户从源代码编译安装软件。换言之，等同于 Gentoo 的 [Distfiles 源](https://mirrors.ustc.edu.cn/help/gentoo.html)|不需要源代码方式编译软件可以不配置。|
|update|用于更新基本系统（内核 + 用户空间） | 预计在 FreeBSD 15 或 16 中废弃，转而使用 [pkgbase](https://wiki.freebsd.org/PkgBase) 代替之|
|kernel modules（kmods）| 内核模块源，为解决小版本间可能存在的 ABI 不兼容问题 | 参见 [Possible solution to the drm-kmod kernel mismatch after upgrade from Bapt](https://forums.freebsd.org/threads/possible-solution-to-the-drm-kmod-kernel-mismatch-after-upgrade-from-bapt.96058/#post-682984)、[CFT: repository for kernel modules](https://lists.freebsd.org/archives/freebsd-ports/2024-December/006997.html)|


>**技巧**
>
>本文对于一个源列出了多个镜像站，无须全部配置，只需选择其一即可。

目前境内没有官方镜像站，以下均为非官方镜像站。

>**注意**
>
>[NJU](https://github.com/nju-lug/NJU-Mirror-Issue/issues/54) 和 163 均同步自 USTC 而非 FreeBSD 直接上游。

## pkg 源：pkg 源提供了二进制软件包

境内的源一般只支持 aarch64（arm64）和 amd64 两个架构。

FreeBSD 中 pkg 源分为系统级和用户级两个配置文件。**不建议**直接修改 `/etc/pkg/FreeBSD.conf` ~~但是太麻烦啦，一般我都是直接改这个文件的~~，因为该文件会随着基本系统的更新而发生改变。

---

并非所有源都有 `quarterly` 和 `latest`，具体请看 <https://pkg.freebsd.org/> 。


### pkg 换源

若要获取滚动更新的包，请将 `quarterly` 修改为 `latest`。二者区别见 FreeBSD 手册。请注意，`CURRENT` 版本只有 `latest`。

使用命令修改系统级 pkg 源使用 latest：

```sh
# sed -i '' 's/quarterly/latest/g' /etc/pkg/FreeBSD.conf
```

---

- 创建用户级源目录和文件：

```sh
# mkdir -p /usr/local/etc/pkg/repos
# ee /usr/local/etc/pkg/repos/mirrors.conf
```

---

- 中国科学技术大学开源软件镜像站（USTC）

>**技巧**
>
>视频教程见 [005-FreeBSD14.2 更换 pkg 源为 USTC 镜像站](https://www.bilibili.com/video/BV13ji2YLEkV)

写入以下内容：

```sh
ustc: {
url: "http://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/latest",
}
FreeBSD: { enabled: no }
```

- 南京大学开源镜像站

写入以下内容：

```sh
nju: {
url: "http://mirrors.nju.edu.cn/freebsd-pkg/${ABI}/latest",
}
FreeBSD: { enabled: no }
```

- 网易开源镜像站

写入以下内容：

```sh
163: {
url: "http://mirrors.163.com/freebsd-pkg/${ABI}/latest",
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

---

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
# tar -zxvf ports.tar.gz -C /usr/ # 解压至路径
# rm ports.tar.gz # 删除存档
```

### ports 源

这个源是下载 ports 中的软件的源。


> **警告**
>
> ports 源可能并不完整。其余的大概只镜像了不到十分之一。见 <https://github.com/ustclug/discussions/issues/408>。

创建或修改文件 :

```sh
# ee /etc/make.conf
```

---

- 南京大学开源镜像站


写入以下内容：

```sh
MASTER_SITE_OVERRIDE?=http://mirrors.nju.edu.cn/freebsd-ports/distfiles/${DIST_SUBDIR}/
```

- 网易开源镜像站

写入以下内容：

```sh
MASTER_SITE_OVERRIDE?=http://mirrors.163.com/freebsd-ports/distfiles/${DIST_SUBDIR}/
```

- 中国科学技术大学开源软件镜像站


写入以下内容：

```sh
MASTER_SITE_OVERRIDE?=http://mirrors.ustc.edu.cn/freebsd-ports/distfiles/${DIST_SUBDIR}/
```

## kernel modules（kmods）内核模块源：面向 FreeBSD 14.2 及更高版本（不含 15.0-CURRENT）

新建文件夹 `/usr/local/etc/pkg/repos`（即 `mkdir -p /usr/local/etc/pkg/repos`），再新建文件 `/usr/local/etc/pkg/repos/FreeBSD-kmods.conf`：


### FreeBSD 官方源

写入：

#### quarterly 分支

```sh
FreeBSD-kmods {
	url: pkg+https://pkg.freebsd.org/${ABI}/kmods_quarterly_2
	signature_type: "fingerprints"
	fingerprints: "/usr/share/keys/pkg"
	mirror_type: "srv"
	enabled: yes
}
```

#### latest 分支

```sh
FreeBSD-kmods {
	url: pkg+https://pkg.freebsd.org/${ABI}/kmods_latest_2
	signature_type: "fingerprints"
	fingerprints: "/usr/share/keys/pkg"
	mirror_type: "srv"
	enabled: yes
}
```

### 中国科学技术大学开源软件镜像站


写入：

#### quarterly 分支

```sh
FreeBSD-kmods {
	url: https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_quarterly_2
	enabled: yes
}
```

#### latest 分支

```sh
FreeBSD-kmods {
	url: https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_latest_2
	enabled: yes
}
```


## 不受安全支持的版本（请酌情使用）

>**技巧**
>
>网易开源镜像站还提供了 FreeBSD 11、12 等过期版本的 pkg 二进制源。可自行配置使用。

不受安全支持的版本也是可以使用二进制源的。以下，以 `FreeBSD 9.2` 为例：

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

>**注意**
>
>pkg 是不可用的，会提示找不到 `digests.txz` 和 `repo.txz`，因为当时 pkgng 还没有被官方所支持，仍然仅支持使用 `pkg_*` 命令。

## 参考文献

- [FreeBSD ports](https://mirrors.ustc.edu.cn/help/freebsd-ports.html)，USTC Mirrors 换源帮助
- [FreeBSD pkg](https://mirrors.ustc.edu.cn/help/freebsd-pkg.html)，USTC Mirrors 换源帮助
