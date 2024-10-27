# 第 4.16 节 安装 CDE

> **CDE 是 Common Desktop Environment（通用桌面环境）的缩写。历史悠久的桌面环境，常被用于 Unix 商业发行版。**


## 安装软件

执行：

```sh
# pkg install xorg cde
```

或者：

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11/cde/ && make install clean
```

## 开启各项服务

在 shell 中执行：

```sh
# sysrc rpcbind_enable="YES"
# sysrc dtcms_enable="YES"
# sysrc inetd_enable=yes
# ln -s /usr/local/dt/bin/Xsession ~/.Xsession
# env LANG=C startx
```
	
将以下内容添加到 `/etc/inetd.conf`：

```sh
dtspc	stream	tcp	nowait	root	 /usr/local/dt/bin/dtspcd	/usr/local/dt/bin/dtspcd
```

将以下内容添加到 `/etc/services`：

```sh
dtspc		6112/tcp
```


重启系统。

```sh
# reboot
```

## 参考文献

- [cde Common Desktop Environment](https://www.freshports.org/x11/cde)
