# 第4.5节 安装 Xfce

## 安装 xfce4

> 以下教程适用于 shell 为 bash/sh/zsh 的用户。
>
> 首先看看现在自己的 shell 是不是 `sh`,`bash`,`zsh`：
>
> `# echo $0`
>
> 如果是 `sh`,`bash`,`zsh` 其中之一，请继续；

通过 pkg 安装

```
# pkg install xorg lightdm lightdm-gtk-greeter xfce wqy-fonts xdg-user-dirs	
```

或

通过 ports 安装

```
# cd /usr/ports/x11-wm/xfce4
# make install clean
```

## 启用 xfce

`# echo "/usr/local/etc/xdg/xfce4/xinitrc" > ~/.xinitrc`

或者

`# echo "/usr/local/etc/xdg/xfce4/xinitrc" > ~/.xsession`

> 此处为 root 用户，普通用户需要再在自己的环境下操作一次。下同。

根据条件使用

## 启动服务

```
# sysrc dbus_enable="YES"
# sysrc lightdm_enable="YES"
```

## 设置中文显示

在 `.xinitrc` 或者 `.profile` 中添加以下内容（但要在最前面才正常启用） `export LANG=zh_CN.UTF-8`

## 可选配置

### 安装输入法

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
# ee ~/.xinitrc 
```

在该文件中添加以下内容:

```
export XMODIFIERS="@im=fcitx"
export XIM_PROGRAM="fcitx"
export GTK_IM_MODULE="fcitx"
fcitx &
```

## 全局菜单（可选）

```
# pkg install xfce4-appmenu-plugin appmenu-gtk-module appmenu-registrar
$ xfconf-query -c xsettings -p /Gtk/ShellShowsMenubar -n -t bool -s true
$ xfconf-query -c xsettings -p /Gtk/ShellShowsAppmenu -n -t bool -s true
$ xfconf-query -c xsettings -p /Gtk/Modules -n -t string -s "appmenu-gtk-module"
```

## 故障排除

### FreeBSD 的 xfce 终端动态标题不显示问题

tcsh 配置:

`home` 目录创建 `.tcshrc`,

写入以下配置

`alias h history 25 alias j jobs -l alias la ls -aF alias lf ls -FA alias ll ls -lAF setenv EDITOR vi setenv PAGER less switch ($TERM) case "xterm*": set prompt="%{033]0;[]%~007%}%#" set filec set history = 1000 set savehist = (1000 merge) set autolist = ambiguous # Use history to aid expansion set autoexpand set autorehash breaksw default: set prompt="%#" breaksw endsw`

## 配置集参考

* [https://github.com/Wamphyre/BSD-XFCE](https://github.com/Wamphyre/BSD-XFCE)
