# 第 4.4 节 安装 Mate

你也许不认识 mate，即巴拉圭冬青（Ilex paraguariensis），但是你可能听说“马黛茶”。许多南美球员（如梅西）非常热衷于这种植物制成的茶饮。

---

>**注意**
>
> 本文适用于 shell 为 bash/sh/zsh 的用户。
>
> 首先看看现在自己的 shell 是不是 `sh`（FreeBSD 默认 shell）、`bash` 或 `zsh`：
>
>```sh
># echo $0
>```


## 安装

```sh
# pkg install mate xorg wqy-fonts lightdm slick-greeter xdg-user-dirs lightdm-gtk-greeter-settings
```

或者：

```sh
# cd /usr/ports/x11/mate/ && make install clean # 主程序
# cd /usr/ports/x11/xorg/ && make install clean # X11
# cd /usr/ports/x11-fonts/wqy/ && make install clean # 文泉驿字体
# cd /usr/ports/x11/lightdm/ && make install clean # lightdm
# cd /usr/ports/x11/slick-greeter/ && make install clean # lightdm 需要
# cd /usr/ports/x11/lightdm-gtk-greeter-settings && make install clean # slick-greeter 配置工具
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean # 创建家目录的子目录
```

## 安装后启动服务

```sh
# service moused enable 
# service dbus enable 
# service lightdm enable 
```

## `startx` 配置文件

在 `~/.xinitrc` 文件内加入下面一行:

```sh
exec mate-session
```

## 显示中文桌面环境


编辑 `/etc/login.conf`：

找到 `default:\` 这一段，把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：

```sh
# cap_mkdb /etc/login.conf
```

![FreeBSD 安装 MATE](../.gitbook/assets/mate1.png)

![FreeBSD 安装 MATE](../.gitbook/assets/mate2.png)

![FreeBSD 安装 MATE](../.gitbook/assets/mate3.png)

## 输入法

![FreeBSD 安装 MATE](../.gitbook/assets/mate4.png)

ibus 测试成功。请参见输入法相关章节。

