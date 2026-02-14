# 5.2 更换 FreeBSD 软件源

## 软件源概览



|源 | 说明 | 备注|
|:---:|:---|:---|
|pkg|类似于传统 Linux 的包管理器，用于安装二进制软件包 | 如果不需要以二进制方式安装软件可以不配置，默认未安装 `pkg`，输入 `pkg` 回车会提示安装|
|ports|Gentoo 的包管理器 Portage（命令为 `emerge`）即是源于此。用于帮助用户从源代码编译安装软件。换言之，等同于 Gentoo 的 [Distfiles 源](https://mirrors.ustc.edu.cn/help/gentoo.html) [备份](https://web.archive.org/web/20260120222541/https://mirrors.ustc.edu.cn/help/gentoo.html)|不需要源代码方式编译软件可以不配置。|
|freebsd-update|用于更新基本系统（内核 + 用户空间） | 预计在 FreeBSD 16 中退役，转而使用 pkgbase|
|pkgbase|将 FreeBSD 基本系统（内核 + 用户空间）打包成 pkg 包，使用 pkg(8) 管理基本系统的方式，取代传统的 freebsd-update 和 distribution |从 FreeBSD 15.0 开始可选（技术预览，在整个 15.X 周期内可选），预计在 16.0 成为默认/标准方式。14.X 为实验性支持，可使用 pkgbasify 工具转换。基本系统升级/维护使用 `pkg upgrade`。生产环境建议继续使用传统方式。需配置 FreeBSD-base 源（见下文）。参考 [PkgBase Wiki](https://wiki.freebsd.org/PkgBase)[备份](https://web.archive.org/web/20260120222940/https://wiki.freebsd.org/action/show/pkgbase?action=show&redirect=PkgBase) |
|kernel modules（kmods）| 内核模块源（包含无线网卡驱动、以太网卡驱动、DRM 显卡驱动等），用于解决小版本之间可能存在的 ABI 不兼容问题 | 参见 [Possible solution to the drm-kmod kernel mismatch after upgrade from Bapt](https://forums.freebsd.org/threads/possible-solution-to-the-drm-kmod-kernel-mismatch-after-upgrade-from-bapt.96058/#post-682984) [备份](https://web.archive.org/web/20260120222509/https://forums.freebsd.org/threads/possible-solution-to-the-drm-kmod-kernel-mismatch-after-upgrade-from-bapt.96058/#post-682984)、[CFT: repository for kernel modules](https://lists.freebsd.org/archives/freebsd-ports/2024-December/006997.html) [备份](https://web.archive.org/web/20251207043842/https://lists.freebsd.org/archives/freebsd-ports/2024-December/006997.html)。可以使用命令 `fwget` 自动安装所需驱动|
|FreeBSD（pub） |提供 ISO 安装镜像、文档、开发资料、`snapshots`，在系统安装、系统救援和开发参考时有很大帮助 | 此处的 Pub，指的是官方的 <http://ftp.freebsd.org/pub/FreeBSD/>。其性质类似于普通的镜像分发仓库，与 debian-cd、ubuntu-releases 等属于同一类型。目前已知全量同步 FreeBSD（Pub）源的镜像站：<https://mirrors.nju.edu.cn/freebsd>。其提供了完整的目录结构（如 `snapshots`、`development`），且更新较为及时，参见 [FreeBSD.org ftp server](http://ftp.freebsd.org/pub/FreeBSD/) [备份](https://web.archive.org/web/20260122042612/https://download.freebsd.org/ftp/) 目录结构。 |

### 理解 quarterly 季度分支与滚动更新的 latest 分支

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

根据 [Merriam‑Webster](https://www.merriam-webster.com/dictionary/stable) [备份](https://web.archive.org/web/20260121073246/https://www.merriam-webster.com/dictionary/stable) 和 [Cambridge Dictionary](https://dictionary.cambridge.org/us/dictionary/english/stable)，Stable 有“fixed”（固定）的意思。我们来看一下《现代汉语词典（第 7 版）》第 1374 页，就会发现“稳定”第一个释义被解释为“形容词，稳定安固，没有变动”；第 470 页载“固定”为“动词，不变动或不移动（跟‘流动’相对）”。因此，“固定”是实现“稳定”的一种手段，而“稳定”是一种目的。

>**技巧**
>
>Debian 是通过 **固定** 软件包的版本，仅接受安全更新不接受功能更新来实现的 **稳定**，手段是其软件源是 **固定**，Stable 系统的软件源也是 Stable 分支的——Debian 还有 testing 等分支。我们可以看到常见发行版是通过 **固定** 软件来实现的 **Stable** 版本。由于这些软件包已经历经了从 unstable（即 sid，Ubuntu 即基于此）testing 等多个分支的测试和发展，软件包自然比较 **稳定**。而且在 **Stable** 版本的系统生命周期内，任何软件基本上都不会得到大版本更新和功能更新。参见 [DebianStability](https://wiki.debian.org/DebianStability) [备份](https://web.archive.org/web/20260121103142/https://wiki.debian.org/DebianStability)（看起来是稳定的意思）、[Chapter 3. Choosing a Debian distribution](https://www.debian.org/doc/manuals/debian-faq/choosing.en.html#s3.1.1) [备份](https://web.archive.org/web/20260121073434/https://www.debian.org/doc/manuals/debian-faq/choosing.en.html#s3.1.1)（实际上是固定的意思），中文版在 [第 3 章 选择一个 Debian 发布版本](https://www.debian.org/doc/manuals/debian-faq/choosing.zh-cn.html) [备份](https://web.archive.org/web/20251220152433/https://www.debian.org/doc/manuals/debian-faq/choosing.zh-cn.html)、[2.2. Are there package upgrades in "stable"?](https://www.debian.org/doc/manuals/debian-faq/getting-debian.en.html#updatestable) [备份](https://web.archive.org/web/20251210090450/https://www.debian.org/doc/manuals/debian-faq/getting-debian.en.html#updatestable) 指出软件不会有功能性更新。

FreeBSD pkg 的 quarterly 分支也试图实现相同的目的（提供可预测和稳定的用户体验），也是通过 **非功能性更新** 来实现的——除非涉及 Ports 框架、安全更新（故并非完全禁止版本更替）、简单错误修复（构建、编译、打包）等。任何功能性更新都不会被回溯至 quarterly 分支。可以看出 FreeBSD 的 quarterly 也同时兼有稳定和固定的双重含义。

>**注意**
>
>并非所有源都提供 `quarterly` 和 `latest`，具体请参见 <https://pkg.freebsd.org/> 。也并非为所有架构都提供了 pkg 源，与平台支持等级有关。

### 参考文献

- [Wiki QuarterlyBranch](https://wiki.freebsd.org/Ports/QuarterlyBranch) [备份](https://web.archive.org/web/20260120222534/https://wiki.freebsd.org/Ports/QuarterlyBranch)

## 15.0-RELEASE 快速切换软件源到中国科学技术大学开源镜像站

该配置要求读者在安装过程中就使用了 pkgbase 方式。可以帮助读者配置 pkg 二进制包源（ports 构建而来）、pkgbase 源、内核模块源。

使用 ee 编辑器打开 `/usr/local/etc/pkg/repos/FreeBSD.conf` 文件。

>**技巧**
>
>如果提示文件不存在或打开后内容并非 `FreeBSD-base: { enabled: yes }`，则本小节不适用。请按下文内容手动配置。

清空 `FreeBSD.conf` 中原有内容 `FreeBSD-base: { enabled: yes }`。

写入以下内容：

```sh
USTC-ports: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/quarterly",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}

FreeBSD-ports: { enabled: no }

USTC-ports-kmods: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_quarterly_${VERSION_MINOR}",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}

FreeBSD-ports-kmods: { enabled: no }

USTC-base: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_release_${VERSION_MINOR}",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkgbase-${VERSION_MAJOR}",
  enabled: yes
}
```

随后运行命令 `pkg update -f` 刷新软件源即可。

>**技巧**
>
>可以简单的将上述配置中的两个 `quarterly` 都替换成 `latest` 来使用滚动更新的软件源。

## pkg 二进制包（由 Ports 构建的二进制包）换源

FreeBSD 中的 pkg 源分为系统级和用户级两个配置文件。**不建议** 直接修改 `/etc/pkg/FreeBSD.conf`，**因为该文件会随着基本系统的更新而发生改变。**

>**警告**
>
> 请勿同时启用多个 pkg 镜像站，无论是官方镜像站（如 `pkg.freebsd.org` 与 USTC 混用），还是境内非官方镜像站都不建议混合使用！后果类似于 FreeBSD 季度分支的 Ports 和 latest 分支的 pkg 混用，可能会破坏软件的依赖关系。案例：[混用导致 KDE 桌面被删除](https://blog.mxdyeah.top/mxdyeah_blog_post/freebsd_exp_kde6.html) [备份](https://web.archive.org/web/20260121073302/https://blog.mxdyeah.com/post/freebsd_exp_kde6)。

>**警告**
>
>请勿同时混用 `quarterly` 和 `latest`，在所有配置文件中尽量保持一致。

若要获取滚动更新的包，请将 `quarterly` 修改为 `latest`。二者区别参见上文。**请注意，对于 `CURRENT` 版本默认只提供了 `latest`。**

示例：使用命令修改系统级 pkg 源使用 latest：

```sh
# sed -i '' 's/quarterly/latest/g' /etc/pkg/FreeBSD.conf
```

### 14.X-RELEASE

#### 创建用户级源目录和文件

创建 pkg 仓库配置目录:

```sh
# mkdir -p /usr/local/etc/pkg/repos
```

使用 `ee` 编辑器打开配置文件 `/usr/local/etc/pkg/repos/USTC.conf`（将自动创建文本文件 `USTC.conf`）:

```sh
# ee /usr/local/etc/pkg/repos/USTC.conf
```

>**注意**
>
>在本文中，`/usr/local/etc/pkg/repos/USTC.conf` 将是 pkg 二进制源、模块源和 pkgbase 源共用的配置文件。不再赘述这一过程。

#### 中国科学技术大学开源软件镜像站

编辑 `/usr/local/etc/pkg/repos/USTC.conf` 文件，写入以下配置之一：

- quarterly：

```sh
USTC: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/quarterly"
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
FreeBSD: { enabled: no }
```

- latest：

```sh
USTC: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/latest"
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
FreeBSD: { enabled: no }
```

### 15.0-RELEASE

自 `FreeBSD 15.0-RELEASE` 以降，`FreeBSD` 源的名称，由 `FreeBSD-kmods` 变更为 `FreeBSD-ports`。

#### 官方源

欲了解更多，参见源代码 [usr.sbin/pkg/FreeBSD.conf.quarterly-release](https://github.com/freebsd/freebsd-src/blob/releng/15.0/usr.sbin/pkg/FreeBSD.conf.quarterly-release)。下同。

这是 15.0-RELEASE 系统安装完成后默认的软件源。

#### 中国科学技术大学开源软件镜像站

编辑 `/usr/local/etc/pkg/repos/USTC.conf` 文件，写入以下配置之一：

- quarterly 分支：

```sh
USTC-ports: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/quarterly",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
FreeBSD-ports: { enabled: no }
```

- latest 分支：

```sh
USTC-ports: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/latest",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
FreeBSD-ports: { enabled: no }
```

## 内核模块源（Kernel modules, kmods）

### 14.X-RELEASE

#### 中国科学技术大学开源软件镜像站

编辑 `/usr/local/etc/pkg/repos/USTC.conf`，写入以下配置之一：

- quarterly 分支：

```sh
USTC-kmods:  {
  url: https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_quarterly_${VERSION_MINOR}
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
```

- latest 分支：

```sh
USTC-kmods: {
  url: https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_latest_${VERSION_MINOR}
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
```

### 15.0-RELEASE

自 `FreeBSD 15.0-RELEASE` 以降，`kmods` 源的名称，由 `FreeBSD-kmods` 变更为 `FreeBSD-kmods-ports`。

#### 中国科学技术大学开源镜像站

编辑 `/usr/local/etc/pkg/repos/USTC.conf` 文件，写入以下配置之一：

- quarterly 分支：

```sh
USTC-ports-kmods: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_quarterly_${VERSION_MINOR}",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
FreeBSD-ports-kmods: { enabled: no }
```

- latest 分支

```sh
USTC-ports-kmods: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_latest_${VERSION_MINOR}",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
FreeBSD-ports-kmods: { enabled: no }
```

> **注意**
>
>最好保持 ports 源和 kmods 源（若开启 pkgbase，则还须纳入 pkgbase 源）为同一镜像站，以避免发生潜在的依赖等问题。

## 面向基本系统的 pkgbase 源（适用 FreeBSD 14.3-RELEASE 及以上）

`pkgbase` 在 `FreeBSD 15.0-RELEASE` 中为技术预览出现，FreeBSD 项目仍支持传统方式直至 15.X 结束。在生产环境中使用 `pkgbase` 升级系统时应注意备份。

> **技巧**
>
> 14.x 用户可以选择由传统安装方式直接转换为 pkgbase，参见本书其他相关文章。

#### 官方源

默认路径：`/etc/pkg/repos/FreeBSD.conf`（请勿修改，仅做展示）

```sh
FreeBSD-base: {
  url: "pkg+https://pkg.FreeBSD.org/${ABI}/base_release_${VERSION_MINOR}",
  mirror_type: "srv",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkgbase-${VERSION_MAJOR}",
  enabled: no
}
```

>**注意**
>
>根据 FreeBSD 源代码 [usr.sbin/bsdinstall/scripts/pkgbase.in](https://github.com/freebsd/freebsd-src/blob/releng/15.0/usr.sbin/bsdinstall/scripts/pkgbase.in) 最后几段源代码，`/etc/pkg/repos/FreeBSD.conf` 中的 FreeBSD-base 源 虽然是 `enabled: no`，但是那些在安装中选择了 pkgbase 的用户，会在 `/usr/local/etc/pkg/repos/FreeBSD.conf` 中写入 `FreeBSD-base: { enabled: yes }` 这行来显式覆盖默认配置，即对于那些 pkgbase 用户，FreeBSD-base 源实际上是默认启用的。

#### 中国科学技术大学开源软件镜像站

禁用默认启用的官方 FreeBSD-base 源：

```sh
# mv /usr/local/etc/pkg/repos/FreeBSD.conf /usr/local/etc/pkg/repos/FreeBSD.conf.back
```

>**技巧**
>
>在某些环境中，文件 `/usr/local/etc/pkg/repos/FreeBSD.conf` 里也可能包含非 FreeBSD-base 仓库的定义，建议用户在重命名之前先确认文件内容。

编辑 `/usr/local/etc/pkg/repos/USTC.conf` 文件，写入以下配置：

```sh
USTC-base: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_release_${VERSION_MINOR}",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkgbase-${VERSION_MAJOR}",
  enabled: yes
}
```
>**警告**
>
>对于 **RELEASE** 版本的系统，pkgbase 在整个生命周期内是几乎固定不变的！
>
>仓库 `base_latest` 和 `base_weekly` 仅面向 STABLE 或 CURRENT！
>
>请勿变动字符串 `base_release_${VERSION_MINOR}`！

> **技巧**
>
> 在从 14.X pkgbase 系统升级到 15.0 时，常遇到签名密钥问题。请确保 `/usr/share/keys/pkgbase-15` 存在（如果缺失，可从官方源手动 fetch 或参考 Release Notes 中的升级说明）。否则会出现 “no trusted public keys found” 错误。详见 [15.0 Release Notes - Upgrading](https://www.freebsd.org/releases/15.0R/relnotes/#upgrade) [备份](https://web.archive.org/web/20260212000000/https://www.freebsd.org/releases/15.0R/relnotes/#upgrade) 和论坛相关讨论。


## STABLE/CURRENT 快速切换软件源到中国科学技术大学开源镜像站

>**警告**
>
> STABLE/CURRENT 并非生产版本，不适用于生产环境，使用上述版本的用户被推定为具有一定的知识基础，故此小节未列出具体步骤和过多解释。

### 内核模块源

- 对于 `FreeBSD 14.x-STABLE`

```sh
USTC-kmods: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_latest",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
```

- 对于 `FreeBSD 15.0-STABLE / FreeBSD 16.0-CURRENT`：

```sh
USTC-ports-kmods: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_latest",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
```

### pkgbase 源

```sh
USTC-base: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_latest",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkgbase-${VERSION_MAJOR}",
  enabled: yes
}
```

## 故障排除与未竟事宜

### 平衡安全与便利

### 为什么配置中要写完整选项（mirror_type / signature_type / fingerprints）

虽然只写 `url` 和 `enabled: yes` pkg 也能正常工作（pkg 会默认 `mirror_type: "none"` 和 `signature_type: "none"`），但这样做 **关闭了签名验证**。不会检查 pkg 下载的包是否被篡改，可能存在安全风险（尤其是 ports、kmods 和 pkgbase 系统包）。

其优点在于：

- 启用 `signature_type: "fingerprints"` 核 `fingerprints`：使用 FreeBSD 官方内置密钥验证包签名
- `mirror_type: "none"`：适合国内的 HTTPS 直链镜像（官方用 `"srv"` 是因为 `pkg+https://` 支持 DNS SRV，但镜像站不需要）

推荐在生产环境始终启用签名验证。如果追求极简，可以去掉这些行，但不建议，除非你完全信任网络环境。

>**警告**
>
>目前中国大陆境内不存在任何 FreeBSD 官方镜像站。
>
>对于那些以安全性为较高优先级的用户来说，应该使用默认的官方镜像 `pkg.freebsd.org`！其由 FreeBSD 项目官方构建、分发和维护。


### 旧版本存档的 pkg 二进制包源（请酌情使用）

> **技巧**
>
> 网易开源镜像站还提供了 FreeBSD 11、12 等过期版本的 pkg 二进制源。可自行配置使用。但可能存在安全风险。

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
