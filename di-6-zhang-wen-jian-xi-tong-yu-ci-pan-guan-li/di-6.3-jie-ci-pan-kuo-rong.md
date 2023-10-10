# 第 6.3 节 磁盘扩容

## 扩容方法

请注意 ZFS 和 UFS 都只能扩大不能缩小！

1. `gpart show`

```shell-session
root@freebsd:~ # gpart show
=>       3  41943035  da0  GPT  (20G)
         3       122    1  freebsd-boot  (61K)
       125     66584    2  efi  (33M)
     66709   2097152    3  freebsd-swap  (1.0G)
   2163861  10486633    4  freebsd-ufs  (5.0G)
  12650494  29292544       - free -  (14G)
```

查看系统盘大小只有 5G，显示 `da0` 只有这一个盘。

1. 执行扩容命令，`da0` 可从 `gpart show` 执行后查看到具体名称

> **警告** 如果你使用的是 GPT 分区表，上边的扩容操作（**在虚拟机或云服务器上的**）会破坏 GPT 分区表，所以需要先恢复之：
>
> ```shell-session
> # gpart recover da0
> ```
>
> 执行后下面步骤相同。

`i` 为要扩容的分区，这里扩容 / 分区 `freebsd-ufs`。

```shell-session
root@freebsd:~ #  gpart resize -i 4 da0
da0p4 resized
```

2. 启动 `growfs` 服务，自动完成扩展

```shell-session
root@freebsd:~ # service growfs onestart
Growing root partition to fill device
da0 recovering is not needed
da0p4 resized
growfs: no room to allocate last cylinder group; leaving 7.7MB unused
super-block backups (for fsck_ffs -b #) at:
 11544384, 12827072, 14109760, 15392448, 16675136, 17957824, 19240512, 20523200, 21805888, 23088576, 24371264,
 25653952, 26936640, 28219328, 29502016, 30784704, 32067392, 33350080, 34632768, 35915456, 37198144, 38480832
```

3. 用 `df -h` 命令查看结果。

```shell-session
root@freebsd:~ # df -hl
Filesystem         Size    Used   Avail Capacity  Mounted on
/dev/gpt/rootfs     18G    4.8G     12G    29%    /
devfs              1.0K      0B    1.0K     0%    /dev
/dev/gpt/efiesp     32M    651K     31M     2%    /boot/efi
tmpfs               20M    4.0K     20M     0%    /tmp
tmpfs               32M    156K     32M     0%    /var
```

