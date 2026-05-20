# 4.3 macOS 用户迁移指南

从商标角度看，macOS 是符合标准的 UNIX 操作系统。~~因此，要安装 UNIX 的人可考虑 macOS。~~

从表面看，这是 Android 与 iOS 之争，实质上则是 Linux 与 BSD 之争。~~这也许还是大教堂与市集之争。~~

## 共同的 BSD 血脉

从历史角度看，macOS（以及由此衍生的 iOS、iPadOS 等）的核心层（Darwin）确实是基于 BSD 代码，并融合了其他技术，macOS 系列操作系统因此可视作独立的、类 BSD 操作系统分支，与 OpenBSD、NetBSD 和 FreeBSD 等系统具有同等地位。

| 组件     | 来源/说明                                                                   |
| ---- | ----------------------------------------------------------------------- |
| XNU 内核 | 基于 Mach 微内核（CMU）、NeXTStep/OpenStep 架构，整合 BSD 子系统                        |
| 网络栈    | BSD/FreeBSD TCP/IP 协议栈为核心，支持 IPv4/IPv6，包含 IOKIT 驱动接口；NKE（Network Kernel Extensions，网络内核扩展） |
| 虚拟文件系统 | 基于 BSD VFS，支持 HFS+、APFS、UFS 等文件系统                                       |
| 用户空间工具 | BSD 用户工具（如 ls、cp、grep 等），经过苹果改造和增强                                      |
| 内存管理   | Mach 虚拟内存管理（VM），受 BSD 内存管理机制部分影响，支持分页、保护和共享内存                           |
| 进程模型   | Mach IPC、Security Trailers、强制访问控制（MAC）机制，支持多任务和安全策略                     |

### 参考文献

- Apple Inc. Darwin[EB/OL]. [2026-04-18]. <https://opensource.apple.com/>. Apple 开源的 Darwin 操作系统基础，包含 XNU 内核及 BSD 子系统。
- LEVIN J. 深入解析Mac OS X & iOS操作系统[M]. 郑思遥, 房佩慈, 译. 北京: 清华大学出版社, 2014. ISBN: 978-7-302-34867-2.
- Jason Perlow. Apple's Open Source Roots: The BSD Heritage Behind macOS and iOS[EB/OL]. (2024-07-08)[2026-03-26]. <https://thenewstack.io/apples-open-source-roots-the-bsd-heritage-behind-macos-and-ios/>. 比较表格参考此处。

## 基本比较

macOS 与 FreeBSD 共享大量 BSD 组件，因此从 macOS 迁移至 FreeBSD 时的命令行适应成本低于从 Windows 迁移。

### 功能比较

|功能|macOS|FreeBSD|说明|
|---|---|---| ---- |
|shell|zsh|sh|FreeBSD 可选支持 zsh|
|权限提升|sudo|可选|FreeBSD 可选支持 sudo|
|软件管理（二进制包）|可选，通常为 Homebrew |pkg||
|软件管理（基于源代码）|MacPorts |Ports|MacPorts 源自 Ports |
|防火墙|pf (Packet Filter) |内置 pf (Packet Filter) 等多种防火墙|可选支持|
|服务管理|launchd（命令 `launchctl`）|BSD init + RC 系统|/|
|编译程序|Clang + LLVM |Clang + LLVM |/|
|生命周期|3年|4年|
|文件系统|APFS（默认）|ZFS（默认）|

> **注意**
>
> macOS 中的许多命令行工具（如 `sed`、`grep`、`awk`）已是较旧版本，与 FreeBSD 当前版本相比存在差异。例如 macOS 的 `sed -i` 需要与 FreeBSD 相同的 `-i ''` 后缀语法，这一点与 GNU sed 不同。

## 文件系统 APFS 与 ZFS 比较

| 特性 | APFS | ZFS |
| ---- | ---- | --- |
| 校验和 | 仅元数据 | 元数据 + 数据（端到端） |
| 快照 | 支持 | 支持 |
| 写时复制 | 支持 | 支持 |
| 压缩 | 仅支持上层特定文件压缩，非底层实时流压缩 | 支持（LZ4、GZIP、ZSTD 等） |
| 加密 | 原生支持 | 原生支持（14.0+） |
| 去重 | 不支持全局去重 | 支持 |
|克隆|支持|支持|
| RAID | 不支持 | RAID-Z / RAID-Z2 / RAID-Z3 |
| 空间共享 | 容器内卷共享 | 存储池内数据集共享 |
| 最大卷/池大小 | 8 EB | 256 ZB |
| 大小写敏感性 | macOS 默认不区分 | 默认区分（可通过属性调节） |

macOS 的 APFS 默认不区分大小写（Case-Insensitive），而 FreeBSD 的 ZFS 和 UFS 默认均区分大小写。

### 参考文献

- Apple Inc. File System[EB/OL]. [2026-04-18]. <https://developer.apple.com/documentation/foundation/about-apple-file-system>. APFS 官方技术指南。
- OpenZFS. OpenZFS Documentation[EB/OL]. [2026-04-18]. <https://openzfs.org/wiki/Main_Page>. OpenZFS 项目文档。
