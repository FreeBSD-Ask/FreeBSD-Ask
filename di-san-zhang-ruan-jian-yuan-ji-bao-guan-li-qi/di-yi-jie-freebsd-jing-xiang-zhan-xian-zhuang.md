# 第一节 FreeBSD 镜像站现状

## 现状 <a href="xian-zhuang" id="xian-zhuang"></a>

　　主要问题在于官方无论如何也不开放 rsync 且不接受镜像站的官方二级镜像申请。

　　多次联系均无二次联系，如邮件列表，大概五次，其中三次回应，两次无回应。其主要回复内容为“深表歉意，但台湾地区已有镜像”。并未直接说明如何镜像，此外特别向科大 Linux 协会(其中其他镜像站并未理会，如清华大学 TUNA 协会)申请镜像，对方提到，FreeBSD 也是无人回应。中国大陆目前没有 FreeBSD 官方镜像站。

　　如有朋友们能够联系 FreeBSD 官方，还望早日开放镜像，lftp 不能解决问题。此外，Kernel 或者 Base system 源码 SVN 速度更加感人，除非安装系统的时候安装源码，否则… 国内网络环境如此，提升速度采取代理方式也是基本功，但是，不能够要求每个人都一样，提供便捷的网络服务，方便更多人的使用，才是发展 FreeBSD 的核心要义。

　　请朋友们注意这一点，镜像站是基础设施，就像那句话，“要想富，先修路”，如果通往 FreeBSD 的康庄大道不通，那就全是荆棘的小道。

　　在此号召能够联系到 FreeBSD 官方的朋友们，首先解决这一基本问题。

　　目前开放的非官方 issue 镜像申请：

USTC：

{% embed url="https://github.com/ustclug/mirrorrequest/issues/172" %}

{% embed url="https://github.com/ustclug/mirrorrequest/issues/171" %}

　　目前已经关闭的非官方 issue 镜像申请：

TUNA：

{% embed url="https://github.com/tuna/issues/issues/16" %}

## 官方给出的镜像站基本要求

服务器的Root 权限，这一点上国内的大学开源镜像站不会给与；

IPv6 及 CN2 网络——国内也很缺乏；

BGP 网络；

足够的存储空间（约50TB）和 1G 带宽；

上述计算机 5 台。

备案问题——需要专门公司组织才能给 cn.FreeBSD.org 备案；

还有最大的问题，没有钱； 　

## 非官方镜像站

FreeBSD 在中国大陆境内没有非官方镜像站；

FreeBSD 目前在大陆非官方镜像站有 4 个：

USTC

{% embed url="https://mirrors.ustc.edu.cn" %}

仅 pkg ports

ChinaFreeBSD

{% embed url="http://chinafreebsd.cn/article/chinafreebsd-resouce" %}

或者 freebsd.cn

北京交通大学自由与开源镜像站（四类源

mirror.bjtu.edu.cn

联系方式:

{% embed url="https://t.me/bjtumirror" %}

网易 163 镜像站（仅 ports 源

　　FreeBSD 官方联系方式：

[_freebsd-hubs@freebsd.org_](mailto:freebsd-hubs@freebsd.org)__
