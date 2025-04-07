# 第 4.18 节 root 登录桌面

> **警告**
>
> 鉴于部分用户希望 root 登录桌面，为贯彻自由精神撰写本章节。请注意 root 账户拥有最高权限，失误使用 root 账户很可能会**破坏系统**，因此用其登录图形界面存在**极高的安全风险**。以下内容请谨慎操作，风险自负。我们不承担任何责任。

## GDM（GNOME 显示管理器）

打开 `/usr/local/etc/pam.d/gdm-password`，注释掉 `account requisite pam_securetty.so` 这一行（即往最前面加 `#`）

重启服务

```sh
# service gdm restart
```

## lightdm

然后修改配置文件：

- 编辑 `/usr/local/etc/lightdm/lightdm.conf`：

往下拉，找到 `greeter-show-manual-login=true` 移除前面的 `#`。该行会多次出现，第一次出现是为你介绍用法，请勿修改！而应该继续往下拉。

- 编辑 `/usr/local/etc/pam.d/lightdm`：

注释掉 `account requisite pam_securetty.so` 这一行（即往最前面加 `#`）

重启服务

```sh
# service lightdm restart
```

即可。

## sddm

更改 `/usr/local/etc/pam.d/sddm` 文件：把 `include` 之后的 `login`，替换成 `system`。一共有 4 处需要替换。

重启服务

```sh
# service sddm restart
```

之后就可以 root 登录 sddm 了！

### 故障排除与未竟事宜

sddm 左下角选项不能为 `Wayland`，否则可能进不去，你可以试试 `Plasma-x11`

> **警告**
>
> root 账户拥有最高权限，失误使用 root 账户可能**破坏系统**，因此用其登录图形界面存在**极高的安全风险**。
