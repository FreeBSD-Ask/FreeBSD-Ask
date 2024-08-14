# 第 29.2 节 安装 CDE

> **CDE 是 Common Desktop Environment（通用桌面环境）的缩写。历史悠久的桌面环境，常被用于 Unix 商业发行版。**
>
>以下内容未经测试，并不可靠。

## 安装软件

执行：

```shell-session
# pkg install xorg cde
```

或者：

```
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11/cde/ && make install clean
```

## 开启各项服务

在 shell 中执行：

```shell-session
# sysrc rpcbind_enable="YES"
# sysrc dtcms_enable="YES"
# sysrc inetd_enable=yes
# ln -s /usr/local/dt/bin/Xsession ~/.Xsession
# env LANG=C startx
```
	
将以下内容添加到 `/etc/inetd.conf`：

```shell-session
dtspc	stream	tcp	nowait	root	 /usr/local/dt/bin/dtspcd	/usr/local/dt/bin/dtspcd
```

将以下内容添加到 `/etc/services`：

```
dtspc		6112/tcp
```


重启系统。

```
# reboot
```

## 参考文献

- [cde Common Desktop Environment](https://www.freshports.org/x11/cde)