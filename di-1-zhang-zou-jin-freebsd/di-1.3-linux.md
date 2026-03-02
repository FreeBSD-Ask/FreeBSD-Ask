# 1.3 Linux 与类 UNIX

## 何为 Linux？


我们首先来看一下 Linux 内核项目（[What is Linux?](https://www.kernel.org/doc/html/latest/admin-guide/README.html)）是如何回答这一问题的：

>What is Linux?（什么是 Linux？）
>
>Linux is a clone of the operating system Unix, written from scratch by Linus Torvalds with assistance from a loosely-knit team of hackers across the Net. It aims towards POSIX and Single UNIX Specification compliance.（Linux 是 Unix 操作系统的克隆版本，由 Linus Torvalds 从零开始编写，并在网络上一支组织松散的极客团队协助下完成。Linux 旨在实现对 POSIX 和单一 UNIX 规范的兼容。）
>
>It has all the features you would expect in a modern fully-fledged Unix, including true multitasking, virtual memory, shared libraries, demand loading, shared copy-on-write executables, proper memory management, and multistack networking including IPv4 and IPv6.（Linux 具备你在现代、功能完备的 Unix 中所期望的一切特性，如真正的多任务处理、虚拟内存、共享库、按需加载、共享写时复制可执行文件、完善的内存管理，以及包括对 IPv4 和 IPv6 在内的多协议栈网络支持。）
>
>It is distributed under the GNU General Public License v2 - see the accompanying COPYING file for more details.（Linux 在 GNU 通用公共许可证 v2 下进行分发 —— 有关更多细节，请参阅随附的 COPYING 文件。）

再看看这个框架图：

```
+-----------------------------------------+
|               应用程序层                |
|  (浏览器/办公软件/开发工具/数据库等)      |
+-----------------------------------------+
|             图形界面（可选）             |
|       (GNOME █ KDE █ XFCE 等)           |
+-----------------------------------------+
|           核心系统工具层                 |
|  █ GNU 基础工具 (bash/gcc/glibc 等)      |
|  █ 包管理器 (apt/yum/pacman 等)          |
|  █ 初始化系统 (systemd/OpenRC 等)        |
+-------------------+---------------------+
|                   |   狭义的 Linux       |
|    Linux 内核层   +---------------------+
|                   | (直接控制硬件的中枢)  |
+-------------------+---------------------+
|                   硬件层                 |
|    (CPU █ 内存 █ 硬盘 █ 网卡 █ 外设)      |
+-----------------------------------------+
```

Linux 是一款开源软件。

Linux 之名来自 Linux 之父 Linus Torvalds。

Linux 受启发于 Minix（UNIX 版权限制下的产物），一款设计用于教学的微内核操作系统。当时 22 岁的 Linus Torvalds 是芬兰赫尔辛基大学计算机科学系的研究生。

Linus Torvalds 的硕士毕业论文是 [《Linux: A Portable Operating System》](https://www.cs.helsinki.fi/u/kutvonen/index_files/linus.pdf) [备份](https://web.archive.org/web/20251114200921/https://www.cs.helsinki.fi/u/kutvonen/index_files/linus.pdf)（Linux：一款可移植的操作系统），他在 1997 年（28 岁）获得理学硕士学位。为什么花了这么长时间都没被学校清退呢？芬兰是典型的学分制国家。根据芬兰赫尔辛基大学官网说明，并无 [最长学习期限](https://studies.helsinki.fi/instructions/article/expiry-studies?) [备份](https://web.archive.org/web/20260114070831/https://studies.helsinki.fi/instructions/article/expiry-studies) 限制，仅规定某课程成绩有效时间为十年。“你的课程到期不会影响你在大学继续学习的权利”。

>我们探讨了在将 Linux 操作系统移植到多种 CPU 和总线架构时所暴露出的硬件可移植性问题。我们还讨论了软件接口的可移植性问题，尤其是与能够共享同一硬件平台的其他操作系统之间的二进制兼容性问题。文中描述了 Linux 所采取的方法，并对其中几个架构进行了更为详细的介绍。
>
>《Linux：一款可移植的操作系统》论文摘要

>**技巧**
>
>现在，几乎每颗英特尔处理器上都运行着 Minix。
>
>~~或许 Minix 才是世界上最流行的操作系统~~

UNIX 标准 SUS 包含 POSIX 标准，是其超集。Linux 实现了 POSIX 标准，但未获得 [POSIX 认证](http://get.posixcertified.ieee.org/) [备份](https://web.archive.org/web/20260114153011/https://posix.opengroup.org/)。

从本质上说，Linux 是 UNIX 的一种仿制或克隆产物（类似于人与机器人的关系）。


## 狭义 Linux 是内核

[Linux kernel](https://www.kernel.org/) [备份](https://web.archive.org/web/20260114152922/https://www.kernel.org/) 项目 1991；

## 广义 Linux 是 GNU/Linux

GNU/Linux = Linux kernel + GNU 等软件 + 包管理器

>**[Chimera Linux](https://chimera-linux.org/) [备份](https://web.archive.org/web/20260114152849/https://chimera-linux.org/)  除外。**

Linux 全称为 GNU/Linux；

GNU's Not Unix，从 GNU 这个名字（GNU 不是 UNIX）你也能看出来 Linux 与 UNIX 并无直接关联。

具体地：

- GNU/Linux 发行版 = Ubuntu、RHEL、Deepin、openSUSE……
  - Ubuntu = Linux kernel + apt/dpkg + Gnome（默认桌面环境）
  - openSUSE = Linux kernel + libzypp/rpm（包管理器后端，支持 RPM 格式）+ KDE（默认的桌面环境之一）

> **思考题**
>
> 1. 如果去掉文件系统、Linux 内核、Shell、systemd（init）、桌面环境、包管理器以及所有第三方软件，一个 Linux 发行版还剩下哪些内容？
> 2. 在上述组件全部移除，并将其重新组合后，若仍将该系统称为“发行版”，它与传统 Linux 发行版相比存在哪些本质区别？
> 3. 在这种情况下，该系统是否仍然可以被视为原来的发行版？请说明理由。
> 4. 如果不能被视为原来的发行版，是在移除哪一类关键组件之后，其不再具备“发行版”的属性？
> 5. 如果仍然可以被视为原来的发行版，那么其哪些部分可以被认为真正继承自原有发行版，其依据是什么？


> **注意**
>
> 如果读者还是有所疑惑，建议亲自安装试试 [Gentoo](https://www.gentoo.org/downloads/) [备份](https://web.archive.org/web/20260115021338/https://www.gentoo.org/downloads/) （stage3）或 [Slackware](http://www.slackware.com/) ，再不明白可以试试 [Gentoo（stage1）](https://wiki.gentoo.org/wiki/Stage_file) [备份](https://web.archive.org/web/20260115132845/https://wiki.gentoo.org/wiki/Stage_file)  或 [LFS](https://www.linuxfromscratch.org/lfs/) [备份](https://web.archive.org/web/20260115021242/https://www.linuxfromscratch.org/lfs/) 。
>
> 上述操作较为复杂，需要一定的经验与基础知识。~~又陷入了前理解循环~~

## 什么是 Unix-like？

Unix-like 即类 Unix，指一切符合 UNIX 标准、基本遵守 POSIX 规范但未获得第一节中所述 UNIX 认证的操作系统。

也就是说，除 Windows 外，世界上绝大多数操作系统都可称为 Unix-like，包括 Linux 和 FreeBSD。

