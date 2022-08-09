# 第四节 FreeBSD 发行说明

>FreeBSD 的生命周期为每个大版本 5 年，小版本是发布新的小版本版后 +3 个月。
>
>FreeBSD 14 开发计划 <https://github.com/bsdjhb/devsummit/blob/main/14.0/planning.md>

## FreeBSD 2022 年第二季度 季度状况报告 

>原文地址<https://www.freebsd.org/status/report-2022-04-2022-06/>

FreeBSD 季度状态报告 2022 年第二季度

这里是 2022 年的第二份季度报告，共包括 26 份报告。

在本季度，季度团队设法更快地发布报告，并希望能减少错误。然而，如果你注意到某些错误，请报告，以便我们能够纠正它们，并在我们的工具中添加自动检查设置，以防止将来出现这些错误，并尽可能对发布过程保持高效率。

我们还想提醒你，如果由于任何原因，你需要更多的时间来提交季度报告，团队将等待你，但请提醒我们，以便我们意识到有些报告仍未提交。

非常感谢所有选择通过季度报告与 FreeBSD 社区分享其工作的人。

Lorenzo Salvadore，代表现状报告小组。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

本报告的渲染版可在此查阅： https://www.freebsd.org/status/report-2022-04-2022-06/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

目录

   •  FreeBSD 团队报告  
   □  FreeBSD 核心团队  
□  FreeBSD 基金会  
□  FreeBSD 发布工程团队  
□ 集群管理团队  
□ 持续集成  
□ ports 系列  
• 项目
□ Linux 兼容层更新
□ 在 FreeBSD riscv64 上运行
□ 微软 HyperV 和 Azure 上的 FreeBSD
• 用户园地
□ 正在进行的关于 LLDB 多进程调试支持的工作

□  makefs(8) 中的 ZFS 支持。  
﻿ □ 基础系统OpenSSH更新
□ 基金会的最新状况
• 内核
□ ENA FreeBSD驱动程序更新
□ 新的蓝牙®配置守护程序：blued
□ OpenVPN DCO
□ 无线更新
□ 共享的页面地址随机化
• 架构
□ 支持恩智浦DPAA2
□ 关于arm64及其他的中型超级页面
• 文件
□ 文档工程团队
• 码头
□ FreeBSD上的KDE
□ 其他地方
□ GCC ：更新GCC_DEFAULT和其他改进
□ Valgrind - 13.1/14.0的大量错误修正和更新
□ FreeBSD上的Pantheon桌面
□ 英特尔的igt-gpu-tools的完整移植功能。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

FreeBSD团队报告

来自各官方和半官方团队的参赛作品，可在行政页面找到。

FreeBSD核心团队

联系。FreeBSD核心团队 core@FreeBSD.org

FreeBSD核心团队是FreeBSD的管理机构。

第十二个FreeBSD核心团队是由活跃的开发者选举产生的。core.12的成员是

• Baptiste Daroussin (bapt, 现任)

• Benedict Reuschling (bcr)

• 埃德-马斯特（Emaste，现任）。
﻿ • 格雷格-勒黑 （grog）

• John Baldwin (jhb)

• 徐立文 (lwhsu)

• 埃马纽埃尔-瓦多特(manu)

• Tobias C. Berner (tcberner)

• 马特乌斯-皮奥特罗斯基 (0mp)

6月10日，即将离任的core.11和即将上任的core.12团队召开了交接会议，新的核心团队于6 月18日宣布成立。

现任核心小组秘书穆罕默德-莫伊努尔-拉赫曼（bofh）将卸任。
在任命新的核心小组秘书和完成交接任务后。

在本季度，Kornel Dulęba（kd）和Dmitry Salychev （dsl）的src提交位已经被批 准。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

FreeBSD基金会的链接。
FreeBSD基金会网址：https://www.FreeBSDFoundation.org
技术路线图 URL:
https://FreeBSDFoundation.org/blog/technology-roadmap/
捐赠 URL: https://www.FreeBSDFoundation.org/donate/
基金会合作计划网址: https://www.FreeBSDFoundation.org/ FreeBSD- foundation-partnership-program
FreeBSD杂志网址：https://www.FreeBSDFoundation.org/journal/ 基金会 新闻和活动网址：https://www.FreeBSDFoundation.org/ news-and- events/

联系。Deb Goodkin deb@FreeBSDFoundation.org

FreeBSD基金会是一个501(c)(3)的非营利组织，致力于支持和促进全球的FreeBSD 项目和社区。捐献
﻿来自个人和企业的资金被用来资助和管理软件开发项目、会议和开发者峰会。我们还为 FreeBSD贡献者提供旅行补助，购买和支持硬件以改善和维护FreeBSD的基础设施，并提 供资源以改善安全、质量保证和发布工程工作。我们发布营销
材料来推广、教育和宣传FreeBSD项目，促进商业供应商和FreeBSD开发者之间的合作， 最后，在执行合同、许可协议和其他需要公认的法律实体的法律安排中代表FreeBSD项目 。

筹集资金的努力

首先，我想向所有为我们的工作提供资金捐助的人表示衷心的感谢。我们的资金100%来 自于你们的捐款，因此每一笔捐款都可以帮助我们在许多方面继续支持FreeBSD，包括在 这份状况报告中资助和发表的一些工作。

我们今年的目标是为大约200万美元的支出预算筹集至少140万美元。在我写这份报告的 时候，我们已经筹集到了不到100万美元。
20万美元的目标。因此，我们显然需要加强我们的筹款努力。到目前为止，这是我工作中 最难的部分。我更愿意和社区中的人们讨论我们如何帮助你们，帮助创建内容以招募更多 的用户和贡献者加入项目，并了解个人和组织在使用FreeBSD时遇到的挑战和痛点，以便 我们能够帮助改善这些方面。索取金钱并不在此列。

我们在五个主要领域支持FreeBSD。软件开发是我们资助的最大的领域，我们有六个软件 开发人员，他们介入实现新的功能，支持一级平台，审查补丁，并修复问题。您可以
在这份报告中，可以看到我们在操作系统改进方面所做的一些工作。FreeBSD宣传是我们支 持的另一个领域，我们通过会议、在线和面对面的演讲、教程和方法来传播关于FreeBSD的 信息。
指南。我们购买并支持用于支持项目工作的FreeBSD基础设施的硬件。基金会组织的虚拟 和现场活动帮助联系和吸引社区成员分享他们的知识并在项目上进行合作。最后，我们在 需要时为项目提供法律支持，并保护FreeBSD的商标。

如果你今年还没有捐款，请考虑捐款，地址是：https:/

/freebsdfoundation.org/donate/。

我们还有一个针对大型商业捐助者的合作伙伴计划。你可以在 https://freebsdfoundation.org/our-donors/ 找到更多信息。
freebsd-foundation-partnership-program/
﻿操作系统的改进

在2022年第二季度，有243份src、62份port和12份文档树的提交将FreeBSD基金会列为 赞助商。这分别代表了每个版本库中提交总数的 10.6、0.7 和 4.5%。

赞助工作

你可以在个别季度报告条目中读到一些基金会赞助的工作。

• 基础系统OpenSSH更新

• 正在进行的关于LLDB多进程调试支持的工作

• 无线状态

• 在makefs中支持ZFS

这里介绍了其他正在进行的赞助工作。

• FreeBSD Wireguard的改进

Wireguard项目的目的是改善对FreeBSD Wirguard内核模块的支持。
John Baldwin 的工作涉及到调整模块，使其使用 FreeBSD 的 OCF 而不是 Wireguard
的内部实现。
它还涉及添加新的密码和API支持。最新的上游版本包含了 这项工作。

• FreeBSD上的Openstack

OpenStack是一个用于不同类型资源的云系统，如虚拟机。
然而，OpenStack只非官方地支持FreeBSD作为客户系统。
这意味着用户可以在开放的云平台上生成FreeBSD实例，但目前还不能在FreeBSD主机 上运行OpenStack。
这个项目的目标是移植OpenStack组件，使FreeBSD能够作为OpenStack主机运行。

• Bhyve问题支持

基金会最近签署了一份支持Byhve的新合同。
﻿ 这份合同将使约翰-鲍德温能够在出现问题时为Bhyve奉献时间，特别是安全问题。

• 手册改进探索

在基金会的赞助下，保罗-阿玛完成了一个小型项目，探索如何改进《手册》。
已经发出了一份调查，结果将很快与大家分享。

持续集成和质量保证

基金会提供一名全职工作人员，并资助项目，以改善持续集成、自动测试和整体质量保证。
为FreeBSD项目所做的努力。

支持 FreeBSD 基础设施

基金会为该项目提供硬件和支持。一个新的澳大利亚镜像被集群管理团队带到了网上。 如果你是大洋洲或东南亚的FreeBSD用户，请让我们知道安装程序镜像和软件包的下载 速度是否有所提高。

通过你们的捐款，基金会购买了新的硬件来修复两个PowerPC软件包的构建器，一个是小 恩典软件包（powerpc64le），第二个是大恩典软件包（powerpc64，powerpc）。新 的硬件刚刚到达数据中心，很快就会安装。预计在不久的将来会有很多PowerPC软件包。

倡导和教育 FreeBSD

我们的大部分工作是致力于项目的宣传。这可能涉及到突出有趣的FreeBSD工作， 制作文献和视频教程，参加活动，或者做演讲。我们所制作的文献的目标是向人们 传授FreeBSD的基本知识，并帮助使他们
采纳或贡献的途径更容易。除了参加活动和发表演讲之外，我们还鼓励和帮助社区成员举 办自己的FreeBSD活动。
做出演讲，或担任FreeBSD的工作人员。

FreeBSD基金会在全球范围内赞助了许多会议、活动和峰会。这些活动可以是与BSD相关的 ，也可以是开源的，或者是面向未被代表的群体的技术活动。我们支持以FreeBSD为中心的 活动，以帮助提供一个分享知识、共同开展项目的场所。

并促进开发者和商业用户之间的合作。这
﻿都有助于提供一个健康的生态系统。我们支持非FreeBSD的活动，以促进和提高对 FreeBSD的认识，增加FreeBSD在不同应用中的使用，并招募更多的贡献者加入该计 划。我们将继续参加虚拟活动，并计划在2022年6月举行开发者峰会。除了参加和策 划虚拟活动之外，我们还在不断地进行新的培训计划，并更新我们的指南选择，以促 进更多的人尝试使用FreeBSD。

请看我们上一季度所做的一些宣传和教育工作。

• 我们获得了2022年10月30日至11月2日在北卡罗来纳州罗利举行的All Things Open 的展位和非营利性赞助商地位。

• 我们在7月28-30 日在加州洛杉矶举行的Scale 19x上的展位和研讨会已经确定。 FreeBSD研讨会将于2022年7月29 日星期五举行，你可以到基金会的502号展位 参观。

• 确认我们是2022年9月15-18日在奥地利维也纳举行的EuroBSDcon的银牌赞助商

• 赞助并帮助组织2022年6月16-17日的FreeBSD开发者峰会。视频可以在FreeBSD项目的 YouTube频道上看到。

• 庆祝2022年6月19日的FreeBSD日，以及接下来的整个一周。

• 我们获得了7月30日至31日在台湾举行的COSCUP之友级别的赞助。

• 发布FreeBSD基金会2022年春季更新

• 新的博客文章

□ 我们来谈谈基金会的资金问题  

□ 新董事会成员访谈。猫咪奥曼  

□ 欢迎FreeBSD的谷歌代码之夏参与者  

□  13.1版本中的FreeBSD基金会工作  

□ 基金会选举新的官员，采访即将离任的董事会成员  

□ 帮助我们庆祝整个星期的FreeBSD日  
• 新的和更新的如何操作和快速指南。
﻿ □ 网络基础知识。WiFi和蓝牙

□  FreeBSD上的音频  

□ 用VirtualBox安装FreeBSD (Mac/Windows) - 视频指南  

□  FreeBSD操作系统简介 - 视频指南  

□ 在FreeBSD上安装一个桌面环境 - 视频指南  

□ 在FreeBSD上安装一个端口 - 视频指南  
我们通过出版专业的FreeBSD杂志来帮助世界了解FreeBSD。正如我们之前提到的， FreeBSD杂志现在是一份免费出版物。了解更多信息并访问最新的期刊：https://
www.FreeBSDfoundation.org/journal/。

你可以在https:// www.FreeBSDfoundation.org/news-and-events/，了解更多关于我们 参加的活动和即将举行的活动。

法律/FreeBSD知识产权

基金会拥有 FreeBSD的商标，保护这些商标是我们的责任。我们还为核心团队提供 法律支持，以调查出现的问题。

进入https://www.FreeBSDFoundation.org，了解更多关于我们如何支持FreeBSD以及我 们如何帮助你的信息。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

FreeBSD 发布工程团队的链接。
FreeBSD 13.1-RELEASE schedule URL: https://www.freebsd.org/releases/13.1R/
时间表/
FreeBSD 13.1-RELEASE公告 URL:
https://www.freebsd.org/releases/13.1R/
announce/
FreeBSD的发布URL: https://download.freebsd.org/releases/ISO-IMAGES/
FreeBSD的开发快照URL: https://download.freebsd.org/snapshots/ ISO-IMAGES/
﻿联系。FreeBSD发布工程团队， re@FreeBSD.org

FreeBSD 发布工程团队负责为FreeBSD的官方项目发布制定并发布发布计划，宣布代码 冻结并维护相应的分支，以及其他事项。

在2022年的第二季度，发布工程团队完成了13.1-RELEASE周期的工作。这是稳定/13的第 二个版本
分支。在整个发布周期中，发生了三次BETA构建和六次RC （候选发布版）构建，将最终 发布日期从2022年4月21日移至2022年5月16日，因为在最后一刻发现了一些问题。

我们感谢所有测试13.1-RELEASE的FreeBSD开发人员和贡献者，他们报告了问题，并随 着周期的进展勤奋地进行了修改。

此外，在整个季度中，还为主分支、stable/13和stable/12分支发布了几个开发快照版本 。

赞助商。Rubicon Communications, LLC ("Netgate") 赞助商。FreeBSD基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

集群管理团队链接。
集群管理小组成员网址。
https://www.freebsd.org/administration

/#t-clusteradm

联系。集群管理团队 clusteradm@FreeBSD.org

FreeBSD集群管理团队的成员负责管理该项目所依赖的机器，以同步其分布式工作和通信 。在这一季度，该团队进行了以下工作。

• 在澳大利亚悉尼安装了一个新的镜像，由IX澳大利亚公司托管

• 修复了CI集群的硬件故障

• 建立一个新的内部监测系统
﻿ • 定期进行集群范围内的软件升级

• 对FreeBSD.org用户账户的定期支持 工作正在进行

中。

• 与PowerPC团队合作，改进软件包构建者、通用和参考机器。

• 计划硬件更新，并修复各站点的杂项故障

• 改善成套建筑的基础设施

• 审查服务监狱和服务管理员的运作情况

• 与doceng@合作，改善https://www.freebsd.org 和https://docs.freebsd.org 的部署 。

• 改进网络服务架构

• 完善集群备份计划

• 完善日志分析系统

我们正在欧洲寻找一个额外的全镜像站点（五个服务器）。请看一般的镜像布局， 以满足我们的需要。我们也欢迎提供额外的单服务器镜像（见小镜像），特别是在 欧洲。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

持续集成链接。
FreeBSD Jenkins Instance URL: https://ci.FreeBSD.org
FreeBSD CI工件档案URL: https://artifact.ci.FreeBSD.org FreeBSD
Jenkins wiki URL: https://wiki.freebsd.org/Jenkins Hosted CI wiki
URL: https://wiki.freebsd.org/HostedCI
第三方软件CI URL: https://wiki.freebsd.org/3rdPartySoftwareCI
与 freebsd-testing@ 相关的票据 URL: https://preview.tinyurl.com/y9maauwg FreeBSD
CI 存储库 URL: https://github.com/freebsd/freebsd-ci
dev-ci 邮件列表 URL: https://lists.freebsd.org/subscription/dev-ci
﻿联系。Jenkins Admin jenkins-admin@FreeBSD.org 联 系。Li-Wen Hsu lwhsu@FreeBSD.org
联系：freebsd-testing 邮件列表联系。IRC
#freebsd-ci channel on EFNet

FreeBSD CI 团队负责维护 FreeBSD 项目的持续集成系统。CI系统检查所提交的修改是否 能够成功构建，然后对新构建的结果进行各种测试和分析。该系统
这些构建的工件被归档到工件服务器中，以便进一步
测试和调试的需要。CI团队成员检查失败的构建和不稳定的测试，并与该领域的专家合作， 修复代码或调整
测试基础设施。

在2022年的第二季度，我们继续与项目中的贡献者和开发者合作，以满足他们的测试需 求，同时也与外部项目和公司保持合作，以改进他们的产品和FreeBSD。

重要的已完成任务。

• 修正了CI集群的硬件故障问题 工作中的任务。

• 设计和实施提交前的CI构建和测试（以支持工作流程工作组的工作）

• 设计和实施CI集群的使用，以建立发布工程的工件。

• 测试和合并FreeBSD-ci repo中的拉动请求

• 简化贡献者和开发者的CI/测试环境设置

• 设置CI阶段环境，并将实验性工作放在上面

• 整理freebsd-ci版本库中的脚本，为合并到src版本库做准备

• 更新维基上的文件 打开或排队

的任务。

• 收集和整理CI任务和想法
﻿ • 为运行测试的虚拟客体设置公共网络接入

• 实施使用裸机硬件来运行测试套件

• 增加drm端口，针对-CURRENT构建测试

• 计划运行ztest测试

• 增加更多外部工具链相关的工作

• 提高硬件实验室的成熟度，增加更多测试用硬件

• 帮助更多的软件在其CI管道中获得FreeBSD支持 (Wiki页面:
3rdPartySoftwareCI, HostedCI)

• 与托管CI供应商合作以获得更好的FreeBSD支持

更多的WIP信息请参见freebsd-testing@相关票据，请不要犹豫，加入我们的努力吧!

赞助商。FreeBSD基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

端口收集链接。
关于 FreeBSD 端口 URL:https://www.FreeBSD.org/ports/
贡献给 Ports 的 URL: https://docs.freebsd.org/en/articles/contributing/# ports- contributing
FreeBSD端口监控URL: http://portsmon.freebsd.org/ 端口管理团队 URL: https://www.freebsd.org/portmgr/
端口 Tarball URL: http://ftp.freebsd.org/pub/FreeBSD/ports/ports/

联系。René Ladan portmgr-secretary@FreeBSD.org

联系。FreeBSD端口管理团队 portmgr@FreeBSD.org

港口管理团队负责监督港口树的整体方向、建筑配套和人事事务。以下是上一季度发生 的情况。

港口的数量略高于30,000个。上一季度有9,137个
﻿在 "主 "上有151个提交者的提交，在 "主 "上有61个提交者的589个提交。
"2022Q2 "分支。在写这篇文章的时候，有 2700 个开放的 ports PR ，其中 682 个是 未分配的。与上一季度相比， 提交活动略有减少， 而 PR 的数量则保持不变。注意： Freshports 似乎大幅多计了。本季度的端口计数是以不同的方式得出的，与上一季度 的计数没有可比性。

在上个季度，portmgr 欢迎 salvadore@ 的回归，但也因缺乏活动而与七个 ports
committer 告别。

在两周一次的会议中，portmgr讨论了以下议题。* ca_root_nss的未来 * 基础系统 提供某些.pc文件的可行性 * 处理基础系统小版本升级时内核模块端口不兼容的方法

经过开发人员的讨论， portmgr 决定授予所有文档和源码提交者批准， 以修复 Ports 树中 任何不影响其功能的文档相关错误。

在 2022q2 期间对 Ports 树进行了如下修改： * pkg 更新到了 1.18.3 版， Firefox 更新 到了 102.0 版， Chromium 更新到了 103.0.50060.53 版 * GCC、 Lazarus、 Python
和 Ruby 的默认版本分别更新到了 11 (powerpcspe 保持 8 版)、 2.2.2、 3.9 和 3.0。*
加入了两个新的USES，gstreamer用于支持基于GStreamer插件的端口，pytest用于帮 助使用pytest进行测试。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

项目

跨越多个类别的项目，从内核和用户空间到端口集合或外部项目。

Linux兼容层更新

联系。Dmitry Chagin dchagin@FreeBSD.org 联系方式。Edward Tomasz
Napierala <
trasz@FreeBSD.org>

这个项目的目标是提高 FreeBSD 执行未经修改的 Linux 二进制文件的能力。目前对特定
Linux 应用程序的支持状态正在 Linux 应用程序状态 Wiki 页面上进行跟踪。
﻿Y2k38 Linux项目的实施已基本完成；所有'*_time64()'系统调用都已提交。

arm64 Linux仿真层的状态被带到了amd64 Linux仿真层的状态：即实现了vDSO、机器 依赖的futexes、信号传递。

线程亲和力系统调用被修改以实现Linux语义。

总共修复了50多个错误；glibc-2.35测试套件报告了不到80个失败的测试。

Linux仿真层的所有变化都被合并到stable/13分支。

在libsysdecode和kdump中加入了对花式Linux系统调用追踪的初步支持。目前正在进 行的工作是使追踪更多的系统调用发挥作用。

赞助商。EPSRC （爱德华的工作）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

go on FreeBSD riscv64

Links:
golang主页网址：https://github.com/golang/go
FreeBSD riscv64 github repo URL: https://github.com/MikaelUrankar/go/tree/
freebsd_riscv64
FreeBSD riscv64 golang问题URL: golang/go#53466

联系。Mikaël Urankar mikael@FreeBSD.org 联系 。Dmitri Goutnik dmgk@FreeBSD.org

已经完成了将 go 移植到 FreeBSD riscv64 上的工作，它可以构建并通过所有 run.bash
测试，包括 cgo （在 QEMU 和 Unmatched 上测试）。在上游创建了一个拉动请求，该 提案已被添加到提案项目的活动栏中，并将在每周的提案审查会议上被审查。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━
﻿微软HyperV和Azure上的FreeBSD

链接。
微软Azure文章在FreeBSD维基上的URL ：https://wiki.freebsd.org/ MicrosoftAzure
微软HyperV文章在FreeBSD wiki上的网址：https://wiki.freebsd.org/HyperV

联系。Microsoft FreeBSD集成服务团队 bsdic@microsoft.com 联系人：freebsd- cloud Mailing List
联系。FreeBSD Azure 发布工程团队
releng-azure@FreeBSD.org 联系。胡 伟 whu@FreeBSD.org
联系方式。徐立文 lwhsu@FreeBSD.org

Azure Marketplace上的13.1-RELEASE镜像已经发布。正在进行的工作任务。

• 实现图像构建和发布过程的自动化

• 构建并向Azure市场发布基于ZFS的镜像

□ 通过合并makefs(8)和release(7)的ZFS支持，taks将受益。  

  ☆https://reviews.freebsd.org/D23334  

  ☆https://reviews.freebsd.org/D34426  

  ☆https://reviews.freebsd.org/D35248  
• 构建和发布Hyper-V gen2 VM镜像到Azure Marketplace

□ 被https://bugs.freebsd.org/264267 屏蔽  
上述任务由FreeBSD基金会赞助，并由微软提供资源。

胡伟和他在微软的同事正在从事由微软赞助的几项任务。

• 修复Azure中Hyper-V gen2 VM的启动问题

□  https://bugs.freebsd.org/264267  
﻿ • 移植Hyper-V客户支持到arch64 打开任务。

• 在https://docs.microsoft.com 更新FreeBSD的相关文档

• 在Azure管线中支持FreeBSD

• 将Azure代理端口更新到最新版本

• 阿泽尔代理的上游本地修改

赞助商。微软提供了胡伟等人在微软的工作，以及其他方面的资源 赞助商。 FreeBSD基金会提供其他一切

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

用户园地

影响基础系统和其中程序的变化。正在进行的关于LLDB多进程

调试支持的工作 链接。
莫里茨系统项目描述URL: https://www.moritz.systems/blog/
multiprocess-support-for-lldb/
进度报告1 URL: https://www.moritz.systems/blog/
implementing-non-stop-protocol-compatibility in-lldb/

联系。Kamil Rytarowski kamil@moritz.systems 联系。 Michał Górny mgorny@moritz.systems

根据上游的描述，"LLDB是下一代的。
高性能调试器。它是作为一套可重复使用的组件构建的，高度利用了更大的LLVM项目中 的现有库，如
Clang表达式解析器和LLVM反汇编器。"

FreeBSD在基本系统中包含了LLDB。之前赞助的项目改进了 LLDB ，使其成为基础系统 中可信的调试器，尽管与 GNU GDB 的当代版本相比，它仍有一些限制。这个项目于 2022年4月开始。它的目标是实现对同时调试多个进程的全面支持。
﻿在项目开始时，LLDB对多进程调试的支持非常有限。客户端的特点是支持调试多个
通过维护与不同服务器实例的多个连接，可以同时追踪独立的进程。由于我们先前的工作 ，服务器能够处理fork(2)和vfork(2)调用，并且要么分离新分叉的子进程并继续跟踪父进 程，要么分离父进程并跟踪子进程（相当于GDB的follow-fork模式设置）。

一旦该项目完成，LLDB将能够同时追踪任意数量的分叉进程（相当于GDB的detach- on-fork off）。将实现对GDB远程串行协议的多进程扩展的完全支持，以及对不停机扩 展的部分支持，该扩展将使多个进程独立恢复和停止。

赞助商。FreeBSD基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

在 makefs(8) 链接中支持

ZFS。
邮件列表帖子网址：https://lists.freebsd.org/archives/freebsd-hackers/
2022-May/001128.html
makefs(8) 代码审查 URL: link:https://reviews.freebsd.org/D35248 release(7) 代码 审查 URL: link:https://reviews.freebsd.org/D34426

联系方式。马克-约翰斯顿 markj@FreeBSD.org

makefs(8)是一个源自NetBSD的工具，它完全在用户空间创建文件系统镜像。它是建 立虚拟机（VM）镜像的一个有用的工具链组件，因为它不需要任何特殊的权限，不 像格式化一个字符设备、挂载新的文件系统那样。
并将文件复制到它上面。此外， makefs 可以创建可重复的映像，并旨在最大限度地减 少资源消耗。目前， FreeBSD的makefs可以建立 UFS、cd9660和 msdos （FAT）文件 系统镜像。

最近的工作使makefs能够创建ZFS镜像。makefs的ZFS支持包括创建多个数据集的能力 ，每个数据集映射到输入文件层次中的一个目录。然而，许多ZFS功能并不被支持，因 为该实现只提供了获得可重复的根池所需的功能。
﻿后续工作使release(7)框架能够使用这个新的makefs扩展创建基于ZFS的虚拟机和云图像。

赞助商。FreeBSD基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

基础系统OpenSSH更新链接。
OpenSSH URL: https://www.openssh.com/
OpenSSH 8.9发布说明 URL:https://www.openssh.com/txt/release-8.9[https://
www.openssh.com/txt/release-8.9]
OpenSSH 9.0发布说明 URL:https://www.openssh.com/txt/release-9.0[https://
www.openssh.com/txt/release-9.0]

联系。Ed Maste emaste@freebsd.org

OpenSSH ， 一套远程登录和文件传输工具， 在 FreeBSD 基本系统中从 8.8p1 版 本更新到了 9.0p1。

它还没有被合并到 stable/13 和 stable/12 分支。我预计将在7月这样做。

注意: OpenSSH 9.0p1将scp(1)从使用传统的scp/rcp协议改为默认使用SFTP协议。-O 标志 可用于使用
以前的协议代替。

赞助商。FreeBSD基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

基金会的最新状况

联系。Kristof Provost kp@FreeBSD.org 联系方式。Reid Linnemann <
rlinnemann@netgate.com>

以太网

pf最近增加了对以太网层过滤的支持。见2021q2 pf_ethernet报告。
﻿从那时起，以太网层的过滤功能已经扩展到了。

• 锚杆支持

• 能够查看第3层头，以便与源/ 目的IP （v4/v6）地址相匹配

• 对IP地址匹配的表支持

• 直接派遣到Dummynet

• 将以太网层的数据包直接传递给dummynet ，而不是对数据包进行标记，并依靠 第3层来处理dummynet。

杜米尼网

pf最近开始能够使用dummynet进行数据包调度。这种支持已经得到扩展和改进，现在 相信已经可以用于生产了。

一个值得注意的修正是，回复到/路由到的流量现在也受制于dummynet调度。

最后一次比赛的时间戳

pf 现在可以跟踪一个规则最后一次被匹配的时间。与 ipfw 规则的时间戳类似， 这些 时间戳在内部是系统 "墙面时间 "时钟的 uint32_t 跳转， 单位是秒。(参见 time(9))。 时间戳是CPU本地的，并在每次规则或状态被匹配时更新。

赞助商。Rubicon Communications, LLC （"Netgate"）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

内核

对内核子系统/特性、驱动支持、文件系统等进行更新。ENA FreeBSD 驱动程序更新

链接。
ena readme url:

https://github.com/amzn/amzn-drivers/blob/master/kernel/fbsd/
﻿ena/README.rst

联系。Michal Krawczyk mk@semihalf.com 联系。 Dawid Gorecki dgr@semihalf.com 联系方式。 Marcin Wojtas mw@FreeBSD.org

ENA （弹性网络适配器）是亚马逊网络服务（AWS）的虚拟化环境中可用的智能网卡。 ENA驱动程序支持多个发送和接收队列，可以处理高达100Gb/s的网络流量，这取决于它 所使用的实例类型。

自上次更新以来已完成。

• ENA驱动程序v2.5.0的上游，其中包括。

• 改进了对重置程序的处理。

• 延长定时器服务寿命，以便能够检测更多的硬件故障。

• 修正验证Tx请求ID的逻辑。

• 修复Tx的IPv6 L4校验和卸载处理。

• 在驱动程序中增加NUMA意识。

• 对即将发布的ENA驱动程序（v2.6.0）进行内部审查，包括。

• 进一步改进复位处理。

• 代码清理和风格修正。

• 记录的改进。

• 对ENI指标的检索进行了修正。工作正在

进行中。

• 测试即将发布的ENA驱动程序（v2.6.0）。赞助商。

Amazon.com Inc

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━
﻿新的蓝牙®配置守护程序：blued

链接。

blued git URL: https://git.lysator.liu.se/kempe/blued

联系。
邮件：kempe@lysator.liu.se
IRC：kempe@libera.chat

简介

blued工具提供了一个IPC接口，可以让无特权的用户
以用户友好的方式连接和使用蓝牙设备，并支持安全的简单配对（公钥加密法，如果设备允 许的话
中间人保护）。

什么是发蓝？

blued有三个部分：一个库、一个守护程序和一个命令行工具。库抽象了蓝牙的细节 ，守护程序管理蓝牙设备，命令行工具让用户列出或扫描蓝牙设备，与设备配对或解 除配对。命令行工具通过UNIX套接字与守护程序进行通信。

与bthidd和hcsecd不同，blued支持安全的简单配对并提供IPC。为了让HID设备工作， 仍然需要bthidd。我们提供了一个脚本
对一个蓝牙设备进行配对，并对bthidd进行适当的配置，这样它就能正常工作并重新 连接，不需要用户干预。

一旦配对被证明是稳定的，并且错误已经被解决，我们计划以某种方式将bthidd与blued 集成，使HID设备在配对时自动开始运作，而不需要使用外部脚本。A
长期目标是提供一个图形用户界面，可以列出设备并提供简单的一键式设置来连接 它们。

安装和使用blued v0.1

你需要在/etc/src中安装可选的src组件。

首先，确保你已经加载了工作的蓝牙驱动，如FreeBSD手册中所解释的。

要测试blued，请获取blued v0.1的源代码。然后编译它，给你的
﻿使用kernel_patches中的补丁对FreeBSD内核进行修改，并按照README中的解释重新编 译hci模块。

我主要在FreeBSD 12.3上测试了blued，但在13.1上测试时，我的补丁应用得很干净 。目前我还没有提供端口，但可以直接从构建目录中运行该软件，或者运行 "make
install "来安装所有需要的文件。blued和bluecontrol都使用capsicum，blued可以 被配置为放弃其root权限。

更多信息请参考README中的运行blued部分。帮忙的人

测试

我只用自己的鼠标试过这个软件，并意识到一个单一的蓝牙设备的样本量是相当小 的。我期待着问题的出现，并非常期待着其他人的反馈!

如果出现问题，从/var/log/debug.log和/var/log/messages的输出以及尝试配对时 从 "hcidump -x "获得的流量转储将有助于故障排除。

贡献

如果你想参与代码并提交补丁，欢迎你访问Lysator的Git上的存储库。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

OpenVPN DCO链接

。
D34340网址。D34340
OpenVPN维基网址。OpenVPN wiki

联系。Kristof Provost kp@FreeBSD.org

OpenVPN DCO （或称数据通道卸载）将OpenVPN的数据包处理移至
内核。

传统上，OpenVPN使用一个tun(4)接口来传输和接收数据包。
﻿在这种设置下，收到的数据包由内核接收，传递给OpenVPN应用程序进行解密，然后 再传回内核进行网络堆栈处理。这需要在内核和用户空间之间进行多次转换，自然会造 成性能损失。

新的if_ovpn OpenVPN DCO卸载驱动完全在内核内执行加密/解密，提高了性能。

初步性能测试显示，吞吐量从约660Mbit/s提高到约2Gbit/s。

用户空间的OpenVPN代码也需要修改以使用新的if_ovpn卸载驱动。这有望成为未来 2.6.0版OpenVPN的一部分。

赞助商。Rubicon Communications, LLC （"Netgate"）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

无线更新链接。
英特尔iwlwifi状态 FreeBSD wiki页面URL: https://wiki.freebsd.org/WiFi/
Iwlwifi Realtek rtw88 status FreeBSD wiki页面URL: https://wiki.freebsd.org/
WiFi/Rtw88 Realtek rtw89 status FreeBSD wiki页面URL: https://wiki.freebsd.org
/WiFi/Rtw89

联系。Bjoern A. Zeeb bz@FreeBSD.org

整个项目旨在为FreeBSD带来对较新芯片组的支持。
目前使用的是由本地net80211和内核代码支持的LinuxKPI兼容代码。此外，我们的目标是 继续努力支持更新的无线标准。在第二季度，有 40 项提交进入了 FreeBSD CURRENT。
与

更多的用户尝试多个驱动程序的支持时间也在上升。

早期版本的 Intel iwlwifi 衍生的无线驱动在 13.1-RELEASE 中发布， 将这项 工作带入了第一个 FreeBSD 版本。iwlwifi
驱动程序和固件在CURRENT和stable/13中再次被更新，作为持续开发的一部分。与上 游Intel Linux版本的驱动程序共享的文件中的变化现在不到400行。最近，一个长期存 在的老式芯片组的问题（希望）得到了解决，允许支持iwm(4)的卡在近三个月后再次与 iwlwifi(4)一起工作。在今年年底之前，项目的主要重点将是让我们的
﻿到当代的速度。

4月1日，使用与iwlwifi工作相同的LinuxKPI基础设施，Realtek的rtw88(4)驱动被纳 入了CURRENT。由于一个
在接下来的几周里，我们开发了一个解决方法，并把它放在树上，这样用户就不必再给内 核打补丁。该驱动仍然需要一个可调整的
对于物理内存超过4GB的机器，在loader.conf中设置。这一调整使得驱动程序在6月 被合并到stable/13，随后在CURRENT和stable/13中进一步更新。随着基于rtw88的 芯片组的USB部分被准备纳入Linux，准备FreeBSD也能支持USB部分的工作已经开始 （需要更多时间）。

在过去的几个月里，Realtek的rtw89已经开始编译，并且仍然是一项正在进行中的工作，以 便稳定地运行，并且在它能够被启用之前，与之相关。
目前。

感谢所有用户的测试和反馈，耐心等待下一次的更新、错误修复，或者只是我的回 复。我很高兴能够
与您一起工作!继续向我发送错误报告，但请记住，您应该感谢FreeBSD基金会，因为它使 大部分的工作成为可能。

关于最新的发展状况，请关注freebsd-wireless邮件列表并查看wiki页面。

赞助商。FreeBSD基金会

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

共享的页面地址随机化链接。

D35392 D35393 D35349

联系。Kornel Duleba mindal@semihalf.com 联系 。Marcin Wojtas mw@FreeBSD.org

共享页是一个R/X页，由图像激活器映射到每个进程。它存储了信号蹦床，以及其他元 数据，例如实现用户空间时间计数器所需的信息。以前，它被映射在进程虚拟地址空间 的顶部。随着上述变化，它的地址将被随机化。我们计划对所有架构的64位二进制文件 默认开启该功能。目前，这些补丁正在审查中，等待批准。
﻿赞助商。风暴盾

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

架构

更新特定平台的功能，并引入对新硬件平台的支持。

恩智浦DPAA2支持链接
改变历史
树木

联系。Dmitry Salychev dsl@FreeBSD.org 联系。 Bjoern A. Zeeb bz@FreeBSD.org

恩智浦的一些SoC （LX2160A、LS1088A）配备了DPAA2，即第二代数据路径加速架构。 它允许动态配置和连接数据包处理 "对象" （网络接口的DPNI，媒体访问控制器的DPMAC等 ），以形成片上网络。

在上个季度，该驱动开始工作得很好，足以用于SolidRun的Honeycomb LX2 （ACPI测试平 台），Traverse Technologies已经为（他们的）Ten64 （用作FDT测试平台）制作了一个 FreeBSD预览版。

该驱动程序仍在进行中，但已接近审查，以便将第一个版本放入树中，让大家从中 受益。

创作中。

• FDT MDIO支持。FreeBSD 目前缺乏对 SPF 部分的支持。

• 驱动程序资源去分配，以正确卸载dpaa2.ko。

• 错误修复和改进。TODO:

• CPU对DPIO和DPNI的亲和力。
﻿ • 缓存的内存支持的软件门户。

• 缓解瓶颈。

• 硬件支持的更多部件（DPSW、DCE等）。赞助商。赤诚之心 :)

赞助商。Traverse Technologies （提供Ten64 HW用于测试）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

关于arm64及其他的中型超级页面

联系。Eliot H. Solomon ehs3@rice.edu 联 系。Alan L. Cox alc@rice.edu

64位ARM架构的页表描述符格式包含一个称为连续位的标志。这告诉MMU，它可 以缓存一组对齐的、物理上连续的16个页表项，这些页表项具有相同的权限和属性 ，只使用一个TLB项。

毗连位，以及概念上类似于RISC-V架构的Svnapot扩展，允许使用64KiB超级页。 这些中等大小的超级页可以为较小的内存对象带来
地址翻译的速度通常与更传统的2 MiB超级页有关。

这个项目专注于为 FreeBSD 带来对中等大小的超级页的支持。到目前为止，我们已经修 改了arm64的pmap代码，通过检测物理上连续的页表项并使用Contiguous位来自动利 用64 KiB的超级页。现在，我们正在努力调整内核的超级页保留模块，以支持64 KiB的 保留，除了目前的2 MiB的保留之外。增加中等大小的预留将允许虚拟内存系统明确地分 配符合超级页推广要求的内存块，而不是仅仅希望它们偶然出现。

我们的目标是以一种通用的方式来实现这一点，使其有可能指定多个任意的2次方保留 大小，从而更容易利用其他架构上的硬件功能，如Ryzen的PTE凝聚，它透明地将4
KiB的页表项组合并为中等大小的超级页。
﻿赞助商。莱斯大学计算机科学系

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

文件

文档树、手册页或新的外部书籍/文件中值得注意的变化。

文档工程团队链接。FreeBSD文档项目
链接。为新的贡献者提供的FreeBSD文档项目入门手册
链接。文档工程团队

联系。FreeBSD Doceng团队 doceng@FreeBSD.org

doceng@ 团队是一个处理与 FreeBSD 文档项目相关的一些元项目问题的机构； 要了解更 多信息，请参见 FreeBSD Doceng 团队章程。

在上一季度，格雷厄姆-佩林（grahamperrin@）和保罗-阿玛（pauamma@）。
被授予文件提交位。

有几个项目尚未完成，正在讨论中。

• 用项目的GeoDNS基础设施对网站和文件门户进行镜像。

• 如何处理文件中的商标。

• 删除网站和文档门户中过时的翻译。Weblate上的FreeBSD翻译

链接。在Weblate上翻译FreeBSD 链接。 FreeBSD Weblate 实例

2022年第二季度状况

• 12种语言
﻿ • 152名注册用户（9名新用户） 语言

• 中文(简体) (zh-cn)

• 中文(繁体) (zh-tw)

• 荷兰语 (nl)

• 法语 (fr)

• 德文(de)

• 印度尼西亚语 (id)

• 意大利语 (it)

• 挪威语 (nb-no)

• 波斯语(fa-ir)

• 葡萄牙语 (pt-br)

• 西班牙文(es)

• 土耳其语(tr)

我们要感谢每一个作出贡献、翻译或审阅文件的人。

而且，请帮助在你的本地用户组上推广这项工作，我们总是需要更多的志愿者。

FreeBSD网站改版 - WebApps工作组 联系。Sergio

Carlavilla carlavilla@FreeBSD.org

负责创建新的FreeBSD文档门户和重新设计FreeBSD主网站及其组件的工作小组。 FreeBSD的开发者可以
关注并加入FreeBSD Slack频道#wg-www21的工作小组。这项工作将分为四个阶段。

重新设计文件门户
﻿ 创建一个新的设计，响应并具有全球搜索功能。(完成)

重新设计网络上的手册页面

使用mandoc生成HTML页面的脚本。(工作正在进行中)

重新设计网页上的 "港口 "页面
端口脚本，以创建一个应用门户。(工作正在进行中)

重新设计FreeBSD主网站
新的设计，响应性和黑暗主题。(未开始)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

码头

影响 Ports Collection 的变化， 无论是涉及大部分树的全面变化， 还是个别端口本身的 变化。

KDE on FreeBSD 链

接。
KDE FreeBSD URL: https://freebsd.kde.org/
KDE Community FreeBSD URL: https://community.kde.org/FreeBSD

联系。Adriaan de Groot kde@FreeBSD.org

FreeBSD上的KDE项目将来自KDE社区的软件打包，连同
与依赖关系和相关软件，用于 FreeBSD ports 树。该软件包括一个名为KDE Plasma 的完整桌面环境（适用于X11和Wayland）和数百个可以在任何FreeBSD机器上使用 的应用程序。

KDE 团队 (kde@) 也是 desktop@ 和 x11@ 的一部分，他们建立了软件栈，以使
FreeBSD 作为基于图形的日常驱动的桌面机器变得漂亮和可用。下面的说明主要描述了 KDE的端口，但也有
包括对整个桌面堆栈的进口项目。

KDE堆栈
﻿KDE Gear每季度发布一次，KDE Plasma每月更新一次，而KDE
框架每个月也有一个新版本。这些（大型）更新在其上游发布后不久就会登陆，不单独列出 。

• astro/kstars最新版本3.5.9。

• deskutils/grantleetheme 在 UPDATING 中得到了一个条目， 因为 port 的安装结 构发生了一些异常的变化。

• deskutils/kalendar加入了KDE Gear版本。

• 开发/okteta对二进制（以及八进制和十六进制）数据查看器和编辑器的更新。

• finance/kraft需要对较新的KDE框架进行特定的构建修复。

• games/gcompris-qt扩展，新版本，现在支持更多的图像格式（某些活动需要）。

• graphics/digikam在构建过程中不再需要一个SQL服务器。

• graphics/krita被更新到5.0.5，可能是最后一个5.0版本。

• math/labplot在最近的版本中有大量的新功能，如果你需要任何类型的数据绘 图，非常值得关注。

• net-im/ruqola已经更新。这是一个Qt风格的火箭聊天应用程序。

• www/falkon加入了KDE Gear的发布。相关

的应用程序

• archivers/quazip已更新。

• deskutils/semantik更新。

• devel/py-qt5-pyqt 已被更新，因此该端口现在也能拉入 DBus 了。几乎所有的桌 面 Qt 应用程序都需要 DBus ，包括那些用 Python 编写的应用程序。

• development/qcoro在某些FreeBSD版本上有构建问题，已解决。
﻿ • 开发/qtcreator随每个新版本更新。

• devel/qt5 在 ports 中更新了它的基础结构， 这样它在卸载时就不会产生奇怪 的错误信息。

• graphics/ksnip和相关库更新到最近的版本。

• Matrix 客户端 Nheko (net-im/nheko) 和 Neochat (net-im/neochat) 在发布 和库颠覆之后被更新。

• x11/rsibreak更新；有助于防止在写长的季度报告时受伤。

其他地方

• development/appstream更新支持更多的应用信息。

• 如果用户安装了多个python3端口和lang/python3，devel/cmake更倾向于通用 的python3而不是版本化的python3。

• 更新了developer/dbus。

• 图形/多普勒更新数次。

• graphics/ImageMagick （包括6和7）更新了几次。

• 多媒体/gstreamer更新。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

GCC ：更新GCC_DEFAULT和其他改进 链接。
GCC项目网址：https://gcc.gnu.org
GCC 11发布系列网址：https://gcc.gnu.org/gcc-11/

联系方式： toolchain@FreeBSD.org
联系方式。Gerald Pfeifer gerald@pfeifer.com
联系。Lorenzo Salvadore salvadore@FreeBSD.org 联系 。Piotr Kubaj pkubaj@FreeBSD.org

• salvadore@致力于将Mk/ bsd.default-versions.mk中的GCC_DEFAULT从 10升级到11，在此基础上打开bug报告
﻿ antoine@的exp-runs，并修复了一些：非常感谢所有帮助完成这项任务的人。 GCC_DEFAULT从GCC 10到GCC 11的更新现在已经由gerald@提交，并在下一个季 度的分支中及时发生。https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=258378

• pkubaj@通过引入一个默认启用的新选项，将GCC引导转换为使用GCC本身的链接时间 优化，适用于GCC 11和更新版本。启用LTO_BOOTSTRAP进行构建需要大量的内存和 时间。实际需要多少资源取决于您的配置 (例如，您是用端口还是用 poudriere 构建？ 什么是
你的架构？）。为了给出一个概念，一个用户报告说需要5吉比特的
tmpfs ，而在PR 265254中，由于产生了过多的进程，估计需要大约130GB的内存（也 见https://gcc.gnu.org/ bugzilla/show_bug.cgi?id=106328）。考虑禁用 LTO_BOOTSTRAP而改用STANDARD_BOOTSTRAP （或完全禁用BOOTSTRAP），以 防
a

问题。

• pkubaj@ 还添加了 lang/gcc12 和 lang/gcc13-devel 端口， 并将 lang/gcc9 更新到
9.5。

• 在这三个变化方面仍然需要帮助，以便与上游的 GCC 一起工作（需要 src 的专业知 识，而不是 ports）。

□ 上游的 lang/gcc11/patch-gets-no-more  

□ 上游 lang/gcc11/patch-arm-unwind-cxx-support  

□  https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=256874  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

Valgrind - 对13.1/14.0链接进行了大量的错误修复和更新
Valgrind主页URL: https://www.valgrind.org/
Valgrind新闻网址: https://www.valgrind.org/docs/manual/dist.news.html

联系。Paul Floyd pjfloyd@wanadoo.fr

在过去的几个月里，FreeBSD上的Valgrind已经进行了相当多的错误修正。特别是，i386 版本在很大程度上 "抓住了
与其更大的兄弟amd64一起。
﻿devel/valgrind-devel端口已经提升到3.20.0.g20220612,1，其中包括以下所有变化。如 果你经常使用Valgrind ，请
转到Valgrind-devel。

以下是自 Valgrind 3.19.0 发布以来的变化列表（该版本是与 devel/valgrind 移植 一起提供的版本）。

• 如果在Valgrind为系统调用保存携带标志时有信号到达，则信号恢复不正确。

• 修正了从ld后9版生成的PT_LOADs中读取DWARF调试信息，它将RW段分成两部分， 这主要影响到共享库（.so文件）。

• 在 i386 上正确实现线程 GDTs 的管理，这限制了应用程序只能创建 8192 个线 程。

• 使'brk'的第一页在寻址时无效

• 分析和清理回归测试套件，特别是调整i386的泄漏测试，以避免检测到ECX中 遗留的指针可能造成的泄漏。

• 让lldb可以读取corredumps。

• 通过C分配的函数来改进errno的设置

• 修正用llvm-devel(15.0.0)构建Valgrind的问题 对

于FreeBSD 13.1 / 14.0，有以下几点

• funlinkat, copy_file_range, swapoff, shm_open2的系统调用包装器。

• 在fcntl中增加K_INFO处理功能

• 增加对新的auxv条目的处理

• 为DRD和Helgrind增加了一些默认的抑制措施

现在有一个初始版本的 vgdb invoker 支持 - 这允许 vgdb 使用 ptrace 来强迫
valgrind 轮询 gdb 命令。这在 ports 版本中还不能使用。
﻿这并没有留下多少悬而未决的问题。我预计14.0和更新版本的llvm将继续需要支持。 除此以外，还有

• 错误信息的一些小问题，获得正确的源信息

• 更好的核心转储（低优先）。

• 为Helgrind处理TLS （线程本地存储）（如果不是不可能的话，也很 难）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

FreeBSD上的Pantheon桌面链接。
基本操作系统网址：https://elementary.io
开发库URL：https://codeberg.org/olivierd/ freebsd-ports- elementary

联系方式。Olivier Duchateau duchateau.olivier@gmail.com

Pantheon桌面环境是为初级操作系统设计的。它建立在GNOME技术之上（如Mutter、 GNOME Shell、GTK 3和4），并且是用Vala编写的。

我们的目标是为用户提供一个新的桌面。有些功能没有得到很好的支持，但我们可 以有完整的会议。

仓库包含Mk/Uses框架 elementary.mk ，官方应用程序，以及依赖x11-toolkits/granite 的策划的端口（共56个新端口）。

我已经提交了几个补丁，特别是。

• x11-toolkits/granite7

• 开发/libgee更新至0.20.5 bug #262893

• sysutils/bamf更新至0.5.6 bug #264203 打开

任务
﻿ • 增加对用户设置的支持（它非常以Ubuntu为中心）。

• 完成移植翼板-指示器-电源（电源管理）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━

特点 英特尔的igt-gpu-tools的完整移植 链接。FreeBSD Wiki项目页面URL: https://wiki.freebsd.org/SummerOfCode2022Projects/ImprovingTheLinuxKPICompatibilityLayerForTheFreeBSDGraphicsStack 状态报告 URL: https://cdaemon.com/tags/gsoc2022

联系方式。Jake Freeland jfree@freebsd.org

英特尔的 igt-gpu-tools 作为一个通用的测试套件，用于 Linux 上的 drm 驱动。igt- gpu-tools 套件被分成针对 kms、内存管理和命令提交的测试和工具。该工具提供低级别的报告用于透明地跟踪内核变化和高效地调试现代drm驱动。

将这个项目移植到 FreeBSD 上，可以为 FreeBSD 的 LinuxKPI 驱动的 drm 驱动的未来版本 带来更大的稳定性。一个合适的 kms 驱动的测试套件也可以增加代码输出，使 FreeBSD 的桌面体验与 Linux 代码库同步。

该项目在 FreeBSD 的 Google Summer of Code 项目下正式开始，于 2022 年 6月 13 日.我改编的代码可以用非 FreeBSD 兼容的片段进行编译移除。我们的计划是以符合 POSIX 的方式重新实现这些被剥离的组件。

值得注意的不兼容代码包括： debugfs、 libkmod、 libprocps、 Linux 性能事件，以及 Linux userfaultfd。如果您愿意协助将 libkmod 或 libprocps 移植到 ports 树中， 请不要犹豫， 与我联系。

当 FreeBSD 兼容代码完成后，我将在 FreeBSD 14.0-CURRENT 上使用大量的图形处理器运行修改后的 igt 测试。如果一切顺利的话。项目的差异将被提交到 ports 树中。 赞助商。FreeBSD 的谷歌代码之夏

## FreeBSD 13.1 发行说明

> 原文链接 <https://www.freebsd.org/releases/13.1R/relnotes/>

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

根据 /usr/src/UPDATING 中的说明，可以支持基于源代码的升级 (那些基于从源代码重新编译 FreeBSD 基本系统的升级) 。

所有 powerpc 架构的用户，在成功安装内核和 world 之后，需要手动运行 `kldxref /boot/kernel`。

> **只有在备份了所有数据和配置文件之后，才能尝试升级 FreeBSD。**

> **升级之后，sshd (来自 OpenSSH 8.8p1) 将不接受新的连接，直到它被重新启动。在安装了新的用户空间之后，要么重新启动(按照源码升级程序中的规定)，要么执行 service sshd 重启。**

### 用户空间

本节涵盖了对用户空间应用程序、贡献的软件和系统实用程序的更改和添加。

#### 用户空间配置的变化

在 /etc/defaults/rc.conf 中的 rtsol(8) 和 rtsold(8) 默认加入了 `-i` 标志，a0fc5094bf4c (由 https://www.patreon.com/cperciva 赞助)

用户空间应用程序的变化
在 rtsol(8) 和 rtsold(8) 中加入了 `-i` 选项，以禁用零到一秒之间的随机延迟，从而加快了启动过程。8056b73ea163 (由 https://www.patreon.com/cperciva 赞助)

对于 64 位架构，基本系统在构建时默认启用了位置独立可执行文件 (PIE) 支持。你可以使用 `WITHOUT_PIE` 参数来禁用它。这需要一个干净的构建环境。396e9f259d96

有一个新的 zfskeys rc(8) 服务脚本，它允许在启动时自动解密用 ZFS 本地加密的 ZFS 数据集。请参阅 rc.conf(5) 手册以了解更多信息。33ff39796ffe, 8719e8a951b7 (由 Modirum 和 Klara Inc.赞助)

bhyve(8)中的 NVMe 模拟已经升级到 NVMe 规范的 1.4 版本，b7a2cf0d9102 - eae02d959363

bhyve(8) 中针对大型 IO 的 NVMe iovec 结构已被修复。这个问题是由 Rocky Linux 8.4 中包含的 UEFI 驱动程序暴露的。

为巴西葡萄牙语 ABNT2 键盘增加了额外的 Alt Gr 映射。310623908c20

chroot 工具现在支持非特权操作了，chroot(8) 程序现在有了 `-n` 选项来启用它。460b4b550dc9 (由 EPSRC 赞助)

对 CAM 库进行了修改，以便在解析设备名称之前对其使用 realpath(3) ，这使得诸如 camcontrol(8) 和 smartctl(8) 等工具在使用符号链接时能够更加友好，e32acf95ea25

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

内核的一般变化
powerpc64 上串行控制台的输出损坏已经被修复。

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
ZFS 的变化
ZFS 已经升级到 OpenZFS 2.1.4 版本。OpenZFS 的发行说明可以在 https://github.com/openzfs/zfs/releases 找到。

#### NFS 的变化
两个新的守护进程 rpc.tlsclntd(8) 和 rpc.tlsservd(8)，现在已经默认在 amd64 和 arm64 上建立了。它们提供了对 NFS-over-TLS 的支持，这在题为“实现远程过程调用默认加密”的互联网草案中有所描述。这些守护进程是在指定 WITH_OPENSSL_KTLS 的情况下建立的。它们使用 KTLS 来加密/解密所有的 NFS RPC 消息流量，并通过 X.509 证书提供可选的机器身份验证。2c76eebca71b 59f6f5e23c1a

用于 NFSv4 挂载的默认次要版本已被修改为 NFSv4 服务器支持的最高次要版本。这个默认值可以通过使用 minorversion mount 选项来覆盖。8a04edfdcbd2

增加了一个新的 NFSv4.1/4.2 挂载选项 nconnect，可以用来指定挂载时使用的 TCP 连接数，最多为16个。第一个（默认）TCP 连接将被用于所有由小型 RPC 消息组成的 RPC。由大型 RPC 消息组成的 RPC(Read/Readdir/ReaddirPlus/Write)将以轮流方式在其他 TCP 连接上发送。如果 NFS 客户端或 NFS 服务器有多个网络接口聚合在一起，或者有一个使用多个队列的网络接口，这可以提高挂载的 NFS 性能。9ec7dbf46b0a

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

由于大部分的32位测试是由开发人员在 64 位硬件上使用 lib32 库，并在内核中使用 `COMPAT_FREEBSD32` 选项来完成，所以这种改变可以确保更好的覆盖率和用户体验。这也与大多数 Linux® 发行版已经做了相当长一段时间的工作相一致。

预计这将是 i386 中默认 CPUTYPE 的最后一次改变。

>**这一变化并不影响 FreeBSD 12.x 系列的发布。**

