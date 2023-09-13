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

## 故障排除

- `xxx Is Not in the Sudoers File. This Incident Will Be Reported`

应当在 sudoers 中加入一句话来解决这个问题：

使用 ee 打开 sudoers：

```shell-session
# ee /usr/local/etc/sudoers
```
找到 `root ALL=(ALL:ALL) ALL` 这行，一般是在第 94 行。在这行下面加一句：

```
你的用户名 ALL=(ALL:ALL) ALL
```
然后保存退出即可。
