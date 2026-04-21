# 9.3 FreeBSD 镜像站现状

本节介绍了 FreeBSD 镜像站的当前格局、历史演进及相关技术考量。

## 镜像站现状与基本格局

### 官方未开放 rsync 服务

当前 FreeBSD 镜像站生态面临两个核心约束：一是官方 rsync 服务暂未对公众开放；二是项目未接受镜像站的官方二级镜像申请。这两项政策共同构成了镜像站部署的基本限制条件。

根据可查证的历史信息，FreeBSD 项目最迟在 2015 年 5 月就已停止公开 rsync 服务。相关文档 [Add small section explaining we are not allowing public mirrors of packages and possible workarounds.](https://reviews.freebsd.org/R9:3418e47d2f6cd8dd04ac934f38d136ba9101a5a8) 记录了项目禁止公共包镜像的决策及替代方案。官方给出的理由如下：

> Due to very high requirements of bandwidth, storage and administration the FreeBSD Project has decided not to allow public mirrors of packages.
>
> 由于对带宽、存储和管理的要求极高，FreeBSD 项目决定不允许公共镜像软件包。

---

2025 年 2 月获取的最新官方回复进一步阐明了项目立场：

> On Fri, 28 Feb 2025, at 17:45, ykla wrote:
>> How to mirror pkg and update from official mirror sites?
>
> As we replied on several occasions before: pkg and freebsd-update need machines under our control with internet connectivity to the rest of our cluster.
>
> At one point someone tried to offer a machine in Nanjing. That then turned into a virtual machine and the conversation went nowhere. We can't use a virtual machine. We need real hardware. With real storage. And real transit.

翻译如下：

> 2025 年 2 月 28 日星期五 17:45，ykla 写道：
>> 如何通过官方镜像站点进行 pkg 镜像和系统更新？
>
> 正如我们此前多次回复的，pkg 和 freebsd-update 功能需要由我们管控的物理服务器支持（注：此处指 root 权限），这些服务器需与我们的集群保持网络连接。
>
> 此前有人曾提议提供南京的一台机器，但后续方案变更为虚拟机形式后讨论便陷入停滞。我们无法使用虚拟机方案，需要真实的硬件设备（注：指裸金属）、实体存储介质和物理网络传输链路。

### 未开放的可能原因分析

#### 安全性因素

从历史记录追溯，FreeBSD 基础设施集群在过去曾发生安全入侵事件。在全面转向 pkg 分发机制后，项目便终止了外部镜像的授权。这一战略决策可能与保障软件供应链完整性与安全性直接相关。

参考文献：

- delphij. FreeBSD.org 这次的入侵事件[EB/OL]. (2012-12-17)[2026-03-25]. <https://blog.delphij.net/posts/2012/12/freebsdorg-2/>. 中文说明。
- FreeBSD Project. FreeBSD.org intrusion announced November 17th 2012[EB/OL]. (2012-11-17)[2026-03-25]. <http://www.freebsd.org/news/2012-compromise.html>. FreeBSD 项目官方说明。

#### 传输机制因素

当前集群的数据同步机制采用了基于 ZFS 文件系统的直接传输方式（通过 `zfs send` / `zfs receive` 命令实现），而非传统的 rsync 镜像站同步模式。这一技术选型构成了外部镜像可行性的潜在限制因素。

#### 资源限制因素

根据 [[NEW MIRROR] New full mirror in Belgium](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=288631)，集群管理员 bofh 回复如下：

> There are couple of reasons:
>
> 1. Bandwidth from our central servers. Increasing number of community mirrors require more bandwidth in case everyone starts pulling altogether like just after a new quarterly branch
> 2. While many sites are excited to create mirrors as they think they have real bandwidth in reality they lose their moral bandwidth in couple of days and our mirrors are no longer in sync. We are often communicated regarding the problems of other community mirrors. We already operate in a tight schedule and often overseeing other mirrors is just another nail in the wall.
> 3. We still accept mirrors but on a different way. If people can sponsor bare metal we would be happy to deploy a new mirror. However our mirror requirements are pretty high. You can have a look at the following to understand our requirements:
>
> - <https://wiki.freebsd.org/Teams/clusteradm/generic-mirror-layout>
>
> - <https://wiki.freebsd.org/Teams/clusteradm/tiny-mirror>

译文：

> 有几个原因：
>
> 1. 来自我们中心服务器的带宽。社区镜像数量增加时，如果大家都同时开始拉取，比如在一个新的 quarterly 分支刚发布之后，就会需要更多带宽。
>
> 2. 许多站点在创建镜像时非常兴奋，确信自己拥有真实的带宽，但实际上，他们的“道义带宽”往往在几天后就耗尽了，也不再同步我们的镜像。我们经常收到关于其他社区镜像问题的沟通。我们本来日程就很紧，再去监督其他镜像就如同给墙上再钉一颗钉子。
>
> 3. 我们仍然接受镜像，但方式有所不同。如果有人能够赞助裸金属服务器，我们会很乐意部署新的镜像。不过，我们对镜像的要求相当高。你可以查看以下内容来了解我们的要求：
>
> - <https://wiki.freebsd.org/Teams/clusteradm/generic-mirror-layout>
>
> - <https://wiki.freebsd.org/Teams/clusteradm/tiny-mirror>

> **思考题**
>
>> 我认为，“不接受社区镜像”与“拒绝镜像”是两件完全不同的事情。Ubuntu 拥有大量社区镜像，而其中真正被官方认可的只是极少数。这本质上体现了用户的自由选择。用户可以选择看起来更安全的官方镜像，也可以为了速度而牺牲部分安全与隐私。我们没有资格替用户做这个选择。
>>
>> 对于一个快要渴死的人来说，问题不是他该喝可口可乐还是污水。
>
>> 在关闭 rsync 且不提供其他同步渠道的情况下，而多数开源镜像都依赖 rsync，他们实际上阻碍了 FreeBSD 项目的自身发展。项目声称带宽不足，但我怀疑 OpenBSD 或 NetBSD 的带宽能显著更多。然而它们却通过开放与自由的方式，让用户自己掌握选择。
>>
>> 就像今天发生的事情一样：我批评了一个据说用于测试并切换不同 FreeBSD 包镜像的测速工具，可安装它却需要额外拉上 45 个依赖。感觉就像在想象皇帝应该穿什么衣服、用哪种金锄头锄地——或者发明一种只能在白天亮灯的灯泡。
>>
>> 我并非在批评任何个人；我真正质疑的是，这套系统及其设计本身是否合理。
>>
>> FreeBSD 只是在技术上切换到了 Git，思想还停留在 SVN 时代。SVN 是集中式的、统一的、强权限的；Git 是分布式的，去权限的，允许自由分支的。当代互联网强调的是去中心化和分享。没有为什么，正如城市化和逆城市化一样都是合理的，也都是不合理的，只是一种趋势要求我们必须这样那样做，否则就会失去自身存在的合理性。你说得有道理也是现实，他们可能同步几天就撒手不管了。而问题在于，选择权应该取决于用户而不是项目本身。我认为这是一种家长制作风的体现。这也表明了老项目转型的困难更多不是技术而是理念。
>
>> 即日已抵龙南，明日入巢，四路兵皆已如期并进，贼有必破之势。某向在横水，尝寄书仕德云：“破山中贼易，破心中贼难。”区区剪除鼠窃，何足为异？若诸贤扫荡心腹之寇，以收廓清平定之功，此诚大丈夫不世之伟绩。数日来谅已得必胜之策，捷奏有期矣。何喜如之！
>>
>> 日孚美质，诚可与共学，此时计已发舟。倘未行，出此同致意。廨中事以累尚谦，想不厌烦琐。小儿正宪，犹望时赐督责。（《王阳明全集·卷四·文录一·与杨仕德薛尚谦书》）
>
>> 结合王阳明平定南赣，改革吏治，肃清朝野，破官、民“心中贼”的历史史实，请读者阐述：强迫某人使之自由，这本身是一种自由还是法西斯主义？

### 中国大陆目前没有 FreeBSD 官方镜像站

经多次沟通尝试（包括通过邮件列表联系约五次，其中三次获得回应，两次未获回应），均未形成有效推进。官方主要回复为“深表歉意，但台湾地区已有镜像”，未就镜像申请的具体流程提供进一步说明。此外，曾特别向中国科学技术大学 Linux 用户协会申请镜像，反馈 FreeBSD 官方亦未有回应。

目前开放的非官方 issue 镜像申请：

USTC：

- <https://github.com/ustclug/mirrorrequest/issues/172>
- <https://github.com/ustclug/mirrorrequest/issues/171>

目前已经关闭的非官方 issue 镜像申请：

TUNA: <https://github.com/tuna/issues/issues/16>

## 呼吁高校学生参与镜像 FreeBSD

如果有条件搭建非官方镜像，可以使用 USTCLUG 所提供的同步脚本：

1. USTCLUG. FreeBSD-pkg Script[EB/OL]. [2026-03-25]. <https://github.com/ustclug/ustcmirror-images/blob/master/freebsd-pkg/sync.sh>.
2. USTCLUG. FreeBSD-ports Script[EB/OL]. [2026-03-25]. <https://github.com/ustclug/ustcmirror-images/blob/master/freebsd-ports/sync-ports.sh>.

来搭建非官方镜像站。赠人玫瑰，手有余香。

优先建议高校学生使用校内资源搭建，或者直接从 USTC 的 `rsync` 服务来同步。建议同步前先咨询 USTCLUG，以免带来不必要的麻烦，联系方式：[lug@ustc.edu.cn](mailto:lug@ustc.edu.cn)。参考 [科大源同步方法与注意事项](https://mirrors.ustc.edu.cn/help/rsync-guide.html) 来进行同步。

## 官方给出的镜像站基本要求

- 服务器的 root 权限，这一要求在国内同样稀缺，开源镜像站通常不会给予；
- IPv6 及 BGP 网络——国内也很缺乏；其中 CN2 网络在中国大陆同样稀缺，但并非 FreeBSD 官方要求，而是国内网络环境的额外考量；
- 足够的存储空间（约 50 TB）和 1 G 带宽；
- 上述服务器共计 5 台；
- 备案问题——需要专门公司/社会组织才能给 cn.FreeBSD.org 备案；
- 还有一个最大的问题：**缺乏资金**。

细节可查看：

- 单个镜像：<https://wiki.freebsd.org/Teams/clusteradm/tiny-mirror>
- 完整镜像：<https://wiki.freebsd.org/Teams/clusteradm/generic-mirror-layout>

## 非官方镜像站

FreeBSD 在中国大陆境内没有官方镜像站；在中国台湾地区有官方镜像站。

FreeBSD 在中国大陆境内为数不多且能正常同步的镜像站，均未使用 `rsync` 等方式进行同步，而是采取了一些特殊“手段”，参见 USTCLUG 所提供的同步脚本：

- [FreeBSD-pkg 脚本](https://github.com/ustclug/ustcmirror-images/blob/master/freebsd-pkg/sync.sh)
- [FreeBSD-ports 脚本](https://github.com/ustclug/ustcmirror-images/blob/master/freebsd-ports/sync-ports.sh)

> **注意**
>
> 呼吁有余力者对上述两个脚本进行维护修订，以减轻 USTC 镜像站的压力，同时为境内提供更好的 FreeBSD 镜像服务。

FreeBSD 目前在大陆有若干个非官方镜像站：

- 中国科学技术大学镜像站（USTC）（pkg、ports、pub）<https://mirrors.ustc.edu.cn/>
  - FreeBSD Pub <https://mirrors.ustc.edu.cn/freebsd/>
  - FreeBSD Packages <https://mirrors.ustc.edu.cn/freebsd-pkg/>
  - FreeBSD Ports
    - [使用文档](https://mirrors.ustc.edu.cn/help/freebsd-ports.html)
    - <https://mirrors.ustc.edu.cn/freebsd-ports/>
  - 联系方式：[lug@ustc.edu.cn](mailto:lug@ustc.edu.cn)

- 网易 163 镜像站（pkg 和 ports 上游均为中国科学技术大学）<https://mirrors.163.com/>
  - FreeBSD Pub <https://mirrors.163.com/freebsd/>
  - FreeBSD Packages <https://mirrors.163.com/freebsd-pkg/>
  - FreeBSD Ports <https://mirrors.163.com/freebsd-ports/>

- 南京大学开源镜像站（pkg 和 ports 上游均为中国科学技术大学）<https://mirrors.nju.edu.cn/>
  - FreeBSD Pub <https://mirrors.nju.edu.cn/freebsd/>
  - FreeBSD Packages <https://mirrors.nju.edu.cn/freebsd-pkg/>
  - FreeBSD Ports <https://mirrors.nju.edu.cn/freebsd-ports/>
  - 联系方式：[GitHub Issue](https://github.com/nju-lug/NJU-Mirror-Issue/issues)

FreeBSD 官方联系方式：

- [mirror-admin@freebsd.org](mailto:mirror-admin@freebsd.org)
- [freebsd-hubs@freebsd.org](mailto:freebsd-hubs@freebsd.org)，这个邮件列表似乎已不再活跃。

## 其他思路或解决方案

自行使用 Poudriere 进行构建并分发。如 [RISC-V FreeBSD-pkg 软件源上线！11619+ 预编译包助力快速构建 FreeBSD 环境](https://mp.weixin.qq.com/s/ngv3eZh1TEVgk3Pn3XfRBg)（项目已停止维护）

## 课后习题

1. 查找 USTCLUG 提供的 FreeBSD-pkg 同步脚本，在本地搭建一个最小化的 pkg 镜像站，并测试其是否可以被其他 FreeBSD 系统作为软件源使用。

2. 比较 FreeBSD、OpenBSD 和 NetBSD 三个项目的镜像站授权政策差异，分析这种差异如何影响各自的用户群体规模与生态健康度。

3. 假设有一台裸金属服务器可以赞助给 FreeBSD 项目，设计一个完整的镜像站部署方案。
