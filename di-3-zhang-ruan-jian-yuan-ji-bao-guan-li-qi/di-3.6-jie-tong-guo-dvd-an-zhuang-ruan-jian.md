# 第3.6节 通过 DVD 安装软件

挂载 DVD 到 **/mnt/DVD** 目录:

```
# mkdir -p /mnt/DVD
# mount -t cd9660 /dev/cd0 /mnt/DVD
```

安装软件：

```
# env REPOS_DIR=/mnt/DVD/packages/repos pkg install xorg
```

要列出看 DVD 中的可用软件：

```
# env REPOS_DIR=/mnt/DVD/packages/repos pkg rquery "%n"
```

参考资料：

[https://www.freebsdmall.com/cgi-bin/fm/bsddvd10.1](https://www.freebsdmall.com/cgi-bin/fm/bsddvd10.1)
