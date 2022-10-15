# 第五节 通过源代码 ports 方式安装软件


>**注意**
>
>ports 和 pkg 可以同时使用，大部分人也是这么用的。但是要注意 pkg 的源必须是 latest，否则会存在一些依赖上比如 lib 库上的问题。latest 的源也比主线上的 ports 要出来的晚（是从中编译出来的），因此即使是 latset 源也可能会出现上述问题，总之有问题出现时就卸载那个 pkg 安装的包，重新使用 ports 编译即可。

## FreeBSD ports 基本用法

>**警告**
>
>FreeBSD 关于在未来弃用 portsnap 的说明：<https://marc.info/?l=freebsd-ports&m=159656662608767&w=2>


### 首先获取 portsnap

`# portsnap auto`

### 使用 whereis 查询软件路径

如 `# whereis python`

输出 `python: /usr/ports/lang/python`

### 如何安装 python3：

```
# cd /usr/ports/lang/python
# make BATCH=yes clean
```

其中 BATCH=yes 的意思是使用默认配置

## FreeBSD ports 多线程编译（推荐）

Linux 如 gentoo 上一般是直接 `-jx` 或者 `jx+1`, `x` 为核心数。

FreeBSD ports 多线程编译

```
FORCE_MAKE_JOBS=yes
MAKE_JOBS_NUMBER=4
```

写入 `/etc/make.conf` 没有就新建。

`4` 是处理器核心数（还是线程数？），不知道就别改。英特尔的处理器搜索 `CPU型号+ARK` 转跳英特尔官网可查询线程数。

### 如何使用多线程下载：

>**警告**
>
>**注意此小节内容不再对 FreeBSD 13 有效，在 2022-10-11 日 axel 由于上游长期停止开发[被移除了](https://www.freshports.org/ftp/axel/)。推荐使用 `www/aria2`**


~`# pkg install axel #下载多线程下载工具#`~

~新建或者编辑 `# ee /etc/make.conf` 文件，写入以下两行：~


```
FETCH_CMD=axel
FETCH_BEFORE_ARGS= -n 10 -a
FETCH_AFTER_ARGS=
DISABLE_SIZE=yes
```


### 进阶

如果不选择 `BATCH=yes` 的方法手动配置依赖：

看看 python 的 ports 在哪：

```
# whereis python
# python: /usr/ports/lang/python
```

安装python3：

`# cd /usr/ports/lang/python`

如何设置全部所需的依赖：

`# make config-recursive`

如何删除当前 port 的配置文件：

`# make rmconfig`

如何一次性下载所有需要的软件包：

`# make BATCH=yes fetch-recursive`

升级 ports

`# portsnap auto

ports 编译的软件也可以转换为 pkg 包

`# pkg create nginx`

### FreeBSD 包升级管理工具

首先更新 Ports 

```
# portsnap auto
```

然后列出过时 Ports 组件
```
# pkg_version -l '<'
```
下边分别列出 2 种 FreeBSD 手册中提及的升级工具:

一、portupgrade

```
# cd /usr/ports/ports-mgmt/portupgrade && make install clean
# portupgrade -ai #自动升级所有软件
# portupgrade -R screen #升级单个软件
```

二、portmaster （推荐）

```
# cd /usr/ports/ports-mgmt/portmaster && make install clean
# portmaster -ai #自动升级所有软件
# portmaster screen #升级单个软件
# portmaster -a -m "BATCH=yes" #或者-D -G –no-confirm 都可以免除确认
```
