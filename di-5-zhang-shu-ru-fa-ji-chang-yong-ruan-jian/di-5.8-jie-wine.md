# 第 5.8 节 Wine

FreeBSD 上的 Wine 以往一直就有问题，[无法运行 win32 程序](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=265273)。始终报错 `0024:fixme:ntdll:create_logical_proc_info stub`。

## 开发版

### 安装

```sh
# pkg install wine-devel
```
或者：

```sh
# cd /usr/ports/emulators/wine-devel/ 
# make install clean
```

