# UEFI/BIOS 概述与警告

本节介绍 UEFI 和 BIOS 的基本概念、区别、警告事项以及技术信息。

## 警告与免责声明

本节包含重要的安全警告和免责声明，请务必仔细阅读。

BIOS 默认值通常经过厂商严格测试和优化，可在一般情况下确保系统稳定性和最佳性能。除非熟悉 BIOS 设置，否则请使用默认值，以避免系统损坏或启动失败。应仅在必要时更新或降级 BIOS。

BIOS 界面、选项和设置可能因系统不同而有所差异。

本注解基于公开资料及作者个人理解整理，可能存在技术误差、表达不当或致命错误。BIOS 作为计算机硬件的关键底层固件，其设置直接影响系统的稳定性和硬件安全。错误或不当的配置可能导致系统崩溃、硬件损坏、数据丢失，甚至设备无法启动等严重后果。本文件所述产品或系统的操作仅限经过专门培训、具备相关资质的专业人员，按照相关文档中的要求，尤其是其中的警告信息和安全指示进行操作。“具备资质的专业人员”是指那些基于其培训和经验，能够识别作业中存在的风险并避免潜在危害的人员。

作者及发布单位对本文档中包含的技术性或编辑性错误或遗漏不承担任何责任。本信息以“不附加任何保证”的方式提供，没有任何种类的担保。在法律允许的范围内，在任何情况下，作者及发布单位均不对偶然性、特殊性或继发性损失负责，包括停机成本、利润损失、因获取替代产品或服务而产生的损失，以及数据丢失或软件损坏。本文档包含的信息可能随时更改，恕不另行通知。本文中所涉及的其他产品和公司名称可能是其相应所有者的商标。使用前请务必做好数据备份，确保相关设置与设备兼容，并在受控环境中谨慎测试。

## 说明

本节的相关内容可参考华硕. NUC BIOS 概述[EB/OL]. [2026-03-26]. <https://www.asus.com.cn/support/faq/1052524/>，该文档提供了 BIOS 配置的基础说明。其他参考：英特尔公司. Unified Extensible Firmware Interface[EB/OL]. [2026-04-17]. <https://www.intel.com/content/www/us/en/developer/articles/tool/unified-extensible-firmware-interface.html>.EFI/UEFI 发展历史；

## 为什么选择 AMI BIOS

本节介绍 AMI BIOS 的技术特点和市场地位。AMI BIOS 是美国安迈科技公司（American Megatrends Inc.，简称 AMI）开发的 BIOS 固件，广泛应用于个人计算机和服务器平台。

据 AMI 官方网站介绍（美国安迈科技公司. The World Runs on AMI[EB/OL]. [2026-03-26]. <https://www.ami.com/about-us/>），全球约 70% 的服务器平台采用 AMI 软件。另据安迈信息科技（昆山）有限公司官网介绍“AMI 为 BIOS 业界公认领导者之一，整体市场占有率超过 65%”两个数据分别统计服务器市场和整体市场，均展示了 AMI 固件在市场中的主导地位。（安迈信息科技（昆山）有限公司官网[EB/OL]. [2026-03-26]. <https://www.ami.com.cn/>）

市场上大部分英特尔迷你主机所使用的 BIOS 均为 AMI BIOS，因此对 AMI BIOS 进行注解具有普遍意义，能够覆盖大多数实际应用场景。

## 技术信息

本节列出本注解的适用平台、版本信息以及基本符号说明。

- 本注解主要面向 Intel x86 平台，对 AMD 平台仅具有一定的参考价值。
- 此注解主要基于 AMI BIOS 5.27。
- 文中 (R) 标志为 ®，表示注册商标；TM 为 ™，表示该图形或文字作为商标使用，但尚未注册，通常指已向商标管理机构提交注册申请但尚未正式获准的商标。
- 置灰的选项表示在当前状态下不可被选中。
- 带有“▶”符号的项目，表示该选项包含子菜单。

## BIOS 与 UEFI 简介

本节介绍 BIOS 和 UEFI 的基本概念、发展历程及主要区别。

BIOS（Basic Input/Output System，基本输入输出系统）是计算机启动时最先执行的固件程序，多采用汇编语言编写以实现硬件直接操作。BIOS 最早出现于 20 世纪 70 年代（1974 年，加里·基尔代尔为 Intel 8080 微处理器开发的 CP/M 操作系统首次引入了 BIOS 概念），其工作流程包括加电自检（POST）、硬件初始化、引导加载等步骤，目的是识别和初始化处理器、内存、硬盘驱动器、光驱以及其他硬件。BIOS 采用实模式运行，地址空间限制在 1 MB 以内。

UEFI（Unified Extensible Firmware Interface，统一可扩展固件接口）是一种规范，定义了操作系统和平台固件之间的软件接口，多采用 C/C++ 编写以支持模块化开发。相比 BIOS，UEFI 具有支持更大磁盘分区（GPT）、图形界面、网络启动、安全启动（Secure Boot）等优势。UEFI 的原型 EFI 最早由 Intel 于 1998 年启动的 Intel Boot Initiative（IBI）计划开发，至 EFI 1.10 版本后于 2005 年交由统一 EFI 论坛（UEFI Forum）继续维护并更名为 UEFI。UEFI 取代了基本输入输出系统（BIOS）的固件接口，大多数 UEFI 固件实现仍提供对 BIOS 服务的遗留支持以兼容旧操作系统。

目前主流电脑（自 2012 年微软要求 Windows 8 认证必须支持 UEFI 起，约 2012—2013 年间）配备的都是 UEFI，而不是传统的 BIOS。由于 UEFI 在界面和操作逻辑上与 BIOS 类似，且需要向后兼容，人们仍习惯将其统称为 BIOS 或 UEFI BIOS。

## 设置 BIOS 后无法开机的处理方法（CMOS 简介）

本节介绍 CMOS 的基本概念以及在 BIOS 设置错误后如何恢复系统。

CMOS（Complementary Metal-Oxide-Semiconductor，互补金属氧化物半导体）原指一种由电池供电的芯片，用于存储 BIOS 配置信息（如时间信息、BIOS 密码和硬件设置等）。该芯片采用 CMOS 工艺制造，功耗极低，可由纽扣电池维持数据数月甚至数年。在现代 UEFI 系统中，系统的相关配置信息通常存储在非易失性 RAM（NVRAM）中，但出于习惯，人们仍将这种存储 BIOS/UEFI 设置的非易失性存储称为 CMOS。

清空 CMOS 可清除所有 BIOS 配置参数，恢复出厂默认设置。当 BIOS 设置错误导致系统无法启动时，可通过短接主板上的 CMOS 清除跳线、移除纽扣电池或使用专用按钮来清空 CMOS。具体操作方法因主板型号而异，可参考主板说明书或访问华硕官网（华硕. 主板如何 Clear CMOS[EB/OL]. [2026-03-26]. <https://www.asus.com.cn/support/faq/1040820/>）获取详细指导。

BIOS 是执行硬件初始化的固件程序，而 CMOS 是存储 BIOS 配置参数的硬件芯片。两者功能不同但紧密相关：BIOS 在启动时读取 CMOS 中的配置信息来初始化硬件。更多区别可参考联想官网（联想. BIOS 和 CMOS 有什么不同？[EB/OL]. [2026-03-26]. <https://iknow.lenovo.com.cn/detail/043962?type=undefined&amp;keyword=BIOS&amp;keyWordId=>）。

## 参考文献

- KILDALL G A. CP/M Operating System: System Description[M]. Pacific Grove: Digital Research, 1974. 参见 Intel Corporation. Unified Extensible Firmware Interface[EB/OL]. [2026-04-18]. <https://www.intel.com/content/www/us/en/developer/articles/tool/unified-extensible-firmware-interface.html>. CP/M 是早期微机操作系统的代表，UEFI 规范则由 Intel 发起以替代传统 BIOS。
- Intel Corporation. Intel Boot Initiative (IBI) and UEFI Forum Formation[EB/OL]. [2026-04-18]. <https://www.intel.com/content/www/us/en/developer/articles/tool/unified-extensible-firmware-interface.html>. 记载 Intel 启动倡议计划及 UEFI 论坛的成立过程。
- National Institute of Standards and Technology. FIPS 140-3: Security Requirements for Cryptographic Modules[S]. Gaithersburg: NIST, 2019. 参见 Chainguard. FIPS 140-3: Everything You Need to Know[EB/OL]. [2026-04-18]. <https://www.chainguard.dev/supply-chain-security-101/fips-140-3-everything-you-need-to-know>. 规定密码模块的安全要求与认证标准。
