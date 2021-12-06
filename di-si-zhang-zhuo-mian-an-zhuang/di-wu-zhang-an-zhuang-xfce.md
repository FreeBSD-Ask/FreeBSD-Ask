# 第五节 安装 Xfce

## 安装xfce4

通过ports安装

```
# cd /usr/ports/x11-wm/xfce4
# make install clean
```

通过pkg安装 `# pkg install xfce4`

## 启用xfce

`# echo ". /usr/local/etc/xdg/xfce4/xinitrc"> ~/.xinitrc`

或者

`# echo ". /usr/local/etc/xdg/xfce4/xinitrc" > ~/.xsession` 根据条件使用

## 启动服务

```
# syrc dbus_enable="YES"
# service dbus start
```

## 设置中文显示

在.xinitrc添加以下内容（但要在最前面才正常启用） `export LANG=zh_CN.UTF-8`

## 可选配置

`# pkg install zh-fcitx`

#(安装中文输入法，需要设置中文输入环境)

#cd ~

#ee .xinitrc #文件添加以下内容

```
export XMODIFIERS="@im=fcitx"
export XIM_PROGRAM="fcitx"
export GTK_IM_MODULE="fcitx"
fcitx &
```

```
# pkg install firefox #（火狐浏览器）
# pkg install smplayer  #(视频播放器)
# pkg install zh_CN-libreoffice #(办公软件)
# pkg install gimp #(图片处理)
# pkg install thunderbird #(邮件客户端)
# pkg install wqy-fonts #（安装文泉驿字体）
# pkg install transmission  #(BT下载工具)`
```

## 故障排除

### xfce 普通用户关机按钮灰色解决方案

`# chown -R polkitd /usr/local/etc/polkit-1`

即可解决xfce4普通用户关机按钮灰色的问题

### FreeBSD 的xfce 终端动态标题不显示问题

tcsh 配置，home 目录创建.tcshrc,

写入以下配置

```
alias h history 25 alias j jobs -l alias la ls -aF alias lf ls -FA alias ll ls -lAF setenv EDITOR vi setenv PAGER less switch ($TERM) case "xterm*": set prompt="%{033]0;[]%~007%}%#" set filec set history = 1000 set savehist = (1000 merge) set autolist = ambiguous # Use history to aid expansion set autoexpand set autorehash breaksw default: set prompt="%#" breaksw endsw
```
