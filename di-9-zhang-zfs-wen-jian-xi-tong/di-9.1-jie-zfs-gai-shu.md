# 9.1 ZFS 概述

ZFS 源于 Sun Solaris，2005 年以 CDDL 许可证开源，2007 年导入 FreeBSD。Oracle 收购 Sun 后 ZFS 转为闭源开发，开源社区于 2013 年发起 OpenZFS 项目延续其发展。2020 年 OpenZFS 2.0 统一了 FreeBSD 与 Linux 的 ZFS 代码库，提供写时复制、快照、端到端校验与自愈等存储特性。

## ZFS 特性和术语

ZFS 不仅仅是一个文件系统，它在本质上是不同的。ZFS 将文件系统和卷管理器的角色结合起来，使得新的存储设备可以添加到一个在线系统中，并且这些新的空间可以立刻在该池中现有的文件系统上使用。通过将传统上分开的角色合并，ZFS 能够克服之前阻止 RAID 组扩展的限制。*vdev* 是池中的顶级设备，可以是简单的磁盘，也可以是 RAID 阵列，例如镜像或 RAID-Z 阵列。ZFS 文件系统（称为 *数据集*）每个都可以访问整个池的合并空闲空间。池中已使用的块会减少每个文件系统可用的空间。这种方法避免了大量分区时常见的陷阱，其中空闲空间在各个分区中变得碎片化。

|ZFS 概念|解释|
|---|---|
| 池 | 存储 *池* 是 ZFS 的最基本构建模块。一个池由一个或多个 vdev 组成，这些 vdev 是存储数据的底层设备。然后，可以使用池来创建一个或多个文件系统（数据集）或块设备（卷）。这些数据集和卷共享池中的剩余空闲空间。每个池都有一个唯一的名称和 GUID。池上的 ZFS 版本号决定了可用的功能。 |
| vdev 类型 | <p>池 (Pool) - 池由一个或多个 vdev 组成，vdev 本身是一个磁盘或多个磁盘组成的 RAID。当使用多个 vdev 时，ZFS 会将数据分布到各个 vdev 上，以提高性能并最大化可用空间。所有 vdev 的大小必须至少为 128 MB。</p><p><strong>磁盘 (Disk)</strong> - 最基本的 vdev 类型是标准块设备。这可以是整个磁盘（如 <code>/dev/ada0</code> 或 <code>/dev/da0</code>）或一个分区（如 <code>/dev/ada0p3</code>）。在 FreeBSD 上，使用分区而不是整个磁盘不会带来性能损失。这与 Solaris 文档中的推荐不同。</p><p><strong>小心：</strong><br>强烈不建议将整个磁盘作为启动池的一部分，因为这可能导致池无法启动。同样，不应将整个磁盘作为镜像或 RAID-Z vdev 的一部分。由于在启动时无法可靠地确定未分区磁盘的大小，因此没有地方可以放置启动代码。</p><p><strong>文件 (File)</strong> - 常规文件也可以构成 ZFS 池，这对于测试和实验非常有用。使用文件的完整路径作为设备路径来创建池（<code>zpool create</code>）。</p><p><strong>镜像 (Mirror)</strong> - 创建镜像时，指定 <code>mirror</code> 关键字，后跟镜像成员设备的列表。镜像由两个或更多设备组成，将所有数据写入所有成员设备。镜像 vdev 将保存与其最小成员相同数量的数据。镜像 vdev 可以承受除一个成员外的所有成员的故障，而不会丢失任何数据。</p><p><strong>注意：</strong><br>要随时将常规单个磁盘 vdev 升级为镜像 vdev，请使用 <code>zpool attach</code>。</p><p><strong>RAID-Z</strong> - ZFS 使用 RAID-Z，它是标准 RAID-5 的一种变体，提供了更好的奇偶校验分布，并消除了 “RAID-5 写入漏洞”，即在意外重启后数据和奇偶校验信息不一致的情况。ZFS 支持三种级别的 RAID-Z，根据阵列中奇偶校验设备的数量和可以故障的磁盘数量，提供不同级别的冗余和可用存储。<br>在 RAID-Z1 配置中，四个磁盘，每个 1 TB，实际可用存储为 3 TB，并且池可以在一个磁盘故障的情况下以降级模式运行。如果在更换和重新校验故障磁盘之前另一个磁盘掉线，则会丢失所有池数据。<br>在 RAID-Z3 配置中，八个 1 TB 的磁盘，卷提供 5 TB 的可用空间，并且在三个磁盘故障的情况下仍能运行。Sun™ 建议每个 vdev 最多不超过九个磁盘。如果配置中包含更多磁盘，建议将它们分成多个 vdev，并跨它们条带化池数据。<br>两个 RAID-Z2 vdev 配置，每个包含 8 个磁盘，类似于 RAID-60 阵列。RAID-Z 组的存储容量大约是最小磁盘大小乘以非奇偶校验磁盘的数量。四个 1 TB 磁盘的 RAID-Z1 配置有效大小约为 3 TB，而八个 1 TB 磁盘的 RAID-Z3 配置提供约 5 TB 的可用空间。</p><p><strong>备用 (Spare)</strong> - ZFS 具有一种特殊的伪 vdev 类型，用于跟踪可用的热备份。请注意，已安装的热备份不会自动部署；需要手动配置它们来替换故障设备，使用 <code>zfs replace</code>。</p><p><strong>日志 (Log)</strong> - ZFS 日志设备，也称为 ZFS 意图日志（ZIL），将意图日志从常规池设备转移到专用设备，通常是 SSD。拥有专用日志设备可以提高高同步写入量应用程序（如数据库）的性能。日志设备可以镜像，但不支持 RAID-Z。如果使用多个日志设备，写入将会负载均衡。</p><p><strong>缓存 (Cache)</strong> - 向池中添加缓存 vdev 将会将缓存的存储添加到 L2ARC。缓存设备不能镜像。由于缓存设备仅存储现有数据的副本，因此不会有数据丢失的风险。</p> |
| 事务组（TXG） | <p>事务组（Transaction Groups）是 ZFS 将块更改组合在一起并写入池的方式。事务组是 ZFS 用于确保一致性的原子单位。ZFS 为每个事务组分配一个唯一的 64 位连续标识符。最多可以有三个活动事务组，分别处于以下三种状态之一：</p><p><strong>开放 (Open)</strong> - 新的事务组在开放状态下开始，并接受新的写入。如果事务组达到限制，它可能会拒绝新的写入。每个时候总会有一个事务组处于开放状态，但如果达到限制，或者达到 vfs.zfs.txg.timeout，事务组会进入下一个状态。</p><p><strong>静默 (Quiescing)</strong> - 一个短暂的状态，允许任何挂起的操作完成，而不阻塞新的开放事务组的创建。待该事务组中的所有事务完成，事务组会进入最终状态。</p><p><strong>同步 (Syncing)</strong> - 将事务组中的所有数据写入稳定存储。这个过程会反过来改变其他数据，如元数据和空间映射，ZFS 也会将它们写入稳定存储。同步过程包含多个阶段。在第一个阶段，所有更改过的数据块会被写入；接下来是元数据，它可能需要多个阶段才能完成。由于为数据块分配空间会生成新的元数据，因此同步状态不能在一个阶段完成，直到没有使用新空间的阶段完成。同步状态还是 <em>synctasks</em> 完成的地方。Synctasks 是管理操作，如创建或销毁快照和数据集，它们完成 uberblock 的更改。待同步状态完成，处于静默状态的事务组会进入同步状态。所有管理功能，如 快照 写入都会作为事务组的一部分。ZFS 会将创建的 synctask 添加到开放事务组，并尽可能快速地将该组推进到同步状态，以减少管理命令的延迟。</p> |
| 自适应替换缓存（ARC） | ZFS 使用自适应替换缓存（ARC），而不是传统的最少最近使用（LRU）缓存。LRU 缓存是一个简单的缓存项目列表，按对象被使用的最近时间排序，将新项目添加到列表头部。当缓存满时，从列表尾部驱逐项目，以为更多活跃对象腾出空间。ARC 由四个列表组成：最常使用（MRU）和最频繁使用（MFU）的对象，以及每个列表的幽灵列表。这些幽灵列表跟踪被驱逐的对象，以防止它们重新加入缓存。这通过避免有偶尔使用历史的对象，增加了缓存命中率。使用 MRU 和 MFU 的另一个优点是，扫描整个文件系统时，MRU 或 LRU 缓存中的所有数据都会被驱逐，以便容纳这些新访问的内容。而在 ZFS 中，还使用了 MFU 来跟踪最常使用的对象，最常访问的块的缓存保持在缓存中。 |
| L2ARC | L2ARC 是 ZFS 缓存系统的第二级。RAM 存储了主要的 ARC。由于可用 RAM 的数量通常有限，ZFS 还可以使用 [缓存 vdevs](https://docs.freebsd.org/en/books/handbook/zfs/#zfs-term-vdev-cache)。固态硬盘（SSDs）常被用作这些缓存设备，因为它们相比传统的旋转磁盘具有更高的速度和更低的延迟。L2ARC 是完全可选的，但如果有一个，它将提高从 SSD 上缓存文件的读取速度，而不必从常规磁盘中读取。L2ARC 还可以加速 [去重](https://docs.freebsd.org/en/books/handbook/zfs/#zfs-term-deduplication)，因为一个适合放入 L2ARC 但不能放入 RAM 的去重表（DDT）将比必须从磁盘读取的 DDT 快得多。对添加到缓存设备的数据速率的限制可以防止通过额外写入过早损坏 SSD。直到缓存满（驱逐第一个块以腾出空间），写入到 L2ARC 的速度限制为写入限制和加速限制的总和，之后将限制为写入限制。成对的 [sysctl(8)](https://man.freebsd.org/cgi/man.cgi?query=sysctl\&sektion=8\&format=html) 值控制这些速率限制。[`vfs.zfs.l2arc_write_max`](https://docs.freebsd.org/en/books/handbook/zfs/#zfs-advanced-tuning-l2arc_write_max) 控制每秒写入到缓存的字节数，而 [`vfs.zfs.l2arc_write_boost`](https://docs.freebsd.org/en/books/handbook/zfs/#zfs-advanced-tuning-l2arc_write_boost) 在“加速预热阶段”（写入加速）期间增加此限制。 |
| ZIL | ZIL 通过使用比主存储池中使用的存储设备更快的存储设备（如 SSD）来加速同步事务。当应用程序请求同步写入时（保证数据被写入磁盘，而不是仅仅被缓存以便后续写入），将数据写入更快的 ZIL 存储，然后稍后再刷新到常规磁盘，极大地减少了延迟并提高了性能。像数据库这样的同步工作负载将从仅使用 ZIL 中受益。常规的异步写入（如复制文件）则完全不会使用 ZIL。 |
| 写时复制 | 与传统文件系统不同，ZFS 写入的是一个不同的块，而不是在原地覆盖旧数据。完成写入时，元数据会更新以指向新位置。当发生短写（如系统崩溃或在写文件过程中断电）时，文件的原始全部内容仍然可用，ZFS 会丢弃不完整的写入。这也意味着 ZFS 在意外关机后不需要执行 [fsck(8)](https://man.freebsd.org/cgi/man.cgi?query=fsck\&sektion=8\&format=html)。 |
| 数据集 | *数据集* 是 ZFS 文件系统、卷、快照或克隆的通用术语。每个数据集都有一个唯一的名称，格式为 *poolname/path\@snapshot*。池的根目录本身也是一个数据集。子数据集具有类似目录的层次结构名称。例如，*mypool/home* 作为 home 数据集，是 *mypool* 的子数据集，并继承其属性。可以通过创建 *mypool/home/user* 来进一步扩展。这个孙子数据集将继承父数据集和祖父数据集的属性。可以在子数据集上设置属性，覆盖从父数据集和祖父数据集继承的默认值。数据集及其子数据集的管理可以通过委派进行。 |
| 文件系统 | ZFS 数据集通常用作文件系统。与大多数其他文件系统一样，ZFS 文件系统挂载在系统目录结构中的某个位置，并包含自己的文件和目录，这些文件和目录具有权限、标志以及其他元数据。 |
| 卷 | ZFS 还可以创建卷，这些卷表现为磁盘设备。卷具有与数据集相似的许多特性，包括写时复制、快照、克隆和校验和。卷对于在 ZFS 上运行其他文件系统格式非常有用，例如 UFS 虚拟化或导出 iSCSI 扩展。 |
| 快照 | ZFS 的写时复制（COW）设计允许几乎瞬时地创建一致的快照，并可以使用任意名称。在对数据集进行快照或对父数据集进行递归快照（包括所有子数据集）后，新数据会写入新块，但不会回收旧块作为空闲空间。快照包含原始文件系统版本，而实时文件系统则包含自快照以来所做的任何更改，且不占用其他空间。写入实时文件系统的新数据会使用新块存储这些数据。快照将随着块在实时文件系统中不再使用，而仅在快照中使用而增长。以只读方式挂载这些快照可以恢复以前的文件版本。可以对实时文件系统执行回滚操作，将其恢复到特定快照，从而撤销自快照以来所做的任何更改。池中的每个块都有一个引用计数器，用于跟踪哪些快照、克隆、数据集或卷使用了该块。当文件和快照被删除时，引用计数减少，当不再引用块时，空闲空间被回收。标记快照为 保留会导致任何尝试销毁该快照的操作返回 `EBUSY` 错误。每个快照可以有一个唯一名称的保留。使用释放命令移除保留，从而可以删除快照。快照、克隆和回滚可以在卷上操作，但无法独立挂载。 |
| 克隆 | 快照的克隆也是可能的。克隆是快照的可写版本，允许文件系统作为新数据集分叉。与快照一样，克隆最初不消耗任何新空间。当新数据写入克隆时，它会使用新块，从而使克隆的大小增长。当克隆的文件系统或卷中的块被覆盖时，之前块的引用计数会减少。删除克隆所基于的快照是不可能的，因为克隆依赖于它。快照是父级，克隆是子级。克隆可以被提升，从而反转这个依赖关系，使克隆成为父级，原父级成为子级。这个操作不需要新的空间。由于父级和子级使用的空间量会反转，它可能会影响现有的配额和保留。 |
| 校验和 | <p>每个块也都有校验和。使用的校验和算法是每个数据集的属性，参见 set。每个块的校验和在读取时会透明地进行验证，这使得 ZFS 可以检测到静默损坏。如果读取的数据与预期的校验和不匹配，ZFS 将尝试从任何可用的冗余（如镜像或 RAID-Z）中恢复数据。可以使用 scrub 来触发所有校验和的验证。校验和算法包括：</p><ul><li>fletcher2</li><li>fletcher4</li><li>sha256</li></ul><p><code>fletcher</code> 算法更快，但 <code>sha256</code> 是一种强加密哈希，具有更低的碰撞概率，但性能稍差。禁用校验和是可能的，但极不推荐。</p> |
| 压缩 | <p>每个数据集都有一个压缩属性，默认值为关闭。将此属性设置为可用的压缩算法，将导致对所有写入数据进行压缩。除了节省空间外，读取和写入吞吐量通常会增加，因为需要读取或写入的块较少。</p><p><strong>LZ4</strong> - 在 ZFS 池版本 5000（功能标志）中添加，LZ4 现在是推荐的压缩算法。LZ4 在处理可压缩数据时比 LZJB 快约 50%，在处理不可压缩数据时快超过三倍。LZ4 的解压缩速度也比 LZJB 快约 80%。在现代 CPU 上，LZ4 通常可以在每个 CPU 核心上以超过 500 MB/s 的速度进行压缩，以超过 1.5 GB/s 的速度进行解压。</p><p><strong>LZJB</strong> - 默认的压缩算法。由 Jeff Bonwick（ZFS 的原始创建者之一）创建。LZJB 提供了较好的压缩效果，同时与 GZIP 相比，CPU 开销较小。在未来，默认压缩算法将更改为 LZ4。</p><p><strong>GZIP</strong> - 在 ZFS 中可用的流行压缩算法。使用 GZIP 的主要优点之一是它可以配置压缩级别。在设置 <code>compress</code> 属性时，管理员可以选择压缩级别，从 <code>gzip1</code>（最低压缩级别）到 <code>gzip9</code>（最高压缩级别）。这使管理员可以控制为节省磁盘空间而交换多少 CPU 时间。</p><p><strong>ZLE</strong> - 零长度编码是一种特殊的压缩算法，仅压缩连续的零块。当数据集包含大量零块时，这种压缩算法非常有用。</p> |
| 复制 | 当设置为大于 1 的值时，`copies` 属性指示 ZFS 在文件系统或 [卷](https://docs.freebsd.org/en/books/handbook/zfs/#zfs-term-volume) 中维护每个块的副本。将此属性设置在重要数据集上可以提供额外的冗余，以便从与校验和不匹配的块中恢复。在没有冗余的池中，副本功能是唯一的冗余形式。副本功能可以从单个坏扇区或其他形式的小故障中恢复，但它不能保护池免受整个磁盘丢失的影响。 |
| 去重 | 校验和使得在写入数据时能够检测到重复的块。通过去重，现有的相同块的引用计数增加，从而节省存储空间。ZFS 在内存中保持一个去重表（DDT）来检测重复的块。该表包含唯一校验和的列表、这些块的位置以及引用计数。在写入新数据时，ZFS 计算校验和并将其与列表进行比较。当找到匹配项时，ZFS 会使用现有的块。使用 SHA256 校验和算法结合去重提供了一个安全的加密哈希。去重是可调的。如果 `dedup` 设置为 `on`，那么匹配的校验和表示数据是相同的。将 `dedup` 设置为 `verify`，ZFS 会对数据进行逐字节检查，确保它们确实是相同的。如果数据不相同，ZFS 会记录哈希冲突并将这两个块分别存储。由于 DDT 必须存储每个唯一块的哈希，它会消耗大量内存。一个大致的经验法则是每去重 1 TB 数据需要 5-6 GB 的内存。在没有足够内存将整个 DDT 保存在内存中的情况下，性能会大幅下降，因为 DDT 必须在写入每个新块之前从磁盘读取。去重可以使用 L2ARC 来存储 DDT，提供系统内存和较慢磁盘之间的折衷。考虑改用压缩，它通常能提供几乎相同的空间节省，而不会增加内存消耗。 |
| Scrub | 与类似 [fsck(8)](https://man.freebsd.org/cgi/man.cgi?query=fsck\&sektion=8\&format=html) 的一致性检查不同，ZFS 使用 `scrub`。`scrub` 会读取池中存储的所有数据块，并将它们的校验和与存储在元数据中的已知良好校验和进行验证。定期检查池中存储的所有数据，确保在需要之前恢复任何损坏的块。`scrub` 在非正常关机后不是必需的，但建议至少每三个月进行一次。ZFS 在正常使用过程中会验证每个块的校验和，但 `scrub` 会确保检查那些即使是很少使用的块是否有潜在的损坏。ZFS 在归档存储情况下提高了数据安全性。通过调整 [`vfs.zfs.scrub_delay`](https://docs.freebsd.org/en/books/handbook/zfs/#zfs-advanced-tuning-scrub_delay) 的相对优先级，防止 `scrub` 降低池中其他工作负载的性能。 |
| 数据集配额 | <p>ZFS 提供了快速准确的数据集、用户和组空间核算，以及配额和空间预留。这使管理员能够精细地控制空间分配，并为关键文件系统保留空间。</p><p>ZFS 支持不同类型的配额：数据集配额、引用配额 (refquota)、用户配额 和 组配额。</p><p>配额限制数据集及其后代的总大小，包括数据集的快照、子数据集及其快照。</p><p><strong>注意：</strong><br>卷不支持配额，因为 <code>volsize</code> 属性作为隐式配额。</p> |
| 参考配额 | 引用配额通过强制硬限制来限制数据集可以使用的空间量。这个硬限制只包括数据集本身引用的空间，不包括由后代（如文件系统或快照）使用的空间。 |
| 用户配额 | 用户配额用于限制指定用户使用的空间量。 |
| 组配额 | 组配额限制指定组可以使用的空间量。 |
| 数据集保留 | <p><strong>reservation</strong> 属性使得为特定数据集及其后代保证一定的空间成为可能。这意味着，在 <strong>storage/home/bob</strong> 上设置 10 GB 的 reservation，可以防止其他数据集占用所有的空闲空间，确保至少有 10 GB 的空间为该数据集保留。与常规的 refreservation 不同，快照和后代所使用的空间不计入 reservation。当对 <strong>storage/home/bob</strong> 进行快照时，除了 <code>refreservation</code> 部分外，必须有足够的磁盘空间才能成功进行此操作。主数据集的后代不计入 <code>refreservation</code> 的空间，因此不会占用已设置的空间。</p><p>任何形式的 reservation 都在以下情况中非常有用，例如在新系统中规划和测试磁盘空间分配的适用性，或确保文件系统上有足够的空间用于音频日志或系统恢复过程和文件。</p> |
| 参考预留 | `refreservation` 属性使得可以为特定数据集保留一定的空间，但**不包括**其后代的数据集。这意味着，在 **storage/home/bob** 上设置 10 GB 的 reservation，另一个数据集尝试使用空闲空间时，仍会为该数据集保留至少 10 GB 的空间。与常规的 [reservation](https://docs.freebsd.org/en/books/handbook/zfs/#zfs-term-reservation) 不同，快照和后代数据集所使用的空间不计入该 reservation。例如，如果对 **storage/home/bob** 进行快照，除了 `refreservation` 部分外，必须有足够的磁盘空间才能成功完成操作。主数据集的后代不计入 `refreservation` 空间，因此不会占用已设置的空间。 |
| 重新同步 | 在更换故障磁盘时，ZFS 必须将丢失的数据填充到新磁盘中。*重新同步* 是使用分布在剩余磁盘上的奇偶校验信息来计算并将丢失的数据写入新磁盘的过程。 |
| 在线 | 处于 `Online` 状态的池或 vdev 其成员设备已连接且完全正常运行。处于 `Online` 状态的单个设备也在正常工作。 |
| 离线 | 管理员将单个设备置于 `Offline` 状态，如果足够的冗余存在以避免将池或 vdev 置于 [Faulted](https://docs.freebsd.org/en/books/handbook/zfs/#zfs-term-faulted) 状态。管理员可能选择将磁盘设置为离线，以便为更换磁盘做准备，或为了更容易识别它。 |
| 降级 | 处于 `Degraded` 状态的池或 vdev 有一个或多个磁盘丢失或故障。该池仍然可用，但如果其他设备发生故障，池可能变得无法恢复。重新连接丢失的设备或更换故障磁盘后，池将恢复到 [Online](https://docs.freebsd.org/en/books/handbook/zfs/#zfs-term-online) 状态，前提是重新连接或新设备完成了 [重新同步](https://docs.freebsd.org/en/books/handbook/zfs/#zfs-term-resilver) 过程。 |
| 故障 | 处于 `Faulted` 状态的池或 vdev 不再可操作，无法访问数据。当丢失或故障的设备数量超过 vdev 中冗余级别时，池或 vdev 进入 `Faulted` 状态。如果重新连接丢失的设备，池将恢复到 [Online](https://docs.freebsd.org/en/books/handbook/zfs/#zfs-term-online) 状态。如果冗余不足以弥补故障磁盘的数量，则会丢失池中的数据，需要从备份恢复。 |

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
