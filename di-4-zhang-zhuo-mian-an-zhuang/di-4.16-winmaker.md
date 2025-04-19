# 第 4.16 节 Window Maker

## 安装

- 使用 pkg 安装：

```sh
# pkg install windowmaker wmakerconf xorg lightdm lightdm-gtk-greeter wqy-fonts xdg-user-dirs
```

- 或者使用 Ports：

```sh
# cd /usr/ports/x11/windowmaker/ && make install clean
# cd /usr/ports/x11-wm/wmakerconf/ && make install clean 
# cd /usr/ports/x11/xorg/ && make install clean 
# cd /usr/ports/x11/lightdm/ && make install clean 
# cd /usr/ports/x11/lightdm-gtk-greeter/ && make install clean 
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```

- 解释：



| 包名                     | 作用说明                                                                 |
|--------------------------|-------------------------------------------------------|
| `xorg`                   | X Window 系统                                           |
| `windowmaker`            | X11 窗口管理器 |
| `wmakerconf`             | Window Maker 的配置工具，未作为依赖包安装；包含语言包，但是没中文|
| `lightdm`                | 轻量级显示管理器 LightDM |
| `lightdm-gtk-greeter`    | LightDM 的 GTK+ 登录界面插件，缺少将无法启动 LightDM |
| `wqy-fonts`              | 文泉驿中文字体|
| `xdg-user-dirs`          | 管理用户目录，如“桌面”、“下载”等|



## `startx`

编辑 `~/.xinitrc`，加入：

```sh
exec wmaker
```

### 参考文献

- [How to startx window maker?](https://www.linuxquestions.org/questions/debian-26/how-to-startx-window-maker-230516/)

## 启动项

```sh
# service dbus enable
# service lightdm enable
```

## fstab

编辑 `/etc/fstab`，加入：

```sh
proc           /proc       procfs  rw  0   0
```

### 中文配置

在 `/etc/rc.conf` 下加入：

```sh
lightdm_env="LC_MESSAGES=zh_CN.UTF-8" 
```

---

编辑 `/etc/login.conf`，找到 `default:\` 这一段，把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：

```sh
# cap_mkdb /etc/login.conf
```

## 图片

![FreeBSD 安装 Window Maker](../.gitbook/assets/WindowMaker1.png)

![FreeBSD 安装 Window Maker](../.gitbook/assets/WindowMaker2.png)

## 故障排除与未竟事宜

- `Could not execute command: exec WPrefs`

可以在终端输入

```sh
# /usr/local/GNUStep/Applications/WPrefs.app/WPrefs
```

![FreeBSD 安装 Window Maker](../.gitbook/assets/WindowMaker3.png)

- 无法中文化

待解决。

### 参考文献

- [windowmaker could not execute wprefs!](https://forums.freebsd.org/threads/windowmaker-could-not-execute-wprefs.92625/)
