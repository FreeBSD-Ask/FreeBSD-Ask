# 7.2 IceWM

IceWM 是基于 X Window 系统的窗口管理器。IceWM 的目标是速度快、简单，并且不干扰用户操作。它自带分页器任务栏、全局和每个窗口的快捷键以及动态菜单系统。窗口可以通过键盘和鼠标来管理。窗口可以被图标化到任务栏、托盘、桌面，或被隐藏。用户可以通过快速切换窗口（Alt+Tab）或窗口列表来控制它们。多种可配置的焦点模型可通过菜单选择。多显示器环境由 RandR 和 Xinerama 支持。IceWM 高度可配置、可自定义主题且文档完善。IceWM 拥有可选的外部背景墙纸管理器（支持透明）、简单的会话管理器和系统托盘。可在流行的 Linux 发行版，以及大多数 *BSD 系统上使用 IceWM。——引自 [IceWM Window Manager](https://ice-wm.org/)

## 安装

### 使用 pkg 安装

```sh
# pkg install xorg icewm slim wqy-fonts xdg-user-dirs
```

### 使用 Ports 安装

```sh
# cd /usr/ports/x11-wm/icewm/ && make install clean # fluxbox
# cd /usr/ports/x11-themes/icewm-extra-themes/ && make install clean 
# cd /usr/ports/x11/xorg/ && make install clean 
# cd /usr/ports/x11/slim/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean
```

### 软件包解释
  
| 包名               | 作用说明                                                                 |
|:------------------|:-----------------------------------------------------------------------|
| `xorg`           |X Window 系统                                           |
| `icewm`          | 轻量级窗口管理器                    |
| `slim`           | 轻量级图形登录管理器                            |
| `wqy-fonts`      | 文泉驿中文字体                                              |
| `xdg-user-dirs`  | 管理用户目录，如“桌面”、“下载”……                                          |


## `startx`

编辑 `~/.xinitrc`，加入（用谁登录就用谁写入）：

```sh
exec icewm-session
```

## 启动项

```sh
# service dbus enable # 作为依赖自动安装
# service slim enable
```

## fstab

编辑 `/etc/fstab`，加入：

```sh
proc           /proc       procfs  rw  0   0
```

## 中文环境

编辑 `/etc/login.conf`：找到 `default:\` 这一段，把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：


```sh
# cap_mkdb /etc/login.conf
```


## 桌面欣赏

![FreeBSD 安装 icewm](../.gitbook/assets/icewm3.png)

安装后默认如上。我们可以换主题：

![FreeBSD 安装 icewm](../.gitbook/assets/fluxbox1.png)

![FreeBSD 安装 icewm](../.gitbook/assets/icewm1.png)

![FreeBSD 安装 icewm](../.gitbook/assets/icewm2.png)


## 故障排除与未竟事宜

### 中文环境不完整

待 PR。

## 参考文献

- [icewm-preferences(5)](https://man.freebsd.org/cgi/man.cgi?query=icewm-preferences)，手册页
