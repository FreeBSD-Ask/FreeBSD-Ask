# 1.3 Linux 与类 UNIX

本节以 Linux 内核官方文档的定义为起点，阐述 Linux 作为 UNIX 克隆操作系统的技术架构与许可证体系，并说明其“类 UNIX”属性的法律与功能依据。

## 何谓 Linux？

Linux 是当今世界广泛使用的开源操作系统。Linux 在不同语境下含义不同：狭义上指 Linux 内核，广义上通常指完整的操作系统，即 GNU/Linux。参见 Linux Kernel Organization. What is Linux?[EB/OL]. [2026-04-04]. <https://www.kernel.org/doc/html/latest/admin-guide/README.html>，该组织对这一问题的回答如下：

> What is Linux?（什么是 Linux？）
>
> Linux is a clone of the operating system Unix, written from scratch by Linus Torvalds with assistance from a loosely-knit team of hackers across the Net. It aims towards POSIX and Single UNIX Specification compliance.（Linux 是 UNIX 操作系统的克隆版本，由 Linus Torvalds 从零开始编写，并在网络上一支组织松散的极客团队协助下完成。Linux 旨在实现对 POSIX 和单一 UNIX 规范的兼容）
>
> It has all the features you would expect in a modern fully-fledged Unix, including true multitasking, virtual memory, shared libraries, demand loading, shared copy-on-write executables, proper memory management, and multistack networking including IPv4 and IPv6.（Linux 拥有现代化、功能完备的 UNIX 系统所应具备的全部特性：真正的多任务处理、虚拟存储器、共享库、按需加载、共享写时复制可执行文件、完善的内存管理，并且内置 IPv4 和 IPv6 多栈网络支持）
>
> It is distributed under the GNU General Public License v2 - see the accompanying COPYING file for more details.（Linux 在 GNU 通用公共许可证 v2 下进行分发——更多有关细节，请参阅随附的版权文件）

通过以下框架图可更为清晰地展示 Linux 系统的层次结构：

```text
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

**核心系统工具层**包含 GNU 基础工具（如 bash、gcc、glibc 等）、包管理器和初始化系统等组件。**GNU 基础工具**是 GNU 项目开发的命令行工具和系统库，为操作系统提供基本功能。

Linux 的开发受 Minix 启发，后者是一款专用于教学的微内核操作系统，产生于 UNIX 版权受限的背景之下。当时 21 岁的 Linus Torvalds 就读于芬兰赫尔辛基大学计算机科学系。彼时芬兰高等教育体系尚未区分本科与硕士阶段，学生入学后直接攻读硕士学位，但 1991 年 Torvalds 仍处于学业的早期阶段。关于芬兰学制的发展，参见：杨天平，金如意.博洛尼亚进程述论[J].华东师范大学学报(教育科学版),2009,27(01):9-22.DOI:10.16382/j.cnki.1000-5560.2009.01.007.

GNU 与 Linux 的成功离不开 Minix 引发的社区讨论。1991 年，Andrew Stuart "Andy" Tanenbaum（Minix 作者） 就内核架构与 Linus 展开激烈辩论，最终 Linus 认为微内核不实用。为此，他放弃教育用途限制，转向 GPL 许可证，并吸收 GNU 组件，逐步完善 Linux 的生态体系。这场论战促使 Linux 转向宏内核，为后续发展奠定基础。

Linus Torvalds 的硕士毕业论文是 [《Linux: A Portable Operating System》](https://www.cs.helsinki.fi/u/kutvonen/index_files/linus.pdf)（Linux：一款可移植的操作系统），他在 1997 年（27 岁）获得理学硕士学位。其能长期保留学籍，在于芬兰实行典型的学分制。根据芬兰赫尔辛基大学官网的说明，该校并无最长学习期限限制，仅规定课程成绩的有效期为十年。官网明确指出：“课程到期不会影响在大学继续学习的权利。”（University of Helsinki. Expiry of Studies[EB/OL]. (2026-02-16)[2026-04-04]. <https://studies.helsinki.fi/instructions/article/expiry-studies>.）

> 我们探讨了在将 Linux 操作系统移植到多种 CPU 和总线架构时所暴露出的硬件可移植性问题。我们还讨论了软件接口的可移植性问题，尤其是与能够共享同一硬件平台的其他操作系统之间的二进制兼容性问题。文中描述了 Linux 所采取的方法，并对其中几个架构进行了更为详细的介绍。
>
> Torvalds L. Linux: a Portable Operating System[D/OL]. Helsinki: University of Helsinki, 1997 [2026-04-04]. <https://www.cs.helsinki.fi/u/kutvonen/index_files/linus.pdf>. 论文摘要中文译文。

> **技巧**
>
> 几乎每颗英特尔处理器上的管理引擎（Intel Management Engine）都运行着基于 Minix 的微内核。自 ME 11（随 Skylake 处理器引入）起，Intel Management Engine 基于 Intel Quark x86 微控制器并运行 MINIX 3 操作系统。
>
> ~~或许基于 Minix 的微内核才是世界上最广泛部署的操作系统内核。~~

UNIX 标准 SUS 包含 POSIX 标准，前者是后者的超集。Single UNIX Specification 的基础卷是现有 POSIX.1 和 POSIX.2 规范的超集。Linux 实现了 POSIX 标准，但未获得 POSIX 认证：IEEE, The Open Group. POSIX Certification Policy[EB/OL]. (2012-12-05)[2026-04-04]. <http://get.posixcertified.ieee.org/docs/POSIX_Certification_Policy_v1.1.pdf>.

### 参考文献

- The Open Group. The Base Specifications Issue 6, Preface[EB/OL]. [2026-04-23]. <https://pubs.opengroup.org/onlinepubs/009604299/frontmatter/preface.html>. 指出“These were selected since they were a superset of the existing POSIX.1 and POSIX.2 specifications and had some organizational aspects that would benefit the audience for the new revision.”
- Portnoy E, Eckersley P. Intel's Management Engine is a security hazard[EB/OL]. (2017-05-08)[2026-04-23]. <https://www.eff.org/deeplinks/2017/05/intels-management-engine-security-hazard-and-users-need-way-disable-it>.
- HandWiki. Intel Management Engine[EB/OL]. [2026-04-23]. <https://handwiki.org/wiki/Intel_Management_Engine>.
- jmcph4. Intel Management Engine[EB/OL]. [2026-04-23]. <https://jmcph4.dev/wiki/ime.html>.

## 狭义 Linux：操作系统内核

Linux 在不同语境下含义不同。从狭义上讲，Linux 指的是 Linux 内核。[Linux kernel](https://www.kernel.org/) 项目始于 1991 年。

## 广义 Linux：GNU/Linux 操作系统

从广义上讲，Linux 通常指完整的操作系统。GNU/Linux = Linux 内核 + GNU 等软件 + 包管理器。

**[Chimera Linux](https://chimera-linux.org/) 除外。**

Linux 的全称为 GNU/Linux。

从 GNU 这一递归缩写（GNU's Not Unix，意为“GNU 不是 UNIX”）可以看出，Linux 与 UNIX 并无直接的源流关系。

具体而言：

- GNU/Linux 发行版 = Ubuntu、RHEL、Deepin、openSUSE……
  - Ubuntu = Linux kernel + apt/dpkg + GNOME（默认桌面环境）
  - openSUSE = Linux kernel + libzypp/rpm（包管理器后端，支持 RPM 格式）+ KDE（默认桌面环境之一）

> **思考题**
>
> 1. 如果去掉文件系统、Linux 内核、Shell、systemd（init）、桌面环境、包管理器以及所有第三方软件，一个 Linux 发行版还剩下哪些内容？
> 2. 在上述组件全部移除，并将其重新组合后，若仍将该系统称为“发行版”，它与传统 Linux 发行版相比存在哪些本质区别？
> 3. 在这种情况下，该系统是否仍然可以被视为原来的发行版？请说明理由。
> 4. 如果不能被视为原来的发行版，是在移除哪一类关键组件之后，其不再具备“发行版”的属性？
> 5. 如果仍然可以被视为原来的发行版，那么哪些部分可以被认为真正继承自原有发行版，依据是什么？

> **注意**
>
> 若存疑虑，建议亲自安装 [Gentoo](https://www.gentoo.org/downloads/)（stage3）或 [Slackware](http://www.slackware.com/)，若仍存疑虑可亲自体验 [Gentoo (stage1)](https://wiki.gentoo.org/wiki/Stage_file) 或 [LFS](https://www.linuxfromscratch.org/lfs/)。
>
> 上述操作较为复杂，需要一定的经验与基础知识。~~又陷入了前理解循环。~~

## UNIX-like 系统的概念界定

除获得正式 UNIX 认证的系统外，还有许多采用类似 UNIX 设计理念的操作系统。

UNIX-like 即类 UNIX，指基本符合 UNIX 标准，或基本遵守 POSIX 规范但未获得相应认证、商标使用权的操作系统。

该术语用于描述设计理念和技术实现上与 UNIX 高度相似但缺乏正式认证的系统。

当前主流操作系统中，除 Windows 外，绝大多数操作系统均可称为 UNIX-like，包括 Linux 和 FreeBSD。

## 课后习题

1. 在现代 FreeBSD 环境中配置交叉编译工具链，构建并在 QEMU 中运行 4.4BSD-Lite2，记录交叉编译过程中遇到的工具链兼容性问题。
2. 查阅 SUS 与 POSIX 标准的正式文档，从系统调用接口、C 标准库函数和编译程序约定三个维度列举两者的异同。
3. 梳理 OpenRC 与 FreeBSD 原生 rc.d 框架在服务依赖解析机制上的差异。
