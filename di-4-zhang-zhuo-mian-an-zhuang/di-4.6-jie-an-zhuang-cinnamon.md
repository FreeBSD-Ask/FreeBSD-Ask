# 第 4.6 节 Cinnamon

>**注意**
>
> 以下教程适用于 shell 为 bash/sh/zsh 的用户。
>
> 首先看看现在自己的 shell 是不是 `sh`（FreeBSD 默认）、`bash`、`zsh`：
>
>```sh
># echo $0
>```


## 安装

- 使用 pkg 安装：

```sh
# pkg install xorg lightdm slick-greeter cinnamon wqy-fonts xdg-user-dirs
```

| 包名               | 作用说明                   |
|:--------------------|:----------------------------------|
| `xorg`             |  X Window 系统 |
| `lightdm`          | 轻量级显示管理器 LightDM，提供图形登录界面 |
| `slick-greeter`    | LightDM 的美观登录界面插件，缺少将无法启动 LightDM|
| `cinnamon`         | 基于 GNOME 3 的现代桌面环境|
| `wqy-fonts`        | 文泉驿中文字体 |
| `xdg-user-dirs`    | 管理用户目录，如“桌面”、“下载”等  |

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11/cinnamon/ && make install clean 
# cd /usr/ports/x11-fonts/wqy/ && make install clean 
# cd /usr/ports/x11/lightdm/ && make install clean 
# cd /usr/ports/x11/slick-greeter/ && make install clean 
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```


## 配置 `startx`

编辑 `~/.xinitrc`，添加：

```sh
exec cinnamon-session
```

## 配置 `fstab`

编辑 `/etc/fstab`，添加：

```sh
proc /proc procfs rw 0 0
```

## 服务管理

```sh
# service dbus enable 
# service lightdm enable
```

## 中文化

编辑 `/etc/login.conf`：找到 `default:\` 这一段（写作时为第 24 行），把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：

```sh
# cap_mkdb /etc/login.conf
```

## 桌面欣赏

![cinnamon on FreeBSD](../.gitbook/assets/cinnamon1.png)

![cinnamon on FreeBSD](../.gitbook/assets/cinnamon2.png)

壁纸就是黑色的，不是哪儿出了问题。

![cinnamon on FreeBSD](../.gitbook/assets/cinnamon3.png)

自定义壁纸。
