# 7.1 bspwm

bspwm，据说更符合 UNIX 哲学（参见 [bspwm 入门](https://zerovip.vercel.app/zh/63233/)，7.2 Unix 哲学）。

## 安装 bspwm

- 通过 pkg 安装

```sh
# pkg install xorg bspwm sxhkd rofi kitty feh picom polybar dunst lightdm lightdm-gtk-greeter wqy-fonts xdg-user-dirs
```

- 使用 Ports 安装：


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
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean
```

说明：


| 包名                  | 作用说明                                                                 |
|:---------------------|:--------------------------------------------------------------------------|
| `xorg`              | X Window 系统（X Window System）          |
| `bspwm`             | 轻量级平铺窗口管理器（Binary Space Partitioning Window Manager）                            |
| `sxhkd`             | 快捷键绑定工具（Simple X Hotkey Daemon）                                    |
| `rofi`              | 程序启动器（Rofi），支持应用启动、窗口切换等功能                                     |
| `kitty`             |终端模拟器（Kitty）                         |
| `feh`               | 桌面背景设置工具（Feh）             |
| `picom`             |窗口合成器（Picom），提供透明、阴影和动画效果   |
| `polybar`           | 面板工具（Polybar），显示系统信息和应用图标等            |
| `dunst`             | 通知管理器（Dunst）  |
| `lightdm`           | LightDM 显示管理器（Light Display Manager），提供图形登录界面             |
| `lightdm-gtk-greeter`| LightDM 的 GTK+ 登录界面插件（LightDM GTK+ Greeter），缺失时将无法启动 LightDM  |
| `wqy-fonts`         | 文泉驿字体（WenQuanYi Fonts）                               |
| `xdg-user-dirs`     | 用户目录管理工具（XDG User Dirs），管理如“桌面”、“下载”等目录          |



>**提示**
>
>由于 Polybar 在 FreeBSD 上功能不完整，建议替换为 `x11/tint`（pkg 包名为 `tint2`），可显示系统托盘图标。



## 启用服务

```sh
# service dbus enable
```

## 创建配置文件

```sh
$ mkdir -p ~/.config
$ mkdir -p ~/.config/bspwm
$ mkdir -p ~/.config/sxhkd
$ cp /usr/local/share/examples/bspwm/bspwmrc ~/.config/bspwm
$ cp /usr/local/share/examples/bspwm/sxhkdrc ~/.config/sxhkd
$ chmod +x ~/.config/bspwm/bspwmrc
```

编辑 `~/.config/sxhkd/sxhkdrc` 文件：

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

然后执行以下命令

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

### 快捷键

按 Windows + 空格：使用 Rofi 启动应用

按 Windows + 回车：启动终端（Kitty）

更多快捷键设置可参考 `~/.config/sxhkd/sxhkdrc` 文件


### 设置桌面背景

- 初次设置

```sh
$ feh --bg-center "$HOME/.local/share/wallpapers/wallpaper.jpg"
```

- 执行一次后自动设置

在 `~/.config/bspwm/bspwmrc` 中的 polybar 启动脚本 **前** 添加

```sh
$HOME/.fehbg &
```

## 展示图片

![](../.gitbook/assets/bspwm.png)

图片中显示的 Chrome 浏览器和 Thunar 文件管理器均需用户自行安装

## 参考文献

- [从零开始的 Bspwm 安装与配置教程](https://zhuanlan.zhihu.com/p/568211941)
