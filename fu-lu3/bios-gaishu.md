# UEFI/BIOS 概述与警告

## 警告与免责声明

默认值通常可提供最佳性能，可在一般情况下确保系统稳定性。除非你熟悉 BIOS 设置，否则请务必使用默认值，以避免系统损坏或启动失败。应仅在必要时更新或降级 BIOS。

BIOS 界面、选项和设置可能因系统不同而有所差异。

本注解基于公开资料及作者个人理解整理，可能存在技术误差、表达不当或致命错误。BIOS 作为计算机硬件的关键底层固件，其设置直接影响系统的稳定性和硬件安全。错误或不当的配置可能导致系统崩溃、硬件损坏、数据丢失，甚至设备无法启动等严重后果。本文件所述产品或系统的操作仅限经过专门培训、具备相关资质的专业人员，按照相关文档中的要求，尤其是其中的警告信息和安全指示进行操作。“具备资质的专业人员”是指那些基于其培训和经验，能够识别作业中存在的风险并避免潜在危害的人员。

作者及发布单位对本文档中包含的技术性或编辑性错误或遗漏不承担任何责任。本信息以“不附加任何保证”的方式提供，没有任何种类的担保。在法律允许的范围内，在任何情况下，作者及发布单位均不对偶然性、特殊性或继发性损失负责，包括停机成本、利润损失、因获取替代产品或服务而产生的损失，以及数据丢失或软件恢复损坏。本文档包含的信息可能随时更改，恕不另行通知。本文中所涉及的其他产品和公司名称可能是其相应所有者的商标。使用前请务必做好数据备份，确保相关设置与设备兼容，并在受控环境中谨慎测试。

## 说明

参见 [[NUC] NUC BIOS 概述](https://www.asus.com.cn/support/faq/1052524/)。

## 为什么选择 AMI BIOS

根据 AMI 官方网站 [The World Runs on AMI](https://www.ami.com/about-us/) 的介绍，全球约 70% 的服务器平台采用 AMI 软件。

根据 [安迈信息科技（昆山）有限公司](https://www.ami.com.cn/) [备份](https://web.archive.org/web/20260120155120/https://www.ami.com.cn/) 官网介绍，AMI 为 BIOS 业界的公认领导者之一，市场占有率超过 65％。

市场上大部分英特尔迷你主机所使用的 BIOS 均为 AMI BIOS。

因此，对 AMI BIOS 进行注解具有普遍意义。

## 技术信息

- 本注解主要面向 Intel x86 平台，对 AMD 平台仅具一定的参考价值。
- 此注解主要基于 AMI BIOS 5.27。
- 文中 (R) 标志为 ®，表示注册商标；tm 为 ™，表示该图形或文字作为商标使用，但尚未注册，通常指已向商标管理机构提交注册申请但尚未正式获准的商标。
- 置灰的选项表示在当前状态下不可被选中。
- 带有“▶”符号的项目，表示该选项包含子菜单。

## BIOS 与 UEFI 简介

BIOS：Basic Input/Output System，基本输入输出系统，多采用汇编语言编写。BIOS 最早出现于 20 世纪 70 年代。BIOS 的目的是识别和初始化处理器、内存、硬盘驱动器、光驱以及其他硬件。

UEFI：Unified Extensible Firmware Interface，统一可扩展固件接口。UEFI 是一种规范，定义了操作系统和平台固件之间的软件接口，多采用 C/C++ 编写。UEFI 的原型 EFI 最早出现在 20 世纪末。UEFI 取代了基本输入输出系统（BIOS）的固件接口，大多数 UEFI 固件实现仍提供对 BIOS 服务的遗留支持。

目前主流电脑（大约从 2013 年起）配备的都是 UEFI，而不是传统的 BIOS。也就是说，现在很多人可能根本没见过真正的 BIOS，但是出于习惯（界面和操作逻辑都类似），我们仍将 UEFI 统称作 BIOS 或 UEFI BIOS。

## 设置 BIOS 后无法开机怎么办（CMOS 简介）

CMOS（Complementary Metal-Oxide-Semiconductor，互补金属氧化物半导体）是计算机内部一种由电池供电的芯片，用于存储信息（如时间信息、BIOS 密码和 BIOS 设置等）。它通常与实时时钟（RTC）配合使用，系统的相关配置信息（如 UEFI/BIOS 设置）存储在非易失性 RAM（NVRAM）中。CMOS 一般是由纽扣电池供电的，部分嵌入式设备的 CMOS 电池是可充电式纽扣电池。

清空 CMOS 可清除上述参数。清空方法参见 [主板如何 Clear CMOS](https://www.asus.com.cn/support/faq/1040820/) [备份](https://web.archive.org/web/20260120204201/https://www.asus.com.cn/support/faq/1040820/)。

参见 [BIOS 和 CMOS 有什么不同？](https://iknow.lenovo.com.cn/detail/043962?type=undefined&keyword=BIOS&keyWordId=) [备份](https://web.archive.org/web/20260120204219/https://iknow.lenovo.com.cn/detail/043962?type=undefined&keyword=BIOS&keyWordId=)。
