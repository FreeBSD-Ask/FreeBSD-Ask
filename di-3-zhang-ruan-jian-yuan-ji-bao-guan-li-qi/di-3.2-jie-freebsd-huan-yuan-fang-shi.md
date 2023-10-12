# 第 3.2 节 FreeBSD 换源方式

FreeBSD 有四类源：pkg、ports、portsnap、update。

> 注意：
>
> `portsnap` 在 FreeBSD 14 中已经弃用，改为使用 `gitup`（请参考第 3.3 节）：
>
> ```shell-session
> 20230422:
> 	Remove portsnap(8).  Users are encouraged to obtain the ports tree
> 	using git instead.
> 	```
>

> 赞助我们：
>
> freebsd.cn **永久下线**，目前正在与 NJU 进行沟通软件源问题。本教程待补充。freebsd.cn 镜像站大概需要 100M 的 CN2 宽带。要求 HK 最好。有 10T+ 硬盘。如能提供者请通过微信公众号发送你的微信号，我加你好友。或者发你微信的二维码到 <ykla@bsdcn.org>

**对于失去安全支持的版本，请参考最后一节。**

**本文对于一个源列出了多个镜像站，无需全部配置，只需选择其一即可。**

**目前境内没有官方镜像站，以下均为非官方镜像站。**

## pkg 源:pkg 源提供二进制安装包

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

>**并非所有源都有 `quarterly` 和 `latest`，具体请看 <https://pkg.freebsd.org/> 。**
>
>**若要获取滚动更新的包，请将 `quarterly` 修改为 `latest`。二者区别见 FreeBSD 手册。请注意, `CURRENT` 版本只有 `latest`：**
>
>>```shell-session
>># sed -i '' 's/quarterly/latest/g' /etc/pkg/FreeBSD.conf
>>```
>
>**若要使用 https,请先安装 `security/ca_root_nss` ,并将 `http` 修改为 `https`,最后使用命令 `# pkg update -f` 刷新缓存即可,下同。**

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

