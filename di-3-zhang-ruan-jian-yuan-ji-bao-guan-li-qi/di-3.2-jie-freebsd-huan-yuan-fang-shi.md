# 第 3.2 节 FreeBSD 换源方式

## FreeBSD 包管理器设计理念

熟悉 Linux 的人也许会发现，FreeBSD 的包管理方案实际上大约等于以下两大 Linux 发行版包管理器的完美合体：

Arch Linux: Pacman，对应 pkg（同样秉持 KISS 的理念）

Gentoo Linux: Portage，对应 Ports（Portage 本身就是 Ports 的仿制品）

> 如果需要查询一个软件包在 FreeBSD 中的具体情况可以这样用：谷歌或者必应（必应很多时候搜索不出来）搜索“freebsd ports 包名”。如果无法使用，可以直接在网站里搜索包名 [https://www.freshports.org/](https://www.freshports.org/)。

## FreeBSD 有四类源：pkg、ports、portsnap、update。

> 注意：
>
> `portsnap` 在 FreeBSD 14 中已经弃用，改为使用 `gitup`（请参考第 3.3 节）：
>
> ````shell-session
> 20230422:
> 	Remove portsnap(8).  Users are encouraged to obtain the ports tree
> 	using git instead.
> ````

> **警告**
>
> FreeBSD 关于弃用 portsnap 的说明：[[HEADS UP] Planned deprecation of portsnap](https://marc.info/?l=freebsd-ports&m=159656662608767&w=2)。
>
> 以下是邮件翻译：
>
> 我们正计划废除在 ports 中使用 portsnap 的做法。
>
> 原因如下 (无特定排序)。
>
> - Portsnap 不支持季度分支，即使在季度分支被创建并改为非 HEAD 软件包的默认值的多年之后。
> - 与 svn 或 git 相比，Portsnap 似乎并不节省磁盘空间，如果你算上元数据（存储的）的话。算上元数据（默认存储在 /var/db/portsnap 中），并且你对 svn 或 git 做一个没有历史记录的相同的比较，并且忽略可能的 ZFS 压缩。也就是说，你用 `svn export` 或 `git clone --depth 1`，你会看到这样的磁盘用量：
>
> ```shell-session
>     342M svnexport
>     426M git
>     477M portsnap
> ```
>
> - Portsnap 也不像 git 那样可以离线工作。使用 git，你可以也可以通过运行 `git pull --unshallow` 轻松添加历史记录。
> - 这种从 portsnap 的迁移与计划中的向 git 的迁移很相称。
> - 另外，根据我们在 Bugzilla 上看到的补丁，使用使用 portsnap 导致人们很容易意外地提交补丁到 Bugzilla，而这些补丁并不容易应用。
> - 由于 portsnap 不支持季度分支，它经常导致用户在错误的分支上进行编译，或最终使用不匹配的软件包。也就是说，他们通过 pkg 从季度分支安装软件包，然后想要定制，因此运行 portsnap 并从 head 编译，这可能会导致问题。正如我们经常看到的那样。即使这种情况没有发生，也会增加故障排除的几率，以确认它没有发生。
>
> 我们知道人们已经习惯了 portsnap，但我们相信：
>
> - 人们应该能够轻松地使用在基本系统或 git 来使用 pkg 的 svnlite（似乎很少有人真正使用 `WITHOUT_SVNLITE`）。
> - 也有可能退回到来获取 tar 或 zip。从 [https://cgit-beta.freebsd.org/ports/](https://cgit-beta.freebsd.org/ports/)，尽管这确实使更新难度增加。
>
> 我们将如何做，按顺序进行：
>
> - 更新 poudriere 以默认使用 svn。这已经完成了：
>
> <https://github.com/freebsd/poudriere/pull/764>
>
> <https://github.com/freebsd/poudriere/commit/bd68f30654e2a8e965fbdc09aad238c8bf5cdc10>
>
> - 更新文档，不再提及 portsnap。这项工作已经在进行中了：
>
>   <https://reviews.freebsd.org/D25800>
>
>   <https://reviews.freebsd.org/D25801>
>
>   <https://reviews.freebsd.org/D25803>
>
>   <https://reviews.freebsd.org/D25805>
>
>   <https://reviews.freebsd.org/D25808>
>
>   <https://svnweb.freebsd.org/changeset/base/363798>
>
>   非常感谢那些已经和正在从事这项工作的人们！
>
> - 让 `WITHOUT_PORTSNAP` 成为默认的基本系统参数。目前还不确定这一点何时会发生。可能在 13.0 之前不会发生，但希望它能生效。
>   
> - 最终，portsnap 服务器的使用率会低至可以被禁用。
>
> 我们欢迎任何有建设性的反馈。所有的意见都会被听取，如果计划需要修改，我们会在几周内把修改后的计划反馈给你。这个过程将需要一些时间，但希望不会对任何人的正常工作流程造成太大的干扰。
>
> Steve (portmgr@)

**对于失去安全支持的版本，请参考最后一节。**

**本文对于一个源列出了多个镜像站，无需全部配置，只需选择其一即可。**

**目前境内没有官方镜像站，以下均为非官方镜像站。**

## pkg 源：pkg 源提供二进制安装包

pkg 的下载路径是 `/var/cache/pkg/`

FreeBSD 中 pkg 源分为系统级和用户级两个配置文件。_不建议_ 直接修改 `/etc/pkg/FreeBSD.conf` （~~但是太麻烦啦，一般我都是直接改这个文件的~~）,因为该文件会随着基本系统的更新而发生改变。

创建用户级源目录:

```shell-session
# mkdir -p /usr/local/etc/pkg/repos
```

### 网易开源镜像站

创建用户级源文件:

```shell-session
# ee /usr/local/etc/pkg/repos/163.conf
```

写入以下内容:

```shell-session
163: {
url: "http://mirrors.163.com/freebsd-pkg/${ABI}/quarterly",
}
FreeBSD: { enabled: no }
```

**故障排除**

> **并非所有源都有 `quarterly` 和 `latest`，具体请看 <https://pkg.freebsd.org/> 。**
>
> **若要获取滚动更新的包，请将 `quarterly` 修改为 `latest`。二者区别见 FreeBSD 手册。请注意, `CURRENT` 版本只有 `latest`：**
>
> > ```shell-session
> > # sed -i '' 's/quarterly/latest/g' /etc/pkg/FreeBSD.conf
> > ```
>
> **若要使用 https,请先安装 `security/ca_root_nss` ,并将 `http` 修改为 `https`,最后使用命令 `# pkg update -f` 刷新缓存即可,下同。**

### 中国科学技术大学开源软件镜像站

创建用户级源文件:

```shell-session
# ee /usr/local/etc/pkg/repos/ustc.conf
```

写入以下内容:

```shell-session
ustc: {
url: "http://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/quarterly",
}
FreeBSD: { enabled: no }
```

### 南京大学开源镜像站

```shell-session
# ee /usr/local/etc/pkg/repos/nju.conf
```

写入以下内容:

```shell-session
nju: {
url: "http://mirrors.nju.edu.cn/freebsd-pkg/${ABI}/quarterly",
}
FreeBSD: { enabled: no }
```

## ports 源:提供源码方式安装软件的包管理器

### 获取 port

这个源是下载 port 本身的源。等于以前的 portsnap。

#### 获取压缩文件方法

```shell-session
# fetch https://mirrors.nju.edu.cn/freebsd-ports/ports.tar.gz
```

或者

```shell-session
# fetch https://mirrors.ustc.edu.cn/freebsd-ports/ports.tar.gz
```

然后

```shell-session
# tar -zxvf ports.tar.gz -C /usr/ports #解压至路径
# rm ports.tar.gz #删除存档
```

#### Git 方法

> 注意：
>
> 请参考第 3.3 节，使用 gitup 可能会更简单。

须提前安装 git：

```shell-session
# pkg install git
```

然后：

```shell-session
# git clone --depth 1 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git /usr/ports
```

### port 源

这个源是下载 port 中的软件的源。

ports 下载路径是 `/usr/ports/distfiles`

> **警告**
>
> ports 源可能并不完整。其余的大概只镜像了不到十分之一。见 <https://github.com/ustclug/discussions/issues/408>。

#### 南京大学开源镜像站

创建或修改文件 `# ee /etc/make.conf`:

写入以下内容:

`MASTER_SITE_OVERRIDE?=http://mirrors.nju.edu.cn/freebsd-ports/distfiles/${DIST_SUBDIR}/`

#### 网易开源镜像站

创建或修改文件 `# ee /etc/make.conf`:

写入以下内容:

`MASTER_SITE_OVERRIDE?=http://mirrors.163.com/freebsd-ports/distfiles/${DIST_SUBDIR}/`

#### 中国科学技术大学开源软件镜像站

创建或修改文件 `# ee /etc/make.conf`:

写入以下内容:

`MASTER_SITE_OVERRIDE?=http://mirrors.ustc.edu.cn/freebsd-ports/distfiles/${DIST_SUBDIR}/`

## portsnap 源:打包的 ports 文件【FreeBSD 14.0 及以后不可用】

**获取 portsnap 更新**

```shell-session
# portsnap auto #同时支持命令行和 cron
```

或

```shell-session
# portsnap fetch extract
```

**故障排除**

```shell-session
Snapshot appears to have been created more than one day into the future!
(Is the system clock correct?)
Cowardly refusing to proceed any further.
```

需要同步时间。

```shell-session
ntpdate ntp.api.bz
```

## freebsd-update 源:提供基本系统更新

注意：只有一级架构的 release 版本才提供该源。也就是说 current 和 stable 是没有的。 关于架构的支持等级说明请看：

[Supported Platforms](https://www.freebsd.org/platforms)

**例:从 FreeBSD 12 升级到 13.0**

`# freebsd-update -r 13.0-RELEASE upgrade`

## 不受安全支持的版本（请酌情使用）

不受安全支持的版本也是可以使用二进制源的。

> 以下，以 `FreeBSD 9.2` 为例：

首先切换成可以用的二进制源

```shell-session
# setenv PACKAGESITE http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest
```

如果 shell 不是 csh，那么:

```shell-session
# export PACKAGESITE=http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest
```

安装示例：现在安装 `bsdinfo`。

```shell-session
root@ykla:~ # pkg_add -r bsdinfo
Fetching http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest/bsdinfo.tbz... Done.
```

**pkg 是不可用的，会提示找不到 `digests.txz` 和 `repo.txz`，因为当时 pkgng 还没有被官方所支持，仍然仅支持使用 `pkg_*` 命令。**
