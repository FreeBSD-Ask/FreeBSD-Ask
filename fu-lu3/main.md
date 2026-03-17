# Main 主菜单

本章节主要介绍 BIOS 主菜单的基本界面元素，包括顶部标题、菜单选项、主页面内容、帮助信息等。

![](../.gitbook/assets/R7HQ2ZAJNW76VA29V7AM-20250719125219-xv8j22t.png)

## 顶部标题

Aptio Setup - AMI

Aptio 设置 - AMI

## 菜单选项

BIOS 主菜单包含以下主要功能选项，每个选项对应不同的配置页面。

| 英文菜单    | 中文翻译   |
| ----------- | ---------- |
| Main        | 主菜单     |
| Advanced    | 高级       |
| Chipset     | 芯片组     |
| Security    | 安全性     |
| Boot        | 启动       |
| Save & Exit | 保存并退出 |

## 主页面内容

### BIOS Information（BIOS 信息）

本页面展示 BIOS 的基本信息，包括厂商、版本、兼容性等关键参数。

- BIOS Vendor（BIOS 厂商）: American Megatrends（安迈科技）
- Core Version（核心版本）: 5.27
- Compliancy（兼容性）: UEFI 2.8; PI 1.7
- Project Version（项目版本）: X4-V004
- Build Date and Time（构建日期和时间）: 03/05/2025 21:22:06（2025 年 03 月 05 日 21:22:06）
- M/B Name（主板名称）: RAXDA X4
- Access Level（访问级别）: Administrator（管理员）

### Processor Information（处理器信息）

本页面展示处理器的详细信息，包括名称、类型、频率等。

- Name（名称）: AlderLake ULX
- Type（类型）: Intel(R) N100
- Speed（频率）: 800 MHz
- ID（编号）: 0xB06E0
- Stepping（步进）: A0

步进（Stepping）：当制造过程有所改进，或者功能被修复或删除时，将为英特尔® 处理器创建新的步进代码。

目前常见的 Intel 处理器步进值通常由“一位字母 + 一位数字”组成，例如根据 [英特尔 ® 处理器 N100](https://www.intel.cn/content/www/cn/zh/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/ordering.html) [备份](https://web.archive.org/web/20260120163356/https://www.intel.cn/content/www/cn/zh/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/ordering.html) 的官方资料可知，其当前步进为“N0”（一般消费者获得的均为该步进）。字母越接近 Z，数字越大，通常表明步进版本越高，处理器相对较新。但上图 BIOS 显示该 N100 处理器的步进为“A0”，这通常表明其为工程样片。

参见：

- [英特尔 ® 处理器步进意味着什么？](https://www.intel.cn/content/www/cn/zh/support/articles/000057218/processors.html) [备份](https://web.archive.org/web/20260120163248/https://www.intel.cn/content/www/cn/zh/support/articles/000057218/processors.html)
- [CPU“步进”介绍](https://iknow.lenovo.com.cn/detail/320528) [备份](https://web.archive.org/web/20260120210927/https://iknow.lenovo.com.cn/detail/320528)

### Memory Information（内存信息）

本页面展示内存的基本信息，包括版本、容量和频率。

- Memory RC Version（内存 RC 版本）: 0.0.4.73
- Total Memory（总内存）: 16384 MB
- Memory Frequency（内存频率）: 4800 MHz

### Language and Time（语言与时间）

本页面用于配置系统语言、日期和时间。

- System Language（系统语言）: [English]（[英语]）
- System Date（系统日期）: [Sat 07/19/2025]（[2025 年 07 月 19 日 星期六]）
- System Time（系统时间）: [04:49:48]

## 右侧帮助信息

本区域提供当前选中选项的帮助说明，帮助用户了解各项功能的作用。

Choose the system default language（选择系统默认语言）

## 键盘帮助（底部右侧）

本区域提供操作快捷键说明，帮助用户快速导航和操作 BIOS 界面。

- →↑↓←: Select Screen / Item

  →↑↓←：选择页面 / 项目

- Enter: Select

  Enter：选择

- +/-: Change Opt.

  +/-：更改选项

- F1: General Help

  F1：常规帮助

- F2: Previous Values

  F2：上一次的值

- F3: Optimized Defaults

  F3：加载优化默认值

- F4: Save & Exit

  F4：保存并退出

- ESC: Exit

  ESC：退出

- K/k：对右上角的提示内容向上翻页
- M/m：对右上角的提示内容向下翻页

## 底部版本信息

本区域显示 BIOS 的版本信息和版权声明。

Version 2.22.1289 Copyright (C) 2025 AMI（版本 2.22.1289 版权所有 (C) AMI 2025）
