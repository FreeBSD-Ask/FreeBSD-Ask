# 第 4.8 节 安装 LXQt

## 安装 LXQt

通过 pkg 安装

```sh
# pkg install xorg sddm lxqt gvfs wqy-fonts xdg-user-dirs
```

或者：

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11-wm/lxqt/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/x11/sddm/ && make install clean
# cd /usr/ports/devel/gvfs/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean
```

解释：

- sddm：LXQt 首选的显示管理器

- gvfs：GNOME 虚拟文件系统，LXQt 依赖此打开 Computer 和 Network ，否则会提示 `Operation not supported`

## 准备

启用 dbus 服务

```sh
# sysrc dbus_enable="YES"
```

修改 fstab

```sh
# ee /etc/fstab
添加如下内容
proc	/proc	procfs	rw	0	0
```

## 启动 LXQt

### 通过 startx

```sh
$ echo "exec ck-launch-session startlxqt" > ~/.xinitrc
```

### 通过 sddm

```sh
# sysrc sddm_enable="YES"
```

## 设置中文显示

进入 LXQt 后 菜单 -> "Preferences" -> "LXQt Settings" -> "Locale" -> "Region" 下拉菜单选择中文

sddm 本地化语言见 KDE 章节。


## 故障排除

### 桌面图标不显示

菜单 -> "Preferences" -> "LXQt Settings" -> "Appearance" -> "Icons Theme" 选择 "Oxygen" -> "Apply"

之后重新登陆

你也可以事先安装自己喜欢的其他图标在这里启用