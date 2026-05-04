# 9.2 ZFS 快照与还原

ZFS 快照采用写时复制（Copy-on-Write, CoW）机制，创建过程瞬时完成且不占用额外磁盘空间。快照创建后，当原文件系统中的数据块被修改时，ZFS 将新数据写入新位置，旧数据块原地保留，快照继续指向旧数据块，从而捕获文件系统在快照创建时刻的时间点状态。与虚拟机快照相比，ZFS 快照在文件系统层面实现，具有更轻量、更高效的特性，是数据备份、版本控制与灾难恢复的核心技术手段。

FreeBSD 中文社区（CFC）提供了 ZFS 脚本，可用于查看、创建、删除和恢复 ZFS 快照（ZFS snapshot）。[ZFS 脚本项目地址](https://github.com/FreeBSD-Ask/zfs-snap)。该脚本已部署至 [https://docs.bsdcn.org/zfs.sh](https://docs.bsdcn.org/zfs.sh)，可在 FreeBSD 系统上直接使用 `fetch` 命令下载。

## 创建快照

默认情况下，使用 Auto ZFS 布局创建的分区结构如下：

```sh
# zfs list  # 列出所有 ZFS 文件系统及其属性
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

```sh
zroot/
├── ROOT/
│   └── default/
├── tmp/
├── usr/
│   ├── home/
│   ├── ports/
│   └── src/
└── var/
    ├── audit/
    ├── crash/
    ├── log/
    ├── mail/
    └── tmp/
```

创建名为 test 的 zroot 快照，使用 `-r` 参数可递归创建快照：

```sh
# zfs snapshot -r zroot@test   # 为 zroot 池及其所有子文件系统递归创建名为 test 的快照
# zfs list -t snap              # 列出所有 ZFS 快照
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
```

> **技巧**
>
> 在命令中，`snapshot` 可以缩写为 `snap`，其他命令也有对应的缩写形式，可自行查阅文档研究使用。

经测试，在上述默认分区布局下，该操作会快照整个 ZFS 文件系统。

## 还原快照

> **警告**
>
> 请勿在生产环境中进行此类测试。

## 文件变动测试

可以通过增删文件来验证快照的有效性。在测试环境中，如果事先创建了快照，即使执行 `rm -rf /*` 命令也可以顺利恢复；若系统使用 UEFI，则需要根据其他章节的说明自行恢复 EFI 引导。注意，此操作仅应在测试环境中进行。

## 快照还原测试

> **思考题**
>
> 探索更优的快照回滚方案；已知网络上存在相关脚本，可考虑将其作为功能请求或提交 Pull Request（PR）至 OpenZFS 项目。或者使用中文社区的 [ZFS 脚本项目](https://github.com/FreeBSD-Ask/zfs-snap)。

与虚拟机快照不同，在默认状态下，`zfs rollback` 命令只能回滚到最新快照（[参考手册](https://docs.oracle.com/cd/E19253-01/819-7065/gbcxk/index.html)，Oracle 官方 ZFS 回滚命令文档）；使用 `-r` 参数可以销毁比目标快照更新的所有快照，从而允许回滚到非最新的快照。ZFS 不支持一次性递归回滚所有子数据集，需要对每个子文件系统单独执行回滚操作。

```sh
# zfs rollback -r zroot@test             # 回滚 zroot 到 test 快照并销毁更新的快照
# zfs rollback -r zroot/ROOT@test        # 回滚 zroot/ROOT 到 test 快照并销毁更新的快照
# zfs rollback -r zroot/ROOT/default@test # 回滚 zroot/ROOT/default 到 test 快照并销毁更新的快照
# zfs rollback -r zroot/tmp@test         # 回滚 zroot/tmp 到 test 快照并销毁更新的快照
# zfs rollback -r zroot/usr@test         # 回滚 zroot/usr 到 test 快照并销毁更新的快照
# zfs rollback -r zroot/usr/home@test    # 回滚 zroot/usr/home 到 test 快照并销毁更新的快照
# zfs rollback -r zroot/usr/ports@test   # 回滚 zroot/usr/ports 到 test 快照并销毁更新的快照
# zfs rollback -r zroot/var@test         # 回滚 zroot/var 到 test 快照并销毁更新的快照
# zfs rollback -r zroot/var/log@test     # 回滚 zroot/var/log 到 test 快照并销毁更新的快照
```

## 销毁快照

销毁快照时，可以使用 `-r` 参数递归删除：

```sh
# zfs destroy -r zroot@test   # 递归删除 zroot 池及其子文件系统的 test 快照
# zfs list -t snap             # 列出所有 ZFS 快照
no datasets available
```

## 参考文献

- FreeBSD Project. zfs -- configures ZFS datasets[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?zfs(8)>. ZFS 数据集管理工具手册页，涵盖快照、克隆与回滚操作。
- FreeBSD Project. zpool -- configures ZFS storage pools[EB/OL]. [2026-04-14]. <https://man.freebsd.org/cgi/man.cgi?zpool(8)>. ZFS 存储池管理工具手册页。
- FreeBSD Project. FreeBSD Handbook, Chapter 21: The Z File System (ZFS)[EB/OL]. [2026-04-14]. <https://docs.freebsd.org/en/books/handbook/zfs/>. FreeBSD 手册中关于 ZFS 的完整配置与管理指南。
- OpenZFS Project. zfs-rollback(8)[EB/OL]. [2026-04-18]. <https://openzfs.github.io/openzfs-docs/man/master/8/zfs-rollback.8.html>. 详细说明了 -r 参数用于销毁更新的快照，而非递归回滚子数据集。

## 课后习题

1. 查找 FreeBSD 中文社区的 ZFS 脚本项目，在 FreeBSD 虚拟机中部署并测试其快照管理功能，对比手动操作与脚本操作在效率上的差异。
2. 选取 ZFS 快照与回滚的核心机制，编写一个最小化脚本实现递归回滚所有子文件系统的功能，分析为什么 ZFS 默认不支持一次性递归回滚，尝试回溯上游。
3. 修改 ZFS 快照策略，禁用自动快照功能并手动创建一个快照，通过修改测试文件后恢复，验证其恢复能力。
