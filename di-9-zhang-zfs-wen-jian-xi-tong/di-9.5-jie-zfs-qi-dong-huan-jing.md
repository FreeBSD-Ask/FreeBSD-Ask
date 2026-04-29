# 9.5 ZFS 启动环境

## 概述

本节介绍 ZFS 启动环境（ZFS Boot Environments, BE）的基本概念和使用方法。

ZFS 启动环境是基于 ZFS 快照与克隆技术构建的系统版本管理机制。

从技术定义而言，“ZFS 启动环境是由某个时间点创建的 ZFS 快照克隆出的可写 ZFS 克隆文件系统”（参见：ZFS Boot Environments Explained[EB/OL]. [2026-03-26]. <https://vermaden.wordpress.com/2025/11/25/zfs-boot-environments-explained/>）。该技术实现了原子更新、多系统并存与快速回滚等核心功能。

启动环境与 Android 系统的 A/B 分区具有相似的设计理念，本质上是原子更新、双系统以及快照与回滚功能的集合。

如果单纯从 FreeBSD 系统备份与还原的角度理解启动环境，可以将正在使用的系统视为“正常世界”。有一种物理学观点认为世界每时每刻都在以不同的事件选择进行分支，将那些我们没有做出选择的事件而产生的分支世界视为可能世界。那么正常世界始终是最新、最完整的；而可能世界只能是用来测试的、有缺陷的，实际上只是我们这样使用而已。即使将其还原到正常世界，也只是回到正常世界的时间线，而不是用可能世界替代正常世界，尽管启动管理在理论上允许这种操作。可能世界也可以被视为“正常世界”，只是我们拣选了 FreeBSD 的某个特定版本或部署作为标准。

> **思考题**
>
> 你相信我们所在的世界相比其他世界具有唯一性而不是其他正常世界的 **副本** 吗？如果是，你可以简单证明一下吗：我们的这个世界是所有可能世界中 **最完美** 的那个。如果不是，那么必然存在一个正常世界，你认为它可能 **正常** 在哪里？

使用 ZFS 快照等技术可以在一个 ZFS 文件系统中实现多套完全独立的操作系统，例如 FreeBSD 14.3-RELEASE、FreeBSD 15.0-RELEASE、Gentoo Linux 等，它们彼此互不干扰。

启动环境还可以实现所谓的“不可变系统”，并且在实现不可变性方面比传统方法更彻底。利用此功能可以直接完整地替换操作系统。

> **思考题**
>
> 可以看到，某些看似时髦的概念往往是旧瓶装 **旧酒**，而 FreeBSD 缺乏的正是这种形式的包装。你怎么看？

启动环境的作用不仅限于系统更新前的备份快照。

## 查看环境

本节介绍如何查看 ZFS 池的升级信息和启动环境状态。首先，查看可升级的 ZFS 池及其支持的特性：

```sh
# zpool upgrade
This system supports ZFS pool feature flags.

All pools are formatted using feature flags.

Every feature flags pool has all supported and requested features enabled.
```

“该系统支持 ZFS 存储池功能标记。所有存储池都采用 feature flags 格式化，每个存储池均启用了所有受支持且被请求的功能。”

说明 ZFS 存储池无需更新。上述命令仅具有预览作用，本身无法实现更新。如需更新，命令为：

```sh
# zpool upgrade ZFS池名
```

该命令用于将指定的 ZFS 存储池升级到当前系统所支持的最新功能版本。

## 启动环境基本用法

本节介绍 ZFS 启动环境的基本创建和管理操作。在默认安装中 `zroot/ROOT/default` 是默认的启动环境。

创建一个 ZFS 快照示例：

```sh
# zfs snap zroot/ROOT/default@new  # 为 zroot/ROOT/default 文件系统创建名为 new 的快照
```

使用刚创建的快照生成一个克隆文件系统：

```sh
# zfs clone zroot/ROOT/default@new zroot/ROOT/new  # 基于 zroot/ROOT/default@new 快照创建一个新的可写 ZFS 克隆文件系统 zroot/ROOT/new
```

生成的克隆文件系统可以作为启动环境，可以使用工具 `bectl` 列出所有 ZFS 启动环境（Boot Environments）：

```sh
# bectl list
BE                                Active Mountpoint Space Created
0915                              -      -          4.00M 2023-09-19 19:44
13.2-RELEASE-p2_2023-09-13_141111 -      -          29.0M 2023-09-13 14:11
new                               -      -          432K  2023-09-20 15:17
default                           NR     /          40.8G 2023-04-10 10:06
```

在 `Active` 列中，`N` 表示当前使用的启动环境，`R` 表示下次启动时将使用的启动环境。

`bectl` 工具可以改变下次使用的启动环境（在启动 FreeBSD 时，启动菜单里选 `8`，也可以改变启动环境）。

激活名为 new 的 ZFS 启动环境，下一次启动将使用该环境：

```sh
# bectl activate new
Successfully activated boot environment new
```

再次用 `bectl list` 查看所有 ZFS 启动环境（Boot Environments），观察 Active 列的变化：

```sh
# bectl list
BE                                Active Mountpoint Space Created
0915                              -      -          4.00M 2023-09-19 19:44
13.2-RELEASE-p2_2023-09-13_141111 -      -          29.0M 2023-09-13 14:11
new                               R      /          2.84M 2023-09-20 15:17
default                           N      -          40.8G 2023-04-10 10:06
```

重启 FreeBSD（在启动菜单中选择 `new` 启动环境，或使用 `bectl activate new` 切换到 `new` 启动环境），使用 `df` 查看挂载的根目录文件系统，确认已经切换为 `zroot/ROOT/new`。

列出当前文件系统的磁盘使用情况：

```sh
# df
Filesystem          1K-blocks     Used     Avail Capacity  Mounted on
zroot/ROOT/new      110611616 42612156  67999460    39%    /
devfs                       1        1         0   100%    /dev
/dev/gpt/efiboot0      266176     1872    264304     1%    /boot/efi
fdescfs                     1        1         0   100%    /dev/fd
```

若需切换回 `zroot/ROOT/default` 启动环境，可在启动菜单中选择 `default`，或使用 `bectl activate default` 切换到 `default` 启动环境。

## ZFS 启动环境与多版本共存

本节系统介绍 ZFS 启动环境（Boot Environment，BE）的创建与管理，以及基于 pkgbase 的系统版本升级方法。

ZFS 启动环境为 FreeBSD 提供了安全、灵活的系统更新与多版本共存机制。

### 创建启动环境 15.0-RELEASE

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

Active 字段解释（来自 [bectl(8) 手册页](https://man.freebsd.org/cgi/man.cgi?bectl)）：

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

### 将启动环境中的系统版本更新到 15.0-RELEASE

创建好启动环境后，需要在其中进行系统版本的更新操作。整个过程分为挂载启动环境、验证版本、转换为 pkgbase 以及升级到目标版本等步骤。

#### 挂载启动环境 15.0-RELEASE

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

由输出可知，已经成功将启动环境 15.0-RELEASE 挂载到了指定路径。

#### 验证当前 FreeBSD 版本

目前 15.0-RELEASE 实际上仍是 14.3-RELEASE。虽然这是已知事实，但仍可使用命令 `freebsd-version` 进行验证。

在 `/mnt/upgrade` 环境中运行 `freebsd-version`：

```sh
# chroot /mnt/upgrade freebsd-version -kru
14.3-RELEASE
14.3-RELEASE
14.3-RELEASE
```

`freebsd-version` 参数解释（摘自手册页 [freebsd-version(1)](https://man.freebsd.org/cgi/man.cgi?freebsd-version)）：

- `-k`：打印已安装内核的版本和补丁级别。与 [uname(1)](https://man.freebsd.org/uname(1)) 不同的是，如果新的内核已经安装但系统尚未重启，`freebsd-version` 会打印新内核的版本和补丁级别。
- `-r`：打印正在运行中的内核的版本和补丁级别。与 [uname(1)](https://man.freebsd.org/uname(1)) 不同的是，`freebsd-version` 不受环境变量影响。
- `-u`：打印已安装用户态的版本和补丁级别。这些信息在构建过程中会被写入程序 `freebsd-version` 中。

#### 使用 pkgbase 将启动环境中的 14.3-RELEASE（系统版本）转换为 pkgbase

在开始升级之前，需要将传统的 FreeBSD 系统转换为 pkgbase 格式。pkgbase 是 FreeBSD 官方提供的一种新的基本系统打包方式，它使用 pkg 包管理器来管理系统组件。

pkgbase 的设计初衷是为了让 stable、current 和 release（包括 BETA、RC 等）都能使用统一的二进制工具进行更新。之前，stable 和 current 只能通过完整编译源代码的方式进行更新。

> **注意**
>
> 仅 FreeBSD 14.0-RELEASE 及更高版本才能直接转换为 pkgbase。旧版仍需要通过 `freebsd-update` 进行更新（运行时 pkgbasify 会提示 `Unsupported FreeBSD version`，即 FreeBSD 版本不受支持）。

> **警告**
>
>**存在风险，可能会丢失所有数据！建议在操作前做好备份。**

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

由输出可知，pkgbasify 已将系统更新到最新的补丁版本，并完成了向 pkgbase 的转换。

#### 使用 pkgbase 将启动环境中的系统版本更新到 15.0-RELEASE

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

#### 启动到启动环境 15.0-RELEASE

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

### 附录：永久性使用 15.0-RELEASE

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

### 将基本系统中的 ZFS 替换为 Ports 版本

在实现多版本 FreeBSD 共存时，一个重要的考虑因素是 ZFS 池版本的兼容性问题。不同版本的 FreeBSD 内置的 ZFS 版本可能不同，这可能导致无法互相访问存储池。

通常，在 FreeBSD 大版本之间，ZFS 池版本和特性都会发生变化，例如从 13 到 14 时 zpool 就有所变动。

可通过 Ports 中的 OpenZFS 实现 13、14、15 等多个系统版本的共存。

> **警告**
>
> 如不按照下方进行设置就强行升级 ZFS 池/特性，将无法访问旧版系统。

那些有意愿实现多版本共存的读者可以直接重启，进入启动环境 `default`（14.3-RELEASE）。

#### 验证当前的系统版本

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

#### 查看内置的 OpenZFS 版本

首先，查看一下当前系统内置的 ZFS 版本信息，以便了解要替换的是什么。

显示当前 ZFS 工具和内核模块的版本信息：

```sh
# zfs --version
zfs-2.2.7-FreeBSD_ge269af1b3
zfs-kmod-2.2.7-FreeBSD_ge269af1b3
```

目前 FreeBSD 基本系统内置的是 OpenZFS 2.2.7（即来自 <https://github.com/openzfs/zfs/commit/e269af1b3>）

#### 安装 filesystems/openzfs

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

#### 编辑 `/boot/loader.conf` 文件

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

#### 检查 ZFS 版本

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

### 附录：给 pkgbasify 脚本切换软件源

对于网络环境受限制的用户，可能需要为 pkgbasify 脚本配置国内镜像源以提高下载速度。下面介绍如何修改脚本中的源地址。

#### 修改示例（使用 USTC）

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

#### 南京大学开源镜像站 NJU

除了 USTC 镜像站外，南京大学也提供了 FreeBSD pkgbase 的镜像源，其地址如下。

```ini
https://mirrors.nju.edu.cn/freebsd-pkg/
```

#### 网易开源镜像站 163

网易开源镜像站同样提供了 FreeBSD pkgbase 的镜像服务，地址如下。

```ini
https://mirrors.163.com/freebsd-pkg/
```

### 附录：配置软件源

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

本节介绍的内容涉及多个技术点，下面列出了一些相关的参考文献，供有兴趣的读者进一步学习。

- vermaden. ZFS Boot Environments Explained[EB/OL]. [2026-03-25]. <https://vermaden.wordpress.com/2025/11/25/zfs-boot-environments-explained/>. 详细阐释 ZFS 启动环境的原理与实践，包含跨版本 ZFS 池兼容方案。
- FreeBSD Project. BootEnvironments[EB/OL]. [2026-03-25]. <https://wiki.freebsd.org/BootEnvironments>. FreeBSD 官方关于启动环境的 Wiki。
- FreeBSD Project. bectl(8)[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?bectl>. ZFS 启动环境管理工具的官方技术规范。
- FreeBSD Project. freebsd-version -- print the version and patch level of the installed FreeBSD[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=freebsd-version&sektion=1>. 系统版本查询命令手册页。
- FreeBSD Project. uname -- print operating system name[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=uname&sektion=1>. 系统信息查询命令手册页。
- FreeBSD Project. wiki/BootEnvironments[EB/OL]. [2026-04-02]. <https://wiki.freebsd.org/BootEnvironments>. FreeBSD 官方维基关于启动环境的文档。
- FreeBSD Project. zfs -- configures ZFS datasets[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?zfs(8)>. ZFS 数据集管理工具手册页，涵盖快照、克隆与回滚操作。
- FreeBSD Project. zpool -- configures ZFS storage pools[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?zpool(8)>. ZFS 存储池管理工具手册页。
- FreeBSD Project. bectl -- manage ZFS boot environments[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?bectl(8)>. ZFS 启动环境管理工具手册页，涵盖创建、激活与销毁启动环境。

## 课后习题

1. 在 FreeBSD 虚拟机中使用 bectl 创建 2 个不同版本的启动环境，分别安装不同软件包，测试切换启动环境并验证其隔离性。
2. 基于 ZFS 启动环境的快照克隆机制，编写一个最小脚本实现自动创建和管理启动环境。
3. 修改 ZFS 启动环境的默认策略，将测试环境设为默认启动环境，重启验证其效果。
