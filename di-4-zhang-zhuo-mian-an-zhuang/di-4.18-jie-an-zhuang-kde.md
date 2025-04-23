# 第 4.18 节 KDE6

KDE 旨在开发一套现代桌面系统，如果你觉得 KDE 界面很像 Windows，那么从时间线上看，应该说是“Windows 很像 KDE”。

>**技巧**
>
>视频教程见 [003-FreeBSD14.2 安装 KDE6](https://www.bilibili.com/video/BV12zAYeKEej)

>**注意**
>
>旧版本升级说明：即卸载后安装新的 KDE。
>
>```
># pkg remove -f kde5 && pkg autoremove
>```
>
>或
>
>```
># pkg remove -f kde6 && pkg autoremove
>```

然后按下文操作即可。

## 安装

- 使用 pkg 安装：

```sh
# pkg install xorg sddm kde plasma6-sddm-kcm wqy-fonts xdg-user-dirs
```

> **故障排除与未竟事宜**
>
> 如果有时候提示 `pkg` 找不到或者没有 kde6，请点击 [x11/kde](https://www.freshports.org/x11/kde) 看看是不是二进制包没有被构建出来。有时候需要切换 quarterly（待上游构建出来了再换到 latest 源，`pkg upgrade` 更新即可）或者 latest 源。类似方法适用于所有软件，故后边不再赘述。如果没有，需要自己使用上述的 Port 进行编译。


- 或者使用 Ports 安装：

```sh
# cd /usr/ports/x11/xorg/ && make install clean 
# cd /usr/ports/x11/kde/ && make install clean 
# cd /usr/ports/x11/sddm/ && make install clean 
# cd /usr/ports/deskutils/plasma6-sddm-kcm/ && make install clean 
# cd /usr/ports/x11-fonts/wqy/ && make install clean 
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```

- 解释

| 包名                   | 作用                     |
|:----------------------|:------------------------|
| `xorg`               | 图形界面基础，提供 X Window 系统              |
| `sddm`               | 登录管理器                |
| `kde`    | KDE 桌面环境              |
| `plasma6-sddm-kcm`   | 配置 SDDM 的 KDE 模块，可在配置登录界面外观等参数。     |
| `wqy-fonts`          |  文泉驿中文字体              |
| `xdg-user-dirs`      | 可自动管理家目录子目录（可选安装）          |


## 启动项设置

```sh
# service dbus enable # 用于桌面环境的进程间通信
# service sddm enable # SDDM 登录管理器
```

![KDE 6 界面](../.gitbook/assets/kde6-1.png)

### `startx`

```sh
# echo "exec ck-launch-session startplasma-x11" > ~/.xinitrc
```

> 如果你在 root 下已经执行过了，那么新用户仍要再执行一次才能正常使用（无需 root 权限或 sudo 等）`startx`。


## 基于 Wayland

- 在前文的基础上，把 `/usr/local/share/xsessions/plasmax11.desktop` 中的 `/usr/local/bin/startplasma-x11` 都改成 `/usr/local/bin/startplasma-wayland`。重启即可。

- 或者在 SDDM 左下角选择 Wayland，物理机默认应该就是。

![KDE 6 wayland FreeBSD](../.gitbook/assets/kde6-3.png)

## 权限设置

普通用户还需要将用户加入 wheel 组（或 `video` 组）：

```sh
# pw groupmod wheel -m 用户名
```

## 登录界面主题

- 使用 pkg 安装：

```sh
# pkg install sddm-freebsd-black-theme
```

- 或使用 Ports 安装：

```sh
# cd /usr/ports/x11-themes/sddm-freebsd-black-theme/ 
# make install clean
```


- 查看安装后配置：

```sh
root@ykla:/home/ykla # pkg info -D sddm-freebsd-black-theme
sddm-freebsd-black-theme-1.3:
On install:
To enable this theme edit:

 /usr/local/etc/sddm.conf
# 若要启用此主题，请编辑 /usr/local/etc/sddm.conf 文件。

 This theme use the x11-fonts/montserrat font by default. However, it
 can be changed to any desired font editing:

 /usr/local/share/sddm/themes/sddm-freebsd-black-theme/theme.conf
# 此主题默认使用 montserrat 字体（需安装 x11-fonts/montserrat），
# 你可以通过编辑 theme.conf 文件更改为任意你想要的字体。

Always:
===>   NOTICE:
# 注意事项：

The sddm-freebsd-black-theme port currently does not have a maintainer. As a result, it is
more likely to have unresolved issues, not be up-to-date, or even be removed in
the future. To volunteer to maintain this port, please create an issue at:

https://bugs.freebsd.org/bugzilla
# 此 port 目前没有维护者，因此可能存在未解决的问题、不够及时的更新，甚至未来可能被移除。
# 若你愿意接手维护，请到上述链接创建一个问题（issue）。

More information about port maintainership is available at:

https://docs.freebsd.org/en/articles/contributing/#ports-contributing
# 有关 port 维护的更多信息，请参考 FreeBSD 官方文档中关于贡献 port 的章节。
```

- 编辑 `/usr/local/etc/sddm.conf`，写入：

```sh
[Theme]
Current=sddm-freebsd-black-theme
```

重启，设置完成：

 ![KDE 6 FreeBSD 主题](../.gitbook/assets/kde-theme.png)

### 参考文献

- [デスクトップ 環境 の 構築 - 4-7. LXQT のインストールと 設定 (LXQT 2.0.0)](http://silversack.my.coocan.jp/bsd/fbsd11x_bde-4-7_lxqt.htm)

## 中文化

### SDDM 中文化

```sh
# sysrc sddm_lang="zh_CN"
```

### 系统中文化方法 ① 用户分级

编辑 `/etc/login.conf`：找到 `default:\` 这一段，把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：

```sh
# cap_mkdb /etc/login.conf
```

![SDDM](../.gitbook/assets/sddmcn.png)

![KDE 6](../.gitbook/assets/kde6-2.png)

### 系统中文化方法 ② 系统设置

点击开始-> System Settings ->  `Language & Time` 在 `Region & Language` 项的 `Language` 栏点击右侧 `Modify` 中找到“简体中文”（一般是倒数第二，如果都是 `□□□□`，检查你的中文字体安装否）单击之。然后单击 `Apply` 按钮；logout（注销）后重新登录，此时系统语言将变为中文。

![KDE 6](../.gitbook/assets/kde6-4.png)

![KDE 6](../.gitbook/assets/kde6-5.png)

#### 参考文献

- [SDDM login screen with KDE: change language?](https://forums.freebsd.org/threads/sddm-login-screen-with-kde-change-language.80535/)


## 故障排除与未竟事宜

### sddm 登录闪退


如果你使用 VMware 虚拟机时，压根看不见 sddm 最下边的选项，请按照配置虚拟机章节的教程配置屏幕自动缩放。


### 启动 sddm 提醒 `/usr/bin/xauth: (stdin):1: bad display name`，但是可以正常 `startx`

你需要在 `/etc/rc.conf` 里面检查你的 `hostname` 是否为空（理论上不应该为空），有没有设置：

![](../.gitbook/assets/errornohostname.png)

按需设置 `hostname` 即可。

### 菜单缺失关机、重启等四个按纽

如果无效请先看看你是不是在 sddm 界面选择了 `用户会话`（读取 `.xinitrc`），应该选择 `plasma-x11`。

修改 `/etc/sysctl.conf` 将其中 `security.bsd.see_other_uid` 的值改为 `1`（`1` 为开启）。重启后即可。

#### 参考文献

- [Missing power buttons when logged in from SDDM](https://forums.freebsd.org/threads/missing-power-buttons-when-logged-in-from-sddm.88231/)

### 解除自动锁屏

单击“设置”——>“安全和隐私”——>“锁屏”——>“自动锁定屏幕”选择“不自动锁屏”，然后点击“应用”。（休眠唤醒后锁定屏幕可按需设置）

注销后重新登录即可。


![关闭 KDE 6 锁屏](../.gitbook/assets/suoping.png)

### 状态栏不显示时钟和时间

点击时区设置，输入 `beijing`，设置上海即可。若无效，请先更新软件包。
