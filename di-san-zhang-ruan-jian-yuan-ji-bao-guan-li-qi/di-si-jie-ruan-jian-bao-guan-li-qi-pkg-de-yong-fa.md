# 第四节 软件包管理器 pkg 的用法

## 如何用 pkg 安装软件

装上系统默认没有 pkg，先获取 pkg：

#pkg 回车即可输入 y 确认下载 ————————————————————————————————————

pkg 使用 https，先安装 ssl 证书：

`# pkg install ca_root_nss`

然后把 repo.conf 里的 pkg+http 改成 pkg+https 即可。

最后刷新 pkg 数据库：

`# pkg update -f`

————————————————————————————————————

安装 python 3：

`# pkg install python`

————————————————————————————————————

pkg 升级：

`# pkg upgrade`

———————————————————————————————————-—

错误：You must upgrade the ports-mgmt/pkg port first

解决：

```
# cd /usr/ports/ports-mgmt/pkg
# make deinstall reinstall
```

## 如何卸载软件

直接使用 `pkg delete` 会破坏正常的依赖关系，应该尽量避免使用（ports 的 `make deinstall` 也一样），转而使用 `pkg-rmleaf` 命令，该命令属于的软件需要自行安装：

`# pkg install pkg-rmleaf`

## 故障排除

### FreeBSD pkg 安装软件时出现创建用户失败解决

　问题示例：

```
[1/1] Installing package…
===> Creating groups.
Creating group ‘package’ with gid ‘000’.
===> Creating users
Creating user ‘package’ with uid ‘000’.
pw: user ‘package’ disappeared during update
pkg: PRE-INSTALL script failed
```

问题解析：数据库未同步 　　

问题解决:

```
# /usr/sbin/pwd_mkdb -p /etc/master.passwd
```

### Shared object "x.so.x" not found, required by "xxx"

出现该问题一般是由于 ABI 破坏，更新即可。

```
# pkg  install bsdadminscripts
# pkg_libchk
# port-rebuild
```

### Newer FreeBSD version for package pkg

```
Neuer FreeBSD version for package pkg:
To ignore this error set IGNORE_OSVERSION=yes
- package: 1402843
- running kernel: 1400042
Ignore the mismatch and continue? [y/N]:
```

这通常发生在失去安全支持的或者在 Current 版本的系统上，不影响使用，输入`y`即可。

如果想要从根源上解决，需要自己卸载 pkg，从 ports 安装 `ports-mgmt/pkg`；或者从源代码更新整个系统。

如果只是不想看到这个提示只需要按照提示将 `IGNORE_OSVERSION=yes` 写到 `/etc/make.conf`里面（没有就新建）。
