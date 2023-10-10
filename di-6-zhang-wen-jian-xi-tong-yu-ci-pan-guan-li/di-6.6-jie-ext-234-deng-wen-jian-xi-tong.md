# 第 6.6 节 Ext 2/3/4 等文件系统

## EXT 文件系统

请注意：此处应该安装 `fusefs-ext2`（同时支持 EXT2/3/4）而非 `fusefs-ext4fuse`，因为后者是只读且被废弃的。

- 安装 fusefs-ext2

```shell-session
# pkg install fusefs-ext2
```

- 加载

  打开`/etc/rc.conf`，在 `kld_list`一栏里添加 **ext2fs**，结果可能如 `kld_list="ext2fs i915kms"`

- 重启后，挂载。

  对于用户名为 `XiaoMing` 的账号，可如下操作：

```shell-session
$ cd ~
$ mkdir media
$ cd media
$ mkdir first
# mount -t ext2fs /dev/da0sX /home/XiaoMing/media/first/
```

_提示：上式不一定是 `da0sX`（X 为对应的数字），可通过 `# gpart list` 命令查看硬盘名。_

- 卸载硬盘

`# umount /home/XiaoMing/media/first/`

## Brtfs/XFS 文件系统

> 未经测试

```shell-session
# pkg install fusefs-lkl
```
