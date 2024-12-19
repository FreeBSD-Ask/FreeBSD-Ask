# 第 4.21 节 安装 KDE6


## KDE6-基于 Xorg

### 安装

```sh
# pkg install xorg sddm x11/kde6 plasma6-sddm-kcm wqy-fonts xdg-user-dirs
```

或者

```sh
# cd /usr/ports/x11/xorg/ && make install clean # X11
# cd /usr/ports/x11/kde6/ && make install clean # KDE5
# cd /usr/ports/x11/sddm/ && make install clean # 窗口管理器
# cd /usr/ports/deskutils/plasma6-sddm-kcm/ && make install clean # KDE 管理 SDDM 的模块
# cd /usr/ports/x11-fonts/wqy/ && make install clean # 文泉驿字体
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean # 自动创建用户目录的工具
```

### 配置

- 启动项设置

```sh
# sysrc dbus_enable="YES"
# sysrc sddm_enable="YES"
```

然后（可选，如果不需要 startx）

```sh
$ echo "exec ck-launch-session startplasma-x11" > ~/.xinitrc
```

如果你在 root 下已经执行过了，那么新用户仍要再执行一次才能正常使用（无需 root 权限或 sudo 等）startx。

- 权限设置

普通用户还需要将用户加入 wheel 组：

```sh
# pw groupmod wheel -m 用户名
```

- SDDM 中文化

```sh
# sysrc sddm_lang="zh_CN"
```

![FreeBSD 安装 KDE6](../.gitbook/assets/kde6-1.png)

![FreeBSD 安装 KDE6](../.gitbook/assets/kde6-2.png)

![FreeBSD 安装 KDE6](../.gitbook/assets/kde6-3.png)

##  KDE6-基于 Wayland

在 KDE6-基于 Xorg 的基础上，把 `/usr/local/share/xsessions/plasmax11.desktop` 中的 `Exec` 和 `TryExec` 都改成 `/usr/local/bin/startplasma-wayland`。重启即可。

![FreeBSD 安装 KDE6](../.gitbook/assets/kde6-4.png)


