# 第 6.2 节 ZFS

## 使用建议

- 建议在 8G 及以上的内存机器上使用 ZFS（但是这并不意味着 512 M 内存就绝对无法使用）。
- 为了提高机械硬盘随机读能力，可设置 `vfs.zfs.prefetch_disable=1`。
- 为了避免 ZFS 吃掉太多内存，可设置 `vfs.zfs.arc_max="XXX"`，例如：1024 M。
- 如果要复制某个文件系统，可以用 `zfs send/recv`，亦支持通过 ssh 跨网络传输。


以上部分来自网络，更多优化见 [ZFSTuningGuide](https://wiki.freebsd.org/ZFSTuningGuide)。

## ZFS 快照与还原

ZFS 快照类似于虚拟机快照。

- 创建快照

默认创建分区（Auto ZFS）如下：

```sh
root@ykla:/home/ykla #  zfs list
NAME                 USED  AVAIL     REFER  MOUNTPOINT
zroot               1.72G   440G       96K  /zroot
zroot/ROOT          1004M   440G       96K  none
zroot/ROOT/default  1004M   440G     1004M  /
zroot/tmp            104K   440G      104K  /tmp
zroot/usr            760M   440G       96K  /usr
zroot/usr/home       128K   440G      128K  /usr/home
zroot/usr/ports       96K   440G       96K  /usr/ports
zroot/usr/src        759M   440G      759M  /usr/src
zroot/var            628K   440G       96K  /var
zroot/var/audit       96K   440G       96K  /var/audit
zroot/var/crash       96K   440G       96K  /var/crash
zroot/var/log        148K   440G      148K  /var/log
zroot/var/mail        96K   440G       96K  /var/mail
zroot/var/tmp         96K   440G       96K  /var/tmp
```

快照 `zroot`（经测试，在上述默认分区下代表快照整个 ZFS 文件系统，`-r` 即递归创建快照，`test` 是随便起的名字）：

```sh
root@ykla:/home/ykla # zfs snapshot -r zroot@test
root@ykla:/home/ykla # zfs list -t snap
NAME                      USED  AVAIL     REFER  MOUNTPOINT
zroot@test                  0B      -       96K  -
zroot/ROOT@test             0B      -       96K  -
zroot/ROOT/default@test     0B      -     7.18G  -
zroot/tmp@test              0B      -      176K  -
zroot/usr@test              0B      -       96K  -
zroot/usr/home@test         0B      -     31.1M  -
zroot/usr/ports@test        0B      -     1.98G  -
zroot/var@test              0B      -       96K  -
zroot/var/log@test          0B      -      444K  -
root@ykla:/home/ykla # ls /usr/ports/
CHANGES          archivers/       emulators/       misc/            textproc/
CONTRIBUTING.md  astro/           finance/         multimedia/      ukrainian/
COPYRIGHT        audio/           french/          net-im/          vietnamese/
GIDs             base/            ftp/             net-mgmt/        www/
INDEX-13         benchmarks/      games/           net-p2p/         x11-clocks/
Keywords/        biology/         german/          net/             x11-drivers/
MOVED            cad/             graphics/        news/            x11-fm/
Makefile         chinese/         hebrew/          polish/          x11-fonts/
Mk/              comms/           hungarian/       ports-mgmt/      x11-servers/
README           converters/      irc/             portuguese/      x11-themes/
Templates/       databases/       japanese/        print/           x11-toolkits/
Tools/           deskutils/       java/            russian/         x11-wm/
UIDs             devel/           korean/          science/         x11/
UPDATING         distfiles/       lang/            security/
accessibility/   dns/             mail/            shells/
arabic/          editors/         math/            sysutils/
root@ykla:/home/ykla # rm /usr/ports/
```

- 还原快照

还原时不能递归还原快照，必须挨个还原（如果你有更好的方案请告诉我们,网络上有一些脚本可用）：

与虚拟机快照有所不同，在缺省情况下，`zfs rollback` 命令无法回滚到除最新快照以外的快照（[参考手册](https://docs.oracle.com/cd/E19253-01/819-7065/gbcxk/index.html)），除非使用 `r`，但这会删除该快照创建后的所有快照。

```sh
root@ykla:/home/ykla # zfs rollback -r zroot@test
root@ykla:/home/ykla # zfs rollback -r zroot/ROOT@test
root@ykla:/home/ykla # zfs rollback -r zroot/ROOT/default@test
root@ykla:/home/ykla # zfs rollback -r zroot/tmp@test
root@ykla:/home/ykla # zfs rollback -r zroot/usr@test
root@ykla:/home/ykla # zfs rollback -r zroot/usr/home@test
root@ykla:/home/ykla # zfs rollback -r zroot/usr/ports@test
root@ykla:/home/ykla # zfs rollback -r zroot/var@test
root@ykla:/home/ykla # zfs rollback -r zroot/var/log@test
```

- 销毁快照

销毁快照（销毁的时候可以使用 `r` 递归销毁）：

```sh
root@ykla:/home/ykla # zfs destroy -r zroot@test
root@ykla:/home/ykla # zfs list -t snap
no datasets available
root@ykla:/home/ykla #
```

> `snapshot`在命令中可以缩写为`snap`。


## 启动环境

什么是启动环境？用 snapshot 和 rollback 结合，相当于在一条时间上线进行跳转。启动环境相当于一条时间线，复制一个启动环境相当于再造一条时间线(复制之后两个启动环境互相独立)，两个启动环境间的切换是两条时间线的穿越（或者说平行空间的穿越）。默认安装中 `zroot/ROOT/default` 是默认的启动环境。

```sh
# zfs snap zroot/ROOT/default@new                         # 建一个 zfs 快照
# zfs clone zroot/ROOT/default@new zroot/ROOT/new         # 用刚建的快照复制一个镜像
```

复制的镜像可以作为一个启动环境，可以用工具 `bectl` 查看可用的启动环境

```sh
# bectl list
BE                                Active Mountpoint Space Created
0915                              -      -          4.00M 2023-09-19 19:44
13.2-RELEASE-p2_2023-09-13_141111 -      -          29.0M 2023-09-13 14:11
new                               -      -          432K  2023-09-20 15:17
default                           NR     /          40.8G 2023-04-10 10:06
```

其中 Active 这一列中 `N` 表示当前使用环境，`R` 表示下次启动时使用的环境。`bectl` 工具可以改变下次使用的启动环境（在启动 FreeBSD 时，启动菜单里选 `8`，也可以改变启动环境）

```sh
bectl activate new
Successfully activated boot environment new
```

再次用 `bectl list` 查看，观察 Active 列的变化

```sh
bectl list
BE                                Active Mountpoint Space Created
0915                              -      -          4.00M 2023-09-19 19:44
13.2-RELEASE-p2_2023-09-13_141111 -      -          29.0M 2023-09-13 14:11
new                               R      /          2.84M 2023-09-20 15:17
default                           N      -          40.8G 2023-04-10 10:06
```

重启 FreeBSD （启动菜单里选择 `new` 启动环境，或如上用 `bectl activate new` 切换到 new 启动环境），用 `df` 观察，挂载的根目录的文件系统已经是 `zroot/ROOT/new`

```sh
# df
Filesystem          1K-blocks     Used     Avail Capacity  Mounted on
zroot/ROOT/new      110611616 42612156  67999460    39%    /
devfs                       1        1         0   100%    /dev
/dev/gpt/efiboot0      266176     1872    264304     1%    /boot/efi
fdescfs                     1        1         0   100%    /dev/fd
```

切换回 `zroot/ROOT/default` 启动环境，在启动菜单里选择 default 启动环境，或如上用 `bectl activate default` 切换到 default 启动环境

用法扩展：可以把一个启动环境升级为 FreeBSD 14，实现 13、14 多版本共存

>**警告**
>
>用法扩展实现的代价是 zfs 不能升级，一升级就挂了，因为旧版 ZFS 程序无法向后兼容。实践的意义不大，可以仅做备份还原使用。

参考文献：

- [wiki/BootEnvironments](https://wiki.freebsd.org/BootEnvironments)

## FreeBSD on zfs 的 zpool 升级

13.2 升级 14.0 ，zpool 版本有升级。

此处假定已经用 `freebsd-update` 从 13.2 升级到 14.0。

开始前的提醒：准备好 livecd 以应对意外，livecd 要 14.0 及以上的，13.2 不支持（不能访问） 14.0 的 zfs

查看 zpool 状态：

```sh
root@u13t14 # zpool status

  pool: zroot
 state: ONLINE
status: Some supported and requested features are not enabled on the pool.
The pool can still be used, but some features are unavailable.
action: Enable all features using 'zpool upgrade'. Once this is done,
the pool may no longer be accessible by software that does not support
the features. See zpool-features(7) for details.
config:

NAME        STATE     READ WRITE CKSUM
zroot       ONLINE       0     0     0
  ada0p3    ONLINE       0     0     0

errors: No known data errors
```

未升级前不能使用所有 zfs 新功能，下面进行升级：

```sh
root@u13t14 # zpool upgrade zroot

This system supports ZFS pool feature flags.

Enabled the following features on 'zroot':
  edonr
  zilsaxattr
  head_errlog
  blake3
  block_cloning
  vdev_zaps_v2

Pool 'zroot' has the bootfs property set, you might need to update
the boot code. See gptzfsboot(8) and loader.efi(8) for details.
```

### 重写引导（仅非 EFI 引导需要）

>**警告**
>
>`bootfs` 属性是在 zfs 上引导 FreeBSD 的重要标志，不理睬这个提示可能没事，但出了问题就不能引导系统，建议按提示重写 `boot code` (为什么这么建议？~~因为我炸了~~)。如果你没有 **freebsd-boot** 分区就 **不需要** 以下操作。

查看分区信息：

```sh
root@u13t14 # gpart show

=>      40  33554352  ada0  GPT  (16G)
        40      1024     1  freebsd-boot  (512K)
      1064       984        - free -  (492K)
      2048   4194304     2  freebsd-swap  (2.0G)
   4196352  29356032     3  freebsd-zfs  (14G)
  33552384      2008        - free -  (1.0M)
```

找到 `freebsd-boot` 类型分区，这里序号为 `1`，对应下面命令中 `-i` 选项，接着重写 `bootcode`：

```sh
root@u13t14 # gpart bootcode -p /boot/gptzfsboot -i 1 ada0
partcode written to ada0p1
```

可再次查看 `zpool` 状态：

```sh
root@u13t14 # zpool status

  pool: zroot
 state: ONLINE
config:

NAME        STATE     READ WRITE CKSUM
zroot       ONLINE       0     0     0
  ada0p3    ONLINE       0     0     0

errors: No known data errors
```

## 用户级 zfs 管理

zfs 允许非特权用户管理。

自 FreeBSD 14.1 以降（请参阅发行说明），`bsdinstall(8)` 使用的工具 `adduser(8)`：当用户主目录的父目录位于 zfs 数据集上时（即 `/home` 是 zfs 数据集，`/home/xxx` 亦如此），会为用户的主目录创建一个 zfs 数据集。`adduser`  的参数 `-Z` 可禁用这一行为。zfs 加密功能亦已可用。

以下操作基于 `FreeBSD 14.1-RELEASE`。

### 基础的用户级 zfs 管理

先了解一下非特权用户的 zfs 数据集。

我们首先在安装系统时，创建了两个普通用户“aria2”和“safreya”。

```sh
safreya ~ % zfs list
NAME                                           USED  AVAIL  REFER  MOUNTPOINT
zroot                                         53.7G   396G    96K  /zroot
zroot/ROOT                                    12.8G   396G    96K  none
zroot/ROOT/14.1-RELEASE-p3_2024-09-17_194642     8K   396G  11.6G  /
zroot/ROOT/default                            12.8G   396G  11.9G  /
zroot/aria2                                    187M   396G   187M  /usr/local/data/aria2
zroot/home                                    7.74G   396G    96K  /home
zroot/home/aria2                               128K   396G   128K  /home/aria2   #请注意此行
zroot/home/safreya                            7.74G   396G  7.70G  /home/safreya #请注意此行
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
safreya ~ %
```

其中

```sh
zroot/home/aria2                               128K   396G   128K  /home/aria2
zroot/home/safreya                            7.74G   396G  7.70G  /home/safreya
```

即，在创建用户时，已默认为用户 `safreya` 、`aria2` 分别创建了各自独立的数据集 `zroot/home/aria2` 和 `zroot/home/safreya`。

接下来，查看一下两个数据集上的用户权限。

```sh
safreya ~ % zfs allow zroot/home/aria2
---- Permissions on zroot/home/aria2 ---------------------------------
Local+Descendent permissions:
        user aria2 create,destroy,mount,snapshot
safreya ~ % zfs allow zroot/home/safreya
---- Permissions on zroot/home/safreya -------------------------------
Local+Descendent permissions:
        user safreya create,destroy,mount,snapshot
safreya ~ %
```

可以看到，在创建用户集时，默认为用户创设了 `create`、`destroy`、`mount` 和 `snapshot` 四项权限。

所以，对于这两个数据集，普通用户亦可使用快照功能：

```sh
safreya ~ % zfs snap zroot/home/safreya@snap1
safreya ~ % zfs list -t snap
NAME                                       USED  AVAIL  REFER  MOUNTPOINT
zroot/home/safreya@snap1                     0B      -  7.70G  -
```

再来看 `create`, `destroy`, `mount` 权限：

```sh
safreya ~ % zfs create zroot/home/safreya/dataset_1
cannot mount 'zroot/home/safreya/dataset_1': Insufficient privileges
filesystem successfully created, but not mounted
```

```sh
safreya ~ % su -m root -c 'sysctl vfs.usermount=1'
Password:
vfs.usermount: 0 -> 1
safreya ~ % zfs create zroot/home/safreya/dataset_2
safreya ~ % zfs list
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
safreya ~ % zfs destroy zroot/home/safreya/dataset_1
safreya ~ % zfs destroy zroot/home/safreya/dataset_2      
```

可以看到，创建（create）权限、销毁（destroy）可以正常使用，但是挂载（mount）权限需要开启内核参数 `vfs.usermount`，以允许用户级挂载。

到这里，用户级的 zfs 管理需求已经基本满足。但是你够仔细的话会发现 `rollback` 权限并不可用，可以用 root 用户授权普通用户 rollback 权限。即：

```sh
safreya ~ % zfs rollback zroot/home/safreya@snap1
cannot rollback 'zroot/home/safreya': permission denied
safreya ~ % su -m root -c 'zfs allow safreya rollback zroot/home/safreya'
Password:
safreya ~ % zfs rollback zroot/home/safreya@snap1
```

### 用户级 zfs 加密功能

FreeBSD 14.1 中 zfs 已经支持加密功能。在用户级使用中需要为用户授于特定权限。

```sh
safreya ~ % su -m root -c 'zfs allow safreya change-key,load-key,keyformat,keylocation,encryption zroot/home/safreya'
Password:
safreya ~ % zfs allow zroot/home/safreya
---- Permissions on zroot/home/safreya -------------------------------
Local+Descendent permissions:
        user safreya change-key,create,destroy,encryption,keyformat,keylocation,load-key,mount,snapshot
safreya ~ %
```

`change-key`、`load-key`、`keyformat`、`keylocation` 和 `encryption` 这五个权限属性都用于 zfs 加密功能。

现在创建一个加密数据集 `zroot/home/safreya/secret`：

```sh
safreya ~ % zfs create -o encryption=on -o keyformat=passphrase zroot/home/safreya/secret
Enter new passphrase:     #此处输入密码，密码不会回显，就是什么也没有
Re-enter new passphrase:  #此处重复输入上述密码，密码不会回显，就是什么也没有
```

查看加密情况：

```sh
safreya ~ % zfs get mounted zroot/home/safreya/secret
NAME                       PROPERTY  VALUE    SOURCE
zroot/home/safreya/secret  mounted   yes      -
```

查看 `mounted` 属性，加密数据集创建即挂载，现在创建一个文件，然后卸载加密数据集：

```sh
safreya ~ % cd secret
safreya secret % echo "a secret makes a man mad" >abc.txt
safreya secret % cd ..
safreya ~ % zfs unmount zroot/home/safreya/secret
safreya ~ % zfs unload-key zroot/home/safreya/secret
safreya ~ % zfs get mounted zroot/home/safreya/secret
NAME                       PROPERTY  VALUE    SOURCE
zroot/home/safreya/secret  mounted   no       -
safreya ~ % ls secret #并无输出
safreya ~ %
```

卸载加密数据集必须记得也要同时卸载密钥。挂载加密数据集亦要先加载密钥：

```sh
safreya ~ % zfs load-key zroot/home/safreya/secret
Enter passphrase for 'zroot/home/safreya/secret':
safreya ~ % zfs mount zroot/home/safreya/secret
safreya ~ % ls secret
Permissions Size User    Date Modified Name
.rw-r--r--    25 safreya 19 Sep 20:26  abc.txt
```

注意： 子命令 `destroy` 不管数据集是否挂载，都可以成功销毁数据集，因为 `destroy` 权限是默认就授予的，所以如果非用户本人操作系统的话，可能出现“我得不到的，就毁灭”的情况。而且要记住的是，“授权”是授于普通用户“代理权限”，操作有授权的数据集时相当于 root，过程不需要密码。因此在授于权限时还要综合考虑，合理的限制授权范围和权限属性，如禁用 `destroy` 权限属性等。

```sh
safreya ~ % su -m root -c 'zfs unallow safreya destroy zroot/home/safreya'
Password:
safreya ~ % zfs allow  zroot/home/safreya
---- Permissions on zroot/home/safreya -------------------------------
Local+Descendent permissions:
        user safreya change-key,create,encryption,keyformat,keylocation,load-key,mount,rollback,snapshot
```

这里 `zroot/home/safreya/secret` 会继承 `zroot/home/safreya` 数据集的权限属性，授权反授权都针对 `zroot/home/safreya`，对 `zroot/home/safreya/secret` 操作不起作用。

  
## 注意事项

- ZFS 并不使用 `/etc/fstab`，但是 EFI、Swap 仍然使用。
