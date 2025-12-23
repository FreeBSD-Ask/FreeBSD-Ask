# 5.2 更换 FreeBSD 软件源

## FreeBSD 包管理器设计理念

熟悉 Linux 的人也许会发现，FreeBSD 的包管理方案实际上大约等于以下两大 Linux 发行版包管理器的完美合体：

- Arch Linux：Pacman，对应 pkg（同样秉持 KISS 的理念）
- Gentoo Linux：Portage，对应 Ports（Portage 本身就是 Ports 的仿制品）

|源 | 说明 | 备注|
|:---:|:---|:---|
|pkg|类似于传统 Linux 的包管理器，用于安装二进制软件包 | 如果不需要以二进制方式安装软件可以不配置，默认未安装 `pkg`，输入 `pkg` 回车会提示安装|
|~~portsnap~~|拉取 Ports 的源代码模板（本身不含源代码，只是一些描述文件和补丁集）。换言之，这个源类似 Gentoo 的 [ebuild 数据库](https://mirrors.ustc.edu.cn/help/gentoo.html)|**已于 FreeBSD 14 及后续版本废弃，无需配置** 改用 `git`、`gitup` 和压缩包 `ports.tar.gz` 等方式获取。|
|ports|Gentoo 的包管理器 Portage（命令为 `emerge`）即是源于此。用于帮助用户从源代码编译安装软件。换言之，等同于 Gentoo 的 [Distfiles 源](https://mirrors.ustc.edu.cn/help/gentoo.html)|不需要源代码方式编译软件可以不配置。|
|update|用于更新基本系统（内核 + 用户空间） | 预计在 FreeBSD 15 或 16 中废弃，转而使用 [pkgbase](https://wiki.freebsd.org/PkgBase) 代替之|
|kernel modules（kmods）| 内核模块源（包含无线网卡驱动、以太网卡驱动、DRM 显卡驱动等），用于解决小版本之间可能存在的 ABI 不兼容问题 | 参见 [Possible solution to the drm-kmod kernel mismatch after upgrade from Bapt](https://forums.freebsd.org/threads/possible-solution-to-the-drm-kmod-kernel-mismatch-after-upgrade-from-bapt.96058/#post-682984)、[CFT: repository for kernel modules](https://lists.freebsd.org/archives/freebsd-ports/2024-December/006997.html)。可以使用命令 `fwget` 自动安装所需驱动|
|FreeBSD（pub） |提供 ISO 安装镜像、文档、开发资料、`snapshots`，在系统安装、系统救援和开发参考时有很大帮助 | 参考 [FreeBSD.org ftp server](http://ftp.freebsd.org/pub/FreeBSD/) 目录结构。 |


> **技巧**
>
> 本文对于一个源列出了多个镜像站，无须全部配置，只需选择其一即可。

目前境内没有官方镜像站，以下均为非官方镜像。

> **注意**
>
> [NJU](https://github.com/nju-lug/NJU-Mirror-Issue/issues/54) 和 163 均同步自 USTC 而非 FreeBSD 直接上游。

>**警告**
>
>对于那些以安全性为较高优先级的用户来说，应该使用默认的官方镜像 `pkg.freebsd.org`！其由官方构建、分发和维护，且不受境内网络监管。


## pkg 源：pkg 源提供了二进制软件包

境内的源一般只支持 aarch64（arm64）和 amd64 两个架构。

FreeBSD 中的 pkg 源分为系统级和用户级两个配置文件。**不建议** 直接修改 `/etc/pkg/FreeBSD.conf` ~~但是太麻烦啦，一般我都是直接改这个文件的~~，因为该文件会随着基本系统的更新而发生改变。

>**警告**
>
> 请勿同时启用多个 pkg 镜像站，无论是官方镜像站（如 `pkg.freebsd.org` 与 USTC 混用），还是境内非官方镜像站（如 USTC 和 NJU 混用）都不要混合使用！后果类似于 FreeBSD 季度分支的 Ports 和 latest 分支的 pkg 混用，可能会破坏软件的依赖关系。案例：[混用导致 KDE 桌面被删除](https://blog.mxdyeah.top/mxdyeah_blog_post/freebsd_exp_kde6.html)。

### 理解 quarterly 季度分支

FreeBSD 的 pkg 分为 quarterly（季度，由 Ports 的 XXXXQY 分支构建而来）分支和 latest（实时更新，由 Ports 的 main 分支构建而来）分支两个源。quarterly 目前是 FreeBSD 默认的 pkg 软件分支。

```sh
# git clone https://git.FreeBSD.org/ports.git /usr/ports # 克隆 FreeBSD ports 仓库到 /usr/ports 目录
正克隆到 '/usr/ports'...
remote: Enumerating objects: 6715646, done.
remote: Counting objects: 100% (936/936), done.
remote: Compressing objects: 100% (120/120), done.
remote: Total 6715646 (delta 923), reused 816 (delta 816), pack-reused 6714710 (from 1)
接收对象中: 100% (6715646/6715646), 1.50 GiB | 10.26 MiB/s, 完成.
处理 delta 中: 100% (4065984/4065984), 完成.
正在更新文件: 100% (168004/168004), 完成.
root@ykla:/home/ykla # cd /usr/ports/ # 切换到 git 的 Ports 路径
root@ykla:/usr/ports # git branch -a # 列出本地所有分支
* main
  remotes/origin/2014Q1
  remotes/origin/2014Q2
  remotes/origin/2014Q3
  remotes/origin/2014Q4

     ……省略一部分……

  remotes/origin/2025Q2
  remotes/origin/2025Q3
  remotes/origin/2025Q4
  remotes/origin/HEAD -> origin/main # 可以看到 main 是默认分支
  remotes/origin/main
root@ykla:/usr/ports # git for-each-ref --sort=-committerdate --format='%(committerdate:short) %(authorname) %(refname:short) %(objectname:short)' refs/remotes/ # 列出所有分支及最后提交者与时间 ①
2025-10-24 Hiroki Tagato origin be5283280c16
2025-10-24 Hiroki Tagato origin/main be5283280c16
2025-10-23 Colin Percival origin/2025Q4 060d3d65fcbb
2025-10-14 Bryan Drewery origin/2025Q3 9f09f84b2dd5
2025-07-01 FiLiS origin/2025Q2 c339266c40e5

  ……省略一部分……

2015-07-23 Palle Girgensohn origin/2015Q2 7d7c2271f6c9
2015-04-09 Alonso Schaich origin/2015Q1 5bd325869bde
2014-10-01 Bryan Drewery origin/2014Q3 a0ccd6f83108
2014-06-28 Thomas Zander origin/2014Q2 a3377806e58e
2014-03-29 Lars Engels origin/2014Q1 5f4d6e1d6b07
root@ykla:/usr/ports # git merge-base origin/main origin/2025Q4 # 查找两个分支的最近共同祖先 commit
6c256c6adb790f0588b920d41a5fe4dfa550079f
root@ykla:/usr/ports # git branch -r --contains 6c256c6adb790f0588b920d41a5fe4dfa550079f # 列出哪些远程分支历史中包含此 commit ②
  origin/2025Q4
  origin/HEAD -> origin/main
  origin/main
root@ykla:/usr/ports # for branch in $(git branch -r | grep -v HEAD); do # 查看分支创建的时间 ③
>   mb=$(git merge-base origin/main $branch)
>   date=$(git show -s --format='%ci' $mb)
>   echo "$branch created around $date"
> done

origin/2014Q1 created around 2013-12-16 08:00:15 +0000
origin/2014Q2 created around 2014-04-01 12:02:40 +0000
origin/2014Q3 created around 2014-07-01 10:13:26 +0000
origin/2014Q4 created around 2014-10-01 06:43:32 +0000
origin/2015Q1 created around 2015-01-01 14:35:03 +0000
origin/2015Q2 created around 2015-04-01 12:19:37 +0000
origin/2015Q3 created around 2015-07-01 12:12:08 +0000
origin/2015Q4 created around 2015-10-01 19:24:12 +0000

……省略一部分……

origin/2024Q4 created around 2024-10-07 20:46:12 +0200
origin/2025Q1 created around 2025-01-05 11:22:53 +0100
origin/2025Q2 created around 2025-04-01 12:58:51 +0200
origin/2025Q3 created around 2025-07-01 22:32:34 +0300
origin/2025Q4 created around 2025-10-01 21:27:17 +0200
origin/main created around 2025-10-24 12:43:02 +0900
```


其中，quarterly 的内容由 main 分支（latest）的提交回溯而来，每年的 1 月、4 月、7 月、10 月 ③ 会发布新的分支（从特定时间点的 main 分支切出 ①），形如 `2014Q3`、`2025Q1`。这是为了便于通过 git 直接拉取所需的分支，但 Ports 管理团队（portmgr）只会维护最新分支，旧分支不再允许任何合并。②

quarterly 实际上类似于 Debian 的 Stable 版本，此处的 Stable 不仅表示“稳定”，也包含“固定”的含义。我们有必要区分“稳定”和“固定”两个词语：

根据 [Merriam‑Webster](https://www.merriam-webster.com/dictionary/stable) 和 [Cambridge Dictionary](https://dictionary.cambridge.org/us/dictionary/english/stable)，Stable 有“fixed”（固定）的意思。我们来看一下《现代汉语词典（第 7 版）》第 1374 页，就会发现“稳定”第一个释义被解释为“形容词，稳定安固，没有变动”；第 470 页载“固定”为“动词，不变动或不移动（跟‘流动’相对）”。因此，“固定”是实现“稳定”的一种手段，而“稳定”是一种目的。

>**技巧**
>
>Debian 是通过 **固定** 软件包的版本，仅接受安全更新不接受功能更新来实现的 **稳定**，手段是其软件源是 **固定**，Stable 系统的软件源也是 Stable 分支的——Debian 还有 testing 等分支。我们可以看到常见发行版是通过 **固定** 软件来实现的 **Stable** 版本。由于这些软件包已经历经了从 unstable（即 sid，Ubuntu 即基于此）testing 等多个分支的测试和发展，软件包自然比较 **稳定**。而且在 **Stable** 版本的系统生命周期内，任何软件基本上都不会得到大版本更新和功能更新。参见 [DebianStability](https://wiki.debian.org/DebianStability)（看起来是稳定的意思）、[Chapter 3. Choosing a Debian distribution](https://www.debian.org/doc/manuals/debian-faq/choosing.en.html#s3.1.1)（实际上是固定的意思），中文版在 [第 3 章 选择一个 Debian 发布版本](https://www.debian.org/doc/manuals/debian-faq/choosing.zh-cn.html)、[2.2. Are there package upgrades in "stable"?](https://www.debian.org/doc/manuals/debian-faq/getting-debian.en.html#updatestable) 指出软件不会有功能性更新。

FreeBSD pkg 的 quarterly 分支也试图实现相同的目的（提供可预测和稳定的用户体验），也是通过 **非功能性更新** 来实现的——除非涉及 Ports 框架、安全更新（故并非完全禁止版本更替）、简单错误修复（构建、编译、打包）等。任何功能性更新都不会被回溯至 quarterly 分支。可以看出 FreeBSD 的 quarterly 也同时兼有稳定和固定的双重含义。

>**注意**
>
>并非所有源都提供 `quarterly` 和 `latest`，具体请参见 <https://pkg.freebsd.org/> 。也并非为所有架构都提供了 pkg 源，与平台支持等级挂钩。

#### 参考文献

- [Wiki QuarterlyBranch](https://wiki.freebsd.org/Ports/QuarterlyBranch)

### pkg 换源

若要获取滚动更新的包，请将 `quarterly` 修改为 `latest`。二者区别见 FreeBSD 手册。请注意，`CURRENT` 版本只有 `latest`。

使用命令修改系统级 pkg 源使用 latest：

```sh
# sed -i '' 's/quarterly/latest/g' /etc/pkg/FreeBSD.conf
```


#### 创建用户级源目录和文件

```sh
# mkdir -p /usr/local/etc/pkg/repos  # 创建 pkg 仓库配置目录
# ee /usr/local/etc/pkg/repos/mirrors.conf  # 使用 ee 编辑器创建或修改 mirrors.conf 配置文件
```

#### 中国科学技术大学开源软件镜像站（USTC）

> **技巧**
>
> 视频教程见 [005-FreeBSD14.2 更换 pkg 源为 USTC 镜像站](https://www.bilibili.com/video/BV13ji2YLEkV)

写入以下内容：

```sh
ustc: {
url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/latest"
}
FreeBSD: { enabled: no }
```

#### 南京大学开源镜像站

写入以下内容：

```sh
nju: {
url: "https://mirrors.nju.edu.cn/freebsd-pkg/${ABI}/latest"
}
FreeBSD: { enabled: no }
```

#### 网易开源镜像站

写入以下内容：

```sh
163: {
url: "https://mirrors.163.com/freebsd-pkg/${ABI}/latest"
}
FreeBSD: { enabled: no }
```

## ports 源：以源代码方式编译安装软件的包管理器

### 下载 ports

该源用于下载 ports 本身的源代码，等同于以前的 `portsnap`。


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

> **注意**
>
> `--depth 1` 会给服务器带来较大计算压力，请尽量使用参数 `--filter=tree:0`。

#### 下载压缩文件的方法

> **警告**
>
> 通过下载 Ports 的压缩文件来使用 Ports 属于一次性方式：Ports 后续无法更新，建议优先采用 Git 方法。


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

该源用于下载 ports 中软件的源代码。


> **警告**
>
> ports 源可能并不完整，其内容大约只镜像了不到十分之一。见 <https://github.com/ustclug/discussions/issues/408>。

创建或修改文件 :

```sh
# ee /etc/make.conf
```


#### 南京大学开源镜像站


写入以下内容：

```sh
MASTER_SITE_OVERRIDE?=https://mirrors.nju.edu.cn/freebsd-ports/distfiles/${DIST_SUBDIR}/
```

#### 网易开源镜像站

写入以下内容：

```sh
MASTER_SITE_OVERRIDE?=https://mirrors.163.com/freebsd-ports/distfiles/${DIST_SUBDIR}/
```

#### 中国科学技术大学开源软件镜像站


写入以下内容：

```sh
MASTER_SITE_OVERRIDE?=https://mirrors.ustc.edu.cn/freebsd-ports/distfiles/${DIST_SUBDIR}/
```

## Kernel modules（kmods）内核模块源：面向 FreeBSD 14.2 及更高版本（不含 15.0-CURRENT）

- 对于 14.2-RELEASE：新建文件夹 `/usr/local/etc/pkg/repos`（即 `mkdir -p /usr/local/etc/pkg/repos`），再新建文件 `/usr/local/etc/pkg/repos/FreeBSD-kmods.conf`。
- \> 14.2-RELEASE：编辑 `/etc/pkg/FreeBSD.conf`。

### FreeBSD 官方源

写入：

#### quarterly 分支

```sh
FreeBSD-kmods {
	url: pkg+https://pkg.freebsd.org/${ABI}/kmods_quarterly_${VERSION_MINOR}
	signature_type: "fingerprints"
	fingerprints: "/usr/share/keys/pkg"
	mirror_type: "srv"
	enabled: yes
}
```

#### latest 分支

```sh
FreeBSD-kmods {
	url: pkg+https://pkg.freebsd.org/${ABI}/kmods_latest_${VERSION_MINOR}
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
	url: https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_quarterly_${VERSION_MINOR}
	enabled: yes
}
```

#### latest 分支

```sh
FreeBSD-kmods {
	url: https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_latest_${VERSION_MINOR}
	enabled: yes
}
```


## 不受安全支持的版本（请酌情使用）

> **技巧**
>
> 网易开源镜像站还提供了 FreeBSD 11、12 等过期版本的 pkg 二进制源。可自行配置使用。

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
# pkg_add -r bsdinfo
Fetching http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest/bsdinfo.tbz... Done.
```

> **注意**
>
> pkg 是不可用的，会提示找不到 `digests.txz` 和 `repo.txz`，因为当时 pkgng 还没有被官方所支持，仍然仅支持使用 `pkg_*` 命令。

## FreeBSD（Pub）源：提供 ISO 安装镜像、文档、开发资料以及各种架构的 `snapshot`

此处的 Pub，指的是官方的 <http://ftp.freebsd.org/pub/FreeBSD/>。其性质类似于普通的镜像分发仓库，与 debian-cd、ubuntu-releases 等属于同一类型。

目前已知全量同步 FreeBSD（Pub）源的镜像站：<https://mirrors.nju.edu.cn/freebsd>。其提供了完整的目录结构（如 `snapshots`、`development`），且更新及时。

## 参考文献

- [FreeBSD ports](https://mirrors.ustc.edu.cn/help/freebsd-ports.html)，USTC Mirrors 换源帮助
- [FreeBSD pkg](https://mirrors.ustc.edu.cn/help/freebsd-pkg.html)，USTC Mirrors 换源帮助
