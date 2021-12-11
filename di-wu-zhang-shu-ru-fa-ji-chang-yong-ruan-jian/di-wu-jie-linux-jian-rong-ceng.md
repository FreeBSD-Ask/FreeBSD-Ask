# 第五节 Linux 兼容层

**注意：一个常见误解就是把 FreeBSD 的 Linux 兼容层当做 Wine，认为这样做会降低软件的运行效率。实际情况是不仅不会慢，而且速度还会比在 Linux 中更快，运行效率更高。**

**1、安装 Linux 兼容层：**

以下参考

{% embed url="https://docs.freebsd.org/en/books/handbook/linuxemu" %}

开启服务：

```
# sysrc linux_enable="YES"
# sysrc kld_list="linux linux64"
# service linux start
# pkg install emulators/linux-c7
# reboot
```
