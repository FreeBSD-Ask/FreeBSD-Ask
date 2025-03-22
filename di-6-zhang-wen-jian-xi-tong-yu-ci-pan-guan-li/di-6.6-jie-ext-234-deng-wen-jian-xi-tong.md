# 第 6.6 节 Linux 文件系统

本文示例环境：

```sh
# gpart show -p nda1
=>      34  41942973    nda1  GPT  (20G)
        34      2014          - free -  (1.0M)
      2048   1339392  nda1p5  linux-data  (654M) # ext2
   1341440  19630080  nda1p1  linux-data  (9.4G) # ext4
  20971520   8388608  nda1p2  linux-data  (4.0G) # btrfs
  29360128   4194304  nda1p3  ms-basic-data  (2.0G) # fat32
  33554432   8386560  nda1p4  linux-data  (4.0G) # xfs
  41940992      2015          - free -  (1.0M)
```

里面各放置了一些文件和目录用于判断挂载情况。

## EXT 文件系统

fusefs-ext2 只是名字叫“ext2”，实际上也支持 ext3、ext 4。

### 安装 fusefs-ext2

```sh
# pkg install fusefs-ext2
```

或者

```sh
# cd /usr/ports/filesystems/ext2/ 
# make install clean
```

### 加载模块

```sh
# sysrc kld_list+="ext2fs"
```

### 挂载磁盘

- 创建挂载目录

```sh
$ mkdir -p /home/ykla/test # 这是我的示例文件夹，改成你自己的
```

- 只读挂载
  
```sh
# fuse-ext2 /dev/nda1p1 /home/ykla/test # 挂载磁盘分区。默认为只读
Mounting /dev/nda1p1 Read-Only.
Use 'force' or 'rw+' options to enable Read-Write mode
# ls /home/ykla/test/ # 查看挂载情况
lost+found	test		test.pdf
```

- 改成可读写挂载：

```sh
# fuse-ext2 -o rw+ /dev/nda1p1 /home/ykla/test # 挂载磁盘分区为可写
# ls /home/ykla/test/ # 查看挂载情况
lost+found	test		test.pdf
# cd /home/ykla/test/ # 切换到挂载路径
root@ykla:/home/ykla/test # touch my.txt # 创建一个文件测试看看能不能写
root@ykla:/home/ykla/test # ls # 查看读写 
lost+found	my.txt		test		test.pdf
```

## Brtfs/XFS/Ext4 文件系统

### 安装 fusefs-lkl

```sh
# pkg install fusefs-lkl
```

或者

```sh
# cd /usr/ports/filesystems/lkl/ 
# make install clean
```

### 加载内核模块

```sh
# sysrc kld_list+=fusefs
```

### 测试挂载 btrfs

```sh
# mkdir -p /home/ykla/btrfs # 创建挂载目录
# lklfuse -o type=btrfs /dev/nda1p2 /home/ykla/btrfs # 挂载磁盘分区
# ls /home/ykla/btrfs # 看看挂载情况
test1	test2	test3	test4
```

### 测试挂载 xfs

```sh
# mkdir -p /home/ykla/xfs # 创建挂载目录
# lklfuse -o type=xfs  /dev/nda1p4 /home/ykla/xfs # 挂载磁盘分区
# ls /home/ykla/xfs # 看看挂载情况
cfc	test1	test2
```

## 故障排除

- 怎么卸载？

待解决。

- 如何持久化挂载——如何写入 `/etc/fstab`？

待解决。


## 参考文献

- [mount linux ext4 drives on Freebsd](https://forums.freebsd.org/threads/mount-linux-ext4-drives-on-freebsd.74414/)
- [XFS support](https://forums.freebsd.org/threads/xfs-support.61449/)
