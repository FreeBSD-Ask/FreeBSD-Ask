# 5.5 使用 Ports 以源代码方式安装软件

## Ports 与 Port 概述

### Ports 历史

Ports 是一种从源代码（也支持闭源二进制包）构建软件的框架。由 Jordan K. Hubbard（jkh@FreeBSD.org）创建，最初于 1994 年 8 月公开发布。

```sh
# git log --reverse --max-parents=0 --pretty=format:"commit: %h%nAuthor: %an%nDate: %ci%n%n%B" # 打印第一次提交
commit: d27f048e966a
Author: Jordan K. Hubbard
Date: 1994-08-21 13:12:57 +0000

Commit my new ports make macros.  Still not 100% complete yet by any means
but fairly usable at this stage.
Submitted by:   jkh
```

“提交了我为 ports 编写的新 Make 宏。虽然还远未完全完善，但目前已经可以较为正常地使用了。”

>**技巧**
>
>我们可以看到：对于一个开源项目，无论使用的何种版本控制系统，保留完整的提交记录，是多么地重要。读者慢慢就会发现，这不仅仅是考古上的意义。

NetBSD 和 OpenBSD 也使用 Ports，但实现并不通用。

#### 参考文献

- [\[FreeBSD-Ports-Announce\] Happy 20th birthday FreeBSD ports tree!](https://lists.freebsd.org/pipermail/freebsd-ports-announce/2014-August/000088.html)，2014 庆祝 Ports 20 年，文中还有个庆祝视频。

### Ports 与 Port 释义

一款软件的相关文件或文件夹（补丁文件、校验码、Makefile 等）的集合（表现为一个文件夹）称为一个 Port，所有 Port（移植软件）的集合即 Ports Collection 或 Ports Tree，简称 Ports。

```sh
$ cd /usr/ports # 切换到 /usr/ports
$ ls # 列出此目录下所有文件  ①
accessibility	COPYRIGHT	GIDs		misc		README		www
arabic		databases	graphics	Mk		russian		x11
archivers	deskutils	hebrew		MOVED		science		x11-clocks
astro		devel		hungarian	multimedia	security	x11-drivers
audio		dns		irc		net		shells		x11-fm
benchmarks	editors		japanese	net-im		sysutils	x11-fonts
biology		emulators	java		net-mgmt	Templates	x11-servers
cad		filesystems	Keywords	net-p2p		textproc	x11-themes
CHANGES		finance		korean		news		Tools		x11-toolkits
chinese		french		lang		polish		UIDs		x11-wm
comms		ftp		mail		ports-mgmt	ukrainian
CONTRIBUTING.md	games		Makefile	portuguese	UPDATING
converters	german		math		print		vietnamese
$ ls databases/ # 切换到 databases 数据库分类目录下
adminer						php-xapian
adodb5						php81-dba

    ……省略一部分……

mongodb60					py-apache-arrow
mongodb70					py-apsw
mongodb80					py-asyncmy
mongosh						py-asyncpg
$ cd databases/postgresql18-server # 切换到 postgresql18-server 目录
ykla@ykla:/usr/ports/databases/postgresql18-server $ ls ②
distinfo		pkg-descr		pkg-plist-contrib	pkg-plist-pltcl
files			pkg-install-server	pkg-plist-plperl	pkg-plist-server
Makefile		pkg-plist-client	pkg-plist-plpython
```

- ① `/usr/ports` 这个文件夹整体称作 Ports，包括几十种不同的分类目录，每个目录下有若干 Port。
- ② `/usr/ports/databases/postgresql18-server` 这个文件夹整体称作一个 Port，由 `distinfo`（校验和文件）、`pkg-descr`（软件描述文件）、`Makefile`	（主文件，包含构建方法、版本号及下载方式等）、`pkg-plist`（安装文件列表及其权限和属组信息）、`files`（一般为补丁文件，该 Port 下还包含安装后的说明文件 `pkg-message`）等文件构成。

之所以称为“Ports Collection”，移植集合（不应理解为端口集合，参见 [What does 'port' mean in 'develop a port of BSD'?](https://www.reddit.com/r/linuxquestions/comments/ll2q6j/what_does_port_mean_in_develop_a_port_of_bsd)，注：此来源不可信，请求其他来源）是因为这些软件绝大部分并不由 FreeBSD 控制、管理和维护。Port 提交者主要做的事情是将 FreeBSD 上 Port 更新到上游开发者提供的最新版本，删除上游不再维护的软件 Port。在上游不接受 BSD 特有的 PR 补丁或难以直接通过既有 Ports 框架实现构建的情况下，Port 维护者也需要自行复刻一个分支出来维护（如 [editors/vscode](https://github.com/tagattie/FreeBSD-VSCode)）。

## Ports 构建 pkg 软件包的流程

> **注意**
>
> ports 和 pkg 可以同时使用，而且大部分人也是这么用的。但是要注意 pkg 的源必须是 latest，否则会存在一些依赖上的问题（比如 ssl）。latest 源也比 main 分支上的 Ports 发布得更晚（其软件包由 main 构建而来），因此即使使用 latest 源，也可能会出现上述问题，总之有问题出现时就卸载那个 pkg 安装的包，重新使用 ports 编译即可。

>**警告**
>
>需要对上面的“注意”进行补充说明的是：一旦你使用了 `make config` 修改了 Port 的默认构建参数（进行了自定义），那么如果你仍然想保留该设置，后续的软件更新是不能通过 pkg 进行管理的，否则通过 pkg 安装的软件包会完全取代之前自定义的 Port（即 Port 开发者默认设定的构建参数将覆盖你自定义的 Port 参数）。

![Ports 流程图](../.gitbook/assets/ports-pkg.png)


>**技巧**
>
>Ports 的下载路径是 `/usr/ports/distfiles/`。


## 使用 ports 压缩包

使用压缩包可以规避“先有鸡还是先有蛋”的问题（例如需要安装 Git，但系统中既没有 Ports 又不想使用 pkg 的情况）。

### 下载 ports 压缩包

- NJU:

```sh
# fetch https://mirrors.nju.edu.cn/freebsd-ports/ports.tar.gz
```

- 或 USTC

```sh
# fetch https://mirrors.ustc.edu.cn/freebsd-ports/ports.tar.gz
```

- 又或 FreeBSD 官方

```sh
# fetch https://download.freebsd.org/ftp/ports/ports/ports.tar.gz
```

### 解压 ports 压缩包


```sh
# tar -zxvf ports.tar.gz -C /usr/ # 解压至路径
# rm ports.tar.gz # 删除存档
```

## 使用 Git 获取 Ports

### 安装 Git

使用 pkg 安装：

```sh
# pkg install git
```

### 拉取 Ports 存储库（USTC）浅克隆

```sh
# git clone --filter=tree:0 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git /usr/ports
```

### 拉取 Ports 存储库（FreeBSD 官方）浅克隆

```sh
# git clone --filter=tree:0 https://git.FreeBSD.org/ports.git /usr/ports
```

### 完全拉取 Ports 存储库（FreeBSD 官方）并指定分支

```sh
# git clone https://git.FreeBSD.org/ports.git /usr/ports
```

查看所有分支：

```sh
# cd /usr/ports/ # 切换到 git 项目
# git branch -a	# 打印 git 分支
* main # * 代表当前分支
  remotes/origin/2014Q1

	……省略…………

  remotes/origin/2025Q1
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```

切换到 `2025Q1` 分支：

```sh
# git switch 2025Q1
正在更新文件: 100% (14323/14323), 完成.
分支 '2025Q1' 设置为跟踪 'origin/2025Q1'。
切换到一个新分支 '2025Q1'
```

查看本地分支：

```sh
# git branch
* 2025Q1
  main
```

Git 分支已经切换成功。


### 同步更新 Ports Git

```sh
# cd /usr/ports/ # 切换目标目录
# git pull # 同步更新上游 Ports
```

如果提示本地已经修改，放弃本地修改，再更新：

```sh
# git checkout . # 放弃本地修改
# git pull
```

### 附录：时间错误导致的证书无效

报错形似：

```sh
fatal: unable to access 'https://mirrors.ustc.edu.cn/freebsd-ports/ports.git/': SSL certificate problem: certificate is not yet valid
```

先检查系统的时间：

```sh
# date
Fri May 31 12:09:26 UTC 2024
```

时间错误。使用 `pool.ntp.org` 服务器同步系统时间：


```sh
# ntpdate -u pool.ntp.org
 5 Oct 08:39:16 ntpdate[3276]: step time server 202.112.29.82 offset +10960053.088901 sec
```

检查时间：

```sh
# date
Sat Oct  5 08:39:21 UTC 2024
```

## 使用 `whereis` 查询软件路径

查找 python 可执行文件、源代码及手册页所在路径：

```sh
# whereis python
```

将输出

```sh
python: /usr/ports/lang/python
```

## 查看软件包依赖

在已经安装该软件包的情况下：

```sh
# pkg info -d screen
screen-4.9.0_6:
	indexinfo-0.3.1
```

在未安装该软件包的情况下：

```sh
root@ykla:/usr/ports/sysutils/htop # make all-depends-list
/usr/ports/ports-mgmt/pkg
/usr/ports/devel/pkgconf
/usr/ports/devel/kyua
……省略一部分……
```

## 看看 python 的 ports 在哪个位置

查找 python 可执行文件、源代码及手册页所在路径：

```sh
# whereis python
python: /usr/ports/lang/python
```

## 安装 python3

```sh
# cd /usr/ports/lang/python
# make BATCH=yes clean
```

其中 `BATCH=yes` 意味着使用默认参数进行构建。

## 如何设置全部所需的依赖

```sh
# make config-recursive
```

## 如何使用 pkg 安装依赖

不使用 Ports 来编译依赖，仅使用 Ports 来编译软件包本体：

```sh
# make install-missing-packages
```

以 `chinese/fcitx` 为示例：

```sh
# cd /usr/ports/chinese/fcitx
# make install-missing-packages
Updating FreeBSD repository catalogue...
FreeBSD repository is up to date.
Updating FreeBSD-base repository catalogue...
FreeBSD-base repository is up to date.
All repositories are up to date.
Updating database digests format: 100%
The following 2 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
	e2fsprogs-libuuid: 1.47.1 [FreeBSD]
	enchant2: 2.2.15_5 [FreeBSD]

Number of packages to be installed: 2

94 KiB to be downloaded.

Proceed with this action? [y/N]: 
```

## 如何删除当前 port 及其依赖的配置文件

```sh
# make rmconfig-recursive
```

## 如何一次性下载所有需要的软件包

```sh
# make BATCH=yes fetch-recursive
```

## ports 编译的软件也可以转换为 pkg 包

```sh
# pkg create nginx
```

## 更新 FreeBSD 软件包/Port

先同步更新 Ports Git。

然后列出过时 Port 软件：

```sh
# pkg version -l '<'
chromium-127.0.6533.99             <
curl-8.9.1_1                       <
ffmpeg-6.1.2,1                     <
vlc-3.0.21_4,4                     <
w3m-0.5.3.20230718_1               <
```

下面分别列出 FreeBSD 手册中提及的两种升级工具：

### ① portmaster（推荐）

- 更新已安装的 Port：

```sh
# cd /usr/ports/ports-mgmt/portmaster && make install clean	# 安装 portmaster
# portmaster -a # 自动升级所有软件
# portmaster screen # 升级单个软件
```

如果不想回答问题解决依赖，可使用类似 BATCH=yes 的选项 `-a -G --no-confirm`：

```sh
# portmaster -a -G --no-confirm
```

#### 查看 Port 依赖关系

```sh
# portmaster sysutils/htop  --show-work

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

### ② portupgrade

```sh
# cd /usr/ports/ports-mgmt/portupgrade && make install clean
# portupgrade -ai # 自动升级所有软件，i 会挨个确认
# portupgrade -R screen # 升级单个软件
# portupgrade -a --batch		# 不询问，直接执行，等同于 BATCH=yes
```

#### 参考资料

- [portmaster -- manage your ports without external databases or languages](https://man.freebsd.org/cgi/man.cgi?portmaster(8))
- [portupgrade,  portinstall -- tools to upgrade installed packages	or in- stall new ones via ports	or packages](https://man.freebsd.org/cgi/man.cgi?portupgrade(1))
  

## FreeBSD USE

### 如何全局屏蔽 MYSQL

```sh
# echo "OPTION_UNSET+= MYSQL" >> /etc/make.conf
```

完整的 USE 列表见 <https://cgit.freebsd.org/ports/tree/Mk/bsd.default-versions.mk>。

## FreeBSD ports 多线程编译

将以下内容写入 `/etc/make.conf`，若不存在则 `touch` 新建对应文件。

```ini
FORCE_MAKE_JOBS=yes       # 强制启用并行编译
MAKE_JOBS_NUMBER=4        # 设置并行编译的作业数为 4
```

在 Linux（如 Gentoo）上，一般直接使用 `-jX` 或 `-j(X+1)`，其中 `X` 为核心数。

`4` 表示处理器的并行编译数（通常对应核心数或线程数）。

可以通过命令查看系统检测到的 CPU 核心数量：

```sh
# sysctl kern.smp.cpus
kern.smp.cpus: 16
```

或者查看系统可用的 CPU 核心数：

```sh
# sysctl hw.ncpu 
hw.ncpu: 16
```

输出值即可作为 `MAKE_JOBS_NUMBER` 的取值。

英特尔的处理器搜索 `CPU 型号 ARK` 跳转到英特尔官网可查询线程数。

个别情况下可以通过设置别名加速编译（非永久设置，FreeBSD 14 默认已生效，无须额外设置）：

```ini
# alias ninja='ninja -j4'	# 为 ninja 命令设置别名，指定并行编译 4 个作业
```

### 参考资料

- [Easy way to get cpu features](https://forums.freebsd.org/threads/easy-way-to-get-cpu-features.10553/)，获取 CPU 线程数量的命令来自此处。

## 设置内存为 `tmp`

编辑 `/etc/fstab` 文件，写入下行：

```ini
tmpfs /tmp tmpfs rw 0 0
```

`reboot` 重启即可。

### 参考资料

- [tmpfs --in-memory file system](https://man.freebsd.org/cgi/man.cgi?tmpfs(5))

## ccache

>**警告**
>
>使用 ccache 可能会导致编译失败。它仅在重复编译时才有效，首次编译不仅不会加速，反而可能更慢，是一种以空间换时间的手段。


### ccache3

使用 pkg 安装：

```sh
# pkg install ccache
```

- 使用 Ports 安装：

```sh
# cd /usr/ports/devel/ccache/ 
# make install clean
```

- 查看软链接情况：

```sh
# ls -al /usr/local/libexec/ccache
total 56
drwxr-xr-x   3 root wheel 15 Sep 20 02:02 .
drwxr-xr-x  18 root wheel 49 Sep 20 01:39 ..
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 CC -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 c++ -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 cc -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 clang -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 clang++ -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 clang++15 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 02:02 clang++18 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 clang15 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 02:02 clang18 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 cpp13 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 g++13 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 gcc13 -> /usr/local/bin/ccache
drwxr-xr-x   2 root wheel 15 Sep 20 02:02 world
```

---

- 修改 `/etc/make.conf` 文件，加入下面一行启用 ccache 加速编译：

```ini
WITH_CCACHE_BUILD=yes
```

- 设置 ccache 编译缓存最大为 10GB：

```sh
# ccache -M 10G  
Set cache size limit to 10.0 GB
root@ykla:/usr/ports/www/chromium # ccache -s
cache directory                     /root/.ccache
primary config                      /root/.ccache/ccache.conf
secondary config      (readonly)    /usr/local/etc/ccache.conf
cache hit (direct)                     0
cache hit (preprocessed)               0
cache miss                             0
cache hit rate                      0.00 %
cleanups performed                     0
files in cache                         0
cache size                           0.0 kB
max cache size                      10.0 GB
```

- 在 Ports 编译一段时间后显示 ccache 的统计信息：

```sh
# ccache -s
cache directory                     /root/.ccache
primary config                      /root/.ccache/ccache.conf
secondary config      (readonly)    /usr/local/etc/ccache.conf
stats updated                       Fri Sep 20 02:05:35 2024
cache hit (direct)                    20
cache hit (preprocessed)              17
cache miss                           918
cache hit rate                      3.87 %
called for link                      121
called for preprocessing              26
compile failed                       115
preprocessor error                    66
bad compiler arguments                15
autoconf compile/link                523
no input file                         71
cleanups performed                     0
files in cache                      2305
cache size                           0.0 kB
max cache size                      10.0 GB
```

### ccache4

目前的最新版本是 ccache4：

使用 pkg 安装：

```sh
# pkg install ccache4
```

或使用 Ports 安装：

```sh
# cd /usr/ports/devel/ccache4/
# make install clean
```

- 查看软链接情况：

```sh
# ls -al  /usr/local/libexec/ccache    total 55	# 查看 /usr/local/libexec/ccache 目录下的详细文件信息
drwxr-xr-x   3 root wheel 13  9月 20 02:29 .
drwxr-xr-x  20 root wheel 54  9月 20 02:29 ..
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 c++ -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 cc -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 CC -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 clang -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 clang++ -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 clang++15 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 clang15 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 cpp13 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 g++13 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 gcc13 -> /usr/local/bin/ccache
drwxr-xr-x   2 root wheel 13  9月 20 02:29 world
```

---

- 修改 `/etc/make.conf` 文件，加入下面一行启用 ccache 加速编译：

```sh
WITH_CCACHE_BUILD=yes
```

- 设置编译缓存最大为 20GB：

```sh
# ccache -M 20G  
Set cache size limit to 20.0 GB
```

- 在 Ports 编译一段时间后，查看编译缓存：

```sh
# ccache -s
Cacheable calls:   558 /  579 (96.37%)
  Hits:            110 /  558 (19.71%)
    Direct:        110 /  110 (100.0%)
    Preprocessed:    0 /  110 ( 0.00%)
  Misses:          448 /  558 (80.29%)
Uncacheable calls:  21 /  579 ( 3.63%)
Local storage:
  Cache size (GB): 0.0 / 20.0 ( 0.11%)
  Hits:            110 /  558 (19.71%)
  Misses:          448 /  558 (80.29%)
```

显示 ccache 的当前配置参数：

```sh
# ccache -p 
(default) absolute_paths_in_stderr = false
(default) base_dir =
(default) cache_dir = /root/.cache/ccache
……省略一部分……
```

### 参考文献

- [ccache-howto-freebsd.txt.in](https://github.com/freebsd/freebsd-ports/blob/main/devel/ccache/files/ccache-howto-freebsd.txt.in)
- [ccache -a fast C/C++ compiler cache](https://man.freebsd.org/cgi/man.cgi?query=ccache&sektion=1&n=1)

## 多线程下载

### axel

使用 pkg 安装：

```sh  
# pkg install axel
```

或者使用 ports 安装：

```sh
# cd /usr/ports/ftp/axel/
# make install clean
```

新建或者编辑 `/etc/make.conf` 文件，写入以下几行：

```ini
FETCH_CMD=axel                # 设置使用 axel 作为下载工具
FETCH_BEFORE_ARGS=-n 10 -a    # 设置 axel 下载前的参数：使用 10 个线程并启用自动模式
FETCH_AFTER_ARGS=              # 下载后执行的命令参数为空
DISABLE_SIZE=yes               # 禁用文件大小检查
```

### wget2
  

使用 Ports 安装：

```sh
# cd /usr/ports/www/wget2/ && make install clean
```

新建或者编辑 `/etc/make.conf` 文件，写入以下几行：

```ini
FETCH_CMD=wget2               # 设置使用 wget2 作为下载工具
FETCH_BEFORE_ARGS=-c -t 3 --max-threads=16 # 设置 wget2 下载前的参数
FETCH_AFTER_ARGS=             # 下载后执行的命令参数为空
DISABLE_SIZE=yes              # 禁用文件大小检查
```

wget2 参数说明：

- `-c` 断点续传
- `-t 3` 重试次数 3
- `--max-threads=16` 将最大并发下载线程数设为 16，默认为 5

>**技巧**
>
>请注意很多服务器不支持较多线程同时下载。同时会给服务器带来较大压力，也可能会触发服务器的反制措施，如将下载的 IP 拉入黑名单。

### 参考文献

- [ports --contributed applications](https://man.freebsd.org/cgi/man.cgi?query=ports&sektion=7)，`FETCH_CMD` 的出处，同时也是参数 `BATCH` 的出处。


## 故障排除与未竟事宜

### `autoconf-2.72 Invalid perl5 version 5.42.`

也可以将其理解为“xxx-yy Invalid zz version aa”这一类报错。

实例，在使用 Ports 安装 openjdk21 时报错如下：

```sh
[root@Server /usr/ports/java/openjdk21]# make install clean
===> openjdk21-21.0.4+7.1 depends on executable: zip - found
===> openjdk21-21.0.4+7.1 depends on package: autoconf>0 - not found ①
===> autoconf-2.72 Invalid perl5 version 5.42. ②
*** Error code 1

Stop.
make[1]: stopped in /usr/ports/devel/autoconf
*** Error code 1

Stop.
make: stopped in /usr/ports/java/openjdk21
```

观察整个流程可以发现，openjdk21 依赖 autoconf，但系统中没有。于是递归查找 autoconf 的依赖，发现 autoconf 依赖 perl5；结合 ② 可以发现系统中已有 perl5，但是报错“Invalid version”，即 perl5 的版本不对。

此问题一般需要先更新 Ports，然后通过 `pkg install -f perl5` 或 `pkg upgrade` 更新 perl5 的版本即可解决。

#### 参考文献

- [Invalid perl5 version 5.32](https://forums.freebsd.org/threads/invalid-perl5-version-5-32.77628/)，出现了同样的问题
