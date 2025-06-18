# 第 5.8 节 Lumina

Lumina 使用 BSD 许可证。Lumina 技术栈为 QT5，不使用任何基于 Linux 的桌面框架，主张轻量化。

2025.1.8 测试在 VMware 中无法进入桌面，进入后闪退。参见 [Some problem Under FreeBSD 13.2 with Xorg and Lumina Desktop...How to solve?](https://forums.freebsd.org/threads/some-problem-under-freebsd-13-2-with-xorg-and-lumina-desktop-how-to-solve.88882/)。但是在 VirtualBox 中显示正常。


>**注意**
>
>[Lumina](https://github.com/lumina-desktop/lumina) 在换了开发者后，开发长期处于停滞状态，我向其提交的 pull 长期无人处理，并且没有新的 commit 信息。

## 安装

- 使用 pkg 安装：

```sh
# pkg install lumina xorg lightdm lightdm-gtk-greeter wqy-fonts xdg-user-dirs
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11/lumina/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/x11/lightdm/ && make install clean
# cd /usr/ports/x11/lightdm-gtk-greeter/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```

- 解释

| 包名                   | 作用说明                                                                 |
|:------------------------|:--------------------------------------------------------------------------|
| `lumina`               | Lumina 桌面环境 |
| `xorg`                 | X Window 系统 |
| `lightdm`              | 轻量级显示管理器 LightDM|
| `lightdm-gtk-greeter`  | LightDM 的 GTK+ 登录界面插件。缺少将无法启动 LightDM |
| `wqy-fonts`            | 文泉驿中文字体|
| `xdg-user-dirs`        | 管理用户目录，如“桌面”、“下载”等 |


## 配置服务


```sh
# service dbus enable
# service lightdm enable
```

## 配置 `startx`

编辑 `~/.xinitrc`，添加：

```sh
exec lumina-desktop
```

## 中文化

在 `/etc/rc.conf` 下加入：

```sh
lightdm_env="LC_MESSAGES=zh_CN.UTF-8" 
```

---

编辑 `/etc/login.conf`：找到 `default:\` 这一段，把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：

```sh
# cap_mkdb /etc/login.conf
```

## 桌面欣赏

![FreeBSD 安装 Lumina](../.gitbook/assets/lumina1.png)

![FreeBSD 安装 Lumina](../.gitbook/assets/lumina2.png)

![FreeBSD 安装 Lumina](../.gitbook/assets/lumina3.png)
