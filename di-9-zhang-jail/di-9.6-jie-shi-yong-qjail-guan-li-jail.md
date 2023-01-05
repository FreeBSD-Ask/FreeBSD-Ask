# 第9.6节 使用 qjail 管理 jail

qjail 是 jail 环境的部署工具，分支自 ezjail 3.1

下文中部署的 jail 在概念上结构如下图

![](../.gitbook/assets/qjailnetstruct.jpg)

文中会用到 pf 防火墙，使用其它防火墙的可以自行尝试进行防火墙相关配置

## 安装 qjail 工具

```
# pkg install qjail
```

## 部置 qjail 使用的目录结构

使用 qjail 前首先要部置 qjail 使用的目录结构，执行

```
# qjail install
```

此时 qjail 会从 FreeBSD 官网下载 base.txz 文件，示例输出如下：

```
root@freebsd:~ # qjail install
resolving server address: ftp.freebsd.org:80
requesting http://ftp.freebsd.org/pub/FreeBSD/releases/amd64/amd64/13.1-RELEASE/base.txz
remote size / mtime: 195363380 / 1652346155
...
```

国内网络问题，速度缓慢的，也可以用镜像手动进行，以中国科学技术大学镜像为例（下载文件是注意版本号，qjail 要求文件版本与宿主机一致，这里是 FreeBSD amd64 13.1)

```
# fetch https:://mirrors.ustc.edu.cn/freebsd/release/amd64/13.1-RELEASE/base.txz
# qjail install -f `pwd`/base.txz  (-f 只能接受绝对路径，等价于 qjail install -f /root/base.txz)
```

部署好 qjail 的目录结构后 `/usr/jails` 目录下生成 `sharedfs` `template` `archive` `flavors` 四个目录

sharedfs 包含一份只读的操作系统可执行库文件，挂载为 nullfs ，在各 jail 之间共享，以节省存储空间的使用

template 包含操作系统的配置文件，将被复制到每个 jail 的基本文件系统中

archive 保存 jail archive 命令产生的存档文件

flavors  包含系统风格（ flavors ）和用户创建的自定义风格
