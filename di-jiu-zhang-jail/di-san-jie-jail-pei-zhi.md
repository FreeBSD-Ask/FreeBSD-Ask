# 第三节 jail 配置

## 创建jail目录 <a href="chuang-jian-jail-mu-lu" id="chuang-jian-jail-mu-lu"></a>

### 放入基本系统

方案一

```
make buildworld #编译基本系统
make installworld DESTDIR=/usr/jail/ #安装到jail
make distribution DESTDIR=/usr/jail/ #或者
```

方案二

下载base.txz 或者从iso提取baes.txz，然后解压到jail
tar -xvf base.txz -C /usr/jail/
#挂载 devfs文件系统。(不是必须)
mount -t devfs devfs /usr/jail/dev

### 写入rc.conf

sysrc jail_enable=”YES”
创建jail.conf文件(可以写进rc.conf但这样便于管理)
www {
host.hostname = [www.example.org](http://www.example.org); # 主机名
ip4.addr = 192.168.0.10; # IP 地址
path =”/usr/jail”; # jail位置
devfs_ruleset = “www_ruleset”; # devfs ruleset
mount.devfs; # 挂载 devfs文件系统到jail
exec.start = “/bin/sh /etc/rc”; # 启动命令
exec.stop = “/bin/sh /etc/rc.shutdown”; # 关闭命令
}

## 管理

jls查看在线监狱信息列表
JID IP Address Hostname Path
3 192.168.0.10 www /usr/jail/www

中英对照
英语 中文
JID 监狱ID
IP Address IP地址
Hostname 主机名
Path 监狱路径

## 启动与停止jail

service jail start www
service jail stop www

## 登录jail

jexec 1 tcsh

## 干净关闭jail

jexec 3 /etc/rc.shutdown

## 升级jail

freebsd-update -b /here/is/the/jail fetch
freebsd-update -b /here/is/the/jail install

## ping与网络

### 开启ping

写入/etc/jail.conf
allow.raw_sockets=1;
allow.sysvipc=1;

### 网络

创建/etc/resolv.conf,并编辑

search lan
nameserver 119.29.29.29
nameserver 182.254.116.116
nameserver 114.114.114.114
nameserver 223.5.5.5
nameserver 223.6.6.6
#不要写路由器地址

## 创建jail目录

创建4个 分别是模板 骨架 数据 项目

### 创建模板目录

mkdir -p /jail/j1
#然后放入基本目录，上边说过不再写

### 创建骨架目录

mkdir -p /jail/j2
#移动目录 etc usr tmp var root

```
cd /jail/j2/ # 注意目录
mv /jail/j1/etc ./etc
mv /jail/j1/tmp ./tmp
mv /jail/j1/var ./var
mv /jail/j1/root ./root
```

### 创建数据目录

就是复制一份骨架给他用
cp -R /jail/j2/ /jail/js/www/

### 创建项目目录

mkdir -p /jail/www/

### 建立链接

```
cd /jail/j1 #cd 到模板目录
mkdir -p jusr #创建用来做链接数据的目录
ln -s jusr/etc etc
ln -s jusr/home home
ln -s jusr/root root
ln -s jusr/usr usr
ln -s jusr/tmp tmp
ln -s jusr/var var
#链接目录，注意链接的目录
```

### 创建fstab

```
#ee /jail/www.fstab
#将公共只读系统挂载到项目目录
/jail/j1/ /jail/www/ mullfs ro 0 0
#将项目数据目录挂载到项目目录
/jail/js/www/ /jail/www/jusr/ mullfs ro 0 0
```

创建fstab

```
ee /jail/www.fstab
#将公共只读系统挂载到项目目录
/jail/j1/ /jail/www/ mullfs ro 0 0
#将项目数据目录挂载到项目目录
/jail/js/www/ /jail/www/jusr/ mullfs ro 0 0
awk
```

写入 jail.conf

#全局部分

```
exec.start = "/bin/sh /etc/rc";
exec.stop = "/bin/sh /etc/rc.shutdown";
exec.clean;
mount.devfs;
allow.raw_sockets = 1;
allow.sysvipc = 1;
```

#网关 没用就不写

interface = “网卡地址“；
#主机名也可以用变量代替

hostname = “$name.domain.local”;
#jail 位置，也可以用变量
path = “/jail/$name”;

#ip地址

ip4.addr = 192.168.1.$ip;

#fstab位置

mount.fstab = /jail/www.fstab；
www {
$ip=2

#不使用fstab,使用

#mount.fstab =””；

#替换全局
}

## 删除文件没有权限

chflags -R noschg directory
