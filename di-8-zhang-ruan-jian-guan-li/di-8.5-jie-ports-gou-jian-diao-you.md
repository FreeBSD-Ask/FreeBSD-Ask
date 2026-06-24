# 8.5 Ports 构建调优

## FreeBSD Ports 多线程编译

为加快编译速度，可配置多线程编译选项，利用多核处理器的性能。

将以下内容写入 **/etc/make.conf** 文件，若不存在则 `touch` 新建对应文件。

```ini
FORCE_MAKE_JOBS=yes       # 强制启用并行编译
MAKE_JOBS_NUMBER=4        # 设置并行编译的作业数为 4
```

在 Linux（如 Gentoo）上，一般直接使用 `-jX` 或 `-j(X+1)`，`X` 为核心数。

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

输出值即可作为 `MAKE_JOBS_NUMBER` 取值。

搜索英特尔处理器型号加 `ARK`，可跳转至英特尔官网查询线程数。

- FreeBSD Project. SMP -- symmetric multiprocessing kernel subsystem[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?query=SMP&sektion=4>. SMP 子系统中 kern.smp.cpus 与 hw.ncpu 等 sysctl 变量的文档。

## 将 /tmp 设置为内存文件系统

为提高临时文件的读写速度，可将 **/tmp** 目录挂载为内存文件系统 tmpfs。

编辑 **/etc/fstab** 文件，写入下行：

```ini
tmpfs /tmp tmpfs rw 0 0
```

`reboot` 重启即可。

### 参考文献

- FreeBSD Project. tmpfs -- in-memory file system[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?query=tmpfs&sektion=4>. 内存文件系统 tmpfs 的官方技术规范。

## 使用 ccache 编译缓存

ccache 是一款编译缓存工具，可加速重复编译的过程。

> **警告**
>
> 使用 ccache 可能会导致编译失败。它仅在重复编译时才有效，首次编译不仅不会加速，反而可能更慢，是一种以空间换时间的手段。

```sh
ccache 工作原理

  首次编译（Cache Miss）：
    源代码 ──► ccache ──► 编译器 ──► 目标文件          　　　　　　　　　　　　　　　　　　　　　
                  │　
                  └──► 存入缓存    　　　　　

  重复编译（Cache Hit）：
    源代码 ──► ccache ──► 直接输出目标文件           　　　　　　　　　　　　　　　　
                  │　
                  └──► 命中缓存（跳过编译）          　　　　　
```

ccache3 是一个常用的版本。

### 安装 ccache3

使用 pkg 安装：

```sh
# pkg install ccache
```

- 使用 Ports 安装：

```sh
# cd /usr/ports/devel/ccache/
# make install clean
```

安装完成后，可以查看 ccache 创建的软链接：

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

#### 配置 ccache3

配置 ccache 以启用编译缓存：

- 修改 **/etc/make.conf** 文件，加入下面一行启用 ccache 加速编译：

```ini
WITH_CCACHE_BUILD=yes
```

为了避免缓存占用过多磁盘空间，建议设置缓存大小上限。

- 设置 ccache 编译缓存最大为 10 GB：

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

在使用一段时间后，可以查看 ccache 的统计信息，了解缓存的命中情况。

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

### 安装 ccache4

ccache4 是 ccache 的较新主版本，安装与配置方式与 ccache3 相同，仅包名不同。

使用 pkg 安装：

```sh
# pkg install ccache4
```

或使用 Ports 安装：

```sh
# cd /usr/ports/devel/ccache4/
# make install clean
```

#### 配置 ccache4

软链接与 **/etc/make.conf** 配置均与 ccache3 一致，不再赘述。ccache4 的输出格式略有不同：

- 设置编译缓存最大为 20 GB：

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

显示 ccache4 的当前配置参数：

```sh
# ccache -p
(default) absolute_paths_in_stderr = false
(default) base_dir =
(default) cache_dir = /root/.cache/ccache
……省略一部分……
```

### 参考文献

关于 ccache 的更多详细信息和使用方法，可以参考以下资料。

- FreeBSD Project. ccache-howto-freebsd.txt.in[EB/OL]. [2026-03-25]. <https://github.com/freebsd/freebsd-ports/blob/main/devel/ccache/files/ccache-howto-freebsd.txt.in>. FreeBSD Ports 中 ccache 的配置指南，说明如何在编译时启用缓存加速。
- FreeBSD Project. ccache - a fast C/C++ compiler cache[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?query=ccache&sektion=1&n=1>.

## 多线程下载

为加快 Ports 源代码的下载速度，可使用多线程下载工具。

### axel

axel 是一款轻量级的多线程下载工具，可显著提高下载速度。

使用 pkg 安装：

```sh
# pkg install axel
```

或者使用 Ports 安装：

```sh
# cd /usr/ports/ftp/axel/
# make install clean
```

安装完成后，需要配置 Ports 框架使用 axel 作为下载工具。

新建或者编辑 **/etc/make.conf** 文件，写入以下几行：

```ini
FETCH_CMD=axel                # 设置使用 axel 作为下载工具
FETCH_BEFORE_ARGS=-n 10 -a    # 设置 axel 下载前的参数：使用 10 个线程并显示替代进度条
FETCH_AFTER_ARGS=              # 下载后执行的命令参数为空
DISABLE_SIZE=yes               # 禁用文件大小检查
```

### wget2

使用 Ports 安装：

```sh
# cd /usr/ports/www/wget2/ && make install clean
```

新建或者编辑 **/etc/make.conf** 文件，写入以下几行：

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

> **技巧**
>
> 很多服务器不支持较多线程同时下载。这会给服务器带来较大压力，也可能会触发服务器的反制措施，如将下载的 IP 加入黑名单。

### 参考文献

- FreeBSD Project. ports -- contributed applications[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?query=ports&sektion=7>. Ports 框架的官方文档，包含 FETCH_CMD 与 BATCH 等参数说明。
