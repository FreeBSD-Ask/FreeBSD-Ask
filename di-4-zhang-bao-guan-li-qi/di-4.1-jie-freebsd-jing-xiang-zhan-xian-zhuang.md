# 4.1 FreeBSD 镜像站现状

## 现状

### 官方拒不开放 rsync

主要问题在于官方无论如何也不开放 rsync 且不接受镜像站的官方二级镜像申请。

根据目前可查信息，FreeBSD 项目至迟在 2015 年 5 月就停止了公开 rsync。参见 [Add small section explaining we are not allowing public mirrors of packages and possible workarounds.](https://reviews.freebsd.org/R9:3418e47d2f6cd8dd04ac934f38d136ba9101a5a8)。给出的说明理由是：

>Due to very high requirements of bandwidth, storage and adminstration the FreeBSD; Project has decided not to allow public mirrors of packages.
>
>由于对带宽、存储和管理的要求极高，FreeBSD 项目决定不允许公共镜像软件包。

这个理由着实让人摸不到头脑。

---

2025 收到的回复：

>On Fri, 28 Feb 2025, at 17:45, ykla wrote:
>> How to mirror pkg and update from official mirror sites?
>
>As we replied on several occasions before: pkg and freebsd-update need machines under our control with internet connectivity to the rest of our cluster.
>
>At one point someone tried to offer a machine in Nanjing. That then turned into a virtual machine and the conversation went nowhere. We can't use a virtual machine. We need real hardware. With real storage. And real transit.

翻译如下：

>2025 年 2 月 28 日 星期五 17:45，ykla 写道：
>> 如何通过官方镜像站点进行 pkg 镜像和系统更新？
>
>正如我们此前多次回复的：pkg 和 freebsd-update 功能需要由我们管控的物理服务器支持（**注：这里对方指 root 权限**），这些服务器需与我们的集群保持网络连接。
>
>此前有人曾提议提供南京的一台机器，但后续方案变更为虚拟机形式后讨论便陷入停滞。我们无法使用虚拟机方案，需要真实的硬件设备（**注：对方指裸金属**）、实体存储介质和物理网络传输链路。

---

### 中国大陆没有 FreeBSD 官方镜像站

多次联系均无二次联系，如邮件列表，大概五次，其中三次回应，两次无回应。其主要回复内容为“深表歉意，但台湾地区已有镜像”。并未直接说明如何镜像，此外特别向中国科学技术大学 Linux 用户协会（其中其他镜像站并未理会，如清华大学 TUNA 协会）申请镜像，对方提到，FreeBSD 也是无人回应。

国内网络环境如此，提升速度采取代理方式也是基本功，但是，不能够要求每个人水平都一样，提供便捷的网络服务，方便更多人的使用，才是发展 FreeBSD 的核心要义。请朋友们注意这一点，镜像站是基础设施，就像那句话，“要想富，先修路”，如果通往 FreeBSD 的康庄大道不通，则全是荆棘的小道。在此号召能够联系到 FreeBSD 官方的朋友们，首先解决这一基本问题。

目前开放的非官方 issue 镜像申请：

USTC：

- <https://github.com/ustclug/mirrorrequest/issues/172>
- <https://github.com/ustclug/mirrorrequest/issues/171>

目前已经关闭的非官方 issue 镜像申请：

TUNA: <https://github.com/tuna/issues/issues/16>

## 呼吁高校学生参与镜像 FreeBSD

如果你有办法或者能够有条件搭建非官方镜像，也可以使用 USTCLUG 所提供的同步脚本：

- [FreeBSD-pkg Script](https://github.com/ustclug/ustcmirror-images/blob/master/freebsd-pkg/sync.sh)
- [FreeBSD-ports Script](https://github.com/ustclug/ustcmirror-images/blob/master/freebsd-ports/sync-ports.sh)

来搭建非官方镜像站。赠人玫瑰，手留余香。

优先建议高校学生使用校内资源搭建，或者直接从 USTC 的 `rsync` 服务来同步。建议同步前先咨询 USTCLUG，以免带来不必要的麻烦，联系方式： [lug@ustc.edu.cn](mailto:lug@ustc.edu.cn)。参考[科大源同步方法与注意事项](https://mirrors.ustc.edu.cn/help/rsync-guide.html)来进行同步。

## 官方给出的镜像站基本要求

- 服务器的 root 权限，这一点上国内的大学开源镜像站不会给与；
- IPv6 及 CN2 网络——国内也很缺乏；
- BGP 网络；
- 足够的存储空间（约 50TB）和 1G 带宽；
- 上述计算机 5 台。
- 备案问题——需要专门公司/社会组织才能给 cn.FreeBSD.org 备案；
- 还有最大的问题，**没有钱**

细节可看：

- 单个镜像：<https://wiki.freebsd.org/Teams/clusteradm/tiny-mirror>
- 完整镜像：<https://wiki.freebsd.org/Teams/clusteradm/generic-mirror-layout>

## 非官方镜像站

FreeBSD 在中国大陆境内没有官方镜像站；在中国台湾地区有官方镜像站。

FreeBSD 在中国大陆境内的唯一几个能正常同步的镜像站，均未使用 `rsync` 等方式进行同步，都是采取的一些特殊"手段"，参见 USTCLUG 所提供的同步脚本：

- [FreeBSD-pkg 脚本](https://github.com/ustclug/ustcmirror-images/blob/master/freebsd-pkg/sync.sh)
- [FreeBSD-ports 脚本](https://github.com/ustclug/ustcmirror-images/blob/master/freebsd-ports/sync-ports.sh)

>**注意**
>
>我们呼吁有余力者对上述两个脚本进行维护修订以减轻 USTC 镜像站的压力，同时为境内提供更好的 FreeBSD 镜像服务。

FreeBSD 目前在大陆非官方镜像站有若干个：

- 中国科学技术大学镜像站（USTC）（pkg、ports、pub）<https://mirrors.ustc.edu.cn/>
  - FreeBSD Pub <https://mirrors.ustc.edu.cn/freebsd/>
  - FreeBSD Packages <https://mirrors.ustc.edu.cn/freebsd-pkg/>
  - FreeBSD Ports
    - [使用文档](https://mirrors.ustc.edu.cn/help/freebsd-ports.html)
    - <https://mirrors.ustc.edu.cn/freebsd-ports/>
  - 联系方式: [lug@ustc.edu.cn](mailto:lug@ustc.edu.cn)

- 网易 163 镜像站（pkg 和 ports 上游均为中科大）<https://mirrors.163.com/>
  - FreeBSD Pub <https://mirrors.163.com/freebsd/>
  - FreeBSD Packages <https://mirrors.163.com/freebsd-pkg/>
  - FreeBSD Ports <https://mirrors.163.com/freebsd-ports/>

- 南京大学开源镜像站（pkg 和 ports 上游均为中科大）<https://mirrors.nju.edu.cn/>
  - FreeBSD Pub <https://mirrors.nju.edu.cn/freebsd/>
  - FreeBSD Packages <https://mirrors.nju.edu.cn/freebsd-pkg/>
  - FreeBSD Ports <https://mirrors.nju.edu.cn/freebsd-ports/>
  - 联系方式：[Github Issue](https://github.com/nju-lug/NJU-Mirror-Issue/issues)

FreeBSD 官方联系方式：

- [mirror-admin@freebsd.org](mailto:mirror-admin@freebsd.org)
- [freebsd-hubs@freebsd.org](mailto:freebsd-hubs@freebsd.org)，这个邮件列表似乎已经死亡，没有任何人回复和收发邮件。
