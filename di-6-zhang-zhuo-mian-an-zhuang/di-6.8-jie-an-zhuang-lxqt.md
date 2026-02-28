# 6.9 LXQt

## 安装 LXQt

- 通过 pkg 安装：

```sh
# pkg install xorg sddm lxqt gvfs wqy-fonts xdg-user-dirs
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11-wm/lxqt/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/x11/sddm/ && make install clean
# cd /usr/ports/devel/gvfs/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```

- 软件包说明：

| 包名               | 功能说明                                                                 |
|:--------------------|:--------------------------------------------------------------------------|
| `xorg`             |  X Window System |
| `sddm`             | 登录管理器 |
| `lxqt`             | LXQt 桌面环境 |
| `gvfs`             | GNOME 虚拟文件系统，LXQt 依赖此组件以打开 Computer 和 Network，否则会提示 `Operation not supported`|
| `wqy-fonts`        | 文泉驿中文字体|
| `xdg-user-dirs`    | 管理用户目录，如“桌面”、“下载”等，并处理目录名称的本地化|


## 服务管理

```sh
# service dbus enable  # 设置 D-Bus 服务开机自启
# service sddm enable  # 设置 SDDM 显示管理器开机自启
```

## 挂载 proc 文件系统


编辑 `/etc/fstab` 文件，加入下行：

```sh
proc	/proc	procfs	rw	0	0
```

将 `procfs` 文件系统挂载到 `/proc`，读写模式。

## 通过 startx 启动 LXQt

将启动命令写入 `~/.xinitrc` 文件，以启动 LXQt 桌面环境：

```sh
$ echo "exec ck-launch-session startlxqt" > ~/.xinitrc
```

读者使用哪个账户登录，就使用该账户写入。

## 设置中文显示

### 设置 SDDM 显示管理器语言为中文

```sh
# sysrc sddm_lang="zh_CN"
```

![FreeBSD 安装 LXQt](../.gitbook/assets/lxqt1.png)

![FreeBSD 安装 LXQt](../.gitbook/assets/lxqt2.png)

![FreeBSD 安装 LXQt](../.gitbook/assets/lxqt3.png)

### 中文化桌面

进入 LXQt 后，菜单 -> "Preferences" -> "LXQt Settings" -> "Locale" -> "Region"，在下拉菜单中选择中文。

![FreeBSD 安装 LXQt](../.gitbook/assets/lxqt4.png)

![FreeBSD 安装 LXQt](../.gitbook/assets/lxqt5.png)

## 故障排除与未竟事宜

### 桌面图标不显示

请事先安装自己喜欢的其他图标主题。然后：菜单 -> "Preferences" -> "LXQt Settings" -> "Appearance" -> "Icons Theme"，选择已安装的图标主题，点击 "Apply" 后重新登录。

