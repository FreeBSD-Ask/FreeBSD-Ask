# 第 4.5 节 Xfce

Xfce 旨在开发一款轻量级但功能齐全的桌面。Xfce 的 Logo 是只[老鼠🐀](https://docs.xfce.org/faq#what_does_it_mean)，曾有人反馈 bug 称因 Xfce 屏幕壁纸是只老鼠🐀导致自己的电脑屏幕被猫🐈抓坏了（[\[joke\] The default desktop startup screen causes damage to monitor!](https://bugzilla.xfce.org/show_bug.cgi?id=12117)）。

## 安装 xfce4

- 通过 pkg 安装

```sh
# pkg install xorg lightdm lightdm-gtk-greeter xfce wqy-fonts xdg-user-dirs xfce4-goodies lightdm-gtk-greeter-settings
```

- 或通过 ports 安装

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11-wm/xfce4 && make install clean # 注意有个 4
# cd /usr/ports/x11/xfce4-goodies/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/x11/lightdm/ && make install clean
# cd /usr/ports/x11/lightdm-gtk-greeter/ && make install clean
# cd /usr/ports/x11/lightdm-gtk-greeter-settings/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
# cd /usr/ports/x11/xfce4-goodies/ && make install clean
```

- 解释

| 包名                          | 作用说明                               |
|:-------------------------------|:------------------------------------|
| `xorg`                        |  X Window 系统|
| `lightdm`                     | 轻量级显示管理器 LightDM |
| `lightdm-gtk-greeter`         | LightDM 的 GTK+ 登录界面插件|
| `xfce`                        | Xfce 桌面环境 |
| `wqy-fonts`                   | 文泉驿中文字体|
| `xdg-user-dirs`               | 管理用户主目录 |
| `xfce4-goodies`               | XFCE 的附加组件和插件集合 |
| `lightdm-gtk-greeter-settings`| 配置 LightDM GTK+ 登录界面的图形工具，缺少将无法启动 |


## `startx`

```sh
$ echo "/usr/local/etc/xdg/xfce4/xinitrc" > ~/.xinitrc
```

或者

```sh
$ echo "/usr/local/etc/xdg/xfce4/xinitrc" > ~/.xsession
```


## 启动服务

```sh
# service dbus enable
# service lightdm enable
```

## 设置中文界面

编辑 `/etc/login.conf`：找到 `default:\` 这一段，把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：

```sh
# cap_mkdb /etc/login.conf
```

## 图片欣赏

![FreeBSD 安装 Xfce](../.gitbook/assets/xfce1.png)

![FreeBSD 安装 Xfce](../.gitbook/assets/xfce2.png)

![FreeBSD 安装 Xfce](../.gitbook/assets/xfce3.png)

## 全局菜单（可选）

安装：

```sh
# pkg install xfce4-appmenu-plugin appmenu-gtk-module appmenu-registrar
```

或：

```sh
# cd /usr/ports/x11/xfce4-appmenu-plugin/ && make install clean
# cd /usr/ports/x11/gtk-app-menu/ && make install clean
# cd /usr/ports/x11/appmenu-registrar/ && make install clean
```

查看安装后说明，安装说明配置：

```sh
$ xfconf-query -c xsettings -p /Gtk/ShellShowsMenubar -n -t bool -s true
$ xfconf-query -c xsettings -p /Gtk/ShellShowsAppmenu -n -t bool -s true
$ xfconf-query -c xsettings -p /Gtk/Modules -n -t string -s "appmenu-gtk-module"
```

## 软件推荐

FreeBSD 的 xfce 邮箱客户端推荐用 `mail/evolution`，可搭配 `xfce4-mailwatch-plugin`、`security/gnome-keyring` 一道使用。

还有一款桌面插件，叫 `x11/xfce4-verve-plugin`。配合设置智能书签，可以查网页内容。可通过设置 FreeBSD 的 man 手册，就可以搜索需要的内容。


## XTerm 终端动态标题


- sh: `~/.profile` 写入配置
- bash: `~/.bash_profile` 或 `~/.profile` 写入配置
- zsh: `~/.zprofile` 写入配置
- csh: `~/.cshrc` 写入配置
- tcsh: `~/.tcshrc` 写入配置


### sh

```sh
if [ -t 1 ]; then            # 确保是交互式
  while :; do
    # 1) 命令空闲时：标题显示当前路径
    printf '\033]0;%s\007' "$PWD"    # ESC ]0;… BEL  设置 xterm 标题:contentReference[oaicite:4]{index=4}
    # 显示提示
    printf '\n$ '
    # 2) 读取用户输入
    if ! IFS= read -r cmd; then
      break
    fi
    # 3) 命令执行前：标题显示将要执行的命令
    printf '\033]0;%s\007' "$cmd"
    # 4) 执行命令
    eval "$cmd"
  done
  exit
fi
```


### zsh

```sh
precmd ()   a function which is executed just before each prompt
chpwd ()    a function which is executed whenever the directory is changed
\e          escape sequence for escape (ESC)
\a          escape sequence for bell (BEL)
%n          expands to $USERNAME
%m          expands to hostname up to first '.'
%~          expands to directory, replacing $HOME with '~'
```

### tcsh

```sh
precmd ()   a function which is executed just before each prompt
cwdcmd ()   a function which is executed whenever the directory is changed
%n          expands to username
%m          expands to hostname
%~          expands to directory, replacing $HOME with '~'
%#          expands to '>' for normal users, '#' for root users
%{...%}     includes a string as a literal escape sequence
```

### bash

```sh
\u          expands to $USERNAME
\h          expands to hostname up to first '.'
\w          expands to directory, replacing $HOME with '~'
\$          expands to '$' for normal users, '#' for root
\[...\]     embeds a sequence of non-printing characters
```

### csh

```sh
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

### 参考文献

- [Xterm-Title](http://www.faqs.org/docs/Linux-mini/Xterm-Title.html#ss4.1)

## 配置集参考

- [Wamphyre/BSD-XFCE](https://github.com/Wamphyre/BSD-XFCE)


## 故障排除与未竟事宜

动态标题 csh 和 tcsh 应该是一样的，故应该只需要保留一个，待测试。

