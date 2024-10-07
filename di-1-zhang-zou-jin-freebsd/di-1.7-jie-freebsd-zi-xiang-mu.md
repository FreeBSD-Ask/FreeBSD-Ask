# 第 1.7 节 FreeBSD 特色开发项目

>**警告**
>
>正在校对，请谨慎参考。

本节是对 FreeBSD 基金会赞助的项目进行的说明。

本节是对 [Projects](https://freebsdfoundation.org/our-work/projects/) 的翻译。


## FreeBSD 基金会赞助和社区贡献的特色 FreeBSD 项目

FreeBSD 基金会以资金和资源支持 FreeBSD 操作系统的开发活动，重点是提升 FreeBSD 的安全性、性能和可用性。我们与社区携手合作，共同努力，确保 FreeBSD 的恒久生命力。

基金会参与的开发项目由多种因素决定，包括与核心团队讨论需要填补的开发空白、该开发工作对改进项目的总体影响，以及基金会可提供的资金。以下是这些项目。

如想参与，请访问 [FreeBSD 项目页面](https://www.freebsd.org/projects/)。


## OCI 容器支持

正在进行

### 基于 Jail/Bhyve 实现 OCI 容器，支持 Podman 和 Buildah。

**联系人：** Doug Rabson [dfr@rabson.org](mailto:dfr@rabson.org)

[开放容器计划 (OCI)](https://opencontainers.org/) 为云原生容器格式和运行时制定了开放的行业标准，来确保平台的一致性。一个 [OCI 工作组](https://github.com/opencontainers/wg-freebsd-runtime) 正在为 FreeBSD 制定这些标准，利用 jail 进行实现，并有可能通过 FreeBSD 的 **[bhyve](https://docs.freebsd.org/en/books/handbook/virtualization/#virtualization-host-bhyve)** 虚拟化管理程序支持轻量级虚拟机（可在 FreeBSD 主机上的容器中运行 FreeBSD 以外的其他操作系统）。

FreeBSD 项目成员 Doug Rabson 开发了 **ocijail**，这是一种兼容 OCI 的 FreeBSD jail 运行时实验工具。该工具旨在与容器管理系统（如 Podman 和 Buildah）集成，提供完善的容器管理体验。

**在 OCI 容器中运行应用程序的优势：**

* **标准化：** 确保不同环境间的兼容性和互操作性，简化开发和部署过程。
* **可移植性：** 封装应用程序及其依赖项，使其能够在任何支持 OCI 的环境中一致运行。
* **高效性：** 轻量且高效，具备快速启动时间和最佳资源利用率，减少了与传统虚拟机相比的开销。
* **隔离性：** 提供类似虚拟机的强隔离功能，但开销较小，适合微服务和现代架构。它确保应用程序独立安全运行，避免冲突，增强了系统稳定性。

Doug Rabson 的 [GitHub 仓库](https://github.com/dfr/ocijail) 有与 Podman 和 Buildah 集成的初始代码。您还可以观看 Doug Rabson 在 Open Source Summit Seattle 前的 Container Plumbing Day 活动上关于实现 **ocijail** 的演讲 [这里](https://www.youtube.com/watch?v=pggcc6fi-ow)。

Doug 还撰写了一篇[文章](https://freebsdfoundation.org/freebsd-container-images/)，讨论了预构建的 FreeBSD OCI 容器镜像的实现功能。FreeBSD 项目设想将使用现有的容器镜像基础设施（例如 Docker Hub 和 [GitHub 容器注册表](https://github.blog/2020-09-01-introducing-github-container-registry/)）进行管理，或者通过 FreeBSD 自有基础设施托管镜像注册表。

更多信息请访问：**[ocijail (GitHub)](https://github.com/dfr/ocijail)**

## UnionFS 稳定性与增强

正在进行

### UnionFS 项目旨在稳定、增强其在 FreeBSD 上的实用性，重点包括：支持对只读文件系统的表面修改，支持多个共享相同基础的 jail 并简化升级，以及通过分层的预打包镜像促进容器场景的实现。

**联系人：** Olivier Certner [olce@freebsd.org](mailto:olce@freebsd.org)

由 Olivier Certner 领导的 FreeBSD 上的 UnionFS 项目专注于增强和稳定 UnionFS 的功能，特别是涉及分层文件系统、jail、容器和存储优化的场景。Jason Harmening 多年来一直致力于 UnionFS 的开发，持续解决诸如 vnode 锁、whiteout 管理和其他系统性问题等关键问题。该项目涉及大量代码重写，并进行了精心的协调，以确保变更的合理性和与项目目标的一致性。重要的审查包括 D44288、D44601、D44788 和 D45398。

**项目的主要贡献：**

1. **UnionFS 功能：**

    * **表面修改：** 允许对只读文件系统（例如 CDROM、NFS）进行更改，而不修改原始文件。适用于创建临时/永久的私人副本。
    * **Jail：** 支持多个 jail 共享基础文件系统，简化更新，提高存储效率。
    * **容器：** 支持具有可修改顶层的预打包容器镜像，类似于 Docker。
    * **存储优化：** 将 HDD 支持的文件系统堆叠在 SSD 支持的文件系统上，优化存储使用，同时利用二者的优势。


2. **协调与开发：**

    * Olivier Certner 与 Jason Harmening 协作，继续开发和稳定 UnionFS。Certner 的方法是尽量减少变更的范围，同时确保变更与重写 UnionFS 大部分代码的总体目标相一致。

3. **审查贡献：**

    * **D44288：** 实现了 VOP\_UNP\_\*，并移除了对 VSOCK vnode 的特殊处理。
    * **D44601：** 解决了对 vnode 私有数据的非法访问问题，并提出了强制卸载的测试方案。
    * **D44788：** 修复了 unionfs\_rename 中的多个锁定问题，确保变更最小化以保证稳定性。
    * **D45398：** 重新设计了锁方案，使其仅锁定一个 vnode，经过多轮审查后，最终于 7 月 13 日提交。

4. **咨询：**

    * **Whiteout 处理 (D45987)：** 与 Kirk McKusick 和 Jason Harmening 合作，解决了在 tmpfs 中重命名/rmdir 操作期间 whiteout 条目的问题，涉及 UnionFS 导出的元数据。

此项目是一项全方位的努力，旨在确保 UnionFS 可靠、高效，并适用于 FreeBSD 的现代用例，包括 jail、容器和复杂的存储配置。


## OpenZFS 分级速率限制

正在进行

### 该项目旨在通过引入类似配额可配置的分级速率限制，控制读/写操作次数和读/写带宽，从而提升系统性能和资源管理。

**联系人：** Pawel Dawidek [pjd@freebsd.org](mailto:pjd@freebsd.org)

FreeBSD 的 OpenZFS 分级速率限制项目旨在通过引入分级速率限制大幅提升 OpenZFS 文件系统的功能。这些速率限制可像配额一样进行配置，用于控制读/写操作次数和读/写带宽，从而提高系统性能，优化资源管理。

OpenZFS 尤为适合大规模和高要求的应用程序，如虚拟化和容器化（使用 jail 框架），这些应用程序需要对资源消耗进行精确控制。该项目将实现限制读/写/总操作次数以及读/写/总带宽的功能。限制将在 ZPL（ZFS POSIX 层）强制执行，确保下层数据集不会超过其父数据集上配置的限制。

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

正在进行

### 开发完整的 FreeBSD AMD IOMMU（输入输出内存管理单元）驱动的项目。

**联系人：** Konstantin Belousov [kib@FreeBSD.org](mailto:kib@FreeBSD.org)

由 Advanced Micro Devices（AMD）与 FreeBSD 基金会共同发起的新项目，旨在开发完整的 FreeBSD AMD IOMMU（输入输出内存管理单元）驱动程序。此项目的目标是使 FreeBSD 完全支持超过 256 核的系统，并集成高级功能，如 CPU 映射和 bhyve 虚拟化支持。

开发 AMD IOMMU 驱动对于提升 FreeBSD 管理高核数系统的能力至关重要，有助于优化性能并确保强大的资源管理。该驱动将促进硬件资源的高效分配，改善 FreeBSD 在高需求环境中的整体功能性和可扩展性。

**更多信息：**  **[Konstantin Belousov 的代码提交 (GitHub)](https://github.com/freebsd/freebsd-src/commits/main/?author=kostikbel)**

## FreeBSD 图形化安装程序

正在进行

### 开发 FreeBSD 图形化安装界面的项目

**联系人：** Pierre Pronchery [pierre@freebsdfoundation.org](mailto:pierre@freebsdfoundation.org)

对于首次尝试新操作系统的用户来说，安装过程是他们面临的第一个挑战，也是他们对系统的原初印象来源。如今，大多数操作系统安装程序都搭载了图形界面，如 RedHat Enterprise Linux、Ubuntu 和 Debian GNU/Linux 等流行系统中所见。这种图形化方式在 UNIX 系统（包括 FreeBSD）中也变得越来越普遍。无论用户的技术水平如何，安装过程对于公众对该平台的看法至关重要。

有多个项目已将 FreeBSD 转化为面向桌面的系统，其中 GhostBSD 就是个重要的例子，它提供了图形化安装程序。然而，GhostBSD 的安装程序依赖于由 Python 编写的 Gtk+ 界面，如果将其整合到 FreeBSD 常规的镜像生成过程中，可能会大幅增加安装介质的体积。此外，这一方法还需要在 Ports 中引入、维护新的项目。

为了解决这个问题，提出了一个 BSD 许可证下 man:Xdialog[1] 的替代方案，并借鉴了现有的 man:bsdinstall[8] 和 man:bsdconfig[8] 工具的知识。这个新工具名为 man:gbsddialog[1]，将提供图形化安装功能，同时与当前的安装程序基础设施共享资源。与 2006 年发布的过时的 Xdialog 不同，gbsddialog 提供了一个现代化、高效的替代方案，确保占用最小的空间并保持 FreeBSD 的简洁镜像生成流程。

在 FreeBSD 14.0 版本发布后，完成了概念验证原型。FreeBSD 基金会随后用两个月的时间完成了一个可用的实现。该项目最终在 2024 年 AsiaBSDCon 大会的 WIP（半成品）环节中展示了功能齐全的图形化安装程序，标志着 FreeBSD 安装过程在用户友好性和视觉吸引力方面的重大进展。

**更多信息：**  **[图形安装程序 (GitHub)](https://github.com/Jehops/freebsd-doc/blob/2024q2_ff/website/content/en/status/report-2024-01-2024-03/bsdinstall.adoc)**

## FreeBSD 对 RISC-V 64 位的支持

正在进行

### 为 64 位 RISC-V 架构提供支持的项目

**联系人：** [Mitchell Horne](mhorne@FreeBSD.org)

**联系人：** [Ruslan Bukin](br@FreeBSD.org)

**联系人：** [Jari Sihvola](jsihv@gmx.com)

FreeBSD/RISC-V 项目旨在为 [RISC-V 指令集架构](https://riscv.org/) 提供 FreeBSD 的支持。

**更多信息：**  **[RISC-V 支持](https://wiki.freebsd.org/riscv)**  **(FreeBSD.org)**

## FreeBSD 的视觉辅助子系统

正在进行

### 为盲人、低视力和色盲用户提供子系统的项目

**联系人：** [Joe Mingrone](<jrm@freebsdfoundation.org)

该项目将为盲人、低视力和色盲用户提供一个“视觉辅助子系统”的开端。新功能将包括盲文刷新显示框架、虚拟终端控制台的通信通道、语音合成器、高对比度 TUI 工具和一本文档化 FreeBSD 上可用辅助技术的辅助技术书籍。

项目交付物包括：

- 修改基础系统中的 TUI 工具，以提供高对比度选项，可能处理 GUI 终端模拟器和 vt(4) 的“NO COLOR”环境变量。更新手册描述新功能。
- 新选项可以通过启动对话框菜单选择“安装”和“高对比度安装”来以高对比度运行 bsdinstall(8)。
- 为 vt(4) 和语音合成器提供新通信方法。手册将更新以描述新功能。
- 盲文设备框架，可能作为 https://brltty.app 的 Port，具有其盲文刷新显示“驱动程序”。如果时间允许，还包括其语音能力功能。
- 新工具实现 bsdinstall(8) 对话框，作为适合屏幕阅读器的简单文本界面。
- 新的“语音安装”选项通过新的 CLI 工具运行 bsdinstall(8)。该功能将作为概念验证提供（会议和社交网络的视频和演示），因为语音合成器和 BRLTTY 在类似 GPL 的许可下发布。
- 在文档库中新增“可访问性”书籍，以描述新的视觉辅助子系统和 Ports 中的工具。

## 改进音频

正在进行中

### 加强 FreeBSD 的音频堆栈，以改善对现代音频硬件和软件应用程序的支持。

**联系人：** Christos Margiolis [christos@FreeBSD.org](mailto:christos@FreeBSD.org)

尽管以其高质量著称，但 FreeBSD 的音频堆栈一直处于欠缺维护的状态。一个新项目旨在全面增强该堆栈，解决框架、实用程序和内核驱动程序的 bug，以改善整体功能。

近期开发中已经取得了几项重大改进。FreeBSD 14.1-RELEASE 和 14-STABLE 现已支持异步音频设备分离，提供了更灵活的音频设备管理。过时的 “snd_clone” 框架已被 DEVFS_CDEVPRIV(9) 取代，该框架也随 FreeBSD 14.1-RELEASE 和 14-STABLE 一同发布，使设备管理框架现代化。

音频系统进行了多次崩溃和 bug 修复，并且在笔记本电脑上，对 man:snd_hda[4] 的支持得到了改善，确保了更稳定可靠的音频性能。OSS API 的增强改善了 SNDCTL_AUDIOINFO 和 SNDCTL_ENGINEINFO IOCTL 的实现，从而提高了兼容性和功能。

新实现包括启动 man:audio[3]，一个 OSS 音频和 MIDI 库，以及接管 man:virtual_oss[8] 的维护，这两者都为扩展 FreeBSD 音频堆栈的功能作出了贡献。

展望未来，该项目计划开发新的 man:audio[8] 工具和蓝牙管理工具，进一步改善用户体验。还计划对 man:mixer[3] 和 man:mixer[8] 进行增强。此外，项目将改进文档和测试套件，以确保全面的测试和用户指导。还在进行一项实验尝试，以自动化 man:snd_hda[4] 引脚补丁，如果成功，将显著简化音频配置。

这些努力旨在全面提升 FreeBSD 的音频能力，确保更好的用户支持和功能，并巩固 FreeBSD 在高质量音频性能方面的声誉。

**更多信息：**  **[音频堆栈改进 (GitHub)](https://github.com/Jehops/freebsd-doc/blob/2024q2_ff/website/content/en/status/report-2024-04-2024-06/audio.adoc)**

## CI 增强

正在进行

### 改进持续集成 (CI) 基础设施，以确保更可靠和高效的软件开发和测试过程。

**联系人：** Li-Wen Hsu: [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

在 2024 年第一季度，我们与项目贡献者和开发人员合作，解决他们的测试需求。同时，我们与外部项目和公司合作，通过在 FreeBSD 上进行更多测试来增强他们的产品。

在 2024 年第一季度，FreeBSD 项目增强了其持续集成 (CI) 基础设施。由 Christos Margiolis 领导的团队与贡献者和外部项目合作，以满足测试需求并改善在 FreeBSD 上的产品测试。

关键成就包括使用来自退役机器的零件升级测试虚拟机的磁盘和内存，将 stable/13 任务的构建环境更新为 13.3-RELEASE，并将主分支上的 i386 构建过渡为使用 amd64 的交叉构建。

正在进行的努力包括合并关键审查，向 CI 集群添加新硬件，以及设计预提交 CI 系统和拉取/合并请求系统。团队还在致力于利用 CI 集群构建发布工件，简化 CI/测试环境设置，以及重新设计硬件测试实验室。

未来计划包括收集 CI 任务和想法，为虚拟机客机测试设置公共网络访问，实现裸金属硬件测试套件，添加针对 -CURRENT 的 DRM Port 构建测试，以及运行 ztest 测试。团队的目标是改善 FreeBSD 在 CI 流水线中的支持，并与托管的 CI 提供商合作。

**更多信息：**  **[持续集成 (GitHub)](https://github.com/Jehops/freebsd-doc/blob/2024q2_ff/website/content/en/status/report-2024-01-2024-03/ci.adoc)**

##  将 FreeBSD 作为 cloud-init 一级平台

正在进行

### 增强对 cloud-init 的支持，使 FreeBSD 成为 Tier I 平台，改善FreeBSD 在云环境中的集成和可用性。

**联系人：** Mina Galić [freebsd@igalic.co](mailto:freebsd@igalic.co)

Cloud-init 现已成为在云中设置服务器的标准。在过去一年半的时间里，FreeBSD 在支持 cloud-init 方面取得了显著进展。今年的重点是同 cloud-init 开发者和 FreeBSD 基金会密切合作，增强 FreeBSD，使 cloud-init 团队能够直接测试未来对 FreeBSD 代码路径的更改。

为此，FreeBSD 必须在 LXD（和 Incus）的控制下运行，并由 lxd-agent（或 incus-agent）管理。最近，已经取得了一些可见的改进。一个小型测试框架在 sh 中开发，正在逐步迁移到 OpenTofu/Terraform。该框架安装测试 cloud-init-devel 和 cloud-init 的最新版本。为支持这一点，创建了一个专用的公共代码库，包含 FreeBSD 13 和 14 在 amd64 和 aarch64 上的 cloud-init-devel 和 cloud-init 的最新版本。

此外，Linux vsock 测试框架也已移植到 FreeBSD。基于 HyperV Socket 驱动程序创建了 VirtIO Socket 驱动程序的驱动程序框架，导致 HyperV 套接字的多个改进。这些改进已部分接受，但仍需更多工作。

最新的 cloud-init 24.1 系列经过测试并发布，修复了长期存在的错误，例如将 /run/cloud-init 移动到 BSD 上的 /var/run/cloud-init，并纠正了 user_groups 的 homedir 参数。此次发布还包括社区贡献的 OpenBSD 代码路径的多个修复。

展望未来，这项工作涉及几个关键任务。完成 FreeBSD VirtIO Socket 驱动程序和修复 Go 的运行时以支持 FreeBSD 上的 VirtIO 是首要任务。将 lxd-agent 的依赖项及 lxd-agent 本身移植到 FreeBSD 也至关重要。这些努力将与对 BSD 上 cloud-init 的进一步改进和在不同云提供商上的额外测试交替进行。

**更多信息：**  **[Cloud-Init (GitHub)](https://github.com/Jehops/freebsd-doc/blob/2024q2_ff/website/content/en/status/report-2024-01-2024-03/cloud-init.adoc)**

## FreeBSD 上的 OpenStack

正在进行

### FreeBSD 上的 OpenStack 项目旨在将 OpenStack 云基础设施与 FreeBSD 操作系统无缝集成，利用 FreeBSD 的独特功能，同时保持与 OpenStack 标准的兼容性。

**联系人：** Chih-Hsin Chang [starbops@hey.com](mailto:starbops@hey.com)，Li-Wen Hsu [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

**第一季度：**

在 2024 年第一季度，该项目取得了重大进展。提交了 BSDCan 2024 的提案，团队参加了 AsiaBSDCon 2024，分享了移植经验并收集了有价值的反馈，这帮助完善了项目的方向。第一阶段的任务进行了审查，进行了必要的调整，并将第二和第三阶段的计划与长期目标进行了对齐。一项关键技术成就是验证了 bhyve 串口控制台通过 TCP 的功能。还制作了一个演示视频，展示了项目的进展和特性。

**第二季度：**

第二季度继续取得进展。团队在 BSDCan 2024 上介绍了“朝着强大的基于 FreeBSD 的云：移植 OpenStack 组件”，这增加了项目的可见性，并吸引了潜在贡献者的兴趣。概念验证（POC）站点从单节点设置扩展到三节点设置，涉及详细的环境设置和网络规划。还启动了将基础迁移到 FreeBSD 15.0-CURRENT 的工作，以保持与最新 FreeBSD 发展的对齐。

此外，手动安装步骤和代码补丁开始转换为 FreeBSD Port，以简化安装过程。一个重要的里程碑是启动了对 FreeBSD 实例和 OpenStack Ironic 服务主机进行裸机配置的工作。

**未来计划：**

展望下一个季度，重点将放在完善这些进展并进一步增强项目的稳健性和易用性。具体计划包括将 OpenStack 组件从 Xena 版本升级到更近期的版本，因为 Xena 正接近生命周期的尽头。欢迎社区的建议和贡献，以帮助实现这些目标。

**更多信息：**  [OpenStack (GitHub)](https://github.com/Jehops/freebsd-doc/blob/2024q2_ff/website/content/en/status/report-2024-04-2024-06/openstack.adoc)

## WiFi 更新 – Intel 驱动程序和 802.11ac

正在进行

### 此更新支持了当前一代 Intel WiFi 设备和 802.11ac 标准，来改善无线连接性。

**联系人：** Björn Zeeb [bz@freebsd.org](mailto:bz@freebsd.org)

在 2023 年 11 月，FreeBSD 基金会启动了一项重大举措，来改善 iwlwifi 驱动程序，该驱动程序对支持 FreeBSD 上的 Intel Wi-Fi 芯片至关重要。这个项目由 FreeBSD 开发者 Cheng Cui 领导，并与 Björn Zeeb 合作，旨在通过多个关键里程碑增强 FreeBSD 的无线功能。

项目的主要目标之一是解决影响 iwlwifi 驱动程序的多个关键问题报告（PR）。在 PR 271979、273985、274382 和 275710 中记录的问题通过系统化和创新的调试技术成功解决。例如，使用铝箔包裹的纸板隔离信号是一种新颖的方法，证明在识别和修复这些问题上效果显著。

该项目还专注于提高系统稳定性。审查和实施补丁显著改善了 FreeBSD 版本 13.3-RELEASE 和即将发布的 14.1 的稳定性。项目强调启用硬件支持的加密功能，这涉及创建 PR 277095 和 277100，以应对复杂的调试场景。

改善对 802.11n 标准的支持是另一个重点领域。该项目通过利用深厚的领域专业知识并采用 Linux 中的 Driver API 跟踪等新调试技术，解决了 PR 276083。这一增强对于推动项目目标和改善 FreeBSD 的无线性能至关重要。

此外，该项目在确保 FreeBSD 13.3 成功发布方面发挥了重要作用。通过重现用户报告的问题并测试后续修复，项目为操作系统的整体可靠性和性能做出了贡献。

增强 iwlwifi 驱动程序的努力改善了 FreeBSD 对 Intel Wi-Fi 的支持。该项目确保了用户更好的无线性能和稳定性。持续的工作将继续提升 FreeBSD 的网络功能，使其成为更强大、更可靠的操作系统。

**更多信息：**  [Wi-Fi 增强（FreeBSD 基金会）](https://freebsdfoundation.org/blog/improving-and-debugging-freebsds-intel-wi-fi-support-cheng-cuis-key-role-in-the-iwlwifi-project/)

---

　　　　以下为已完成部分

---

## 改进 Bhyve

对 FreeBSD 虚拟机监视器的各种改进

**联系人：** [Chris Moerz](freebsd@ny-central.org)

### I/O 性能测量

最近，Bhyve 生产用户之间的讨论强调了正式 I/O 性能分析的必要性。作为回应，团队开始使用一组 shell 脚本和 benchmarks/fio 包测试不同的配置。重点评估不同的存储后端、内存设置、CPU 固定选项以及支持存储和虚拟磁盘的块大小。团队还比较了不同 CPU 制造商以及客户和主机环境的性能。

### 虚拟机工具

FreeBSD 基金会的企业工作组认为需要类似于 jail 的 Bhyve 工具。这促成了“vmstated”的开发，这是一款使用基本 FreeBSD 工具构建的守护进程和管理实用程序。Vmstated 通过 UCL 配置，提供灵活的虚拟机管理，具有类似于 jail 的命令集和状态转换钩子等功能。该工具已在 ports 中作为 sysutils/vmstated 提供，并在 GitHub 上持续更新。欢迎贡献和反馈。

### 文档更新

对 FreeBSD 手册和 Porter 手册进行了几次更新，重点关注虚拟化、Bhyve 配置和管理 Bhyve 客户。正在进行 Bhyve 手册页结构的更新审查，并计划进一步改进内容。欢迎对此次更新提出反馈。

### 为 arm64 客户创建的扁平设备树

Mark Johnston 和 Andrew Turner 合作创建了构建 arm64 bhyve 客户的扁平设备树（FDT）的基本例程。FDT 描述了不同的硬件组件，例如 CPU、内存、UART、PCIe 控制器、中断控制器和平台定时器，客户操作系统应当了解这些组件。

**更多信息：** [Bhyve 更新（GitHub）](https://github.com/Jehops/freebsd-doc/blob/2024q2_ff/website/content/en/status/report-2024-01-2024-03/bhyve.adoc)

## 在 Azure 和 Hyper-V 上的 FreeBSD

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

## 移植 .NET (dotnet) 

### 将“dotnet”原生移植到 FreeBSD，初始版本为 8，后续版本的移植正在进行

**联系人：** Gleb Popov [arrowd@freebsd.org](mailto:arrowd@freebsd.org)

在 FreeBSD 上对 .NET 的支持（**dotnet**）使开发者能够选择自己喜欢的平台而不受限制。这种兼容性使他们能够利用 FreeBSD 独特的优势，同时保持与 .NET 一致的开发环境。

新的 .NET 原生移植目前可用于 **amd64** 架构（对 **aarch64** 的支持正在进行中），将 .NET 运行时版本 8 带入 FreeBSD。这确保了完全兼容，同时利用了 FreeBSD 的性能和安全特性，使开发者能够充分利用 FreeBSD 的功能。

将 .NET 移植到 FreeBSD 是一个协作努力，涉及主要社区贡献者。Gleb Popov（**arrowd@FreeBSD.org**）维护 .NET 移植，**[thefrank](https://github.com/Thefrank)**、Naram Qashat（**cyberbotx@cyberbotx.com**）和 Szczepan Ćwikliński（**[sec](https://github.com/sec)**）也做出了重要贡献。团队与 dotnet 上游项目积极合作，包括在 GitHub 上提交 PR。他们的共同努力对实现 .NET 在 FreeBSD 上的运行至关重要。

**更多信息：** **[dotnet (GitHub)](https://github.com/dotnet)**

## FreeBSD 集群现代化

### 加强 FreeBSD 项目基础设施、提升其能力，并为用户提供更好的服务的倡议

**联系人：** Joseph Mingrone [jrm@freebsdfoundation.org](mailto:jrm@freebsdfoundation.org) 和 Philip Paeps [phil@freebsd.org](mailto:phil@freebsd.org)

FreeBSD 基金会投资 10 余万美元在芝加哥部署了一套服务器集群。此项投资旨在加强 FreeBSD 项目的基础设施、提升其能力，并为用户提供更好的服务。为了支持这一扩展，基金会与 NYI 合作，后者慷慨地在其芝加哥设施中提供了四个机架。

新的集群配置旨在优化 FreeBSD 项目的运营效率，包括：

* **两台路由器：** 用于引导网络流量。
* **五个软件包构建器：** 旨在加速软件包发布过程。
* **三台通用服务器：** 这些服务器将提升 FreeBSD 项目面向公众和开发者的服务（如 Bugzilla、Git、Phabricator、Wiki 等）的可用性和性能。
* **两个软件包镜像站：** 一个托管在芝加哥的新集群，另一个托管在加州的 ISC。这些是 FreeBSD 项目日益扩大的 pkg.FreeBSD.org 和 download.FreeBSD.org 服务器网络的一部分，战略性地分布在全球，可提供更快的软件包下载速度。
* **两台 CI 服务器：** 以提高自动化代码测试的速度和效率。
* **一台管理堡垒服务器：** 这是管理集群的安全入口点，运行集群管理团队（clusteradm）工具、集群 DNS、监控以及其他管理系统所需的服务。

这一硬件配置预计将显著提升 FreeBSD 项目的处理能力和服务响应速度。

FreeBSD clusteradm 团队在新集群的集成阶段发挥了关键作用。

* **硬件兼容性和固件调试：** 为确保服务器固件与 FreeBSD 兼容，需要克服初期面临的多个障碍。集群依赖于能够网络启动机器，并要求可靠的带外管理。
* **网络配置和自动化：** 服务器能够可靠启动后，进行了网络配置，包括集群内部 DNS、数据包过滤规则和与互联网的 BGP 会话。
* **自动化和系统配置：** 团队的自动化工具大大简化了服务器的安装和配置。在使用临时 FreeBSD 安装克服了一些启动问题后，服务器被网络启动到集群安装镜像中，并使用标准集群构建进行安装。
* **监控和管理集成：** 团队在管理服务器上安装和配置了监控代理，将新站点集成到项目的中央监控系统中。这使得集群的管理和故障排除更加高效，确保了稳定性和性能。
* **最终系统安装和网络服务设置：** 团队通过使用工具自动化重新安装管理服务器，设置路由和防火墙配置，并在光纤上行链路上启用 BGP 会话，完成了集成工作。这一设置确保了新集群的运行，并优化了性能和安全性。

## Olivier Certner 的杂项更新

已完成

### FreeBSD 源代码树各部分的杂项更新。

**联系人：** Olivier Certner [olce@freebsd.org](mailto:olce@freebsd.org)

在 2024 年第二季度，长期承包商 Olivier Certner 在系统的多个不同部分积极工作：

* [rtprio(2)](https://man.freebsd.org/cgi/man.cgi?query=rtprio&sektion=2&format=html)：将每个运行队列的队列数量从 64 升级到 256。
* **Vnode 回收/ZFS ARC 回收：** 审查了 [bug #275594](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=275594) 的修复，与上游沟通以获取和测试回移，并发出了一份 EN 并作为 13.3-RELEASE-p2 应用，同时开始了长期工作以改进 vnode 回收机制，并确保 ZFS 传递正确的信息。
* **ULE 调度器：** 更新为在单个运行队列上工作，而不是为满足 POSIX 合规性而使用 3 个运行队列，以处理 SCHED\_FIFO/SCHED\_RR 优先级级别的数量。
* **杂项：** 进行了多达 26 项评审、软件包更新，并调查了 DRM 问题。
* 在 FreeBSD Journal 发布了 [EuroBSDCon 2023 大会报告](https://freebsdfoundation.org/eurobsdcon-2023/)。

## Center for Internet Security (CIS) FreeBSD 14 基准

已完成

这是一个全面的安全加固指南，旨在帮助安全高效地配置 FreeBSD 系统。

**联系人：** Moin Rahman [bofh@freebsd.org](mailto:bofh@freebsd.org)

此新 CIS 基准涵盖了关键领域，包括：

* **用户和组管理：** 采用最佳实践指南安全地管理用户账户和组。
* **服务配置：** 关于安全配置基本服务的建议。
* **文件系统和权限：** 管理文件系统安全和权限的最佳实践。
* **网络配置：** 提供保护网络设置以防止未经授权访问和攻击的安全建议。
* **审计和日志记录：** 设置强大日志和审计的说明，以监控系统活动。

该基准是系统管理员、安全审计员以及必须遵守行业标准和法规的组织的重要资源。我们鼓励 FreeBSD 社区提供反馈并为这些指南的持续完善做出贡献。安全工作在协作中最为有效，我们期待看到社区如何利用和扩展这一新资源。

我们对 FreeBSD 社区在此基准中的重要贡献表示衷心感谢。特别感谢基准撰写者 Moin Rahman、编辑 Carole Fennelly、评审 Jason Kafer 和 Rick Miller、项目经理 Joe Mingrone，以及 CIS 的 Justin Brown 和 Eric Pinnell。同时，我们也感谢 [Verisign](https://www.verisign.com/) 对创建 CIS FreeBSD 14 基准部分费用的资助，以及对 [FreeBSD 基金会的慷慨捐赠者](https://freebsdfoundation.org/our-donors/donors/) 给予的支持。

**更多信息：** [FreeBSD 14 基准](https://freebsdfoundation.org/blog/new-cis-freebsd-14-benchmark-secure-your-systems-with-expert-guided-best-practices/)（FreeBSD 基金会）

## 在 FreeBSD 上的 VPP

### 将矢量数据包处理（VPP）框架移植到 FreeBSD，来增强网络性能能力。

**联系人：** Tom Jones [tj@freebsdfoundation.org](mailto:tj@freebsdfoundation.org)

FreeBSD 上的矢量数据包处理（VPP）项目旨在将 VPP 这一开源的高性能用户空间网络栈移植到 FreeBSD。VPP 通过矢量化操作和并行处理优化数据包处理，非常适合软件定义网络（SDN）和网络功能虚拟化（NFV）应用。该工作启动于 2023 年 11 月，由专注于网络性能的 FreeBSD 开发者 Tom Jones 在 FreeBSD 基金会的合同下领导。

关键里程碑包括修复 VPP 在 FreeBSD 上的构建，确保其能够编译和运行，验证并添加基本功能，以及开发全面的测试和回归套件以维护可靠性和稳定性。性能基准测试帮助识别和解决潜在瓶颈，并提出改进和优化建议。

文档工作专注于 FreeBSD 特定的 API 和用法，为开发者和用户提供清晰的指导。创建 VPP 的 FreeBSD 移植成功简化了安装和部署，使用户更易于使用。

VPP 的 FreeBSD 移植取得了成功，正在进行的工作旨在进一步增强其能力。不断进行改进和优化，以确保 FreeBSD 的网络性能保持强大和高效，巩固其在高速网络应用中的适用性。

**更多信息：** **[Vector Packet Processor (GitHub)](https://github.com/adventureloop/vpp)**


## 网络夏季实习

已完成

Naman Sood 是 FreeBSD 基金会的夏季实习生，一直在从事与网络相关的任务。Naman 在开始实习时提交了对 FreeBSD 中一个防火墙（pf）的改进。如，他们完成了 Luiz Amaral 开展的工作，以允许 pfsync（pf 的状态表同步接口）流量通过 IPv6 进行传输。他们还提交了对 pf 完全圆锥 NAT 实现 RFC 4787 REQs 1 和 3 的工作。完全圆锥 NAT 意味着来自内部 IP/端口的所有请求都映射到相同的外部 IP/端口，这使得某些设备（如 Nintendo Switch）能够在 FreeBSD 上运行 pf 的情况下正常工作。Naman 还承担了一些杂项任务，例如探索从 Klaus P. Ohrhallinger 开展的 FreeBSD 项目 VPS 中提取 TCP 检查点和故障转移的工作，以及提交 pw(8) 和 du(1) 的 bug 修复。

## 文档和测试实习

已完成

2023 年 7 月，Yan-Hao Wang 开始在基金会进行夏季实习，承担各种任务。以下是一些计划的工作内容：

* 构建一款在线手册页面编辑器
* 更新 FreeBSD 的 jenkins-tinderbox
* 为 /bin、/sbin、/usr/bin 和 /usr/sbin 中的用户空间工具添加测试用例
* 研究开发 FreeBSD 手册页面和文档的“专家系统”
* 修复 libxo 问题，并编写相关测试
* 调查 RPI4 和 IPV6 待办事项的开发路线图

FreeBSD 手册页面和文档的“专家系统”将是一个尽力而为的概念验证任务，包括将 FreeBSD 文档（如手册页面和手册）导入到向量数据库中，以便像 ChatGPT 这样的语言模型可以“阅读”它们，从而在查询与 FreeBSD 相关的问题时能提供更好的答案。


## 解决 OpenSSL 3 / LLVM 16 Port 问题

已完成

随着 FreeBSD 主分支中 OpenSSL 更新到版本 3，许多 Port 构建错误必须在 FreeBSD 14.0 发布之前解决。与 OpenSSL 3 和 LLVM 15 的大多数关键问题已经得到修复，但在使用 LLVM 16 时，约有 800 个额外的 Port 无法构建，导致在完整的 Ports 构建中跳过了 2800 个依赖 Port。穆罕默德·莫伊努尔（Moin）·拉赫曼将完成所有与 OpenSSL 3 和 LLVM 16 更新相关 Port 问题的耗时且繁琐的修复工作。

## SIMD 增强的 libc

完成

现代计算机架构提供了SIMD（单指令多数据）指令集扩展，以便一次处理多个数据。SIMD技术常用于视频编解码、图形渲染和科学计算等数值应用中，同时也有助于基本的数据处理任务，例如libc函数实现的任务。虽然其他libc实现已经提供了标准libc函数的SIMD增强版本，但FreeBSD的libc大体上并没有。罗伯特·克劳塞克（Robert Clausecker）发起的这个项目旨在提供相关libc库函数的SIMD增强版本，从而提高与之链接的软件性能。由于这些libc函数被大多数可用的FreeBSD软件使用，因此这些增强预计会为广泛的程序带来广泛的好处。该项目的主要关注点是amd64，目标是基于x86\_64 psAB定义的架构级别生成SIMD优化的实现。

如果例程受益于较高架构级别可用的附加指令，计划实现多种例程的多个实现。这通常意味着一个基线或x86-64-v2的例程，以及每个x86-64-v3和x86-64-v4的一个例程。计划建立基准测试套件，以确定这些例程对libc性能的影响。在未来的工作中，这些例程可以适应i386，或移植到其他架构，包括arm64（ASIMD，SVE）和ppc64/ppc64le，前提是有足够的兴趣。

**技术细节**

计划将优化的例程实现为汇编，以确保工具链独立性。对于动态链接的可执行文件，计划使用ifunc机制在运行时选择每个例程的最佳实现。如果可能，将查询一个环境变量，以允许用户选择不同的架构级别或完全禁用SIMD增强。对于静态链接的可执行文件或直接调用函数时（例如，通过隐藏别名从libc内部调用），计划提供调度跳板。在第一次调用跳板时，调用解析为一个调度函数，该函数确定使用哪个实现。调度函数将调度目标写入由跳板使用的函数指针中，然后尾调用选定的例程。在下一次迭代中，直接调用正确的函数。这两种机制都将以线程安全和异步信号安全的方式实现。最佳实现通常是使用CPU支持的最高架构级别的实现。然而，硬件约束，例如热许可和AVX-SSE转换惩罚，可能使某些处理器上的架构级别v3和v4变得不具吸引力。实现可能会在读取时超出字符串的末尾，但确保不会跨越页面边界。这样的溢出在未设置段限制时是无害的，但可能会让分析工具如valgrind感到困惑。这在处理以NUL结尾的字符串时尤其需要快速性能。

**文档**

SIMD增强函数的存在将在新的手册页simd(7)中记录。该页面将向用户解释libc如何选择使用哪个实现以及如何配置这种行为。其他手册页，如environ(7)、string(3)和bstring(3)，将根据需要增强交叉引用和附加信息。内部文档将解释调度和函数选择机制。由于不计划将这些机制提供给用户代码，因此不会生成最终用户文档。根据需要，可能会生成关于基准测试和测试设置的附加文档。最终报告将描述所使用的技术，并给出最终性能改进。

## Capsicum 实习

已完成

从 2023 年 6 月 1 日到 9 月 1 日，Jake Freeland 将在基金会实习，致力于 Capsicum，这是 FreeBSD 的沙箱框架。Capsicum 的设计目的是限制应用程序和库的能力。Capsicum 模型简单且安全，但围绕该框架的进展和发展在近年来逐渐减缓。Capsicum 的核心思想直观易懂；一旦进入能力模式，资源获取和外部通信就会受到严格限制。围绕这一原则设计程序相对容易，但当现有的未设计为沙箱的应用程序需要在此环境中运行时，问题便接踵而来。确定哪些操作会导致 Capsicum 违规是困难的，而预先打开尚未请求/命名的资源是不可能的。此外，开发人员在开始实现 Capsicum 功能之前需要对程序有充分的了解。这些原因解释了为何 Capsicum 化的工作逐渐减缓。

这次实习将涉及多个项目，这些项目的整体目标是振兴 Capsicum。主要目标是增强和简化希望将现有程序 Capsicum 化的开发人员的体验。Capsicum 最大的敌人是其陡峭的学习曲线。重构程序支持能力模式通常要求开发人员了解导致 Capsicum 违规的原因，并知道如何重构给定程序以避免违规。有时，这一过程相对简单，但较大的程序往往需要按需资源，而弄清楚如何满足这些需求可能会很困难。扩展可供开发人员使用的工具数量，以便方便地将程序 Capsicum 化，将显著平缓上述学习曲线。如果 Capsicum 化变得简单，更多的开发人员将会采用它。

**项目**

**1. 跟踪 Capsicum 违规**

在撰写本文时，修改程序以支持 Capsicum 需要开发人员手动解析他们的代码并找到 Capsicum 违规。如果有一个工具可以在运行时跟踪应用程序并确定违规发生的位置，那将是很方便的。这一功能可以在 ktrace(1) 中添加一个选项标志。其前提是钩住通常会返回 ENOCAP 的位置，记录该位置，然后正常继续执行。David Chisnall 提出的差异修订 https://reviews.freebsd.org/D33248 也可以用来通过信号通知记录违规。

**2. Capsicum 化 syslogd(8)**

syslogd 守护进程负责读取并记录消息到系统控制台、日志文件和其他机器。记录是任何操作系统不可或缺且常常敏感的职责，因此 syslogd 理应使用 Capsicum 进行沙箱化。通过 ktrace(1) 跟踪 Capsicum 违规，将重新设计 syslogd 以在能力模式下运行。syslog.conf 配置文件负责为 syslogd 提供设施和程序进行监视，以及对应的日志文件位置。这一约定使我们能够解析 syslog.conf，并确定 syslogd 正常运行所需的资源。通过在执行开始时解析 syslog.conf 进行沙箱化并不可行。如果在任何时间接收到 SIGHUP 信号，syslogd 将重新处理其配置，并可能需要新的资源。为了绕过这个问题，syslogd 应该被分为两个并发进程：一个处理日志，另一个监听 SIGHUP，读取配置文件，并在必要时将能力传递给另一个进程。

**3. Capsicum 化 NFS 守护进程**

NFS 套件由许多守护进程组成，包括 nfsd(8)、mountd(8)、rpcbind(8)、rpc.statd(8)、rpc.lockd(8) 和 rpc.tlsservd(8)。该项目的重点将放在 Capsicum 化 rpcbind 上。rpcbind 守护进程负责将 RPC 程序号转换为标准通用 DARPA 地址。这个程序非常适合 Capsicum 化，因为它通常由 root 运行，因此是一个有价值的攻击目标。快速浏览 usr.sbin/rpcbind/rpcbind.c:152 显示 rpcbind 限制自身至少使用 128 个资源，这表明它可能会按需请求打开任意文件。这是 Capsicum 化的一个明显障碍，因为我们无法在能力模式下打开任意文件。我们可能需要使用类似 libcasper(3) 的机制（或其他类似机制），在需要时将能力传递给 rpcbind。记录下这些命名资产的请求：rpc 锁文件、日志文件、网络配置文件、用于线程唤醒的管道、rpcbind 套接字。毫无疑问，还有更多。可能还会完成对其他 NFS 守护进程的 Capsicum 化。

**4. Capsicum 化 ggatec(8) 和 ggated(8)**

GEOM Gate 网络设施提供对存储设备的远程访问，并建立在 FreeBSD 的 GEOM 框架之上。与 NFS 类似，设备导出可以在导出文件 /etc/gg.exports 中管理。ggate 工具是 Capsicum 化的主要候选，因为它们以 root 身份运行，处理网络请求，并曾在 CVE-2021-29630 中遭受远程代码执行。ggatec 客户端工具用于创建 ggate 设备并与 ggated 通信。由于远程主机和设备路径在命令行参数中指定，因此 Capsicum 化 ggatec 应该相对简单。在进入能力模式之前，简单的文件和套接字预打开应该足够。ggated 工具查看 /etc/gg.exports 或指定的替代导出文件，并为 ggatec 服务 GEOM Gate 请求。所有所需资源似乎都在命令行参数和导出文件中指定，因此在进入能力模式之前预打开这些资源应该足够。

**5. Capsicum 化 tftpd(8)**

tftpd 服务器实现了互联网微型文件传输协议（RFC 1350），允许远程读取 tftpd 参数中指定的文件。由于所需资源提前指定，因此 tftpd 的 Capsicum 化应该涉及简单的目录预打开。

**6. Capsicum 化 ntpd(8)**

与 syslogd(8) 和 rpcbind(8) 不同，ntpd 的代码库似乎分为大约一百个大文件。根据手册页面，这些文件都有名称，且很容易进行预打开：配置文件、漂移文件、网络接口设备、密钥文件、日志文件、pid 文件和统计文件。假设不需要任意文件，Capsicum 化过程应该相对温和。

**7. Capsicum 化 libarchive(3)**

libarchive 库专注于压缩和解压缩多种流行的归档格式。已注意到 iconv(3) 的共享库获取正在引发 Capsicum 违规。一个临时解决方案是在 unzip(1) 中预打开这些 iconv(3) 文件，但这实际上应该发生在 libarchive 中。libarchive Capsicum 化的目标是在能力模式下引入与归档无关的创建和提取。这可能通过添加 Capsicum 特定的接口来实现，作为标准 API 的补充。如果这可行，下一步将是对 tar(1) 进行 Capsicum 化。由于大多数 tar 文件提取到当前目录，因此 Capsicum 化过程应包括打开当前目录文件描述符，并将所有文件系统资源获取调用更改为其 at() 派生函数。例如：open() 将更改为 openat()。

**8. 完成 SIGCAP 违规信号实现**

David Chisnall 提出的差异修订 https://reviews.freebsd.org/D33248 提议在 Capsicum 违规时可选地发送 SIGCAP 信号。不幸的是，该审查尚未完成，几个月来没有更新。完成此审查并添加 SIGCAP 信号可以使使用违规信号来触发 Capsicum 违规的程序的调试变得更加容易。我们可以使用 SIGCAP 告诉代码退回到替代路径，而不是等待可能被调试器拦截的 SIGTRAP。此外，拥有一个明确的 Capsicum 违规信号将允许 Capsicum 违规跟踪工具记录 Capsicum 特定的失败。例如，当 kern.trap enotcap=1 被设置时，任何 Capsicum 违规将提示 SIGTRAP 及程序终止。并不透明的是，这个程序是否因为违规而终止，还是因为不相关的 SIGTRAP 信号而终止。将 kern.trap enotcap 更改为发送 SIGCAP 将消除这种混淆。这个 SIGCAP 信号还可以为前述的 ktrace(1) 引入一种跟踪 Capsicum 违规的替代方法。ktrace(1) 程序可以拦截并记录 SIGCAP 调用，并使用适当的信号处理程序将原始程序送回执行。

## 无线实习

完成

En-Wei Wu 是 2022 年 Google Summer of Code 的贡献者，他于 2023 年初开始在 FreeBSD 基金会实习，专注于 FreeBSD 的无线驱动程序和工具。工作分为三个部分。

wtap(4) 是由 Monthadar Al Jaberi 和 Adrian Chadd 于 2012 年推出的 net80211(4) Wi-Fi 模拟器。En-Wei 将通过添加对 802.11b 以外的更多 802.11 物理层的支持来扩展 wtap。对 wtap 的其他工作还将包括添加对 WPA/WPA2/WPA3 的支持，以便可以测试 wpa supplicant(8) 和 hostapd(8)。

将为 hostapd(8) 添加对 WPA2 预认证的支持。WPA2 是作为 IEEE 802.11i 规范的一部分定义的认证协议。该协议现在通常用于将无线站点认证到接入点。该协议的一部分是能够与一个或多个接入点预认证站点，以便快速漫游。FreeBSD 在用于构建 WPA 启用接入点的 hostapd 程序中缺乏对该协议这一方面的支持。此任务将移植现有的 Linux 代码，以支持 hostapd 中的预认证。这主要涉及重写一些用户模式的多播代码并测试结果。对托管在 FreeBSD 之外的第三方源的修改应在适用时上游到相应的项目中。

802.11 驱动程序的工作将完成。ath10k 驱动程序将通过完成 Adrian Chadd 开始的工作进行移植。同时，将为 Bjoern Zeeb 提供帮助，开发和测试 Realtek 驱动程序，例如 rtw88 和 rtw89。

## 改进 kinst DTrace 提供程序

完成

DTrace 是一个框架，赋予管理员和内核开发人员实时观察内核行为的能力。DTrace 具有称为“提供程序”的内核模块，这些模块通过“探针”在内核中执行特定的插桩。

kinst 是一个新的低级 DTrace 提供程序，由 Christos Margiolis 和 Mark Johnston 为 FreeBSD 操作系统共同编写。它允许用户跟踪任意指令，并且自 FreeBSD 14.0 起成为基础系统的一部分。

kinst 探针的形式为 \`kinst::\<function\>:\<instruction\>\`，其中 \`\<function\>\` 是要跟踪的内核函数，\`\<instruction\>\` 是相对于函数开头的指令偏移量，可以从该函数的反汇编中获得。

该项目的主要目标是实现内联函数跟踪（这是一个备受期待的 DTrace 功能），并将 kinst 移植到 riscv 和 arm64。对于内联跟踪，kinst 将利用 DWARF 调试标准，以便检测内联调用并为每个调用创建探针。未来，这一功能可以用于解决 FBT 的一些不足之处，例如尾调用优化问题（DTrace 手册第 20.4 章）以及缺乏内联跟踪能力。

该项目的交付成果包括：

– 扩展 kinst，以利用 FreeBSD 的 dwarf(3) 标准跟踪内联调用。
– 添加一个新的 dtrace(1) 标志，当 libdtrace 应用语法转换时（如果有），可以转储 D 脚本。这对调试 libdtrace 本身以及新的内联跟踪功能非常有用。
– 将 kinst 移植到 riscv 和 arm64。


## 使用日志化软更新的文件系统快照

完成

UFS/FFS 文件系统具有快照的能力。由于快照功能是在软更新编写之后添加的，因此它们与软更新完全集成。然而，当在 2010 年添加日志化软更新时，它们从未与快照集成。因此，在运行日志化软更新的文件系统上无法使用快照。

当 FreeBSD 添加对 ZFS 的支持时，快照的重要性降低了。ZFS 可以快速且轻松地进行快照。然而，仍然存在两个实例，其中 UFS 快照仍然很重要。首先，它们允许对实时文件系统进行可靠的转储，从而避免可能数小时的停机时间。其次，它们允许在后台运行 fsck。与 ZFS 中需要进行清理的情况类似，fsck 需要定期运行，以发现未检测到的磁盘故障。快照允许在实时文件系统上运行 fsck，而不需要安排停机时间。

经过与开发者社区的磋商，FreeBSD 基金会的工作人员一致认为这样的基础设施工作将产生积极的影响。因此，基金会开始赞助 Marshall Kirk McKusick 实施所需的更改，以允许使用日志化软更新的 UFS/FFS 文件系统进行快照。此项工作需要对 UFS/FFS 软更新和快照内核代码以及 fsck_ffs 实用程序进行广泛的更改。

该项目预计将在 2023 年中期完成，工作分为两个里程碑。在里程碑 1 后，当运行日志化软更新时，将启用快照，并且它们将可用于对实时文件系统进行后台转储。里程碑 2 涉及扩展 fsck_ffs，使其能够在运行日志化软更新的文件系统上使用快照进行后台检查。每个里程碑在代码通过审查过程并已提交到主树时被视为完成。

## WireGuard 审查、更新与集成

完成

WireGuard 是一种安全的隧道协议，具有用户空间和内核实现。在初期的修复程序发布后，FreeBSD 内核的 WireGuard 代码库更加完整和稳定。现在为每个提交设置了自动 CI，对 wireguard-freebsd 支持的版本进行编译并运行小规模的烟雾测试。

基金会正在资助 John Baldwin 对 WireGuard 进行更新，主要是通过更新上游 WireGuard 驱动程序中的数据路径加密，使用内核中的 OpenCrypto 框架来处理数据路径。通过 WireGuard 隧道发送的数据包使用 Chacha20-Poly1305 AEAD 加密算法进行加密。与 TLS 和 IPsec 不同，WireGuard 使用 8 字节的随机数（nonce），而不是与该算法配合使用的 12 字节随机数。

截至目前，大部分工作集中在更新 OCF，以更好地支持给定加密算法的多随机数（nonce）和标签/MAC 长度。John 之前已开始着手支持所有 AES-CCM NIST KAT 向量的工作，其中许多使用非默认的随机数和标签长度。该方法经过改进，更好地适应现有 OCF 模型，其中随机数和 MAC 长度是会话的属性（类似于密钥长度）。之前的一个分支将随机数长度设为单独操作的属性。这主要涉及扩展 /dev/crypto 接口，以允许为会话设置这些参数。现有的 OCF 测试在用户空间中运行，并使用 /dev/crypto 接口，包括 cryptocheck 实用程序和 NIST KAT 向量测试。

在这些框架更改的基础上，John 扩展了 OCF 中现有的 Chacha20-Poly1305 加密算法，以支持 8 字节和 12 字节的随机数，包括在加速的 ossl(4) 驱动程序中。针对上游 WireGuard FreeBSD 驱动程序的补丁，已验证与标准 WireGuard 驱动程序的互操作性。

## LLDB 改进第三部分 – 内核调试支持

完成

FreeBSD 的基础系统包括 LLDB，这是 LLVM 家族的调试器。与 GNU GDB 调试器相比，FreeBSD 的 LLDB 目前存在一些限制，尚未完全取代 GDB。这个多阶段项目旨在为 FreeBSD 提供现代化的调试器，使 LLDB 更接近于一个功能齐全的 GDB 替代品。

[第一部分](https://freebsdfoundation.org/project/lldb-debugger-improvements/)和 [第二部分](https://freebsdfoundation.org/project/lldb-improvements-part-ii-additional-cpu-support-follow-fork-operations-and-savecore-functionality/) 的 LLDB 改进项目描述了 FreeBSD 上 LLDB 的用户空间改进。第三部分专注于内核调试的改进。

FreeBSD 上的 LLDB 调试器仍然缺乏一个可替代的 [kgdb(1)](https://www.freebsd.org/cgi/man.cgi?query=kgdb&sektion=1)，kgdb 是一个包装了修改版 GDB 的调试器，依赖 libkvm 接口来调试死后和实时的 BSD 内核内存。LLDB 在 FreeBSD 内核调试中的一个主要限制是缺乏与 GDB 的远程协议兼容性。这种不兼容意味着 LLDB 前端与现有的 gdb-server 实现不兼容，尤其是与 qemu 使用的实现不兼容。第三部分的一个主要目标是解决这些不兼容，使得在内核调试中不再需要安装 GDB，并允许 FreeBSD 开发人员使用 LLDB 满足他们所有的调试需求。

GDB 和 LLDB 都支持通过 TCP/IP 进行远程调试。然而，GDB 还支持一种通过串口的 gdb-remote 协议变体。由于这种方法对于在不依赖内核 TCP/IP 堆栈的情况下进行远程内核调试非常有用，因此将会在 LLDB 中添加支持。

libkvm 是 FreeBSD 基础系统的一部分，提供了一种统一的接口，用于访问内核虚拟内存映像，并支持实时内核和内核核心转储。为了促进在非 FreeBSD 平台上调试内核核心转储，libkvm 需要支持这些平台。第三部分的另一个目标是提供一个可移植的 libkvm 变体，将原始 FreeBSD 源代码与可移植的构建系统集成，类似于其他 \*-portable 包（如 openssh-portable）。希望 libkvm-portable 能够支持在所有由 LLDB 支持的平台上，在 LLDB 中处理 FreeBSD 内核核心转储，包括不同的操作系统和不同的架构。FreeBSD 上的实时内核调试支持将会添加，从 amd64 开始，然后在时间允许的情况下扩展到其他平台（如 arm64 和 i386）。

## LLDB 改进第二部分 – 额外的 CPU 支持、跟踪 Fork 操作和 SaveCore 功能

完成

FreeBSD 的基础系统包括 LLDB，这是 LLVM 家族的调试器。与 GNU GDB 调试器相比，FreeBSD 的 LLDB 目前存在一些限制，尚未完全取代 GDB。这个多阶段项目旨在为 FreeBSD 提供现代化的调试器，使 LLDB 更接近于一个功能齐全的 GDB 替代品。

[LLDB 改进项目的第一部分](https://freebsdfoundation.org/project/lldb-debugger-improvements/)描述了用现代方法替换 FreeBSD x86_64 上过时的 LLDB 插件模型，该方法在单独的 lldb-server 进程下执行目标进程。传统的单体目标支持仍然在非 x86 目标上使用。该项目的第二部分涉及将一些非 x86 CPU 架构切换到新的远程进程插件框架，并完全移除旧的本地调试进程插件。一旦移植完成，将重点重新执行所有 ARM64 上的 LLDB 测试，并在时间允许的情况下解决任何错误，将非平凡的问题标记为已知故障。

第二部分的其他里程碑包括：

1. 支持跟踪 Fork 和 vfork 操作，以便与 GNU GDB 相媲美地调试子进程。
2. 添加 follow-spawn 以增强进程跟踪支持（如果时间允许）。
3. SaveCore 功能，允许用户按需创建核心转储文件。
4. 在 FreeBSD 手册中记录改进后的 LLDB 支持。

## LLDB 改进第一部分 – 基础设施改进

完成

FreeBSD 的基础系统包括 LLDB，这是 LLVM 家族的调试器。与 GNU GDB 调试器相比，FreeBSD 的 LLDB 目前存在一些限制，尚未完全取代 GDB。这个多阶段项目旨在为 FreeBSD 提供现代化的调试器，使 LLDB 更接近于一个功能齐全的 GDB 替代品。

FreeBSD 的 LLDB 使用的传统单体目标支持在同一进程空间中执行调试器的前端和后端，并依赖于一个过时的插件模型，技术债务日益增加。其他受支持目标上使用的现代 LLDB 插件方法是在单独的 lldb-server 进程下执行目标进程。这提高了可靠性，并简化了 LLDB 自身的进程/线程模型。此外，远程和本地调试都采用相同的方法。该项目的第一部分涉及为 FreeBSD x86_64 开发基本的远程进程插件，并将该工作上游提交到 LLVM。迁移到新进程模型完成后，将对 LLDB 的测试套件进行审查，并在时间允许的情况下进行必要的修复。此项工作预计在 2020 年完成。

## 针对 Linuxulator 兼容性的改进

完成

基金会此前资助了改善 Linux ABI 层（“Linuxulator”）的项目，重点是基础设施和诊断工具。这些早期项目为进一步的工作奠定了良好的基础，并修复了许多问题，但对用户的实际影响并不一定明确。

基金会已向 Edward Tomasz Napierała 授予开发资助，旨在调查在 Linuxulator 下运行一系列流行的客户端和服务器相关的 Linux 应用程序，并修复或记录发现的问题。

感兴趣的服务器软件应用程序将来自 Docker Hub 中的流行镜像。将识别出一些客户端应用程序，从基本的“烟雾测试”案例（如 xterm）到大型应用程序（如 Firefox、Chrome、VLC 等）。

该项目于 2021 年第一季度完成。

## DRM 图形驱动更新

完成

FreeBSD 当前的直接渲染管理器（DRM）图形驱动程序在源代码树之外进行维护。这部分是由于许可问题，因为它们依赖于 GPL 下的一些 Linux 代码（尽管驱动程序本身是双重 BSD + GPL 许可）。这些驱动程序也越来越过时。

该项目将更新 DRM 驱动程序至较新版本的 Linux，最初目标是长期支持（LTS）内核版本 5.4，并在可能的情况下实现 BSD 许可的内核兼容性适配层。一旦完成，将继续更新到更新的 Linux 内核版本。

这项工作将使我们在图形驱动程序的开发和支持方面处于更好的位置，包括为非 x86 平台的图形支持后续工作提供便利。

## ZStd 集成到 OpenZFS

完成

ZFS 是一个结合了文件系统和逻辑卷管理器的设计，旨在防止数据损坏并支持高存储容量。OpenZFS 提供了一种透明的压缩功能，能够在存储数据之前对其进行压缩，并在将数据返回给应用程序之前进行解压缩。这种压缩不仅节省空间，而且借助高性能的压缩算法，可以通过减少数据总量来降低读写延迟。

OpenZFS 提供了两种主要的压缩选项，分别是 LZ4（高速，低节省）和 gzip（低速，高节省）。如今，预期的压缩比大约在 1.1 到 2.0 倍之间。

将 ZStd 压缩算法集成到 OpenZFS 中，这是一种中速且高节省的压缩算法，将在对性能影响最小的情况下提供额外的空间节省。使用 ZStd 预期的压缩比范围在 1.1 到 3.6 倍之间。

该项目将与其他 OpenZFS 开发者合作，更新和增强 Allan Jude 的原始原型实现，以准备将其合并到正式的 OpenZFS 中。工作还将包括额外的测试、向后兼容性改进、文档和性能分析。

## if_bridge 性能提升

完成

当前的 if_bridge 实现严重依赖于单个 BRIDGE_LOCK 互斥锁。因此，其性能限制在每秒略高于 100 万个数据包，无论系统中有多少核心。这意味着，对于小数据包，它几乎可以饱和 1Gbps 的链路，但也仅此而已。对于完整的（1500 字节）数据包，它可以饱和 10Gbps 的链路，但无法满足 40Gbps 或更高速度的链路。系统在等待获取桥接锁的过程中花费了绝大多数时间。

总体思路是用两个读多写锁替换单个互斥锁，一个保护整体桥接，另一个保护转发表。绝大多数数据包只需要读取锁，从而允许多个核心同时通过桥接传输数据包。

该项目正在进行中，目标完成日期为 2020 年春初。

## 可扩展性和性能提升

完成

每年，CPU 的核心和线程数量不断增加，而在这些新 CPU 上运行 FreeBSD 往往会显示出新的可扩展性瓶颈。该项目将使用一些激励性的用例，例如“poudriere -j 128”软件包构建和“will-it-scale”。

在此过程中可能会发现并解决可扩展性诊断工具（如 LOCK_PROFILING）中的不足。该项目预计将带来可共享锁、VFS 名称缓存锁、进程管理的改进，以及多个内核子系统的性能提升。

## Linuxulator 诊断改进

完成

FreeBSD 长期以来提供了一个 Linux 系统调用兼容层，之前能够执行大多数 Linux 二进制文件（在某些情况下速度甚至超过 Linux）。不幸的是，它最近没有得到太多开发，已逐渐落后，无法执行大多数现代 Linux 二进制文件。

该项目将为调试运行现代 Linux 二进制文件时遇到的失败提供坚实的基础，并在二进制和源代码级别改善 Linux 兼容性。同时，它还将清理现有的 Linuxulator 实现，使其更容易和更快速地移植最初为 Linux 编写并主要在 Linux 下维护的软件。

## FUSE 用户空间文件系统更新

完成

FreeBSD 的 fuse(4) 驱动程序存在错误且过时。它基本上无法用于任何网络文件系统，如 CephFS、MooseFS 或 Tahoe-LAFS。该项目将修复所有已知的 fuse 错误，更新内核 API，并添加新的测试套件。

FUSE（用户空间中的文件系统）允许 FreeBSD 系统挂载由用户空间守护进程提供服务的文件系统，大多数 FUSE 守护进程很容易移植到 FreeBSD。截至本文撰写时， Ports 中包含 41 个 FUSE 文件系统。其中最受欢迎的是 fuse-ntfs，这是使用 FreeBSD 访问 Microsoft NTFS 格式媒体的唯一方法。

Fuse(4) 可以使用，但存在错误且不完整。在该项目开始时，错误跟踪器中有 26 个未解决的错误，其中一些已开放多年。最严重的是与缓存相关的错误，这可能导致任何 FUSE 网络文件系统中的数据损坏（在 Ports 中的 11 个，以及一些重要的非 Port 文件系统，如 CephFS 和 MooseFS）。

Fuse(4) 的内核 API（内核与文件系统守护进程之间的通信协议）大约滞后于标准 11 年。这意味着我们无法支持与缓存失效、ioctl(2)、poll(2)、chflags(2)、文件锁定、utimes(2)、posix_fallocate(2) 和 ACL 相关的一些功能。我们还缺少一些性能增强功能，如 readdirplus、异步直接 I/O、回写缓存、SEEK_HOLE 和异步读取。

该项目将修复所有已知的 fuse 错误，更新内核 API，并添加新的测试套件。

预计于 2019 年夏季完成。


## SDIO 集成

完成

该项目旨在集成 SDIO 支持，为支持 SDIO 连接的 WiFi 模块（如 Raspberry Pi 等设备）迈出第一步。

Raspberry Pi 3 和 Zero W，以及 3A+ 和 3B+ 都基于博通的 FullMAC WiFi 设备集成了 WLAN。这些设备通过 SDIO WiFi 连接。目前，FreeBSD 既不支持 FullMAC WLAN 驱动程序，也没有其他 SDIO WiFi 连接。

基于 Ilya Bakulin 的 MMCCAM SDIO 堆栈工作，该项目将帮助整合进一步的工作，并在必要时进行测试和增强，以提供 SDIO WiFi 通信基础设施。


## USB 大容量存储目标

完成

该项目提供了一个 USB 大容量存储目标，使得运行在嵌入式设备上的 FreeBSD 能够作为 USB 闪存驱动器出现，为用户提供必要的文档和驱动程序，以便充分利用嵌入式目标。这在教学和产品环境中是非常宝贵的，成为出色的“开箱即用”体验的一部分。

许多嵌入式板，例如 Beaglebone Black，提供 USB 目标或 USB On-the-Go (OTG) 接口。这允许嵌入式目标充当 USB 设备，并向 USB 主机（可能运行 FreeBSD、Linux、Mac OS、Windows、Android 或其他操作系统）呈现一个或多个接口（USB 设备类）。USB 设备类包括音频输入或输出（例如耳机）、大容量存储（USB 闪存驱动器）、人机接口设备（键盘、鼠标）、通信（以太网适配器）等。

## 博通 Wi-Fi 现代化

完成

该基金会资助了 Landon Fuller 的工作，以现代化 FreeBSD 对博通 Wi-Fi 适配器的支持，为 FreeBSD 上全面的博通 Wi-Fi 支持奠定基础，包括启用从博通的 ISC 许可的 Linux 驱动程序中采用额外的 softmac PHY 和 fullmac 设备支持。

此前，FreeBSD 对博通 Wi-Fi 适配器的支持由 bwn(4) 和 siba(4) 驱动程序提供，其中 siba(4) 负责调解 bwn(4) 访问通过片上 SSB 互连可访问的硬件核心。该项目将当前的 bwn(4) 驱动程序移植到 bhnd(4)——这是为了替换不再支持的 siba(4) 驱动程序而编写的，且被 FreeBSD/MIPS 博通移植使用——提供了一个统一的接口，支持 SSB 和 BCMA 互连，兼容 Wi-Fi 适配器和 Wi-Fi SoC。

该项目于 2018 年 2 月完成，并将在 FreeBSD 12.0 中发布。


## 开箱即用的无头模式

完成

该基金会资助了 Edward Napiarala 的工作，以提供 USB 供电功能（USB On The Go，USB OTG）的无头操作支持。虽然 FreeBSD 具备 OTG 支持，但默认情况下未启用或配置，且往往无法正常工作。这使得在嵌入式设备上使用 FreeBSD（例如 Raspberry Pi Zero）变得繁琐。

该项目旨在添加开箱即用的 USB OTG 支持，使 FreeBSD 对于缺乏设备来设置无头操作的新手以及寻求更友好的选项的公司来说，更具吸引力。

该项目的成功完成意味着用户只需下载映像，将其复制到 SD 卡上，通过 MicroUSB 电缆将开发板连接到笔记本电脑，然后…就完成了：控制台和网络将作为虚拟 USB 设备出现，随时可以使用。这将显著降低新用户在嵌入式设备上使用 FreeBSD 的门槛，使我们与 Linux 处于同一水平。

## ZFS 的“RAID-Z 扩展”功能开发

完成

Zettabyte 文件系统（ZFS）是一种组合文件系统和逻辑卷管理器，旨在防止数据损坏并支持高存储容量。

该基金会资助 Matthew Ahrens 开发“RAID-Z 扩展”功能。这将允许向现有的 RAID-Z 组添加额外的磁盘，例如将一个 4 宽的 RAID-Z1 组扩展为一个 5 宽的 RAID-Z1 组。

这将通过“重新排列”所有现有数据来实现，将数据重新写入新的磁盘排列中，在逻辑 RAID-Z 组的末尾（因此在每个物理磁盘的末尾）留出一个新的连续空闲空间。重新排列的数据仍将保持原有的逻辑条带宽度，即数据与校验的比例将保持不变，而新写入的数据将使用新的逻辑条带宽度，具有改进的数据与校验比。重新排列的过程将在在线进行的同时，其他 zfs 和 zpool 操作也可以进行。

该项目已完成。

## 将 'blacklistd' 守护进程移植到 FreeBSD

完成

该项目提供了一个轻量级的守护进程，可以实时通知各种守护进程的“恶意行为”尝试。该守护进程将攻击的数据存储在一个持久化数据库中，并可以更新数据包过滤器，以阻止来自攻击者网络地址的访问。

该项目于 2016 年 6 月完成，并在此之后进行了额外改进，并在 FreeBSD 11.0 中发布。

## 在 FreeBSD 中集成 VIMAGE 支持

完成

该项目旨在完善 VIMAGE 网络栈代码，使其准备好投入生产。首先将更新以前在 Perforce 仓库中审查过的工作，逐步测试补丁，向社区展示，并将其纳入 FreeBSD SVN 基系统仓库的头部/分支。重点关注的两个主要领域是 (i) 网络栈的拆卸和排序，以及 (ii) 在拆卸过程中填补最后剩余的内存泄漏。

该项目于 2016 年中完成。VIMAGE 是 FreeBSD 11 的一部分。在 2017 年 10 月，为了准备 FreeBSD 12.0，VIMAGE 默认启用。

## 增强网络栈虚拟化项目

完成

FreeBSD 开发者：Bjoern Zeeb

虚拟化的网络栈将显著增强 FreeBSD 的 jail 功能，使 jail 可以拥有自己完整且本地管理的网络栈，包括防火墙、路由和 IPsec 配置。基金会将资助 FreeBSD 网络开发者 Bjoern Zeeb 来增强现有原型，目前正在合并到 FreeBSD 8.x，并提供代码审查。

该项目于 2011 年完成。

## FreeBSD 的多路径 TCP

完成

多路径操作的 TCP 扩展（MPTCP）允许一个多宿主主机在单个 TCP 会话中利用多个网络接口或路径。该协议目前正在 IETF 中标准化，参考文献为 [RFC 6824](http://tools.ietf.org/html/rfc6824)。

基金会资助了一个专注于 FreeBSD 多路径 TCP 的硕士研究奖学金。从现有实现出发，网络栈的设计将被完善，并增加其他功能，目标是在 2015 年中期发布一个功能性实现。还计划在 2014 年和 2015 年初进行几次增量发布。

该项目的目标是设计和实现一个 FreeBSD MPTCP 栈，以促进进一步的 MPTCP 研究活动。关键在于实现一个可扩展的设计，以简化拥塞控制、调度和路径管理方案的实验。

之前已经发布了一个 [实验内核补丁](http://caia.swin.edu.au/urp/newtcp/mptcp/tools.html)。正在对 HEAD 分支进行持续开发。

目前正在进行的功能包括扩展单路径模块 CC 代码以与 MPTCP 连接一起使用，以及添加一个模块化的数据包调度框架。此过程的一部分涉及重构现有 MPTCP 会话管理代码的大部分，以及创建新的多路径特定协议挂钩，这些步骤减少了 MPTCP 代码与现有 TCP 代码之间的耦合。

基金会很高兴能够支持使用 FreeBSD 的大学研究，并通过这样的赞助为项目的增强作出贡献。

## FreeBSD ARMv8 64 位 ARM 移植

完成

开发者：Andrew Turner 和 Semihalf sp.j.

官方称为 AArch64 的 64 位 ARM 架构也被称为 ARMv8 和 arm64。与广泛采用 32 位 ARM 的嵌入式和移动市场相比，预计 64 位 ARM 架构将在传统服务器市场中找到应用。

FreeBSD 基金会与 ARM、Cavium、Semihalf sp.j. 和 Andrew Turner 合作，将 FreeBSD 移植到 arm64。Cavium 直接向基金会提供支持，为开发社区提供工程专业知识和硬件。Cavium 的 ThunderX 平台与 FreeBSD 作为服务器操作系统的优势非常契合，支持在单个封装中最多 48 个核心。ThunderX 将是该项目的初始参考目标，但后续还会移植到其他 arm64 平台。

该项目的总体目标是使 FreeBSD/arm64 达到一级地位，包括发布媒体和预构建的软件包集。有关 arm64 移植的更多信息，请访问 [FreeBSD wiki](https://wiki.freebsd.org/arm64)，正在进行中的源代码树可通过 FreeBSD 基金会的 [GitHub 账号](https://github.com/FreeBSDFoundation/freebsd/tree/arm64-dev) 获得。

## Newcons 控制台驱动集成

完成

FreeBSD 开发者：Aleksandr Rybalko、Ed Maste

Newcons 项目交付了一个更新的 FreeBSD 控制台驱动，增加了对 Unicode 的支持，并改善了对图形模式的支持。这提高了与 X11 和内核模式设置 (KMS) 图形驱动的互操作性。

该项目已集成，并在 FreeBSD 10.1 中进行了初始发布。对新控制台基础设施的其他改进仍在进行中。

## 改进硬件性能计数器支持

完成

FreeBSD 开发者：Joseph Koshy

在 Google 的慷慨资助下，FreeBSD 基金会与 Joseph Koshy 合作，旨在改善 FreeBSD 中的硬件性能计数器支持。该项目的目标是在 hwpmc 驱动中添加调用图支持。通过调用图支持，开发人员可以更清晰地可视化性能问题，了解确切的代码路径，而不仅仅是某个特定函数，因为该函数可能仅通过一条路径显示出问题，而其他路径却没有问题。除了对软件的改进外，Google 还提供了资金用于购买两台现代 CPU 机器，用于开发和测试。这些新机器被放置在由加拿大安大略省的 Sentex Corp 托管的网络性能集群中。

以下是更详细的新增功能列表：

* hwpmc 驱动现在支持调用链捕获，适用于内核和用户进程。
* 对于 i386 和 amd64 架构的内核（hwpmc 可用的架构），机器相关和无关的部分进行了增强，以支持 hwpmc(4) 调用图支持所需的额外功能。
* libpmc(3) 库已增强，以处理内核模块收集的新信息。
* pmcstat(8) 工具使用捕获的调用链数据生成两种类型的报告：(a) 传统的 gprof(1) 调用图和 (b) 调用链摘要，为收集到的数据提供两种不同的“视图”。
* 驱动程序 hwpmc(4)、命令行工具 pmcstat(8) 和接口库 pmc(3) 的手册页现在反映了可用的新功能。

该项目于 2007 年完成。

## 确保安全地移除挂载文件系统的磁盘设备

完成

FreeBSD 开发者：Edward Tomasz Napierala

该项目旨在使 FreeBSD 能够容忍活动磁盘设备的移除，例如当用户物理拔掉带有挂载文件系统的 USB 闪存设备时。目前，在这种情况下，系统可能会出现崩溃。该工作涉及在内核的关键部分添加适当的引用计数，并修改文件系统以正确处理“设备丢失”错误。

该项目于 2009 年完成。

## 对 FreeBSD TCP 堆栈的改进

完成

FreeBSD 开发者：Lawrence Stewart 和 [斯威本科技大学](http://caia.swin.edu.au/) 的高级互联网架构中心（CAIA）

该三部分项目将包括实现适当字节计数（ABC）RFC3465 支持、将 CAIA 的 TCP 研究统计信息（SIFTR）TCP 分析工具适配并合并到 FreeBSD 中，以及对 TCP 重新组装队列进行改进。

该项目于 2009 年 7 月完成。

## 无线网状网络支持

完成

FreeBSD 开发者：Rui Paulo

Rui Paulo 将为 FreeBSD 实现即将推出的 IEEE 802.11s 无线网状网络标准。预计无线网状网络将变得普遍，因为路由器和网络设备将部署它们，从而允许动态构建和扩展无线网络。对该标准的支持将使 FreeBSD 用户能够利用这一新技术。


#@ 扁平设备树项目

完成

FreeBSD 开发者：Rafal Jaworowski

Rafal Jaworowski 和 Semihalf 获得了一笔资助，以为 FreeBSD 提供对扁平设备树（FDT）技术的支持。该项目允许以平台中立和可移植的方式描述计算机系统的硬件资源及其依赖关系。

这一功能的主要消费者是嵌入式系统，其硬件资源分配无法探测或自我发现。FDT 的概念源自 Open Firmware IEEE 1275 设备树的概念（常规 Open Firmware 实现的一部分），并且在其他部署中作为 Power.org 嵌入式平台参考规范（ePAPR）的基础。

您可以在 [http://wiki.freebsd.org/FlattenedDeviceTree](http://wiki.freebsd.org/FlattenedDeviceTree) 上了解更多关于该项目的信息。

该项目于 2010 年完成。

## 高可用存储项目

FreeBSD 开发者：Pawel Jakub Dawidek

Pawel Jakub Dawidek 获得了一笔资助，以实施存储复制软件，使用户能够使用 FreeBSD 操作系统进行高可用配置，其中数据必须在集群节点之间共享。该项目部分由 [OMCnet Internet Service GmbH](http://www.omc.net/ "OMCnet Internet Service GmbH") 和 [TransIP BV](https://www.transip.nl/ "TransIP BV") 资助。

该软件将允许通过 TCP/IP 网络对任何存储介质（GEOM 提供者，使用 FreeBSD 术语）进行同步块级复制，并实现快速故障恢复。HAST 将利用 GEOM 基础设施提供存储，这意味着它将与文件系统和应用程序无关，并可以与任何现有的 GEOM 类结合使用。在主节点发生故障的情况下，集群将能够切换到从节点，检查并挂载 UFS 文件系统或导入 ZFS 池，并继续工作而不会丢失任何数据。

该项目于 2010 年完成。

## 网络栈虚拟化项目

完成

FreeBSD 开发者：Marko Zec

网络栈虚拟化项目旨在扩展 FreeBSD 内核，以维护多个独立的网络状态实例。这将允许系统上不同 jail 之间实现完全的网络独立性，包括为每个 jail 提供自己的防火墙、虚拟网络接口、流量限制、路由表和 IPSEC 配置。

该原型与 FreeBSD -CURRENT 保持同步，目前已经足够稳定以进行测试。它虚拟化了基本的 INET 和 INET6 内核结构和子系统，包括 IPFW 和 PF 防火墙等。下一步是对 IPSEC 代码进行完全虚拟化，并完善和记录管理 API。短期目标是为 FreeBSD 7.0-RELEASE 提供生产级内核支持的虚拟化网络（作为可插拔内核替换），同时继续与 -CURRENT 保持代码同步，以便将来可能合并。

该项目于 2008 年完成。

## 基于 FreeBSD Jail 的虚拟化项目

完成

FreeBSD 开发者：Bjoern Zeeb

Bjoern A. Zeeb 获得了一项资助，以改善 FreeBSD 的基于 jail 的虚拟化基础设施，并继续开发虚拟网络栈。他的雇主 CK Software GmbH 也在以工时形式匹配基金会的资助。

在过去的十年中，FreeBSD 以其基于 jail 的虚拟化而闻名。随着虚拟网络栈的引入，FreeBSD 的操作系统级虚拟化达到了一个新的高度。

该项目包括对两年的导入工作和开发进行清理，更重要的是，带来了网络栈拆解的基础设施。干净地关闭 FreeBSD 中的网络栈将是虚拟化领域面临的主要挑战，以使新特性达到 9.x 版本生命周期的生产就绪质量。

此外，该项目还包括虚拟网络栈框架的通用化，将公共代码分离出来。这将提供一个基础设施，并将最小化开销地简化进一步子系统（如 SYSV/Posix IPC）的虚拟化。所有进一步虚拟化的子系统将立即受益于共享的调试设施，这是新技术早期采用者的一个重要特性。

“改进的基于 jail 的虚拟化支持将继续保持轻量且易于管理，这将是未来几年的一大杀手级特性，”FreeBSD 开发者 Bjoern A. Zeeb 说。他还补充道：“这将使人们能够对他们的 FreeBSD 服务器进行分区，无需大量硬件就能运行模拟，或者在托管环境中相对轻松高效地提供数千个虚拟实例。虽然这符合绿色计算的趋势，但它也增强了 FreeBSD 的虚拟化组合，支持 Xen 或其他更重量级的虚拟机监控器，可以根据需要与 jail 混合使用。”

该项目的资助持续至 2010 年 7 月。

## DTrace 用户空间项目

完成

FreeBSD 开发者：Rui Paulo

Rui Paulo 获得了一项资助，以在 FreeBSD 中添加 DTrace 用户空间支持。

DTrace 是一个通用且轻量的跟踪框架，允许管理员、开发者和用户调查系统故障或性能瓶颈的原因。自 FreeBSD 8.0 起，FreeBSD 操作系统就支持内核专用的 DTrace，但缺少用户空间支持。具备用户空间支持的 DTrace 允许检查用户空间软件及其与内核的关联，从而提供更清晰的后台运行情况。

该项目将首先集中于添加 libproc 支持，包括符号与地址的映射、地址与符号的映射、断点设置以及 rtld 与 DTrace 的交互。接下来将重点关注 DTrace 进程控制，导入 pid 提供者并将其适配到 FreeBSD，同时移植用户空间静态定义探测提供者 (usdt)。最后将引入 plockstat 提供者。

“通过拥有用户空间 DTrace 支持，公司可以使其产品在 FreeBSD 上表现得更好，因为他们现在可以访问这个出色的工具，”FreeBSD 开发者 Rui Paulo 说。他还表示：“当我们将用户空间支持与内核侧的 DTrace 支持结合时，我们还可以使 FreeBSD 成为更好的操作系统，因为我们可以更容易地调查性能瓶颈。”

该项目于 2010 年 9 月完成。

## DAHDI FreeBSD 驱动程序移植

完成

FreeBSD 开发者：Max Khon

Max Khon 获得了一项资助，以完成 DAHDI FreeBSD 驱动程序的移植。

DAHDI/FreeBSD 项目的目的是使 FreeBSD 能够作为软件 PBX 解决方案的基础系统。

DAHDI（Digium/Asterisk 硬件设备接口）是一个开源设备驱动程序框架和一套用于 E1/T1、ISDN 数字卡和 FXO/FXS 模拟卡的硬件驱动程序（[http://www.asterisk.org/dahdi/](http://www.asterisk.org/dahdi/)）。Asterisk 是最流行的开源软件 PBX 解决方案之一（[http://www.asterisk.org/](http://www.asterisk.org/)）。

该项目包括将 DAHDI 框架和 E1/T1、FXO/FXS 模拟卡以及 ISDN 数字卡的硬件驱动程序移植到 FreeBSD。这还包括 TDMoE 支持、软件和硬件回声消除（Octasic, VPMADT032）以及硬件转码支持（TC400B）。该工作在官方的 DAHDI SVN 仓库中进行，并与 Digium 的 DAHDI 团队密切合作。

目前，大部分 DAHDI 组件已被移植，包括 DAHDI 框架本身、硬件驱动程序、TDMoE 驱动程序、软件和硬件回声消除（Octasic, VPMADT032）以及硬件转码（TC400B）。该项目托管在 [官方 DAHDI SVN 仓库](http://svn.digium.com/svn/dahdi/freebsd/) 中。

FreeBSD ports 集合中的 [misc/dahdi](http://www.freshports.org/misc/dahdi/) 现在包含 DAHDI/FreeBSD 的最新组件以及由于许可和版权限制而不在 DAHDI/FreeBSD SVN 中提供的一些内容。这些内容包括 OSLEC 回声消除器和实验性的 zaphfc 驱动程序。

该项目于 2010 年 9 月完成。

## 资源容器项目

完成

FreeBSD 开发者：Edward Tomasz Napierala

Edward Tomasz Napierala 获得了一项资助，以实现资源容器和简单的每个 jail 资源限制机制。

与 Solaris 区域（zones）不同，当前的 FreeBSD Jail 实现并不提供每个 jail 的资源限制。因此，用户通常被迫用其他虚拟化机制替代 jail。该项目的目标是创建一个统一的框架来控制资源使用，并利用该框架实现每个 jail 的资源限制。未来，同一框架可能会用于实现更复杂的资源控制，例如层次资源限制，或实现类似于 AIX WLM 的机制。它还可以用于提供精确的资源使用计量，以便于管理或计费。

“基金会决定资助这个项目真是太好了，”Edward 表示。“这将使基于 jail 的虚拟化在许多场景中成为更好的选择，例如对于虚拟专用服务器提供商。”

该项目于 2011 年初完成。

## BSNMP 改进项目

完成

FreeBSD 开发者：Shteryana Shopova

FreeBSD 基金会很高兴宣布 Shteryana Shopova 获得了一项资助，用于改进 BSNMP。

该项目包括对现有 FreeBSD SNMP 框架的几项增强功能，其中包括符合 SNMPv3 的用户身份验证、数据包加密和基于视图的访问控制。此外，该项目还包括一个新模块，该模块将允许对 FreeBSD 无线网络栈进行完整的 SNMP 管理和监控。项目完成后，FreeBSD 将成为构建基于开源的嵌入式无线设备的首选操作系统，这得益于其先进的无线网络栈能力，以及由 bsnmpd(1) 提供的轻量级、安全且完整的管理解决方案。使用 bsnmpd(1) 进行监控的现有 FreeBSD 安装也将从新增的安全功能和更细粒度的 SNMP 数据访问控制中受益。

“SNMP 是网络监控的事实标准，”FreeBSD 开发者 Shteryana Shopova 说道。她还补充道：“SNMP 无处不在——用于网络服务器、交换机、路由器、防火墙、工作站、IP 电话、打印机、不间断电源设备和各种嵌入式设备。很高兴有机会为 bsnmpd(1) 增加一些 FreeBSD 社区请求的功能。”

该项目于 2010 年 12 月完成。

## FreeBSD 和 PC-BSD 中的 IPv6 支持

完成

FreeBSD 开发者：Bjoern Zeeb

FreeBSD 基金会很高兴地宣布，已授予 Bjoern Zeeb 资助，以提高 FreeBSD 和 PC-BSD 中 IPv6 支持的成熟度。该项目由 iXsystems 联合赞助。

FreeBSD 基于 KAME 的 IPv6 参考实现最早出现在 FreeBSD 4.0 中，并广泛应用于各种基于 FreeBSD 的商业产品中。到目前为止，IPv6 是默认 FreeBSD 内核中可选配置的功能，但配置 IPv6 时通常也意味着同时配置 IPv4。由于许多“IPv6 准备好”的应用程序依赖双栈行为，破损的 IPv6 应用程序往往被忽视。为不带 IPv4 的内核添加 IPv6 支持，将使 FreeBSD 和 PC-BSD 成为开源和专有 IPv6 兼容应用软件的理想测试和开发平台。

“减少代码库对传统 IP 的依赖将有助于我们识别需要改进的操作系统和应用组件，以便在 IPv6 环境中良好运行。该项目将有助于确保 FreeBSD 作为全球互联网的组成部分继续在 IPv6 未来中占据重要地位：从根域名服务器、存储设备、路由器、防火墙、电视、桌面和移动系统，到全球一些最繁忙的网站，”Zeeb 先生说道。FreeBSD 基金会董事会成员兼 FreeBSD 核心团队成员 Robert Watson 将该项目描述为 FreeBSD 未来的关键，“Bjoern 的工作不仅会提高我们 IPv6 实现的成熟度，还将推动数百万部署的 FreeBSD 和其衍生系统上应用程序的改进。”该项目还将提高 FreeBSD IPv6 栈的质量和性能。

Bjoern Zeeb 是一位总部位于德国的顾问，自 2004 年起成为 FreeBSD 的活跃提交者。他目前也是 FreeBSD 安全和发布工程团队的成员，最近因其在 FreeBSD 中的 IPv6 工作荣获 Itojun 服务奖。

该项目于 2011 年 6 月完成。

## 为 Intel 驱动程序实现 GEM、KMS 和 DRI 支持

完成

FreeBSD 开发者：Konstantin Belousov

FreeBSD 基金会很高兴地宣布，Konstantin Belousov 已获得资助，为 Intel 驱动程序实现 GEM、KMS 和 DRI 支持。该项目由 iXsystems 共同赞助。

该项目的目标是实现 GEM、移植 KMS 并为 Intel 图形驱动编写新的 DRI 驱动程序，包括最新的 Sandy Bridge 集成图形单元。此工作将使最新的 Intel 开源驱动程序在 FreeBSD 上运行，从而扩大 FreeBSD 适用于桌面系统的硬件范围。

“基金会资助的项目将允许我花更多的时间在这项有趣的工作上，并希望解决 FreeBSD 桌面系统持续使用的一个重大问题，”Konstantin 表示。

iXsystems 公司首席技术官 Matt Olander 说：“为 GEM/KMS 提供支持将使 FreeBSD 和 PC-BSD 能在未来具有集成 3D 加速图形功能的高级架构上运行增强的本地图形支持。FreeBSD 长期以来在服务器市场占据主导地位，这是让 FreeBSD 成为笔记本、台式机和服务器完整平台的又一步。我们很高兴参与该项目。”

Konstantin 是一位软件开发者，居住在乌克兰基辅。他在 2006 年获得了 src 提交权限，自那时起，他将大部分空闲时间花在操作系统上，修复错误并实现他认为有趣的功能。他目前还担任项目的发布工程师和核心团队成员。

该项目于 2011 年 8 月完成。

## 五种新的 TCP 拥塞控制算法

完成

FreeBSD 开发者：斯威本科技大学

FreeBSD 基金会很高兴地宣布，斯威本科技大学高级互联网架构中心已获得资助，在 FreeBSD 中实现五种新的 TCP 拥塞控制算法。

正确运行的拥塞控制（CC）对互联网和 IP 网络的高效运行至关重要。拥塞控制动态地在流的吞吐量与对网络的推测影响之间取得平衡，必要时降低吞吐量以保护网络。

目前，FreeBSD 操作系统的 TCP 协议栈采用了事实上的标准——基于丢包的 NewReno 拥塞控制算法，但该算法在处理现代数据网络的诸多方面（如高丢包率或大带宽/延迟路径）时存在已知问题。研究界和工业界都在持续进行大量工作，解决与拥塞控制相关的问题，特别是在广泛部署和使用的 TCP 协议上。

斯威本科技大学与 FreeBSD 的 TCP 协议栈和拥塞控制实现的持续研究工作已逐步成熟。该项目旨在完善我们的原型并将其集成到 FreeBSD 中。

该项目于 2011 年 3 月完成。

## 前馈时钟同步算法

完成

FreeBSD 开发者：墨尔本大学

FreeBSD 基金会很高兴地宣布，墨尔本大学的 Julien Ridoux 和 Darryl Veitch 获得了资助，来实现前馈时钟同步算法的支持。

网络时间协议（NTP）被广泛用于通过网络进行同步，而 ntpd 守护进程是当前参考的同步算法。FreeBSD 的系统时钟目前是以 ntpd 为基础设计的，这导致了内核与同步守护进程之间的强耦合反馈。

[RADclock](http://www.cubinlab.ee.unimelb.edu.au/radclock/) 是基于前馈原理的另一类同步算法的一个示例。该项目将为前馈算法提供核心支持，使得可以开发和测试 ntpd 的替代方案。其核心动机在于这些方法在提供高度稳健和精确的同步方面具有巨大的潜力。

此外，虚拟化是时间保持系统即将面临的主要挑战之一。目前的反馈同步模型过于复杂，并引入了自身的动态，这种方法不适合虚拟化的要求。基于前馈的同步提供了一种更简洁、更简单的方法，能够在虚拟机实时迁移时提供精确的时间保持。

该项目于 2011 年 9 月完成。

## 实现 xlocale API

完成

FreeBSD 开发者：David Chisnall

C 标准库（libc）是 UNIX 系统中最重要的部分之一，因为大多数程序通过用 C 语言编写的接口与内核交互。在类似的 libc 实现之间移植代码是非常容易的，如果某个功能在 libc 中得到支持，高级语言可以使用它，而无需重新实现。

随着时间的推移，C 语言逐渐演变以适应现代多核系统，但仍然存在一些问题区域，其中之一就是本地化支持。C 语言最初并不支持本地化。FreeBSD 的 libc 和 Darwin 的 libc（Mac OS X 使用的库）相似，这使得从 OS X 移植代码到 FreeBSD 比移植到 Linux 容易得多。OS X 使用的 libc 支持一组扩展的本地化函数（xlocale），允许在每个线程的基础上设置本地化。

此外，LLVM 项目中的 libc++ 最初是在 Darwin 上开发的，因此它使用 xlocale 来支持大部分 C++ 的本地化功能。缺乏这种支持是将 libc++ 移植到 FreeBSD 的主要障碍。

一旦 FreeBSD libc 支持 xlocale，我们就可以将 libc++ 移植到 FreeBSD，从而为我们提供一个 MIT 许可的 C++11 标准库实现。结合 Clang 和 libcxxrt，这意味着 FreeBSD 中的整个 C++ 栈将不再包含任何 GNU 代码。此时，链接器将成为实现完全无 GPL 的 FreeBSD 10 唯一显著的障碍。

该项目于 2011 年 9 月完成。

## 分析 FreeBSD 的 IPv6 栈性能

完成

FreeBSD 开发者：Bjoern Zeeb

FreeBSD 基金会很高兴宣布已向 Bjoern Zeeb 提供资助，以分析 FreeBSD 的 IPv6 栈性能。该项目由 iXsystems 共同赞助。

去年，Bjoern 改进了 FreeBSD 的 IPv6 支持，使得构建不包含 IPv4 支持的 FreeBSD 系统成为可能。该项目将基于这一工作，专注于内核，分析 FreeBSD 的 IPv6 栈性能。不同用户在对比 FreeBSD 上的 IPv4 和 IPv6 性能时，发现了 IPv6 性能较低的情况。尽管不同版本之间的数据有所不同，但原因大多未知。

该项目将首先通过基准测试对 IPv6 和 IPv4 进行详细的性能分析，以获取最新的数据，帮助更好地理解当前的状况。接下来将继续确定性能差异的原因，并在可能的情况下直接解决这些问题，或为未来的工作确定改进方向。初步的基准测试数据将使我们能够通过重新运行测量来评估变更，并量化改进效果。

“随着全球开始部署 IPv6，流量模式从 IPv4 向 IPv6 转移，不仅需要关注正确性和稳定性，功能一致性和性能也至关重要，”开发者 Bjoern Zeeb 说道。“使性能数据与 IPv4 对齐将确保用户在使用 IPv6 时不会需要更多的资源。”

## 实现 auditdistd 守护进程

完成

FreeBSD 开发者：Paweł Jakub Dawidek

FreeBSD 的审计功能提供了针对安全相关事件的细粒度、可配置的日志记录。记录安全事件日志的一个关键目的是在系统遭到入侵时进行事后分析。目前，内核可以将审计记录直接写入文件或通过 /dev/auditpipe 设备进行读取。由于审计日志由内核本地存储，一旦系统被入侵，攻击者就可以访问这些日志，从而有可能清除其活动痕迹。

auditdistd 项目的目标是通过 TCP/IP 网络在本地 auditdistd 守护进程和远程 auditdistd 守护进程之间安全且可靠地分发审计记录。如果源系统遭到入侵，可以通过远程系统收集的数据分析攻击者的活动，因为此时只有远程系统的审计日志是可信的。

该项目于 2012 年 2 月完成。

## 已挂载文件系统的 Growfs

完成

FreeBSD 开发者：Edward Tomasz Napierała

该项目实现了在读写挂载状态下扩展 UFS 或 ZFS 文件系统的功能。此功能涉及对文件系统、GEOM 基础设施以及驱动程序的修改。

从系统管理员的角度来看，这使得可以通过 gpart(8) 扩展分区，然后使用 growfs(8) 调整其包含的文件系统大小，而无需先卸载文件系统。这对于扩展根文件系统特别有用，尤其对于虚拟机而言尤为重要。

该项目于 2012 年 11 月完成。

## 文档项目基础设施增强

完成

FreeBSD 开发者：Gabor Kovesdan

FreeBSD 文档项目长期依赖过时的工具来生成 FreeBSD 手册和其他文档。该项目将文档集升级到 DocBook 5.0，并提供了改进的渲染流程。

该项目于 2013 年 7 月完成。

## ARMv7 的超页支持

完成

FreeBSD 开发者：Zbigniew Bodek，Semihalf

ARM 架构正在扩展到高端服务器计算市场，支持该平台的复杂特性是 FreeBSD 在这些新领域取得成功的关键。该项目为大型内存工作负载增加了超页支持，以提升性能。

此项工作专门针对 ARMv7 架构，同时保持与 ARMv6 的兼容性。该项目由 FreeBSD 基金会和 Semihalf 共同资助。

该项目于 2013 年 9 月完成，并在 FreeBSD 10.0 中发布。

## 原生 iSCSI 内核栈

完成

FreeBSD 开发者：Edward Tomasz Napierala

该项目提供了一个原生的内核级 iSCSI 栈（包括目标和发起者），以支持日益流行的块存储协议。虽然已有多个支持 FreeBSD 的 iSCSI 实现，但项目缺乏一个高性能且可靠的内核级目标。iSCSI 栈首次出现在 FreeBSD 10.0 中。后续版本将进一步优化并支持硬件卸载。

该项目于 2014 年初完成，并在 FreeBSD 11.0 中发布。

## Capsicum 集成

完成

FreeBSD 开发者：Paweł Jakub Dawidek

该项目继续将 Capsicum 和 Casper 守护进程集成到 FreeBSD 中。新结构的能力权利增加了可能的能力权利数量，约为 1000，既支持了未来的开发，又保持了 API/ABI 兼容性。该项目还将 Casper、libcapsicum 和 libcasper 合并到 FreeBSD 中。

该项目于 2014 年初完成，并与 FreeBSD 11.0 一同发布。

## 基于 Autofs 的自动挂载程序

完成

FreeBSD 开发者：Edward Tomasz Napierała

amd(8) 自动挂载程序的局限性是许多 FreeBSD 用户反映的一个反复出现的问题。新的自动挂载程序项目旨在解决这些问题。

该自动挂载程序是对大多数其他 Unix 系统中可用功能的独立实现，使用通过 autofs 文件系统实现的内核支持。自动挂载程序支持标准的 Sun 映射格式，并与轻量级目录访问协议（LDAP）服务集成。

FreeBSD 基金会与企业和大学用户合作，在现有的基于 LDAP 的环境中测试新的自动挂载程序，其中包括一些具有数千个映射条目的环境。

该项目于 2014 年 9 月完成，并在 FreeBSD 10.1 和 11.0 中发布。

## UEFI 引导集成

完成

开发者：Ed Maste

统一可扩展固件接口（UEFI）为 x86 计算机提供引导和运行时服务，取代了传统的 BIOS。本项目旨在适配 FreeBSD 的加载程序和内核引导过程，以兼容当今服务器、台式机和笔记本电脑上常见的 UEFI 固件。

该项目建立在 Benno Rice 的赞助项目基础上，旨在改进 UEFI 引导程序，并于 2013 年提供了一个可行性证明。

此项目于 2014 年完成，并在 FreeBSD 10.1 和 11.0 中发布。

## OpenCrypto 的 AES 模式更新

完成

开发者：John-Mark Gurney

本项目为 FreeBSD 的 OpenCrypto 加密框架添加了现代 AES 模式，以供 IPsec 和其他使用者使用。该项目由 FreeBSD 基金会和 Netgate 联合赞助，Netgate 是一家领先的 BSD 基础防火墙和网络设备供应商。

该项目增加了新的加密模式，同时从 OpenBSD 导入了基础设施更新，为 FreeBSD 用户提供前所未有的高性能加密通信支持。新增模式包括 AES-CTR 和 AES-GCM，并使用 Intel 的 AES-NI 指令实现硬件加速。

该项目的工作于 2014 年 12 月提交到 FreeBSD，并在 FreeBSD 11.0 中发布。
