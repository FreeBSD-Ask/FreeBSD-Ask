# 第五节 安装 Xfce

## 安装 xfce4

通过 pkg 安装

```
# pkg install xorg lightdm lightdm-gtk-greeter xfce
```

或

通过 ports 安装

```
# cd /usr/ports/x11-wm/xfce4
# make install clean
```

## 启用 xfce

`# echo "./usr/local/etc/xdg/xfce4/xinitrc"  >  ~/.xinitrc`

或者

`# echo "./usr/local/etc/xdg/xfce4/xinitrc"  >  ~/.xsession` 

根据条件使用

## 启动服务

```
# sysrc dbus_enable="YES"
# sysrc lightdm_enable="YES"
```

## 设置中文显示

在`.xinitrc`添加以下内容（但要在最前面才正常启用） `export LANG=zh_CN.UTF-8`

## 可选配置

### 输入法

请检查自己的shell是不是 `sh`、`bash`、`zsh` 其中之一。

```
# echo $0
```

如果是以上三个 SHELL 之一，请继续，如果不是请参考第五章第一节：

```
# pkg install zh-fcitx zh-fcitx-configtool fcitx-qt5 fcitx-m17n zh-fcitx-libpinyin
```

配置文件：

```
#ee ~/.xinitrc 
```

在该文件中添加以下内容:

```
export XMODIFIERS="@im=fcitx"
export XIM_PROGRAM="fcitx"
export GTK_IM_MODULE="fcitx"
fcitx &
```

### 其他软件

```
# pkg install firefox #（火狐浏览器）
# pkg install smplayer  #(视频播放器)
# pkg install zh_CN-libreoffice #(办公软件)
# pkg install gimp #(图片处理)
# pkg install thunderbird #(邮件客户端)
# pkg install wqy-fonts #（安装文泉驿字体）
# pkg install transmission  #(BT下载工具)`
```

## 全局菜单（可选）

```
# pkg install xfce4-appmenu-plugin appmenu-gtk-module appmenu-registrar
$ xfconf-query -c xsettings -p /Gtk/ShellShowsMenubar -n -t bool -s true
$ xfconf-query -c xsettings -p /Gtk/ShellShowsAppmenu -n -t bool -s true
$ xfconf-query -c xsettings -p /Gtk/Modules -n -t string -s "appmenu-gtk-module"
```

## 故障排除

### xfce 普通用户关机按钮灰色解决方案

`# chown -R polkitd /usr/local/etc/polkit-1`

即可解决 xfce4 普通用户关机按钮灰色的问题

### FreeBSD 的 xfce 终端动态标题不显示问题

tcsh 配置:

`home`目录创建`.tcshrc`,

写入以下配置

`alias h history 25 alias j jobs -l alias la ls -aF alias lf ls -FA alias ll ls -lAF setenv EDITOR vi setenv PAGER less switch ($TERM) case "xterm*": set prompt="%{033]0;[]%~007%}%#" set filec set history = 1000 set savehist = (1000 merge) set autolist = ambiguous # Use history to aid expansion set autoexpand set autorehash breaksw default: set prompt="%#" breaksw endsw`
