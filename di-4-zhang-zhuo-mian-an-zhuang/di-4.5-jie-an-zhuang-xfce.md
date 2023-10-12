# 第 4.5 节 安装 Xfce

## 安装 xfce4

通过 pkg 安装

```shell-session
# pkg install xorg lightdm lightdm-gtk-greeter xfce wqy-fonts xdg-user-dirs
```

或

通过 ports 安装

```shell-session
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

```shell-session
# sysrc dbus_enable="YES"
# sysrc lightdm_enable="YES"
```

## 设置中文显示

在 `.xinitrc` 或者 `.profile` 中添加以下内容（但要在最前面才正常启用） `export LANG=zh_CN.UTF-8`

lightdm 登陆管理器本地化语言见 KDE 章节。
## 可选配置


## 全局菜单（可选）

```shell-session
# pkg install xfce4-appmenu-plugin appmenu-gtk-module appmenu-registrar
$ xfconf-query -c xsettings -p /Gtk/ShellShowsMenubar -n -t bool -s true
$ xfconf-query -c xsettings -p /Gtk/ShellShowsAppmenu -n -t bool -s true
$ xfconf-query -c xsettings -p /Gtk/Modules -n -t string -s "appmenu-gtk-module"
```

## 故障排除

### FreeBSD 的 xfce 终端动态标题不显示问题


 - sh: `~/.profile` 写入配置
 - bash: `~/.bash_profile` 或 `~/.profile` 写入配置
 - zsh: `~/.zprofile` 写入配置
 - csh: `~/.cshrc` 写入配置
 - tcsh: `~/.tcshrc` 写入配置

zsh:

```shell-session
precmd ()   a function which is executed just before each prompt
chpwd ()    a function which is executed whenever the directory is changed
\e          escape sequence for escape (ESC)
\a          escape sequence for bell (BEL)
%n          expands to $USERNAME
%m          expands to hostname up to first '.'
%~          expands to directory, replacing $HOME with '~'
```

tcsh:

```shell-session
precmd ()   a function which is executed just before each prompt
cwdcmd ()   a function which is executed whenever the directory is changed
%n          expands to username
%m          expands to hostname
%~          expands to directory, replacing $HOME with '~'
%#          expands to '>' for normal users, '#' for root users
%{...%}     includes a string as a literal escape sequence
```

bash:
```shell-session
\u          expands to $USERNAME
\h          expands to hostname up to first '.'
\w          expands to directory, replacing $HOME with '~'
\$          expands to '$' for normal users, '#' for root
\[...\]     embeds a sequence of non-printing characters
```

csh
```shell-session
switch ($TERM)
    case "xterm*":
        set host=`hostname`
        alias cd 'cd \!*; echo -n "^[]0;${user}@${host}: ${cwd}^Gcsh% "'
        breaksw
    default:
        set prompt='csh% '
        breaksw
endsw
```

参考文献： 

 - [Xterm-Title](http://www.faqs.org/docs/Linux-mini/Xterm-Title.html#ss4.1)



## 配置集参考

- [Wamphyre/BSD-XFCE](https://github.com/Wamphyre/BSD-XFCE)



## lightdm 登陆管理器本地化语言

### 方法①

`/etc/rc.conf` 里写入：

```
lightdm_env="LC_MESSAGES=zh_CN.UTF-8" 
```

###  方法②

修改 `slick-greeter.desktop`：

编辑 `/usr/local/share/xgreeters/slick-greeter.desktop`：

`Exec=slick-greeter` 改成 `Exec=env LANGUAGE=zh_CN slick-greeter` 保存，重启 `lightdm` 服务就生效:


```shell-session
# service lightdm restart
```

