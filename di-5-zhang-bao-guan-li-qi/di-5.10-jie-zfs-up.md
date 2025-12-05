# 使用 ZFS 启动环境更新 FreeBSD 并实现多版本共存

## 从 FreeBSD 14 更新到 FreeBSD 15

### 创建启动环境 15.0-RELEASE

- 使用工具 bectl 创建启动环境 `15.0-RELEASE`

>**注意**
>
>我们只是将其命名为 15.0，实际上系统仍然是 14.3。

```sh
# bectl create 15.0-RELEASE
```

- 使用 bectl 检查：

```
# bectl list # 显示所有启动环境
BE           Active Mountpoint Space Created
15.0-RELEASE -      -          176K  2025-12-05 22:27
default      NR     /          10.6G 2025-01-14 20:36
```

Active 字段解释（来自 [bectl(8) 手册页](https://man.freebsd.org/cgi/man.cgi?bectl)）:

- “N”：表示该启动环境当前是否处于活动状态（现在是否正位于此环境中）
- “R”：在重启时是否处于活动状态（下次是否选中，用于固定选项）
- “T”：是否会在下次启动时生效（且仅下次，用于一次性选项）
- “NRT”：这些标识（N / R / T）可以组合出现（实际上不会出现，该选项存在矛盾）

- 使用 zfs 命令检查：

```sh
# zfs list
NAME                      USED  AVAIL  REFER  MOUNTPOINT

……其他省略……

zroot/ROOT/15.0-RELEASE     8K  83.8G  10.6G  /

……其他省略……
```

注意 `zroot/ROOT/15.0-RELEASE     8K  83.8G  10.6G  /` 这行是刚刚创建的。

### 将启动环境 15.0-RELEASE 更新到 15.0-RELEASE

#### 挂载启动环境 15.0-RELEASE

- 创建一个临时目录用于更新启动环境 15.0-RELEASE 中的 FreeBSD 系统

```sh
# mkdir /mnt/upgrade
```

- 将启动环境（实际上是个快照）15.0-RELEASE 挂载到上面的路径里

```sh
# bectl mount 15.0-RELEASE /mnt/upgrade
/mnt/upgrade
```

- 检查：

```sh
root@ykla:/home/ykla # df
Filesystem              1K-blocks     Used    Avail Capacity  Mounted on

……其他省略……

zroot/ROOT/15.0-RELEASE  99036272 11132688 87903584    11%    /mnt/upgrade

……其他省略……
```

注意到，已经成功地将启动环境 15.0-RELEASE 挂载到了我们设置的路径里。


#### 验证当前 FreeBSD 版本

目前 15.0-RELEASE 实际上是 14.3-RELEASE。虽然是明知的，但还是让我们来用命令 `freebsd-version` 验证这一点：

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


#### 将 14.3-RELEASE 转换到 pkgbase

pkgbase 的设计初衷是为了让 stable、current 和 release（BETA、RC 等）都能使用一种二进制工具进行更新。当下，stable、current 只能通过完全编译源代码的方式来更新。

>**注意**
>
>仅 FreeBSD 14.0-RELEASE 及更高版本才能直接被转换为 pkgbase。旧版仍需要通过 `freebsd-update` 进行更新。

>**警告**
>
>**存在风险，可能会丢失所有数据！建议在操作之前做好备份。**

- 创建 pkgbase 软件源目录

```sh
# mkdir -p /mnt/upgrade/usr/local/etc/pkg/repos/
```

- 编辑 `/mnt/upgrade/usr/local/etc/pkg/repos/FreeBSD-base.conf`，添加 pkgbase 源

```sh
FreeBSD-base {
    url = "https://pkg.freebsd.org/${ABI}/base_release_${VERSION_MINOR}";
    enabled = yes;
}
```

- 锁定 pkg 防止 pkg 故障

```sh
# pkg -c /mnt/upgrade lock pkg
pkg-2.4.2_1: lock this package? [y/N]: y # 输入 y 按回车键确认锁定 pkg
Locking pkg-2.4.2_1
```

- 下载 pkgbase 转换脚本

```sh
# fetch -o /mnt/upgrade https://raw.githubusercontent.com/FreeBSDFoundation/pkgbasify/main/pkgbasify.lua
```

- 使用 pkgbasify 进行转换

>**警告**
>
>在接受 `Do you accept this risk and wish to continue? (y/n)` 这个风险提示后就没有其他二次确认了！

```sh
# chroot /mnt/upgrade /usr/libexec/flua pkgbasify.lua
Running this tool will irreversibly modify your system to use pkgbase.
This tool and pkgbase are experimental and may result in a broken system.
It is highly recommended to backup your system before proceeding.
Do you accept this risk and wish to continue? (y/n) y # 这里是风险提示，确认
Updating FreeBSD repository catalogue...
Fetching meta.conf: 100%    179 B   0.2kB/s    00:01    
Fetching data.pkg: 100%   11 MiB  11.1MB/s    00:01    
Processing entries: 100%
FreeBSD repository update completed. 36787 packages processed.
Updating FreeBSD-kmods repository catalogue...
Fetching meta.conf: 100%    179 B   0.2kB/s    00:01    
Fetching data.pkg: 100%   33 KiB  33.8kB/s    00:01    
Processing entries: 100%
FreeBSD-kmods repository update completed. 214 packages processed.
Updating FreeBSD-base repository catalogue...
Fetching meta.conf: 100%    179 B   0.2kB/s    00:01    
Fetching data.pkg: 100%   48 KiB  49.1kB/s    00:01    
Processing entries: 100%
FreeBSD-base repository update completed. 525 packages processed.
All repositories are up to date.
Creating /usr/local/etc/pkg/repos/FreeBSD-base.conf
Adding BACKUP_LIBRARIES=yes to /usr/local/etc/pkg.conf
Updating FreeBSD-base repository catalogue...
Fetching meta.conf: 100%    179 B   0.2kB/s    00:01    
Fetching data.pkg: 100%   48 KiB  49.1kB/s    00:01    
Processing entries: 100%
FreeBSD-base repository update completed. 525 packages processed.
FreeBSD-base is up to date.
The following 370 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
        FreeBSD-acct: 14.3p6 [FreeBSD-base]
        FreeBSD-acct-man: 14.3p6 [FreeBSD-base]
        FreeBSD-acpi: 14.3p6 [FreeBSD-base]
        FreeBSD-acpi-man: 14.3p6 [FreeBSD-base]

……此处省略……
```


#### 使用 pkgbase 进行更新


- 把系统转换到 14.3-RELEASE 的 pkgbase

```sh
# pkg -c /mnt/upgrade update -r FreeBSD-base
Updating FreeBSD-base repository catalogue...
Fetching meta.conf: 100%    179 B   0.2kB/s    00:01    
Fetching data.pkg: 100%   48 KiB  49.1kB/s    00:01    
Processing entries: 100%
FreeBSD-base repository update completed. 525 packages processed.
FreeBSD-base is up to date.
```

```sh
# pkg -c /mnt/upgrade upgrade -r FreeBSD-base
```


## 附录：多版本/系统共存的 ZFS 版本问题

可以把一个启动环境升级为 FreeBSD 14，实现 13、14 多版本共存。需要在共存后安装 Port filesystems/openzfs，否则永远无法升级 zfs 池。

### 安装 filesystems/openzfs

- 使用 pkg 安装

```sh
# pkg ins openzfs
```

- 使用 ports 安装：

```sh
# cd /usr/ports/filesystems/openzfs/ 
# make install clean
```

### 编辑 `/boot/loader.conf`

为了让系统不要加载基本系统内的 zfs 版本。需要在 `zfs_load=YES` 前加上注释 `#`，取消其开机自动加载。

形如：

```ini
# zfs_load=YES
```

再新增下列数行：

```ini
zfs_load=NO
openzfs_load=YES
kern.geom.label.disk_ident.enable=0 # 为磁盘禁用 /dev/diskid/*，目的待考察
```

即可。然后检查存储池版本，再行更新其他存储池。

## 参考文献

- [ZFS Boot Environments Explained](https://vermaden.wordpress.com/2025/11/25/zfs-boot-environments-explained/)，指出可以手动安装 openzfs 来达到旧系统使用新 zfs 池的目的
- [wiki/BootEnvironments](https://wiki.freebsd.org/BootEnvironments)，维基
- man [bectl(8)](https://man.freebsd.org/cgi/man.cgi?bectl)
