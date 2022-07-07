# 第二节 ZFS

## 使用建议

- 建议在 8G 及以上的内存机器上使用 ZFS。
- 为了提高机械硬盘随机读能力，可设置 `vfs.zfs.prefetch_disable=1`。
- 为了避免 ZFS 吃掉太多内存，可设置 `vfs.zfs.arc_max="XXX"`，例如：1024 M。
- 如果要复制某个文件系统，可以用 `zfs send/recv`，这样还能通过 ssh 跨网络传输。
- 推荐使用固态硬盘，使用 SSD 可以改善 ZFS 随机读能力，并且 ZFS 这种写时复制的文件系统也有益于 SSD 寿命。

更多优化见 <https://wiki.freebsd.org/ZFSTuningGuide> 。

## ZFS 快照与还原


ZFS 快照类似于虚拟机快照。

- 创建快照

默认创建分区（Auto ZFS）如下：

```
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

```
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

与虚拟机快照有所不同，在缺省情况下，`zfs rollback` 命令无法回滚到除最新快照以外的快照（[参考手册](https://docs.oracle.com/cd/E19253-01/819-7065/gbcxk/index.html)），除非使用`r`，但这会删除该快照创建后的所有快照。

```
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


销毁快照（销毁的时候可以使用`r`递归销毁）：

```
root@ykla:/home/ykla # zfs destroy -r zroot@test
root@ykla:/home/ykla # zfs list -t snap
no datasets available
root@ykla:/home/ykla # 
```

>`snapshot`在命令中可以缩写为`snap`。

## 注意事项

- ZFS 并不使用 `/etc/fstab`，但是 EFI、Swap 仍然使用。
