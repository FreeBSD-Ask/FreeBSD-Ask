# 第 1.1 节 UNIX、Unix-like、Linux 简介

## 什么是 UNIX？

UNIX 从前是一个操作系统。最后由 C 语言改写产生。——源自 AT\&T 的贝尔实验室

现在是一个 **标准规范和商业商标**。更是 **一种哲学思想（KISS - Keep It Simple, Stupid! 一言以蔽之，即“大道至简”），软件工程原则（比如模块化、管道流等）**。

查询网址：[The Open Group official register of UNIX Certified Products](http://www.opengroup.org/openbrand/register)

我们现在可以知道认证 UNIX 需要：

1. 符合单一 UNIX 规范
2. 交钱认证

![](../.gitbook/assets/图片1.png)

> 常见的经过认证的 UNIX 操作系统有 MacOS。

**以下为详细说明：**

### Mutlics

1964 年麻省理工学院推出的 CTSS（兼容分时系统），是当时最有创造性的操作系统，有了 CTSS 这种高效的操作系统，麻省理工学院的研究人员决定做一个更好的版本。他们开始设计 Multics 系统。Mutlics 意思是多路复用信息和计算服务。

Multics 意图创造强悍的新软件和比肩 IBM 7094 功能更丰富的新硬件，麻省理工学院邀请了两家公司来帮忙。美国通用电气公司负责设计及生产有全新硬件特性、能更好地支撑分时及多用户体系的计算机，贝尔实验室在计算机发展早期就开发了自己的操作系统，因此麻省理工邀请了贝尔实验室与美国通用电气公司共同开发 Multics。

最终 Multics 的开发陷入了困境，Multics 设计了大量的程序及功能，经常塞入很多不同的东西进去，导致系统过于复杂。1969 年，由于在贝尔实验室看来作为一套信息处理工具，它已经无法为实验室提供计算服务的目标，它的设计太昂贵了，于是在同年 4 月，贝尔实验室退出 Multics 项目，只剩麻省理工和美国通用电气公司继续开发。

### UNICS

贝尔实验室退出 Multics 开发项目后，项目组成员肯·汤普逊（Kenneth Lane Thompson）找到一台 DEC PDP-7 型计算机，这台计算机性能不算强大，只有 4KB 内存，但是图形界面比较美观，汤普逊用他写了个太空游戏（Space Travel），PDP-7 有个问题就是磁盘转速远远低于计算机的读写速度，为了解决这个问题，汤普逊写了磁盘调度算法来提高磁盘总吞吐量。

如何测试这个新的算法？需要往磁盘上装载数据，汤普逊需要写一个批量写数据的程序。

他需要写三个程序，每周写一个：创建代码的编辑器，将代码转换为 PDP-7 能运行的机器语言汇编器，再加“内核的外层——操作系统就完成了”。

新的 PDP-7 操作系统编写没多时，汤普逊和几个同事讨论，当时新系统还没有名字，当时它被命名为“UNICS”，UNICS 最后改名为 **UNIX**，这个名字更加方便记忆。

> 在 Huawei EulerOS（基于 CentOS） 都能通过 UNIX 认证的今天，再讨论是不是 UNIX 这件事已经变得索然无味，毫无意义可言。甚至 Windows 加钱也能认证成为 UNIX（其也实现了大部分 POSIX)。

### UNIX 哲学简介

>我认为 Linux 的道路走歪了，它把 Unix 之路引向了苦难哲学，而且还在越走越歪，走了改旗易帜的邪路。单是 Linux Kernel 引入 Systemd 就能看出这一点。

Unix 哲学源于 UNIX 操作系统的开发，作者是 Ken Thompson。Unix 哲学一言以蔽之即大道至简（`keep it simple, stupid`）：

- 小即美
- 一个程序只做一件事
- 原型先行
- 可移植性先于高效率性
- 不使用二进制
- 避免仅用户界面（无命令行，仅 GUI）

……

参考文献：

- 《UNIX 编程艺术》，Eric Raymond 著，ISBN: 9787121176654，电子工业出版社。
- 《Linux/Unix 设计思想》，Mike Gancarz 著，9787115266927，人民邮电出版社。（已绝版）



## 什么是 Unix-like？

Unix-like 即类 Unix，亦即一切基于 UNIX 的操作系统，基本遵守 POSIX 规范，而没有获得第一节中所说的 UNIX 的认证。

也就是说，除了 Windows，基本上世界上大多数操作系统都被叫做 Unix-like，其中就包括 Linux 和 FreeBSD。

## 什么是 Linux？

> UNIX 标准 SUS 包含了 POSIX 标准，是其超集。Linux 实现了 POSIX 标准，但是没有进行 [POSIX 认证](http://get.posixcertified.ieee.org/)。本质上说 Linux 最初是 UNIX 的一个仿制品。
>
> _**Those who do not understand Unix are condemned to reinvent it,poorly.**_ ——[Henry Spencer](https://www.nasa.gov/history/alsj/henry.html)（那些不懂 Unix 的人注定要重复发明一个蹩脚的 Unix）

### 狭义是内核

Linux kernel 项目 1990；

### 广义是 GNU/Linux

GNU/Linux = Linux kernel + GNU 等软件 + 包管理器

>**[Chimera Linux](https://chimera-linux.org/) 除外。**

Linux 全称为 GNU/Linux；GNU 项目 1984；

具体地：

- GNU/Linux 发行版 = Ubuntu、RHEL、Deepin、OpenSUSE……
  - Ubuntu = Linux kernel + apt/dpkg + Gnome
  - OpenSUSE = Linux kernel + libzypp/rpm + KDE

> 注意：如果你还是不明白，建议亲自安装试试 Gentoo（stage3）或 Slackware，再不明白可以试试 Gentoo（stage1）或 LFS。都非常简单。

