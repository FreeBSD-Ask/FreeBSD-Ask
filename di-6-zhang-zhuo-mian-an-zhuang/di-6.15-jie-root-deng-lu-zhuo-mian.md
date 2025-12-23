# 6.15 启用 root 桌面登录

> **警告**
>
> 鉴于部分用户希望 root 登录桌面，本章节予以撰写。请注意 root 账户拥有最高权限，错误使用 root 账户很可能会 ​**破坏系统**​，因此使用其登录图形界面存在 ​**极高的安全风险**​。以下内容请谨慎操作，风险自负，我们不承担任何责任。


## GDM

GDM，即 GNOME Display Manager，GNOME 显示管理器。

打开 `/usr/local/etc/pam.d/gdm-password`，注释掉 `account requisite pam_securetty.so` 这一行（即往最前面加 `#`）

重启 GDM 服务：

```sh
# service gdm restart
```

## LightDM

LightDM，即 Light Display Manager，轻量级显示管理器。

编辑 `/usr/local/etc/pam.d/lightdm`，注释掉 `account requisite pam_securetty.so` 这一行（即往最前面加 `#`）

然后重启 LightDM 服务：

```sh
# service lightdm restart
```

即可。

## SDDM

SDDM 即 Simple Desktop Display Manager，简单的桌面显示管理器。

更改 `/usr/local/etc/pam.d/sddm` 文件：将 `include` 之后的 `login`，替换成 `system`，共计四处。

重启 SDDM 服务：

```sh
# service sddm restart
```

之后即可使用 root 登录 SDDM。


> **警告**
>
> root 账户拥有最高权限，错误使用 root 账户可能 ​**破坏系统**​，因此使用其登录图形界面存在 ​**极高的安全风险**​。
