# 第 1.7 节 FreeBSD 子项目

>**警告**
>
>正在校对，请谨慎参考。

本节是对 FreeBSD 基金会赞助的项目进行的解释。

本页面是对 [Projects](https://freebsdfoundation.org/our-work/projects/) 的翻译。


## FreeBSD 基金会赞助和社区贡献的特色 FreeBSD 项目

FreeBSD 基金会通过资金和资源支持 FreeBSD 操作系统的开发活动，重点是提升其安全性、性能和可用性。我们与社区携手合作，共同努力，确保 FreeBSD 的长期生命力。

基金会参与的开发项目由多种因素决定，包括与核心团队讨论需要填补的开发空白、该开发工作对改进项目的总体影响，以及基金会可提供的资金。以下是这些项目。

如想参与，请访问 [FreeBSD 项目页面](https://www.freebsd.org/projects/)。


## OCI 容器支持

进行中

### 基于 Jails/Bhyve 实现 OCI 容器，支持 Podman 和 Buildah。

**联系人：** Doug Rabson \<[dfr@rabson.org](mailto:dfr@rabson.org)\>

[开放容器计划 (OCI)](https://opencontainers.org/) 为云原生容器格式和运行时制定了开放的行业标准，以确保平台的一致性。一个 [OCI 工作组](https://github.com/opencontainers/wg-freebsd-runtime) 正在为 FreeBSD 定义这些标准，利用 jails 进行实现，并有可能通过 FreeBSD 的 **[bhyve](https://docs.freebsd.org/en/books/handbook/virtualization/#virtualization-host-bhyve)** 虚拟化管理程序支持轻量级虚拟机（这将允许在 FreeBSD 主机上的容器中运行 FreeBSD 以外的其他操作系统）。

FreeBSD 项目成员 Doug Rabson 开发了 **ocijail**，这是一种兼容 OCI 的 FreeBSD jails 运行时实验工具。该工具旨在与容器管理系统（如 Podman 和 Buildah）集成，提供全面的容器管理体验。

**在 OCI 容器中运行应用程序的优势：**

* **标准化：** 确保不同环境之间的兼容性和互操作性，简化开发和部署过程。
* **可移植性：** 封装应用程序及其依赖项，使其能够在任何支持 OCI 的环境中一致运行。
* **高效性：** 轻量且高效，具备快速启动时间和最佳资源利用率，减少了与传统虚拟机相比的开销。
* **隔离性：** 提供类似虚拟机的强隔离功能，但开销较小，适合微服务和现代架构。它确保应用程序独立安全运行，防止冲突并增强系统稳定性。

Doug Rabson 的 [GitHub 仓库](https://github.com/dfr/ocijail) 提供了与 Podman 和 Buildah 集成的初始代码。您还可以观看 Doug Rabson 在 Open Source Summit Seattle 前的 Container Plumbing Day 活动上关于 **ocijail** 实现的演讲 [这里](https://www.youtube.com/watch?v=pggcc6fi-ow)。

Doug 还撰写了一篇[文章](https://freebsdfoundation.org/freebsd-container-images/)，讨论了预构建的 FreeBSD OCI 容器镜像的实现选项。FreeBSD 项目设想将使用现有的容器镜像基础设施（例如 Docker Hub 或 [GitHub 容器注册表](https://github.blog/2020-09-01-introducing-github-container-registry/)）进行管理，或者通过 FreeBSD 自有基础设施托管镜像注册表。

更多信息请访问：**[ocijail (GitHub)](https://github.com/dfr/ocijail)**

## UnionFS 稳定性与增强

进行中

### UnionFS 项目旨在稳定并增强其在 FreeBSD 上的实用性，重点包括：支持对只读文件系统的表面修改，支持多个共享相同基础的 jails 并简化其升级，以及通过分层的预打包镜像促进容器场景的实现。

**联系人：** Olivier Certner \<[olce@freebsd.org](mailto:olce@freebsd.org)\>

由 Olivier Certner 领导的 FreeBSD 上的 UnionFS 项目专注于增强和稳定 UnionFS 的功能，特别是涉及分层文件系统、jails、容器和存储优化的场景。Jason Harmening 多年来一直致力于 UnionFS 的开发，继续解决诸如 vnode 锁定、whiteout 管理和其他系统性问题等关键问题。该项目涉及大量代码重写，并进行精心的协调，以确保变更的合理性和与项目目标的一致性。重要的审查包括 D44288、D44601、D44788 和 D45398。

**项目的主要贡献：**

1. **UnionFS 功能：**

    * **表面修改：** 允许对只读文件系统（例如 CDROM、NFS）进行更改，而不修改原始文件。适用于创建临时或永久的私人副本。
    * **Jails：** 支持多个 jails 共享基础文件系统，简化更新并提高存储效率。
    * **容器：** 支持具有可修改顶层的预打包容器镜像，类似于 Docker。
    * **存储优化：** 将 HDD 支持的文件系统堆叠在 SSD 支持的文件系统上，优化存储使用，同时利用二者的优势。
2. **协调与开发：**

    * Olivier Certner 与 Jason Harmening 协同，继续开发和稳定 UnionFS。Certner 的方法是尽量减少变更的范围，同时确保变更与重写 UnionFS 大部分代码的总体目标相一致。
3. **审查贡献：**

    * **D44288：** 实现了 VOP\_UNP\_\*，并移除了对 VSOCK vnode 的特殊处理。
    * **D44601：** 解决了对 vnode 私有数据的非法访问问题，并提出了强制卸载的测试方案。
    * **D44788：** 修复了 unionfs\_rename 中的多个锁定问题，确保变更最小化以保证稳定性。
    * **D45398：** 重新设计了锁定方案，使其仅锁定一个 vnode，经过多轮审查后于 7 月 13 日最终提交。
4. **咨询：**

    * **Whiteout 处理 (D45987)：** 与 Kirk McKusick 和 Jason Harmening 合作，解决在 tmpfs 中重命名/rmdir 操作期间 whiteout 条目的问题，涉及 UnionFS 导出的元数据。

此项目是一项全面的努力，旨在确保 UnionFS 可靠、高效，并适用于 FreeBSD 的现代用例，包括 jails、容器和复杂的存储配置。


## OpenZFS 分级速率限制

进行中

### 该项目旨在通过引入类似配额可配置的分级速率限制，控制读/写操作次数和读/写带宽，从而提升系统性能和资源管理。

**联系人：** Pawel Dawidek \<[pjd@freebsd.org](mailto:pjd@freebsd.org)\>

FreeBSD 的 OpenZFS 分级速率限制项目旨在通过引入分级速率限制大幅提升 OpenZFS 文件系统的功能。这些速率限制可像配额一样进行配置，用于控制读/写操作次数和读/写带宽，从而提高系统性能并优化资源管理。

OpenZFS 非常适合大规模和高要求的应用程序，如虚拟化和容器化（使用 jails 框架），这些应用程序需要对资源消耗进行精确控制。该项目将实现限制读/写/总操作次数以及读/写/总带宽的功能。限制将在 ZPL（ZFS POSIX 层）强制执行，确保下层数据集不会超过其父数据集上配置的限制。

**主要功能：**

* **分级强制执行：**  限制将在 ZPL 层强制执行，确保下层数据集不会超过其父数据集上配置的限制。
* **六个新属性：**

  * **ratelimit bw read：** 限制每秒读取的字节数。
  * **ratelimit bw write：** 限制每秒写入的字节数。
  * **ratelimit bw total：** 限制每秒可以读取或写入的总字节数。
  * **ratelimit op read：** 限制每秒的读操作次数（数据或元数据读取）。
  * **ratelimit op write：** 限制每秒的写操作次数（数据或元数据写入）。
  * **ratelimit op total：** 限制每秒读或写操作（数据或元数据）的总次数。

这些增强功能旨在提供对资源消耗的精确控制，使 OpenZFS 更加适用于高需求环境。通过实施分级速率限制，该项目确保了资源管理的高效和有效性，提升了 FreeBSD 操作系统的整体稳健性和可靠性。

**更多信息：**  [OpenZFS 分级速率限制 (GitHub)](https://github.com/openzfs/zfs/pull/16205)


## AMD IOMMU

进行中

### 开发完整的 FreeBSD AMD IOMMU（输入输出内存管理单元）驱动的项目。

**联系人：** Konstantin Belousov \<[kib@FreeBSD.org](mailto:kib@FreeBSD.org)\>

由 Advanced Micro Devices（AMD）与 FreeBSD 基金会共同发起的新项目，旨在开发完整的 FreeBSD AMD IOMMU（输入输出内存管理单元）驱动程序。此项目的目标是使 FreeBSD 完全支持超过 256 核的系统，并集成高级功能，如 CPU 映射和 bhyve 虚拟化支持。

开发 AMD IOMMU 驱动对于提升 FreeBSD 管理高核数系统的能力至关重要，有助于优化性能并确保强大的资源管理。该驱动将促进硬件资源的高效分配，改善 FreeBSD 在高需求环境中的整体功能性和可扩展性。

**更多信息：**  **[Konstantin Belousov 的代码提交 (GitHub)](https://github.com/freebsd/freebsd-src/commits/main/?author=kostikbel)**

## FreeBSD 图形安装程序

进行中

### **开发 FreeBSD 图形化安装界面的项目**

**联系人：** Pierre Pronchery \<[pierre@freebsdfoundation.org](mailto:pierre@freebsdfoundation.org)\>

对于首次尝试新操作系统的用户来说，安装过程是他们面临的第一个挑战，也是他们对系统的初步印象来源。如今，大多数操作系统安装程序都配备了图形界面，如 RedHat Enterprise Linux、Ubuntu 和 Debian GNU/Linux 等流行系统中所见。这种图形化方式在 UNIX 系统（包括 FreeBSD）中也变得越来越普遍。无论用户的技术水平如何，安装过程对于公众对该平台的看法至关重要。

多个项目已将 FreeBSD 转化为面向桌面的系统，其中 GhostBSD 是一个显著例子，它提供了图形化安装程序。然而，GhostBSD 的安装程序依赖于由 Python 驱动的 Gtk+ 界面，如果将其整合到 FreeBSD 常规的镜像生成过程中，可能会大幅增加安装介质的体积。此外，这一方法还需要在端口树中引入并维护新的项目。

为了解决这个问题，提出了一个 BSD 许可证下 man:Xdialog[1] 的替代方案，并借鉴了现有的 man:bsdinstall[8] 和 man:bsdconfig[8] 工具的知识。这个新工具名为 man:gbsddialog[1]，将提供图形化安装功能，同时与当前的安装程序基础设施共享资源。与 2006 年发布的过时的 Xdialog 不同，gbsddialog 提供了一个现代化、高效的替代方案，确保占用最小的空间并保持 FreeBSD 的简洁镜像生成流程。

在 FreeBSD 14.0 版本发布后，完成了一个概念验证原型。FreeBSD 基金会随后提供了两个月的时间以完成一个可用的实现。该项目最终在 2024 年 AsiaBSDCon 大会的 WIP 环节中展示了功能齐全的图形安装程序，标志着 FreeBSD 安装过程在用户友好性和视觉吸引力方面的重大进展。

**更多信息：**  **[图形安装程序 (GitHub)](https://github.com/Jehops/freebsd-doc/blob/2024q2_ff/website/content/en/status/report-2024-01-2024-03/bsdinstall.adoc)**

## FreeBSD 的 RISC-V 64 位支持

进行中

### **为 64 位 RISC-V 架构提供支持的项目**

**联系人：** Mitchell Horne \<mhorne@FreeBSD.org\>

**联系人：** Ruslan Bukin \<br@FreeBSD.org\>

**联系人：** Jari Sihvola \<jsihv@gmx.com\>

FreeBSD/RISC-V 项目旨在为 [RISC-V 指令集架构](https://riscv.org/) 提供 FreeBSD 的支持。

**更多信息：**  **[RISC-V 支持](https://wiki.freebsd.org/riscv)**  **(FreeBSD.org)**

## FreeBSD 的视觉辅助子系统

进行中

### 为盲人、低视力和色盲用户提供子系统的项目

**联系人：** Joe Mingrone \<jrm@freebsdfoundation.org\>

该项目将为盲人、低视力和色盲用户提供一个“视觉辅助子系统”的起始点。新功能将包括盲文刷新显示框架、虚拟终端控制台的通信通道、语音合成器、高对比度 TUI 工具和一本文档化 FreeBSD 上可用辅助技术的辅助技术书籍。

项目交付物包括：

- 修改基础系统中的 TUI 工具，以提供高对比度选项，可能处理 GUI 终端模拟器和 vt(4) 的“NO COLOR”环境变量。手册将更新以描述新选项。
- 新选项可以通过启动对话框菜单选择“安装”或“高对比度安装”来以高对比度运行 bsdinstall(8)。
- 为 vt(4) 和语音合成器提供新通信方法。手册将更新以描述新功能。
- 盲文设备框架，可能作为 https://brltty.app 的端口，具有其盲文刷新显示“驱动程序”。如果时间允许，还包括其语音能力功能。
- 新工具实现 bsdinstall(8) 对话框，作为适合屏幕阅读器的简单文本界面。
- 新的“语音安装”选项通过新的 CLI 工具运行 bsdinstall(8)。该功能将作为概念验证提供（会议和社交网络的视频和演示），因为语音合成器和 BRLTTY 在类似 GPL 的许可下发布。
- 在文档库中新增“可访问性”书籍，以描述新的视觉辅助子系统和端口树中的工具。

## 音频改进

进行中

### 加强 FreeBSD 的音频堆栈，以改善对现代音频硬件和软件应用程序的支持。

**联系人：** Christos Margiolis \<[christos@FreeBSD.org](mailto:christos@FreeBSD.org)\>

尽管以其高质量著称，FreeBSD 的音频堆栈一直处于维护不足的状态。一个新项目旨在全面增强该堆栈，解决框架、实用程序和内核驱动程序的 bug，以改善整体功能。

近期开发中已经取得了几项重大改进。FreeBSD 14.1-RELEASE 和 14-STABLE 现已支持异步音频设备分离，提供了更灵活的音频设备管理。过时的 “snd_clone” 框架已被 DEVFS_CDEVPRIV(9) 取代，该框架也随 FreeBSD 14.1-RELEASE 和 14-STABLE 一同发布，现代化了设备管理框架。

音频系统进行了多次崩溃和 bug 修复，并且在笔记本电脑上对 man:snd_hda[4] 的支持得到了改善，确保了更稳定可靠的音频性能。OSS API 的增强改善了 SNDCTL_AUDIOINFO 和 SNDCTL_ENGINEINFO IOCTL 的实现，从而提高了兼容性和功能。

新实现包括启动 man:audio[3]，一个 OSS 音频和 MIDI 库，以及接管 man:virtual_oss[8] 的维护，这两者都为扩展 FreeBSD 音频堆栈的功能作出了贡献。

展望未来，该项目计划开发新的 man:audio[8] 实用程序和蓝牙管理实用程序，进一步改善用户体验。还计划对 man:mixer[3] 和 man:mixer[8] 进行增强。此外，项目将改进文档和测试套件，以确保全面的测试和用户指导。还在进行一项实验尝试，以自动化 man:snd_hda[4] 引脚补丁，如果成功，将显著简化音频配置。

这些努力旨在全面提升 FreeBSD 的音频能力，确保更好的用户支持和功能，并巩固 FreeBSD 在高质量音频性能方面的声誉。

**更多信息：**  **[音频堆栈改进 (GitHub)](https://github.com/Jehops/freebsd-doc/blob/2024q2_ff/website/content/en/status/report-2024-04-2024-06/audio.adoc)**

## CI 增强

进行中

### 改进持续集成 (CI) 基础设施，以确保更可靠和高效的软件开发和测试过程。

**联系人：** Li-Wen Hsu: \<[lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)\>

在 2024 年第一季度，我们与项目贡献者和开发人员合作，解决他们的测试需求。同时，我们与外部项目和公司合作，通过在 FreeBSD 上进行更多测试来增强他们的产品。

在 2024 年第一季度，FreeBSD 项目增强了其持续集成 (CI) 基础设施。由 Christos Margiolis 领导的团队与贡献者和外部项目合作，以满足测试需求并改善在 FreeBSD 上的产品测试。

关键成就包括使用来自退役机器的零件升级测试虚拟机的磁盘和内存，将 stable/13 任务的构建环境更新为 13.3-RELEASE，并将主分支上的 i386 构建过渡为使用 amd64 的交叉构建。

正在进行的努力包括合并关键审查，向 CI 集群添加新硬件，以及设计预提交 CI 系统和拉取/合并请求系统。团队还在致力于利用 CI 集群构建发布工件，简化 CI/测试环境设置，以及重新设计硬件测试实验室。

未来计划包括收集 CI 任务和想法，为虚拟机客机测试设置公共网络访问，实现裸金属硬件测试套件，添加针对 -CURRENT 的 DRM 端口构建测试，以及运行 ztest 测试。团队的目标是改善 FreeBSD 在 CI 流水线中的支持，并与托管的 CI 提供商合作。

**更多信息：**  **[持续集成 (GitHub)](https://github.com/Jehops/freebsd-doc/blob/2024q2_ff/website/content/en/status/report-2024-01-2024-03/ci.adoc)**

## FreeBSD 作为 Tier I cloud-init 平台

进行中

### 增强对 cloud-init 的支持，使 FreeBSD 成为 Tier I 平台，以改善其在云环境中的集成和可用性。

**联系人：** Mina Galić \<[freebsd@igalic.co](mailto:freebsd@igalic.co)\>

Cloud-init 现已成为在云中设置服务器的标准。在过去一年半的时间里，FreeBSD 在支持 cloud-init 方面取得了显著进展。今年的重点是与 cloud-init 开发者和 FreeBSD 基金会密切合作，增强 FreeBSD，使 cloud-init 团队能够直接测试未来对 FreeBSD 代码路径的更改。

为此，FreeBSD 必须在 LXD（和 Incus）的控制下运行，并由 lxd-agent（或 incus-agent）管理。最近，已经取得了一些显著的改进。一个小型测试框架在 sh 中开发，正在逐步迁移到 OpenTofu/Terraform。该框架安装并测试 cloud-init-devel 和 cloud-init 的最新版本。为支持这一点，创建了一个专用的公共代码库，包含 FreeBSD 13 和 14 在 amd64 和 aarch64 上的 cloud-init-devel 和 cloud-init 的最新版本。

此外，Linux vsock 测试框架也已移植到 FreeBSD。基于 HyperV Socket 驱动程序创建了 VirtIO Socket 驱动程序的驱动程序框架，导致 HyperV 套接字的多个改进。这些改进已部分接受，但仍需更多工作。

最新的 cloud-init 24.1 系列经过测试并发布，修复了长期存在的错误，例如将 /run/cloud-init 移动到 BSD 上的 /var/run/cloud-init，并纠正了 user_groups 的 homedir 参数。此次发布还包括社区贡献的 OpenBSD 代码路径的多个修复。

展望未来，这项工作涉及几个关键任务。完成 FreeBSD VirtIO Socket 驱动程序和修复 Go 的运行时以支持 FreeBSD 上的 VirtIO 是首要任务。将 lxd-agent 的依赖项及 lxd-agent 本身移植到 FreeBSD 也至关重要。这些努力将与对 BSD 上 cloud-init 的进一步改进和在不同云提供商上的额外测试交替进行。

**更多信息：**  **[Cloud-Init (GitHub)](https://github.com/Jehops/freebsd-doc/blob/2024q2_ff/website/content/en/status/report-2024-01-2024-03/cloud-init.adoc)**

## FreeBSD 上的 OpenStack

进行中

### FreeBSD 上的 OpenStack 项目旨在将 OpenStack 云基础设施与 FreeBSD 操作系统无缝集成，利用 FreeBSD 的独特功能，同时保持与 OpenStack 标准的兼容性。

**联系人：** Chih-Hsin Chang \<[starbops@hey.com](mailto:starbops@hey.com)\>，Li-Wen Hsu \<[lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)\>

**第一季度：**

在 2024 年第一季度，该项目取得了重大进展。提交了 BSDCan 2024 的提案，团队参加了 AsiaBSDCon 2024，分享了移植经验并收集了有价值的反馈，这帮助完善了项目的方向。第一阶段的任务进行了审查，进行了必要的调整，并将第二和第三阶段的计划与长期目标进行了对齐。一项关键技术成就是验证了 bhyve 串口控制台通过 TCP 的功能。还制作了一个演示视频，以展示项目的进展和特性。

**第二季度：**

第二季度继续取得进展。团队在 BSDCan 2024 上介绍了“朝着强大的基于 FreeBSD 的云：移植 OpenStack 组件”，这增加了项目的可见性，并吸引了潜在贡献者的兴趣。概念验证（POC）站点从单节点设置扩展到三节点设置，涉及详细的环境设置和网络规划。还启动了将基础迁移到 FreeBSD 15.0-CURRENT 的工作，以保持与最新 FreeBSD 发展的对齐。

此外，手动安装步骤和代码补丁开始转换为 FreeBSD 端口，以简化安装过程。一个重要的里程碑是启动了对 FreeBSD 实例和 OpenStack Ironic 服务主机进行裸机配置的工作。

**未来计划：**

展望下一个季度，重点将放在完善这些进展并进一步增强项目的稳健性和易用性。具体计划包括将 OpenStack 组件从 Xena 版本升级到更近期的版本，因为 Xena 正接近生命周期的尽头。欢迎社区的建议和贡献，以帮助实现这些目标。

**更多信息：**  [OpenStack (GitHub)](https://github.com/Jehops/freebsd-doc/blob/2024q2_ff/website/content/en/status/report-2024-04-2024-06/openstack.adoc)

## WiFi 更新 – Intel 驱动程序和 802.11ac

进行中

### 此更新支持当前一代 Intel WiFi 设备和 802.11ac 标准，以改善无线连接性。

**联系人：** Björn Zeeb \<[bz@freebsd.org](mailto:bz@freebsd.org)\>

在 2023 年 11 月，FreeBSD 基金会启动了一项重大举措，以改善 iwlwifi 驱动程序，该驱动程序对支持 FreeBSD 上的 Intel Wi-Fi 芯片至关重要。这个项目由 FreeBSD 开发者 Cheng Cui 领导，并与 Björn Zeeb 合作，旨在通过多个关键里程碑增强 FreeBSD 的无线功能。

项目的主要目标之一是解决影响 iwlwifi 驱动程序的多个关键问题报告（PR）。在 PR 271979、273985、274382 和 275710 中记录的问题通过系统化和创新的调试技术成功解决。例如，使用铝箔包裹的纸板隔离信号是一种新颖的方法，证明在识别和修复这些问题上效果显著。

该项目还专注于提高系统稳定性。审查和实施补丁显著改善了 FreeBSD 版本 13.3-RELEASE 和即将发布的 14.1 的稳定性。项目强调启用硬件支持的加密功能，这涉及创建 PR 277095 和 277100，以应对复杂的调试场景。

改善对 802.11n 标准的支持是另一个重点领域。该项目通过利用深厚的领域专业知识并采用 Linux 中的 Driver API 跟踪等新调试技术，解决了 PR 276083。这一增强对于推动项目目标和改善 FreeBSD 的无线性能至关重要。

此外，该项目在确保 FreeBSD 13.3 成功发布方面发挥了重要作用。通过重现用户报告的问题并测试后续修复，项目为操作系统的整体可靠性和性能做出了贡献。

增强 iwlwifi 驱动程序的努力改善了 FreeBSD 对 Intel Wi-Fi 的支持。该项目确保了用户更好的无线性能和稳定性。持续的工作将继续提升 FreeBSD 的网络功能，使其成为更强大、更可靠的操作系统。

**更多信息：**  [Wi-Fi 增强（FreeBSD 基金会）](https://freebsdfoundation.org/blog/improving-and-debugging-freebsds-intel-wi-fi-support-cheng-cuis-key-role-in-the-iwlwifi-project/)

---

　　　　以下为已完成部分

---

## Bhyve 改进

对 FreeBSD 虚拟机监视器的各种改进

**联系人：** Chris Moerz \<freebsd@ny-central.org\>

### I/O 性能测量

最近，Bhyve 生产用户之间的讨论强调了正式 I/O 性能分析的必要性。作为回应，团队开始使用一组 shell 脚本和 benchmarks/fio 包测试不同的配置。重点评估不同的存储后端、内存设置、CPU 固定选项以及支持存储和虚拟磁盘的块大小。团队还比较了不同 CPU 制造商以及客户和主机环境的性能。

### 虚拟机工具

FreeBSD 基金会的企业工作组识别出需要类似于 jails 的 Bhyve 工具。这促成了“vmstated”的开发，这是一个使用基本 FreeBSD 工具构建的守护进程和管理实用程序。Vmstated 通过 UCL 配置，提供灵活的虚拟机管理，具有类似于 jail 的命令集和状态转换钩子等功能。该工具已在 ports 集合中作为 sysutils/vmstated 提供，并在 GitHub 上持续更新。欢迎贡献和反馈。

### 文档更新

对 FreeBSD 手册和 Porter 手册进行了几次更新，重点关注虚拟化、Bhyve 配置和管理 Bhyve 客户。正在进行 Bhyve 手册页结构的更新审查，并计划进一步改进内容。欢迎对此次更新提出反馈。

### 为 arm64 客户创建的扁平设备树

Mark Johnston 和 Andrew Turner 合作创建了构建 arm64 bhyve 客户的扁平设备树（FDT）的基本例程。FDT 描述了不同的硬件组件，例如 CPU、内存、UART、PCIe 控制器、中断控制器和平台定时器，客户操作系统应当了解这些组件。

**更多信息：** [Bhyve 更新（GitHub）](https://github.com/Jehops/freebsd-doc/blob/2024q2_ff/website/content/en/status/report-2024-01-2024-03/bhyve.adoc)

## FreeBSD 在 Azure 和 Hyper-V 上

### 自动化 Azure Marketplace 中 FreeBSD 镜像的构建过程

**联系人：**

* Microsoft FreeBSD 集成服务团队: bsdic@microsoft.com
* FreeBSD Azure 发布工程团队: releng-azure@FreeBSD.org
* Wei Hu: whu@FreeBSD.org
* Souradeep Chakrabarti: schakrabarti@microsoft.com
* Li-Wen Hsu: lwhsu@FreeBSD.org

在第一季度，团队成功解决了所有阻塞问题，并在 Azure Marketplace 上发布了 FreeBSD 13.3-RELEASE，使其可以在云环境中供用户使用。

### 进行中的工作：

团队目前专注于几个关键任务：

* **自动化镜像构建和发布过程：**  正在进行的努力旨在自动化镜像构建和发布过程，以将这些改进合并到 FreeBSD 的 src/release/ 仓库中。
* **构建和发布快照构建：**  快照构建正在开发和发布到 Azure 社区画廊，为用户提供最新的开发和更新。

## .NET (dotnet) 移植

### 将“dotnet”本地移植到 FreeBSD，初始版本为 8，后续版本移植正在进行中

**联系人：** Gleb Popov \<[arrowd@freebsd.org](mailto:arrowd@freebsd.org)\>

在 FreeBSD 上对 .NET 的支持（**dotnet**）使开发者能够选择自己喜欢的平台而不受限制。这种兼容性使他们能够利用 FreeBSD 独特的优势，同时保持与 .NET 一致的开发环境。

新的 .NET 本地移植当前可用于 **amd64** 架构（**aarch64** 支持正在进行中），将 .NET 运行时版本 8 带入 FreeBSD。这确保了完全兼容，同时利用了 FreeBSD 的性能和安全特性，使开发者能够充分利用 FreeBSD 的功能。

将 .NET 移植到 FreeBSD 是一个协作努力，涉及主要社区贡献者。Gleb Popov（**arrowd@FreeBSD.org**）维护 .NET 移植，**[thefrank](https://github.com/Thefrank)**、Naram Qashat（**cyberbotx@cyberbotx.com**）和 Szczepan Ćwikliński（**[sec](https://github.com/sec)**）也做出了重要贡献。团队与 dotnet 上游项目积极合作，包括在 GitHub 上提交 PR。他们的共同努力对实现 .NET 在 FreeBSD 上的运行至关重要。

**更多信息：** **[dotnet (GitHub)](https://github.com/dotnet)**

## FreeBSD 集群现代化

### 加强 FreeBSD 项目基础设施、提升其能力，并为用户提供更好的服务的倡议

**联系人：** Joseph Mingrone \<[jrm@freebsdfoundation.org](mailto:jrm@freebsdfoundation.org)\> 和 Philip Paeps \<[phil@freebsd.org](mailto:phil@freebsd.org)\>

FreeBSD 基金会投资超过 10 万美元在芝加哥安装了一套服务器集群。此项投资旨在加强 FreeBSD 项目的基础设施、提升其能力，并为用户提供更好的服务。为了支持这一扩展，基金会与 NYI 合作，后者慷慨地在其芝加哥设施中提供了四个机架。

新的集群配置旨在优化 FreeBSD 项目的运营效率，包括：

* **两台路由器：** 用于引导网络流量。
* **五个软件包构建器：** 旨在加速软件包发布过程。
* **三台通用服务器：** 这些服务器将提升 FreeBSD 项目面向公众和开发者的服务（如 Bugzilla、Git、Phabricator、Wiki 等）的可用性和性能。
* **两个软件包镜像：** 一个在芝加哥的新集群中托管，另一个由加州的 ISC 托管。这些是 FreeBSD 项目日益扩大的 pkg.FreeBSD.org 和 download.FreeBSD.org 服务器网络的一部分，战略性地分布在全球，以提供更快的软件包下载速度。
* **两台 CI 服务器：** 以提高自动化代码测试的速度和效率。
* **一台管理堡垒服务器：** 这是管理集群的安全入口点，运行集群管理团队（clusteradm）工具、集群 DNS、监控以及其他管理系统所需的服务。

这一硬件配置预计将显著提升 FreeBSD 项目的处理能力和服务响应速度。

FreeBSD clusteradm 团队在新集群的集成阶段发挥了关键作用。

* **硬件兼容性和固件调试：** 为确保服务器固件与 FreeBSD 兼容，初期面临的多个障碍需要克服。集群依赖于能够网络启动机器，并要求可靠的带外管理。
* **网络配置和自动化：** 服务器能够可靠启动后，进行了网络配置，包括集群内部 DNS、数据包过滤规则和与互联网的 BGP 会话。
* **自动化和系统配置：** 团队的自动化工具大大简化了服务器的安装和配置。在使用临时 FreeBSD 安装克服了一些启动问题后，服务器被网络启动到集群安装镜像中，并使用标准集群构建进行安装。
* **监控和管理集成：** 团队在管理服务器上安装和配置了监控代理，将新站点集成到项目的中央监控系统中。这使得集群的管理和故障排除更加高效，确保了稳定性和性能。
* **最终系统安装和网络服务设置：** 团队通过使用工具自动化重新安装管理服务器，设置路由和防火墙配置，并在光纤上行链路上启用 BGP 会话，完成了集成工作。这一设置确保了新集群的运行，并优化了性能和安全性。

## Olivier Certner 的杂项更新

完成

### FreeBSD 源代码树各部分的杂项更新。

**联系人：** Olivier Certner \<[olce@freebsd.org](mailto:olce@freebsd.org)\>

在 2024 年第二季度，长期承包商 Olivier Certner 在树的几个不同部分积极工作：

* [rtprio(2)](https://man.freebsd.org/cgi/man.cgi?query=rtprio&sektion=2&format=html)：将每个运行队列的队列数量从 64 更新到 256。
* **Vnode 回收/ZFS ARC 回收：** 审查了 [bug #275594](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=275594) 的修复，与上游沟通以获取和测试回移，并发出了一份 EN 并作为 13.3-RELEASE-p2 应用，同时开始了长期工作以改进 vnode 回收机制，并确保 ZFS 传递正确的信息。
* **ULE 调度器：** 更新为在单个运行队列上工作，而不是为满足 POSIX 合规性而使用 3 个运行队列，以处理 SCHED\_FIFO/SCHED\_RR 优先级级别的数量。
* **杂项：** 进行了多达 26 项评审、软件包更新，并调查了 DRM 问题。
* 在 FreeBSD Journal 发布了 [EuroBSDCon 2023 大会报告](https://freebsdfoundation.org/eurobsdcon-2023/)。

## Center for Internet Security (CIS) FreeBSD 14 基准

完成

这是一个全面的安全强化指南，旨在帮助安全高效地配置 FreeBSD 系统。

**联系人：** Moin Rahman \<[bofh@freebsd.org](mailto:bofh@freebsd.org)\>

此新 CIS 基准涵盖了关键领域，包括：

* **用户和组管理：** 采用最佳实践指南安全地管理用户账户和组。
* **服务配置：** 关于安全配置基本服务的建议。
* **文件系统和权限：** 管理文件系统安全和权限的最佳实践。
* **网络配置：** 提供保护网络设置以防止未经授权访问和攻击的安全建议。
* **审计和日志记录：** 设置强大日志和审计的说明，以监控系统活动。

该基准是系统管理员、安全审计员以及必须遵守行业标准和法规的组织的重要资源。我们鼓励 FreeBSD 社区提供反馈并为这些指南的持续完善做出贡献。安全工作在协作中最为有效，我们期待看到社区如何利用和扩展这一新资源。

我们对 FreeBSD 社区在此基准中的重要贡献表示衷心感谢。特别感谢基准撰写者 Moin Rahman、编辑 Carole Fennelly、评审 Jason Kafer 和 Rick Miller、项目经理 Joe Mingrone，以及 CIS 的 Justin Brown 和 Eric Pinnell。同时，我们也感谢 [Verisign](https://www.verisign.com/) 对创建 CIS FreeBSD 14 基准部分费用的资助，以及对 [FreeBSD 基金会的慷慨捐赠者](https://freebsdfoundation.org/our-donors/donors/) 给予的支持。

**更多信息：** [FreeBSD 14 基准](https://freebsdfoundation.org/blog/new-cis-freebsd-14-benchmark-secure-your-systems-with-expert-guided-best-practices/)（FreeBSD 基金会）

## VPP 在 FreeBSD 上

### 将矢量数据包处理（VPP）框架移植到 FreeBSD，以增强网络性能能力。

**联系人：** Tom Jones \<[tj@freebsdfoundation.org](mailto:tj@freebsdfoundation.org)\>

FreeBSD 上的矢量数据包处理（VPP）项目旨在将 VPP 这一开源的高性能用户空间网络栈移植到 FreeBSD。VPP 通过矢量化操作和并行处理优化数据包处理，非常适合软件定义网络（SDN）和网络功能虚拟化（NFV）应用。该工作于 2023 年 11 月启动，由专注于网络性能的 FreeBSD 开发者 Tom Jones 在 FreeBSD 基金会的合同下领导。

关键里程碑包括修复 VPP 在 FreeBSD 上的构建，以确保其能够编译和运行，验证并添加基本功能，以及开发全面的测试和回归套件以维护可靠性和稳定性。性能基准测试帮助识别和解决潜在瓶颈，并提出改进和优化建议。

文档工作专注于 FreeBSD 特定的 API 和用法，为开发者和用户提供清晰的指导。创建 VPP 的 FreeBSD 移植成功简化了安装和部署，使用户更易于使用。

VPP 的 FreeBSD 移植取得了成功，正在进行的工作旨在进一步增强其能力。不断进行改进和优化，以确保 FreeBSD 的网络性能保持强大和高效，巩固其在高速网络应用中的适用性。

**更多信息：** **[Vector Packet Processor (GitHub)](https://github.com/adventureloop/vpp)**

