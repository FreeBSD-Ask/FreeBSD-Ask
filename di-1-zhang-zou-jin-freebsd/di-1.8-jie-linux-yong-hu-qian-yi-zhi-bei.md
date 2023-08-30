# 第 1.8 节 Linux 用户迁移指北

由于 GNU 开源运动的大规模开展和 Linux 的蓬勃发展，大部分人对于开源的理解被囿于 GPL 与 Linux，无法走进 FreeBSD 这片 BSD 世界，主要表现为某些自诩为 **开源社团** 的组织，其实际上的、具体的活动并没有超越 Linux 的基本边界。为此特撰写本文。

关于二者的对比在前文已经写过了，不再赘述，也毫无意义。再强调 FreeBSD 的优越性也是啰啰嗦嗦的废话而已。与其强调 FreeBSD，不如走进 Linux，真实的 Linux。

以下言论可能某些人可能会感到冒犯，但这就是真实：

## 各大 GNU/LInux 发行版对比

### Ubuntu

Ubuntu 是著名的内部错误发行版。有些人为此争辩“那是 Ubuntu 太谦虚了，他把不属于自己的报错也揽到自己身上”，但无可辩驳的是 Ubuntu 基于 Debian 的 SID 版本，本身稳定性是没有保证的。

### Fedora

Fedora 俗称“地沟油”，是基于 RHEL 的上游系统，我更喜欢称其为小白鼠发行版，其发行的根本目的是为了测试 RHEL 系统的新设计和新架构，待稳定后迁移到 RHEL。稳定性可见一斑。由此可见 Linux 所谓成功的商业模式就是开源社区免费测试，测试稳定了引入企业版。更多地例如 wine 与 crossover？

### CentOS/Rocky Linux/RHEL

目前，CentOS 已经不再是以往的基于 RHEL 源代码构建的操作系统，而是 RHEL 的中游测试系统，和 Fedora 差不多了。其替代品五花八门，甚至还有取得了 UNIX 认证的所谓 **欧拉系统**。但是我认为 Rocky Linux 更加有前景。这些系统在服务器上被广泛部署，具体缺点就是以牺牲软件的“新”来换取“稳”，软件版本非常陈旧。

### Debian

Debian 俗称“大便”。有个很奇怪的事情，设置了 root 密码就不会安装 sudo。Debian 的软件包也不甚更新。（此处仅指 stable）。

### OpenSUSE

完整的 OpenSUSE 安装后系统非常的卡顿，据说是 btrfs 文件系统的某个特性，也许卡就是特性之一吧。OpenSUSE 俗称大蜥蜴。他所做的最搞笑的一件事是他的版本号，为了纪念英国作家道格拉斯·亚当斯在《银河系漫游指南》中写到的这个数字“42”，（被称作 “the answer to life, the universe and everything”，生命、宇宙以及任何事情的终极答案），OpenSUSE 把版本号从 13 蹦到了 42，然后又从 42 回到了 15。然后搞笑的一件事是，从 42 到 15 应该是升级的过程，但是 42 的版本号比 15 大，于是你到了 15 再升级就会再反向升级到 42。 那么现在问题来了，到了 41 再升级是到 42 还是 43 呢？

### Gentoo

Gentoo 俗称“元发行版”。一切软件都要通过 **编译** 的方式来进行安装。其缺点也很明显，如果一个程序编译不过去就无法安装了，实际上这种软件非常多。有人会抬杠说 Gentoo 有二进制安装方式，但那也需要自己先本地构建，并没有统一的官方二进制源，自己制作也不具备通用性。一旦你一段时间不更新，Gentoo 会告诉你什么叫做 **循环依赖**。而且 Gentoo 难以大规模部署，也难以在服务器上部署。另外 Gentoo 的 portage（包管理器）是 python 语言编写的，这直接导致计算依赖的时间的延迟：在树莓派 4 上，安装 KDE 5 往往要计算几个小时……

简而言之，Gentoo 用自己的哲学捆绑了用户，简单问题复杂化，自己折磨自己；USE 过于复杂，对于一些常用软件，都经常出现循环依赖问题，破坏系统稳定性，软件安装升级卸载困难。

### Deepin/UOS/中标麒麟

UOS 和 Deepin 的关系就好比 RHEL 之于 Fedora。本质上是一种东西。Deepin 系统似乎从不进行软件测试，直接就将更新包推送给用户，最直接结果就是他知道更新会导致系统崩溃也不撤回当次更新，而是在官网一个小角落里写个帖子和你讲怎么修复？这是令人迷惑的思路和解决方案。Deepin 这个系统仅仅是复制文件就会导致桌面卡死，无法理解他的系统是怎么做出来的，难道他自己的开发者不需要复制文件吗？UOS 个人桌面版就是让别人参与小白鼠测试，居然还需要注册，无话可说。

对于中标麒麟这类所谓国产系统无话可说。

### Arch Linux/Manjaro

Arch Linux 俗称“**邪教、洗发水**”。这是我所见过的一个最不稳定的 Linux 发行版，也是被别人忽悠从而安装最多的一个。我难以理解为什么有这么多人选择如此不稳定的一个操作系统。你安装的软件越多，挂的越快。有人会说这是你不看软件发行注记的后果，此言差矣。一个需要看发行注记才能更新的系统，本身就是有问题。Arch Linux 唯一优点就是软件新。似乎随处可见的就是 Arch Linux。Arch Linux 似乎是与苦难哲学挂钩的，关于这一点，请参看 [第十九章-第三节](../di-19-zhang-wen-xue-gu-shi/di-19.3-jie-linux-yu-ku-nan-zhe-xue.md)。

Arch Linux 官方源里基本上没有什么软件，不导入 aur 源（ Arch User Repository，Arch 用户软件仓库）就完全没法用。而 aur 源是[未经过任何代码审查的](https://wiki.archlinux.org/title/Arch_User_Repository)（`Warning: AUR packages are user-produced content. These PKGBUILDs are completely unofficial and have not been thoroughly vetted. Any use of the provided files is at your own risk.`，`警告： AUR 中的软件包是由其他用户编写的，这些 PKGBUILD 完全是非官方的，未经彻底审查。使用这些文件的风险由您自行承担。`）实际上不是未经彻底审查，是根本没有任何审查：也就是说有人往里面塞 `rm -rf /*` 也是可以的。虽然他使用了 fakeroot 但是也无济于事。

## FreeBSD 与 Linux 不同之处

- FreeBSD 仍然使用传统的 INIT 引导，而非 systemd；
- FreeBSD root 用户 shell 默认是 csh（14 改为 sh），而不是 bash；
- FreeBSD 基本系统几乎不包含任何非 BSD 协议的软件，并致力于去 GNU 化（这意味着基本系统不使用 Glibc、GCC 等软件），见

https://wiki.freebsd.org/GPLinBase

- FreeBSD 的用户配置文件和系统配置文件严格分离，即内核和基本系统与第三方应用程序是完全分离的；
- FreeBSD 项目是作为一个完整的操作系统维护的，而非内核与 userland 单独维护；也就是说如果你要使用 FreeBSD，那么就只有一个 FreeBSD 可选；
- FreeBSD 没有 free 命令也不支持安装这个包(FreeBSD 早就不使用 procfs 了)，FreeBSD 基本系统自带的文本编辑器有 ee 和 vi（不是软链接到 vim 的 vi，是真实的 vi），没有预装 wget，而是 fetch。

## 命令替代/软件替代

因为 Linux 广泛使用的也是 GNU 工具，因此只要理论上不是依赖于特定的 Linux 函数库，该工具都可以在 FreeBSD 上运行。

| Linux 命令/GNU 软件 | FreeBSD 命令/BSD 软件 | 需要安装的包（安装方式） |      作用说明      |                                                                                    额外说明/苦难哲学                                                                                     |
| :-----------------: | :-------------------: | :----------------------: | :----------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|        lsusb        |         lsusb         |   pkg install usbutils   |   显示 USB 信息    |                                                                            粗略地可以用 `cat /var/run/dmesg`                                                                             |
|        lspci        |         lspci         |   pkg install pciutils   |    显示主板信息    |                                                                            粗略地可以用 `cat /var/run/dmesg`                                                                             |
|        lsblk        |         lsblk         |    pkg install lsblk     |  显示磁盘使用情况  |                                                                                            /                                                                                             |
|        free         |       freecolor       |  pkg install freecolor   |  显示内存使用情况  | FreeBSD 没有提供`free`命令，因为其依赖 Linux，由包`procps`提供，但是呢，FreeBSD 早就不使用`procfs`了。如实在需要`free`可以用 `https://github.com/j-keck/free` 其他可选命令是 `vmstat -m` |
|        lscpu        |         lscpu         |    pkg install lscpu     |   显示处理器信息   |                                                                                            /                                                                                             |
|        glibc        |        bsdlibc        |            /             |        C 库        |                                                                                            /                                                                                             |
|         GCC         |     LLVM + Clang      |            /             | 编译器、编译链工具 |                                                                              非要用也可以`pkg install gcc`                                                                               |
|         vim         |          vim          |     pkg install vim      |     文本编辑器     |                                                                  FreeBSD 默认的`vi`并不被软连接到`vim`，而是真正的`vi`                                                                   |
|        wget         |         wget          |     pkg install wget     |       下载器       |                                                                               系统默认的下载工具是`fetch`                                                                                |
|        bash         |         bash          |     pkg install bash     |       shell        |                                              系统默认的`root shell`是`csh`,修改会导致配置输入法环境变量时遇到困难以及可能会无法进入恢复模式                                              |
|   NetworkManager    |      networkmgr       |  pkg install networkmgr  |    网络连接工具    |                                                                        NetworkManager 依赖 `systemd` 无法直接移植                                                                        |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
