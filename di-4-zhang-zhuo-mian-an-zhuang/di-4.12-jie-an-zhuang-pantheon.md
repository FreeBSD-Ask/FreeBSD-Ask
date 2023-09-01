# 第 4.12 节 安装 Pantheon

**尚未完成，仍然在测试！**

```shell-session
root@ykla:~ # pkg install git
root@ykla:~ # git clone --depth 1 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git /usr/ports
root@ykla:~ # fetch https://codeberg.org/olivierd/freebsd-ports-elementary/raw/branch/master/Tools/scripts/elementary-merge
elementary-merge                                      6048  B 1413 kBps    00s
root@ykla:~ # mkdir freebsd-ports-elementary
root@ykla:~ # cd freebsd-ports-elementary/
root@ykla:~/freebsd-ports-elementary # pwd
/root/freebsd-ports-elementary             # 记住此路径！
root@ykla:~ # ee elementary-merge
LOCAL_REP="/root/freebsd-ports-elementary" # 修改为上述路径
root@ykla:~ # sh elementary-merge -c
Cloning into '.'...
remote: Enumerating objects: 484, done.
remote: Counting objects: 100% (484/484), done.
remote: Compressing objects: 100% (441/441), done.
Receiving objects: 100% (484/484), 171.99 KiB | 360.00 KiB/s, done.
Resolving deltas: 100% (54/54), done.
remote: Total 484 (delta 54), reused 285 (delta 24), pack-reused 0
```

```shell-session
root@ykla:~ # sh elementary-merge -m
Switched to a new branch 'elementary'
/root/freebsd-ports-elementary/x11-wm/switchboard-plug-pantheon-shell/Makefile -> x11-wm/switchboard-plug-pantheon-shell/Makefile
/root/freebsd-ports-elementary/x11-wm/switchboard-plug-pantheon-shell/distinfo -> x11-wm/switchboard-plug-pantheon-shell/distinfo
/root/freebsd-ports-elementary/x11-wm/switchboard-plug-pantheon-shell/pkg-descr -> x11-wm/switchboard-plug-pantheon-shell/pkg-descr

………………

/root/freebsd-ports-elementary/x11-clocks/wingpanel-indicator-datetime/pkg-descr -> x11-clocks/wingpanel-indicator-datetime/pkg-descr
/root/freebsd-ports-elementary/x11-clocks/wingpanel-indicator-datetime/pkg-plist -> x11-clocks/wingpanel-indicator-datetime/pkg-plist
```

**最后使用 `sh elementary-merge -r` 可还原 Ports**

```shell-session
root@ykla:~ # cd /usr/ports/x11/elementary-session
root@ykla:/usr/ports/x11/elementary-session # pkg install cmake pkgconf gnome-settings-daemon desktop-file-utils gnome-keyring accountsservice
root@ykla:/usr/ports/x11/elementary-session # make BATCH=yes install clean
```

```shell-session
$ cp /usr/local/share/examples/elementary-session/xprofile ~/.xprofile
```

## 参考文献

- [olivierd/freebsd-ports-elementary](https://codeberg.org/olivierd/freebsd-ports-elementary/wiki)

