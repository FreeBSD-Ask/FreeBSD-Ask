# 第 9.4 节 jail 更新

如果要同时管理多个jail,那么在升级jail的时候就要对每个jail单独进行一遍操作，这不仅非常耗时而且相当无聊。通过建立统一的模板，可以让所有jail共用一个基础环境，同时拥有各自的可写空间，互不干扰。

本教程将建立以下的目录结构（你也可以自行更改）：

一、```/jail/mroot```是模板，是所有jail的共用只读部分，在本例中将被挂载到```/jail/www```。

二、```/jail/skel```是框架，方便创建jail，本身并不为任何jail使用。

三、```/jail/www```是 jail ```www```运行的根目录，也是只读模板的挂载点，本身是个空目录。

四、```/jail/www/s```是 jail ```www```的可写部分的挂载点，也是个空目录。

五、```/jail/files/www```是 jail ```www```的可写部分的实际存放位置，将被挂载到```/jail/www/s```

如果要创建多个jail，则重复三四五三个部分，这样所有的jail都会共用```/jail/mroot```

## 创建模板目录



```
# mkdir -p /jail/j1
#然后放入基本目录，上边说过不再写
```


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

## 创建框架目录

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

## 创建数据目录

就是复制一份骨架给他用

`# cp -R /jail/j2/ /jail/js/www/`

## 创建项目目录

```
# mkdir -p /jail/www/
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
