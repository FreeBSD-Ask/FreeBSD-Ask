# 1.1 什么是 UNIX？

FreeBSD 源自 BSD，即加州大学伯克利分校开发的 UNIX® 版本。

## 何谓 UNIX？

UNIX 的内涵由具体技术实现演变为文化象征。UNIX 系统起源于美国电话电报公司（American Telephone & Telegraph，AT&T）贝尔实验室。

20 世纪 60 年代末至 70 年代初，UNIX 作为一款操作系统，最初采用汇编语言编写，后来主要以 C 语言重写。

20 世纪 80 年代以后，UNIX 逐渐成为一种 **[标准规范](https://www.opengroup.org/openbrand/register/xym0.htm)**。

在当代语境下，UNIX 不仅意味着法律上的 **[商标](https://www.opengroup.org/openbrand/register/index2.html)**，更是一种 **哲学思想** 和一系列 **软件工程原则**。

根据当前 UNIX 商标持有者开放组织（The Open Group）官网 [UNIX® Certification](https://www.opengroup.org/openbrand/register/) 所述：“Only systems that are fully compliant and certified according to the Single UNIX Specification are qualified to use the UNIX® trademark.”（只有完全符合《单一 UNIX 规范》并通过认证的系统，才有资格使用 UNIX® 商标）

---

查询美国专利商标局 UNIX 商标注册信息如下：

![法律上的商标](../.gitbook/assets/unix-trademark-uspto.png)

---

UNIX 操作系统认证查询网址：[The Open Group official register of UNIX Certified Products](http://www.opengroup.org/openbrand/register)。

![UNIX 认证查询](../.gitbook/assets/unix-certification-query.png)

根据开放组织要求，认证 UNIX 需要满足以下两项核心条件：

1. 技术标准要求：符合 [单一 UNIX 规范](https://www.opengroup.org/openbrand/register/xym0.htm)（Single UNIX Specification，SUS），该规范定义了 UNIX 系统必须实现的接口、命令、实用程序和库函数，确保不同 UNIX 操作系统之间互相兼容。
2. 法律与费用要求：缴纳相应的 [认证费用](https://www.opengroup.org/openbrand/Brandfees.htm)。

当前经认证的 UNIX 操作系统包括 Apple 公司的 macOS。从商标角度看，macOS 是符合标准的 UNIX 操作系统。~~故，要安装 UNIX 的人可考虑 macOS。~~

> **技巧**
>
> macOS/iOS 与 BSD 的关系
>
> 从历史角度看，macOS（以及由此衍生的 iOS、iPadOS 等）的核心层（Darwin）确实是基于 BSD 代码，并融合了其他技术。因此可将 macOS 系列操作系统视作独立的、类 BSD 操作系统分支，与 OpenBSD、NetBSD 和 FreeBSD 等系统具有同等地位。参见：Jason Perlow. Apple's Open Source Roots: The BSD Heritage Behind macOS and iOS[EB/OL]. (2024-07-08)[2026-03-26]. <https://thenewstack.io/apples-open-source-roots-the-bsd-heritage-behind-macos-and-ios/>.
>
> 表面观之，此为 Android 与 iOS 之争，实质则为 Linux 与 BSD 之争。~~这也许还是大教堂与市集之争。~~

## 传统的 UNIX 哲学观（以《UNIX 编程艺术》为核心）

UNIX 哲学是 UNIX 操作系统长期开发实践中逐渐形成的设计理念，由肯·汤普森（Ken Thompson）与丹尼斯·里奇（Dennis Ritchie）等早期核心开发者共同塑造。其核心主张可归纳为以下原则：

- **小即美**：程序应设计得简洁小巧，功能单一明确，便于理解和维护。
- **一个程序只做一件事**：每个工具专注于单一功能，通过组合多个工具协作完成复杂任务。
- **原型先行**：先快速构建可工作的原型，再逐步优化，避免过度设计。
- **可移植性先于高效性**：优先保证代码能在不同平台上运行，性能优化次之。
- **避免使用不必要的二进制格式或复杂表示**：使用简单、文本格式，便于人工阅读和处理。
- **沉默是金**：程序在正常执行时不应产生冗余输出，仅在出错时提示，成功操作无输出，不显示进度等。
- **避免仅用户界面**：应提供命令行接口，确保可通过脚本实现自动化操作。

这些原则在当时的软件设计中相辅相成，帮助开发者构建出简洁、高效、可维护的系统。FreeBSD 的开发实践深受 UNIX 哲学影响。FreeBSD 提供先进的网络功能、性能、安全与兼容性，这一目标同 UNIX 哲学中“可移植性先于高效性”及“小即美”等原则一脉相承。

FreeBSD 的手册页系统是 UNIX 哲学的典型体现：每个命令、系统调用和配置文件均配有独立的手册页，内容简明扼要，便于用户通过 `man` 命令随时查阅。

> **思考题**
>
>> 1. UNIX 哲学一言以蔽之，大道至简。“Keep it simple, stupid”。
>
>> 2. Brooks F P Jr. 人月神话[M]. UMLChina，译. 纪念典藏版. 北京：清华大学出版社，2023. ISBN: 978-7-302-63538-3
>
> 阅读上述文本和参考文献，如何理解 UNIX 哲学的局限性，以及背后的时代背景。

> **思考题**
>
>> Those who do not understand UNIX are condemned to reinvent it, poorly.（那些不懂 UNIX 的人注定要再造一个四不像式 UNIX。）
>>
>> SPENCER H. space news from Sept 28 AW&ST[EB/OL]. sci.space.shuttle, Google Groups, (1987-11-15)[2026-04-17]. <https://groups.google.com/g/sci.space.shuttle/c/L8-Upf8gZoY/m/NN6ngTI0K0QJ>.
>
> 亨利·斯宾塞（Henry Spencer）并未明确批评某一操作系统，试问，当前该论断更适用于何种主流操作系统？原因何在？

## UNIX 的一段历史

UNIX 的诞生有特定的历史背景，需追溯至前身 Multics。

### Multics 项目

Multics 是一个对 UNIX 产生直接影响的重要项目。1961 年，麻省理工学院（Massachusetts Institute of Technology，MIT）演示了 **兼容分时系统**（Compatible Time-Sharing System，CTSS），这是当时最具创新性的操作系统。在此基础上，研究人员于 1964 年决定设计更为先进的版本，即 **多路复用** 信息和计算服务（Multiplexed Information and Computing Service，Multics）系统。

Multics 旨在创造功能强大的新软件，以及比肩 IBM 7094 功能更丰富的新硬件。1965 年，通用电气公司（General Electric，GE）与贝尔实验室加入该项目，形成三方合作。其中，通用电气公司负责设计及生产具有全新硬件特性、以更好地支撑分时及多用户体系的计算机；贝尔实验室在计算机发展早期就开发了自己的操作系统，具备相关经验。

最终 Multics 的开发陷入困境，该系统设计了大量程序及功能，且频繁引入相互矛盾的组件，导致系统过于复杂。1969 年，贝尔实验室认为，作为信息处理工具，Multics 已无法实现为实验室提供计算服务的目标，且设计成本过高。同年 4 月，贝尔实验室退出 Multics 项目，仅麻省理工学院和通用电气公司继续开发。

### UNICS 的诞生

UNICS 是 UNIX 的直接前身，其诞生源于一项游戏项目。贝尔实验室退出 Multics 开发项目后，项目组成员肯尼斯·蓝·汤普森（Kenneth Lane Thompson）获取了一台数字设备公司（Digital Equipment Corporation，DEC）PDP-7 型计算机，该计算机性能有限，仅 8K 字（约 18 KB）内存，但具备较为完善的图形显示能力。Thompson 此前已在 Multics 系统上编写了游戏 Space Travel（《星际旅行》），随后将其改写为 Fortran 版本，在 GE 635 计算机的 GECOS 操作系统上运行，但因运行费用高昂且显示效果不佳，Thompson 与 Ritchie 将该游戏移植到了 PDP-7 上。PDP-7 配备了一台大容量单盘片磁盘驱动器，Thompson 编写了磁盘调度算法以最大化磁盘吞吐量。

> **技巧**
>
> 《星际旅行》已被移植，目前可通过网页端体验（[Space Travel](https://akr.am/st/)），移植后的项目源代码位于 [C port of Ken Thompson's Space Travel](https://github.com/mohd-akram/st)。
>
> ~~虽然操作简单，但还是看不懂怎么玩。~~

为验证该算法，需向磁盘写入数据，Thompson 遂编写了一款批量写入数据的程序。

他以每周一个程序的速度编写了三项成果：创建代码的编辑器、将代码转换为 PDP-7 可执行机器语言的汇编器，以及“内核的外层，即操作系统”，最终完成了操作系统的初步构建。

PDP-7 上的新操作系统开发后不久，Thompson 与几位同事进行讨论，当时系统尚未命名，最初称为“UnICS”（**非复用** 信息和计算服务，Uniplexed Information and Computing Service），后改为 UNIX，更便于记忆。

## 参考文献

- Raymond E S. UNIX 编程艺术[M]. 北京：电子工业出版社，2012. ISBN: 978-7-121-17665-4. 系统阐述 UNIX 哲学与软件工程实践原则。
- Gancarz M. Linux/Unix 设计思想[M]. 北京：人民邮电出版社，2012. ISBN: 978-7-115-26692-7. （已绝版）提炼 UNIX 系统设计核心思想与实践方法。
- The Open Group. The Open Group Standards Process[EB/OL]. [2026-03-25]. <https://www.opengroup.org/standardsprocess/certification.html>. 规范 UNIX 认证流程与技术标准框架。
- National Academy of Engineering. Dr. Fernando J. Corbato[EB/OL]. [2026-04-16]. <https://www.nae.edu/29551/Dr-Fernando-J-Corbato>. Corbato 主持开发了 CTSS，据该文记载，CTSS 于 1961 年 11 月首次演示于 IBM 709。
- Ritchie D M. The Development of the C Language[EB/OL]. [2026-04-16]. <https://www.bell-labs.com/usr/dmr/www/chist.html>. Ritchie 回忆 C 语言与早期 UNIX 开发历程，提及 PDP-7 内存为 8K 18-bit words。
- Tom Van Vleck. The Multicians web site[EB/OL]. (2026-04-08)[2026-04-17]. <https://multicians.org/history.html>. 记载 Multics 项目历史，贝尔实验室与通用电气于 1965 年加入。
- Computer History Museum. Chilton Atlas installation[EB/OL]. [2026-04-17]. <https://www.computerhistory.org/timeline/1962/>. 记载 Atlas 计算机于 1962 年首次投入运行，引入虚拟存储器概念。
- Ritchie D M. The Evolution of the Unix Time-sharing System[EB/OL]. (1984)[2026-04-18]. <https://www.read.seas.harvard.edu/~kohler/class/aosref/ritchie84evolution.pdf>. Ritchie 详述 Unix 从 PDP-7 到 PDP-11 的演进历程，记载 Space Travel 最初编写于 Multics，后改写为 Fortran 运行于 GECOS/GE 635，最终移植至 PDP-7。
- Van Vleck T. Multics: Bell Labs withdrawal[EB/OL]. [2026-04-18]. <https://www.multicians.org/general.html>. 记载贝尔实验室于 1969 年 4 月退出 Multics 项目。
- 克尼汉 B W. UNIX 传奇：历史与回忆[M]. 韩磊，译. 北京：人民邮电出版社，2021：31-42. ISBN: 978-7-115-55717-9. 2.3 节记载 Thompson 编写磁盘调度算法以最大化 PDP-7 磁盘吞吐量，并以每周一款程序的速度编写了编辑器、汇编器与内核。

## 课后习题

1. 查找 PDP-7 模拟器与早期 UNIX 源代码存档，构建一个可运行的早期 UNIX 环境，并运行一个 C 语言的“Hello world”程序。
2. 在网页端体验 Thompson 最初的 Space Travel，并总结其玩法。
3. 试列举 SUS 规范与 Windows 操作系统设计与实现的差异。
