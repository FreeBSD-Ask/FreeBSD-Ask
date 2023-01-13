# 第4.3节 安装 Gnome

## 安装

```
# pkg install xorg gnome-shell noto-sc xdg-user-dirs
```

>若要精简安装可以将 `gnome` 替换为 `gnome-shell`。
>
>如果安装了完整版本也可以使用 pkg 包管理器卸载多余软件：
>
>```
># pkg delete gnome-2048 gnome-klotski gnome-tetravex gnome-mines gnome-taquin gnome-sudoku gnome-robots gnome-nibbles lightsoff tali quadrapassel swell-foop gnome-mahjongg five-or-more iagno aisleriot four-in-a-row
>```

解释:

|       软件     |       用途      |
| :-----------: | :-----------: |
|      xorg     |      X11      |
|  gnome         |   Gnome 主程序   |
|    noto-sc    |   思源黑体——简体中文   |
| xdg-user-dirs | 用于创建用户家目录的子目录 |

## 配置

`# ee /etc/fstab`

添加内容如下:

```
proc /proc procfs rw 0 0
```

配置启动项：

```
# sysrc dbus_enable="YES"
# sysrc gdm_enable="YES"
# sysrc gnome_enable="YES"
```

输入以下命令：

```
% echo "/usr/local/bin/gnome-session" > ~/.xinitrc
```

## 中文化 

### GNOME界面
> 本小节用户 shell 应该是默认的 `sh`，判断方法见下一小节“安装输入法”（root 用户默认 shell 是 csh，无法适用）。

`# cd /usr/local/etc/gdm && ee locale.conf`

添加以下内容

```
LANG="zh_CN.UTF-8"
LC_CTYPE="zh_CN.UTF-8"
LC_MESSAGES="zh_CN.UTF-8"
LC_ALL="zh_CN.UTF-8"
```

### 中文输入法

以下 `ibus`、`fcitx5` 二选一即可。

#### ibus

gnome 捆绑的输入法面板是 `ibus`。

`# pkg install zh-ibus-libpinyin`（安装好运行初始化命令 `ibus-setup`）

#### fcitx 5

首先看看现在自己的 shell 是不是 `sh`,`bash`,`zsh`：

`# echo $0`

如果是 `sh`,`bash`,`zsh` 其中之一，请继续；如果不是，请参考第五章第一节。

安装 `fcitx5`:

```
# pkg install fcitx5 fcitx5-qt fcitx5-gtk fcitx5-configtool zh-fcitx5-chinese-addons
```

打开或新建文件 `~/.xprofile`，写入:

```
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
```

参考：以下是该文件的一个示例：

```
# $FreeBSD$
#
# .profile - Bourne Shell startup script for login shells
#
# see also sh(1), environ(7).
#

# These are normally set through /etc/login.conf.  You may override them here
# if wanted.
# PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin:$HOME/bin; export PATH

# Setting TERM is normally done through /etc/ttys.  Do only override
# if you're sure that you'll never log in via telnet or xterm or a
# serial line.
# TERM=xterm; 	export TERM

EDITOR=vi;   	export EDITOR
PAGER=less;  	export PAGER

# set ENV to a file invoked each time sh is started for interactive use.
ENV=$HOME/.shrc; export ENV

# Let sh(1) know it's at home, despite /home being a symlink.
if [ "$PWD" != "$HOME" ] && [ "$PWD" -ef "$HOME" ] ; then cd ; fi

# Query terminal size; useful for serial lines.
if [ -x /usr/bin/resizewin ] ; then /usr/bin/resizewin -z ; fi

# Display a random cookie on each login.
if [ -x /usr/bin/fortune ] ; then /usr/bin/fortune freebsd-tips ; fi

export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
```

提示：如果要显示 `fcitx` 输入法面板，需要安装 gnome 插件 `TopIconsFix`,请勿安装 `AppIndicator and KStatusNotifierItem Support`，已知该插件与 `fcitx5` 相冲突，会造成输入法卡死。

该插件需要通过火狐浏览器进行安装：

```
# pkg install -y firefox chrome-gnome-shell
```

打开链接 `https://extensions.gnome.org/extension/1674/topiconsfix/` 即可安装插件。

### 终端显示中文（文件用户根目录）

`# ee .cshrc`

添加以下内容

```
setenv LANG zh_CN.UTF-8
setenv LC_CTYPE zh_CN.UTF-8
setenv LC_ALL zh_CN.UTF-8
```

## 优化系统

`# pkg install gnome-tweaks`
