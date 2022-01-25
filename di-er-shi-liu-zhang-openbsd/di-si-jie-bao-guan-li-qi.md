# 第四节 包管理器

同其它 Unix-like 系统一样，OpenBSD 的软件安装主要有两种方式：采用官方预编译好的二进制包，以及通过源代码自己打包安装。这里我们推荐第一种方式安装。

## 二进制包

我们推荐以二进制包的方式来安装软件，以火狐浏览器为例：

- 安装软件 `pkg_add firefox`

- 删除软件 `pkg_delete firefox`

- 查询软件 `pkg_info -Q firefox`

- 升级软件 `pkg_add -iu firefox`

此外，全局的命令有：升级所有软件 `pkg_add -iu`； 删除所有软件包缓冲 `pkg_delete -a`。

## ports 

[查询网站](https://openports.se/)

OpenBSD 的 ports 安装比较复杂，这里只作一番简单介绍，学有余力的网友可进一步查看[手册](https://www.openbsd.org/faq/ports/ports.html)，获取更详细的信息。

OpenBSD 对应多个系统版本(release、stable 以及 current)，各版本间的 ports 并不通用。

## pkgsrc
