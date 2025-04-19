# 第 4.13 节 CDE

CDE 是 Common Desktop Environment（通用桌面环境）的缩写。是一款历史悠久的桌面环境，常被用于 Unix 商业发行版。


## 安装软件

- 使用 pkg 安装：

```sh
# pkg install xorg cde wqy-fonts xdg-user-dirs
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11/cde/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```


- 解释：

| 包名             | 作用说明                                                                 |
|:------------------|:--------------------------------------------------------------------------|
| `xorg`           |X Window 系统                                          |
| `cde`            | CDE 提供传统的桌面环境                            |
| `wqy-fonts`      | 文泉驿中文字体                                          |
| `xdg-user-dirs`  | 管理用户目录，如“桌面”、“下载”等。                                           |



## 查看安装后信息

```sh
root@ykla:/home/ykla # pkg info -D cde
cde-2.5.2_4:
On install:
CDE - The Common Desktop Environment is an X Windows desktop environment
that was commonly used on commercial UNIX variants such as Sun Solaris,
HP-UX, and IBM AIX. Developed between 1993 and 1999, it has now been
released under an Open source license by The Open Group.
# CDE（通用桌面环境）是早期 X Windows 的桌面环境，曾广泛用于商用 UNIX 系统如 Solaris、HP-UX 和 AIX。
# 开发时间大致为 1993–1999 年，现由 The Open Group 以开源协议发布。

Common Desktop Environment requires the Subprocess Control Service,
dtcms, and the inetd super server to fully function.
# 要完整运行 CDE，需启用子进程控制服务（dtspc）、日历管理服务（dtcms）以及 inetd 超级服务器。

First, add the following line to /etc/inetd.conf:

dtspc	stream	tcp	nowait	root	 /usr/local/dt/bin/dtspcd	/usr/local/dt/bin/dtspcd
# 第一步，在 /etc/inetd.conf 中添加 dtspcd 服务行。

Second, add the following line to /etc/services:

dtspc		6112/tcp # CDE Subprocess Control Service
# 第二步，在 /etc/services 中注册 dtspc 服务端口。

# sysrc rpcbind_enable=YES
# sysrc dtcms_enable=YES
# sysrc inetd_enable=YES
# service rpcbind start && service dtcms start && service inetd start
# 启用并启动 rpcbind、dtcms 和 inetd 服务，这是 CDE 所依赖的组件。

Finally, make sure to add /usr/local/dt/bin to your path.
# 最后，请将 /usr/local/dt/bin 添加到你的 PATH 环境变量中。

To start the Common Desktop Environment:
% env LANG=C startx /usr/local/dt/bin/Xsession
# 使用上述命令启动 CDE 桌面环境，设置环境变量 LANG=C 以避免本地化问题。

Alternatively, if you want to use the Login Manager as well, create
/usr/local/etc/X11/Xwrapper.config and add this line:

allowed_users=anybody
# 如果你想启用图形登录管理器（Login Manager），请创建 Xwrapper.config 并添加 allowed_users=anybody。

To start the Common Desktop Enviroment Login Manager:

% /usr/local/dt/bin/dtlogin -daemon

# 使用 dtlogin -daemon 命令启动 CDE 登录管理器（守护进程模式）。
```

## 配置服务与文件


- 配置服务

```sh
# service rpcbind enable
# service dtcms enable
# service inetd enable
# service dtlogin enable
```

- 配置可登录桌面的用户

```sh
# echo "allowed_users=anybody" > /usr/local/etc/X11/Xwrapper.config
```

- 为了 `startx`

```sh
# ln -s /usr/local/dt/bin/Xsession ~/.xinitrc
```

- 将以下内容添加到 `/etc/inetd.conf`：

```sh
dtspc	stream	tcp	nowait	root	 /usr/local/dt/bin/dtspcd	/usr/local/dt/bin/dtspcd
```

- 将以下内容添加到 `/etc/services`：

```sh
dtspc		6112/tcp
```


### 中文配置

编辑 `/etc/login.conf`：找到 `default:\` 这一段，把 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

刷新数据库：

```sh
# cap_mkdb /etc/login.conf
```

## 桌面欣赏


![dtlogin](../.gitbook/assets/cde2.png)

![FreeBSD 安装 CDE](../.gitbook/assets/cde4.png)

每次启动时都会在这里卡上几分钟。

![FreeBSD 安装 CDE](../.gitbook/assets/cde1.png)

![终端](../.gitbook/assets/cde3.png)

## 故障排除与未竟事宜

- 无法中文化（似乎日历是中文）

待解决


## 参考文献

- [cde Common Desktop Environment](https://www.freshports.org/x11/cde)
- [Setting up Common Desktop Environment for modern use](https://forums.freebsd.org/threads/setting-up-common-desktop-environment-for-modern-use.69475/)，详细配置可参考此处
- [CDE - Common Desktop Environment Wiki](https://sourceforge.net/p/cdesktopenv/wiki/FreeBSDBuild/)，CDE 项目官方 WiKi
