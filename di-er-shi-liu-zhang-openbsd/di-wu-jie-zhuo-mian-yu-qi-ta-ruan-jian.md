# 第五节 桌面与其他软件

## MATE 桌面

### 安装

登入 `root` 账号，终端运行 `# pkg_add mate mate-utils mate-extras`

打开 `/etc/rc.conf.local`，添加以下几行：

```
pkg_scripts=messagebus avahi_daemon
apmd_flags=-A
multicast=YES
```

终端输入`# pkg_add noto-cjk noto-emoji`，安装中文字体。
 
退出 root 账号，以普通账号登录。

打开 `.xinitrc` (没有就新建一个)，添加一行 `exec mate-session`。

全部设置完毕，重启后即可进入 MATE 桌面。

### 安装输入法

`#pkg_add fcitx fcitx-configtool zh-libpinyin`


### 中文界面：

打开用户目录下的 `.profile` 文件，添加以下文本：

```
export LANG="zh_CN.UTF-8"

export XIM_PROGRAM=fcitx
export XIM=fcitx
export XMODIFIERS="@im=fcitx"
export QT_IM_MODULE=XIM
export GTK_IM_MODULE=XIM
```

## XFCE 桌面

### 安装

终端运行 `# pkg_add xfce xfces-extras`

打开 `/etc/rc.conf.local`，添加以下几行：

```
pkg_scripts=messagebus avahi_daemon
apmd_flags=-A
multicast=YES
```

终端输入`# pkg_add noto-cjk noto-emoji`，安装中文字体。
 
退出 `root` 账号，以普通账号登录。

打开 `.xinitrc` (没有就新建一个)，添加一行 `exec startxfce4`。

全部设置完毕，重启后即可进入 XFCE 桌面。

### 输入法

`#pkg_add fcitx fcitx-configtool zh-libpinyin`


### 中文界面：

打开用户目录下的 `.profile` 文件，添加以下文本：

```
export LANG="zh_CN.UTF-8"

export XIM_PROGRAM=fcitx
export XIM=fcitx
export XMODIFIERS="@im=fcitx"
export QT_IM_MODULE=XIM
export GTK_IM_MODULE=XIM
```

##  Gnome 桌面

### 安装

打开终端，输入 `# pkg_add gnome gnome-extras`。

然后打开终端，运行以下几条命令：

`#usermod -L gnome 用户名`，`#rcctl disable xenodm`，`#rcctl enable messagebus avahi_daemon gdm`。最后重启系统，即可登入 Gnome 桌面。

 ### 中文字体
 
 `# pkg_add noto-cjk noto-emoji`

### 中文界面

终端打开`/etc/gdm/locale.conf`, 修改文本为以下内容：

```
LC_CTYPE="zh_CN.UTF-8"
LC_MESSAGES="zh_CN.UTF-8"
```

重启后，即可进入中文界面。

## 主题和图标

以下仅举两个实例，[Qogir](https://www.gnome-look.org/p/1230631/) 主题、和 [Tela](https://www.gnome-look.org/p/1279924/) 图标，
大家可访问 [相关网站](https://www.gnome-look.org/)，自行选择喜欢的主题和图标来安装。

### 提前准备

终端运行 `#pkg_add git bash`。


### 主题安装

`git clone https://github.com/vinceliuice/Qogir-theme && cd Qogir-theme`

`vi .install.sh`，修改文件中的第一行 **shebang** 为 `#!/usr/local/bin/bash`
 
之后 `bash ./install.sh`

### 图标安装

`git clone https://github.com/vinceliuice/Tela-icon-theme && cd Tela-icon-theme`

`vi .install.sh`，修改文件中的第一行 **shebang** 为 `#!/usr/local/bin/bash`

之后 `bash ./install.sh`

