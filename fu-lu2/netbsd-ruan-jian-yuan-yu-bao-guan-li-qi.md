# NetBSD 软件源与包管理器

在完成 NetBSD 系统安装的基础上，本节介绍 NetBSD 的包管理系统。NetBSD 的包管理器是 pkgsrc，该系统同时支持二进制安装和从源代码编译安装两种模式。底层工具为 `pkg_*` 系列命令（例如 `pkg_add`），pkgin 是基于这些工具的上层封装，提供更便捷的包管理功能。

pkgsrc 是跨平台的软件包管理框架。

## 二进制软件源配置

以 NetBSD 10.1 为例，更换二进制软件源的方法如下。首先需要配置 pkgin 软件仓库，具体操作步骤如下：

`/usr/pkg/etc/pkgin/repositories.conf` 是 pkgin 的软件仓库配置文件，用于指定二进制包的下载地址。设置 pkgin 软件仓库为清华大学镜像源：

```sh
# echo https://mirrors.tuna.tsinghua.edu.cn/pkgsrc/packages/NetBSD/amd64/10.1/All/  > /usr/pkg/etc/pkgin/repositories.conf
```

设置 pkgin 软件仓库为南京大学开源镜像源：

```sh
# echo https://mirrors.nju.edu.cn/pkgsrc/packages/NetBSD/x86_64/10.1/All/  > /usr/pkg/etc/pkgin/repositories.conf
```

> **思考题**
>
> 请思考为什么上述软件源路径中一个架构是 `x86_64` 而另外一个却是 `amd64`？

NetBSD 的软件源分布较为分散，有时单个源无法完全满足需求，需尝试多个源。可通过 `pkgin search` 命令搜索软件包，或访问 [https://cdn.netbsd.org/pub/pkgsrc/](https://cdn.netbsd.org/pub/pkgsrc/) 查看官方软件包集合。

由于二进制包的构建可能存在差异，NetBSD 用户经常需要在不同源之间切换，以下是一个示例：

```sh
# echo http://mirrors.nju.edu.cn/pkgsrc/packages/NetBSD/x86_64/10.0_2024Q4/All/  > /usr/pkg/etc/pkgin/repositories.conf  # 设置 pkgin 软件仓库为南京大学镜像源，适用于 NetBSD 10.0_2024Q4
```

## 关闭 ABI 检测（可选）

使用 pkgin 安装软件时，NetBSD 默认会检测 ABI（Application Binary Interface，应用程序二进制接口）版本兼容性。ABI 定义了二进制程序与操作系统之间的接口规范，检测机制用于确保软件包与当前系统版本兼容。由于软件包更新存在滞后性，可能导致某些软件包无法正常安装，可通过以下方式禁用检测：

`/etc/pkg_install.conf` 是 pkg_install 工具的配置文件，添加以下配置可禁用 OSABI 检查：

```sh
# echo CHECK_OSABI=no >> /etc/pkg_install.conf
```

在 `pkg_install` 配置中禁用 OSABI 检查后，将允许跨版本安装软件包，但可能引入兼容性风险，请谨慎使用。

## pkgsrc 编译安装

pkgsrc 编译安装的方法与 FreeBSD 相似，以下是一个安装 KDE 元包的示例：

进入 pkgsrc 目录并查看内容：

```sh
# cd /usr/pkgsrc/meta-pkgs/kde  # 进入 pkgsrc 中 KDE 元包目录
# ls  # 列出该目录下的文件和子目录
CVS               Makefile          applications.mk   kf6.mk            plasma6.mk
DESCR             Makefile.common   kf5.mk            plasma5.mk
```

执行编译安装，`make install` 会自动处理依赖关系并安装软件包，`clean` 目标用于清理编译过程中产生的临时文件：

```sh
# make install clean  # 编译安装当前 pkgsrc 包并清理临时文件
===> Installing dependencies for kde-20240828
=> Tool dependency mktools-[0-9]*: NOT found
=> Verifying reinstall for ../../pkgtools/mktools
===> Installing dependencies for mktools-20250213

……以下构建过程省略……

```

以下是 NetBSD 包管理相关的目录和文件结构：

```sh
/
├── etc/
│   └── pkg_install.conf # pkg 安装配置文件，用于禁用 ABI 检测等
└── usr/
    ├── pkg/
    │   └── etc/
    │       └── pkgin/
    │           └── repositories.conf # pkgin 软件仓库配置文件
    └── pkgsrc/ # pkgsrc 源代码根目录
        └── meta-pkgs/
            └── kde/ # KDE 元包目录
```

## pkgsrc-wip 项目

pkgsrc-wip（pkgsrc work-in-progress，pkgsrc 进行中）是 pkgsrc 的实验性软件包集合，包含许多尚未完成或正在测试的项目，但不少软件依赖这些项目。以下是具体的使用方法：

首先确保存在 `/usr/pkgsrc` 目录，然后安装 Git 并克隆 pkgsrc-wip 仓库：

```sh
# mkdir -p /usr/pkgsrc/                         # 如果 /usr/pkgsrc 目录不存在，则创建该目录
# cd /usr/pkgsrc/                                # 进入 /usr/pkgsrc 目录
# pkgin install git                              # 使用 pkgin 安装 Git
# git clone --depth 1 https://github.com/NetBSD/pkgsrc-wip wip   # 将 pkgsrc-wip 仓库克隆到 wip 目录，--depth 1 表示仅获取最新提交，减少下载量
```

如需通过代理访问 GitHub，可配置 Git 代理（请根据实际可用代理修改）：

```sh
# git config --global http.proxy http://192.168.31.77:7890   # 设置 Git HTTP 代理
# git config --global https.proxy http://192.168.31.77:7890  # 设置 Git HTTPS 代理
```

## 参考文献

- 清华大学开源软件镜像站. pkgsrc 镜像使用帮助[EB/OL]. [2026-03-25]. <https://mirrors.tuna.tsinghua.edu.cn/help/pkgsrc/>. 切换软件源方式，提供详细的国内镜像源配置指南。
- 肖楠. pkgsrc 与 IPS[EB/OL]. [2026-03-25]. <https://web.archive.org/web/20221118031504/https://nanxiao.me/pkgsrc-ang-ips/>. 基本常识，对比分析 pkgsrc 与其他包管理系统。
- pkgsrc Project. The pkgsrc-wip project[EB/OL]. (2025-12-20)[2026-03-25]. <https://pkgsrc.org/wip>. pkgsrc 官方使用说明，介绍工作中软件包的贡献流程。
- pkgsrc Project. pkgsrc[EB/OL]. (2025-12-20)[2026-03-25]. <https://www.pkgsrc.org/>. 官方安装说明，提供跨平台包管理系统的权威技术文档。
