# 第四节 软件包管理器 pkg 的用法

## FreeBSD 包管理器设计理念 <a href="freebsd-bao-guan-li-qi-she-ji-li-nian" id="freebsd-bao-guan-li-qi-she-ji-li-nian"></a>

熟悉 Linux 的人也许会发现，FreeBSD 的包管理方案实际上大约等于以下两大 Linux 发行版包管理器的完美合体：

Arch: pacman，对应 pkg（秉承同样的 KISS 理念）

Gentoo: Portage，对应 Ports（Portage 本身就是 Ports 的仿制品）

## FreeBSD pkg基础教程1

装上系统默认没有pkg，先获取pkg：\
\#pkg 回车即可输入y 确认下载\
————————————————————————————————————\
pkg使用https，先安装ssl 证书：\
`#pkg install ca_root_nss`\
然后把repo.conf 里的pkg+http 改成pkg+https 即可。\
最后刷新pkg数据库：

`#pkg update -f`\
————————————————————————————————————\
安装python 3：\
`#pkg install python`\
————————————————————————————————————\
pkg 升级：\
`#pkg upgrade`\
———————————————————————————————————-—\
错误：You must upgrade the ports-mgmt/pkg port first\
解决：
```
#cd /usr/ports/ports-mgmt/pkg
#make deinstall reinstall
```
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
/usr/sbin/pwd_mkdb -p /etc/master.passwd
```
