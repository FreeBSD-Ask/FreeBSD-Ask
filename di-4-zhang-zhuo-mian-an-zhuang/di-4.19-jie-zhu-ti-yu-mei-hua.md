# 第 4.19 节 主题美化

FreeBSD 安装桌面环境后，很多时候扑面而来的，是简单朴素的色调。这种未加修饰的设定，可能一时会让新用户无法接受。为了系统的美观，我们将在本节尝试添加 **主题** 和 **图标**。

>**注意**
>
>本节仅涉及了 `GTK` 库的桌面主题，囊括了 `Gnome`、`XFCE`、`MATE`、`Cinnamon` 和 `LXDE` 等桌面环境。

以下仅收录了部分图标和主题，想要获取更多资源，可访问 [FreshPorts](https://www.freshports.org)。

## 主题

- matcha 主题： `# pkg install matcha-gtk-themes`
- Qogir 主题： `# pkg install qogir-gtk-themes`
- Pop 主题：`# pkg install pop-gtk-themes`
- Flat 主题：`# pkg install flat-remix-gtk-themes`
- Numix 主题： `# pkg install numix-gtk-theme`
- Sierra 主题：`# pkg install sierra-gtk-themes`
- Yaru 主题： `# pkg install yaru-gtk-themes`
- Canta 主题：`# pkg install canta-gtk-themes`

## 图标

- papirus 图标： `# pkg install papirus-icon-theme`
- Qogir 图标： `# pkg install qogir-icon-themes`
- Pop 图标： `# pkg install pop-icon-theme`
- Flat 图标：`# pkg install flat-remix-icon-themes`
- Numix 图标： `# pkg install numix-icon-theme`
- Numix 圆形图标： `# pkg install numix-icon-theme-circle`
- Yaru 图标：`# pkg install yaru-icon-theme`
- Canta 图标：`# pkg install canta-icon-theme`


## KDE 主题美化

我们要安装的是 [WhiteSur](https://www.pling.com/p/1398840/) 主题。

1. 下载主题源码包： `git clone https://github.com/vinceliuice/WhiteSur-kde`
2. 进入主题包目录： `cd WhiteSur-kde`
3. 修改 shebang： `ee install.sh`，修改第一行为 `#!/usr/local/bin/bash`，然后保存。
4. 执行安装： `bash install.sh`

## Gnome 主题美化

同样我们要安装的是 [WhiteSur](https://www.pling.com/p/1403328/) 主题。

1. 下载主题源码包： `git clone https://github.com/vinceliuice/WhiteSur-gtk-theme`
2. 进入主题包目录： `cd WhiteSur-gtk-theme`
3. 修改 shebang： `ee install.sh`，修改第一行为 `#!/usr/local/bin/bash`，然后保存。
4. 执行安装： `bash install.sh`

## [图标](https://www.pling.com/p/1405756/)

1. 下载图标： `git clone https://github.com/vinceliuice/WhiteSur-icon-theme`
2. 进入软件目录： `cd WhiteSur-icon-theme`
3. 修改 shebang： `ee install.sh`，修改第一行为 `#!/usr/local/bin/bash`，然后保存。
4. 执行安装： `bash install.sh`

## [光标](https://www.pling.com/p/1355701/)

1. 下载光标： `git clone https://github.com/vinceliuice/McMojave-cursors`
2. 进入软件目录： `cd McMojave-cursors`
3. 修改 shebang： `ee install.sh`，修改第一行为 `#!/usr/local/bin/bash`，然后保存。
4. 执行安装： `bash install.sh`

## 背景图片

[下载地址](https://github.com/vinceliuice/WhiteSur-kde/tree/master/wallpaper)

## 思考题

试着按照下面的步骤，在终端安装 [Papirus 图标](https://www.gnome-look.org/p/1166289/):

```sh
git clone https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
cd papirus-icon-theme
./install.sh
```

## 系统更新提示 `freebsd-update-notify`

>**技巧**
>
>FreeBSD 上的 KDE6 自带类似功能，无需安装 `freebsd-update-notify`，本教程仅做示例。


`freebsd-update-notify` 可以自动检测更新 FreeBSD 系统和 pkg 包。

### 安装 `freebsd-update-notify`

```sh
# pkg install freebsd-update-notify
```

或

```sh
# cd /usr/ports/deskutils/freebsd-update-notify/
# make install clean
```

### 配置 `freebsd-update-notify`

配置文件位于 `/usr/local/etc/freebsd-update-notify/freebsd-update-notify.conf`：

默认配置更新间隔太久，可以改成：

```ini
max-days-between-updates    1   # 更新检测间隔（日）      
hours-between-reminders     8   # 提醒间隔（小时）
```

### 图片示例


>**注意**
>
>截图为手动执行示例，实际上程序可以在后台自动运行，无需手动运行验证。若无法再现，可以尝试将 `freebsd-update-notify.conf` 中两个值都改为 `0`，再手动以 `root` 权限执行 `usr/local/libexec/freebsd-update-notify`。

日志位于 `/var/log/freebsd-update-cron`、`/var/log/freebsd-update-notify`。若要反馈故障，请使用英文提交 [issue](https://github.com/outpaddling/freebsd-update-notify/issues)。


![freebsd-update-notify on FreeBSD](../.gitbook/assets/notify1.png)

![freebsd-update-notify on FreeBSD](../.gitbook/assets/notify1.png)

![freebsd-update-notify on FreeBSD](../.gitbook/assets/notify3.png)

