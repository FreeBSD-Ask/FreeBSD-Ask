# 第 9.3 节 jail 配置

## 创建 jail 目录

### 放入 FreeBSD 基本系统

方案一

```
# make buildworld #编译基本系统
# make installworld DESTDIR=/usr/jail/ #安装到 jail
# make distribution DESTDIR=/usr/jail/ #或者
```

方案二

下载 base.txz 或者从 iso 提取 baes.txz，然后解压到 jail

`# tar -xvf base.txz -C /usr/jail/`

挂载 devfs 文件系统。(不是必须)

`# mount -t devfs devfs /usr/jail/dev`

### 写入 `rc.conf`

```
# sysrc jail_enable="YES"
```

创建 `jail.conf` 文件（可以写进 `rc.conf` 但这样便于管理）

```
www {
host.hostname =www.example.org; # 主机名
ip4.addr = 192.168.0.10; # IP 地址
path ="/usr/jail"; # jail 位置
devfs_ruleset = "www_ruleset"; # devfs ruleset
mount.devfs; # 挂载 devfs 文件系统到 jail
exec.start = "/bin/sh /etc/rc"; # 启动命令
exec.stop = "/bin/sh /etc/rc.shutdown"; # 关闭命令
}
```

## 管理

`jls` 查看在线 jail 信息列表

```
JID IP Address    Hostname   Path
3   192.168.0.10  www       /usr/jail/www
```

中英对照

|    英语    |   中文    |
| :--------: | :-------: |
|    JID     |  jail ID  |
| IP Address |  IP 地址  |
|  Hostname  |  主机名   |
|    Path    | jail 路径 |

## 启动与停止 jail

```
# service jail start www
# service jail stop www
```

## 登录 jail

```
# jexec 1 tcsh
```

## 干净关闭 jail

```
# jexec 3 /etc/rc.shutdown
```

## 升级 jail

```
# freebsd-update -b /here/is/the/jail fetch
# freebsd-update -b /here/is/the/jail install
```

## ping 与网络

### 开启 ping

写入 `/etc/jail.conf`

```
allow.raw_sockets=1;
allow.sysvipc=1;
```

### 网络

创建 `/etc/resolv.conf`,并编辑

```
search lan
nameserver 119.29.29.29
nameserver 182.254.116.116
nameserver 114.114.114.114
nameserver 223.5.5.5
nameserver 223.6.6.6
#不要写路由器地址
```

## 删除文件没有权限

```
# chflags -R noschg directory
```
