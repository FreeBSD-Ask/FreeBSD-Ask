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

停止 jail

```
# qjail stop (停止所有 jail)
# qjail stop jail1 (停止 jail1)
```


重启 jail

```
# qjail restart (重启所有 jail)
# qjail restart jail1 (重启 jail1)
```

进入 jail 控制台

```
# qjail console jail1 (进入 jail1)
```

进入 jail 控制台后，此时是jail 中的 root 帐号（进入 jail 的控制台，不需要输入密码），因 jail 可能开启对外服务，为安全考虑建议设置帐号密码

## jail 更新

下面更新 jail 的部分不针对单个 jail ，而是针对每个 jail ，因为这些文件利用 nullfs 共享一份。

### 更新 jail 的基本二进制文件

既上面提到的 sharedfs 中的文件

```
# qjail update -b
```

### 更新 ports tree 

这里有`-p`（小写） 、 `-P`（大写）两个选项，`-p`（小写）使用 portsnap 更新 jail 的 ports tree，`-P`（大写）使用宿主机的 ports tree 更新 jail 的 ports tree。建议使用 `-P`（大写），避免两次下载 ports tree。

```
# qjail update -P
```

### 更新 src 

```
# qjail update -S (大写）
```

### 建议的更新过程

这里使用了 gitup （需自行安装）

```
# freebsd-update fetch install
# gitup src
# gitup ports
# qjail stop
# qjail update -b
# qjail update -S
# qjail update -P
# qjail start
```

## jail 设置

qjail 可以用 `qjail config` 命令对 每个 jail 另作设置，运行 `qjail config` 前须选停用指定的 jail。

`qjail config` 命令选项较多，这里列出几个常用的，更多的请参考手册页

### 1 `-h`

```
# qjail config -h jail1
```

快速开启 jail1 的 ssh 服务,新建一个 wheel 组用户，用户名和密码同 jail 名，首次用这个用户登录要求修改密码。也可以在登录 jail 控制台后，自行配置 sshd 服务。 

### 2 `-m` `-M`

```
# qjail config -m jail1
```

设置 jail1 需手动启动（manual 状态），`qjail_enable="YES"` 写入 `/etc/rc.conf` 后在系统启动时会自动启动各个 jail ，设为手动启动后则不会在系统启动时自动启动相应的 jail ，须用 `qjail start jailname` 启动。

对应小写的 `-m` 选项，有大写的 `-M` 选项，作用为关闭手动启动状态，即清除 manual 状态，可以在系统启动时自动启用 jail。qjail 中有大量类似的选项，小写字母的选项启用某个功能，大写字母的选项关闭对应功能。如果下文中同时出现小写和大写的选项就不在过多作出说明。

### 3 `-r` `-R`

```
# qjail config -r jail1
```

将 jail1 设为不允许启动（norun 状态），相当于禁用该 jail。

### 4 `-y` `-Y`

```
# qjail config -y jail1
```

启用该 jail 的 SysV IPC,在 jail 中安装 postgresql 时，需要打开这个选项，postgresql 运行基于这个功能。

## 网络设定

此时的 jail 还不能连接网络，因为 jail 绑定在 lo1 网络接口上，接下来通过 pf 设定网络, 其中 `em0` 为外网接口

在 `/etc/pf.conf` 中写入

```
nat pass on em0 inet from lo1 to any ->em0  （从 lo1 接口发出的连接通过 nat 转发到 em0
rdr pass on em0 inet proto tcp from any to em0 port 22 -> 192.168.1.1 port 22  （端口重定向，把连接到 em0 上22端口上的 tcp 连接重定向到 192.168.1.1 地址（即 jail1 ）的22端口上
```

```
# sysrc pf_enable=YES
# service pf start
```



