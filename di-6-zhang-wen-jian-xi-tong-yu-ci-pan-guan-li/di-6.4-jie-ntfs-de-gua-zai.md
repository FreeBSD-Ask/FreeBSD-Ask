# 第 6.4 节 NTFS 的挂载

1. 安裝 ntfs-3g 软件 `# pkg install sysutils/fusefs-ntfs`
2. 把你的 ntfs 格式的硬盘或 U 盘插入计算机。这时候你会看到它的设备名，例如 `da0`。
3. 修改 `rc.conf`

```shell-session
# sysrc kld_list+="fusefs"
```

## 永久性挂载，修改 fstab 自动挂载

为了开机自动挂载，修改添加

```shell-session
# ee /etc/fstab
```

加入：

```shell-session
/dev/da0s1  /media/NTFS ntfs  rw,mount_prog=/usr/local/bin/ntfs-3g,late  0  0
```

## 手动挂载

```shell-session
# ntfs-3g  /dev/da0s1  /media/NTFS   -o  rw,uid=1000,gid=1000,umask=0
```

如果不知道哪个磁盘分区是 NTFS，可以用命令来查看

```shell-session
# fstyp /dev/da0s1
```

**注意：如果报错，尝试删除休眠文件：**

```shell-session
# ntfs-3g  /dev/da0s1 /mnt/NTFS -o remove_hiberfile
```

如果还是有问题：

```shell-session
# ntfsfix /dev/da0s1
```

然后重新挂载。

详细参数见 [ntfs-3g manpage](https://www.freebsd.org/cgi/man.cgi?query=ntfs-3g&format=html)。如果无法挂载请先关闭 windows 的休眠，然后重启几次。
