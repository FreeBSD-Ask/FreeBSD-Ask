# 12.2 IceWM

## 安装

- 使用 pkg 安装：

```sh
# pkg install xorg icewm slim wqy-fonts xdg-user-dirs
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/x11-wm/icewm/ && make install clean # fluxbox
# cd /usr/ports/x11-themes/icewm-extra-themes/ && make install clean 
# cd /usr/ports/x11/xorg/ && make install clean 
# cd /usr/ports/x11/slim/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean
```

- 解释
  
| 包名               | 作用说明                                                                 |
|:------------------|:-----------------------------------------------------------------------|
| `xorg`           |X Window 系统                                           |
| `icewm`          | 轻量级窗口管理器                    |
| `slim`           | 轻量级图形登录管理器                            |
| `wqy-fonts`      | 文泉驿中文字体                                              |
| `xdg-user-dirs`  | 管理用户目录，如“桌面”、“下载”……                                          |


## `startx`

编辑 `~/.xinitrc`，加入（用谁登录就用谁写入）：

```sh
exec icewm-session
```

## 启动项

```sh
# service dbus enable
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

## 故障排除与未竟事宜

- 菜单缺失文字

待解决

- 没有中文

待解决
