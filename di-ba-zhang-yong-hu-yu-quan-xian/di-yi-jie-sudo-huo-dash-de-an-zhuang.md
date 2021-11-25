# 第一节 sudo

## 安装

系统默认不提供 `sudo` 命令，需要使用 `root` 用户自行安装：

```
#pkg install sudo
```

## sudo 免密码



在 `/usr/local/etc/sudoers.d/` 下新建两个文件 username（需要免密码的用户）`admin` 和 `wheel`：

`username`内容如下：

```
%admin ALL=(ALL) ALL
```

`wheel`内容如下，多加一行 `NOPASSWD:` ，使用 `sudo` 时不需要输入密码：

```
%wheel ALL=(ALL) NOPASSWD:ALL
```

