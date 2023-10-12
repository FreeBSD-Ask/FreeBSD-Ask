# 第 3.4 节 软件包管理器 pkg 的用法

包管理器目前是 pkgng，其命令是 pkg。

> 请注意：pkg 只能管理第三方软件包，并不能起到升级系统，获取安全更新的作用。这是因为 FreeBSD 项目是把内核与用户空间作为一个整体来进行维护的，而不是像 Linux 那样 linus torvalds 负责维护内核，各个发行版的人负责维护 GNU 工具（他们这些软件实际上被设计为单个软件包，因此可以用包管理器更新与升级系统）。FreeBSD 使用 `freebsd-update` 来升级系统，获取安全补丁。<https://pkg-status.freebsd.org/> 可以查看当前的 pkg 编译状态。

> 偏好图形化的用户可以安装使用 `ports-mgmt/octopkg`，该工具是 pkg 的图形化前端，由 ghostbsd 开发。

## 如何用 pkg 安装软件

基本系统默认没有 pkg，先获取 pkg：

`# pkg` 回车即可输入 y 确认下载

pkg 使用 https，先安装 ssl 证书：

`# pkg install ca_root_nss`

然后把 repo.conf 里的 pkg+http 改成 pkg+https 即可。

最后刷新 pkg 数据库：

`# pkg update -f`

安装 python 3：

`# pkg install python`

pkg 升级：

`# pkg upgrade`

错误：`You must upgrade the ports-mgmt/pkg port first`

解决：

```shell-session
# cd /usr/ports/ports-mgmt/pkg
# make deinstall reinstall
```

查看已经安装的所有软件：

```shell-session
# pkg info
```

## 如何卸载软件

直接使用 `pkg delete` 会破坏正常的依赖关系，应该尽量避免使用（ports 的 `make deinstall` 也一样），转而使用 `pkg-rmleaf` 命令，该命令属于的软件需要自行安装：

`# pkg install pkg-rmleaf`

## 故障排除

### FreeBSD pkg 安装软件时出现创建用户失败解决

问题示例：

```shell-session
[1/1] Installing package…
===> Creating groups.
Creating group ‘package’ with gid ‘000’.
===> Creating users
Creating user ‘package’ with uid ‘000’.
pw: user ‘package’ disappeared during update
pkg: PRE-INSTALL script failed
```

问题解析：数据库未同步

问题解决：

```shell-session
# /usr/sbin/pwd_mkdb -p /etc/master.passwd
```

### Shared object "x.so.x" not found, required by "xxx"

出现该问题一般是由于 ABI 破坏，更新即可。

```shell-session
# pkg  install bsdadminscripts
# pkg_libchk
# port-rebuild
```

### Newer FreeBSD version for package pkg

问题示例：

```shell-session
Neuer FreeBSD version for package pkg:
To ignore this error set IGNORE_OSVERSION=yes
- package: 1402843
- running kernel: 1400042
Ignore the mismatch and continue? [y/N]:
```

这通常发生在失去安全支持的或者在 Current 版本的系统上，不影响使用，输入 `y` 即可。

如果想要从根源上解决，需要自己卸载 pkg，从 ports 安装 `ports-mgmt/pkg`；或者从源代码更新整个系统。

如果只是不想看到这个提示只需要按照提示将 `IGNORE_OSVERSION=yes` 写到 `/etc/make.conf`里面（没有就新建）。

