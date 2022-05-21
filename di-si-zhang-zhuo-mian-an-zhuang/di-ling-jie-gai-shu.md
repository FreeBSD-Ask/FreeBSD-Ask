# 第〇节 概述

> 所有 FreeBSD 安装介质默认均不包含图形界面，需要手动安装。**请勿使用`sysutils/desktop-installer`，会引发不必要的错误和问题。**
> 执着于一定要让 FreeBSD 表现出如 Linux 甚至是 Windows 一般的桌面力是一种奢求，FreeBSD 的口号是 `The power to serve`。


本章内容并非是让大家把所有的桌面都安装一遍，而是尽可能多地提供选择。

安装桌面的基本步骤是：① 安装显卡驱动 -> ② 安装 Xorg/Wayland -> ③ 安装 KDE5/Gnome/XFCE/MATE -> ④ 安装显示管理器 sddm/lightdm/slim -> ⑤ 安装输入法等软件

其中，Gnome 可省略第四步，因为其显示管理器 gdm 早就在第二步就进行了安装。

目前支持 Wayland 的桌面为 0。

显示管理器推荐搭配是 ：

KDE5 + sddm

Xfce/Mate + lightdm

Slim 由于作者早在 2013 年就停止了开发，不推荐使用，会产生一些奇怪的 bug （比如 fcitx5 用不了，加载不了 dbus）。

输入法框架目前推荐使用 fcitx（对于 KDE 5 桌面）、ibus（对于其他基于 GTK 的桌面，如 gnome、xfce、mate……）。请勿使用 scim，作者早就跑路（大概已经距今 16 年了）。对于不同的 SHELL，环境变量的配置方法是不一样的，FreeBSD 默认使用 `csh`，而且不同桌面加载环境变量的方法也是不一样的，所以针对不同桌面，不同 SHELL 的配置方法是不一样的，具体方法请看具体桌面。
