# 第 6.5 节 SWAP 交换分区的设置

如果在安装系统的时候并未设置 swap 即交换分区，那么只能通过 dd 生成一个交换分区文件或 ZFS 卷来实现了。因为无论是 UFS 还是 ZFS 都是不支持缩小文件系统分区的。

>**警告**
>
>本节操作可能会影响到崩溃转储。

## 传统的 dd 单个文件

dd 一个 大小为 1GB 的 swap 文件（1G=1024MB，要更多就做个计算题）：

```sh
# dd if=/dev/zero of=/usr/swap0 bs=1M count=1024
```

设置权限为 600，即只有拥有者有读写权限。

```sh
# chmod 0600 /usr/swap0
```

如果要立即使用：

```sh
# mdconfig -a -t vnode -f /usr/swap0 -u 0 && swapon /dev/md0
```

为了重启后仍然有效，还需要往 `/etc/rc.conf` 中加入

```sh
swapfile="/usr/swap0"
```

## 使用 ZFS 卷充当 swap

```sh
# zfs create -V 8G zroot/swap
# swapon /dev/zvol/zroot/swap
```

以上，参数 `-V` 创建 zfs 卷而不是 zfs 文件系统。zfs 默认的名字就是 `zroot`。

写入 `/etc/fstab` 开机时自动挂载：

```sh
/dev/zvol/zroot/swap none swap sw
```

写入后用命令 `mount -al` 检查一下，无错误输出才可。

## 查看 swap 用量


```sh
root@ykla:~ # swapinfo -h
Device              Size     Used    Avail Capacity
/dev/nda0p3         2.0G       0B     2.0G     0%
```

可以看到，`/dev/nda0p3` 是交换分区，大小为 2G，已用 0。
