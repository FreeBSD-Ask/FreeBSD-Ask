# 第 3.8 节 通过源代码更新 FreeBSD

基本思路就是获取 FreeBSD 的源代码，然后进行编译安装。可以使用 git 直接拉取代码，也可以直接下载 ISO 镜像里面的 txz 压缩文件或者去 github 上下载当前 FreeBSD 项目的 zip 压缩包。

编译流程见 Handbook 即可。非常地简单。


>**svn 到 git 的迁移**
>
>FreeBSD 项目在 2021 年从 SVN 全面迁移到了 Git，即 [https://git.freebsd.org](https://git.freebsd.org)
>
>所以获取源代码的方式也产生了变化，不再使用 svn 了。


## 从 Git 获取源代码


### 安装 Git

```sh
# pkg install git
```

或者：

```
# cd /usr/ports/devel/git/ && make install clean
```


### Git 代理设置方法


- 如果使用的是 `sh`, `bash`, `zsh`：

设置：

```sh
# git config --global http.proxy http://192.168.X.X:7890
# git config --global https.proxy http://192.168.X.X:7890
```

取消：

```sh
# git config --global --unset http.proxy
# git config --global --unset https.proxy
```

### Git 拉取源代码

```
# git clone --depth 1 https://git.FreeBSD.org/src.git /usr/src 
```

或者（GitHub 是 FreeBSD.org 上 src 的镜像，每 10 分钟同步一次）

```
# git clone --depth 1 https://github.com/freebsd/freebsd-src /usr/src
```

### 参考文献

- [Submitting GitHub Pull Requests to FreeBSD](https://freebsdfoundation.org/our-work/journal/browser-based-edition/configuration-management-2/submitting-github-pull-requests-to-freebsd/)


### 故障排除与未竟事宜


- Git：`fatal: unable to update url base from redirection`

使用 FreeBSD 源却没加 `.git`

## Gitup

```sh
# pkg install gitup
```

或者：

```
# cd /usr/ports/net/gitup/ && make install clean
```

```
# gitup release # 具体版本需要参考当前 gitup 配置 https://github.com/johnmehr/gitup/blob/main/gitup.conf
# gitup current # 获取 current 源代码
```

### 故障排除与未竟事宜

- Git：`fatal: unable to access 'https://git.FreeBSD.org/src.git/': SSL certificate problem: certificate is not yet valid`

可能是时间不对造成的，同步时间：

```sh
# ntpdate -u pool.ntp.org # 当时间相差较大时必须使用该命令，其他命令不会生效
```

## 从压缩包获取源代码（方便但非最新）

该方法比较简单快捷。

以 FreeBSD 14.2 为例：

```sh
# fetch https://download.freebsd.org/ftp/releases/amd64/14.2-RELEASE/src.txz
# tar xvzf src.txz  -C /
```

>**为何要解压到 `/`？**
>
>因为 `/` 会将源代码解压到 `/usr/src`。如果把上面的路径改成 `/usr/src`，会把源代码解压到 `/usr/src/usr/src`。因为他这个压缩包是带路径压缩的。

>**技巧**
>
>如果速度慢可以切换到 <https://mirrors.ustc.edu.cn/freebsd/releases/amd64/14.2-RELEASE/src.txz>

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

### 故障排除与未竟事宜

- `Conflicts remain from previous update, aborting.`

需要 **解决冲突**

>**技巧**
>
>与绝大多数现代 Linux 不同，[FreeBSD](https://github.com/freebsd/freebsd-src/tree/main/contrib/nvi)（OpenBSD）上的 `vi` 是 *[nvi](https://sites.google.com/a/bostic.com/keithbostic/keith-bostic?authuser=0)*（原版 **ex/vi** 的再实现），并不是指向任何 *vim* 的链接符号。基本上没人会用，一般亦无学习的必要，故有必要换成别的文本编辑器。
>
>```sh
># export  EDITOR=/usr/bin/ee # 切换 vi 为 ee。针对 FreeBSD 14 之前的版本或 csh 使用：setenv EDITOR /usr/bin/ee
># export  VISUAL=/usr/bin/ee # 切换 vi 为 ee。针对 FreeBSD 14 之前的版本或 csh 使用：setenv VISUAL /usr/bin/ee
>```

```sh
root@ykla:~ # etcupdate -B     
Conflicts remain from previous update, aborting.

```

```
# etcupdate resolve          # 解决冲突
Resolving conflict in '/etc/group':
Select: (p) postpone, (df) diff-full, (e) edit,
        (h) help for more options: e # 输入 e 解决冲突
# etcupdate -B 
```

## ZFS 相关升级请参见 ZFS 一节

## 参考资料

- [FreeBSD 手册](https://handbook.bsdcn.org/)。
- [etcupdate -- manage updates to system files not updated by installworld](https://man.freebsd.org/cgi/man.cgi?etcupdate(8))
