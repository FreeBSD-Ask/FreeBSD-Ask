# 第 4.23 节 安装 Fluxbox

## 安装

```sh
# pkg install xorg fluxbox fluxbox-tenr-styles-pack slim wqy-fonts xdg-user-dirs
```

或者：

```sh
# cd /usr/ports/x11-wm/fluxbox/ && make install clean # fluxbox
# cd /usr/ports/x11-themes/fluxbox-tenr-styles-pack/ && make install clean # fluxbox 主题 配置工具，未作为依赖包安装，包含语言包，但是没中文
# cd /usr/ports/x11/xorg/ && make install clean # X11
# cd /usr/ports/x11/slim/ && make install clean # slim 窗口管理器
# cd /usr/ports/x11-fonts/wqy/ && make install clean # 文泉驿字体
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean # 自动创建用户目录的工具
```


## `startx`

编辑 `~/.xinitrc`，加入（用谁登录就用谁写入）：

```sh
exec startfluxbox
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

## 中文配置


编辑 `/etc/login.conf`：

找到 `default:\` 这一段，把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：

```sh
# cap_mkdb /etc/login.conf
```

## 桌面欣赏

![FreeBSD 安装 fluxbox](../.gitbook/assets/fluxbox1.png)

![FreeBSD 安装 fluxbox](../.gitbook/assets/fluxbox2.png)

## 故障排除

- light、xdm 均不可用，无法启动 fluxbox

待解决

- 没有中文

待解决