# 第 29.1 节 安装 i3wm

## 安装 i3wm


```shell-session
# pkg install xorg i3 i3status dmenu i3lock
```

或者：

```
# cd /usr/ports/x11/xorg/
# make install clean
```

- i3status 为状态栏，
- dmenu 为菜单
- 默认配置需要以上两个组件（估且称之为组件），i3lock 是锁屏可选


## 配置

```shell-session
$ echo "/usr/local/bin/i3" >> ~/.xinitrc
$ chown 你的用户名 ~/.xinitrc
```

## 启动

可以用 `startx` 启动 i3 了。

**下图为纯 i3，无插件！**

![i3 on freebsd](../.gitbook/assets/i3wm_preview.png)


# 虚拟机扩展
如果使用 virtualbox,则下面启用 virtualbox 扩展：

```shell-session
& echo "exec VBoxClient-all" >> ~/.config/i3/config
```

## 参考

- [i3 使用手册](https://www.freebsd.org/cgi/man.cgi?query=i3&apropos=0&sektion=1&manpath=freebsd-ports&format=html)
- [Installing i3wm on FreeBSD](http://bottlenix.wikidot.com/installing-i3wm)
- [How to setup FreeBSD with a riced desktop - part 3 - i3](https://unixsheikh.com/tutorials/how-to-setup-freebsd-with-a-riced-desktop-part-3-i3.html#xterm)
- [How to install i3?](https://forums.freebsd.org/threads/how-to-install-i3.62305/)
- [i3 - an improved	dynamic, tiling	window manager](https://www.freebsd.org/cgi/man.cgi?query=i3&apropos=0&sektion=1&manpath=freebsd-ports&format=html)

