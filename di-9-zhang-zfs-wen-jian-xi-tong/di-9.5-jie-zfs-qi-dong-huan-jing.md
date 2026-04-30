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

## 参考文献

- vermaden. ZFS Boot Environments Explained[EB/OL]. [2026-03-25]. <https://vermaden.wordpress.com/2025/11/25/zfs-boot-environments-explained/>. 详细阐释 ZFS 启动环境的原理与实践，包含跨版本 ZFS 池兼容方案。
- FreeBSD Project. BootEnvironments[EB/OL]. [2026-03-25]. <https://wiki.freebsd.org/BootEnvironments>. FreeBSD 官方关于启动环境的 Wiki。
- FreeBSD Project. wiki/BootEnvironments[EB/OL]. [2026-04-02]. <https://wiki.freebsd.org/BootEnvironments>. FreeBSD 官方维基关于启动环境的文档。
- FreeBSD Project. zfs -- configures ZFS datasets[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?zfs(8)>. ZFS 数据集管理工具手册页，涵盖快照、克隆与回滚操作。
- FreeBSD Project. zpool -- configures ZFS storage pools[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?zpool(8)>. ZFS 存储池管理工具手册页。
- FreeBSD Project. bectl -- manage ZFS boot environments[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?bectl(8)>. ZFS 启动环境管理工具手册页，涵盖创建、激活与销毁启动环境。

## 课后习题

1. 在 FreeBSD 虚拟机中使用 bectl 创建 2 个不同版本的启动环境，分别安装不同软件包，测试切换启动环境并验证其隔离性。
2. 基于 ZFS 启动环境的快照克隆机制，编写一个最小脚本实现自动创建和管理启动环境。
3. 修改 ZFS 启动环境的默认策略，将测试环境设为默认启动环境，重启验证其效果。
