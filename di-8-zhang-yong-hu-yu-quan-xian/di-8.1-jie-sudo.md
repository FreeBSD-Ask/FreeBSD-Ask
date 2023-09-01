# 第 8.1 节 sudo

## 安装

> OpenBSD 认为该软件漏洞太多，自行开发了 [doas](https://man.openbsd.org/doas)（FreeBSD 也可以用）。daos 教程在 26.2 节

FreeBSD 基本系统默认不自带 `sudo` 命令，需要使用 `root` 权限自行安装：

```shell-session
# pkg install sudo
```

## sudo 免密码

在 `/usr/local/etc/sudoers.d/` 下新建两个文件 `username`（需要免密码的用户）和 `wheel`：

- 文件 `username`内容如下：

```shell-session
%admin ALL=(ALL) ALL
```

- 文件 `wheel` 内容如下：

多加一行，使用 `sudo` 时不需要输入密码：

```shell-session
%wheel ALL=(ALL) NOPASSWD:ALL
```

