# 第 4.7 节 安装 Lumina

2025.1.8 测试在 VMware 中无法进入桌面，进入后闪退。参见 [Some problem Under FreeBSD 13.2 with Xorg and Lumina Desktop...How to solve?](https://forums.freebsd.org/threads/some-problem-under-freebsd-13-2-with-xorg-and-lumina-desktop-how-to-solve.88882/)
但是在 VirtualBox 中显示正常。


>**注意**
>
>[Lumina](https://github.com/lumina-desktop/lumina) 在换了开发者后，开发长期处于停滞状态，我向其提交的 pull 长期无人处理，并且没有新的 commit 信息。

## 安装

```sh
# pkg install lumina xorg lightdm lightdm-gtk-greeter wqy-fonts xdg-user-dirs
```

或者

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11/lumina/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/x11/lightdm/ && make install clean
# cd /usr/ports/x11/lightdm-gtk-greeter/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean
```

## 配置

```sh
# sysrc dbus_enable="YES"
# sysrc lightdm_enable="YES"
```

```sh
# ee ~/.xinitrc
```

添加：

```sh
exec lumina-desktop
```

## 中文化

在 `/etc/rc.conf` 下加入：

```sh
lightdm_env="LC_MESSAGES=zh_CN.UTF-8" 
```

编辑 `/etc/login.conf`：

找到 `default:\` 这一段，把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：

```sh
# cap_mkdb /etc/login.conf
```

![FreeBSD 安装 Lumina](../.gitbook/assets/lumina1.png)

![FreeBSD 安装 Lumina](../.gitbook/assets/lumina2.png)

![FreeBSD 安装 Lumina](../.gitbook/assets/lumina3.png)