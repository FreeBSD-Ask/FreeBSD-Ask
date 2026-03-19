# 1.1 什么是 UNIX？

## 何为 UNIX？

UNIX 作为操作系统发展史上的里程碑式成果，其内涵历经了从技术实现到文化符号的深刻演变。从前，UNIX 是一款操作系统。它最初使用汇编语言编写，后主要由 C 语言重写。UNIX 起源于美国电话电报公司（American Telephone & Telegraph，AT&T）的贝尔实验室。

现在，它是一种 **[标准规范](https://www.opengroup.org/openbrand/register/xym0.htm)**、一款 **[法律上的商标](https://www.opengroup.org/openbrand/register/index2.html)**，更是一种 **哲学思想** 和一项 **软件工程原则**。这种多维度的身份界定，使得 UNIX 超越了单纯的技术范畴，成为现代操作系统设计的思想源泉。


> Only systems that are fully compliant and certified according to the Single UNIX Specification are qualified to use the UNIX® trademark.（只有完全符合并经过《单一 UNIX 规范》认证的系统，才有资格使用 UNIX® 商标。）——[UNIX® Certification](https://www.opengroup.org/openbrand/register/)

---

查询美国专利商标局 UNIX 商标注册情况，见图 1-1。

![图 1-1 法律上的商标](../.gitbook/assets/usshangbiao.png)

---

UNIX 认证查询网址：[The Open Group official register of UNIX Certified Products](http://www.opengroup.org/openbrand/register) [备份](https://web.archive.org/web/20260108065248/https://www.opengroup.org/openbrand/register/)，见图 1-2。

![图 1-2 UNIX 认证查询](../.gitbook/assets/unixrenzheng.png)


现在，我们可以知道认证 UNIX 需要满足以下两项核心要件：

1. 技术标准要求：[符合单一 UNIX 规范](https://www.opengroup.org/openbrand/register/xym0.htm) [备份](https://web.archive.org/web/20260114071648/https://www.opengroup.org/openbrand/register/xym0.htm)
2. 法律与费用要求：缴纳相应的[认证费用](https://www.opengroup.org/openbrand/Brandfees.htm) [备份](https://web.archive.org/web/20260114154111/https://www.opengroup.org/openbrand/Brandfees.htm)


可以看到，常见的经过认证的 UNIX 操作系统有苹果公司（Apple）的 macOS。从商标角度讲，macOS 可以称得上是标准的 UNIX 操作系统。~~故，要安装 UNIX 的人可以去黑苹果了~~

>**技巧**
>
>macOS/iOS 等与 BSD 的关系
>
>从历史角度看，macOS（以及由此衍生的 iOS、iPadOS 等）的核心层（Darwin）确实基于 BSD 代码，并融合了其他技术。它可被视为一款独立的、类 BSD 的操作系统分支，与 OpenBSD、NetBSD 和 FreeBSD 等系统类似。参见 [《苹果的开源基石：macOS 和 iOS 背后的 BSD 传统》](https://book.bsdcn.org/fan-yi-wen-zhang-cun-dang/2024-nian-11-yue/apple) [备份](https://web.archive.org/web/20260115132720/https://book.bsdcn.org/fan-yi-wen-zhang-cun-dang/2024-nian-11-yue/apple)
>
>所以看似是安卓和苹果之争，其实是 Linux 与 BSD 之争。~~也许也是大教堂与市集之争。~~


## 传统的 Unix 哲学观（以《UNIX 编程艺术》为核心）

Unix 哲学是在 UNIX 操作系统长期的开发实践中逐渐形成的一套设计理念，它影响了无数后来的操作系统和软件的开发思路。作为软件工程领域的重要思想遗产，Unix 哲学为系统设计提供了一套经过实践检验的方法论框架，具有重要的理论与实践价值。

>**思考题**
>
>> Those who do not understand Unix are condemned to reinvent it, poorly. （那些不懂 Unix 的人注定要再造一个四不像式 Unix）
>>
>>——[Henry Spencer](https://www.nasa.gov/history/alsj/henry.html) [备份](https://web.archive.org/web/20260115025048/https://www.nasa.gov/history/alsj-and-afj/)
>
>作者亨利·斯宾塞（Henry Spencer）并未明确批评哪个操作系统，那么你认为，现在这句话更适合哪个常见的操作系统？为什么？

Unix 哲学源于 UNIX 操作系统的开发实践，并由肯·汤普森（Ken Thompson）与丹尼斯·里奇（Dennis Ritchie）等早期核心开发者共同塑造与提炼。Unix 哲学一言以蔽之，即大道至简（“keep it simple, stupid”），其核心主张可归纳为以下原则：

- 小即美
- 一个程序只做一件事
- 原型先行
- 可移植性先于高效率性
- 避免使用不必要的二进制格式或复杂表示
- 沉默是金（无报错就沉默，成功则无输出，不显示操作进度等）
- 避免仅用户界面（避免无命令行，仅 GUI）

### 参考文献

- 《UNIX 编程艺术》，埃里克·雷蒙德（Eric Raymond）著，ISBN：9787121176654，电子工业出版社。
- 《Linux/Unix 设计思想》，迈克·甘卡兹（Mike Gancarz）著，ISBN：9787115266927，人民邮电出版社。（已绝版）
- [The Open Group Standards Process](https://www.opengroup.org/standardsprocess/certification.html) [备份](https://web.archive.org/web/20260115021154/https://www.opengroup.org/standardsprocess/certification.html)


## Unix 的一段历史

Unix 的诞生与一段充满故事的历史紧密相连，让我们从它的前身 Multics 开始说起。

### Multics

Multics 是一个对 Unix 产生直接影响的重要项目。1964 年，麻省理工学院（Massachusetts Institute of Technology，MIT）推出了兼容分时系统（Compatible Time-Sharing System，CTSS），是当时最具创新性的操作系统。有了 CTSS 这种高效的操作系统，研究人员决定设计一个更好的版本——多路复用信息和计算服务（Multiplexed Information and Computing Service，Multics）系统。

Multics 意图创造强悍的新软件和比肩 IBM 7094 功能更丰富的新硬件，麻省理工学院邀请了两家公司来帮忙。美国通用电气公司（General Electric，GE）负责设计及生产有全新硬件特性、能更好地支撑分时及多用户体系的计算机。贝尔实验室在计算机发展早期就开发了自己的操作系统，因此麻省理工学院邀请了贝尔实验室与美国通用电气公司共同开发 Multics。

最终 Multics 的开发陷入了困境，Multics 设计了大量的程序及功能，经常塞入很多不同的东西，导致系统过于复杂。1969 年，由于在贝尔实验室看来作为一套信息处理工具，它已经无法实现为实验室提供计算服务的目标，设计太昂贵了，于是在同年 4 月，贝尔实验室退出 Multics 项目，只剩麻省理工学院和美国通用电气公司继续开发。

### UNICS

UNICS 是 Unix 的直接前身，它的诞生源于一个游戏项目。贝尔实验室退出 Multics 开发项目后，项目组成员肯尼斯·蓝·汤普森（Kenneth Lane Thompson）找到一台数字设备公司（Digital Equipment Corporation，DEC）PDP-7 型计算机，该计算机性能有限，只有 4KB 内存，但图形界面较为美观。Thompson 在其上开发了游戏 Space Travel（《星际旅行》）。PDP-7 的磁盘转速远低于计算机的读写速度，为解决这一问题，Thompson 编写了磁盘调度算法以提高磁盘总吞吐量。

>**技巧**
>
>《星际旅行》已被移植，现在可以直接在网页上玩，项目位于 [C port of Ken Thompson's Space Travel](https://github.com/mohd-akram/st) [备份](https://web.archive.org/web/20260115021129/https://github.com/mohd-akram/st) ，在线游玩的网站是 [Space Travel](https://akr.am/st/) [备份](https://web.archive.org/web/20260114153540/https://akr.am/st/) 。

如何测试这个新的算法？需要往磁盘上装载数据，Thompson 需要写一个批量写数据的程序。

他需要写三个程序，每周写一个：创建代码的编辑器，将代码转换为 PDP-7 能运行的机器语言汇编器，再加“内核的外层——操作系统就完成了”。

新的 PDP-7 操作系统开发不久后，Thompson 和几位同事讨论，当时系统尚未命名，最初称为“UnICS”（非复用信息和计算机服务，Uniplexed Information and Computing Service），后来改名为 UNIX，更易于记忆。
