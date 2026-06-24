# 8.6 使用 DVD 安装软件

## 挂载 DVD

使用 DVD 安装软件前，首先需将 DVD 挂载到系统。挂载方式有两种，分别适用于本地 ISO 文件和物理 DVD 设备。

要挂载现有的文件系统镜像，请使用 `mdconfig` 为 ISO 文件的指定名称和空闲的单元编号。随后，引用该单元编号将其挂载到现有的挂载点。挂载后，ISO 文件中的文件将显示在挂载点中。

```sh
DVD 安装软件流程

  ISO 文件
      │　
      │ mdconfig　　　　　　　　　　
      ▼
  /dev/md0
      │　
      │ mount -t cd9660　　　　　　　　　　　　　　　　　
      ▼
  /dist（挂载点）
      │　
      │ pkg install　　　　　　　　　　　　　
      ▼
  软件安装完成（离线）
```

此示例将 **FreeBSD-14.2-RELEASE-amd64-dvd1.iso** 附加到内存设备 **/dev/md0**，随后将该内存设备挂载到 **/dist**：

### 直接挂载本地 ISO

```sh
# mdconfig -f /home/ykla/FreeBSD-14.2-RELEASE-amd64-dvd1.iso  # 请替换为实际 ISO 路径，可使用 pwd 查看当前路径
md0
# mkdir -p /dist  # 创建挂载路径，必须是此路径
# mount -t cd9660 /dev/md0 /dist # 不能直接挂载 ISO，会报错 block device required
```

注意，`-t cd9660` 用于挂载 ISO 格式。

### 直接使用 DVD 设备（如通过虚拟机直接挂载的 ISO 镜像）

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

因为 `packages/repos/FreeBSD_install_cdrom.conf` 中的路径是固定值，无法修改，所以如果将目录 **/dist** 改为其他路径，则使用环境变量的方法无效。

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

将 `FreeBSD_install_cdrom.conf` 复制到 **/etc/pkg/** 目录下：

```sh
# cp /dist/packages/repos/FreeBSD_install_cdrom.conf /etc/pkg/
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

## 弹出 DVD 并释放资源

当不再使用内存磁盘时，应将其资源释放回系统。首先，卸载文件系统，随后使用 `mdconfig` 从系统中分离磁盘并释放其资源。继续此示例：

```sh
# umount /dist
# mdconfig -d -u 0
```

要确定是否仍有内存磁盘附加到系统，请输入 `mdconfig -l` 命令。

## 参考文献

- FreeBSD Project. HOWTO: Install binary package without internet access[EB/OL]. [2026-03-25]. <https://forums.freebsd.org/threads/howto-install-binary-package-without-internet-acces.60723/>. 无网络环境下通过 DVD 安装二进制包的方法。
- FreeBSD Project. pkg(8) -- package manager[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=8>. FreeBSD 包管理器手册页。

## 课后习题

1. 阅读 `bsdconfig` 的源代码，定位 `No pkg(8) database found!` 错误的原因，并尝试修复该问题使其能够正常利用 DVD 安装软件。

2. 分析 DVD 安装方式中路径被硬编码为 **/dist** 的设计，重构这一机制使其支持自定义路径。

3. 修改 pkg 的仓库配置机制，使其支持从本地文件系统的任意目录作为软件源，并验证其在离线环境中的可用性。
