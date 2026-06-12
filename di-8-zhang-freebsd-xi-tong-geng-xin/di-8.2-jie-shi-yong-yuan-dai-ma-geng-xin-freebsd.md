# 8.2 使用源代码更新 FreeBSD

从源代码构建 FreeBSD 可以自定义内核选项和编译参数，适用于 freebsd-update 不支持的架构或需要裁剪系统的场景。

基本思路是获取 FreeBSD 的源代码，随后编译安装。可以使用 Git 直接拉取代码，也可以从 FreeBSD 下载站点获取 txz 压缩文件，或者从 GitHub 下载当前 FreeBSD 项目的 zip 压缩包。

编译流程请参考本书其他章节。

## 从 Git 获取源代码

### 安装 Git

使用 pkg 安装 Git：

```sh
# pkg install git
```

或者使用 Ports 安装 Git：

```sh
# cd /usr/ports/devel/git/
# make install clean
```

### Git 代理设置方法

在网络环境受限制的情况下，可能需要为 Git 设置代理才能正常拉取源代码。下面介绍设置和取消 Git 代理的方法。

- 设置 Git 全局代理：

```sh
# git config --global http.proxy http://192.168.X.X:7890  # 设置 Git 全局 HTTP 代理
# git config --global https.proxy http://192.168.X.X:7890  # 设置 Git 全局 HTTPS 代理
```

- 取消 Git 全局代理：

```sh
# git config --global --unset http.proxy  # 取消 Git 全局 HTTP 代理设置
# git config --global --unset https.proxy  # 取消 Git 全局 HTTPS 代理设置
```

### Git 拉取源代码

#### 拉取 CURRENT

从 FreeBSD 官方存储库拉取源代码。将 FreeBSD 源代码仓库克隆至 **/usr/src**，采用浅克隆以减少下载量：

```sh
$ git clone --depth 1 https://git.FreeBSD.org/src.git /usr/src
```

参数 `--depth 1` 说明：采用浅克隆模式，仅获取最新提交，不包含完整的提交历史记录。

从 GitHub 拉取源代码（GitHub 为 FreeBSD.org 上 src 仓库的镜像，每 10 分钟同步一次）。

```sh
$ git clone --depth 1 https://github.com/freebsd/freebsd-src /usr/src
```

#### 拉取某 RELEASE

通过 FreeBSD 官方存储库拉取。克隆 FreeBSD 15.0 发布分支源代码到 **/usr/src**，使用浅克隆并仅包含该分支：

```sh
$ git clone --branch releng/15.0 --single-branch --depth 1 https://git.freebsd.org/src.git /usr/src
```

选项解释：

- `--branch releng/15.0`：指定拉取分支（FreeBSD RELEASE 的版本）
- `--single-branch`：仅克隆一个分支，除所克隆的单一分支外不含任何其他引用（refs）。

或者通过 GitHub 拉取。从 GitHub 克隆 FreeBSD 15.0 发布分支源代码到 **/usr/src**，使用浅克隆并仅包含该分支：

```sh
$ git clone --branch releng/15.0 --single-branch --depth 1 https://github.com/freebsd/freebsd-src /usr/src
```

### 参考文献

- Warner Losh. Submitting GitHub Pull Requests to FreeBSD[EB/OL]. [2026-03-25]. <https://freebsdfoundation.org/our-work/journal/browser-based-edition/configuration-management-2/submitting-github-pull-requests-to-freebsd/>. 详解通过 GitHub 向 FreeBSD 提交拉取请求的工作流程与注意事项。

## 从压缩包获取源代码（方便但非最新）

该方法操作简便。

以 FreeBSD 15.0-RELEASE 为例：

```sh
# fetch https://download.freebsd.org/releases/amd64/amd64/15.0-RELEASE/src.txz  # 下载 FreeBSD 15.0-RELEASE 的源代码压缩包
# tar xvf src.txz -C /                                                    # 将源代码解压到根目录
```

> **为何需解压至 `/`？**
>
> 因为该压缩包包含路径，解压到 **/** 会将源代码解压到 **/usr/src**。如果将上面的路径改为 **/usr/src**，会将源代码解压到 **/usr/src/usr/src**。

> **技巧**
>
> 如果速度慢可以切换到 <https://mirrors.ustc.edu.cn/freebsd/releases/amd64/amd64/15.0-RELEASE/src.txz>

## 开始编译

```sh
# cd /usr/src          # 切换到工作目录
# make -j4 buildworld  # 编译世界
# make -j4 kernel      # 编译并安装内核（相当于 buildkernel 后跟 installkernel）
# reboot               # 重启以使用新内核
# cd /usr/src          # 切换回工作目录
# etcupdate -p         # 合并 installworld 前必须更新的配置文件
# make installworld    # 安装世界
# etcupdate -B         # 复用之前构建的对象树来合并更新
# reboot               # 重启以完成更新流程
```

### 附录：解决冲突

- `Conflicts remain from previous update, aborting.`

需要解决冲突。

> **技巧**
>
> 与多数现代 Linux 发行版不同，[FreeBSD](https://github.com/freebsd/freebsd-src/tree/main/contrib/nvi)（OpenBSD）上的 `vi` 为 *[nvi](https://sites.google.com/a/bostic.com/keithbostic/keith-bostic?authuser=0)*（原版 **ex/vi** 的再实现），并非指向 *vim* 的符号链接。该编辑器使用频率较低，因此建议更换为其他文本编辑器。
>
> ```sh
> export EDITOR=/usr/bin/ee # 切换默认编辑器为 ee。若使用 csh/tcsh，改用 setenv EDITOR /usr/bin/ee
export VISUAL=/usr/bin/ee # 切换可视化编辑器为 ee。若使用 csh/tcsh，改用 setenv VISUAL /usr/bin/ee
> ```

合并冲突。使用 `etcupdate` 合并配置文件更新：

```sh
# etcupdate -B
Conflicts remain from previous update, aborting.
```

`etcupdate` 在合并后会自动触发若干系统文件的后续处理：

| 变更文件 | 触发命令 |
| -------- | -------- |
| **/etc/master.passwd** | `pwd_mkdb` |
| **/etc/login.conf** | `cap_mkdb` |
| **/etc/mail/aliases** | `newaliases` |
| **/etc/services** | `services_mkdb` |
| **/etc/localtime**（且 **/var/db/zoneinfo** 存在） | `tzsetup` |
| **/etc/motd** | `/etc/rc.d/motd` |

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

系统时间不正确所致，使用 `ntpd -q -g pool.ntp.org` 同步系统时间即可解决。详细说明参考本书其他相关章节。

## 参考文献

- FreeBSD Foundation. 2021 in Review: Software Development[EB/OL]. [2026-04-16]. <https://freebsdfoundation.org/blog/2021-in-review-software-development/>
- FreeBSD Project. etcupdate -- manage updates to system files not updated by installworld[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?query=etcupdate&sektion=8>. 系统配置文件更新工具的官方技术文档。

## 课后习题

1. 总结从 FreeBSD Git 仓库获取源代码的完整流程，列出所需命令及参数含义。

2. 使用 etcupdate 管理 **/etc** 目录的配置文件更新，记录一次完整的合并冲突处理过程。

3. 修改 **/etc/src.conf**，排除不需要的组件（如某些调试工具），测量 `make buildworld` 编译时间的变化。
