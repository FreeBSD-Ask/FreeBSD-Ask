# 5.8 使用源代码更新 FreeBSD

基本思路是获取 FreeBSD 的源代码，然后进行编译和安装。可以使用 Git 直接拉取代码，也可以从 ISO 镜像中下载 txz 压缩文件，或者从 GitHub 下载当前 FreeBSD 项目的 zip 压缩包。

编译流程参见 Handbook 即可。

## SVN 到 Git 的迁移

FreeBSD 项目在 2021 年从 SVN 全面迁移到了 Git，即 [https://git.freebsd.org](https://git.freebsd.org)

因此，获取源代码的方式也发生了变化，不再使用 SVN。

## 从 Git 获取源代码

### 安装 Git

使用 pkg 安装 Git：

```sh
# pkg install git
```

或者使用 ports 安装 Git：

```sh
# cd /usr/ports/devel/git/
# make install clean
```

### Git 代理设置方法

- 设置 Git 全局代理：

```sh
# git config --global http.proxy http://192.168.X.X:7890    # 设置 Git 全局 HTTP 代理
# git config --global https.proxy http://192.168.X.X:7890   # 设置 Git 全局 HTTPS 代理
```

- 取消 Git 全局代理：

```sh
# git config --global --unset http.proxy    # 取消 Git 全局 HTTP 代理设置
# git config --global --unset https.proxy   # 取消 Git 全局 HTTPS 代理设置
```


### Git 拉取源代码

#### 拉取 CURRENT

通过 FreeBSD 官方存储库拉取。克隆 FreeBSD 源码仓库到 `/usr/src`，使用浅克隆减少下载量：

```sh
$ git clone --depth 1 https://git.FreeBSD.org/src.git /usr/src 
```

参数 `--depth 1` 说明：浅克隆，仅拉取最新的提交，不拉取全部的日志及历史记录

或者通过 GitHub 拉取（GitHub 是 FreeBSD.org 上 src 仓库的镜像，每 10 分钟同步一次。）

```sh
$ git clone --depth 1 https://github.com/freebsd/freebsd-src /usr/src
```

#### 拉取某 RELEASE

通过 FreeBSD 官方存储库拉取。克隆 FreeBSD 15.0 发布分支源码到 `/usr/src`，使用浅克隆并仅包含该分支：

```sh
$ git clone --branch releng/15.0 --single-branch --depth 1 https://git.FreeBSD.org/src.git /usr/src
```

- `--branch releng/15.0`：指定拉取分支（FreeBSD RELEASE 的版本）
- `--single-branch`：仅克隆一个分支，除该已克隆的单一分支外不含任何其他引用（refs）。

或者通过 GitHub 拉取。从 GitHub 克隆 FreeBSD 15.0 发布分支源码到 `/usr/src`，使用浅克隆并仅包含该分支：

```sh
$ git clone --branch releng/15.0 --single-branch --depth 1 https://github.com/freebsd/freebsd-src /usr/src
```

### 参考文献

- [Submitting GitHub Pull Requests to FreeBSD](https://freebsdfoundation.org/our-work/journal/browser-based-edition/configuration-management-2/submitting-github-pull-requests-to-freebsd/)


## Gitup

使用 pkg 安装 Gitup：

```sh
# pkg install gitup
```

还可以使用 ports 安装 Gitup：

```sh
# cd /usr/ports/net/gitup/ 
# make install clean
```

```sh
# gitup release # 具体版本需要参考当前 gitup 配置 https://github.com/johnmehr/gitup/blob/main/gitup.conf
# gitup current # 获取 current 源代码
```


## 从压缩包获取源代码（方便但非最新）

该方法较为简单快捷。

以 FreeBSD 15.0-RELEASE 为例：

```sh
# fetch https://download.freebsd.org/ftp/releases/amd64/15.0-RELEASE/src.txz  # 下载 FreeBSD 15.0-RELEASE 的源码压缩包
# tar xvf src.txz -C /                                                    # 将源码解压到根目录
```

>**为何要解压到 `/`？**
>
>因为解压到 `/` 会将源代码解压到 `/usr/src`。如果将上面的路径改成 `/usr/src`，会将源代码解压到 `/usr/src/usr/src`。因为该压缩包是包含路径的。

>**技巧**
>
>如果速度慢可以切换到 <https://mirrors.ustc.edu.cn/freebsd/releases/amd64/15.0-RELEASE/src.txz>

## 开始编译

```sh
# cd /usr/src          # 切到工作目录
# make -j4 buildworld  # 编译世界
# make -j4 kernel      # 编译并安装内核
# reboot               # 重启以使用新内核
# cd /usr/src          # 切回工作目录
# etcupdate -p         # 进行必要的配置文件合并  
# make installworld    # 安装世界 
# etcupdate -B         # 合并更新
# reboot               # 重启以完成更新流程
```

### 附录：解决冲突

- `Conflicts remain from previous update, aborting.`

需要解决冲突。

>**技巧**
>
>与绝大多数现代 Linux 不同，[FreeBSD](https://github.com/freebsd/freebsd-src/tree/main/contrib/nvi)（OpenBSD）上的 `vi` 是 *[nvi](https://sites.google.com/a/bostic.com/keithbostic/keith-bostic?authuser=0)*（原版 **ex/vi** 的再实现），并不是指向任何 *vim* 的链接符号。基本上很少有人使用，也一般没有学习的必要，因此有必要更换为其他文本编辑器。
>
>```sh
># export  EDITOR=/usr/bin/ee # 切换 vi 为 ee。针对 FreeBSD 14 之前的版本或 csh 使用：setenv EDITOR /usr/bin/ee
># export  VISUAL=/usr/bin/ee # 切换 vi 为 ee。针对 FreeBSD 14 之前的版本或 csh 使用：setenv VISUAL /usr/bin/ee
>```

合并冲突。使用 `etcupdate` 执行备份模式，以便在更新配置文件前备份现有文件：

```sh
# etcupdate -B     
Conflicts remain from previous update, aborting.
```

解决冲突：

```sh
# etcupdate resolve          # 解决冲突
Resolving conflict in '/etc/group':
Select: (p) postpone, (df) diff-full, (e) edit,
        (h) help for more options: e # 输入 e 解决冲突
# etcupdate -B 
```


## 故障排除与未竟事宜

### Git：`fatal: unable to update url base from redirection`

使用 FreeBSD 源仓库地址时未加 `.git` 后缀。

### Git：`fatal: unable to access 'https://git.FreeBSD.org/src.git/': SSL certificate problem: certificate is not yet valid`

可能是系统时间不正确导致的，使用 `pool.ntp.org` 服务器同步系统时间

```sh
# ntpdate -u pool.ntp.org # 当时间相差较大时必须使用该命令，其他命令不会生效
```

## 参考资料

- [FreeBSD 手册](https://handbook.bsdcn.org/)。
- [etcupdate -- manage updates to system files not updated by installworld](https://man.freebsd.org/cgi/man.cgi?etcupdate(8))
