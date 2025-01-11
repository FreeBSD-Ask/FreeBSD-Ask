# 第 4.13 节 安装 KDE6

在 Port 开发库中已经不再区分 kde5与 kde6 了。预计在可见的未来，将直接使用元包 `x11/kde`。


## 基于现有二进制包

### KDE6-基于 Xorg（不推荐）

不推荐使用此方法安装，由于严重落后于开发进度，全是 Bug——如文件管理器打不开，打开后无法点击顶栏等等。

#### 安装

```sh
# pkg install xorg sddm x11/kde6 plasma6-sddm-kcm wqy-fonts xdg-user-dirs
```

#### 配置

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

###  KDE6-基于 Wayland（不推荐）

在 KDE6-基于 Xorg 的基础上，把 `/usr/local/share/xsessions/plasmax11.desktop` 中的 `Exec` 和 `TryExec` 都改成 `/usr/local/bin/startplasma-wayland`。重启即可。

![FreeBSD 安装 KDE6](../.gitbook/assets/kde6-4.png)


## 基于开发中的 Ports（需要长时间编译）

```sh
# pkg install git
# git clone -b kde-it_goes_to_6 https://github.com/freebsd/freebsd-ports-kde /usr/ports # 你也许需要设置 git 代理才能访问 Github
```

安装 KDE6：

```sh
# whereis kde # 看看 KDE Port 的路径
# kde: /usr/ports/x11/kde
# cd /usr/ports/x11/kde
# make BATCH=yes install clean
```

配置方法同上。