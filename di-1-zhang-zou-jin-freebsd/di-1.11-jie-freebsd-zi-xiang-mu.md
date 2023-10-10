# 第 1.11 节 FreeBSD 子项目

本页面是对 [Projects](https://freebsdfoundation.org/our-work/projects/) 的翻译。

**FreeBSD 项目完全依靠来自 FreeBSD 社区成员和关注我们使命的外部企业的慷慨捐赠及资助。**

本页面列出的项目是由捐赠给 FreeBSD 基金会的款项资助的。还有很多正在进行中的项目由志愿者、公司等为 FreeBSD 项目进行开发。要了解更多关于这些项目的信息，请访问 [FreeBSD 项目](https://freebsd.org/)的网站。

为了帮助资助将来的项目，请考虑向基金会进行[捐赠](https://freebsdfoundation.org/donate/)。

## 提交项目提案

FreeBSD 基金会正在征集与 FreeBSD 操作系统中的任何主要子系统或基础设施相关的工作提案。将根据其可行性、技术价值和成本效益对提案进行评估。

有关流程的简要概述，请参阅[项目提案概述](https://freebsdfoundation.org/project-proposal-overview/)。要获取详情，请参阅[提交指南](https://freebsdfoundation.org/wp-content/uploads/2017/06/FreeBSDProposalSubmission.pdf)。

## 文档和测试实习

<https://freebsdfoundation.org/project/documentation-and-testing-internship/>

**进行中**

2023 年 7 月，Yan-Hao Wang 开始了与基金会的暑期实习，即从事各种任务。以下是部分计划工作的列表：

- 构建在线手册编辑器
- 更新 FreeBSD jenkins-tinderbox
- 为 `/bin`、`/sbin`、`/usr/bin`、`/usr/sbin` 中的用户空间工具添加测试用例
- 调查并开发用于 FreeBSD 手册和文档的“专家系统”
- 修复 libxo 问题，并编写适用的测试用例
- 调查开发树莓派 4 和 IPV6 任务的路线图
- 针对 FreeBSD 手册和文档的“专家系统”将是一个尽力而为的概念验证任务，其中将包括将 FreeBSD 文档（如手册和手册）导入矢量数据库，以便像 ChatGPT 这样的大型语言模型在查询涉及 FreeBSD 的问题时可以“阅读”它们，从而提供更好的答案。

## 解决 OpenSSL 3 / LLVM 16 移植带来的问题

<https://freebsdfoundation.org/project/addressing-openssl-3-llvm-16-ports-fallout/>

**进行中**

随着 FreeBSD 在主分支中将 OpenSSL 更新到 3.0 版本，出现了许多需要修复的 Port 编译错误，这些错误必须在 FreeBSD 14.0 发布之前修复。大部分涉及 OpenSSL 3 和 LLVM 15 的关键问题已经得到解决，但是在 LLVM 16 中，大约有 800 个额外的 Port 无法编译，导致在完整的 Ports 编译中还有 2800 个相关的依赖的 Port 被跳过。Muhammad Moinur (Moin) Rahman 将完成这一耗时且繁琐的工作，解决与更新到 OpenSSL 3 和 LLVM 16 相关的所有  Port 问题。

## SIMD 增强的 libc

<https://freebsdfoundation.org/project/simd-enhanced-freebsd-libc-functions/>

**进行中**

在现代计算机架构中，提供了 SIMD（单指令多数据）指令集扩展，可以同时处理多个数据。这些指令常用于数值应用程序，如视频编解码器、图形渲染和科学计算，如同时使用 SIMD 技术还有助于基本的数据处理任务，例如由 libc 函数实现的任务。虽然其他的 libc 实现已经为标准 libc 函数提供了经过 SIMD 增强的变体，但 FreeBSD libc 在这方面尚有很大的提升空间。Robert Clausecker 对这个项目的目标是为相关的 libc 库函数提供这样的经过 SIMD 增强的版本，从而提高与其链接的软件性能。由于大多数适用于 FreeBSD 的软件都使用这些 libc 函数，因此这些增强预计将为广泛的程序带来显著的好处。该项目的主要关注点是 amd64 架构，旨在根据 x86_64 psAB 定义的架构级别，生成针对 SIMD 优化的实现。

如果特定例程可以受益于更高架构级别的额外指令，计划实现多个不同的例程。通常意味着一个基线例程或 x86-64-v2，以及分别针对 x86-64-v3 和 x86-64-v4 的例程。计划创建基准测试套件，以确定这些例程对 libc 性能的影响。在未来的工作中，如果有足够的兴趣，这些例程可能会被适配到 i386 架构，或者移植到其他架构，包括 arm64（ASIMD，SVE）和 ppc64/ppc64le。

在技术细节方面，计划采用汇编语言实现优化例程，以确保工具链无关。对于动态链接的可执行文件，计划使用 ifunc 机制，在运行时选择每个例程的最佳实现。如果可能，将查询一个环境变量，可让用户选择不同的架构级别，或者完全禁用 SIMD 增强。对于静态链接的可执行文件，或者直接调用函数（例如通过 libc 内部的隐藏别名），计划提供分发跳板。在第一次调用跳板时，调用将解析为一个分发函数，该函数确定要使用哪个实现。分发函数将分发目标写入分发函数指针，然后尾调用选定的例程。在下一次迭代中，将直接调用正确的函数。这两种机制都将以线程安全和异步信号安全的方式实现。通常情况下，最佳实现是使用 CPU 支持的最高架构级别。然而，硬件限制，如热许可和 AVX-SSE 过渡开销，可能会使架构级别 v3 和 v4 在某些处理器上变得不太吸引人。实现可能会被编写成在读取期间超出字符串末尾，但确保不会越过页面边界。这种超出边界在没有设置段限制的情况下是无害的，但可能会混淆诸如 valgrind 等分析工具。这在处理以 NUL 结尾的字符串时尤其需要。

关于文档方面，存在 SIMD 增强函数的信息将会在一个新的手册页 simd(7) 中进行记录。该页面将向用户解释 libc 如何选择要使用的实现，以及如何配置这种行为。其他手册页，如 environ(7)、string(3) 和 bstring(3)，将根据需要添加交叉引用和额外的信息来进行增强。将产生内部文档，解释分发和函数选择机制。由于不计划将这些机制提供给用户代码，因此不会产生面向最终用户的文档。根据需要，还可能会产生关于基准测试和测试设置的额外文档。还可能会产生最终报告，描述所使用的技术并提供最终的性能改进情况。

## Capsicum 实习

<https://freebsdfoundation.org/project/capsicum-internship/>

**进行中**

从 2023 年 6 月 1 日到 9 月 1 日，Jake Freeland 将与基金会一起进行实习，致力于开发 FreeBSD 的沙盒框架 Capsicum。Capsicum 被设计用来限制应用程序和库所具有的能力。Capsicum 模型简单且安全，但近年来在该框架周围的进展和发展已经减缓。Capsicum 的核心思想很直观，进入能力模式后，资源获取和外部通信都会受到严格限制。围绕这一原则设计程序相对容易，但问题在于，那些未设计为沙盒化的现有应用程序需要在这个环境中工作。很难确定哪些操作会引发 Capsicum 违规，并且不可能在请求或命名资源之前预先打开尚未被请求或命名的资源。此外，开发人员在实施 Capsicum 功能之前必须对程序非常熟悉。这些原因解释了为什么 Capsicum 化的努力正逐渐减少。

这个实习项目将涉及多个项目，总体目标是为希望将现有程序 Capsicum 化的开发人员提供更好的体验和便利。Capsicum 的最大障碍是其陡峭的学习曲线。重构程序以支持能力模式通常需要开发人员知道什么会导致 Capsicum 违规，并知道如何重构给定的程序以避免违规。有时这个过程很简单，但较大的程序通常需要按需获取资源，找到如何满足这些需求可能会很困难。扩展开发人员可用的工具数量，以方便进行程序的 Capsicum 化，将大大平缓上述的学习曲线。如果 Capsicum 化变得简单，那么更多的开发人员将会采用它。

### 项目

1. 跟踪 Capsicum 违规

在撰写本文时，需要修改程序以支持 Capsicum 需要开发人员手动解析他们的代码，找到 Capsicum 违规。拥有一个在运行时可以跟踪应用程序并找出违规发生位置的实用工具将会很方便。这个功能可以添加到 ktrace(1) 中作为一个选项标志。基本思路是钩子 ENOCAP 通常会返回的位置，记录该位置，并继续正常执行。David Chisnall 在 Differential revision <https://reviews.freebsd.org/D33248> 中提出的想法也可以通过信号通知的方式记录违规。

2. Capsicum 化 syslogd(8)

syslogd 守护进程负责读取和记录消息到系统控制台、日志文件和其他机器。记录是任何操作系统的重要且经常敏感的任务，因此应该自然地将 syslogd 与 Capsicum 进行沙盒化。使用 ktrace(1) 的 Capsicum 违规跟踪，将对 syslogd 进行重新架构，以使其在能力模式下运行。syslog.conf 配置文件负责为 syslogd 提供设备和程序，以及相应的日志文件位置。这个约定允许我们解析 syslog.conf 并确定 syslogd 正常运行所需的资源。不可能通过在执行开始时解析 syslog.conf 来沙盒化 syslogd。如果在任何时候收到 SIGHUP 信号，syslogd 将重新处理其配置，可能需要新的资源。为了解决这个问题，应将 syslogd 分为两个并发进程：一个处理日志记录，另一个监听 SIGHUP，读取配置文件，并在必要时将能力传递给另一个进程。

3. Capsicum 化 NFS 守护进程

NFS 套件由许多守护进程组成，包括 nfsd(8)、mountd(8)、rpcbind(8)、rpc.statd(8)、rpc.lockd(8) 和 rpc.tlsservd(8)。这个项目将重点放在 Capsicum 化 rpcbind 上。rpcbind 守护进程负责将 RPC 程序号转换为标准的通用 DARPA 地址。由于它通常由 root 运行，因此 rpcbind 是 Capsicum 化的理想候选对象，因为它常常成为利用的目标。在查看 `usr.sbin/rpcbind/rpcbind.c:152` 时，可以看到 rpcbind 正在限制自己至少使用 128 个资源，这表明它可能会请求按需打开任意文件。这是 Capsicum 化的一个突出难题，因为在能力模式内我们无法打开任意文件。我们可能需要使用类似于 libcasper(3) 的机制（或类似的机制），以在需要时将能力传递给 rpcbind。已经注意到了这些命名资源的请求：一个 rpc 锁文件、日志文件、netconfig 文件、用于线程唤醒的管道，rpcbind 套接字。毫无疑问还有更多。还可能会对其他 NFS 守护进程进行 Capsicum 化。

4. Capsicum 化 ggatec(8) 和 ggated(8)

GEOM Gate 网络工具提供了对存储设备的远程访问，并建立在 FreeBSD 的 GEOM 框架之上。与 NFS 类似，设备导出可以在 exports 文件 `/etc/gg.exports` 内进行管理。ggate 实用工具非常适合 Capsicum 化，因为它们以 root 身份运行，处理网络请求，并且在 CVE-2021-29630 中已经遭受远程代码执行。ggatec 客户端实用工具用于创建 ggate 设备并与 ggated 进行通信。Capsicum 化 ggatec 应该相对简单，因为远程主机和设备路径都在命令行参数中指定。在进入能力模式之前，应该进行简单的文件和套接字预打开。ggated 实用工具查看 `/etc/gg.exports`，或指定的备用 exports 文件，并从 ggatec 处理 GEOM Gate 请求。所有需要的资源都在命令行参数和 exports 文件中指定，因此在进入能力模式之前，预打开这些资源应该足够了。

5. Capsicum 化 tftpd(8)

tftpd 服务器实现了互联网微型文件传输协议（RFC 1350），以允许远程读取 tftpd 的参数中指定的文件。由于所需的资源在前面指定，tftpd 的 Capsicum 化应该包括简单的目录预打开。

6. Capsicum 化 ntpd(8)

与 syslogd(8) 和 rpcbind(8) 不同，ntpd 代码库似乎分为大约一百个大文件。根据手册页，这些文件都有命名，并且很容易预打开：配置文件、漂移文件、网络接口设备、密钥文件、日志文件、PID 文件和统计文件。假设不需要任何任意文件，Capsicum 化的过程应该相对平稳。

7. Capsicum 化 libarchive(3)

libarchive 库是专门用于压缩和解压缩多种流行的存档格式。已经注意到，为 iconv(3) 获取共享库会引发 Capsicum 违规。一个临时解决方案是在 unzip(1) 中预打开这些 iconv(3) 文件，但这实际上应该在 libarchive 中完成。libarchive 的目标是在能力模式下引入与存档无关的创建和提取。这可能通过在标准 API 旁边添加 Capsicum 特定的接口来实现。如果可行，下一步将是对 tar(1) 进行 Capsicum 化。由于大多数 tar 文件都会解压到当前目录，Capsicum 化的过程应该涉及打开当前目录文件描述符，并将所有文件系统资源获取调用更改为其 at() 派生版本。例如：open() 将被更改为 openat()。

8. 完成 SIGCAP 违规信号的实现

David Chisnall 在 Differential revision <https://reviews.freebsd.org/D33248> 中提出了一个可选的 SIGCAP 信号，可以在发生 Capsicum 违规时传递。不幸的是，这个 revision 没有完成，几个月没有进行更新了。完成这个 revision 并添加 SIGCAP 信号可以使那些使用违规信号来触发 Capsicum 违规的程序的调试更加容易。我们可以使用 SIGCAP 告诉代码转到备用路径，而不是等待 SIGTRAP，后者可能会被调试器拦截。此外，有一个明确的 Capsicum 违规信号将允许 Capsicum 违规跟踪工具记录特定于 Capsicum 的故障。例如，当设置 `kern.trap enotcap=1` 时，任何 Capsicum 违规都会引发一个带有程序终止的 SIGTRAP。这不透明，因为无法确定该程序终止是因为违规还是因为无关的 SIGTRAP 信号。将 kern.trap enotcap 改为传递 SIGCAP 将消除这种混淆。这个 SIGCAP 信号还可以为上述 ktrace(1) 中的追踪 Capsicum 违规引入一个替代方法。ktrace(1) 可以截获并记录 SIGCAP 调用，并使用适当的信号处理程序将原始程序送回执行。

## 无线网络实习

<https://freebsdfoundation.org/project/wireless-internship/>

**进行中**

2022 年谷歌代码之夏的贡献者 En-Wei Wu 于 2023 年初开始在 FreeBSD 基金会进行实习，致力于开发 FreeBSD 的无线驱动程序和工具。该工作分为三个部分。

- `wtap` 将通过添加对更多 802.11 物理层的支持来进行扩展，目前仅支持 802.11b。`wtap` 的其他工作将包括添加 WPA/WPA2/WPA3 支持，以便可以测试 `wpa_supplicant(8)` 和 `hostapd(8)`。
- 将在 `hostapd(8)` 中添加对 WPA2 预验证的支持。WPA2 是 IEEE 802.11i 规范的一部分，用于认证无线站点以访问接入点。该协议的一部分是能够与一个或多个接入点预先验证一个站点，以便快速进行漫游。FreeBSD 在用于构建支持 WPA 的接入点的 `hostapd` 程序中缺乏对协议的此方面的支持。这项任务将移植现有的 Linux 代码，以支持 `hostapd` 中的预验证。这主要涉及重写一些用户模式的组播代码并测试结果。应将对 FreeBSD 之外托管的第三方源代码的修改在适用时上游到适当的项目中。
- 将完成对 802.11 驱动程序的工作。`ath10k` 驱动程序将通过完成 Adrian Chadd 已开始的驱动程序工作进行移植。此外，还将通过帮助开发和测试诸如 `rtw88` 和 `rtw89` 等 Realtek 驱动程序，为 Bjoern Zeeb 提供协助。

## 增强持续集成

<https://freebsdfoundation.org/project/continuous-integration-enhancements/>

**进行中**

FreeBSD 的持续集成（CI）基础设施基于 Jenkins。每当开发人员向 FreeBSD 源代码存储库推送提交时，就会运行一个作业。现希望在预提交环境中为开发人员提供更多便利。当 CI 运行中出现问题时，解决这些问题可能会很困难。此外，希望拥有私有的 FreeBSD 运行程序，供流行的 Git 托管服务使用，以为推送到私有分支的人创建 CI 基础设施。为此，Muhammad Moinur Rahman 的目标是将由 Li-Wen Hsu 编写的 CI 脚本作为构建系统的一部分提供给开发人员。与 `make universe` 或 `make tinderbox` 为所有支持的架构构建类似，`make ci` 将为所有支持的构建执行类似的操作。另一个目标是在调试问题时，使开发人员能够运行单个 CI 作业。希望这种灵活性也能让其他人将这些构建/脚本集成到其他 CI 工具（如从 Github 运行的 Cirrus CI）中。

## FreeBSD 作为一级的 cloud-init 平台

<https://freebsdfoundation.org/project/freebsd-as-a-tier-i-cloud-init-platform/>

**进行中**

cloud-init 是在云中配置服务器的标准方式。不幸的是，除了 Linux 以外的操作系统对 cloud-init 的支持相当有限，而且 FreeBSD 上缺乏支持 cloud-init 成为希望将 FreeBSD 作为一级平台的云提供商的障碍。为了解决这个问题，FreeBSD 基金会已经委托 Mina Galić，以将 FreeBSD 的 cloud-init 支持与 Linux 支持保持一致。项目交付内容包括完成特定网络类的提取，实现`ifconfig(8)`和`login.conf(5)`解析器，实现`IPv6`配置，为 Azure 创建`devd`规则，并编写关于将 FreeBSD 投入生产的 Handbook 文档。

### 背景

cloud-init 最初是一个 Linux 项目，对于除 Linux 以外的 BSD 操作系统的支持是后来添加的。当试图扩展 cloud-init 以更好地与 FreeBSD 配合时，发现即使是不同 Linux 发行版之间的支持也很差。从这个问题诞生了一个重构项目，将网络功能提取到 cloud-init 的发行版类中。该项目最初由 Mina 提出和推动，但 cloud-init 的维护人员和贡献者仍未完成。原因是对于 Linux 来说，当前的设计已经足够好了。然而，为了改善对 FreeBSD 和其他 BSD 的网络支持，这将是第一个重要的步骤。

### 网络重构

cloud-init 重构的一个问题是辅助函数在 Linux 上访问`/sys`。在 BSD 上的等效操作是解析`ifconfig(8)`，然而结果会更高级一些。这将使得一些较为容易的优化机会得以整理，同时也可以对解析器进行验证。这项工作包括为 BSD 实现`ifconfig(8)`解析器，并对`is_bond`、`is_bridge`、`is_physical`、`is_up`、`is_vlan`、`get_interfaces`、`get_interface_mac`、`get_interfaces_by_mac`和`interface_has_own_mac`进行重构。在网络更新之后，还需要重构`EphemeralIPv4Network`、`EphemeralIPv6Network`和`EphemeralDHCPv4`类。最后的网络步骤将是将网络渲染器与启动/关闭分离，实现`BSDRenderer.start_services`，为 FreeBSD 实现`IPv6`和`WiFi`配置。

### 文档

将编写支持性文档，以链接各种 cloud-init 阶段与`rc.conf`、`rc.local`以及类似的启动阶段，以及涵盖 FreeBSD 特定信息，包括在哪里以及如何自动安装软件包，运行`freebsd-update`，执行安装后步骤等。还将编写 FreeBSD Handbook 文档，描述如何将 FreeBSD 投入生产。

### 验证

将进行特定于云提供商的验证工作，包括将`pycloudlib`引入其他操作系统及其默认设置，为 Azure 创建`devd`规则，以及审查现有的 GCP/Azure/AWS 等云提供商配置是否有更改。

### 未来工作

一些未来工作的想法包括为`ifconfig(8)`和类似工具实现`libxo(3)`，以及为 cloud-init 实现 UCL 解析器。

## 在 FreeBSD 上运行的 OpenStack

<https://freebsdfoundation.org/project/openstack-on-freebsd/>

**进行中**

OpenStack 是一个开源的云操作系统，用于管理各种资源，包括虚拟机、容器和裸金属服务器。然而，OpenStack 的控制平面主要针对 Linux。FreeBSD 只在非官方上支持作为客户操作系统。用户可以在开放的云平台上创建 FreeBSD 实例，但目前管理员或操作员无法在 FreeBSD 主机上设置运行 OpenStack 的部署。鉴于云部署的日益重要以及 OpenStack 在各种云提供商中的受欢迎程度，FreeBSD 基金会已经委托 Chin-Hsin Chang 来移植 OpenStack 组件，以便在 FreeBSD 主机上运行 OpenStack。

该项目的主要目标是将基于 Linux 的 OpenStack 组件移植到 FreeBSD/amd64 平台。这些组件包括但不限于：

- Keystone（身份和服务目录）
- Ironic（裸金属服务器供应）
- Nova（实例生命周期管理）
- Neutron（覆盖网络管理）

这些组件将被添加到 FreeBSD 的 ports 树中，并在 FreeBSD Handbook 和维基上进行记录，工作将在 FreeBSD Journal 文章中进行描述。

该工作还将涉及构建三个基于 FreeBSD 的 OpenStack 集群。第一个集群将用于剑桥大学的 CHERI 团队，用于管理 CHERI 启用的 Morello 开发板，并协调开发人员的访问请求。第二个和第三个集群将部署在主要的 FreeBSD.org 集群中。第二个集群将转换为 netperf 集群的资源管理系统。第三个集群将作为不同开发分支和架构的参考机器的迷你云进行构建。第三个集群将使开发人员能够生成他们可以完全控制的虚拟机，以满足其移植或系统开发的需求。这些 OpenStack 部署都将通过 OpenStack Tempest 和 Rally 进行测试，以确保正确性。

### 详细信息

该项目将包括三个阶段。第一阶段包括在 amd64 FreeBSD 主机上将关键的 OpenStack 组件作为集群控制平面运行起来。这将涉及将 OpenStack 作为 CHERI 启用的 Morello 开发板的生命周期管理器。将基于 Linux 的关键组件 Identity、Keystone 和 Ironic 移植到 FreeBSD。尽管可以将 Ironic 设置为独立服务，也就是说，不需要由 Keystone 提供的服务目录和集成认证，但在这个阶段最好是同时移植 Keystone 和 Ironic。Ironic 使用 BMC（基板管理控制器）来实现带外控制。存在许多现有的协议和解决方案，如 IPMI、Redfish、Dell iDRAC 和 HPE iLO。然而，Morello 开发板不带有 BMC。为了使 Ironic 能够管理这些 ARM 开发板，可能需要开发并测试特定的 Ironic 驱动程序，以成功执行供应、管理和清理任务。

netperf 集群提供了各种规格的机器，让开发人员进行网络功能和性能测试。目前，该集群可按需提供，并由集群管理团队管理机器。尽管它具有一定的自动化能力，通过 PXE、IPMI 和各种脚本进行供应和回收，但如果有一个完整的系统，配有仪表板，可以在硬件库存、资源管理和分配方面照顾集群，将会更好。在第二阶段开始之前，将构建一个 netperf 集群。CHERI 集群和 netperf 集群之间的主要区别在于受管理的硬件。CHERI 集群是 arm64 的，netperf 集群将是基于 amd64 的硬件，具有用于带外控制的 BMC。集群之间的 BMC 差异可能需要一些额外的工作。

第二阶段将涉及设置一个迷你 OpenStack 集群，以在 FreeBSD.org 集群中管理多台裸金属服务器和虚拟机。在主要的 FreeBSD.org 集群中使用迷你 OpenStack 集群具有以下优势：

- 向集群用户提供自助服务
- 提高物理和虚拟资源的生命周期管理效率
- 保证服务器的网络连接性
- 分配 root 权限更简单，风险得到减轻

为了将这些功能带到 FreeBSD.org 集群中，其他关键的 OpenStack 组件必须移植到 FreeBSD，包括实例生命周期管理服务和覆盖网络服务。

在第三阶段，将实现更一般的集群设置，具有用户感知的网络，即网络隔离。将移植至少一个 Neutron ML2 模块化第 2 层驱动程序，以提供这种功能。与 OpenStack SIG（特殊兴趣小组）

进行合作，工作将被贡献回上游项目。另一个目标是在这些项目中建立一个 FreeBSD 版本测试流水线。

## 使用日志软更新在文件系统上创建快照

<https://freebsdfoundation.org/project/snapshots-on-filesystems-using-journaled-soft-updates/>

**进行中**

UFS/FFS 文件系统具备创建快照的能力。因为创建快照的能力是在软更新被编写之后添加的，所以它们与软更新完全集成在一起。然而，当日志式软更新于 2010 年被引入时，它们从未与快照集成。因此，在运行日志式软更新的文件系统上无法使用快照。

在支持 ZFS 添加到 FreeBSD 之后，快照变得不再重要。ZFS 可以快速轻松地创建快照。然而，仍然有两种情况，让 UFS 快照很重要。首先，它们允许对活动文件系统进行可靠的转储，从而避免可能的长时间停机。其次，它们允许运行后台 fsck。与 ZFS 中需要 Scrub 类似，fsck 需要定期运行以查找未检测到的磁盘故障。快照允许在活动文件系统上运行 fsck，而无需安排停机时间。

在与开发者社区进行磋商后，FreeBSD 基金会的工作人员认为此类基础设施工作将产生积极影响。因此，基金会开始资助 Marshall Kirk McKusick 进行必要的更改，以允许使用日志式软更新的 UFS/FFS 文件系统创建快照。这项工作需要对 UFS/FFS 软更新和快照内核代码进行广泛的更改，以及对 fsck_ffs 实用程序进行更改。

该项目预计将于 2023 年中旬完成，工作将分为两个里程碑。在里程碑 1 之后，当使用日志式软更新时，将启用快照，并且可以在活动文件系统上执行后台转储。里程碑 2 涉及扩展 fsck_ffs，使其能够在运行日志式软更新的文件系统上使用快照进行后台检查。每个里程碑被认为已完成，当代码通过审核流程并已提交到源码的主分支。

## WiFi 更新——Intel 驱动和 802.11ac

<https://freebsdfoundation.org/project/wifi-update-intel-drivers-and-802-11ac/>

**进行中**

为了跟上新的标准和设备，FreeBSD WiFi 堆栈需要持续的维护和开发。基金会正在资助 Bjoern Zeeb 通过迁移到 Linux 内核中的双许可上游驱动程序，来把当前一代的 Intel WiFi 设备集成到 FreeBSD 中。

我们还将与 FreeBSD WiFi 开发社区合作，集成 802.11ac 基础设施支持。

## ZFS“RAID-Z 扩展”功能的开发

<https://freebsdfoundation.org/project/development-of-the-raid-z-expansion-feature-for-zfs/>

**进行中**

Zettabyte 文件系统（ZFS）是一种集成了文件系统和逻辑卷管理器的设计，旨在防止数据损坏并支持高存储容量。

基金会正在资助 Matthew Ahrens 开发“RAID-Z 扩展”功能。这将允许向现有的 RAID-Z 组中添加额外的磁盘，例如允许将由 4 个磁盘组成的 RAID-Z1 组扩展为 5 个磁盘的 RAID-Z1 组。

实现这一目标的方法是“重新排列”所有现有数据，将其重新编写到新的磁盘排列中，从而在逻辑 RAID-Z 组的末尾（以及每个物理磁盘的末尾）留出一个新的连续的空闲空间块。重新排列后的数据仍将保持原始的逻辑条带宽度，即数据到奇偶校验的比率将保持不变，而新写入的数据将使用新的逻辑条带宽度，具有改进的数据到奇偶校验比率。重新排列在在线状态下进行，同时还可以执行其他 zfs 和 zpool 操作。

该项目目前正在进行中。

