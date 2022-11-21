# 第七节 安装 Lumina

## 安装

```
# pkg install lumina xorg  lightdm lightdm-gtk-greeter wqy-fonts 
```

## 配置

```
# sysrc dbus_enable="YES"
# sysrc lightdm_enable="YES"
```

```
# ee ~/.xinitrc
```

添加：

```
exec lumina-desktop
```

## 中文化

>设置完毕还是英语。原因未知，如果你知道，请提交 issue 或者 pull request。

Desktop Settings ——> Localization ——> 全部调整为“简体中文”，然后“save”，退出登录，重启系统。操作无效。
