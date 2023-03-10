# 第3.6节 通过 DVD 安装软件

挂载 DVD 到 **/dist** 目录:

```
# mkdir -p /dist
# mount -t cd9660 /dev/cd0 /dist
```

安装软件：

```
# env REPOS_DIR=/dist/packages/repos pkg install xorg
```

要列出看 DVD 中的可用软件：

```
# env REPOS_DIR=/dist/packages/repos pkg rquery "%n"
```

## 故障排除

**/dist** 目录若改为其他则无效，原因未知，若你知道请告诉我们。

参考资料：

[https://www.freebsdmall.com/cgi-bin/fm/bsddvd10.1](https://www.freebsdmall.com/cgi-bin/fm/bsddvd10.1)
