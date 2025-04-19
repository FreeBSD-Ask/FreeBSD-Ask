# 第 1.4 节 为什么要使用 FreeBSD？


## 选择 FreeBSD 的一句话原因——FreeBSD 能在流变的世界中寻求理想的中道

- **FreeBSD 能在这激变的世界中寻求理想的中道**

如果你想选择一款同 Windows、Android 一样的，在大版本更新后也不怎么影响日常工作的系统，而不是每天都在和操作系统斗智斗勇，FreeBSD 值得信赖。

绝大部分或者说几乎所有的 Linux 的配置文件和系统组件都是 **变来变去的**，这在大版本变动时尤为突出。而且 Linux 始终是在进行着 **破坏性变化**（Breaking change）。

CentOS、Debian 只是 **在生命周期内不变** 罢了，但是大版本更新也不具有任何的连贯性和稳定性。且由于 **长期不变**，大版本的 **变动**，只会更加离谱，更加无法迁移。而且由于 Linux 设计上从未区分基本系统与第三方用户软件，故此类系统 **在生命周期内不变** 的代价是，任何软件的版本也不会变，也变不了，更不能变。

这意味着：

1、如果你需要不断地更新你工作所需的软件版本或者开发工作。那么你几乎总是在处理和操作系统有关的故障，不能专注于自己的开发或服务或者解决其本身的实际问题。

你几乎就是每天都在和系统打架，修理这个难用的锤子，因为他总是会脱把。而不是真正在用它来钉钉子。——单单仅是 Systemd 造成的 Bug 几辈子也修不完，你每天基本上不用干活，都在和这些东西斗智斗勇。

2、除非你的 Linux 环境从未升级过也从未打过补丁更新，因为生产工具和环境已经固定且不再变动，也不想或没有意义花钱更新，即直接放弃了更新与升级。事实上，之前大部分 Linux 就是这么被使用的。所以看起来没有一点问题。但是这存在着巨大的安全隐患和共同故障点。并且你迟早是要升级的，除非你破产倒闭了。这只是时间问题。但是因为你选择了 Linux，升级将是不可能的，几乎所有的配置文件和依赖项目都在变，甚至不存在了，变没了也是常有的事，只能从头再来。你原来的稳定性将不复存在。

即使你 **不想变**，那些非技术人员和整个市场也会迫使你去更新换代，**让你不得不变**。比如，你现在还能继续使用你的 Flash 吗？

## 选择 FreeBSD 的一般原因

- **从道家来讲，你爱用不用，不用拉倒。太长不看，不用？对其他的原因有意见？请重复看此条目**
- 从佛学来说，因为缘分。万物缘起性空，我们有缘相聚，又会者定离。万般诸相皆如此。
- 从基督教来讲，这是主的指引。上帝在永恒的现在中创世。就像出埃及记一样，你看上去是自己的选择，实际上都是主的安排。
- 从黑格尔来讲，是因为辩证否定。FreeBSD 是 UNIX 直接后裔，而 Linux 仅仅是款仿制品，而很多协议又脱胎于 UNIX，所以你注定了要来到这里。
- 按照我个人观点而言，追求软件的稳定和新，既要有二进制源，又要能编译安装。除了 FreeBSD 之外我找不到 Linux 系统。（~~VoidLinux？~~）
- BSD 三则授权协议：允许自由分发。GPL 与 BSD 协议，究竟何者是真正的自由？GPL 最多只是通过限制自由来确保他所谓的自由罢了。学习 BSD 就和学习哲学一样，本身并不是为了某种确切的知识而去学习，而是为了自由而去学习（因为在大多数人眼中 BSD 已然不具有所谓的实用价值了）。那么在这一点上，可以说，按照他们的想法，BSD 与其他操作系统有根本上的不同——即 BSD 是真正的自由。
- FreeBSD 是学院派的开源实践产物，也是 UNIX 哲学的忠实践行者。
- 远离碎片化的 Linux 发行版，使得选择困难症用户免受痛苦。
- BSD 是一个完整的 OS，而不是内核。内核和基本系统作为一个项目来整体维护。——请注意，这是所有 Linux 系统的缺陷所在。没有事实上的基本系统的概念和区分会造成一系列违反直觉的事情。
- Linux 社区已经成为一个肮脏的泥潭，无论是内核开发还是用户群组。——见文学故事。

## 选择 FreeBSD 的技术性原因

- 基本系统的配置文件与第三方软件配置文件相分离。你不会遇到像在 RHEL 中使用 rpm 命令卸载 glibc 导致系统毁灭这种奇葩的事情（无独有偶，有时候 yum 的错误操作会卸载包括使用中的所有内核），FreeBSD 的包管理器不干涉基本系统。
- 不会锁死软件版本，比如 Python GCC 等 Linux 中系统依赖的软件。所有软件都会滚动更新。这些非滚动版本的 linux 的软件版本基本上在该版本上锁死的，不会得到任何功能版本更新。滚动版本的又有一堆稳定性问题。BSD 所有版本共用一个 ports，只有极小一部分软件和系统版本硬捆绑，其他都是可以滚动更新的。而且由于基本系统的存在，第三方的软件几乎不影响系统的稳定性。Linux 则无法在软件更新和系统稳定之间找到平衡点。
- 文档齐全，FreeBSD doc 与 src 是同等地位的，不分高下。
- 安全漏洞相比于 Linux 较少。
- 可以避免在产品和架构中出现共同故障点。
- 接近 2 年的版本发布周期，4 年的维护周期赋予了 FreeBSD 稳定性。
- 通过 BSD 的 Ports 可以编译安装软件，进行自由配置。
- ZFS 文件系统可以被配置为 `\` 分区。ZFS 被誉为最强大的文件系统。
- Jail 与 byhve 虚拟化，不必配置底层虚拟化，节约系统资源。
- 传统的 BSD INIT 引导，使你免受 systemd 迫害。
- DTrace 框架与 GEOM 存储框架。
- Linux 二进制兼容层，可运行 Linux 软件，只要其支持 CentOS 或 Ubuntu/Debian。且软件运行速度快于 Linux。
- 安全事件审计。
- 不同于 Linux 驱动捆绑内核的做法，FreeBSD 的驱动在大致上与内核解耦合。
- Linux 内核开发是一个[相当封闭的过程](https://www.kernel.org/doc/html/latest/process/submitting-patches.html)，只有少数人能够参与直接提交代码。而 FreeBSD 秉持人人自由开发的理念，目前[你可以直接在 Github 上提交你的代码](https://github.com/freebsd/freebsd-src/pulls)，或者注册个账号在 <https://reviews.freebsd.org/> 进行大规模变更。
- 另请参见 [Linux 内核编码风格](https://www.kernel.org/doc/html/latest/process/coding-style.html)。而 FreeBSD 的代码风格是 Kernighan & Ritchie 的《C 程序设计语言》中使用的风格。
- 由于 Ports 的存在，FreeBSD 的老系统的软件源仍然可以正常使用，而不像 Linux 那样一旦 EoL 就没有软件源可用了。

### 参考文献

- [Submitting GitHub Pull Requests to FreeBSD](https://freebsdfoundation.org/our-work/journal/browser-based-edition/configuration-management-2/submitting-github-pull-requests-to-freebsd/)，翻译在[在 GitHub 上向 FreeBSD 提交 PR](https://github.com/taophilosophy/freebsd-journal-cn/blob/main/2024-0506/zai-github-shang-xiang-freebsd-ti-jiao-pr.md)
- [Contribution Guidelines for GitHub](https://github.com/freebsd/freebsd-src/blob/main/CONTRIBUTING.md)，应该以此为准


## 选择 FreeBSD 的社会意义

### GNU 与开源软件运动已走到了尽头

- Linux Kernel 由 Linus 一人裁决：“[Linus Torvalds 是决定改动能否进入 Linux 内核的最终裁决者。](https://www.kernel.org/doc/html/latest/translations/zh_CN/process/submitting-patches.html)”而 FreeBSD 最终由两年一届的核心团队集体决策。


>**思考题**
>>
>> 显而易见：目前 FreeBSD 上的桌面部件的缺失很大程度上是因为他们过分依赖了 Linux 特有函数库，比如包含 `ip` 命令的 `iproute2` 软件包。更多的原因则是因为这些桌面或部件和 systemd 做了深度捆绑或者根本就是强制依赖，比如 `NetworkManager` 。而 Samba 开发者则会说“We use Linux, we develop for Linux, all others please submit patches”。FreeBSD 社区的人把这种行为叫做“Linuxism”（Linux 主义/Linux 歧视），你会在文学故事章节里引用的链接中再次见到这个词，且某些人以此为豪。
>>
>> 这种行为会导致何种后果我们不得而知，但是这种程序愈来愈多了，而且有成为主流的趋势，甚至就连大部分开发者在开发程序时也不再考虑兼容 init，比如 `todesk`。甚至 Java 程序都丧失掉了他的可移植性，为什么 FreeBSD 上的 Eclipse 将近两年没有更新？就是因为这类[捆绑问题](https://git.eclipse.org/r/c/platform/eclipse.platform.swt/+/163641/)。最近甚至还有了 `systemd-boot` 来取代 `grub2`，在可预见的未来，Linux 将被 systemd 统一。而其程序（预计所有可运行在 Linux 上的程序）也不再具有任何的可移植性。
>>
>>或许 Linux 的开源到了尽头。“你可以继续造你的轮子，但是你不兼容我的 systemd 你就运行不了任何程序。”现在 FreeBSD 所面临的这种困境，将是所有人要面对的。
>>
>>Linux 已经完完全全背弃了他所出发的哲学与思想这件事是确凿无疑的。
>
>真的是这样吗？又为什么会这样，你怎么看？

- 选择 FreeBSD，就是选择在 Linux 被 systemd 及其背后的商业公司控制以后，还能够保留一份火种。纵观各大操作系统，有能力替代的，开源的操作系统只有 FreeBSD。
- 选择 FreeBSD，就是选择保留下一份真正开源的、自由的操作系统。能够使开源事业继续坚持下去，并践行真正的 UNIX 哲学，不走改旗易帜的邪路，封闭之路。

### 旧闻：《[FreeBSD 基金会收到史上最大一笔捐款](https://freebsdfoundation.blogspot.com/2014/11/freebsd-foundation-announces-generous.html)》


>上周，我向 FreeBSD 基金会捐赠了 100 万美元，FreeBSD 基金会支持着开源操作系统 FreeBSD。FreeBSD 帮助了数百万程序员追随他们的热情、实现创意。我自己就是受益者。在 90 年代末，我开始使用 FreeBSD，那时我经济拮据，住在政府提供的住房中。在某种程度上，FreeBSD 帮助我摆脱了贫困——我能进入 Yahoo!（雅虎）工作的重要原因是，他们使用 FreeBSD，而这正是我首选的操作系统。多年后，当 Brian 和我开始创建 WhatsApp 时，我们依然使用 FreeBSD 来支撑我们的服务器运营，直到今天亦如此。
>
>我发布这项捐赠的消息，是希望让更多人看到 FreeBSD 基金会所做的有益工作，并激励他人也能支持 FreeBSD。我们大家都会受益，如果 FreeBSD 能够继续为像我一样的人提供机会，帮助更多的移民子女脱贫，帮助更多的初创公司创造出成功，甚至是具有变革性的成果。
>
>——WhatsApp 原 CEO 及创始人 Jan Koum

实际上，这并非一锤子买卖，在查阅 FreeBSD 基金会捐款名单（可查 [2018](https://freebsdfoundation.org/our-donors/donors/?donationYear=2018)、[2019](https://freebsdfoundation.org/our-donors/donors/?donationYear=2019)、[2020](https://freebsdfoundation.org/our-donors/donors/?donationYear=2020)、[2021](https://freebsdfoundation.org/our-donors/donors/?donationYear=2021)、[2022](https://freebsdfoundation.org/our-donors/donors/?donationYear=2022)）后就会发现，Jan Koum 仍在继续以 [Koum Family Foundation](https://philanthropynewsdigest.org/news/other-sources/article/?id=15306123&title=Tech-Philanthropy-Watch:-WhatsApp-Founder-Jan-Koum-Has-a-New-$1.5-Billion-Fund) 的名义在持续地为 FreeBSD 捐款。每年都捐款 25 万美元以上。

### 诚实与可信

像 FreeBSD 这样默默地在后台工作以至于快被用户遗忘的系统，可能真算得上是个老古董了，如果每日时不时地出现一些蓝屏报错，Kernel Panic 亦或者“内部错误”、`You are in emergency mode`、`BusyBox （initramfs）`、`grub  rescue>` 等等，反而能提醒用户自己的存在。不是吗？那些弹窗软件、3Q 大战、摇一摇的恶俗广告、百度的莆田系和国产操作系统、从绿坝娘再到现在安卓手机预装的反诈软件不也挺成功的吗？

目前大部分使用 Linux 作为专用设备操作系统，或是基于其他 GPL 软件构建自己商业产品的公司，都没有严格遵守 GPL 协议发布他们的代码。而对于国内公司来说，他们甚至不知 GPL 为何物，只认为免费就可以了，那些为了逃避 GPL 强制开源规定的企业之产品是不值得我们去使用的。抢注开源软件商标的事情亦时有发生。比较起来，那些使用 FreeBSD 的公司至少更为诚实、可靠和值得信赖。也真正使得 BSD 的代码为众人所用——哪怕有人认为 FreeBSD 已经日落西山——尽管在这些人的确一直生活在 FreeBSD 的光芒的照耀之下。

#### 参考文献

王波《FreeBSD 在中国的未来》。引自《FreeBSD 使用大全》第二版，机械工业出版社，2002，ISBN 9787111102861


## 进一步了解

- 有基金会的官方版本，参见[《为什么你应该使用 FreeBSD》](https://book.bsdcn.org/fan-yi-wen-zhang-cun-dang/2024-nian-11-yue/why)。
- [systemd 背后的真正动机](https://freebsd.gitbook.io/translated-articles/the-real-motivation-behind-systemd)
- [systemd 在任何地方都不安全](https://freebsd.gitbook.io/translated-articles/systemd-isnt-safe-to-run-anywhere)
- [GPL 之殇](https://freebsd.gitbook.io/translated-articles/the-problems-with-the-gpl)
- [为什么你应该将所有东西从 Linux 迁移到 BSD](https://freebsd.gitbook.io/translated-articles/why-you-should-migrate-everything-from-linux-to-bsd)
- [新的 Ports 提交者：oel Bodenmann (jbo@freebsd.org)](https://book.bsdcn.org/freebsd-za-zhi-jian-ti-zhong-wen-ban/2023-1112/xin-de-port-ti-jiao-zhe-oel-bodenmann-jbofreebsd.org)
