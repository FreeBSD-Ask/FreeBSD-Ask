# 5.12 LXDE

## 安装

- 使用 pkg 安装：

```sh
# pkg install lxde-meta xorg lightdm lightdm-gtk-greeter wqy-fonts xdg-user-dirs
```


- 或者使用 Ports 安装：

```sh
# cd /usr/ports/x11/lxde-meta/ && make install clean 
# cd /usr/ports/x11/xorg/ && make install clean 
# cd /usr/ports/x11/lightdm/ && make install clean 
# cd /usr/ports/x11/lightdm-gtk-greeter/ && make install clean 
# cd /usr/ports/x11-fonts/wqy/ && make install clean 
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```


- 解释：


| 包名                     | 作用说明                                                                 |
|:--------------------------|:-------------------------------------------|
| `xorg`                   |  X Window 系统                                            |
| `lxde-meta`              | LXDE 桌面环境的元包                              |
| `lightdm`                | 轻量级显示管理器 LightDM                                      |
| `lightdm-gtk-greeter`    | LightDM 的 GTK+ 登录界面插件，缺少将无法登录  LightDM                          |
| `wqy-fonts`              | 文泉驿中文字体                                           |
| `xdg-user-dirs`          | 管理用户目录，如“桌面”、“下载”等                                           |


## `startx`

编辑 `~/.xinitrc`，加入：

```sh
exec startlxde
```

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

编辑 `/etc/login.conf`：找到 `default:\` 这一段，把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：

```sh
# cap_mkdb /etc/login.conf
```

## 桌面欣赏

![FreeBSD 安装 LXDE](../.gitbook/assets/lxde1.png)

![FreeBSD 安装 LXDE](../.gitbook/assets/lxde2.png)

![FreeBSD 安装 LXDE](../.gitbook/assets/lxde3.png)

## 参考文献

- [Install & Configure a Desktop Environment: LXDE](https://wiki.freebsd.org/LXDE)
