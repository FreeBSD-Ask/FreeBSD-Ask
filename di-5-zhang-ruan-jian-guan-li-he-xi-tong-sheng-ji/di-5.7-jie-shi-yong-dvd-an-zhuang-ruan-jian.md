# 5.5 使用 DVD 安装软件

本节介绍通过 DVD 介质进行软件安装的方法与流程。

DVD 安装作为离线环境下的重要软件获取途径，在网络受限场景下具有特殊实用价值。

## 挂载 DVD 到 `/dist` 目录

使用 DVD 安装软件前，首先需要将 DVD 挂载到系统中。挂载方式有两种，分别适用于本地 ISO 文件和真实的 DVD 设备。这两种方式构成了 DVD 介质挂载的完整技术方案。

目录结构：

```sh
/
└── dist/ # DVD 挂载路径
    ├── packages/
    │   └── repos/
    │       └── FreeBSD_install_cdrom.conf # pkg 仓库配置文件
    ├── bin/
    ├── boot/
    ├── dev/
    ├── etc/
    ├── lib/
    ├── libexec/
    ├── media/
    ├── mnt/
    ├── net/
    ├── proc/
    ├── rescue/
    ├── root/
    ├── sbin/
    ├── tmp/
    ├── usr/
    └── var/
```

- 直接挂载本地 ISO：

```sh
# mdconfig /home/ykla/FreeBSD-14.2-RELEASE-amd64-dvd1.iso  # 请改为实际路径，可以用 pwd 命令查看当前路径
md0
# mkdir -p /dist  # 创建挂载路径，必须是此路径
# mount -t cd9660 /dev/md0 /dist # 不能直接挂载 ISO，会报错 block device required
```

- 直接使用 DVD 设备（如通过虚拟机直接挂载的 ISO 镜像）：

观察 ISO 镜像的挂载情况：

```sh
# gpart show  # 显示系统中所有磁盘分区表信息

……省略无用磁盘……

=>      9  2356635  cd0  MBR  (4.5G)
        9  2356635       - free -  (4.5G)
```

可以看到存在 `cd0`，大小符合预期。

```sh
# mkdir -p /dist # 创建挂载点
# mount -t cd9660 /dev/cd0 /dist # 挂载 ISO
# ls /dist/ # 查看挂载情况
.cshrc		bin		lib		net		root		var
.profile	boot		libexec		packages	sbin
.rr_moved	dev		media		proc		tmp
COPYRIGHT	etc		mnt		rescue		usr
```

### 故障排除与未竟事宜

**/dist** 目录若改为其他目录，则使用环境变量的方法无效，因为 `packages/repos/FreeBSD_install_cdrom.conf` 中的路径被写死，无法修改。

## 使用 `bsdconfig` 安装 DVD 软件（当前无效）

先按上述方法完成挂载。

```sh
# bsdconfig
```

`3 Packages` → `1 CD/DVD Install from a FreeBSD CD/DVD`

存在 Bug，会报错 `No pkg(8) database found!`。

> **思考题**
>
> 请读者自行阅读源代码，分析如何解决该问题。

## 使用环境变量直接安装 DVD 软件

让 pkg 使用指定的软件仓库路径安装 Xorg：

```sh
# env REPOS_DIR=/dist/packages/repos pkg install xorg
Updating FreeBSD_install_cdrom repository catalogue...
FreeBSD_install_cdrom repository is up to date.
All repositories are up to date.
Checking integrity... done (0 conflicting)
The following 1 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
	xorg: 7.7_3

Number of packages to be installed: 1

Proceed with this action? [y/N]:
```

要列出 DVD 中的可用软件：

```sh
# env REPOS_DIR=/dist/packages/repos pkg rquery "%n"
```

## 更换软件源为 DVD

### 创建 DVD 软件源

将 `FreeBSD_install_cdrom.conf` 复制到 `/etc/pkg/` 目录下：

```sh
# cp /dist/packages/repos/FreeBSD_install_cdrom.conf /etc/pkg/
```

```sh
/etc/
└── pkg/ # pkg 仓库配置目录
    └── FreeBSD_install_cdrom.conf # DVD 仓库配置文件
```

### 测试安装

安装 Xorg 图形系统：

```sh
# pkg install xorg
Updating FreeBSD_install_cdrom repository catalogue...
FreeBSD_install_cdrom repository is up to date.
All repositories are up to date.
Checking integrity... done (0 conflicting)
The following 1 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
	xorg: 7.7_3

Number of packages to be installed: 1

Proceed with this action? [y/N]:
```

## 参考文献

- FreeBSD Project. HOWTO: Install binary package without internet access[EB/OL]. [2026-03-25]. <https://forums.freebsd.org/threads/howto-install-binary-package-without-internet-acces.60723/>. 无网络环境下通过 DVD 安装二进制包的方法。
- FreeBSD Project. pkg(8) -- package manager[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=8>. FreeBSD 包管理器手册页。

## 课后习题

1. 阅读 `bsdconfig` 的源代码，定位 `No pkg(8) database found!` 错误的原因，并尝试修复该问题使其能够正常使用 DVD 安装软件。

2. 分析 DVD 安装方式中路径被硬编码为 `/dist` 的设计，重构这一机制使其支持自定义路径。

3. 修改 pkg 的仓库配置机制，使其支持从本地文件系统的任意目录作为软件源，并验证其在离线环境中的可用性。
