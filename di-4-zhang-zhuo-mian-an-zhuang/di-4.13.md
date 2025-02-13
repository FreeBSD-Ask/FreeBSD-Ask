# 第 4.13 节 安装 IceWM

## 安装

```sh
# pkg install xorg icewm slim wqy-fonts xdg-user-dirs
```

或者：

```sh
# cd /usr/ports/x11-wm/icewm/ && make install clean # fluxbox
# cd /usr/ports/x11-themes/icewm-extra-themes/ && make install clean # 主题
# cd /usr/ports/x11/xorg/ && make install clean # X11
# cd /usr/ports/x11/slim/ && make install clean # slim 窗口管理器
# cd /usr/ports/x11-fonts/wqy/ && make install clean # 文泉驿字体
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean # 自动创建用户目录的工具
```


## `startx`

编辑 `~/.xinitrc`，加入（用谁登录就用谁写入）：

```sh
exec icewm-session
```

## 启动项

```sh
# sysrc dbus_enable="YES"
# sysrc slim_enable="YES"
```

## fstab

编辑 `/etc/fstab`，加入：

```sh
proc           /proc       procfs  rw  0   0
```


## 桌面欣赏

![FreeBSD 安装 icewm](../.gitbook/assets/fluxbox1.png)

![FreeBSD 安装 icewm](../.gitbook/assets/icewm1.png)

![FreeBSD 安装 icewm](../.gitbook/assets/icewm2.png)

## 故障排除

- 菜单缺失文字

待解决

- 没有中文

待解决
