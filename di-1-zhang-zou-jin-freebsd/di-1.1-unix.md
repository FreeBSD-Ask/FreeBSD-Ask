# 第 1.1 节 操作系统的历程：UNIX、BSD、Linux 与 FreeBSD 的起源

## 什么是 UNIX？

从前，UNIX 是一款操作系统。最后由 C 语言改写产生。——源自 `AT&T`（American Telephone & Telegraph，美国电话电报公司）的贝尔实验室。

现在是一种 **标准规范**、一款 **法律上的商标**。更是一种 **哲学思想**，一项 **软件工程原则。**

---

查询美国专利商标局 UNIX 商标注册情况：

![法律上的商标](../.gitbook/assets/usshangbiao.png)

---

UNIX 认证查询网址：[The Open Group official register of UNIX Certified Products](http://www.opengroup.org/openbrand/register)

![The Open Group official register of UNIX Certified Products](../.gitbook/assets/unixrenzheng.png)


现在，我们可以知道认证 UNIX 需要：

1. [符合单一 UNIX 规范](https://www.opengroup.org/openbrand/register/xym0.htm)
2. 交钱认证


可以看到，常见的，经过认证的 UNIX 操作系统有 Apple macOS。即从商标的角度上讲，macOS 可以称得上是标准的 UNIX 操作系统。~~故，要安装 UNIX 的人可以去黑苹果了~~

>**技巧**
>
>macOS/iOS 等与 BSD 的关系
>
>从历史与现实来看，macOS/iOS 等基于 BSD 确凿无疑，但并非全然基于某款 BSD：macOS/iOS 等应该被理解为一款独立的 BSD 操作系统——同 OpenBSD、NetBSD 和 FreeBSD 一样。参见[《苹果的开源基石：macOS 和 iOS 背后的 BSD 传统》](https://book.bsdcn.org/fan-yi-wen-zhang-cun-dang/2024-nian-11-yue/apple)
>
>所以看似是安卓和苹果之争，其实是 Linux 与 BSD 之争。~~也许也是大教堂与市集之争。~~


### UNIX 哲学与软件工程原则简介

#### 传统的 Unix 哲学观（以《UNIX 编程艺术》为核心）

>**思考题**
>
>> Those who do not understand Unix are condemned to reinvent it, poorly. （那些不懂 Unix 的人注定要再造一个四不像式 Unix）
>>
>>——[Henry Spencer](https://www.nasa.gov/history/alsj/henry.html)
>
>作者 Henry Spencer 并未明确批评哪个操作系统，那么你认为，现在这句话更适合哪个常见的操作系统？为什么？

Unix 哲学源于 UNIX 操作系统的开发，作者是 Ken Thompson。Unix 哲学一言以蔽之即大道至简（“keep it simple, stupid”）：


- 小即美
- 一个程序只做一件事
- 原型先行
- 可移植性先于高效率性
- 不使用二进制
- 沉默是金（无报错就沉默，成功则无输出，不显示操作进度等）
- 避免仅用户界面（避免无命令行，仅 GUI）

##### 参考文献

- 《UNIX 编程艺术》，Eric Raymond 著，ISBN: 9787121176654，电子工业出版社。
- 《Linux/Unix 设计思想》，Mike Gancarz 著，9787115266927，人民邮电出版社。（已绝版）
- [The Open Group Standards Process](https://www.opengroup.org/standardsprocess/certification.html)

### 二十一世纪四分之一处的 Unix 哲学观

事实证明，技术很快就会过时。这也是很多人在今天认为谈论 Unix，谈论 Unix 哲学毫无意义的重要原因。因为他们的确过时了，将 Unix 哲学简单仅归结为纯粹而具体的技术性操作，这是对 Unix 哲学最大的误读。也是促使不少人走上苦难哲学这条改旗易帜的歪路的诱因。

真正的 Unix 哲学绝不是上面那些陈旧古板的祖宗之法，Unix 哲学的精髓在于以人为本，真正的 Unix 哲学是一种人道主义。在不同的年代，Unix 哲学应有不同的诠释，但是归根结底是一种人道主义——我们要高扬人的主体性。正是为了好玩，为了玩太空旅行才诞生了 Unix，为了“Just For Fun” 才有了 Linux：这无不说明，是改造计算机以适应人，而非强迫让人去适应所谓计算机的规则，去迎合吹捧那些本就拙劣不堪的设计思路。

大道至简在西方哲学中表现为奥卡姆的剃刀，即“如无必要，勿增实体。”这在某种程度上也启发了现象学的观念，我们应该把一些自行设定的观念从我们的脑子里排除出去，只留下我们能够直接感受到的东西——即回到事物本身。

我们现在回到操作系统本身，回到计算机本身，计算机不应成为一种额外的负担，而应为人所服务——正如 FreeBSD 的口号“The Power To Serve（服务的力量）”那样。

所以，现代的 Unix 哲学具体不应该是“避免仅用户界面”，而应该是“避免仅命令行”。每款程序都应该报告自己的操作进度，最好还有进度条（无论是否真的体现了进度），可以使用参数静默上述行为，但默认行为不应该是所谓的沉默是金——你有多少次在使用 `dd`、`cp` 等命令的时候渴望看到一个进度条而不是什么都没有，即使是卡死了也不知道？ChatGPT 这种程序无疑是对“小即美”，“一个程序只做一件事”最大的反叛。人们需要什么，就应该有什么。

### Unix 的一段历史

#### Mutlics

1964 年麻省理工学院推出的 CTSS（兼容分时系统），是当时最有创造性的操作系统，有了 CTSS 这种高效的操作系统，麻省理工学院的研究人员决定做一个更好的版本。他们开始设计 Multics 系统。Mutlics 意思是多路复用信息和计算服务。

Multics 意图创造强悍的新软件和比肩 IBM 7094 功能更丰富的新硬件，麻省理工学院邀请了两家公司来帮忙。美国通用电气公司负责设计及生产有全新硬件特性、能更好地支撑分时及多用户体系的计算机，贝尔实验室在计算机发展早期就开发了自己的操作系统，因此麻省理工邀请了贝尔实验室与美国通用电气公司共同开发 Multics。

最终 Multics 的开发陷入了困境，Multics 设计了大量的程序及功能，经常塞入很多不同的东西进去，导致系统过于复杂。1969 年，由于在贝尔实验室看来作为一套信息处理工具，它已经无法为实验室提供计算服务的目标，它的设计太昂贵了，于是在同年 4 月，贝尔实验室退出 Multics 项目，只剩麻省理工和美国通用电气公司继续开发。

#### UNICS

贝尔实验室退出 Multics 开发项目后，项目组成员 Kenneth Lane Thompson 找到一台 DEC PDP-7 型计算机，这台计算机性能不算强大，只有 4KB 内存，但是图形界面比较美观，Thompson 用他写了个游戏 *Space Travel*（《星际旅行》），PDP-7 有个问题就是磁盘转速远远低于计算机的读写速度，为了解决这个问题，Thompson 写了磁盘调度算法来提高磁盘总吞吐量。

>**技巧**
>
>《星际旅行》被人移植了，现在可以直接在网页上玩，项目位于 [C port of Ken Thompson's Space Travel](https://github.com/mohd-akram/st)，在线游玩的网站是 [Space Travel](https://akr.am/st/)。
>
>~~虽然操作简单但是看不懂怎么玩~~

如何测试这个新的算法？需要往磁盘上装载数据，Thompson 需要写一个批量写数据的程序。

他需要写三个程序，每周写一个：创建代码的编辑器，将代码转换为 PDP-7 能运行的机器语言汇编器，再加“内核的外层——操作系统就完成了”。

新的 PDP-7 操作系统编写没多时，Thompson 和几个同事讨论，当时新系统还没有名字，当时它被命名为“UnICS”（Uniplexed Information and Computing Service，非复用信息和计算机服务），UnICS 最后改名为 **UNIX**，这个名字更加方便记忆。


## 什么是 Unix-like？

Unix-like 即类 Unix，亦即一切符合 UNIX 标准的操作系统，基本遵守 POSIX 规范，而没有获得第一节中所说的 UNIX 的认证。

也就是说，除了 Windows，基本上世界上大多数操作系统都被叫做 Unix-like，其中就包括 Linux 和 FreeBSD。

## GNU 与自由软件运动

由于 Unix 在后期愈发封闭，许可证昂贵、受限制于商业公司等原因，RMS（Richard Matthew Stallman）就想创造一款自由且兼容 Unix 的操作系统。

- 1983 年，RMS 发表[《GNU 宣言》](https://www.gnu.org/gnu/manifesto.html)，其中 GNU 即 GNU is Not Unix（GNU 不是 Unix）。GNU 是一款操作系统——旨在完全替代 Unix。
- 1984 年，创建 [GNU 项目](https://www.gnu.org/)
- 1985 年，RMS 创建自由软件基金会（Free Software Foundation，FSF）
- 1989 年，FSF 发布 GPLv1 
- 1991 年，FSF 发布 GPLv2
- 2007 年，FSF 发布 GPLv3

一开始他为 Unix 写了很多实用程序（用户空间），然而 GNU 的目标操作系统始终缺乏稳定的内核（即使到了 2025 年，[GNU Hurd](https://hurd.gnu.org/) 仍未完成）。Linux 内核的诞生为这一困境带来了突破。作为一款由 Linux 内核和 GNU 软件拼凑起来的操作系统，Linux 不断地的 GNU 化，成为了一款操作系统——这就是 GNU/Linux 其中 GNU 的来历，然而很多人无视这一事实，掩盖了 GNU 软件的贡献。这是因为：Linux 内核由创始人 Linus Torvalds 一人裁决。Linus 本人对 FSF 和 RMS 并不认可。所以显而易见的，Linux 项目的理念与自由软件运动的理念、乃至于同真正开源的理念（Linux 内核里存在大量非开源非自由的存在，参见 [Linux-libr](https://www.fsfla.org/ikiwiki/selibre/linux-libre/)）都存在明显的张力。并且 Linux 内核使用 GPLv2，而非 GNU 推荐的 GPLv3。事实是，Linus 随意移除 Linux 项目的参与者，却未同时移除他们贡献的代码。——这同自由还是开源理念都是冲突的。

我们将 Linux 之前这段时间称作“自由软件运动”（代表人物 RMS）。Linux 的流行促成了另一种理念的兴起，即“开源运动”——代表人物有 Eric S. Raymond，OSI（Open Source Initiative，开放源代码促进会）的创始人，《UNIX 编程艺术》、《大教堂与集市》的作者；Bruce Perens，Debian 项目前领导人——想想下面有关开源的定义为什么是自 [Debian 的开源定义 DFSG](https://www.debian.org/social_contract#guidelines) 衍生而来？

自由软件运动并未停止，但人们对开源的误解却越来越重。

### 自由软件运动与开源运动之间的张力

需要注意的是，根据笔者与 RMS 的通讯，其强调的 GNU 与自由软件运动并不强调“开源”（甚至是反对开源），而是强调“Free” 式自由。有些人可能认为现在的“开源”仅仅是由 [OSI 定义](https://opensource.org/osd)的那样，这是一种极其片面的观点。

>致所有阅读我邮件的 NSA（美国国家安全局）和 FBI 特工：请考虑一下，捍卫美国宪法以抵御一切敌人，无论是外国的还是本国的，是否需要你效仿斯诺登的做法。
>
>>但是我有点困惑：GNU 项目是否强制要求开发必须开源？因为 GNU 通用公共许可证（GPL）强制开源。
>
>GNU 项目并不倡导“开源”。我们从不用这个词，除非是为了表达与它的分歧。我们代表的是自由软件（Free Software）——自由如同自由的言论。我们致力于在计算中为用户争取自由。
>
>请参见：<https://gnu.org/philosophy/free-software-even-more-important.html>
>
>“开源”这个词是一些反对自由软件运动的人发明的——他们与我们意见相左。他们想谈论同样的软件，却又掩盖自由的理念。
>
>关于自由软件与开源的区别，请参见：<https://gnu.org/philosophy/open-source-misses-the-point.html>
>
>另请阅读 Evgeny Morozov 的文章：<https://thebaffler.com/salvos/the-meme-hustler>，他在文中也探讨了这一点。
>
>所以请不要问我们关于“开源”或“开放”某些东西的问题。我们不是那样思考的。你真正应该问我们的是：我们如何以自由软件的方式做事情。
>
>>它属于 GNU 项目，那么 GNU 项目是否也会强制他人……
>
>我不太确定你所说的“强制”是什么意思，这里可能存在误解。通常我们会告诉人们我们认为什么是对的，什么是错的，但我们无法命令他们做什么。
>
>唯一的例外是他们使用了 GPL 许可的软件代码。在这种情况下，GNU GPL 本身是一种法律上的约束，规定了他们如何使用这些代码。它要求他们在再发布代码时，尊重其他用户的自由。
>
>这正是 copyleft（著佐权）的意义所在。
>
>如果你还有更多问题，请写信至 licensing@gnu.org。

此为私人通信引用，不涉及隐私话题。

## 什么是 Linux？

```
+-----------------------------------------+
|               应用程序层                |
|  (浏览器/办公软件/开发工具/数据库等)     |
+-----------------------------------------+
|             图形界面（可选）             |
|       (GNOME █ KDE █ XFCE 等)           |
+-----------------------------------------+
|           核心系统工具层                  |
|  █ GNU 基础工具 (bash/gcc/glibc 等)      |
|  █ 包管理器 (apt/yum/pacman 等)          |
|  █ 初始化系统 (systemd/OpenRC 等)         |
+-------------------+---------------------+
|                   |   狭义的 Linux       |
|    Linux 内核层   +---------------------+
|                   | (直接控制硬件的中枢) |
+-------------------+---------------------+
|                   硬件层                 |
|    (CPU █ 内存 █ 硬盘 █ 网卡 █ 外设)     |
+-----------------------------------------+
```

Linux 是一款开源软件。

Linux 之名来自 Linux 之父 Linus Torvalds。

Linux 受启发于 Minix（UNIX 版权限制下的产物），一款设计用于教学的微内核操作系统。当时 22 岁的 Linus Torvalds 是芬兰赫尔辛基大学计算机科学系的研究生。

Linus Torvalds 的硕士毕业论文是[《Linux: A Portable Operating System》](https://www.cs.helsinki.fi/u/kutvonen/index_files/linus.pdf)（Linux：一款可移植的操作系统），他在 1997 年（28 岁）获得理学硕士学位。为什么花了这么长时间都没被学校清退呢？芬兰是典型的学分制国家。根据芬兰赫尔辛基大学官网说明，并无[最长学习期限](https://studies.helsinki.fi/instructions/article/expiry-studies?) 限制，仅规定某课程成绩有效时间为十年。“你的课程到期不会影响你在大学继续学习的权利”。

>我们探讨了在将 Linux 操作系统移植到多种 CPU 和总线架构时所暴露出的硬件可移植性问题。我们还讨论了软件接口的可移植性问题，尤其是与能够共享同一硬件平台的其他操作系统之间的二进制兼容性问题。文中描述了 Linux 所采取的方法，并对其中几个架构进行了更为详细的介绍。
>
>《Linux：一款可移植的操作系统》论文摘要

>**技巧**
>
>现在，几乎每颗英特尔处理器上都运行着 Minix。
>
>~~或许 Minix 才是世界上最流行的操作系统~~

UNIX 标准 SUS 包含了 POSIX 标准，是其超集。Linux 实现了 POSIX 标准，但是未进行 [POSIX 认证](http://get.posixcertified.ieee.org/)。

本质上说 Linux 是 UNIX 的一种仿制品或者说克隆产物（类似于人与机器人的关系）。


### 狭义 Linux 是内核

[Linux kernel](https://www.kernel.org/) 项目 1991；

### 广义 Linux 是 GNU/Linux

GNU/Linux = Linux kernel + GNU 等软件 + 包管理器

>**[Chimera Linux](https://chimera-linux.org/) 除外。**

Linux 全称为 GNU/Linux；

GNU's Not Unix，从 GNU 这个名字（GNU 不是 UNIX）你也能看出来 Linux 与 UNIX 并无直接关联。

具体地：

- GNU/Linux 发行版 = Ubuntu、RHEL、Deepin、OpenSUSE……
  - Ubuntu = Linux kernel + apt/dpkg + Gnome
  - OpenSUSE = Linux kernel + libzypp/rpm + KDE

> **注意**
>
> 如果你还是不明白，建议亲自安装试试 [Gentoo](https://www.gentoo.org/downloads/)（stage3）或 [Slackware](http://www.slackware.com/)，再不明白可以试试 [Gentoo（stage1）](https://wiki.gentoo.org/wiki/Stage_file) 或 [LFS](https://www.linuxfromscratch.org/lfs/)。
>
> 上述操作较为复杂，需要一定的经验与基础知识。


## 什么是 FreeBSD？

FreeBSD 不是 Linux。FreeBSD 也不是 UNIX 的克隆产物。FreeBSD 是一款自由软件。

![](../.gitbook/assets/nolinux.png)

---

FreeBSD 这个词语由两部分构成，即“Free”和“BSD”。

BSD 最初是由加州大学伯克利分校（University of California, Berkeley）所开发的，意为 `Berkeley Software Distribution`（伯克利软件发行版）。

Free 则代表 Liberty 式自由和免费两种含义。

FreeBSD 日为 6 月 19 日。FreeBSD 基金会和社区在这天庆祝 FreeBSD 的生日。——[Join us to celebrate FreeBSD Day!](https://freebsdfoundation.org/freebsd-day/)

### UNIX 之船：FreeBSD 是不是 UNIX？

这个问题远没有想象中的那么清楚明白。我看到不少讨论者，甚至是亲历当初那段岁月的人，亦难以回答或澄清。或者只是简单的说，BSD 并未进行过任何 UNIX 认证，没有持有法律上的商标就草草终结话题；更有甚者只是笼统地说 FreeBSD 是 UNIX 的延续者与正统继承者，仅是“有实无名”；还有人认为，BSD 之于 UNIX，正如 Linux 之于 UNIX。

之所以有上述这些不同的回答，正是因为这个问题不是能够简单地套用法律上的商标归属或者代码上继承性进行分析的纯粹技术性难题。这其实牵涉到了一个深刻的本体论哲学问题——我们究竟是不能两次踏进同一条河流，还是一次也不能踏进同一条河流？（类似的问题如谷堆问题、秃头问题，感兴趣的读者可参见 SEP 条目“[Identity Over Time](https://plato.stanford.edu/entries/identity-time)”、“[Sorites Paradox](https://plato.stanford.edu/entries/sorites-paradox/)”）。对这个问题回答如何，其实映射着你的哲学观与科学技术观。

>>**忒修斯之船**
>>
>>忒修斯和雅典青年安全返航所乘的是有三十支桨的大帆船，雅典人把这只船一直保存到德米特里·法勒琉斯的时代。他们一次又一次地拆掉了朽烂的旧船板，换上坚实的新船板。从此以后，这只船就成为哲学家们就事物的发展问题展开争论时经常援引的实例，一派认为它还是原来那只船，另一派争辩说它已不再是原来的船了。
>>
>>- [古希腊] 普鲁塔克. 希腊罗马名人传[M]. 译者：黄宏煦 主编 / 陆永庭 / 吴彭鹏, 第1版. 商务印书馆, 1990-11. 第 23 页（23）。
>
>**思考题**
>
>①如果这艘船替换了若干组件，这艘船是不是忒修斯之船？
>
>②如果有一天，这艘船原有的所有组件都被完全替换了一遍，这艘船还是不是忒修斯之船？
>
>③如果把所有替换下来的组件拼凑起来，组成一艘新船，这艘船是不是忒修斯之船？


BSD 操作系统并非复制品，而是 AT&T 研究 UNIX（Research Unix）操作系统的开源衍生版本，也是现代 UNIX® System V 的祖先。在 4.4BSD 以前，BSD 全称为 BSD UNIX。

最初，Unix 是 `AT&T` 开发的操作系统，可以获取源代码，但并非开源。在 20 世纪 70 年代末，伯克利大学的计算机系统研究小组（Computer Systems Research Group，CSRG）开始对 Unix 进行深入研究，并为其开发了大量用户空间的程序，形成了名为 BSD（Berkeley Software Distribution，伯克利软件套件）的新系统。随着时间推移，BSD 系统逐渐发展，加入了许多创新，比如实现了 TCP/IP 协议栈。尽管 Unix 内核经历了多个版本的演变，但到了 90 年代，Net/2 版本发布后，Unix 内核中的 AT&T 代码已经被完全替换，成为了一款没有专利代码的系统。BSD 系统逐渐演化成为 4.2BSD，BSD 4.4-lite……进而成为了 386BSD。

在此过程中，BSD 和 AT&T 之间的关系发生了变化，最终引发了法律争议，导致 BSD 系统的分裂。1993 年，BSD 的核心代码分裂为两个主要的项目：NetBSD 和 FreeBSD。1996 年，OpenBSD 从 NetBSD 中复刻出来；2003 年，DragonFlyBSD 从 FreeBSD 中复刻出来。

```
AT&T UNIX (1969)
 │
 │ (衍生出早期版本)
 ▼
Research UNIX (AT&T 专有)
 │
 │ (1977年: 伯克利 CSRG 开始开发)
 ▼
BSD UNIX (1BSD, 2BSD...4.3BSD) 
 │
 │ (1991年: Net/2 发布)
 ▼
Net/2 (完全替换 AT&T 代码)
 │
 ├───────────────┐
 │               │
 ▼               ▼
386BSD      4.4BSD-Lite (1994)
(1992)       │
 │           ├─────────────────┐
 ▼           ▼                 ▼
┌───────────────────┐      FreeBSD
│    诉讼案          │      (1993)
│ (AT&T vs. BSDi)   │         │
└───────────────────┘         ├───────────────┐
       │                     ▼               ▼
       │                 FreeBSD         DragonFlyBSD
       │                分支版本          (2003)
       ▼                     
    NetBSD (1993)
       │
       ├───   ────┐
       ▼               ▼
   OpenBSD      其他 BSD 变种
   (1996)      (NetBSD, FreeBSD
               OpenBSD 的后代)
```