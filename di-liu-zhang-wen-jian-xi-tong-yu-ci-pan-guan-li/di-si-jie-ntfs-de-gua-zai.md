# 第四节 NTFS 的挂载

1. 安裝 ntfs-3g 软件 #`pkg install sysutils/fusefs-ntfs`
2. 把你的 ntfs 硬盘或 U 盘插入计算机。 这时候你会看到它的设备名，例如 `da0`。
3. 修改 `rc.conf`

```
sysrc kld_list+="fusefs"
```

4、修改 fstab 自动挂载

为了开机自动挂载，修改添加

```
# ee /etc/fstab
/dev/da0s1  /media/NTFS ntfs  rw,mount_prog=/usr/local/bin/ntfs-3g,late  0  0
```

或者，手动挂载

```
# ntfs-3g  /dev/da0s1  /media/NTFS   -o  rw,uid=1000,gid=1000,umask=0`
```

如果不知道哪个磁盘分区是 NTFS，可以用命令来查看

```
# fstyp /dev/da0s1
```

详细参数见 [ntfs-3g manpage。](https://www.freebsd.org/cgi/man.cgi?query=ntfs-3g\&format=html)
