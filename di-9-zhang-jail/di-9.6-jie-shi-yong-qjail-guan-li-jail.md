# 第9.6节 使用 qjail 管理 jail

qjail 是 jail 环境的部署工具，分支自 ezjail 3.1

下文中部署的 jail 在概念上结构如下图

![](../.gitbook/assets/qjailnetstruct.jpg)

文中会用到 pf 防火墙，使用其它防火墙的可以自行尝试进行防火墙相关配置

## 预留 jail 的 ip

`/etc/rc.conf` 文件中写入

```
cloned_interfaces="lo1"  (克隆出 lo1 ，尽量和宿主机网络配置分开）
ifconfig_lo1_alias0="inet 192.168.1.0-9" (宿主机 ip 为 10.0.2.15, 选择该网段是为了和宿主机网段分开，可自行斟酌）
```

运行

```
# service netif restart
```

lo1 将获得10个 ip 地址，下面将用1-9这9个ip给jail使用。

## 安装 qjail 工具

```
# pkg install qjail
```

启用 qjail

```
# sysrc qjail_enable=YES
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

flavors  包含系统风格（ flavors ）和用户创建的自定义风格，其实就是自己定义的配置文件等

## 部署 jail

```
# qjail create -n lo1 -4 192.168.1.1 jail1
```

`-n` 指定使用lo1作为网络接口，`-4` 指定 ipv4 地址。

生成 jail1 后，`/usr/jails/` 目录下对应生成 `jail1` 目录( `/usr/jails/jail1/`),保存相应文件。

可以在上面提到的 `flavors` 目录中建立自己的配置文件以便在部署 jail 时复制到新的 jail 中。

如，新建 `/usr/jails/flavors/default/usr/local/etc/pkg/repos/FreeBSD.conf` ,那么之后再新建 jail 时，会自动把这个文件复制到对应的 jail 中，既

```
# qjail create -n lo1 -4 192.168.1.2 jail2
```

建立 jail2 后，自动建立 `/usr/jails/jail2/usr/local/etc/pkg/repos/FreeBSD.conf` ,既修改了之后所有 jail 的默认pkg镜像。但对应 jail1 并没有生成这个文件，因为生成 jail1 时，还没有在 flavors 目录中写入相应文件。

## qjail 基本使用

启用 jail

```
# qjail start (启动所有 jail)
# qjail start jail1 (启动 jail1)
```
