# 第 3.5 节 使用 ports 以源代码方式安装软件

> **注意**
>
> ports 和 pkg 可以同时使用，而且大部分人也是这么用的。但是要注意 pkg 的源必须是 latest，否则会存在一些依赖上比如 lib 库上的问题。latest 的源也比主线上的 ports 要出来的晚（是从中编译出来的），因此即使是 latset 源也可能会出现上述问题，总之有问题出现时就卸载那个 pkg 安装的包，重新使用 ports 编译即可。

## FreeBSD ports 基本用法

### 首先使用 Git 获取 Ports（其他方法参见前节）

安装 Git：
```
# pkg install git
```
拉取 Ports 存储库：

```
# git clone --depth 1 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git /usr/ports
```

#### 同步更新 Ports Git


```
root@ykla:/ # cd /usr/ports/ #切换目标目录
root@ykla:/usr/ports # git pull #同步更新上游 Ports
```

### 使用 whereis 查询软件路径

如 

```
# whereis python
```

将输出 

```python: /usr/ports/lang/python
```

### 如何安装 python3：

```shell-session
# cd /usr/ports/lang/python
# make BATCH=yes clean
```

其中 `BATCH=yes` 意味着使用默认参数进行编译。

## 加速编译

### FreeBSD ports 多线程编译（推荐）


- FreeBSD ports 多线程编译

将以下内容写入 `/etc/make.conf`，没有就 `touch` 新建一个。

```shell-session
FORCE_MAKE_JOBS=yes
MAKE_JOBS_NUMBER=4
```
Linux 如 Gentoo 上一般是直接 `-jx` 或者 `jx+1`, `x` 为核心数。

`4` 是处理器核心数（还是线程数？），不知道就别改。英特尔的处理器搜索 `CPU 型号+ARK` 转跳英特尔官网可查询线程数。

- 个别情况下可以设置别名加速编译：（非永久设置，FreeBSD 14 无须设置即生效）

```shell-session
# alias ninja='ninja -j4'
```

### 设置内存为 tmp

`ee /etc/fstab` 写入：

```shell-session
tmpfs /tmp tmpfs rw 0 0
```

重启。

参考资料：[tmpfs --in-memory file system](https://man.freebsd.org/cgi/man.cgi?tmpfs(5))


### ccache

**这部分现在有点问题，先不要用，见 [Bug](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=272917)**

>**警告**
>
>使用 ccache 可能会导致编译失败！只在重复编译时起效果，首次编译不仅不会加速还会慢上一些。是一种以空间换时间的行为。


目前最新版本是 ccache4：

```shell-session
# pkg install ccache4
```

或

```shell-session
# cd /usr/ports/devel/ccache4/ && make install clean
```

- ksh/sh 添加到 `/etc/profile`:
```shell-session
export CCACHE_PREFIX=distcc
export DISTCC_HOSTS="localhost host1 host2"
```
- csh/tcsh 添加到 `/etc/csh.cshrc`:
```shell-session
setenv CCACHE_PREFIX distcc
setenv DISTCC_HOSTS "localhost host1 host2"
```

做软链接：
```shell-session
# ccache-update-links
```
```shell-session
root@ykla:/usr/ports/devel/ccache4 # ccache -M 5G  # 设置编译缓存最大为 5GB
Set cache size limit to 5.0 GB

root@ykla:/usr/ports/devel/ccache4 # ccache -s  # 查看编译缓存
Local storage:
  Cache size (GB): 0.0 / 5.0 ( 0.00%)

root@ykla:~ # find /  -name ccache.conf # 全局查找配置文件路径
/root/.config/ccache/ccache.conf
```


参考文献：

- [ccache-howto-freebsd.txt.in](https://github.com/freebsd/freebsd-ports/blob/main/devel/ccache/files/ccache-howto-freebsd.txt.in)
- [ccache -a fast C/C++ compiler cache](https://man.freebsd.org/cgi/man.cgi?query=ccache&sektion=1&n=1)
### 如何使用多线程下载：

- axel

```shell-session  
# pkg install axel
```

新建或者编辑 `# ee /etc/make.conf` 文件，写入以下几行：

```shell-session
FETCH_CMD=axel
FETCH_BEFORE_ARGS= -n 10 -a
FETCH_AFTER_ARGS=
DISABLE_SIZE=yes
```

- wget2
  
**wget2 正在进行测试！先不要用**
  
```shell-session
# cd /usr/ports/www/wget2/ && make install clean
```
新建或者编辑 `# ee /etc/make.conf` 文件，写入以下几行：
```shell-session
FETCH_CMD=wwget2
FETCH_BEFORE_ARGS= -c -t 3 -o 10
FETCH_AFTER_ARGS=
DISABLE_SIZE=yes
```

`-c` 断点续传；`-t 3` 重试次数 3；` -o 10` 启用 10 个线程进行下载。

**`10` 这个参数可能过于保守，我一般直接用 `50` 或 `100`。但是要注意很多服务器不支持这么多线程同时下载。**


## 进阶

如果不选择 `BATCH=yes` 的方法手动配置：

看看 python 的 ports 在哪：

```shell-session
# whereis python
# python: /usr/ports/lang/python
```

安装 python3：

```
# cd /usr/ports/lang/python
```

如何设置全部所需的依赖：

```
# make config-recursive
```

如何删除当前 port 及其依赖的配置文件：

```
# make rmconfig-recursive
```

如何一次性下载所有需要的软件包：

```
# make BATCH=yes fetch-recursive
```

升级 ports

```
# portsnap auto
```

ports 编译的软件也可以转换为 pkg 包

```
# pkg create nginx
```

## FreeBSD 包升级管理工具

首先更新 Ports

```shell-session
# portsnap auto
```

然后列出过时 Ports 组件

```shell-session
# pkg_version -l '<'
7-zip-22.01                        <
AppStream-0.16.1                   <
alsa-plugins-1.2.2_11              <
aom-3.7.0.r1                       <
ark-23.04.3                        <
baloo-widgets-23.04.3              <
brotli-1.0.9,1                     <
ca_root_nss-3.92                   <
cargo-c-0.9.23                     <
chromium-116.0.5845.110            <
consolekit2-1.2.6_1                <
discount-2.2.7c                    <
dolphin-23.04.3                    <
…………
```

下边分别列出 2 种 FreeBSD 手册中提及的升级工具:

一、portupgrade

```shell-session
# cd /usr/ports/ports-mgmt/portupgrade && make install clean
# portupgrade -ai #自动升级所有软件
# portupgrade -R screen #升级单个软件
```

二、portmaster （推荐）

- 更新：

```shell-session
# cd /usr/ports/ports-mgmt/portmaster && make install clean
# portmaster -a #自动升级所有软件
# portmaster screen #升级单个软件
```

- 查看依赖关系：

```shell-session
root@ykla:/usr/ports/ports-mgmt/portmaster # portmaster sysutils/htop  --show-work

===>>> Port directory: /usr/ports/sysutils/htop

===>>> Starting check for all dependencies
===>>> Gathering dependency list for sysutils/htop from ports

===>>> Installed devel/autoconf
===>>> Installed devel/automake
===>>> NOT INSTALLED		devel/libtool
===>>> NOT INSTALLED		devel/pkgconf
===>>> NOT INSTALLED		lang/python311
===>>> Installed ports-mgmt/pkg
```

- 安装软件

参考资料：

- [portmaster -- manage your ports without external databases or languages](https://man.freebsd.org/cgi/man.cgi?portmaster(8)#end)
  
## FreeBSD USE

- 如何指定 Ports 编译的版本？

如 Python 现在的默认编译版本是 3.9，要改为 3.11，：

```shell-session
# echo "DEFAULT_VERSIONS+= python=3.11  python3=3.11" >> /etc/make.conf
```
>如果只设置了单个参数，那么出现警告是正常的，见 [Bug](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=243034)
>```shell-session
>/!\ WARNING /!\
>
>PYTHON_DEFAULT must be a version present in PYTHON2_DEFAULT or PYTHON3_DEFAULT,
>if you want more Python flavors, set BUILD_ALL_PYTHON_FLAVORS in your make.conf
>```


完整的列表见 <https://cgit.freebsd.org/ports/tree/Mk/bsd.default-versions.mk>

参考资料：

- [Ports/DEFAULT_VERSIONS](https://wiki.freebsd.org/Ports/DEFAULT_VERSIONS)
- [Python](https://wiki.freebsd.org/Python)


- 如何全局屏蔽 mysql

```shell-session
# echo "OPTION_UNSET+= MYSQL" >> /etc/make.conf
```

## 查看依赖

已经安装：

```shell-session
root@ykla:~ # pkg info -d screen
screen-4.9.0_6:
	indexinfo-0.3.1
```

未安装：

```shell-session
root@ykla:/usr/ports/sysutils/htop # make all-depends-list
/usr/ports/ports-mgmt/pkg
/usr/ports/devel/pkgconf
/usr/ports/devel/kyua
/usr/ports/devel/lutok
/usr/ports/lang/lua54
/usr/ports/devel/libedit
/usr/ports/databases/sqlite3
/usr/ports/lang/tcl86
/usr/ports/lang/python311
/usr/ports/devel/gettext-runtime
/usr/ports/print/indexinfo
/usr/ports/devel/gettext-tools
/usr/ports/devel/libtextstyle
/usr/ports/devel/libffi
/usr/ports/misc/dejagnu
/usr/ports/devel/gmake
/usr/ports/lang/expect
/usr/ports/devel/autoconf
/usr/ports/devel/m4
/usr/ports/print/texinfo
/usr/ports/misc/help2man
/usr/ports/devel/p5-Locale-gettext
/usr/ports/lang/perl5.34
/usr/ports/devel/p5-Locale-libintl
/usr/ports/converters/libiconv
/usr/ports/converters/p5-Text-Unidecode
/usr/ports/textproc/p5-Unicode-EastAsianWidth
/usr/ports/devel/autoconf-switch
/usr/ports/devel/automake
/usr/ports/math/mpdecimal
/usr/ports/devel/readline
/usr/ports/devel/libtool
```

