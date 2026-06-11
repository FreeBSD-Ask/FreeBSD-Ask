# 2.1 FreeBSD：理想、现实与中道

## 谁在使用 FreeBSD

以下是一些典型的应用案例。

![谁在使用 FreeBSD](../.gitbook/assets/who-uses-freebsd.png)

图片来源 [FreeBSD 基金会宣传图](https://i.imgur.com/qW0IePB.png)。

- 华纳兄弟. 黑客帝国[EB/OL]. [2026-03-26]. <https://movie.douban.com/subject/1291843/>. 黑客帝国的特效正是在一组 FreeBSD 集群上制作的。另见 Urban M, Tiemann B. FreeBSD 技术内幕[M]. 智慧东方工作室，译. 北京：机械工业出版社，2002：2. ISBN: 978-7-111-10201-4、FreeBSD Project. FreeBSD Press Release: April 22, 1999[EB/OL]. (1999-04-22)[2026-03-26]. <https://www.freebsd.org/press/press-rel-1/>.
- The New Stack. Apple’s Open Source Roots: The BSD Heritage Behind macOS and iOS[EB/OL]. [2026-03-26]. <https://thenewstack.io/apples-open-source-roots-the-bsd-heritage-behind-macos-and-ios/>. Apple 的操作系统如 macOS、iOS 等大量复用了 BSD（不限于 FreeBSD）的技术栈。BSD 堪称 macOS 的开源基石。
- Sony. FreeBSD Kernel[EB/OL]. [2026-03-26]. <https://www.playstation.com/en-us/oss/ps4/freebsd-kernel/>. 索尼（Sony）的游戏机 PlayStation 4（PS4）和 PlayStation 5（PS5）使用的操作系统基于 FreeBSD。PlayStation 3（PS3）的 CellOS 和 PlayStation Vita（PSV）的操作系统也以 FreeBSD 和 NetBSD 为基础构建。
- FreeBSD Foundation. Netflix Case Study[EB/OL]. [2026-03-26]. <https://freebsdfoundation.org/netflix-case-study/>. 奈飞（Netflix）几乎所有网络活动（内容缓存/CDN）均基于 FreeBSD 设备运行。
- QNX. Search Results[EB/OL]. [2026-03-26]. <https://www.qnx.com/developers/docs/8.0/search.html?searchQuery=freebsd>. QNX 操作系统。QNX 是一种微内核实时操作系统（RTOS），其内核为自主研发，并非基于 FreeBSD。QNX 以前是黑莓手机的操作系统。QNX 现在被广泛应用为汽车安全操作系统——在主流座舱架构中，QNX Hypervisor 负责安全关键域（如仪表盘、ADAS），同时将 Android Automotive 作为客户操作系统在虚拟机中运行，以实现信息娱乐功能（参见：BlackBerry QNX. QNX Hypervisor 8.0[EB/OL]. [2026-04-17]. <https://blackberry.qnx.com/en/products/foundation-software/qnx-hypervisor>）。国内新能源车辆广泛采用了 QNX 操作系统，QNX 在汽车安全关键系统中占据重要市场份额。QNX 在其新一代网络栈 io-sock（QNX 8.0 起）及部分用户空间组件中复用了 FreeBSD 的代码（旧版网络栈 io-pkt 复用的是 NetBSD 代码）。
- Dell. PowerScale OneFS：了解基于源的路由[EB/OL]. (2024-05-28)[2026-03-26]. <https://www.dell.com/support/kbdoc/zh-cn/000020056/isilon-onefs-understanding-source-based-routing-sbr-in-isilon?lang=zh>. Dell EMC Isilon，戴尔的 Isilon（面向企业的 NAS 存储设备）设备使用的操作系统 OneFS 基于 FreeBSD（OneFS 8.2 基于 FreeBSD 11；OneFS 9.x 的 FreeBSD 底层版本未公开）。
- Beckhoff. TwinCAT/BSD: operating system for Industrial PCs[EB/OL]. [2026-03-26]. <https://www.beckhoff.com/en-en/products/ipc/software-and-tools/twincat-bsd/>. Beckhoff 倍福自动化控制系统的操作系统 TwinCAT/BSD，将 TwinCAT 实时核与 FreeBSD 结合，应用于工业 PC 平台。
- OpenHarmony. kernel_liteos_a[EB/OL]. [2026-03-26]. <https://gitee.com/openharmony/kernel_liteos_a/tree/master>. OpenHarmony LiteOS 内核引入了 FreeBSD 代码用于驱动程序等。

### 参考文献

- FreeBSD Foundation. Read how organisations are using FreeBSD across the globe[EB/OL]. [2026-03-25]. <https://freebsdfoundation.org/end-user-stories/>. FreeBSD 基金会官方整理的 FreeBSD 各领域典型应用案例汇总。

## 为什么选择 FreeBSD

### 核心缘由：FreeBSD 能在这流变的世界中寻求理想的中道

相较于大多数主流操作系统或内核，FreeBSD 在 STABLE 分支内保持 ABI 稳定，内核 API 则不保证跨版本兼容。

FreeBSD 项目整体风格偏于保守，奉行最小惊讶原则（Principle of Least Astonishment，POLA），即设计必须符合用户的习惯、期望和心智能力。其配置文件和系统组件不会频繁变化，大版本间迁移尤为审慎。FreeBSD 也谨慎对待破坏性变更（Breaking change），要求在大版本内保持 ABI 稳定。

FreeBSD 不仅在生命周期内保持稳定，大版本更新也具有连贯性和稳定性，可便捷实现大版本间的迁移。FreeBSD 上的软件版本可以滚动更新，不会锁定特定版本（如 Python 等）。

### 选择 FreeBSD 的一般原因

- 追求软件的稳定性与新颖性，既需具备二进制包，又需支持编译安装。除 FreeBSD 外，鲜有开源系统兼具上述特征（~~Void Linux 还是算了吧~~）。
- BSD 赋予了更纯粹的自由：不以限制自由来保障自由，而以信任与开放成就真正的自由。
- FreeBSD 是学院派工程实践的成果，也是 UNIX 哲学的现代延续。
- 其他操作系统生态愈发碎片化，而 FreeBSD 的一体化设计避免了持续的选择困境，但这并非限制，亦可按需自由修改。
- BSD 是一款完整的操作系统，而非单纯的内核。内核和基本系统作为一个项目整体维护。缺乏基本系统的概念，将带来持续的混乱与有悖直觉的使用体验。
- FreeBSD 项目由核心小组领导。
- FreeBSD 社区与开发者均秉持“慢就是快，快就是慢”的哲学理念。~~我们的确需要花些时间慢下来，审视自己的一切，无论知识还是自我。花些时间在路旁的花朵石子上面，也许并不是浪费时间，无所事事。~~

- 教育与研究：FreeBSD 项目将内核与用户空间整合在同一代码仓库中，极大便利了研究与学习，且代码注释清晰丰富，便于查阅特定功能的实现方式。

> **技巧**
>
> 还可以从更多视角审视选择 FreeBSD 的原因：
>
> - 从佛法来说，因为缘分。万物缘起性空，有缘相聚，会者定离。万般诸相皆如此。
>
> - 从基督教来讲，这是主的指引。上帝在永恒的现在中创世。就像《出埃及记》一样，看上去是自己的选择，实际上都是主的安排。
> - 从黑格尔来讲，由于辩证否定。FreeBSD 是 UNIX 的直接后裔，而很多协议又脱胎于 UNIX，所以注定了要来到这里。

### 选择 FreeBSD 的技术原因

- FreeBSD 基本系统的配置文件与第三方软件配置文件相分离，系统级配置文件与用户配置文件相分离。FreeBSD 的文件系统层次结构遵循明确的组织原则。~~再也不用到处用 `find` 命令查找某个 `.conf` 文件到底安装在哪了。~~
- 由于基本系统的存在，第三方的软件几乎不影响系统的稳定性。FreeBSD 在软件更新和系统稳定之间保持了平衡。
- 通过 BSD 的 Ports 可以编译安装软件，自由配置。
- 不会锁定软件版本。例如 Python、GCC 等常见的系统依赖软件。但所有的 FreeBSD 都共用相同的 Ports，无论新旧系统，其第三方软件的版本都是相同的；仅极个别软件和系统版本硬捆绑，其余所有软件都可滚动更新。
- 由于 Ports 系统的存在，旧版 FreeBSD 系统仍能正常获取并编译软件，并非在达到生命周期终点（EoL）后便无法获得软件更新。
- 在 FreeBSD 项目中，文档并非附属品。FreeBSD doc 项目与 src 项目地位同等，无主次之分。
- 可便捷地为根分区（**/**）配置使用 ZFS 文件系统。ZFS 被公认为功能最为完备的文件系统之一。
- 每 2 年一次的大版本发布周期和 4 年的维护周期（自 FreeBSD 15 起由原有的 5 年调整为 4 年）保障了 FreeBSD 的稳定性。
- Jail 不需要额外安装和维护底层虚拟化栈，也无需为每个实例启动完整的操作系统内核和用户空间，节省系统资源；bhyve 虚拟化同样内置于基本系统，但作为虚拟机管理程序，每个实例需运行完整的客户操作系统。
- 传统的 BSD init 引导，回归简洁，回归纯文本的可见性。
- DTrace 框架与 GEOM 存储框架。
- Linux 二进制兼容层可运行 Linux 软件，系统调用密集型工作负载下存在少量性能开销，计算密集型任务则接近原生性能。
- FreeBSD 的驱动以内核模块形式存在，可动态加载和卸载，便于按需管理硬件。
- FreeBSD 秉持人人自由开发的理念，可以直接在 GitHub 上[提交代码](https://github.com/freebsd/freebsd-src/pulls)，或者注册账号在 <https://reviews.freebsd.org/> 提交大规模变更。
- FreeBSD 的代码风格是 BSD KNF（Kernel Normal Form），基于 CSRG 的 KNF 规范，其大括号布局是 K&R 风格的一种变体（函数左大括号独占一行，控制语句左大括号与语句同行），与 Kernighan & Ritchie 经典著作《The C Programming Language》（中译本：Kernighan B W, Ritchie D M. C 程序设计语言[M]. 徐宝文，李志，译. 第 2 版. 北京：机械工业出版社，2019. ISBN: 978-7-111-61794-5.）中使用的 K&R 风格一致。

#### 参考文献

- FreeBSD Foundation. Submitting GitHub Pull Requests to FreeBSD[EB/OL]. [2026-03-25]. <https://freebsdfoundation.org/our-work/journal/browser-based-edition/configuration-management-2/submitting-github-pull-requests-to-freebsd/>. 详解 FreeBSD 通过 GitHub 接受贡献的流程与规范。
- FreeBSD Project. Contribution Guidelines for GitHub[EB/OL]. [2026-03-25]. <https://github.com/freebsd/freebsd-src/blob/main/CONTRIBUTING.md>. FreeBSD 源代码贡献的官方指导与要求。
- Linux Kernel Documentation. Linus Torvalds 是决定改动能否进入 Linux 内核的最终裁决者[EB/OL]. [2026-03-25]. <https://www.kernel.org/doc/html/latest/translations/zh_CN/process/submitting-patches.html>. 展示 Linux 内核开发的集中式决策模式。
- Linux Kernel Documentation. Linux 内核编码风格[EB/OL]. [2026-03-25]. <https://www.kernel.org/doc/html/latest/process/coding-style.html>. 规范 Linux 内核代码风格与格式要求。
- Linux Kernel Documentation. Linux 内核开发是个较为封闭的过程[EB/OL]. [2026-03-25]. <https://www.kernel.org/doc/html/latest/process/submitting-patches.html>. 说明 Linux 内核开发的参与门槛与流程。
- Cdaemon. Sandbox Your Program Using FreeBSD's Capsicum[EB/OL]. [2026-03-25]. <https://cdaemon.com/posts/capsicum>. FreeBSD 安全沙盒框架的基本原理与使用方法。

### 选择 FreeBSD 的社会意义

#### 红帽公司影响下的 Linux 生态偏向

GNOME、Xorg（X11）、D-Bus、systemd、PulseAudio、Wayland、PipeWire 等主流 Linux 项目实际上受到红帽公司（Red Hat）的显著影响，且大多难以完全适配其他类 UNIX 操作系统。

目前 FreeBSD 桌面部件缺失，在较大程度上源自对 Linux 特有函数库的强依赖，例如包含 ip 命令的 `iproute2` 软件包。更为重要的原因在于这些桌面或部件与 systemd 存在深度捆绑或强制依赖关系，例如 `NetworkManager`。而 Samba 等项目的开发以 Linux 为中心，对非 Linux 平台的兼容性关注不足。FreeBSD 社区将此类现象称为“Linuxism”（Linux 主义/Linux 歧视）。

这种行为将导致何种后果尚不得而知，但此类程序正变得越来越多，并有成为主流的趋势。许多开发者开发程序（如 `todesk`）时也不再考虑对传统 init 系统的兼容。Java 程序也逐渐丧失了可移植性；由于此类捆绑问题，FreeBSD 上的 Eclipse 更新曾长期滞后。如果此趋势持续，可运行在 Linux 上的程序的可移植性可能进一步降低。

目前 FreeBSD 所面临的困境，未来其他系统也可能会遇到。

- 选择 FreeBSD，即选择保留自由软件的根基。
- 选择 FreeBSD，即选择保留一份真正自由的操作系统。能够使开源事业持续发展，并践行真正的 UNIX 哲学。

##### 参考文献

- D'Pong P. Bug 562443 - SWT spams temp folder with innumerable folders[EB/OL]. (2020-05-26)[2026-04-05]. <https://gitlab.simantics.org/simantics/eclipse/eclipse.platform.swt/-/commit/19153b908d6d4cedcbd59824686717502cfde4f7>.
- FreshPorts. java/eclipse[EB/OL]. [2026-06-06]. <https://www.freshports.org/java/eclipse/>. 截至 2026 年，Port **java/eclipse** 已恢复活跃维护
- FreeBSD Forums. Are Linuxisms impossible to overcome when porting?[EB/OL]. [2026-06-07]. <https://forums.freebsd.org/threads/are-linuxisms-impossible-to-overcome-when-porting.45805/>.

#### FreeBSD 基金会重大捐赠事件

>上周，我向 FreeBSD 基金会捐赠了 100 万美元，FreeBSD 基金会支持着开源操作系统 FreeBSD。FreeBSD 帮助了数百万程序员追随他们的热情、实现创意。我自己就是受益者。在 90 年代末，我开始使用 FreeBSD，那时我经济拮据，住在政府提供的住房中。在某种程度上，FreeBSD 帮助我摆脱了贫困——我能进入 Yahoo!（雅虎）工作的重要原因是他们使用 FreeBSD，而这正是我首选的操作系统。多年后，当 Brian 和我开始创建 WhatsApp 时，我们依然使用 FreeBSD 来支撑我们的服务器运营，直到今天也是如此。
>
> 我发布这项捐赠的消息，是希望让更多人看到 FreeBSD 基金会所做的有益工作，并激励他人也能支持 FreeBSD。我们大家都会受益，如果 FreeBSD 能够继续为像我一样的人提供机会，帮助更多的移民子女脱贫，帮助更多的初创公司取得成功，甚至是具有变革性的成果。
>
> ——WhatsApp 原 CEO 及创始人 Jan Koum（FreeBSD Foundation. Updated! – FreeBSD Foundation Announces Generous Donation and Fundraising Milestone[EB/OL]. (2014-11-17)[2026-04-05]. <https://freebsdfoundation.org/blog/updated-freebsd-foundation-announces-generous-donation-and-fundraising-milestone/>.）

#### 诚实与可信

像 FreeBSD 这样在后台静默运行以至于鲜为用户所察觉的系统，堪称久经考验。如果每日不时出现蓝屏报错、内核恐慌（Kernel Panic）抑或“内部错误”、`You are in emergency mode`、`BusyBox (initramfs)`、`grub rescue>` 等，反而能提醒用户该系统的存在。

目前，部分将 Linux 用作专用设备操作系统，或基于其他 GPL 软件构建商业产品的公司，并未严格遵守 GPL 协议发布其修改后的代码。部分国内企业对 GPL 的含义认识不足，仅将“免费”视为唯一考量。那些为规避 GPL 强制开源规定而采取规避措施的企业产品，其合规性与技术可信度均存疑。抢注开源软件商标的现象亦不鲜见。相较而言，采用 FreeBSD 的公司在许可证合规方面更为规范、可靠，也切实推动了 BSD 代码的广泛复用。纵然有人认为 FreeBSD 已趋衰落，事实上，大量用户可能始终受益于 FreeBSD 技术的支撑。

##### 参考文献

- 王波. FreeBSD 在中国的未来[M]//王波. FreeBSD 使用大全. 第 2 版. 北京: 机械工业出版社, 2002: 前言. ISBN: 978-7-111-10286-1. 探讨了 FreeBSD 在中国的发展前景与应用前景。

## FreeBSD 当前的技术局限性

FreeBSD 具有诸多优势，但也面临着现实的挑战。

- 大型技术企业对 FreeBSD 支持不足，如 GitHub Actions 需通过第三方工具（如 `vmactions/freebsd-vm`）实现 CI/CD，NVIDIA CUDA 也未予支持，在 AI 与 LLM 时代存在滞后。
- FreeBSD 项目缺乏对欧洲和北美以外地区的关注与投入。
- 相比其他开源项目中“仁慈的终身独裁者”模式，集体领导在 FreeBSD 项目中并未显现出明显优势，有时甚至可能导致责任分散、效率低下的问题（即“集体行动困境”）。部分分管 FreeBSD 子项目的核心成员对项目本身的了解和关注尚有不足，面对若干问题亦难以有效决策和承担责任。
- FreeBSD 项目整体风格偏于保守，新技术的引入往往需要数年，跨越多个大版本方能完成。通常需等待已有技术轮替一到两代后才会引入；引入后亦往往缺乏后续关注与维护开发。
- FreeBSD 系统在部分方面尚欠现代化，缺少某些当代操作系统常见的特性。尤其是在嵌入式方面仍有较大提升空间。
- FreeBSD 未在基本系统中提供预配置的桌面环境。
- FreeBSD 的硬件驱动支持相对有限。
- 关于 FreeBSD 的学习资料相对较少。
- FreeBSD 的开发者数量较少，且对外部贡献者的反馈往往不及时。
- FreeBSD 基金会、期刊、Bug 报告系统等对外部贡献者的反馈也常有不及时的情况。
- FreeBSD 文档项目曾停滞多年，个人贡献者除季度报告外的提交事实上很难被接纳；src 和 Ports 项目也同样难以接纳新的个人贡献者。
- 尚未完全支持安全启动（Secure Boot），需通过手动签名 EFI 二进制文件实现。
- 对 TPM 的支持有限。
- 由于部分软件对 Linux 特有特性存在依赖（Linuxism），导致若干软件无法直接移植。
- FreeBSD 支持的两款主要文件系统 ZFS 与 UFS，其存储空间通常只能扩大，难以直接缩小（ZFS 自 FreeBSD 13.0 起可通过 `zpool remove` 移除镜像或非冗余顶级 vdev，但无法移除 raidz vdev，且需满足 `device_removal` 特性标志已启用的条件；UFS 则不支持缩小）
- FreeBSD 在面向最终用户的上层应用生态方面有所欠缺，虚拟化技术 bhyve 也有待改进。

### 参考文献

- FreeBSD Foundation. FreeBSD UEFI Secure Boot[EB/OL]. [2026-06-06]. <https://freebsdfoundation.org/freebsd-uefi-secure-boot/>.
- OpenZFS. zpool-remove(8)[EB/OL]. [2026-06-07]. <https://openzfs.github.io/openzfs-docs/man/v2.2/8/zpool-remove.8.html>. 可通过 zpool remove 移除镜像或非冗余顶级 vdev，但无法移除 raidz vdev

## 课后习题

1. 观察四周，分析你身边哪些产品是基于 FreeBSD 操作系统构建的。
