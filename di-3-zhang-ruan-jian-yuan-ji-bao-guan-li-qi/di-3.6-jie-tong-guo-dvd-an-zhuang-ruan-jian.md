# 第3.6节 通过 DVD 安装软件

## 使用环境变量

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

### 故障排除

**/dist** 目录若改为其他则无效，原因未知，若你知道请告诉我们。

## 换源为 DVD

```
mkdir /mnt/DVD
mount -t /dev/cd0 /mnt/DVD
mkdir /usr/local/etc/pkg/repos
```

创建 `/usr/local/etc/pkg/repos/DVD.conf`：

```
FreeBSD:{enabled:no}
DVD:{
url:"file:///mnt/DVD/packages/FreeBSD:12:amd64",
enabled:yes
}
```


参考资料：

[https://www.freebsdmall.com/cgi-bin/fm/bsddvd10.1](https://www.freebsdmall.com/cgi-bin/fm/bsddvd10.1)
