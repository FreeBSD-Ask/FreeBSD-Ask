# 第 9.4 节 jail 更新

如果要同时管理多个 jail,那么在更新 jail 的时候就要对每个 jail 单独进行一遍操作，这不仅非常耗时而且相当无聊。通过建立统一的模板，可以让所有 jail 共用一个基础环境，同时拥有各自的可写空间，互不干扰。

本教程将建立以下的目录结构（你也可以自行更改）：

1、`/jail/mroot` 是模板，是所有 jail 的共用只读部分，在本例中将被挂载到 `/jail/www`。

2、`/jail/skel` 是框架，方便创建 jail，本身并不为任何 jail 使用。

3、`/jail/www` 是 jail `www` 运行的根目录，也是只读模板的挂载点，本身是个空目录。

4、`/jail/www/s` 是 jail `www` 的可写部分的挂载点，也是个空目录。

5、`/jail/files/www` 是 jail `www` 的可写部分的实际存放位置，将被挂载到 `/jail/www/s`。

如果要创建多个 jail，则重复创建数据目录和项目目录，这样所有的 jail 都会共用 `/jail/mroot`。

本教程需要安装 `cpdup`

```shell-session
# pkg install cpdup
```

## 创建模板目录

```shell-session
# mkdir -p /jail/mroot
# 然后放入基本目录，上边说过不再写
# 将 ports 和源码放入模板
# git clone --depth 1 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git /jail/mroot/usr/ports
# cpdup /usr/src /jail/mroot/usr/src # 需要提前获取源码，且要注意源码对应的版本要与 /jail/mroot 的版本相同
```

将可写部分连接到可写目录位置

```shell-session
# cd /jail/mroot # cd 到模板目录
# mkdir s        # 创建用来做链接的目录
# ln -s s/etc etc
# ln -s s/home home
# ln -s s/root root
# ln -s ../s/usr-local usr/local
# ln -s ../s/usr-X11R6 usr/X11R6
# ln -s ../../s/distfiles usr/ports/distfiles
# ln -s s/tmp tmp
# ln -s s/var var
```

## 创建框架目录

```shell-session
# mkdir -p /jail/skel
# mkdir /jail/skel /jail/skel/home /jail/skel/usr-X11R6 /jail/skel/distfiles /jail/skel/portbuild
# 移动可写部分
# mv /jail/mroot/etc /jail/skel
# mv /jail/mroot/usr/local /jail/skel/usr-local
# mv /jail/mroot/tmp /jail/skel
# mv /jail/mroot/var /jail/skel
# mv /jail/mroot/root /jail/skel
```

使用 etcupdate 安装缺少的配置文件。

```shell-session
# etcupdate -s /jail/mroot/usr/src -d /jail/skel/var/db/etcupdate -D /jail/skel
```

为 `make` 创建通用配置文件

```shell-session
# echo “WRKDIRPREFIX?=  /s/portbuild” >> /jail/skel/etc/make.conf
```

## 创建数据目录

就是复制一份框架

```shell-session
# cpdup /jail/skel /jail/files/www
```

## 创建项目目录

```shell-session
# mkdir /jail/www /jail/www/s
```

## 创建 fstab

```shell-session
# ee /jail/www.fstab
# 将公共只读系统挂载到项目目录
/jail/mroot /jail/www nullfs ro 0 0
# 将项目数据目录挂载到项目目录
/jail/files/www /jail/www/s nullfs rw 0 0
```

## 写入 jail.conf

```shell-session
# 全局部分

exec.start = "/bin/sh /etc/rc";
exec.stop = "/bin/sh /etc/rc.shutdown";
exec.clean;
mount.devfs;
allow.raw_sockets = 1;
allow.sysvipc = 1;
interface = "网卡地址";

# 主机名也可以用变量代替
hostname = "$name.domain.local";

# jail 位置，也可以用变量
path = "/jail/$name";

## ip地址
ip4.addr = 192.168.1.$ip;

## fstab位置
mount.fstab = /jail/$name.fstab;

www {
$ip=2
#                  #如不使用 fstab,使用
# mount.fstab =""; # 替换全局
}
```

