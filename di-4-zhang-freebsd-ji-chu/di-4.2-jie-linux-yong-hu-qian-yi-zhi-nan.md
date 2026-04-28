# 4.2 Linux 用户迁移指南

Linux 与 FreeBSD 同属类 UNIX 操作系统，但二者在内核架构、包管理哲学、系统设计理念等方面存在根本差异。Linux 采用宏内核架构，发行版众多且各自维护独立的用户空间；FreeBSD 则采用整体式开发模型，内核与基本系统由同一团队统一维护，形成完整的操作系统而非仅内核。在包管理方面，Linux 发行版多采用各自独立的包管理器（如 apt、dnf、pacman），而 FreeBSD 则使用 pkg(8) 管理二进制包、Ports 框架管理源代码编译安装，两者互补。本节旨在帮助 Linux 用户理解这些差异，并顺利完成迁移。

## 遗失的世界

许多 Linux 体系的核心概念与技术实践，其最初提出者与实践者是 BSD 系统，包括：

- 容器技术的原型可追溯至 FreeBSD Jail 机制；
- 发行版概念框架；
- Gentoo 采用的 Ports 包管理方法论，其技术渊源可追溯至 BSD Ports 框架；
- BSD 是最早的开源理念实践者之一，BSD 许可证也是历史上最早出现的自由软件许可证之一。

> **思考题**
>
>>“一切真历史都是当代史”。
>
> 读者如何理解这句话？如何定义“真”与“非真”？

### 参考文献

- FreeBSD Foundation. FreeBSD: The Torchbearer of the Original Operating System Distribution[EB/OL]. [2026-04-04]. <https://freebsdfoundation.org/blog/freebsd-the-torchbearer-of-the-original-operating-system-distribution/>. BSD 最早提出并实践了“发行版”概念框架。
- Linux Foundation. A Brief Look at the Roots of Linux Containers[EB/OL]. [2026-04-18]. <https://www.linuxfoundation.org/blog/blog/a-brief-look-at-the-roots-of-linux-containers>. 该文指出：“In 2000, FreeBSD extended chroot to FreeBSD Jails”，容器技术原型可追溯至 FreeBSD Jail。
- Phull R, Bhatt D. Portage: Bringing Hackers' Wisdom to Science[EB/OL]. arXiv preprint arXiv:1610.02742, 2016. [2026-04-18]. <https://arxiv.org/abs/1610.02742>. 该论文指出：“Portage, written in Python and inspired by the ports system from FreeBSD”及“Portage is a GPLv2 package management system based on FreeBSD's ports collection”，Gentoo Portage 技术渊源可追溯至 BSD Ports。
- FreeBSD Project. Why you should use a BSD style license for your Open Source Project[EB/OL]. [2026-04-18]. <https://docs.freebsd.org/en/articles/bsdl-gpl/>. 该文记载了 BSD 许可证自 20 世纪 70 年代末起即以源代码自由分发的方式实践开源理念，早于 1985 年的 GNU Emacs 许可证和 1989 年的 GPL。
- Red Hat. 什么是 Linux 容器？[EB/OL]. [2026-04-04]. <https://www.redhat.com/zh/topics/containers/whats-a-linux-container>. 介绍 Linux 容器的基本概念与技术原理。
- Open Source Initiative. The Open Source Definition[EB/OL]. [2026-04-17]. <https://opensource.org/osd>. 虽然“开源”（Open Source）一词直到 1998 年才由 Christine Peterson 正式提出，但 BSD 许可证自 20 世纪 80 年代起便以源代码自由分发的方式实践了这一理念。
- Croce B. 历史学的理论和历史[M]. 田时纲，译. 北京：中国社会科学出版社，2018. 提出一切真历史都是当代史的核心命题，探讨历史认识的当代性。

## FreeBSD 与 Linux 的不同之处

### 理解 FreeBSD 的操作系统本质：并非发行版

FreeBSD 是一个完整的操作系统，包含基本系统（用户空间 + 内核）和 Ports 框架两大部分，二者相互独立。

#### 独立自存的基本系统

freebsd-src = 基本系统存储库 = 用户空间 + 内核。

FreeBSD 版本分支分为三个主要系列：

- **CURRENT**：开发版本，对应 main 分支；
- **STABLE**：固定分支，对应 stable/15 等分支；
- **RELEASE**：正式发布版本，对应 releng/15.0 等分支。

新特性首先提交到 CURRENT，根据需要回溯到 STABLE，再回溯到点版本的 RELEASE。RELEASE 大版本由 CURRENT 经由短期的 STABLE 发展而来。

pkgbase 直接由 freebsd-src 构建：

```sh
# cd /usr/src # 需要预先拉取 freebsd-src 到该路径
# make -j8 buildworld # 世界即用户空间
# make -j8 buildkernel # 内核
# make -j8 packages # 构建 pkgbase 二进制包
```

#### 安装第三方软件的 Ports 框架与 pkg 包管理器

freebsd-ports = 第三方软件集合（单个称为 Port）= Ports 框架存储库。

Port 是若干文件的集合，由源代码包校验和、说明文件、补丁等构成，其中 Makefile 是核心。Arch 的 PKGBUILD 或 Gentoo 的 ebuild 与此类似，事实上它们是由 Ports 框架衍生出的技术。

pkg 包直接由 freebsd-ports 通过 poudriere 构建系统构建而来。

freebsd-ports 的 main 分支即 latest 源，形如 2026Q1 的分支（最新的那个季度）即 quarter 分支。季度分支直接从 main 按季度切出。

默认基本系统不包含任何 Port 软件，甚至没有 pkg 包管理器本体（传统安装模式）。大多数硬件的固件也从基本系统移到了 Ports。

#### 总结

FreeBSD 整体系统结构符合一般 Windows、Android 或 macOS 用户的直觉，采用统一的系统管理方式。

### init 系统

FreeBSD 使用 BSD init 而非 systemd；BSD init 与传统的 SysVinit 也有所不同，BSD 没有运行级别（runlevel），也没有 `/etc/inittab`，均由 rc 系统控制。

当以用户进程身份运行 init 时，可以模拟 AT&T System V UNIX 的行为，超级用户可在命令行中指定所需的运行级别，该 init 进程会向原始的（PID 为 1 的）init 进程发送特定信号，以执行相应操作。例如，在 FreeBSD 中执行 `init 0` 仍然表示关机。

此外，PID 为 1 的 init 进程还响应以下信号（需通过 `kill` 命令手动发送）：SIGUSR1（仅停止运行，不断电）、SIGWINCH（停止运行、关电源并重启，需硬件支持）。

### Shell

FreeBSD 所有用户的默认 Shell 均为 sh（14 之前 root 默认为 csh），而非 bash（如有需要亦可切换）。

### 基本系统去 GNU 化

FreeBSD 基本系统几乎不包含任何与 BSD 协议不兼容的软件。

### 参考文献

- MYSQLZOUQI. 浅析 Linux 初始化 init 系统，第 1 部分：sysvinit 第 2 部分：UpStart 第 3 部分：Systemd[EB/OL]. [2026-03-25]. <https://www.cnblogs.com/MYSQLZOUQI/p/5250336.html>. 是存档，原文已佚，系统介绍了各初始化系统。
- FreeBSD Project. init -- process control initialization[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?query=init>. FreeBSD init 手册页。BSD init 无 SysV 风格运行级别与 /etc/inittab，以及以用户进程身份运行 init 时的运行级别-信号对应关系。
- FreeBSD Project. ttys -- terminal initialization information[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=ttys&sektion=5>. 终端初始化配置文件手册页。
- Gentoo. Comparison of init systems[EB/OL]. [2026-03-25]. <https://wiki.gentoo.org/wiki/Comparison_of_init_systems>. 各大 init 对比图，为系统选型提供参考。
- FreeBSD Project. GPL Software in FreeBSD Base[EB/OL]. [2026-03-25]. <https://wiki.freebsd.org/GPLinBase>. FreeBSD 基本系统中的 GPL 软件，系统梳理了基本系统的许可证兼容性。
- FreeBSD Project. FreeBSD 14.0-RELEASE Release Notes[EB/OL]. [2026-04-18]. <https://www.freebsd.org/releases/14.0R/relnotes/>. “The default shell for the root user is now sh(1)”，FreeBSD 14 起默认 root shell 由 csh/tcsh 变更为 sh。
- FreeBSD Project. Ports Quarterly Branch[EB/OL]. [2026-04-18]. <https://wiki.freebsd.org/Ports/QuarterlyBranch>. “quarterly is the familiar name for ports branched from main”，main 分支即 latest 源、季度分支按 YYYYQn 命名。
- FreeBSD Core Team. Change to FreeBSD release scheduling and support period[EB/OL]. (2024-07-16)[2026-04-18]. <https://lists.freebsd.org/archives/freebsd-announce/2024-July/000143.html>. “the FreeBSD core team has approved reducing the stable branch support duration from 5 years to 4 years starting with FreeBSD 15”。
- FreeBSD Wiki. Desktop[EB/OL]. [2026-04-18]. <https://wiki.freebsd.org/Desktop>. “NetworkManager itself cannot be ported due to a monolithic architecture and extensive Linux syscall use”，NetworkManager 无法移植的真实原因。

## 基本对比

| 操作系统 | 发布/生命周期（主要版本） | 主要包管理器（命令） | 许可证（主要） | 工具链 | Shell | 桌面 |
| -------- | ------------------------- | -------------------- | -------------- | ------ | ----- | ---- |
| Ubuntu | [2 年/5 年（LTS 标准支持），10 年（需 Ubuntu Pro）](https://ubuntu.com/about/release-cycle) | [apt](https://ubuntu.com/server/docs/package-management) | [GNU](https://ubuntu.com/legal/intellectual-property-policy) | gcc | bash | GNOME |
| Gentoo Linux | 滚动更新 | [Portage（emerge）](https://wiki.gentoo.org/wiki/Portage) | GNU | gcc | bash | 可选 |
| Arch Linux | 滚动更新 | [pacman](https://wiki.archlinux.org/title/pacman) | GNU | gcc | bash | 可选 |
| RHEL | [3/最长 12 年](https://access.redhat.com/zh_CN/support/policy/updates/errata) | [RPM（yum、dnf）](https://www.redhat.com/sysadmin/how-manage-packages) | GNU | gcc | bash | GNOME |
| FreeBSD | [约 2/4 年](https://www.freebsd.org/security/)（FreeBSD 14 及以前为 5 年，自 FreeBSD 15 起缩短为 4 年） | pkg/Ports | BSD | clang | sh | 可选 |
| Windows | [不固定](https://docs.microsoft.com/zh-cn/lifecycle/faq/windows) | 可选 | 专有 | 可选 | PowerShell | Windows 桌面 |
| macOS | 1 年/约 3 年 | 无 | [专有](https://www.apple.com/legal/sla/) | clang | zsh | Aqua |

由于 Linux 广泛使用 GNU 工具，因此理论上只要不依赖特定的 Linux 函数库，这些工具都可以在 FreeBSD 上运行。

| Linux 命令/GNU 软件 | BSD Port/命令 | 作用说明 | 备注 |
| ------------------- | ------------- | -------- | ---- |
| `lsusb` | `sysutils/usbutils` | 显示 USB 信息 | 也可粗略使用 `cat /var/run/dmesg` |
| `lspci` | `sysutils/pciutils` | 显示 PCI 信息 | 也可粗略使用 `cat /var/run/dmesg` |
| `lsblk` | `sysutils/lsblk` | 显示磁盘使用情况 | / |
| `free` | `sysutils/freecolor` | 显示内存使用情况 | FreeBSD 未提供 `free` 命令，因为该命令依赖 Linux 特性，通常由 `procps` 包提供。如确实需要 `free`，可使用 <https://github.com/j-keck/free>，其他替代命令包括 `vmstat` |
| `lscpu` | `sysutils/lscpu` | 显示处理器信息 | / |
| glibc | FreeBSD libc | C 库 | / |
| GCC | LLVM + Clang | 编译器、编译链工具 | 如有特殊需要也可以安装 `devel/gcc` |
| `vim` | `editors/vim` | 文本编辑器 | FreeBSD 的 `vi` 不是软链接到 `vim`，而是早期的 `nvi` |
| `wget` | `ftp/wget` | 下载器 | 系统默认的下载工具是 `fetch` |
| bash | `shells/bash` | Shell | 系统默认的 Shell 是 `sh`（非软链接）。可以自行修改。 |
| NetworkManager | `net-mgmt/networkmgr` | 网络连接工具 | NetworkManager 因其单体架构（monolithic architecture）及对 Linux 系统调用的广泛依赖而无法直接移植至 FreeBSD |
| `lsmod` | `kldstat` | 列出已加载的内核模块 | / |
| `strace` | `truss` | 跟踪系统调用 | / |
| `modprobe` | 加载内核模块：`kldload`；卸载内核模块：`kldunload` | 加载内核模块、卸载内核模块 | / |

### 参考文献

- FreeBSD Foundation. Navigating FreeBSD's New Quarterly and Biennial Release Schedule[EB/OL]. [2026-04-16]. <https://freebsdfoundation.org/blog/navigating-freebsds-new-quarterly-and-biennial-release-schedule/>. 该博文说明 FreeBSD 发布周期变更。

## 课后习题

1. 在 FreeBSD 中构建一个简单的 Port，编写 Makefile 使其能下载、编译并安装一个最小化程序，验证 Ports 框架的完整构建流程。
2. 查阅 FreeBSD rc 脚本的最小实现（`/etc/rc.subr`），分析其服务依赖声明机制，并与 systemd 的 unit 文件依赖模型进行比较。
3. 从技术本体论角度分析：当 Linux 发行版的各组件（内核、包管理器、桌面环境等）均可独立替换时，“发行版”这一概念的同一性依据是什么？
