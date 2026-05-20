# 4.3 macOS 用户迁移指南

macOS 与 FreeBSD 拥有共同的技术祖先——BSD（Berkeley Software Distribution）。macOS 的 Darwin 内核基于 XNU（X is Not Unix），XNU 融合了 Mach 微内核与 FreeBSD 内核子系统，因此 macOS 的用户空间大量代码直接源于 FreeBSD。理解这一渊源，便能更顺畅地从 macOS 迁移至 FreeBSD。

## 共同的 BSD 血统

macOS 的许多核心组件均可追溯至 FreeBSD：

- **TCP/IP 协议栈**：macOS 的网络栈源自 FreeBSD，可通过以下命令验证：

```sh
$ strings /usr/lib/system/libsystem_c.dylib | grep "FreeBSD" | head -5
```

- **POSIX 系统调用**：macOS 的 `open()`、`read()`、`write()`、`sendfile()` 等系统调用实现与 FreeBSD 高度一致；
- **文件系统层次结构**：部分目录布局相似（如 **/usr**、**/etc**、**/var**）；
- **BSD 子系统**：如 `kqueue` 事件通知机制、`sysctl` 接口、`pf` 防火墙等均源于 FreeBSD；
- **命令行工具链**：macOS 的大部分命令行工具源自 FreeBSD 而非 GNU（如 `sed`、`grep`、`awk` 等均使用 BSD 实现）。

> **思考题**
>
>>"天下大势，分久必合，合久必分。"
>
> macOS 与 FreeBSD 同出一源，却走向了截然不同的道路：一个成为消费电子帝国的基础，一个坚守服务器与嵌入式领域的阵地。如何理解开源软件与商业产品之间的分合逻辑？

### 参考文献

- Apple Inc. Darwin[EB/OL]. [2026-04-18]. <https://opensource.apple.com/>. Apple 开源的 Darwin 操作系统基础，包含 XNU 内核及 BSD 子系统。
- Levin J. Mac OS X and iOS Internals: To the Apple's Core[M]. New York: Wrox, 2013. ISBN: 978-1-118-05765-0. 系统剖析 macOS 内核架构与 BSD 子系统的关系。
- Levin J. *OS Internals, Volume I: User Space[M]. New York: Technologeeks Press, 2017. ISBN: 978-0-9910555-4-8. 深入分析 macOS 用户空间组件与 BSD 工具链的关系。
- FreeBSD Project. FreeBSD in the Apple Ecosystem[EB/OL]. [2026-04-18]. <https://freebsdfoundation.org/blog/freebsd-in-the-apple-ecosystem/>. FreeBSD 在 Apple 生态中的技术贡献与影响。

## 基本对比

| 操作系统 | 发布/生命周期 | 主要包管理器（命令） | 默认文件系统 | 许可证 | Shell | 桌面 |
| -------- | ------------ | ------------------ | ------------ | ------ | ----- | ---- |
| macOS | [每年秋季大版本发布](https://support.apple.com/guide/mac-help/mchlpx1065/mac)，安全更新约 3 年 | [Homebrew（`brew`）](https://brew.sh)/[MacPorts（`port`）](https://www.macports.org) | [APFS](https://developer.apple.com/documentation/foundation/file_system/about_apple_file_system)（默认不区分大小写，可选大小写敏感） | [APSL](https://opensource.apple.com/apsl/)/ECL | zsh（10.15 起）/bash（10.14 及以前） | [Aqua](https://developer.apple.com/macos/human-interface-guidelines/)（不可替换） |
| FreeBSD | [约 2/4 年](https://www.freebsd.org/security/) | [pkg/Ports](https://www.freebsd.org/ports/) | [ZFS](https://openzfs.org/)/[UFS](https://www.freebsd.org/doc/handbook/filesystems.html) | BSD | sh | 可选（KDE、GNOME、Xfce 等） |

macOS 与 FreeBSD 共享大量 BSD 组件，因此从 macOS 迁移至 FreeBSD 时的命令行适应成本低于从 Windows 迁移。

### 命令对比

| macOS 命令 | FreeBSD 等价/Port | 说明 | 备注 |
| --------- | ----------------- | ---- | ---- |
| `brew install` | `pkg install` | 安装二进制包 | pkg 包由官方构建系统统一构建，Homebrew 构建过程分散于用户设备 |
| `port install` | Ports 编译安装 | 从源代码编译安装 | MacPorts 直接源自 FreeBSD Ports 框架 |
| `launchctl` | `service` / `sysrc` | 管理服务/守护进程 | macOS 使用 launchd，FreeBSD 使用 BSD init + rc 系统 |
| `diskutil` | `gpart` / `zpool` / `zfs` | 磁盘与分区管理 | macOS 的 diskutil 封装了 diskarbitrationd |
| `idevice_id` 等 | 无直接对应 | iOS 设备管理工具 | FreeBSD 不提供此功能 |
| `ifconfig` | `ifconfig` | 网络接口配置 | 二者语法一致 |
| `sysctl` | `sysctl` | 内核状态查询/设置 | 二者用法一致，但变量名可能不同 |
| `pfctl` | `pfctl` | PF 防火墙管理 | 二者均使用 pf |
| `dmesg` | `dmesg` | 内核消息缓冲区 | 二者一致 |
| `route` | `route` | 路由表操作 | 二者基本一致 |

> **注意**
>
> macOS 中的许多命令行工具（如 `sed`、`grep`、`awk`）已是较旧版本，与 FreeBSD 当前版本相比存在差异。例如 macOS 的 `sed -i` 需要与 FreeBSD 相同的 `-i ''` 后缀语法，这一点与 GNU sed 不同。

### 关键差异对比

| 特性 | macOS | FreeBSD |
| ---- | ----- | ------- |
| 内核 | [XNU](https://github.com/apple-oss-distributions/xnu)（Mach + BSD） | FreeBSD 内核（单体式） |
| 初始化系统 | launchd（XML plist 配置） | BSD init + rc（Shell 脚本） |
| 设备驱动框架 | I/O Kit | 直接驱动或内核模块 |
| 系统完整性保护 | SIP（System Integrity Protection） | 无等效机制，通过安全等级实现部分功能 |
| 沙盒机制 | Seatbelt Sandbox（强制） | Capsicum/CASPER（按需） |
| 桌面环境 | Aqua（专有，不可替换） | 多种开源桌面环境可选 |
| 系统更新 | App Store / `softwareupdate` | `freebsd-update` / 源代码编译 |
| 图形架构 | Metal / Quartz | X11 / Wayland |
| 文件系统默认 | APFS（加密、快照、空间共享） | ZFS（校验、快照、RAID-Z） |

### 参考文献

- Apple Inc. About the Virtual Memory System[EB/OL]. [2026-04-18]. <https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/AboutMemory.html>. macOS 统一缓冲区缓存与 FreeBSD 共享技术渊源。
- FreeBSD Project. macOS-Compatible USB Device Management[EB/OL]. [2026-04-18]. <https://man.freebsd.org/cgi/man.cgi?query=usb>. FreeBSD 的 USB 子系统。
- Apple Inc. system integrity protection[EB/OL]. [2026-04-18]. <https://support.apple.com/zh-cn/guide/security/sec8d776632b/mac>. macOS 系统完整性保护（SIP）技术文档。

## 文件系统差异

### APFS 与 ZFS 对比

| 特性 | APFS | ZFS |
| ---- | ---- | --- |
| 校验和 | 仅元数据 | 元数据 + 数据（端到端） |
| 快照 | 支持 | 支持 |
| 克隆（写时复制） | 支持 | 支持 |
| 压缩 | 支持（LZ4、ZSTD 等） | 支持（LZ4、GZIP、ZSTD 等） |
| 加密 | 原生支持 | 原生支持（14.0+） |
| 去重 | 不支持 | 支持 |
| RAID | 不支持 | RAID-Z / RAID-Z2 / RAID-Z3 |
| 空间共享 | 容器内卷共享 | 存储池内数据集共享 |
| 最大卷/池大小 | 8 EB | 256 ZB（256 万亿亿字节） |
| 大小写敏感性 | 默认不区分 | 区分大小写（可设 `casesensitivity` 属性） |

macOS 的 APFS 默认不区分大小写（Case-Insensitive），而 FreeBSD 的 ZFS 和 UFS 均区分大小写。这是实际使用中最容易遇到的兼容性陷阱。

在 FreeBSD ZFS 上，可通过 `casesensitivity` 属性在数据集级别控制大小写敏感性：

```sh
# zfs set casesensitivity=sensitive pool/dataset   # 大小写敏感（默认）
# zfs set casesensitivity=insensitive pool/dataset # 大小写不敏感
```

### HFS+ 遗留问题

如果从使用 HFS+ 的旧版 macOS 迁移，还需要注意：
- HFS+ 默认也不区分大小写；
- HFS+ 使用 NFD（Normalization Form D）形式的 Unicode 规范化，而 FreeBSD 通常使用 NFC；
- 文件名中包含特殊 Unicode 字符（如带声调的字母 `é`）时，HFS+ 存储为分解形式（`e` + `´`），与 FreeBSD 的表现形式不同。

例如，在 macOS HFS+ 文件系统中：

```sh
$ echo "café" | xxd
# 某些 HFS+ 版本可能以 NFD 形式存储，即 café → cafe + ́（组合重音符）
```

这一问题在 macOS 切换到 APFS 后仍可能存在，取决于文件系统的原始来源。

### 参考文献

- Apple Inc. Apple File System Guide[EB/OL]. [2026-04-18]. <https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/>. APFS 官方技术指南，涵盖 APFS 功能、限制与最佳实践。
- OpenZFS. OpenZFS Documentation[EB/OL]. [2026-04-18]. <https://openzfs.org/wiki/Main_Page>. OpenZFS 项目文档，涵盖 ZFS 的所有特性与技术细节。
- Unicode Consortium. Unicode Normalization Forms[EB/OL]. [2026-04-18]. <https://unicode.org/reports/tr15/>. Unicode 规范化形式的技术规范（NFC、NFD 等）。
- Apple Inc. Technical Q&A QA1173: Text Encodings in OS X[EB/OL]. [2026-04-18]. <https://developer.apple.com/library/archive/qa/qa1173/>. Apple 关于 Unicode 规范化形式的说明，HFS+ 使用 NFD 变体。

## 包管理差异

macOS 中最流行的包管理器是 [Homebrew](https://brew.sh)，其次是 [MacPorts](https://www.macports.org)。MacPorts 直接继承自 FreeBSD Ports 框架的设计理念，使用 Tcl 编写，其 Portfile 与 FreeBSD 的 Makefile 在设计思路上有相似之处。

| 特性 | Homebrew | MacPorts | FreeBSD pkg/Ports |
| ---- | -------- | -------- | ----------------- |
| 二进制包 | 默认（Bottle） | 可选 | 默认（pkg） |
| 源代码编译 | 可选（`--build-from-source`） | 默认 | Ports 框架 |
| 安装路径 | **/opt/homebrew**（Apple Silicon）/ **/usr/local**（Intel） | **/opt/local** | **/usr/local** |
| 依赖管理 | 自动安装依赖 | 自动安装依赖 | 自动安装依赖 |
| 开发语言 | Ruby | Tcl | Makefile / Lua（pkg） |
| 软件源模型 | 社区维护（Homebrew/core） | 社区维护 | 官方 + 社区 |
| 与基本系统关系 | 独立于系统 | 独立于系统 | 与基本系统严格分离 |

### 安装第三方软件的实际差异

在 macOS 上使用 Homebrew：

```sh
$ brew install wget
```

在 FreeBSD 上安装同一软件：

```sh
# pkg install wget   # 使用二进制包
# cd /usr/ports/ftp/wget && make install clean  # 使用 Ports 编译
```

FreeBSD 的 pkg 包由官方构建集群（使用 poudriere）在干净 jail 环境中统一构建，确保了构建环境的一致性和可重现性；Homebrew 的 Bottle 则由 CI 构建，MacPorts 的源代码编译发生在用户本地设备上。

### 参考文献

- Homebrew. Homebrew Documentation[EB/OL]. [2026-04-18]. <https://docs.brew.sh/>. Homebrew 官方文档，涵盖 Bottle 构建与分发机制。
- MacPorts. MacPorts Guide[EB/OL]. [2026-04-18]. <https://guide.macports.org/>. MacPorts 使用指南，说明 Portfile 的设计与 FreeBSD Ports 框架的关系。

## 常见的路径差异

macOS 与 FreeBSD 在部分目录结构上存在差异：

| 路径 | macOS | FreeBSD |
| ---- | ----- | ------- |
| 用户主目录 | **/Users/username** | **/home/username** |
| 第三方软件安装 | **/opt/homebrew**、**/usr/local**、**/opt/local** | **/usr/local** |
| 临时文件 | **/private/tmp**（**/tmp** 为符号链接） | **/tmp** |
| 系统可执行文件 | **/bin**、**/usr/bin** | **/bin**、**/usr/bin**（14.0 起 **/bin** 为 **/usr/bin** 符号链接） |
| 守护进程配置 | **/Library/LaunchDaemons**（plist） | **/etc/rc.conf**、**/usr/local/etc/rc.d/** |
| 内核与内核模块 | **/System/Library/Kernels/** | **/boot/kernel/** |
| 套接字与 PID 文件 | **/private/var/run** | **/var/run** |
| 共享库缓存 | **/private/var/db/dyld/** | **/var/run/ld-elf.so.hints** |

### 参考文献

- FreeBSD Project. hier(7)[EB/OL]. [2026-04-18]. <https://man.freebsd.org/cgi/man.cgi?query=hier&sektion=7>. FreeBSD 文件系统层次结构手册页。
- Apple Inc. File System Programming Guide[EB/OL]. [2026-04-18]. <https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/>. macOS 文件系统编程指南，含目录结构说明。

## Gatekeeper、代码签名与软件验证

macOS 自 10.15 Catalina 起强制要求所有软件经过公证（Notarization），并默认要求应用签名。FreeBSD 无此类强制机制，软件安全更多依赖：

- **端口/包完整性**：通过校验和验证源代码包完整性；
- **pkg 签名**：支持对 pkg 仓库进行签名验证；
- **MAC 框架**：强制访问控制（Mandatory Access Control）可提供细粒度安全策略；
- **安全等级（securelevel）**：限定内核对系统文件的修改权限。

此外，macOS 的应用程序通常为 **.app** Bundle 格式（实际为目录），而 FreeBSD 与其他 UNIX 系统一样使用传统可执行文件路径（如 **/usr/local/bin/nvim**）。

### 参考文献

- Apple Inc. Notarizing macOS software[EB/OL]. [2026-04-18]. <https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution>. macOS 软件公证机制。
- FreeBSD Project. mandoc(1)[EB/OL]. [2026-04-18]. <https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=7>. pkg(7) 签名验证机制。

## 虚拟机与双系统

macOS 用户迁移至 FreeBSD 的常见路径：

### 在 macOS 上虚拟化 FreeBSD

使用以下虚拟化软件可在 macOS 上运行 FreeBSD：

- [UTM](https://mac.getutm.app/)：基于 QEMU 的免费虚拟化工具，支持 Apple Silicon 与 Intel，提供图形化界面。项目地址：<https://github.com/utmapp/UTM>；
- [Parallels Desktop](https://www.parallels.com)：商业虚拟化软件，对 macOS 兼容性良好；
- [VMware Fusion Pro](https://www.vmware.com/products/fusion.html)：2024 年起对个人用户免费。

> 关于上述工具的详细使用指南，参见本书第 3.3—3.5 节。

### 在 Apple Silicon Mac 上安装 FreeBSD

Apple Silicon（M1/M2/M3/M4）Mac 使用 ARM64 架构。FreeBSD 提供了 `FreeBSD-*-arm64-aarch64-*.img` 镜像，可借助 UTM 或 Parallels Desktop 安装。

> UTM 安装指南参见第 3.5 节。

### 在 Intel Mac 上双系统或纯 FreeBSD

Intel Mac 使用标准 x86-64（AMD64）架构，安装方式与 PC 一样。

**Boot Camp 与 FreeBSD 的兼容性**：

Boot Camp 助手主要为 Windows 设计。对于 FreeBSD，推荐：
1. 使用虚拟化方案（UTM、Parallels Desktop、VMware Fusion）；
2. 在 Intel Mac 上直接安装 FreeBSD 单系统。

在 Intel Mac 上直接安装 FreeBSD 时，需注意：
- Mac 的 UEFI 固件（较旧型号使用 EFI 1.x）可能与 FreeBSD 引导程序存在兼容性问题；
- 部分 Mac 型号的 T2 安全芯片可能阻止非 macOS 操作系统的安装（启动安全性实用工具可调整）；
- 键盘（Touch Bar 等）和触控板在 FreeBSD 上的驱动支持可能不完整。

### 参考文献

- Apple Inc. Start up your Intel-based Mac in macOS or Windows[EB/OL]. [2026-04-18]. <https://support.apple.com/en-us/102622>. Boot Camp 安装与切换 macOS 和 Windows 的官方指南。
- UTM. UTM Documentation[EB/OL]. [2026-04-18]. <https://docs.getutm.app/>. UTM 虚拟化工具官方文档，介绍在 macOS 中创建 FreeBSD 虚拟机的方法。

## 课后习题

1. 在 FreeBSD 中使用 `kldstat` 列出已加载的内核模块，与 macOS 的 `kextstat` 对比，分析二者模块管理机制的异同。
2. 查询 FreeBSD 的 `sysctl` 与 macOS 的 `sysctl` 共有变量，列出至少 10 个共有的内核状态变量。
3. 比较 macOS 的 launchd plist 与 FreeBSD 的 rc 脚本的语法与执行模型差异，将一段简单的 launchd plist 转换为 FreeBSD rc 脚本。
4. 在 HFS+ 卷中创建带 Unicode 组合字符的文件名（如 café̈），分别查看其在 macOS 与 FreeBSD NFS 挂载中的表示形式差异。