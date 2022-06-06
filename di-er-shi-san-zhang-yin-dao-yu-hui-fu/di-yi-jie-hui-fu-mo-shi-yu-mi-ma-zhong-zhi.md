# 第一节 恢复模式与密码重置

开机按 2 进入 `single user` 单用户模式。

## UFS 文件系统

```
# mount -u /
# mount -a -t ufs
```

## ZFS 文件系统

```
# mount -u
# zfs mount -a
```

## 使用 U 盘设备

```
# mount /dev/adaXpN -o rw /mnt
```
`X`、`N` 的参数取决于具体设备。
