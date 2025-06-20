# 本书中使用的一些约定

## 本书中命令及符号含义

`#` 代表 `root` 下的操作，基本等同 `su`、`sudo` 和 `doas`。

`$`、`%` 代表普通用户账户权限。

>**注意**
>
>提示一些注意事项。

>**技巧**
>
>提示一些技巧。

>**警告**
>
>如果不知道、不做就无法完成或造成重大危害的事项。

---

章节：

```
故障排除与未竟事宜
```

旨在将现存的问题和改进的方向/建议或谜团留置其中，以期后人的智慧。

## pkg 与 ports

因为 FreeBSD 有两种安装软件的方式（但个别软件不支持 pkg 安装）：因此为了方便，在本教程中已经尽可能地列出了两种方式的安装说明。但希望大家明白，只是为了方便，而并非不能使用 ports 或者 pkg 进行安装或必须使用二者其一进行安装。

>**请注意**
>
> ports 一般是 HEAD 分支，你的 pkg 最好与 ports 保持在同一主线上，即都选择 `latest`。但是你亦可以自行拉取 pkg 对应的 Ports 季度分支，如 `2025Q1`。

如果要安装软件 `yyy`，`yyy` 在 ports 里是 `xxx/yyy`，那么路径便是 `/usr/ports/xxx/yyy`。

- 那么首先可以通过 pkg 安装二进制软件包，和绝大多数 Linux 用法一样，下同：

```sh
# pkg install yyy
```

还可以这样：

```sh
# pkg install xxx/yyy
```

或者这样简写：

```sh
# pkg ins yyy
```

- 那么还可以通过 Ports 编译安装：

```sh
# cd /usr/ports/xxx/yyy
# make install clean
```

将会不断地弹出来窗口询问你怎么选。如果是使用默认选项，请这样做，则：

```sh
# cd /usr/ports/xxx/yyy
# make BATCH=yes install clean
```

如果你想一次性完成所有配置：

```sh
# cd /usr/ports/xxx/yyy
# make config-recursive # 会一直问你，直到结束依赖
# make install clean
```
