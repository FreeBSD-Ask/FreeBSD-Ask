# 1.4 什么是 FreeBSD

>一群 PC 黑客坐下来，试图为 PC（个人电脑）编写一套 Unix 系统，其产物便是 Linux。
>
>一群 Unix 黑客坐下来，试图将 Unix 系统移植到 PC（个人电脑）上，其产物便是 BSD。
>
>——佚名

此处的黑客（hacker）指热心并精通于计算机编程和设计等方面的人员，而非利用系统安全漏洞对网络进行攻击破坏或窃取资料的人。

## 如何拼读 FreeBSD

FreeBSD 的正确读法是新用户普遍关注的问题。目前社区共识和普遍的读法是：/ˌfriːˌbiːɛsˈdiː/，即读作“Free（/friː/）+ B（/biː/）+ S（/ɛs/）+ D（/diː/）”，类似“福瑞/必/哎司/地”。

即先读 Free，再逐字母拼读 B、S、D。

通常不会将 BSD 或 FreeBSD 视为一个词语连读。不会读作“百思得”或“福瑞百思德”。~~FreeBSD 基金会在中国大陆注册商标的机构中文译名为“福瑞百思德基金会”。~~

## 什么是 FreeBSD？

FreeBSD 不是 Linux，也不是 UNIX 的克隆。FreeBSD 是一种自由软件，源代码公开且可自由使用、修改和分发。

![什么是 FreeBSD？](../.gitbook/assets/freebsd-not-linux.png)

FreeBSD 一词由两部分构成，即"Free"和"BSD"。

```sh
FreeBSD 名称构成

FreeBSD = Free + BSD
           │      │
           │      └── Berkeley Software Distribution
           │           （伯克利软件发行版）
           │           源自加州大学伯克利分校 CSRG
           │
           └── 双重含义：
                · 自由（Liberty）—— BSD 许可证，自由使用/修改/分发
                · 免费（Gratis） —— 无需付费即可获取
```

BSD 最初由加州大学伯克利分校（University of California, Berkeley）的计算机系统研究小组（CSRG）开发，这一工作被命名为 `Berkeley Software Distribution`（伯克利软件发行版）。FreeBSD 等 BSD 系统都是计算机系统研究小组（CSRG）工作的延续。

Free 包含自由（Liberty）和免费（Gratis）两种含义。

FreeBSD 日为 6 月 19 日。FreeBSD 基金会和社区在这天庆祝 FreeBSD 的生日。

## UNIX 之船：FreeBSD 是不是 UNIX？

该问题远非表面所见那般清晰明确。诸多讨论者，甚至是那段岁月的亲历者，也难以给出明确回答或澄清。有观点认为，BSD 并未进行过任何 UNIX 认证，没有持有法律上的商标便简单定论；更有甚者只是笼统地说 FreeBSD 是 UNIX 的延续者与正统继承者，仅是“有实无名”；另有观点认为，BSD 之于 UNIX，正如 Linux 之于 UNIX。

上述回答存在分歧，原因在于该问题并非可简单套用法律商标归属或代码继承性来分析的纯粹技术性难题。其牵涉到深刻的本体论哲学问题：究竟是不能两次踏进同一条河流，还是一次也不能踏进同一条河流？如何回答此问题，反映着回答者的哲学观与科学技术观。

>> **忒修斯之船**
>>
>>忒修斯和雅典青年安全返航所乘的是有三十支桨的大帆船，雅典人把这只船一直保存到德米特里·法勒琉斯的时代。他们一次又一次地拆掉了朽烂的旧船板，换上坚实的新船板。从此以后，这只船就成为哲学家们就事物的发展问题展开争论时经常援引的实例，一派认为它还是原来那只船，另一派争辩说它已不再是原来的船了。
>>
> - Plutarch. 希腊罗马名人传[M]. 黄宏煦，陆永庭，吴彭鹏，译. 北京：商务印书馆，1990：23.
>
> **思考题**
>
> 1. 如果这艘船替换了若干组件，这艘船是不是忒修斯之船？
>
> 2. 如果有一天，这艘船原有的所有组件都被完全替换了一遍，这艘船还是不是忒修斯之船？
>
> 3. 如果将所有替换下来的组件拼凑起来，组成一艘新船，这艘船是不是忒修斯之船？

BSD 操作系统并非复刻品，而是 AT&T Research Unix 操作系统的开源衍生版本，与现代 UNIX® System V 同为 UNIX 的两大主要分支。在 4.4BSD 以前，BSD 全称为 BSD UNIX。

![UNIX 之船：FreeBSD 是不是 UNIX？](../.gitbook/assets/bsd-unix-history.png)

最初，UNIX 是 AT&T 开发的操作系统。20 世纪 80 年代初，加州大学伯克利分校的计算机系统研究小组（CSRG）正式成立，开始深入研究 UNIX，并为其开发了大量用户空间的程序，形成了新系统 BSD（Berkeley Software Distribution, 伯克利软件发行版）。随着时间推移，BSD 系统逐渐发展，加入了许多创新，例如实现了 TCP/IP 协议栈。至 20 世纪 90 年代初，CSRG 开始重新实现 AT&T 专有代码，于 1991 年发布了 Networking Release 2（Net/2）。然而，Net/2 中仍残留少量 AT&T 代码，成为日后 USL 诉讼的导火索。1992 年，William Jolitz 与 Lynne Jolitz 夫妇将 Net/2 移植到 Intel i386 平台，形成 386BSD。1993 年，FreeBSD 和 NetBSD 相继从 386BSD 分支诞生。1994 年 USL 诉讼和解后发布的 4.4BSD-Lite 彻底移除了所有 AT&T 代码，FreeBSD 2.0（1994 年 11 月）与 NetBSD 后续版本相继整合 4.4BSD-Lite 代码。此后，BSD 系统进一步分裂：1995 年 OpenBSD 从 NetBSD 中复刻出来，2003 年 DragonFly BSD 从 FreeBSD 中复刻出来。

上述 BSD 系统的源流与分裂关系可归纳如下：

```sh
BSD 系统家族树

AT&T UNIX
  │
  └─ BSD（CSRG，加州大学伯克利分校）
       │
    4.3BSD-Reno → Net/2（1991，近乎完整的自由 BSD）
       │
       └─ 386BSD（1992，Jolitz 夫妇移植到 i386）
            │
       ┌────┴────┐
       │         │
    FreeBSD   NetBSD        两者均于 1993 年从 386BSD 分支
    (1993)    (1993)
       │         │
       │      OpenBSD       1995 年从 NetBSD 复刻
       │       (1995)
       │
       └─ DragonFly BSD     2003 年从 FreeBSD 复刻
          (2003)

  注：1994 年 USL 诉讼和解后发布 4.4BSD-Lite（移除全部
      AT&T 代码），FreeBSD 2.0（1994 年 11 月）与 NetBSD
      后续版本相继整合 4.4BSD-Lite 代码。
```

如果查阅 FreeBSD 的源代码，还会看到早期开发者在 1982 年留下的注释和版权声明：

```C
/*-
 * SPDX-License-Identifier: BSD-3-Clause
 *
 * Copyright (c) 1982, 1986, 1993
 *	The Regents of the University of California.  All rights reserved.

 ……以下省略许可证原文……

 */
```

上面这段版权声明出自源代码文件 **sys/sys/_timespec.h**。

> **思考题**
>
> 如何理解 FreeBSD 与 UNIX 的关系？

## 参考文献

- M.D.Fuller, BSD For Linux Users[EB/OL]. [2026-06-01]. <https://www.over-yonder.net/~fullermd/rants/bsd4linux/01>. 文章转述了“Linux is what you get when a bunch of PC hackers sit down and try to write a Unix system for the PC. BSD is what you get when a bunch of Unix hackers sit down to try to port a Unix system to the PC.” 这一名言。
- FreeBSD Foundation. Join us to celebrate FreeBSD Day![EB/OL]. [2026-03-26]. <https://freebsdfoundation.org/freebsd-day/>.
- Identity Over Time[EB/OL]. [2026-03-26]. <https://plato.stanford.edu/entries/identity-time>. SEP 条目：跨时间的同一性。
- Sorites Paradox[EB/OL]. [2026-03-26]. <https://plato.stanford.edu/entries/sorites-paradox/>. SEP 条目：沙堆问题、秃头问题。

## 课后习题

1. 观看纪录片《操作系统革命》（Moore J T S, 导演. 操作系统革命[V]. 美国: Seventh Art Releasing, 2002.），结合影片内容与本章所述 UNIX/BSD 历史，分析开源运动对传统软件商业模式的冲击。
