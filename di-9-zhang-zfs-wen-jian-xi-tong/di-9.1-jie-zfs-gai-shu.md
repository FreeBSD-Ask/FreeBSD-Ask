# 9.1 ZFS 历史与现实

ZFS 源于 Sun Solaris，2005 年以 CDDL 许可证开源，2007 年导入 FreeBSD。Oracle 收购 Sun 后 ZFS 转为闭源开发，开源社区于 2013 年发起 OpenZFS 项目延续其发展。2020 年 OpenZFS 2.0 统一了 FreeBSD 与 Linux 的 ZFS 代码库，提供写时复制、快照、端到端校验与自愈等存储特性。

## ZFS 特性和术语

ZFS 文件系统与其他文件系统有本质区别。

ZFS 将文件系统和卷管理器的角色合而为一：可向在线系统添加新的存储设备，新增的存储空间立即可供池中现有文件系统使用。

通过合并传统上分离的角色，ZFS 从根本上改变了存储扩展的方式：管理员无需调整现有 RAID 组，只需向池中添加新 vdev，新增容量即可由池中所有文件系统共享。**vdev**（虚拟设备）是构成池的基本单元，可以是单块磁盘（叶子 vdev），也可以是镜像或 RAID-Z 等冗余设备组。所有的 ZFS 文件系统（称为 **数据集**）都可以访问整个池中合并的空闲空间。池中已使用的块会减少每个文件系统可用的空间。这种方法避免了传统卷管理中空闲空间在各分区中碎片化且难以在线调整的常见陷阱。

```sh
                         ZFS 文件系统层次 (ZFS File System Hierarchy)
                         根：存储池 (Pool / zpool)
────────────────────────────────────────────

pool
├─ root                        (mountpoint=/)
│  ├─ var                      (继承 mountpoint)
│  └─ usr                      (继承 mountpoint)
│
├─ home                        (mountpoint=/home)
│  ├─ user1                    (继承 → /home/user1)
│  └─ user2                    (继承 → /home/user2)
│
├─ data                        (mountpoint=none)
│  └─ archive                  (不可自动挂载)
│
└─ legacyfs                    (mountpoint=legacy)
   (由 /etc/fstab 管理挂载)

说明：
- mountpoint=路径：自动挂载
- mountpoint=none：不挂载
- mountpoint=legacy：交由传统系统管理


                              数据集层 (Dataset Layer)
─────────────────────────────────────────
类型：filesystem | volume | snapshot | bookmark | clone

文件系统 (filesystem)            卷 (volume / zvol)
──────────────────────
* POSIX 目录树                   * 原始块设备
* 空间动态分配                   * 固定大小 (refreservation)
* 属性可继承                     * 可构建 UFS / ext4 / NTFS

                ───────────────┬───────────────
                      ─────────▼────────
               ───────▼───────    ───────▼───────      克隆 (Clone)
               快照 Snapshot      书签 Bookmark
               ─────────────                           从快照派生可写数据集
               @snap (只读)       #bkmk (元数据) ◄──── 共享数据块 (COW)
               回滚 / 克隆源      Send 增量参照

核心特性：COW / Checksum / Compression / Encryption

                              存储池层 (Pool / zpool)
───────────────────────────────────────
池状态：ONLINE / DEGRADED / FAULTED / SUSPENDED
操作：Scrub / Resilver / Trim

顶级 VDEV × N
数据在顶级 VDEV 间条带化，冗余在 VDEV 内实现

                              虚拟设备层 (VDEV Layer)
───────────────────────────────────────

[数据 VDEV]                     [分配类设备]

Mirror        RAID-Z           Special        Log
n-way         z1/z2/z3         元数据池       SLOG

   │              │               │            └─► 同步写日志 (ZIL)
   │              │               └────────────► 元数据 / 小块

dRAID         Spare            Cache          Dedup
分布式        热备盘           L2ARC          DDT

                                   │            └─► 去重表
                                   └────────────► 读缓存


                              物理层 (Physical)
────────────────────────────────────────

物理磁盘                磁盘分区                文件 VDEV
/dev/ada0              /dev/ada0p3            /tmp/vdev
推荐整盘                一般不推荐              测试用途
                        GEOM 保证一致性        无掉电保护


注：
- Pool 是整个 ZFS 层次结构的根
- 属性 (compression / quota / mountpoint 等) 可自上而下继承
- Snapshot / Bookmark 不占用挂载点
```

- **vdev 类型**：

  - **磁盘 (Disk)**：最基本的 vdev 类型，可以是整块磁盘（如 **/dev/ada0**、**/dev/da0**）或单个分区（如 **/dev/ada0p3**）。在 FreeBSD 中，分区与整盘相比通常不会有显著性能损失，但 OpenZFS 官方仍推荐优先使用整盘。

  - **文件 (File)**：常规文件也可构成 ZFS 池，但强烈建议不要用于生产环境，仅适用于测试和实验场景。文件的容错能力取决于其所在文件系统。创建池时，必须使用文件的完整路径作为设备路径。

  - **镜像 (Mirror)**：创建镜像时指定关键字 `mirror`，后跟镜像成员设备列表。镜像由两个及以上设备组成，所有数据写入全部成员设备。镜像 vdev 的可用容量等于最小成员的容量。除一个成员外，其余全部成员发生故障时数据仍不丢失。

  - **RAID-Z**：ZFS 使用 RAID-Z，即标准 RAID-5/6 的变体。RAID-Z 的奇偶校验分布更均匀，消除了意外重启后数据与奇偶校验不一致的“RAID-5 写入漏洞”。ZFS 支持三种 RAID-Z 级别（raidz/raidz1、raidz2、raidz3），raidz 是 raidz1 的别名，三种级别相应提供不同程度的冗余。RAID-Z 组最少需要 `奇偶校验数 + 1` 块磁盘，建议每 vdev 使用 3 至 9 块磁盘以获得较好性能。

    以四块 1 TB 磁盘组成的 RAID-Z1 为例，实际可用存储约 3 TB，一块磁盘故障时池可降级运行；若更换和重建之前第二块磁盘掉线，所有池数据将丢失。

    以八块 1 TB 磁盘组成的 RAID-Z3 为例，可用空间约 5 TB，最多可承受三块磁盘故障。Sun 最初建议每个 RAID-Z vdev 不超过 9 块磁盘；OpenZFS 此后的实践指导将上限放宽至约 16 块磁盘（机械盘的重建时间过长仍是主要考量）。若配置更多磁盘，建议拆分为多个 vdev 并跨 vdev 条带化数据。两个各含 8 块磁盘的 RAID-Z2 vdev 类似于 RAID-60 阵列。RAID-Z 组的存储容量约为最小磁盘大小乘以非奇偶校验磁盘数量。

  - **备用 (Spare)**：备用盘属于伪 vdev（pseudo-vdev）类型，用于跟踪可用的热备盘。活动设备发生故障时，热备盘自动替换故障设备；待使用 `zpool replace` 将故障设备永久替换后，热备盘自动释放并恢复为可用状态。热备盘可在多个池之间共享，但不能替换日志设备。正在使用的共享热备盘会导致池无法导出，因为其他池也可能使用同一热备盘，从而引发数据损坏。此外，共享热备盘存在额外风险：若各池在不同主机上导入，且同时发生设备故障，两个池可能同时尝试使用同一热备盘，ZFS 可能无法检测到这种情况，从而导致数据损坏。

  - **日志 (Log)**：日志 vdev 是独立的意图日志设备（separate intent log device），将 ZIL（ZFS 意图日志）从常规池设备转移至专用存储设备（通常为 NVRAM 或专用 SSD）。专用日志设备可提升数据库等高同步写入负载的性能。日志设备可镜像，但不支持 RAID-Z；使用多个日志设备时，写入负载会均匀分布。

  - **缓存 (Cache)**：向池中添加缓存 vdev 会将缓存存储加入 L2ARC。缓存设备不可镜像或配置为 RAID-Z 组。由于缓存设备仅存储现有数据的副本，不存在数据丢失风险。缓存设备的内容在重启后持久保存，导入池时异步恢复到 L2ARC 中（持久 L2ARC），可通过设置 `l2arc_rebuild_enabled=0` 禁用。缓存设备小于 1 GiB 时，ZFS 不会写入重建 L2ARC 所需的元数据结构以节省空间，此行为可通过 `l2arc_rebuild_blocks_min_l2size` 调整。

  - **分布式 RAID-Z (dRAID)**：dRAID 由 RAID-Z 思路演进而来，是独立的 vdev 类型，提供集成的分布式热备盘，支持更快的顺序重建（sequential resilver）。dRAID 使用固定条带宽度（必要时以零填充），将所有数据、奇偶校验和备用空间均匀分布于全部设备。支持 draid1（单奇偶校验）、draid2（双奇偶校验）和 draid3（三重奇偶校验），draid 是 draid1 的别名。dRAID 的 I/O 性能与 RAID-Z 类似，但顺序重建速度显著更快。注意固定条带宽度会影响可用容量和 IOPS，并可能降低压缩效率；若池中存放大量小块数据，建议额外添加镜像 special vdev。

  - **特殊分配类 (Special)**：特殊 vdev 专用于存储特定类型的块，默认包括所有元数据、用户数据的间接块、意图日志（无独立日志设备时）及重复数据删除表，也可按数据集粒度接受小文件块或卷块。通常使用高性能 SSD 以加速元数据密集型操作。池中必须始终至少有一个普通（非 dedup/special）vdev 后才能分配特殊类设备。若特殊 vdev 写满，后续分配将回退至普通 vdev。取消设置 `zfs_ddt_data_is_special` 模块参数，即可将重复数据删除表排除在特殊类之外。小文件块或卷块纳入特殊类为可选功能，各数据集将 `special_small_blocks` 属性设为非零值，即可控制允许纳入特殊类的小块大小上限。

  - **重复数据删除分配类 (Dedup)**：专门存储重复数据删除表（DDT）的独立 vdev。其冗余级别应与其他普通 vdev 匹配。若指定多个去重设备，分配将均匀散布到这些设备。

- **设备状态**：

    池中的顶层 vdev 或组件设备可处于以下状态：

  - **ONLINE（在线）**：设备正常运行。
  - **OFFLINE（离线）**：管理员使用 `zpool offline` 命令显式下线设备。
  - **DEGRADED（降级）**：设备出现过多校验和错误、慢 I/O 或 I/O 错误，但因仍有足够冗余，系统继续降级使用该设备；或者 I/O 错误数超过可接受水平但因副本不足而无法标记为故障。
  - **FAULTED（故障）**：设备无法打开，或 I/O 错误数超过阈值；系统已将其标记为故障以防止继续使用。
  - **REMOVED（已移除）**：设备在系统运行期间被物理移除。设备移除检测依赖硬件支持，并非所有平台均可用。
  - **UNAVAIL（不可用）**：设备无法打开。若导入池时某设备不可用，该设备将以唯一标识符（而非路径）显示。

- **池**：存储池是 ZFS 最基本的构建单元。存储池的顶层为 root vdev，root vdev 聚合了一到多个顶级 vdev（top-level vdev），顶级 vdev 是实际承载数据的底层设备或设备组。ZFS 将数据动态条带化到池中所有顶级 vdev。通过池可以创建一个或多个文件系统（数据集）或块设备（卷），这些数据集和卷共享池中剩余的空闲空间。每个池拥有唯一的名称和 GUID，池的特性标志（feature flags）决定了可用的功能。

- **池健康状态**：

    池的整体健康状态分为三种：

  - **ONLINE（在线）**：池中所有设备正常运行。
  - **DEGRADED（降级）**：一个或多个设备故障或离线，但因有冗余配置，数据仍然可用。
  - **FAULTED（故障）**：元数据损坏，或故障设备数量超出冗余上限，池已不可用且数据无法访问。

- **写时复制（COW）**：与传统文件系统不同，ZFS 将新数据写入不同的块，而非原地覆盖旧数据。写入完成后，元数据更新以指向新位置。短写发生时（如系统崩溃或写入过程中断电），文件的原始完整内容仍然可用，ZFS 会丢弃不完整的写入。这也意味着 ZFS 意外关机后无需执行 fsck(8)。

- **事务组（TXG）**：事务组（Transaction Groups）是 ZFS 将数据块变更批量写入池的机制，也是 ZFS 确保一致性的原子单位。每个事务组对应一个唯一的 64 位连续标识符。系统最多可同时存在三个活动事务组，分别处于以下状态：

  - **开放 (Open)**：新事务组以开放状态创建并接受新写入。一旦达到大小限制或 `vfs.zfs.txg.timeout` 超时，事务组将进入下一状态。系统中始终有一个事务组处于开放状态。

  - **静默 (Quiescing)**：短暂的过渡状态，允许所有挂起操作完成，同时不阻塞新开放事务组的创建。待该事务组内所有事务完成后进入同步状态。

  - **同步 (Syncing)**：将事务组中的所有数据写入稳定存储。该过程会连带修改元数据、空间映射等，ZFS 也会将这些一并写入。同步过程包含多个阶段：首先写入所有已变更的数据块，随后写入元数据（可能需要多个阶段，因为为数据块分配空间会生成新元数据）。同步状态也是 *synctask*（如创建或销毁快照和数据集等管理操作）完成的地方，它们最终完成 uberblock 的更新。所有管理功能（如快照写入）均作为事务组的一部分执行。ZFS 会将创建的 synctask 添加到开放事务组，并尽可能快速地将该组推进到同步状态，以减少管理命令的延迟。

- **校验和**：每个数据块均附带校验和，所用算法为数据集属性。读取时校验和自动透明验证，使 ZFS 能够检测静默数据损坏。若数据与预期校验和不匹配，ZFS 会尝试利用可用冗余（如镜像或 RAID-Z）恢复。`scrub` 可触发全量校验和验证。支持的校验和算法包括 `on`（默认，非去重数据集为 `fletcher4`，去重数据集为 `sha256`），可设为 `off` 禁用校验和，但极不推荐。

- **压缩**：每个数据集均有压缩属性。设为 `on`（默认值）时表示使用当前默认压缩算法，该默认值平衡了压缩与解压速度及压缩比，适用于广泛的工作负载。与所有其他压缩设置不同，`on` 不选择固定的压缩类型——随着新压缩算法加入 ZFS 并在池中启用，默认压缩算法可能发生变化。当前默认压缩算法为 `lzjb`，或在启用了 `lz4_compress` 功能标志时为 `lz4`。启用压缩算法后，所有新写入数据都会压缩。除节省空间外，由于读写块数减少，吞吐量通常也会提升。任何非 `off` 的压缩设置均自动检测全零块（NUL 字节）并存储为空洞（hole）。压缩后的数据会按扇区（2^`ashift` 字节）向上取整；若节省空间不足一个扇区，该块将不压缩存储。此外，还有 12.5% 的默认压缩阈值。

- **加密**：ZFS 支持原生数据集级别加密（GUID：`com.datto:encryption`）。启用加密后，ZFS 会加密文件与 ZVOL 数据、文件属性、ACL、权限位、目录列表、FUID 映射及用户/组/项目空间使用数据。加密必须在数据集创建时指定，创建后不可更改。支持的加密套件包括 `aes-256-gcm`（当前默认）。密钥可存储于本地文件、通过 HTTPS/HTTP 远程获取，或通过命令行提示输入。OpenZFS 2.2.8 与 2.3.3 之前的版本，对加密数据集执行 zfs send 的同时创建快照存在数据损坏风险；若使用未修复版本，建议对加密数据集的复制操作始终采用原始发送模式（zfs send -w）。

- **复制**：`copies` 属性设置为大于 1 的值时，ZFS 会为文件系统或卷中每个块维护多份副本（可能存储于不同磁盘）。这些副本是对池级冗余（如镜像或 RAID-Z）的额外补充。为重要数据集设置此属性可提供额外冗余，以便利用校验和不匹配的块恢复数据。无冗余配置的池中，副本功能是唯一的冗余形式。它可恢复单个坏扇区或其他小范围故障，但不保护池免受整盘丢失的影响。

- **去重/重复数据删除**：校验和机制使写入时能够检测重复块。通过重复数据删除，已存在块的引用计数递增，从而节省存储空间。ZFS 将重复数据删除表（DDT）写入磁盘并缓存于 ARC 内存，写入时通过 DDT 检测重复块，表内包含唯一校验和列表、块位置及引用计数。写入新数据时，ZFS 计算校验和并与列表比对，匹配时复用现有块。`sha256` 校验和配合重复数据删除提供安全的加密哈希。`dedup` 设为 `on` 时，校验和匹配即视为数据相同；设为 `verify` 时，ZFS 将逐字节比对确保一致，发现差异则记录哈希冲突并分别存储。DDT 须存储每个唯一块的哈希，内存消耗巨大，官方建议启用重复数据删除时至少每 1 TiB 存储配备 1.25 GiB 内存，实际需求取决于存储的数据类型。若内存不足以容纳完整 DDT，每次写入前须从磁盘读取 DDT，性能将严重下降，甚至可能导致因内存耗尽而无法导入池。重复数据删除可利用 L2ARC 存储 DDT，作为内存与磁盘之间的折中方案。建议优先考虑压缩，通常能以相近的空间节省效果避免额外的内存开销。

- **Scrub（清洗）**：与 fsck(8) 这类一致性检查不同，ZFS 使用 `scrub`。`scrub` 读取池中所有数据块，将其校验和与元数据中已知良好的校验和比对验证。定期检查所有存储数据可确保在需要前恢复损坏的块。`scrub` 非正常关机后并非必需，但建议至少每三个月执行一次。ZFS 日常使用时即验证每个块的校验和，但 `scrub` 确保连极少使用的块也能检查潜在损坏，对归档存储场景进一步提升了数据安全性。

- **重建 (Resilver)**：更换故障磁盘时，ZFS 须将丢失数据填充到新磁盘中。镜像 vdev 重建时，从剩余镜像成员复制数据；RAID-Z vdev 重建时，利用剩余磁盘的奇偶校验信息计算丢失数据并写入新磁盘。

- **自适应替换缓存（ARC）**：ZFS 采用自适应替换缓存（ARC）替代传统的最近最少使用（LRU）缓存。LRU 缓存是一个按最近使用时间排序的简单列表，新项目加入列表头部，缓存满时从尾部驱逐项目以腾出空间。ARC 由四个列表组成：最近最多使用（MRU）和最频繁使用（MFU）对象，以及各自对应的幽灵列表（ghost list）。幽灵列表追踪已驱逐的对象，驱逐后的数据再次被请求时（即幽灵命中），ARC 会据此动态调整 MRU 与 MFU 的缓存空间分配，从而提高命中率。使用 MRU 和 MFU 的另一个优势在于：扫描整个文件系统时，LRU 缓存中的所有数据都会被驱逐以容纳新访问的内容；而 ZFS 通过 MFU 跟踪最频繁使用的对象，使最常访问的缓存块得以保留。

- **L2ARC**：L2ARC 是 ZFS 缓存系统的第二级。主 ARC 存储于 RAM。由于 RAM 容量通常有限，ZFS 还可使用缓存 vdev 扩展缓存。SSD 因速度更快、延迟更低而常用作缓存设备。L2ARC 完全可选，但部署后可提升从 SSD 读取缓存文件的速度，避免从普通磁盘读取。L2ARC 还可加速重复数据删除：重复数据删除表（DDT）超出 RAM 容量但能容纳于 L2ARC 时，其读取速度远快于从磁盘读取。ZFS 对写入缓存设备的数据速率施加限制，以防止额外写入过早损耗 SSD。缓存满（首个块被驱逐以腾出空间）之前，L2ARC 写入速率限制为写入限制与加速限制之和；之后则仅限于写入限制。

- **ZIL**：ZFS 意图日志（ZIL，ZFS Intent Log）负责满足 POSIX 对同步事务的要求（如数据库事务、NFS 操作、fsync(2) 调用）。在默认情况下，意图日志从主池内的块分配。添加独立的日志设备（separate intent log device，如 NVRAM 或专用 SSD）可将意图日志转移到更快的存储，大幅降低同步写入延迟并提升性能。数据库等同步工作负载能显著受益于专用日志设备，而常规异步写入（如文件复制）完全不使用 ZIL。

- **数据集**：数据集是 ZFS 文件系统、卷、快照或书签的通用术语。克隆本质上是文件系统或卷，而非独立的数据集类型。每个数据集拥有唯一的名称，文件系统格式为 `存储池/路径`，快照格式为 `存储池/路径@快照`，书签格式为 `存储池/路径#书签`。池的根目录本身也是一个数据集。子数据集采用类似目录的层次化命名，例如 `mypool/home` 是 `mypool` 的子数据集并继承其属性，可进一步创建 `mypool/home/user` 作为孙数据集，该孙数据集继承父数据集和祖父数据集的属性。为子数据集设置的属性可覆盖继承的默认值。数据集及其子数据集的管理可通过委派完成。

- **文件系统 (filesystem)**：ZFS 数据集中最常用的类型。ZFS 文件系统即是 ZFS 自身的原生文件系统格式——并非 FAT32/NTFS/ext4，也不可在其上再格式化其他文件系统。它挂载在系统目录树中（由 `mountpoint` 属性控制），提供完整的 POSIX 文件接口（open、read、write、mkdir 等）。挂载点可设为具体路径（自动挂载）、`legacy`（通过 `/etc/fstab` 传统挂载）或 `none`（不自动挂载）。文件系统支持层次化命名（如 `pool/home/user`），子数据集默认继承父数据集的属性，也可覆盖为独立值。

- **卷 (volume / ZVOL)**：ZFS 卷是数据集的另一主要类型。卷本身不含文件系统——它是以原始块设备形式暴露的裸设备，位于 `/dev/zvol/pool/path`。正因其为裸块设备，可被格式化为任意文件系统（FAT32、NTFS、UFS、ext4 等），也可直接用作虚拟机磁盘或 iSCSI target 等需要块设备的场景。默认情况下创建卷会建立等量空间预留（`refreservation`）；使用 `-s` 参数可创建稀疏卷而不预留空间。卷同样支持快照、克隆、回滚等 ZFS 特性，但无法像文件系统那样独立挂载，且不支持配额（其 `volsize` 属性本身即作为隐式配额）。

  **ZFS 文件系统可以通过卷在内部承载其他文件系统**

  ```sh
  物理硬盘（disk）
   └── vdev（镜像 / RAIDZ / 条带）
      └── 存储池（zpool）
           └── ZFS 数据集（dataset 抽象层）
                ├── ZFS 文件系统（ZFS filesystem）
                │    ├── 文件 / 目录
                │    ├── 快照（snapshot）
                │    ├── 克隆（clone）
                │    └── 书签（bookmark）
                │
                └── 卷（zvol，块设备）
                     ├── 其他文件系统（UFS / ext4 / FAT32 等）
                     │			└── 文件 / 目录
                     ├── 快照（snapshot）
                     ├── 克隆（clone）
                     └── 书签（bookmark）
   ```

  - **文件系统与卷的比较**：

| 特性 | ZFS 文件系统 (filesystem) | ZFS 卷 (volume / ZVOL) |
| ---- | ------------------------- | ---------------------- |
| 本质 | ZFS 原生文件系统格式 | 原始块设备 |
| 暴露方式 | 挂载为目录树（`mountpoint` 属性） | 设备文件（`/dev/zvol/pool/path`） |
| 自身是否为文件系统 | 是——ZFS 自己即是文件系统 | 否——裸块设备，无自带文件系统 |
| 可否格式化其他 FS | 不可以（它已经是文件系统） | 可以（FAT32、NTFS、UFS、ext4 等） |
| POSIX 文件接口 | 直接提供（open/read/write/mkdir） | 不直接提供（须格式化后挂载） |
| 创建命令 | `zfs create pool/fs` | `zfs create -V size pool/vol` |
| 默认空间行为 | 共享池中空闲空间 | 默认预留等量空间（`-s` 创建稀疏卷） |
| 适用场景 | 通用文件存储，用户与服务数据 | 虚拟机磁盘，iSCSI，需非 ZFS 文件系统 |
| 快照/克隆/书签/回滚 | 支持 | 支持 |
| COW/校验和/压缩/加密 | 支持 | 支持 |
| 层次化命名 | 支持（可嵌套） | 支持（可与文件系统并列） |
| 配额支持 | 支持（`quota`/`refquota`/用户/组/项目） | 不支持（`volsize` 本身即为隐式配额） |
| 独立挂载 | 可以 | 不可以（须格式化后通过对应 FS 挂载） |

- **快照**：ZFS 的写时复制（COW）设计支持近乎瞬时地创建一致性快照，快照可任意命名。对数据集或其父数据集递归快照（包括所有子数据集）后，新数据写入新块，旧块不会立即回收。快照保存文件系统的原始版本，实时文件系统则包含快照之后的所有变更，二者不额外占用空间。写入实时文件系统的新数据使用新块存储。快照体积随旧块从实时文件系统释放而逐步增长。以只读方式挂载快照可恢复文件的历史版本；还可回滚实时文件系统，将其恢复到特定快照，撤销该快照之后的所有变更。池中每个块都有一个引用计数器，跟踪哪些快照、克隆、数据集或卷引用了该块。删除文件和快照时引用计数递减，计数归零后空间即回收。可将快照标记为保留，尝试销毁该快照时返回 `EBUSY` 错误，使用 `zfs release` 命令移除保留后即可删除。卷支持快照、克隆和回滚操作，但无法独立挂载。

- **克隆**：快照可以创建克隆。克隆是快照的可写版本，允许文件系统作为新数据集分叉。与快照一样，克隆初始不消耗新空间。写入克隆的新数据使用新块，克隆体积随之增长。克隆中的块被覆盖时，原块的引用计数递减。无法删除克隆所依赖的快照——快照是父级，克隆是子级。克隆可提升，以反转此依赖关系：使克隆成为父级，原父级变为子级。此操作不消耗新空间，但由于父子空间占用关系反转，可能影响现有配额和保留。

- **块克隆 (Block Cloning)**：块克隆是一种允许克隆文件（或文件的一部分）的机制，即创建浅层副本，其中现有数据块被引用而不复制。后续对数据的修改将触发数据块的写时复制。此功能用于实现“reflinks”或“文件级写时复制”。克隆的块由一种称为块引用表（BRT，Block Reference Table）的特殊磁盘结构跟踪。与重复数据删除不同，该表开销极小，因此可始终启用。与重复数据删除的另一个区别是，克隆须由用户程序主动请求。许多常见的文件复制程序（包括较新版本的 **/bin/cp**）会自动尝试创建克隆。块克隆存在一些限制：只能克隆完整的块；尚未写入磁盘的块、加密块，或源与目标 `recordsize` 属性不同的块无法克隆。

- **书签**：书签类似于快照，但创建速度更快且不占用额外空间。与快照不同，书签无法以任何方式通过文件系统访问。从存储角度看，书签的作用是引用快照创建时的状态，将其作为独立对象。书签最初与快照关联，而非直接与文件系统或卷关联；即使原始快照被销毁，书签仍继续存在。由于书签非常轻量，通常没有销毁的必要。书签格式为 `存储池/路径#书签`。

- **配额**：

    ZFS 提供快速准确的数据集、用户、组及项目空间核算，以及配额和空间预留功能，使管理员能精细控制空间分配并为关键文件系统保留空间。

  - **数据集配额**：限制数据集及其后代的总大小，包括快照和子数据集。卷不支持配额，因其 `volsize` 属性已作为隐式配额。
  - **引用配额 (refquota)**：以硬限制限定数据集可使用的最大空间量。该限制仅包括数据集本身引用的空间，不包括由后代（如文件系统或快照）使用的空间。
  - **用户配额**：限制指定用户使用的空间量。
  - **组配额**：限制指定组可以使用的空间量。
  - **项目配额**：限制指定项目的空间使用量，以项目 ID 标识。与用户和组配额类似，项目配额可对属于同一项目的文件和目录进行空间核算和限制。

- **保留**：

  - **数据集保留 (reservation)**：`reservation` 属性可为特定数据集及其后代保证一定量的存储空间。例如为 `storage/home/bob` 设置 10 GB 保留，可防止其他数据集耗尽空闲空间，确保该数据集始终有至少 10 GB 可用。

  - **引用预留 (refreservation)**：`refreservation` 属性可为特定数据集保留一定空间，但不包括其后代数据集。例如为 `storage/home/bob` 设置 10 GB 保留后，即使其他数据集尝试占用空闲空间，仍会为该数据集保留至少 10 GB。与常规 `reservation` 不同，快照和后代数据集所占空间不计入该保留。若对 `storage/home/bob` 创建快照，除 `refreservation` 占用的空间外，必须有足够磁盘空间才能成功完成。主数据集的后代不占用 `refreservation` 空间。
   任何形式的保留在以下场景中均具有实用价值：规划与测试新系统的磁盘空间分配方案，或确保文件系统有足够空间用于审计日志、系统恢复过程及文件。

- **池检查点（Pool Checkpoint）**：执行包含破坏性操作的关键流程（如 `zfs destroy`）之前，管理员可对池状态建立检查点，并在出错时将整个池回滚到检查点。检查点类似池级快照，包含池的所有状态（属性、vdev 配置等）。存在检查点时，vdev 移除/附加/分离、镜像拆分、更改池 GUID 等操作不可执行。允许添加新 vdev，但回滚后需重新添加。回滚后检查点将永久删除。

> **注意**
>
> 存在检查点时，数据集保留可能无法强制生效，且已释放的检查点数据不会被 scrub 扫描。

## ZFS 发展历程：从 Solaris 到 OpenZFS

ZFS 最早由 Sun 公司开发，旨在取代 Solaris（早期曾用名 SunOS）上的 UFS 文件系统。SunOS 和 BSD Unix 的关键开发者之一是 Bill Joy，他同时也是 Sun 的创始人之一。SunOS 早期基于 BSD Unix 开发，随后转向 SVR4（Unix System V Release 4，即与 AT&T 合作开发）。

ZFS 源代码于 2005 年 10 月 31 日集成到 Solaris 开发主干（revision 789），随后于 2005 年 11 月 16 日作为 OpenSolaris build 27 以 CDDL（Common Development and Distribution License，通用开发及发行许可）开源发布。

ZFS 于 2007 年导入 FreeBSD 源代码树，FreeBSD 7.0-RELEASE（2008 年 2 月，pool v6）以实验状态发布；FreeBSD 8.0-RELEASE（2009 年 11 月，pool v13）宣布为生产就绪状态。

2009 年 4 月 Oracle 宣布收购 Sun（2010 年 1 月收购完成）之后，Solaris 项目（易名为 Oracle Solaris）及 ZFS（易名为 Oracle Solaris ZFS）进入闭源开发模式，OpenSolaris 社区管理委员会于 2010 年 8 月自行解散（revision 13149，解散时 ZFS pool 为 [v28](https://github.com/freebsd/freebsd-src/commit/572e285762521df27fe5b026f409ba1a21abb7ac)）。OpenSolaris 的主要社区开发力量迁移至新分支 [illumos 项目](https://github.com/illumos/illumos-gate)。从此以后（v28），Oracle Solaris ZFS 与社区版本分道扬镳。

目前 illumos 采用类似 Linux 内核的开发模式，衍生出 OpenIndiana、OmniOS 等十余款发行版。但其年平均代码提交量约 150 次，开发活跃度已显著降低。

2011 年 2 月，FreeBSD 采用了 ZFS pool v15，这是 2009 年 10 月随 Solaris 10 update 8（Solaris 10 10/09）分发的版本。

2011 年 11 月，Oracle Solaris 11 发布，ZFS pool 升级至 v31。

2012 年 1 月 12 日，FreeBSD 9.0-RELEASE 支持了 ZFS pool v28。参见：Finally... Import the latest open-source ZFS version - (SPA) 28[EB/OL]. [2026-03-26]. <https://github.com/freebsd/freebsd-src/commit/10b9d77bf1ccf2f3affafa6261692cb92cf7e992>。

OpenSolaris 关停 3 年后（2013 年），OpenZFS 项目正式成立，统一了 ZFS 的开源开发（此前 ZFS on Linux 原生内核模块项目已于 2010 年启动，而基于 FUSE 的 ZFS-FUSE 项目则始于 2008 年）。由于 Oracle Solaris ZFS 的闭源开发，OpenZFS 很难兼容 Oracle Solaris ZFS。

“时来天地皆同力，运去英雄不自由。”（[唐] 罗隐《筹笔驿》）OpenZFS 新功能的主要开发商 Delphix 公司（Delphix 于 2024 年 3 月被 Perforce Software 收购）将设备操作系统从 illumos 迁移至 Linux，基本放弃了对 illumos 的投入。其理由是几乎所有云平台厂商和虚拟机平台仅支持 Linux，因此 illumos 再难获得支持。甚至 Oracle Solaris 本身也进入了维护模式（版本 11.4 的生命周期可延续至 2037 年）。Oracle ZFS 迁移至企业级存储解决方案 [Oracle 存储](https://www.oracle.com/cn/storage/#zfs-storage-appliance)。

illumos 版本的 ZFS（其主要开发仍由 OpenZFS 推动）得到的功能更新日趋减少，FreeBSD 对该版本 ZFS 的维护难度也不断上升，ZFS 出现新功能时，通常要先等待其合并到 illumos，再回溯至 FreeBSD。但 illumos 的开发已基本停滞。2018 年 8 月，FreeBSD 项目开始研究如何将 FreeBSD ZFS 从 illumos 迁移至上流 OpenZFS。

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

从知识产权与开源许可的角度分析，ZFS 未能直接纳入 Linux 内核树，核心原因在于许可证兼容性问题。Linux 内核采用 GPLv2（GNU General Public License version 2）许可，这是一种强 copyleft 许可证，要求衍生作品也必须以相同许可发布；而 ZFS 采用 CDDL（Common Development and Distribution License）许可，同样包含 copyleft 条款，但传染范围仅限于 CDDL 许可的代码文件。两者在 copyleft 传染范围与权利义务要求方面存在实质性冲突，无法通过双许可证方式解决兼容性问题，因此 ZFS 未能进入 Linux 主内核树。

> **思考题**
>
> 阅读 GPLv2 和 CDDL 许可证的原文或译文。
>
> 1. 解释为什么二者存在冲突？
> 2. 如果仅从许可来看，自由软件基金会称任何树外模块都是不合规的 ~~当然最后要看法院的意见~~，Ubuntu ZFS 模块即是一例。那么，这是否能反证整个 Linux 内核都是以 GPLv2 授权的？

## 技术潜能与现实困境

ZFS 的性能优势与高级特性通常需要针对性的参数调优才能充分发挥，调优策略高度依赖具体环境，需结合存储硬件、工作负载特征与使用场景作个性化配置，主要调优方向包括 ARC 缓存大小、记录大小、压缩算法选择等。ZFS 不属于典型的开箱即用型文件系统。

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
