# 第 2.3 节 键盘布局和主机名

## 设定键盘布局

![](../.gitbook/assets/ins4.png)

`FreeBSD 系统控制台驱动程序默认使用标准` US `（美式）键盘布局。可以在下面选择别的键盘布局。`

这里是键盘布局菜单，直接按 **回车键** 使用默认键盘布局即可（因目前中国使用美式键盘布局）。

## 设定主机名

![](../.gitbook/assets/ins5.png)

`请选择此机器的主机名。如果你正运行在受管理的网络上，请向你的网络管理员询问合适的名称。`

此处为设置主机名菜单。

>**警告**
>
>**不要** 在这一步直接按 **回车键**！这样会导致主机名为空！登录管理器 sddm 会无法启动。

>**警告**
>
>官方手册上说的是错的（`Amnesiac`），如果你不设置主机名，那么你的主机名不会被赋予任何值（不会给你分配 `Amnesiac`！），因为 FreeBSD 源码已经假设你会通过 DHCP 分配该值了。根据目前的源代码逻辑，只要你使用了 DHCP，也不会有任何报错提示主机名为空，当且仅当你没有网络时，才会在登录时将 login 信息打印为 `Amnesiac`，并打印一条报错信息。

### 参考信息

- [If the hostname is not set for the host, the value "Amnesiac" should be written to rc.conf. ](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=286847)，笔者发现的 bug
- [libexec/getty/main.c](https://github.com/freebsd/freebsd-src/blob/80c12959679ab203459dc20eb9ece3a7328b7de5/libexec/getty/main.c#L178)，`Amnesiac` 源码
- [bsdinstall: Warn if hostname is empty](https://github.com/freebsd/freebsd-src/pull/1700)，笔者的 PR

