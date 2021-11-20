# 第四节 安装 Mate 桌面

FreeBSD 安装mate 桌面环境

## 安装开始（主要程序）

`pkg install -y mate xorg`

在文件/etc/rc.conf 中加入下面的行
```
moused\_enable=”YES”\
dbus\_enable=”YES”\
hald\_enable=”YES”
```

## 安装 Slim 作为登陆管理器

`pkg install -y slim`

在/etc/rc.conf 中加入下面的行：

slim\_enable=”YES”

在主目录.xinitrc 文件内加入下面的行:

`exec mate-session`

## 显示中文桌面环境

默认是csh，在.cshrc 中添加如下内容：\
```
setenv LANG zh\_CN.UTF-8\
setenv LC\_CTYPE zh\_CN.UTF-8
```

## 安装输入法

`pkg install zh-ibus-libpinyin`（安装好运行初始化命令ibus-setup）\
设置输入法变量\
ee .xinitrc\
文件添加以下内容\
```
export GTK\_IM\_MODULE=ibus\
export XMODIFIERS=@im=ibus\
export QT\_IM\_MODULE=ibus\
ibus &
```

## 安装软件/安装字体
```
pkg install -y noto-sc zh-sourcehanserif-sc-otf\
pkg install -y firefox\
pkg install -y networkmgr\
pkg install -y zh\_CN-libreoffice
```
