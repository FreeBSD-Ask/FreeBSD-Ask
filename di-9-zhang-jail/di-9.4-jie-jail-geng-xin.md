# 第 9.4 节 jail 更新



## 创建 jail 目录

创建 4 个 分别是模板 骨架 数据 项目

### 创建模板目录

```
# mkdir -p /jail/j1
#然后放入基本目录，上边说过不再写
```

### 创建骨架目录

```
# mkdir -p /jail/j2
#移动目录 etc usr tmp var root
```

```
# cd /jail/j2/ # 注意目录
# mv /jail/j1/etc ./etc
# mv /jail/j1/tmp ./tmp
# mv /jail/j1/var ./var
# mv /jail/j1/root ./root
```

### 创建数据目录

就是复制一份骨架给他用

`# cp -R /jail/j2/ /jail/js/www/`

### 创建项目目录

```
# mkdir -p /jail/www/
```

### 建立链接

```
# cd /jail/j1 #cd 到模板目录
# mkdir -p jusr #创建用来做链接数据的目录
# ln -s jusr/etc etc
# ln -s jusr/home home
# ln -s jusr/root root
# ln -s jusr/usr usr
# ln -s jusr/tmp tmp
# ln -s jusr/var var
#链接目录，注意链接的目录
```

### 创建 fstab

```
#ee /jail/www.fstab
#将公共只读系统挂载到项目目录
/jail/j1/ /jail/www/ mullfs ro 0 0
#将项目数据目录挂载到项目目录
/jail/js/www/ /jail/www/jusr/ mullfs ro 0 0
```

创建 fstab

```
# ee /jail/www.fstab
#将公共只读系统挂载到项目目录
/jail/j1/ /jail/www/ mullfs ro 0 0
#将项目数据目录挂载到项目目录
/jail/js/www/ /jail/www/jusr/ mullfs ro 0 0
```

写入 jail.conf

```
#全局部分


exec.start = "/bin/sh /etc/rc";
exec.stop = "/bin/sh /etc/rc.shutdown";
exec.clean;
mount.devfs;
allow.raw_sockets = 1;
allow.sysvipc = 1;


#网关 没用就不写

interface = "网卡地址"； #主机名也可以用变量代替


hostname = "$name.domain.local";
#jail 位置，也可以用变量
path = "/jail/$name";


#ip地址


ip4.addr = 192.168.1.$ip;


#fstab位置


mount.fstab = /jail/www.fstab；
www {
$ip=2
#不使用fstab,使用
#mount.fstab =""；

#替换全局
}
```
