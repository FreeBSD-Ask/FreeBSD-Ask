# 第五节 桌面与其他软件

## 安装桌面

### 安装 MATE 桌面

登入 root 账号，终端运行 `# pkg_add slim mate mate-utils mate-extras`

打开 `/etc/rc.local`，添加一行 `/usr/local/bin/slim -d` 。

打开 `/etc/rc.conf.local`，添加以下几行：
```
pkg_scripts="dbus_daemon avahi_daemon"
dbus_enable=YES
multicast_host=YES
```
退出 root 账号，以普通账号登录。

打开 `.xinitrc` (没有就新建一个)，添加一行 `exec mate-session`。

全部设置完毕，重启后即可进入 MATE 桌面。

### 安装 XFCE 桌面

终端运行 `# pkg_add slim xfce`

打开 `/etc/rc.local`，添加一行 `/usr/local/bin/slim -d` 。

打开 `/etc/rc.conf.local`，添加以下几行：
```
pkg_scripts="dbus_daemon avahi_daemon"
dbus_enable=YES
multicast_host=YES
```
退出 root 账号，以普通账号登录。

打开 `.xinitrc` (没有就新建一个)，添加一行 `exec startxfce4`。

全部设置完毕，重启后即可进入 XFCE 桌面。

### 安装 Gnome 桌面

待补充。
