# 第 4.9 节 bspwm

bspwm，据说更符合 UNIX 哲学（参见 [bspwm 入门](https://zerovip.vercel.app/zh/63233/)，7.2 Unix 哲学）。

## 安装 bspwm

- 通过 pkg 安装

```sh
# pkg install xorg bspwm sxhkd rofi kitty feh picom polybar dunst lightdm lightdm-gtk-greeter wqy-fonts xdg-user-dirs
```

xdg-user-dirs 可自动管理家目录子目录（可选安装）

- 通过 Ports 安装：


```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11-wm/bspwm/ && make install clean
# cd /usr/ports/x11/sxhkd/ && make install clean
# cd /usr/ports/x11/rofi/ && make install clean
# cd /usr/ports/x11/kitty/ && make install clean
# cd /usr/ports/graphics/feh/ && make install clean
# cd /usr/ports/x11-wm/picom/ && make install clean
# cd /usr/ports/x11/polybar/ && make install clean
# cd /usr/ports/sysutils/dunst/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/x11/lightdm/ && make install clean
# cd /usr/ports/x11/lightdm-gtk-greeter/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean # 自动管理家目录子目录
```

解释：


| 包名                  | 作用说明                                                                 |
|:---------------------|:--------------------------------------------------------------------------|
| `xorg`              |  X Window 系统                                            |
| `bspwm`             | 轻量级的平铺式窗口管理器                                 |
| `sxhkd`             | 用于绑定快捷键的工具                                     |
| `rofi`              | 程序启动器，支持应用启动、窗口切换等功能                                        |
| `kitty`             | 终端模拟器                             |
| `feh`               | 桌面背景修改                                       |
| `picom`             | 窗口合成器，添加窗口透明，阴影，动效等                                     |
| `polybar`           | 面板，显示系统信息、应用图标等                                          |
| `dunst`             | 通知管理器                                                |
| `lightdm`           | LightDM 显示管理器，提供图形登录界面                                                 |
| `lightdm-gtk-greeter`| LightDM 的 GTK+ 登录界面插件，缺少将无法启动 LightDM                     |
| `wqy-fonts`         | 文泉驿中文字体                                             |
| `xdg-user-dirs`     | 管理用户目录，如“桌面”、“下载”等                                          |



>**提示**
>
>polybar 建议换成别的，因为 polybar 在 freebsd 上功能不全。建议换成 `chinese/tintin++`，可显示 systray 图标


## 启用服务

```sh
# service dbus enable
```

## 创建配置文件

```sh
$ mkdir ~/.config
$ mkdir ~/.config/bspwm
$ mkdir ~/.config/sxhkd
$ cp /usr/local/share/examples/bspwm/bspwmrc ~/.config/bspwm
$ cp /usr/local/share/examples/bspwm/sxhkdrc ~/.config/sxhkd
$ chmod +x ~/.config/bspwm/bspwmrc
```

修改 `~/.config/sxhkd/sxhkdrc`

```sh
super + Return
    kitty

super + @space
    rofi -show drun
```

## 设置 polybar 启动脚本和配置文件

```sh
$ mkdir ~/.config/polybar 
$ cp /usr/local/etc/polybar/config.ini ~/.config/polybar
```

创建 `~/.config/polybar/launch.sh`

```sh
#!/bin/sh
killall -q polybar
polybar example 2>&1 | tee -a /tmp/polybar.log
```

并执行

```sh
$ chmod +x ~/.config/polybar/launch.sh
```

## 设置 picom、polybar、dunst 启动

```sh
$ echo "picom &" >> ~/.config/bspwm/bspwmrc
$ echo "\$HOME/.config/polybar/launch.sh" >> ~/.config/bspwm/bspwmrc
$ echo "dunst &" >> ~/.config/bspwm/bspwmrc
```


## 通过 startx 启动 bspwm

```sh
$ echo "exec bspwm" >> ~/.xinitrc
```

## 通过 lightdm 启动 bspwm

- 创建 `/usr/local/share/xsessions/bspwm.desktop`

```sh
# mkdir /usr/local/share/xsessions
# ee /usr/local/share/xsessions/bspwm.desktop # 写入以下内容

[Desktop Entry]
Name=bspwm
Comment=Log in with bspwm
Exec=/usr/local/bin/bspwm
Type=Application
```

- lightdm 服务

```sh
# service lightdm enable
```

## 一些操作和设置

Windows + 空格：用 rofi 启动应用

Windows + 回车：启动终端（即 kitty）

更多快捷键可以参考 `~/.config/sxhkd/sxhkdrc`

生成桌面文件夹（Downloads，Documents 等）

```sh
$ xdg-user-dirs-update
```

设置桌面背景：

```sh
$ feh --bg-center "$HOME/.local/share/wallpapers/wallpaper.jpg"
```

执行一次后自动设置：

在 `~/.config/bspwm/bspwmrc` 中的 polybar 启动脚本 **之前** 添加

```sh
$HOME/.fehbg &
```

## 展示图片

![](../.gitbook/assets/bspwm.png)

注：图片中的 Chrome 浏览器，Thunar 文件管理器均需要自己安装。

## 参考文献

- [从零开始的 Bspwm 安装与配置教程](https://zhuanlan.zhihu.com/p/568211941)
