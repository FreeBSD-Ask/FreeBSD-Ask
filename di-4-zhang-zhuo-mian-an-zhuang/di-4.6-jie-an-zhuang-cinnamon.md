# 第 4.6 节 安装 Cinnamon

>**注意**
>
> 以下教程适用于 shell 为 bash/sh/zsh 的用户。
>
> 首先看看现在自己的 shell 是不是 `sh`（FreeBSD 默认）、`bash`、`zsh`：
>
>```sh
># echo $0
>```




## 安装

```sh
# pkg install xorg lightdm slick-greeter cinnamon wqy-fonts xdg-user-dirs
```

xdg-user-dirs 可自动管理家目录子目录（可选安装）

或者

```sh
# cd /usr/ports/x11/xorg/ && make install clean # X11
# cd /usr/ports/x11/cinnamon/ && make install clean # 桌面元包
# cd /usr/ports/x11-fonts/wqy/ && make install clean # 文泉驿字体
# cd /usr/ports/x11/lightdm/ && make install clean # 登录管理器
# cd /usr/ports/x11/slick-greeter/ && make install clean # 登录管理器插件
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean # 创建用户家目录子目录
```


## 配置

```sh
# ee ~/.xinitrc
```

添加：

```sh
exec cinnamon-session
```

然后

```sh
# ee /etc/fstab
```

添加：

```sh
proc /proc procfs rw 0 0
```

### 添加启动项：

```sh
# service dbus enable 
# service lightdm enable
```

### 中文化

编辑 `/etc/login.conf`：

找到 `default:\` 这一段（写作时为第 24 行），把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：

```sh
# cap_mkdb /etc/login.conf
```


![cinnamon on FreeBSD](../.gitbook/assets/cinnamon1.png) 

![cinnamon on FreeBSD](../.gitbook/assets/cinnamon2.png) 

壁纸就是黑色的，不是哪儿出了问题。

![cinnamon on FreeBSD](../.gitbook/assets/cinnamon3.png) 

自定义壁纸。
