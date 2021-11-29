# 第四节 软件包管理器 pkg 的用法

## FreeBSD 包管理器设计理念 <a href="freebsd-bao-guan-li-qi-she-ji-li-nian" id="freebsd-bao-guan-li-qi-she-ji-li-nian"></a>

熟悉 Linux 的人也许会发现，FreeBSD 的包管理方案实际上大约等于以下两大 Linux 发行版包管理器的完美合体：

Arch: pacman，对应 pkg（秉承同样的 KISS 理念）

Gentoo: Portage，对应 Ports（Portage 本身就是 Ports 的仿制品）

## 如何用 pkg 安装软件

装上系统默认没有 pkg，先获取 pkg：

#pkg 回车即可输入y 确认下载
————————————————————————————————————

pkg使用https，先安装ssl 证书：

`#pkg install ca_root_nss`

然后把 repo.conf 里的 pkg+http 改成 pkg+https 即可。

最后刷新 pkg 数据库：

`#pkg update -f`

————————————————————————————————————

安装 python 3：

`#pkg install python`

————————————————————————————————————

pkg 升级：

`#pkg upgrade`

———————————————————————————————————-—

错误：You must upgrade the ports-mgmt/pkg port first

解决：

```
#cd /usr/ports/ports-mgmt/pkg
#make deinstall reinstall
```

## 如何卸载软件

直接使用 pkg delete 会破坏正常的依赖关系，应该尽量避免使用（ports 的 make deinstall 也一样），转而使用 pkg-rmleaf 命令，该命令属于的软件需要自行安装：

`pkg install pkg-rmleaf`

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
#/usr/sbin/pwd_mkdb -p /etc/master.passwd
```

### Shared object "x.so.x" not found, required by "xxx"

出现该问题一般是由于 ABI 破坏，更新即可。

```
#pkg  install bsdadminscripts`
#pkg\_libchk
#port-rebuild`
```


