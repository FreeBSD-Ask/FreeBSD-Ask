# 计算机系统结构

## 总线、接口与协议概念辨析

总线、接口与协议是现代计算机系统中实现数据传输的核心要素。三者共同构成计算机硬件之间的通信基础设施。正确理解它们之间的关系，有助于认识计算机的硬件架构和数据传输机制。

M.2 是一种物理接口，其设计理念可视为 Mini PCIe 的后继者。该接口可直接连接物理引脚而无需额外芯片。

根据 M.2 规范，M.2 接口最大支持 3.3 V、3 A（约 10 W）。

---

此外，需要区分三个概念：物理接口、总线协议（或总线通道）以及通道（或协议）。

上述概念可简化为两类。因为通道或协议等同于总线协议（或总线通道）与物理总线（例如 PCIe、RJ45、Type-C 等物理接口、连接器、连接线）之和。通道或协议是一个泛指术语：既可以指二者之和，也可以单独指其中之一。

- 通道 ≈ 协议；
- 物理总线 ≈ 物理接口；
- **物理接口**：指实际的物理连接形式和传输介质，例如 M.2、USB Type-C 接口、SATA 接口、以太网线、USB 数据线等；
- **总线协议（或总线通道）**：指用于数据传输的规则和标准，例如 PCIe 协议、USB 协议、SATA 协议、TCP/IP 协议；
- **总线/通道**：总线/通道 = 物理总线/物理介质 + 总线协议/总线通道。

> **注意**
>
> **总线是指整个数据传输路径，是物理总线（即物理连接和传输介质）和总线协议（即数据传输的规则和标准）的组合。**

> 例如，可以使用以太网线缆传输 HDMI 数字信号。这展示了物理总线的可复用性。
>
> 参考 [绿联（UGREEN）HDMI 延长器 50 米 HDMI 转 RJ45 网传网口转换器单网线网络高清 1080P 视频传输信号放大器一对装 90811](https://item.jd.com/100053619301.html)。它使用以太网线来延长 HDMI 信号，其传输的物理介质是以太网线，接头是 RJ45。
>
> 从设计上讲，以太网线通常使用以太网协议传输数据，物理介质是以太网线，接头是 RJ45。然而，该产品的存在表明，物理总线可以承载不同的信号类型。以太网线作为物理介质，既可以用于传输以太网协议下的 TCP/IP 数据，也可以通过不同的信号编码和转换器传输 HDMI 的数据。
>
> 并且该产品在实际传输 HDMI 数据时，并未使用以太网协议，而是采用 HDMI 协议下的信号编码方式（TMDS）进行传输。
>
> 参考文献：
>
> - [将 HDMI 信号通过单条网线传输的方法](https://patents.google.com/patent/CN101572074A/zh)

物理接口在理论上决定了其承载上限和电气性能。例如可承受的电压、电流和功率、IP 等级，以及尺寸规格（如具体的长宽尺寸）。常见的物理接口包括 M.2、U.2、SATA、USB（包括 Type-C）、HDMI、DP 和 RJ45。

在大多数情况下，讨论的是物理接口。但严格来说，将物理接口与其所承载的协议混为一谈是不准确的。因为在理论上，任何物理接口都可以通过适配器进行相互转换。

例如，USB Type-C 接口可以支持 USB 2.0、USB 3.x、DisplayPort、HDMI、Thunderbolt 和 USB Power Delivery 等多种协议。因此，M.2 接口在理论上既可以连接 NVMe 硬盘，也可以连接 SATA 硬盘，还可以连接显卡、声卡以及主板上的 PCIe 设备，而无需任何驱动，但可能需要额外的 12 V 电源供应。

总线协议（本文将直接连接到 CPU 的通道称为总线，而总线在本质上也是一种通道）。现代 x86 计算机通常仅存在三种总线：**USB**、**SATA**、**PCIe**。

例如，现代消费级英特尔处理器仅直接支持这三种总线。

SATA 协议或 SATA 硬盘性能较低，主要是由协议设计所限制的，与 SATA 这一物理接口本身关系不大。SATA-IO 组织已基本停止对 SATA 协议的性能演进，其倾向于引导用户转向 PCIe 硬盘，或通过桥接方式将 SATA 设备连接到 PCIe 总线上。目前已有通过桥接方式在 PCIe 总线上使用 SATA 设备的实现方案。

由于直接连接到 CPU 的通道被称为总线，因此其他通道通常被称为普通协议或普通通道。对于现代处理器而言，仅 USB、SATA 和 PCIe 这三种总线直接连接到 CPU。而大多数其他设备（如网卡、显卡、声卡和摄像头）通常连接到 PCIe 接口。

尽管这些设备连接到了 PCIe 总线，但并非所有设备都直接连接到 CPU（通常是通过主板上的 DMI 通道转接的）。

下面介绍 2010 年以前大多数 x86 计算机（即第三代酷睿处理器之前）的典型架构：

- CPU→前端总线 FSB→北桥→PCI→南桥→PCI→其他设备。

> 以上 PCI 也可以替换为 PCIe。

但在 PCIe 和新一代酷睿处理器大规模应用之后，北桥芯片逐渐从主板上消失。曾经的北桥负责高速设备（比如内存、集显），南桥负责低速设备（网卡、声卡、摄像头等）。南桥与北桥之间通常通过 PCI 或 PCIe 总线进行连接。

> 以前的 PS/2 鼠标、PS/2 键盘相当于直连 CPU（北桥）。
>
> 但是现在仍然有直连 CPU 的 USB 总线，一样可以接入键盘和鼠标。因此，用是否直连 CPU 来论证 PS/2 接口的优越性是缺乏依据的。

在现代 x86 处理器中，主板上已不再独立存在北桥芯片。但其功能被集成进 CPU 内部，并由相关逻辑单元负责处理。同时 PCIe 总线也从 CPU 中引出。

直连到 CPU 的 PCIe，本质上就是之前直连北桥的 PCI。现代 CPU 通过引脚连接到主板。CPU 与芯片组之间的互连在英特尔平台上称为 DMI（Direct Media Interface，直接媒体接口），而在 AMD 平台上则采用 PCIe 互连。DMI 3.0x4 相当于 PCIe 3.0x4。

主板上的设备要么直连到 CPU，要么通过主板上的 DMI 总线转接到 CPU。

由于北桥已经集成到 CPU 中，因此有两种方式连接 CPU：

- ① CPU → PCIe（处理器上的 PCIe）→ 设备（任何设备），称之为直连 CPU 的 PCIe；

- ② CPU → PCIe（DMI，芯片组/PCH 上的 PCIe）→ 主板 → PCIe（或转换成其他接口，如 SATA、USB、M.2）→ 设备。

因此，从理论上讲，要获得最大带宽应采用方式 ①，但在实际应用中可能会受到平台稳定性和资源分配的限制。

同时需要注意，PCIe 并不是无限多的，这由 CPU 的规格决定。英特尔处理器提供的 PCIe 通道数量是有限的，例如 PCIe 3.0 ×20，其中 3.0 表示 PCIe 版本，20 表示通道数量。

> 因此，DMI 的上限也不是无穷大的，如果在主板上安装了很多 PCIe x16 插槽，由于 DMI 通道的限制，这只是看上去很好，但实际上不能达到预期效果（如果插满，肯定不会符合预期）。

> **除了直连到 CPU 的设备外，其他设备都共享主板上的 DMI 总线。**

> 从体系结构角度来看，北桥是否集成在 CPU 中在本质上并无根本区别。这是由冯·诺依曼架构所决定的。但在性能和效率上有所提升。

设备之间的转换不仅需要在物理层面进行连接，还需要在软件层面（即驱动程序层面）进行适配。例如，所谓 NVMe 转 USB 的正确说法应该是 USB 3.1 Gen 2 到 PCIe Gen3 x2 桥接控制器。这种转换并不是将 NVMe 转换为 USB，而是将 PCIe 转换为 USB。

不需要单独安装驱动程序，并不意味着设备内部没有控制芯片，因为这类驱动通常已内置于操作系统中。

总线、接口与协议这三者在严格意义上应该是分开的。因此，当谈论 M.2 转换为 PCIe 时，只是物理上将它们连接起来，不需要额外的芯片（因此也不需要驱动程序）。但是，如果要将 M.2 支持 SATA，就需要进行协议转换。

> 例如，虽然 M.2 物理接口相同，但要连接 SATA 硬盘，就必须通过转换芯片进行连接。

> 同样，严格来说并不是 SATA 转换为 M.2，而是 SATA 转换为 PCIe，即使用的是 PCIe Gen3 x1 转 2xSATA 桥接控制器。

因此，当提及 M.2 NVMe SSD 时，应该明确它是一种 PCIe 硬盘，NVMe 则是基于 PCIe 的应用层协议。就像英特尔连接主板与 CPU 的通道的 DMI 在本质上也是 PCIe 一样。

M.2 在物理连接层面上与 PCIe 通道直接对应（无 12 V 供电）。无需任何芯片或电平转换。M.2 接口在设计理念上可视为 Mini PCIe 的后继者，历史上二者也存在一定的继承关系。但是 M.2 没有 12 V（U.2 接口支持，可以视为增强型的 M.2）。

标准的 PCIe 接口同时供电 3.3 V、12 V，最大支持 75 W。而标准的 M.2 最高支持 3.3 V 3 A，即 10 W。

从抽象层面看，总线可以视为一种协议，其特点在于作为公共通道，被多个设备直接或间接共享。真正存在的只有两种类别，物理的接口和软件的协议。这与协议分层无关。硬件信号可以通过电气和逻辑转换进行适配，但在实际应用中仍受成本、性能和稳定性等因素限制。

## microSD 卡（存储卡/TF 卡/SD 卡/内存卡）参数简介

除总线、接口与协议的概念辨析外，了解存储设备的参数也是计算机系统结构的重要组成部分。本节将以 microSD 卡为例，详细介绍其各项参数的含义与选购要点。

存储卡规范是由 [SD 协会](https://www.sdcard.org/) 制定的。

SD 卡的标准较为复杂。即使与 USB-IF 协会制定的 USB 标准相比，其复杂程度亦难分伯仲。

SD 卡标准之所以显得复杂，根源在于：随着技术发展，SD 卡协会既不会弃用既有旧标准（如放弃英制单位、改用公制单位），也很少对原有标准进行升级（如提升版本号）。而是另行制定更高等级的新标准。**SD 卡存在多种并行的度量衡体系，其量程各有重叠和差异。**

![闪迪 microSD 卡](../.gitbook/assets/SD.png)

上图是一张 microSD（Micro Secure Digital，微型 SD）卡，常用于树莓派和手机等设备。

> **注意**
>
> 仅最老款的树莓派使用标准 SD 卡，目前标准 SD 卡“大卡”主要用于相机。

microSD 通常也称为 TF 卡（二者关系类似于 EFI 与 UEFI），亦常被称作手机存储卡。

这块闪迪的 microSD 卡标注了以下信息：

- `SanDisk Ultra`：`SanDisk` 是品牌名“闪迪”的英文名称；`Ultra` 是闪迪的产品型号系列，通常译为“至尊高速”。
- `128 GB`：存储卡的容量是 128 GB。
- `C10`（`10` 被圆形“C”符号环绕）：该参数在当前产品中的参考意义不大，目前市售存储卡几乎全部标注为 C10，低于该等级的产品已较为少见。
- `U1`（`1` 被圆形“U”符号环绕）：`U1` 的最低持续写入速度为 10 MB/s，`U3` 为 30 MB/s。**不存在 U2 等级**。目前仅有 U1 和 U3，通常只有较老产品或低速产品会标注 U1。
- `microSDXC`：表示该卡容量位于 32 GB–2 TB 范围内；2 GB–32 GB 的规格称为 microSDHC。其余规格目前已基本见不到——容量小于 2 GB（microSD）或容量大于 2 TB（microSDUC）。该参数在实际选购中意义不大，因为存储卡本身已明确标注了容量大小。
- `1`（位于 XC 右侧、U1 下方）：表示使用 UHS-I 总线，理论最高速率为 104 MB/s；UHS-II 的理论速率为 312 MB/s。该总线规格决定了存储卡的理论速度上限。
- `A1`：表示应用性能等级，主要反映随机读写能力。目前仅有 A1 和 A2 两个等级；未标注则表示未达到 A1。树莓派官方建议使用 A2 等级的存储卡。

### 补充

- `667x`、`1066x`：雷克沙会标 667x 或 1066x。这种标识方法主要源自光驱倍速体系，目前仅在光盘设备等领域沿用，属于较为古老的标注方式（起源于 20 世纪 80 年代）。

① 667x = 150 KB/s × 667 ≈ 83 MB/s；

② 1066x = 150 KB/s × 1066 ≈ 156 MB/s。

- `V30`：新产品一般将 `U3` 标为 **V30**。不必刻意选择 V60，该等级产品价格较高（普通 A2 存储卡约 1 元/GB，V60 约 3 元/GB，且 V60 与 A2 规格通常不共存）。V90 等级的 microSD 卡目前较为少见；低于 V30 的也较为少见，一般就标注为 `U1`。

速率标准换算：***C10 = U1 = V10*** 这三个等级是同一回事，但通常会同时标注。

这块闪迪 microSD 存储卡上标注了 7 项参数，其中有 4 项在实际使用中的参考价值较低。从参数来看，这款存储卡整体性能较为普通，并无明显优势。

### 存储卡挑选总结

对于树莓派，主要关注容量（推荐至少 32 GB）、连续读写性能（至少 V30）以及随机读写性能（A2）。但目前市面上的存储卡普遍采用这一标注方式，而且除树莓派 5 之外，其他设备（如 Switch）本身大多无法达到 SD 卡设计的总线速率，**因此在实际选购时，主要关注 A1 或 A2 这一参数即可。**

#### 是否符合标称参数？

**扩容卡似乎已不再是常态**

在过去，廉价的大容量存储卡往往是扩容卡，但这类卡连树莓派启动盘制作工具都通不过，因为该工具内置了镜像校验程序。如果标称容量和实际容量不符，就无法完成镜像写入。因此，对于树莓派不必考虑这种问题。另外现在的存储颗粒已经非常廉价了，一般不至于再这么做。如果标称容量并非明显异常（如超过 128 GB 却价格极低），一般不存在此类问题。

**部分标称参数与实际测试不符且会出现掉盘现象**

**移速（MOVE SPEED）**

![移速 128 G A2 U3 V30 128 G 存储卡速度测试](../.gitbook/assets/ys1.png)

![移速 128 G A2 U3 V30 128 G 存储卡速度测试](../.gitbook/assets/ys2.png)

移速（MOVE SPEED）这张卡的测试速度甚至高于部分三星产品。~~这是用空间换时间了吗？~~ 某些 A2 存储卡，实际测试 4K 读写只有不到 1.5 MB/s，这已不单纯是参数虚标的问题。

经过实测，移速 128 G A2 U3 V30 128 G 存储卡，仅仅写入约 60 GB 就会掉盘。

![移速 128 G A2 U3 V30 128 G 存储卡掉盘](../.gitbook/assets/yisusd.png)

![移速 128 G A2 U3 V30 128 G 存储卡掉盘](../.gitbook/assets/yisusd2.png)

### 如何测试存储卡和硬盘？

可以用 `CrystalDiskInfo` 查看硬盘的 S.M.A.R.T. 信息及基本参数。还可以用 `CrystalDiskMark` 测试硬盘和存储卡的读写（请使用 USB 3.0 及以上规格的读卡器）。

上述两款软件由同一位开发者开发，但其[官方网站](https://crystalmark.info/en/)包含较多广告内容，可能导致用户误下载非官方文件。

请从 **[这里](https://sourceforge.net/projects/crystaldiskinfo)** 下载 CrystalDiskInfo；请从 **[这里](https://sourceforge.net/projects/crystaldiskmark/files/)** 下载 CrystalDiskMark。

不建议直接访问其官方网站，因为最终下载链接仍会跳转至上述页面。

在撰写本文时，下载使用的是 `CrystalDiskInfo9_3_2Shizuku.exe` 和 `CrystalDiskMark8_0_5Shizuku.exe`。由于界面配色不同，如不需要额外的视觉效果，可分别选择“CrystalDiskInfo9_3_2.exe”、“CrystalDiskMark8_0_5.exe”代替。

在选购固态硬盘时，不能仅关注读写速度，更重要的是要看固态硬盘的主控、NVMe 协议版本及支持状态。例如，大多数小众品牌固态硬盘都不支持 ASPM（Active State Power Management，活动状态电源管理）技术。此技术能在保证固态硬盘运行效率的情况下尽可能地对固态硬盘进行降温，在实际测试中可使硬盘温度降低约 20 ℃。而一些小众品牌固态硬盘，因为无法很好地适配，开启后就会掉盘，于是主动在固态硬盘的固件中关闭该技术。还有一些小众品牌固态硬盘仍在使用 NVMe 1.4 协议版本。甚至存在多块硬盘使用相同序列号的情况，而硬盘序列号的重要性不亚于网卡的 MAC 地址，原则上不应重复，否则可能导致系统无法正确识别多块硬盘。

#### 使用 CrystalDiskInfo 查看梵想 S690（1 TB）NVMe SSD PCIe 4.0 硬盘参数

![梵想 S690（1 TB）NVMe SSD PCIe4.0](../.gitbook/assets/pciessd3.png)

#### 使用 CrystalDiskMark 测试梵想 S690（1 TB）NVMe SSD PCIe 4.0 读写速率

![梵想 S690（1 TB）NVMe SSD PCIe4.0 读写速率](../.gitbook/assets/pcie4ssd2.png)

![梵想 S690（1 TB）NVMe SSD PCIe4.0 读写速率](../.gitbook/assets/pcie4ssd1.png)

#### 使用 CrystalDiskMark 测试雷克沙 1066x A2 U3 128 GB 存储卡读写速率（使用 USB 3.0 读卡器）

![雷克沙 1066x A2 U3 128 GB 存储卡读写速率](../.gitbook/assets/lkssd2.png)

![雷克沙 1066x A2 U3 128 GB 存储卡读写速率](../.gitbook/assets/lkssd1.png)

雷克沙 1066x A2 U3 128 GB 存储卡实际测试与页面标称严重不符：标称 A2，应达到读 4000 IOPS，写 2000 IOPS。实际上，无论随机读还是随机写都只有一半。这是为什么？

#### 标称速度超过 104 MB/s 的 microSD 存储卡在常规使用场景下意义有限

一方面因为使用的不是超频读卡器（即雷克沙配套的读卡器，用于支持其自定义协议），另一方面，因为 UHS-I 协议的理论速度上限为 104 MB/s（SDR104）。任何存储卡在理论上无法超越这个速度，除非使用 UHS-II（两排金手指），但是对于 microSD 来说，几乎没有使用 UHS-II 的，只有标准大小的 SD 卡才有（相机使用）。因此，市面上无论是三星还是闪迪，只要其标称速度超过 UHS-I 的理论上限且并非 UHS-II 产品，通常都是通过非标准协议实现的。**这种非标准协议只有他们的官方读卡器才能支持（售价极高且一般捆绑销售）。其他设备都不支持这种速率，故没有意义。**

#### 使用 CrystalDiskMark 测试三星 BAR 升级版 + USB 3.1 闪存盘 64 G 读写速率

即金属款。

![三星 BAR 升级版 + USB3.1 闪存盘 64 G 读写速率](../.gitbook/assets/san1.png)

![三星 BAR 升级版 + USB3.1 闪存盘 64 G 读写速率](../.gitbook/assets/san2.png)

### 参考文献

- FreeBSD 中文社区. Raspberry Pi 树莓派中文文档[EB/OL]. [2026-03-25]. <https://rpicn.bsdcn.org>.
- Heath N. Inside the Raspberry Pi: The story of the $35 computer that changed the world[EB/OL]. [2026-03-25]. <https://www.techrepublic.com/article/inside-the-raspberry-pi-the-story-of-the-35-computer-that-changed-the-world/>.
- Kingston Technology. SD 卡和 microSD 卡类型指南[EB/OL]. [2026-03-25]. <https://www.kingston.com/cn/blog/personal-storage/microsd-sd-memory-card-guide>.
- Kingston Technology. SD 卡和 microSD 卡速度等级指南[EB/OL]. [2026-03-25]. <https://www.kingston.com/cn/blog/personal-storage/memory-card-speed-classes>.
- Kingston Technology. 了解 SD 卡和 microSD 卡的命名惯例和标签[EB/OL]. [2026-03-25]. <https://www.kingston.com/cn/blog/personal-storage/microsd-sd-memory-card-naming-conventions>.
- odinkuo. 電腦概論中的考古題，關於光碟機的倍數是指什麼[EB/OL]. [2026-03-25]. <https://www.mobile01.com/topicdetail.php?f=300&t=2126605&p=3>.
- RC丸钢. 移速（MOVE SPEED）64 GB TF（MicroSD）存储卡测试[EB/OL]. [2026-03-25]. <https://www.bilibili.com/read/mobile?id=21681916>.
- SilentNocturne. 移速这个卡虚标了，速度只有标注的二分之一[EB/OL]. [2026-03-25]. <https://post.smzdm.com/talk/p/az6o8zkr/>.
- 远航的加菲猫. Mvespeed 移速 400G 内存卡简单测评[EB/OL]. [2026-03-25]. <https://post.smzdm.com/p/arq759g7/>.
- 尼奥叔叔. 移速 TF 卡翻不翻车？看来没翻（附游戏测试）[EB/OL]. [2026-03-25]. <https://post.smzdm.com/p/awzqn9z4/>.
- Western Digital. 闪迪至尊超极速移动 ™ microSDXC™ UHS-I 存储卡 - 128GB[EB/OL]. [2026-03-25]. <https://www.westerndigital.com/zh-cn/products/memory-cards/sandisk-extreme-pro-uhs-i-microsd?sku=SDSQXCY-128G-ZN6MA>. 参见注释 8：“采用专利技术”。
- 滕飞et. 存储卡也超频？实测结果非常意外[EB/OL]. [2026-03-25]. <https://mp.weixin.qq.com/s/CMioVrUx0YJbF_v7zvQMRA>.
- Samsung. BAR 升级版 + USB3.1 闪存盘[EB/OL]. [2026-03-25]. <https://www.samsung.com.cn/memory-storage/usb-flash-drive/usb-3-1-flash-drive-bar-plus-64gb-titanium-gray-muf-64be4-cn/>.

## 课后习题

1. 在 FreeBSD 系统上使用 CrystalDiskMark 测试不同接口（USB 3.0、NVMe PCIe 3.0）的存储设备，并对比其理论与实际性能差异。
2. 选取 PCIe 协议与 SATA 协议的设计差异，重构一个简化的总线协议模拟程序，用于衡量不同设计对性能与延迟的影响。
3. 修改 NVMe 硬盘的 ASPM 电源管理策略，观察系统功耗与性能的变化。
