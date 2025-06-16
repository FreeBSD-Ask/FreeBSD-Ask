# 第 4.12 节 i3wm

## 安装 i3wm

- 使用 pkg 安装：

```sh
# pkg install xorg i3 i3status dmenu i3lock
```

- 或者使用 Ports：

```
# cd /usr/ports/x11/xorg/
# make install clean
```

- 解释：

| 包名       | 作用说明                                                  |
|:------------|:--------------------------------------------------|
| `xorg`     |  X Window                                             |
| `i3`       | 轻量级平铺式窗口管理器                  |
| `i3status` | 状态栏 |
| `dmenu`    | 动态菜单生成器|
| `i3lock`   | 锁屏工具 |


## 配置 `startx`

```sh
$ echo "/usr/local/bin/i3" > ~/.xinitrc
```

用哪个用户登录 GUI 就使用哪个用户进行编辑。

## 启动 i3

可以用 `startx` 启动 i3 了。

下图为纯 i3，无插件！

![i3 on freebsd](../.gitbook/assets/i3wm_preview.png)


## 虚拟机扩展

如果使用 VirtualBox，下面可启用 VirtualBox 扩展：

```sh
& echo "exec VBoxClient-all" >> ~/.config/i3/config
```

## 参考文献

- [i3 使用手册](https://www.freebsd.org/cgi/man.cgi?query=i3&apropos=0&sektion=1&manpath=freebsd-ports&format=html)
- [Installing i3wm on FreeBSD](http://bottlenix.wikidot.com/installing-i3wm)
- [How to setup FreeBSD with a riced desktop - part 3 - i3](https://unixsheikh.com/tutorials/how-to-setup-freebsd-with-a-riced-desktop-part-3-i3.html#xterm)
- [How to install i3?](https://forums.freebsd.org/threads/how-to-install-i3.62305/)
- [i3 - an improved	dynamic, tiling	window manager](https://www.freebsd.org/cgi/man.cgi?query=i3&apropos=0&sektion=1&manpath=freebsd-ports&format=html)
