# 6.4 使用 Ports 以源代码方式安装软件

Ports 是 FreeBSD 从源代码构建软件的框架，适用于需要自定义编译选项、打补丁或安装 pkg 仓库中未收录的软件。

## 获取 Ports

使用压缩包可以规避“先有鸡还是先有蛋”的问题（例如需要安装 Git，但系统中既没有 Ports 又不想使用 pkg 的情况）。

### 使用 Ports 压缩包

可以从多个镜像源下载 Ports 压缩包，下面列出了几个常用的源地址。

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

#### 解压 Ports 压缩包

下载完成后，需要将压缩包解压到指定位置。

```sh
# tar -zxvf ports.tar.gz -C /usr/ # 解压至路径
# rm ports.tar.gz # 删除存档
```

### 使用 Git 获取 Ports

Git 是获取 Ports 源代码的推荐方式，可以方便地管理版本和更新。

#### 安装 Git

首先需要安装 Git 工具，以便能够拉取源代码。

使用 pkg 安装：

```sh
# pkg install git
```

#### 拉取 Ports 存储库（USTC）的浅克隆

中国科学技术大学提供了 FreeBSD Ports 的镜像源，可以使用浅克隆的方式快速获取代码。

```sh
# git clone --filter=tree:0 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git /usr/ports
```

> **注意**
>
> `--depth 1`（仅拉取最新的日志和提交记录）会给服务器带来较大计算压力，请尽量使用参数 `--filter=tree:0` 拉取。

#### 拉取 Ports 存储库（FreeBSD 官方）浅克隆

也可以直接从 FreeBSD 官方仓库获取源代码。

```sh
# git clone --filter=tree:0 https://git.FreeBSD.org/ports.git /usr/ports
```

#### 完全拉取 Ports 存储库（FreeBSD 官方）并指定分支

如果需要完整的提交历史和所有分支，可以完整克隆。

```sh
# git clone https://git.FreeBSD.org/ports.git /usr/ports
```

关于 quarterly 分支与 latest（main）分支的详细说明，参见第 6.1 节。根据需要，可以切换到特定的分支，例如季度分支。

切换到 `2025Q1` 分支：

```sh
# git switch 2025Q1
正在更新文件: 100% (14323/14323), 完成.
分支 '2025Q1' 设置为跟踪 'origin/2025Q1'。
切换到一个新分支 '2025Q1'
```

切换完成后，可以查看本地分支以确认。

查看本地分支：

```sh
# git branch
* 2025Q1
  main
```

Git 分支已经切换成功。

#### 同步更新 Ports Git

获取 Ports 源代码后，需要定期同步更新以获取最新的修改。

```sh
# cd /usr/ports/ # 切换目标目录
# git pull -p # 同步更新上游 Ports（-p/--prune 用于清理远程已删除的端口）
```

如果提示本地已经修改，可以放弃本地修改后再更新：

```sh
# git restore .
# git pull -p
```

#### 附录：因时间错误导致的证书无效

在使用 Git 拉取代码时，可能会遇到 SSL 证书问题（报错形如 `SSL certificate problem: certificate is not yet valid`），常见原因是系统时间不正确。使用 `ntpd -q -g pool.ntp.org` 同步系统时间即可解决。详细说明参考本书其他相关章节。

## 使用 `whereis` 查询软件路径

`whereis` 命令可以帮助快速查找软件的可执行文件、源代码及手册页所在路径。

查找 python 可执行文件、源代码及手册页所在路径：

```sh
# whereis python
```

将输出：

```sh
python: /usr/ports/lang/python
```

## 查看软件包依赖

查看软件包依赖关系的方法如下。可在软件已安装或未安装的情况下查看其依赖。

在已安装该软件包的情况下：

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
……省略一部分……
```

## 如何删除当前 Port 及其依赖的配置文件

如果需要清理之前配置的选项，可以使用以下命令删除当前 Port 及其所有依赖的配置文件。该命令递归遍历依赖树，逐个清除每个 Port 的 `make config` 设置，恢复为默认构建参数。

```sh
# make rmconfig-recursive
```

## 如何一次性下载所有需要的软件包

为了避免在编译过程中因网络问题中断，可以先一次性下载所有需要的软件包。`fetch-recursive` 会递归获取主 Port 及其全部依赖的源代码包，配合 `BATCH=yes` 跳过交互式选项。

```sh
# make BATCH=yes fetch-recursive
```

## Ports 编译的软件也可以打包为 pkg 包

使用 Ports 编译安装的软件也可以打包为 pkg 格式的二进制包，方便在其他机器上部署，避免重复编译。打包后的文件默认输出至当前目录，可拷贝到目标机器后用 `pkg add` 安装。

```sh
# pkg create nginx
```

## 更新 FreeBSD 软件包/Port

更新前需要先同步更新 Ports Git。

随后列出过时的 Port 软件：

```sh
# pkg version -l '<'
chromium-127.0.6533.99             <
curl-8.9.1_1                       <
ffmpeg-6.1.2,1                     <
vlc-3.0.21_4,4                     <
w3m-0.5.3.20230718_1               <
```

### 安装 portmaster

portmaster 是一款常用的 Ports 更新工具，可以帮助管理和更新已安装的软件。

- 更新已安装的 Port：

```sh
# cd /usr/ports/ports-mgmt/portmaster && make install clean	# 安装 portmaster
# portmaster -a # 自动升级所有软件
# portmaster screen # 升级单个软件
```

若需跳过交互确认，可使用类似 BATCH=yes 的选项 `-a -G --no-confirm`：

```sh
# portmaster -a -G --no-confirm
```

### 查看 Port 依赖关系

在更新软件前，可以先查看 Port 的依赖关系，了解更新会影响哪些软件。

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

### 参考文献

更多信息可以参考以下官方文档。

- FreeBSD Project. portmaster -- manage your ports without external databases or languages[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?query=portmaster&sektion=8>. 无需外部数据库的 Ports 管理工具完整说明。

## 全局设置 Ports 构建选项

FreeBSD Ports 框架支持在 **/etc/make.conf** 中全局控制构建选项和依赖。

### 如何全局屏蔽 MySQL

如果不希望使用 MySQL 相关选项，可以在全局配置中屏蔽它。

```sh
# echo "OPTIONS_UNSET+= MYSQL" >> /etc/make.conf
```

完整的 OPTIONS 列表见 <https://cgit.freebsd.org/ports/tree/Mk/bsd.port.mk>。完整的 USE 列表见 <https://cgit.freebsd.org/ports/tree/Mk/bsd.default-versions.mk>。

## 附录：Port 安装示例

### 安装 python3

现在以安装 python3 为例，演示如何使用 Ports 编译安装软件。

```sh
# cd /usr/ports/lang/python
# make BATCH=yes clean
```

其中 `BATCH=yes`（批处理）意味着按默认参数构建。

### 如何设置所有必需的依赖

在编译软件前，有时需要先设置所有依赖项的配置选项。

```sh
# make config-recursive
```

### 如何使用 pkg 安装依赖

为了节省编译时间，可以使用 pkg 来安装所需的依赖，仅使用 Ports 来编译软件包本体。

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

## 故障排除与未竟事宜

### `autoconf-2.72 Invalid perl5 version 5.42.`

也可理解为“xxx-yy Invalid zz version aa”这一类报错。

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

观察整个流程可知，openjdk21 依赖 autoconf，但系统中并未安装。于是递归查找 autoconf 的依赖，发现 autoconf 依赖 perl5；结合 ② 可知系统中已有 perl5，但报错 `Invalid version`，即 perl5 的版本不符合要求。

此问题一般需要先更新 Ports，随后通过 `pkg install -f perl5` 或 `pkg upgrade` 更新 perl5 版本即可解决。

#### 参考文献

- FreeBSD Forums. Invalid perl5 version 5.32[EB/OL]. [2026-03-25]. <https://forums.freebsd.org/threads/invalid-perl5-version-5-32.77628/>. 出现了与上文同样的问题。
