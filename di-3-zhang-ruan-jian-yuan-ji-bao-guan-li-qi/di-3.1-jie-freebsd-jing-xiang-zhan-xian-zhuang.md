# 第 3.1 节 FreeBSD 镜像站现状

## 现状

主要问题在于官方无论如何也不开放 rsync 且不接受镜像站的官方二级镜像申请（原因可能是没有钱或者防止篡改镜像文件？）。

多次联系均无二次联系，如邮件列表，大概五次，其中三次回应，两次无回应。其主要回复内容为“深表歉意，但台湾地区已有镜像”。并未直接说明如何镜像，此外特别向中国科学技术大学 Linux 用户协会（其中其他镜像站并未理会，如清华大学 TUNA 协会）申请镜像，对方提到，FreeBSD 也是无人回应。中国大陆目前没有 FreeBSD 官方镜像站。

如有朋友们能够联系 FreeBSD 官方，还望早日开放镜像，非官方镜像站不能解决问题。此外，Kernel 或者 Base system 源码 SVN 速度更加感人，除非安装系统的时候安装源码，否则……国内网络环境如此，提升速度采取代理方式也是基本功，但是，不能够要求每个人都一样，提供便捷的网络服务，方便更多人的使用，才是发展 FreeBSD 的核心要义。

请朋友们注意这一点，镜像站是基础设施，就像那句话，“要想富，先修路”，如果通往 FreeBSD 的康庄大道不通，那就全是荆棘的小道。

在此号召能够联系到 FreeBSD 官方的朋友们，首先解决这一基本问题。

目前开放的非官方 issue 镜像申请：

USTC：

<https://github.com/ustclug/mirrorrequest/issues/172>

<https://github.com/ustclug/mirrorrequest/issues/171>

目前已经关闭的非官方 issue 镜像申请：

TUNA：

<https://github.com/tuna/issues/issues/16>

## 官方给出的镜像站基本要求

- 服务器的 root 权限，这一点上国内的大学开源镜像站不会给与；
- IPv6 及 CN2 网络——国内也很缺乏；
- BGP 网络；
- 足够的存储空间（约 50TB）和 1G 带宽；
- 上述计算机 5 台。
- 备案问题——需要专门公司/社会组织才能给 cn.FreeBSD.org 备案；
- 还有最大的问题，没有钱；

细节可看 <https://docs.freebsd.org/en/articles/hubs/>
## 非官方镜像站

FreeBSD 在中国大陆境内没有官方镜像站；在中国台湾地区有官方镜像站。

FreeBSD 目前在大陆非官方镜像站有若干个（详见第二节。）：

- USTC（仅 pkg ports）

  <https://mirrors.ustc.edu.cn>

- ~~http://freebsd.cn（四类源）~~【不可用】
- 北京交通大学自由与开源镜像站（四类源）【不可用】

  <https://mirror.bjtu.edu.cn>

  联系方式:

  <https://t.me/bjtumirror>

- 网易 163 镜像站（仅 ports pkg）
- 南京大学开源镜像站

  无法进行有效联络，找不到负责人。

FreeBSD 官方联系方式：

[freebsd-hubs@freebsd.org](mailto:freebsd-hubs@freebsd.org)

> 附
>
> [FreeBSD 个人主页](https://people.freebsd.org/homepage.html)
>
> [FreeBSD committer 名单](https://github.com/freebsd/freebsd-src/blob/fcaf016796cc0272a8c239850fa87244eebefe13/usr.bin/calendar/calendars/calendar.freebsd)

