# 第二节 ZFS

## 使用建议

- 建议在 8G 及以上的内存机器上使用 ZFS。
- 最好不要在非 64 位系统上使用 ZFS。
- 为了提高机械硬盘随机读能力，可设置 `vfs.zfs.prefetch_disable=1`。
- 为了避免 ZFS 吃掉太多内存，可设置 `vfs.zfs.arc_max="XXX"`，例如：1024 M。
- 如果要复制某个文件系统，可以用 `zfs send/recv`，这样还能通过 ssh 跨网络传输。
- 推荐使用固态硬盘，使用 SSD 可以改善 ZFS 随机读能力，并且 ZFS 这种写时复制的文件系统也有益于 SSD 寿命。

更多优化见 <https://wiki.freebsd.org/ZFSTuningGuide> 。

## ZFS 快照与还原

ZFS 快照类似于虚拟机快照。

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

快照 `/`（经测试，在上述默认分区下代表快照整个 ZFS 文件系统，`start1` 是随便起的名字）：

```
root@ykla:/ # zfs snapshot zroot/ROOT/default@start1
root@ykla:/ # zfs list -t snapshot
NAME                        USED  AVAIL     REFER  MOUNTPOINT
zroot@start                   0B      -       96K  -
zroot/ROOT/default@start1     0B      -     1004M  -
```


快照还原验证：

```
root@ykla:/ # rm 1.txt
root@ykla:/ # ls
.cshrc		boot		home		mnt		root		usr
.profile	dev		lib		net		sbin		var
COPYRIGHT	entropy		libexec		proc		sys		zroot
bin		etc		media		rescue		tmp
root@ykla:/ # zfs rollback -r zroot/ROOT/default@start1
root@ykla:/ # ls
.cshrc		bin		etc		media		rescue		tmp
.profile	boot		home		mnt		root		usr
1.txt		dev		lib		net		sbin		var
COPYRIGHT	entropy		libexec		proc		sys		zroot
```

销毁快照：

```
root@ykla:/ # zfs destroy zroot@start 
root@ykla:/ # zfs list -t snap
NAME                        USED  AVAIL     REFER  MOUNTPOINT
zroot/ROOT/default@start1     8K      -     1004M  -
root@ykla:/ # 
```

## 注意事项

- ZFS 并不使用`/etc/fstab`
