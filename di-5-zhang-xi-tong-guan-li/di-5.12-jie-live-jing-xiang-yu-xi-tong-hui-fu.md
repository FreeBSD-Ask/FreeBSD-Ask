# 5.12 Live 镜像与系统恢复

## 系统恢复方法概述

单用户模式是 FreeBSD 提供的一种系统维护模式，在该模式下系统仅加载最小化环境，以 root 权限运行，默认无需输入密码。进入单用户模式后，可进行系统修复、密码重置等操作。

开机按 2 进入 `single user` 模式，即可进入单用户模式。该模式下默认无需输入 root 密码，可使用 `passwd` 命令自行重置密码。

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
> ![Ubuntu ZFS](../.gitbook/assets/Ubuntu-zfs.png)

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

组合使用 `zpool import -fR /mnt zroot` 表示强制将 zroot 池导入到 `/mnt` 作为备用根目录。

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

将指定 U 盘分区挂载到 /mnt 并以读写模式访问：

```sh
# mount /dev/adaXpN -o rw /mnt
```

参数说明：

- 可通过 `dmesg` 命令查看设备信息来确定 `ada` 后的具体编号
- `X`、`N` 的参数取决于具体设备编号。

## 课后习题

1. 进入单用户模式后，尝试修改 ZFS 文件系统的只读属性并重置 root 密码，比较 UFS 和 ZFS 在系统恢复时的操作差异。

2. 尝试修改 FreeBSD Live 镜像生成脚本，使其可挂载，并将其贡献到 FreeBSD 项目。
