# 第 1.1 节 UNIX、Unix-like、Linux 简介

## 什么是 UNIX？

UNIX 从前是一个操作系统。最后由 C 语言改写产生。——源自 AT\&T 的贝尔实验室

现在是一种 **标准规范、法律上的商标**。更是一种 **哲学思想**，一项 **软件工程原则。**

UNIX 认证查询网址：[The Open Group official register of UNIX Certified Products](http://www.opengroup.org/openbrand/register)

现在，我们可以知道认证 UNIX 需要：

1. [符合单一 UNIX 规范](https://www.opengroup.org/openbrand/register/xym0.htm)
2. 交钱认证

![The Open Group official register of UNIX Certified Products](../.gitbook/assets/unixrenzheng.png)

可以看到，常见的，经过认证的 UNIX 操作系统有 Apple MacOS。即从商标的角度上讲，MacOS 可以称得上是标准的 UNIX 操作系统。

### UNIX 哲学与软件工程原则简介

>**注意**
>
>>Linux 已几乎完全背离了 UNIX 哲学，不提 Linux Kernel 引入 Systemd。单是 Wayland、Btrfs、PulseAudio 就能看出这一点。
>
>所以你在 Linux 上，强调传统的 UNIX 哲学或软件工程原则——比如一切皆文件，管道流等，并不十分妥帖。


>**思考题**
>
>>在 Huawei EulerOS（基于 CentOS） 都能通过 UNIX 认证的今天，再讨论是不是 UNIX 这件事看起来已经变得索然无味，毫无意义可言。甚至 Windows 加钱也能认证成为 UNIX（其也实现了大部分 POSIX)。
>
>结合全文，是 UNIX 哲学过时了，不再适应现代操作系统了？还是 Linux 将开源之路引向了苦难哲学（失去了其原本的简洁和透明性？），走了改旗易帜的邪路？


>**思考题**
>
> _**Those who do not understand Unix are condemned to reinvent it,poorly.**_ ——[Henry Spencer](https://www.nasa.gov/history/alsj/henry.html)（那些不懂 Unix 的人注定要重复发明一个蹩脚的 Unix）
>
>>作者 Henry Spencer 并未明确批评哪个操作系统，那么你认为，现在这句话更适合哪个常见的操作系统？是 FreeBSD、Windows、Android、MacOS 亦或 Linux？又为什么？

Unix 哲学源于 UNIX 操作系统的开发，作者是 Ken Thompson。Unix 哲学一言以蔽之即大道至简（“keep it simple, stupid”）：

- 小即美
- 一个程序只做一件事
- 原型先行
- 可移植性先于高效率性
- 不使用二进制
- 避免仅用户界面（无命令行，仅 GUI）

……

### 参考文献

- 《UNIX 编程艺术》，Eric Raymond 著，ISBN: 9787121176654，电子工业出版社。
- 《Linux/Unix 设计思想》，Mike Gancarz 著，9787115266927，人民邮电出版社。（已绝版）
- [The Open Group Standards Process](https://www.opengroup.org/standardsprocess/certification.html)

### 详细说明

#### Mutlics

1964 年麻省理工学院推出的 CTSS（兼容分时系统），是当时最有创造性的操作系统，有了 CTSS 这种高效的操作系统，麻省理工学院的研究人员决定做一个更好的版本。他们开始设计 Multics 系统。Mutlics 意思是多路复用信息和计算服务。

Multics 意图创造强悍的新软件和比肩 IBM 7094 功能更丰富的新硬件，麻省理工学院邀请了两家公司来帮忙。美国通用电气公司负责设计及生产有全新硬件特性、能更好地支撑分时及多用户体系的计算机，贝尔实验室在计算机发展早期就开发了自己的操作系统，因此麻省理工邀请了贝尔实验室与美国通用电气公司共同开发 Multics。

最终 Multics 的开发陷入了困境，Multics 设计了大量的程序及功能，经常塞入很多不同的东西进去，导致系统过于复杂。1969 年，由于在贝尔实验室看来作为一套信息处理工具，它已经无法为实验室提供计算服务的目标，它的设计太昂贵了，于是在同年 4 月，贝尔实验室退出 Multics 项目，只剩麻省理工和美国通用电气公司继续开发。

#### UNICS

贝尔实验室退出 Multics 开发项目后，项目组成员 Kenneth Lane Thompson 找到一台 DEC PDP-7 型计算机，这台计算机性能不算强大，只有 4KB 内存，但是图形界面比较美观，Thompson 用他写了个太空游戏（Space Travel），PDP-7 有个问题就是磁盘转速远远低于计算机的读写速度，为了解决这个问题，Thompson 写了磁盘调度算法来提高磁盘总吞吐量。

如何测试这个新的算法？需要往磁盘上装载数据，Thompson 需要写一个批量写数据的程序。

他需要写三个程序，每周写一个：创建代码的编辑器，将代码转换为 PDP-7 能运行的机器语言汇编器，再加“内核的外层——操作系统就完成了”。

新的 PDP-7 操作系统编写没多时，Thompson 和几个同事讨论，当时新系统还没有名字，当时它被命名为“UNICS”，UNICS 最后改名为 **UNIX**，这个名字更加方便记忆。



## 什么是 Unix-like？

Unix-like 即类 Unix，亦即一切基于 UNIX 的操作系统，基本遵守 POSIX 规范，而没有获得第一节中所说的 UNIX 的认证。

也就是说，除了 Windows，基本上世界上大多数操作系统都被叫做 Unix-like，其中就包括 Linux 和 FreeBSD。

## 什么是 Linux？

UNIX 标准 SUS 包含了 POSIX 标准，是其超集。Linux 实现了 POSIX 标准，但是未进行 [POSIX 认证](http://get.posixcertified.ieee.org/)。本质上说 Linux 最初是 UNIX 的一款仿制品。


### 狭义 Linux 是内核

[Linux kernel](https://www.kernel.org/) 项目 1990；

### 广义 Linux 是 GNU/Linux

GNU/Linux = Linux kernel + GNU 等软件 + 包管理器

>**[Chimera Linux](https://chimera-linux.org/) 除外。**

Linux 全称为 GNU/Linux；[GNU 项目](https://www.gnu.org/) 1984；

具体地：

- GNU/Linux 发行版 = Ubuntu、RHEL、Deepin、OpenSUSE……
  - Ubuntu = Linux kernel + apt/dpkg + Gnome
  - OpenSUSE = Linux kernel + libzypp/rpm + KDE

> **注意**
>
> 如果你还是不明白，建议亲自安装试试 [Gentoo](https://www.gentoo.org/downloads/)（stage3）或 [Slackware](http://www.slackware.com/)，再不明白可以试试 [Gentoo（stage1）](https://wiki.gentoo.org/wiki/Stage_file)或 [LFS](https://www.linuxfromscratch.org/lfs/)。
>
> **上述操作较为复杂，需要一定的经验与基础知识。**

