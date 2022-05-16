# 第四节 FreeBSD 发行说明

# FreeBSD 13.1 发行说明

> 原文链接 https://www.freebsd.org/releases/13.1R/relnotes/

### 摘要
FreeBSD 13.1-RELEASE 的发行说明包含了在 13-STABLE 开发线上对 FreeBSD 基本系统所做修改的摘要。这份文件列出了自上次发布以来所发布的相关安全公告，以及对 FreeBSD 内核和用户区的重大修改。同时还介绍了一些关于升级的简要说明。

### 简介

这份文件包含了 FreeBSD 13.1-RELEASE 的发行说明。它描述了 FreeBSD 最近增加、改变或删除的功能。它还提供了一些关于从以前版本的 FreeBSD 升级的说明。

这些发行说明所适用的发行版，代表了自 13-STABLE 创建以来沿 13-STABLE 开发分支的最新进展。有关这个分支的预编译二进制发行版的信息，可以在 https://www.FreeBSD.org/releases/ 找到。

这些发行说明所适用的发行版本代表了 13-STABLE 开发分支中介于 13.0-RELEASE 和未来的 13.2-RELEASE 之间的一个点。关于这个分支的预编译二进制发行版的信息，可以在 https://www.FreeBSD.org/releases/ 找到。

这个 FreeBSD 13.1-RELEASE 的发行版是一个发布版。它可以在 https://www.FreeBSD.org/releases/ 或其任何一个镜像中找到。关于获得这个(或其他) FreeBSD 发行版的更多信息，可以在 FreeBSD 手册的附录中找到。

我们鼓励所有用户在安装 FreeBSD 之前参考发行勘误表。勘误表文件会根据发布周期晚期或发布后发现的“迟发”信息进行更新。通常情况下，它包括已知的错误，安全公告，以及对文档的修正。FreeBSD 13.1-RELEASE 的勘误表的最新版本可以在 FreeBSD 网站上找到。

这份文件描述了自 13.0-RELEASE 以来 FreeBSD 中最容易被用户看到的新功能或变化。一般来说，这里描述的变化都是 13-STABLE 分支所特有的，除非特别标注为合并的特性。

典型的发布说明记录了在 13.0-RELEASE 之后发布的安全公告，新的驱动或硬件支持，新的命令或选项，主要的错误修正，或贡献的软件升级。他们也可能列出主要的 port/包的变化或发布工程实践。显然，发行说明不可能列出 FreeBSD 在不同版本之间的每一个变化； 这份文件主要关注安全公告、 用户可见的变化，以及主要的架构改进。

### 从以前的 FreeBSD 版本升级
使用 freebsd-update(8) 工具可以在 RELEASE 版本 (以及各种安全分支的快照) 之间进行二进制升级。二进制升级过程将更新未修改的用户区工具，以及作为官方 FreeBSD 发行版一部分的未修改的 GENERIC 内核。freebsd-update(8) 工具要求被升级的主机有互联网连接。

根据 /usr/src/UPDATING 中的说明，可以支持基于源代码的升级 (那些基于从源代码重新编译 FreeBSD 基本系统的升级) 。

所有 powerpc 架构的用户，在成功安装内核和 world 之后，需要手动运行 `kldxref /boot/kernel`。

> **只有在备份了所有数据和配置文件之后，才能尝试升级 FreeBSD。**

> **升级之后，sshd (来自 OpenSSH 8.8p1) 将不接受新的连接，直到它被重新启动。在安装了新的用户区之后，要么重新启动(按照源码升级程序中的规定)，要么执行 service sshd 重启。**

### 用户区
本节涵盖了对用户区应用程序、贡献的软件和系统实用程序的更改和添加。

#### 用户区配置的变化
在 /etc/defaults/rc.conf 中的 rtsol(8) 和 rtsold(8) 默认加入了 `-i` 标志，a0fc5094bf4c (由 https://www.patreon.com/cperciva 赞助)

用户区应用程序的变化
在 rtsol(8) 和 rtsold(8) 中加入了 `-i` 选项，以禁用零到一秒之间的随机延迟，从而加快了启动过程。8056b73ea163 (由 https://www.patreon.com/cperciva 赞助)

对于 64 位架构，基本系统在构建时默认启用了位置独立可执行文件 (PIE) 支持。您可以使用 `WITHOUT_PIE` 参数来禁用它。这需要一个干净的构建环境。396e9f259d96

有一个新的 zfskeys rc(8) 服务脚本，它允许在启动时自动解密用 ZFS 本地加密的 ZFS 数据集。请参阅 rc.conf(5) 手册以了解更多信息。33ff39796ffe, 8719e8a951b7 (由 Modirum 和 Klara Inc.赞助)

bhyve(8)中的 NVMe 模拟已经升级到 NVMe 规范的 1.4 版本，b7a2cf0d9102 - eae02d959363

bhyve(8) 中针对大型 IO 的 NVMe iovec 结构已被修复。这个问题是由 Rocky Linux 8.4 中包含的 UEFI 驱动程序暴露的。

为巴西葡萄牙语 ABNT2 键盘增加了额外的 Alt Gr 映射。310623908c20

chroot 工具现在支持非特权操作了，chroot(8) 程序现在有了 `-n` 选项来启用它。460b4b550dc9 (由 EPSRC 赞助)

对 CAM 库进行了修改，以便在解析设备名称之前对其使用 realpath(3) ，这使得诸如 camcontrol(8) 和 smartctl(8) 等工具在使用符号链接时能够更加友好，e32acf95ea25

md5sum(1) 和类似的消息加密程序与 Linux 上的程序兼容，如果程序名称以 sum 结尾，则让相应的 BSD 程序以 `-r` 选项运行，c0d5665be0dc (由 Netflix 赞助)

默认情况下，svnlite(1) 在联编过程中被禁用，a4f99b3c2384

mpsutil(8) 扩展到了显示适配器信息和控制 NCQ。395bc3598b47

使用 camcontrol(8) 将固件下载到设备后出现的问题，通过在固件下载后强制重新扫描 LUN 得到了修复。327da43602cc (由 Netflix 赞助)

在 bsdinstall(8) 中为变量磁盘名称的脚本分区编辑器增加了一种新模式。如果磁盘参数 DEFAULT 被设置为代替实际的设备名称，或没有为 PARTITIONS 参数指定磁盘，则安装程序将遵循自动分区模式中使用的逻辑，即如果有几个磁盘，它将为其中一个提供选择对话框，或在只有一个磁盘时自动选择。这简化了为具有不同磁盘名称的硬件或虚拟机创建全自动安装媒体的工作。5ec4eb443e81

### 贡献的软件
在所有 powerpc 架构上都启用了 LLDB 的构建，cb1bee9bd34

一个 True Awk 已经更新到了上游的最新版本 (20210215)。除了一个补丁之外，所有的 FreeBSD 补丁现在都已经被上传到了上游或被抛弃了。值得注意的变化包括：

- 区域划分不再用于范围

- 修复了各种错误

- 与 gawk 和 mawk 有更好的兼容性

剩下的一个 FreeBSD 变化，可能会在 FreeBSD 14 中被删除，就是我们仍然允许以`0x`为前缀的十六进制数字被解析和解释为十六进制数字，而所有其他 awk（现在包括 One True Awk）都将它们解释为 0，这与 awk 的历史行为一致。

zlib 升级到了 1.2.12 版。

libarchive 升级到了 3.6.0 版，在即将发布的补丁级别中增加了错误和安全修复。发布说明可以在 https://github.com/libarchive/libarchive/releases 找到。

ssh 软件包已经更新到 OpenSSH v8.8p1，包括安全更新和错误修复。其他的更新包括这些变化。

ssh(1)。当提示是否记录一个新的主机密钥时，接受该密钥的指纹作为"Yes"的同义词。

ssh-keygen(1)。当作为 CA 并用 RSA 密钥签署证书时，默认使用 rsa-sha2-512 签名算法。

ssh(1): 默认启用 UpdateHostkeys，但需要满足一些保守的前提条件。

scp(1)。远程拷贝到远程的行为 (例如 scp host-a:/path host-b:) 被修改为默认通过本地主机传输。

scp(1) 实验性地支持使用 SFTP 协议进行传输，以取代传统上使用的古老的 SCP/RCP 协议。

在 ssh 中启用了对 FIDO/U2F 硬件认证器的使用，并使用了新的公钥类型 ecdsa-sk 和 ed25519-sk 以及相应的证书类型。对 FIDO/U2F 的支持在 https://www.openssh.com/txt/release-8.2 中有所描述，a613d68fff9a (由 FreeBSD 基金会 赞助)

### 运行时库和 API
在 powerpc、powerpc64 和 powerpc64le 上增加了 OpenSSL 的汇编优化代码，ce35a3bc852

修复了对加速 ARMv7 和 ARM64 的加密操作的 CPU 特性的检测，大大加快了 aes-256-gcm 和 sha256 的速度。32a2fed6e71f（由 Ampere Computing LLC 和 Klara Inc.赞助）

在 riscv64 和 riscv64sf 上启用了构建 ASAN 和 UBSAN 库。8c56b338da7

OFED 库现已在 riscv64 和 riscv64sf 上构建。2b978245733

OPENMP 库现在已在 riscv64 和 riscv64sf 上构建，aaf56e35569

### 内核
本节涵盖了对内核配置、系统调校和系统控制参数的改变，这些改变没有其他分类。

内核的一般变化
powerpc64 上串行控制台的输出损坏已经被修复。

更改了 CAS 以支持 Radix MMU。

在使用 TCG 的 QEMU 上运行启用了 HPT 超级页的 FreeBSD，在 powerpc64(le) 上得到了修正。

在 powerpc64(le) 上的 pmap_mincore 增加了对超级缓存的支持。32b50b8520d

在 arm64 上为 32 位 ARM 二进制文件添加了 HWCAP/HWCAP2 辅助参数支持。这修正了在 COMPAT32 仿真环境下 golang 的构建/运行。28e22482279f (由 Rubicon Communications, LLC (`Netgate`)赞助)

### 设备和驱动
本节涵盖了自 13.0-RELEASE 以来对设备和设备驱动的变化和补充。

#### 设备驱动程序
igc(4) 驱动程序是为英特尔 I225 以太网控制器引入的。这个控制器支持 2.5G/1G/100Mb/10Mb 的速度，并允许 tx/rx 校验和卸载、 TSO、 LRO 和多队列操作，d7388d33b4dd (由 Rubicon Communications, LLC (`Netgate`) 赞助)

在 powerpc64(le) 的启动过程中，增加了对带有 AST2500 的 VGA/HDMI 控制台的修复，c41d129485e

在 virtio(4) 中的大 endian 目标上修复了 PCI 通用读/写功能。7e583075a41, 8d589845881

在 mpr(4) 中加入了对大 endian 的支持。7d45bf699dc, 2954aedb8e5, c80a1c1072d

减少了最大 I/O 大小，以避免 aacraid(4) 中的 DMA 问题。572e3575dba

修正了一个阻止使用 virtio_random(8) 的虚拟用户关闭或重启的 bug，fa67c45842bb

ice(4) 驱动程序已经更新到了 1.34.2-k，增加了固件日志和初始 DCB 支持，a0cdf45ea1d1 (由 Intel 公司赞助)

新增了 mgb(4) 网络接口驱动程序，它支持带有 PHY 的 Microchip 设备 LAN7430 PCIe 千兆以太网控制器和带有 RGMII 接口的 LAN7431 PCIe 千兆以太网控制器。e0262ffbc6ae (由 FreeBSD 基金会 赞助)

新增了对 cdce(4) 设备的链接状态、 媒体和 VLAN MTU 的支持。973fb85188ea

新增了 iwlwifi(4) 驱动程序和 LinuxKPI 802.11 兼容性层，以补充 iwm(4) 对较新的 Intel 无线芯片组的支持。(由 FreeBSD 基金会 赞助)

当内核被配置为 MMCCAM 选项时，内核崩溃转储现在可以通过 dwmmc 控制器保存在 SD 卡和 eMMC 模块上了。79c3478e76c3

当内核被配置为 MMCCAM 选项时，现在可以使用 sdhci 控制器在 SD 卡上保存内核崩溃数据。8934d3e7b9b9

#### 支持的平台
增加了对 HiFive Unmatched RISC-V 板的支持。

### 存储系统
本节涵盖了对文件系统和其他存储子系统（包括本地和网络）的改变和补充。

#### 一般存储
ZFS 的变化
ZFS 已经升级到 OpenZFS 2.1.4 版本。OpenZFS 的发行说明可以在 https://github.com/openzfs/zfs/releases 找到。

#### NFS 的变化
两个新的守护进程 rpc.tlsclntd(8) 和 rpc.tlsservd(8)，现在已经默认在 amd64 和 arm64 上建立了。它们提供了对 NFS-over-TLS 的支持，这在题为“实现远程过程调用默认加密”的互联网草案中有所描述。这些守护进程是在指定 WITH_OPENSSL_KTLS 的情况下建立的。它们使用 KTLS 来加密/解密所有的 NFS RPC 消息流量，并通过 X.509 证书提供可选的机器身份验证。2c76eebca71b 59f6f5e23c1a

用于 NFSv4 挂载的默认次要版本已被修改为 NFSv4 服务器支持的最高次要版本。这个默认值可以通过使用 minorversion mount 选项来覆盖。8a04edfdcbd2

增加了一个新的 NFSv4.1/4.2 挂载选项 nconnect，可以用来指定挂载时使用的 TCP 连接数，最多为16个。第一个（默认）TCP 连接将被用于所有由小型 RPC 消息组成的 RPC。由大型 RPC 消息组成的 RPC(Read/Readdir/ReaddirPlus/Write)将以轮流方式在其他 TCP 连接上发送。如果 NFS 客户端或 NFS 服务器有多个网络接口聚合在一起，或者有一个使用多个队列的网络接口，这可以提高挂载的 NFS 性能。9ec7dbf46b0a

增加了一个名为`vfs.nfsd.srvmaxio`的 sysctl 设置项，可以用来将 NFS 服务器的最大 I/O 大小从 128Kbytes 增加到 2 的任何幂数，直至 1Mbyte。它只能在 nfsd 线程未运行时进行设置，并且通常需要将 kern.ipc.maxsockbuf 增加到至少是首次尝试设置 `vfs.nfsd.srvmaxio` 时生成的控制台日志消息所建议的值。9fb6e613373c

#### UFS 更改
继 5cc52631b3b8 之后，fsck_ffs(8) 在 preen 模式下对后台 fsck 不起作用，在该模式下 UFS 被调整为没有软更新日志的软更新。修正: fb2feceac34c

### 引导加载器的变化
本节涵盖了启动加载器、启动菜单以及其他与启动相关的变化。

#### 引导加载器的变化
UEFI 启动对 amd64 进行了改进。装载器检测加载的内核是否可以处理原地暂存区（非复制模式）。默认是 copy_staging auto。自动检测可以被覆盖，例如：在 copy_staging enable 下，加载器将无条件地把暂存区复制到 2M，而不管内核的能力如何。另外，增长暂存区的代码更加健壮；为了增长，不再需要手工调整和重新编译加载器。(由 FreeBSD 基金会赞助)

boot1 和 loader 在 powerpc64le 上得到了修正。8a62b07bce7

#### 其他启动方面的改动
对 loader(8)、 nvme(4)、 random(4)、 rtsold(8) 和 x86 时钟校准进行了性能改进，这使得系统启动时间明显加快了。EC2 平台上的配置变化提供了额外的好处，使 13.1-RELEASE 的启动速度是 13.0-RELEASE 的两倍以上。(由 https://www.patreon.com/cperciva 赞助)

EC2 镜像现在被默认构建为使用 UEFI 而不是传统 BIOS 启动。请注意，基于 Xen 的 EC2 实例或“裸机” EC2 实例不支持 UEFI。65f22ccf8247 (由 https://www.patreon.com/cperciva 赞助)

增加了对在 AWS 系统管理器参数库中记录 EC2 AMI Ids 的支持。FreeBSD 将使用公共前缀 `/aws/service/freebsd`，导致参数名称看起来像`/aws/service/freebsd/amd64/base/ufs/13.1/RELEASE`。242d1c32e42c (Sponsored by https://www.patreon.com/cperciva)

### 联网
这一节说明了影响 FreeBSD 网络的变化。

#### 一般网络
对 IPv4 (sub) net (host 0) 上的最低地址的处理方式进行了修改，使得除非这个地址被设置为广播地址，否则数据包不会以广播方式发送。这使得最低的地址对主机来说是可用的。旧的行为可以通过 `net.inet.ip.broadcast_lowest` sysctl 来恢复。请参阅 https://datatracker.ietf.org/doc/draft-schoen-intarea-unicast-lowest-address/ 了解背景信息。3ee882bf21af

### 关于未来 FreeBSD 发行版的一般说明
#### 默认 CPUTYPE 的变化
从 FreeBSD-13.0 开始，i386 架构的默认 CPUTYPE 将从 486 变为 686。

这意味着，在默认情况下，所生产的二进制文件将需要一个 686 级的 CPU，包括但不限于由 FreeBSD 发行工程团队提供的二进制文件。FreeBSD 13.0 将继续支持更老的 CPU，然而需要这一功能的用户需要建立自己的官方支持版本。

由于 i486 和 i586 CPU 的主要用途一般是在嵌入式市场，一般最终用户的影响预计是最小的，因为采用这些 CPU 类型的新硬件早已淡出，而且据统计，这些系统的大部分部署基础已经接近退休年龄了。

这一变化有几个因素被考虑在内。例如，i486 没有 64 位原子，虽然它们可以在内核中被模拟，但不能在用户区被模拟。此外，32 位的 amd64 库从一开始就是 i686 的。

由于大部分的32位测试是由开发人员在 64 位硬件上使用 lib32 库，并在内核中使用 `COMPAT_FREEBSD32` 选项来完成，所以这种改变可以确保更好的覆盖率和用户体验。这也与大多数 Linux® 发行版已经做了相当长一段时间的工作相一致。

预计这将是 i386 中默认 CPUTYPE 的最后一次改变。

>**这一变化并不影响 FreeBSD 12.x 系列的发布。**

