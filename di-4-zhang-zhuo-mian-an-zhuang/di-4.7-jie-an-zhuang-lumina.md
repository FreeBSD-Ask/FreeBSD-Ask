# 第 4.7 节 安装 Lumina

提示：该桌面可能已经停止开发，我向其提交的 pull 长期无人处理，并且没有新的 commit 信息。

## 安装

```shell-session
# pkg install lumina xorg  lightdm lightdm-gtk-greeter wqy-fonts xdg-user-dirs
```

## 配置

```shell-session
# sysrc dbus_enable="YES"
# sysrc lightdm_enable="YES"
```

```shell-session
# ee ~/.xinitrc
```

添加：

```shell-session
exec lumina-desktop
```

## 中文化

> 设置完毕还是英语。原因未知，如果你知道，请提交 issue 或者 pull request。

Desktop Settings ——> Localization ——> 全部调整为“简体中文”，然后“save”，退出登录，重启系统。操作无效。
