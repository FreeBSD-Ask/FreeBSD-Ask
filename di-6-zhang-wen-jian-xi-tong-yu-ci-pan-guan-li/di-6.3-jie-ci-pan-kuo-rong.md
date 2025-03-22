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

选择第四分区进行扩容：

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

已经扩展完成。

### 参考文献

- [Solved-extend ZFS partition](https://forums.freebsd.org/threads/extend-zfs-partition.55964/)

## UFS 磁盘扩容



- `gpart show` 查看磁盘分区

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

- 执行扩容命令





> **警告** 
>
>如果你使用的是 GPT 分区表，上边的扩容操作（**在虚拟机或云服务器上的**）会破坏 GPT 分区表，所以需要先恢复之：
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

分区扩展完成。

## 附录

**技巧：** 分区编号可从 `gpart show` 执行后查看到具体名称，或使用参数 `-p`：

```sh
root@ykla:~ # gpart show -p
=>       40  244277168    mmcsd0  GPT  (116G)
         40     532480  mmcsd0p1  efi  (260M)
     532520       2008            - free -  (1.0M)
     534528  243740672  mmcsd0p2  freebsd-zfs  (116G)
  244275200       2008            - free -  (1.0M)

=>       34  976773101    nda0  GPT  (466G)
         34          6          - free -  (3.0K)
         40     567256  nda0p1  efi  (277M)
     567296  419436064  nda0p2  ms-basic-data  (200G)
  420003360  310592132  nda0p3  ms-basic-data  (148G)
  730595492          4          - free -  (2.0K)
  730595496  177626968  nda0p4  ms-basic-data  (85G)
  908222464   67100672  nda0p5  freebsd-swap  (32G)
  975323136    1445937  nda0p6  ms-recovery  (706M)
  976769073       4062          - free -  (2.0M)
```

- 打印分区类型 GUID
（如果是 GPT）或原始分区类型（MBR）

```sh
root@ykla:~ # gpart show -rp
=>       40  244277168    mmcsd0  GPT  (116G)
         40     532480  mmcsd0p1  c12a7328-f81f-11d2-ba4b-00a0c93ec93b  (260M)
     532520       2008            - free -  (1.0M)
     534528  243740672  mmcsd0p2  516e7cba-6ecf-11d6-8ff8-00022d09712b  (116G)
  244275200       2008            - free -  (1.0M)

=>       34  976773101    nda0  GPT  (466G)
         34          6          - free -  (3.0K)
         40     567256  nda0p1  c12a7328-f81f-11d2-ba4b-00a0c93ec93b  (277M)
     567296  419436064  nda0p2  ebd0a0a2-b9e5-4433-87c0-68b6b72699c7  (200G)
  420003360  310592132  nda0p3  ebd0a0a2-b9e5-4433-87c0-68b6b72699c7  (148G)
  730595492          4          - free -  (2.0K)
  730595496  177626968  nda0p4  ebd0a0a2-b9e5-4433-87c0-68b6b72699c7  (85G)
  908222464   67100672  nda0p5  516e7cb5-6ecf-11d6-8ff8-00022d09712b  (32G)
  975323136    1445937  nda0p6  de94bba4-06d1-4d40-a16a-bfd50179d6ac  (706M)
  976769073       4062          - free -  (2.0M)
```

- 查看详情：

```sh
root@ykla:~ # gpart list mmcsd0
Geom name: mmcsd0
modified: false
state: OK
fwheads: 255
fwsectors: 63
last: 244277207
first: 40
entries: 128
scheme: GPT
Providers:
1. Name: mmcsd0p1
   Mediasize: 272629760 (260M)
   Sectorsize: 512
   Stripesize: 512
   Stripeoffset: 0
   Mode: r1w1e2
   efimedia: HD(1,GPT,ea7e17b0-f265-11ef-a633-1002b5860ef9,0x28,0x82000)
   rawuuid: ea7e17b0-f265-11ef-a633-1002b5860ef9 # 这个是 fstab 中可用的 UUID，是唯一的，下同
   rawtype: c12a7328-f81f-11d2-ba4b-00a0c93ec93b # 这个是分区类型 GUID，相同类型的文件系统其 ID 也是一样的，下同
   label: efiboot0
   length: 272629760
   offset: 20480
   type: efi
   index: 1
   end: 532519
   start: 40
2. Name: mmcsd0p2
   Mediasize: 124795224064 (116G)
   Sectorsize: 512
   Stripesize: 512
   Stripeoffset: 0
   Mode: r1w1e1
   efimedia: HD(2,GPT,ea843e57-f265-11ef-a633-1002b5860ef9,0x82800,0xe873000)
   rawuuid: ea843e57-f265-11ef-a633-1002b5860ef9
   rawtype: 516e7cba-6ecf-11d6-8ff8-00022d09712b
   label: zfs0
   length: 124795224064
   offset: 273678336
   type: freebsd-zfs
   index: 2
   end: 244275199
   start: 534528
Consumers:
1. Name: mmcsd0
   Mediasize: 125069950976 (116G)
   Sectorsize: 512
   Stripesize: 512
   Stripeoffset: 0
   Mode: r2w2e5
```

### 参考文献

- [GPT 分区详解](https://www.jinbuguo.com/storage/gpt.html)，GPT 基础知识
- [如何轻松改变分区类型 ID？试试这2种方法！](https://www.disktool.cn/content-center/change-partition-type-id-2111.html)，分不清分区类型 ID 和分区 UUID 的可以参考此文。~~旧时，安装过黑苹果的人应该都设置过分区类型 ID~~

### 关于 UFS
UFS 全称是 Unix File System，即 UNIX 文件系统，基于 UNIX v7。过去，macOS 也使用该文件系统作为 root 文件系统。目前 FreeBSD 在使用的是 UFS2。Linux 对 UFS 的读写支持也不完整。这个文件系统只能扩大不能被缩小。

> **注意**
>
> UFS 文件系统和手机等设备中使用的 UFS 存储完全不是一回事，那个 UFS 是 Universal Flash Storage（通用闪存存储）的缩写，已经出到 4.0 了（FreeBSD 于 10.4 支持 eMMC；而 UFS 出现在 FreeBSD 15.0 的开发计划中，尚不支持）。而作为文件系统的 UFS 版本号才是 2。而且手机内部的系统也不可能是 UFS 文件系统，因为基于 Linux 的安卓根本不支持 UFS 这个文件系统，这些设备一般的根文件系统是 ext4（一些新设备是 F2FS）。