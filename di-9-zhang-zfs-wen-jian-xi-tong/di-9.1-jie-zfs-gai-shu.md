# 9.1 ZFS 概述

ZFS 源于 Sun Solaris，2005 年以 CDDL 许可证开源，2007 年导入 FreeBSD。Oracle 收购 Sun 后 ZFS 转为闭源开发，开源社区于 2013 年发起 OpenZFS 项目延续其发展。2020 年 OpenZFS 2.0 统一了 FreeBSD 与 Linux 的 ZFS 代码库，提供写时复制、快照、端到端校验与自愈等存储特性。

## ZFS 特性和术语

ZFS 不仅仅是一个文件系统，它在本质上是不同的。ZFS 将文件系统和卷管理器的角色结合起来，使得新的存储设备可以添加到一个在线系统中，并且这些新的空间可以立刻在该池中现有的文件系统上使用。通过将传统上分开的角色合并，ZFS 能够克服之前阻止 RAID 组扩展的限制。*vdev* 是池中的顶级设备，可以是简单的磁盘，也可以是 RAID 阵列，例如镜像或 RAID-Z 阵列。ZFS 文件系统（称为 *数据集*）每个都可以访问整个池的合并空闲空间。池中已使用的块会减少每个文件系统可用的空间。这种方法避免了大量分区时常见的陷阱，其中空闲空间在各个分区中变得碎片化。

| ZFS 概念 | 解释 |
| -------- | ---- |
| 池 | 存储池是 ZFS 最基本的构建单元。一个池由一个或多个 vdev 组成，vdev 是实际存储数据的底层设备。基于池可以创建一个或多个文件系统（数据集）或块设备（卷），这些数据集和卷共享池中的剩余空闲空间。每个池拥有唯一的名称和 GUID，池的 ZFS 版本号决定了可用的功能。 |
| vdev 类型 | **磁盘 (Disk)**——最基本的 vdev 类型，可以是整个磁盘（如 **/dev/ada0**、**/dev/da0**）或单个分区（如 **/dev/ada0p3**）。在 FreeBSD 上使用分区而非整盘不会带来性能损失，这与 Solaris 文档的建议不同。<br><br>**文件 (File)**——常规文件也可构成 ZFS 池，适用于测试和实验场景。使用文件的完整路径作为设备路径来创建池（`zpool create`）。<br><br>**镜像 (Mirror)**——创建镜像时指定 `mirror` 关键字，后跟镜像成员设备列表。镜像由两个或更多设备组成，所有数据写入全部成员设备。镜像 vdev 的可用容量等于最小成员的容量，可承受除一个成员外所有成员的故障而不丢失数据。可随时使用 `zpool attach` 将单个磁盘 vdev 升级为镜像 vdev。<br><br>**RAID-Z**——ZFS 使用 RAID-Z，它是标准 RAID-5 的变体，具有更好的奇偶校验分布，消除了意外重启后数据与奇偶校验不一致的"RAID-5 写入漏洞"。ZFS 支持三种 RAID-Z 级别（raidz/raidz1、raidz2、raidz3），根据奇偶校验设备数量和可容忍故障磁盘数量提供不同级别的冗余。<br>以四个 1 TB 磁盘组成的 RAID-Z1 为例，实际可用存储约 3 TB，池可在一个磁盘故障时以降级模式运行；若在更换和重新校验前第二个磁盘掉线，则所有池数据将丢失。<br>以八个 1 TB 磁盘组成的 RAID-Z3 为例，可用空间约 5 TB，可承受最多三个磁盘故障。Sun 建议每个 vdev 不超过九个磁盘；若配置更多磁盘，建议拆分为多个 vdev 并跨 vdev 条带化数据。两个各含 8 个磁盘的 RAID-Z2 vdev 类似于 RAID-60 阵列。RAID-Z 组的存储容量约为最小磁盘大小乘以非奇偶校验磁盘数量。<br><br>**备用 (Spare)**——ZFS 提供一种特殊的伪 vdev 类型，用于跟踪可用的热备盘。当活动设备故障时，热备盘会自动替换故障设备；待使用 `zpool replace` 将故障设备永久替换后，热备盘自动释放并恢复为可用状态。<br><br>**日志 (Log)**——ZFS 日志设备（即 ZFS 意图日志 ZIL）将意图日志从常规池设备转移到专用存储设备（通常为 SSD）。专用日志设备可提升数据库等高同步写入负载的性能。日志设备可镜像，但不支持 RAID-Z；使用多个日志设备时写入将负载均衡。<br><br>**缓存 (Cache)**——向池中添加缓存 vdev 会将缓存存储加入 L2ARC。缓存设备不可镜像。由于缓存设备仅存储现有数据的副本，不存在数据丢失风险。<br><br>**分布式 RAID-Z (dRAID)**——dRAID 是 RAID-Z 的变体，提供集成的分布式热备盘，支持更快的顺序重建（sequential resilver）。dRAID 使用固定条带宽度，将数据、奇偶校验和备用空间均匀分布到所有设备上。支持 draid1（单奇偶校验）、draid2（双奇偶校验）和 draid3（三重奇偶校验）。dRAID 的 I/O 性能与 RAID-Z 类似，但顺序重建速度显著更快。<br><br>**特殊分配类 (Special)**——特殊 vdev 专用于存储内部元数据（如文件系统元数据、去重表、间接块），也可按数据集粒度接受小文件块。通常使用高性能 SSD 以加速元数据密集型操作。若特殊 vdev 写满，后续分配将回退至普通 vdev。<br><br>**去重分配类 (Dedup)**——专用于存储去重表（DDT）的独立 vdev。其冗余级别应与其他普通 vdev 匹配。<br><br>**警告：** 强烈不建议将整个磁盘用作启动池的一部分，这可能导致池无法启动。同理，不应将整个磁盘作为镜像或 RAID-Z vdev 的成员，因为系统在启动时无法可靠确定未分区磁盘的大小，无处放置引导代码。 |
| 事务组（TXG） | 事务组（Transaction Groups）是 ZFS 将数据块变更批量写入池的机制，也是 ZFS 确保一致性的原子单位。每个事务组被分配一个唯一的 64 位连续标识符。系统最多可同时存在三个活动事务组，分别处于以下状态：<br><br>**开放 (Open)**——新事务组在开放状态下创建并接受新写入。一旦达到大小限制或 `vfs.zfs.txg.timeout` 超时，事务组将进入下一状态。系统中始终有一个事务组处于开放状态。<br><br>**静默 (Quiescing)**——短暂的过渡状态，允许所有挂起操作完成，同时不阻塞新开放事务组的创建。待该事务组内所有事务完成后进入最终状态。<br><br>**同步 (Syncing)**——将事务组中的所有数据写入稳定存储。该过程会连带修改元数据、空间映射等，ZFS 也会将这些一并写入。同步过程包含多个阶段：首先写入所有已变更的数据块，随后写入元数据（可能需要多个阶段完成，因为为数据块分配空间会生成新元数据）。同步状态也是 *synctask*（如创建或销毁快照和数据集等管理操作）完成的地方，它们最终完成 uberblock 的更新。同步完成后，处于静默状态的事务组进入同步状态。所有管理功能（如快照写入）均作为事务组的一部分执行。ZFS 会将创建的 synctask 添加到开放事务组，并尽可能快速地将该组推进到同步状态，以减少管理命令的延迟。 |
| 自适应替换缓存（ARC） | ZFS 采用自适应替换缓存（ARC）替代传统的最近最少使用（LRU）缓存。LRU 缓存是一个按最近使用时间排序的简单列表，新项目加入列表头部，缓存满时从尾部驱逐项目以腾出空间。ARC 由四个列表组成：最常使用（MRU）和最频繁使用（MFU）对象，以及各自对应的"幽灵列表"。幽灵列表跟踪已被驱逐的对象，防止其重新加入缓存，从而提高缓存命中率。使用 MRU 和 MFU 的另一个优势在于：扫描整个文件系统时，LRU 缓存中的所有数据都将被驱逐以容纳新访问的内容；而 ZFS 通过 MFU 跟踪最频繁使用的对象，使最常访问的缓存块得以保留。 |
| L2ARC | L2ARC 是 ZFS 缓存系统的第二级。主 ARC 存储在 RAM 中。由于 RAM 容量通常有限，ZFS 还可使用缓存 vdev 扩展缓存。SSD 因速度更快、延迟更低而常被用作缓存设备。L2ARC 完全可选，但部署后可提升从 SSD 读取缓存文件的速度，避免从普通磁盘读取。L2ARC 还可加速去重：当去重表（DDT）超出 RAM 容量但能容纳于 L2ARC 时，其读取速度远快于从磁盘读取。ZFS 对写入缓存设备的数据速率施加限制，以防止额外写入过早损耗 SSD。在缓存满（首个块被驱逐以腾出空间）之前，L2ARC 写入速率限制为写入限制与加速限制之和；之后则仅限于写入限制。`vfs.zfs.l2arc_write_max` 控制每秒写入缓存的字节数，`vfs.zfs.l2arc_write_boost` 在"加速预热"阶段提高此限制。 |
| ZIL | ZIL 使用比主存储池更快的存储设备（如 SSD）来加速同步事务。当应用程序请求同步写入（保证数据写入磁盘而非仅缓存）时，数据先写入更快的 ZIL 存储，随后再刷新到常规磁盘，从而大幅降低延迟并提升性能。数据库等同步工作负载能显著受益于 ZIL，而常规异步写入（如文件复制）完全不使用 ZIL。 |
| 写时复制 | 与传统文件系统不同，ZFS 将新数据写入不同的块，而非原地覆盖旧数据。写入完成后，元数据更新以指向新位置。当发生短写（如系统崩溃或写入过程中断电）时，文件的原始完整内容仍然可用，ZFS 会丢弃不完整的写入。这也意味着 ZFS 在意外关机后无需执行 fsck(8)。 |
| 数据集 | 数据集是 ZFS 文件系统、卷、快照或克隆的通用术语。每个数据集拥有唯一的名称，格式为 `poolname/path@snapshot`。池的根目录本身也是一个数据集。子数据集采用类似目录的层次化命名，例如 `mypool/home` 是 `mypool` 的子数据集并继承其属性，可进一步创建 `mypool/home/user` 作为孙数据集，该孙数据集继承父数据集和祖父数据集的属性。子数据集上设置的属性可覆盖继承的默认值。数据集及其子数据集的管理可通过委派进行。 |
| 文件系统 | ZFS 数据集通常用作文件系统。与大多数其他文件系统一样，ZFS 文件系统挂载在系统目录结构中的某个位置，并包含自己的文件和目录，这些文件和目录具有权限、标志以及其他元数据。 |
| 卷 | ZFS 还可以创建卷，这些卷表现为磁盘设备。卷具有与数据集相似的许多特性，包括写时复制、快照、克隆和校验和。卷对于在 ZFS 上运行其他文件系统格式非常有用，例如 UFS 虚拟化或导出 iSCSI 扩展。 |
| 快照 | ZFS 的写时复制（COW）设计支持近乎瞬时地创建一致性快照，快照可使用任意名称命名。对数据集或其父数据集递归快照（包括所有子数据集）后，新数据写入新块，旧块不会立即回收。快照保存文件系统的原始版本，实时文件系统则包含快照之后的所有变更，二者不额外占用空间。写入实时文件系统的新数据使用新块存储。随着旧块在实时文件系统中不再使用而仅存在于快照中，快照体积会逐渐增长。以只读方式挂载快照可恢复文件的历史版本；还可对实时文件系统执行回滚，将其恢复到特定快照，撤销该快照之后的所有变更。池中每个块都有一个引用计数器，跟踪哪些快照、克隆、数据集或卷引用了该块。删除文件和快照时引用计数递减，计数归零后空间被回收。可将快照标记为保留，尝试销毁该快照时将返回 `EBUSY` 错误，使用释放命令移除保留后即可删除。快照、克隆和回滚可在卷上操作，但无法独立挂载。 |
| 克隆 | 快照可以创建克隆。克隆是快照的可写版本，允许文件系统作为新数据集分叉。与快照一样，克隆初始不消耗新空间。写入克隆的新数据使用新块，克隆体积随之增长。当克隆中的块被覆盖时，原块的引用计数递减。无法删除克隆所依赖的快照——快照是父级，克隆是子级。克隆可被提升，反转此依赖关系：使克隆成为父级，原父级变为子级。此操作不消耗新空间，但由于父子空间占用关系反转，可能影响现有配额和保留。 |
| 校验和 | <p>每个块都带有校验和，所用算法为数据集属性（参见 `zfs set`）。每次读取时校验和会被透明验证，使 ZFS 得以检测静默损坏。若数据与预期校验和不符，ZFS 将尝试从可用冗余（如镜像或 RAID-Z）中恢复。`scrub` 可触发全量校验和验证。支持的校验和算法：</p><ul><li><code>fletcher2</code></li><li><code>fletcher4</code>（当前默认）</li><li><code>sha256</code></li><li><code>sha512</code>（SHA-512/256，64 位硬件上比 SHA-256 快约 50%）</li><li><code>skein</code>（SHA-3 候选算法，64 位硬件上比 SHA-256 快约 80%）</li><li><code>edonr</code>（高性能 SHA-3 候选算法，比 SHA-256 快约 350%）</li><li><code>blake3</code>（高性能安全哈希，针对现代 CPU 优化）</li></ul><p><code>fletcher</code> 类算法速度更快但不提供密码学安全性；<code>sha256</code> 及以上为强加密哈希，碰撞概率更低。<code>skein</code> 和 <code>edonr</code> 采用带盐校验和（salted checksum），以池内存储的 256 位随机密钥预置种子，可防止去重系统中的哈希碰撞攻击。禁用校验和是可能的，但极不推荐。</p> |
| 压缩 | 每个数据集均有压缩属性，默认为关闭。启用压缩算法后，所有写入数据将被压缩。除节省空间外，由于读写块数减少，吞吐量通常也会提升。<br><br>**LZ4**——ZFS 池版本 5000（功能标志）引入，是目前推荐的压缩算法。LZ4 处理可压缩数据比 LZJB 快约 50%，处理不可压缩数据快三倍以上，解压速度也比 LZJB 快约 80%。在现代 CPU 上，LZ4 单核压缩速度通常超过 500 MB/s，解压速度超过 1.5 GB/s。<br><br>**LZJB**——默认压缩算法，由 ZFS 创始人之一 Jeff Bonwick 设计。LZJB 压缩效果良好且 CPU 开销低于 GZIP。未来默认算法将切换为 LZ4。<br><br>**GZIP**——流行压缩算法，主要优势在于可配置压缩级别。设置 `compress` 属性时，管理员可从 `gzip1`（最低）到 `gzip9`（最高）之间选择，以在 CPU 时间与磁盘空间之间取得平衡。<br><br>**ZLE**——零长度编码，仅压缩连续零块，适用于包含大量零块的数据集。 |
| 复制 | `copies` 属性设置为大于 1 的值时，ZFS 将在文件系统或卷中为每个块维护多份副本。为重要数据集设置此属性可提供额外冗余，以便从校验和不匹配的块中恢复。在无冗余的池中，副本功能是唯一的冗余形式。它可恢复单个坏扇区或其他小范围故障，但不保护池免受整盘丢失的影响。 |
| 去重 | 校验和机制使写入时能够检测重复块。通过去重，已存在块的引用计数递增，从而节省存储空间。ZFS 在内存中维护一个去重表（DDT）以检测重复块，表内包含唯一校验和列表、块位置及引用计数。写入新数据时，ZFS 计算校验和并与列表比对，匹配时复用现有块。SHA256 校验和配合去重提供安全的加密哈希。`dedup` 设为 `on` 时，校验和匹配即视为数据相同；设为 `verify` 时，ZFS 将逐字节比对确保一致，发现差异则记录哈希冲突并分别存储。DDT 须存储每个唯一块的哈希，内存消耗巨大，经验值为每去重 1 TB 数据约需 5-6 GB 内存。若内存不足以容纳完整 DDT，每次写入前须从磁盘读取 DDT，性能将严重下降。去重可利用 L2ARC 存储 DDT，作为内存与磁盘之间的折中方案。建议优先考虑压缩，通常能以相近的空间节省效果避免额外的内存开销。 |
| Scrub | 与 fsck(8) 这类一致性检查不同，ZFS 使用 `scrub`。`scrub` 读取池中所有数据块，将其校验和与元数据中的已知良好校验和进行比对验证。定期检查所有存储数据可确保在需要前恢复损坏的块。`scrub` 在非正常关机后并非必需，但建议至少每三个月执行一次。ZFS 在日常使用中即验证每个块的校验和，但 `scrub` 确保连极少使用的块也能检查潜在损坏，在归档存储场景下进一步提升了数据安全性。可通过调整 `vfs.zfs.scrub_delay` 的相对优先级，防止 `scrub` 影响池中其他工作负载的性能。 |
| 数据集配额 | ZFS 提供快速准确的数据集、用户和组空间核算，以及配额和空间预留功能，使管理员能精细控制空间分配并为关键文件系统保留空间。ZFS 支持多种配额类型：数据集配额、引用配额（refquota）、用户配额和组配额。配额限制数据集及其后代的总大小，包括数据集的快照、子数据集及其快照。<br><br>**注意：** 卷不支持配额，因其 `volsize` 属性已作为隐式配额。 |
| 参考配额 | 引用配额通过强制硬限制来限制数据集可以使用的空间量。这个硬限制只包括数据集本身引用的空间，不包括由后代（如文件系统或快照）使用的空间。 |
| 用户配额 | 用户配额用于限制指定用户使用的空间量。 |
| 组配额 | 组配额限制指定组可以使用的空间量。 |
| 数据集保留 | `reservation` 属性可为特定数据集及其后代保证一定量的存储空间。例如在 `storage/home/bob` 上设置 10 GB 保留，可防止其他数据集耗尽空闲空间，确保该数据集始终有至少 10 GB 可用。与 `refreservation` 不同，快照和后代所占空间不计入保留。对 `storage/home/bob` 创建快照时，除 `refreservation` 占用的空间外，必须有足够的空闲磁盘空间才能成功。主数据集的后代不占用 `refreservation` 空间。<br><br>任何形式的保留在以下场景中均非常有用：规划与测试新系统的磁盘空间分配方案，或确保文件系统有足够空间用于审计日志、系统恢复过程及文件。 |
| 参考预留 | `refreservation` 属性可为特定数据集保留一定空间，但不包括其后代数据集。例如在 `storage/home/bob` 上设置 10 GB 保留后，即使其他数据集尝试占用空闲空间，仍会为该数据集保留至少 10 GB。与常规 `reservation` 不同，快照和后代数据集所占空间不计入该保留。若对 `storage/home/bob` 创建快照，除 `refreservation` 占用的空间外，必须有足够磁盘空间才能成功完成。主数据集的后代不占用 `refreservation` 空间。 |
| 重新同步 | 在更换故障磁盘时，ZFS 必须将丢失的数据填充到新磁盘中。*重新同步* 是使用分布在剩余磁盘上的奇偶校验信息来计算并将丢失的数据写入新磁盘的过程。 |
| 在线 | 处于 `Online` 状态的池或 vdev 其成员设备已连接且完全正常运行。处于 `Online` 状态的单个设备也在正常工作。 |
| 离线 | 管理员可将单个设备置于 `Offline` 状态，前提是存在足够的冗余，以免池或 vdev 进入 `Faulted` 状态。管理员可能选择将磁盘设置为离线，以便为更换磁盘做准备，或为了更容易识别它。 |
| 降级 | 处于 `Degraded` 状态的池或 vdev 有一个或多个磁盘丢失或故障。该池仍然可用，但如果其他设备发生故障，池可能变得无法恢复。重新连接丢失的设备或更换故障磁盘后，池将恢复到 `Online` 状态，前提是重新连接或新设备完成了重新同步过程。 |
| 故障 | 处于 `Faulted` 状态的池或 vdev 不再可操作，无法访问数据。当丢失或故障的设备数量超过 vdev 中冗余级别时，池或 vdev 进入 `Faulted` 状态。如果重新连接丢失的设备，池将恢复到 `Online` 状态。如果冗余不足以弥补故障磁盘的数量，则会丢失池中的数据，需要从备份恢复。 |

## ZFS 发展历程：从 Solaris 到 OpenZFS

ZFS 最早由 Sun 公司开发，旨在取代 Solaris（早期曾用名 SunOS）上的 UFS 文件系统。SunOS 和 BSD Unix 的关键开发者之一是 Bill Joy，他同时也是 Sun 的创始人之一。SunOS 早期基于 BSD Unix 开发，随后转向 SVR4（Unix System V Release 4，即与 AT&T 合作开发）。

ZFS 源代码于 2005 年 10 月 31 日集成到 Solaris 开发主干（revision 789），随后于 2005 年 11 月 16 日作为 OpenSolaris build 27 以 CDDL（Common Development and Distribution License，通用开发及发行许可）开源发布。

ZFS 于 2007 年导入 FreeBSD 源代码树，在 FreeBSD 7.0-RELEASE（2008 年 2 月，pool v6）中以实验状态发布；在 FreeBSD 8.0-RELEASE（2009 年 11 月，pool v13）中宣布为生产就绪状态。

2009 年 4 月 Oracle 宣布收购 Sun（2010 年 1 月收购完成）之后，Solaris 项目（易名为 Oracle Solaris）及 ZFS（易名为 Oracle Solaris ZFS）进入闭源开发模式，OpenSolaris 社区管理委员会于 2010 年 8 月自行解散（revision 13149，在解散时 ZFS pool 为 [v28](https://github.com/freebsd/freebsd-src/commit/572e285762521df27fe5b026f409ba1a21abb7ac)）。OpenSolaris 的主要社区开发力量迁移到了新分支 [illumos 项目](https://github.com/illumos/illumos-gate)。从此以后（v28），Oracle Solaris ZFS 与社区版本开始分道扬镳。

目前 illumos 采用类似 Linux 内核的开发模式，衍生出 OpenIndiana、OmniOS 等十余款发行版。但其年平均代码提交量约 150 次，开发活跃度已显著降低。

2011 年 2 月，FreeBSD 采用了 ZFS pool v15，这是 2009 年 10 月随 Solaris 10 update 8（Solaris 10 10/09）分发的版本。

2011 年 11 月，Oracle Solaris 11 发布，ZFS pool 升级至 v31。

2012 年 1 月 12 日，FreeBSD 9.0-RELEASE 支持了 ZFS pool v28。参见：Finally... Import the latest open-source ZFS version - (SPA) 28[EB/OL]. [2026-03-26]. <https://github.com/freebsd/freebsd-src/commit/10b9d77bf1ccf2f3affafa6261692cb92cf7e992>。

在 OpenSolaris 关停 3 年后（2013 年），OpenZFS 项目正式成立，统一了 ZFS 的开源开发（此前 ZFS on Linux 原生内核模块项目已于 2010 年启动，而基于 FUSE 的 ZFS-FUSE 项目则始于 2008 年）。由于 Oracle Solaris ZFS 的闭源开发，OpenZFS 很难再兼容 Oracle Solaris ZFS。

“时来天地皆同力，运去英雄不自由。”（[唐] 罗隐《筹笔驿》）OpenZFS 新功能的主要开发商 Delphix 公司（Delphix 于 2024 年 3 月被 Perforce Software 收购）将其设备的操作系统从 illumos 迁移到了 Linux，基本上放弃了对前者的投入。其理由是几乎所有云平台厂商和虚拟机平台仅支持 Linux，因此 illumos 几乎再难得到支持。甚至 Oracle Solaris 本身也进入了维护模式（版本 11.4 的生命周期可延续至 2037 年）。Oracle ZFS 迁移到了企业级存储解决方案 [Oracle 存储](https://www.oracle.com/cn/storage/#zfs-storage-appliance)。

illumos 版本的 ZFS（其主要开发仍由 OpenZFS 推动）得到的功能更新日趋减少，FreeBSD 对该版本 ZFS 的维护难度也不断上升，当 ZFS 出现新功能时，通常要先等待其合并到 illumos，再回溯到 FreeBSD 中。但 illumos 的开发已基本停滞。2018 年 8 月，FreeBSD 项目开始研究如何将 FreeBSD ZFS 由 illumos 迁移到直接上游 OpenZFS。

OpenZFS 于 2020 年 8 月合入 FreeBSD-CURRENT，随 FreeBSD 13.0-RELEASE（2021 年 4 月）正式发布，“ZFS 的实现目前由 OpenZFS 提供。[9e5787d2284e](https://cgit.freebsd.org/src/commit/?id=9e5787d2284e)（由 iXsystems 赞助）”取代了 OpenSolaris/illumos 版本的 ZFS。这一迁移使 FreeBSD 与主流 ZFS 开源生态重新接轨。

目前 OpenZFS 代码提交量的首位成员来自美国劳伦斯利弗莫尔国家实验室（LLNL，Lawrence Livermore National Laboratory），OpenZFS 的开发由多家组织共同推动，主要贡献者包括 LLNL、Klara Systems、iXsystems、Delphix 等。LLNL 的核心职责是确保美国国家核威慑的安全、可靠和有效。

Sun 原意是太阳，太阳虽有西落，但同时也在地球的另一侧东升。这一隐喻恰当地概括了 ZFS 从 Sun 生态向更广泛的开源生态迁移的历史进程。

### 参考文献

- FreeBSD Foundation. The Future of ZFS in FreeBSD[EB/OL]. [2026-04-02]. <https://staging.freebsdfoundation.org/wp-content/uploads/2015/12/2011-FOSDEM-ZFS-in-Open-Source-Operating-Systems.pdf>. Oracle 闭源后的 FreeBSD 项目报告，记录关键时间节点与开发人员。
- FreeBSD Project. Comprehensive changes for vendored openzfs[EB/OL]. (2020-07-29)[2026-04-02]. <https://reviews.freebsd.org/D25872>. 切换至 OpenZFS 的代码审查过程文档。
- FreeBSD Project. 9e5787d2284e[EB/OL]. [2026-04-02]. <https://github.com/freebsd/freebsd-src/commit/9e5787d2284e187abb5b654d924394a65772e004>. GitHub 上的迁移提交记录。
- OpenZFS Project. History[EB/OL]. [2026-04-02]. <https://openzfs.org/wiki/History>. OpenZFS 项目官方历史记录。
- OpenZFS Project. Add support for FreeBSD[EB/OL]. [2026-04-02]. <https://github.com/openzfs/zfs/pull/8987>. 向 OpenZFS 提交的 FreeBSD 支持 PR。
- Dimitropoulos S. Debugging ZFS: From Illumos to Linux[EB/OL]. [2026-04-02]. <https://www.youtube.com/watch?v=uDDJnzSb-2w>. Delphix 迁移使 ZFS 开发集中于 Linux 平台。
- 红帽. 红帽与实验室携手打造全球性能最强的超级计算机[EB/OL]. [2026-04-02]. <https://www.redhat.com/zh-cn/success-stories/LLNL>. LLNL 与红帽合作及大规模使用 Linux 的介绍。
- Oracle. Oracle and Sun System Software and Operating Systems Oracle Lifetime Support Policy[EB/OL]. [2026-04-02]. <https://www.oracle.com/us/assets/lifetime-support-hardware-301321.pdf>. Oracle 产品支持周期文档，第 41 页为 Solaris。
- OpenZFS Project. Announcement[EB/OL]. (2015-04-15)[2026-04-16]. <https://www.openzfs.org/wiki/Announcement>. 记载 OpenZFS 项目于 2013 年 9 月 17 日正式成立：“Today we announce OpenZFS: the truly open source successor to the ZFS project.”
- Burt J. Oracle Completes Sun Acquisition[EB/OL]. (2010-01-27)[2026-04-16]. <https://www.eweek.com/storage/oracle-completes-sun-acquisition/>. 记载 Oracle 于 2010 年 1 月 27 日完成对 Sun 的收购。
- NERA Economic Consulting. US DOJ and DG Comp Clear Oracle's Acquisition of Sun Microsystems[EB/OL]. [2026-04-16]. <https://www.nera.com/experience/2010/us-doj-and-dg-comp-clear-oracles-acquis.html>. 记载“On 20 April 2009, Oracle and Sun announced that Oracle would acquire Sun”及“On 27 January 2010, Oracle completed its acquisition of Sun”。
- Perforce Software. Perforce Software Completes Acquisition of Delphix[EB/OL]. (2024-03-25)[2026-04-17]. <https://www.perforce.com/press-releases/perforce-completes-delphix-acquisition>. 记载 Perforce 于 2024 年 3 月 25 日完成对 Delphix 的收购。
- Jude A. The History and Future of OpenZFS[EB/OL]. (2020-03)[2026-04-17]. <http://www.allanjude.com/bsd/asiabsdcon2020_history_and_future_of_zfs.pdf>. AsiABSDCon 2020 演示文稿，明确区分 ZFS-FUSE（2008 年基于 FUSE 的用户态实现，由 LLNL 启动）与 ZFS on Linux 原生内核模块项目（2010 年由 LLNL 启动）。LLNL, Lawrence Livermore National Laboratory, 劳伦斯利弗莫尔国家实验室。

## 许可证兼容性分析

从知识产权与开源许可的角度分析，ZFS 未能直接纳入 Linux 内核树的核心原因在于许可证兼容性问题。Linux 内核采用 GPLv2（GNU General Public License version 2）许可，这是一种强 copyleft 许可证，要求衍生作品也必须以相同许可发布；而 ZFS 采用 CDDL（Common Development and Distribution License）许可，同样包含 copyleft 条款，但传染范围仅限于 CDDL 许可的代码文件。两者在 copyleft 传染范围与权利义务要求上存在实质性冲突，导致无法通过双许可证方式解决兼容性问题，因此 ZFS 未被接受进入 Linux 主内核树。

> **思考题**
>
> 阅读 GPLv2 和 CDDL 许可证的原文或译文。
>
> 1. 解释为什么二者存在冲突？
> 2. 如果仅从许可来看，自由软件基金会称任何树外模块都是不合规的 ~~当然最后要看法院的意见~~，Ubuntu ZFS 模块即是一例。那么，这是否能反证整个 Linux 内核都是以 GPLv2 授权的？

## 技术潜能与现实困境

ZFS 的性能优势与高级特性通常需要针对性的参数调优才能充分发挥，调优策略具有高度环境依赖性，需结合具体存储硬件、工作负载特征与使用场景进行个性化配置，主要调优方向包括 ARC 缓存大小、记录大小、压缩算法选择等。ZFS 不属于典型的开箱即用型文件系统。

### 文档生态现状分析

目前可用的 ZFS 文档包括：

- [Oracle Solaris 管理：ZFS 文件系统](https://docs.oracle.com/cd/E26926_01/html/E25826/index.html)：该文档撰写于 OpenZFS 项目启动之前，不包含 OpenZFS 近十五年来的开发进展。
- *FreeBSD Mastery: ZFS* 与 *FreeBSD Mastery: Advanced ZFS*
- 《FreeBSD 操作系统设计与实现（第二版）》：包含 ZFS 原理性描述

OpenZFS 项目的官方文档可作为参考来源。

> **技巧**
>
> ZFS 有多种实现，其功能差异对比表参见：Feature Flags[EB/OL]. [2026-03-26]. <https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Feature%20Flags.html>。

## 附录：ZFS 与传统文件系统挂载方式的差异

ZFS 并不使用 **/etc/fstab** 管理文件系统挂载，而是通过 `zfs mount` 命令和 ZFS 数据集的 `mountpoint` 属性进行管理。但 EFI 系统分区和 swap 分区仍然需要使用 **/etc/fstab**。

## 课后习题

1. 查找 OpenZFS 2.4.0 的源代码仓库，编译并在 FreeBSD 14.3 中安装，对比原生 ZFS 在编译时间和内存占用上的差异。
2. 选取 ZFS 从 illumos 迁移到 OpenZFS 的关键提交 9e5787d2284e，重构其最小兼容层。
3. 修改当前系统的 ZFS 功能集配置，禁用 3 个你认为不必要的特性，验证系统启动与运行状态。
4. 为 ZFS 添加国际化支持。
