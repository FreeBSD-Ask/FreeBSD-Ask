# 第 0.4 节 FreeBSD 发行说明

> FreeBSD 的生命周期为每个大版本 5 年，小版本是发布新的小版本版后 +3 个月。
>
> FreeBSD 14 开发计划 [https://github.com/bsdjhb/devsummit/blob/main/14.0/planning.md](https://github.com/bsdjhb/devsummit/blob/main/14.0/planning.md)


## FreeBSD 2023 年第二季度 季度状况报告

这是第二份 2023 年状态报告，共有 37 个条目。

正如您可能注意到的，我们比上个季度有更多的报告。这是个好消息，也显示了 FreeBSD 社区的活跃程度，他们一直在努力提供高质量的软件。

特别需要注意的是，夏季已经开始了，请不要错过由我们的 Google Summer of Code 学生分享的令人惊叹的项目。

祝您阅读愉快。

Lorenzo Salvadore，代表 Status 团队。
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- FreeBSD 团队报告
  - FreeBSD 核心团队
  - FreeBSD 基金会
  - FreeBSD 发布工程团队
  - 集群管理团队
  - 持续集成
  - Ports
- 项目
  - Cirrus-CI
  - FreeBSD 内核中的 BATMAN 支持
  - LinuxBoot 上的 FreeBSD 支持
- 用户空间
  - 基于 OpenSSL 3 的更新
  - Linux 兼容层更新
  - 服务 Jail-自动将 rc.d 服务置于监狱中
  - 使用 ktrace(1)进行安全隔离
  - NVMe over Fabrics
- 内核
  - 启动性能改进
  - 引导加载程序的 CI 测试工具
  - FreeBSD 内核的物理内存压缩
  - 增加 MAXCPU
  - FreeBSD 内核的 SquashFS 移植
  - Pf 改进
  - 网络接口 API（IfAPI）
  - 使 Netgraph 无锁化
- 架构
  - AMD64 的 SIMD 增强
  - 将 mfsBSD 集成到发布构建工具中
- 云计算
  - FreeBSD 作为 Tier 1 的 cloud-init 平台
  - FreeBSD 上的 OpenStack
  - FreeBSD 在 Microsoft HyperV 和 Azure 上
  - FreeBSD 在 EC2 上
- 文档
  - 文档工程团队
- ports
  - FreeBSD 上的 KDE
  - FreeBSD 上的 GCC
  - Puppet
  - FreeBSD 上的 MITRE Caldera
  - FreeBSD 上的 Wazuh
- 第三方项目
  - PkgBase.live
  - 容器和 FreeBSD：Pot，Potluck 和 Potman

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### FreeBSD 团队报告
以下是来自各个官方和半官方团队的条目，这些信息可以在[管理页面](https://www.freebsd.org/administration/)找到。

#### FreeBSD 核心团队
联系方式：FreeBSD 核心团队 <core@FreeBSD.org>

FreeBSD 核心团队是 FreeBSD 的管理机构。

**202305 开发者峰会**

核心团队在 2023 年 5 月 17 日至 18 日的 FreeBSD 开发者峰会上进行了状态更新的展示。可在<https://wiki.freebsd.org/DevSummit/202305> 上查看幻灯片。

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

FreeBSD 基金会网址：<https://www.freebsdfoundation.org>

技术路线图网址：<https://freebsdfoundation.org/blog/technology-roadmap/>

捐赠网址：<https://www.freebsdfoundation.org/donate/>

基金会合作计划网址：<https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/>

FreeBSD 杂志网址：<https://www.freebsdfoundation.org/journal/>

基金会新闻和活动网址：<https://www.freebsdfoundation.org/news-and-events/>

联系人：Deb Goodkin <deb@FreeBSDFoundation.org>

FreeBSD 基金会是一个 501(c)(3) 非营利组织，致力于在全球支持和推广 FreeBSD 项目和社区。个人和公司的捐赠用于资助和管理软件开发项目、会议和开发者峰会。我们还为 FreeBSD 贡献者提供差旅补助，购买和支持硬件以改善和维护 FreeBSD 基础设施，并提供资源来改进安全性、质量保证和发布工程工作。我们发布营销材料以推广、教育和支持 FreeBSD 项目，促进商业供应商和 FreeBSD 开发者之间的合作，并最终代表 FreeBSD 项目执行合同、许可协议和其他需要被认可的法律安排。

**祝 FreeBSD 30 岁生日快乐！**

我们自豪地支撑这个出色的操作系统和充满活力的社区已经超过 23 年了，并且我们热切期待在未来的多年里继续支持它们。在本次报告中，我们将概述我们在多个领域对 FreeBSD 的贡献。我们将涉及一些具有详细报告的项目开发倡议。此外，我们还将展示我们对 FreeBSD 的支持、促进社区参与的努力以及扩大合作伙伴关系的努力。最后，我们将深入探讨我们持续增加资金的工作，以便在项目中填补更多的差距。

**筹款**

在这个季度，我们在与 FreeBSD 商业用户进行合作方面取得了重大进展。为了加强与现有和潜在商业用户的合作伙伴关系，我们聘请了 Greg Wallace 担任合作伙伴和研究总监。他的主要目标是扩大我们与商业用户的合作。自担任该职务以来，Greg 已经开始着手工作，仅在一个季度内就与众多公司进行了会面。这些互动为我们了解 FreeBSD 的使用情况、用户面临的挑战以及项目可以改进的领域提供了宝贵的见解。通过了解这些方面，我们可以做出明智的决策，确定在哪些方面投入资金，并认识到 FreeBSD 的独特优势。此外，这个角色还包括进行研究，以确定目标市场，探索 FreeBSD 的新机会，并确保我们的声音在相关讨论中得到听取。有关 Greg 的目标和成就的更多详细信息，请参阅他下面的状态更新。

基金会向所有对我们的工作作出财务捐赠的人表示衷心的感谢。除了许多个人捐赠外，我们还很高兴收到 NetApp 和 Blackberry 的较大捐赠。此外，我们还从 Tarsnap、iXsystems 和 LPI 获得了 FreeBSD 开发者峰会的赞助。这些赞助在抵消我们的费用方面提供了极大的帮助，并使我们能够向参与者提供实惠的注册费用。

今年我们的预算约为 2,230,000 美元，其中包括增加用于 FreeBSD 推广和软件开发的支出。我们预算的一半以上用于直接改进 FreeBSD 并保持其安全性。

通过有一个专门负责合作伙伴关系的人，我们可以有效地强调投资我们的努力的重要性，并强调项目的长期可行性。

您的支持在我们的使命中发挥着至关重要的作用，我们深表对您对 FreeBSD 社区的承诺表示感谢。请考虑向我们的 2023 年筹款活动捐款！<https://www.freebsdfoundation.org/donate/>

对于更重要的商业捐赠者，我们还有 [FreeBSD 基金会合作计划](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/)，该计划成立于 2017 年。

**合作计划**

大家好，我是 Greg Wallace。我于四月初加入基金会，担任合作伙伴关系和研究总监。[这篇博客介绍了我和我的角色](https://freebsdfoundation.org/blog/freebsd-foundation-welcomes-new-team-members/)。对于合作伙伴关系，我的重点是与使用 FreeBSD 的公司建立联系。我已经与几家公司会面，了解他们如何使用 FreeBSD。其中一些会面已经引发了有关潜在合作伙伴关系的讨论。我继续了解使用 FreeBSD 的有趣公司，并与他们取得联系。

我的目标是与每一家使用和构建 FreeBSD 的公司取得联系，倾听他们的故事。如果您是其中之一，而我们尚未建立联系，请在我的[日历](https://calendly.com/greg-freebsdfound/30min)上安排一次会话。

本季度其他合作伙伴关系相关活动：

- 我创建了关于如何与基金会合作推进 FreeBSD 的[幻灯片](https://docs.google.com/presentation/d/1tDCpbfxbqIucmJF6H15vK-ETrQsCMOVtxoqLem_V0Z0/edit?usp=sharing)。如果您对如何改进这些幻灯片有任何想法，或者希望我向您的组织介绍这些内容，请给我发送[电子邮件](greg@freebsdfoundation.org)或[安排通话](https://calendly.com/greg-freebsdfound/30min)。并且请随意自由地分享这份演示文稿，无论全部还是部分内容。
- 我与基金会的同事合作，为向行业分析师进行演示准备了许多特定行业的用例幻灯片。
- 我还在寻求与以下机构的资助机会：
  - NSF 安全可信的网络空间（SaTC）
  - Sovereign Tech 基金
  - NGI。

在研究方面，我的广泛目标是确保这个社区的所有专业知识都能在全球关于计算性能、安全性和能源效率的对话中得到体现。作为一个社区，我们在这项工作中有很多贡献可以提供。

到目前为止，我一直在跟踪和参与以下主题：

- [Open Forum Europe](https://openforumeurope.org/open-source/)
- [CHIPS 研究与开发](https://www.nist.gov/chips/research-and-development-program)。

如果您对研究方面有想法，或者对在这个领域合作感兴趣，请[给我发送电子邮件](greg@freebsdfoundation.org)或[安排通话](https://calendly.com/greg-freebsdfound/30min)。

**操作系统改进**

在 2023 年第二季度，共有 339 个 src 提交，155 个 ports 提交和 20 个文档提交被认定为由 FreeBSD 基金会赞助。关于一些由基金会赞助的工作以及其他工作的描述在单独的报告条目中：

- 持续集成
- FreeBSD 作为 Tier 1 的 cloud-init 平台
- 基于 OpenSSL 3 的更新
- FreeBSD 上的 OpenStack
- 使用 ktrace(1)进行安全隔离
- AMD64 的 SIMD 增强

以下是其他由基金会赞助的工作的一部分：

- fsck_ffs(8)的错误修复
- killpg(2)的错误修复
- hwpmc 的改进
- vmm 的改进
- 针对 LLVM 16 和 OpenSSL 3.0 的 port 修复和解决方案
- 将 kinst 移植到 RISC-V 以及相关的 DTrace 工作
- 将 libfido2 更新到 1.9.0 版本
- 各种 LinuxKPI 802.11 的改进
- 各种 RISC-V 的改进
- 从版本 4.9.3 升级到版本 4.99.4 的 tcpdump 的供应商导入和更新。

关于当前和过去由基金会承包的工作的状态，可以在[基金会项目页面上](https://freebsdfoundation.org/our-work/projects/)查看。

基金会技术团队的成员在加拿大渥太华举行的开发者峰会上进行了演讲。这包括主持谷歌代码之夏、[FreeBSD 基金会技术审查](https://wiki.freebsd.org/DevSummit/202305?action=AttachFile&do=view&target=FreeBSD_Foundation_Devsummit_Spring_2023_Day_2_part1.pdf)和[工作流](https://docs.google.com/presentation/d/e/2PACX-1vSnEW5Z0ttQOAeqEEY8KHkfiRGeFUm4i8XrYsfY8TNYD%E2%80%94%E2%80%8Byx1P6MUu2_u-mCcpe6PMMITjeDIgT31CC/pub)工作组会议。Pierre Pronchery 谈到了 [BSD 之间的驱动程序兼容性](https://www.bsdcan.org/events/bsdcan_2023/schedule/speaker/89-pierre-pronchery/)问题，而 En-Wei Wu 则讨论了在与基金会签订的合同下完成的 [wtap 工作](https://www.bsdcan.org/events/bsdcan_2023/schedule/session/139-add-operating-modes-to-wtap4/)。

**持续集成和质量保证**

基金会提供了全职员工和资金，用于改进 FreeBSD 项目的持续集成、自动化测试和整体质量保证工作。您可以在专用的报告条目中了解更多关于持续集成工作的内容。

**宣传**

我们的很多工作都致力于推广 FreeBSD 项目。这可能涉及突出显示有趣的 FreeBSD 工作、制作文献和视频教程、参加活动或进行演讲。我们制作的文献的目标是教授人们 FreeBSD 的基础知识，并帮助他们更轻松地采用或贡献。除了参加和演讲活动外，我们鼓励并帮助社区成员举办自己的 FreeBSD 活动、进行演讲或管理 FreeBSD 展台。

FreeBSD 基金会赞助全球范围内的许多会议、活动和峰会。这些活动可能与 BSD 相关，也可能是面向弱势群体的开源或技术活动。我们支持以 FreeBSD 为重点的活动，以便为知识分享、项目合作和开发者与商业用户之间的合作提供场所。这些都有助于提供一个健康的生态系统。我们支持非 FreeBSD 活动，以促进和提高 FreeBSD 的认知度，增加在不同应用中使用 FreeBSD 的程度，并吸引更多的项目贡献者。我们很高兴恢复了大多数以亲自参加活动。除了参加和计划活动外，我们还在不断努力推进新的培训计划，并更新我们的[指南](https://freebsdfoundation.org/freebsd-project/resources/)，以鼓励更多的人尝试 FreeBSD。

以下是我们进行的一些倡导和教育工作：

- 协助组织并参加了于 2023 年 5 月 17 日至 18 日在加拿大安大略省渥太华举行的[开发者峰会](https://wiki.freebsd.org/DevSummit/202305)
- 在于 2023 年 5 月 17 日至 20 日在加拿大安大略省渥太华举行的 BSDCan 活动中，主持了一个展台，并担任 Tote Bag 赞助商
  - 可以在[博客](https://freebsdfoundation.org/our-work/latest-updates/)上找到相关行程报告
- 在 BSDCan 庆祝了项目的 [30 周岁生日](https://freebsdfoundation.org/past-issues/freebsd-30th-anniversary-special-edition/)，并提供了特别版本的 FreeBSD 杂志的印刷本
- 成功争取到于 2023 年 7 月 13 日至 16 日在美国俄勒冈州波特兰举行的 [FOSSY](https://sfconservancy.org/fossy/) 上举办 FreeBSD 研讨会和演讲
- 成功争取到于 2023 年 9 月 14 日至 17 日在葡萄牙科英布拉举办的 [EuroBSDCon 2023](https://2023.eurobsdcon.org/) 的银牌赞助
- 成功争取到于 2023 年 10 月 15 日至 17 日在美国北卡罗来纳州罗利举办的 [All Things Open](https://2023.allthingsopen.org/) 的展位
- 开始筹划 FreeBSD 秋季供应商峰会
- 欢迎两名[新团队成员](https://freebsdfoundation.org/blog/freebsd-foundation-welcomes-new-team-members/)：Greg Wallace 和 Pierre Pronchery
- 发布了[四月](https://freebsdfoundation.org/news-and-events/newsletter/freebsd-foundation-update-april-2023/)和[六月](https://freebsdfoundation.org/news-and-events/newsletter/12518/)的新闻通讯
- 在 6 月 19 日庆祝了 [FreeBSD 日](https://freebsdfoundation.org/national-freebsd-day/)和项目的 30 周年，并在整个周内发布了特别的视频和博客文章
- 其他博客文章：
  - [EuroBSDcon 2023 旅行津贴申请现已开放](https://freebsdfoundation.org/blog/eurobsdcon-2023-travel-grant-application-now-open/)-请注意：申请将于 2023 年 8 月 2 日截止
  - [AsiaBSDcon 行程报告](https://freebsdfoundation.org/blog/asiabsdcon-2023-trip-report/)
- FreeBSD 在新闻中：
  - [InfoWorld：FreeBSD 30 岁生日快乐！](https://freebsdfoundation.org/news-and-events/latest-news/infoworld-happy-30th-freebsd/)

我们通过发布专业制作的 FreeBSD 杂志来丰富全世界关于 FreeBSD 的知识。正如我们之前提到的，FreeBSD 杂志现在是免费发布的。您可以在<https://www.freebsdfoundation.org/journal/> 了解更多信息并访问最新的期刊。

您可以在 <https://www.FreeBSDfoundation.org/news-and-events/> 了解有关我们参加的活动和即将举行的活动的更多信息。

**法律/FreeBSD 知识产权**

基金会拥有 FreeBSD 商标，并有责任保护它们。我们还为核心团队提供法律支持，以调查涉及的问题。

您可以在 <https://www.freebsdfoundation.org> 找到更多关于我们如何支持FreeBSD以及我们如何帮助您的信息！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 发布工程团队
链接：

FreeBSD 13.2-RELEASE 日程网址：<https://www.freebsd.org/releases/13.2R/schedule/>

FreeBSD 14.0-RELEASE 日程网址：<https://www.freebsd.org/releases/14.0R/schedule/>

FreeBSD 发行版本网址：<https://download.freebsd.org/releases/ISO-IMAGES/>

FreeBSD 开发快照网址：<https://download.freebsd.org/snapshots/ISO-IMAGES/>


联系人：FreeBSD 发布工程团队 <re@FreeBSD.org>

FreeBSD 发布工程团队负责制定和发布 FreeBSD 官方项目版本的发布计划，宣布代码冻结并维护相应的分支，等等。

在 2023 年第二季度，团队继续进行了 13.2-RELEASE 的工作。13.2 周期紧密遵循了设定的日程安排，在最后增加了三个额外的 RC 构建，在 4 月中旬发布了最终的 RELEASE 构建并进行了宣布。

与项目管理中的各个团队协调，FreeBSD 发布工程团队重新考虑了即将到来的 14.0-RELEASE 的原始计划，主要是因为有进行中的工作。更新后的计划经过讨论并稍作调整以考虑一些问题，并最终在 FreeBSD 项目网站上发布。新的计划将 14.0-RELEASE 定于 2023 年 10 月。

团队继续为 `main` 分支、`stable/13` 分支和 `stable/12` 分支提供每周开发快照构建。请注意，`stable/12` 分支将不再提供快照构建。

赞助者：Tarsnap 赞助者：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 集群管理团队

链接：

FreeBSD 集群管理团队成员网址：<https://www.freebsd.org/administration/#t-clusteradm>

联系人：FreeBSD 集群管理团队 clusteradm@FreeBSD.org

FreeBSD 集群管理团队负责管理项目依赖的机器，用于同步分布式工作和通信。

在本季度，该团队完成了以下工作：

- 定期支持 FreeBSD.org 用户帐户。
- 为所有物理主机和镜像提供定期磁盘和零件支持（和更换）。
- 在 FreeBSD 项目管理的镜像中启用了 <https://www.FreeBSD.org> 和 <https://docs.FreeBSD.org> 的镜像。
- 对所有主机和容器进行了集群刷新，将它们升级到最新版本的 14-CURRENT、13-STABLE 和 12-STABLE。

**正在进行的工作：**

- 主要站点进行大规模网络升级。
  - 在主要站点，新的 [Juniper](https://www.juniper.net/) 交换机已经到货，以替换以前的交换机。我们感谢 Juniper 的捐赠。
- 在主要站点和一些镜像站点上替换旧服务器。
  - 除了损坏的持续集成服务器，我们还有一些老旧的服务器，有磁盘损坏和故障的电源供应器。这项任务是与 FreeBSD 基金会以及捐赠者/赞助商一起进行的。
- 安装从软件包构建机转用的新持续集成（CI）机器。
- 审查在 FreeBSD 集群运行的服务的备份配置。

**FreeBSD 官方镜像概述**

当前的位置是澳大利亚、巴西、德国、日本（两个完整的镜像站点）、马来西亚、南非、台湾、英国（完整的镜像站点）、美国加利福尼亚州、新泽西州（主要站点）和华盛顿州。

这些硬件和网络连接是由以下机构慷慨提供的：

- [Bytemark Hosting](https://www.bytemark.co.uk/)
- [BroadBand Tower](https://www.bbtower.co.jp/en/corporate/)，Inc 的云和 SDN 实验室
- [国立阳明交通大学计算机科学系](https://www.cs.nycu.edu.tw/)
- [Equinix](https://deploy.equinix.com/)
- [澳大利亚互联网协会](https://internet.asn.au/)
- [Internet Systems Consortium](https://www.isc.org/)
- [INX-ZA](https://www.inx.net.za/)
- [KDDI Web Communications Inc](https://www.kddi-webcommunications.co.jp/english/)
- [马来西亚研究与教育网络](https://www.mohe.gov.my/en/services/research/myren)
- [Metapeer](https://www.metapeer.com/)
- [NIC.br](https://www.metapeer.com/)
- [Your.Org](https://your.org/)
- [365 数据中心](https://365datacenters.com/)

法兰克福单服务器镜像是欧洲带宽和使用率最高的主要镜像。

我们仍在寻找一个额外的完整镜像站点（五个服务器）在欧洲来替换英国的旧服务器。

我们发现在全球范围内的互联网交换点（澳大利亚、巴西和南非）拥有单一的镜像是一个很好的模式；如果您了解或为其中的一些公司工作，他们可以赞助一个单一的镜像服务器，请与我们联系。美国（西海岸）和欧洲（任何地方）是较为理想的地点。

有关完整镜像站点规格的通用镜像布局，请参阅 [full mirror site specs](https://wiki.freebsd.org/Teams/clusteradm/generic-mirror-layout)，有关单一镜像站点的信息，请参阅 [tiny-mirror](https://wiki.freebsd.org/Teams/clusteradm/tiny-mirror)。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#### 持续集成
链接：

FreeBSD Jenkins 实例网址：<https://ci.FreeBSD.org>

FreeBSD CI artifact 存档网址：<https://artifact.ci.FreeBSD.org>

FreeBSD Jenkins Wiki 网址：<https://wiki.FreeBSD.org/Jenkins>

托管 CI Wiki 网址：<https://wiki.FreeBSD.org/HostedCI>

第三方软件 CI 网址：<https://wiki.FreeBSD.org/3rdPartySoftwareCI>

与 freebsd-testing@相关的票务网址：<https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=open&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals>

FreeBSD CI 存储库网址：<https://github.com/freebsd/freebsd-ci>

dev-ci 邮件列表网址：<https://lists.FreeBSD.org/subscription/dev-ci>

联系人：Jenkins 管理员 <jenkins-admin@FreeBSD.org>

联系人：Li-Wen Hsu <lwhsu@FreeBSD.org>

联系人：freebsd-testing 邮件列表

联系人：IRC #freebsd-ci 频道 on EFNet

在 2023 年第二季度，我们与项目贡献者和开发者合作，满足了他们的测试需求。同时，我们还与外部项目和公司合作，在 FreeBSD 上进行更多的测试，以增强他们的产品。

重要完成的任务：

- 添加了 [FreeBSD-stable-13-amd64-gcc12_build](https://ci.freebsd.org/job/FreeBSD-stable-13-amd64-gcc12_build/) 任务。
- 将 main 分支和 stable/13 分支的构建环境更改为 13.2-RELEASE，将 stable/12 分支更改为 12.4-RELEASE。
- 使用 gcc12 的\*-build 任务正在向[ dev-ci 邮件列表](https://lists.freebsd.org/subscription/dev-ci)发送故障报告。
- 在 [BSDCan 2023 开发者峰会](https://wiki.freebsd.org/DevSummit/202305)上展示测试/CI 状态更新。

正在进行的任务：

- 设计和实施预提交 CI 构建和测试（以支持[工作流工作组](https://gitlab.com/bsdimp/freebsd-workflow)）。
- 设计和实施使用 CI 集群构建发布工件，就像发布工程一样。
- 简化贡献者和开发者的 CI/测试环境设置。
- 设置 CI 舞台环境并将实验性任务放在其中。
- 整理 freebsd-ci 存储库中的脚本，为将其合并到 src 存储库做准备。
- 改进硬件测试实验室并增加更多硬件进行测试。
- 合并 <https://reviews.freebsd.org/D38815>。
- 合并 <https://reviews.freebsd.org/D36257>。

待处理或排队的任务：

- 收集和整理 [CI 任务](https://hackmd.io/@FreeBSD-CI/freebsd-ci-todo)和想法。
- 为运行测试的虚拟机客户端设置公共网络访问。
- 实施使用裸机硬件运行测试套件。
- 添加针对-CURRENT 的 drm port 构建测试。
- 计划运行 ztest 测试。

帮助更多软件在其 CI 流水线中获得 FreeBSD 支持（Wiki 页面：[3rdPartySoftwareCI](https://wiki.freebsd.org/3rdPartySoftwareCI)，[HostedCI](https://wiki.freebsd.org/HostedCI)）。

与托管 CI 提供者合作，以获得更好的 FreeBSD 支持。

请参阅与 [freebsd-testing@相关的事情](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals)，了解更多进行中的信息，并欢迎加入这项工作！

赞助者：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### Ports
链接：

关于 FreeBSD Ports 的网址：<https://www.FreeBSD.org/ports/>

贡献 Ports 的网址：<https://docs.freebsd.org/en/articles/contributing/#ports-contributing>

FreeBSD Ports 监控网址：<http://portsmon.freebsd.org/>

Ports 管理团队网址：<https://www.freebsd.org/portmgr/>

Ports Tarball 网址：<http://ftp.freebsd.org/pub/FreeBSD/ports/ports/>

联系人：René Ladan <portmgr-secretary@FreeBSD.org>

联系人：FreeBSD Ports 管理团队 <portmgr@FreeBSD.org>

Ports 管理团队负责监督 Ports 的整体方向、构建软件包以及人员事务。以下是上一个季度的情况。

目前，Ports 中有超过 34,400 个 port。目前有 3,019 个未解决的 port 问题(PR)，其中有 746 个未被分配。上个季度 `main` 分支有来自 151 位提交者的 10,439 次提交，2023Q2 分支有来自 55 位提交者的 745 次提交。与上个季度相比，这意味着 port 数量略有增加，未解决的 PR 数量略有减少， port 提交数量有较大增加。

在本季度，我们欢迎 Tom Judge (tj@) 回归，同时告别了 Steve Wills (swills@)。Steve 也是 portmgr 的一员。作为 portmgr 潜伏者计划的一部分，我们欢迎 Ronald Klop (ronald@)、Renato Botelho (garga@)和 Matthias Andree (mandree@)的加入。

Portmgr 已经恢复了对将子软件包引入树中的工作，但仍有一些事项需要进一步完善。

在软件方面，pkg 已更新至 1.19.2，Firefox 更新至 114.0.2，Chromium 更新至 114.0.5735.198，KDE Gear 更新至 23.04.2。在上个季度，antoine@运行了 23 次 exp-runs 来测试软件包更新，将 CPU_MAXSIZE 提升至 1024，修复了 devel/cmake-core 的 armv7 失败，并在 USES=meson 中添加了--auto-features=enabled 选项。最后，Ports 已更新以支持 FreeBSD-CURRENT 中的 LLVM 16 和 OpenSSL 3。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 项目
涵盖多个类别的项目，从内核和用户空间到 Ports 或外部项目。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

##$# Cirrus-CI

链接：

FreeBSD Cirrus-CI Repositories 网址：<https://cirrus-ci.com/github/freebsd/>

FreeBSD src CI 网址：<https://cirrus-ci.com/github/freebsd/freebsd-src>

FreeBSD doc CI 网址：<https://cirrus-ci.com/github/freebsd/freebsd-doc>

联系人：Brooks Davis <brooks@FreeBSD.org>

联系人：Ed Maste <emaste@FreeBSD.org>

联系人：Li-Wen Hsu <lwhsu@FreeBSD.org>

Cirrus-CI 是一个托管的持续集成服务，支持在 Linux、Windows、macOS 和 FreeBSD 上进行开源项目的 CI 服务。它是我们自己 Jenkins CI 基础设施的补充，支持其他用例，包括测试 GitHub 的 pull requests 和 FreeBSD 的 forks。我们在 2019 年为 FreeBSD src 树添加了 Cirrus-CI 配置，并在 2020 年为 doc 添加了配置。许多其他托管在 GitHub 上的 FreeBSD 项目（如 drm-kmod、kyua、pkg 和 poudriere）也使用了 Cirrus-CI。

在上一个季度，Cirrus-CI 配置接受了持续的维护更新（转换到最新的 FreeBSD 发布镜像）。在 src 树中，我们添加了一些额外的检查。这些检查确保在需要时更新生成的文件（`make sysent` 和 `make makeman`），并检查是否缺少目录。我们添加了使用 Clang/LLVM 16 工具链包进行构建的作业，与现在在基本系统中的 Clang 版本相匹配。现在，对于所有提交，GCC 作业默认在 GitHub 镜像上运行。

赞助者：DARPA 赞助者：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 在 FreeBSD 内核中支持 BATMAN

链接：

维基页面网址：<https://wiki.freebsd.org/SummerOfCode2023Projects/CallingTheBatmanFreeNetworksOnFreeBSD>

源代码（Pull Request）网址：<https://github.com/obiwac/freebsd-gsoc/pull/1>

联系人：Aymeric Wibo <obiwac@FreeBSD.org>

BATMAN （Better Approach to Mobile Ad-hoc Networking）。BATMAN 是由 Freifunk 项目开发和使用的一种用于多跳自组织网络（主要是无线网络）的路由协议。Freifunk 是德国的一个倡议，旨在基于网络中立性原则在城市范围内构建开放的 Wi-Fi 网络。BATMAN 的目标是成为一个完全分散的协议；网络中的任何一个节点都不需要了解或关心整个网络的拓扑结构。

在 Linux 中，由 batman-adv 内核模块提供支持 BATMAN 的功能。而这个项目的目标是将类似的支持带到 FreeBSD，包括开发内核模块本身，以及创建 BATMAN 网络所需的用户空间网络库和工具。

目前，创建接口并与其进行交互已经可以在 Linux 和 FreeBSD 的用户空间中工作，尽管数据包传输（有点）可以工作，但仍然不完整。该项目还在 [ifconfig(8)](https://man.freebsd.org/cgi/man.cgi?query=ifconfig&sektion=8&format=html) 中添加了对 batadv 接口的支持。

导师：Mahdi Mokhtari

赞助商：2023 谷歌代码之夏 项目

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 在 LinuxBoot 上的支持

联系人：Warner Losh <imp@bsdimp.com>

链接：

LinuxBoot 项目网址：<https://www.linuxboot.org/>

BSDCan 2023 kboot 演讲幻灯片链接：<https://docs.google.com/presentation/d/1N5Jp6XzYWv9Z9RhhETC-e6tFkqRHvp-ldRDW_9h2JCw/edit?usp=sharing>

LinuxBoot 是一个致力于创建干净、健壮、可审计和可重复启动的启动固件的项目。最初是谷歌的一个特定项目，现已扩展到包括使用 Linux 来启动最终操作系统的任何启动环境。现在许多平台都支持这个环境，并且在某些情况下它是唯一可用的启动环境。此外，一些嵌入式设备上有一个硬编码的 LinuxBoot 环境，很难更改，因此能够重新启动到 FreeBSD 是可取的。

旧的 Sony PlayStation 3 port 使用了一个名为'kboot'的引导加载程序来从其 Linux 内核启动 FreeBSD port（都是在 LinuxBoot 项目之前）。该代码已经大大扩展，并且通过易于替换的体系结构插件通用化。正常的 FreeBSD /boot/loader 被构建为 Linux 二进制文件，它读取 FreeBSD 内核、模块和可调整参数，并将它们放入内存，就像它在预启动环境中运行一样，然后使用 kexec_load(2)将该映像加载到 Linux 内核中，并进行特殊的重新启动到该映像。对于支持 UEFI 的系统，它会传递 UEFI 内存表和指向 UEFI 运行时服务的指针给新内核。

它支持从主机文件系统、主机块设备上的任何 loader(8)支持的文件系统（包括跨多个设备的池）、RAM 磁盘映像以及通过网络下载的文件加载文件。可以混合使用这些功能。例如，可以从主机文件系统加载配置覆盖，同时内核从专用存储（如 NVME）或 RAM 磁盘映像加载。它支持在 stdin/stdout 上运行的主机控制台。它支持显式位置，例如 /dev/nvme0ns1:/boot/loader/gerbil.conf，用于加载文件系统的位置。它还支持 ZFS 引导环境，包括一次性引导功能。

有关 kboot 的更多详细信息，以及它支持的内容和一些常规背景，可以在 Warner 的 BSDcan 演讲中找到（上面链接的幻灯片）。

FreeBSD/aarch64 现在可以在 LinuxBoot 环境中从 Linux 启动，支持和功能与 loader.efi(8)相当。内存布局传递用于 GICv3 补丁。需要为 aarch64 内核提供 GICv3 补丁（https://reviews.freebsd.org/D40902）。

FreeBSD/amd64 的支持正在进行中，可能已完成 80%。由于 amd64 是一个较早的 port，amd64 引导环境对引导加载程序提供内核数据有更多要求。由于内核无法从长模式访问这些数据，所有 BIOS 环境中的数据来源都必须由引导加载程序提供。虽然 UEFI 和 ACPI 提供了让内核获取这些数据的方式，但许多数据仍然必须由引导加载程序提供。内核在初始化过程中会发生崩溃，因为这些前提条件尚未被发现和实现。

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

链接:
OpenSSL 下载网址：<https://www.openssl.org/source/>

OpenSSL 3.0 已发布！网址：<https://www.openssl.org/blog/blog/2021/09/07/OpenSSL3.Final/>

openssl-fipsinstall 网址：<https://www.openssl.org/docs/man3.0/man1/openssl-fipsinstall.html>

联系人: Pierre Pronchery <pierre@freebsdfoundation.org>

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

Linuxulator 状态 Wiki 页面网址：<https://wiki.freebsd.org/Linuxulator>

Linux 应用程序状态 Wiki 页面网址：<https://wiki.freebsd.org/LinuxApps>

联系人: Dmitry Chagin <dchagin@FreeBSD.org>

该项目的目标是改进 FreeBSD 执行未经修改的 linux(4) 二进制文件的能力。

截至 [cbbac5609115](https://cgit.freebsd.org/src/commit/?id=cbbac5609115)，已实现在 amd64 上信号传递时保留 fpu xsave 状态。这使得可以在其中运行具有抢占式调度程序的现代 golang。

新的功能是在 [namei(9)](https://man.freebsd.org/cgi/man.cgi?query=namei&sektion=9&format=html)中添加了指定替代 ABI 根路径的功能。以前，要动态重新查找每个需要路径名转换的 [linux(4)](https://man.freebsd.org/cgi/man.cgi?query=linux&sektion=4&format=html)系统调用，需要一些不太美观的代码，并使用 `kern_alternate_path()`，该函数在解析目标中带有前导/的符号链接时不起作用。现在，非本机 ABI（即 [linux(4)](https://man.freebsd.org/cgi/man.cgi?query=linux&sektion=4&format=html)）在 exec 时使用一次 `pwd_altroot()` 调用来指定其根目录（例如 `/compat/ubuntu`），并忽略路径名转换。这样可以在 Ubuntu 兼容性环境中进行 chroot，而无需手动修复此类符号链接。

总共修复了 10 多个错误；glibc-2.37 测试套件报告的失败测试少于 70 个。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### Service Jail - 自动将 rc.d 服务加入 jail
链接：

D40369: 扩展 /usr/bin/service 以设置环境变量的可能性 网址: <https://reviews.freebsd.org/D40369>

D40370: 自动加入 rc.d 服务的基础设施 网址: <https://reviews.freebsd.org/D40370>

D40371: 自动服务 jail：为在自动服务 jail 中实现服务的全部功能进行一些设置 网址: <https://reviews.freebsd.org/D40371>

联系人：Alexander Leidinger <netchild@FreeBSD.org>

Service Jail 扩展了 rc(8)系统，允许自动将 rc.d 服务加入 jail。服务 jail 继承父主机或 jail 的文件系统，但默认情况下使用 jail 的所有其他限制（进程可见性、受限网络访问、文件系统挂载权限、sysvipc 等）。附加配置允许继承父级的 IP 地址、sysvipc、内存页锁定和使用 bhyve 虚拟机监视器（vmm(4)）。

如果您想将例如 local_unbound 加入服务 jail 并允许 IPv4 和 IPv6 访问，只需更改 rc.conf(5)为：

```
local_unbound_svcj_options=net_basic
local_unbound_svcj=YES
```
尽管这不具有手动 jail 设置与单独的文件系统和 IP/VNET 相同的安全性好处，但设置要简单得多，同时提供像隐藏同一用户的其他进程等 jail 的某些安全性好处。

链接中的补丁是[我在 2019 年所提供的重写](https://lists.freebsd.org/pipermail/freebsd-jail/2019-February/003710.html)。主要区别在于使用了一个 ENV 变量来进行更合理的跟踪，因此需要更改 service(8)。

我的意图是在 stable/14 分支之前提交 D40369。在发布 14.0 之前，我不会提交 D40370 或 D40371，并且两者都将受益于更多人的审查。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 使用 ktrace(1)进行安全沙箱化
链接：

ktrace 分支 网址: <https://github.com/jakesfreeland/freebsd-src/tree/ff/ktrace>

联系人：Jake Freeland <jfree@FreeBSD.org>

使用 ktrace(1)进行 Capiscum 化

本报告介绍了对 ktrace(1)的扩展，用于记录未进行 Capiscum 化的程序的能力违规情况。

在 Capiscum 化的第一步是确定您的程序在哪里引发了能力违规。您可以通过查看源代码并删除与 Capiscum 不兼容的代码来解决此问题，但这可能很繁琐，并要求开发人员熟悉在能力模式中不允许的所有内容。

另一种寻找违规的替代方法是使用 ktrace(1)。ktrace(1)工具记录指定进程的内核活动。能力违规发生在内核内部，因此 ktrace(1)可以使用-t p 选项记录和返回有关程序违规的额外信息。

传统上，需要将程序放入能力模式，然后它们才能报告违规。当输入受限制的系统调用时，它将失败并返回 `ECAPMODE: Not permitted in capability mode`。如果开发人员进行错误检查，那么他们的程序可能会以该错误终止。这种行为使得违规跟踪变得不方便，因为 ktrace(1)只会报告第一个能力违规，然后程序将终止。

幸运的是，ktrace(1)的新扩展可以在程序没有进入能力模式时记录违规。这意味着任何开发人员都可以在其程序上运行能力违规跟踪而无需修改，以查看它引发违规的位置。由于程序实际上从未进入能力模式，因此它仍将获取资源并正常执行。

**违规跟踪示例**

下面显示的 cap_violate 程序尝试引发 ktrace(1)可以捕获的每种类型的违规：

```
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

前 7 个 ` system call not allowed` 条目并不是显式地来自 `cap_violate` 程序代码。相反，它们是由 FreeBSD 的 C 运行时库引发的。当您使用 `-t np` 选项跟踪 namei 转换和能力违规时，这一点变得明显：

```
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

下一个示例从 unzip(1)实用程序（在进行 Capsicum 化之前）跟踪违规行为：

```
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

unzip(1)的违规跟踪输出更类似于开发人员在首次跟踪自己的程序时所看到的情况。大多数程序都会链接到库。在这种情况下，unzip(1)链接到 libarchive(3)，这在追踪中反映了出来：

```
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libarchive.so.7"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/usr/lib/libarchive.so.7"
```

unzip(1)的违规行为可以在 C 运行时违规行为之后找到：

```
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

在这种情况下，unzip(1)正在重新创建 zip 归档中包含的文件结构。违规行为是因为在能力模式下不能使用 AT_FDCWD 值。这些违规行为的大部分可以通过在进入能力模式之前打开 AT_FDCWD（当前目录）并将该描述符传递给 openat(2)、fstatat(2)和 mkdirat(2)作为相对引用来解决。

虽然违规行为跟踪可能不会自动将程序 Capsicum 化，但它是开发者工具箱中的另一种工具。在 ktrace(1)下运行程序只需要几秒钟的时间，结果几乎总是一个不错的起点，用于使用 Capsicum 对程序进行沙盒化。

赞助：FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### NVMe over Fabrics

链接：nvmf2 branch 网址: <https://github.com/bsdjhb/freebsd/tree/nvmf2>

联系人: John Baldwin <jhb@FreeBSD.org>

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

Wiki 页面 网址: <https://wiki.freebsd.org/BootTime>

BSDCan 演讲幻灯片 网址:  <https://www.bsdcan.org/events/bsdcan_2023/sessions/session/116/slides/44/BSDCan23-Firecracker.pdf>

联系人: Colin Percival <cperciva@FreeBSD.org>

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

[Github 项目链接](https://github.com/mightyjoe781/freebsd-src/tree/bootloader-smk/tools/boot/bootloader_test)

联系人: Sudhanshu Mohan Kashyap <smk@FreeBSD.org>

FreeBSD 支持多种体系结构、文件系统和磁盘分区方案。我正在尝试编写一个 Lua 脚本，该脚本将允许测试所有支持的第一和第二级支持的体系结构组合的引导加载程序，并提供关于任何不兼容组合和预期功能的报告。如果时间允许，还可以进一步探索将脚本集成到现有的构建基础设施中（如 Jenkins 或 Github Actions），以生成测试结果的综合摘要。

目前，开发人员所做的任何更改可能会影响操作系统在某些特定环境中的启动能力。这些脚本确保更改不会导致已测试环境的回归。这些脚本的设计高效且比目前所需的完整构建更便宜。这些特性允许开发人员经常使用脚本，并在 CI 流水线中集成而不会产生过多的成本。

目前脚本相关的工作似乎进展顺利，但在未来我需要找到各种 QEMU 配方以测试不同的环境。如果有任何工作中的 QEMU 配方适用于当前发布版本的 FreeBSD，请随时通过邮件发送至 smk@FreeBSD.org。

赞助者: 2023 谷歌代码之夏项目

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 内核的物理内存压缩
链接：

谷歌代码之夏项目维基页面 网址：<https://wiki.freebsd.org/SummerOfCode2023Projects/PhysicalMemoryAntiFragmentationMechanisms>
[Differential revision 40575](https://reviews.freebsd.org/D40575) 网址：<https://reviews.freebsd.org/D40575>
[Differential revision 40772](https://reviews.freebsd.org/D40772) 网址：<https://reviews.freebsd.org/D40772>

联系人：Bojan Novković <bnovkov@FreeBSD.org>

大多数现代 CPU 架构通过支持大于标准页面大小的页面来提供性能提升。不幸的是，由于高度的物理内存碎片化，分配这种页面可能会失败。这项工作实现了物理内存压缩作为一种主动减少运行系统碎片化的手段。这项工作是正在进行的 Google Summer of Code 项目的一部分，其目标是向虚拟内存子系统添加各种物理内存抗碎片化措施。

Differential [D40575](https://reviews.freebsd.org/D40575) 实现了用于量化物理内存碎片化程度的众所周知的度量标准。 Differential [D40772](https://reviews.freebsd.org/D40772) 实现了物理内存压缩，并添加了一个守护程序，监视系统并在需要时执行压缩。

计划的未来工作包括设计适当的基准测试套件，运行测试，并根据评审和测试结果调整代码。这仍然是一个正在进行的工作，因此非常欢迎进行任何测试、评审和反馈。

赞助者：2023 谷歌代码之夏项目

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 增加 MAXCPU

链接：

[D36838：amd64：将 MAXCPU 从 256 增加到 1024](https://reviews.freebsd.org/D36838) 网址：<https://reviews.freebsd.org/D36838>

联系人：Ed Maste <emaste@FreeBSD.org>

默认的 amd64 和 arm64 FreeBSD 内核配置目前支持最多 256 个 CPU。可以通过设置 `MAXCPU` 内核选项来构建支持更大核心数的自定义内核。然而，拥有超过 256 个 CPU 的普通系统正在变得越来越多，并且在 FreeBSD 14 的支持生命周期中将变得越来越常见。我们希望将默认的最大 CPU 数增加到 1024，以便在 FreeBSD 14 上“开箱即用”地支持这些系统。

为了支持更大的默认 MAXCPU，进行了一些更改，包括将 `cpuset_t` 的用户空间最大值修复为 1024。还进行了一些更改，以避免静态的 `MAXCPU` 大小的数组，将它们替换为按需内存分配。

需要进一步的工作来继续减少由 `MAXCPU` 大小确定的静态分配，并解决在非常高核心数系统上的可伸缩性瓶颈，但目标是在 FreeBSD 14 发布时提供对大型 CPU 数量的支持，具有稳定的 ABI 和 KBI。

赞助者：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### SquashFS 在 FreeBSD 内核的移植

链接：

Wiki 页面 网址：<https://wiki.freebsd.org/SummerOfCode2023Projects/PortSquashFuseToTheFreeBSDKernel>

源代码 网址：<https://github.com/Mashijams/freebsd-src/tree/gsoc/squashfs>

联系人：Raghav Sharma <raghav@FreeBSD.org>

SquashFS 是一个只读文件系统，可以非常高效地压缩整个文件系统或单个目录。自 2009 年以来，Linux 内核内置了对它的支持，并在嵌入式 Linux 发行版中非常常见。该项目的目标是为 FreeBSD 内核添加 SquashFS 支持，以实现从内存中的 SquashFS 文件系统引导 FreeBSD。

目前，该驱动程序与 FreeBSD 13.2 版本兼容。该驱动程序能够正确解析 SquashFS 磁盘文件，并支持工作中的 mount(8)。Linux SquashFS 支持许多压缩选项，如 zstd、lzo2、zlib 等，根据用户的喜好选择，我们的驱动程序也支持所有这些压缩方式。

计划的未来工作包括添加对目录、文件、扩展属性和符号链接的读取支持。该项目仍在 [Chuck Tuffli](chuck@FreeBSD.org) 的指导下进行中，并预计将在谷歌代码之夏项目结束时完成。

赞助者：2023 谷歌代码之夏项目

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 改进 Pf 

链接：

D40911 网址：<https://reviews.freebsd.org/D40911>

D40861 网址：<https://reviews.freebsd.org/D40861>

D40862 网址：<https://reviews.freebsd.org/D40862>

D40863 网址：<https://reviews.freebsd.org/D40863>

D40864 网址：<https://reviews.freebsd.org/D40864>

D40865 网址：<https://reviews.freebsd.org/D40865>

D40866 网址：<https://reviews.freebsd.org/D40866>

D40867 网址：<https://reviews.freebsd.org/D40867>

D40868 网址：<https://reviews.freebsd.org/D40868>

D40869 网址：<https://reviews.freebsd.org/D40869>

D40870 网址：<https://reviews.freebsd.org/D40870>

联系人：Kajetan Staszkiewicz <vegeta@tuxpowered.net>

联系人：Naman Sood <naman@freebsdfoundation.org>

联系人：Kristof Provost <kp@FreeBSD.org>

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

联系人：Justin Hibbits <jhibbits@FreeBSD.org>

IfAPI（原名 DrvAPI）项目始于 2014 年，其目标是隐藏网络驱动程序中的 ifnet(9)结构。相反，所有对成员的访问都将通过访问器函数进行。这允许更改网络堆栈而无需重新编译驱动程序，还有可能让单个驱动程序支持多个 FreeBSD 版本。

目前，在基本系统中已经实现了这一目标，但是还需要更新一些 port 来使用 IfAPI。有一个工具可以自动完成大部分的转换，即 `tools/ifnet/convert_ifapi.sh`。文档也正在准备中，但可能需要帮助。ifnet(9)需要进行大量的清理，因为目前其中的一些信息已经过时了。

赞助：Juniper Networks, Inc.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 使 Netgraph 无锁化

链接：
维基页面 网址：<https://wiki.freebsd.org/SummerOfCode2023Projects/LocklessSynchronizationBetweenNodesInNetgraph>

仓库 网址：<https://github.com/zinh88/epoch-netgraph>

联系人：Zain Khan <zain@FreeBSD.org>

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

SIMD 调度框架草案 网址：<https://reviews.freebsd.org/D40693>

项目提案 网址：<http://fuz.su/~fuz/freebsd/2023-04-05_libc-proposal.txt>

联系人：Robert Clausecker <clausecker@FreeBSD.org>

SIMD 指令集扩展，如 SSE、AVX 和 NEON，在现代计算机上普遍存在，并为许多应用程序提供性能优势。该项目的目标是为常见的 libc 函数（主要是 string(3)中描述的函数）提供 SIMD 增强版本，加速大多数 C 程序的执行。

对于每个优化的函数，将提供多达四种实现：

- 标量实现，针对 amd64 进行了优化，但没有使用 SIMD。
- 基准实现，使用 SSE 和 SSE2 或者使用 x86-64-v2，涵盖了 SSE4.2 之前的所有 SSE 扩展。
- 使用 AVX 和 AVX2 的 x86-64-v3 实现。
- 使用 AVX-512F/BW/CD/DQ 的 x86-64-v4 实现。

用户可以通过设置 AMD64_ARCHLEVEL 环境变量来选择要使用的 SIMD 增强级别。

虽然当前的项目只涉及 amd64 架构，但未来可能会扩展到其他架构，如 arm64。

赞助：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 将 mfsBSD 集成到发布构建工具中


链接：

维基文章 网址：<https://wiki.freebsd.org/SummerOfCode2023Projects/IntegrateMfsBSDIntoTheReleaseBuildingTools>

项目存储库（integrate-mfsBSD-building 分支）网址：<https://github.com/soobinrho/freebsd-src/tree/integrate-mfsBSD-building>

联系人：Soobin Rho <soobinrho@FreeBSD.org>

**什么是 mfsBSD？**

"mfsBSD 是一个工具集，用于创建基于 FreeBSD 的小型但功能齐全的 mfsroot 发行版，它将所有文件存储在内存中（MFS）[内存文件系统]，并从硬盘、USB 存储设备或光盘加载。它可以用于各种目的，包括无盘系统、恢复分区以及远程覆盖其他操作系统。"

[Martin Matuska](mm@FreeBSD.org) 既是 [mfsBSD 白皮书](https://people.freebsd.org/~mm/mfsbsd/mfsbsd.pdf)的作者，也是 [mfsBSD 存储库](https://github.com/mmatuska/mfsbsd)的维护者。

**目的**

该项目在 src/release makefile 中为当前版本和稳定版本的 mfsBSD 映像创建额外的目标。目前，只生产发布版本的 mfsBSD 映像，这意味着它们往往与基本工具不同步。该项目旨在解决这个问题。

**位置**

这是 2023 年的 GSoC（Google Summer of Code）项目。因此，官方的编码期限是从 2023 年 5 月 29 日到 2023 年 8 月 28 日。作为开源社区的初学者，作者欢迎在项目存储库中提出所有的意见、建议和拉取请求，该存储库将是整个期间内所有代码的位置。

导师：[Juraj Lutter](otis@FreeBSD.org)和 [Joseph Mingone](jrm@FreeBSD.org)
 
赞助：2023 谷歌代码之夏项目

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


### 云平台

更新特定于云环境的功能，并为新的云平台提供支持。

#### FreeBSD 作为一级云平台的 cloud-init 支持

链接：

cloud-init 网站 网址：<https://cloud-init.io/>

cloud-init 文档 网址：<https://cloudinit.readthedocs.io/en/latest/>

cloud-init 正在进行的重构 网址：<https://github.com/canonical/cloud-init/blob/main/WIP-ONGOING-REFACTORIZATION.rst>

联系人：Mina Galić <freebsd@igalic.co>

cloud-init 是在云中配置服务器的标准方式。不幸的是，除了 Linux 以外的操作系统对 cloud-init 的支持一直相对较差，而在 FreeBSD 上缺乏 cloud-init 支持阻碍了希望将 FreeBSD 作为一级平台的云提供商。为了解决这个问题，该项目旨在使 FreeBSD 的 cloud-init 支持与 Linux 支持相当。更广泛的计划是在所有 BSD 上提供支持。

这个季度进展缓慢，但我已经完成了一个新的里程碑：

- 瞬时网络类别已被重写并与平台无关。这些类别被多个云提供商用于在检索实际配置之前初始化临时网络。
- cloud-init 已经在 Vultr 上成功测试。我希望在下一个发布版本中，我能说服 Vultr 将他们的 FreeBSD 映像切换到 cloud-init。

除此之外，我还扩展了 BSD 上的 rsyslog 支持。我还为 cloud-init 的 ds-identify 添加了一个 rc 脚本，这应该使零配置设置的速度提高几个数量级：ds-identify 首先运行，并快速猜测机器正在运行的云提供商。然后 cloud-init 仅使用该猜测，而不是在所有可能的云提供商列表中进行迭代和失败。构建自定义映像的人可以轻松禁用此功能（通过删除 `/usr/local/etc/rc.d/dsidentify`），并自己提供一个特定的列表，从引导中节省几毫秒的时间。

接下来的步骤将是继续处理网络重构任务，并为 FreeBSD 添加 [LXD](https://github.com/canonical/lxd/pull/11761) 支持，以便可以将其包含在 CI 测试中。后者将涉及对 LXD 的工作，以及对 [FreeBSD virtio](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=271793) 子系统的工作。

与往常一样，我非常欢迎早期测试者检查 [net/cloud-init-devel](https://cgit.freebsd.org/ports/tree/net/cloud-init-devel/)，并报告 bug。自上次报告以来，cloud-init 的 bug 跟踪器已从 Launchpad 迁移到 GitHub，因此这可能会减少一些摩擦。

赞助商：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 上的 OpenStack

链接：

OpenStack 网站 网址：<https://www.openstack.org/>

FreeBSD 上的 OpenStack 网址：<https://github.com/openstack-on-freebsd>

联系人：Chih-Hsin Chang <starbops@hey.com>

联系人：Li-Wen Hsu <lwhsu@FreeBSD.org>

该项目旨在将关键的 OpenStack 组件，如 keystone、nova 和 neutron，移植到 FreeBSD，使其可以作为 OpenStack 主机运行。

我们已经开始移植 `nova-novncproxy` 和 `nova-serialproxy`，以增加访问实例控制台的方式。为了降低想要尝试该项目的人的门槛，我们还将开发环境从物理机迁移到虚拟机。但在 Linux KVM 之上运行 bhyve 虚拟机仍然存在问题。关于这个问题的详细解释可以在[这里](https://hackmd.io/@starbops/SkdJON2un)找到。其他的成就包括：

解决实例内部的网络连接问题

能够生成多个实例

从 Python 3.8 移植到 3.9。

在下个季度，我们将继续改进控制台代理服务，以使整体工作流更加流畅。

在[文档存储库中](https://github.com/openstack-on-freebsd/docs)还可以找到构建 POC 站点的逐步文档。每个 OpenStack 组件的修补版本都在同一 GitHub 组织下。

有兴趣帮助该项目的人可以先按照安装指南检查文档。欢迎提供反馈和帮助。

赞助商：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 在 Microsoft HyperV 和 Azure 上的支持

链接：
Microsoft Azure 上的 FreeBSD Wiki 文章 网址：<https://wiki.freebsd.org/MicrosoftAzure>

Microsoft HyperV 上的 FreeBSD Wiki 文章 网址：<https://wiki.freebsd.org/HyperV>

联系人：Microsoft FreeBSD Integration Services 团队 <bsdic@microsoft.com>

联系人：freebsd-cloud 邮件列表

联系人：The FreeBSD Azure Release Engineering Team <releng-azure@FreeBSD.org>

联系人：Wei Hu <whu@FreeBSD.org>

联系人：Souradeep Chakrabarti <schakrabarti@microsoft.com>

联系人：Li-Wen Hsu <lwhsu@FreeBSD.org>

在本季度，我们主要在 ARM64 架构支持以及构建和发布到 [Azure 社区库](https://learn.microsoft.com/azure/virtual-machines/share-gallery-community)的镜像方面进行了工作。项目的测试公共库中提供了一些测试镜像，命名为`FreeBSDCGTest-d8a43fa5-745a-4910-9f71-0c9da2ac22bf`：FreeBSD-CURRENT-testing FreeBSD-CURRENT-gen2-testing FreeBSD-CURRENT-arm64-testing

要使用它们，在创建虚拟机时： . 在 `Select an Image` 步骤中，在 `Other items` 中选择 `Community Images (PREVIEW)` . 搜索 `FreeBSD`

正在进行中的任务：

- 自动化镜像构建和发布过程，并合并到 src/release/。
- 构建和发布基于 ZFS 的镜像到 Azure Marketplace
 - 所有所需的代码都合并到主分支，可以通过指定 VMFS=zfs 来创建基于 ZFS 的镜像。
 - 需要将构建过程更加自动化，并与发布工程合作开始生成快照。
- 构建和发布 Hyper-V gen2 VM 镜像到 Azure Marketplace
- 构建和发布快照版本到 Azure 社区库

以上任务由 The FreeBSD Foundation 赞助，并由 Microsoft 提供资源。

Microsoft 的 Wei Hu 和 Souradeep Chakrabarti 正在进行由 Microsoft 赞助的几项任务：

- 将 Hyper-V 客户机支持移植到 aarch64
 -<https://bugs.freebsd.org/267654>
 -<https://bugs.freebsd.org/272461>

待办任务：

- 更新 [Microsoft Learn](https://learn.microsoft.com/) 上与 FreeBSD 相关的文档

- 在 [Azure Pipelines](https://azure.microsoft.com/products/devops/pipelines/) 中支持 FreeBSD

- 将 [Azure 代理 port](https://www.freshports.org/sysutils/azure-agent)更新到最新版本

- 同步上游[本地修改 Azure 代理](https://github.com/Azure/WALinuxAgent/pull/1892)

赞助商：Microsoft 负责 Microsoft 人员的赞助和其他资源，The FreeBSD Foundation 负责其他方面的赞助。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 在 EC2 上的支持

链接：

FreeBSD/EC2 Patreon 网址：<https://www.patreon.com/cperciva>

联系人：Colin Percival <cperciva@FreeBSD.org>

FreeBSD 可在 x86（Intel 和 AMD）和 ARM64（Graviton）EC2 实例上使用。继续努力确保即将推出的实例类型得到支持，包括最近宣布的 M7a“EPYC”实例，预计将在 FreeBSD 14.0-RELEASE 中得到支持。

最近，每周的 FreeBSD 快照从“UEFI”引导模式更改为“UEFI Preferred”引导模式，允许它们获得 UEFI 提供的引导性能改进，同时仍然支持与 UEFI 不兼容的“裸机”和“前代”实例类型。这一变化将在 FreeBSD 14.0-RELEASE 中出现。

EC2 引导脚本最近已更新以支持 IMDSv2。这一变化将在 FreeBSD 14.0-RELEASE 中出现。

如果 FreeBSD 13.2 的用户需要这些更新中的任何一项，作者可以提供 FreeBSD“13.2-RELEASE 加更新” AMI。

此工作得到 Colin 的 FreeBSD/EC2 Patreon 的支持。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 文档部分
文档、手册页面或新的外部书籍/文件中值得注意的变化。

#### 文档工程团队

链接：FreeBSD 文档项目 网址：<https://www.freebsd.org/docproj>

链接：FreeBSD 文档项目新贡献者入门指南 网址：<https://docs.freebsd.org/en/books/fdp-primer/>

链接：文档工程团队 网址：<https://www.freebsd.org/administration/#t-doceng>

联系人：FreeBSD 文档工程团队 <doceng@FreeBSD.org>

doceng@ 团队负责处理与 FreeBSD 文档项目相关的一些元项目问题；有关更多信息，请参阅 [FreeBSD Doceng Team Charter](https://www.freebsd.org/internal/doceng/)（FreeBSD Doceng 团队章程）。

在本季度：

- 已任命 fernape@ 为新的 Doceng 团队成员。
- 由于 www/gohugo 是我们文档基础设施的关键部分，该 port 的维护权已转移到 doceng@。我们与前任维护者达成了一致意见。
- 改进了翻译工作流程（在下面的章节中描述）。

**Porter's Handbook（Port 开发者手册）**

已记录 [USES=nextcloud](https://cgit.freebsd.org/doc/commit/?id=634a34b7bb37650e4f8fcbea9fd7428b3f5b911a)。

**FDP Primer**

[FreeBSD 文档项目新贡献者入门指南](https://docs.freebsd.org/en/books/fdp-primer/weblate/)添加了一个新的章节，重点关注 Weblate。这个全面的章节提供了逐步指导，帮助加入 FreeBSD 翻译团队，无论是在线在 Weblate 上翻译还是离线。它提供了有关高效翻译、校对和测试过程的宝贵见解和实用建议。此外，这一章节还为贡献者提供了必要的知识，以正式提交他们的翻译到文档存储库，确保无缝集成他们的工作。

**FreeBSD 在 Weblate 上的翻译**

链接：在 Weblate 上翻译 FreeBSD 网址：<https://wiki.freebsd.org/Doc/Translation/Weblate>

链接：FreeBSD Weblate 实例 网址：<https://translate-dev.freebsd.org/>

2023 年第二季度状态

- 15 种语言
- 183 名注册用户
- [新的 Weblate 服务器](https://lists.freebsd.org/archives/freebsd-translators/2023-April/000111.html)

FreeBSD Weblate 实例现在运行在专用服务器上，大大提高了速度，并增强了翻译工作的效率。我们衷心感谢 ebrandi@提供的硬件升级。

语言

- 简体中文（zh-cn）（进度：7%）
- 繁体中文（zh-tw）（进度：3%）
- 荷兰语（nl）（进度：1%）
- 法语（fr）（进度：1%）
- 德语（de）（进度：1%）
- 印度尼西亚语（id）（进度：1%）
- 意大利语（it）（进度：5%）
- 韩语（ko）（进度：32%）
- 挪威语（nb-no）（进度：1%）
- 波斯语（fa-ir）（进度：3%）
- 波兰语（进度：1%）
- 葡萄牙语（pt-br）（进度：22%）
- 僧伽罗语（si）（进度：1%）
- 西班牙语（es）（进度：33%）
- 土耳其语（tr）（进度：2%）

我们要感谢所有贡献者，无论是翻译还是审查文档。

请帮助在您的当地用户组宣传这项工作，我们总是需要更多的志愿者。

**FreeBSD 手册工作组**

联系人：Sergio Carlavilla <carlavilla@FreeBSD.org>

[正在重新修订网络章节。](https://reviews.freebsd.org/D40546)

**FreeBSD 网站改版- WebApps 工作组**

联系人：Sergio Carlavilla <carlavilla@FreeBSD.org>

负责创建新的 FreeBSD 文档门户网站，并重新设计 FreeBSD 主网站及其组件的工作组。FreeBSD 开发人员可以在 FreeBSD Slack 频道# wg-www21 上关注和加入工作组。工作分为四个阶段：

- 文档门户的重新设计

创建一个新的设计，响应式设计，并具有全局搜索功能。（已完成）

- 网页上手册页面的重新设计

使用 mandoc 生成 HTML 页面的脚本。（已完成）在 <https://man-dev.FreeBSD.org> 上提供公共实例。

- 网页上 Ports 页面的重新设计

Ports 脚本以创建一个应用程序门户。（正在进行中）

- FreeBSD 主网站的重新设计

新设计，响应式设计和深色主题。（正在进行中）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Ports 部分
影响 Ports 的变化，无论是涉及大部分树的全面性变化，还是个别 port 本身的变化。

#### FreeBSD 上的 KDE
链接：

KDE/FreeBSD 计划 网址：<https://freebsd.kde.org/>

FreeBSD — KDE 社区维基 网址：<https://community.kde.org/FreeBSD>

联系人：Adriaan de Groot <kde@FreeBSD.org>

KDE on FreeBSD 项目将 CMake、Qt 和来自 KDE 社区的软件打包到 FreeBSD 的 Ports 中。这些软件包括一个完整的桌面环境，名为 KDE Plasma（适用于 X11 和 Wayland），以及数百个可在任何 FreeBSD 机器上使用的应用程序。

KDE 团队（kde@）是 desktop@和 x11@的一部分，构建软件堆栈，使 FreeBSD 成为漂亮且可用作日常图形桌面工作站的系统。下面的说明主要描述了与 KDE 有关的 port，但也包括整个桌面堆栈中重要的项目。

**基础设施**

Qt5 port 进行了各种更新：

- devel/qt5-webengine 在使用 Clang 16 进行构建时进行了修复。这是为了准备即将发布的 FreeBSD 14。\
- devel/qt5-qmake 进行了修复，以解决在否则不安装 Qt 的系统上安装 qmake 会导致奇怪错误的问题。

Qt6 port 进行了各种更新：

- devel/qt6-tools 在使用 Clang 16 进行构建时进行了修复。这是为了准备即将发布的 FreeBSD 14。

accessibility/at-spi2-core port ——桌面上的辅助技术的重要组成部分——更新到版本 2.48.0。

accessibility/at-spi2-core port 现在更好地支持非 X11 桌面。这对于基于 Wayland 的系统是一个改进。感谢 Jan Beich 的工作。

graphics/poppler port ——许多 PDF 查看器的基础——更新到版本 23.05。

ports-mgmt/packagekit-qt port 是新添加的，为 FreeBSD 上的图形化包管理器铺平了道路。

**KDE 堆栈**

KDE Gear 每个季度发布，KDE Plasma 每月更新，KDE Frameworks 每月发布一次。这些（大规模）更新在其上游发布后不久就会实现，不会单独列出。

- KDE Frameworks 更新至 5.105、.106 和.107。
- KDE Gear 更新至 23.04.0，然后是.1 和.2，包含错误修复。
- KDE Plasma Desktop 更新至版本 5.27.4，然后是.5 和.6，包含错误修复。

**相关 port**

弃用：

- graphics/ikona，一个使用 Rust 和 Qt 绑定编写的图标查看器，已经被上游弃用。
- polish/kadu，曾在波兰很受欢迎的聊天应用程序，已被弃用，上游消失了。
- sysutils/plasma5-ksysguard，一个系统监控应用程序，已经被上游弃用，将不再更新。

更新：

- astro/kstars，一个交互式天文馆，更新至版本 3.6.4。
- devel/qcoro，一个 C++协程实现，更新至版本 0.9.0。
- devel/qtcreator，一个用于 Qt、C++等的集成开发环境，更新至版本 10.0.2。
- games/gcompris-qt，一个针对 3-12 岁儿童的教育套件，更新至版本 3.2。
- graphics/kphotoalbum，一个照片相册和显示实用程序，更新至版本 5.10.0。
- net-im/tokodon，一个 Mastodon 社交网络客户端，加入了 KDE Gear。
- textproc/kdiff3，一个文本差异工具，更新至版本 1.10.1。

新增软件：

- devel/kommit，一个 Git 客户端，已添加。它是先前包 gitklient 的改名。
- multimedia/kasts 是 KDE 社区的一个新的播客收听和享受应用程序。
- textproc/arianna 是 KDE 社区的一款面向移动设备的电子书阅读器，使阅读 FreeBSD 文档变得愉悦。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 在 FreeBSD 上的 GCC

链接：

GCC 项目 网址：<https://gcc.gnu.org/>

GCC 10 版本系列 网址：<https://gcc.gnu.org/gcc-10/>>

GCC 11 版本系列 网址：<https://gcc.gnu.org/gcc-11/>

GCC 12 版本系列 网址：<https://gcc.gnu.org/gcc-12/>

GCC 13 版本系列 网址：<https://gcc.gnu.org/gcc-13/>

联系人：Lorenzo Salvadore <salvadore@FreeBSD.org>

上游发布了 [GCC 13](https://gcc.gnu.org/gcc-13)。如前面的状态报告中宣布的，我计划尝试在第一个 GCC 13 版本中更新 GCC_DEFAULT，因此本季度的大部分工作都是为此做准备。

随着 GCC 13.1 的发布（第一个 GCC 13 版本：我提醒一下，GCC 从 1 开始计算小版本号），在 ports 中创建了两个新 port：

lang/gcc13，跟踪 GCC 13 版本；

lang/gcc14-devel，跟踪新的 GCC 14 上游分支的快照。

**\*-devel port**

已启用对 .init_array 和 .fini_array 的支持。FreeBSD 自 [83aa9cc00c2d](https://cgit.freebsd.org/src/commit/?id=83aa9cc00c2d83d05a0efe7a1496d8aab4a153bb) 提交开始就支持这两个功能。

i386、amd64 和 aarch64 上的默认 bootstrap 选项从 LTO_BOOTSTRAP 回滚为 STANDARD_BOOTSTRAP：

- LTO 引导在这些架构上产生了太多的失败
- 对于希望使用 LTO_BOOTSTRAP 的用户，LTO_BOOTSTRAP 仍然可用。

这些更改将被应用到生产 port 中。

**生产 port**

上游已发布了 GCC 13，为此创建了新 port lang/gcc13。GCC 11 和 GCC 12 已在上游更新，计划发布 GCC 10 的新版本。现在需要更新所有相应的 port。

为了方便 port 维护者和用户的工作，我计划同时测试和更新以下所有更改：

- 更新 lang/gcc10、lang/gcc11、lang/gcc12；
- 将 GCC_DEFAULT 更新为 13；
- 在生产 port 上启用.init_array 和.fini_array；
- 将生产 port 从 LTO_BOOTSTRAP 切换回 STANDARD_BOOTSTRAP。

这将带来以下优势：

- 更少的 exp 运行进行更多的测试；
- 对于 ports 用户来说，需要的构建更少。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### Puppet
链接：

Puppet 网址: <https://puppet.com/docs/puppet/latest/puppet_index.html>

联系人：Puppet 团队 <puppet@FreeBSD.org>

Puppet 是一款自由软件的配置管理工具，由一个可信的源（Puppet Server）组成，它用领域特定语言描述机器的预期配置，以及在每个节点上运行的代理（Puppet Agent），用于强制实际配置与预期配置相匹配。可以设置一个可选的数据库（PuppetDB）用于报告和描述高级模式，其中一个机器的配置依赖于另一个机器的配置。

Puppet 团队正在维护 Puppet 和相关工具的 ports。

最近发布了 Puppet 8，并已添加到 ports 树中。

Puppet 6 已达到生命周期终点，并已被弃用。它现在已过期。因此，建议使用 Puppet 6 的用户更新到 Puppet 7 或 Puppet 8。

目前，Puppet 7 仍然是 ports 中依赖于 Puppet 的 port 的默认版本。Puppet 社区正在努力确保各种 Puppet 模块与最新代码兼容，在撰写本报告时，更新到 Puppet 8 可能会有一些挑战。情况每天都在好转，我们预计在几个月后，当模块更新的浪潮结束时，将切换到 Puppet 8 作为 Puppet 的默认版本。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### MITRE Caldera 在 FreeBSD 上的支持
链接：

MITRE Caldera 网址: <https://caldera.mitre.org/>

Red Canary 网址: <https://www.redcanary.com/>

联系人：José Alonso Cárdenas Márquez <acm@FreeBSD.org>

MITRE Caldera 是一个网络安全平台，旨在轻松自动化对手仿真，协助手动红队活动，并自动化事件响应。

它建立在 MITRE ATT&CK® 框架上，是 MITRE 的一个积极研究项目。

MITRE Caldera（security/caldera）于 2023 年 4 月添加到了 ports 中。这个 port 包含了对 [MITRE Caldera atomic 插件](https://github.com/mitre/atomic)使用的 [Atomic Red Team 项目](https://github.com/redcanaryco/atomic-red-team)的支持。

这项工作的主要目标是提高 FreeBSD 作为信息安全或网络安全有用平台的可见性。

此外，您可以使用 <https://github.com/alonsobsd/caldera-makejail> 或 <https://github.com/AppJail-makejails/caldera> 来测试MITRE Caldera 基础设施。AppJail 是一个用于从命令行管理 jail 容器的好工具。

欢迎有兴趣参与该项目的人提供帮助。

当前版本：4.2.0

**待办事项：**

- 添加 Caldera 测试基础设施 makejail。
- 将 FreeBSD 添加到 MITRE Caldera 官方支持的平台中，请参见 <https://github.com/mitre/caldera/pull/2752。>
- 将 FreeBSD 添加到 Red Canary 官方支持的平台中，请参见 <https://github.com/redcanaryco/atomic-red-team/pull/2450。>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### Wazuh 在 FreeBSD 上的支持

链接：

Wazuh 网址: <https://www.wazuh.com/>

联系人：José Alonso Cárdenas Márquez <acm@FreeBSD.org>

Wazuh 是一个免费且开源的平台，用于威胁预防、检测和响应。它能够保护在本地部署、虚拟化、容器化和云环境中的工作负载。

Wazuh 解决方案由部署在被监控系统上的终端安全代理和收集和分析代理收集的数据的管理服务器组成。Wazuh 的特性包括与 Elastic Stack 和 OpenSearch 的完全集成，通过这些工具，用户可以浏览安全警报。

Wazuh 在 FreeBSD 上的移植由 Michael Muenz 开始。他在 2021 年 9 月将 Wazuh 首次添加到 ports 树中，即 security/wazuh-agent。在 2022 年 7 月，我接手了这个 port 的维护，并开始移植其他 Wazuh 组件。

目前，所有的 Wazuh 组件都已经移植或适配：security/wazuh-manager、security/wazuh-agent、security/wazuh-server、security/wazuh-indexer 和 security/wazuh-dashboard。

在 FreeBSD 上，security/wazuh-manager 和 security/wazuh-agent 是从 Wazuh 源代码编译而来的。security/wazuh-indexer 是一个适配后的 textproc/opensearch，用于存储代理数据。security/wazuh-server 包含针对 FreeBSD 的配置文件适配。运行时依赖项包括 security/wazuh-manager、sysutils/beats8 (filebeat) 和 sysutils/logstash8。security/wazuh-dashboard 使用了一个适配后的 textproc/opensearch-dashboards 和从 wazuh-kibana-app 源代码生成的 FreeBSD 版本的 wazuh-kibana-app 插件。

这项工作的主要目标是提高 FreeBSD 作为信息安全或网络安全有用平台的可见性。

此外，您可以使用 <https://github.com/alonsobsd/wazuh-makejail> 或 <https://github.com/AppJail-makejails/wazuh> 来轻松测试 Wazuh 单节点基础设施（All-in-one）。AppJail 是一个用于从命令行管理 jail 容器的好工具。

欢迎有兴趣参与该项目的人提供帮助。

当前版本：4.4.4

**待办事项：**

- 添加 Wazuh 集群模式基础设施 makejail（正在进行中）
- 将 FreeBSD 添加到 Wazuh Inc 官方支持的平台中，请参见 <https://github.com/wazuh/wazuh-kibana-app/pull/5413>
- 添加 FreeBSD SCA 策略（正在进行中）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 第三方项目

许多项目构建在 FreeBSD 之上或将 FreeBSD 组件纳入其项目中。由于这些项目可能对更广泛的 FreeBSD 社区感兴趣，因此我们有时在季度报告中包含这些项目提交的简要更新。FreeBSD 项目对这些提交中的任何声明的准确性或真实性不作任何陈述。

#### PkgBase.live
链接：

网站 网址: <https://alpha.pkgbase.live/>

源代码 网址: <https://codeberg.org/pkgbase>

联系人：Mina Galić <freebsd@igalic.co>

PkgBase.live，一个非官方的 FreeBSD [PkgBase 项目存储库](https://wiki.freebsd.org/PkgBase)，已经恢复正常运行。

PkgBase.live 这项服务灵感来自于 <https://up.bsd.lv/>，它为 STABLE 和 CURRENT 分支提供了 freebsd-update(8) 的服务。up.bsd.live 本身已经暂停运行，所以这就更有理由重新启动 PkgBase.live。

目前，我们为以下平台提供构建：

- FreeBSD 13.2-RELEASE
- FreeBSD 13-STABLE
- FreeBSD 14-CURRENT

每个平台又分为以下架构：

- amd64
- aarch64
- armv7
- i386

你可能会注意到 RISCv64 目前暂时不可用。

硬件是在 Vultr 上的一台强大的 VPS。服务器和运行构建作业和提供软件包的 jail 是“自托管”的，这意味着它们安装并且保持更新，使用的是 PkgBase。

由于我们还没有弄清楚如何在 FreeBSD jails 中配置 Vultr 的 IPv6，PkgBase.live 目前不支持 IPv6。如果您对此有经验，请与我们联系！

除了用户和测试者外，我们仍然[非常鼓励其他人进行复制和模仿](https://alpha.pkgbase.live/howto/howdo.html)。

PkgBase 的硬件由 FreeBSD 社区的一名成员慷慨赞助。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 容器和 FreeBSD：Pot、Potluck 和 Potman
链接：
Pot 在 GitHub 上的组织 网址: <https://github.com/bsdpot>

联系人：Luca Pizzamiglio (Pot) <pizzamig@FreeBSD.org>

联系人：Bretton Vine (Potluck) <bv@honeyguide.eu>

联系人：Michael Gmelin (Potman) <grembo@FreeBSD.org>

Pot 是一个[支持通过 Nomad](https://www.freebsd.org/news/status/report-2020-01-2020-03/#pot-and-the-nomad-pot-driver) 进行编排的 FreeBSD Jail 管理工具。

在本季度，发布了 [Pot 0.15.5](https://github.com/bsdpot/pot/releases/tag/0.15.5) 版本，其中包含了一些来自多位贡献者的错误修复和特性，用于设置属性（[即 Jail 的 sysctl 变量](https://github.com/bsdpot/pot/pull/263)）。它将在 2023Q3 季度软件包集中提供。

Potluck 的目标是成为 FreeBSD 和 Pot 的 Dockerhub：一个 Pot 流派和完整容器映像的存储库，可在 Pot 中使用，并在许多情况下支持 Nomad。

所有 Potluck 容器都已重新构建为基于 FreeBSD 13.2 的映像，并使用 Pot signify 进行签名。

编写了《[使用 Ansible、Pot 等在 FreeBSD 上构建虚拟数据中心的初学者指南](https://honeyguide.eu/posts/ansible-pot-foundation/)》，其中解释了如何使用 Ansible playbooks 部署基于 Pot 和 Potluck 的复杂环境，包括示例节点（如 MariaDB、Prometheus、Grafana、nginx、OpenLDAP 或 Traefik），以及由 Nomad 和 Consul 管理的容器编排。

[Pot 团队提交的一个改进 Nomad 安全性的补丁](https://github.com/hashicorp/nomad/pull/13343)（Nomad 是支持通过 sysutils/nomad-pot-driver 进行 Pot 编排的调度程序和编排工具）已被上游接受，并将成为 Nomad 1.6.0 的一部分。

如常，欢迎提供反馈和补丁。

赞助商：Honeyguide Group


## FreeBSD 2023 年第一季度 季度状况报告

这是 2023 年第一季度的首份状态报告，共包括 25 个报告。除了我们习惯的团队报告，还包含云项目的一些新闻，以及 src、ports 和 doc 方面的进展等内容。

我们还介绍了 13.2-RELEASE 的一些信息，该版本被推迟到了 2023Q2 的开头。不过，由于这份报告的发布时间在 FreeBSD 新版本发布之后，因此该版本现在已经可以安装了。RELEASE 版本的用户现在可以受益于许多改进，例如更好的 iwlwifi（4）驱动程序支持或新的 rtw88（4）驱动程序。这些主题在过去的状态报告中也有涉及。

祝你愉快阅读。

状态团队代表 Lorenzo Salvadore

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

这份报告的网页版本可以在此处查看：

https://www.freebsd.org/status/report-2023-01-2023-03/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

目录

- FreeBSD 团队报告
  - FreeBSD 核心团队
  - FreeBSD 基金会
  - FreeBSD 发行工程团队
  - 集群管理团队
  - 持续集成
  - ports
  - 状态团队
- 用户空间
  - daemon(8) 改进
- 内核
  - 在 13.2 上启用使用日志软更新的文件系统的快照
  - 改进 kinst DTrace 提供程序
  - 原生 Linux timerfd
- 架构
  - 在 AArch64 上启用内核地址检测器
  - bsd-user：上游和状态报告
  - 云
  - 将 FreeBSD 作为一级 cloud-init 平台
  - 在 FreeBSD 上的 OpenStack
- 文档
  - 文档工程团队
  - FreeBSD 俄语文档项目
- ports
  - Freshports：SQL 注入攻击和帮助请求
  - DRM 驱动程序（即 GPU 驱动程序）
  - FreeBSD 上的 KDE
  - FSX
  - FreeBSD 上的 GCC
  - Valgrind - 准备 Valgrind 3.21
- 第三方项目
  - PkgBase.live
  - 容器和 FreeBSD：Pot、Potluck 和 Potman

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### FreeBSD 团队报告

这里是来自各个官方和半官方团队的条目，可在管理页面中找到。

#### FreeBSD 核心团队

联系方式：FreeBSD 核心团队 [core@FreeBSD.org](mailto:core@FreeBSD.org)

FreeBSD 核心团队是 FreeBSD 的管理机构。

**项目**

**核心团队章程：草稿**

2023 年第一次核心团队会议上，来自 12 月份在美国博尔德举行的会议的代表向整个团队呈报了他们的结论。团队将继续讨论这些问题，并与 FreeBSD 基金会一道努力。

**FreeBSD 年度开发者调查**

核心团队与 FreeBSD 基金会决定，由 FreeBSD 基金会负责进行年度开发者调查。

**Matrix 即时通讯方案**

核心团队继续评估 Matrix 作为 FreeBSD 开发者的即时通讯方案。一个实例已经准备好并正在进行测试。【译者注：Matrix 是一个开源的、去中心化的即时通讯协议和网络】

**提交权限**

- 核心团队批准了 Cheng Cui（cc@）的 src 提交权限。
- 核心团队批准恢复了 Joseph Koshy（jkoshy@）的 src 提交权限。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 基金会

链接：

FreeBSD 基金会网址：https://www.freebsdfoundation.org

技术路线图网址：https://freebsdfoundation.org/blog/technology-roadmap/

捐赠网址：https://www.freebsdfoundation.org/donate/

基金会合作伙伴计划网址：https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/

FreeBSD 杂志网址：https://www.freebsdfoundation.org/journal/

基金会新闻和事件网址：https://www.freebsdfoundation.org/news-and-events/

联系人：Deb Goodkin [deb@FreeBSDFoundation.org](mailto:deb@FreeBSDFoundation.org)

FreeBSD 基金会是一个 501(c)(3)非营利组织，致力于支持和推广全球的 FreeBSD 项目和社区。个人和企业的捐赠资金将用于资助和管理软件开发项目、会议和开发者峰会。我们还为 FreeBSD 贡献者提供旅行补助金，购买和支持硬件以改进和维护 FreeBSD 基础设施，并提供资源以改进安全、质量保证和发布工程方面的工作。我们出版营销材料以推广、教育和宣传 FreeBSD 项目，促进商业供应商和 FreeBSD 开发者之间的合作，并最终代表 FreeBSD 项目执行合同、许可协议和其他需要认可法律实体的法律安排。

**募捐工作**

我们终于得到了 2022 年的筹款数额，总共筹集了 $1,231,096！虽然我们没有达到预定目标，导致我们不得不从我们的长期投资中撤回了约 $74,000。

除了从我们的用户和贡献者那里获得了许多捐赠外，我们还从 Juniper、Meta、Arm、Netflix、Beckhoff、Tarsnap、Modirum、Koum 家族基金会和 Stormshield 等公司获得了较大的捐赠。我代表基金会向所有个人和企业，包括捐赠者，对你们在 2022 年的财政贡献表示衷心感谢！

今年我们的预算约为 2,230,000 美元，其中包括增加对 FreeBSD 宣传和软件开发的支出。超过一半的预算被分配给与改进 FreeBSD 和保持其安全性直接相关的工作。为了给 2023 年的预算提供资金，我们提高了筹款目标，并计划使用一些投资资金。当我们收到第一笔百万美元的捐款时，我们的计划是每年最多使用其中的 10% 来增加我们改进 FreeBSD 的工作，所以这已经是我们几年来资金计划的一部分。【译者注：我也没看懂最后一句话是什么意思】

2023 年的预算正在董事会的审批过程中，并将在获批后发布。

本季度我们收到了来自 Juniper、Tarsnap、微软和 Stormshield 的捐赠。所以，我们已经有了一个很好的开端！但是，我们绝对需要更多的支持来支持我们 2023 年的计划。

如果您想帮助我们继续努力，请考虑向我们的 2023 年筹款活动捐款！https://www.freebsdfoundation.org/donate/

我们还有一个针对更大的商业捐赠者的合作伙伴计划。您可以在https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/了解详情。

#### 系统优化

在 2023 年第一季度，有 226 个 src、39 个 port 和 12 个 doc 提交的改动中，有一些是由 FreeBSD 基金会赞助的。其中一些受赞助的工作在单独的报告条目中有所描述，包括：

- 持续集成
- 在使用日志软更新的文件系统上启用快照
- 将 FreeBSD 作为一级 cloud-init 平台
- FreeBSD 发布工程团队
- 改进 kinst DTrace provider
- 在 FreeBSD 上使用 OpenStack

基金会赞助的其他工作包括：

- 修复和更新 OpenSSH 到 9.2p1 和 9.3p1 版本
- 厂商将 libpcap 导入和更新到 1.10.3 版本【译者注："vendor import" 意味着该更新是由软件供应商导入的，可能是为了提高该软件库与其它软件之间的兼容性。】
- 改进 tmpfs、msdosfs 和 makefs
- 添加新的 kqueue1 系统调用
- 更新 man 页面
- 修复 dtrace 和 bhyve 问题
- LinuxKPI 的工作

**持续集成和质量保证**

基金会为 FreeBSD 项目提供流量全职员工和资金，以改进持续集成、自动化测试和整体质量保证工作。您可以在专门的报告中阅读有关 CI 工作的更多信息。FreeBSD 基金会目前资助的一个项目是开发一组脚本，帮助 src 开发人员自行进行 CI 测试。其中的主要目标之一是在提交前提供更多的可见性。[第一个里程碑式的代码审查](https://reviews.freebsd.org/D38815)已经提交。

**FreeBSD 的宣传和教育**

我们的大部分工作都致力于推广 FreeBSD 项目。这可能包括推广有趣的 FreeBSD 项目，制作文献和视频教程，参加活动或者进行演讲。我们制作的文献旨在教授人们 FreeBSD 基础知识，帮助他们更容易地使用或者为项目做出贡献。除了参加活动和演讲，我们还鼓励和帮助社区成员自行组织 FreeBSD 活动、演讲或者承担 FreeBSD 展台。

FreeBSD 基金会赞助了全球许多会议、活动和峰会。这些活动可能与 BSD 相关，也可能与开源或者技术有关，面向的人群可能是被较少关注的群体。我们支持以 FreeBSD 为主题的活动，帮助为分享知识、共同开发项目以及促进开发者和商业用户之间的协作提供场所，从而提供健康的生态环境。我们支持非 FreeBSD 相关的活动，以促进和提高对 FreeBSD 的认识，扩大 FreeBSD 在不同应用领域的使用，并招募更多项目贡献者。我们现在大部分时间都是亲自参加活动，并开始计划于 2023 年 5 月举办的 BSDCan 开发者峰会。除了参加和计划活动外，我们还在不断制定新的培训计划，更新我们的指南，以帮助更多人尝试使用 FreeBSD。

看看我们的宣传和教育工作：

- 在 2023 年 2 月 4-5 日比利时布鲁塞尔举办的 FOSDEM 上设置了展台。查看旅行报告。
- 在 2023 年 2 月 7-8 日英国伦敦举办的“开放状态”（State of Open Con）上设立了桌子。阅读更多信息。
- 在 2023 年 3 月 9-12 日加利福尼亚州帕萨迪纳举办了 SCALE 20x 的工作坊和展台。查看旅行报告。
- 在 2023 年 3 月 23 日，赞助了在北卡罗来纳州夏洛特市举办的“开源 101”活动。
- 赞助并开始策划于 2023 年 5 月 17-18 日在安大略省渥太华举行的 2023 年 5 月开发者峰会。
- 获得了媒体合作伙伴赞助地位，并为 2023 年 10 月 15-17 日在北卡罗来纳州罗利举办的“All Things Open”提交了工作坊申请。
- 提交了在 2023 年 7 月 13-16 日在俄勒冈州波特兰举办的 FOSSY 的工作坊提案。
- FreeBSD 项目被接纳为谷歌代码之夏的参与组织。
- 我们举办了 GSoC Office Hours，以帮助有问题的潜在参与者。
- 发布了三月份的通讯。
- 其他博客文章
  - [了解 FreeBSD 和 Ampere Altra 的内部结构](https://freebsdfoundation.org/blog/under-the-hood-with-freebsd-and-ampere-altra/)
  - [新的开放职位：FreeBSD 用户空间软件开发人员](https://freebsdfoundation.org/blog/under-the-hood-with-freebsd-and-ampere-altra/) - 注意：此招聘已关闭。
  - [BSDCan 2023 旅行补助申请现已开放](https://freebsdfoundation.org/blog/bsdcan-2023-travel-grant-application-now-open/) - 注意：申请已关闭。
- FreeBSD 在新闻中的表现
  - [VMBlog 与 Deb Goodkin 关于开放状态的问答](https://freebsdfoundation.org/news-and-events/latest-news/vmblog-state-of-open-con-qa-with-deb-goodkin/)

我们通过出版专业制作的 FreeBSD Journal 来帮助全球了解 FreeBSD。正如我们之前提到的，FreeBSD Journal 现在是免费的出版物。您可以在 https://www.freebsdfoundation.org/journal/ 了解更多信息并访问最新问题。

您可以在 https://www.FreeBSDfoundation.org/news-and-events/ 了解我们参加的活动和即将举行的活动。

**法律/FreeBSD 知识产权**

基金会拥有 FreeBSD 商标，并有责任保护它们。我们还为核心团队提供法律支持，以调查出现的问题。【译者注：基金会至今为止并未就 FreeBSD 在中国境内的商标被抢注一事给出解决方案】

请访问 https://www.freebsdfoundation.org 了解有关我们如何支持 FreeBSD 以及如何帮助您的更多信息！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 发布工程团队

链接：

FreeBSD 13.2-RELEASE 日程安排网址：https://www.freebsd.org/releases/13.2R/schedule/

FreeBSD 14.0-RELEASE 日程安排网址：https://www.freebsd.org/releases/14.0R/schedule/

FreeBSD releases 版本网址：https://download.freebsd.org/releases/ISO-IMAGES/

FreeBSD 开发快照网址：https://download.freebsd.org/snapshots/ISO-IMAGES/

联系人：FreeBSD 发布工程团队，re@FreeBSD.org

FreeBSD 发布工程团队负责制定和发布 FreeBSD 官方项目的发布时间表，宣布代码冻结并维护相应的分支，等等。

在 2023 年第一季度，发布工程团队开始着手筹备即将到来的 13.2-RELEASE 版本。截至本文写作时，13.2 版本的开发已经按照最初设定的时间表进行，只不过增加了第四、第五和第六个 RC 版本的构建，将最终版本的发布时间从 3 月底推迟到了 4 月初。

发布工程团队继续为主分支、stable/13 分支和 stable/12 分支提供每周开发快照版本的构建。

赞助商：Rubicon Communications，LLC（“Netgate”）

赞助商：Tarsnap

赞助商：FreeBSD 基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 集群管理团队

链接： 集群管理团队成员链接：https://www.freebsd.org/administration/#t-clusteradm 联系方式：集群管理团队 clusteradm@FreeBSD.org

FreeBSD 集群管理团队负责管理项目所依赖的机器，以同步分布式工作和通信。

在本季度中，该团队开展了以下工作：

- 定期支持 FreeBSD.org 用户账户。
- 为所有物理主机和镜像提供定期的磁盘和零件支持（和更换）。
- 改进 PowerPC 软件包构建器。
  - 借助 FreeBSD 基金会获得的新部件，构建器现在具有新的带散热片和带有更多缓存的 NVME。它有助于解决散热问题，现在他们正在更快地构建软件包。
- 将动态资源从主网站中解耦。
  - 与 doceng 和 webmaster 协调工作，从网站 www.FreeBSD.org 和 docs.FreeBSD.org 中解耦动态资源。

**正在进行的工作**

- 在我们的主站点进行大规模的网络升级。
  - 新的 Juniper 交换机已经到达我们的主站点，以替换以前的交换机。我们感谢 Juniper 的捐赠。
- 替换我们主站点和几个镜像中的旧服务器。
  - 除了已经损坏的 CI 服务器外，我们还有一些带有损坏磁盘和有故障电源的旧服务器。这项任务与 FreeBSD 基金会和捐助者/赞助商协作。
- 部署基础设施以镜像网站。
  - 由于 FreeBSD 网站现在基本上是静态的，我们已经开始部署基础设施，在由 FreeBSD 项目管理的镜像中在全球范围内镜像 www.FreeBSD.org 和 docs.FreeBSD.org。
- 为内部 FreeBSD.org 搜索需求（如邮件列表和文档）创建新的搜索数据库引擎。

**FreeBSD 官方镜像概述**

当前位置包括澳大利亚、巴西、德国、日本（两个完整的镜像站点）、马来西亚、南非、台湾、英国（完整的镜像站点）和美国（加利福尼亚州、新泽西州\[主站点]和华盛顿州）。

硬件和网络连接由以下机构慷慨地提供：

- [Bytemark Hosting](https://www.bytemark.co.uk/)
- [BroadBand Tower 公司的云和 SDN 实验室](https://www.bbtower.co.jp/)
- [国立阳明交通大学计算机科学系](https://www.cs.nycu.edu.tw/)
- [Equinix](https://deploy.equinix.com/)
- [澳大利亚互联网协会](https://internet.asn.au/)
- [互联网系统协会](https://www.isc.org/)
- [INX-ZAv](https://www.inx.net.za/)
- [KDDI Web Communications 公司](https://www.kddi-webcommunications.co.jp/)
- [马来西亚研究和教育网络](https://myren.net.my/)
- [Metapeer](https://www.metapeer.com/)
- [New York Internet](https://www.nyi.net/)
- [NIC.br](https://nic.br/)
- [Your.Org](https://your.org/)

法兰克福单服务器镜像是欧洲带宽和使用率方面的主要镜像。

我们仍在寻找一个额外的全镜像站点（五台服务器）来取代英国的全镜像站点中的旧服务器。

我们发现在全球互联网交换点拥有单个镜像的模式非常好（在澳大利亚，巴西和南非）；如果您知道或在这些机构工作，可以赞助单个镜像服务器，请与我们联系。美国（西海岸）和欧洲（任何地方）是首选地点。

请查看完整镜像站点规格的[通用镜像布局](https://wiki.freebsd.org/Teams/clusteradm/generic-mirror-layout)和单个镜像站点的 [Tiny Mirror](https://wiki.freebsd.org/Teams/clusteradm/tiny-mirror)。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**连续集成**

链接：

FreeBSD Jenkins 实例网址：https://ci.FreeBSD.org

FreeBSD CI 构件存档网址：https://artifact.ci.FreeBSD.org

FreeBSD Jenkins wiki 网址：https://wiki.FreeBSD.org/Jenkins

托管 CI wiki 网址：https://wiki.FreeBSD.org/HostedCI

第三方软件 CI 网址：https://wiki.FreeBSD.org/3rdPartySoftwareCI

与 freebsd-testing@ 相关的工单网址：https://bugs.freebsd.org/bugzilla/buglist.cgi?bug\_status=open\&email1=testing%40FreeBSD.org\&emailassigned\_to1=1\&emailcc1=1\&emailtype1=equals

FreeBSD CI 代码库网址：https://github.com/freebsd/freebsd-ci

dev-ci 邮件列表网址：https://lists.FreeBSD.org/subscription/dev-ci

联系人：Jenkins 管理员 jenkins-admin@FreeBSD.org

联系人：Li-Wen Hsu lwhsu@FreeBSD.org

联系人：freebsd-testing 邮件列表

联系人：IRC EFNet 上的 #freebsd-ci 频道

2023 年第一季度，我们与项目的贡献者和开发人员合作，满足他们的测试需求。同时，我们与外部项目和公司合作，通过在 FreeBSD 上进行更多测试来增强他们的产品。

重要的已完成的任务：

- 添加了 FreeBSD-main-aarch64-KASAN_test 及其支持任务。
- 添加了 FreeBSD-stable-13-amd64-KASAN_test 及其支持任务。
- FreeBSD-main-amd64-gcc12_build 现在会将失败的报告发送给可能相关的提交者。
- trasz@ 修复或解决了非 x86 架构测试中的各种问题。
- 在 AsiaBSDCon 2023 开发者峰会上呈现测试/CI 状态更新。

正在进行的任务：

- 设计并实施预提交 CI 构建和测试（以支持工作流工作组）。
- 设计并实施使用 CI 集群来构建发布产品，就像发布工程所做的那样。
- 简化为贡献者和开发者设置 CI/测试环境的步骤。
- 设置 CI 阶段环境并在其中放置实验性任务。
- 整理 freebsd-ci 存储库中的脚本，为合并到 src 存储库做准备。
- 改进硬件测试实验室并添加更多硬件进行测试。
- 合并 https://reviews.freebsd.org/D38815。
- 合并 https://reviews.freebsd.org/D36257。

开放或等待中的任务：

- 收集和分类 CI 任务和想法。
- 为运行测试的 VM 客户机设置公共网络访问。
- 实现使用裸金属硬件运行测试套件。
- 添加对 -CURRENT 的 drm port 构建测试。
- 计划运行 ztest 测试。
- 帮助更多软件在其 CI 流水线中获得 FreeBSD 支持（Wiki 页面：3rdPartySoftwareCI、HostedCI）。
- 与托管 CI 服务提供商合作，以获得更好的 FreeBSD 支持。

请参阅与 freebsd-testing@ 相关的工单，以获取更多正在进行的信息，也欢迎加入我们的努力！

赞助：FreeBSD 基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Ports**

链接：

FreeBSD Ports 简介：https://www.FreeBSD.org/ports/

贡献 Ports：https://docs.freebsd.org/en/articles/contributing/#ports-contributing

FreeBSD Ports 监控：http://portsmon.freebsd.org/

Ports 管理团队：https://www.freebsd.org/portmgr/

Ports 压缩包：http://ftp.freebsd.org/pub/FreeBSD/ports/ports/

联系人：René Ladan portmgr-secretary@FreeBSD.org

联系人：FreeBSD Ports 管理团队 portmgr@FreeBSD.org

Ports 管理团队负责监督 Ports 的整体方向、构建软件包（通过其附属项 pkgmgr），以及人员问题。以下是本季度的情况。

目前，我们的 Ports 中大约有 33,500 个 port。对于这些 port，共有 3,021 个待解决的 bug 报告，其中 764 个未分配。今年前三个月，主分支有 163 名提交者提交了 9,021 个 commit，2023Q1 分支有 55 名提交者提交了 701 个 commit。与 2022Q4 相比，这意味着在 port 数量、ports PR、ports commit 和活跃的 port 提交者数量略有增加。

在本季度，我们欢迎了 Robert Clausecker (fuz@)、Vladimir Druzenko (vvd@)、Robert Nagy (rnagy@)，并欢迎 Norikatsu Shigemura (nork@) 回归，同时告别了 Marius Strobl (marius@)。Portgmr 在成功地担任 lurkership 后，新增了 Muhammad Moinur Rahman (bofh@) 为新成员。

在 portmgr 双周会议期间，讨论了以下话题：

- 改善内核模块二进制包的情况
- 如何衡量 ports 对它们的依赖项的影响以及如何维护高影响力的 ports。

在本季度，进行了 32 次 exp-run 来测试 port 更新、更新默认版本（LLVM 到 15、MySQL 到 8.0、Ruby 到 3.1）以及在基础设施中更新 byacc。此外，Go 的默认版本更改为 1.20，Lazarus 的默认版本更改为 2.2.6。

引入了四个新的 USES：

- `budgie` 用于支持与 Budgie 桌面相关的 port
- `ldap` 提供对 OpenLDAP 的支持，新的默认版本为 2.6
- `nextcloud` 用于支持 Nextcloud 应用程序
- `ruby` 用于提供对 Ruby ports 的支持（前身为 bsd.ruby.mk）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**状态团队**

链接:

FreeBSD 状态报告网址: https://www.freebsd.org/status/

FreeBSD 状态报告流程网址: https://docs.freebsd.org/en/articles/freebsd-status-report-process/

归档状态报告的 GitHub 仓库网址: https://github.com/freebsd/freebsd-quarterly

联系: status@FreeBSD.org

**新的工作计划已经启动**

在今年的第一季度，状态团队开始实施在 2022 年底宣布的新的工作流。以下是一些详细信息。

新的电子邮件地址

上一季度，我们宣布创建了新的电子邮件地址:

• status@FreeBSD.org, 用于直接与状态团队互动；

• status-submissions@FreeBSD.org, 用于发送报告提交；

• freebsd-status-calls@FreeBSD.org, 一个邮件列表，您可以订阅以获得有关状态报告提交截止日期的提醒。

不幸的是，邮件列表目前无法正常工作。该问题已报告，但尚未找到解决方案。但是，通过一种变通方法，第二和最后一个提醒可以发送到该列表。

**自动化**

为了确保没有报告遗漏，一些自动化措施已经被引入：

- 在 Phabricator 上，引入了一个 Heral 规则，自动阻止任何与状态报告目录相关的代码评审：即使报告提交者忘记将状态团队添加为评审人，Salvadore@（状态团队成员）也会阻止补丁的合并。同样的规则还会阻止任何将状态团队列为评审人的评审，以确保提交之前至少有一个状态团队成员审核了补丁。
- 一个 GitHub action 自动将新引入的状态报告标签添加到任何涉及状态报告目录的 pull request 中。该 GitHub action 应该可以轻松地由任何人进行修改，以便根据修改文件的路径自动应用更多标签。

计划引入更多自动化。

**文档重组**

状态报告的 README 和 How To 已经更新并合并为一个独特的文档：FreeBSD 状态报告过程。您可以查看该文档以了解有关报告提交和发布的详细信息。随着状态团队继续实施其新工作流程，该文档将定期更新。特别是，有关自动化的新材料即将推出。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 用户空间

影响基础系统和其中程序的更改。

#### 改进 daemon(8)

链接: daemon(8) 网址: https://man.freebsd.org/daemon/8

Libera IRC 网址: https://libera.chat/

联系人: Ihor Antonov ihor@antonovs.family

联系人: Kyle Evans kevans@FreeBSD.org

一项持续改进的工作正在进行，旨在提高 daemon 实用工具的代码质量和监督能力。daemon 是一个工具，可以将任何运行中的进程守护化（发送到后台）或监督它，如果它崩溃则自动重启。Daemon 在 port 中被广泛使用，并可以在基础系统中更多地使用。

本季度添加了 `long_opts` 支持，代码库经过了初始的重构阶段，以准备进行进一步的更改。目前还没有功能性的更改，但是更多的更改即将到来。如果遇到意外的错误，请直接联系或在 Libera IRC 的 #freebsd-dev 上进行反馈。

下一季度计划的工作项：

- 使用 kqueue 作为所有事件源【译者注：利用 kqueue 作为事件驱动的框架，来监听并响应所有的事件】
- 修复 Bug #268580
- 修复 Bug #236117
- 修复 Bug #254511
- 修复 Bug #212829
- `procctl PROC_REAP_ACQUIRE`

我们正在寻求反馈、错误报告（旧和新）和功能请求。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 内核

在内核子系统、驱动程序支持、文件系统等方面的更新。

#### 在 13.2 上启用基于日志软更新的文件系统快照

联系人：Marshall Kirk McKusick [mckusick@freebsd.org](mailto:mckusick@freebsd.org)

在 2023 年第一季度，能够在运行日志软更新时对 UFS/FFS 文件系统进行快照，并使用它们对活动文件系统进行后台转储的功能被合并到 releng/13.2，将在 FreeBSD 13.2-RELEASE 中发布。

使用 `-L` 参数请求后台转储。

这个项目的详细信息在 [2022 年第四季度的报告](https://www.freebsd.org/status/report-2022-10-2022-12/#_enabling_snapshots_on_filesystems_using_journaled_soft_updates)中有说明。

赞助：FreeBSD 基金会 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 改进 kinst DTrace provider

链接：

libdtrace: 实现内联函数跟踪网址：https://reviews.freebsd.org/D38825

dtrace(1): 添加 -d 参数以在 post-dt_sugar 后转储 D 脚本网址：https://reviews.freebsd.org/D38732

联系人：Christos Margiolis [christos@FreeBSD.org](mailto:christos@FreeBSD.org)

联系人：Mark Johnston [markj@FreeBSD.org](mailto:markj@FreeBSD.org)

kinst 是由 christos@ 和 markj@ 创建的新的 DTrace provider，允许对内核函数进行任意指令跟踪。kinst 已经添加到 FreeBSD 14.0 的基本系统中。

2022Q3 状态报告简要介绍了 kinst。我们现在正在进行内联函数跟踪（请参见上面的 D38825 审阅）-这是一个备受期待的 DTrace 功能-通过使用内核 DWARF 和 ELF 信息找到每个内联副本的调用点，并使用该信息转换 D 语法，将 kinst 探针转换为以下形式：

```
   kinst::<inline_func>:<entry/return>
        /<pred>/
        {
                <acts>
        }
```

变为：

```
   kinst::<caller_func1>:<offset>,
        kinst::<caller_func2>:<offset>,
        kinst::<caller_func3>:<offset>
        /<pred>/
        {
                <acts>
        }
```

示例：

```
   # dtrace -dn 'kinst::cam_iosched_has_more_trim:entry { printf("\t%d\t%s", pid, execname); }'
        kinst::cam_iosched_get_trim:13,
        kinst::cam_iosched_next_bio:13,
        kinst::cam_iosched_schedule:40
        {
                printf("\t%d\t%s", pid, execname);
        }

        dtrace: description 'kinst::cam_iosched_has_more_trim:entry ' matched 3 probes
        CPU     ID                    FUNCTION:NAME
          2  79315          cam_iosched_next_bio:13     0       kernel
          2  79316          cam_iosched_schedule:40     0       kernel
          0  79316          cam_iosched_schedule:40     12      intr
          2  79315          cam_iosched_next_bio:13     0       kernel
          2  79316          cam_iosched_schedule:40     0       kernel
          0  79316          cam_iosched_schedule:40     12      intr
        ^C
```

dtrace(1) 新增了一个 `-d` 参数 ，它在 libdtrace 应用语法转换后会将 D 脚本进行转储。

其他的目标包括：

- 在 D 中实现一个 `locals` 结构，用于存储跟踪函数的局部变量。例如，在 `kinst::foo:<x>` 中，我们可以通过在 D 脚本中使用 `print(locals→bar)` 来打印局部变量 bar。
- 将 kinst 移植到 RISC-V / ARM64。

赞助者：FreeBSD 基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 原生的 Linux timerfd

链接:

Differential revision 网址: https://reviews.freebsd.org/D38459

联系人: Jake Freeland jfree@FreeBSD.org

timerfd 是一组 Linux 标准系统调用，可操作间隔定时器。这些定时器类似于每个进程的定时器，但由文件描述符表示，而不是进程。这些文件描述符可以传递给其他进程，在 fork(2) 时保留，并可以通过 kevent(2)、poll(2) 或 select(2) 进行监视。

FreeBSD 已经存在一个 timerfd 实现，用于 Linux 兼容性，但此差异修订使接口本地化。这个更改的目标是为了方便在包含 timerfd 的程序的 FreeBSD 移植过程。

此特定实现避免向系统调用表中添加新名称。相反，timerfd_create() 被 specialfd() 系统调用包装。timerfd_gettime() 和 timerfd_settime() 调用由 ioctl() 包装。

希望支持 FreeBSD 的开发人员应避免使用 timerfd。首选使用 kqueue() EVFILT_TIMER 过滤器来建立任意定时器。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 架构

更新平台特定功能并为新硬件平台带来支持。

#### AArch64 上的内核地址消毒剂（Kernel Address Sanitizer）

联系人：Kyle Evans kevans@FreeBSD.org

内核地址消毒剂是一种检测 bug 的设施，它使用编译器（在本例中为 LLVM）插入的仪器和运行时状态跟踪的组合来检测 C 代码中的 bug。它们可以自动检测许多类型的 C 语言编程 bug，例如使用后释放和使用未初始化的变量，否则可能需要大量工作才能确定。它们特别适用于与回归测试套件或模糊工具（如 syzkaller）组合使用。与 Valgrind 等工具不同，必须重新编译软件才能启用给定的内核地址消毒剂，但内核地址消毒剂可以在内核中使用。启用了内核地址消毒剂的内核会在运行时产生显着的性能开销，包括 CPU 利用率和内存使用。

自 [89c52f9d59fa](https://cgit.freebsd.org/src/commit/?id=89c52f9d59fa) 以来，先前仅限于 amd64 的内核地址消毒剂已经被移植到了 arm64。

此前已在多种机器上进行了测试，包括：

- 各种 Ampere Altra 机器
- QEMU
- 微软的“Volterra”Devkit
- bhyve（正在进行中）。

欢迎和感激在其他硬件上进行进一步测试。

赞助：Juniper Networks，Inc.

赞助：Klara，Inc.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### bsd-user：上游支持和状态报告

【译者注：bsd-user 是 QEMU（Quick Emulator）项目的一部分，它是一个用户空间模拟器，可以在不同的操作系统之间进行二进制指令的转换，从而实现在一个操作系统上运行另一个操作系统的程序。具体来说，bsd-user 是 QEMU 中用于模拟 BSD 系统调用的部分。通过 bsd-user，用户可以在基于 BSD 的操作系统之间运行二进制程序，而无需重新编译它们。】

链接：

QEMU 项目网址：https://qemu.org

FreeBSD bsd-user qemu fork 网址：https://github.com/qemu-bsd-user/qemu-bsd-user

QEMU 项目的 GitLab 镜像网址：https://gitlab.com/qemu-project/qemu

联系人：Warner Losh imp@FreeBSD.org

在这一季度中，Warner Losh 在 qemu-project 仓库上提交了两个 patch 集（第三个还在等待中）。Doug Rabson 提交了一些优化，以保存 qemu-user 模拟器的句柄供未来的 exec 使用。联系了一些希望在 NetBSD 上让 bsd-user 工作的人。代码之夏上游的项目表现出了一些兴趣。

**上游的努力**

本季度 sysctl 系统调用被上游了。Doug 的一些更改也被上游了（见下文）。在 NetBSD 和 OpenBSD 上进行一些清理以及在运行时动态生成系统调用仍在等待上游。

**Doug Rabson 的更改**

在他的容器工作的一部分中，Doug 提交了一些更改，允许内核缓存用于运行程序的模拟器。这使得内核可以使用缓存的模拟器直接 exec 新二进制文件。这简化了 bsd-user 并消除了它与 linux-user 之间的一个差异。Doug 还提供了一个重要的修复，防止 aarch64 运行失败。

**Bug 修复和改进**

除了 Doug 的修复外，这一季度 Warner 还进行了一些清理工作：

- Warner 移除了仿真器中存在的“运行在任何 BSD 代码上”的最后几个部分。
- 虽然基本的系统调用可以在所有 BSD 之间进行仿真，但它们的系统调用接口已经分化太多，太过丰富，因此短期内无法实现。
- Warner 原计划只移除 NetBSD 和 OpenBSD 的部分，但至少 NetBSD 的人员对构建这些东西表现出了兴趣。
- 现在，NetBSD 的人员已经有了联系方式并知道了方向，Warner 希望他们会提交一个 pull 请求，用于在 NetBSD 上构建 bsd-user。
- Warner 添加了 SIGSYS 支持，以便我们能够更早地捕获未实现的系统调用，并改进了有关它们的报告，以获取更多关于失败原因的数据。
- Warner 在 `blitz` 分支中清理了一些代码。
- 我们已经在使用的 `blitz` 分支中合并了上游最新的 8.0rc1。

**代码之夏项目**

对于 Qemu 的 project 列表中添加的 bsd-user upstreaming 任务，有很大的兴趣。运气好的话，我们将有一个学生来完成上游化所有运行简单程序所需的系统调用的工作。运气更好的话，我们将能够运行任何执行与 clang 相同的操作的程序（其中一个目标是使其编译 helloworld）。如果我们有机会得到这个位置，未来的季度报告将提供详细信息。

**需要帮助**

我们始终需要关于 bsd-user 的帮助。

- 欢迎为新系统调用提交 pull 请求。
- 自动生成我们手动完成的许多工作的自动化将会有所帮助（例如系统调用参数跟踪）。
- 热情的志愿者想要帮助我进行上游（如果您不想提交代码，许多任务都很简单和快速）。
- 与 NetBSD 人员协调和清理他们提出的内容。
- 需要修复 bug（特别是线程的 bug）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 云计算

更新云计算特定功能并引入对新云平台的支持。

#### FreeBSD 作为一级 Cloud-init 平台

链接：

cloud-init 网站 网址: https://cloud-init.io/

cloud-init 文档 网址: https://cloudinit.readthedocs.io/en/latest/

cloud-init 持续重构 网址: https://github.com/canonical/cloud-init/blob/main/WIP-ONGOING-REFACTORIZATION.rst

联系人：Mina Galić freebsd@igalic.co

Cloud-init 是云中配置服务器的标准方式。不幸的是，除 Linux 外，其他操作系统的 cloud-init 支持相对较差，而 FreeBSD 上缺乏 cloud-init 支持则妨碍了那些希望将 FreeBSD 作为一级平台提供的云服务提供商。为了解决这个问题，该项目旨在使 FreeBSD 的 cloud-init 支持与 Linux 支持相当。更广泛的计划是提高所有 BSD 的支持。

由于个人原因，本季度进展非常缓慢，也因为缺乏正确资源的访问。我一直在尝试移植 Infiniband 功能。这证明很困难，因为它推翻了我的观点，即 ifconfig(8) 是在 FreeBSD 上了解网络接口所需的全部内容。

在等待资源的同时，我调试了引导 pamic 并解决了它：[499171a98c88](https://cgit.freebsd.org/src/commit/?id=499171a98c8813e4dc6e085461d5c47750efa555)。这使得可以在 LXD 上引导 FreeBSD，即 cloud-init 的 CI 平台。我们仍然需要解决高 CPU 使用率问题，但已经有一个已接受的审核：D38898。

一个 cloud-init 的同事在 Azure 工作，他成功让我使用 Azure 上的 HPC VM。不幸的是，这只是一个有限的时间，并不足以弄清楚如何在 FreeBSD 上启用 Infiniband，这是由 Linux 上的 Azure Agent 处理的任务，但 FreeBSD 的 sysutils/azure-agent 相当缺乏。

对此项目感兴趣的人可以提供来自其 Infiniband 系统的 ifconfig(8)、ibstat(8)、ibv_devinfo(1) 等复制。我也非常希望获得配有 Infiniband NIC 的硬件访问权限，或者听到在 Azure HPC 上成功使用 FreeBSD 的人的消息。

如果对该平台感兴趣，我将把一些精力用于修复 Azure Agent。

赞助商：FreeBSD 基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 在 FreeBSD 上运行 OpenStack

链接：

OpenStack 网址: https://www.openstack.org/

FreeBSD 上的 OpenStack 网址: https://github.com/openstack-on-freebsd

联系人：Chih-Hsin Chang [starbops@hey.com](mailto:starbops@hey.com)

联系人：Li-Wen Hsu [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

该项目旨在移植关键的 OpenStack 组件，以便 FreeBSD 可以作为 OpenStack 主机运行。

在 2023 年第一季度，最重要的消息是我们能够在 OpenStack 平台上使用 bhyve(8) 生成 FreeBSD 实例。但仍存在一些需要解决的主要限制，包括：

- 没有自助网络（仅支持平面网络）【译者注：即在 FreeBSD 上使用 OpenStack 平台时，没有自动创建虚拟网络的能力。只能使用 "flat network"，这意味着所有虚拟机都连接到同一网络中，并且需要手动进行网络配置。】
- 实例内没有网络连接
- 仅支持 FreeBSD RAW 镜像（已测试 FreeBSD-13.1-RELEASE-amd64.raw）
- 无法调整磁盘大小
- 没有控制台集成（需要手动使用 cu(1)命令）

在文档存储库中可以找到构建 POC 站点的逐步文档。每个 OpenStack 组件的修补版本都在同一个 GitHub 组织下。

此外，我们在三月底参加了 AsiaBSDCon 2023，并在开发者峰会上就当前项目状态发表了短暂的演讲。我们在活动中得到了宝贵的反馈，下一季度将专注于以下事项：

- 解决 Open vSwitch 网络问题
- 将每个 OpenStack 组件转换为 FreeBSD port

有兴趣帮助该项目的人可以首先按照安装指南检查文档。以下是该项目的一个开放任务：

- oslo.privsep 库的 FreeBSD 特定实现

欢迎提供反馈和帮助。

赞助商：The FreeBSD Foundation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 文档

文档、手册页面或新外部书籍/文档的重要更改。

### 文档工程团队

链接：

FreeBSD 文档项目网址: https://www.freebsd.org/docproj/

FreeBSD 文档项目新贡献者指南网址: https://docs.freebsd.org/en/books/fdp-primer/

文档工程团队网址: https://www.freebsd.org/administration/#t-doceng

联系方式：FreeBSD 文档工程团队 [doceng@FreeBSD.org](mailto:doceng@FreeBSD.org)

doceng@ 团队是处理 FreeBSD 文档项目中一些元项目问题的机构。有关详细信息，请参见 FreeBSD 文档工程团队章程。

在最近的季度中：

- Pau Amma 获得了 doc 提交权限。
- 提议将 Lorenzo Salvadore 作为 doc 提交者。carlavilla@ 和 dbaio@ 将担任他的导师。
- Ryusuke SUZUKI 从 doceng 中退出。doceng 感谢 ryusuke@ 的贡献。

待处理和讨论的事项：

- 添加了有关许可证的新文档。

Port 开发者手册:

已向手册添加了三个新的 `Uses` 开关：

- 新的 Uses = ruby。
- 新的 Uses = ldap。
- 新的 Uses = budgie。

此外：

- 修复了 NVIDIA 的安装和配置选项。
- 改进了高级网络章节。

#### 在 Weblate 上的 FreeBSD 翻译

链接：在 Weblate 上翻译 FreeBSD

链接：FreeBSD Weblate 实例

**Q4 202 2 状态**

- 12 种语言
- 150 名注册用户

**语言**

- 简体中文(zh-cn) (进度：14%)【译者注：实际进度应该是 0%。本社区项目因为种种原因无法合并，现在需要人手来合并，要求了解 adoc 和 markdown 语法，能找到对应英语的中文翻译译文】
- 繁体中文(zh-tw) (进度：11%)
- 荷兰语(nl) (进度：1%)
- 法语(fr) (进度：1%)
- 德语(de) (进度：1%)
- 印尼语(id) (进度：1%)
- 意大利语(it) (进度：10%)
- 韩语(ko) (进度：11%)
- 挪威语(nb-no) (进度：1%)
- 波斯语(fa-ir) (进度：6%)
- 葡萄牙语(pt-br) (进度：29%)
- 锡兰语(si) (进度：1%)
- 西班牙语(es) (进度：37%)
- 土耳其语(tr) (进度：5%)

我们要感谢所有翻译或审核文档的贡献者。

请帮助在您的本地用户组推广此项目，我们总是需要更多的志愿者。

#### FreeBSD 手册工作组

联系方式：Sergio Carlavilla [carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)

已更新第 1 到 6 章。第 7 章正在进行中。

FreeBSD 网站翻新-WebApps 工作组

联系人：Sergio Carlavilla carlavilla@FreeBSD.org

工作组负责创建新的 FreeBSD 文档门户网站和重新设计 FreeBSD 主要网站及其组件。FreeBSD 开发人员可以关注并加入 FreeBSD Slack 频道 #wg-www21 的工作组。该工作将分为四个阶段：

- 重新设计文档门户网站

创建一个新的设计，具有响应式和全局搜索功能。（已完成）

- 重新设计 Web 上的手册页面

使用 mandoc 生成 HTML 页面的脚本。（已完成）公共实例在 https://man-dev.FreeBSD.org上

- 重新设计 Web 上的 Ports 页面

Ports 脚本用于创建应用程序门户网站。（正在进行中）

- 重新设计 FreeBSD 主要网站

新的设计，响应式和暗色主题。（正在进行中）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 俄语文档项目

链接：

FAQ 网址: https://docs.freebsd.org/ru/books/faq/

网址: https://www.freebsd.org/ru/

联系人：Andrey Zakhvatov [andrey.zakhvatov@gmail.com](mailto:andrey.zakhvatov@gmail.com)

FreeBSD 俄语文档项目的目标是提供最新的 FreeBSD 文档（FAQ，Handbook，Web）的俄语翻译。为了让说俄语的人们使用高质量的官方技术材料，并增加这个操作系统在全球的接受度。我们希望这项活动能够得到俄语社区的支持，并带来更多的翻译材料。

FAQ 的翻译已经更新并与最新的原版同步。网页更新方面也有一些微小的进展。

如果你想帮助翻译，可以查看官方的翻译指南。我们会感激你帮助翻译以下材料：

- 网页（简单的）
- Handbook 章节（目前只有 X11 部分正在进行中）
- 文章

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Ports

影响到 Ports 的更改，无论是影响整个结构的全面变化，还是单个 port 本身的变化。

### Freshports: SQL 注入攻击和求助请求

链接：

FreshPorts 网址: freshports.org

FreshPorts 博客网址: https://news.freshports.org/

联系人：Dan Langille dvl@FreeBSD.org

FreshPorts 和 FreshSource 已经报道了 FreeBSD 提交记录 20 年了。它们涵盖了所有提交，而不仅是 port。

FreshPorts 跟踪提交并从 portMakefiles 中提取数据，以创建对 port 维护者和 port 用户都有用的信息数据库。

例如，https://www.freshports.org/security/acme.sh/ 显示了 security/acme.shport 的历史记录，从 2017 年 5 月的创建到现在。还提供了依赖关系、风格、配置选项和可用包等。所有这些对 port 的用户和开发人员都很有用。

**SQL 注入攻击**

三月份，发现了一次 SQL 注入攻击，网站已被修补。通知已通过我们的 Twitter 账户、我们的状态页面以及网站每个页面顶部的通知发送。立即关闭了攻击向量\[译者注：攻击向量（attack vector）是指攻击者利用安全漏洞或弱点，进入目标系统或者攻击目标的途径和手段】，并很快进行了修补。网站上还添加了额外的预防性补丁。我们所知道的所有问题都已经修复。用户已被通知并建议更改密码。

详情请见：

- https://news.freshports.org/2023/03/24/sql-inejection-issues-fixed/
- https://news.freshports.org/2023/03/24/freshsource-code-fixes/

需要帮助

FreshPorts 已经成立超过 22 年了。最后必须有其他人将其接过来。FreshPorts 有几个方面：

- FreeBSD 管理员（更新操作系统和软件包）
- 前端代码（网站 - 大多数是 PHP）
- 后端代码（提交处理 - Perl、Python、shell）
- 数据库设计（PostgreSQL）。

与应用程序和操作系统相比，数据库的更改不经常发生，并且需要很少的维护。网站几乎自己运行。偶尔会出现对 FreeBSDport 基础架构的更改会破坏某些内容或需要进行修改，但很少有紧急情况需要修复。这不是一个巨大的时间承诺。有很多东西需要学习。虽然 FreshPorts 不是一个复杂的应用程序，但也不是微不足道的。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### DRM 驱动程序（即 GPU 驱动程序）

链接：

GitHub 上的 Git 存储库网址：https://github.com/freebsd/drm-kmod

联系人：Emmanuel Vadot manu@FreeBSD.org

联系人：Jean-Sébastien Pédron dumbbell@FreeBSD.org

联系人：图形团队 freebsd-x11@FreeBSD.org

GPU 由 DRM 驱动程序驱动。它们是专门为 Linux 开发的，使用宽松的许可证。我们的使命是将这些驱动程序移植到 FreeBSD，以确保现代 GPU 得到充分支持。

我们很长时间没有发布报告来分享我们的进展。因此，本状态报告条目将涵盖不止上一季度的情况。

**更新到了 Linux 5.15 LTS 和 Linux 5.16**

截至本状态报告，graphics/drm-kmod 元 port 仍在 FreeBSD 13.1 及更高版本上安装来自 Linux 5.10（发布于 2020 年 12 月 13 日）的 DRM 驱动程序。该驱动程序版本不支持最近的 GPU，特别是英特尔第 12 代 Alder Lake。在过去的几个月中，我们致力于更新 DRM 驱动程序，以支持更现代的 AMD 和 Intel GPU。

drm-kmod Git 存储库主分支首先更新到 Linux 5.15（于 2021 年 10 月 31 日发布）。这是 Linux 中的 LTS 分支，我们想利用这个机会。因此，在那个时候，我们走了两条路：

- 创建了一个 5.15-lts 分支，用于将所有错误修复从 Linux 5.15.x 补丁版本中回溯。这项工作现在在 drm-515-kmodport 中可用。
- 继续从随后的 Linux 版本进行移植工作。主分支现在位于 Linux 5.16（于 2022 年 1 月 9 日发布）。

来自 Linux 5.15 LTS 的英特尔驱动程序支持第 12 代 GPU（Alder Lake）。它似乎在 FreeBSD 上运行良好，但我们迄今为止只进行了轻微的测试。我们仍然需要更多的测试，这就是为什么 graphics/drm-kmod 仍然安装 graphics/drm-510-kmod 而不是 graphics/drm-515-kmod 的原因。最后，FreeBSD 应该可以在这一代 GPU 和几款新的 AMD GPU 上运行桌面，尽管在实际测试和使用中肯定会出现问题。

在此过程中，我们将固件更新为 linux-firmware 20230210。

**Linux 5.17 和未来的工作**

Linux 5.17 中的 DRM 驱动程序（发布于 2022 年 3 月 20 日）已经被移植，但这项工作仍然停留在自己的分支中。

有几个问题阻碍了进一步的测试和合并到主分支中：

- 我们当前与 vt（4）的集成，即控制台/终端驱动程序，与基于 Linux 的 fbdev KPI 的 DRM 驱动程序的期望相去甚远。在英特尔和 AMD 驱动程序中都发生了变化，这意味着 vt（4）会在更新到 5.17 版本时出现问题。
- 初始的 Linux 5.17 版本不包含被反向移植到 Linux 5.15 LTS 的修复程序。它在先前提到的英特尔第 12 代 GPU 上似乎非常不稳定。

为了解决我们的 vt（4）集成层的问题，我们开始编写一个新的 vt 后端，专门使用 DRM 驱动程序公开的 fbdev 回调。该后端将随着 DRM 驱动程序而提供，而不是随 FreeBSD 内核提供，以使得随着驱动程序的发展更易于维护。这仍然是一项正在进行中的工作，特别是锁定的正确使用比较棘手。

关于 5.17 更新中对英特尔第 12 代支持不佳的问题，Linux 5.17.x 补丁程序中反向移植的错误修复可能不会作为此项工作的一部分进行移植。相反，我们将专注于 Linux 5.18（发布于 2022 年 5 月 22 日）和随后的版本。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FreeBSD 上的 KDE

链接：

KDE FreeBSD 网址：https://freebsd.kde.org/

KDE 社区 FreeBSD 网址：https://community.kde.org/FreeBSD

联系人：Adriaan de Groot [kde@FreeBSD.org](mailto:kde@FreeBSD.org)

KDE on FreeBSD 项目为 FreeBSD 的 port 打包了 CMake、Qt 和 KDE 社区的软件。该软件包括一个完整的桌面环境 KDE Plasma（适用于 X11 和 Wayland）以及数百个可在任何 FreeBSD 机器上使用的应用程序。

KDE 团队（kde@）是 desktop@ 和 x11@ 的一部分，构建软件堆栈，使 FreeBSD 美观易用，成为日常使用的基于图形界面的桌面机器。以下说明主要说明了 KDE 的 port，但也包括整个桌面堆栈的重要内容。

**基础设施**

- Qt5 port 更新到了 KDE patch collection 5.15.8 发行版。
- Qt6 port - KDE 尚未使用这些 port，但有许多 port 可以使用 Qt6 并具有 Qt6 flavor，已更新到了 6.4.2 版本。新增了 Qt6 发行版的 WebEngine 的 Python 绑定。
- Cmake port 已更新到 3.25.1 版本，FreeBSD 软件包的 CPack 生成器已修复。
- graphics/poppler port——许多 PDF 阅读器使用 - 已更新到 23.01 版本。
- sysutils/bsdisks port——用作应用程序的 shim，这些应用程序需要 Linux udisk，这意味着大多数桌面环境——已更新到 0.29 版本。

**KDE 软件堆栈**

KDE Gear 每季度发布一次，KDE Plasma 每月更新一次，KDE Framework 每月都有新版本发布。这些（大型）更新会在上游发布后不久到达，不会单独列出。

- KDE Framework 更新到 5.104 版本。
- KDE Gear 更新到 22.12.3 版本。
- KDE Plasma Desktop 更新到了 5.27 版本。由于支持堆栈中的未解决问题和 KDE Plasma 早期版本中的误置补丁，这是一个迟来的更新。感谢 arrowd@ 和 Serenity Cybersecurity, LLC 排解了这个问题。
- 新的 devel/ktextaddons port 已添加到 ports 中。这是 KDE PIM 套件的一部分，并计划在未来某个版本中成为新的 KDE Framework。

**相关的软件包**

- 音频播放器 amarok 是 KDE 最受欢迎的播放器之一，但已被标记为 ports 中弃用，它不再得到上游的维护。
- 星空模拟软件 kstars 更新至 3.6.3 版本。
- git 的图形用户界面 gitqlient 更新至 1.6.1 版本，并支持新的 git 命令。
- 二进制文件的十六进制查看器和编辑器 okteta 更新至 0.26.10 版本。
- 带有 Qt 支持的 C++ 协程库 qcoro 更新至 0.8.0 版本。
- 绘画和图形工作应用 krita 更新至 5.1.5 版本。
- 图形可视化库 quickqanava 发布了一个真正的版本，并在 ports 中进行了更新。
- IRC 客户端 kvirc 被更新至最新的提交版本。虽然没有真正的发布版本，但有一些 bug 修复。
- 视频和音频播放器 haruna 更新至 0.10.3 版本。
- 一款 Matrix 客户端 neochat 更新以追踪新版本的 net-im/libquotient。由于与较旧的 FreeBSD 版本的兼容性问题，KDE-FreeBSD 团队宣布 FreeBSD 12 发行版“已被有效地停止支持”。
- Rocket Chat 客户端 ruqola 更新至 1.9.1 版本。
- 双因素认证支持应用 keysmith 更新至 23.01.0 版本。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### FSX

链接：

GitHub 网址: https://github.com/asomers/fsx-rs

FreshPorts 网址: https://www.freshports.org/devel/fsx/

联系人：Alan Somers [asomers@freebsd.org](mailto:asomers@freebsd.org)

FSX (File System eXerciser) 工具最初在九十年代由苹果公司开发，一直作为 FreeBSD 的一部分存在，自 5.0 版本以来就一直存在。该工具通过一系列随机生成的操作对文件系统进行压力测试，在每次读取后验证文件数据。然而，它从未作为操作系统的一部分安装；它只存在于源代码中。这使得它在 CI 管道中使用起来很困难。它还有其他一些限制。

因此，在本季度，我使用 Rust 对整个工具进行了重写。新版本与原版本完全兼容，只要种子值相同。然而，未来版本将打破向后兼容性，以添加新功能，如 fspacectl 和 copy_file_range。新版本可以在 ports 中找到，我会逐步移除原版本。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 在 FreeBSD 上的 GCC

链接：

GCC 项目网址: https://gcc.gnu.org

GCC 11 发行系列网址: https://gcc.gnu.org/gcc-11/

GCC 12 发行系列网址: https://gcc.gnu.org/gcc-12/

联系人：Lorenzo Salvadore [salvadore@FreeBSD.org](mailto:salvadore@FreeBSD.org)

联系人：Gerald Pfeifer [gerald@pfeifer.com](mailto:gerald@pfeifer.com)

本季度的主要消息是从 ports 中清除旧的 GCC 版本：这将允许更有效地处理错误。

**废弃旧的 GCC port**

ports 仍然包含多个与旧且不受支持的 GCC 版本相关的 port。它们通常作为一些旧 port 的依赖项，最好的方法是将其更新为使用受支持的 GCC 版本或废弃。已创建错误报告以跟踪此问题，并已经开始了解决该问题的工作。感谢所有贡献者的帮助。

**废弃 USE_GCC=X+**

Gerald 曾长期维护 FreeBSD 上的 GCC port，最近仍在通过帮助简化 ports 中的 GCC 基础架构来为 GCC 的维护做出贡献，例如通过删除处理旧不受支持的 GCC 版本的特殊情况。

本季度他最重要的更改可能是删除对 `USE_GCC=X+` 结构的支持：任何依赖于 GCC 的 port 都应该设置 `USE_GCC=yes`，如果 `GCC_DEFAULT` 可用的话；如果不是，则应该要求特定版本（例如 `USE_GCC=11`）；它不能再要求最小版本（例如 `USE_GCC=11+`）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### Valgrind——为 Valgrind 3.21 做准备

链接：

Valgrind 官方网站网址: https://www.valgrind.org/

Valgrind 新闻页面网址: https://www.valgrind.org/docs/manual/dist.news.html

联系人：Paul Floyd [pjfloyd@wanadoo.fr](mailto:pjfloyd@wanadoo.fr)

devel/valgrind-devel port 于 2023-02-20 提交了一个中间更新，其中包含了即将发布的 Valgrind 3.21 正式版本的大部分内容，正式版本将会在本状态报告之后不久发布。

vgdb 接口得到了一个不错的改进。现在更容易看到哪些内存位被初始化和哪些没有。Helgrind 执行的线程检查也进行了一些修复。

特别是对于 FreeBSD，地址空间限制已经被提高到与 Linux 和 Solaris 上的 amd64 相同。之前是 32G 字节，现在是 128G 字节。`kern.proc.pathname.PID` sysctl(3) 已经修复，使其返回 guest exe 的路径而不是 Valgrind 主机的路径。同时，我还修复了一些 `_umtx_op` 的误报，并以与 `kern.proc.pathname.PID` 相似的方式纠正了 auxv AT_EXECPATH。还添加了 sctp_generic_sendmsg(2) 和 sctp_generic_recvmsg(2) 的系统调用包装器。

Valgrind 的 port 版本中尚不可用，有一个用于 rfork(2) 的解决方法。之前，由于不支持，它会导致 Valgrind 中止。现在它会以优雅的方式失败并设置 EINVAL 或 ENOSYS。这个系统调用的主要用途是在 posix_spawn(3) 中，它会回退到使用 vfork(2)。

mknodat(2) 系统调用包装器在 i386 上被错误地实现了，现在已经修复。

所有对齐分配函数都进行了重新设计，使其的行为更像 Valgrind 的构建平台，而不是像 Linux glibc。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 第三方项目

许多项目基于 FreeBSD 或将 FreeBSD 组件合并到其项目中。由于这些项目可能会引起更广泛的 FreeBSD 社区的兴趣，因此我们有时会在我们的季度报告中包括这些项目提交的简要更新。FreeBSD 项目不对这些提交中的任何声明的准确性或真实性做出陈述。

#### PkgBase.live

链接:

网站(archive.org) 网址: https://web.archive.org/web/20221220222828/https://alpha.pkgbase.live/

网站源代码网址: https://codeberg.org/pkgbase/website

联系人: Mina Galić [freebsd@igalic.co](mailto:freebsd@igalic.co)

PkgBase.live 是一个非官方的 FreeBSD PkgBase 项目存储库。作为一个服务，PkgBase.live 的灵感来自于 https://up.bsd.lv/，为 STABLE 和 CURRENT 分支提供 freebsd-update(8)。

PkgBase 的硬件由 FreeBSD 社区的一位成员慷慨赞助。然而，随着生活和项目的变化，他们不得不废弃硬件，给了我三个月的通知时间。在那段时间里，由于最近搬到了另一个国家，我的生活相当动荡，所以我没有能够找到替代品。

目前，PkgBase.live 已经关闭。

该网站及其 [How Did She Do it？！](https://codeberg.org/pkgbase/website/src/branch/main/howto/howdo.md)仍然在 [Git](https://codeberg.org/pkgbase/website) 中提供。我强烈鼓励模仿。

我也会很乐意接受新的硬件赞助商！

请注意，我已经联系了 FreeBSD 项目，他们正在将 PkgBase 集成到发布工程中。然而，他们还没有准备好，也不能“简单地”接管 PkgBase.live，因为它使用完全不同的过程。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 容器和 FreeBSD：Pot、Potluck 和 Potman

链接： Pot 在 GitHub 上的组织网址：https://github.com/bsdpot

联系人：Luca Pizzamiglio（Pot）[pizzamig@freebsd.org](mailto:pizzamig@freebsd.org)

联系人：Bretton Vine（Potluck）[bv@honeyguide.eu](mailto:bv@honeyguide.eu)

联系人：Michael Gmelin（Potman）[grembo@freebsd.org](mailto:grembo@freebsd.org)

Pot 是一个 jail 管理工具，也支持通过 Nomad 进行编排。

在上个季度，Pot 收到了一些次要修复，但尚未发布新版本。

Potluck 旨在成为 FreeBSD 和 pot 的 Dockerhub，提供 pot 风味和完整的容器镜像，可用于与 pot 配合使用，而在许多情况下还可用于 Nomad。

所有 Potluck 镜像都已重新构建以包含最新的 FreeBSD 安全公告，新增了一个 Smokeping 网络延迟监视镜像，对 Jitsi 镜像进行了大量的工作，但不幸的是似乎仍存在一些可靠性问题。

此外，有两篇新的博客文章介绍使用 Potluck 镜像的简单方法，一篇解释如何使用 Minio 作为对象存储和 Prometheus 进行监视来设置 Nextcloud，一篇展示如何使用 OpenLDAP 运行自己的 Matrix Synapse 服务器以进行访问管理。

像往常一样，欢迎反馈和补丁。

## FreeBSD 2022 年第三季度 季度状况报告

> 原文地址 [https://www.freebsd.org/status/report-2022-07-2022-09/](https://www.freebsd.org/status/report-2022-07-2022-09/)

FreeBSD 季度状态报告—— 2022 年第三季度

这里是 2022 年的第三季度报告，包括 24 份报告。这比上一季度略少。

我注意到，在过去，我们的季度报告要多得多：经常超过 30 份，有时甚至超过 40 份。因此，我想鼓励你们所有的人提交报告：报告对于分享你的工作、寻找帮助、让更多的人审视你的变化、让更多的人了解你的工作是非常有用的。有更多的人审查你的修改，让更多的人测试你的软件，让你在需要的时候接触到更多的人。当你需要向所有的 FreeBSD 社区讲述一些事情时，你可以接触到更多的读者。告知所有的 FreeBSD 社区以及其他许多情况。请不要害羞，也不要担心您的母语不是英语，或者您不精通 AsciiDoc 的语法：季刊团队将很乐意帮助您解决任何需要。

另一方面，如果你真的没有什么可报告的，那么也许你想加入下面描述的一个有趣的项目，或者你会从其中的一个项目中得到启发，去做一个新的项目。也许你会受到其中一个项目的启发，去做一些新的事情，从而在未来有一些报道。

我们祝愿大家有一个愉快的阅读体验。

Lorenzo Salvadore，代表状态报告小组。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

本报告的渲染版可在此查阅：

[https://www.freebsd.org/status/report-2022-07-2022-09/](https://www.freebsd.org/status/report-2022-07-2022-09/)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

目录

- FreeBSD 团队报告
  - FreeBSD 核心团队
  - FreeBSD 基金会
  - FreeBSD 发布工程团队
  - 集群管理团队
  - 持续集成
  - ports
- 项目
  - OpenStack 与 FreeBSD
  - 作为一级云计算平台的 FreeBSD
- 用户空间
  - bhyve 调试服务器的改进
  - 重写 pjdfstest
  - 正在进行的 LLDB 多进程调试支持工作
  - DTrace：指令级动态跟踪
- 内核
  - ENA FreeBSD 驱动程序更新
  - wtap(4) 增强
  - 英特尔无线走向 11ac
  - 更多的无线更新
  - 使用日志式软更新在文件系统上启用快照
- 架构
  - FreeBSD/Firecracker
- 文档
  - 文档工程团队
- ports
  - Calendar-data: 增加了许可证
  - KDE 与 FreeBSD
  - GCC 有新的维护者，GCC 12.2 和更多
  - sysutils/lsof 重大升级
- 第三方项目
  - 容器和 FreeBSD：Pot, Potluck 和 Potman

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### FreeBSD 团队报告

来自各个官方和半官方团队的条目，可以在[管理](https://www.freebsd.org/administration/)页面找到。

### FreeBSD 核心团队

联系：FreeBSD 核心团队 [core@FreeBSD.org](mailto:core@FreeBSD.org)

FreeBSD 核心团队是 FreeBSD 的管理机构。

#### 已完成的项目

**新的核心团队秘书**

核心小组的所有成员公开表示感谢 Muhammad Moinur Rahman (bofh) 在过去两年中担任核心小组的秘书。

核心小组批准 Sergio Carlavilla（carlavilla）为新的核心小组秘书。

**处理 GDPR 删除请求的程序**

在基金会律师的帮助下，核心小组已经审查了处理 GDPR 删除请求的程序。该文件目前正在撰写中，将会在完成后公布。

**新的隐私政策**

核心团队正在与 FreeBSD 基金会紧密合作，以更新隐私政策，使之与当前的法律和类似网站的做法保持一致，例如我们的网站。

**Bruce Evans 纪念牌**

核心团队经投票一致同意为 Bruce Evans 设立纪念牌，提及他是 FreeBSD 的联合创始人。

**EuroBSDCon 核心团队办公时间**

9 月 1 6 日星期五，新的核心团队在 EuroBSDcon 2022 开发者峰会上发表了演讲。核心团队做了自我介绍，并谈了一下他们这一届的计划。与会人员对细节进行了讨论、问答和建议。

#### Commit 权限

核心小组批准了重启 Konrad Witaszczyk（def@）的源代码提交权限。现在 Konrad 在剑桥大学工作，负责开发 CheriBSD。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### FreeBSD 基金会

链接：

FreeBSD 基金会的网址: https://www.FreeBSDFoundation.org

技术路线图网址: https://FreeBSDFoundation.org/blog/technology-roadmap/

捐赠网址: https://www.FreeBSDFoundation.org/donate/

基金会合作伙伴计划网址: https://www.FreeBSDFoundation.org/

FreeBSD——基金会-合作伙伴关系-计划：[https://www.FreeBSDFoundation.org/FreeBSD-foundation-partnership-program](https://www.freebsdfoundation.org/FreeBSD-foundation-partnership-program)

FreeBSD 杂志网址: https://www.FreeBSDFoundation.org/journal/

基金会新闻和活动网址: https://www.FreeBSDFoundation.org/

联系：Deb Goodkin [deb@FreeBSDFoundation.org](mailto:deb@FreeBSDFoundation.org)

FreeBSD 基金会是符合 501(c)(3) 的非盈利组织，致力于支持和推广 FreeBSD 项目和全球社区。来自个人和企业的捐款被用来资助和管理软件开发项目、会议和开发者峰会。我们还为 FreeBSD 贡献者提供旅行补助，购买和支持硬件以改善和维护 FreeBSD 基础设施，并提供资源以改善安全、质量保证和发布工程工作。我们出版营销材料来推广、教育和宣传 FreeBSD 项目，促进商业供应商和 FreeBSD 开发者之间的合作，最后，在执行合同、许可协议和其他需要一个公认的法律实体的法律安排时代表 FreeBSD 项目。

#### 筹款工作

首先，我想向所有为我们的工作提供资金捐助的人表示衷心的感谢。我们的资金 100% 来自于你们的捐款，所以每一笔捐款都可以帮助我们继续在许多方面支持 FreeBSD，包括在这份状况报告中资助和发表的一些工作。

我们主要在五个方面支持 FreeBSD：软件开发是我们资助的最大领域，通过员工开发人员和承包商来实现新的功能，支持一级平台，审查补丁，并修复问题。您可以在这份报告中了解到我们在操作系统改进方面所做的一些工作。宣传 FreeBSD 是我们支持的另一个领域，通过会议、网上和现场的演讲，以及教程和操作指南来传播 FreeBSD 的信息。我们购买并支持用于支持该项目工作的 FreeBSD 基础设施的硬件。基金会组织的虚拟和现场活动帮助联系和吸引社区成员分享他们的知识并进行项目合作。最后，我们在需要时为项目提供法律支持并保护 FreeBSD 的商标。

我们今年的目标是为 200 万美元左右的支出预算筹集至少 140 万美元。当我们进入 2022 年的最后一个季度时，我们的捐款总额为 167,348 美元，所以我们仍然需要您的帮助。如果你今年还没有捐款，请考虑 https://freebsdfoundation.org/donate/。我们还有一个针对大型商业捐助者的合作伙伴计划。你可以在https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/ 找到更多信息。

#### 系统改进

在 2022 年的第三季度，有 300 个 src，36 个 port，和 13 个 doc 树的提交将 FreeBSD 基金会列为赞助商。其中一些工作有专门的报告条目。

- 作为一级云计算平台的 FreeBSD
- 对英特尔 11ac 的无线支持
- LLDB 多进程调试支持
- FreeBSD 上的 OpenStack
- 使用日志式软更新的文件系统上的快照

其他赞助的工作是很难简明扼要地总结的。它从复杂的新功能到跨越 src 源代码的各种 bug 修复都不相同。以下是一个小样本，可以让大家了解上一季度的工作。

- 240afd8 makefs: 增加对 ZFS 的支持

这允许人们采用一个阶段性的目录树，并创建一个由 ZFS 池组成的文件，其中有一个或多个数据集，包含目录树的内容。这对于创建虚拟机镜像非常有用，而不需要使用内核来创建池；“zpool create”需要 root 权限，目前在 jail 中禁用。makefs -t zfs 还通过使用固定的种子来生成伪随机数，提供可重复的镜像，用于生成 GUID 和加盐哈希。

- 36f1526 在 arm64 上增加实验性的 16k 页面支持

在 arm64 上添加了初始的 16k 页面支持。它被认为是实验性的，不能保证与用户空间或以当前 4k 页大小构建的内核模块兼容。测试表明，在内核工作负载中取得了良好的效果，这些工作负载包括分配和释放大量的内存，因为在最好的情况下，只需要调用虚拟机子系统的四分之一。

- 1424f65 vm_pager: 删除默认的页表

它现在没有被使用。保留了 OBJ_DEFAULT 标识符，但将其作为　 OBJT_SWAP 的别名，以方便树外代码的使用。

- a889a65 eventtimer：修复定时器重载代码中的几个 race

在 handleevents() 中，在获取下一个事件的时间之前锁定定时器状态。一个并发的 callout_cc_add() 调用可能正在改变下一个偶数时间，而竞赛可能导致 handleevents() 编程一个过时的时间。导致 callout 运行得更晚（不受限制的时间，最多到闲置的硬时钟周期为 1s）比要求的时间晚。

**Bhyve 问题支持**

基金会与 John Baldwin 签订了合同，以便在出现问题时为 Bhyve 奉献时间，特别是安全问题。以下是他在该合同中对 2022q3 年的工作总结：

- bb31aee bhyve virtio-scsi: 避免对访客请求的越界访问。
- 62806a7 bhyve virtio-scsi: 整理警告和调试打印文件。
- 7afe342 bhyve e1000: 净化传输环索引。
- c94f30e bhyve: 验证用于映射穿透式 BAR 的主机 PA。
- 16bedf5 pci: 添加辅助程序以遍历设备的 BAR。
- baf753c bhyve: 支持其他命名直通设备的方案。
- fa46f37 bhyve e1000: 跳过有小头的数据包。
- e7439f6 bhyve xhci: 在初始化端点时缓存 MaxPStreams 的值。

**RISC-V 的改进**

在本季度末，基金会与 Mitchell Horne 签订了合同，增加和改进对 RISC-V 硬件的支持。Mitchell 还将进行一般的维护工作，如修复错误，处理报告，为新的代码修改提供审查，以及改善源代码的可读性和文档。

#### 持续集成和质量保障

基金会提供了一名全职工作人员，并资助了一些项目，以改善持续集成、自动测试以及 FreeBSD 项目的整体质量保障工作。您可以在专门的条目中阅读本季度的 CI 活动。

#### FreeBSD 推广与教育

我们的大部分工作是致力于项目的宣传。这可能涉及到突出有趣的 FreeBSD 工作，制作文献和视频教程，参加活动，或做演讲。我们制作文献的目的是教给人们 FreeBSD 的基本知识，并帮助他们在采用或贡献的道路上更加容易。除了参加活动和发表演讲之外，我们还鼓励和帮助社区成员举办他们自己的 FreeBSD 活动，发表演讲，或者担任 FreeBSD 的工作人员。

FreeBSD 基金会在全球范围内赞助了许多会议、活动和峰会。这些活动可以是与 BSD 相关的，也可以是开源的，或者是面向未被代表的群体的技术活动。我们支持以 FreeBSD 为中心的活动，以帮助提供一个分享知识的场所，在项目上一起工作，并促进开发者和商业用户之间的合作。这都有助于提供一个健康的生态系统。我们支持非 FreeBSD 的活动，以促进和提高对 FreeBSD 的认识，增加 FreeBSD 在不同应用中的使用，并招募更多的贡献者加入该计划。我们将继续参加个人和虚拟的活动，并计划 11 月的供应商峰会。除了参加和策划虚拟活动之外，我们还在不断地开展新的培训活动，并更新我们的指南选择，以方便让更多的人尝试使用 FreeBSD。

请看我们上一季度所做的一些宣传和教育工作：

- 在 7 月 28 日至 30 日于加州洛杉矶举行的 Scale 19x 会议上举办了一个 FreeBSD 研讨会并设立了一个展位。您可以在 SCALE19X 会议报告中了解更多关于我们的参与情况。
- 赞助并出席 7 月 30-31 日在台湾举行的 COSCUP 会议
- 参加了 EuroBSDCon 开发者峰会，赞助并出席了 9 月 15-18 日在奥地利维也纳举行的 EuroBSDcon 2022。
- 赞助并出席了 2022 年 9 月 29-30 日在洛基山举行的“计算机领域女性庆典”。可以在这里找到 Deb 的演讲的幻灯片。
- 发布 FreeBSD 基金会 2022 年夏季更新
- 继续以管理员和导师的身份参与 Google Summer of Code。在这里可以看到对一些 Google Summer of Code 学生的采访。
- 介绍了一个新的 FreeBSD 资源页面，可以按主题类型、内容类型和难度进行搜索。
- 新的博客文章：
  - 特邀文章：科研中的 FreeBSD
  - 为 2022 年及以后的 FreeBSD 做宣传
  - 八月基金会筹款更新
  - 在 Linux 和 FreeBSD 之间共享双许可证的驱动程序
- 新的和更新的操作指南和快速指南：
  - FreeBSD 快速指南: 在 FreeBSD 上播放视频
  - FreeBSD 上的二进制包管理

我们通过出版专业的 FreeBSD 杂志来帮助大家了解 FreeBSD。正如我们之前提到的，FreeBSD 杂志现在是一份免费出版物。了解更多信息并访问最新的期刊：https://www.FreeBSDfoundation.org/journal/。

你可以在 https://www.FreeBSDfoundation.org/news-and-events/ 找到更多关于我们参加的活动和即将举行的活动。

#### 法律/FreeBSD 知识产权

基金会拥有 FreeBSD 的商标，保护这些商标是我们的责任。我们还为核心团队提供法律支持，以调查出现的问题。

前往 https://www.FreeBSDFoundation.org 了解更多关于我们如何支持 FreeBSD 以及我们如何帮助您的信息!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### FreeBSD 发布工程团队

链接：

FreeBSD 12.4-RELEASE 计划表链接: https://www.freebsd.org/releases/12.4R/schedule/

FreeBSD 13.2-RELEASE 计划表链接: https://www.freebsd.org/releases/13.2R/schedule/

FreeBSD 14.0-RELEASE 计划表链接: https://www.freebsd.org/releases/14.0R/schedule/

FreeBSD development 计划表链接: https://download.freebsd.org/snapshots/ISO-IMAGES/

联系：FreeBSD 发布工程团队, [re@FreeBSD.org](mailto:re@FreeBSD.org)

FreeBSD 发布工程团队负责制定和发布 FreeBSD 官方项目版本的发布时间表，宣布代码冻结并维护相应的分支，以及其他一些工作。

在 2022 年的第三季度，发布工程小组继续为 main、 stable/13 和 stable/12 分支提供每周的开发快照构建。

此外，即将到来的 12.4、13.2 和 14.0 发布周期的时间表也在项目网站上公布。

赞助商：Rubicon Communications, LLC (“Netgate”) 赞助商：FreeBSD 基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 集群管理团队

链接：

集群管理团队成员链接： https://www.freebsd.org/administration/#t-clusteradm

联系：集群管理团队 [clusteradm@FreeBSD.org](mailto:clusteradm@FreeBSD.org)

FreeBSD 集群管理团队的成员负责管理该项目所依赖的机器，以同步其分布式工作和通信。在本季度，该团队进行了以下工作：

- 为 CI 系统增加了额外的存储空间。这将有助于存储更多的工件。
- 在所有官方镜像中部署了 VuXML。它加快了 pkg 的审计功能。
- 一个新的（和额外的）监控系统已经到位。
- 一些旧的和有问题的机器已经退役。
- 将几个服务移到了较新的硬件上。
- 定期进行集群范围内的软件升级
- 定期支持 FreeBSD.org 用户账户
- 对所有物理主机和镜像机进行定期的磁盘和部件支持（和更换）。

正在进行的工作。

- git infra: 增加 `--filter` 支持。
- 与 PowerPC 团队合作，改进软件包构建者、通用和参考机器。
- 在我们的主站点进行站点审计：清点备件和其他占用我们机柜空间的杂物。
- 与 Juniper 讨论为我们的主站点捐赠新的交换机的问题。
- 计划在我们的主站点进行大规模的网络升级。
- 集群更新（更多的扩展项目）。截至 2022-09-30，大多数集群机器都在运行 FreeBSD 13-STABLE 或 14-CURRENT。只有少数机器还在使用 FreeBSD 12-STABLE。

我们正在欧洲寻找一个额外的全镜像站点（五台服务器）。请看适合我们需求的通用镜像布局。我们也欢迎提供额外的单服务器镜像，特别是在欧洲。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 持续集成

链接：

FreeBSD Jenkins Instance 网址: https://ci.FreeBSD.org

FreeBSD CI artifact archive 网址: https://artifact.ci.FreeBSD.org

FreeBSD Jenkins wiki 网址: https://wiki.freebsd.org/Jenkins

Hosted CI wiki 网址: https://wiki.freebsd.org/HostedCI

3rd Party Software CI 网址: https://wiki.freebsd.org/3rdPartySoftwareCI

Tickets related to freebsd-testing@ 网址: https://preview.tiny网址.com/y9maauwg

FreeBSD CI Repository 网址: https://github.com/freebsd/freebsd-ci

dev-ci Mailing List 网址: https://lists.freebsd.org/subscription/dev-ci

联系：Jenkins Admin [jenkins-admin@FreeBSD.org](mailto:jenkins-admin@FreeBSD.org)

联系：Li-Wen Hsu [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

联系：freebsd-testing Mailing List

联系：IRC #freebsd-ci channel on EFNet

FreeBSD CI 团队负责维护 FreeBSD 项目的持续集成系统。CI 系统检查提交的修改是否能够成功构建，然后对新构建的结果进行各种测试和分析。这些构建的工件被归档到工件服务器中，以备进一步测试和调试的需要。CI 团队成员检查失败的构建和不稳定的测试，并与该领域的专家合作，修复代码或调整测试基础设施。

在 2022 年第三季度，我们继续与项目中的贡献者和开发者合作，以满足他们的测试需求，同时也继续与外部项目和公司合作，改进他们的产品和 FreeBSD。

重要的已完成任务:

- 扩大工件存储空间，以增加更多类型的工件和更长的保留期。
- 在 EuroBSDcon 2022 开发者峰会上展示测试/CI 状态更新
- 增加 main-powerpc-images 和 main-powerpcspe-images

正在进行的工作任务：

- 设计并实施预提交的 CI 构建和测试（以支持工作流工作组）
- 设计和实现使用 CI 集群来构建发布工件，就像发布工程那样
- 测试和合并 FreeBSD-ci repo 中的拉动请求
- 为贡献者和开发者简化 CI/测试环境的设置
- 设置 CI 阶段环境，并将实验性工作放在上面
- 整理 freebsd-ci 代码库中的脚本，为合并到 src 代码库做准备
- 更新 wiki 上的文档

已有或等待执行的任务：

- 收集和整理 CI 任务和想法
- 为运行测试的虚拟客体设置公共网络接入
- 实现使用裸机硬件来运行测试套件
- 添加 drm port，并针对 -CURRENT 编译测试
- 计划运行 ztest 测试
- 增加更多外部工具链相关的工作
- 提 - 高硬件实验室的成熟度，增加更多测试用的硬件
- 帮助更多的软件在其 CI 管道中获得 FreeBSD 支持 (Wiki 页面: 3rdPartySoftwareCI, HostedCI)
- 与托管 CI 供应商合作以获得更好的 FreeBSD 支持

请参阅 freebsd-testing@ 相关信息以了解更多的 WIP 信息，不要犹豫，加入我们一起努力吧!

赞助商：FreeBSD 基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Ports

链接：

About FreeBSD Ports 网址:https://www.FreeBSD.org/ports/

Contributing to Ports 网址: https://docs.freebsd.org/en/articles/contributing/#ports-contributing

FreeBSD Ports Monitoring 网址: http://portsmon.freebsd.org/

Ports Management Team 网址: https://www.freebsd.org/portmgr/

Ports Tarball 网址: http://ftp.freebsd.org/pub/FreeBSD/ports/ports/

联系：René Ladan [portmgr-secretary@FreeBSD.org](mailto:portmgr-secretary@FreeBSD.org)

联系：FreeBSD Ports Management Team [portmgr@FreeBSD.org](mailto:portmgr@FreeBSD.org)

ports 管理团队负责监督 ports 的整体方向、建筑配套和人事事务。下面是上一季度的情况。

目前，在 Ports 中有超过 30,500 个 port。目前有不到 2,800 个开放的 port PR，其中 750 个是未分配的。上一季度，主分支上有 151 个提交者提交了 9,137 份代码，2022Q3 分支上有 61 个提交者提交了 589 份代码。与两个季度前相比，这意味着 port 的数量略有增加，但也意味着（未分配的）port PR 的数量略有增加，提交的数量略有减少。

在上一季度，我们欢迎 Felix Palmen (zirias@) 成为新的 ports committer，欢迎 Akinori MUSHA (knu@) 回来，并向 Olli Hauer (ohauer@) 道别。我们还欢迎 Luca Pizzamiglio (pizzamig@) 成为 portmgr 的正式成员。

在上个季度中，对 Ports 树进行了一些大的修改。

从每个 Makefile 的顶部删除了“Created by” 一行，因为其中很多都已经过时了。

WWW: 已经从每个 pkg-descr 中移到了每个 Makefile 中作为一个变量； 以下是 Stefan Eßer (se@) 所写的，他做了这项工作。

对一个 port 功能的描述，应以提供进一步信息的网页的 网址 结束，例如使用或配置的最佳实践。这些信息可以用 pkg query -e 来显示已安装的包，或 pkg rquery -e 来显示可用的包。网址 曾经被附加到 ports 的 pkg-descr 文件的末尾，并以“WWW:”为前缀，这样工具就可以从描述中提取 网址。随着时间的推移，许多这样的 网址 都变得过时了，因为 port 的更新通常只修改 Makefile，而不是 pkg-descr 文件。通过将这些 网址 的定义移到 Makefile 中，维护者更有可能将 网址 与其它的 port 变更一起更新，而工具也能更容易地访问它们。现在，网址 被分配给 Makefile 中的 WWW 宏，并可以通过 port 目录中的 make -V WWW 进行查询。处理软件包文件中的描述的工具仍然能够工作，因为最后的“WWW:”行是由 Makefile 中的 WWW 值生成的。

在 EuroBSDCon 期间，portmgr@ 对改善内核模块包的情况进行了讨论。讨论了各种可能性。

以下是发生在幕后的情况：

- 一个新的 USES，“vala”，被添加进来。
- Go 的默认版本被提升到了 1.19。
- CMake 现在是一个元 port
- 增加了对 Qt 6 的初步支持，版本为 6.3.2
- Vim 不再在系统中安装 vimrc 了。
- 一些主要的 ports 得到了更新：
  - pkg 1.18.4
  - Chromium 106.0.5249.91
  - Firefox 105.0.1
  - 火狐长期支持版本 102.3.0
  - KDE 应用程序 22.8.1
  - KDE 框架 5.98
  - Rust 1.63.0
  - SDL 2.24.0
  - Xorg 服务器 21.1.4 (大修)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 项目

跨越多个类别的项目，从内核和用户空间到 Ports 或外部项目。

### FreeBSD 上的 OpenStack

链接：

OpenStack 网址: https://www.openstack.org/

OpenStack on FreeBSD 网址: https://github.com/openstack-on-freebsd

联系：Chih-Hsin Chang [starbops@hey.com](mailto:starbops@hey.com) 联系：Li-Wen Hsu [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

OpenStack 是一个开源的云操作系统，适用于不同类型的资源，如虚拟机和裸机。用户可以在这个开放的云平台上催生 FreeBSD 实例，但目前还不能在 FreeBSD 主机上运行 OpenStack 控制面板。这个项目的目标是移植 OpenStack 的关键组件，使 FreeBSD 能够作为 OpenStack 主机运行。

学术界和工业界的研究小组从 2022 年中期开始对支持 CHERI 的 Morello 板进行了评估。像 OpenStack 这样的资源协调平台可以提高配置、管理和回收这些板子的速度和成本。

从 2022 年 1 月开始，Chih-Hsin Chang 一直在努力将几个 OpenStack 组件移植到 FreeBSD 上运行，包括：

- Keystone（身份服务）
- Glance (图像服务)
- Placement (资源跟踪和库存服务)
- Neutron (网络服务)
- Nova (计算服务)

其中一些项目仍在大力开发中。例如，由于 Neutron 的设计，DHCP 服务器被放在 Linux 网络命名空间内。有必要在 FreeBSD 上找到一个替代品，例如 vnet，并对其进行调整。大多数情况下，移植的策略是通过绕过障碍物来尽可能地减少影响。但是像 oslo.privsep 这样的东西值得进行真正的移植。oslo.privsep 根植于 Linux 的能力，可以进行权限分离工作。现在我们只是在 oslo.privsep 中绕过了任何与 Linux 功能相关的操作。所以目前在源代码和配置中存在大量的 hack 行为。所有这些连同编译和安装步骤将被收集在项目库中。

在第四季度，Chih-Hsin 计划专注于移植 Neutron 和 Nova，以完成虚拟机的生命周期操作。亮点包括：

- DHCP 集成
- FreeBSD 桥接驱动/代理
- Bhyve + Libvirt 集成
- 赞助商：FreeBSD 基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 作为一级云计算平台的 FreeBSD

链接：

cloud-init Website 网址: https://cloud-init.io/

cloud-init Documentation 网址: https://cloudinit.readthedocs.io/en/latest/

cloud-init ongoing refactorization 网址: link:https://github.com/canonical/cloud-init/blob/main/WIP-ONGOING-REFACTORIZATION.rst

联系：Mina Galić [me+FreeBSD@igalic.co](mailto:me+FreeBSD@igalic.co)

cloud-init 是在云中配置服务器的标准方式。不幸的是，对 Linux 以外的操作系统的云计算支持相当差，而 FreeBSD 缺乏对云计算的支持，这对那些希望提供 FreeBSD 作为一级平台的云计算供应商来说是一个障碍。为了补救这种情况，这个项目旨在使 FreeBSD 的云端启动支持与 Linux 的支持相提并论。更广泛的计划是提升对所有 BSD 的支持。

这个项目的成果包括完成对某些网络类的提取，实现 ifconfig(8) 和 login.conf(5) 解析器，实现 IPv6 配置，为 Azure 创建 devd.conf(5) 规则，以及 FreeBSD Handbook 关于生产 FreeBSD 的文档。

在这个过程中，任何在模块和文档中发现的与 BSD 相关的错误也将被修复。

有兴趣帮助这个项目的人可以通过 net/cloud-init-devel 来帮助测试新的功能和修复，这个项目将每周更新一次。此外，我们也非常欢迎能够使用 OpenBSD 和 NetBSD 并有相关经验的人提供帮助。

赞助商：FreeBSD 基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 用户空间

影响基本系统和其中程序的变化。

#### bhyve 调试服务器的增强

链接：

链接：Wiki project page

链接：Differential

联系：Bojan Novković [bojan.novkovic@kset.org](mailto:bojan.novkovic@kset.org)

这个项目的目标是增强 bhyve 的调试服务器的功能。现有的几个与单步走有关的功能与英特尔特定的虚拟机机制有关，这严重损害了 bhyve 在其他 x86 平台上的调试功能。第一个目标是将单步支持扩展到 AMD 主机上。第二个目标是使用客户操作系统的硬件调试寄存器增加对硬件观察点的支持。

该项目是在谷歌的夏季代码计划下进行的，大约在 7 月底完成。这个项目的维基还包含了关于几个已实现机制的详细文档。

这些变化可以总结为以下几点：

- 支持在 AMD 平台的虚拟机内放置软件断点。
- 支持在 AMD 平台上对虚拟机进行单步操作。
- 支持在英特尔和 AMD 平台的虚拟机中放置硬件观察点。

欢迎任何反馈、评论和讨论，我们将不胜感激。

赞助商：谷歌代码之夏

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 重写 pjdfstest

链接：

Github 网址: https://github.com/musikid/pjdfstest

Blog 网址: https://musikid.github.io/blog/rewrite-pjdfstest/

联系：Alan Somers [asomers@FreeBSD.org](mailto:asomers@FreeBSD.org)

早在 2007 年，Pawel Jakub Dawidek [pjd@FreeBSD.org](mailto:pjd@FreeBSD.org) 编写了 pjdfstest，一个 POSIX 文件系统的一致性测试工具。他最初写这个工具是为了验证 ZFS 对 FreeBSD 的移植，但后来它也被用于其他文件系统和其他操作系统。

今年，Sayafdine Said [musikid@outlook.com](mailto:musikid@outlook.com)在 Google 的赞助下重写了它。新版本有几个改进：

- 可配置性增强，以便更好地与其他文件系统一起使用。
- 速度更快，主要得益于上述可配置性。
- 更好的测试案例隔离，使故障易于调试。
- 所有测试用例不再需要 root 权限。
- 测试用例可以在调试器中运行。
- 可维护性增强，减少重复操作。

仍有几个悬而未决的 PR 需要完成，但我们希望能把这些工作做完，并很快把 pjdfstest 加入到 ports 中。在那里，它将被 /usr/tests 用于 ZFS 和 UFS，以及被外部开发者用于其他文件系统。

赞助商：谷歌代码之夏

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 正在进行的关于 LLDB 多进程调试支持的工作

链接：

Moritz Systems Project Description 网址: https://www.moritz.systems/blog/multiprocess-support-for-lldb/

Progress Report 1 网址: https://www.moritz.systems/blog/implementing-non-stop-protocol-compatibility-in-lldb/

Progress Report 2 网址: https://www.moritz.systems/blog/full-multiprocess-support-in-lldb-server/

联系：Kamil Rytarowski [kamil@moritz.systems](mailto:kamil@moritz.systems)

联系：Michał Górny [mgorny@moritz.systems](mailto:mgorny@moritz.systems)

根据上游的描述，“LLDB 是下一代高性能调试器。它是作为一组可重用的组件构建的，这些组件高度利用了更大的 LLVM 项目中的现有库，例如 Clang 表达式解析器和 LLVM 反汇编器。”

FreeBSD 在基本系统中包括 LLDB。之前赞助的项目改进了 LLDB，使其成为基础系统中可信的调试器，尽管它与 GNU GDB 的当代版本相比仍有一些限制。这个项目于 2022 年 4 月开始。它的目标是实现对多个进程同时调试的全面支持。

在项目开始时，LLDB 对多进程调试的支持非常有限。目前，服务器已经能够使用 GDB 远程串行协议的多进程扩展来监控多个进程。为该协议实现客户端对应的工作正在进行。

一旦该项目完成，LLDB 将能够同时跟踪任意数量的分叉进程（相当于 GDB 的 detach-on-fork off）。

赞助商：FreeBSD 基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### DTrace：指令级动态跟踪

链接：

Wiki article 网址: https://wiki.freebsd.org/SummerOfCode2022Projects/InstructionLevelDynamicTracing

Final code review 网址: https://reviews.freebsd.org/D36851

联系：Christos Margiolis [christos@FreeBSD.org](mailto:christos@FreeBSD.org)

联系：Mark Johnston [markj@FreeBSD.org](mailto:markj@FreeBSD.org)

kinst 是一个新的 DTrace 提供者，允许任意的内核指令追踪。

该提供程序目前只针对 amd64 实现，但我们计划在未来将其移植到其他架构上。

kinst 探针是由 libdtrace 按需创建的，几乎可以为内核中的每一条指令创建探针。探针的形式如下：

```
kinst:<module>:<function>:<offset>
```

其中 `module` 是包含指定函数的内核模块，`function`是要追踪的内核函数，`offset` 是特定指令的偏移量。省略 `offset` 会使函数中的所有指令都被追踪。省略 `module` 会导致 DTrace 搜索该函数的所有内核模块。

例如，要追踪 amd64_syscall() 中的第二条指令，首先确定第二条指令的偏移量：

```
# kgdb
(kgdb) disas /r amd64_syscall
Dump of assembler code for function amd64_syscall:
   0xffffffff809256c0 <+0>:     55      push   %rbp
   0xffffffff809256c1 <+1>:     48 89 e5        mov    %rsp,%rbp
   0xffffffff809256c4 <+4>:     41 57   push   %r15
```

偏移量为 1。然后，要追踪它：

```
# dtrace -n 'kinst::amd64_syscall:1'
```

D 语言中还增加了一个新的关键字 `regs`，提供了对探针启动时的 CPU 寄存器的只读访问。例如，当 kinst::amd64_syscall:1 探针启动时，追踪帧指针的内容（amd64 上的寄存器 %rbp）:

```
# dtrace -n 'kinst::amd64_syscall:1 {printf("0x%x", regs[R_RBP]);}'
```

kinst 的工作方式与 FBT（函数边界跟踪）提供者类似，它在目标指令上放置一个断点，并钩住内核的断点处理程序。它比 FBT 更强大，因为它可以用来在一个函数中的任意点上创建探针，而不是在函数边界。因为 kinst 必须能够追踪任意指令，所以它没有在软件中模拟大多数指令，而是使被追踪的线程在返回到原始代码之前执行一个指令的副本。

计划中的未来工作包括将 kinst 移植到更多的平台上，特别是 arm64 和 riscv，以及开发可以使用 kinst 追踪使用内核调试符号的内联函数调用的工具。

赞助商：谷歌公司（GSOC 2022）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 内核

内核子系统/功能、驱动支持、文件系统等方面的更新。

#### ENA FreeBSD 驱动程序更新

链接：

ENA README 网址: https://github.com/amzn/amzn-drivers/blob/master/kernel/fbsd/ena/README.rst

联系：Michal Krawczyk [mk@semihalf.com](mailto:mk@semihalf.com)

联系：David Arinzon [darinzon@amazon.com](mailto:darinzon@amazon.com)

联系：Marcin Wojtas [mw@FreeBSD.org](mailto:mw@FreeBSD.org)

ENA（弹性网络适配器）是亚马逊网络服务（AWS）的虚拟化环境中可用的智能网卡。ENA 驱动程序支持多个发送和接收队列，可以处理高达 100Gb/s 的网络流量，这取决于它所使用的实例类型。

自上次更新以来已完成：

- ENA 驱动 v2.6.0 和 v2.6.1 的上游，包括。
- 修复了第 6 代实例重置后的性能下降问题。
- 修复了启用 KASSERT 时的错误网图断言。
- 代码清理和风格修正。
- 记录的改进。
- 修复了 ENI 指标的检索问题。

赞助商：Amazon.com Inc

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### wtap(4) 增强

链接：

Add sta, hostap and adhoc mode to wtap wlan simulator

联系：En-Wei Wu [enweiwu@FreeBSD.org](mailto:enweiwu@FreeBSD.org)

联系：Li-Wen Hsu [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

联系：Bjoern A. Zeeb [bz@FreeBSD.org](mailto:bz@FreeBSD.org)

wtap(4) 是 Monthadar Al Jaberi [monthadar@gmail.com](mailto:monthadar@gmail.com) 和 Adrian Chadd [adrian@FreeBSD.org](mailto:adrian@FreeBSD.org) 在 2012 年推出的一个 net80211(4)Wi-Fi 模拟器。它最初支持 802.11s 网状模式，并被用于验证。在 2022 年谷歌代码之夏期间，En-Wei 一直致力于为它带来 sta、hostap、adhoc 和监控模式。这项工作还包括用 atf(7) 编写的 wtap(4) 为 net80211(4) 添加基本测试。

更多细节，请查看项目的 wiki 页面。

赞助商：Google Summer of Code 赞助商：FreeBSD 基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 英特尔无线向 11ac 发展

链接：

Intel iwlwifi status FreeBSD wiki page 网址: https://wiki.freebsd.org/WiFi/Iwlwifi

联系：Bjoern A. Zeeb [bz@FreeBSD.org](mailto:bz@FreeBSD.org)

这个正在进行的项目旨在使用 LinuxKPI 兼容代码和本地 net80211 和内核代码支持 FreeBSD 上最新的 Intel 无线芯片组。此外，在 LinuxKPI 802.11 兼容代码中支持 11n 和 11ac 标准的工作正在进行中，并在本地 net80211 无线堆栈中填补 11ac 的空白。

对于英特尔 iwlwifi 无线驱动程序，在过去几个月中没有重大更新。我们将固件更新到最新的公开可用版本，并修复了一些最明显的错误。支持 D3 节电代码的工作也在进行中。

LinuxKPI 兼容代码也得到了一些改进和修复，这些改进和修复有时只在某些世代的 iwlwifi 芯片组上可以看到。

net80211 和 LinuxKPI 兼容代码对 11n 和 11ac 的改变到目前为止几乎没有公开可见，以避免破坏基本支持。基于较新的 802.11 标准的常量更新和其他没有用户可见效果的变化被合并了，功能上的变化将在未来几个月内跟进，最初隐藏在编译时或运行时选项后面。

为了跟踪这个分支的用户的利益，以及帮助进行更多的测试，改进和更新大部分被合并回 stable/13。

要了解最新的开发状况，请关注 freebsd-wireless 邮件列表和查看 wiki 页面。

赞助商：FreeBSD 基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 更多无线更新

链接：

Bjoern’s Wireless Work In Progress landing page 网址: https://people.freebsd.org/\~bz/wireless/

Realtek rtw88 status FreeBSD wiki page 网址: https://wiki.freebsd.org/WiFi/Rtw88

Realtek rtw89 status FreeBSD wiki page 网址: https://wiki.freebsd.org/WiFi/Rtw89

MediaTek mt76 status FreeBSD wiki page 网址: https://wiki.freebsd.org/WiFi/Mt76

QCA ath11k status FreeBSD wiki page 网址: https://wiki.freebsd.org/WiFi/Ath11k

联系：Bjoern A. Zeeb [bz@FreeBSD.org](mailto:bz@FreeBSD.org)

目前的发展主要是由英特尔的 iwlwifi 驱动再次推动（见其他报告）。俗话说“互相帮助”，所以 Realtek 的 rtw89 驱动的工作有助于发现困扰 iwlwifi 用户的 LinuxKPI 的错误。在这份状态报告中，主题主要是更多的驱动程序，它们确实需要更多的 LinuxKPI 支持。

各种工作正在进行中：

- Realtek 的 rtw88 PCI 正在进行中，在 EuroBSDCon 上与 Hans Petter Selasky 进行了富有成效的讨论后，rtw88 USB WiFi 加密狗的 LinuxKPI USB 支持工作将继续进行。
- Realtek 的 rtw89 驱动已经提交给 main，但还没有连接到构建中。扫描工作已经开始，但数据包还没有通过。有了这个驱动，就可以为拥有该芯片组的用户提供测试便利，以确定更多未实现的 LinuxKPI 位（其中一些也会帮助其他驱动），并减少我的工作。
- 下一个驱动可能是基于联发科的 mt76 驱动（用于 7921 和 7915），我已经在编译并开始测试。
- 根据要求，我也在开发支持 STA 模式的 ATH11K，因为一些供应商似乎用这些芯片运送笔记本电脑。

虽然其中一些工作显然得益于 FreeBSD 基金会赞助的 iwlwifi 和较新的标准支持，但其中很多只是自由时间的工作。如果你对这些驱动程序中的任何一个感兴趣，我将非常感激，如果有更多的人能够帮助其中的一个或另一个。这可能是定期测试主程序的更新，编写文档和更新 wiki 页面，跟踪 PR，尝试补丁，帮助个别 LinuxKPI 位的工作，无论是否有 802.11 的工作，或者只是调试个别驱动和/或芯片组的问题。如果你有兴趣帮助上述任何一项工作，请给我发邮件。

对于最新的发展状况，请关注 freebsd-wireless 邮件列表并查看 wiki 页面（如果存在）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 在使用日志式软更新的文件系统上启用快照

链接：

Milestone 1 Core Changes 网址: https://reviews.freebsd.org/D36491

联系：Kirk McKusick [mckusick@FreeBSD.org](mailto:mckusick@FreeBSD.org)

这个项目将使 UFS/FFS 文件系统的快照在使用日志式软更新运行时可用。

UFS/FFS 文件系统有拍摄快照的能力。因为快照的拍摄是在软更新编写之后加入的，它们与软更新完全集成。当日志式软更新在 2010 年被添加时，它们从未与快照整合。因此，快照不能在运行有日志的软更新的文件系统上使用。

随着 FreeBSD 对 ZFS 的支持，快照变得不那么重要了，因为 ZFS 可以快速而容易地进行快照。然而，在两种情况下，UFS 快照仍然是重要的。第一是它们允许可靠地转储实时文件系统，从而避免了可能的数小时的停机时间。第二种情况是，它们允许运行后台 fsck。类似于 ZFS 中对刷新的需求，fsck 需要定期运行以发现未被发现的磁盘故障。快照允许 fsck 在实时文件系统上运行，而不是需要安排停机时间来运行它。

这个项目有两个目标：

- 在运行日记式软更新时启用快照，并确保它们可以被用于在实时文件系统上进行后台转储。这个目标应该在 2022 年底前完成。
- 扩展 fsck_ffs，使其能够使用快照对运行有日记软更新的文件系统进行后台检查。这个目标预计将在 2023 年第三季度完成。

赞助：FreeBSD 基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 架构

更新特定平台的功能并引入对新硬件平台的支持。

#### FreeBSD/Firecracker

链接：

Firecracker VM

联系：Colin Percival [cperciva@FreeBSD.org](mailto:cperciva@FreeBSD.org)

Firecracker 是由 Amazon Web Services 开发的开源“微型虚拟机”；它是为“无服务器”计算环境的需要而设计的，并特别注重安全和极简主义。

从 2022 年 6 月开始，Colin Percival 一直在努力将 FreeBSD 移植到 Firecracker 环境中运行，并得到了其他 FreeBSD 开发者的大力协助。在这份季度报告中，一组补丁正在等待审查，这些补丁共同增加了所需的支持，使 FreeBSD 能够在 Firecracker 的补丁版本中运行。

在第四季度，Colin 打算完成对 FreeBSD 的相关补丁的提交，发布内核和磁盘镜像，以便其他 FreeBSD 用户可以尝试使用 Firecracker，并更新和合并 Firecracker 的补丁，增加 PVH 启动支持（被 FreeBSD 使用）。

这项工作已经产生了“附带”的好处，揭示了加速 FreeBSD 启动过程的方法；由于其低开销和最小的环境，Firecracker 是进行这项工作的绝佳环境。

这项工作得到了 Colin 的 FreeBSD/EC2 Patreon 的支持。

赞助商：https://www.patreon.com/cperciva

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 文档

在文档、手册页或新的外部书籍/文档中值得注意的变化。

#### 文档工程团队

链接：FreeBSD 文档项目

链接：为新的贡献者提供的 FreeBSD 文 档项目入门手册

链接：文档工程团队

联系：FreeBSD Doceng 团队 [doceng@FreeBSD.org](mailto:doceng@FreeBSD.org)

doceng@ 团队是一个处理与 FreeBSD 文档工程相关的一些元项目问题的机构；更多信息请参见 FreeBSD Doceng 团队章程。

在上个季度：

- 0mp@ 卸任了 Doceng 的秘书，fernape@ 加入成为新的秘书。Doceng 感谢 0mp@ 的服务。
- eadler@ 的文档位在他的要求下被收走保管。
- 为文档库添加了一个 git 提交信息模板。

待定和讨论中的项目：

- 删除网站和文档门户中过时的翻译。

#### FreeBSD 的文档项目入门

- FDP 中增加了关于商标处理的信息。

#### port 开发者手册

- 更新了关于移植 Haskell 程序的文档。
- 记录了将 WWW 从 pkg-descr 移到 Makefile 的过程。
- 在 ports 框架中导入 Qt 6 库之后，增加了与之相关的文档。

#### FreeBSD 网站的翻译

链接：在 Weblate 上翻译 FreeBSD

链接：FreeBSD Weblate 实例

**2022 年第三季度状况**

12 种语言

148 个注册用户

Gasol Wu 加入了中文翻译团队。

Alvaro Felipe Calle 加入了西班牙语翻译团队。

**语种**

- 中文（简体） (zh-cn) (进度: 8%)
- 中文（繁体）（zh-tw）（进度：4%）。
- 荷兰语 (nl) (进展: 1%)
- - 法语 (fr) (进展: 1%)
- 德文 (de) (进展: 1%)
- 印度尼西亚语 (id) (进展: 1%)
- 意大利语 (it) (进展: 4%)
- 挪威语 (nb-no) (进展: 1%)
- 波斯语 (fa-ir) (进展: 3%)
- 葡萄牙语 (pt-br) (进展: 16%)
- 西班牙文 (es) (进展: 15%)
- 土耳其语 (tr) (进展: 2%)

我们要感谢每一个作出贡献、翻译或审阅文件的人。

请在您当地的用户群中推广这项工作，我们总是需要更多的志愿者。

#### FreeBSD 手册页面门户网站

联系：Sergio Carlavilla [carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)

Manual Pages Portal 已经被重新设计为使用 mandoc(1) 进行渲染。门户网站的预览版已经推出。我们已经收集了反馈，并在可能的情况下进行了处理。还有一些剩余的非阻塞问题。Doceng@ 希望继续推进向这个新门户的迁移。

感谢所有审查和提供反馈的人。

#### FreeBSD 网站改版——WebApps 工作组

联系人：Sergio Carlavilla [carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)

负责创建新的 FreeBSD 文档门户和重新设计 FreeBSD 主网站及其组件的工作小组。FreeBSD 开发者可以在 FreeBSD Slack 频道 #wg-www21 上关注并加入该工作组。这项工作将分为四个阶段。

1. 重新设计文档门户

创建一个新的设计，具有响应性和全局搜索功能。(完成)

1. 重新设计网络上的手册页面

使用 mandoc 生成 HTML 页面的脚本。(完成)

1. 重新设计网络上的“ports”页面

用 ports 脚本来创建一个应用门户。(工作正在进行中)

1. 重新设计 FreeBSD 的主网站

新设计，响应式和暗色主题。(未开始)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### ports

影响 Ports 的变化，无论是涉及大部分的全面变化，还是个别 port 本身。

### Calendar-data：添加了许可证

链接：

GitHub calendar-data 仓库的 网址: https://github.com/freebsd/calendar-data

联系：Stefan Eßer [se@FreeBSD.org](mailto:se@FreeBSD.org)

联系：Lorenzo Salvadore [salvadore@FreeBSD.org](mailto:salvadore@FreeBSD.org)

联系：Warner Losh [imp@FreeBSD.org](mailto:imp@FreeBSD.org)

port deskutils/calendar-data 包含了 BSD 日历程序的日历文件，由 se@ 维护。这个 ports 的数据存在于 GitHub 仓库，目前主要由 salvadore@ 维护。

大约两年前，基础仓库中的日历文件被从那里删除，并在 GitHub 上创建了一个新的仓库；也可以参见这篇关于创建相关 ports 的 Phabricator 评论。这一改进使得日历文件可以独立于基础系统进行更新。

不幸的是，在创建存储库的时候，忘记了给它添加许可证。这个问题在本季度通过这个由 salvadore@ 提交并由 imp@ 合并的拉动请求得到了解决。由于这些数据最初来自 src 仓库，所以同样的许可证也适用。如果你在过去为日历文件贡献了不同的许可预期，请通知我们，这样我们就可以为你的贡献提供相应的许可，或者删除它们。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### FreeBSD 上 的 KDE

链接：

KDE FreeBSD 网址: https://freebsd.kde.org/

KDE Community FreeBSD 网址: https://community.kde.org/FreeBSD

联系：Adriaan de Groot [kde@FreeBSD.org](mailto:kde@FreeBSD.org)

KDE on FreeBSD 项目将来自 KDE Community 的软件，以及依赖关系和相关软件打包到 FreeBSD ports 上。这些软件包括一个叫做 KDE Plasma 的完整桌面环境（适用于 X11 和 Wayland）和数百个可以在任何 FreeBSD 机器上使用的应用程序。

KDE 团队 (kde@) 是 desktop@ 和 x11@ 的一部分，他们建立了软件堆栈，使 FreeBSD 成为漂亮的、可用于日常驱动的基于图形的桌面机器。下面的说明主要描述的是 KDE 的 ports，但也包括对整个桌面栈很重要的项目。

#### Qt6 可用

KDE ports 中的大新闻并不直接与 KDE 有关。Qt6 已经可用了，它为我们准备好了下一代基于 Qt 的应用程序。

现在可以用 USES=qt:6 来选择新的 Qt 版本。一些 ports 已经进行了调整以使用新的版本。

KDE 本身没有受到影响：针对 Qt6 的 KDE 框架的上游工作还没有完成。大多数 KDE Frameworks 会在 Qt6 上编译，但这对 FreeBSD 的 port 来说并不重要。使用 devel/qt6 可以得到 Qt 6.4.0，在本季度末发布。

#### KDE Stack

KDE Gear 每季度发布一次，KDE Plasma 每月更新一次，KDE Frameworks 每月也有一个新版本。这些（大型）更新在其上游发布后不久就登陆了，并没有单独列出。

- KDE Frameworks 5 现在是 5.98 版本（从 2022 年 9 月开始每月最新发布）。
- KDE Gear 现在是 22.08.1 版（2022 年 9 月的更新）。
- KDE Plasma 现在是 5.24.6 版（2022 年 7 月的更新）。

请注意，KDE Plasma 5.25 已经在上游发布了，但在登陆 ports 之前还在等待修正 (例如，KDE 的 bug 跟踪中的这个 KActivityManager bug)。

#### 相关的 port

- accessibility/qt5-speech 现在支持多个后端，以及无后端的语音合成。
- devel/cmake 被重新组织了，因此 devel/cmake 现在是一个安装了 devel/cmake-core 和其余 CMake 套件的 metaport。(感谢 diizzy@) CMake ports 也被更新到了 3.24 版，并在整个树上的 ports 中做了相应的改动。
- net/qt5-network 改善了与 libressl 的兼容性。
- x11/plasma-wayland-protocols 在下一季度的 KDE Plasma 桌面更新之前已经更新。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### GCC：新的维护者，GCC 12.2 等等

链接：

GCC 项目网址：https://gcc.gnu.org

GCC 11 发布系列的网址：https://gcc.gnu.org/gcc-11/

GCC 12 发布系列的网址：https://gcc.gnu.org/gcc-12/

联系：[toolchain@FreeBSD.org](mailto:toolchain@FreeBSD.org)

联系：Lorenzo Salvadore [salvadore@FreeBSD.org](mailto:salvadore@FreeBSD.org)

- salvadore@ 采用了所有对应于 gcc 支持版本的现有 ports，即：lang/gcc10、lang/gcc11、lang/gcc11-devel、lang/gcc12、lang/gcc12-devel 和 lang/gcc13-devel。目前 -devel port 每周都会更新，除非是编译失败导致无法更新。当然，在后一种情况下，会尽快修复和/或向上游报告构建失败的情况。
- GCC 12.2 已经发布了。传统上，FreeBSD 会等待 GCC 的第二个次要版本的发布，将其作为默认的 GCC 版本，因此大部分需要用 GCC 编译的软件已经被移植到最新的主要版本。因此，将 GCC 默认版本更新为 12 版的工作已经开始。非常感谢已经运行了第一个 exp-run 的 antoine@ 以及所有参与这个过程的贡献者、维护者和提交者。https://bugs.freebsd.org/bugzilla/show\_bug.cgi?id=2659548
- 关于 LTO 的讨论一直在进行，有很多不同的观点。如果有兴趣，你可以阅读该主题的最新贡献：lang/gcc11: Needs build time warning for /tmp consumption 和 lang/gcc11: build gets stuck。提醒一下。LTO_BOOTSTRAP 是一个默认启用的选项。如果您在自己的机器上联编 port，而它的资源消耗是不可接受的，禁用这个选项会让您得到更轻的编译。
- jbeich@ 提交了一个补丁，以暴露非默认的 -stdlib=libc++ 支持，这个补丁已经成功地提交给所有相关的 port (gcc >= 11)。链接：https://bugs.freebsd.org/bugzilla/show\_bug.cgi?id=265962
- diizzy@ 刷新了 MASTER_SITE_GCC 变量中的镜像列表，同时删除了 ftp 镜像。GCC 主站点被用作后备站点。链接: https://reviews.freebsd.org/D36372
- 仍然需要对这三个变化提供帮助，以便与上游的 GCC 一起工作 (需要对 GCC 源码和上游的专业知识，而不是对 ports 框架的专业知识)。
  - upstreaming lang/gcc11/patch-gets-no-more
  - upstreaming lang/gcc11/patch-arm-unwind-cxx-support
  - https://bugs.freebsd.org/bugzilla/show\_bug.cgi?id=256874

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### sysutils/lsof 主要更新

链接：

lsof 项目 repo 网址: https://github.com/lsof-org/lsof

联系：

Larry Rosenman [ler@FreeBSD.org](mailto:ler@FreeBSD.org)

sysutils/lsf 进行了一次重大升级，不再在 `/dev/kmem` 中查找数据，而是使用用户空间的 API。这在源代码上花了很长时间，但终于完成了。自 13.0-RELEASE 以来，它第一次修复了 lsof(8) 与 ZFS 一起工作。

这将使今后的维护工作更加容易。

内核人员：如果你做了破坏 lsof 的改动，请提交 GitHub 拉取请求到 https://github.com/lsof-org/lsof。请测试对 lsof 使用的接口的任何改动，并确保它们仍然工作。现在这些都应该是用户地接口，但请测试。

我感谢 Warner Losh [imp@FreeBSD.org](mailto:imp@FreeBSD.org), Mateusz Guzik [mjg@FreeBSD.org](mailto:mjg@FreeBSD.org), 和 Ed Maste [emaste@FreeBSD.org](mailto:emaste@FreeBSD.org) 帮助我完成这一重大改变。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#### 第三方项目

许多项目都建立在 FreeBSD 的基础上，或者将 FreeBSD 的组件纳入他们的项目中。由于这些项目可能会引起更广泛的 FreeBSD 社区的兴趣，我们有时会在季度报告中加入这些项目提交的简短更新。FreeBSD 项目对这些提交的信息的准确性和真实性不做任何陈述。

#### 容器和 FreeBSD：Pot, Potluck and Potman

链接：

Pot 组织在 github 上的 网址: https://github.com/bsdpot

联系：Luca Pizzamiglio (Pot) [pizzamig@freebsd.org](mailto:pizzamig@freebsd.org)

联系：Stephan Lichtenauer (Potluck) [sl@honeyguide.eu](mailto:sl@honeyguide.eu)

联系。Michael Gmelin (Potman) [grembo@freebsd.org](mailto:grembo@freebsd.org)

Pot 是一个 jail 管理工具，也支持通过 Nomad 进行协调。

在上一季度，pot 0.15.3 已经发布。它包含了许多改进，比如 mount-out 可以移除或卸载之前 mount-in 的文件夹或文件系统，信号和 exec 命令，更好的 jail 生命周期处理，以及许多 bug 修复。

Nomad 驱动的新版本 nomad-pot-driver 0.9.0 也已经发布，支持信号和 exec，并进行了稳定性修复。

Potluck 的目标是成为 FreeBSD 和 pot，就像 Dockerhub 之于 Linux 和 Docker 一样：一个 pot 风味和完整的容器镜像的存储库，可用于 pot 和许多情况下 Nomad 的使用。

自从上次的状态报告以来，已经提交了许多变化，包括对核心镜像的许多修复和改进，如 grafana、postgresql-patroni 或 loki。此外，所有的镜像都已经针对 FreeBSD 13.1 和 12.3 进行了重建，并包含了当前正在使用的软件包的季度版本。

最后，Luca 在 EuroBSDCon 2022 上举办了 Pot 的实施和生态系统的讲座——一个天真的 FreeBSD 容器实施可以走多远。

一如既往，我们欢迎反馈和补丁。

## FreeBSD 2022 年第二季度 季度状况报告

> 原文地址 [https://www.freebsd.org/status/report-2022-04-2022-06/](https://www.freebsd.org/status/report-2022-04-2022-06/)。

FreeBSD 季度状态报告 2022 年第二季度

这里是 2022 年的第二份季度报告，共包括 26 份报告。

在本季度，季度团队设法更快地发布报告，并希望能减少错误。然而，如果你注意到某些错误，请报告，以便我们能够纠正它们，并在我们的工具中添加自动检查设置，以防止将来出现这些错误，并尽可能对发布过程保持高效率。

我们还想提醒你，如果由于任何原因，你需要更多的时间来提交季度报告，团队将等待你，但请提醒我们，以便我们意识到有些报告仍未提交。

非常感谢所有选择通过季度报告与 FreeBSD 社区分享其工作的人。

Lorenzo Salvadore，代表现状报告小组。

---

本报告的渲染版可在此查阅： [https://www.freebsd.org/status/report-2022-04-2022-06/](https://www.freebsd.org/status/report-2022-04-2022-06/)

---

目录

- FreeBSD 团队报告
  - FreeBSD 核心团队
  - FreeBSD 基金会
  - FreeBSD 发布工程团队
  - 集群管理团队
  - 持续集成
  - Ports
- 项目
  - Linux 兼容层更新
  - FreeBSD 与 riscv64
  - 微软 HyperV 和 Azure 上的 FreeBSD
- 用户空间
  - 正在进行的关于 LLDB 多进程调试支持的工作
  - makefs(8) 中的 ZFS 支持
  - 基础系统 OpenSSH 更新
  - pf 的最新状况
- 内核
  - ENA FreeBSD 驱动程序更新
  - 新的蓝牙 ® 配置守护程序：blued
  - OpenVPN DCO
  - 无线更新
  - 共享页地址随机化
- 架构
  - 支持恩智浦 DPAA2
  - 关于 arm64 及其他的中型超级页
- 文件
  - 文档工程团队
- Ports
  - FreeBSD 上的 KDE
  - 其他地方
  - GCC ：更新 GCC_DEFAULT 和其他改进
  - Valgrind - 13.1/14.0 的大量错误修正和更新
  - FreeBSD 上 的 Pantheon 桌面
  - 英特尔的 igt-gpu-tools 的完整功能移植

---

### FreeBSD 团队报告

来自各官方和半官方团队的报告，可在[行政页面](https://www.freebsd.org/administration/)找到。

### FreeBSD 核心团队

联系：FreeBSD 核心团队 [core@FreeBSD.org](mailto:core@FreeBSD.org)

FreeBSD 核心团队是 FreeBSD 的管理机构。

第十二代 FreeBSD 核心团队是由活跃的开发者选举产生的。core.12 的成员是：

- Baptiste Daroussin（bapt, 现任）
- Benedict Reuschling（bcr）
- Ed Maste（emaste, 现任）
- Greg Lehey（grog）
- John Baldwin（jhb）
- Li-Wen Hsu（lwhsu）
- Emmanuel Vadot（manu）
- Tobias C. Berner（tcberner）
- Mateusz Piotrowski（0mp）

6 月 10 日，即将离任的 core.11 和即将上任的 core.12 团队召开了交接会议，新的核心团队于 6 月 18 日宣布成立。

在任命新的核心小组秘书和完成交接任务后，现任核心小组秘书 Muhammad Moinur Rahman (bofh) 将卸任。

在本季度，Kornel Dulęba（kd）和 Dmitry Salychev（dsl）的 src 提交权限已经被批准。

---

### FreeBSD 基金会

链接：

FreeBSD 基金会 网址：https://www.FreeBSDFoundation.org

技术路线图 网址：https://FreeBSDFoundation.org/blog/technology-roadmap/

捐赠 网址：https://www.FreeBSDFoundation.org/donate/

基金会合作计划 网址：https://www.FreeBSDFoundation.org/FreeBSD-foundation-partnership-program

FreeBSD 杂志 网址：https://www.FreeBSDFoundation.org/journal/

基金会新闻和活动 网址：https://www.FreeBSDFoundation.org/news-and-events/

联系：Deb Goodkin deb@FreeBSDFoundation.org

FreeBSD 基金会是一个 501(c)(3) 的非营利组织，致力于支持和促进全球的 FreeBSD 项目和社区。捐献来自个人和企业的资金被用来资助和管理软件开发项目、会议和开发者峰会。我们还为 FreeBSD 贡献者提供旅行补助，购买和支持硬件以改善和维护 FreeBSD 的基础设施，并提供资源以改善安全、质量保证和发布工程工作。我们发布营销材料来推广、教育和宣传 FreeBSD 项目，促进商业供应商和 FreeBSD 开发者之间的合作，最后，在执行合同、许可协议和其他需要公认的法律实体的法律安排中代表 FreeBSD 项目。

#### 筹集资金的努力

首先，我想向所有为我们的工作提供资金捐助的人表示衷心的感谢。我们的资金 100% 来自于你们的捐款，因此每一笔捐款都可以帮助我们在许多方面继续支持 FreeBSD，包括在这份状况报告中资助和发表的一些工作。

我们今年的目标是为大约 200 万美元的支出预算筹集至少 140 万美元。在我写这份报告的时候，我们为实现这一目标筹集了不到 20 万美元。因此，我们显然需要加紧努力筹款。这是迄今为止我工作中最困难的部分。我更愿意和社区中的人们讨论我们如何帮助你们，帮助创造内容以招募更多的用户和贡献者加入项目，并了解个人和组织在使用 FreeBSD 时遇到的挑战和痛点，以便我们能够帮助改善这些方面。索取金钱并不在此列。

我们在五个主要领域支持 FreeBSD。软件开发是我们资助的最大的领域，我们有六个软件开发人员，他们介入实现新的功能，支持一级平台，审查补丁，并修复问题。你可以在这份报告中了解到我们在操作系统改进方面所做的一些工作。FreeBSD 宣传是我们支持的另一个领域，通过会议、网上和现场的演讲、教程和操作指南来传播 FreeBSD 的信息。我们购买并支持用于支持该项目工作的 FreeBSD 基础设施的硬件。基金会组织的虚拟和现场活动帮助联系和吸引社区成员分享他们的知识并进行项目合作。最后，我们在需要时为项目提供法律支持，并保护 FreeBSD 的商标。

如果你今年还没有捐款，请考虑一下捐款，地址是：[https://freebsdfoundation.org/donate/](https://freebsdfoundation.org/donate/)。

我们还有一个针对大型商业捐助者的合作伙伴计划。你可以在 [https://freebsdfoundation.org/our-donors/ ](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/)找到更多信息。

#### 操作系统的改进

在 2022 年第二季度，有 243 份 src、62 份 port 和 12 份文档树的提交将 FreeBSD 基金会列为赞助商。这分别占了每个版本库中提交总数的 10.6%、0.7% 和 4.5%。

#### 赞助工作

你可以在个别季度报告条目中读到一些基金会赞助的工作。

- 基础系统 OpenSSH 更新
- 正在进行的关于 LLDB 多进程调试支持的工作
- 无线状态
- 在 makefs 中支持 ZFS

这里介绍了其他正在进行的赞助工作。

- FreeBSD Wireguard 的改进

> Wireguard 项目的目的是改善对 FreeBSD Wirguard 内核模块的支持。
>
> John Baldwin 的工作包括调整模块，使其使用 FreeBSD 的 OCF 而不是 Wireguard 的内部实现。 它还包括增加新的密码和 API 支持。
>
> 最新的上游版本包含了这项工作。

- FreeBSD 上的 Openstack

> OpenStack 是一个用于不同类型资源（如虚拟机）的云系统。
>
> 然而，OpenStack 只非官方地支持 FreeBSD 作为客户系统。
>
> 这意味着用户可以在开放的云平台上催生 FreeBSD 实例，但目前还不能在 FreeBSD 主机上运行 OpenStack。
>
> 这个项目的目标是移植 OpenStack 组件，使 FreeBSD 能够作为 OpenStack 主机运行。

- Bhyve 问题支持

> 基金会最近签署了一份支持 Byhve 的新合同。
>
> 这份合同将使 John Baldwin 能够在 Bhyve 出现问题时为其奉献时间，特别是安全问题。

- Handbook 改进探索

> 在基金会的赞助下，Pau Amma 完成了一个小型项目，探索如何改进《Handbook》。
>
> 已经发出了一份调查，结果将很快与大家分享。

#### 持续集成和质量保证

基金会提供了一名全职工作人员，并资助了一些项目，以改善持续集成、自动测试以及 FreeBSD 项目的整体质量保障工作。

#### 支持 FreeBSD 基础设施

基金会为该项目提供硬件和支持。一个新的澳大利亚镜像被集群管理团队部署到了网上。如果你是大洋洲或东南亚的 FreeBSD 用户，请让我们知道安装程序镜像和软件包的下载速度是否有所提高。

通过你们的捐款，基金会购买了新的硬件来修复两个 PowerPC 软件包的构建器，一个是小端软件包（powerpc64le），第二个是大端软件包（powerpc64，powerpc）。新的硬件刚刚到达数据中心，很快就会安装。预计在不久的将来会有很多 PowerPC 软件包。

#### 倡导和教育 FreeBSD

我们的大部分工作是致力于项目的宣传。这可能涉及到突出有趣的 FreeBSD 工作，制作文献和视频教程，参加活动，或做演讲。我们制作文献的目的是教给人们 FreeBSD 的基本知识，并帮助他们在采用或贡献的道路上更加容易。除了参加活动和发表演讲之外，我们还鼓励和帮助社区成员举办他们自己的 FreeBSD 活动，发表演讲，或者担任 FreeBSD 的工作人员。

FreeBSD 基金会在全球范围内赞助了许多会议、活动和峰会。这些活动可以是与 BSD 相关的，也可以是开源的，或者是面向未被代表的群体的技术活动。我们支持以 FreeBSD 为中心的活动，以帮助提供一个分享知识的场所，在项目上一起工作，并促进开发者和商业用户之间的合作。这都有助于提供一个健康的生态系统。我们支持非 FreeBSD 的活动，以促进和提高对 FreeBSD 的认识，增加 FreeBSD 在不同应用中的使用，并招募更多的贡献者加入该计划。我们将继续参加虚拟活动，并计划在 2022 年 6 月举行开发者峰会。除了参加和策划虚拟活动之外，我们还在不断地进行新的培训计划，并更新我们的指南选择，以促进更多的人尝试使用 FreeBSD。

请看我们上一季度所做的一些宣传和教育工作：

- 我们获得了 2022 年 10 月 30 日至 11 月 2 日在北卡罗来纳州罗利举行的 All Things Open 的展位和非营利性赞助商地位
- 我们在 7 月 28-30 日在加州洛杉矶举行的 Scale 19x 上的展位和研讨会已经确定。FreeBSD 研讨会将于 2022 年 7 月 29 日星期五举行，你可以到基金会的 502 号展位参观
- 确认我们是 2022 年 9 月 15-18 日在奥地利维也纳举行的 EuroBSDcon 的银牌赞助商
- 赞助并帮助组织 2022 年 6 月 16-17 日的 FreeBSD 开发者峰会。视频可以在 FreeBSD 项目的 YouTube 频道上看到
- 庆祝 2022 年 6 月 19 日的 FreeBSD 日，以及接下来的整个一周
- 我们获得了 7 月 30 日至 31 日在台湾举行的 COSCUP 之友级别的赞助
- 发布 FreeBSD 基金会 [2022 年春季更新](https://freebsdfoundation.org/news-and-events/newsletter/freebsd-foundation-spring-2022-update/)
- 新的博客文章
- [我们来谈谈基金会的资金问题](https://freebsdfoundation.org/blog/lets-talk-about-foundation-funding/)
- [新董事会成员访谈：Cat Allman](https://freebsdfoundation.org/blog/new-board-member-interview-cat-allman/)
- [欢迎 FreeBSD 的谷歌代码之夏参与者](https://freebsdfoundation.org/blog/welcome-freebsd-google-summer-of-code-participants/)
- [13.1 版本中的 FreeBSD 基金会工作](https://freebsdfoundation.org/blog/freebsd-foundation-work-in-the-13-1-release/)
- [基金会选举新的官员，采访即将离任的董事会成员](https://freebsdfoundation.org/blog/foundation-elects-new-officers-interviews-outgoing-board-members/)
- [帮助我们庆祝整个星期的 FreeBSD 日](https://freebsdfoundation.org/blog/help-us-celebrate-freebsd-day-all-week-long/)
- 新的和更新的如何操作和快速指南
  - [网络基础知识：WiFi 和蓝牙](https://freebsdfoundation.org/freebsd-project/resources/networking-basics-wifi-and-bluetooth/)
  - [FreeBSD 上的音频](https://freebsdfoundation.org/freebsd-project/resources/audio-on-freebsd/)
  - [用 VirtualBox 安装 FreeBSD (Mac/Windows)——视频指南](https://freebsdfoundation.org/freebsd/how-to-guides/installing-freebsd-with-virtualbox-video-guide/)
  - [FreeBSD 操作系统简介——视频指南](https://freebsdfoundation.org/freebsd-project/resources/an-introduction-to-the-freebsd-operating-system-video/)
  - [在 FreeBSD 上安装一个桌面环境——视频指南](https://freebsdfoundation.org/freebsd-project/resources/installing-a-desktop-environment-on-freebsd-video-guide/)
  - [在 FreeBSD 上安装一个 port——视频指南](https://freebsdfoundation.org/freebsd-project/resources/installing-a-port-on-freebsd-video-guide/)

我们通过出版专业的 FreeBSD 杂志来帮助世界了解 FreeBSD。正如我们之前提到的，FreeBSD 杂志现在是一份免费出版物。了解更多信息并访问最新的期刊：https://www.FreeBSDfoundation.org/journal/。

你可以在 https://www.FreeBSDfoundation.org/news-and-events/ 找到更多关于我们参加的活动和即将举行的活动。

#### 法律/FreeBSD 知识产权

基金会拥有 FreeBSD 的商标，保护这些商标是我们的责任。我们还为核心团队提供法律支持，以调查出现的问题。

进入 https://www.FreeBSDFoundation.org ,了解更多关于我们如何支持 FreeBSD 以及我们如何帮助你的信息。

---

### FreeBSD 发布工程团队

链接:

FreeBSD 13.1-RELEASE schedule 网址：https://www.freebsd.org/releases/13.1R/schedule/

FreeBSD 13.1-RELEASE 公告 网址：https://www.freebsd.org/releases/13.1R/announce/

FreeBSD 的发布 网址：https://download.freebsd.org/releases/ISO-IMAGES/

FreeBSD 的开发快照 网址：https://download.freebsd.org/snapshots/ISO-IMAGES/

联系:FreeBSD 发布工程团队，re@FreeBSD.org

FreeBSD 发布工程团队负责为 FreeBSD 的官方项目发布制定并发布发布计划，宣布代码冻结并维护相应的分支，以及其他事项。

在 2022 年的第二季度，发布工程团队完成了 13.1-RELEASE 周期的工作。这是 stable/13 的第二个版本分支。在整个发布周期中，发生了三次 BETA 构建和六次 RC（候选发布版）构建，将最终发布日期从 2022 年 4 月 21 日移至 2022 年 5 月 16 日，因为在最后一刻发现了一些问题。

我们感谢所有测试 13.1-RELEASE 的 FreeBSD 开发人员和贡献者，他们报告了问题，并 着周期的进展勤奋地进行了修改。

此外，在整个季度中，还为主分支、stable/13 和 stable/12 分支发布了几个开发快照版本。

赞助商：Rubicon Communications, LLC ("Netgate") 赞助商：FreeBSD 基金会

---

### 集群管理团队

链接：

集群管理小组成员 网址：https://www.freebsd.org/administration/#t-clusteradm

FreeBSD 集群管理团队的成员负责管理该项目所依赖的机器，以同步其分布式工作和通信。在这一季度，该团队进行了以下工作：

- 在澳大利亚悉尼安装了一个新的镜像，由 IX 澳大利亚公司托管
- 修复了 CI 集群的硬件故障
- 建立一个新的内部监测系统
- 定期进行集群范围内的软件升级
- 对 FreeBSD.org 用户账户的定期支持工作

正在进行中：

- 与 PowerPC 团队合作，改进软件包构建者、通用和参考机器。
- 计划硬件更新，并修复各站点的杂项故障
- 改善成套建筑的基础设施
- 审查服务 jail 和服务管理员的运作情况
- 与 doceng@ 合作，改善 https://www.freebsd.org 和 https://docs.freebsd.org 的部署。
- 改进网络服务架构
- 完善集群备份计划
- 完善日志分析系统

我们正在欧洲寻找一个额外的全镜像站点（五个服务器）。请看[通用镜像布局](https://wiki.freebsd.org/Teams/clusteradm/generic-mirror-layout)，以满足我们的需要。我们也欢迎提供额外的单服务器镜像（见[小镜像](https://wiki.freebsd.org/Teams/clusteradm/tiny-mirror)），特别是在欧洲。

---

### 持续集成

链接：

FreeBSD Jenkins Instance 网址：https://ci.FreeBSD.org

FreeBSD CI 软件存档 网址：https://artifact.ci.FreeBSD.org

FreeBSD Jenkins wiki 网址：https://wiki.freebsd.org/Jenkins Hosted CI wiki 网址：https://wiki.freebsd.org/HostedCI

第三方软件 CI 网址：https://wiki.freebsd.org/3rdPartySoftwareCI

与 freebsd-testing@ 相关的票据 网址：https://preview.tiny网址.com/y9maauwg

FreeBSD CI 存储库 网址：https://github.com/freebsd/freebsd-ci

dev-ci 邮件列表 网址：https://lists.freebsd.org/subscription/dev-ci

联系：Jenkins Admin jenkins-admin@FreeBSD.org

联系：Li-Wen Hsu lwhsu@FreeBSD.org

联系：[freebsd-testing 邮件列表](https://lists.freebsd.org/mailman/listinfo/freebsd-testing)

联系：IRC EFNet 平台上的 #freebsd-ci

FreeBSD CI 团队负责维护 FreeBSD 项目的持续集成系统。CI 系统检查提交的修改是否能够成功构建，然后对新构建的结果进行各种测试和分析。这些构建的工件被归档到工件服务器中，以备进一步测试和调试的需要。CI 团队成员检查失败的构建和不稳定的测试，并与该领域的专家合作，修复代码或调整测试基础设施。

在 2022 年的第二季度，我们继续与项目中的贡献者和开发者合作，以满足他们的测试需求，同时也与外部项目和公司保持合作，以改进他们的产品和 FreeBSD。

重要的已完成任务：

- 修正了 CI 集群的硬件故障问题

进行中的任务：

- 设计和实施提交前的 CI 构建和测试（以支持[工作流程工作组](https://gitlab.com/bsdimp/freebsd-workflow)的工作）
- 设计和实施 CI 集群的使用，以建立发布工程的工件。
- 测试和合并 [FreeBSD-ci repo](https://github.com/freebsd/freebsd-ci/pulls) 中的提交请求
- 简化贡献者和开发者的 CI/测试环境设置
- 设置 CI 阶段环境，并将实验性工作放在上面
- 整理 freebsd-ci 版本库中的脚本，为合并到 src 版本库做准备
- 更新 wiki 上的文件

正在进行或等待的任务：

- 收集和整理 [CI 任务和想法](https://hackmd.io/@FreeBSD-CI/freebsd-ci-todo)
- 为运行测试的虚拟客体设置公共网络接入
- 实施使用裸机硬件来运行测试套件
- 增加 drm port，针对 -CURRENT 构建测试
- 计划运行 ztest 测试
- 增加更多外部工具链相关的工作
- 提高硬件实验室的成熟度，增加更多测试用硬件
- 帮助更多的软件在其 CI 管道中获得 FreeBSD 支持（Wiki 页面:[3rdPartySoftwareCI](https://wiki.freebsd.org/3rdPartySoftwareCI), [HostedCI](https://wiki.freebsd.org/HostedCI)）
- 与托管 CI 供应商合作以获得更好的 FreeBSD 支持

更多的 WIP 信息请参见 [freebsd-testing@相关票据](https://preview.tiny网址.com/y9maauwg)，请不要犹豫，加入我们的努力吧!

赞助商：FreeBSD 基金会

---

### Ports

链接：

关于 FreeBSD ports 网址：https://www.FreeBSD.org/ports/

贡献 Port 的 网址：https://docs.freebsd.org/en/articles/contributing/#ports-contributing

FreeBSD Ports 监控 网址：http://portsmon.freebsd.org/

Ports 管理团队 网址：https://www.freebsd.org/portmgr/

Ports Tarball 网址：http://ftp.freebsd.org/pub/FreeBSD/ports/ports/

联系：René Ladan portmgr-secretary@FreeBSD.org

联系：FreeBSD Ports 管理团队 portmgr@FreeBSD.org

Ports 管理团队负责监督 Ports 的整体方向、建筑配套和人事事务。以下是上一季度发生的情况。

Port 的数量略高于 30,000。在上一季度，“main”分支有 151 个提交者提交了 9137 个代码，"2022Q2" 分支有 61 个提交者提交了 589 个代码。在写这篇文章的时候，有 2700 个开放 port 的 PR，其中 682 个是未分配的。与上一季度相比，提交活动略有减少，而 PR 的数量则保持不变。注意：Freshports 似乎大幅多计了。本季度的 port 数是以不同的方式得出的，与上一季度的 port 数没有可比性。

在上一季度，portmgr 欢迎 salvadore@ 的回归，但同时也因为缺乏活跃而与七个 port 提交者告别。

在两周一次的会议上，portmgr 讨论了以下主题。\* ca_root_nss 的未来 \* 基础系统提供某些 .pc 文件的可行性 \* 处理基础系统小版本升级时内核模块 port 不兼容问题的方法

经过开发人员的讨论，portmgr 决定授予所有文档和源码提交权限，以修复 Ports 树中任何与文档相关的错误，但不影响其功能。

以下是在 2022q2 期间对 Ports Tree 所做的修改： \* pkg 更新到了 1.18.3 版，Firefox 更新到了 102.0 版，Chromium 更新到了 103.0.50060.53 版 \* GCC、 Lazarus、 Python 和 Ruby 的默认版本分别更新为 11 (powerpcspe 保持 8 版)、 2.2.2、 3.9 和 3.0。\* 加入了两个新的 USES，gstreamer 用于支持基于 GStreamer 插件的 port，pytest 用于帮助使用 pytest 进行测试。

---

### 项目

跨越多个类别的项目，从内核和用户空间到 port 或外部项目。

### Linux 兼容层更新

联系：Dmitry Chagin [dchagin@FreeBSD.org](mailto:dchagin@FreeBSD.org) 联系：Edward Tomasz Napierala [trasz@FreeBSD.org](mailto:trasz@FreeBSD.org)

这个项目的目标是提高 FreeBSD 执行未经修改的 Linux 二进制文件的能力。目前特定的 Linux 应用程序的支持状态正在 Linux 应用程序状态 Wiki 页面上进行跟踪。

Y2k38 Linux 项目的实施已基本完成；所有 `'*_time64()'` 系统调用都已提交。

arm64 Linux 仿真层的状态与 amd64 Linux 仿真层的状态保持一致：即实现了 vDSO、机器依赖的 futexes、信号传递。

线程亲和性系统调用被修改以实现 Linux 语义。

总共修复了 50 多个错误；glibc-2.35 测试套件报告了不到 80 个失败的测试。

Linux 仿真层的所有修改都合并到了 stable/13 分支。

在 libsysdecode 和 kdump 中加入了对流行的 Linux 系统调用跟踪的初步支持。目前正在进行的工作是让追踪更多的系统调用发挥作用。

赞助商：EPSRC (Edward 的工作)

---

### FreeBSD 与 riscv64

链接:

golang 主页 网址：https://github.com/golang/go

FreeBSD riscv64 github repo 网址：https://github.com/MikaelUrankar/go/tree/freebsd\_riscv64

FreeBSD riscv64 golang 问题 网址：golang/go#53466

联系：Mikaël Urankar mikael@FreeBSD.org 联系：Dmitri Goutnik dmgk@FreeBSD.org

已经完成了将 go 移植到 FreeBSD riscv64 上的工作，它可以构建并通过所有 run.bash 测试，包括 cgo （在 QEMU 和 Unmatched 上测试）。在上游创建了一个拉动请求，该提案已被添加到提案项目的活动栏中，并将在每周的提案审查会议上被审查。

---

### 微软 HyperV 和 Azure 上的 FreeBSD

链接：

微软在 FreeBSD 上的 Azure WIKI 文章 网址：https://wiki.freebsd.org/MicrosoftAzure

微软在 FreeBSD 上的 HyperV WIKI 文章 网址：https://wiki.freebsd.org/HyperV

联系：Microsoft FreeBSD 集成服务团队 bsdic@microsoft.com

联系人：[freebsd- cloud 邮件列表](https://lists.freebsd.org/mailman/listinfo/freebsd-cloud)

联系：FreeBSD Azure 发布工程团队 releng-azure@FreeBSD.org

联系：Wei Hu whu@FreeBSD.org

联系：Li-Wen Hsu lwhsu@FreeBSD.org

Azure Marketplace 上的 [13.1-RELEASE 镜像](https://azuremarketplace.microsoft.com/marketplace/apps/thefreebsdfoundation.freebsd-13_1)已经发布。

正在进行的工作任务：

- 实现镜像构建和发布过程的自动化
- 构建并向 Azure 市场发布基于 ZFS 的镜像
  - 通过合并 [makefs(8)](https://www.freebsd.org/cgi/man.cgi?query=makefs&sektion=8&format=html) 和 [release(7)](https://www.freebsd.org/cgi/man.cgi?query=release&sektion=7&format=html) 的 ZFS 支持，taks 将受益。
    - https://reviews.freebsd.org/D23334
    - https://reviews.freebsd.org/D34426
    - https://reviews.freebsd.org/D35248
- 构建和发布 Hyper-V gen2 VM 镜像到 Azure Marketplace
- 被 https://bugs.freebsd.org/264267 阻拦

上述任务由 FreeBSD 基金会赞助，并由微软提供资源。

Wei Hu 和他在微软的同事正在从事由微软赞助的几项任务：

- 修复 Azure 中 Hyper-V gen2 VM 的启动问题
  - https://bugs.freebsd.org/264267
- 移植 Hyper-V 客户端以支持 arch64

开启的任务：

- 在 https://docs.microsoft.com 更新 FreeBSD 的相关文档
- 在 [Azure Pipelines](https://azure.microsoft.com/services/devops/pipelines/) 中支持 FreeBSD
- 将 [Azure 代理](https://www.freshports.org/sysutils/azure-agent) port 更新到最新版本
- [Azure 代理代理](https://github.com/Azure/WALinuxAgent/pull/1892)的上游本地修改

赞助商:微软提供了 Wei Hu 等人在微软的工作，以及其他方面的资源 赞助商：FreeBSD 基金会提供其他一切

---

### 用户空间

影响基础系统和其中程序的变化。

### 正在进行的关于 LLDB 多进程

链接：

Moritz Systems 项目简介网址：https://www.moritz.systems/blog/multiprocess-support-for-lldb/

进度报告 1 网址：https://www.moritz.systems/blog/implementing-non-stop-protocol-compatibility-in-lldb/

联系：Kamil Rytarowski kamil@moritz.systems 联系：Michał Górny mgorny@moritz.systems

根据上游的描述，“LLDB 是下一代高性能调试器。它是作为一组可重用的组件构建的，这些组件高度利用了更大的 LLVM 项目中的现有库，例如 Clang 表达式解析器和 LLVM 反汇编器。”

FreeBSD 在基本系统中包括 LLDB。之前赞助的项目改进了 LLDB，使其成为基础系统中可信的调试器，尽管它与 GNU GDB 的当代版本相比仍有一些限制。这个项目于 2022 年 4 月开始。它的目标是实现对多个进程同时调试的全面支持。

在项目开始时，LLDB 对多进程调试的支持非常有限。客户端的特点是支持通过维护与不同服务器实例的多个连接来同时调试多个独立进程。由于我们早期的工作，服务器能够处理 fork(2) 和 vfork(2) 调用，并且要么分离新分叉的子进程并继续跟踪父进程，要么分离父进程并跟踪子进程（等同于 GDB 的 `follow-fork-mode` 设置）。

一旦项目完成，LLDB 将能够同时追踪任意数量的分叉进程（相当于 GDB 的 `detach-on-fork off`）。将实现对 GDB 远程串行协议的多进程扩展的完全支持，以及对不停机扩展的部分支持，该扩展将使多个进程独立恢复和停止。

赞助商：FreeBSD 基金会

---

### 在 makefs(8) 中支持 ZFS

链接：

邮件列表 网址：https://lists.freebsd.org/archives/freebsd-hackers/2022-May/001128.html

makefs(8) 代码审查 网址：https://reviews.freebsd.org/D35248 release(7) 代码审查 网址：https://reviews.freebsd.org/D34426

联系：Mark Johnston [markj@FreeBSD.org](mailto:markj@FreeBSD.org)

makefs(8) 是一个源自 NetBSD 的工具，它完全在用户空间创建文件系统镜像。它是建立虚拟机（VM）镜像的一个有用的工具链组件，因为它不需要任何特殊的权限，不像格式化一个字符设备，挂载新的文件系统，并将文件复制到上面。此外，makefs 可以创建可重复的镜像，并旨在最大限度地减少资源消耗。目前，FreeBSD 的 makefs 可以创建 UFS、cd9660 和 msdos（FAT）文件系统镜像。

最近的工作使 makefs 能够创建 ZFS 镜像。makefs 的 ZFS 支持包括创建多个数据集的能力，每个数据集映射到输入文件层次中的一个目录。然而，许多 ZFS 功能并不被支持，因为该实现只提供了获得可重复的根池所需的功能。

后续工作使 release(7) 框架能够使用这个新的 makefs 扩展来创建基于 ZFS 的虚拟机和云镜像。

赞助商：FreeBSD 基金会

---

链接：

OpenSSH 网址：https://www.openssh.com/

OpenSSH 8.9 发布说明 网址：https://www.openssh.com/txt/release-8.9\[https://www.openssh.com/txt/release-8.9

OpenSSH 9.0 发布说明 网址：https://www.openssh.com/txt/release-9.0\[https://www.openssh.com/txt/release-9.0

联系：Ed Maste [emaste@freebsd.org](mailto:emaste@freebsd.org)

OpenSSH，一套远程登录和文件传输工具，在 FreeBSD 基本系统中从 8.8p1 版本更新到 9.0p1。

它还没有被合并到 stable/13 和 stable/12 分支。我预计将在七月进行。

注意: OpenSSH 9.0p1 将 scp(1) 从使用传统的 scp/rcp 协议改为默认使用 SFTP 协议。可以使用 -O 标志来代替以前的协议。

赞助商：FreeBSD 基金会

---

### pf 的最新状况

联系：Kristof Provost [kp@FreeBSD.org](mailto:kp@FreeBSD.org) 联系：Reid Linnemann [rlinnemann@netgate.com](mailto:rlinnemann@netgate.com)

#### 以太网

pf 最近增加了对以太网层过滤的支持。见 2021q2 pf_ethernet 报告。

从那时起，以太网层的过滤功能得到了扩展：

- anchor 支持
- 查看第三层头的能力，以便与源/目的 IP（v4/v6）地址匹配
- 对 IP 地址匹配的表格支持
- 直接派发到 dummynet
- 将以太网层的数据包直接传给 dummynet，而不是对数据包进行标记，并依靠第三层来处理 dummynet

#### Dummynet

pf 最近开始能够使用 dummynet 进行数据包调度。这种支持已经被扩展和改进，现在相信已经可以用于生产了。

一个值得注意的修正是，回复到/路由到的流量现在也要接受 dummynet 调度。

#### 最后匹配时间戳

pf 现在可以跟踪一个规则最后一次被匹配的时间。与 ipfw 规则的时间戳类似，这些时间戳在内部是以秒为单位的系统“墙上时钟时间”的 uint32_t 捕捉。(参见 time(9))。时间戳是 CPU 本地的，并且在每次规则或状态被匹配时更新。

赞助商：Rubicon Communications, LLC（"Netgate"）

---

### 内核

内核子系统/功能、驱动支持、文件系统等方面的更新。

### ENA FreeBSD 驱动程序更新

链接：

ENA readme 网址：https://github.com/amzn/amzn-drivers/blob/master/kernel/fbsd/ena/README.rst

联系：Michal Krawczyk [mk@semihalf.com](mailto:mk@semihalf.com) 联系：Dawid Gorecki [dgr@semihalf.com](mailto:dgr@semihalf.com) 联系：Marcin Wojtas Marcin Wojtas [mw@FreeBSD.org](mailto:mw@FreeBSD.org)

ENA（Elastic Network Adapter）是亚马逊网络服务（AWS）的虚拟化环境中可用的智能网卡。ENA 驱动程序支持多个发送和接收队列，可以处理高达 100Gb/s 的网络流量，这取决于它所使用的实例类型。

自上次更新以来已完成：

- ENA 驱动程序的上游版本 v2.5.0，其中包括：
  - 改进复位程序的处理
  - 延长定时器服务寿命，以便能够检测更多的硬件故障
  - 修复验证 Tx 请求 ID 的逻辑
  - 修复用于 Tx 的 IPv6 L4 校验和卸载处理
  - 在驱动中添加 NUMA awareness
- 对即将发布的 ENA 驱动（v2.6.0）进行内部审查，包括：
  - 进一步改进复位处理
  - 代码清理和风格修正
  - 记录的改进
  - 对 ENI 指标的检索进行修复

正在进行的工作：

- 测试即将发布的 ENA 驱动程序（v2.6.0）

赞助商：亚马逊

---

### 新的蓝牙 ® 配置守护程序：blued

链接： blued git 网址：https://git.lysator.liu.se/kempe/blued

联系：

邮件：kempe@lysator.liu.se

IRC: kempe@libera.chat

#### 简介

blued 工具提供了一个 IPC 接口，可以让非特权用户以用户友好的方式连接和使用蓝牙设备，并支持安全的简单配对（公钥加密，如果设备允许，还可以进行中间人保护）。

#### 什么是 blued？

blued 有三个部分：一个库、一个守护程序和一个命令行工具。库对蓝牙的细节进行抽象，守护程序管理蓝牙设备，命令行工具让用户列出或扫描蓝牙设备，与设备配对，或从一个设备上取消配对。命令行工具通过 UNIX 套接字与守护程序进行通信。

与 bthidd 和 hcsecd 不同，blued 支持安全的简单配对并提供 IPC。为了让 HID 设备工作，仍然需要 bthidd。我们提供了一个脚本来配对蓝牙设备，并对 bthidd 进行适当的配置，这样它就可以在没有用户干预的情况下工作和重新连接。

一旦配对被证明是稳定的，错误也被解决了，我们计划以某种方式将 bthidd 与 blued 集成，使 HID 设备在配对时自动开始工作，而不需要使用外部脚本。长期目标是提供一个图形化的用户界面，可以列出设备并提供简单的一键式设置来连接它们。

#### 安装和使用 blued v0.1

你需要在 `/etc/src` 中安装可选的 src 组件。

首先，[按照 FreeBSD 手册中的解释](https://docs.freebsd.org/en/books/handbook/advanced-networking/#network-bluetooth)，确保你已经加载了工作的蓝牙驱动。

为了测试 blued，请获取 [blued v0.1 的源代码](https://git.lysator.liu.se/kempe/blued/-/releases/v0.1)。然后编译它，用 kernel_patches 中的补丁修补你的 FreeBSD 内核，并按照 README 中的解释重新编译 hci 模块。

我主要在 FreeBSD 12.3 上测试了 blued，但在 13.1 上测试时，我的补丁应用得很干净。目前我还没有提供 port，但可以直接从构建目录中运行该软件，或者运行`make install`来安装所有需要的文件。blued 和 bluecontrol 都使用 capsicum，blued 可以被配置为无需 root 权限。

更多信息请参考 `README` 中的运行 blued 部分。

#### 帮助

**测试**

我只用自己的鼠标试过这个软件，并意识到一个单一的蓝牙设备的样本量是相当小的。我期待着问题的出现，同时也非常期待其他人的反馈!

如果出现问题，从 /var/log/debug.log 和 /var/log/messages 的输出，以及尝试配对时从 `hcidump -x` 得到的流量转储，将有助于故障排除。

**贡献**

如果你想参与代码并提交补丁，欢迎你[访问 Lysator 的 Git 上的仓库](https://git.lysator.liu.se/kempe/blued)

---

### OpenVPN DCO

链接：

D34340 网址：[D34340](https://reviews.freebsd.org/D34340)

OpenVPN 维基 网址：[OpenVPN wiki](https://community.openvpn.net/openvpn/wiki/DataChannelOffload)

联系：Kristof Provost [kp@FreeBSD.org](mailto:kp@FreeBSD.org)

OpenVPN DCO（或称数据通道卸载）将 OpenVPN 的数据包处理转移到内核中。

传统上，OpenVPN 使用 tun(4) 接口来传输和接收数据包。在这种设置下，收到的数据包由内核接收，传递给 OpenVPN 应用程序进行解密，然后再传回内核进行网络栈处理。这需要在内核和用户空间之间进行多次转换，自然会造成性能损失。

新的 if_ovpn OpenVPN DCO 卸载驱动完全在内核中执行加密/解密，提高了性能。

最初的性能测试显示，吞吐量从大约 660Mbit/s 提高到大约 2Gbit/s。

用户空间的 OpenVPN 代码也需要修改以使用新的 if_ovpn 卸载驱动。这预计将成为未来 2.6.0 版 OpenVPN 的一部分。

赞助商：Rubicon Communications, LLC (“Netgate”)

---

### 无线更新

链接：

Intel iwlwifi 状态 FreeBSD wiki 页面 网址：https://wiki.freebsd.org/WiFi/Iwlwifi

Realtek rtw89 状态 FreeBSD wiki 页面 网址：https://wiki.freebsd.org/WiFi/Rtw89

联系：Bjoern A. Zeeb [bz@FreeBSD.org](mailto:bz@FreeBSD.org)

整个项目旨在为目前使用 LinuxKPI 兼容代码的 FreeBSD 带来对较新芯片组的支持，该代码由本地 net80211 和内核代码支撑。此外，我们的目标是继续努力支持更新的无线标准。在第二季度，有 40 个提交进入了 FreeBSD CURRENT。随着越来越多的用户尝试多种驱动，支持时间也在增加。

早期版本的 Intel iwlwifi 衍生的无线驱动在 13.1-RELEASE 中发布了，这使得这项工作进入了第一个 FreeBSD 版本。此后，iwlwifi 驱动程序和固件又在 CURRENT 和 stable/13 中进行了更新，这是持续开发的一部分。与上游 Intel Linux 版本的驱动共享的文件中的变化现在不到 400 行。最近，一个长期存在的老式芯片组的问题（有希望）得到解决，允许支持 iwm(4) 的网卡在近三个月后再次与 iwlwifi(4) 一起工作。在今年年底之前，项目的主要重点将是让我们达到当代的速度。

4 月 1 日，使用与 iwlwifi 工作相同的 LinuxKPI 基础设施，Realtek 的 rtw88(4) 驱动被纳入了 CURRENT。由于 DMA 的问题，在接下来的几周里，一个解决方法被开发出来并放到了代码仓库上，因此用户不再需要修补内核。对于物理内存超过 4GB 的机器，该驱动仍然需要在 loader.conf 中设置一个调整项。这个调整项使得该驱动在六月被合并到了 stable/13，随后又在 CURRENT 和 stable/13 中进一步更新。随着基于 rtw88 的芯片组的 USB 部分被准备纳入 Linux，准备 FreeBSD 也能支持 USB 部分的工作已经开始（需要更多时间）。

在过去的几个月里，Realtek 的 rtw89 已经开始编译，在它能够在 URRENT 启用之前，仍然是一个稳定运行和关联的工作。

感谢所有用户的测试和反馈，耐心等待下一次的更新、错误修复，或者只是我的一个答复。和你们一起工作是一件非常愉快的事情! 继续向我发送错误报告，但请记住，你应该感谢 FreeBSD 基金会，因为它使大部分工作成为可能。

要了解最新的开发状况，请关注 freebsd-wireless 邮件列表 并查看 wiki 页面。

赞助商：FreeBSD 基金会

---

### 共享页地址随机化

链接：

[D35392](https://reviews.freebsd.org/D35392) [D35393](https://reviews.freebsd.org/D35393) [D35349](https://reviews.freebsd.org/D35349)

联系：Kornel Duleba [mindal@semihalf.com](mailto:mindal@semihalf.com)

联系：Marcin Wojtas [mw@FreeBSD.org](mailto:mw@FreeBSD.org)

共享页是一个 R/X 页，由 image activator 映射到每个进程中。它存储了 signal trampoline 以及其他元数据，例如实现用户空间定时器所需的信息。以前，它被映射在进程虚拟地址空间的顶部。随着上述变化，它的地址将被随机化。我们计划对所有架构的 64 位二进制文件默认开启该功能。目前，这些补丁正在审查中，等待批准。

赞助商：Stormshield

---

### 架构

更新特定平台的功能，并引入对新硬件平台的支持。

### 恩智浦 DPAA2 支持

链接：

[更改历史](https://github.com/mcusim/freebsd-src/commits/lx2160acex7-dev)

[代码](https://github.com/mcusim/freebsd-src/tree/lx2160acex7-dev/sys/dev/dpaa2)

联系：Dmitry Salychev [dsl@FreeBSD.org](mailto:dsl@FreeBSD.org)

联系：Bjoern A. Zeeb [bz@FreeBSD.org](mailto:bz@FreeBSD.org)

恩智浦的一些 SoC（LX2160A、LS1088A）配备了 [DPAA2](https://www.nxp.com/design/qoriq-developer-resources/second-generation-data-path-acceleration-architecture-dpaa2:DPAA2)，即第二代的数据路径加速架构。它允许动态配置和连接数据包处理“对象”（网络接口的 DPNI，媒体访问控制器的 DPMAC 等），以形成一个片上网络。

在上个季度，该驱动开始运行良好，足以用于 [SolidRun 的 Honeycomb LX2](https://solidrun.atlassian.net/wiki/spaces/developer/pages/197494288/HoneyComb+LX2+ClearFog+CX+LX2+Quick+Start+Guide)（ACPI 测试平台），Traverse Technologies 已经为（他们的）Ten64（用作 FDT 测试平台）制作了一个 [FreeBSD 预览](https://forum.traverse.com.au/t/freebsd-preview-for-ten64/173)。

该驱动仍在进行中，但已接近审查，以便将第一个版本放入代码库中，让大家从中受益。

WIP：

- FDT MDIO 支持。FreeBSD 目前缺乏对 SPF 部分的支持
- 驱动程序资源的去分配，以正确卸载 dpaa2.ko
- [错误修复](https://github.com/mcusim/freebsd-src/issues)和改进

TODO:

- 对 DPIO 和 DPNI 的处理器亲和性
- 缓存的内存支持的软件门户
- 缓解瓶颈
- 支持更多的硬件组件（DPSW、DCE 等）

赞助商：赤裸裸的热情 :)

赞助商：Traverse Technologies (提供 Ten64 HW 用于测试)

---

### 关于 arm64 及其他的中等规模的超级页

联系：Eliot H. Solomon [ehs3@rice.edu](mailto:ehs3@rice.edu) 联系：Alan L. Cox [alc@rice.edu](mailto:alc@rice.edu)

64 位 ARM 架构的页表描述符格式包含一个称为连续位的标志。这告诉 MMU，它可以缓存一组对齐的、物理上连续的 16 个页表条目，这些条目具有相同的权限和属性，只需使用一个 TLB 条目。

毗连位，以及概念上类似于 RISC-V 架构的 Svnapot 扩展，允许使用 64KB 的超级页。这些中等大小的超级页可以为较小的内存对象带来地址转换的速度，通常与更传统的 2 MiB 超级页相关。

这个项目的重点是为 FreeBSD 带来对中型超级页的支持。到目前为止，我们已经修改了 arm64 pmap 的代码，通过检测物理上连续的页表项并使用 Contiguous 位来自动利用 64 KiB 超级页。现在，我们正在努力调整内核的超级页保留模块，以支持 64 KiB 的保留，除了目前的 2 MiB 的保留之外。增加中等大小的预留将允许虚拟内存系统明确地分配符合超级页推广要求的内存块，而不是仅仅希望它们偶然出现。

我们的目标是以一种通用的方式来实现这一点，使其有可能指定多个任意的 2 次方预留尺寸，从而更容易利用其他架构上的硬件功能，如 Ryzen 的 PTE 凝聚，它可以透明地将 4 KiB 的页表条目组合并为中等大小的超级页。

赞助商：莱斯大学计算机科学系

---

### 文档

文档树、手册页或新的外部书籍/文件中值得注意的变化。

### 文档工程团队

链接：FreeBSD 文档项目

链接：为新的贡献者提供的 FreeBSD 文档项目入门手册

链接：文档工程团队

联系：FreeBSD Doceng 团队 [doceng@FreeBSD.org](mailto:doceng@FreeBSD.org)

doceng@ 团队是一个处理与 FreeBSD 文档工程相关的一些元项目问题的机构；更多信息请参见 [FreeBSD Doceng 团队章程](https://www.freebsd.org/internal/doceng/)。

在上个季度，Graham Perrin (grahamperrin@) 和 Pau Amma (pauamma@)，被授予文档提交权限。

有几个项目还在讨论中。

将网站和文档门户与项目的 GeoDNS 基础设施进行镜像。

如何处理文档中的商标。

从网站和文档门户中删除过时的翻译。

### Weblate 上的 FreeBSD 翻译

链接：在 Weblate 上翻译 FreeBSD 链接：FreeBSD Weblate 实例

2022 年第二季度状况

- 12 种语言
- 152 个注册用户（9 个新用户）

语种

- 中文（简体）(zh-cn)
- 中文（繁体）(zh-tw)
- 荷兰语 (nl)
- 法语(fr)
- 德语 (de)
- 印度尼西亚语 (id)
- 意大利语 (it)
- 挪威语 (nb-no)
- 波斯语 (fa-ir)
- 葡萄牙语 (pt-br)
- 西班牙文 (es)
- 土耳其语(tr)

我们要感谢每一个作出贡献、翻译或审阅文件的人。

同时，请在你的本地用户组中帮助推广这项工作，我们总是需要更多的志愿者。

### FreeBSD 网站改版——WebApps 工作组

联系：Sergio Carlavilla [carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)

负责创建新的 FreeBSD 文档门户和重新设计 FreeBSD 主网站及其组件的工作小组。FreeBSD 开发者可以在 FreeBSD Slack 频道 #wg-www21 上关注并加入该工作组。这项工作将分为四个阶段：

1.  重新设计文档门户

    创建一个新的设计，具有响应性和全局搜索功能。(完成)

2.  重新设计网络上的手册页面

    使用 mandoc 生成 HTML 页面的脚本。(工作正在进行中)

3.  重新设计网络上的“ports”页面

    创建应用门户的 port 脚本。(工作正在进行中)

4.  重新设计 FreeBSD 的主网站

    新的设计，响应性和暗色主题。(未开始)

---

### Ports

影响 Ports 的变化，无论是涉及大部分目录的全面变化，还是个别 Ports 本身的变化。

### FreeBSD 上的 KDE

链接：

KDE FreeBSD 网址：https://freebsd.kde.org/

KDE Community FreeBSD 网址：https://community.kde.org/FreeBSD

联系：Adriaan de Groot [kde@FreeBSD.org](mailto:kde@FreeBSD.org)

KDE on FreeBSD 项目将来自 KDE Community 的软件，以及依赖关系和相关软件打包到 FreeBSD ports 上。这些软件包括一个叫做 KDE Plasma 的完整桌面环境（适用于 X11 和 Wayland）和数百个可以在任何 FreeBSD 机器上使用的应用程序。

KDE 团队 (kde@) 也是 desktop@ 和 x11@ 的一部分，他们建立了软件栈，使 FreeBSD 成为漂亮的、可用于日常驱动的基于图形的桌面机器。下面的说明主要是描述 KDE 的 Ports，但也包括对整个桌面堆栈有意义的项目。

#### KDE 堆栈

KDE Gear 每季度发布一次，KDE Plasma 每月更新一次，KDE Frameworks 每月也有一个新版本。这些（大型）更新在其上游发布后不久就登陆，不单独列出。

- astro/kstars 最新版本 3.5.9。
- deskutils/grantleetheme 在 UPDATING 中得到了一个条目，因为这个 port 的安装结构发生了一些不寻常的变化。
- deskutils/kalendar 加入了 KDE Gear 版本。
- devel/okteta 更新了二进制（以及八进制和十六进制）数据查看器和编辑器。
- finance/kraft 需要对较新的 KDE 框架进行特定的构建修复。
- games/gcompris-qt 扩展了新版本，现在支持更多的图像格式（某些活动需要）。
- graphics/digikam 在构建过程中不再需要 SQL 服务器。
- graphics/krita 更新到了 5.0.5，可能是最后的 5.0 版本。
- math/labplot 在最近的版本中有大量的新功能，如果你需要任何类型的数据绘图，非常值得一看。
- net-im/ruqola 已经更新。这是一个 Qt 风格的 Rocket 聊天应用程序。
- www/falkon 加入了 KDE Gear 的发布。

#### 相关应用程序

- Archivers/quazip 被更新了。
- deskutils/semantik 已更新。
- 更新了 develop/py-qt5-pyqt，以便该 port 现在也能拉入 DBus。几乎所有桌面 Qt 应用程序都需要 DBus，包括那些用 Python 编写的应用程序。
- devel/qcoro 在某些 FreeBSD 版本上有构建问题，已解决。
- devel/qtcreator 随每个新版本的发布而更新。
- devel/qt5 在 ports 中更新了它的基础架构，这样它在卸载时就不会产生奇怪的错误信息。
- graphics/ksnip 和相关库已更新到最近的版本。
- Matrix 客户端 Nheko (net-im/nheko) 和 Neochat (net-im/neochat) 在发布和库升级之后进行了更新。
- 更新了 x11/rsibreak；有助于防止在写长的季度报告时受伤。

#### 其他方面

- devel/appstream 的更新支持更多的应用程序信息。
- 如果用户安装了多个 python3 Port 和 lang/python3，devel/cmake 更倾向于使用通用的 python3 而不是版本化的 python3。
- 更新了 devel/dbus。
- graphics/poppler 更新了若干次。
- graphics/ImageMagick (包括 6 和 7) 更新了若干次。
- multimedia/gstreamer 已更新。

---

### GCC：更新 GCC_DEFAULT 和其他改进

链接：

GCC 项目 网址：https://gcc.gnu.org

GCC 11 发布系列 网址：https://gcc.gnu.org/gcc-11/

联系：[toolchain@FreeBSD.org](mailto:toolchain@FreeBSD.org)

联系：Gerald Pfeifer [gerald@pfeifer.com](mailto:gerald@pfeifer.com)

联系：Lorenzo Salvadore [salvadore@FreeBSD.org](mailto:salvadore@FreeBSD.org)

联系：Lorenzo Salvadore Piotr Kubaj [pkubaj@FreeBSD.org](mailto:pkubaj@FreeBSD.org)

- salvadore@ 致力于将 Mk/bsd.default-versions.mk 中的 GCC_DEFAULT 从 10 升级到 11，根据 antoine@ 的 exp-runs 打开 bug 报告并修复了一些：非常感谢所有帮助这项工作的人。GCC_DEFAULT 从 GCC 10 到 GCC 11 的更新现在已经由 gerald@ 提交，并在下一个季度的分支中及时发生。https://bugs.freebsd.org/bugzilla/show\_bug.cgi?id=258378 pkubaj@ 通过引入一个默认启用的新选项，将 GCC 引导转换为使用 GCC 本身的链接时间优化，适用于 GCC 11 和更新版本。启用 LTO_BOOTSTRAP 进行构建需要大量的内存和时间。实际需要多少资源取决于你的配置 (例如，你是用 port 还是用 poudriere 构建？你的架构是什么？）。举个例子，一个用户报告说需要 5 GiB 的临时文件，而在 PR 265254 中，由于产生了过多的进程，估计需要大约 130 GB 的内存（也见 https://gcc.gnu.org/bugzilla/show\_bug.cgi?id=106328 ）。考虑禁用 LTO_BOOTSTRAP，改用 STANDARD_BOOTSTRAP（或者完全禁用 BOOTSTRAP），以防出现问题。
- pkubaj@ 还添加了 lang/gcc12 和 lang/gcc13-devel port，并将 lang/gcc9 更新到 9.5。
- 这三个改动仍然需要帮助，以便与上游的 GCC 一起工作（需要 src 专业知识，而不是 ports）。
- 上游的 lang/gcc11/patch-gets-no-more
- upstreaming lang/gcc11/patch-arm-unwind-cxx-support
- https://bugs.freebsd.org/bugzilla/show\_bug.cgi?id=256874

---

### Valgrind - 13.1/14.0 的大量错误修正和更新

链接：

Valgrind 主页 网址：https://www.valgrind.org/

Valgrind 新闻 网址：https://www.valgrind.org/docs/manual/dist.news.html

联系：Paul Floyd [pjfloyd@wanadoo.fr](mailto:pjfloyd@wanadoo.fr)

在过去的几个月里，FreeBSD 上的 Valgrind 已经进行了相当多的错误修正。特别是，i386 版本在很大程度上已经“赶上”了它的老大哥 amd64。

devel/valgrind-devel port 已经提升到 3.20.0.g20220612,1，其中包括以下所有的变化。如果你经常使用 Valgrind，请切换到 valgrind-devel。

以下是自 Valgrind 3.19.0 发布以来的变化列表（该版本是与 devel/valgrind port 一起使用的版本）。

- 如果 Valgrind 在保存系统调用的携带标志时有信号到达，则信号恢复不正确。
- 修正了从 ld 产生的 PT_LOADs 中读取 DWARF 调试信息的问题，版本 9 后的 ld 将 RW 段分成两部分，这主要影响到共享库（.so 文件）。
- 在 i386 上正确实现线程 GDTs 的管理，这限制了应用程序只能创建 8192 个线程
- 使“brk”的第一页对寻址无效
- 分析和清理回归测试套件，特别是调整 i386 的泄漏测试，使其不能检测到 ECX 中剩余指针可能造成的泄漏。
- 让 lldb 可以读取 coredumps。
- 改进 C 语言分配函数的 errno 设置。
- 修正用 llvm-devel (15.0.0) 建立 Valgrind 的问题。

对于 FreeBSD 13.1 / 14.0，有

- funlinkat, copy_file_range, swapoff, shm_open2 的系统调用包装器。
- 在 fcntl 中添加 K_INFO 处理程序
- 增加了对新的 auxv 条目的处理
- 为 DRD 和 Helgrind 增加了一些默认的抑制措施

现在有一个初始版本的 vgdb invoker 支持——这允许 vgdb 使用 ptrace 来强迫 valgrind 轮询 gdb 命令。这在 port 版本中还不能使用。

这并没有留下多少悬而未决的问题。我希望 14.0 和更新的 llvm 版本会继续需要支持。除此以外，还有

- 一些关于错误信息的小问题，以获得正确的源信息
- 更好的核心转储（低优先级）
- 为 Helgrind 处理 TLS（线程本地存储）（如果不是不可能的话，也很难）。

---

### FreeBSD 上的 Pantheon 桌面

链接：

基本操作系统网址：https://elementary.io

开发库 网址：https://codeberg.org/olivierd/freebsd-ports-elementary

联系：Olivier Duchateau [duchateau.olivier@gmail.com](mailto:duchateau.olivier@gmail.com)

Pantheon 桌面环境是为 elementary OS 设计的。它建立在 GNOME 技术（如 Mutter、GNOME Shell、GTK 3 和 4）之上，并以 Vala 语言编写。

其目标是为用户提供一个新的桌面。有些功能没有得到很好的支持，但我们可以有完整的会话。

仓库包含 Mk/Uses 框架 elementary.mk，官方应用程序，以及依赖 x11-toolkits/granite 的策划的 port（总共 56 个新 port）。

我已经提交了几个补丁，特别是：

- x11-toolkits/granite7
- devel/libgee 更新到 0.20.5 [bug #262893](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=262893)
- sysutils/bamf 更新至 0.5.6 [bug #264203](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=264203)

开放任务

- 增加对用户设置的支持（这是非常以 Ubuntu 为中心的）。
- 完成移植 wingpanel-indicator-power（电源管理）。

---

### 英特尔的 igt-gpu-tools 的完整功能移植

链接：

FreeBSD Wiki 项目页面 网址：https://wiki.freebsd.org/SummerOfCode2022Projects/ImprovingTheLinuxKPICompatibilityLayerForTheFreeBSDGraphicsStack

状态报告 网址：https://cdaemon.com/tags/gsoc2022

联系：Jake Freeland [jfree@freebsd.org](mailto:jfree@freebsd.org)

Intel 的 igt-gpu-tools 是 Linux 上 drm 驱动的一个通用测试套件。igt-gpu-tools 套件被分成针对 kms、内存管理和命令提交的测试和工具。该工具提供了详细的报告，以便透明地跟踪内核变化，并对现代 drm 驱动进行有效的调试。

将该项目移植到 FreeBSD 上可以为 FreeBSD 的 LinuxKPI 驱动的 drm 驱动的未来版本带来更大的稳定性。一个合适的 kms 驱动的测试套件也可以增加代码输出，使 FreeBSD 的桌面体验与 Linux 代码库同步。

该项目于 2022 年 6 月 13 日在 FreeBSD 的谷歌代码之夏计划下正式启动。我改编的代码可以在删除非 FreeBSD 兼容片段后进行编译。我们的计划是以符合 POSIX 的方式重新实现这些被剥离的组件。

值得注意的不兼容代码包括：debugfs，libkmod，libprocps，Linux 性能事件，和 Linux userfaultfd。如果你愿意协助将 libkmod 或 libprocps 移植到 ports 中，请不要犹豫，与我联系。

当 FreeBSD 兼容代码完成后，我将在 FreeBSD 14.0-CURRENT 上使用一系列图形处理器运行修改后的 igt 测试。如果一切顺利，这个项目的 diff 将被提交到 ports 中。

赞助商：谷歌代码之夏

## FreeBSD 13.1 发行说明

> 原文链接 [https://www.freebsd.org/releases/13.1R/relnotes/](https://www.freebsd.org/releases/13.1R/relnotes/)

### 摘要

FreeBSD 13.1-RELEASE 的发行说明包含了在 13-STABLE 开发线上对 FreeBSD 基本系统所做修改的摘要。这份文件列出了自上次发布以来所发布的相关安全公告，以及对 FreeBSD 内核和用户空间的重大修改。同时还介绍了一些关于升级的简要说明。

### 简介

这份文件包含了 FreeBSD 13.1-RELEASE 的发行说明。它描述了 FreeBSD 最近增加、改变或删除的功能。它还提供了一些关于从以前版本的 FreeBSD 升级的说明。

这些发行说明所适用的发行版，代表了自 13-STABLE 创建以来沿 13-STABLE 开发分支的最新进展。有关这个分支的预编译二进制发行版的信息，可以在 https://www.FreeBSD.org/releases/ 找到。

这些发行说明所适用的发行版本代表了 13-STABLE 开发分支中介于 13.0-RELEASE 和未来的 13.2-RELEASE 之间的一个点。关于这个分支的预编译二进制发行版的信息，可以在 https://www.FreeBSD.org/releases/ 找到。

这个 FreeBSD 13.1-RELEASE 的发行版是一个发布版。它可以在 https://www.FreeBSD.org/releases/ 或其任何一个镜像中找到。关于获得这个(或其他) FreeBSD 发行版的更多信息，可以在 FreeBSD 手册的附录中找到。

我们鼓励所有用户在安装 FreeBSD 之前参考发行勘误表。勘误表文件会根据发布周期晚期或发布后发现的“迟发”信息进行更新。通常情况下，它包括已知的错误，安全公告，以及对文档的修正。FreeBSD 13.1-RELEASE 的勘误表的最新版本可以在 FreeBSD 网站上找到。

这份文件描述了自 13.0-RELEASE 以来 FreeBSD 中最容易被用户看到的新功能或变化。一般来说，这里描述的变化都是 13-STABLE 分支所特有的，除非特别标注为合并的特性。

典型的发布说明记录了在 13.0-RELEASE 之后发布的安全公告，新的驱动或硬件支持，新的命令或选项，主要的错误修正，或贡献的软件升级。他们也可能列出主要的 port/包的变化或发布工程实践。显然，发行说明不可能列出 FreeBSD 在不同版本之间的每一个变化； 这份文件主要关注安全公告、 用户可见的变化，以及主要的架构改进。

### 从以前的 FreeBSD 版本升级

使用 freebsd-update(8) 工具可以在 RELEASE 版本 (以及各种安全分支的快照) 之间进行二进制升级。二进制升级过程将更新未修改的用户空间工具，以及作为官方 FreeBSD 发行版一部分的未修改的 GENERIC 内核。freebsd-update(8) 工具要求被升级的主机有互联网连接。

根据 /usr/src/UPDATING 中的说明，可以支持基于源代码的升级 (那些基于从源代码重新编译 FreeBSD 基本系统的升级)。

所有 powerpc 架构的用户，在成功安装内核和 world 之后，需要手动运行 `kldxref /boot/kernel`。

> **只有在备份了所有数据和配置文件之后，才能尝试升级 FreeBSD。**

> **升级之后，sshd (来自 OpenSSH 8.8p1) 将不接受新的连接，直到它被重新启动。在安装了新的用户空间之后，要么重新启动(按照源码升级程序中的规定)，要么执行 service sshd 重启。**

### 用户空间

本节涵盖了对用户空间应用程序、贡献的软件和系统实用程序的更改和添加。

#### 用户空间配置的变化

在 /etc/defaults/rc.conf 中的 rtsol(8) 和 rtsold(8) 默认加入了 `-i` 标志，a0fc5094bf4c (由 https://www.patreon.com/cperciva 赞助)

用户空间应用程序的变化 在 rtsol(8) 和 rtsold(8) 中加入了 `-i` 选项，以禁用零到一秒之间的随机延迟，从而加快了启动过程。8056b73ea163 (由 https://www.patreon.com/cperciva 赞助)

对于 64 位架构，基本系统在构建时默认启用了位置独立可执行文件 (PIE) 支持。你可以使用 `WITHOUT_PIE` 参数来禁用它。这需要一个干净的构建环境。396e9f259d96

有一个新的 zfskeys rc(8) 服务脚本，它允许在启动时自动解密用 ZFS 本地加密的 ZFS 数据集。请参阅 rc.conf(5) 手册以了解更多信息。33ff39796ffe, 8719e8a951b7 (由 Modirum 和 Klara Inc.赞助)

bhyve(8)中的 NVMe 模拟已经升级到 NVMe 规范的 1.4 版本，b7a2cf0d9102 - eae02d959363

bhyve(8) 中针对大型 IO 的 NVMe iovec 结构已被修复。这个问题是由 Rocky Linux 8.4 中包含的 UEFI 驱动程序暴露的。

为巴西葡萄牙语 ABNT2 键盘增加了额外的 Alt Gr 映射。310623908c20

chroot 工具现在支持非特权操作了，chroot(8) 程序现在有了 `-n` 选项来启用它。460b4b550dc9 (由 EPSRC 赞助)

对 CAM 库进行了修改，以便在解析设备名称之前对其使用 realpath(3)，这使得诸如 camcontrol(8) 和 smartctl(8) 等工具在使用符号链接时能够更加友好，e32acf95ea25

md5sum(1) 和类似的消息加密程序与 Linux 上的程序兼容，如果程序名称以 sum 结尾，则让相应的 BSD 程序以 `-r` 选项运行，c0d5665be0dc (由 Netflix 赞助)

默认情况下，svnlite(1) 在联编过程中被禁用，a4f99b3c2384

mpsutil(8) 扩展到了显示适配器信息和控制 NCQ。395bc3598b47

使用 camcontrol(8) 将固件下载到设备后出现的问题，通过在固件下载后强制重新扫描 LUN 得到了修复。327da43602cc (由 Netflix 赞助)

在 bsdinstall(8) 中为变量磁盘名称的脚本分区编辑器增加了一种新模式。如果磁盘参数 DEFAULT 被设置为代替实际的设备名称，或没有为 PARTITIONS 参数指定磁盘，则安装程序将遵循自动分区模式中使用的逻辑，即如果有几个磁盘，它将为其中一个提供选择对话框，或在只有一个磁盘时自动选择。这简化了为具有不同磁盘名称的硬件或虚拟机创建全自动安装媒体的工作。5ec4eb443e81

### 贡献的软件

在所有 powerpc 架构上都启用了 LLDB 的构建，cb1bee9bd34

一个 True Awk 已经更新到了上游的最新版本 (20210215)。除了一个补丁之外，所有的 FreeBSD 补丁现在都已经被上传到了上游或被抛弃了。值得注意的变化包括：

- 区域划分不再用于范围
- 修复了各种错误
- 与 gawk 和 mawk 有更好的兼容性

剩下的一个 FreeBSD 变化，可能会在 FreeBSD 14 中被删除，就是我们仍然允许以`0x`为前缀的十六进制数字被解析和解释为十六进制数字，而所有其他 awk（现在包括 One True Awk）都将它们解释为 0，这与 awk 的历史行为一致。

zlib 升级到了 1.2.12 版。

libarchive 升级到了 3.6.0 版，在即将发布的补丁级别中增加了错误和安全修复。发布说明可以在 https://github.com/libarchive/libarchive/releases 找到。

ssh 软件包已经更新到 OpenSSH v8.8p1，包括安全更新和错误修复。其他的更新包括这些变化。

ssh(1)。当提示是否记录一个新的主机密钥时，接受该密钥的指纹作为"Yes"的同义词。

ssh-keygen(1)。当作为 CA 并用 RSA 密钥签署证书时，默认使用 rsa-sha2-512 签名算法。

ssh(1): 默认启用 UpdateHostkeys，但需要满足一些保守的前提条件。

scp(1)。远程拷贝到远程的行为 (例如 scp host-a:/path host-b:) 被修改为默认通过本地主机传输。

scp(1) 实验性地支持使用 SFTP 协议进行传输，以取代传统上使用的古老的 SCP/RCP 协议。

在 ssh 中启用了对 FIDO/U2F 硬件认证器的使用，并使用了新的公钥类型 ecdsa-sk 和 ed25519-sk 以及相应的证书类型。对 FIDO/U2F 的支持在 https://www.openssh.com/txt/release-8.2 中有所描述，a613d68fff9a (由 FreeBSD 基金会 赞助)

### 运行时库和 API

在 powerpc、powerpc64 和 powerpc64le 上增加了 OpenSSL 的汇编优化代码，ce35a3bc852

修复了对加速 ARMv7 和 ARM64 的加密操作的 CPU 特性的检测，大大加快了 aes-256-gcm 和 sha256 的速度。32a2fed6e71f（由 Ampere Computing LLC 和 Klara Inc.赞助）

在 riscv64 和 riscv64sf 上启用了构建 ASAN 和 UBSAN 库。8c56b338da7

OFED 库现已在 riscv64 和 riscv64sf 上构建。2b978245733

OPENMP 库现在已在 riscv64 和 riscv64sf 上构建，aaf56e35569

### 内核

本节涵盖了对内核配置、系统调校和系统控制参数的改变，这些改变没有其他分类。

内核的一般变化 powerpc64 上串行控制台的输出损坏已经被修复。

更改了 CAS 以支持 Radix MMU。

在使用 TCG 的 QEMU 上运行启用了 HPT 超级页的 FreeBSD，在 powerpc64(le) 上得到了修正。

在 powerpc64(le) 上的 pmap_mincore 增加了对超级缓存的支持。32b50b8520d

在 arm64 上为 32 位 ARM 二进制文件添加了 HWCAP/HWCAP2 辅助参数支持。这修正了在 COMPAT32 仿真环境下 golang 的构建/运行。28e22482279f (由 Rubicon Communications, LLC (`Netgate`)赞助)

### 设备和驱动

本节涵盖了自 13.0-RELEASE 以来对设备和设备驱动的变化和补充。

#### 设备驱动程序

igc(4) 驱动程序是为英特尔 I225 以太网控制器引入的。这个控制器支持 2.5G/1G/100Mb/10Mb 的速度，并允许 tx/rx 校验和卸载、 TSO、 LRO 和多队列操作，d7388d33b4dd (由 Rubicon Communications, LLC (`Netgate`) 赞助)

在 powerpc64(le) 的启动过程中，增加了对带有 AST2500 的 VGA/HDMI 控制台的修复，c41d129485e

在 virtio(4) 中的大 endian 目标上修复了 PCI 通用读/写功能。7e583075a41, 8d589845881

在 mpr(4) 中加入了对大 endian 的支持。7d45bf699dc, 2954aedb8e5, c80a1c1072d

减少了最大 I/O 大小，以避免 aacraid(4) 中的 DMA 问题。572e3575dba

修正了一个阻止使用 virtio_random(8) 的虚拟用户关闭或重启的 bug，fa67c45842bb

ice(4) 驱动程序已经更新到了 1.34.2-k，增加了固件日志和初始 DCB 支持，a0cdf45ea1d1 (由 Intel 公司赞助)

新增了 mgb(4) 网络接口驱动程序，它支持带有 PHY 的 Microchip 设备 LAN7430 PCIe 千兆以太网控制器和带有 RGMII 接口的 LAN7431 PCIe 千兆以太网控制器。e0262ffbc6ae (由 FreeBSD 基金会赞助)

新增了对 cdce(4) 设备的链接状态、 媒体和 VLAN MTU 的支持。973fb85188ea

新增了 iwlwifi(4) 驱动程序和 LinuxKPI 802.11 兼容性层，以补充 iwm(4) 对较新的 Intel 无线芯片组的支持。(由 FreeBSD 基金会 赞助)

当内核被配置为 MMCCAM 选项时，内核崩溃转储现在可以通过 dwmmc 控制器保存在 SD 卡和 eMMC 模块上了。79c3478e76c3

当内核被配置为 MMCCAM 选项时，现在可以使用 sdhci 控制器在 SD 卡上保存内核崩溃数据。8934d3e7b9b9

#### 支持的平台

增加了对 HiFive Unmatched RISC-V 板的支持。

### 存储系统

本节涵盖了对文件系统和其他存储子系统（包括本地和网络）的改变和补充。

#### 一般存储

ZFS 的变化 ZFS 已经升级到 OpenZFS 2.1.4 版本。OpenZFS 的发行说明可以在 https://github.com/openzfs/zfs/releases 找到。

#### NFS 的变化

两个新的守护进程 rpc.tlsclntd(8) 和 rpc.tlsservd(8)，现在已经默认在 amd64 和 arm64 上建立了。它们提供了对 NFS-over-TLS 的支持，这在题为“实现远程过程调用默认加密”的互联网草案中有所描述。这些守护进程是在指定 WITH_OPENSSL_KTLS 的情况下建立的。它们使用 KTLS 来加密/解密所有的 NFS RPC 消息流量，并通过 X.509 证书提供可选的机器身份验证。2c76eebca71b 59f6f5e23c1a

用于 NFSv4 挂载的默认次要版本已被修改为 NFSv4 服务器支持的最高次要版本。这个默认值可以通过使用 minorversion mount 选项来覆盖。8a04edfdcbd2

增加了一个新的 NFSv4.1/4.2 挂载选项 nconnect，可以用来指定挂载时使用的 TCP 连接数，最多为 16 个。第一个（默认）TCP 连接将被用于所有由小型 RPC 消息组成的 RPC。由大型 RPC 消息组成的 RPC(Read/Readdir/ReaddirPlus/Write)将以轮流方式在其他 TCP 连接上发送。如果 NFS 客户端或 NFS 服务器有多个网络接口聚合在一起，或者有一个使用多个队列的网络接口，这可以提高挂载的 NFS 性能。9ec7dbf46b0a

增加了一个名为`vfs.nfsd.srvmaxio`的 sysctl 设置项，可以用来将 NFS 服务器的最大 I/O 大小从 128Kbytes 增加到 2 的任何幂数，直至 1Mbyte。它只能在 nfsd 线程未运行时进行设置，并且通常需要将 kern.ipc.maxsockbuf 增加到至少是首次尝试设置 `vfs.nfsd.srvmaxio` 时生成的控制台日志消息所建议的值。9fb6e613373c

#### UFS 更改

继 5cc52631b3b8 之后，fsck_ffs(8) 在 preen 模式下对后台 fsck 不起作用，在该模式下 UFS 被调整为没有软更新日志的软更新。修正: fb2feceac34c

### 引导加载器的变化

本节涵盖了启动加载器、启动菜单以及其他与启动相关的变化。

#### 引导加载器的变化

UEFI 启动对 amd64 进行了改进。装载器检测加载的内核是否可以处理原地暂存区（非复制模式）。默认是 copy_staging auto。自动检测可以被覆盖，例如：在 copy_staging enable 下，加载器将无条件地把暂存区复制到 2M，而不管内核的能力如何。另外，增长暂存区的代码更加健壮；为了增长，不再需要手工调整和重新编译加载器。(由 FreeBSD 基金会赞助)

boot1 和 loader 在 powerpc64le 上得到了修正。8a62b07bce7

### 其他启动方面的改动

对 loader(8)、 nvme(4)、 random(4)、 rtsold(8) 和 x86 时钟校准进行了性能改进，这使得系统启动时间明显加快了。EC2 平台上的配置变化提供了额外的好处，使 13.1-RELEASE 的启动速度是 13.0-RELEASE 的两倍以上。(由 https://www.patreon.com/cperciva 赞助)

EC2 镜像现在被默认构建为使用 UEFI 而不是传统 BIOS 启动。请注意，基于 Xen 的 EC2 实例或“裸机” EC2 实例不支持 UEFI。65f22ccf8247 (由 https://www.patreon.com/cperciva 赞助)

增加了对在 AWS 系统管理器参数库中记录 EC2 AMI Ids 的支持。FreeBSD 将使用公共前缀 `/aws/service/freebsd`，导致参数名称看起来像`/aws/service/freebsd/amd64/base/ufs/13.1/RELEASE`。242d1c32e42c (Sponsored by https://www.patreon.com/cperciva)

### 联网

这一节说明了影响 FreeBSD 网络的变化。

#### 一般网络

对 IPv4 (sub) net (host 0) 上的最低地址的处理方式进行了修改，使得除非这个地址被设置为广播地址，否则数据包不会以广播方式发送。这使得最低的地址对主机来说是可用的。旧的行为可以通过 `net.inet.ip.broadcast_lowest` sysctl 来恢复。请参阅 https://datatracker.ietf.org/doc/draft-schoen-intarea-unicast-lowest-address/ 了解背景信息。3ee882bf21af

## 关于未来 FreeBSD 发行版的一般说明

### 默认 CPUTYPE 的变化

从 FreeBSD-13.0 开始，i386 架构的默认 CPUTYPE 将从 486 变为 686。

这意味着，在默认情况下，所生产的二进制文件将需要一个 686 级的 CPU，包括但不限于由 FreeBSD 发行工程团队提供的二进制文件。FreeBSD 13.0 将继续支持更老的 CPU，然而需要这一功能的用户需要建立自己的官方支持版本。

由于 i486 和 i586 CPU 的主要用途一般是在嵌入式市场，一般最终用户的影响预计是最小的，因为采用这些 CPU 类型的新硬件早已淡出，而且据统计，这些系统的大部分部署基础已经接近退休年龄了。

这一变化有几个因素被考虑在内。例如，i486 没有 64 位原子，虽然它们可以在内核中被模拟，但不能在用户空间被模拟。此外，32 位的 amd64 库从一开始就是 i686 的。

由于大部分的 32 位测试是由开发人员在 64 位硬件上使用 lib32 库，并在内核中使用 `COMPAT_FREEBSD32` 选项来完成，所以这种改变可以确保更好的覆盖率和用户体验。这也与大多数 Linux® 发行版已经做了相当长一段时间的工作相一致。

预计这将是 i386 中默认 CPUTYPE 的最后一次改变。

> **这一变化并不影响 FreeBSD 12.x 系列的发布。**

## FreeBSD 13.2 发行说明

> 原文链接 [https://www.freebsd.org/releases/13.1R/relnotes/](https://www.freebsd.org/releases/13.2R/relnotes/)

### 摘要

FreeBSD 13.2-RELEASE 的发行说明包含了在 13-STABLE 开发线上对 FreeBSD 基本系统所做修改的摘要。这份文件列出了自上次发布以来所发布的相关安全公告， 以及对 FreeBSD 内核和用户区的重大修改。同时还介绍了一些关于升级的简要说明。

### 简介

这份文件包含了 FreeBSD 13.2-RELEASE 的发行说明。它说明了 FreeBSD 最近新增、变化或删除的功能。它还提供了一些关于从旧版 FreeBSD 的升级说明。

这些发行说明所适用的发行版， 代表了自 13-STABLE 创建以来沿 13-STABLE 开发分支的最新进展。有关这个分支的预编译二进制发行版的信息， 可以在 [https://www.FreeBSD.org/releases/](https://www.freebsd.org/releases/) 找到。

这些发行说明所适用的发行版本代表了 13-STABLE 开发分支中介于 13.1-RELEASE 和日后 13.3-RELEASE 之间的一个点。有关这个分支的预编译二进制发行版的信息，可以在 [https://www.FreeBSD.org/releases/](https://www.freebsd.org/releases/) 找到。

这个 FreeBSD 13.2-RELEASE 的发行版是一个 RELEASE。它可以在 [https://www.FreeBSD.org/releases/](https://www.freebsd.org/releases/) 或其任何一个镜像中找到。关于获得这个(或其他) FreeBSD 发行版的更多信息，可以在 FreeBSD 手册的附录中找到。

我们鼓励所有用户在安装 FreeBSD 之前参考发行勘误表。勘误表文件会根据发布周期晚期或发布后发现的“迟发”信息进行更新。通常情况下， 它包括已知的错误， 安全建议， 以及对文档的修正。FreeBSD 13.2-RELEASE 的勘误表的最新版本可以在 FreeBSD 网站上找到。

这份文件描述了自 13.1-RELEASE 以来 FreeBSD 中最容易被用户看到的新功能或变化。一般来说， 这里描述的变化都是 13-STABLE 分支所特有的， 除非特别标注为合并的特性。

典型的发布说明记录了在 13.1-RELEASE 之后发布的安全公告， 新的驱动或硬件支持，新的命令或选项，主要的错误修正，或贡献的软件升级。它们也可能列出主要的 port/包的变化或发布工程实践。显然，发行说明不可能列出 FreeBSD 在不同版本之间的每一个变化；这份文件主要关注安全公告、用户可见的变化， 以及主要的架构改进。

### 从旧版 FreeBSD 升级

使用 freebsd-update(8) 工具可以在 RELEASE 版本 (以及各种安全分支的快照) 之间进行二进制升级。二进制升级过程将更新未修改的用户区工具， 以及作为官方 FreeBSD 发行版一部分的未修改的 GENERIC 内核。freebsd-update(8) 工具要求被升级的主机有互联网连接。

根据 /usr/src/UPDATING 中的说明，可以支持基于源代码的升级 (那些基于从源代码重新编译的 FreeBSD 基本系统)。

所有 PowerPC 架构的用户，在成功安装内核和 world 之后，必须手动运行 `kldxref /boot/kernel`。

> _只有在备份了 **所有的** 数据和配置文件之后，才可以尝试升级 FreeBSD。_

> _在安装了新的用户级软件之后，运行的守护程序仍然是以前的版本。在通过第二次调用 freebsd-update 来安装用户级组件后，或者通过 `installworld` 从源代码升级后，系统应该重新启动，以便用新的软件启动一切。例如，旧版本的 sshd 在安装了新的 /usr/sbin/sshd 后，无法正确处理传入的连接；重启后会启动新的 sshd 和其他守护程序。_

### 用户空间

这部分介绍了一些对用户应用程序、贡献软件和系统工具的更改和添加。

- 在用户配置更改方面，growfs(7) 的启动脚本现在可以在扩展根分区的同时添加交换分区（如果之前没有交换分区）。这在 SD 卡上使用 RAW 镜像安装系统时非常有用。新增了一个 rc.conf(5) 变量——growfs_swap_size，可以在需要时控制添加交换分区的大小。详情请参考 growfs(7)。
- 新增了一个 RC 脚本 zpoolreguid，可为一个或多个 zpool 分配新的 GUID，这在共享数据集的虚拟化环境中非常有用。
- hostid 启动脚本现在可以在没有 /etc/hostid 文件和来自硬件的有效 UUID 的情况下生成一个随机的（第 4 版）的 UUID。此外，如果没有 /etc/machine-id 文件，hostid_save 脚本将在 /etc/machine-id 中存储一个紧凑版本的 hostid（不带连字符）。该文件被诸如 GLib 之类的库使用。
- 现在可以使用 defaultrouter_fibN 和 ipv6_defaultrouter_fibN rc.conf(5) 变量为非主要的 FIB 添加默认路由。 （由 ScaleEngine Inc. 赞助）

以下是一些常用的用户应用程序改进:

- 工具 bhyve(8) 现在支持 virtio-input 设备仿真。这将用于向客户机注入键盘/鼠标输入事件。命令行语法为: `-s <slot>,virtio-input,/dev/input/eventX`。
- 工具 kdump(1) 现在支持解码 Linux 系统调用。
- 工具 killall(1) 现在允许使用语法 `-t pts/N` 向具有其控制终端在 pts(4) 上的进程发送信号。
- 添加了软件 nproc(1)，与同名的 Linux 程序兼容。
- 软件 timeout(1) 已从 /usr/bin 移动到 /bin。
- 软件 pciconf(8) 添加了对 ACS 解码扩展功能的支持。(由 Chelsio Communications 赞助)
- 软件 procstat(1) 现在可以使用新添加的 advlock 命令打印关于文件上的 advisory locks 的信息。
- pwd_mkdb(8) 不再将 /etc/master.passwd 中的注释复制到 /etc/passwd。
- ppp(8) 的 MSS clamp 已得到改进。
- prometheus_sysctl_exporter(8) 中的指标别名已更改，以避免由于度量名称冲突而混淆 Prometheus 服务器。tcp_log_bucket UMA 区已重命名为 tcp_log_id_bucket，并且 tcp_log_node 已重命名为 tcp_log_id_node 以保持一致性。不再导出带有描述中的（LEGACY）的 Sysctl 变量，这些变量由已被其他变量替换的 ZFS sysctl 使用，其中许多变量别名为相同的 Prometheus 度量名称(例如 vfs.zfs.arc_max 和 vfs.zfs.arc.max)。(由 Axcient 赞助)
- uuidgen(1)实用程序具有一个新选项 `-r`，可以生成一个随机的 UUID，版本为 4。
- 在由 inetd(8) 调用时，`ctlstat -P` 现在会生成适合于将其摄入 Prometheus 的输出；请参阅 ctlstat(8)。(由 Axcient 赞助)

以下是一些软件的升级信息：

- 软件 bc 已经升级到了 6.2.4 版本，由 Gavin Howard 维护。
- 软件 expat (libbsdxml) 已经升级到了 2.5.0 版本。
- 软件 file 已经升级到了 5.43 版本。
- 软件 less 已经升级到了 608 版本。
- 软件 libarchive 已经升级到了 3.6.2 版本，并进行了多项可靠性修复。请参阅发行说明：[https://github.com/libarchive/libarchive/releases](https://github.com/libarchive/libarchive/releases)。
- 软件 libedit 已经升级到了 2022-04-11 版本。
- LLVM 和 clang 编译器已经升级到了 14.0.5 版本。
- 现在在 powerpc64 和其它架构上启用了支持的 LLVM sanitizer。
- 软件 mandoc 已经升级到了 1.14.6 版本。
- 软件 OpenSSH 已经升级到了 9.2p1 版本。
- 软件 OpenSSL 已经升级到了 1.1.1t 版本。
- 软件 sendmail 已经升级到了 8.17.1 版本。
- 软件 sqlite3 已经升级到了 3.40.1 版本。
- 软件 tzcode 已经升级到了 2022g 版本，并提高了时区更改检测和可靠性修复。
- 软件 tzdata 已经升级到了 2023b 版本。
- 软件 unbound 已经升级到了 1.17.1 版本。
- 软件 xz 软件已经升级到了 5.4.1 版本。
- 软件 xz-embedded 软件已经升级到了 3f438e15109229bb14ab45f285f4bff5412a9542 版本。
- 软件 zlib 已经升级到了 1.2.13 版本。

### 运行时库和 API

libmd 现在支持 SHA-512/224。此功能由 Klara, Inc. 赞助。

现在，sysdecode(3)和 kdump(1) 支持 Linux 风格的系统调用跟踪。

本机 pthread 库函数现在可以支持 Linux 语义。

### 内核

此部分包括了对内核配置、系统调整和系统控制参数的更改，这些更改没有分类到其他部分。

#### 通用内核变更：

现在 bhyve(8) 虚拟化管理程序和内核模块 vmm(4) 支持在虚拟机中使用超过 16 个虚拟 CPU。在默认情况下，bhyve 允许每个虚拟机创建的虚拟 CPU 数量与主机上的物理 CPU 数量相同。可通过 loader 可调整参数 `hw.vmm.maxcpu` 来更改此限制。这个变更的提交哈希值为 3e02f8809aec。

64 位可执行文件的地址空间布局随机化 (ASLR) 已默认启用。如果应用程序出现意外故障（例如段错误），则可以根据需要对其禁用。要禁用单个调用的 ASLR，请使用 proccontrol(1) 命令：`proccontrol -m aslr -s disable` 命令。要禁用二进制文件的所有调用的 ASLR，请使用 elfctl(1) 命令：`elfctl -e +noaslr` 文件名。如果有问题，请通过问题报告系统 [https://bugs.freebsd.org](https://bugs.freebsd.org) 或在 freebsd-stable@FreeBSD.org 邮件列表中发布问题。这个变更的提交哈希值为 10192e77cfac，由 Stormshield 赞助。

针对英特尔 Alder Lake（第十二代）和可能的在 Raptor Lake（第十三代）混合 CPU 上的一些硬件页面失效问题，实现了一种解决方法。该 bug 可导致 UFS 和 MSDOSFS 文件系统损坏，并可能导致其他内存损坏。慢速核心 (E-cores) 将自动使用更慢的页面失效方法来解决此问题。这个变更的提交哈希值为 567cc4e6bfd9，由 FreeBSD 基金会赞助。

现在有一个新的内核配置选项 SPLIT_KERNEL_DEBUG，可以控制将内核和模块的调试数据分别拆分为单独的文件。该选项与 WITHOUT_KERNEL_SYMBOLS 选项交互，其行为与 13.0-RELEASE 和 13.1-RELEASE 不同，但与之前的版本相似。它现在仅控制调试数据的安装。默认值为 WITH_KERNEL_SYMBOLS 和 WITH_SPLIT_KERNEL_DEBUG，允许在 /boot 中安装没有调试数据的内核和模块，并在 /usr/lib/debug 中安装独立的调试文件，这是在 13.0-RELEASE 之前的版本中默认情况下所做的。使用 WITHOUT_KERNEL_SYMBOLS 和 WITH_SPLIT_KERNEL_DEBUG，将生成独立的调试文件，但不会安装，这与在 13.0-RELEASE 之前的版本中使用 WITHOUT_KERNEL_SYMBOLS 时一样。最后，使用 WITHOUT_KERNEL_SYMBOLS 和 WITHOUT_SPLIT_KERNEL_DEBUG，在 /boot 中安装具有内置调试信息的内核和模块，就像在 13.1-RELEASE 中使用 WITHOUT_KERNEL_SYMBOLS 一样。 哈希值：0c4d13c521aa（由 FreeBSD 基金会赞助）

在 PowerPC 上，pseries 中支持 ISA 3.0 的基数 pmap。这应该会使在 POWER9 实例上的 pseries 显着加快，因为现在需要较少的超级调用来管理 pmap。哈希值：c74c77531248

在 arm64 上现在支持对 L inux 进程的 ptrace（2）的支持。哈希值：99950e8beb72

为了促进稳定分支的 ABI 兼容性，CPU 亲和性系统调用现在更加容忍 CPU 集比内核使用的小。这将有助于增加内核集 MAXCPU 的大小。哈希值：72bc1e6806cc

添加了保存 CPU 浮点状态以在信号传递期间跨越的 64 位 linux（4）ABI 支持。哈希值：0b82c544de58，20d601714206

linux（4）ABI 中的 vDSO（虚拟动态共享对象）支持已经接近完成。哈希值：a340b5b4bd48

将 arm64 linux（4）ABI 的状态与 amd64 linux（4）ABI 保持一致。哈希值：0b82c544de58，a340b5b4bd48

#### 设备驱动程序

这部分介绍自 13.1-RELEASE 以来设备和设备驱动程序的变化和增加。

- 驱动程序 em(4) 现在正确支持较新芯片 82580 和 i350 上可用的完整接收缓冲区大小范围。 哈希值：3f8306cf8e2d
- 驱动程序 ena(4) 已升级到了 2.6.2 版本。（由 Amazon，Inc.赞助）
- 已为 hwpmc(4) 实现对 Intel Alder Lake CPU 的基本支持。 哈希值：b8ef2ca9eae9
- 驱动程序 ice(4) 已更新到了 1.37.7-k 版本。
- 引入了驱动程序 irdma(4) RDMA，用于 Intel E810 以太网控制器，以 per-PF 方式支持 RoCEv2 和 iWARP 协议，其中 RoCEv2 是默认协议，并升级到了 1.1.5-k 版本。哈希值： 42bad04a2156（由 Intel Corporation 赞助）
- 现在提供 DPAA2（第二代数据路径加速架构-在一些 NXP SoC 中发现的硬件级网络架构）的初始支持。它运行由 NXP 提供的固件，该固件提供 DPAA2 对象作为抽象层，并提供 dpni 网络接口。 哈希值：d5a64a935bc9（由 Bare Enthusiasm :)和 Traverse Technologies 赞助）
- 更新了 Intel 无线接口的驱动程序 iwlwifi(4)。（由 FreeBSD 基金会赞助）
- 添加了驱动程序 rtw88(4)，以支持多个 Realtek 无线 PCI 接口。目前仅限于 802.11 a / b / g 操作。请参阅 [https://wiki.freebsd.org/WiFi/Rtw88](https://wiki.freebsd.org/WiFi/Rtw88) 获取更多信息。
- 对于支持 Linux 设备驱动程序的 KPI 进行了许多添加和改进。（由 FreeBSD 基金会赞助）

### 支持的平台

### 存储

本节介绍了本地和网络文件系统以及其他存储子系统的更改和添加。

### 通用存储

#### ZFS 更改

ZFS 已升级到 OpenZFS release 2.1.9。可以在 [https://github.com/openzfs/zfs/releases](https://github.com/openzfs/zfs/releases) 找到 OpenZFS 的发行说明。

#### NFS 更改

修复了导致 NFS 服务器挂起的问题。该问题是由 TCP 中 SACK 处理的错误引起的。

#### UFS 更改

现在在运行日志软更新时可以在 UFS 文件系统上创建快照。因此，现在可以在使用日志软更新运行的活动文件系统上执行后台转储。通过在 dump（8）中使用 `-L` 标志请求后台转储。哈希值： 3f908eed27b4（由 FreeBSD 基金会赞助）

#### 引导加载程序更改

本节包括了引导加载程序、引导菜单和其他与引导相关的更改。

#### 引导加载程序更改

teken.fg_color 和 teken.bg_color loader.conf（5）变量现在接受亮或淡色前缀（和颜色号 8 到 15）来选择亮色。1dcb6002c500（由 FreeBSD 基金会赞助）。另请参见哈希值： 233ab015c0d7

已修复了 loader（8）中的几个错误，导致视频控制台输出消失。这些错误似乎是在引导加载程序启动内核后出现的挂起。（由 Netflix 赞助）

### 其他启动更改

#### 网络

本节说明了影响 FreeBSD 中网络的更改。

#### 一般网络

内核已经重新集成了驱动程序 wg(4) WireGuard，它提供使用了 WireGuard 协议的虚拟专用网络（VPN）接口。（由 Rubicon Communications，LLC（“Netgate”）和 FreeBSD 基金会赞助）。

内核 TLS 实现（KTLS）已添加了对 TLS 1.3 的接收卸载支持。现在，TLS 1.1 到 1.3 都支持接收卸载；TLS 1.0 到 1.3 支持发送卸载。（由 Netflix 赞助）

现在可以使用 netlink(4) 网络配置协议。它是在 RFC 3549 中定义的通信协议，并使用原始套接字在用户空间和内核之间交换配置信息。第三方路由程序和 linux(4) ABI 都使用它。netlink(4) 协议未被包括在 13.2-RELEASE 的 GENERIC（译者注：通用内核）配置中，但可用作内核模块。

现在可以在 ipfw(4) 中支持基数表和查找 MAC 地址。这可以构建和使用 MAC 地址表进行过滤。

内核模块 dpdk_lpm4 和 dpdk_lpm6 现已可用，可以通过 loader.conf(5) 进行加载。它们为具有大量路由表的主机提供了优化的路由功能。它们可以通过 route(8) 进行配置，是模块化 FIB 查找机制的一部分。

TCP 和 SCTP 中有大量的 bug 修复。

### 通用注释——后续 FreeBSD 版本的注意事项：

OPIE 已弃用并将在 FreeBSD 14.0 中删除。

ce(4) 和 cp(4) 同步串行驱动程序已被弃用，并将在 FreeBSD 14.0 中删除。

ISA 声卡的驱动程序已被弃用，并将在 FreeBSD 14.0 中删除。d7620b6ec941 (由 FreeBSD 基金会赞助)

工具 mergemaster(8) 已被弃用，并将在 FreeBSD 14.0 中删除。它的替代品是 etcupdate(8)。5fa16e3c50c5 (由 FreeBSD 基金会赞助)

工具 minigzip(1) 已被弃用，并将在 FreeBSD 14.0 中删除。84d3fc26e3a2

netgraph 中的 ATM 的其余组件（NgATM）已被弃用，并将在 FreeBSD 14.0 中删除。对 ATM NIC 的支持先前已被删除。

Telnet 的守护程序 telnetd(8) 已被弃用，并将在 FreeBSD 14.0 中删除。Telnet 客户端不受其影响。

geom(8) 中的 VINUM 类已被弃用，并将在以后的版本中删除。

#### 默认的 CPUTYPE 更改

从 FreeBSD-13.0 开始，i386 架构的默认 CPUTYPE 将从 486 更改为 686。

这意味着，通过默认设置生成的二进制文件将需要 686 级别的 CPU，包括但不限于 FreeBSD Release Engineering 团队提供的二进制文件。FreeBSD 13.x 将继续支持旧的 CPU，但使用者需要自行构建其官方支持的发行版。

由于 i486 和 i586 CPU 的主要用途通常是嵌入式市场，因此对一般的终端用户的影响预计将很小，因为拥有这些 CPU 类型的新硬件早已消失，而大部分这类系统的已部署基础正处于退役年龄，这是统计数据所显示的。

这个改变考虑了几个因素。例如，i486 没有 64 位原子操作，虽然它们可以在内核中进行仿真，但不能在用户空间中进行仿真。此外，32 位的 amd64 库自其问世以来就是 i686。

由于大部分 32 位测试是由开发人员使用内核中的 COMPAT_FREEBSD32 选项在 64 位硬件上使用 lib32 库来完成的，因此这个变化确保了更好的覆盖率和用户体验。这也与大部分 Linux® 发行版长期以来所做的行为相一致。

这被认为是 i386 默认 CPUTYPE 的最后一次提升。

> **此更改不影响 FreeBSD 12.x 系列的发行版。**
