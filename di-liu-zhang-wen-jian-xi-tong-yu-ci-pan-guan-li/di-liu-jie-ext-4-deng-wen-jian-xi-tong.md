# 第六节 Ext 2/3/4 等文件系统

请注意：这里应该安装 fusefs-ext2（同时支持EXT2/3/4） 而非 fusefs-ext4fuse，因为后者是只读且被废弃的。

```
# 安装fusefs-ext2
#pkg install fusefs-ext2
# 加载
#ee /boot/loader.conf
#添加一行
kldload ext2fs
#重启后，挂载（请注意，这里不一定是ada0pX）
#mount -t /dev/ada0pX /home/test
```

\
