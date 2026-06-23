# 绪论

绪论提供本书的整体概览，包括本书定位、对读者的要求、组织结构、书中命令及符号含义。

## 本书定位

本书涵盖 FreeBSD 15.x-RELEASE 与 14.x-RELEASE 的安装与日常使用，并尽可能向下兼容较早版本，同时包含部分 16.0-CURRENT 的内容。

本书主要面向 amd64（x86-64）与 arm64（AArch64）架构，并尽可能支持其他硬件架构。

本书测试环境为 Windows 11，并保持系统更新。

> **注意**
>
> 本书中涉及的软件版本号、功能状态、兼容性情况等信息以撰写时为准，后续版本可能已有变化。读者在实际操作时应以当前官方文档为准。

## 对读者的要求

本书以高等院校计算机科学与技术专业一般本科毕业生的合格及以上水平为难度基准。读者应具备以下基础知识：

- 操作系统基本概念（进程、内存管理、文件系统等）
- 命令行操作经验
- 计算机网络基础知识
- 英文阅读能力（用于阅读官方文档与手册页）

## 本书的组织结构

**第 1 章 FreeBSD 初见**：介绍什么是 UNIX、GNU 操作系统和自由软件运动、Linux 与类 UNIX、什么是 FreeBSD，以及乔治·贝克莱与 BSD 文化传统。

**第 2 章 FreeBSD 导论**：深入探讨 FreeBSD 的理想、现实与中道，关于 FreeBSD 项目、FreeBSD 开发模型，并追溯 FreeBSD 简史。

**第 3 章 迁移指南**：面向 Windows、Linux 和 macOS 用户提供迁移指南，介绍其他 BSD 发行版概论和 BSD 许可证概览，帮助不同操作系统的用户顺利过渡到 FreeBSD。

**第 4 章 FreeBSD 安装基础**：介绍安装前的准备工作、FreeBSD 15 安装指南（AMD64）、安装故障排除，以及在 Windows 中将 USB 启动盘恢复为普通存储设备的方法。

**第 5 章 虚拟化平台安装 FreeBSD**：介绍使用 VMware Workstation Pro、VirtualBox、Hyper-V 安装 FreeBSD 的方法，以及基于 Apple M1 和 Parallels Desktop、VMware Fusion Pro 的安装方案。

**第 6 章 命令行环境**：涵盖虚拟控制台和终端、shell 基础、切换 shell、命令行基础、文本编辑器及压缩和解压缩等基础操作。

**第 7 章 网络管理**：介绍计算机网络基础、基础网络管理、无线网络管理、蓝牙、USB 网络共享及系统代理的配置方法。

**第 8 章 软件管理**：介绍 FreeBSD 包管理器概述、FreeBSD 软件源、使用 pkg 管理二进制包、使用 Ports 以源代码方式安装软件、Ports 构建调优、使用 DVD 安装软件及 FreeBSD 镜像站现状。

**第 9 章 显卡驱动**：介绍显卡驱动概论，Intel、AMD 和 NVIDIA 显卡驱动的安装与配置。

**第 10 章 X Window 系统**：介绍 X Window 系统概论、显示管理器、系统字体及远程桌面。

**第 11 章 Wayland 系统**：介绍 Wayland 概论及 Wayland 显示管理器。

**第 12 章 桌面环境**：介绍在 FreeBSD 上运行的各类桌面环境与窗口管理器，包括 KDE 6（X11 与 Wayland 会话）、MATE、Xfce、Cinnamon、LXQt、GNOME、IceWM 及 CDE（拟删除）。

**第 13 章 多媒体和外部设备**：介绍声卡、打印机、摄像头、人机输入设备、音频播放器、视频播放器、多媒体处理、文档查看器及 Web 浏览器的使用方法。

**第 14 章 本地化与输入法**：介绍本地化环境变量配置、特定语言的区域配置，以及 Fcitx、IBus 输入法框架和五笔输入法的安装与设置。

**第 15 章 FreeBSD 系统更新**：介绍使用 freebsd-update、源代码方式更新 FreeBSD 的方法，以及使用 PkgBase 更新基本系统和通过 ZFS 启动环境实现多版本共存。

**第 16 章 用户账户与权限**：介绍用户和基本账户管理、权限、用户分级及权限提升工具。

**第 17 章 系统引导**：介绍启动引导器、启动消息（dmesg）、引导管理器与 UEFI 固件、进程与守护进程及管理 FreeBSD 中的服务。

**第 18 章 FreeBSD 高级安装**：介绍安装双系统（先安装 FreeBSD 与后安装 FreeBSD），腾讯云轻量云、KVM/QEMU 等平台安装 FreeBSD（传统引导和 MBR 分区表），阿里云轻量应用服务器安装 FreeBSD（UEFI 和 GPT 分区表），以及 QEMU 安装 RISC-V FreeBSD（基于 x86 Windows 主机）。

**第 19 章 系统管理**：讲解系统目录结构、bsdconfig 配置工具、OpenSSH、设备资源提示、Cron 和 Periodic、系统日志管理、sysctl 工具、NTP 时间同步与时区及 Live 镜像与系统恢复等系统管理功能。

**第 20 章 Linux 兼容层**：介绍 FreeBSD 的 Linux 兼容层架构，涵盖 Rocky Linux、Ubuntu/Debian/Kali Linux、Arch Linux、Slackware、Gentoo 等多种 Linux 发行版的兼容环境搭建，以及微信、QQ、WPS Office 等 Linux 应用的运行方法和故障排除。

**第 21 章 游戏、科学计算和专业工具**：介绍 Godot 开源游戏引擎、我的世界（Minecraft）服务器与客户端、Steam 客户端、R 语言、Wine 配置，以及科研和专业计算工具的使用。

**第 22 章 人工智能**：介绍人工智能术语与概念、Transformer 数学基础与程序演示、人工智能哲学原著选读，以及大模型本地部署与 AI 编程工具（llama.cpp、Ollama、Claude Code、GitHub Copilot CLI）。

**第 23 章 开发环境**：介绍 C/C++、Java、Qt、Python、Rust、Go、Node.js 等语言开发环境的搭建。

**第 24 章 开发工具**：介绍 code-server 和 clangd 开发环境、Vim 开发环境、使用 IDA Pro 调试 FreeBSD 及 DTrace 动态追踪工具的使用。

**第 25 章 嵌入式平台及开发环境**：介绍树莓派上 FreeBSD 的安装与使用、Linux 兼容层配置，Radxa X4 x86 开发板，以及 STM32、ESP-IDF、Arduino 等嵌入式开发环境的搭建方法。

**第 26 章 高级网络**：介绍 TCP/IP 协议栈、网桥、链路聚合与故障转移及 VLAN 的配置方法。

**第 27 章 存储管理**：介绍 USB 存储设备、虚拟内存盘、文件系统自动挂载、新增交换分区及加密交换分区。

**第 28 章 其他文件系统**：介绍 Windows、Linux 与 macOS 文件系统的使用。

**第 29 章 UFS 文件系统**：介绍 UFS 文件系统概述、添加 UFS 磁盘、UFS 磁盘扩展、UFS 磁盘快照、UFS 磁盘配额及 UFS 磁盘加密。

**第 30 章 ZFS 文件系统**：涵盖 ZFS 的历史与现实、特性和术语、存储池管理、更新 ZFS 存储池、ZFS 管理、ZFS 调优、ZFS 委托管理、更新 OpenZFS 及启动环境。

**第 31 章 安全**：介绍信息安全概论、账户认证安全、资源限制、安全等级及 OpenSSL。

**第 32 章 安全审计**：介绍安全事件审计、入侵检测系统（IDS）、第三方漏洞与安全公告，以及强制访问控制框架（MAC 框架）。

**第 33 章 防火墙**：介绍防火墙概论与 FreeBSD 内置防火墙系统，包括 ipfirewall（IPFW）、IPFilter（IPF）、Packet Filter（PF）的配置，以及 Fail2Ban（基于 IPFW、PF 与 IPF）和 blocklistd 工具的使用。

**第 34 章 Jail 容器管理**：介绍 FreeBSD 原生轻量级虚拟化技术 Jail 的基础配置、厚 Jail（Thick Jail）及 Qjail 管理工具的使用。

**第 35 章 Linux Jail**：介绍在 FreeBSD Jail 中运行 Linux 发行版的方法，涵盖 Linux Jail 基础，以及 Debian、Ubuntu、antiX Linux、Alpine Linux 等 Jail 创建及 Linux Jail 中的 GUI 配置。

**第 36 章 虚拟化与容器管理**：介绍使用 bhyve 及 vm-bhyve 工具安装 Windows 11、通过 BVCP 的 Web 界面管理 bhyve 虚拟机、Podman 容器管理及在 FreeBSD 上安装 VirtualBox。

**第 37 章 数据库管理**：介绍数据库概论，以及 PostgreSQL、pgAdmin4、MySQL 及 MongoDB 在 FreeBSD 上的安装与配置。

**第 38 章 文件传输协议（FTP）**：介绍文件传输协议（FTP）概述，以及 Pure-FTPd（基于 MySQL）、ProFTPD（基于 MySQL）、vsftpd 等 FTP 服务器的配置。

**第 39 章 服务器**：介绍 Rsync 数据同步、Samba 文件共享、网络文件系统（NFS）、零配置网络（mDNS/DNS-SD）及 Webmin 管理平台等服务的搭建。

**第 40 章 Web 服务器**：介绍 Apache、Nginx、Caddy Web 服务器的部署，以及 PHP、Tomcat、WildFly 应用服务器的配置，同时涵盖 Nextcloud 云服务（基于 PostgreSQL）、OnlyOffice 部署（基于 PostgreSQL）、GitLab Enterprise Edition 部署和 OpenList 部署。

**第 41 章 监控系统**：介绍 Zabbix 监控系统（基于 PostgreSQL）、Prometheus 监控部署，以及 Telegraf、InfluxDB 与 Grafana 监控平台架构。

**第 42 章 FreeBSD 内核架构**：介绍 FreeBSD 源代码目录结构、内核文件结构、机器相关与机器无关的内核选项注解、GENERIC 内核选项注解（AMD64）、构建定制内核的方法，以及在 Linux 系统上交叉构建 FreeBSD。

**附录 I 工具与资源**：包括 Bug 报告流程、FreeBSD 邮件列表订阅、FreeBSD 开发参与指南、microSD 卡参数简介，以及 V2Ray、Mihomo 的配置方法。

**附录 II 参考文献与术语表**：列出全书核心参考文献和术语表。

**后记**：收录与 FreeBSD 相关的文学性内容，包括个人故事与感悟。

## 本书中的命令及符号含义

### 权限标识

`#` 表示在 `root` 权限下的操作，通常通过 `su`、`sudo` 或 `doas` 获得。

`$`、`%` 表示普通用户权限。本书中通常使用 `$` 作为普通用户提示符；在 FreeBSD 官方文档（例如 Handbook）中，也常使用 `%` 作为普通用户提示符。

### 提示块

#### 注意提示块

> **注意**
>
> 提示读者不应忽略的内容。

#### 技巧提示块

> **技巧**
>
> 提示一些有助于提高效率、转变思路的方法。

#### 警告提示块

> **警告**
>
> 如果不了解或不按要求执行，将无法完成操作或可能造成重大危害。

### 思考题

> **思考题**
>
>>美国国家标准与技术研究院（NIST）发布的数字身份指南（NIST. NIST SP 800-63B-4: Digital Identity Guidelines: Authentication and Authenticator Management[EB/OL]. (2025-07)[2026-04-04]. <https://pages.nist.gov/800-63-4/sp800-63b.html>）指出：
>>
>>必须要求，当密码被用作单因素认证机制时，其长度至少为 15 个字符。可以允许仅作为多因素认证过程一部分使用的密码较短，但必须要求其长度至少为 8 个字符。
>>
>>应当允许最大密码长度至少为 64 个字符。
>>
>>应当接受所有可打印的 ASCII（RFC 20）字符以及空格字符作为密码的一部分。
>>
>>应当接受 Unicode【ISO/IEC 10646】字符作为密码的一部分。在评估密码长度时，每个 Unicode 码点必须被计为一个字符。
>>
>>不得强制要求其他组成规则（例如，要求混合不同类型的字符）用于密码。
>
>>不得要求订阅者定期更改密码。然而，如果有证据表明认证器已被泄露，必须强制更改密码。
>>
>>不得允许订阅者存储提示信息（例如，关于密码如何创建的提醒），该提示信息不应能被未经认证的声明者访问。
>>
>>不得在用户选择密码时提示其使用基于知识的认证（KBA）（例如“你的第一只宠物叫什么名字？”）或安全问题。
>>
>>必须要求完整提供密码（而非部分提供），并且必须验证整个提交的密码（例如，不得截断密码）。
>
>>“尽管近年来不少专家一再批评现行密码规则的弊端，但银行、互联网平台和政府机构大多依然固守这些过时、无效甚至有害的规则。”（GoUpSec. “定期更换密码”是最愚蠢的密码规则？[EB/OL]. (2024-09-27)[2026-04-04]. <https://www.goupsec.com/news/17579.html>.）
>
> 问题：我们习以为常的“知识”究竟有没有坚实可靠的根基？我们固守的一些东西，究竟是一种传承，还是一种陈规陋习？如何划分二者的界限？

思考题旨在帮助有意愿探索和有动力追问的读者。这种形式类似于常见的课后习题，不同之处在于思考题的位置是随机的。需要说明的是，尽管可能预设了某些立场和理解，答案通常是开放的，具体取决于读者自身。此外，若读者感到疲惫，可以选择跳过。

### 特殊章节

```text
故障排除与未竟事宜
```

旨在将现存的问题、改进方向或未解的谜团留置其中，以期借助后人的智慧。

```text
课后习题
```

纯粹理论章节最后通常附有“课后习题”，用以帮助读者深入研讨章节内容。

### 删除线

~~为何人要活着？越是想探究生命的意义，越会陷入混乱。——《Caligula 卡里古拉》（和田纯一，导演. 卡里古拉[V]. 日本：Caligula 制作委员会，2018. <https://www.bilibili.com/bangumi/media/md77552>.）第三集标题。~~

~~KDE 6 在 Wayland 上右键单击会导致黑屏~~（注：2025 年 7 月此问题已通过 qt6-wayland 补丁修复）

删除线表示过时内容或带有诙谐意味的文字，它不属于正文部分；如无法理解相关典故，可直接跳过，不影响阅读。

## pkg 与 ports

FreeBSD 提供两种软件安装方式：pkg（二进制包管理）和 Ports（源代码编译）。这两种方式各有优势，可以根据实际需求选择使用，也可以混合使用。

pkg 是 FreeBSD 的二进制包管理器，通过预编译的软件包提供快速、便捷的安装方式，适合大多数用户的日常使用。Ports 则提供了从源代码编译安装的方式，允许用户根据需要自定义配置选项，适合需要定制化或优化的场景。

> **请注意**
>
> Ports 通常对应 HEAD 分支，建议 pkg 与 Ports 保持在同一主线上，即均选择 `latest`。也可以自行使用 pkg 对应的 Ports 季度分支，如 `2025Q1`。

如果要安装软件 `yyy`，`yyy` 在 Ports 里是 `xxx/yyy`，那么路径即为 **/usr/ports/xxx/yyy**。

首先可通过 pkg 安装二进制软件包，与绝大多数 Linux 发行版的用法一致：

```sh
# pkg install yyy
```

也可以采用以下方式：

```sh
# pkg install xxx/yyy
```

或采用简写形式：

```sh
# pkg ins yyy
```

还可通过 Ports 编译安装：

```sh
# cd /usr/ports/xxx/yyy
# make install clean
```

系统将陆续弹出配置窗口供用户选择。若采用默认选项，可执行以下命令：

```sh
# cd /usr/ports/xxx/yyy
# make BATCH=yes install clean
```

如果需要一次性完成所有依赖配置：

```sh
# cd /usr/ports/xxx/yyy
# make config-recursive # 将递归询问直至所有依赖配置完毕
# make install clean
```
