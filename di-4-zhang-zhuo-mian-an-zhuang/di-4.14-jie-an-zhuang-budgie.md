# 第 4.14 节 安装 Budgie

Budgie 是 Solus Linux 的默认桌面。

## 安装

```sh
# pkg install budgie wqy-fonts
```

或者

```sh
# cd /usr/ports/x11/budgie && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
```

会自动安装 lightdm。

## 配置

查看默认提示：

```sh
root@ykla:/home/ykla # pkg info -D budgie
budgie-10.8:
On install:
Copy 'xprofile' into your home directory:
  cp /usr/local/share/examples/budgie/xprofile ~/.xprofile

More information, https://codeberg.org/olivierd/freebsd-ports-budgie/wiki

If you want to launch new session from a console (without login manager)
  cp /usr/local/share/examples/budgie/xinitrc ~/.xinitrc
```

按需操作：

```sh
$ cp /usr/local/share/examples/budgie/xprofile ~/.xprofile
$ cp /usr/local/share/examples/budgie/xinitrc ~/.xinitrc
```

编辑 `/etc/fstab`，加入：

```sh
proc           /proc       procfs  rw  0   0
```

添加启动项：

```sh
# sysrc dbus_enable="YES"
# sysrc lightdm_enable="YES"
```

![FreeBSD 安装 Budgie](../.gitbook/assets/budgie1.png)

![FreeBSD 安装 Budgie](../.gitbook/assets/budgie2.png)

图中壁纸为默认。拍摄地为新加坡滨海湾区。

## 中文环境

在 `/etc/rc.conf` 下加入：

```sh
lightdm_env="LC_MESSAGES=zh_CN.UTF-8" 
```

编辑 `/etc/login.conf`：

找到 `default:\` 这一段，把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：

```sh
# cap_mkdb /etc/login.conf
```

![FreeBSD 安装 Budgie](../.gitbook/assets/budgie3.png)

## 参考文献

- [Installation](https://codeberg.org/olivierd/freebsd-ports-budgie/wiki/Installation)，本文主要补充来自此处，但是经过测试无需配置 `05-suspend.rules` 也可以做到关机重启。
