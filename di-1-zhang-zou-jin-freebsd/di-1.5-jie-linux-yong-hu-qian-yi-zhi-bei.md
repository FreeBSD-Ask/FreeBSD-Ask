# 第 1.5 节 Linux 用户迁移指北

由于 GNU 开源运动的大规模开展和 Linux 的蓬勃发展，大部分人对于开源的理解被囿于 GPL 与 Linux，无法走进 FreeBSD 这片 BSD 世界。某些自诩为 **开源** 社团的组织，其实际活动主要集中于 Linux，鲜有超越这一范畴的探索。为此特撰写本文。

与其强调 FreeBSD，不如走进 Linux，真实的 Linux。

以下分析可能会触及一些人的灵魂，但这都是基于实际使用经验的真实反馈。

## 各大 GNU/LInux 发行版对比

### Ubuntu

[Ubuntu 是著名的内部错误（internal error）发行版](https://www.google.com/search?q=internal+error+ubuntu+site:askubuntu.com)。有些人为此争辩“那是 Ubuntu 太谦虚了，[他把不属于自己的报错也揽到自己身上](https://linux.cn/article-4660-1.html)”，但无可辩驳的是 Ubuntu 基于 Debian 的 SID 版本，本身稳定性是没有保证的（无论普通版本还是 LTS）：一是内部错误，二是无法跨大、小版本升级（必挂，即使纯净系统也大概率会挂）。最近在 VMware Workstation 17 Pro 虚拟机上测试了 Ubuntu 24.04 LTS，可以说一代不如一代，安装的时候就开始不断地报错，并且 Bug 不断，窗口溢出、找不到鼠标光标、定位不到输入框……费劲安装后，开机更是各种内部错误接连不断（掐表数过了大概每 10 分钟会有 1 次）。

```bash
ykla@ykla-ubuntu:~$ cat /etc/debian_version 
trixie/sid #trixie 即 Debian 13。但是在当前时间点，最新 stable 版本是 Debian 12 bookworm 
ykla@ykla-ubuntu:~$ cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=24.04
DISTRIB_CODENAME=noble
DISTRIB_DESCRIPTION="Ubuntu 24.04 LTS"
```

### Fedora

Fedora 俗称“[地沟油](https://zh.moegirl.org.cn/zh-hans/Fedora%E5%A8%98)”，是基于 RHEL 的上游系统，我愿称其为小白鼠发行版，其发行的根本目的是为了测试 RHEL 系统的新设计和新架构（[该社区由 RedHat 红帽公司完全控制](https://docs.fedoraproject.org/en-US/council/)），待稳定后迁移到 RHEL。

稳定性是绝对谈不上的，无法跨大版本升级（必挂，除非纯净系统），意味着你基本上每几个月就必须完全重装一次系统以及配置你的环境。在这里得不到稳定性和长期支持。与 deb 系不同，即使是细微差别的大版本，软件源亦无法通用（依赖变动极为频繁）。这个系统没有事实上的稳定版，所有版本和 [nightly](https://openqa.fedoraproject.org/nightlies.html) 版本无差别。这个系统的稳定性堪比 ArchLinux。反正不如 Ubuntu：具体测试就是把屏幕保护和锁屏休眠都关掉，然后开始编译软件，比如 Chromium，没几个小时整个 Fedora 系统就会白屏卡死，而 Ubuntu 一点事没有。

由此可见 Linux 所谓成功的商业模式就是开源社区免费测试，测试稳定了引入企业版。更多地例如 wine 与 crossover？

这个系统这几年以来，非常地消耗资源，在 VMware 虚拟机中分配的 4G 内存根本无法满足它，必须给更多内存（6-8G）才能进行安装。否则在安装中就会 hang 住。

### CentOS/Rocky Linux/RHEL

目前，CentOS 已经不再是以往的基于 RHEL 源代码构建的操作系统，而是 RHEL 的中游测试系统（CentOS Stream），和 Fedora 差不多了。其替代品五花八门，甚至还有取得了 UNIX 认证的所谓 **欧拉系统**。但是我认为 Rocky Linux 更加有前景。

尽管这些系统在服务器上被广泛部署，但具体缺点就是以牺牲软件的“新”来换取“稳”，软件版本非常陈旧。亦无法跨大版本升级（必挂，而且他们认为安全漏洞无所谓，也不用升级）。

### Debian

Debian 俗称“大便”（谐音+Logo 长得像）。有个[很奇怪的事情](https://lists.debian.org/debian-cd/2020/02/msg00000.html)，设置了 root 密码就不会安装 sudo，他们社区似乎认为这是一件合理的事情，但是你不知道 Gnome 和大多数的登录管理器都默认禁止 root 登录？。Debian 的软件包也不甚更新（此处仅指 stable）。上述这种肉眼可见的 Bug 随手可拾——必须断网或者用高级用户安装才能把这款系统装上——因为他系统换源不换 `debian-security`，却要在安装时有网络的情况下进行更新（Ubuntu 也有这个毛病）；他的 [NetworkManager](https://wiki.debian.org/NetworkManager) 一直在和 Systemd 打架。这种反人类设计数不胜数，即使你报告了 Bug 他们也不会改，甚至不会有人回复你——另外我至今也不知道这玩意怎么报告 Bug。看起来，Debian 的 [Bug 收集平台](https://www.debian.org/Bugs/Reporting)就没想着让普通用户报告 Bug？这套流程比常见开源开发系统的都要离谱的多。~~果然看不到问题就是没有了吗。~~

Debian stable 大部分的软件包在发布后就版本号几乎不会变了。会锁死。除非你切到 unstable 版本或者 sid 之类的，但是那等同于把自己变成 Ubuntu。

不得不说这个系统很稳定，同时软件包也相当旧。几乎是 deb 版本的 CentOS。

### OpenSUSE

完整的 OpenSUSE 在物理机上安装后系统非常的卡顿，据说是 btrfs 文件系统的某个特性，也许特别卡就是特性之一吧。此处拿的是三台不同时期的英特尔平台的物理机测试的。无论是 3 代、还是 6 代都卡的不要不要的。绝非硬件问题。装上去不到一个小时就卡的鼠标都移动不了了，只能强制断电。故，我严重怀疑那些吹嘘 openSUSE 的人，自己到底有没有用过？亦或者是直接把 btrfs 改成了 ext4？

OpenSUSE 俗称大蜥蜴（Logo）。他所做的最迷惑的一件事是他的版本号：为了纪念英国作家道格拉斯·亚当斯在《银河系漫游指南》中写到的这个数字“42”，（被称作 “the answer to life, the universe and everything”，生命、宇宙以及任何事情的终极答案），OpenSUSE 把版本号从 13 蹦到了 42，然后又从 42 降回到了 15。然后搞笑的一件事是：从 42 到 15 本应是升级的过程，但是 42 的版本号比 15 大，于是你到了 15 再升级就会再反向升级到 42。 那么现在问题来了，到了 41 再升级是到 42 还是 43 呢？能做出如此搞笑又迷惑事情的发行版，据我所知，仅此一家（如果有别的也这么离谱，欢迎 PR）。

openSUSE 有时会往整个正在使用的软件包里加入测试性功能，而不进行任何警告与提示。直到你去给他提交 bug，他才会告诉你那是他们故意那么搞得，然后再把测试功能关掉。

他们的原生包管理器命令 `zypper` 和 `dnf` 一直在打架。目前不知道谁打赢了。但我估计 dnf 会赢，因为 zypper 各种反人类（~~比如你数数这有几个字母？~~ `zypper` 相比 `dnf` 存在明显的卡顿和延迟）。


### Gentoo

Gentoo [自称](https://www.gentoo.org/get-started/about/)是“元发行版（*metadistribution*）”。一切软件都要通过 **编译** 的方式来进行安装（最近好像有了[官方二进制源了](https://www.gentoo.org/news/2023/12/29/Gentoo-binary.html)，但是很遗憾，这除了让他的依赖更加混乱以外好像没有别的用处……）。其缺点也很明显，如果一个程序编译不过去就无法安装了，实际上这种软件非常多。有人会抬杠说 Gentoo 有二进制安装方式，但是自己制作也不具备通用性。一旦你一段时间不更新，Gentoo 会告诉你什么叫做 **循环依赖**。而且 Gentoo 难以大规模部署，也难以在服务器上部署。

另外 Gentoo 的 portage（包管理器）是[纯 Python 语言编写的（92.5 %）](https://github.com/gentoo/portage)，这直接导致了计算依赖的时间延迟：在树莓派 4 上，安装 KDE 5 往往要计算几个小时……即使是在英特尔 i7-6700HQ 处理器上，也要算上个几分钟，如此离谱的包管理器，甚为少见。

简而言之，Gentoo 用自己的哲学捆绑了用户，简单问题复杂化，自己折磨自己；USE 过于复杂，对于一些常用软件，都经常出现循环依赖问题，破坏系统稳定性，软件安装升级卸载困难。

Gentoo 平台几乎没有任何 Bug 跟踪回馈机制。对于使系统完全没法用的包管理器的相关 Bug，他们只会在那个软件被删除后告诉你问题不存在了。或者在 [3 年后](https://bugs.gentoo.org/700744)再回复你。

### Deepin/UOS/中标麒麟

UOS 和 Deepin 的关系就好比 RHEL 之于 Fedora。本质上是一种东西。Deepin 系统似乎[从不进行软件测试](https://bbs.deepin.org/post/218041)（更严重的或者骂的比较厉害的帖子早被删了，目前整个论坛只能搜到 15 个相关的，看不到就是不存在问题啦），直接就将更新包推送给用户，最直接结果就是他知道更新会导致系统崩溃也不撤回当次更新，而是在官网一个小角落里写个帖子和你讲怎么修复？这是令人迷惑的思路和解决方案（无独有偶，如果你用过他们的商业性 UOS 系统，这种类似的迷惑行为和解决思路亦只多不少，到处都是）。是的，我刚安装好系统就升级，然后就挂了，这也不是一次两次了，我从未再用过——要知道，Arch Linux 都没有这么离谱。

Deepin 这个系统仅仅是复制文件就会导致桌面卡死，无法理解他的系统是怎么做出来的，难道他自己的开发者不需要复制文件吗？

>有些人一直在 **云** 这个东西，反驳说他这么垃圾怎么可能还卖得出去，还会有人买。那么**你到底用过没有呢？** 系统的市场表现可能不错，但这并不一定能反映其技术质量——比如 Linux。多说也没用，你用过吗？

这种不测试就推更新的行为不仅发生在开源的 Deepin 上，UOS 也经常如此。而且不是一次两次了，他们好像和微软一样没有测试团队。

对于中标麒麟无话可说。

### Arch Linux/Manjaro

Arch Linux 俗称“**[邪教](https://zh.moegirl.org.cn/zh-hans/Arch_Linux%E5%A8%98)、[洗发水](https://bbs.archlinuxcn.org/viewtopic.php?id=694)**”。这是我所见过的一个最不稳定的 Linux 发行版，也是被别人忽悠从而安装最多的一个。

我难以理解为什么有这么多人选择如此不稳定的一个操作系统。你安装的软件越多，挂的越快（你不信你把完整的 gnome 安装上，看看你能维持几天不挂？）。有人会说这是你不看软件发行注记的后果，此言差矣。一个需要看发行注记才能更新的系统，本身就是有问题——和 Deepin 把解决方案写在墙角有区别？

Arch Linux 唯一优点就是软件新（但是也不是所有的都新，一些工具类、尤其是大部分 **实用工具** 就不怎么新，例如大部分 R 包还没有 FreeBSD 新）。似乎随处可见的就是 Arch Linux。Arch Linux 似乎是与苦难哲学挂钩的。

Arch Linux 官方源里基本上没有什么软件，不导入 aur 源（ Arch User Repository，Arch 用户软件仓库）就完全没法用。而 aur 源是[未经过任何代码审查的](https://wiki.archlinux.org/title/Arch_User_Repository)（`Warning: AUR packages are user-produced content. These PKGBUILDs are completely unofficial and have not been thoroughly vetted. Any use of the provided files is at your own risk.`，`警告： AUR 中的软件包是由其他用户编写的，这些 PKGBUILD 完全是非官方的，未经彻底审查。使用这些文件的风险由您自行承担。`）实际上不是未经彻底审查，是根本没有任何审查：也就是说有人往里面塞 `rm -rf /*` 也是可以的。虽然 fakeroot 在一定程度上限制了恶意软件的执行权限，但它并不能完全防止用户因安装未审查的软件包而面临的安全风险——你忘记[安卓的格机模块](https://www.bilibili.com/read/cv19088202/)了？即使是谷歌市场也有一堆恶意软件，更何况现在压根没有审查。

正如 FreeBSD 开发者 Warner Losh 所说，“如今，在开源项目处于日益恶劣的工作环境下，一些看似多余的步骤却往往是必要的。”

## FreeBSD 与 Linux 不同之处

- FreeBSD 仍然使用传统的 INIT 引导，而非 systemd；
- FreeBSD root 用户 shell 默认是 csh（14 改为 sh），而不是 bash；
- FreeBSD 基本系统几乎不包含任何非 BSD 协议的软件，并致力于去 GNU 化（这意味着基本系统不使用 Glibc、GCC 等软件；**其实不是 BSD 一直在去 GNU 化，而是 Linux 一直在 GNU 化**），见 <https://wiki.freebsd.org/GPLinBase>
- FreeBSD 的用户配置文件和系统配置文件严格分离，即内核和基本系统与第三方应用程序是完全分离的；
- FreeBSD 项目是作为一个完整的操作系统维护的，而非内核与 userland 单独维护；也就是说如果你要使用 FreeBSD，那么就只有一个 FreeBSD 可选；
- FreeBSD 没有 free 命令也不支持安装这个包(FreeBSD 早就不使用 procfs 了)，FreeBSD 基本系统自带的文本编辑器有 ee 和 vi（不是软链接到 vim 的 vi，是真实的 nvi），没有预装 wget，而是 fetch。

## FreeBSD 的缺陷

- FreeBSD 没有为用户提供一个带 GUI 的基本系统，甚至显卡驱动都需要自己通过 ports 编译安装；
- FreeBSD 的驱动很差劲，直到最近才将将完美地支持 WIFI 6 的网卡，比如 AX210；
- FreeBSD 的开发者非常少，这意味着你的 bug 可能很久都无法得到解决，不是所有软件包都像 ARCH 那样时刻保持最新版；
- FreeBSD 的资料相对较少，中文资料更少，除了本文以外的简体中文资料几乎为 0；
- 由于 systemd 不兼容 Linux 以外的操作系统，导致很多软件比如 NetworkManager 无法移植，桌面环境的组件也无法完善；
- FreeBSD 的菊苣们比 Linux 的还要更加高傲，他们不在意你到底会不会换源会不会设置代理，需不需要境内的官方镜像站；
- 由于 FreeBSD 项目的基本目标和设计问题，FreeBSD 基本系统不包含一般 Linux 中常用的一些软件和命令，比如没有 `lspci`,`free`。有些可以自己安装，有些则不行；
- FreeBSD 的两个文件系统 ZFS 与 UFS 都只能扩大不能缩小，一个奇怪的设计；
- FreeBSD 缺乏上层应用软件设计，即使底层有类似 docker 的技术 jail 也没能发展起来；FreeBSD 的虚拟化技术 Byhve 也很难用，没有一个前端的 GUI 来控制，设定参数也缺乏一个统一的教程。

> 我们现在称为容器技术的概念最初出现在 2000 年，当时称为 FreeBSD jail，这种技术可将 FreeBSD 系统分区为多个子系统（也称为 Jail）。Jail 是作为安全环境而开发的，系统管理员可与企业内部或外部的多个用户共享这些 Jail。2001 年，通过 Jacques Gélinas 的 VServer 项目，隔离环境的实施进入了 Linux 领域。在完成了这项针对 Linux 中多个受控制用户空间的基础性工作后，Linux 容器开始逐渐成形并最终发展成了现在的模样。2008 年，Docker 公司凭借与公司同名的容器技术通过 dotCloud 登上了舞台。—— [什么是 Linux 容器？](https://www.redhat.com/zh/topics/containers/whats-a-linux-container)

## 基本对比

|   操作系统   |                           发布/生命周期（主要版本）                           |                          主要包管理器（命令）                          |                        许可证（主要）                        | 工具链 |   shell    |     桌面     |
| :----------: | :---------------------------------------------------------------------------: | :--------------------------------------------------------------------: | :----------------------------------------------------------: | :----: | :--------: | :----------: |
|    Ubuntu    |             [2 年/10 年](https://ubuntu.com/about/release-cycle)              |        [apt](https://ubuntu.com/server/docs/package-management)        | [GNU](https://ubuntu.com/legal/intellectual-property-policy) |  gcc   |    bash    |    Gnome     |
| Gentoo Linux |                                   滚动更新                                    |       [Portage（emerge）](https://wiki.gentoo.org/wiki/Portage)        |                             GNU                              |  gcc   |    bash    |     可选     |
|  Arch Linux  |                                   滚动更新                                    |           [pacman](https://wiki.archlinux.org/title/pacman)            |                             GNU                              |  gcc   |    bash    |     可选     |
|     RHEL     | [3/最长 12 年](https://access.redhat.com/zh_CN/support/policy/updates/errata) | [RPM（yum、dnf）](https://www.redhat.com/sysadmin/how-manage-packages) |                             GNU                              |  gcc   |    bash    |    Gnome     |
|   FreeBSD    |               [约 2.5/5 年](https://www.freebsd.org/security/)                |                               pkg/ports                                |                             BSD                              | clang  |   csh/sh   |     可选     |
|   Windows    |       [不固定](https://docs.microsoft.com/zh-cn/lifecycle/faq/windows)        |                                  可选                                  |                             专有                             |  可选  | powershell | Windows 桌面 |
|    MacOS     |                                 1 年/约 5 年                                  |                                   无                                   |           [专有](https://www.apple.com/legal/sla/)           | clang  |    zsh     |     Aqua     |


## 命令替代/软件替代

因为 Linux 广泛使用的也是 GNU 工具，因此只要理论上不是依赖于特定的 Linux 函数库，该工具都可以在 FreeBSD 上运行。

| Linux 命令/GNU 软件 | FreeBSD 命令/BSD 软件 | 需要安装的包（安装方式） |      作用说明      |                                                                                    额外说明/苦难哲学                                                                                     |
| :-----------------: | :-------------------: | :----------------------: | :----------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|        lsusb        |         lsusb         |   pkg install usbutils   |   显示 USB 信息    |                                                                            粗略地可以用 `cat /var/run/dmesg`                                                                             |
|        lspci        |         lspci         |   pkg install pciutils   |    显示主板信息    |                                                                            粗略地可以用 `cat /var/run/dmesg`                                                                             |
|        lsblk        |         lsblk         |    pkg install lsblk     |  显示磁盘使用情况  |                                                                                            /                                                                                             |
|        free         |       freecolor       |  pkg install freecolor   |  显示内存使用情况  | FreeBSD 没有提供`free`命令，因为其依赖 Linux，由包`procps`提供，但是呢，FreeBSD 早就不使用`procfs`了。如实在需要`free`可以用 `https://github.com/j-keck/free` 其他可选命令是 `vmstat -h` |
|        lscpu        |         lscpu         |    pkg install lscpu     |   显示处理器信息   |                                                                                            /                                                                                             |
|        glibc        |        bsdlibc        |            /             |        C 库        |                                                                                            /                                                                                             |
|         GCC         |     LLVM + Clang      |            /             | 编译器、编译链工具 |                                                                              非要用也可以`pkg install gcc`                                                                               |
|         vim         |          vim          |     pkg install vim      |     文本编辑器     |                                                                  FreeBSD 默认的`vi`并不被软连接到`vim`，而是真正的`nvi`                                                                   |
|        wget         |         wget          |     pkg install wget     |       下载器       |                                                                               系统默认的下载工具是`fetch`                                                                                |
|        bash         |         bash          |     pkg install bash     |       shell        |                                              系统默认的`root shell`是`csh`,修改会导致配置输入法环境变量时遇到困难以及可能会无法进入恢复模式                                              |
|   NetworkManager    |      networkmgr       |  pkg install networkmgr  |    网络连接工具    |                                                                        NetworkManager 依赖 `systemd` 无法直接移植                                                                        |
|                     |                       |                          |                    |                                                                                                                                                                                          |
|                     |                       |                          |                    |                                                                                                                                                                                          |
