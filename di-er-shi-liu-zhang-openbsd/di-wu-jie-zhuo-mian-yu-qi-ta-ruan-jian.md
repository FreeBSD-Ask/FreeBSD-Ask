# 第五节 桌面与其他软件

## 安装桌面

### 安装 MATE 桌面

登入 `root` 账号，终端运行 `# pkg_add slim slim-themes elementary-dock mate mate-utils mate-extras`

打开 `/etc/rc.local`，添加一行 `/usr/local/bin/slim -d` 。

打开 `/etc/rc.conf.local`，添加以下几行：

```
pkg_scripts="dbus_daemon messagebus"
apmd_flags=-A
multicast_host=YES
```

退出 root 账号，以普通账号登录。

打开 `.xinitrc` (没有就新建一个)，添加一行 `exec mate-session`。

全部设置完毕，重启后即可进入 MATE 桌面。

### 安装 XFCE 桌面

终端运行 `# pkg_add slim slim-themes xfce`

打开 `/etc/rc.local`，添加一行 `/usr/local/bin/slim -d` 。

打开 `/etc/rc.conf.local`，添加以下几行：

```
pkg_scripts="dbus_daemon messagebus"
apmd_flags=-A
multicast_host=YES
```

退出 `root` 账号，以普通账号登录。

打开 `.xinitrc` (没有就新建一个)，添加一行 `exec startxfce4`。

全部设置完毕，重启后即可进入 XFCE 桌面。

### Slim 修改主题

注：本节仅涉及 MATE/XFCE ，Gnome 有自己的显示管理器（GDM）。

Slim 的主题文件位于 `/usr/local/share/slim/themes/` 文件夹内，大家可以自己选择喜欢的主题。
这里我们以 `flower2` 主题为例，打开 `/etc/slim.conf`，找到含有 `current_theme` 的一行，将 `default` 改为 `flower2`，保存后即可。

### 安装 Gnome 桌面

打开终端，输入 `# pkg_add gnome gnome-extras`，Gnome 桌面会默认安装 GDM ，因此不需要额外安装显示管理器。

然后打开 `/etc/rc.conf.local`，添加以下几行：
```
multicast_host=YES
pkg_scripts="messagebus dbus_daemon avahi_daemon gdm"
```

最后打开用户账号下的 `.xinitrc` ，添加一行`exec gnome-session`。

## 中文设置

### 安装字体

`#pkg_add noto-cjk noto-emoji`

### 安装输入法

`#pkg_add fcitx fcitx-configtool zh-libpinyin`

### 设置中文

打开用户目录下的 `.profile` 文件 ，添加以下文本：

```
export LANG="zh_CN.UTF-8"
export LC_CTYPE="zh_CN.UTF-8"               
export LC_COLLATE="zh_CN.UTF-8"               
export LC_TIME="zh_CN.UTF-8"                
export LC_NUMERIC="zh_CN.UTF-8"               
export LC_MONETARY="zh_CN.UTF-8"        
export LC_MESSAGES="zh_CN.UTF-8"       
export LC_ALL="zh_CN.UTF-8"

export XIM_PROGRAM=fcitx
export XIM=fcitx
export XMODIFIERS="@im=fcitx"
export QT_IM_MODULE=XIM
export GTK_IM_MODULE=XIM
```
重启后，界面变为中文，Fcitx 输入法亦可正常运行。

## 主题和图标

以下仅举两个实例，[Qogir](https://www.gnome-look.org/p/1230631/) 主题、和 [Tela](https://www.gnome-look.org/p/1279924/) 图标，
大家可访问[相关网站](https://www.gnome-look.org/)，自行选择喜欢的主题和图标来安装。

### 提前准备

终端运行 `#pkg_add git bash`。


### 主题安装

`git clone https://github.com/vinceliuice/Qogir-theme && cd Qogir-theme`

`vi .install.sh`，修改文件中的第一行**shebang** 为 `#!/usr/local/bin/bash`
 
之后`bash ./install.sh`

### 图标安装

`git clone https://github.com/vinceliuice/Tela-icon-theme && cd Tela-icon-theme`

`vi .install.sh`，修改文件中的第一行**shebang** 为 `#!/usr/local/bin/bash`

之后`bash ./install.sh`

