# 5.12 Live 镜像与系统恢复

## 系统恢复方法概述

FreeBSD 系统恢复可根据故障严重程度选择不同的方法，按侵入性从低到高排列如下：

1. **单用户模式（Single-User Mode）**：系统启动至运行级 1（run level 1），仅挂载根文件系统（**/**），不启动网络服务和多用户环境，以 root 权限运行。开机按 2 进入 `single user` 模式，默认无需输入密码，可使用 `passwd` 命令重置密码。

2. **Live 镜像启动**：从安装介质（U 盘或光盘）启动完整的 FreeBSD 运行环境，不依赖硬盘上的系统。适用于引导加载器损坏、根文件系统严重损坏、磁盘分区表丢失等无法从硬盘启动的场景。Live 环境提供了完整的工具链，可执行文件系统检查（`fsck`）、ZFS 池导入（`zpool import`）、数据备份等操作。

3. **灾难恢复**：当整个存储子系统不可用时，须依赖预先创建的备份（如 ZFS 快照的远程复制、`dump`/`restore` 备份）进行系统重建。此场景超出本节范围。

## UFS 文件系统下的系统恢复操作

将根 UFS 文件系统挂载为可写：

```sh
# mount -u /
```

挂载所有 UFS 文件系统：

```sh
# mount -a -t ufs
```

## ZFS 文件系统

> **技巧**
>
> 在某些情况下，FreeBSD Live 镜像对 ZFS 磁盘的操作可能受限，例如无法创建挂载点或修改为可写模式。此类限制通常与 Live 镜像的默认配置有关。
>
> 如遇此类问题，可尝试使用 Ubuntu 24.04 或更高版本的 Live 模式对 ZFS 磁盘进行操作，例如还原快照等。
>
> ![Ubuntu ZFS](../.gitbook/assets/ubuntu-zfs.png)

将根文件系统挂载为可写：

```sh
# mount -u
```

挂载所有 ZFS 文件系统：

```sh
# zfs mount -a
```

挂载 ZFS 根文件系统：

```sh
# zpool import -fR /mnt zroot
```

参数说明：

- `-f`：强制导入（force）。
- `-R`：指定备用根目录（altroot）。

组合使用 **zpool import -fR /mnt zroot** 表示强制将 zroot 池导入到 **/mnt** 作为备用根目录。

### 故障排除与未竟事宜

#### `passwd: pam_chauthtok(): Error in service module`

请检查 ZFS 文件系统是否处于只读状态：

```sh
# zfs get all | grep readonly
```

解除 ZFS 文件系统只读属性：

```sh
# zfs set readonly=off zroot
```

#### 参考文献

- OpenZFS. one ZFS file system always starts with readonly=on temporary on boot[EB/OL]. [2026-03-26]. <https://github.com/openzfs/zfs/issues/2133>. 报告 ZFS 文件系统启动时临时以只读模式挂载的问题及社区讨论。

## 使用 U 盘设备

将指定 U 盘分区挂载到 **/mnt** 并以读写模式访问：

```sh
# mount /dev/adaXpN -o rw /mnt
```

参数说明：

- 可通过 `dmesg` 命令查看设备信息以确定 `ada` 后的具体编号
- `X`、`N` 的参数取决于具体设备编号。

## 课后习题

1. 进入单用户模式后，分别对 UFS 和 ZFS 文件系统执行 root 密码重置操作，比较两种文件系统在只读挂载与读写重新挂载方面的差异。
2. 分析 FreeBSD Live 镜像生成脚本（`release/`），评估使其支持持久化挂载所需的修改范围与技术难度。
3. 单用户模式通过绕过认证直接授予 root Shell 权限，这是一种有意为之的安全“后门”。比较这种恢复机制与 Linux 的 `init=/bin/bash` 内核参数在安全设计上的差异，并分析系统恢复便捷性与物理安全防护之间的不可调和矛盾。
