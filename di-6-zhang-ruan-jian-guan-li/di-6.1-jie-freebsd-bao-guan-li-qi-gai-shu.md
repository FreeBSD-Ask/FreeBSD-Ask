# 6.1 FreeBSD 包管理器概述

## 软件源概览

FreeBSD 提供了多种类型的软件源，分别服务于不同的系统组件与软件安装需求。

对于熟悉 Linux 发行版的读者而言，可将 FreeBSD 的包管理方案类比为两大 Linux 发行版包管理器的功能组合：

- Arch Linux：Pacman，对应 pkg（同样秉持 KISS 理念）。
- Gentoo Linux：Portage，对应 Ports（Portage 本身借鉴自 Ports）。

`pkg install` 可以缩写为 `pkg ins`，其他命令同理。

下表概括了各类软件源的基本信息：

| 软件源 | 简介 | 备注 |
| ------ | ---- | ---- |
| pkg | 类似于传统 Linux 的包管理器，用于安装二进制软件包 | 如果不需要以二进制方式安装软件则无需配置。默认未安装 `pkg`，输入 `pkg` 回车会提示安装。**除 pkgbase 外的 pkg 包实际上都是由 Port 直接构建而来** |
| Ports 框架 | 拉取 Port 的源代码目录（本身不含源代码，只是对第三方软件的描述文件、补丁集和 Makefile）。Ports 是 Port 的集合，在 `freebsd-ports` 存储库中统一维护 | Gentoo 的包管理器 Portage（命令为 `emerge`）正是借鉴于此，用于帮助用户从源代码编译安装第三方软件。也就是说，Ports（Port 集合）类似 Gentoo 的 [ebuild 数据库](https://mirrors.ustc.edu.cn/help/gentoo.html) |
| Ports 源 | 在 Port 中的 Makefile 文件里会定义若干软件包源代码的地址，该软件源用于拉取这些源代码（因为从官方上游拉取速度有时不理想） | 等同于 Gentoo 的 [Distfiles 源](https://mirrors.ustc.edu.cn/help/gentoo.html)。如果不需要以源代码方式编译软件，可以不配置 |
| freebsd-update | 用于更新基本系统（内核 + 用户空间） | 支持 ALPHA、BETA、RC、RELEASE 版本；STABLE/CURRENT 分支不提供二进制更新 |
| pkgbase | 将 FreeBSD 基本系统（内核 + 用户空间）打包成 pkg 包，使用 pkg(8) 管理基本系统，取代传统的 freebsd-update 和 distribution | 从 FreeBSD 15.0 开始可选（技术预览）。14.x 为实验性支持。基本系统升级/维护使用 `pkg upgrade`。生产环境建议继续使用传统方式。需配置 FreeBSD-base 源（见下文）。参考 [PkgBase Wiki](https://wiki.freebsd.org/PkgBase)。pkgbase 实际上由存储库 `freebsd-src` 构建而来，与 Ports 完全无关。FreeBSD 基本系统始终是独立于 Ports 而自存的 |
| kernel modules（kmods） | 内核模块源（包含无线网卡驱动、以太网卡驱动、DRM 显卡驱动等），用于解决小版本之间可能存在的 ABI 不兼容问题 | 参见：Possible solution to the drm-kmod kernel mismatch after upgrade from Bapt[EB/OL]. [2026-03-26]. <https://forums.freebsd.org/threads/possible-solution-to-the-drm-kmod-kernel-mismatch-after-upgrade-from-bapt.96058/#post-682984>、CFT: repository for kernel modules[EB/OL]. [2026-03-26]. <https://lists.freebsd.org/archives/freebsd-ports/2024-December/006997.html>。可以使用命令 `fwget` 自动安装所需固件 |
| FreeBSD（pub） | 提供 ISO 安装镜像、文档、开发资料和 `snapshots`，在系统安装、系统救援和开发参考时有很大帮助 | 此处的 Pub，指的是官方的 <https://ftp.freebsd.org/pub/FreeBSD/>。其性质类似于普通的镜像分发仓库，与 debian-cd、ubuntu-releases 等属于同一类型。目前已知全量同步 FreeBSD（Pub）源的镜像站：<https://mirrors.nju.edu.cn/freebsd>。其提供了完整的目录结构（如 `snapshots`、`development`），且更新较为及时，参见：FreeBSD.org ftp server[EB/OL]. [2026-03-26]. <https://ftp.freebsd.org/pub/FreeBSD/> 目录结构 |

## 理解 pkg 的 quarterly 季度分支与滚动更新的 latest 分支

FreeBSD 的 pkg 分为 quarterly（季度，由 Ports 的 XXXXQY 分支构建而来）分支和 latest（滚动更新，由 Ports 的 main 分支构建而来）分支两个源。quarterly 目前是 FreeBSD 默认的 pkg 软件分支。

```sh
# git clone https://git.FreeBSD.org/ports.git /usr/ports # 克隆 FreeBSD Ports 仓库到 /usr/ports 目录
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

其中，quarterly 的内容由 main 分支（latest）切出，每年的 1 月、4 月、7 月、10 月 ③ 会发布新的分支（从特定时间点的 main 分支切出 ①），形如 `2024Q3`、`2025Q1`。这是为了便于通过 git 直接拉取所需的分支，但 Ports 管理团队（portmgr）仅维护最新分支，旧分支不再接受任何合并。②

quarterly 实际上类似于 Debian 的 Stable 版本，此处的 Stable 不仅表示“稳定”，也包含“固定”的含义。有必要区分“稳定”和“固定”两个词语：

根据 [Merriam‑Webster](https://www.merriam-webster.com/dictionary/stable) 和 [Cambridge Dictionary](https://dictionary.cambridge.org/us/dictionary/english/stable)，Stable 有“fixed”（固定）的意思。查阅《现代汉语词典（第 7 版）》第 1374 页可知，“稳定”的第一个释义为“形容词，稳定安固，没有变动”；第 470 页载“固定”为“动词，不变动或不移动（跟‘流动’相对）”。因此，“固定”是实现“稳定”的一种手段，而“稳定”是一种目的。

> **技巧**
>
> Debian 通过 **固定** 软件包版本、仅接受安全更新而不接受功能更新来实现 **稳定**。其软件源是 **固定的**——Debian 还有 testing 等分支。常见发行版通过 **固定** 软件来实现 **Stable** 版本。由于这些软件包已经历经了从 unstable（即 sid，Ubuntu 即基于此）到 testing 等多个分支的测试和发展，软件包自然比较 **稳定**。在 **Stable** 版本的系统生命周期内，任何软件基本都不会获得大版本更新和功能更新。

quarterly 分支类似于 Debian 的 Stable 版本，固定软件包版本并仅接受安全更新和错误修复，以提供可预测且稳定的用户体验。任何功能性更新都不会回溯至 quarterly 分支。

> **注意**
>
> 并非所有源都提供 `quarterly` 和 `latest`。

### 参考文献

- FreeBSD Project. Ports/QuarterlyBranch[EB/OL]. [2026-03-25]. <https://wiki.freebsd.org/Ports/QuarterlyBranch>. 说明 Ports 季度分支的创建规则与维护策略。
- FreeBSD Project. pkg -- package manager[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=8>. FreeBSD 包管理器手册页。
- Debian. DebianStability[EB/OL]. [2026-03-26]. <https://wiki.debian.org/DebianStability>. 即稳定的意思
- Debian. Chapter 3. Choosing a Debian distribution[EB/OL]. [2026-03-26]. <https://www.debian.org/doc/manuals/debian-faq/choosing.en.html#s3.1.1>. 根据此处实际上是固定的意思
- Debian. 选择一个 Debian 发布版本[EB/OL]. [2026-03-26]. <https://www.debian.org/doc/manuals/debian-faq/choosing.zh-cn.html>. 第 3 章中文版。
- Debian. 2.2. Are there package upgrades in “stable”?[EB/OL]. [2026-03-26]. <https://www.debian.org/doc/manuals/debian-faq/getting-debian.en.html#updatestable>. 此处指出软件不会有功能性更新。
- FreeBSD Project. pkg.freebsd.org[EB/OL]. [2026-03-26]. <https://pkg.freebsd.org/>. 也并非所有架构都提供了 pkg 源，与平台支持等级有关。

## Ports 与 Port 概述

### Ports 历史

Ports 是一种从源代码（也支持闭源二进制包）构建软件的框架。该框架由 Jordan K. Hubbard（<jkh@FreeBSD.org>）创建，最初于 1994 年 8 月公开发布。

```sh
# git log --reverse --max-parents=0 --pretty=format:"commit: %h%nAuthor: %an%nDate: %ci%n%n%B" # 打印第一次提交
commit: d27f048e966a
Author: Jordan K. Hubbard
Date: 1994-08-21 13:12:57 +0000

Commit my new ports make macros.  Still not 100% complete yet by any means
but fairly usable at this stage.
Submitted by:   jkh
```

“提交了为 ports 编写的新 make 宏。虽然还远未完善，但目前已经可以正常使用。”

> **技巧**
>
> 上述示例说明：对于开源项目，无论使用何种版本控制系统，保留完整的提交记录都非常重要。

NetBSD 和 OpenBSD 也使用 Ports，但实现方式并不通用。

#### 参考文献

- FreeBSD-Ports-Announce. Happy 20th birthday FreeBSD ports tree![EB/OL]. (2014-08)[2026-03-25]. <https://lists.freebsd.org/pipermail/freebsd-ports-announce/2014-August/000088.html>. 纪念 FreeBSD Ports 诞生 20 周年，回顾其历史演进与发展历程。

### Ports 与 Port 释义

一款软件的相关文件（补丁文件、校验和、Makefile 等）的集合称为一个 Port，所有 Port（移植软件）的集合即 Ports Collection 或 Ports Tree，简称 Ports。从术语定义角度而言，Port 指单个软件的移植构建配置，Ports 则指整个移植软件集合。

项目结构

```sh
/usr/
└── ports/ # Ports 目录
    ├── accessibility/ # 分类目录
    ├── arabic/
    ├── archivers/
    ├── astro/
    ├── audio/
    ├── benchmarks/
    ├── biology/
    ├── cad/
    ├── chinese/
    ├── comms/
    ├── converters/
    ├── databases/ # 数据库分类
    │   ├── postgresql18-server/ # 单个 Port 示例
    │   │   ├── Makefile # 主文件
    │   │   ├── distinfo # 校验和文件
    │   │   ├── pkg-descr # 软件描述
    │   │   ├── files/ # 补丁文件目录
    │   │   └── pkg-plist-* # 安装文件列表
    │   └── ……其他 Port……
    ├── deskutils/
    ├── devel/
    ├── dns/
    ├── editors/
    ├── emulators/
    ├── finance/
    ├── french/
    ├── ftp/
    ├── games/
    ├── german/
    ├── graphics/
    ├── hebrew/
    ├── hungarian/
    ├── irc/
    ├── japanese/
    ├── java/
    ├── korean/
    ├── lang/
    ├── mail/
    ├── math/
    ├── misc/
    ├── multimedia/
    ├── net/
    ├── net-im/
    ├── net-mgmt/
    ├── net-p2p/
    ├── news/
    ├── polish/
    ├── portuguese/
    ├── print/
    ├── russian/
    ├── science/
    ├── security/
    ├── shells/
    ├── sysutils/
    ├── textproc/
    ├── ukrainian/
    ├── vietnamese/
    ├── www/
    ├── x11/
    ├── x11-clocks/
    ├── x11-drivers/
    ├── x11-fm/
    ├── x11-fonts/
    ├── x11-servers/
    ├── x11-themes/
    ├── x11-toolkits/
    ├── x11-wm/
    ├── ports-mgmt/
    ├── Mk/
    ├── Templates/
    ├── Tools/
    ├── Keywords/
    ├── distfiles/ # 下载源文件目录
    ├── COPYRIGHT
    ├── GIDs
    ├── UIDs
    ├── README
    ├── CHANGES
    ├── MOVED
    ├── UPDATING
    ├── Makefile
    └── CONTRIBUTING.md
```

查看 Ports 框架结构：

```sh
$ cd /usr/ports # 切换到 /usr/ports
$ ls # 列出此目录下所有文件  ①
accessibility	COPYRIGHT	GIDs		misc		README		www
arabic		databases	graphics	Mk		russian		x11
archivers	deskutils	hebrew		MOVED		science		x11-clocks
astro		devel		hungarian	multimedia	security	x11-drivers
audio		dns		irc		net		shells		x11-fm
benchmarks	editors		japanese	net-im		sysutils	x11-fonts
biology		emulators	java		net-mgmt	Templates	x11-servers
cad		filesystems	Keywords	net-p2p		textproc	x11-themes
CHANGES		finance		korean		news		Tools		x11-toolkits
chinese		french		lang		polish		UIDs		x11-wm
comms		ftp		mail		ports-mgmt	ukrainian
CONTRIBUTING.md	games		Makefile	portuguese	UPDATING
converters	german		math		print		vietnamese
$ ls databases/ # 切换到 databases 数据库分类目录下
adminer						php-xapian
adodb5						php81-dba

    ……省略一部分……

mongodb60					py-apache-arrow
mongodb70					py-apsw
mongodb80					py-asyncmy
mongosh						py-asyncpg
$ cd databases/postgresql18-server # 切换到 postgresql18-server 目录
ykla@ykla:/usr/ports/databases/postgresql18-server $ ls ②
distinfo		pkg-descr		pkg-plist-contrib	pkg-plist-pltcl
files			pkg-install-server	pkg-plist-plperl	pkg-plist-server
Makefile		pkg-plist-client	pkg-plist-plpython
```

- ① **/usr/ports** 这个文件夹整体称作 Ports，包括几十种不同的分类目录，每个目录下有若干 Port。
- ② **/usr/ports/databases/postgresql18-server** 这个文件夹整体称作一个 Port，由 `distinfo`（校验和文件）、`pkg-descr`（软件描述文件）、`Makefile`（主文件，包含构建方法、版本号及下载方式等）、`pkg-plist`（安装文件列表及其权限和属组信息）、`files`（一般为补丁文件，该 Port 下还包含安装后的说明文件 `pkg-message`）等文件构成。

之所以称为“Ports Collection”（移植集合，不应理解为“端口集合”），是因为这些软件绝大部分并不由 FreeBSD 控制、管理和维护。Port 提交者的主要工作是将 FreeBSD 上的 Port 更新到上游开发者提供的最新版本，删除上游不再维护的软件 Port。如果上游不接受 BSD 特有的 PR 补丁，或难以直接通过既有 Ports 框架构建，Port 维护者也需要自行复刻一个分支来维护。

## Ports 构建 pkg 软件包的流程

Ports 框架可以将源代码编译并打包成 pkg 格式的二进制包，完整构建流程如下图所示。

![pkg 构建流程图](../.gitbook/assets/portstopkg.png)

> **注意**
>
> 可以同时使用 Ports 和 pkg，多数用户也是如此。但需要注意 Ports 和 pkg 应使用同一分支：如果 Ports 使用 main 分支，则 pkg 应使用 latest 源；如果 Ports 使用 quarterly 分支，则 pkg 应使用 quarterly 源。分支不一致会导致依赖问题（例如 SSL）。latest 源也比 main 分支下的 Ports 发布更晚（其软件包由 main 构建而来），因此即使使用 latest 源，也可能会出现上述问题。遇到问题时卸载 pkg 安装的包，重新使用 Ports 编译即可。

> **警告**
>
> 如果通过 `make config` 修改了 Port 的默认构建参数，且希望保留该自定义设置，则后续不应通过 pkg 更新该软件，否则 pkg 安装的软件包将覆盖自定义参数。

下图为 Ports 构建软件包的详细流程：

![Ports 流程图](../.gitbook/assets/ports-pkg.png)

> **技巧**
>
> Ports 的下载路径是 **/usr/ports/distfiles/**。

```sh
/usr/ports/
└── distfiles/ # Ports 的下载路径
```

## 课后习题

1. 尝试让 Portsnap 工具复活，弥补其原有欠缺的功能，使之现代化。
2. 比较 FreeBSD pkg 仓库、Debian APT 仓库与 Arch Linux pacman 仓库的元数据签名链机制，分析各方案在供应链攻击场景下的防护能力差异。
3. 软件源镜像体系是一种去中心化分发架构。分析镜像站志愿运营模式与商业 CDN 模式在可持续性、审查抗性与分发效率三个维度上的优劣，并提出一种混合分发方案。
