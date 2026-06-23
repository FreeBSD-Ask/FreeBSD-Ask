# 4.1 安装前的准备工作

部署 FreeBSD 系统之前，需完成硬件兼容性评估、安装介质准备与制作等前期工作。

## 硬件兼容性

以下列出 amd64 架构的最低硬件配置与硬件兼容性查询方法。

### 最低硬件需求

amd64（又称 x86-64）是 64 位 x86 架构的扩展，广泛应用于现代个人计算机与服务器。15.0-RELEASE 版本在虚拟机环境中测得的最低硬件需求如下：

| 类别 | 场景/模式 | 最低需求 |
| ---- | --------- | -------- |
| 硬盘 | 仅安装基本系统 | 约 550 MB |
| 硬盘 | 安装 KDE 桌面环境（通过 pkg 安装后） | 约 15 GB |
| 内存 | UEFI 模式 | 256 MB |
| 内存 | BIOS 模式 | 96 MB |
| 内存 | ZFS 文件系统（最低） | 2 GB |

然而，以上为启动安装程序的理论最小值；为了保证基本的系统可用性，实际内存容量应不小于 256 MB。

如果要使用 ZFS 作为文件系统，OpenZFS 项目官方建议设备至少应搭载 2 GB 内存（推荐 8 GB 以上以获得最佳性能），内存低于此值时，可能需要对 ZFS 参数手动调优。

### 实测硬件兼容性

下表列出了部分硬件的实测支持情况：

| 硬件类别 | 系列 | 实测型号 | 备注 |
| -------- | ---- | -------- | ---- |
| CPU | Intel Alder Lake（含混合架构与纯 E-core 架构） | i7-1260P、N100 | 可正常启动运行，但调度机制尚不完善，睿频功能受限。i7-1260P 为混合架构（P-core + E-core），N100 为纯 E-core 架构（4 颗 Gracemont 核心） |
| NVMe 固态硬盘 | M.2 接口 | 英睿达 P310、Intel 600P、梵想 S530Q、S500Pro、S542PRO | 正常工作 |
| 无线网卡 | Intel AX 系列 | AX200 | Wi-Fi 5 速率与 Windows 11 IoT Enterprise 24H2 相当（使用 iperf2 测得） |
| 有线网卡 | Realtek 2.5 G | RTL8125B | 需要额外安装驱动程序，参见本书附录 |
| 有线网卡 | Intel 2.5 G | i226-V | 正常工作 |
| 显卡 | 近十年的 Intel 及 AMD 集成/独立显卡 | 英特尔锐炬® Xe 显卡、英特尔 HD Graphics 4000 | 支持程度与 DRM 驱动程序移植进度相关；drm-kmod 元 Port 会根据系统版本自动选择合适的驱动：在 FreeBSD 14.x 上安装 drm-61-kmod（基于 Linux 6.1），在 FreeBSD 15.0-RELEASE 及更新版本上安装 drm-66-kmod（基于 Linux 6.6），在较新的 FreeBSD 15-STABLE 上安装 drm-612-kmod（基于 Linux 6.12）。用户也可手动安装 drm-latest-kmod（追踪 Linux DRM 最新开发版本，基于 Linux 6.12，适用于较新的 FreeBSD 15 及 FreeBSD 16）。 |
| NVIDIA 显卡 | 近十多年的显卡 | GTX 850M | 受 NVIDIA 官方显卡驱动程序支持 |

> **注意**
>
> FreeBSD 支持安全启动（Secure Boot），但需要用户手动配置密钥并签名引导组件，尚未实现开箱即用。在安装 FreeBSD 前，建议关闭安全启动（Secure Boot）。同时，FreeBSD 也不支持 Fake RAID（伪 RAID），需将控制器模式修改为 AHCI。
>
> Fake RAID 是由主板 BIOS/固件提供的软件 RAID 功能，依赖操作系统驱动程序支持，并非真正的硬件 RAID。AHCI（Advanced Host Controller Interface）是 SATA 控制器的标准工作模式，提供原生支持 SATA 设备的高级特性。
>
> 操作方法：进入 BIOS/UEFI 设置界面，找到存储控制器相关选项，将模式从 RAID 改为 AHCI 后保存重启。具体菜单位置因主板型号而异，可参考主板说明书。

#### 参考文献

- FreeBSD Project. drm-kmod: drm driver for FreeBSD[EB/OL]. [2026-06-05]. <https://github.com/freebsd/drm-kmod>. 该仓库提供 FreeBSD 图形驱动程序内核模块更新，追踪 Linux DRM 驱动程序移植进度。
- FreeBSD Project. SecureBoot[EB/OL]. [2026-03-25]. <https://wiki.freebsd.org/SecureBoot>. 该页面提供 FreeBSD 安全启动相关状态信息。

### 特定硬件兼容性查询

除上述实测硬件外，更多硬件的支持情况可参考以下外部资源。

[bsd-hardware.info. Hardware for BSD](https://bsd-hardware.info/?view=search) 该平台提供 BSD 系统硬件兼容性数据库，可用于查询设备支持情况。

![硬件支持查询](../.gitbook/assets/hardware-support-query-1.png)

![硬件支持查询](../.gitbook/assets/hardware-support-query-2.png)

> **注意**
>
> 因为该网站也可能出现错误（例如将 LPDDR5 误识别为 LPDDR4），建议实际测试。

## 下载 FreeBSD 镜像

了解硬件支持情况后，开始下载 FreeBSD 镜像。首先访问 FreeBSD 项目官网：<https://www.freebsd.org/>。

![FreeBSD 项目官网](../.gitbook/assets/freebsd-official-site.png)

点击黄底红字的 `amd64`，页面将跳转至下载页面：

> **技巧**
>
> 随着时间推移，读者下载时可能已无 15.0-RELEASE 版本。此时只需选择列表最顶部的 `FreeBSD-X.Y-RELEASE`（该版本推荐用于生产环境）。其中，`X.Y` 应为比 `15.0` 更大的版本号，如 `15.1`、`16.0` 等。

![FreeBSD 镜像](../.gitbook/assets/freebsd-mirror-list.png)

```sh
File Name                                          File Size      Date
Parent directory/                                  -              -
CHECKSUM.SHA256-FreeBSD-15.0-RELEASE-amd64	1171	2025-Nov-28 09:05
CHECKSUM.SHA512-FreeBSD-15.0-RELEASE-amd64	1811	2025-Nov-28 09:04
FreeBSD-15.0-RELEASE-amd64-bootonly.iso	556255232	2025-Nov-28 05:15
FreeBSD-15.0-RELEASE-amd64-bootonly.iso.xz	121307196	2025-Nov-28 05:15
FreeBSD-15.0-RELEASE-amd64-disc1.iso	1359900672	2025-Nov-28 05:18
FreeBSD-15.0-RELEASE-amd64-disc1.iso.xz	905854552	2025-Nov-28 05:18
FreeBSD-15.0-RELEASE-amd64-dvd1.iso	4405243904	2025-Nov-28 06:23
FreeBSD-15.0-RELEASE-amd64-dvd1.iso.xz	3532521960	2025-Nov-28 06:23
FreeBSD-15.0-RELEASE-amd64-memstick.img	1560400384	2025-Nov-28 05:20
FreeBSD-15.0-RELEASE-amd64-memstick.img.xz	905654292	2025-Nov-28 05:20
FreeBSD-15.0-RELEASE-amd64-mini-memstick.img	689295872	2025-Nov-28 05:17
FreeBSD-15.0-RELEASE-amd64-mini-memstick.img.xz	119782720	2025-Nov-28 05:17
```

上述列表中：第一行分别为文件名、文件大小、文件构建日期（非发行日期），第二行为返回上一级目录。

| 首列 | 说明 |
| ---- | ---- |
| CHECKSUM.SHA256-FreeBSD-15.0-RELEASE-amd64 | 本页所有镜像的 SHA-256 校验和 |
| CHECKSUM.SHA512-FreeBSD-15.0-RELEASE-amd64 | 本页所有镜像的 SHA-512 校验和 |
| FreeBSD-15.0-RELEASE-amd64-bootonly.iso | 网络安装镜像，安装时需要联网 |
| FreeBSD-15.0-RELEASE-amd64-bootonly.iso.xz | 压缩的网络安装镜像，安装时需要联网 |
| FreeBSD-15.0-RELEASE-amd64-disc1.iso | 标准安装镜像 |
| FreeBSD-15.0-RELEASE-amd64-disc1.iso.xz | 压缩的标准安装镜像 |
| FreeBSD-15.0-RELEASE-amd64-dvd1.iso | DVD 镜像，相比标准安装镜像包含了更多软件包（pkg） |
| FreeBSD-15.0-RELEASE-amd64-dvd1.iso.xz | 压缩的 DVD 镜像，相比标准安装镜像包含了更多软件包（pkg） |
| FreeBSD-15.0-RELEASE-amd64-memstick.img | U 盘用的镜像（可以使用 Rufus 制作 U 盘启动盘） |
| FreeBSD-15.0-RELEASE-amd64-memstick.img.xz | 压缩的 U 盘用的镜像（无需解压缩，可以使用 Rufus 制作 U 盘启动盘） |
| FreeBSD-15.0-RELEASE-amd64-mini-memstick.img | U 盘用的网络安装镜像，安装时需要联网 |
| FreeBSD-15.0-RELEASE-amd64-mini-memstick.img.xz | 压缩的 U 盘用的网络安装镜像，安装时需要联网 |

- **.xz** 是一种高压缩比的文件压缩格式，常用于缩小软件发行包的体积。
- **SHA-256** 和 **SHA-512** 是密码哈希函数，用于生成文件的唯一指纹，校验和（Checksum）则是通过这些函数计算出的固定长度字符串，用于验证文件完整性。

> **技巧**
>
> 网络传输可能产生错误，导致下载的文件与原始镜像不一致。因此，需要使用 **校验和** 来验证所获取的文件与官方发布的镜像完全一致。Windows 10 和 11 系统自带命令行工具 CertUtil，可用于计算校验和，无需安装额外软件。

需要说明的是，DVD 镜像仅包含部分离线软件包，而非全部，具体清单可参见源代码文件 **release/scripts/pkg-stage.sh** 该脚本定义 DVD 镜像包含的预安装软件包清单。

FreeBSD 的所有安装介质默认不提供图形界面，需在系统安装后另行安装和配置。DVD 镜像虽包含更多软件包，但由于图形界面依赖关系复杂，且 DVD 上的软件包版本可能较旧，在安装图形界面时仍可能遇到依赖冲突或版本不匹配问题，因此不建议使用 DVD 镜像。

安装镜像按用途与介质分类如下：

```text
FreeBSD 安装镜像分类

                    ┌── 安装镜像 ──┐
                    │              │
               ┌────┴────┐    ┌────┴────┐
               │  ISO 镜像│    │  IMG 镜像│
               └────┬────┘    └────┬────┘
                    │              │
          ┌─────────┼─────────┐    │
          │         │         │    │
          ▼         ▼         ▼    ▼
     bootonly   disc1     dvd1   memstick
     .iso       .iso      .iso   .img
     (网络安装) (标准)    (含包)  (U盘)
          │         │         │    │
          ▼         ▼         ▼    ▼
      .iso.xz   .iso.xz   .iso.xz .img.xz
     (压缩版)  (压缩版)  (压缩版) (压缩版)

```

## 开发版本及非 amd64 架构

STABLE 和 CURRENT 均为开发分支，不适用于生产环境，生产环境应选用 RELEASE。

要使用开发分支，或者为非 amd64 架构下载镜像，在主页选择“other”即可。

![下载 FreeBSD](../.gitbook/assets/download-freebsd.png)

> **警告**
>
> 使用开发版本的用户应有时间和意愿关注开发动态，浏览邮件列表与问题追踪系统。同时要求用户具备一定的探索和实践能力。否则，建议使用 RELEASE 版本。

| Installer | VM | SD Card | Documentation |
| --------- | -- | ------- | ------------- |
| 安装镜像 | 虚拟机预安装镜像 | 存储卡镜像 | 文档 |
| 适用于常规安装 | 适用于云平台和虚拟机 | 适用于单板机/嵌入式设备 | 发行说明等文档 |

> **技巧**
>
> 如果不确定选择哪种镜像，请选择 `Installer`（标准个人计算机，Apple 除外）。

> **技巧**
>
> 如果不明确 `amd64`、`aarch64`、`riscv64` 等架构的区别，请选择 `amd64`（适用于大多数标准个人计算机，Apple 电脑除外）。

选定安装镜像的主要类型后，将显示具体的下载列表。

| 版本类型 | 部署环境 | 下载地址 |
| -------- | -------- | -------- |
| RELEASE 正式版 | 虚拟机 | <https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/15.0/FreeBSD-15.0-RELEASE-amd64-disc1.iso> |
| RELEASE 正式版 | 物理机 | <https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/15.0/FreeBSD-15.0-RELEASE-amd64-memstick.img> |
| CURRENT 开发版（仅限专业用户） | 虚拟机 | <https://download.freebsd.org/snapshots/amd64/amd64/ISO-IMAGES/16.0/> |
| CURRENT 开发版（仅限专业用户） | 物理机 | 文件名以 `-amd64-memstick.img` 或 `-amd64-memstick.img.xz` 结尾 |

由于版本迭代，实际情况可能已发生变化，请自行查阅，选择合适的 RELEASE 版本用于生产环境。

### 参考文献

- FreeBSD Project. freebsd-src/UPDATING[EB/OL]. [2026-03-25]. <https://github.com/freebsd/freebsd-src/blob/main/UPDATING>. 该文件记录着系统更新重大变更。
- FreeBSD Project. freebsd-src/RELNOTES[EB/OL]. [2026-03-25]. <https://github.com/freebsd/freebsd-src/blob/main/RELNOTES>. 该文件提供发行版发布说明与新特性等文档。
- Dell Technologies. 如何确定用于安全应用程序的文件 SHA-256 哈希[EB/OL]. [2026-03-25]. <https://www.dell.com/support/kbdoc/zh-cn/000130826/%E5%A6%82%E4%BD%95%E7%A1%AE%E5%AE%9A%E7%94%A8%E4%BA%8E%E5%AE%89%E5%85%A8%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E7%9A%84%E6%96%87%E4%BB%B6-sha-256-%E5%93%88%E5%B8%8C>. 该文档介绍 Windows 系统下文件 SHA-256 哈希值计算方法。读者可参考。

## 刻录 FreeBSD 镜像

下载 FreeBSD 镜像后，需要将其刻录到 U 盘上才能安装。

### 推荐镜像格式

制作 U 盘安装介质时，建议使用 `-img` 或 `-img.xz` 格式的镜像。`.iso` 镜像采用混合启动（Hybrid）模式，该模式同时支持从光驱和 U 盘启动，但可能未完全遵循 UEFI 规范，直接写入 U 盘可能导致启动错误。详见 FreeBSD Project. FreeBSD -.iso files not support written to USB drive[EB/OL]. [2026-03-25]. <https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=236786>. 该 Bug 报告记录了 ISO 镜像直接写入 USB 设备的兼容性问题。建议读者优先在使用光学介质、虚拟机或云平台安装时选用 `iso` 结尾的镜像；物理机 U 盘安装应优先使用 `img` 镜像。

然而，也存在例外情况。部分主机的 UEFI 固件支持从 `.iso` 镜像刻录的 U 盘启动（例如一些老款神舟电脑），但并非所有主机都支持此方式（例如部分小米电脑可能无法引导）。

由于设备类型多样，即使在某台主机上测试通过，FreeBSD 的两个 ISO 镜像仍可能出现兼容性问题。如果遇到引导问题，请首先尝试使用 Rufus 刻录 `img` 镜像。

### Windows 平台下 Rufus 刻录方法

不同操作系统平台有不同镜像刻录工具推荐。

Windows 平台建议优先使用 **Rufus**，Linux/FreeBSD 平台可直接使用 `dd` 命令刻录镜像：`dd if=FreeBSD-*.img of=/dev/daX bs=1M status=progress`（其中 **/dev/daX** 为目标 U 盘设备，请根据实际设备名调整；`status=progress` 显示传输进度）。

Rufus 下载地址为 <https://rufus.ie/zh>，该工具为 Windows 平台开源 USB 启动盘制作工具。

使用 Rufus 刻录镜像，无需解压缩文件，直接选择 `-img.xz` 制作启动盘。

![Rufus](../.gitbook/assets/rufus-tool.png)

尽管镜像文件校验和实际正确，但 win32diskimager 在处理某些镜像格式时存在缺陷，有时会错误地报告校验失败。此外，win32diskimager 自 2017 年 3 月发布 1.0.0 版本后已停止更新超过 9 年，其可执行文件未经代码签名，不支持压缩镜像格式（如 `.img.xz`），在现代 UEFI 环境下的兼容性也不如 Rufus 和 balenaEtcher。Ventoy 的启动加载机制与 FreeBSD 镜像不完全兼容，可能导致启动失败。二者均 **不建议使用**。

**读者应优先使用 Rufus；若 Rufus 不可用，可使用 balenaEtcher 作为替代。** balenaEtcher 是一款跨平台（Windows/macOS/Linux）开源镜像刻录工具，支持直接刻录压缩镜像（如 `.img.xz`，无需解压），写入后自动校验数据完整性，且仍在积极维护中。balenaEtcher 下载地址为 <https://etcher.balena.io/>。

> **思考题**
>
> > 有时候绕远路是必须的，人生是片森林，人们终究会再次迷路，短暂相遇。正所谓“念念不忘，必有回响”。然而，人们清醒地意识到，没有什么“必有回响”，有的只是“没有结局的开始”或者“稍纵即逝的追寻”。没有任何人许诺回响，这只是某种哲学层面的寄托，让人们与这种现实“和解”。
>>
>>“念念不忘，必有回响”的完整说明并非李叔同所述，而是源于当代人的《李叔同〈晚晴集〉人生解读》（王少农. 李叔同《晚晴集》人生解读[M]. 北京：线装书局，2008.）其中上半句“念念不忘”亦非李叔同原作，而是看似引用了南宋王龙舒《龙舒净土文卷第四》“蓋欲念念不忘也。如此久久念心成熟。”其中在清俞行敏重辑《净土全书》一书的“净土起信”中同样有类似描述“净土指归云：欲了生死，修行净业，当发十种信心，念念不忘，决生净土。”，再次索引到《净土指归集》，实际上是绕回了《佛说四谛经》，载“亦观持宿命，亦从得道行，念世间行不可悔，摄、止、度世、无为、寂然、止见、一德、无所著、如解脱意观念想念，从念念、念不忘、少言、念不离，是名为直正念，是名为道德谛。”
>>
>>由于这是汉传佛教，在历史上被记载为安世高的翻译贡献，需考察其原始面貌。查《佛说四谛经》，实际对应于中阿含经《分别圣谛经》，即对应《巴利三藏》的《中部》的《一四一分别谛经》（段晴，范晶晶，等，译. 汉译巴利三藏·经藏·中部[M]. 上海：中西书局，2022：963-965.）。是这样写的：“众仁友，何为正念？此谓比丘于身循观身，精勤，正知，具念，于世间戒除贪与忧；于诸受（……）于心（……）于诸法循观法，精勤，正知，具念，于世间断除贪与忧。这被称为正念。”可以清晰地看出，“念念不忘”实际上对应的是“具念”（巴利语 sati），在文献中往往又被翻译为“念”“正念”。
>>
>>实际上，在任何早期人类宗教活动中，传递的思想都是当时最合适不过的道德思想和伦理行为，也是最质朴，最清楚明白的，任何过于复杂的理论绝不可能流传数千年。因此，有必要怀疑这种“念念不忘”说法的合理性。在不同的学术观点中对此看法存在较大差异，但是无可辩驳的是，在佛教最早期的发展中，不可能有任何超越当时信众知识结构、道德伦理、认知能力的理论被普遍认可。因此，无需考察任何文本，越是从经验出发的理解，却往往是最接近合理性的存在。念念不忘实质上接近这种说法：“厨师一定要会做饭、水一定往低处流”，即，xx 就是 xx。可以看到，“念念不忘”与当代欧陆哲学产生了深切共鸣，不是让事情回到本身，而是认识到，有些时候，事情就是本身。“大音希声”。“一切真历史都是当代史”（Croce B. 历史学的理论和历史[M]. 田时纲，译. 北京：中国社会科学出版社，2018），但无论是玄奘短命的“法相唯识宗”，还是“念念不忘”的本义，都启示着一个深邃的事实，“一切真历史都是古代史”。“谁试图诠释历史，谁就在篡改历史。讨论真假无非是在争夺自己的话语权。”历史学是一种解释学。佛经和道教经文的文言文呈现方式仍是绝对主流，且无定本；而与此同时，基督教两会甚至出版了官方的《拼音版圣经》。但在过去，甚至如今的天主教，保守也是常态。形式上的精致化、现代化与内在的理论嬗变的平衡是大多数理论发展的痛点。后人对前人的经典论述究竟是形成了一层又一层的遮蔽，还是使其精致化顺应时代发展？今人所看到的，持有的意见，究竟有几分是最初作者的面貌？后人往往通过注解经典来阐发自己的观点，甚至托名作书。
>>
>>念念不忘，恰好指出了一个道理，“没有回响才是常态”，这不是固执的坚持和重复，而是理解到一个无数人提及的话语，人本就一无所有，唯一重要的事情只有生或死。念念不忘，不是执着于铭记，而是发现，感知到什么，那就是什么。与其说人一生都在选择，不如说人一生都在等待，等待回响。
>
>
> 如何理解“念念不忘”与“必有回响”的关系？
>
> 如果一切都是临时的，短暂的。那么，会不会有一天，有那么一刻，恰巧宇宙本身也不存在了？

## 附录：FreeBSD 兼容的以太网卡

FreeBSD 对多种以太网卡支持良好。

### Realtek（螃蟹卡）

Realtek RTL8125 是一款常见的 2.5 G 以太网卡。在消费级市场中，常见的 2.5 G 网卡多采用该型号芯片。在安装 FreeBSD 前，可在 Windows 设备管理器中查看硬件标识，确认网卡型号是否为 RTL8125。

![Realtek RTL8125 2.5 G](../.gitbook/assets/realtek-rtl8125.png)

> **技巧**
>
> RTL8125 在 FreeBSD 下默认没有驱动，需手动安装。最简单的方法是通过手机 USB 共享网络临时上网，具体方法见本书其他部分。安装网卡驱动后需重启系统。

#### Realtek 以太网卡驱动安装方法

确认网卡型号在支持列表中后，按照以下步骤安装驱动。

- 使用 pkg 安装：

```sh
# pkg install realtek-re-kmod
```

- 使用 Ports 安装：

```sh
# cd /usr/ports/net/realtek-re-kmod/
# make install clean
```

在编译安装时，需确保 **/usr/src** 目录下有源代码。

```sh
/usr/
├── ports/
│   └── net/
│       └── realtek-re-kmod/  # Realtek 网卡驱动 Ports 目录
└── src/                      # 系统源代码目录（编译驱动时需要）
```

> **技巧**
>
> 如果 Realtek 网卡仍存在断流、时断时续等情况，可尝试使用 Port **net/realtek-re-kmod198** 替代 **realtek-re-kmod**。

相关文件结构：

```sh
/boot/
├── loader.conf        # 系统启动加载器配置文件
└── modules/
    └── if_re.ko       # re 网卡驱动内核模块
```

编辑 **/boot/loader.conf** 文件，写入以下两行：

```ini
if_re_load="YES"                        # 设置开机自动加载 re 网卡驱动模块
if_re_name="/boot/modules/if_re.ko"     # 指定 re 网卡驱动模块的完整路径，以覆盖内核内置的 re(4) 驱动
```

默认分配了足够接收巨型帧的缓冲区。巨型帧是指大于标准以太网帧（1500 字节）的帧，通常为 9000 字节。巨型帧可减少网络开销、提升传输效率，但在某些网络环境下可能导致兼容性问题。re 网卡相关配置参数如下：

| 参数 | 建议值 | 作用 |
| ---- | ------ | ---- |
| `hw.re.max_rx_mbuf_sz` | `2048` | 缩小接收缓冲区，降低内存需求，避免内存碎片导致的驱动程序挂起 |
| `hw.re.s5wol` | `1` | 启用 S5 休眠唤醒 |
| `hw.re.s0_magic_packet` | `1` | 启用魔术包唤醒（Wake-on-LAN） |

配置方法为使用 `sysrc` 将参数写入 **/boot/loader.conf**，例如：

```sh
# sysrc -f /boot/loader.conf hw.re.max_rx_mbuf_sz="2048"
# sysrc -f /boot/loader.conf hw.re.s5wol="1"
# sysrc -f /boot/loader.conf hw.re.s0_magic_packet="1"
```

完成以上设置后，需重启系统使其生效。

参考文献：

- FreshPorts. realtek-re-kmod: Kernel driver for Realtek PCIe Ethernet Controllers[EB/OL]. [2026-03-25]. <https://www.freshports.org/net/realtek-re-kmod>. FreshPorts 上的 Realtek 网卡驱动页面，提供安装信息与版本更新。
- Bug 275882 - **net/realtek-re-kmod**: Problem with checksum offload since +199.00[EB/OL]. [2026-03-26]. <https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=275882>.

### Intel 网卡

Intel 网卡也是常见的网络适配器类型，FreeBSD 对其支持良好。

#### 2.5 G

英特尔 i225-V 和 i226-V 2.5 G 网卡默认便可驱动，无需额外配置。已在 I226-V rev04 型号上测试通过，使用 `igc` 驱动，网卡显示为 `igc0` 样式。

参考文献：

- FreeBSD Project. igc: Intel Ethernet Controller I225 driver[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?query=igc&sektion=4>. 手册页，详述了 Intel I225/I226 系列网卡驱动的使用方法。

#### 千兆和百兆及其他以太网卡

除了 2.5 G 网卡外，Intel 还有其他多种型号的以太网卡。i210 和 i211 网卡由 igb 驱动，通常无需额外配置便可使用，但未经实际测试。

支持列表及更多参见：

- FreeBSD Project. em, lem, igb: Intel(R) PRO/1000 Gigabit Ethernet adapter driver[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?query=em&sektion=4>. 手册页，含 Intel PRO/1000 系列千兆网卡驱动说明。

## 附录：USB 网卡推荐

USB 网卡便携性强、使用方便，适合临时使用或设备没有内置网卡的情况。以下介绍 USB 网卡的相关推荐。

> **警告**
>
> 千兆和 2.5 G 网卡在 15.0-RELEASE 以前均存在间歇性断连故障。如果有更稳定的推荐，请提交 PR。
>
> 对于 2.5 G USB 网卡，目前可选的型号仅有 RTL8156 和 RTL8156B。

| 类型 | 品牌/型号 | 芯片组/参数 | 备注 |
| ---- | --------- | ----------- | ---- |
| USB 以太网卡 | 绿联 USB 百兆网卡 CR110 | AX88772A 100M | / |
| USB 以太网卡 | 绿联 USB 千兆网卡 CM209 | AX88179A 1000M | 在 15.0-RELEASE 以前断流 |
| Type-C 以太网卡 | 绿联 Type-C 转百兆网卡 30287 | AX88772A 100M | / |
| Type-C 以太网卡 | 绿联 Type-C 转千兆网卡 CM199 | AX88179A 1000M | 在 15.0-RELEASE 以前断流。在树莓派 5 上的测试表明，目前 15.0-RELEASE 下的 AX88179A 和 RTL8156B 网卡均可持续稳定运行，不会断流，最长连续运行时间超过 72 小时 |
| USB 无线网卡 | COMFAST CF-WU810N（已停产） | RTL8188EUS 2.4 G 150 M | 由 rtwn 驱动 |
| USB 无线网卡 | COMFAST CF-912AC | RTL8812AU 2.4 G & 5 G 1200 M | 由 rtwn 驱动 |
| USB 无线网卡 | COMFAST CF-915AC | RTL8811AU 2.4 G & 5 G 600 M | 由 rtwn 驱动，理论上支持，未经实际测试，无论是否支持，都请提交 issue |
| USB 无线网卡 | 绿联 N300 M | RTL8192EU 2.4 G 300 M | 由 rtwn 驱动，理论上支持，未经实际测试，无论是否支持，都请提交 issue |
| USB 无线网卡 | 绿联 AC 1300 M-双频 | RTL8812AU 2.4 G & 5 G 1300 M | 由 rtwn 驱动，理论上支持，未经实际测试，无论是否支持，都请提交 issue |
| USB 以太网卡 | 绿联 USB 2.5 G 网卡 CM275 | RTL8156 2.5 G | 在 15.0-RELEASE 以前断流 |
| Type-C 以太网卡 | 绿联 Type-C 转 2.5 G 网卡 | RTL8156 2.5 G | 在 15.0-RELEASE 以前断流 |

VendorID（厂商标识）和 ProductID（产品标识）是 USB/PCI 设备的两个标准标识符，驱动程序通过这两个 ID 来识别和匹配硬件。

相同芯片组的硬件可能由不同厂商生产，使用不同的 VendorID/ProductID。

如果仅凭芯片组信息购买网卡，FreeBSD 可能不支持其 `VendorID` 和 `ProductID`，例如 DOREWIN 达而稳。

在这种情况下，需联系驱动开发者将硬件信息加入驱动，并重新编译内核才能使用。

相关 Bug 反馈：

- FreeBSD Bugzilla. Bug 166724 - if_re(4): watchdog timeout[EB/OL]. [2026-03-25]. <https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=166724>. 记载了 Realtek 网卡驱动看门狗超时问题的历史 Bug 报告。
- FreeBSD Bugzilla. Bug 267514 - AXGE(4) ASIX AX88179A ue0: link state changed to DOWN[EB/OL]. [2026-03-25]. <https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=267514>. 记载了 ASIX USB 千兆网卡连接不稳定问题的 Bug 报告。
- FreeBSD Project. if_re(4) -- Realtek PCI Ethernet driver[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=if_re&sektion=4>. Realtek PCI 以太网卡驱动手册页。
- FreeBSD Project. axge(4) -- ASIX USB Gigabit Ethernet driver[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=axge&sektion=4>. ASIX USB 千兆网卡驱动手册页。
- FreeBSD Project. rtwn(4) -- Realtek USB IEEE 802.11 wireless network driver[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=rtwn&sektion=4>. Realtek USB 无线网卡驱动手册页。
- FreeBSD Project. igb(4) -- Intel PRO/1000 Gigabit Ethernet adapter driver[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=igb&sektion=4>. Intel PRO/1000 千兆网卡驱动手册页。
- FreeBSD Project. pciconf(8) -- PCI configuration utility[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=pciconf&sektion=8>. PCI 设备配置工具手册页。
- FreeBSD Project. usbconfig(8) -- USB configuration utility[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=usbconfig&sektion=8>. USB 设备配置工具手册页。

## 附录：共享硬件数据到数据库

如果读者希望上传自己的数据到 <https://bsd-hardware.info>，与社区共享，可参照本节操作。

### 安装 hw-probe

- 使用 pkg 安装 hw-probe：

```sh
# pkg install hw-probe
```

- 或者使用 Ports 安装 hw-probe：

```sh
# cd /usr/ports/sysutils/hw-probe/
# make install clean
```

### 上传硬件数据

执行以下命令可采集硬件信息并上传到 hw-probe 数据库：

```sh
# hw-probe -all -upload
Probe for hardware ... Ok
Reading logs ... Ok
Uploaded to DB, Thank you!

Probe URL: https://bsd-hardware.info/?probe=f64606c4b1
```

访问上述链接可查看设备信息。此处上传的是 Radxa x4 的配置信息。

其他操作系统可参见 linuxhw. hw-probe/INSTALL.BSD.md[EB/OL]. [2026-03-25]. <https://github.com/linuxhw/hw-probe/blob/master/INSTALL.BSD.md>，该文档提供 BSD 系统上 hw-probe 工具的安装说明。

## 附录：镜像资源

FreeBSD `-RELEASE` 历史版本下载地址：

| 版本范围 | 下载地址 |
| -------- | -------- |
| 5.1-RELEASE 至 9.2-RELEASE | <http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/old-releases/amd64/ISO-IMAGES> |
| 9.3-RELEASE 至最新的 `-RELEASE` 版本 | <http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/old-releases/amd64/amd64/ISO-IMAGES/> |

FreeBSD 镜像 BT 种子下载地址（非官方，建议检查文件校验和后使用）：<https://fosstorrents.com/distributions/freebsd/>
