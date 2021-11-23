# 第五节 Linux 兼容层

**1、安装Linux 兼容层：**

以下参考[https://docs.freebsd.org/en/books/handbook/linuxemu/](https://docs.freebsd.org/en/books/handbook/linuxemu/)

`pkg install emulators/linux-c7`

开启服务：

```
sysrc linux_enable=”YES”
sysrc kld_list=”linux linux64”
```