# 第 6.3 节 磁盘扩容



>**警告**
>
>ZFS 和 UFS 都只能扩大不能缩小！

## ZFS 磁盘扩容


```sh
root@ykla:~ # gpart show
=>       40  167772087  nda0  GPT  (80G)
         40     532480     1  efi  (260M)
     532520       1024     2  freebsd-boot  (512K)
     533544        984        - free -  (492K)
     534528    4194304     3  freebsd-swap  (2.0G)
    4728832  142071775     4  freebsd-zfs  (68G)
  146800607   20971520        - free -  (10G)
```

可以看到，`free` 空闲空间是 10GB。

```sh
root@ykla:~ # gpart resize -i 4 nda0
nda0p4 resized
```

再看下：

```sh
root@ykla:~ # gpart show
=>       40  167772087  nda0  GPT  (80G)
         40     532480     1  efi  (260M)
     532520       1024     2  freebsd-boot  (512K)
     533544        984        - free -  (492K)
     534528    4194304     3  freebsd-swap  (2.0G)
    4728832  163043295     4  freebsd-zfs  (78G)
```

```sh
root@ykla:~ # zpool list
NAME    SIZE  ALLOC   FREE  CKPOINT  EXPANDSZ   FRAG    CAP  DEDUP    HEALTH  ALTROOT
zroot  67.5G  2.20G  65.3G        -         -     2%     3%  1.00x    ONLINE  - # 这里看到还是 67.5G 没有扩容
root@ykla:~ # zpool status
  pool: zroot
 state: ONLINE
status: Some supported and requested features are not enabled on the pool.
	The pool can still be used, but some features are unavailable.
action: Enable all features using 'zpool upgrade'. Once this is done,
	the pool may no longer be accessible by software that does not support
	the features. See zpool-features(7) for details.
config:

	NAME        STATE     READ WRITE CKSUM
	zroot       ONLINE       0     0     0 # 可以看到池名是默认的 zroot
	  nda0p4    ONLINE       0     0     0 # 这里看到是 nda0p4

errors: No known data errors
```

扩展 zfs 池：

```sh
root@ykla:~ #  zpool online -e zroot nda0p4
```

查看扩容后：

```sh
root@ykla:~ # zpool list
NAME    SIZE  ALLOC   FREE  CKPOINT  EXPANDSZ   FRAG    CAP  DEDUP    HEALTH  ALTROOT
zroot  77.5G  2.20G  75.3G        -         -     2%     2%  1.00x    ONLINE  -
```

### 参考文献

- [Solved-extend ZFS partition](https://forums.freebsd.org/threads/extend-zfs-partition.55964/)

## UFS 磁盘扩容


- `gpart show`

```sh
root@freebsd:~ # gpart show
=>       3  41943035  da0  GPT  (20G)
         3       122    1  freebsd-boot  (61K)
       125     66584    2  efi  (33M)
     66709   2097152    3  freebsd-swap  (1.0G)
   2163861  10486633    4  freebsd-ufs  (5.0G)
  12650494  29292544       - free -  (14G)
```

查看系统盘大小只有 5G，显示 `da0` 只有这一个盘。

- 执行扩容命令，`da0` 可从 `gpart show` 执行后查看到具体名称

> **警告** 如果你使用的是 GPT 分区表，上边的扩容操作（**在虚拟机或云服务器上的**）会破坏 GPT 分区表，所以需要先恢复之：
>
> ```sh
> # gpart recover da0
> ```
>
> 执行后下面步骤相同。

`i` 为要扩容的分区，这里扩容 / 分区 `freebsd-ufs`。

```sh
root@freebsd:~ #  gpart resize -i 4 da0
da0p4 resized
```

- 启动 `growfs` 服务，自动完成扩展

```sh
root@freebsd:~ # service growfs onestart
Growing root partition to fill device
da0 recovering is not needed
da0p4 resized
growfs: no room to allocate last cylinder group; leaving 7.7MB unused
super-block backups (for fsck_ffs -b #) at:
 11544384, 12827072, 14109760, 15392448, 16675136, 17957824, 19240512, 20523200, 21805888, 23088576, 24371264,
 25653952, 26936640, 28219328, 29502016, 30784704, 32067392, 33350080, 34632768, 35915456, 37198144, 38480832
```

- 用 `df -h` 命令查看结果。

```sh
root@freebsd:~ # df -hl
Filesystem         Size    Used   Avail Capacity  Mounted on
/dev/gpt/rootfs     18G    4.8G     12G    29%    /
devfs              1.0K      0B    1.0K     0%    /dev
/dev/gpt/efiesp     32M    651K     31M     2%    /boot/efi
tmpfs               20M    4.0K     20M     0%    /tmp
tmpfs               32M    156K     32M     0%    /var
```

