# 第3.6节 通过 DVD 安装软件

## 使用环境变量

### 挂载 DVD 到 **/dist** 目录:

若直接挂载本地 ISO：

```
# mdconfig -a -t vnode -f FreeBSD-13.1-RELEASE-amd64-dvd1.iso -u 0 #不能直接挂载，显示错误 block device required
# mkdir -p /dist
# mount -t cd9660 /dev/md0 /dist
```

若直接使用 DVD 设备（如虚拟机直接挂载 ISO 镜像）：

```
# mkdir -p /dist
# mount -t cd9660 /dev/cd0 /dist
```

### 安装软件

测试安装：

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

### 挂载 DVD 到 **/dist** 目录:

若直接挂载本地 ISO：

```
# mdconfig -a -t vnode -f FreeBSD-13.1-RELEASE-amd64-dvd1.iso -u 0 #不能直接挂载，显示错误 block device required
# mkdir -p /dist
# mount -t cd9660 /dev/md0 /dist
```

若直接使用 DVD 设备（如虚拟机直接挂载 ISO 镜像）：

```
# mkdir -p /dist
# mount -t cd9660 /dev/cd0 /dist
```

### 创建源

创建 `/usr/local/etc/pkg/repos/DVD.conf`：

```
FreeBSD:{enabled:no}
DVD:{
url:"file:///dist/packages/FreeBSD:13:amd64",
enabled:yes
}
```


参考资料：

[https://www.freebsdmall.com/cgi-bin/fm/bsddvd10.1](https://www.freebsdmall.com/cgi-bin/fm/bsddvd10.1)
