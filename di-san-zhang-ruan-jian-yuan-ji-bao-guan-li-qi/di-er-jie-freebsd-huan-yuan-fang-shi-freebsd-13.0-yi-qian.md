# 第二节 FreeBSD 换源方式（FreeBSD 13.0以前）

**注意：以下教程使用北京交通大学自由与开源软件镜像站，如果故障请翻到页面底部参考其他镜像站使用。**

{% embed url="https://mirror.bjtu.edu.cn" %}

### pkg 源:pkg 源提供二进制安装包. <a href="#pkg-yuan-pkg-yuan-ti-gong-er-jin-zhi-an-zhuang-bao" id="pkg-yuan-pkg-yuan-ti-gong-er-jin-zhi-an-zhuang-bao"></a>

FreeBSD 中 pkg 源分为系统级和用户级两个源.不建议直接修改 /etc/pkg/FreeBSD.conf,因为该文件会随着基本系统的更新而发生改变.

创建用户级源目录:

`#mkdir -p /usr/local/etc/pkg/repos`

创建用户级源文件:

`#ee /usr/local/etc/pkg/repos/bjtu.conf`

写入以下内容:

```
bjtu: {  
url: "pkg+http://mirror.bjtu.edu.cn/reverse/freebsd-pkg/${ABI}/quarterly",  
mirror_type: "srv",  
signature_type: "none",  
fingerprints: "/usr/share/keys/pkg",  
enabled: yes
}
FreeBSD: { enabled: no }
```

若要获取滚动更新的包,请将`quarterly`修改为`latest`.请注意,`CURRENT`版本只有`latest`.

若要使用https,请先安装security/ca\_root\_nss,并将`http`修改为`https`,最后使用命令`#pkg update -f`刷新缓存即可.

### ports 源:提供源码方式安装软件的包管理器

创建或修改文件`#ee /etc/make.conf`:

写入以下内容:

`MASTER_SITE_OVERRIDE?=http://mirror.bjtu.edu.cn/reverse/freebsd-pkg/ports-distfiles/`

### portsnap 源:打包的 ports文件

编辑portsnap配置文件 `#ee /etc/portsnap.conf` :

将`SERVERNAME=portsnap.FreeBSD.org` 修改为`SERVERNAME=freebsd-portsnap.mirror.bjtulug.org`

获取portsnap更新:

`#portsnap fetch extract`

### freebsd-update 源:提供基本系统更新

编辑`#ee /etc/freebsd-update.conf` 文件:

将`ServerName update.FreeBSD.org` 修改为`ServerName freebsd-update.mirror.bjtulug.org`

例:从 FreeBSD 12 升级到 13.0

`#freebsd-update -r 13.0-RELEASE upgrade`

## 其他镜像站

网易开源镜像站&#x20;

{% embed url="https://mirrors.163.com" %}

中国科学技术大学开源软件镜像

{% embed url="https://mirrors.ustc.edu.cn" %}

freebsd.cn （非官方）

{% embed url="http://freebsd.cn" %}
