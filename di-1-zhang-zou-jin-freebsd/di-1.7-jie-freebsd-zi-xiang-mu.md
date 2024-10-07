# 第 1.7 节 FreeBSD 子项目

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

