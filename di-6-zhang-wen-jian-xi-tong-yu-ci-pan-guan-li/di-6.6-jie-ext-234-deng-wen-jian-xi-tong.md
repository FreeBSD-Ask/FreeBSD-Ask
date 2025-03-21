# 第 6.6 节 Ext 2/3/4 等文件系统

>**警告**
>
> 此章节待测试

## EXT 文件系统

请注意：此处应该安装 `fusefs-ext2`（同时支持 EXT2/3/4）而非 `fusefs-ext4fuse`，因为后者是只读且被废弃的。

### 安装 fusefs-ext2

```sh
# pkg install fusefs-ext2
```

或者

```sh
# cd /usr/ports/filesystems/fusefs-ext2/ 
# make install clean
```

### 加载模块

```sh
# sysrc kld_list+="ext2fs"
```

- 重启后再挂载：

```sh
$ mkdir -p /home/ykla/test # 这是我的示例文件夹，改成你自己的
# mount -t ext2fs /dev/nvd0 /home/ykla/test
```

>**技巧**
>
>上面不一定是 `nvd0`，可通过 `# gpart list` 命令查看硬盘名。_

- 卸载文件系统

```sh
# umount /home/ykla/test
```

## Brtfs/XFS 文件系统

```sh
# pkg install fusefs-lkl
```

或者

```sh
# cd /usr/ports/filesystems/fusefs-lkl/ 
# make install clean
```

## FAT32 文件系统

>**注意**
>
>必须显式声明文件系统类型才能挂载

```sh
# mount -v -t msdosfs  /dev/mmcsd0s1  /mnt
```
