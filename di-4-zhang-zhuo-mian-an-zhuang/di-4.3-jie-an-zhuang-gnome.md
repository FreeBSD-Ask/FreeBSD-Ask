# 第 4.3 节 安装 Gnome

> 当前 gnome 桌面对 dri3 的支持有问题，见 [Bug 255049 - x11/gdm doesn't show the login screen ](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=255049)、[amdgpu no hw acceleration on gnome3 ?? - workaround amdgpu disable DRI3 in xorg.conf and switch to DRI2](https://github.com/freebsd/drm-kmod/issues/72)。可能会导致部分 AMD GPU 显示错误，必须降级到 dri2 才能运行。
## 安装

```sh
# pkg install xorg gnome noto-sc xdg-user-dirs
```

或者

```
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11/gnome/ && make install clean
# cd /usr/ports/x11-fonts/noto-serif-sc/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean
```

解释:

|     软件      |            用途            |
| :-----------: | :------------------------: |
|     xorg      |            X11             |
|     gnome     |        Gnome 主程序        |
|    noto-sc    |     思源黑体——简体中文     |
| xdg-user-dirs | 用于创建用户家目录的子目录 |

> **精简安装（如果不嫌麻烦）**
>
> ```sh
> # pkg install xorg-minimal gnome-lite wqy-fonts xdg-user-dirs
> ```
>或者

```sh
# cd /usr/ports/x11/xorg-minimal/ && make install clean
# cd /usr/ports/x11/gnome/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean
```
> 如果安装了完整版本也可以使用 pkg 包管理器卸载自带的游戏软件：
>
> ```sh
> # pkg delete gnome-2048 gnome-klotski gnome-tetravex gnome-mines gnome-taquin gnome-sudoku gnome-robots gnome-nibbles lightsoff tali quadrapassel swell-foop gnome-mahjongg five-or-more iagno aisleriot four-in-a-row
> ```

## 配置

```sh
# ee /etc/fstab
```

添加内容如下:

```sh
proc /proc procfs rw 0 0
```

配置启动项：

```sh
# sysrc dbus_enable="YES"
# sysrc gdm_enable="YES"
```

输入以下命令：

```sh
$ echo "/usr/local/bin/gnome-session" > ~/.xinitrc
```

## 中文化

### GNOME 界面

> 本小节配置参数与用户 shell 无关，即使是 csh 也该如此配置。

```sh
# ee /usr/local/etc/gdm/locale.conf
```

添加以下内容：

```sh
LANG="zh_CN.UTF-8"
LC_CTYPE="zh_CN.UTF-8"
LC_MESSAGES="zh_CN.UTF-8"
LC_ALL="zh_CN.UTF-8"
```

### 中文输入法

以下 `ibus`、`fcitx5` 二选一即可。

#### ibus

gnome 捆绑的输入法面板是 `ibus`。

```sh
# pkg install zh-ibus-libpinyin
```

或者

```sh
# cd /usr/ports/chinese/ibus-libpinyin/
# make install clean
```

安装后运行初始化命令 `ibus-setup`.

#### fcitx 5

首先看看现在自己的 shell 是不是 `sh`,`bash`,`zsh`：

```sh
# echo $0
```

如果是 `sh`,`bash`,`zsh` 其中之一，请继续；如果不是，请参考第五章第一节。

安装 `fcitx5`:

```sh
# pkg install fcitx5 fcitx5-qt5 fcitx5-qt6 fcitx5-gtk2 fcitx5-gtk3 fcitx5-gtk4 fcitx5-configtool zh-fcitx5-chinese-addons
```

或者：

```sh
# cd /usr/ports/textproc/fcitx5/ && make install clean
# cd /usr/ports/textproc/fcitx5-qt/ && make install clean #同时包含 QT 5 和 QT 6
# cd /usr/ports/textproc/fcitx5-gtk/ && make install clean #同时包含 gtk 2、3、4
# cd /usr/ports/textproc/fcitx5-configtool/ && make install clean
# cd /usr/ports/chinese/fcitx5-chinese-addons/ && make install clean
```

打开或新建文件 `~/.xprofile`，写入:

```sh
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
```

参考：以下是该文件的一个示例：

```sh
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

```sh
# pkg install firefox chrome-gnome-shell
```

或者：

```sh
# cd /usr/ports/www/firefox/ && make install clean
# cd /usr/ports/www/chrome-gnome-shell/ && make install clean
```

打开链接 <https://extensions.gnome.org/extension/1674/topiconsfix/> 即可安装插件。

### 终端显示中文（文件用户根目录）

> 此处对用户 shell 存疑。

```sh
# ee ~/.cshrc
```

添加以下内容

```sh
setenv LANG zh_CN.UTF-8
setenv LC_CTYPE zh_CN.UTF-8
setenv LC_ALL zh_CN.UTF-8
```

## 优化系统

```sh
# pkg install gnome-tweaks
```
或者：

```sh
# cd /usr/ports/deskutils/gnome-tweaks/ 
# make install clean
```
