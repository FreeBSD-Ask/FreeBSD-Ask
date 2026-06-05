# 6.2 FreeBSD 软件源

FreeBSD 的软件源分为 pkg 二进制包源、Ports 源、系统源和更新源四类，分别配置，默认指向官方服务器，国内用户通常需要切换至镜像站以提升下载速度。

## 15.0-RELEASE 快速切换 pkg 软件源到中国科学技术大学开源软件镜像站

该配置要求读者在安装过程中使用 pkgbase 方式，可设置 pkg 二进制包源（由 Ports 构建而来）、pkgbase 源、内核模块源。

使用 ee 编辑器打开 **/usr/local/etc/pkg/repos/FreeBSD.conf** 文件。

> **技巧**
>
> 如果提示文件不存在或打开后内容并非 `FreeBSD-base: { enabled: yes }`，则本小节不适用。请按下文内容手动配置。

清空 **FreeBSD.conf** 文件中原有内容 `FreeBSD-base: { enabled: yes }`。

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

> **技巧**
>
> 将上述配置中的两个 `quarterly` 都改为 `latest` 即可使用滚动更新的软件源。

## pkg 二进制包（由 Ports 构建的二进制包）切换软件源

FreeBSD 中 pkg 源分为系统级与用户级两个配置文件。**由于该文件会随基本系统的更新而改变，因此不建议** 直接修改 **/etc/pkg/FreeBSD.conf** 文件。

> **警告**
>
> 请勿同时启用多个 pkg 镜像站，无论是官方镜像站（如 `pkg.freebsd.org` 与 USTC 混用），还是境内非官方镜像站，都不建议混合使用。其后果类似于混用 FreeBSD 季度分支的 Ports 和 latest 分支的 pkg，可能会破坏软件的依赖关系。案例：[混用导致 KDE 桌面被删除](https://blog.mxdyeah.com/post/freebsd-exp-kde6)。

> **警告**
>
> 请勿同时混用 `quarterly` 和 `latest`，在所有配置文件中应保持一致。

若要获取滚动更新的包，请将 `quarterly` 修改为 `latest`。二者区别参见上文。

> **注意**
>
> 对于 `CURRENT` 只提供了 `latest`。

示例：使用命令修改系统级 `pkg` 源为 latest：

```sh
# sed -i '' 's/quarterly/latest/g' /etc/pkg/FreeBSD.conf
```

### 14.X-RELEASE

#### 创建用户级源目录和文件

创建 pkg 仓库配置目录：

```sh
# mkdir -p /usr/local/etc/pkg/repos
```

使用 `ee` 编辑器打开配置文件 **/usr/local/etc/pkg/repos/USTC.conf**（将自动创建文本文件 **USTC.conf**）:

```sh
# ee /usr/local/etc/pkg/repos/USTC.conf
```

> **注意**
>
> 在本节中，**/usr/local/etc/pkg/repos/USTC.conf** 是 pkg 二进制源、模块源和 pkgbase 源共用的配置文件。后续配置不再重复说明此步骤。

#### 中国科学技术大学开源软件镜像站

编辑 **/usr/local/etc/pkg/repos/USTC.conf** 文件，写入以下配置 **之一**：

- quarterly：

```sh
USTC: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/quarterly",
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
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/latest",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
FreeBSD: { enabled: no }
```

### 15.0-RELEASE

自 `FreeBSD 15.0-RELEASE` 以降，`FreeBSD` 源的名称由 `FreeBSD` 变更为 `FreeBSD-ports`。

#### 官方源

更多信息参见源代码 **usr.sbin/pkg/FreeBSD.conf.quarterly-release**[EB/OL]. [2026-03-26]. <https://github.com/freebsd/freebsd-src/blob/releng/15.0/usr.sbin/pkg/FreeBSD.conf.quarterly-release>。下同。

这是 15.0-RELEASE 系统安装完成后默认的软件源。

#### 中国科学技术大学开源软件镜像站

编辑 **/usr/local/etc/pkg/repos/USTC.conf** 文件，写入以下配置（quarterly 分支即 2024Q3、2025Q1 等）：

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

如果使用 latest 分支（滚动更新，即 Ports 的 main 分支构建而来），改为如下配置：

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

编辑 **/usr/local/etc/pkg/repos/USTC.conf** 文件，写入以下配置（quarterly 分支即 2024Q3、2025Q1 等）：

如果使用 quarterly 分支，配置如下：

```sh
USTC-kmods: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_quarterly_${VERSION_MINOR}",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
```

如果使用 latest 分支，配置如下：

```sh
USTC-kmods: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_latest_${VERSION_MINOR}",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
```

### 15.0-RELEASE

自 `FreeBSD 15.0-RELEASE` 以降，`kmods` 源的名称由 `FreeBSD-kmods` 变更为 `FreeBSD-ports-kmods`。

#### 中国科学技术大学开源软件镜像站

编辑 **/usr/local/etc/pkg/repos/USTC.conf** 文件，写入以下配置（quarterly 分支即 2024Q3、2025Q1 等）：

如果使用 quarterly 分支，配置如下：

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

如果使用 latest 分支，配置如下：

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
> 建议保持 Ports 源和 kmods 源（如果开启 pkgbase，则还需要纳入 pkgbase 源）为同一镜像站，以避免发生潜在的依赖等问题。

## 面向基本系统的 pkgbase 源（适用 FreeBSD 14.3-RELEASE 及以上）

`pkgbase` 在 `FreeBSD 15.0-RELEASE` 中作为技术预览出现，FreeBSD 项目仍支持传统方式直至 15.X 结束。在生产环境中使用 `pkgbase` 升级系统时应注意备份。

> **技巧**
>
> 14.x 用户可以选择由传统安装方式直接转换为 pkgbase，参见本书其他相关章节。

### 官方源

默认路径：**/etc/pkg/FreeBSD.conf**（请勿修改，仅做展示）

```sh
FreeBSD-base: {
  url: "pkg+https://pkg.FreeBSD.org/${ABI}/base_release_${VERSION_MINOR}",
  mirror_type: "srv",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkgbase-${VERSION_MAJOR}",
  enabled: no
}
```

> **注意**
>
> 根据 FreeBSD 源代码 [usr.sbin/bsdinstall/scripts/pkgbase.in](https://github.com/freebsd/freebsd-src/blob/releng/15.0/usr.sbin/bsdinstall/scripts/pkgbase.in) 最后几段源代码，**/etc/pkg/FreeBSD.conf** 中的 FreeBSD-base 源虽然是 `enabled: no`。但是，那些在安装中选择了 pkgbase 的用户，会在 **/usr/local/etc/pkg/repos/FreeBSD.conf** 文件中写入 `FreeBSD-base: { enabled: yes }` 这一行来显式覆盖默认配置。因此，pkgbase 用户的 FreeBSD-base 源实际上是默认启用的。

#### 中国科学技术大学开源软件镜像站

禁用默认启用的官方 FreeBSD-base 源：

```sh
# mv /usr/local/etc/pkg/repos/FreeBSD.conf /usr/local/etc/pkg/repos/FreeBSD.conf.back
```

> **技巧**
>
> 在某些环境中，文件 **/usr/local/etc/pkg/repos/FreeBSD.conf** 里也可能包含非 FreeBSD-base 仓库的定义，建议用户在重命名之前先确认文件内容。

编辑 **/usr/local/etc/pkg/repos/USTC.conf** 文件，写入以下配置：

```sh
USTC-base: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_release_${VERSION_MINOR}",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkgbase-${VERSION_MAJOR}",
  enabled: yes
}
```

> **警告**
>
> 对于 **RELEASE** 版本的系统，pkgbase 在整个生命周期内几乎是固定不变的！
>
> 仓库 `base_latest` 和 `base_weekly` 仅面向 STABLE 或 CURRENT！
>
> 请勿变动字符串 `base_release_${VERSION_MINOR}`！

> **技巧**
>
> 在从 14.X pkgbase 系统升级到 15.0 时，常遇到签名密钥问题。请确保 **/usr/share/keys/pkgbase-15** 存在（如果缺失，可从官方源手动 fetch 或参考 Release Notes 中的升级说明）。否则会出现“no trusted public keys found”错误。详见 [15.0 Release Notes - Upgrading](https://www.freebsd.org/releases/15.0R/relnotes/#upgrade) 和论坛相关讨论。

## STABLE/CURRENT 快速切换 pkg 软件源到中国科学技术大学开源软件镜像站

> **警告**
>
> STABLE/CURRENT 并非生产版本，不适用于生产环境，使用上述版本的用户被推定为具有一定的知识基础，因此此小节未列出具体步骤和过多解释。

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

## Ports 源（Distfiles）

获取 Ports 本身的方法（通过 Git 或归档文件）参见第 6.4 节。该源用于下载 Ports 框架中的软件（称为 Port）的源代码。

> **警告**
>
> Ports 源可能并不完整，这是受 Ports 框架结构的限制。详细信息可参考 <https://github.com/ustclug/discussions/issues/408>。

创建或修改文件 **/etc/make.conf**。写入以下配置 **之一**：

- 南京大学开源镜像站

```ini
MASTER_SITE_OVERRIDE?=https://mirrors.nju.edu.cn/freebsd-ports/distfiles/${DIST_SUBDIR}/
```

- 中国科学技术大学开源软件镜像站

```ini
MASTER_SITE_OVERRIDE?=https://mirrors.ustc.edu.cn/freebsd-ports/distfiles/${DIST_SUBDIR}/
```

## 故障排除与未竟事宜

### 平衡安全与便利

使用非官方镜像站虽提升了下载速度，但引入了中间人攻击的风险——镜像站管理员理论上可在软件包中注入恶意代码。FreeBSD 官方集群内部使用 `zfs send/receive` 而非 rsync 同步数据，且官方 rsync 服务不向公众开放，部分原因正是为了降低此类风险。对于安全要求较高的生产环境，建议使用官方源或自行搭建 Poudriere 构建服务器，以完全控制软件包。

### 为什么 pkg 配置文件中要写完整选项（mirror_type / signature_type / fingerprints）

虽然仅写 `url` 和 `enabled: yes` 时 pkg 也能正常工作（pkg 会默认 `mirror_type: "none"` 和 `signature_type: "none"`），但这样做将 **关闭签名验证**。系统不会检查 pkg 下载的包是否被篡改，可能存在安全风险（尤其是 ports、kmods 和 pkgbase 系统包）。

其优点在于：

- 启用 `signature_type: "fingerprints"` 和 `fingerprints`：使用 FreeBSD 官方内置密钥验证包签名
- `mirror_type: "none"`：适合国内的 HTTPS 直链镜像（因为 `pkg+https://` 支持 DNS SRV，所以官方用 `"srv"`，但镜像站不需要）

推荐在生产环境中始终启用签名验证。若去除此配置则关闭签名验证，除非完全信任网络环境，否则不建议如此操作。

> **警告**
>
> 目前中国大陆境内不存在任何 FreeBSD 官方镜像站。
>
> 对于安全性要求较高的用户，应该使用默认的官方镜像 `pkg.freebsd.org`！其由 FreeBSD 项目官方构建、分发和维护。

### 旧版本存档的 pkg 二进制包源（请酌情使用）

> **警告**
>
> 网易开源镜像站还提供了 FreeBSD 11、12 等过期版本的 pkg 二进制源。可自行配置使用。但可能存在安全风险。

不受安全支持的版本同样可以使用二进制源。以下以 `FreeBSD 9.2` 为例：

首先切换到可用的二进制源。

```sh
# setenv PACKAGESITE https://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest
```

如果 shell 不是 csh，那么：

```sh
# export PACKAGESITE=https://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest
```

安装示例：现在安装 `bsdinfo`。

```sh
# pkg_add -r bsdinfo
Fetching https://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest/bsdinfo.tbz... Done.
```

> **注意**
>
> 因为当时 pkgng 还未获官方支持，仍然仅支持使用 `pkg_*` 命令，所以 pkg 是不可用的，会提示找不到 `digests.txz` 和 `repo.txz`。
