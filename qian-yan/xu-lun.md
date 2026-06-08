# 绪论

绪论提供本书的整体概览，包括本书定位、对读者的要求、组织结构、书中命令及符号含义。

## 本书定位

本书涵盖 FreeBSD 15.x-RELEASE 与 14.x-RELEASE 的安装与日常使用，并尽可能向下兼容较早版本，同时包含部分 16.0-CURRENT 的内容。

本书主要面向 amd64（x86-64）与 arm64（AArch64）架构，并尽可能支持其他硬件架构。

本书测试环境为 Windows 11，并保持系统更新。

## 对读者的要求

本书以高等院校计算机科学与技术专业一般本科毕业生的合格及以上水平为难度基准。读者应具备以下基础知识：

- 操作系统基本概念（进程、内存管理、文件系统等）
- 命令行操作经验
- 计算机网络基础知识
- 英文阅读能力（用于阅读官方文档与 man 页面）

## 本书的组织结构

**第 1 章 FreeBSD 初见**：介绍 UNIX 的起源与发展，涵盖 GNU 操作系统与自由软件运动、Linux 与类 UNIX 系统的关系，以及 FreeBSD 的命名渊源与历史背景、其他 BSD 发行版概述。

**第 2 章 FreeBSD 导论**：深入探讨 FreeBSD 的理想与现实、项目宗旨与治理结构、开发模型与社区生态，并追溯 FreeBSD 的发展简史。

**第 3 章 FreeBSD 安装基础**：指导使用 FreeBSD 内置安装工具 `bsdinstall` 完成系统安装，涵盖 VMware、VirtualBox、Hyper-V 等虚拟化平台上的安装方法、安装故障排除，以及 USB 启动盘恢复为普通存储设备的方法。

**第 4 章 FreeBSD 高级安装**：介绍双系统配置、基于 Apple M1 平台的安装方案（Parallels Desktop、VMware Fusion Pro），以及腾讯云、阿里云、KVM/QEMU 等云平台和虚拟化环境中的安装方法。

**第 5 章 FreeBSD 基础**：面向 Windows、Linux 和 macOS 用户提供迁移指南，涵盖系统目录结构、虚拟控制台、shell 使用、命令行基础、文本编辑器、用户与权限管理及压缩工具等基础操作。

**第 6 章 软件管理**：介绍 FreeBSD 包管理器概述、软件源的更换方法，使用 pkg 管理二进制包、使用 Ports 以源代码方式安装软件、Ports 构建调优，以及使用 DVD 安装软件和 FreeBSD 镜像站现状。

**第 7 章 FreeBSD 系统更新**：介绍使用 freebsd-update、源代码方式或 pkgbase 更新 FreeBSD 的方法。

**第 8 章 网络管理**：介绍基础与高级网络配置、无线网络（Wi-Fi）配置、USB 网络共享、蓝牙、系统代理及 V2Ray、Mihomo 等代理工具的配置。

**第 9 章 X Window 系统**：介绍显卡驱动概论，Intel、AMD 和 NVIDIA 显卡驱动的安装与配置，系统字体的替换方法，以及远程桌面访问。

**第 10 章 桌面环境**：介绍在 FreeBSD 上运行的各类桌面环境与窗口管理器，包括 KDE 6（X11 与 Wayland 会话）、MATE、Xfce、Cinnamon、LXQt、GNOME、IceWM 及 CDE（拟删除）。

**第 11 章 多媒体和外部设备**：介绍 Web 浏览器、声卡配置、音频与视频播放器、打印机、摄像头、文档查看器、人机输入设备及多媒体处理工具的使用方法。

**第 12 章 本地化与输入法**：介绍本地化环境变量配置、特定语言的区域配置，以及 Fcitx、IBus 输入法框架和五笔输入法的安装与设置。

**第 13 章 Linux 兼容层**：介绍 FreeBSD 的 Linux 兼容层架构，涵盖 Rocky Linux、Ubuntu/Debian/Kali Linux、Arch Linux、Slackware、Gentoo 等多种 Linux 发行版的兼容环境搭建，以及微信、QQ、WPS Office 等 Linux 应用的运行方法和故障排除。

**第 14 章 游戏、科学计算和专业工具**：介绍 Godot 开源游戏引擎、Minecraft、Steam 客户端和 Wine 配置，以及科研和专业计算工具的使用。

**第 15 章 人工智能**：介绍人工智能概论与 AI 大模型在 FreeBSD 上的本地部署方法。

**第 16 章 系统管理**：讲解启动引导器、UEFI 固件管理、服务管理、进程与守护进程、用户分级、权限提升工具（sudo、doas 等）、bsdconfig 配置工具、OpenSSH、设备资源提示、定时任务、系统日志管理、sysctl 工具、NTP 时间同步及 Live 镜像与系统恢复等系统管理功能。

**第 17 章 存储管理**：介绍 USB 存储设备、内存盘、文件系统自动挂载、交换分区配置及加密交换分区。

**第 18 章 其他文件系统**：介绍 Windows、Linux 与 macOS 文件系统的使用。

**第 19 章 UFS 文件系统**：介绍 UFS 文件系统概述、添加 UFS 磁盘、磁盘扩展、磁盘快照、磁盘配额及磁盘加密。

**第 20 章 ZFS 文件系统**：涵盖 ZFS 的历史与现实、特性和术语、存储池管理、快照与扩容等 ZFS 核心管理操作、委托管理、启动环境及调优。

**第 21 章 安全**：介绍信息安全概论、账户认证安全、资源限制、安全等级、root 账户桌面登录、安全事件审计、OpenSSL、入侵检测系统（IDS）、第三方漏洞与安全公告，以及强制访问控制框架（MAC 框架）。

**第 22 章 防火墙**：介绍防火墙概论与 FreeBSD 内置防火墙系统，包括 Packet Filter（PF）、IPFilter（IPF）、IPFW 的配置，以及 Fail2Ban 和 blocklistd 工具的使用。

**第 23 章 Jail 容器管理**：介绍 FreeBSD 原生轻量级虚拟化技术 Jail 的基础配置、厚 Jail（Thick Jail）及 Qjail 管理工具的使用。

**第 24 章 Linux Jail**：介绍在 FreeBSD Jail 中运行 Linux 发行版的方法，涵盖 Linux Jail 基础准备，以及 Debian、Ubuntu、antiX Linux、Alpine Linux 等发行版的 Jail 创建与 GUI 配置。

**第 25 章 虚拟化与容器管理**：介绍使用 bhyve 及 vm-bhyve 工具安装 Windows 11、通过 BVCP 的 Web 界面管理 bhyve 虚拟机，以及 Podman 容器管理和在 FreeBSD 上安装 VirtualBox。

**第 26 章 数据库管理**：介绍数据库概论，以及 PostgreSQL、MySQL 及 MongoDB 在 FreeBSD 上的安装与配置，同时涵盖 pgAdmin4 管理工具的使用。

**第 27 章 文件传输协议（FTP）**：介绍文件传输协议（FTP）概述，以及 Pure-FTPd（基于 MySQL）、ProFTPd（基于 MySQL）、vsftpd 等 FTP 服务器的配置。

**第 28 章 服务器**：介绍 Rsync 数据同步、Samba 文件共享、NFS 服务器、零配置网络（mDNS/DNS-SD）及 Webmin 管理平台等服务的搭建。

**第 29 章 Web 服务器**：介绍 Apache、Nginx、Caddy Web 服务器的部署，以及 PHP、Tomcat、WildFly 应用服务器的配置，同时涵盖 Nextcloud、GitLab、OnlyOffice 和 OpenList 等应用的部署。

**第 30 章 监控系统**：介绍 Zabbix、Prometheus 监控系统的部署，以及 Telegraf、InfluxDB 与 Grafana 组成的监控平台架构。

**第 31 章 嵌入式平台**：介绍树莓派上 FreeBSD 的安装与使用、Linux 兼容层配置，以及 Radxa X4 x86 开发板、Linux 系统上交叉构建 FreeBSD、QEMU 模拟 RISC-V 架构，以及 STM32、乐鑫（Espressif）ESP-IDF、Arduino 等嵌入式开发环境的搭建方法。

**第 32 章 开发环境**：介绍 C/C++、Java、Qt、Python、Rust、Go、Node.js 等语言开发环境的搭建，以及 IDA Pro 调试、code-server 与 clangd 配置、Vim 开发环境和 DTrace 动态追踪工具的使用。

**第 33 章 FreeBSD 内核架构**：介绍 FreeBSD 源代码目录结构、内核文件结构、机器相关与无关的内核选项注解、GENERIC 内核选项及定制内核的构建方法。

**附录 I 工具与资源**：包括 BSD 许可证概览、Bug 报告流程、FreeBSD 邮件列表订阅、FreeBSD 开发参与指南及 microSD 卡参数简介。

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
>>应当接受所有可打印的 ASCII（RFC20）字符以及空格字符作为密码的一部分。
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

~~KDE 6 在 Wayland 上右键单击会导致黑屏~~（注：此问题可能已在后续版本中修复）

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
