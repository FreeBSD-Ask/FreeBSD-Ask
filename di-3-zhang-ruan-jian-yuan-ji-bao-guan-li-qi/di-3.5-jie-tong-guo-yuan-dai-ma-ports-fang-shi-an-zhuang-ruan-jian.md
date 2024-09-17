# 第 3.5 节 使用 ports 以源代码方式安装软件

> **注意**
>
> ports 和 pkg 可以同时使用，而且大部分人也是这么用的。但是要注意 pkg 的源必须是 latest，否则会存在一些依赖上的问题（比如 ssl）。latest 的源也比主线上的 ports 要出来的晚（是从中编译出来的），因此即使是 latset 源也可能会出现上述问题，总之有问题出现时就卸载那个 pkg 安装的包，重新使用 ports 编译即可。

## FreeBSD ports 基本用法

### 首先使用 Git 获取 Ports（其他方法参见前节）

安装 Git：
```sh
# pkg install git
```

或者：

```sh
# cd /usr/ports/devel/git
# make install clean
```

拉取 Ports 存储库：

```sh
# git clone --filter=tree:0 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git /usr/ports
```

#### 同步更新 Ports Git


```sh
root@ykla:/ # cd /usr/ports/ #切换目标目录
root@ykla:/usr/ports # git pull #同步更新上游 Ports
```

如果提示本地已经修改，放弃本地修改，再更新：

```sh
root@ykla:/usr/ports # git checkout . #放弃本地修改
root@ykla:/usr/ports # git pull
```

### 使用 `whereis` 查询软件路径

如 

```sh
# whereis python
```

将输出 

```sh
python: /usr/ports/lang/python
```

### 如何安装 python3：

```sh
# cd /usr/ports/lang/python
# make BATCH=yes clean
```

其中 `BATCH=yes` 意味着使用默认参数进行编译。

## 加速编译

### FreeBSD ports 多线程编译（推荐）


- FreeBSD ports 多线程编译

将以下内容写入 `/etc/make.conf`，没有就 `touch` 新建一个。

```json
FORCE_MAKE_JOBS=yes
MAKE_JOBS_NUMBER=4
```
Linux 如 Gentoo 上一般是直接 `-jx` 或者 `jx+1`, `x` 为核心数。

`4` 是处理器核心数（还是线程数？），不知道就别改。英特尔的处理器搜索 `CPU 型号+ARK` 转跳英特尔官网可查询线程数。

- 个别情况下可以设置别名加速编译：（非永久设置，FreeBSD 14 无须设置默认即生效）

```sh
# alias ninja='ninja -j4'
```

### 设置内存为 `tmp`

```sh
# ee /etc/fstab
```

写入：

```sh
tmpfs /tmp tmpfs rw 0 0
```

重启即可。

#### 参考资料

- [tmpfs --in-memory file system](https://man.freebsd.org/cgi/man.cgi?tmpfs(5))


### ccache

>**警告**
>
>默认的自动化配置工具无论是 ccahe3 还是 4 都有问题，需要手动配置如下，参见 [Bug](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=272917)

>**警告**
>
>使用 ccache 可能会导致编译失败！只在重复编译时起效果，首次编译不仅不会加速还会慢上一些。是一种以空间换时间的行为。


目前最新版本是 ccache4：

```sh
# pkg install ccache4
```

或

```sh
# cd /usr/ports/devel/ccache4/
# make install clean
```

配置：

```sh
ln -s ccache	/usr/local/bin/gcc
ln -s ccache	/usr/local/bin/g++
ln -s ccache	/usr/local/bin/cc
ln -s ccache	/usr/local/bin/c++
ln -s ccache	/usr/local/bin/clang
```

设置编译缓存最大为 5GB：

```sh
root@ykla:/usr/ports/devel/ccache4 # ccache -M 20G  
Set cache size limit to 20.0 GB
```

编译一段时间后，查看编译缓存：

```sh
root@ykla:/ # ccache -s
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

查看当前配置文件：

```sh
root@ykla:~ # ccache -p 
(default) absolute_paths_in_stderr = false
(default) base_dir =
(default) cache_dir = /root/.cache/ccache
(default) compiler =
(default) compiler_check = mtime
(default) compiler_type = auto
(default) compression = true
(default) compression_level = 0
(default) cpp_extension =
(default) debug = false
(default) debug_dir =
(default) debug_level = 2
(default) depend_mode = false
(default) direct_mode = true
(default) disable = false
(default) extra_files_to_hash =
(default) file_clone = false
(default) hard_link = false
(default) hash_dir = true
(default) ignore_headers_in_manifest =
(default) ignore_options =
(default) inode_cache = true
(default) keep_comments_cpp = false
(default) log_file =
(default) max_files = 0
(/root/.config/ccache/ccache.conf) max_size = 20.0 GB #配置文件路径
(default) msvc_dep_prefix = Note: including file:
(default) namespace =
(default) path =
(default) pch_external_checksum = false
(default) prefix_command =
(default) prefix_command_cpp =
(default) read_only = false
(default) read_only_direct = false
(default) recache = false
(default) remote_only = false
(default) remote_storage =
(default) reshare = false
(default) run_second_cpp = true
(default) sloppiness =
(default) stats = true
(default) stats_log =
(default) temporary_dir = /root/.cache/ccache/tmp
(default) umask =
```


#### 参考文献

- [ccache-howto-freebsd.txt.in](https://github.com/freebsd/freebsd-ports/blob/main/devel/ccache/files/ccache-howto-freebsd.txt.in)
- [ccache -a fast C/C++ compiler cache](https://man.freebsd.org/cgi/man.cgi?query=ccache&sektion=1&n=1)

### 如何使用多线程下载：

- axel

安装：

```sh  
# pkg install axel
```

或者
```sh
# cd /usr/ports/ftp/axel/
# make install clean
```

新建或者编辑 `/etc/make.conf` 文件，写入以下几行：

```sh
FETCH_CMD=axel
FETCH_BEFORE_ARGS= -n 10 -a
FETCH_AFTER_ARGS=
DISABLE_SIZE=yes
```

- wget2
  
>**警告**
>
>wget2 正在进行测试！先不要用
  
```sh
# cd /usr/ports/www/wget2/ && make install clean
```
新建或者编辑 `# ee /etc/make.conf` 文件，写入以下几行：
```sh
FETCH_CMD=wget2
FETCH_BEFORE_ARGS= -c -t 3 -o 10
FETCH_AFTER_ARGS=
DISABLE_SIZE=yes
```

- `-c` 断点续传；
- `-t 3` 重试次数 3；
- ` -o 10` 启用 10 个线程进行下载。

>**技巧**
>
>`10` 这个参数可能过于保守，我一般直接用 `50` 或 `100`。但是要注意很多服务器不支持这么多线程同时下载。因为可能会给服务器带来较大压力。


### 参考文献

- [ports --	contributed applications](https://man.freebsd.org/cgi/man.cgi?query=ports&sektion=7)，`FETCH_CMD` 的出处
## 进阶

如果不选择 `BATCH=yes` 的方法手动配置：

看看 python 的 ports 在哪：

```sh
# whereis python
# python: /usr/ports/lang/python
```

安装 python3：

```sh
# cd /usr/ports/lang/python
```

如何设置全部所需的依赖：

```sh
# make config-recursive
```

如何删除当前 port 及其依赖的配置文件：

```sh
# make rmconfig-recursive
```

如何一次性下载所有需要的软件包：

```sh
# make BATCH=yes fetch-recursive
```

升级 ports

```sh
# portsnap auto
```

ports 编译的软件也可以转换为 pkg 包

```sh
# pkg create nginx
```

## FreeBSD 包升级管理工具

同步更新 Ports Git。

然后列出过时 Port 软件：

```sh
root@ykla:/usr/ports # pkg version -l '<'
aom-3.10.0                         <
chromium-127.0.6533.99             <
curl-8.9.1_1                       <
expat-2.6.2                        <
ffmpeg-6.1.2,1                     <
firefox-esr-115.15.0,1             <
gdal-3.9.2                         <
geos-3.12.2                        <
imlib2-1.12.3,2                    <
kf5-kimageformats-5.116.0          <                   
libjxl-0.10.3                      <                    
libphonenumber-8.13.45             <                    
librsvg2-rust-2.58.3_2             <                    
libxml2-2.11.8                     <                    
liveMedia-2022.06.16,2             <                    
llvm18-18.1.8_1                    <
marble-23.08.5_2                   <
mosh-1.4.0_3                       <
protobuf-27.3_1,1                  <
py311-build-1.2.1                  <
py311-libxml2-2.11.8_1             <
py311-mdit-py-plugins-0.4.1        <
py311-pbr-6.0.0                    <
ruby-3.2.4,1                       <
rust-bindgen-cli-0.70.1_1          <
sdl2_image-2.8.2_1                 <
texlive-texmf-20240312             <
vlc-3.0.21_4,4                     <
w3m-0.5.3.20230718_1               <
```

下边分别列出 2 种 FreeBSD 手册中提及的升级工具:

1、portupgrade

```sh
# cd /usr/ports/ports-mgmt/portupgrade && make install clean
# portupgrade -ai #自动升级所有软件
# portupgrade -R screen #升级单个软件
# portupgrade -ai --batch		#不要问，只做，等同于  BATCH=yes
```

2、portmaster （推荐）

- 更新：

```sh
# cd /usr/ports/ports-mgmt/portmaster && make install clean
# portmaster -a #自动升级所有软件
# portmaster screen #升级单个软件
```

如果不想回答问题解决依赖，可使用类似 BATCH=yes 的选项 `-a -G --no-confirm`：

```sh
# portmaster -a -G --no-confirm
```

- 查看依赖关系：

```sh
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

### 参考资料

- [portmaster -- manage your ports without external databases or languages](https://man.freebsd.org/cgi/man.cgi?portmaster(8))
- [portupgrade,  portinstall -- tools to upgrade installed packages	or in- stall new ones via ports	or packages](https://man.freebsd.org/cgi/man.cgi?portupgrade(1))
  
## FreeBSD USE

- 如何指定 Ports 编译的版本？

如 Python 现在的默认编译版本是 3.9，要改为 3.11，：

```sh
# echo "DEFAULT_VERSIONS+= python=3.11  python3=3.11" >> /etc/make.conf
```
>如果只设置了单个参数，那么出现警告是正常的，见 [Bug](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=243034)
>```sh
>/!\ WARNING /!\
>
>PYTHON_DEFAULT must be a version present in PYTHON2_DEFAULT or PYTHON3_DEFAULT,
>if you want more Python flavors, set BUILD_ALL_PYTHON_FLAVORS in your make.conf
>```


完整的列表见 <https://cgit.freebsd.org/ports/tree/Mk/bsd.default-versions.mk>

### 参考资料

- [Ports/DEFAULT_VERSIONS](https://wiki.freebsd.org/Ports/DEFAULT_VERSIONS)
- [Python](https://wiki.freebsd.org/Python)


- 如何全局屏蔽 mysql

```sh
# echo "OPTION_UNSET+= MYSQL" >> /etc/make.conf
```

## 查看依赖

已经安装：

```sh
root@ykla:~ # pkg info -d screen
screen-4.9.0_6:
	indexinfo-0.3.1
```

未安装：

```sh
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

