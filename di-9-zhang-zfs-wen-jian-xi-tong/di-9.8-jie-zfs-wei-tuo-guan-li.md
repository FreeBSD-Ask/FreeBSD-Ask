# 9.8 ZFS 委托管理

## 用户级 ZFS 管理

ZFS 委托管理（ZFS delegation）是一种细粒度的权限控制机制，能让系统管理员将特定的 ZFS 管理权限授予非特权用户，而无需提供完整的 root 访问权限。自 FreeBSD 14.1 起，adduser 会自动为非特权用户的 ZFS 主目录创建独立数据集并支持加密。

该变更（commit 516009ce8d38）使 `adduser(8)` 在用户主目录的父目录为 ZFS 数据集时，自动为用户创建独立 ZFS 数据集，例如 **/home/xxx** 继承自 **/home**。`adduser` 的 `-Z` 参数可禁用此行为，同时现已支持为非特权用户的 ZFS 主目录启用加密。

## 基础用户级 ZFS 管理

首先介绍非特权用户的 ZFS 数据集。在安装系统时，手动创建了两个普通用户 aria2 和 safreya。

列出系统中所有 ZFS 文件系统及其属性：

```sh
% zfs list
NAME                                           USED  AVAIL  REFER  MOUNTPOINT
zroot                                         53.7G   396G    96K  /zroot
zroot/ROOT                                    12.8G   396G    96K  none
zroot/ROOT/14.1-RELEASE-p3_2024-09-17_194642     8K   396G  11.6G  /
zroot/ROOT/default                            12.8G   396G  11.9G  /
zroot/aria2                                    187M   396G   187M  /usr/local/data/aria2
zroot/home                                    7.74G   396G    96K  /home
zroot/home/aria2                               128K   396G   128K  /home/aria2   # 请注意此行
zroot/home/safreya                            7.74G   396G  7.70G  /home/safreya # 请注意此行
zroot/jails                                   3.12G   396G  3.12G  /usr/jails
zroot/sec                                     28.5G   396G  28.5G  /usr/local/data/sec
zroot/tmp                                      102M   396G   102M  /tmp
zroot/usr                                     1.34G   396G    96K  /usr
zroot/usr/ports                               1.34G   396G  1.34G  /usr/ports
zroot/usr/src                                   96K   396G    96K  /usr/src
zroot/var                                     1.58M   396G    96K  /var
zroot/var/audit                                 96K   396G    96K  /var/audit
zroot/var/crash                                 96K   396G    96K  /var/crash
zroot/var/log                                 1.02M   396G  1.02M  /var/log
zroot/var/mail                                 168K   396G   168K  /var/mail
zroot/var/tmp                                  120K   396G   120K  /var/tmp
```

其中：

```sh
zroot/home/aria2                               128K   396G   128K  /home/aria2
zroot/home/safreya                            7.74G   396G  7.70G  /home/safreya
```

即在创建用户时，系统已默认为用户 aria2 和 safreya 分别创建了各自独立的数据集 zroot/home/aria2 和 zroot/home/safreya。

接下来，分别查看两个数据集上的用户权限。

```sh
% zfs allow zroot/home/aria2        # 显示或设置 zroot/home/aria2 文件系统的权限授权
---- Permissions on zroot/home/aria2 ---------------------------------
Local+Descendent permissions:
        user aria2 create,destroy,mount,snapshot
safreya ~ % zfs allow zroot/home/safreya
---- Permissions on zroot/home/safreya -------------------------------
Local+Descendent permissions:
        user safreya create,destroy,mount,snapshot
```

由输出可知，系统在创建用户时，会默认为其数据集授予 create、destroy、mount 和 snapshot 四项权限。

ZFS 委托权限存储在数据集的元数据中。“Local+Descendent permissions”表示该权限设置既适用于当前数据集，也会继承到其子数据集。

因此，对于这两个数据集，普通用户也可使用快照功能：

```sh
% zfs snapshot zroot/home/safreya@snap1   # 为 zroot/home/safreya 文件系统创建名为 snap1 的快照
% zfs list -t snap                        # 列出所有 ZFS 快照
NAME                                       USED  AVAIL  REFER  MOUNTPOINT
zroot/home/safreya@snap1                     0B      -  7.70G  -
```

再来看 `create`、`destroy` 和 `mount` 权限：

```sh
% zfs create zroot/home/safreya/dataset_1        # 在 zroot/home/safreya 下创建一个新的 ZFS 数据集 dataset_1
cannot mount 'zroot/home/safreya/dataset_1': Insufficient privileges
filesystem successfully created, but not mounted
```

以 root 用户执行以下命令，将 `vfs.usermount` 设置为 `1`，以允许非 root 用户挂载文件系统。该 sysctl 属于虚拟文件系统（VFS）子系统，默认值为 0 是出于安全考虑，防止非特权用户挂载不可信的文件系统。

```sh
% su -m root -c 'sysctl vfs.usermount=1'
Password:
vfs.usermount: 0 -> 1
% zfs create zroot/home/safreya/dataset_2        # 在 zroot/home/safreya 下创建一个新的 ZFS 数据集 dataset_2
% zfs list        # 列出所有 ZFS 文件系统及其属性
NAME                                           USED  AVAIL  REFER  MOUNTPOINT

      ...此处省略一部分...

zroot/home                                    7.79G   396G    96K  /home
zroot/home/aria2                               128K   396G   128K  /home/aria2
zroot/home/safreya                            7.79G   396G  7.68G  /home/safreya
zroot/home/safreya/dataset_1                    96K   396G    96K  /home/safreya/dataset_1
zroot/home/safreya/dataset_2                    96K   396G    96K  /home/safreya/dataset_2

      ...此处省略一部分...
```

```sh
% zfs destroy zroot/home/safreya/dataset_1       # 删除 ZFS 数据集 zroot/home/safreya/dataset_1
% zfs destroy zroot/home/safreya/dataset_2        # 删除 ZFS 数据集 zroot/home/safreya/dataset_2
```

由输出可知，创建和销毁权限可以正常使用，而挂载权限需要通过开启内核参数 `vfs.usermount` 来允许用户级挂载。

至此，用户级 ZFS 管理的基本需求已经满足。但仔细观察会发现 `rollback` 权限默认不可用，需要由 root 用户为普通用户授予该权限。

将 zroot/home/safreya 文件系统回滚到 snap1 快照状态：

```sh
% zfs rollback zroot/home/safreya@snap1
cannot rollback 'zroot/home/safreya': permission denied
```

以 root 用户授予 `safreya` 用户对 `zroot/home/safreya` 文件系统执行回滚操作的权限：

```sh
% su -m root -c 'zfs allow safreya rollback zroot/home/safreya'
Password:
% zfs rollback zroot/home/safreya@snap1
```

## 用户级 ZFS 加密功能

在 FreeBSD 14.1 中，若要在用户级使用 ZFS 加密功能，必须为用户授予特定权限。

授权用户 safreya 对 zroot/home/safreya 文件系统执行密钥管理和加密操作：

```sh
% su -m root -c 'zfs allow safreya change-key,load-key,keyformat,keylocation,encryption zroot/home/safreya'
Password: # 此处输入 root 账户密码然后按回车键
```

显示 `zroot/home/safreya` 文件系统的当前权限授权设置：

```sh
% zfs allow zroot/home/safreya
---- Permissions on zroot/home/safreya -------------------------------
Local+Descendent permissions:
        user safreya change-key,create,destroy,encryption,keyformat,keylocation,load-key,mount,snapshot
```

`change-key`、`load-key`、`keyformat`、`keylocation` 和 `encryption` 这五项权限属性用于 ZFS 的加密功能。

创建启用加密的 ZFS 数据集 `zroot/home/safreya/secret`，并将密码用作密钥格式：

```sh
% zfs create -o encryption=on -o keyformat=passphrase zroot/home/safreya/secret
Enter new passphrase:     # 在此处输入密码，密码不会回显
Re-enter new passphrase:  # 在此处重复输入密码，密码不会回显
```

查看加密情况：

```sh
% zfs get mounted zroot/home/safreya/secret        # 查询 zroot/home/safreya/secret 数据集是否已挂载
NAME                       PROPERTY  VALUE    SOURCE
zroot/home/safreya/secret  mounted   yes      -
```

查看 `mounted` 属性，加密数据集创建即挂载，现在创建一个文件，然后卸载加密数据集：

```sh
% cd secret                                      # 进入 secret 数据集目录
% echo "a secret makes a man mad" > abc.txt     # 在 secret 数据集中创建文件 abc.txt 并写入内容
% cd ..                                          # 返回上一级目录
% zfs unmount zroot/home/safreya/secret         # 卸载 secret 数据集
% zfs unload-key zroot/home/safreya/secret      # 卸载 secret 数据集的加密密钥
% zfs get mounted zroot/home/safreya/secret     # 查询 secret 数据集是否已挂载
NAME                       PROPERTY  VALUE    SOURCE
zroot/home/safreya/secret  mounted   no       -
% ls secret # 并无输出

```

卸载加密数据集时必须同时卸载其密钥；挂载数据集时也必须先加载密钥：

```sh
% zfs load-key zroot/home/safreya/secret   # 加载 secret 数据集的加密密钥
Enter passphrase for 'zroot/home/safreya/secret':  # 提示输入密钥密码
% zfs mount zroot/home/safreya/secret      # 挂载 secret 数据集
% ls secret                                 # 列出 secret 数据集中的文件
Permissions Size User    Date Modified Name
.rw-r--r--    25 safreya 19 Sep 20:26  abc.txt
```

> **注意**
>
> 无论数据集是否挂载，`destroy` 子命令都可以成功销毁数据集，因为 `destroy` 权限默认已授予用户。因此如果操作者不是该用户本人，仍可能删除数据集。
>
> 授权是为普通用户授予代理权限，使其在操作授权的数据集时拥有类似 root 的权限，无需输入密码。因此，在授予权限时应合理限制授权范围和权限属性，例如禁用 `destroy` 权限属性等。

撤销用户 safreya 对 zroot/home/safreya 文件系统的销毁权限：

```sh
% su -m root -c 'zfs unallow safreya destroy zroot/home/safreya'
Password:        # 此处输入 root 账户密码然后按回车键
```

显示 `zroot/home/safreya` 文件系统的当前权限授权设置：

```sh
% zfs allow zroot/home/safreya
---- Permissions on zroot/home/safreya -------------------------------
Local+Descendent permissions:
        user safreya change-key,create,encryption,keyformat,keylocation,load-key,mount,rollback,snapshot
```

此处，zroot/home/safreya/secret 受 zroot/home/safreya 上“Local+Descendent”权限的作用范围覆盖。ZFS 委托权限不存在继承机制——权限存储在授予它的数据集上，“Local+Descendent”表示该权限的作用范围同时覆盖本数据集及其子孙数据集。在父数据集上撤销权限时，其 Descendent 范围也会被移除，子孙数据集上的用户将失去相应权限。如果需要对子孙数据集单独控制权限，需要显式地在子孙数据集上进行授权或撤销。

## adduser 与用户主目录加密

adduser 命令中可以直接使用加密的用户主目录数据集，但默认给出的权限不足，一经卸载就无法由普通用户直接挂载。

```sh
# adduser        # 在系统中添加新用户，按照提示输入用户名、密码及其他信息
Username: test
Full name:
Uid (Leave empty for default):
Login group [test]:
Login group is test. Invite test into other groups? []:
Login class [default]:
Shell (sh csh tcsh zsh rzsh git-shell bash rbash nologin) [sh]:
Home directory [/home/test]:
Home directory permissions (Leave empty for default):
Enable ZFS encryption? (yes/no) [no]: yes #该功能为新增功能
Use password-based authentication? [yes]:
Use an empty password? (yes/no) [no]:
Use a random password? (yes/no) [no]:
Enter password:
Enter password again:
Lock out the account after creation? [no]:
Username    : test
Password    : *****
Full Name   :
Uid         : 1003
ZFS dataset : zroot/home/test
Encrypted   : yes
Class       :
Groups      : test
Home        : /home/test
Home Mode   :
Shell       : /bin/sh
Locked      : no
OK? (yes/no) [yes]:
Enter encryption keyphrase for ZFS dataset (zroot/home/test):
Enter new passphrase:
Re-enter new passphrase:
adduser: INFO: Successfully created ZFS dataset (zroot/home/test).
adduser: INFO: Successfully added (test) to the user database.
Add another user? (yes/no) [no]: no
Goodbye!
```

查看 `zroot/home/test` 文件系统的当前权限授权设置：

```sh
# zfs allow zroot/home/test
---- Permissions on zroot/home/test ----------------------------------
Local+Descendent permissions:
        user test create,destroy,mount,snapshot
```

卸载数据集和密钥：

```sh
# zfs unmount zroot/home/test        # 卸载 zroot/home/test 数据集
# zfs unload-key zroot/home/test     # 卸载 zroot/home/test 数据集的加密密钥
```

切换到普通用户 `test` 尝试挂载：

```sh
# su test        # 切换到普通用户 `test`
$ zfs load-key zroot/home/test        # 加载 zroot/home/test 数据集的加密密钥
Enter passphrase for 'zroot/home/test':
Key load error: Permission denied.
```

`Permission denied` 表示权限不足，访问被拒绝。

## 参考文献

- OpenZFS Project. man zfs-allow[EB/OL]. [2026-04-02]. <https://openzfs.github.io/openzfs-docs/man/master/8/zfs-allow.8.html>. OpenZFS 官方 zfs-allow 命令手册。
- FreeBSD Project. zfs-allow -- delegate ZFS administration permissions to unprivileged users[EB/OL]. [2026-04-02]. <https://man.freebsd.org/cgi/man.cgi?zfs-allow>. FreeBSD 官方 zfs-allow 命令手册。
- FreeBSD Project. zfs-create -- create ZFS dataset[EB/OL]. [2026-04-02]. <https://man.freebsd.org/cgi/man.cgi?zfs-create>. FreeBSD 官方 zfs-create 命令手册。
- FreeBSD Project. FreeBSD Handbook, Chapter 21 The Z File System (ZFS)[EB/OL]. [2026-04-24]. <https://docs.freebsd.org/en/books/handbook/zfs/>. FreeBSD 手册中关于 ZFS 的章节。
- FreeBSD Foundation. OpenZFS Encryption Arrives on FreeBSD[EB/OL]. (2020-07)[2026-04-02]. <https://freebsdfoundation.org/wp-content/uploads/2020/07/OpenZFS-Encryption-Arrives-on-FreeBSD.pdf>. 说明 GELI 加密与 ZFS 加密的异同点。
- FreeBSD Project. Merge OpenZFS support in to HEAD[EB/OL]. [2026-04-02]. <https://cgit.freebsd.org/src/commit/?id=9e5787d2284e>. FreeBSD 13.0 转向 OpenZFS 的提交记录。

## 课后习题

1. 在 FreeBSD 14.1 虚拟机中创建 3 个普通用户，分别配置不同的 ZFS 委托权限，测试每个用户能执行的操作范围。
2. 选取 ZFS 委托管理的权限继承机制，编写一个最小脚本实现权限的动态继承刷新功能，分析为什么 ZFS 设计成静态继承而非动态继承。
3. 修改普通用户的 ZFS 委托权限，移除 destroy 权限但保留 create 权限，测试用户的操作能力变化。
