# 第 1.13 节 FreeBSD 季度报告

旧的存档可以在这里找到：<https://freebsd.gitbook.io/freebsd-relnotes-cn/>

## FreeBSD 2023 年第二季度 季度状况报告

这是第二份 2023 年状态报告，共有 37 个条目。

正如您可能注意到的，我们比上个季度有更多的报告。这是个好消息，也显示了 FreeBSD 社区的活跃程度，我们一直在努力提供高质量的软件。

特别需要注意的是，夏季已经开始了，请不要错过由我们的谷歌代码之夏学生分享的令人惊叹的项目。

祝您阅读愉快。

Lorenzo Salvadore，代表 Status 团队。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

* FreeBSD 团队报告
  * FreeBSD 核心团队
  * FreeBSD 基金会
  * FreeBSD 发布工程团队
  * 集群管理团队
  * 持续集成
  * Ports
* 项目
  * Cirrus-CI
  * FreeBSD 内核中的 BATMAN 支持
  * LinuxBoot 上的 FreeBSD 支持
* 用户空间
  * 基于 OpenSSL 3 的更新
  * Linux 兼容层更新
  * 服务 Jail-自动将 rc.d 服务置于监狱中
  * 使用 ktrace(1)进行安全隔离
  * NVMe over Fabrics
* 内核
  * 启动性能改进
  * 引导加载程序的 CI 测试工具
  * FreeBSD 内核的物理内存压缩
  * 增加 MAXCPU
  * FreeBSD 内核的 SquashFS 移植
  * Pf 改进
  * 网络接口 API（IfAPI）
  * 使 Netgraph 无锁化
* 架构
  * AMD64 的 SIMD 增强
  * 将 mfsBSD 集成到发布构建工具中
* 云计算
  * FreeBSD 作为 Tier 1 的 cloud-init 平台
  * FreeBSD 上的 OpenStack
  * FreeBSD 在 Microsoft HyperV 和 Azure 上
  * FreeBSD 在 EC2 上
* 文档
  * 文档工程团队
* ports
  * FreeBSD 上的 KDE
  * FreeBSD 上的 GCC
  * Puppet
  * FreeBSD 上的 MITRE Caldera
  * FreeBSD 上的 Wazuh
* 第三方项目
  * PkgBase.live
  * 容器和 FreeBSD：Pot，Potluck 和 Potman

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### FreeBSD 团队报告

以下是来自各个官方和半官方团队的条目，这些信息可以在[管理页面](https://www.freebsd.org/administration/)找到。

#### FreeBSD 核心团队

联系方式：FreeBSD 核心团队 [core@FreeBSD.org](mailto:core@FreeBSD.org)

FreeBSD 核心团队是 FreeBSD 的管理机构。

**202305 开发者峰会**

核心团队在 2023 年 5 月 17 日至 18 日的 FreeBSD 开发者峰会上进行了状态更新的展示。可在[https://wiki.freebsd.org/DevSummit/202305](https://wiki.freebsd.org/DevSummit/202305) 上查看幻灯片。

**FreeBSD 14**

核心团队正在与其他团队合作，以确保 FreeBSD 14.0-RELEASE 具有最高的质量。

核心团队对将 riscv64sf（64 位 RISC-V 软浮点）标记为在 14 版本中再不支持表示认可。

**与 FreeBSD 基金会的会议**

核心团队将与 FreeBSD 基金会继续定期举行会议，讨论 FreeBSD 的管理、开发和未来发展的下一步计划。核心团队与基金会的董事会成员和雇员进行了两次会议。他们讨论了基金会如何帮助核心团队和整个项目。

**Matrix 即时通讯解决方案**

核心团队在 202305 开发者峰会的进行中，提出了一个新的项目通讯解决方案。

目前，由 clusteradm 在 matrix-dev.FreeBSD.org 上设置了一个测试实例。所有开发者都可以使用自己的 Kerberos 凭证访问该实例，并可以通过 Matrix 的联邦功能加入一些公共聊天室。请注意，该实例仅用于测试和评估，因此不保证备份或可用性。

核心团队仍在讨论此服务的范围和管理方式，并收集社区的反馈意见。

**行为准则委员会**

行为准则委员会（conduct@）现在由核心团队负责管理。

**提交权限**

核心团队批准了 Christos Margiolis (christos@)的 src 提交权限。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 基金会

链接：

FreeBSD 基金会网址：[https://www.freebsdfoundation.org](https://www.freebsdfoundation.org)

技术路线图网址：[https://freebsdfoundation.org/blog/technology-roadmap/](https://freebsdfoundation.org/blog/technology-roadmap/)

捐赠网址：[https://www.freebsdfoundation.org/donate/](https://www.freebsdfoundation.org/donate/)

基金会合作计划网址：[https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/)

FreeBSD 杂志网址：[https://www.freebsdfoundation.org/journal/](https://www.freebsdfoundation.org/journal/)

基金会新闻和活动网址：[https://www.freebsdfoundation.org/news-and-events/](https://www.freebsdfoundation.org/news-and-events/)

联系人：Deb Goodkin [deb@FreeBSDFoundation.org](mailto:deb@FreeBSDFoundation.org)

FreeBSD 基金会是一个 501(c)(3) 非营利组织，致力于在全球支持和推广 FreeBSD 项目和社区。个人和公司的捐赠用于资助和管理软件开发项目、会议和开发者峰会。我们还为 FreeBSD 贡献者提供差旅补助，购买和支持硬件以改善和维护 FreeBSD 基础设施，并提供资源来改进安全性、质量保证和发布工程工作。我们发布营销材料以推广、教育和支持 FreeBSD 项目，促进商业供应商和 FreeBSD 开发者之间的合作，并最终代表 FreeBSD 项目执行合同、许可协议和其他需要被认可的法律安排。

**祝 FreeBSD 30 岁生日快乐！**

我们自豪地支撑这个出色的操作系统和充满活力的社区已经超过 23 年了，并且我们热切期待在未来的多年里继续支持它们。在本次报告中，我们将概述我们在多个领域对 FreeBSD 的贡献。我们将涉及一些具有详细报告的项目开发倡议。此外，我们还将展示我们对 FreeBSD 的支持、促进社区参与的努力以及扩大合作伙伴关系的努力。最后，我们将深入探讨我们持续增加资金的工作，以便在项目中填补更多的差距。

**筹款**

在这个季度，我们在与 FreeBSD 商业用户进行合作方面取得了重大进展。为了加强与现有和潜在商业用户的合作伙伴关系，我们聘请了 Greg Wallace 担任合作伙伴和研究总监。他的主要目标是扩大我们与商业用户的合作。自担任该职务以来，Greg 已经开始着手工作，仅在一个季度内就与众多公司进行了会面。这些互动为我们了解 FreeBSD 的使用情况、用户面临的挑战以及项目可以改进的领域提供了宝贵的见解。通过了解这些方面，我们可以做出明智的决策，确定在哪些方面投入资金，并认识到 FreeBSD 的独特优势。此外，这个角色还包括进行研究，以确定目标市场，探索 FreeBSD 的新机会，并确保我们的声音在相关讨论中得到听取。有关 Greg 的目标和成就的更多详细信息，请参阅他下面的状态更新。

基金会向所有对我们的工作作出财务捐赠的人表示衷心的感谢。除了许多个人捐赠外，我们还很高兴收到 NetApp 和 Blackberry 的较大捐赠。此外，我们还从 Tarsnap、iXsystems 和 LPI 获得了 FreeBSD 开发者峰会的赞助。这些赞助在抵消我们的费用方面提供了极大的帮助，并使我们能够向参与者提供实惠的注册费用。

今年我们的预算约为 2,230,000 美元，其中包括增加用于 FreeBSD 推广和软件开发的支出。我们预算的一半以上用于直接改进 FreeBSD 并保持其安全性。

通过有一个专门负责合作伙伴关系的人，我们可以有效地强调投资我们的努力的重要性，并强调项目的长期可行性。

您的支持在我们的使命中发挥着至关重要的作用，我们深表对您对 FreeBSD 社区的承诺表示感谢。请考虑向我们的 2023 年筹款活动捐款！[https://www.freebsdfoundation.org/donate/](https://www.freebsdfoundation.org/donate/)

对于更重要的商业捐赠者，我们还有 [FreeBSD 基金会合作计划](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/)，该计划成立于 2017 年。

**合作计划**

大家好，我是 Greg Wallace。我于四月初加入基金会，担任合作伙伴关系和研究总监。[这篇博客介绍了我和我的角色](https://freebsdfoundation.org/blog/freebsd-foundation-welcomes-new-team-members/)。对于合作伙伴关系，我的重点是与使用 FreeBSD 的公司建立联系。我已经与几家公司会面，了解他们如何使用 FreeBSD。其中一些会面已经引发了有关潜在合作伙伴关系的讨论。我继续了解使用 FreeBSD 的有趣公司，并与他们取得联系。

我的目标是与每一家使用和构建 FreeBSD 的公司取得联系，倾听他们的故事。如果您是其中之一，而我们尚未建立联系，请在我的[日历](https://calendly.com/greg-freebsdfound/30min)上安排一次会话。

本季度其他合作伙伴关系相关活动：

* 我创建了关于如何与基金会合作推进 FreeBSD 的[幻灯片](https://docs.google.com/presentation/d/1tDCpbfxbqIucmJF6H15vK-ETrQsCMOVtxoqLem\_V0Z0/edit?usp=sharing)。如果您对如何改进这些幻灯片有任何想法，或者希望我向您的组织介绍这些内容，请给我发送[电子邮件](../di-0-zhang-freebsd-zhong-wen-she-qu/greg@freebsdfoundation.org)或[安排通话](https://calendly.com/greg-freebsdfound/30min)。并且请随意自由地分享这份演示文稿，无论全部还是部分内容。
* 我与基金会的同事合作，为向行业分析师进行演示准备了许多特定行业的用例幻灯片。
* 我还在寻求与以下机构的资助机会：
  * NSF 安全可信的网络空间（SaTC）
  * Sovereign Tech 基金
  * NGI。

在研究方面，我的广泛目标是确保这个社区的所有专业知识都能在全球关于计算性能、安全性和能源效率的对话中得到体现。作为一个社区，我们在这项工作中有很多贡献可以提供。

到目前为止，我一直在跟踪和参与以下主题：

* [Open Forum Europe](https://openforumeurope.org/open-source/)
* [CHIPS 研究与开发](https://www.nist.gov/chips/research-and-development-program)。

如果您对研究方面有想法，或者对在这个领域合作感兴趣，请[给我发送电子邮件](../di-0-zhang-freebsd-zhong-wen-she-qu/greg@freebsdfoundation.org)或[安排通话](https://calendly.com/greg-freebsdfound/30min)。

**操作系统改进**

在 2023 年第二季度，共有 339 个 src 提交，155 个 ports 提交和 20 个文档提交被认定为由 FreeBSD 基金会赞助。关于一些由基金会赞助的工作以及其他工作的描述在单独的报告条目中：

* 持续集成
* FreeBSD 作为 Tier 1 的 cloud-init 平台
* 基于 OpenSSL 3 的更新
* FreeBSD 上的 OpenStack
* 使用 ktrace(1)进行安全隔离
* AMD64 的 SIMD 增强

以下是其他由基金会赞助的工作的一部分：

* fsck\_ffs(8)的错误修复
* killpg(2)的错误修复
* hwpmc 的改进
* vmm 的改进
* 针对 LLVM 16 和 OpenSSL 3.0 的 port 修复和解决方案
* 将 kinst 移植到 RISC-V 以及相关的 DTrace 工作
* 将 libfido2 更新到 1.9.0 版本
* 各种 LinuxKPI 802.11 的改进
* 各种 RISC-V 的改进
* 从版本 4.9.3 升级到版本 4.99.4 的 tcpdump 的供应商导入和更新。

关于当前和过去由基金会承包的工作的状态，可以在[基金会项目页面上](https://freebsdfoundation.org/our-work/projects/)查看。

基金会技术团队的成员在加拿大渥太华举行的开发者峰会上进行了演讲。这包括主持谷歌代码之夏、[FreeBSD 基金会技术审查](https://wiki.freebsd.org/DevSummit/202305?action=AttachFile\&do=view\&target=FreeBSD\_Foundation\_Devsummit\_Spring\_2023\_Day\_2\_part1.pdf)和[工作流](https://docs.google.com/presentation/d/e/2PACX-1vSnEW5Z0ttQOAeqEEY8KHkfiRGeFUm4i8XrYsfY8TNYD%E2%80%94%E2%80%8Byx1P6MUu2\_u-mCcpe6PMMITjeDIgT31CC/pub)工作组会议。Pierre Pronchery 谈到了 [BSD 之间的驱动程序兼容性](https://www.bsdcan.org/events/bsdcan\_2023/schedule/speaker/89-pierre-pronchery/)问题，而 En-Wei Wu 则讨论了在与基金会签订的合同下完成的 [wtap 工作](https://www.bsdcan.org/events/bsdcan\_2023/schedule/session/139-add-operating-modes-to-wtap4/)。

**持续集成和质量保证**

基金会提供了全职员工和资金，用于改进 FreeBSD 项目的持续集成、自动化测试和整体质量保证工作。您可以在专用的报告条目中了解更多关于持续集成工作的内容。

**宣传**

我们的很多工作都致力于推广 FreeBSD 项目。这可能涉及突出显示有趣的 FreeBSD 工作、制作文献和视频教程、参加活动或进行演讲。我们制作的文献的目标是教授人们 FreeBSD 的基础知识，并帮助他们更轻松地采用或贡献。除了参加和演讲活动外，我们鼓励并帮助社区成员举办自己的 FreeBSD 活动、进行演讲或管理 FreeBSD 展台。

FreeBSD 基金会赞助全球范围内的许多会议、活动和峰会。这些活动可能与 BSD 相关，也可能是面向弱势群体的开源或技术活动。我们支持以 FreeBSD 为重点的活动，以便为知识分享、项目合作和开发者与商业用户之间的合作提供场所。这些都有助于提供一个健康的生态系统。我们支持非 FreeBSD 活动，以促进和提高 FreeBSD 的认知度，增加在不同应用中使用 FreeBSD 的程度，并吸引更多的项目贡献者。我们很高兴恢复了大多数以亲自参加活动。除了参加和计划活动外，我们还在不断努力推进新的培训计划，并更新我们的[指南](https://freebsdfoundation.org/freebsd-project/resources/)，以鼓励更多的人尝试 FreeBSD。

以下是我们进行的一些宣传和教育工作：

* 协助组织并参加了于 2023 年 5 月 17 日至 18 日在加拿大安大略省渥太华举行的[开发者峰会](https://wiki.freebsd.org/DevSummit/202305)
* 在于 2023 年 5 月 17 日至 20 日在加拿大安大略省渥太华举行的 BSDCan 活动中，主持了一个展台，并担任 Tote Bag 赞助商
  * 可以在[博客](https://freebsdfoundation.org/our-work/latest-updates/)上找到相关行程报告
* 在 BSDCan 庆祝了项目的 [30 周岁生日](https://freebsdfoundation.org/past-issues/freebsd-30th-anniversary-special-edition/)，并提供了特别版本的 FreeBSD 杂志的印刷本
* 成功争取到于 2023 年 7 月 13 日至 16 日在美国俄勒冈州波特兰举行的 [FOSSY](https://sfconservancy.org/fossy/) 上举办 FreeBSD 研讨会和演讲
* 成功争取到于 2023 年 9 月 14 日至 17 日在葡萄牙科英布拉举办的 [EuroBSDCon 2023](https://2023.eurobsdcon.org/) 的银牌赞助
* 成功争取到于 2023 年 10 月 15 日至 17 日在美国北卡罗来纳州罗利举办的 [All Things Open](https://2023.allthingsopen.org/) 的展位
* 开始筹划 FreeBSD 秋季供应商峰会
* 欢迎两名[新团队成员](https://freebsdfoundation.org/blog/freebsd-foundation-welcomes-new-team-members/)：Greg Wallace 和 Pierre Pronchery
* 发布了[四月](https://freebsdfoundation.org/news-and-events/newsletter/freebsd-foundation-update-april-2023/)和[六月](https://freebsdfoundation.org/news-and-events/newsletter/12518/)的新闻通讯
* 在 6 月 19 日庆祝了 [FreeBSD 日](https://freebsdfoundation.org/national-freebsd-day/)和项目的 30 周年，并在整个周内发布了特别的视频和博客文章
* 其他博客文章：
  * [EuroBSDcon 2023 旅行津贴申请现已开放](https://freebsdfoundation.org/blog/eurobsdcon-2023-travel-grant-application-now-open/)-请注意：申请将于 2023 年 8 月 2 日截止
  * [AsiaBSDcon 行程报告](https://freebsdfoundation.org/blog/asiabsdcon-2023-trip-report/)
* FreeBSD 在新闻中：
  * [InfoWorld：FreeBSD 30 岁生日快乐！](https://freebsdfoundation.org/news-and-events/latest-news/infoworld-happy-30th-freebsd/)

我们通过发布专业制作的 FreeBSD 杂志来丰富全世界关于 FreeBSD 的知识。正如我们之前提到的，FreeBSD 杂志现在是免费发布的。您可以在[https://www.freebsdfoundation.org/journal/](https://www.freebsdfoundation.org/journal/) 了解更多信息并访问最新的期刊。

您可以在 [https://www.FreeBSDfoundation.org/news-and-events/](https://www.freebsdfoundation.org/news-and-events/) 了解有关我们参加的活动和即将举行的活动的更多信息。

**法律/FreeBSD 知识产权**

基金会拥有 FreeBSD 商标，并有责任保护它们。我们还为核心团队提供法律支持，以调查涉及的问题。

您可以在 [https://www.freebsdfoundation.org](https://www.freebsdfoundation.org) 找到更多关于我们如何支持FreeBSD以及我们如何帮助您的信息！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 发布工程团队

链接：

FreeBSD 13.2-RELEASE 日程网址：[https://www.freebsd.org/releases/13.2R/schedule/](https://www.freebsd.org/releases/13.2R/schedule/)

FreeBSD 14.0-RELEASE 日程网址：[https://www.freebsd.org/releases/14.0R/schedule/](https://www.freebsd.org/releases/14.0R/schedule/)

FreeBSD 发行版本网址：[https://download.freebsd.org/releases/ISO-IMAGES/](https://download.freebsd.org/releases/ISO-IMAGES/)

FreeBSD 开发快照网址：[https://download.freebsd.org/snapshots/ISO-IMAGES/](https://download.freebsd.org/snapshots/ISO-IMAGES/)

联系人：FreeBSD 发布工程团队 [re@FreeBSD.org](mailto:re@FreeBSD.org)

FreeBSD 发布工程团队负责制定和发布 FreeBSD 官方项目版本的发布计划，宣布代码冻结并维护相应的分支，等等。

在 2023 年第二季度，团队继续进行了 13.2-RELEASE 的工作。13.2 周期紧密遵循了设定的日程安排，在最后增加了三个额外的 RC 构建，在 4 月中旬发布了最终的 RELEASE 构建并进行了宣布。

与项目管理中的各个团队协调，FreeBSD 发布工程团队重新考虑了即将到来的 14.0-RELEASE 的原始计划，主要是因为有进行中的工作。更新后的计划经过讨论并稍作调整以考虑一些问题，并最终在 FreeBSD 项目网站上发布。新的计划将 14.0-RELEASE 定于 2023 年 10 月。

团队继续为 `main` 分支、`stable/13` 分支和 `stable/12` 分支提供每周开发快照构建。请注意，`stable/12` 分支将不再提供快照构建。

赞助者：Tarsnap 赞助者：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 集群管理团队

链接：

FreeBSD 集群管理团队成员网址：[https://www.freebsd.org/administration/#t-clusteradm](https://www.freebsd.org/administration/#t-clusteradm)

联系人：FreeBSD 集群管理团队 clusteradm@FreeBSD.org

FreeBSD 集群管理团队负责管理项目依赖的机器，用于同步分布式工作和通信。

在本季度，该团队完成了以下工作：

* 为 FreeBSD.org 用户帐户提供定期支持。
* 为所有物理主机和镜像提供定期磁盘和零件支持（和更换）。
* 在 FreeBSD 项目管理的镜像中启用了 [https://www.FreeBSD.org](https://www.freebsd.org) 和 [https://docs.FreeBSD.org](https://docs.freebsd.org) 的镜像。
* 对所有主机和容器进行了集群更新新，将它们升级到最新版本的 14-CURRENT、13-STABLE 和 12-STABLE。

**正在进行的工作：**

* 主要站点进行大规模网络升级。
  * 在主要站点，新的 [Juniper](https://www.juniper.net/) 交换机已经到货，以替换以前的交换机。我们感谢 Juniper 的捐赠。
* 在主要站点和一些镜像站点上替换旧服务器。
  * 除了损坏的持续集成服务器，我们还有一些老旧的服务器，有磁盘损坏和故障的电源供应器。这项任务是与 FreeBSD 基金会以及捐赠者/赞助商一起进行的。
* 安装从软件包构建机转用的新持续集成（CI）机器。
* 审查在 FreeBSD 集群运行的服务的备份配置。

**FreeBSD 官方镜像概述**

当前的镜像位置是澳大利亚、巴西、德国、日本（两个完整的镜像站点）、马来西亚、南非、台湾、英国（完整的镜像站点）、美国加利福尼亚州、新泽西州（主要站点）和华盛顿州。

这些硬件和网络连接是由以下机构慷慨提供的：

* [Bytemark Hosting](https://www.bytemark.co.uk/)
* [BroadBand Tower](https://www.bbtower.co.jp/en/corporate/)，Inc 的云和 SDN 实验室
* [国立阳明交通大学计算机科学系](https://www.cs.nycu.edu.tw/)
* [Equinix](https://deploy.equinix.com/)
* [澳大利亚互联网协会](https://internet.asn.au/)
* [Internet Systems Consortium](https://www.isc.org/)
* [INX-ZA](https://www.inx.net.za/)
* [KDDI Web Communications Inc](https://www.kddi-webcommunications.co.jp/english/)
* [马来西亚研究与教育网络](https://www.mohe.gov.my/en/services/research/myren)
* [Metapeer](https://www.metapeer.com/)
* [NIC.br](https://www.metapeer.com/)
* [Your.Org](https://your.org/)
* [365 数据中心](https://365datacenters.com/)

法兰克福单服务器镜像是欧洲带宽和使用率最高的主要镜像。

我们仍在寻找一个额外的完整镜像站点（五个服务器）在欧洲来替换英国的旧服务器。

我们发现在全球范围内的互联网交换点（澳大利亚、巴西和南非）拥有单一的镜像是一个很好的模式；如果您了解或为其中的一些公司工作，他们可以赞助一个单一的镜像服务器，请与我们联系。美国（西海岸）和欧洲（任何地方）是较为理想的地点。

有关完整镜像站点规格的通用镜像布局，请参阅 [full mirror site specs](https://wiki.freebsd.org/Teams/clusteradm/generic-mirror-layout)，有关单一镜像站点的信息，请参阅 [tiny-mirror](https://wiki.freebsd.org/Teams/clusteradm/tiny-mirror)。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 持续集成

链接：

FreeBSD Jenkins 实例网址：[https://ci.FreeBSD.org](https://ci.freebsd.org)

FreeBSD CI artifact 存档网址：[https://artifact.ci.FreeBSD.org](https://artifact.ci.freebsd.org)

FreeBSD Jenkins Wiki 网址：[https://wiki.FreeBSD.org/Jenkins](https://wiki.freebsd.org/Jenkins)

托管 CI Wiki 网址：[https://wiki.FreeBSD.org/HostedCI](https://wiki.freebsd.org/HostedCI)

第三方软件 CI 网址：[https://wiki.FreeBSD.org/3rdPartySoftwareCI](https://wiki.freebsd.org/3rdPartySoftwareCI)

与 freebsd-testing@ 相关的事情网址：[https://bugs.freebsd.org/bugzilla/buglist.cgi?bug\_status=open\&email1=testing%40FreeBSD.org\&emailassigned\_to1=1\&emailcc1=1\&emailtype1=equals](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug\_status=open\&email1=testing%40FreeBSD.org\&emailassigned\_to1=1\&emailcc1=1\&emailtype1=equals)

FreeBSD CI 存储库网址：[https://github.com/freebsd/freebsd-ci](https://github.com/freebsd/freebsd-ci)

dev-ci 邮件列表网址：[https://lists.FreeBSD.org/subscription/dev-ci](https://lists.freebsd.org/subscription/dev-ci)

联系人：Jenkins 管理员 [jenkins-admin@FreeBSD.org](mailto:jenkins-admin@FreeBSD.org)

联系人：Li-Wen Hsu [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

联系人：freebsd-testing 邮件列表

联系人：IRC #freebsd-ci 频道 on EFNet

在 2023 年第二季度，我们与项目贡献者和开发者合作，满足了他们的测试需求。同时，我们还与外部项目和公司合作，在 FreeBSD 上进行更多的测试，以增强他们的产品。

重要完成的任务：

* 添加了 [FreeBSD-stable-13-amd64-gcc12\_build](https://ci.freebsd.org/job/FreeBSD-stable-13-amd64-gcc12\_build/) 任务。
* 将 main 分支和 stable/13 分支的构建环境更改为 13.2-RELEASE，将 stable/12 分支更改为 12.4-RELEASE。
* 使用 gcc12 的\*-build 任务正在向[ dev-ci 邮件列表](https://lists.freebsd.org/subscription/dev-ci)发送故障报告。
* 在 [BSDCan 2023 开发者峰会](https://wiki.freebsd.org/DevSummit/202305)上展示测试/CI 状态更新。

正在进行的任务：

* 设计和实施预提交 CI 构建和测试（以支持[工作流工作组](https://gitlab.com/bsdimp/freebsd-workflow)）。
* 设计和实施使用 CI 集群构建发布工件，就像发布工程一样。
* 简化贡献者和开发者的 CI/测试环境设置。
* 设置 CI 舞台环境并将实验性任务放在其中。
* 整理 freebsd-ci 存储库中的脚本，为将其合并到 src 存储库做准备。
* 改进硬件测试实验室并增加更多硬件进行测试。
* 合并 [https://reviews.freebsd.org/D38815](https://reviews.freebsd.org/D38815)。
* 合并 [https://reviews.freebsd.org/D36257](https://reviews.freebsd.org/D36257)。

待处理或排队的任务：

* 收集和整理 [CI 任务](https://hackmd.io/@FreeBSD-CI/freebsd-ci-todo)和想法。
* 为运行测试的虚拟机客户端设置公共网络访问。
* 实施使用裸机硬件运行测试套件。
* 添加针对-CURRENT 的 drm port 构建测试。
* 计划运行 ztest 测试。

帮助更多软件在其 CI 流水线中获得 FreeBSD 支持（Wiki 页面：[3rdPartySoftwareCI](https://wiki.freebsd.org/3rdPartySoftwareCI)，[HostedCI](https://wiki.freebsd.org/HostedCI)）。

与托管 CI 提供者合作，以获得更好的 FreeBSD 支持。

请参阅与 [freebsd-testing@相关的事情](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug\_status=%3Cem%3Eopen%3C/em%3E\&email1=testing%40FreeBSD.org\&emailassigned\_to1=1\&emailcc1=1\&emailtype1=equals)，了解更多进行中的信息，并欢迎加入这项工作！

赞助者：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### Ports

链接：

关于 FreeBSD Ports 的网址：[https://www.FreeBSD.org/ports/](https://www.freebsd.org/ports/)

贡献 Ports 的网址：[https://docs.freebsd.org/en/articles/contributing/#ports-contributing](https://docs.freebsd.org/en/articles/contributing/#ports-contributing)

FreeBSD Ports 监控网址：[http://portsmon.freebsd.org/](http://portsmon.freebsd.org/)

Ports 管理团队网址：[https://www.freebsd.org/portmgr/](https://www.freebsd.org/portmgr/)

Ports Tarball 网址：[http://ftp.freebsd.org/pub/FreeBSD/ports/ports/](http://ftp.freebsd.org/pub/FreeBSD/ports/ports/)

联系人：René Ladan [portmgr-secretary@FreeBSD.org](mailto:portmgr-secretary@FreeBSD.org)

联系人：FreeBSD Ports 管理团队 [portmgr@FreeBSD.org](mailto:portmgr@FreeBSD.org)

Ports 管理团队负责监督 Ports 的整体方向、构建软件包以及人员事务。以下是上一个季度的情况。

目前，Ports 中有超过 34,400 个 port。目前有 3,019 个未解决的 port 问题(PR)，其中有 746 个未被分配。上个季度 `main` 分支有来自 151 位提交者的 10,439 次提交，2023Q2 分支有来自 55 位提交者的 745 次提交。与上个季度相比，这意味着 port 数量略有增加，未解决的 PR 数量略有减少， port 提交数量有较大增加。

在本季度，我们欢迎 Tom Judge (tj@) 回归，同时告别了 Steve Wills (swills@)。Steve 也是 portmgr 的一员。作为 portmgr 开发计划的一部分，我们欢迎 Ronald Klop (ronald@)、Renato Botelho (garga@)和 Matthias Andree (mandree@) 的加入。

Portmgr 已经恢复了对将子软件包引入树中的工作，但仍有一些事项需要进一步完善。

在软件方面，pkg 已更新至 1.19.2，Firefox 更新至 114.0.2，Chromium 更新至 114.0.5735.198，KDE Gear 更新至 23.04.2。在上个季度，antoine@运行了 23 次 exp-runs 来测试软件包更新，将 CPU\_MAXSIZE 提升至 1024，修复了 devel/cmake-core 的 armv7 失败，并在 USES=meson 中添加了 `--auto-features=enabled` 选项。最后，Ports 已更新以支持 FreeBSD-CURRENT 中的 LLVM 16 和 OpenSSL 3。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 项目

涵盖多个类别的项目，从内核和用户空间到 Ports 或外部项目。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### Cirrus-CI

链接：

FreeBSD Cirrus-CI Repositories 网址：[https://cirrus-ci.com/github/freebsd/](https://cirrus-ci.com/github/freebsd/)

FreeBSD src CI 网址：[https://cirrus-ci.com/github/freebsd/freebsd-src](https://cirrus-ci.com/github/freebsd/freebsd-src)

FreeBSD doc CI 网址：[https://cirrus-ci.com/github/freebsd/freebsd-doc](https://cirrus-ci.com/github/freebsd/freebsd-doc)

联系人：Brooks Davis [brooks@FreeBSD.org](mailto:brooks@FreeBSD.org)

联系人：Ed Maste [emaste@FreeBSD.org](mailto:emaste@FreeBSD.org)

联系人：Li-Wen Hsu [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

Cirrus-CI 是一个托管的持续集成服务，支持在 Linux、Windows、macOS 和 FreeBSD 上进行开源项目的 CI 服务。它是我们自己 Jenkins CI 基础设施的补充，支持其他用例，包括测试 GitHub 的 pull requests 和 FreeBSD 的 forks。我们在 2019 年为 FreeBSD src 添加了 Cirrus-CI 配置，并在 2020 年为 doc 添加了配置。许多其他托管在 GitHub 上的 FreeBSD 项目（如 drm-kmod、kyua、pkg 和 poudriere）也使用了 Cirrus-CI。

在上一个季度，Cirrus-CI 配置接受了持续的维护更新（转换到最新的 FreeBSD RELEASE 镜像）。在 src 中，我们添加了一些额外的检查。这些检查确保在需要时更新生成的文件（`make sysent` 和 `make makeman`），并检查是否缺少目录。我们添加了使用 Clang/LLVM 16 工具链包进行构建的作业，与现在在基本系统中的 Clang 版本相匹配。现在，对于所有提交，GCC 作业默认在 GitHub 镜像上运行。

赞助者：DARPA 赞助者：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 在 FreeBSD 内核中支持 BATMAN

链接：

维基页面网址：[https://wiki.freebsd.org/SummerOfCode2023Projects/CallingTheBatmanFreeNetworksOnFreeBSD](https://wiki.freebsd.org/SummerOfCode2023Projects/CallingTheBatmanFreeNetworksOnFreeBSD)

源代码（Pull Request）网址：[https://github.com/obiwac/freebsd-gsoc/pull/1](https://github.com/obiwac/freebsd-gsoc/pull/1)

联系人：Aymeric Wibo [obiwac@FreeBSD.org](mailto:obiwac@FreeBSD.org)

BATMAN （Better Approach to Mobile Ad-hoc Networking）。BATMAN 是由 Freifunk 项目开发和使用的一种用于多跳自组织网络（主要是无线网络）的路由协议。Freifunk 是德国的一个倡议，旨在基于网络中立性原则在城市范围内构建开放的 Wi-Fi 网络。BATMAN 的目标是成为一个完全分散的协议；网络中的任何一个节点都不需要了解或关心整个网络的拓扑结构。

在 Linux 中，由 batman-adv 内核模块提供支持 BATMAN 的功能。而这个项目的目标是将类似的支持带到 FreeBSD，包括开发内核模块本身，以及创建 BATMAN 网络所需的用户空间网络库和工具。

目前，创建接口并与其进行交互已经可以在 Linux 和 FreeBSD 的用户空间中工作，尽管数据包传输（部分）可以工作，但仍然不完整。该项目还在 [ifconfig(8)](https://man.freebsd.org/cgi/man.cgi?query=ifconfig\&sektion=8\&format=html) 中添加了对 batadv 接口的支持。

导师：Mahdi Mokhtari

赞助商：2023 谷歌代码之夏项目

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 在 LinuxBoot 上的支持

联系人：Warner Losh [imp@bsdimp.com](mailto:imp@bsdimp.com)

链接：

LinuxBoot 项目网址：[https://www.linuxboot.org/](https://www.linuxboot.org/)

BSDCan 2023 kboot 演讲幻灯片链接：[https://docs.google.com/presentation/d/1N5Jp6XzYWv9Z9RhhETC-e6tFkqRHvp-ldRDW\_9h2JCw/edit?usp=sharing](https://docs.google.com/presentation/d/1N5Jp6XzYWv9Z9RhhETC-e6tFkqRHvp-ldRDW\_9h2JCw/edit?usp=sharing)

LinuxBoot 是一个致力于创建干净、健壮、可审计和可重复启动的启动固件的项目。最初是谷歌的一个特定项目，现已扩展到包括使用 Linux 来启动最终操作系统的任何启动环境。现在许多平台都支持这个环境，并且在某些情况下它是唯一可用的启动环境。此外，一些嵌入式设备上有一个硬编码的 LinuxBoot 环境，很难更改，因此能够重新启动到 FreeBSD 是有意义的。

旧的 Sony PlayStation 3 port 使用了一个名为 `kboot` 的引导加载程序来从其 Linux 内核启动 FreeBSD port（都是在 LinuxBoot 项目之前）。该代码已经大大扩展，并且通过易于替换的体系结构插件通用化。正常的 FreeBSD /boot/loader 被构建为 Linux 二进制文件，它读取 FreeBSD 内核、模块和可调整参数，并将它们放入内存，就像它在预启动环境中运行一样，然后使用 kexec\_load(2) 将该映像加载到 Linux 内核中，并进行特殊的重新启动到该映像。对于支持 UEFI 的系统，它会传递 UEFI 内存表和指向 UEFI 运行时服务的指针给新内核。

它支持从主机文件系统、主机块设备上的任何 loader(8) 支持的文件系统（包括跨多个设备的池）、RAM 磁盘映像以及通过网络下载的文件加载文件。可以混合使用这些功能。例如，可以从主机文件系统加载配置覆盖，同时内核从专用存储（如 NVME）或 RAM 磁盘映像加载。它支持在 stdin/stdout 上运行的主机控制台。它支持显式位置，例如 `/dev/nvme0ns1:/boot/loader/gerbil.conf`，用于加载文件系统的位置。它还支持 ZFS 引导环境，包括一次性引导功能。

有关 kboot 的更多详细信息，以及它支持的内容和一些常规背景，可以在 Warner 的 BSDcan 演讲中找到（上面链接的幻灯片）。

FreeBSD/aarch64 现在可以在 LinuxBoot 环境中从 Linux 启动，支持和功能与 loader.efi(8) 相当。内存布局传递用于 GICv3 补丁。需要为 aarch64 内核提供 GICv3 补丁（[https://reviews.freebsd.org/D40902](https://reviews.freebsd.org/D40902)）。

FreeBSD/amd64 的支持正在进行中，可能已完成了 80%。由于 amd64 是一个较早的 port，amd64 引导环境对引导加载程序提供内核数据有更多要求。由于内核无法从长模式访问这些数据，所有 BIOS 环境中的数据来源都必须由引导加载程序提供。虽然 UEFI 和 ACPI 提供了让内核获取这些数据的方式，但许多数据仍然必须由引导加载程序提供。内核在初始化过程中会发生崩溃，因为这些前提条件尚未被发现和实现。

PowerPC 已经构建，但其状态未知。作者尝试获取合适的 PlayStation 3 证明过于耗时。

**任务清单：**

1. 编写 loader.kboot(8) 文档，包括如何使用 loader.kboot，创建镜像以及当前支持的用例。
2. 完成 amd64 平台的支持。
3. 统一 kboot 和 efi 的 elf 架构特定元数据代码，目前是从 efi 复制的。由于它们大部分相同，但仍存在编译时的差异，因此需要进行统一。此外，构建基础设施使得共享变得复杂。
4. 添加 riscv64 平台的支持。
5. 进行 PowerPC 平台的测试（在重构开始后未进行测试）。
6. 创建一个脚本，将 EDK-II 镜像（例如来自 QEMU）重新打包为一个包含在 FreeBSD 上构建的 Linux 内核的 linux-boot 镜像，以进行 CI 测试。
7. 从 coreboot LinuxBoot 进行测试。

由 Netflix, Inc 赞助。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 用户空间变更

影响操作系统基本系统和其中程序的修改。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### OpenSSL 3 在基础系统中的导入

链接: OpenSSL 下载网址：[https://www.openssl.org/source/](https://www.openssl.org/source/)

OpenSSL 3.0 已发布！网址：[https://www.openssl.org/blog/blog/2021/09/07/OpenSSL3.Final/](https://www.openssl.org/blog/blog/2021/09/07/OpenSSL3.Final/)

openssl-fipsinstall 网址：[https://www.openssl.org/docs/man3.0/man1/openssl-fipsinstall.html](https://www.openssl.org/docs/man3.0/man1/openssl-fipsinstall.html)

联系人: Pierre Pronchery [pierre@freebsdfoundation.org](mailto:pierre@freebsdfoundation.org)

Pierre 被委派将 OpenSSL 3 导入基础系统。

OpenSSL 是一个通用密码学和安全通信库。它提供了 SSL 和 TLS 网络协议的开源实现，在电子邮件、即时消息、VoIP（网络电话）等应用中被广泛使用，尤其是在全球网络（即 HTTPS）中。假设 Apache 和 nginx Web 服务器使用 OpenSSL，它们在 Web 流量中的综合市场份额超过 50％，这巩固了 OpenSSL 作为互联网基础设施的领导地位和关键重要性。

自 2016 年 8 月首次发布以来，OpenSSL 1.1 分支已被大多数 Linux 和 BSD 系统采用，并通过长期支持（LTS）政策得到上游维护者的支持。然而，官方支持计划在今年 9 月中旬结束，因此迫切需要考虑采用其继任者 OpenSSL 3.0 分支进行 LTS。

OpenSSL 已大幅超越其前身 SSLeay，现在拥有超过 50 万行代码（SLOC）分布在两千多个文件中。或许由此产生的结果是，它的构建系统相对复杂，通常需要 Perl，而 FreeBSD 自 FreeBSD 5.0-RELEASE 以来已经移除了 Perl。幸运的是，可以按照 FreeBSD 的方式导入和设置 OpenSSL 3.0.9，现在它已作为 FreeBSD 14.0-RELEASE 的计划的一部分包含在基本系统中。

形容 OpenSSL 3 为一个重大发布是轻描淡写的。首先，其问题的许可模型终于得到解决，完全转向了 Apache License 2.0。其次，OpenSSL 3 引入了提供者模块的概念。虽然已将过时的加密算法隔离到遗留模块中，但也可以将实现限制为 FIPS 的标准部分，并使用 fips 模块。然后，后者可以受益于专门的认证过程，并得到官方认证（就像写作时发布的 3.0.8 版本一样）。

此外，更新后的库进行了版本升级，因为使用 OpenSSL 1.1 的应用程序需要重新编译以使用 3.0 版本。许多 API 函数已被弃用，并用更新的、更通用的替代方案替换，但仍然可以显式地请求旧的 API，并由 OpenSSL 3 相应地提供它们。在 FreeBSD 中利用了这种可能性来帮助过渡，其中许多库和应用程序只是简单地配置为请求 OpenSSL 1.1 API。这些组件将逐步在未来更新，以使用 OpenSSL 3 的本机 API。

虽然更新会对处理小输入块大小时产生一定的性能影响，但在处理 1 KB 及以上大小的块时，影响较小。另一个挑战在于 FIPS 提供者模块，目前需要一些手动步骤才能使其正常工作。我们目前正在寻找一种解决方案，以便默认情况下在 FreeBSD 中提供一个功能齐全的 FIPS 提供者。

赞助商: The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### Linux 兼容性层更新

链接:

Linuxulator 状态 Wiki 页面网址：[https://wiki.freebsd.org/Linuxulator](https://wiki.freebsd.org/Linuxulator)

Linux 应用程序状态 Wiki 页面网址：[https://wiki.freebsd.org/LinuxApps](https://wiki.freebsd.org/LinuxApps)

联系人: Dmitry Chagin [dchagin@FreeBSD.org](mailto:dchagin@FreeBSD.org)

该项目的目标是改进 FreeBSD 执行未经修改的 linux(4) 二进制文件的能力。

截至 [cbbac5609115](https://cgit.freebsd.org/src/commit/?id=cbbac5609115)，已实现在 amd64 上信号传递时保留 fpu xsave 状态。这使得可以在其中运行具有抢占式调度程序的现代 golang。

新的功能是在 [namei(9)](https://man.freebsd.org/cgi/man.cgi?query=namei\&sektion=9\&format=html)中添加了指定替代 ABI 根路径的功能。以前，要动态重新查找每个需要路径名转换的 [linux(4)](https://man.freebsd.org/cgi/man.cgi?query=linux\&sektion=4\&format=html)系统调用，需要一些不太美观的代码，并使用 `kern_alternate_path()`，该函数在解析目标中带有前导/的符号链接时不起作用。现在，非本机 ABI（即 [linux(4)](https://man.freebsd.org/cgi/man.cgi?query=linux\&sektion=4\&format=html)）在 exec 时使用一次 `pwd_altroot()` 调用来指定其根目录（例如 `/compat/ubuntu`），并忽略路径名转换。这样可以在 Ubuntu 兼容性环境中进行 chroot，而无需手动修复此类符号链接。

总共修复了 10 多个错误；glibc-2.37 测试套件报告的失败测试少于 70 个。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### Service Jail - 自动将 rc.d 服务加入 jail

链接：

D40369: 扩展 `/usr/bin/service` 以设置环境变量的可能性 网址: [https://reviews.freebsd.org/D40369](https://reviews.freebsd.org/D40369)

D40370: 自动加入 rc.d 服务的基础设施 网址: [https://reviews.freebsd.org/D40370](https://reviews.freebsd.org/D40370)

D40371: 自动服务 jail：为在自动服务 jail 中实现服务的全部功能进行一些设置 网址: [https://reviews.freebsd.org/D40371](https://reviews.freebsd.org/D40371)

联系人：Alexander Leidinger [netchild@FreeBSD.org](mailto:netchild@FreeBSD.org)

Service Jail 扩展了 rc(8) 系统，允许自动将 rc.d 服务加入 jail。服务 jail 继承父主机或 jail 的文件系统，但默认情况下使用 jail 的所有其他限制（进程可见性、受限网络访问、文件系统挂载权限、sysvipc 等）。附加配置允许继承父级的 IP 地址、sysvipc、内存页锁定和使用 bhyve 虚拟机监视器（vmm(4)）。

如果您想将例如 local\_unbound 加入服务 jail 并允许 IPv4 和 IPv6 访问，只需更改 rc.conf(5)为：

```shell-session
local_unbound_svcj_options=net_basic
local_unbound_svcj=YES
```

尽管这不具有手动 jail 设置与单独的文件系统和 IP/VNET 相同的安全性好处，但设置要简单得多，同时提供像隐藏同一用户的其他进程等 jail 的某些安全性好处。

链接中的补丁是[我在 2019 年所提供的重写](https://lists.freebsd.org/pipermail/freebsd-jail/2019-February/003710.html)。主要区别在于使用了一个 ENV 变量来进行更合理的跟踪，因此需要更改 service(8)。

我的意图是在 stable/14 分支之前提交 D40369。在发布 14.0 之前，我不会提交 D40370 或 D40371，并且两者都将受益于更多人的审查。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 使用 ktrace(1) 进行安全沙箱化

链接：

ktrace 分支 网址: [https://github.com/jakesfreeland/freebsd-src/tree/ff/ktrace](https://github.com/jakesfreeland/freebsd-src/tree/ff/ktrace)

联系人：Jake Freeland [jfree@FreeBSD.org](mailto:jfree@FreeBSD.org)

使用 ktrace(1) 进行 Capiscum 化

本报告介绍了对 ktrace(1) 的扩展，用于记录未进行 Capiscum 化的程序的能力违规情况。

在 Capiscum 化的第一步是确定您的程序在哪里引发了能力违规。您可以通过查看源代码并删除与 Capiscum 不兼容的代码来解决此问题，但这可能很繁琐，并要求开发人员熟悉在能力模式中不允许的所有内容。

另一种寻找违规的替代方法是使用 ktrace(1)。ktrace(1) 工具记录指定进程的内核活动。能力违规发生在内核内部，因此 ktrace(1) 可以使用 `-t p` 选项记录和返回有关程序违规的额外信息。

传统上，需要将程序放入能力模式，然后它们才能报告违规。当输入受限制的系统调用时，它将失败并返回 `ECAPMODE: Not permitted in capability mode`。如果开发人员进行错误检查，那么他们的程序可能会以该错误终止。这种行为使得违规跟踪变得不方便，因为 ktrace(1)只会报告第一个能力违规，然后程序将终止。

幸运的是，ktrace(1) 的新扩展可以在程序没有进入能力模式时记录违规。这意味着任何开发人员都可以在其程序上运行能力违规跟踪而无需修改，以查看它引发违规的位置。由于程序实际上从未进入能力模式，因此它仍将获取资源并正常执行。

**违规跟踪示例**

下面显示的 cap\_violate 程序尝试引发 ktrace(1)可以捕获的每种类型的违规：

```shell-session
# ktrace -t p ./cap_violate
# kdump
1603 ktrace   CAP   system call not allowed: execve
1603 foo      CAP   system call not allowed: open
1603 foo      CAP   system call not allowed: open
1603 foo      CAP   system call not allowed: open
1603 foo      CAP   system call not allowed: open
1603 foo      CAP   system call not allowed: readlink
1603 foo      CAP   system call not allowed: open
1603 foo      CAP   cpuset_setaffinity: restricted cpuset operation
1603 foo      CAP   openat: restricted VFS lookup: AT_FDCWD
1603 foo      CAP   openat: restricted VFS lookup: /
1603 foo      CAP   system call not allowed: bind
1603 foo      CAP   sendto: restricted address lookup: struct sockaddr { AF_INET, 0.0.0.0:5000 }
1603 foo      CAP   socket: protocol not allowed: IPPROTO_ICMP
1603 foo      CAP   kill: signal delivery not allowed: SIGCONT
1603 foo      CAP   system call not allowed: chdir
1603 foo      CAP   system call not allowed: fcntl, cmd: F_KINFO
1603 foo      CAP   operation requires CAP_WRITE, descriptor holds CAP_READ
1603 foo      CAP   attempt to increase capabilities from CAP_READ to CAP_READ,CAP_WRITE
```

前 7 个 `system call not allowed` 条目并不是显式地来自 `cap_violate` 程序代码。相反，它们是由 FreeBSD 的 C 运行时库引发的。当您使用 `-t np` 选项跟踪 namei 转换和能力违规时，这一点变得明显：

```shell-session
# ktrace -t np ./cap_violate
# kdump
1632 ktrace   CAP   system call not allowed: execve
1632 ktrace   NAMI  "./cap_violate"
1632 ktrace   NAMI  "/libexec/ld-elf.so.1"
1632 foo      CAP   system call not allowed: open
1632 foo      NAMI  "/etc/libmap.conf"
1632 foo      CAP   system call not allowed: open
1632 foo      NAMI  "/usr/local/etc/libmap.d"
1632 foo      CAP   system call not allowed: open
1632 foo      NAMI  "/var/run/ld-elf.so.hints"
1632 foo      CAP   system call not allowed: open
1632 foo      NAMI  "/lib/libc.so.7"
1632 foo      CAP   system call not allowed: readlink
1632 foo      NAMI  "/etc/malloc.conf"
1632 foo      CAP   system call not allowed: open
1632 foo      NAMI  "/dev/pvclock"
1632 foo      CAP   cpuset_setaffinity: restricted cpuset operation
1632 foo      NAMI  "ktrace.out"
1632 foo      CAP   openat: restricted VFS lookup: AT_FDCWD
1632 foo      NAMI  "/"
1632 foo      CAP   openat: restricted VFS lookup: /
1632 foo      CAP   system call not allowed: bind
1632 foo      CAP   sendto: restricted address lookup: struct sockaddr { AF_INET, 0.0.0.0:5000 }
1632 foo      CAP   socket: protocol not allowed: IPPROTO_ICMP
1632 foo      CAP   kill: signal delivery not allowed: SIGCONT
1632 foo      CAP   system call not allowed: chdir
1632 foo      NAMI  "."
1632 foo      CAP   system call not allowed: fcntl, cmd: F_KINFO
1632 foo      CAP   operation requires CAP_WRITE, descriptor holds CAP_READ
1632 foo      CAP   attempt to increase capabilities from CAP_READ to CAP_READ,CAP_WRITE
```

在实际情况下，能力模式总是在 C 运行时库的初始化后进入，因此程序永远不会触发这前 7 个违规行为。我们之所以看到它们，是因为 ktrace(1)在程序启动之前开始记录违规行为。

这个演示清楚地表明，违规跟踪并不总是完美的。它是检测受限制系统调用的有用指南，但可能并不总是模拟程序在能力模式下的实际行为。在能力模式下，违规等同于错误；它们是停止执行的指示。违规跟踪忽略了这一建议，无论如何继续执行，因此可能会报告无效的违规行为。

下一个示例从 unzip(1) 实用程序（在进行 Capsicum 化之前）跟踪违规行为：

```shell-session
# ktrace -t np unzip foo.zip
Archive:  foo.zip
creating: bar/
extracting: bar/bar.txt
creating: baz/
extracting: baz/baz.txt
# kdump
1926 ktrace   CAP   system call not allowed: execve
1926 ktrace   NAMI  "/usr/bin/unzip"
1926 ktrace   NAMI  "/libexec/ld-elf.so.1"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/etc/libmap.conf"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/usr/local/etc/libmap.d"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/var/run/ld-elf.so.hints"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libarchive.so.7"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/usr/lib/libarchive.so.7"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libc.so.7"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libz.so.6"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libbz2.so.4"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/usr/lib/libbz2.so.4"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/liblzma.so.5"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/usr/lib/liblzma.so.5"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libbsdxml.so.4"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libprivatezstd.so.5"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/usr/lib/libprivatezstd.so.5"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libcrypto.so.111"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libmd.so.6"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libthr.so.3"
1926 unzip    CAP   system call not allowed: readlink
1926 unzip    NAMI  "/etc/malloc.conf"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/dev/pvclock"
1926 unzip    NAMI  "foo.zip"
1926 unzip    CAP   openat: restricted VFS lookup: AT_FDCWD
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/etc/localtime"
1926 unzip    NAMI  "bar"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    CAP   system call not allowed: mkdir
1926 unzip    NAMI  "bar"
1926 unzip    NAMI  "bar"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "bar/bar.txt"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "bar/bar.txt"
1926 unzip    CAP   openat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "baz"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    CAP   system call not allowed: mkdir
1926 unzip    NAMI  "baz"
1926 unzip    NAMI  "baz"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "baz/baz.txt"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "baz/baz.txt"
1926 unzip    CAP   openat: restricted VFS lookup: AT_FDCWD
```

unzip(1) 的违规跟踪输出更类似于开发人员在首次跟踪自己的程序时所看到的情况。大多数程序都会链接到库。在这种情况下，unzip(1)链接到 libarchive(3)，这在追踪中反映了出来：

```shell-session
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libarchive.so.7"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/usr/lib/libarchive.so.7"
```

unzip(1) 的违规行为可以在 C 运行时违规行为之后找到：

```shell-session
1926 unzip    NAMI  "foo.zip"
1926 unzip    CAP   openat: restricted VFS lookup: AT_FDCWD
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/etc/localtime"
1926 unzip    NAMI  "bar"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    CAP   system call not allowed: mkdir
1926 unzip    NAMI  "bar"
1926 unzip    NAMI  "bar"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "bar/bar.txt"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "bar/bar.txt"
1926 unzip    CAP   openat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "baz"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    CAP   system call not allowed: mkdir
1926 unzip    NAMI  "baz"
1926 unzip    NAMI  "baz"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "baz/baz.txt"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "baz/baz.txt"
1926 unzip    CAP   openat: restricted VFS lookup: AT_FDCWD
```

在这种情况下，unzip(1) 正在重新创建 zip 归档中包含的文件结构。违规行为是因为在能力模式下不能使用 AT\_FDCWD 值。这些违规行为的大部分可以通过在进入能力模式之前打开 AT\_FDCWD（当前目录）并将该描述符传递给 openat(2)、fstatat(2)和 mkdirat(2)作为相对引用来解决。

虽然违规行为跟踪可能不会自动将程序 Capsicum 化，但它是开发者工具箱中的另一种工具。在 ktrace(1)下运行程序只需要几秒钟的时间，结果几乎总是一个不错的起点，用于使用 Capsicum 对程序进行沙盒化。

赞助：FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### NVMe over Fabrics

链接：nvmf2 branch 网址: [https://github.com/bsdjhb/freebsd/tree/nvmf2](https://github.com/bsdjhb/freebsd/tree/nvmf2)

联系人: John Baldwin [jhb@FreeBSD.org](mailto:jhb@FreeBSD.org)

NVMe over Fabrics（NVMe-oF）允许通过网络通信使用 NVMe 协议与存储设备交互。这类似于使用 iSCSI 通过网络导出存储设备并使用 SCSI 命令进行通信。

NVMe over Fabrics 目前定义了用于光纤通道、RDMA 和 TCP 的网络传输。

在 nvmf2 分支中的工作包括一个用户空间库（`lib/libnvmf`），其中包含用于传输的抽象和 TCP 传输的实现。它还对 nvmecontrol(8)进行了更改，以添加“discover”、“connect”和“disconnect”命令来管理与远程控制器的连接。

该分支还包含一个内核中的 Fabrics 实现。`nvmf_transport.ko` 包含一个在 nvmf 主机（即 SCSI 中的 initiator）和各个传输之间的传输抽象。`nvmf_tcp.ko` 包含一个 TCP 传输层的实现。`nvmf.ko` 包含一个 NVMe over Fabrics 主机（initiator），它连接到远程控制器并将远程命名空间导出为磁盘设备。类似于 NVMe over PCI-express 的 nvme(4)驱动程序，命名空间通过 `/dev/nvmeXnsY` 设备导出，这些设备仅支持简单操作，同时还通过 CAM 导出为 ndaX 磁盘设备。与 nvme(4)不同，nvmf(4)不支持 nvd(4)磁盘驱动程序。nvmecontrol(8) 可用于处理远程命名空间和远程控制器，例如获取日志页、显示识别信息等。

请注意，nvmf(4) 目前还相对简单，有些错误情况仍在待办事项中。如果发生错误，队列（和后端网络连接）将被丢弃，但设备将保留，并暂停 I/O 请求。可以使用 `nvmecontrol reconnect` 命令连接一组新的网络连接以恢复操作。与使用持续型守护程序（iscsid(8)）在错误后重新连接的 iSCSI 不同，重新连接必须手动进行。

当前的代码非常新，可能不太稳定。它肯定还没有准备好用于生产环境。有兴趣在 NVMe over Fabrics 上进行测试的有经验的用户，可以自行承担风险并开始测试。

下一个主要任务是实现一个 Fabrics 控制器（SCSI 中的 target）。可能首先是在用户空间中实现一个简单的控制器，然后再实现一个“真实”的控制器，将数据处理外包给内核，但与 ctld(8)有一定的集成，以便通过 iSCSI 或 NVMe 导出各个磁盘设备，或者通过使用单个配置文件和守护程序来管理所有这些。这可能需要在 ctld 中进行一些重构，使其不那么依赖 iSCSI。在控制器侧的工作还将验证在传输无关层中目前未经充分测试的 API 设计决策。在此步骤之后，可能才有意义将任何 NVMe over Fabrics 的更改合并到树中。

赞助：Chelsio Communications

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Kernel

在内核子系统/功能、驱动程序支持、文件系统等方面的更新。

#### 启动性能改进

链接：

Wiki 页面 网址: [https://wiki.freebsd.org/BootTime](https://wiki.freebsd.org/BootTime)

BSDCan 演讲幻灯片 网址: [https://www.bsdcan.org/events/bsdcan\_2023/sessions/session/116/slides/44/BSDCan23-Firecracker.pdf](https://www.bsdcan.org/events/bsdcan\_2023/sessions/session/116/slides/44/BSDCan23-Firecracker.pdf)

联系人: Colin Percival [cperciva@FreeBSD.org](mailto:cperciva@FreeBSD.org)

Colin 正在协调加快 FreeBSD 启动过程的工作。

最近的工作从 EC2 转向了 Firecracker 虚拟机管理器，该管理器提供了一个非常简化的环境；简化启动过程使得更容易识别剩余时间，并确定是否可以进一步优化。

通过对 FreeBSD 和 Firecracker 进行一些实验性补丁，现在可以在不到 20 毫秒的时间内启动 FreeBSD 内核。

Colin 在 BSDCan 上的“将 FreeBSD 移植到 Firecracker”演讲中讨论了最近的改进。

这项工作得到了他的 FreeBSD/EC2 Patreon 的支持。

赞助者: https://www.patreon.com/cperciva

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### CI 测试工具链用于引导加载程序

链接：

[FreeBSD Wiki 谷歌代码之夏页面](https://wiki.freebsd.org/SummerOfCode2023Projects/CITestHarnessForBootloader)

[Github 项目链接](https://github.com/mightyjoe781/freebsd-src/tree/bootloader-smk/tools/boot/bootloader\_test)

联系人: Sudhanshu Mohan Kashyap [smk@FreeBSD.org](mailto:smk@FreeBSD.org)

FreeBSD 支持多种体系结构、文件系统和磁盘分区方案。我正在尝试编写一个 Lua 脚本，该脚本将允许测试所有支持的第一和第二级支持的体系结构组合的引导加载程序，并提供关于任何不兼容组合和预期功能的报告。如果时间允许，还可以进一步探索将脚本集成到现有的构建基础设施中（如 Jenkins 或 Github Actions），以生成测试结果的综合摘要。

目前，开发人员所做的任何更改可能会影响操作系统在某些特定环境中的启动能力。这些脚本确保更改不会导致已测试环境的回归。这些脚本的设计高效且比目前所需的完整构建更便宜。这些特性允许开发人员经常使用脚本，并在 CI 流水线中集成而不会产生过多的成本。

目前脚本相关的工作似乎进展顺利，但在未来我需要找到各种 QEMU 配置以测试不同的环境。如果有任何工作中的 QEMU 配方适用于当前发布版本的 FreeBSD，请随时通过邮件发送至 smk@FreeBSD.org。

赞助者: 2023 谷歌代码之夏项目

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 内核的物理内存压缩

链接：

谷歌代码之夏项目维基页面 网址：[https://wiki.freebsd.org/SummerOfCode2023Projects/PhysicalMemoryAntiFragmentationMechanisms](https://wiki.freebsd.org/SummerOfCode2023Projects/PhysicalMemoryAntiFragmentationMechanisms) [Differential revision 40575](https://reviews.freebsd.org/D40575) 网址：[https://reviews.freebsd.org/D40575](https://reviews.freebsd.org/D40575) [Differential revision 40772](https://reviews.freebsd.org/D40772) 网址：[https://reviews.freebsd.org/D40772](https://reviews.freebsd.org/D40772)

联系人：Bojan Novković [bnovkov@FreeBSD.org](mailto:bnovkov@FreeBSD.org)

大多数现代 CPU 架构通过支持大于标准页面大小的页面来提供性能提升。不幸的是，由于高度的物理内存碎片化，分配这种页面可能会失败。这项工作实现了物理内存压缩作为一种主动减少运行系统碎片化的手段。这项工作是正在进行的谷歌代码之夏项目的一部分，其目标是向虚拟内存子系统添加各种物理内存抗碎片化措施。

Differential [D40575](https://reviews.freebsd.org/D40575) 实现了用于量化物理内存碎片化程度的众所周知的度量标准。 Differential [D40772](https://reviews.freebsd.org/D40772) 实现了物理内存压缩，并添加了一个守护程序，监视系统并在需要时执行压缩。

计划的未来工作包括设计适当的基准测试套件，运行测试，并根据评审和测试结果调整代码。这仍然是一个正在进行的工作，因此非常欢迎进行任何测试、评审和反馈。

赞助者：2023 谷歌代码之夏项目

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 增加 MAXCPU

链接：

[D36838：amd64：将 MAXCPU 从 256 增加到 1024](https://reviews.freebsd.org/D36838) 网址：[https://reviews.freebsd.org/D36838](https://reviews.freebsd.org/D36838)

联系人：Ed Maste [emaste@FreeBSD.org](mailto:emaste@FreeBSD.org)

默认的 amd64 和 arm64 FreeBSD 内核配置目前支持最多 256 个 CPU。可以通过设置 `MAXCPU` 内核选项来构建支持更大核心数的自定义内核。然而，拥有超过 256 个 CPU 的普通系统正在变得越来越多，并且在 FreeBSD 14 的支持生命周期中将变得越来越常见。我们希望将默认的最大 CPU 数增加到 1024，以便在 FreeBSD 14 上“开箱即用”地支持这些系统。

为了支持更大的默认 MAXCPU，进行了一些更改，包括将 `cpuset_t` 的用户空间最大值修复为 1024。还进行了一些更改，以避免静态的 `MAXCPU` 大小的数组，将它们替换为按需内存分配。

需要进一步的工作来继续减少由 `MAXCPU` 大小确定的静态分配，并解决在非常高核心数系统上的可伸缩性瓶颈，但目标是在 FreeBSD 14 发布时提供对大型 CPU 数量的支持，具有稳定的 ABI 和 KBI。

赞助者：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### SquashFS 在 FreeBSD 内核的移植

链接：

Wiki 页面 网址：[https://wiki.freebsd.org/SummerOfCode2023Projects/PortSquashFuseToTheFreeBSDKernel](https://wiki.freebsd.org/SummerOfCode2023Projects/PortSquashFuseToTheFreeBSDKernel)

源代码 网址：[https://github.com/Mashijams/freebsd-src/tree/gsoc/squashfs](https://github.com/Mashijams/freebsd-src/tree/gsoc/squashfs)

联系人：Raghav Sharma [raghav@FreeBSD.org](mailto:raghav@FreeBSD.org)

SquashFS 是一个只读文件系统，可以非常高效地压缩整个文件系统或单个目录。自 2009 年以来，Linux 内核内置了对它的支持，并在嵌入式 Linux 发行版中非常常见。该项目的目标是为 FreeBSD 内核添加 SquashFS 支持，以实现从内存中的 SquashFS 文件系统引导 FreeBSD。

目前，该驱动程序与 FreeBSD 13.2 版本兼容。该驱动程序能够正确解析 SquashFS 磁盘文件，并支持工作中的 mount(8)。Linux SquashFS 支持许多压缩选项，如 zstd、lzo2、zlib 等，根据用户的喜好选择，我们的驱动程序也支持所有这些压缩方式。

计划的未来工作包括添加对目录、文件、扩展属性和符号链接的读取支持。该项目仍在 [Chuck Tuffli](../di-0-zhang-freebsd-zhong-wen-she-qu/chuck@FreeBSD.org) 的指导下进行中，并预计将在谷歌代码之夏项目结束时完成。

赞助者：2023 谷歌代码之夏项目

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 改进 Pf

链接：

D40911 网址：[https://reviews.freebsd.org/D40911](https://reviews.freebsd.org/D40911)

D40861 网址：[https://reviews.freebsd.org/D40861](https://reviews.freebsd.org/D40861)

D40862 网址：[https://reviews.freebsd.org/D40862](https://reviews.freebsd.org/D40862)

D40863 网址：[https://reviews.freebsd.org/D40863](https://reviews.freebsd.org/D40863)

D40864 网址：[https://reviews.freebsd.org/D40864](https://reviews.freebsd.org/D40864)

D40865 网址：[https://reviews.freebsd.org/D40865](https://reviews.freebsd.org/D40865)

D40866 网址：[https://reviews.freebsd.org/D40866](https://reviews.freebsd.org/D40866)

D40867 网址：[https://reviews.freebsd.org/D40867](https://reviews.freebsd.org/D40867)

D40868 网址：[https://reviews.freebsd.org/D40868](https://reviews.freebsd.org/D40868)

D40869 网址：[https://reviews.freebsd.org/D40869](https://reviews.freebsd.org/D40869)

D40870 网址：[https://reviews.freebsd.org/D40870](https://reviews.freebsd.org/D40870)

联系人：Kajetan Staszkiewicz [vegeta@tuxpowered.net](mailto:vegeta@tuxpowered.net)

联系人：Naman Sood [naman@freebsdfoundation.org](mailto:naman@freebsdfoundation.org)

联系人：Kristof Provost [kp@FreeBSD.org](mailto:kp@FreeBSD.org)

pf(4)是 FreeBSD 中包含的防火墙之一，也可能是最受欢迎的。pf 最初由 OpenBSD 项目创建，后来移植到 FreeBSD。

**OpenBSD 语法的向后兼容**

Kajetan 引入了"scrub"操作的 OpenBSD 语法在"match"和"pass"规则中。现有规则仍然受支持，但现在也支持 OpenBSD 风格的"scrub"配置。

**pfsync 协议版本**

现在可以配置 pfsync(4)协议版本，允许在支持不同内核版本之间的状态同步的同时进行协议更改。主要好处是允许协议更改以实现新功能。

**pfsync：在 IPv6 上传输**

pfsync 流量现在也可以通过 IPv6 进行传输。Naman 完成了 Luiz Amaral 开始的工作。

**SCTP**

正在进行支持 pf 中的 SCTP 工作。该支持包括对端口号的过滤、状态跟踪、pfsync 故障转移以及返回 ABORT 块以拒绝连接。

赞助：InnoGames GmbH 赞助：Orange Business Services 赞助：FreeBSD 基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 网络接口 API（IfAPI）

链接：

原始项目页面 网址：link:https://wiki.freebsd.org/projects/ifnet

联系人：Justin Hibbits [jhibbits@FreeBSD.org](mailto:jhibbits@FreeBSD.org)

IfAPI（原名 DrvAPI）项目始于 2014 年，其目标是隐藏网络驱动程序中的 ifnet(9) 结构。相反，所有对成员的访问都将通过访问器函数进行。这允许更改网络堆栈而无需重新编译驱动程序，还有可能让单个驱动程序支持多个 FreeBSD 版本。

目前，在基本系统中已经实现了这一目标，但是还需要更新一些 port 来使用 IfAPI。有一个工具可以自动完成大部分的转换，即 `tools/ifnet/convert_ifapi.sh`。文档也正在准备中，但可能需要帮助。ifnet(9)需要进行大量的清理，因为目前其中的一些信息已经过时了。

赞助：Juniper Networks, Inc.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 使 Netgraph 无锁化

链接：

维基页面网址：[https://wiki.freebsd.org/SummerOfCode2023Projects/LocklessSynchronizationBetweenNodesInNetgraph](https://wiki.freebsd.org/SummerOfCode2023Projects/LocklessSynchronizationBetweenNodesInNetgraph)

仓库网址：[https://github.com/zinh88/epoch-netgraph](https://github.com/zinh88/epoch-netgraph)

联系人：Zain Khan [zain@FreeBSD.org](mailto:zain@FreeBSD.org)

Netgraph 帮助我们通过将内核对象（称为节点）排列在连接的图中，使用钩子连接它们，从而实现自定义或复杂的网络功能。节点可以对传入的数据包执行一组明确定义的操作，并将输出发送到另一个连接的节点。将数据包“发送”给相邻节点也可以看作在那个相邻节点上调用函数。

在非 SMP 世界中，一个线程（或该线程）总是将节点视为空闲（未繁忙），以便可以立即调用其函数。并发引入了繁忙节点的可能性。此外，数据包的传输也需要注意图的结构的变化，例如：由于不存在的钩子或节点，寻址节点的路径可能不会保持完整，这可能导致引用已被释放的对象的情况。为了防止这种情况，现有的源代码使用了拓扑读写互斥锁来保护数据流不受重构事件的影响（以及重构事件不受其他重构事件的影响）。

我们希望恢复并发 CPU 不存在时存在的相同的数据流程。也就是说，每次发生重构事件时，数据应该根本不需要等待。同时，我们显然也不希望给内核理由导致崩溃。

FreeBSD 拥有一套自己的并发安全数据结构和机制。其中一个机制就是 Epoch。基于 Epoch 的回收涉及等待现有的读侧临界区完成，然后再修改或回收数据结构。

由于正在修改基本系统，这也将影响之前所做的设计选择，例如消息排队、引用计数等。

这个项目涉及大量的测试。目前，一些拓扑保护锁已经被移除，并且只测试了简单的图（在 VM 上运行 FreeBSD）。真正的测试应该在至少有 4 个 CPU 核心的硬件上运行，我会在得到一台这样的设备时进行测试。

赞助：2023 谷歌代码之夏项目

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 架构

更新特定平台的功能，并为新的硬件平台提供支持。

#### 增强 SIMD （针对 amd64 架构）

链接：

SIMD 调度框架草案 网址：[https://reviews.freebsd.org/D40693](https://reviews.freebsd.org/D40693)

项目提案 网址：[http://fuz.su/\~fuz/freebsd/2023-04-05\_libc-proposal.txt](http://fuz.su/\~fuz/freebsd/2023-04-05\_libc-proposal.txt)

联系人：Robert Clausecker [clausecker@FreeBSD.org](mailto:clausecker@FreeBSD.org)

SIMD 指令集扩展，如 SSE、AVX 和 NEON，在现代计算机上普遍存在，并为许多应用程序提供性能优势。该项目的目标是为常见的 libc 函数（主要是 string(3)中描述的函数）提供 SIMD 增强版本，加速大多数 C 程序的执行。

对于每个优化的函数，将提供多达四种实现：

* 标量实现，针对 amd64 进行了优化，但没有使用 SIMD。
* 基准实现，使用 SSE 和 SSE2 或者使用 x86-64-v2，涵盖了 SSE4.2 之前的所有 SSE 扩展。
* 使用 AVX 和 AVX2 的 x86-64-v3 实现。
* 使用 AVX-512F/BW/CD/DQ 的 x86-64-v4 实现。

用户可以通过设置 AMD64\_ARCHLEVEL 环境变量来选择要使用的 SIMD 增强级别。

虽然当前的项目只涉及 amd64 架构，但未来可能会扩展到其他架构，如 arm64。

赞助：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 将 mfsBSD 集成到发布构建工具中

链接：

维基文章 网址：[https://wiki.freebsd.org/SummerOfCode2023Projects/IntegrateMfsBSDIntoTheReleaseBuildingTools](https://wiki.freebsd.org/SummerOfCode2023Projects/IntegrateMfsBSDIntoTheReleaseBuildingTools)

项目存储库（integrate-mfsBSD-building 分支）网址：[https://github.com/soobinrho/freebsd-src/tree/integrate-mfsBSD-building](https://github.com/soobinrho/freebsd-src/tree/integrate-mfsBSD-building)

联系人：Soobin Rho [soobinrho@FreeBSD.org](mailto:soobinrho@FreeBSD.org)

**什么是 mfsBSD？**

"mfsBSD 是一个工具集，用于创建基于 FreeBSD 的小型但功能齐全的 mfsroot 发行版，它将所有文件存储在内存中（MFS）\[内存文件系统]，并从硬盘、USB 存储设备或光盘加载。它可以用于各种目的，包括无盘系统、恢复分区以及远程覆盖其他操作系统。"

[Martin Matuska](../di-0-zhang-freebsd-zhong-wen-she-qu/mm@FreeBSD.org) 既是 [mfsBSD 白皮书](https://people.freebsd.org/\~mm/mfsbsd/mfsbsd.pdf)的作者，也是 [mfsBSD 存储库](https://github.com/mmatuska/mfsbsd)的维护者。

**目的**

该项目在 src/release makefile 中为当前版本和稳定版本的 mfsBSD 映像创建额外的目标。目前，只生产发布版本的 mfsBSD 映像，这意味着它们往往与基本工具不同步。该项目旨在解决这个问题。

**位置**

这是 2023 年的谷歌代码之夏项目。因此，官方的编码期限是从 2023 年 5 月 29 日到 2023 年 8 月 28 日。作为开源社区的初学者，作者欢迎在项目存储库中提出所有的意见、建议和拉取请求，该存储库将是整个期间内所有代码的位置。

导师：[Juraj Lutter](../di-0-zhang-freebsd-zhong-wen-she-qu/otis@FreeBSD.org)和 [Joseph Mingone](../di-0-zhang-freebsd-zhong-wen-she-qu/jrm@FreeBSD.org)

赞助：2023 谷歌代码之夏项目

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 云平台

更新特定于云环境的功能，并为新的云平台提供支持。

#### FreeBSD 作为一级云平台的 cloud-init 支持

链接：

cloud-init 网站网址：[https://cloud-init.io/](https://cloud-init.io/)

cloud-init 文档网址：[https://cloudinit.readthedocs.io/en/latest/](https://cloudinit.readthedocs.io/en/latest/)

cloud-init 正在进行的重构网址：[https://github.com/canonical/cloud-init/blob/main/WIP-ONGOING-REFACTORIZATION.rst](https://github.com/canonical/cloud-init/blob/main/WIP-ONGOING-REFACTORIZATION.rst)

联系人：Mina Galić [freebsd@igalic.co](mailto:freebsd@igalic.co)

cloud-init 是在云中配置服务器的标准方式。不幸的是，除了 Linux 以外的操作系统对 cloud-init 的支持一直相对较差，而在 FreeBSD 上缺乏 cloud-init 支持阻碍了希望将 FreeBSD 作为一级平台的云提供商。为了解决这个问题，该项目旨在使 FreeBSD 的 cloud-init 支持与 Linux 支持相当。更广泛的计划是在所有 BSD 上提供支持。

这个季度进展缓慢，但我已经完成了一个新的里程碑：

* 瞬时网络类别已被重写并与平台无关。这些类别被多个云提供商用于在检索实际配置之前初始化临时网络。
* cloud-init 已经在 Vultr 上成功测试。我希望在下一个 RELEASE 版本中，我能说服 Vultr 将他们的 FreeBSD 镜像切换到 cloud-init。

除此之外，我还扩展了 BSD 上的 rsyslog 支持。我还为 cloud-init 的 ds-identify 添加了一个 rc 脚本，这应该使零配置设置的速度提高几个数量级：ds-identify 首先运行，并快速猜测机器正在运行的云提供商。然后 cloud-init 仅使用该猜测，而不是在所有可能的云提供商列表中进行迭代和失败。构建自定义映像的人可以轻松禁用此功能（通过删除 `/usr/local/etc/rc.d/dsidentify`），并自己提供一个特定的列表，从引导中节省几毫秒的时间。

接下来的步骤将是继续处理网络重构任务，并为 FreeBSD 添加 [LXD](https://github.com/canonical/lxd/pull/11761) 支持，以便可以将其包含在 CI 测试中。后者将涉及对 LXD 的工作，以及对 [FreeBSD virtio](https://bugs.freebsd.org/bugzilla/show\_bug.cgi?id=271793) 子系统的工作。

与往常一样，我非常欢迎早期测试者检查 [net/cloud-init-devel](https://cgit.freebsd.org/ports/tree/net/cloud-init-devel/)，并报告 bug。自上次报告以来，cloud-init 的 bug 跟踪器已从 Launchpad 迁移到 GitHub，因此这可能会减少一些摩擦。

赞助商：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 上的 OpenStack

链接：

OpenStack 网站 网址：[https://www.openstack.org/](https://www.openstack.org/)

FreeBSD 上的 OpenStack 网址：[https://github.com/openstack-on-freebsd](https://github.com/openstack-on-freebsd)

联系人：Chih-Hsin Chang [starbops@hey.com](mailto:starbops@hey.com)

联系人：Li-Wen Hsu [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

该项目旨在将关键的 OpenStack 组件，如 keystone、nova 和 neutron，移植到 FreeBSD，使其可以作为 OpenStack 主机运行。

我们已经开始移植 `nova-novncproxy` 和 `nova-serialproxy`，以增加访问实例控制台的方式。为了降低想要尝试该项目的人的门槛，我们还将开发环境从物理机迁移到虚拟机。但在 Linux KVM 之上运行 bhyve 虚拟机仍然存在问题。关于这个问题的详细解释可以在[这里](https://hackmd.io/@starbops/SkdJON2un)找到。其他的成就包括：

* 解决实例内部的网络连接问题
* 能够生成多个实例
* 从 Python 3.8 移植到 3.9。

在下个季度，我们将继续改进控制台代理服务，以使整体工作流更加流畅。

在[文档存储库中](https://github.com/openstack-on-freebsd/docs)还可以找到构建 POC 站点的逐步文档。每个 OpenStack 组件的修补版本都在同一 GitHub 组织下。

有兴趣帮助该项目的人可以先按照安装指南检查文档。欢迎提供反馈和帮助。

赞助商：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 在 Microsoft HyperV 和 Azure 上的支持

链接：

Microsoft Azure 上的 FreeBSD Wiki 文章网址：[https://wiki.freebsd.org/MicrosoftAzure](https://wiki.freebsd.org/MicrosoftAzure)

Microsoft HyperV 上的 FreeBSD Wiki 文章网址：[https://wiki.freebsd.org/HyperV](https://wiki.freebsd.org/HyperV)

联系人：Microsoft FreeBSD Integration Services 团队 [bsdic@microsoft.com](mailto:bsdic@microsoft.com)

联系人：freebsd-cloud 邮件列表

联系人：The FreeBSD Azure Release Engineering Team [releng-azure@FreeBSD.org](mailto:releng-azure@FreeBSD.org)

联系人：Wei Hu [whu@FreeBSD.org](mailto:whu@FreeBSD.org)

联系人：Souradeep Chakrabarti [schakrabarti@microsoft.com](mailto:schakrabarti@microsoft.com)

联系人：Li-Wen Hsu [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

在本季度，我们主要在 ARM64 架构支持以及构建和发布到 [Azure 社区库](https://learn.microsoft.com/azure/virtual-machines/share-gallery-community)的镜像方面进行了工作。项目的测试公共库中提供了一些测试镜像，命名为`FreeBSDCGTest-d8a43fa5-745a-4910-9f71-0c9da2ac22bf`：FreeBSD-CURRENT-testing FreeBSD-CURRENT-gen2-testing FreeBSD-CURRENT-arm64-testing

要使用它们，在创建虚拟机时： . 在 `Select an Image` 步骤中，在 `Other items` 中选择 `Community Images (PREVIEW)` . 搜索 `FreeBSD`

正在进行中的任务：

* 自动化镜像构建和发布过程，并合并到 src/release/。
* 构建和发布基于 ZFS 的镜像到 Azure Marketplace
* 所有所需的代码都合并到主分支，可以通过指定 VMFS=zfs 来创建基于 ZFS 的镜像。
* 需要将构建过程更加自动化，并与发布工程合作开始生成快照。
* 构建和发布 Hyper-V gen2 VM 镜像到 Azure Marketplace
* 构建和发布快照版本到 Azure 社区库

以上任务由 The FreeBSD Foundation 赞助，并由 Microsoft 提供资源。

Microsoft 的 Wei Hu 和 Souradeep Chakrabarti 正在进行由 Microsoft 赞助的几项任务：

* 将 Hyper-V 客户机支持移植到 aarch64 -[https://bugs.freebsd.org/267654](https://bugs.freebsd.org/267654) -[https://bugs.freebsd.org/272461](https://bugs.freebsd.org/272461)

待办任务：

* 更新 [Microsoft Learn](https://learn.microsoft.com/) 上与 FreeBSD 相关的文档
* 在 [Azure Pipelines](https://azure.microsoft.com/products/devops/pipelines/) 中支持 FreeBSD
* 将 [Azure 代理 port](https://www.freshports.org/sysutils/azure-agent)更新到最新版本
* 同步上游[本地修改 Azure 代理](https://github.com/Azure/WALinuxAgent/pull/1892)

赞助商：Microsoft 负责 Microsoft 人员的赞助和其他资源，The FreeBSD Foundation 负责其他方面的赞助。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 在 EC2 上的支持

链接：

FreeBSD/EC2 Patreon 网址：[https://www.patreon.com/cperciva](https://www.patreon.com/cperciva)

联系人：Colin Percival [cperciva@FreeBSD.org](mailto:cperciva@FreeBSD.org)

FreeBSD 可在 x86（Intel 和 AMD）和 ARM64（Graviton）EC2 实例上使用。继续努力确保即将推出的实例类型得到支持，包括最近宣布的 M7a“EPYC”实例，预计将在 FreeBSD 14.0-RELEASE 中得到支持。

最近，每周的 FreeBSD 快照从“UEFI”引导模式更改为“UEFI Preferred”引导模式，允许它们获得 UEFI 提供的引导性能改进，同时仍然支持与 UEFI 不兼容的“裸机”和“前代”实例类型。这一变化将在 FreeBSD 14.0-RELEASE 中出现。

EC2 引导脚本最近已更新以支持 IMDSv2。这一变化将在 FreeBSD 14.0-RELEASE 中出现。

如果 FreeBSD 13.2 的用户需要这些更新中的任何一项，作者可以提供 FreeBSD“13.2-RELEASE 加更新” AMI。

此工作得到 Colin 的 FreeBSD/EC2 Patreon 的支持。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 文档部分

文档、手册页面或新的外部书籍/文件中值得注意的变化。

#### 文档工程团队

链接：FreeBSD 文档项目 网址：[https://www.freebsd.org/docproj](https://www.freebsd.org/docproj)

链接：FreeBSD 文档项目新贡献者入门指南 网址：[https://docs.freebsd.org/en/books/fdp-primer/](https://docs.freebsd.org/en/books/fdp-primer/)

链接：文档工程团队 网址：[https://www.freebsd.org/administration/#t-doceng](https://www.freebsd.org/administration/#t-doceng)

联系人：FreeBSD 文档工程团队 [doceng@FreeBSD.org](mailto:doceng@FreeBSD.org)

doceng@ 团队负责处理与 FreeBSD 文档项目相关的一些元项目问题；有关更多信息，请参阅 [FreeBSD Doceng Team Charter](https://www.freebsd.org/internal/doceng/)（FreeBSD Doceng 团队章程）。

在本季度：

* 已任命 fernape@ 为新的 Doceng 团队成员。
* 由于 www/gohugo 是我们文档基础设施的关键部分，该 port 的维护权已转移到 doceng@。我们与前任维护者达成了一致意见。
* 改进了翻译工作流程（在下面的章节中描述）。

**Porter's Handbook（Port 开发者手册）**

已记录 [USES=nextcloud](https://cgit.freebsd.org/doc/commit/?id=634a34b7bb37650e4f8fcbea9fd7428b3f5b911a)。

**FDP Primer**

[FreeBSD 文档项目新贡献者入门指南](https://docs.freebsd.org/en/books/fdp-primer/weblate/)添加了一个新的章节，重点关注 Weblate。这个全面的章节提供了逐步指导，帮助加入 FreeBSD 翻译团队，无论是在线在 Weblate 上翻译还是离线。它提供了有关高效翻译、校对和测试过程的宝贵见解和实用建议。此外，这一章节还为贡献者提供了必要的知识，以正式提交他们的翻译到文档存储库，确保无缝集成他们的工作。

**FreeBSD 在 Weblate 上的翻译**

链接：在 Weblate 上翻译 FreeBSD 网址：[https://wiki.freebsd.org/Doc/Translation/Weblate](https://wiki.freebsd.org/Doc/Translation/Weblate)

链接：FreeBSD Weblate 实例 网址：[https://translate-dev.freebsd.org/](https://translate-dev.freebsd.org/)

2023 年第二季度状态

* 15 种语言
* 183 名注册用户
* [新的 Weblate 服务器](https://lists.freebsd.org/archives/freebsd-translators/2023-April/000111.html)

FreeBSD Weblate 实例现在运行在专用服务器上，大大提高了速度，并增强了翻译工作的效率。我们衷心感谢 ebrandi@提供的硬件升级。

语言

* 简体中文（zh-cn）（进度：7%）
* 繁体中文（zh-tw）（进度：3%）
* 荷兰语（nl）（进度：1%）
* 法语（fr）（进度：1%）
* 德语（de）（进度：1%）
* 印度尼西亚语（id）（进度：1%）
* 意大利语（it）（进度：5%）
* 韩语（ko）（进度：32%）
* 挪威语（nb-no）（进度：1%）
* 波斯语（fa-ir）（进度：3%）
* 波兰语（进度：1%）
* 葡萄牙语（pt-br）（进度：22%）
* 僧伽罗语（si）（进度：1%）
* 西班牙语（es）（进度：33%）
* 土耳其语（tr）（进度：2%）

我们要感谢所有贡献者，无论是翻译还是审查文档。

请帮助在您的当地用户组宣传这项工作，我们总是需要更多的志愿者。

**FreeBSD 手册工作组**

联系人：Sergio Carlavilla [carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)

[正在重新修订网络章节。](https://reviews.freebsd.org/D40546)

**FreeBSD 网站改版- WebApps 工作组**

联系人：Sergio Carlavilla [carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)

负责创建新的 FreeBSD 文档门户网站，并重新设计 FreeBSD 主网站及其组件的工作组。FreeBSD 开发人员可以在 FreeBSD Slack 频道# wg-www21 上关注和加入工作组。工作分为四个阶段：

* 文档门户的重新设计

创建一个新的设计，响应式设计，并具有全局搜索功能。（已完成）

* 网页上手册页面的重新设计

使用 mandoc 生成 HTML 页面的脚本。（已完成）在 [https://man-dev.FreeBSD.org](https://man-dev.freebsd.org) 上提供公共实例。

* 网页上 Ports 页面的重新设计

Ports 脚本以创建一个应用程序门户。（正在进行中）

* FreeBSD 主网站的重新设计

新设计，响应式设计和深色主题。（正在进行中）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Ports 部分

影响 Ports 的变化，无论是涉及大部分树的全面性变化，还是个别 port 本身的变化。

#### FreeBSD 上的 KDE

链接：

KDE/FreeBSD 计划网址：[https://freebsd.kde.org/](https://freebsd.kde.org/)

FreeBSD — KDE 社区维基网址：[https://community.kde.org/FreeBSD](https://community.kde.org/FreeBSD)

联系人：Adriaan de Groot [kde@FreeBSD.org](mailto:kde@FreeBSD.org)

KDE on FreeBSD 项目将 CMake、Qt 和来自 KDE 社区的软件打包到 FreeBSD 的 Ports 中。这些软件包括了一个完整的桌面环境，名为 KDE Plasma（适用于 X11 和 Wayland），以及数百个可在任何 FreeBSD 机器上使用的应用程序。

KDE 团队（kde@）是 desktop@和 x11@的一部分，构建软件堆栈，使 FreeBSD 成为漂亮且可用作日常图形桌面工作站的系统。下面的说明主要描述了与 KDE 有关的 port，但也包括整个桌面堆栈中重要的项目。

**基础设施**

Qt5 port 进行了各种更新：

* devel/qt5-webengine 在使用 Clang 16 进行构建时进行了修复。这是为了准备即将发布的 FreeBSD 14。
* devel/qt5-qmake 进行了修复，以解决在否则不安装 Qt 的系统上安装 qmake 会导致奇怪错误的问题。

Qt6 port 进行了各种更新：

* devel/qt6-tools 在使用 Clang 16 进行构建时进行了修复。这是为了准备即将发布的 FreeBSD 14。

accessibility/at-spi2-core port ——桌面上的辅助技术的重要组成部分——更新到版本 2.48.0。

accessibility/at-spi2-core port 现在更好地支持非 X11 桌面。这对于基于 Wayland 的系统是一个改进。感谢 Jan Beich 的工作。

graphics/poppler port ——许多 PDF 查看器的基础——更新到版本 23.05。

ports-mgmt/packagekit-qt port 是新添加的，为 FreeBSD 上的图形化包管理器铺平了道路。

**KDE 堆栈**

KDE Gear 每个季度发布，KDE Plasma 每月更新，KDE Frameworks 每月发布一次。这些（大规模）更新在其上游发布后不久就会实现，不会单独列出。

* KDE Frameworks 更新至 5.105、.106 和.107。
* KDE Gear 更新至 23.04.0，然后是.1 和.2，包含错误修复。
* KDE Plasma Desktop 更新至版本 5.27.4，然后是.5 和.6，包含错误修复。

**相关 port**

弃用：

* graphics/ikona，一个使用 Rust 和 Qt 绑定编写的图标查看器，已经被上游弃用。
* polish/kadu，曾在波兰很受欢迎的聊天应用程序，已被弃用，上游消失了。
* sysutils/plasma5-ksysguard，一个系统监控应用程序，已经被上游弃用，将不再更新。

更新：

* astro/kstars，一个交互式天文馆，更新至版本 3.6.4。
* devel/qcoro，一个 C++ 协程实现，更新至版本 0.9.0。
* devel/qtcreator，一个用于 Qt、C++ 等的集成开发环境，更新至版本 10.0.2。
* games/gcompris-qt，一个针对 3-12 岁儿童的教育套件，更新至版本 3.2。
* graphics/kphotoalbum，一个照片相册和显示实用程序，更新至版本 5.10.0。
* net-im/tokodon，一个 Mastodon 社交网络客户端，加入了 KDE Gear。
* textproc/kdiff3，一个文本差异工具，更新至版本 1.10.1。

新增软件：

* devel/kommit，一个 Git 客户端，已添加。它是先前 gitklient 的改名。
* multimedia/kasts 是 KDE 社区的一个新的播客收听和享受应用程序。
* textproc/arianna 是 KDE 社区的一款面向移动设备的电子书阅读器，使阅读 FreeBSD 文档变得愉悦。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 在 FreeBSD 上的 GCC

链接：

GCC 项目 网址：[https://gcc.gnu.org/](https://gcc.gnu.org/)

GCC 10 版本系列 网址：[https://gcc.gnu.org/gcc-10/](https://gcc.gnu.org/gcc-10/)>

GCC 11 版本系列 网址：[https://gcc.gnu.org/gcc-11/](https://gcc.gnu.org/gcc-11/)

GCC 12 版本系列 网址：[https://gcc.gnu.org/gcc-12/](https://gcc.gnu.org/gcc-12/)

GCC 13 版本系列 网址：[https://gcc.gnu.org/gcc-13/](https://gcc.gnu.org/gcc-13/)

联系人：Lorenzo Salvadore [salvadore@FreeBSD.org](mailto:salvadore@FreeBSD.org)

上游发布了 [GCC 13](https://gcc.gnu.org/gcc-13)。如前面的状态报告中宣布的，我计划尝试在第一个 GCC 13 版本中更新 GCC\_DEFAULT，因此本季度的大部分工作都是为此做准备。

随着 GCC 13.1 的发布（第一个 GCC 13 版本：我提醒一下，GCC 从 1 开始计算小版本号），在 ports 中创建了两个新 port：

lang/gcc13，跟踪 GCC 13 版本；

lang/gcc14-devel，跟踪新的 GCC 14 上游分支的快照。

**\*-devel port**

已启用对 .init\_array 和 .fini\_array 的支持。FreeBSD 自 [83aa9cc00c2d](https://cgit.freebsd.org/src/commit/?id=83aa9cc00c2d83d05a0efe7a1496d8aab4a153bb) 提交开始就支持这两个功能。

i386、amd64 和 aarch64 上的默认 bootstrap 选项从 LTO\_BOOTSTRAP 回滚为 STANDARD\_BOOTSTRAP：

* LTO 引导在这些架构上产生了太多的失败
* 对于希望使用 LTO\_BOOTSTRAP 的用户，LTO\_BOOTSTRAP 仍然可用。

这些更改将被应用到生产 port 中。

**生产 port**

上游已发布了 GCC 13，为此创建了新 port lang/gcc13。GCC 11 和 GCC 12 已在上游更新，计划发布 GCC 10 的新版本。现在需要更新所有相应的 port。

为了方便 port 维护者和用户的工作，我计划同时测试和更新以下所有更改：

* 更新 lang/gcc10、lang/gcc11、lang/gcc12；
* 将 GCC\_DEFAULT 更新为 13；
* 在生产 port 上启用.init\_array 和.fini\_array；
* 将生产 port 从 LTO\_BOOTSTRAP 切换回 STANDARD\_BOOTSTRAP。

这将带来以下优势：

* 更少的 exp 运行进行更多的测试；
* 对于 ports 用户来说，需要的构建更少。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### Puppet

链接：

Puppet 网址: [https://puppet.com/docs/puppet/latest/puppet\_index.html](https://puppet.com/docs/puppet/latest/puppet\_index.html)

联系人：Puppet 团队 [puppet@FreeBSD.org](mailto:puppet@FreeBSD.org)

Puppet 是一款自由软件的配置管理工具，由一个可信的源（Puppet Server）组成，它用领域特定语言描述机器的预期配置，以及在每个节点上运行的代理（Puppet Agent），用于强制实际配置与预期配置相匹配。可以设置一个可选的数据库（PuppetDB）用于报告和描述高级模式，其中一个机器的配置依赖于另一个机器的配置。

Puppet 团队正在维护 Puppet 和相关工具的 ports。

最近发布了 Puppet 8，并已添加到 ports 树中。

Puppet 6 已达到生命周期终点，并已被弃用。它现在已过期。因此，建议使用 Puppet 6 的用户更新到 Puppet 7 或 Puppet 8。

目前，Puppet 7 仍然是 ports 中依赖于 Puppet 的 port 的默认版本。Puppet 社区正在努力确保各种 Puppet 模块与最新代码兼容，在撰写本报告时，更新到 Puppet 8 可能会有一些挑战。情况每天都在好转，我们预计在几个月后，当模块更新的浪潮结束时，将切换到 Puppet 8 作为 Puppet 的默认版本。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### MITRE Caldera 在 FreeBSD 上的支持

链接：

MITRE Caldera 网址: [https://caldera.mitre.org/](https://caldera.mitre.org/)

Red Canary 网址: [https://www.redcanary.com/](https://www.redcanary.com/)

联系人：José Alonso Cárdenas Márquez [acm@FreeBSD.org](mailto:acm@FreeBSD.org)

MITRE Caldera 是一个网络安全平台，旨在轻松自动化对手仿真，协助手动红队活动，并自动化事件响应。

它建立在 MITRE ATT\&CK® 框架上，是 MITRE 的一个积极研究项目。

MITRE Caldera（security/caldera）于 2023 年 4 月添加到了 ports 中。这个 port 包含了对 [MITRE Caldera atomic 插件](https://github.com/mitre/atomic)使用的 [Atomic Red Team 项目](https://github.com/redcanaryco/atomic-red-team)的支持。

这项工作的主要目标是提高 FreeBSD 作为信息安全或网络安全有用平台的可见性。

此外，您可以使用 [https://github.com/alonsobsd/caldera-makejail](https://github.com/alonsobsd/caldera-makejail) 或 [https://github.com/AppJail-makejails/caldera](https://github.com/AppJail-makejails/caldera) 来测试MITRE Caldera 基础设施。AppJail 是一个用于从命令行管理 jail 容器的好工具。

欢迎有兴趣参与该项目的人提供帮助。

当前版本：4.2.0

**待办事项：**

* 添加 Caldera 测试基础设施 makejail。
* 将 FreeBSD 添加到 MITRE Caldera 官方支持的平台中，请参见 [https://github.com/mitre/caldera/pull/2752。](https://github.com/mitre/caldera/pull/2752%E3%80%82)
* 将 FreeBSD 添加到 Red Canary 官方支持的平台中，请参见 [https://github.com/redcanaryco/atomic-red-team/pull/2450。](https://github.com/redcanaryco/atomic-red-team/pull/2450%E3%80%82)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### Wazuh 在 FreeBSD 上的支持

链接：

Wazuh 网址: [https://www.wazuh.com/](https://www.wazuh.com/)

联系人：José Alonso Cárdenas Márquez [acm@FreeBSD.org](mailto:acm@FreeBSD.org)

Wazuh 是一个免费且开源的平台，用于威胁预防、检测和响应。它能够保护在本地部署、虚拟化、容器化和云环境中的工作负载。

Wazuh 解决方案由部署在被监控系统上的终端安全代理和收集和分析代理收集的数据的管理服务器组成。Wazuh 的特性包括与 Elastic Stack 和 OpenSearch 的完全集成，通过这些工具，用户可以浏览安全警报。

Wazuh 在 FreeBSD 上的移植由 Michael Muenz 开始。他在 2021 年 9 月将 Wazuh 首次添加到 ports 树中，即 security/wazuh-agent。在 2022 年 7 月，我接手了这个 port 的维护，并开始移植其他 Wazuh 组件。

目前，所有的 Wazuh 组件都已经移植或适配：security/wazuh-manager、security/wazuh-agent、security/wazuh-server、security/wazuh-indexer 和 security/wazuh-dashboard。

在 FreeBSD 上，security/wazuh-manager 和 security/wazuh-agent 是从 Wazuh 源代码编译而来的。security/wazuh-indexer 是一个适配后的 textproc/opensearch，用于存储代理数据。security/wazuh-server 包含针对 FreeBSD 的配置文件适配。运行时依赖项包括 security/wazuh-manager、sysutils/beats8 (filebeat) 和 sysutils/logstash8。security/wazuh-dashboard 使用了一个适配后的 textproc/opensearch-dashboards 和从 wazuh-kibana-app 源代码生成的 FreeBSD 版本的 wazuh-kibana-app 插件。

这项工作的主要目标是提高 FreeBSD 作为信息安全或网络安全有用平台的可见性。

此外，您可以使用 [https://github.com/alonsobsd/wazuh-makejail](https://github.com/alonsobsd/wazuh-makejail) 或 [https://github.com/AppJail-makejails/wazuh](https://github.com/AppJail-makejails/wazuh) 来轻松测试 Wazuh 单节点基础设施（All-in-one）。AppJail 是一个用于从命令行管理 jail 容器的好工具。

欢迎有兴趣参与该项目的人提供帮助。

当前版本：4.4.4

**待办事项：**

* 添加 Wazuh 集群模式基础设施 makejail（正在进行中）
* 将 FreeBSD 添加到 Wazuh Inc 官方支持的平台中，请参见 [https://github.com/wazuh/wazuh-kibana-app/pull/5413](https://github.com/wazuh/wazuh-kibana-app/pull/5413)
* 添加 FreeBSD SCA 策略（正在进行中）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 第三方项目

许多项目构建在 FreeBSD 之上或将 FreeBSD 组件纳入其项目中。由于这些项目可能对更广泛的 FreeBSD 社区感兴趣，因此我们有时在季度报告中包含这些项目提交的简要更新。FreeBSD 项目对这些提交中的任何声明的准确性或真实性不作任何陈述。

#### PkgBase.live

链接：

网站网址: [https://alpha.pkgbase.live/](https://alpha.pkgbase.live/)

源代码网址: [https://codeberg.org/pkgbase](https://codeberg.org/pkgbase)

联系人：Mina Galić [freebsd@igalic.co](mailto:freebsd@igalic.co)

PkgBase.live，一个非官方的 FreeBSD [PkgBase 项目存储库](https://wiki.freebsd.org/PkgBase)，已经恢复正常运行。

PkgBase.live 这项服务灵感来自于 [https://up.bsd.lv/](https://up.bsd.lv/)，它为 STABLE 和 CURRENT 分支提供了 freebsd-update(8) 的服务。up.bsd.live 本身已经暂停运行，所以这就更有理由重新启动 PkgBase.live。

目前，我们为以下平台提供构建：

* FreeBSD 13.2-RELEASE
* FreeBSD 13-STABLE
* FreeBSD 14-CURRENT

每个平台又分为以下架构：

* amd64
* aarch64
* armv7
* i386

你可能会注意到 RISCv64 目前暂时不可用。

硬件是在 Vultr 上的一台强大的 VPS。服务器和运行构建作业和提供软件包的 jail 是“自托管”的，这意味着它们安装并且保持更新，使用的是 PkgBase。

由于我们还没有弄清楚如何在 FreeBSD jails 中配置 Vultr 的 IPv6，PkgBase.live 目前不支持 IPv6。如果您对此有经验，请与我们联系！

除了用户和测试者外，我们仍然[非常鼓励其他人进行复制和模仿](https://alpha.pkgbase.live/howto/howdo.html)。

PkgBase 的硬件由 FreeBSD 社区的一名成员慷慨赞助。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 容器和 FreeBSD：Pot、Potluck 和 Potman

链接：

Pot 在 GitHub 上的组织 网址: [https://github.com/bsdpot](https://github.com/bsdpot)

联系人：Luca Pizzamiglio (Pot) [pizzamig@FreeBSD.org](mailto:pizzamig@FreeBSD.org)

联系人：Bretton Vine (Potluck) [bv@honeyguide.eu](mailto:bv@honeyguide.eu)

联系人：Michael Gmelin (Potman) [grembo@FreeBSD.org](mailto:grembo@FreeBSD.org)

Pot 是一个[支持通过 Nomad](https://www.freebsd.org/news/status/report-2020-01-2020-03/#pot-and-the-nomad-pot-driver) 进行编排的 FreeBSD Jail 管理工具。

在本季度，发布了 [Pot 0.15.5](https://github.com/bsdpot/pot/releases/tag/0.15.5) 版本，其中包含了一些来自多位贡献者的错误修复和特性，用于设置属性（[即 Jail 的 sysctl 变量](https://github.com/bsdpot/pot/pull/263)）。它将在 2023Q3 季度软件包集中提供。

Potluck 的目标是成为 FreeBSD 和 Pot 的 Dockerhub：一个 Pot 流派和完整容器映像的存储库，可在 Pot 中使用，并在许多情况下支持 Nomad。

所有 Potluck 容器都已重新构建为基于 FreeBSD 13.2 的映像，并使用 Pot signify 进行签名。

编写了《[使用 Ansible、Pot 等在 FreeBSD 上构建虚拟数据中心的初学者指南](https://honeyguide.eu/posts/ansible-pot-foundation/)》，其中解释了如何使用 Ansible playbooks 部署基于 Pot 和 Potluck 的复杂环境，包括示例节点（如 MariaDB、Prometheus、Grafana、nginx、OpenLDAP 或 Traefik），以及由 Nomad 和 Consul 管理的容器编排。

[Pot 团队提交的一个改进 Nomad 安全性的补丁](https://github.com/hashicorp/nomad/pull/13343)（Nomad 是支持通过 sysutils/nomad-pot-driver 进行 Pot 编排的调度程序和编排工具）已被上游接受，并将成为 Nomad 1.6.0 的一部分。

如常，欢迎提供反馈和补丁。

赞助商：Honeyguide Group



