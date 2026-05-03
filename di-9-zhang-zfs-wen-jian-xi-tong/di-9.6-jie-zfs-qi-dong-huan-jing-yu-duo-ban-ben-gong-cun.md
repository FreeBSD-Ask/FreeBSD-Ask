# 9.6 ZFS 启动环境与多版本共存

借助 ZFS 启动环境，可以在同一台机器上保留多个独立的系统版本，升级失败时无需重新安装即可回退到先前状态。

ZFS 启动环境为 FreeBSD 提供了安全、灵活的系统更新与多版本共存机制。

## 创建启动环境 15.0-RELEASE

ZFS 启动环境（Boot Environment，BE）是 FreeBSD 的一个重要特性，它能在系统中创建多个独立的系统环境，从而实现不同系统版本的共存与安全切换。下面将创建一个名为 15.0-RELEASE 的启动环境。

- 使用工具 bectl 创建启动环境 `15.0-RELEASE`：

```sh
# bectl create 15.0-RELEASE
```

> **注意**
>
> 只是将其命名为 15.0，实际上系统仍然是 14.3-RELEASE。

- 使用 bectl 检查启动环境：

```sh
$ bectl list # 显示所有启动环境
BE           Active Mountpoint Space Created
15.0-RELEASE -      -          176K  2025-12-05 22:27
default      NR     /          10.6G 2025-01-14 20:36
```

Active 字段解释（来自 bectl(8) 手册页）：

- “N”：表示该启动环境当前是否处于活动状态（当前是否位于此环境中）
- “R”：在重启时是否处于活动状态（下次是否选中，用于固定选项）
- “T”：是否会在下次启动时生效（且仅下次，用于一次性选项）
- “NRT”：这些标识（N / R / T）理论上可以组合出现（但实际不会出现，该组合在语义上存在矛盾）

- 列出系统中所有 ZFS 文件系统及其属性：

```sh
# zfs list
NAME                      USED  AVAIL  REFER  MOUNTPOINT

……其他省略……

zroot/ROOT/15.0-RELEASE     8K  83.8G  10.6G  /

……其他省略……
```

注意 `zroot/ROOT/15.0-RELEASE     8K  83.8G  10.6G  /` 这一行是刚刚创建的。

## 将启动环境中的系统版本更新到 15.0-RELEASE

创建好启动环境后，需要在其中进行系统版本的更新操作。整个过程分为挂载启动环境、验证版本、转换为 pkgbase 以及升级到目标版本等步骤。

### 挂载启动环境 15.0-RELEASE

要对启动环境进行操作，首先需要将其挂载到文件系统中的某个目录。下面将创建一个临时目录并挂载启动环境。

- 创建一个临时目录，用于更新启动环境 15.0-RELEASE 中的系统

```sh
# mkdir /mnt/upgrade
```

```sh
/mnt/
└── upgrade/ # 启动环境挂载目录
    └── usr/
        └── local/
            └── etc/
                └── pkg/
                    └── repos/
                        └── FreeBSD-base.conf # pkgbase 源配置文件
```

- 将启动环境（实际上是一个数据集）15.0-RELEASE 挂载到下面的路径中

```sh
# bectl mount 15.0-RELEASE /mnt/upgrade
/mnt/upgrade
```

- 显示已挂载文件系统的磁盘使用情况：

```sh
# df
Filesystem              1K-blocks     Used    Avail Capacity  Mounted on

……其他省略……

zroot/ROOT/15.0-RELEASE  99036272 11132688 87903584    11%    /mnt/upgrade

……其他省略……
```

### 验证当前 FreeBSD 版本

目前 15.0-RELEASE 实际上仍是 14.3-RELEASE。虽然这是已知事实，但仍可使用命令 `freebsd-version` 进行验证。

在 `/mnt/upgrade` 环境中运行 `freebsd-version`：

```sh
# chroot /mnt/upgrade freebsd-version -kru
14.3-RELEASE
14.3-RELEASE
14.3-RELEASE
```

`freebsd-version` 参数解释（摘自手册页 freebsd-version(1)）：

- `-k`：打印已安装内核的版本和补丁级别。与 uname(1)) 不同的是，如果新的内核已经安装但系统尚未重启，`freebsd-version` 会打印新内核的版本和补丁级别。
- `-r`：打印正在运行中的内核的版本和补丁级别。与 uname(1)) 不同的是，`freebsd-version` 不受环境变量影响。
- `-u`：打印已安装用户态的版本和补丁级别。这些信息在构建过程中会被写入程序 `freebsd-version` 中。

### 使用 pkgbase 将启动环境中的 14.3-RELEASE（系统版本）转换为 pkgbase

在开始升级之前，需要将传统的 FreeBSD 系统转换为 pkgbase 格式。pkgbase 是 FreeBSD 官方提供的一种新的基本系统打包方式，它使用 pkg 包管理器来管理系统组件。

pkgbase 的设计初衷是为了让 stable、current 和 release（包括 BETA、RC 等）都能使用统一的二进制工具进行更新。之前，stable 和 current 只能通过完整编译源代码的方式进行更新。

> **注意**
>
> 仅 FreeBSD 14.0-RELEASE 及更高版本才能直接转换为 pkgbase。旧版仍需要通过 `freebsd-update` 进行更新（运行时 pkgbasify 会提示 `Unsupported FreeBSD version`，即 FreeBSD 版本不受支持）。

> **警告**
>
> **存在风险，可能会丢失所有数据！建议在操作前做好备份。**

- 在 /mnt/upgrade 环境中锁定 pkg 软件包，防止被升级或修改：

```sh
# pkg -c /mnt/upgrade lock pkg  # 在 /mnt/upgrade 环境中锁定 pkg 软件包
pkg-2.4.2_1: lock this package? [y/N]: y # 输入 y 按回车键确认锁定 pkg
Locking pkg-2.4.2_1
```

- 下载 pkgbase 转换脚本

```sh
# fetch -o /mnt/upgrade https://raw.githubusercontent.com/FreeBSDFoundation/pkgbasify/main/pkgbasify.lua  # 下载 pkgbase 转换脚本
```

- 使用 pkgbasify 进行转换

> **警告**
>
> 在接受 `Do you accept this risk and wish to continue? (y/n)` 这个风险提示后就没有其他二次确认了！

```sh
# chroot /mnt/upgrade /usr/libexec/flua pkgbasify.lua  # 使用 pkgbasify 进行转换
Running this tool will irreversibly modify your system to use pkgbase.
This tool and pkgbase are experimental and may result in a broken system.
It is highly recommended to backup your system before proceeding.
Do you accept this risk and wish to continue? (y/n) y # 这里是风险提示，确认
Updating FreeBSD repository catalogue...

……此处省略……

The following 370 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
        FreeBSD-acct: 14.3p6 [FreeBSD-base]
        FreeBSD-acct-man: 14.3p6 [FreeBSD-base]
        FreeBSD-acpi: 14.3p6 [FreeBSD-base]
        FreeBSD-acpi-man: 14.3p6 [FreeBSD-base]

……此处省略……

Conversion finished.

Please verify that the contents of the following critical files are as expected:
/etc/master.passwd
/etc/group
/etc/ssh/sshd_config

After verifying those files, restart the system.
```

- 检查启动环境 15.0-RELEASE 中的系统版本

```sh
# chroot /mnt/upgrade freebsd-version -kru
14.3-RELEASE-p6
14.3-RELEASE
14.3-RELEASE-p6
```

### 使用 pkgbase 将启动环境中的系统版本更新到 15.0-RELEASE

成功转换为 pkgbase 后，就可以使用 pkg 包管理器来升级系统版本了。下面将配置 pkgbase 源并执行升级操作。

软件源结构：

```sh
/usr/local/etc/pkg/
└── repos/ # pkg 仓库配置目录
    └── FreeBSD-base.conf # pkgbase 源配置文件
```

- 创建 pkgbase 软件源目录

```sh
# mkdir -p /mnt/upgrade/usr/local/etc/pkg/repos/  # 创建 pkgbase 软件源目录
```

- 编辑 `/mnt/upgrade/usr/local/etc/pkg/repos/FreeBSD-base.conf` 文件，添加 pkgbase 源

```ini
FreeBSD-base {
    url = "https://pkg.freebsd.org/${ABI}/base_release_${VERSION_MINOR}";
    enabled = yes;
}
```

> **警告**
>
> 请检查 `FreeBSD-base.conf` 的内容，尤其是 **不应该** 在其中手动硬编码写入指定任何具体的版本（如 `base_release_3`）。

> **技巧**
>
> 需要切换软件源的用户可以将 `url` 这行改为 `url = "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_release_${VERSION_MINOR}";`。而对于那些优先考虑安全性的读者应该维持默认设置。

- 刷新软件源

```sh
# pkg -c /mnt/upgrade update -r FreeBSD-base  # 刷新软件源
```

- 使用 pkgbase 将 14.3-RELEASE 更新到 15.0-RELEASE（即将 ABI 指定为 15）

```sh
# env ABI=FreeBSD:15:amd64 pkg-static -c /mnt/upgrade upgrade -r FreeBSD-base  # 在 /mnt/upgrade 环境中使用指定 ABI 升级 FreeBSD 基本系统包
pkg-static: Setting ABI requires setting OSVERSION, guessing the OSVERSION as: 1500000
pkg-static: Warning: Major OS version upgrade detected.  Running "pkg bootstrap -f" recommended
Updating FreeBSD-base repository catalogue...
pkg-static: Repository FreeBSD-base has a wrong packagesite, need to re-create database
Fetching meta.conf: 100%    179 B   0.2kB/s    00:01
Fetching data.pkg: 100%   80 KiB  81.6kB/s    00:01
Processing entries:   0%
Newer FreeBSD version for package FreeBSD-zlib-dbg:
To ignore this error set IGNORE_OSVERSION=yes
- package: 1500068
- running userland: 1500000
Ignore the mismatch and continue? [y/N]: y # 此处输入 y 后继续
Processing entries: 100%
FreeBSD-base repository update completed. 496 packages processed.
FreeBSD-base is up to date.
Checking for upgrades (230 candidates): 100%
Processing candidates (230 candidates): 100%
The following 290 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
        FreeBSD-atf: 15.0 [FreeBSD-base]
        FreeBSD-atf-dev: 15.0 [FreeBSD-base]
        FreeBSD-atf-lib: 15.0 [FreeBSD-base]

        ……此处省略一部分…

        FreeBSD-zoneinfo: 14.3p6 -> 15.0 [FreeBSD-base]

Number of packages to be installed: 61
Number of packages to be upgraded: 229

The operation will free 100 MiB.
473 MiB to be downloaded.

Proceed with this action? [y/N]: y # 此处输入 y 后继续
```

> **技巧**
>
> 如果检查不到任何更新，请确认当前是否已成功转换为 pkgbase，并检查软件源配置是否正确

- 检查启动环境 15.0-RELEASE 中的系统版本

```sh
# chroot /mnt/upgrade freebsd-version -kru
15.0-RELEASE
14.3-RELEASE
15.0-RELEASE
```

这里 `r` 显示为 14.3-RELEASE 并无异常，说明当前运行的仍是 14.3-RELEASE。结合其他参数，可知重启后才会变为 15.0-RELEASE。

- 解锁 pkg

```sh
# chroot /mnt/upgrade pkg unlock pkg  # 解锁 pkg
pkg: Warning: Major OS version upgrade detected.  Running "pkg bootstrap -f" recommended
pkg-2.4.2_1: unlock this package? [y/N]: y
Unlocking pkg-2.4.2_1
```

- 将所有第三方软件包的 ABI 更新至 FreeBSD 15.0

```sh
# chroot /mnt/upgrade pkg upgrade  # 将所有第三方软件包的 ABI 更新到 FreeBSD 15.0
```

更新过程中需要多次确认才能完成。

### 启动到启动环境 15.0-RELEASE

完成所有更新操作后，可以尝试启动到新的启动环境中验证更新结果。

- 在下次启动时进入启动环境 15.0-RELEASE

```sh
# bectl activate -t 15.0-RELEASE  # 在下次启动时进入启动环境 15.0-RELEASE
Successfully activated boot environment 15.0-RELEASE
for next boot
```

- 验证设置是否成功。列出系统中所有 ZFS 启动环境：

```sh
$ bectl list
BE                             Active Mountpoint   Space Created
15.0-RELEASE                   T      /mnt/upgrade 8.75G 2025-12-05 23:22
default                        NR     /            10.9G 2025-01-14 20:36
```

注意，这是一次性的（`T`），此处仅用于验证其是否能够正常启动。还需要回到当前的主系统 14.3-RELEASE 来更新 ZFS。

- 重启以进入启动环境 15.0-RELEASE

```sh
# reboot  # 重启以进入启动环境 15.0-RELEASE
```

- 验证版本：

```sh
$ freebsd-version -kru
15.0-RELEASE
15.0-RELEASE
15.0-RELEASE
$ bectl list
BE                             Active Mountpoint Space Created
15.0-RELEASE                   N      /          8.75G 2025-12-05 23:22
default                        R      -          10.9G 2025-01-14 20:36
```

由输出可知，已经成功将启动环境 15.0-RELEASE 中的 FreeBSD 系统升级到了 15.0-RELEASE，此时启动环境名称与实际版本一致。

并且 `R` 意味着再次重启将回到启动环境 `default`（14.3-RELEASE）。

## 附录：永久性使用 15.0-RELEASE

前面使用的是通过一次性启动环境的方式进行验证。如果验证通过并且不需要再保留旧版本，可以将新环境设置为永久默认。

如果读者不需要多版本共存，并且验证过目前的环境满足需要，也可以将启动环境 15.0-RELEASE 设置为永久的：

```sh
# bectl activate 15.0-RELEASE
```

随后，读者也可以销毁不再需要的启动环境：

```sh
# bectl destroy 要销毁的启动环境名称
```

将参数 `要销毁的启动环境名称` 替换为命令 `bectl list` 输出中 `BE` 列对应的启动环境名称即可将其销毁。

## 将基本系统中的 ZFS 替换为 Ports 版本

在实现多版本 FreeBSD 共存时，一个重要的考虑因素是 ZFS 池版本的兼容性问题。不同版本的 FreeBSD 内置的 ZFS 版本可能不同，这可能导致无法互相访问存储池。

通常，在 FreeBSD 大版本之间，ZFS 池版本和特性都会发生变化，例如从 13 到 14 时 zpool 就有所变动。

可通过 Ports 中的 OpenZFS 实现 13、14、15 等多个系统版本的共存。

> **警告**
>
> 如不按照下方进行设置就强行升级 ZFS 池/特性，将无法访问旧版系统。

那些有意愿实现多版本共存的读者可以直接重启，进入启动环境 `default`（14.3-RELEASE）。

### 验证当前的系统版本

在开始操作之前，需要确认已经回到了默认的启动环境中。

需要确认确实在启动环境 `default`（14.3-RELEASE）中。

```sh
$ bectl list
BE                             Active Mountpoint Space Created
15.0-RELEASE                   -      -          8.75G 2025-12-05 23:22
default                        NR     /          10.9G 2025-01-14 20:36
$ freebsd-version -kru
14.3-RELEASE
14.3-RELEASE
14.3-RELEASE
```

由输出可知，已回到默认启动环境。

### 查看内置的 OpenZFS 版本

首先，查看一下当前系统内置的 ZFS 版本信息，以便了解要替换的是什么。

显示当前 ZFS 工具和内核模块的版本信息：

```sh
# zfs --version
zfs-2.2.7-FreeBSD_ge269af1b3
zfs-kmod-2.2.7-FreeBSD_ge269af1b3
```

目前 FreeBSD 基本系统内置的是 OpenZFS 2.2.7（即来自 <https://github.com/openzfs/zfs/commit/e269af1b3>）

### 安装 filesystems/openzfs

Ports 中的 OpenZFS 提供了比基本系统更灵活的版本选择。可以使用 pkg 或 Ports 两种方式来安装它。

- 使用 pkg 安装

```sh
# pkg install openzfs
```

- 使用 ports 安装：

```sh
# cd /usr/ports/filesystems/openzfs/
# make install clean
```

### 编辑 `/boot/loader.conf` 文件

安装完成后，需要配置系统启动时加载哪个 ZFS 模块。默认情况下，系统会加载基本系统内置的 ZFS 模块，需要修改这个行为。

为了防止系统加载基本系统内置的 ZFS 版本，需要在 `zfs_load=YES` 前加上注释 `#`，取消其开机自动加载。

形如：

```ini
# zfs_load=YES 	# 不加载内置 ZFS 内核模块
```

再新增下列数行：

```ini
zfs_load=NO        # 显式禁用内置 ZFS 内核模块加载
openzfs_load=YES   # 启用 OpenZFS 模块加载
```

完成后重启系统。

### 检查 ZFS 版本

配置完成并重启后，需要验证系统是否正确加载了 Ports 版本的 OpenZFS。

在重启后，检查 ZFS 版本：

```sh
# zfs --version
zfs-2.2.7-FreeBSD_ge269af1b3
zfs-kmod-2.3.5-1
```

随后即可更新其他存储池或启用新的特性。

> **警告**
>
> 考虑到基本系统中的 OpenZFS 版本不一定是最新的，因此建议对所有版本都使用 Ports 中的版本以期达到统一。换言之，建议读者也在 15.0-RELEASE 中按照相同方法替换 ZFS。

## 附录：给 pkgbasify 脚本切换软件源

对于网络环境受限制的用户，可能需要为 pkgbasify 脚本配置国内镜像源以提高下载速度。下面介绍如何修改脚本中的源地址。

### 修改示例（使用 USTC）

中国科学技术大学（USTC）提供了 FreeBSD 的镜像服务，可以修改 pkgbasify 脚本来使用这个镜像源。首先需要找到脚本中的相关函数。

找到 Lua 脚本中的 `create_base_repo_conf` 函数：

```lua
local function base_repo_url()
	local major, minor, branch = freebsd_version()
	if math.tointeger(major) < 14 then
		fatal("Unsupported FreeBSD version: " .. raw)
	end
	if branch == "RELEASE" or branch:match("^BETA") or branch:match("^RC") then
		return "pkg+https://pkg.FreeBSD.org/${ABI}/base_release_" .. minor
	elseif branch == "CURRENT" or
		branch == "STABLE" or
		branch == "PRERELEASE" or
		branch:match("^ALPHA")
	then
		return "pkg+https://pkg.FreeBSD.org/${ABI}/base_latest"
	else
		fatal("Unsupported FreeBSD version: " .. raw)
	end
end
```

将这个函数修改如下，其中在 `return` 部分指定了镜像站：

```lua
local function base_repo_url()
	local major, minor, branch = freebsd_version()
	if math.tointeger(major) < 14 then
		fatal("Unsupported FreeBSD version: " .. raw)
	end
	if branch == "RELEASE" or branch:match("^BETA") or branch:match("^RC") then
		return "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_release_" .. minor
	elseif branch == "CURRENT" or
		branch == "STABLE" or
		branch == "PRERELEASE" or
		branch:match("^ALPHA")
	then
		return "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_latest"
	else
		fatal("Unsupported FreeBSD version: " .. raw)
	end
end
```

> **警告**
>
> 请删除 `return "pkg+https://"` 这行中的 `pkg+`，否则会报错。

再找到下面的函数 `create_base_repo_conf`

```lua
local function create_base_repo_conf(path)
	assert(os.execute("mkdir -p " .. path:match(".*/")))
	local f <close> = assert(io.open(path, "w"))
	if math.tointeger(freebsd_version()) >= 15 then
		assert(f:write(string.format([[
%s: {
  enabled: yes
}
]], options.repo_name)))
	else
		assert(f:write(string.format([[
%s: {
  url: "%s",
  mirror_type: "srv",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
]], options.repo_name, base_repo_url())))
	end
end
```

修改如下（删除了 srv 相关数行）：

```lua
local function create_base_repo_conf(path)
	assert(os.execute("mkdir -p " .. path:match(".*/")))
	local f <close> = assert(io.open(path, "w"))
	if math.tointeger(freebsd_version()) >= 15 then
		assert(f:write(string.format([[
%s: {
  enabled: yes
}
]], options.repo_name)))
	else
		assert(f:write(string.format([[
%s: {
  url: "%s",
  enabled: yes
}
]], options.repo_name, base_repo_url())))
	end
end
```

> **注意**
>
> 对于那些优先考虑安全性的读者，应该保持默认设置。

### 南京大学开源镜像站 NJU

除了 USTC 镜像站外，南京大学也提供了 FreeBSD pkgbase 的镜像源，其地址如下。

```ini
https://mirrors.nju.edu.cn/freebsd-pkg/
```

### 网易开源镜像站 163

网易开源镜像站同样提供了 FreeBSD pkgbase 的镜像服务，地址如下。

```ini
https://mirrors.163.com/freebsd-pkg/
```

## 附录：配置软件源

为了帮助读者更好地配置 pkgbase 源，下面整理了 FreeBSD 官方源的 pkgbase 信息，包括各分支的更新频率和对应的 URL 地址。

| 分支 | 更新频率 | URL 地址 |
| ---- | -------- | -------- |
| main（16.0-CURRENT） | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_latest> |
| main（16.0-CURRENT） | 每周一次：星期日 20:00 | <https://pkg.freebsd.org/${ABI}/base_weekly> |
| stable/14 | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_latest> |
| stable/14 | 每周一次：星期日 20:00 | <https://pkg.freebsd.org/${ABI}/base_weekly> |
| releng/14.0（RELEASE） | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_release_0> |
| releng/14.1（RELEASE） | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_release_1> |
| releng/14.2（RELEASE） | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_release_2> |
| releng/14.3（RELEASE） | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_release_3> |

以上表格中的时间已转换为北京时间（东八区），对应 FreeBSD 官方镜像站的发布时间。

若官方源下载速度慢，可以考虑改用国内镜像。只需要替换 `https://pkg.freebsd.org` 这部分。

## 参考文献

- vermaden. ZFS Boot Environments Explained[EB/OL]. [2026-03-25]. <https://vermaden.wordpress.com/2025/11/25/zfs-boot-environments-explained/>. 详细阐释 ZFS 启动环境的原理与实践，包含跨版本 ZFS 池兼容方案。
- FreeBSD Project. BootEnvironments[EB/OL]. [2026-03-25]. <https://wiki.freebsd.org/BootEnvironments>. FreeBSD 官方关于启动环境的 Wiki。
- FreeBSD Project. bectl(8)[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?bectl>. ZFS 启动环境管理工具的官方技术规范。
- FreeBSD Project. freebsd-version -- print the version and patch level of the installed FreeBSD[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=freebsd-version&sektion=1>. 系统版本查询命令手册页。
- FreeBSD Project. uname -- print operating system name[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=uname&sektion=1>. 系统信息查询命令手册页。

## 课后习题

1. 阅读 pkgbasify 脚本的源代码，尝试使用高级编程语言重构提高执行效率。

2. 选取 ZFS 启动环境的快照机制，在 UFS 文件系统上进行实现。

3. 修改 pkgbase 的默认更新策略，使其可以同时保留多个版本的系统组件，验证其在回滚场景下的可用性。
