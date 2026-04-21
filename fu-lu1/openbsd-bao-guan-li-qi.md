# OpenBSD 包管理器

OpenBSD 提供了多种软件安装方式供用户选择，以满足不同应用场景的需求。

与其他 BSD 系统一样，OpenBSD 的软件安装主要有两种方式：一种是使用官方预编译的二进制包，另一种是通过 ports 源代码自行打包安装。二进制包方式安装速度快、使用简单，适合大多数用户；ports 方式提供更多的定制选项，适合有特殊需求的用户。推荐使用二进制包方式。

## 二进制包

二进制包是简单、常用的软件安装方式，用户可以直接安装已经编译好的软件。二进制包由 OpenBSD 项目官方预编译，确保与系统的兼容性和稳定性。

在线查询：<https://openports.pl/>

以 Firefox 浏览器为例：

- 安装软件

```sh
# pkg_add firefox  # 安装 Firefox 浏览器
```

- 卸载软件

```sh
# pkg_delete firefox  # 卸载 Firefox 浏览器
```

- 更新软件

```sh
# pkg_add -u  # 更新所有已安装的软件包
```

- 查询软件

```sh
$ pkg_info  # 列出所有已安装的软件包
$ pkg_info firefox  # 查看 Firefox 软件包的详细信息
```

- 搜索软件

```sh
$ pkg_info -Q firefox  # 搜索包含 firefox 关键字的软件包
```

- 清理缓存

```sh
# pkg_delete -a  # 自动删除不再被其他软件包依赖的自动安装的软件包
```

- 查看依赖

```sh
$ pkg_info -r firefox  # 查看 Firefox 依赖的软件包
$ pkg_info -R firefox  # 查看哪些软件包依赖 Firefox
```

### 切换软件源

本节介绍如何更换软件包源。

首先安装文本编辑器，因为 OpenBSD 默认使用的是 [nvi](https://man.openbsd.org/vi)。

安装 ee 文本编辑器：

```sh
# pkg_add ee  # 或者还可以用 nano，即 pkg_add nano
```

如果无法或不想安装 ee 或 nano 等编辑器，也可以使用类似 WinSCP 的软件进行文件修改。

编辑 `/etc/installurl` 文件，将默认源注释掉，即在 `https://cdn.openbsd.org/pub/OpenBSD` 前加 `#`：`#https://cdn.openbsd.org/pub/OpenBSD`。

在文件中另起一行，添加内容 `https://mirrors.tuna.tsinghua.edu.cn/OpenBSD/`。

此处选择 TUNA 清华大学开源软件镜像站，也可以选择：

- 阿里巴巴开源镜像站 [https://mirrors.aliyun.com/openbsd](https://mirrors.aliyun.com/openbsd)
- 南京大学开源镜像站 [https://mirrors.nju.edu.cn/OpenBSD](https://mirrors.nju.edu.cn/OpenBSD)

## ports

用户也可以通过 ports 系统从源代码编译安装软件，以获得更多的定制选项。ports 系统提供了一套标准化的框架，用于从源代码构建软件包。

[查询网站](https://openports.pl/)

CVS 在线浏览地址：<https://cvsweb.openbsd.org/>
OpenBSD 对应多个系统版本（release、stable 和 current），不同版本的 ports 之间不通用。这是因为不同版本的系统库和 ABI 可能存在差异。

release 版本的 ports 不会更新，版本号是固定的。如需使用滚动版本，需要使用 stable 或 current 系统。

升级系统需要通过源代码更新或安装快照版本（current），地址为：<https://cdn.openbsd.org/pub/OpenBSD/snapshots/amd64/>。

对于 release 版本，可直接下载压缩包并解压到 `/usr` 目录，例如：<https://cdn.openbsd.org/pub/OpenBSD/7.7/ports.tar.gz>

获取 current 版本 ports：

```sh
$ cd /usr                                                 # 进入 /usr 目录
$ cvs -qd anoncvs@anoncvs.jp.openbsd.org:/cvs checkout -P ports   # 从 OpenBSD CVS 仓库检出 Ports 树
```

对于 7.7 stable 版本：

```sh
$ cd /usr                                                 # 进入 /usr 目录
$ cvs -qd anoncvs@anoncvs.jp.openbsd.org:/cvs checkout -rOPENBSD_7_7 -P ports   # 从 OpenBSD CVS 仓库检出指定版本 OPENBSD_7_7 的 Ports 树
```

更新 ports：

```sh
$ cvs up -r TAG -Pd  # 使用 CVS 更新代码到指定标签 TAG，同时创建目录并删除不存在的文件
```

### 参考文献

- OpenBSD Project. Ports - Working with Ports[EB/OL]. (2024-03-25)[2026-03-25]. <https://www.openbsd.org/faq/ports/ports.html>. 官方 Ports 系统使用指南，详解源代码包编译流程。
- OpenBSD Project. Anonymous CVS[EB/OL]. (2024-03-25)[2026-03-25]. <https://www.openbsd.org/anoncvs.html>. 官方 CVS 匿名访问说明，提供了代码获取方法。
- OpenBSD Project. Following -current and using snapshots[EB/OL]. (2024-03-25)[2026-03-25]. <https://www.openbsd.org/faq/current.html>. 官方开发版系统使用指南，介绍了快照版本与源代码编译。
- OpenBSD Project. vi(1) -- screen-oriented text editor[EB/OL]. [2026-04-17]. <https://man.openbsd.org/vi>. OpenBSD nvi 文本编辑器手册页。

## pkgsrc

除了 OpenBSD 自带的包管理器外，用户还可以使用 NetBSD 的 pkgsrc 系统，它提供了更多的软件选择。

pkgsrc 为 NetBSD 的软件包管理系统，但其宣称同样支持 Linux 和其他 BSD 系统。pkgsrc 的软件包数量多于 OpenBSD 官方提供的软件包，但需要注意 pkgsrc 与 OpenBSD 的兼容性。以下内容可供感兴趣的用户尝试，不推荐以 pkgsrc 为主力包管理系统。

```sh
$ cd ~/                               # 切换到当前用户主目录
$ ftp https://cdn.netbsd.org/pub/pkgsrc/pkgsrc-2023Q2/pkgsrc.tar.gz  # 从官方 FTP 下载 pkgsrc 压缩包
$ tar -xzf pkgsrc.tar.gz              # 解压下载的 pkgsrc 压缩包
$ cd pkgsrc/bootstrap                 # 进入 bootstrap 目录
$ ./bootstrap --unprivileged          # 以非特权用户方式启动 pkgsrc 引导安装
```

需要将路径 `~/pkg/bin` 添加到环境变量中。pkgsrc 树位于 `~/pkgsrc/`，其所有相关工作文件均位于 `~/pkg/`。

可以在 `~/pkgsrc/` 中搜索软件并安装，安装时使用命令 `bmake install`，例如在 `~/pkgsrc/chat/irssi/` 安装 IRC 客户端 Irssi。

pkgsrc 目录结构：

```sh
~/
├── pkgsrc/
│   └── chat/
│       └── irssi/
└── pkg/
    └── bin/
```
