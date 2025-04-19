# 第 4.17 节 Fluxbox

## 安装

- 使用 pkg 安装：

```sh
# pkg install xorg fluxbox fluxbox-tenr-styles-pack slim wqy-fonts xdg-user-dirs
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/x11-wm/fluxbox/ && make install clean # fluxbox
# cd /usr/ports/x11-themes/fluxbox-tenr-styles-pack/ && make install clean 
# cd /usr/ports/x11/xorg/ && make install clean 
# cd /usr/ports/x11/slim/ && make install clean 
# cd /usr/ports/x11-fonts/wqy/ && make install clean 
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```

- 解释


| 包名                        | 作用说明                                                                 |
|:-----------------------------|:--------------------------------------------------------------------------|
| `xorg`                      | X Window 系统                                           |
| `fluxbox`                   | 窗口管理器|
| `fluxbox-tenr-styles-pack`  | Tenner 提供的 Fluxbox 主题包 |
| `slim`                      | 轻量级图形登录管理器|
| `wqy-fonts`                 | 文泉驿中文字体                                            |
| `xdg-user-dirs`             | 管理用户目录，如“桌面”、“下载”等                                         |



## `startx`

编辑 `~/.xinitrc`，加入（用谁登录就用谁写入）：

```sh
exec startfluxbox
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

## 中文配置


编辑 `/etc/login.conf`：找到 `default:\` 这一段，把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：

```sh
# cap_mkdb /etc/login.conf
```

## 桌面欣赏

![FreeBSD 安装 fluxbox](../.gitbook/assets/fluxbox1.png)

![FreeBSD 安装 fluxbox](../.gitbook/assets/fluxbox2.png)

## 故障排除与未竟事宜

- light、xdm 均不可用，无法启动 fluxbox

待解决

- 没有中文

待解决
