# 第 4.4 节 Mate

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

- 使用 pkg 安装：

```sh
# pkg install mate xorg wqy-fonts lightdm slick-greeter xdg-user-dirs
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/x11/mate/ && make install clean
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/x11/lightdm/ && make install clean 
# cd /usr/ports/x11/slick-greeter/ && make install clean 
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```

- 解释


| 包名               | 作用说明                             |
|:--------------------|:--------------------------------------|
| `mate`             | MATE 桌面环境|
| `xorg`             | X Window 系统        |
| `wqy-fonts`        | 文泉驿中文字体             |
| `lightdm`          | 显示管理器，提供图形登录界面               |
| `slick-greeter`    | LightDM 的美观登录界面插件，缺少 将无法启动 LightDM|
| `xdg-user-dirs`    | 可自动管理家目录子目录（可选安装）         |

## 安装后启动服务

```sh
# service dbus enable 
# service lightdm enable 
```

## `startx` 配置文件

在 `~/.xinitrc` 文件内加入下面一行：

```sh
exec mate-session
```

## 显示中文桌面环境


编辑 `/etc/login.conf`：找到 `default:\` 这一段，把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：

```sh
# cap_mkdb /etc/login.conf
```



## 输入法

![FreeBSD 安装 MATE](../.gitbook/assets/mate4.png)

ibus 测试成功。请参见输入法相关章节。


## 桌面欣赏

![FreeBSD 安装 MATE](../.gitbook/assets/cinnamon1.png)

![FreeBSD 安装 MATE](../.gitbook/assets/mate2.png)

![FreeBSD 安装 MATE](../.gitbook/assets/mate3.png)

## 故障排除与未竟事宜

### 配置 slick-greeter

创建 `/usr/local/etc/lightdm/slick-greeter.conf`，写入

```ini
[Greeter]
# 设置登录界面的背景图片路径
background=/home/ykla/cat.png

# 是否绘制用户自定义的背景图片
draw-user-backgrounds=false

# 设置 GTK+ 主题名称
theme-name=Dracula

# 设置图标主题名称
icon-theme-name=Adwaita

# 是否显示主机名
show-hostname=true

# 设置字体名称和大小
font-name=Sans 12

# 是否显示虚拟键盘选项
show-keyboard=true

# 是否显示电源管理选项（如关机、重启）
show-power=true

# 是否显示时钟
show-clock=true

# 是否显示退出选项
show-quit=true
```

![FreeBSD 安装 MATE](../.gitbook/assets/mate1.png)

#### 参考文献

- [lightdm not reading slick-greeter.conf](https://forums.freebsd.org/threads/lightdm-not-reading-slick-greeter-conf.92256/)
