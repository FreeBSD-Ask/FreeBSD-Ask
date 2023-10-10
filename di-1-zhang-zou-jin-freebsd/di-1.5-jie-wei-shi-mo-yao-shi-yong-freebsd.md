# 第 1.5 节 为什么要使用 FreeBSD

## 选择 FreeBSD 的一般原因

- **从道家来讲，你爱用不用，不用拉倒。太长不看，不用？对其他的原因有意见？请重复看此条目——左转 ArchLinux 吧，不谢。**
- 从佛学来说，因为缘分。万物缘起性空，我们有缘相聚，又会者定离。万般诸相皆如此。
- 从基督教来讲，这是主的指引。就像出埃及记一样，你看上去是自己的选择，实际上都是主的安排。
- 从黑格尔来讲，是因为辩证否定。FreeBSD 是 UNIX 直接后裔，而 Linux 只是仿制品，而很多协议又离不开 UNIX，所以你注定了要来到这里。
- 按照我个人观点而言，追求软件的稳定和新，既要有二进制源，又要能编译安装。除了 FreeBSD 之外我找不到 Linux 系统。（VoidLinux 缺乏类似 USE 的控制系统）
- BSD 三则授权协议：并允许自由分发。GPL 与 BSD 协议，究竟何者是真正的自由？GPL 最多只是通过限制自由来确保他所谓的自由罢了。学习 BSD 就和学习哲学一样，本身并不是为了某种确切的知识而去学习，而是为了自由而去学习（因为在大多数人眼中 BSD 已然不具有所谓的实用价值了）。那么在这一点上，可以说，按照他们的想法，BSD 与其他操作系统有根本上的不同——即 BSD 是真正的自由。
- FreeBSD 是学院派的开源实践产物，也是 UNIX 哲学的忠实践行者。
- 远离碎片化的 Linux 发行版，使得选择困难症用户免受痛苦。
- BSD 是一个完整的 OS，而不是内核。内核和基本系统作为一个项目来整体维护。——请注意，这是所有 Linux 系统的缺陷所在。没有事实上的基本系统的概念和区分会造成一系列违反直觉的事情。
- Linux 社区已经成为一个肮脏的泥潭，无论是内核开发还是用户群组。——见文学故事。

## 选择 FreeBSD 的技术性原因

- 基本系统的配置文件与第三方软件配置文件相分离。你不会遇到像在 RHEL 中使用 rpm 命令卸载 glibc 导致系统毁灭这种奇葩的事情（无独有偶，有时候 yum 的错误操作会卸载包括使用中的所有内核），FreeBSD 的包管理器不干涉基本系统。
- 不会锁死软件版本，比如 Python GCC 等 Linux 中系统依赖的软件。所有软件都会滚动更新。这些非滚动版本的 linux 的软件版本基本上在该版本上锁死的，不会得到任何功能版本更新。滚动版本的又有一堆稳定性问题。BSD 所有版本共用一个 ports，只有极小一部分软件和系统版本硬捆绑，其他都是可以滚动更新的。而且由于基本系统的存在，第三方的软件几乎不影响系统的稳定性。Linux 则无法在软件更新和系统稳定之间找到平衡点。
- 文档齐全，所有涉及一般性的问题 Handbook 手册都有记述。ArchLinux 的 Wiki 虽然有很多，但大都年久失修且不成体系。
- 安全漏洞相比于 Linux 较少。
- 可以避免在产品/架构中出现共同故障点。
- 接近 2.5 年的版本发布周期，5 年的维护周期赋予了 FreeBSD 稳定性。
- 通过 BSD 的 Ports 可以编译安装软件，进行自由配置。
- ZFS 文件系统可以被配置为 `\` 分区。ZFS 被誉为最强大的文件系统。
- Jail 与 byhve 虚拟化，不必配置底层虚拟化，节约系统资源。
- 传统的 BSD INIT 引导，使你免受 systemd 迫害。
- DTrace 框架与 GEOM 存储框架。
- Linux 二进制兼容层，可运行 Linux 软件，只要其支持 CentOS 或 Ubuntu/Debian。且软件运行速度快于 Linux。
- 安全事件审计。
- 不同于 Linux 驱动捆绑内核的做法， FreeBSD 的驱动在大致上与内核解耦合。
- Linux 内核开发是一个相当封闭的过程，只有少数人能够参与直接提交代码，而 FreeBSD 则秉持着人人可参与的思路。

## 选择 FreeBSD 的社会意义

> 显而易见：目前 FreeBSD 上的桌面部件的缺失很大程度上是因为他们过分依赖了 Linux 特有函数库，比如包含 `ip`命令的`iproute2`软件包。更多的原因则是因为这些桌面或部件和 systemd 做了深度捆绑或者根本就是强制依赖，比如`NetworkManager` 。而 Samba 开发者则会说“We use Linux, we develop for Linux, all others please submit patches”。FreeBSD 社区的人把这种行为叫做“Linuxism”（Linux 主义/Linux 歧视），你会在文学故事章节里引用的链接中再次见到这个词，且某些人以此为豪。
>
> 这种行为会导致何种后果我们不得而知，但是这种程序愈来愈多了，而且有成为主流的趋势，甚至就连大部分开发者在开发程序时也不再考虑兼容 init，比如 `todesk`。甚至 Java 程序都丧失掉了他的可移植性，为什么 FreeBSD 上的 Eclipse 将近两年没有更新？就是因为这类[捆绑问题](https://git.eclipse.org/r/c/platform/eclipse.platform.swt/+/163641/)。最近甚至还有了 `systemd-boot` 来取代 `grub2`，在可预见的未来，Linux 将被 systemd 统一。而其程序（预计所有可运行在 Linux 上的程序）也不再具有任何的可移植性。
>
> 或许 Linux 的开源到了尽头。“你可以继续造你的轮子，但是你不兼容我的 systemd 你就运行不了任何程序。”现在 FreeBSD 所面临的这种困境，将是所有人要面对的。虽然 UNIX 已经变得毫无意义，但是 Linux 已经完完全全背弃了他所出发的哲学与思想这件事是确凿无疑的。

- 选择 FreeBSD，就是选择在 Linux 被 systemd 及其背后的商业公司控制以后，还能够保留一份火种。纵观各大操作系统，有能力替代的，开源的操作系统只有 FreeBSD。
- 选择 FreeBSD，就是选择保留下一份真正开源的、自由的操作系统。能够使开源事业继续坚持下去，并践行真正的 UNIX 哲学，不走改旗易帜的邪路，封闭之路。

## 进一步了解

- [systemd 背后的真正动机](https://freebsd.gitbook.io/translated-articles/the-real-motivation-behind-systemd)
- [systemd 在任何地方都不安全](https://freebsd.gitbook.io/translated-articles/systemd-isnt-safe-to-run-anywhere)
- [GPL 之殇](https://freebsd.gitbook.io/translated-articles/the-problems-with-the-gpl)
- [为什么你应该将所有东西从 Linux 迁移到 BSD](https://freebsd.gitbook.io/translated-articles/why-you-should-migrate-everything-from-linux-to-bsd)

