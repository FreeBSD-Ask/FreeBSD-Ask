# 第二节 FreeBSD 换源方式

**对于失去安全支持的版本，如 FreeBSD 9.0 是没有 pkg 源可用的，只能使用当时的 ports 编译安装软件。**

{% embed url="https://mirror.bjtu.edu.cn" %}

**本文对于一个源列出了多个镜像站，无需全部配置，只需选择其一即可。**

## pkg 源:pkg 源提供二进制安装包. 

FreeBSD 中 pkg 源分为系统级和用户级两个源.不建议直接修改`/etc/pkg/FreeBSD.conf`,因为该文件会随着基本系统的更新而发生改变.

创建用户级源目录:

`# mkdir -p /usr/local/etc/pkg/repos`

### 北京交通大学自由与开源软件镜像站

创建用户级源文件:

`# ee /usr/local/etc/pkg/repos/bjtu.conf`

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

**若要获取滚动更新的包,请将`quarterly`修改为`latest`.请注意,`CURRENT`版本只有`latest`.**

**若要使用https,请先安装security/ca\_root\_nss,并将`http`修改为`https`,最后使用命令`# pkg update -f`刷新缓存即可,下同。**



## ports 源:提供源码方式安装软件的包管理器

创建或修改文件`# ee /etc/make.conf`:

写入以下内容:

`MASTER_SITE_OVERRIDE?=http://mirror.bjtu.edu.cn/reverse/freebsd-pkg/ports-distfiles/`

## portsnap 源:打包的 ports文件

编辑portsnap配置文件 `# ee /etc/portsnap.conf` :

将`SERVERNAME=portsnap.FreeBSD.org` 修改为`SERVERNAME=freebsd-portsnap.mirror.bjtulug.org`

获取portsnap更新:

`# portsnap fetch extract`

## freebsd-update 源:提供基本系统更新

注意：只有一级架构的 release 版本才提供该源。也就是说 current 和 stable 是没有的。关于架构的支持等级说明请看：

{% embed url="https://www.freebsd.org/platforms" %}

编辑`# ee /etc/freebsd-update.conf` 文件:

将`ServerName update.FreeBSD.org` 修改为`ServerName freebsd-update.mirror.bjtulug.org`

例:从 FreeBSD 12 升级到 13.0

`# freebsd-update -r 13.0-RELEASE upgrade`

# 其他镜像站

**注意：FreeBSD 目前在中国大陆并没有官方镜像站提供，具体可参考前一节。**

网易开源镜像站 （pkg+ ports）

{% embed url="https://mirrors.163.com" %}

中国科学技术大学开源软件镜像 (pkg + ports)

{% embed url="https://mirrors.ustc.edu.cn" %}

freebsd.cn (pkg + ports + update + portsnap)

{% embed url="http://freebsd.cn" %}

南京大学开源镜像站（pkg + ports）

{% embed url="https://mirrors.nju.edu.cn" %}
