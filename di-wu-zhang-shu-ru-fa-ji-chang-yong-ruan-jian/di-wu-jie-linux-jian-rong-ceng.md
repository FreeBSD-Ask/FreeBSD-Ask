# 第五节 Linux 兼容层

**注意：一个常见误解就是把 FreeBSD 的 Linux 兼容层当做 Wine，认为这样做会降低软件的运行效率。实际情况是不仅不会慢，而且速度还会比在 Linux 中更快，运行效率更高。**

## 系统自带；

以下参考

https://docs.freebsd.org/en/books/handbook/linuxemu

开启服务：

```
# sysrc linux_enable="YES"
# sysrc kld_list+="linux linux64"
# kldload linux64
# pkg install emulators/linux-c7
# service linux start
# dbus-uuidgen > /compat/linux/etc/machine-id
# reboot
```

## 自己构建 ubuntu/debian 兼容层（未经过实际测试，仅供专业人士自行测试！）

FreeBSD 12.0： https://forums.freebsd.org/threads/linuxulator-how-to-run-google-chrome-linux-binary-on-freebsd.77559/

FreeBSD 13.0： https://forums.freebsd.org/threads/linuxulator-how-to-install-brave-linux-app-on-freebsd-13-0.78879/
