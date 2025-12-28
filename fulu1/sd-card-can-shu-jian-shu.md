# 存储设备基础

## microSD 卡（存储卡/TF 卡/SD 卡/内存卡）参数简介

存储卡规范是由 [SD 协会](https://www.sdcard.org/) 制定的。

SD 卡的标准较为复杂，甚至与 USB-IF 协会制定的 USB 标准相比，其复杂程度亦难分伯仲，这一点 SD 卡协会负有主要责任。

SD 卡标准之所以显得复杂，根源在于随着技术发展，SD 卡协会既不会弃用既有旧标准（如放弃英制单位、改用公制单位），也很少对原有标准进行升级（如提升版本号），而是另行制定更高等级的新标准。**简言之，SD 卡存在多种并行的度量衡，且量程各有重叠和差异。**

![闪迪 microSD 卡](../.gitbook/assets/SD.png)

上图是一张 microSD（Micro Secure Digital，微型 SD）卡，常用于树莓派和手机等设备。

>**注意**
>
>仅最老款的树莓派使用标准 SD 卡，目前标准 SD 卡“大卡”主要用于相机。

microSD 也就是通常所说的 TF 卡（两者关系类似于 EFI 与 UEFI），也常被称为手机存储卡。

这块闪迪的 microSD 卡，上面标有：

- `SanDisk Ultra`：`SanDisk` 是品牌名“闪迪”的英文名称；`Ultra` 是闪迪的产品型号系列，通常译为“至尊高速”。
- `128 GB`：存储卡的容量是 128 GB。
- `C10`（`10` 被圆形“C”符号环绕）：该参数在当前产品中的参考意义不大，目前市售存储卡几乎全部标注为 C10，低于该等级的产品已较为少见。
- `microSDXC`：表示该卡容量位于 32 GB–2 TB 范围内；2 GB–32 GB 的规格称为 microSDHC。其他的，现在基本上见不到——容量小于 2G（microSD）或容量大于 2TB（microSDUC）。该参数在实际选购中意义不大，因为存储卡本身已明确标注了容量大小。
- `U1`（`1` 被圆形“U”符号环绕）：`U1` 的最低持续写入速度为 10 MB/s，`U3` 为 30 MB/s。​**不存在 U2 等级**​。目前仅有 U1 和 U3，通常只有较老产品或低速产品会标注 U1。
- `1`（位于 XC 右侧、U1 下方）：表示使用 UHS-I 总线，理论最高速率为 104 MB/s；UHS-II 的理论速率为 312 MB/s。该总线规格决定了存储卡的理论速度上限。
- `A1`：表示应用性能等级，主要反映随机读写能力。目前仅有 A1 和 A2 两个等级，未标注则表示未达到 A1。树莓派官方建议使用 A2 等级的存储卡。


## 补充

- `667x`、`1066x`：雷克沙等卡会标 667x、或 1066x，这种标识方法主要源自光驱倍速体系，目前仅在光盘设备等领域沿用，属于较为古老的标注方式（起源于 20 世纪 80 年代）。

① 667x = 150 KB/s × 667 ≈ 83 MB/s；

② 1066x = 150 KB/s × 1066 ≈ 156 MB/s。

- `V30`：新产品一般将 `U3` 标为 **V30**。不必刻意选择 V60，该等级产品价格较高（普通 A2 存储卡约 1 元/GB，V60 约 3 元/GB，且 V60 与 A2 规格通常不共存）。V90 等级的 microSD 卡目前较为少见。低于 V30 的也较为少见，一般就标注为 `U1`。速率标准换算：***C10 = U1 = V10*** 这 3 个东西其实是一回事，但同时标着。


总结：这块闪迪 microSD 存储卡上标注了 7 项参数，其中有 4 项在实际使用中的参考价值较低。从参数来看，这款存储卡整体性能较为普通，并无明显优势。

## 存储卡挑选总结

总结：对于树莓派，主要关注容量（推荐至少 32 GB）、连续读写性能（至少 V30）以及随机读写性能（A2）。但目前市面上的存储卡普遍采用这一标注方式，而且除树莓派 5 之外，其他设备（如 Switch）本身大多无法达到 SD 卡设计的总线速率，**因此在实际选购时，主要关注 A1 或 A2 这一参数即可。**

### 参数标称就符合？

**扩容卡似乎已不再是常态**

在过去，廉价的大容量存储卡往往是扩容的，但是这种卡连树莓派启动盘制作工具都通不过，因为该工具内置了镜像校验程序。如果标称容量和实际对不上，就无法完成镜像写入。所以，对于树莓派不必考虑这种问题。另外现在的存储颗粒已经非常廉价了，一般不至于再这么做。如果标称容量并非明显异常（如超过 128 GB 却价格极低），一般不存在此类问题。

**部分标称参数与实际测试不符且会掉盘**

**移速（MOVE SPEED）**

![移速 128G A2 U3 V30 128G 存储卡速度测试](../.gitbook/assets/ys1.png)

![移速 128G A2 U3 V30 128G 存储卡速度测试](../.gitbook/assets/ys2.png)

移速（MOVE SPEED）这张卡的测试速度甚至高于部分三星产品。~~这是用空间换时间了吗？~~ 某些 A2 存储卡，实际测试 4k 读写只有不到 1.5MB/s，快赶上那个金士顿 DT100G3 了。这已经超出了单纯参数虚标的问题。

但是经过实测，移速 128G A2 U3 V30 128G 存储卡，仅仅写入约 60 GB 就会掉盘。变成这样：

![移速 128G A2 U3 V30 128G 存储卡掉盘](../.gitbook/assets/yisusd.png)

![移速 128G A2 U3 V30 128G 存储卡掉盘](../.gitbook/assets/yisusd2.png)


## 如何测试存储卡和硬盘？

我们可以用 `CrystalDiskInfo` 查看硬盘的 S.M.A.R.T. 信息及基本参数。还可以用 `CrystalDiskMark` 测试硬盘和存储卡的读写（请使用 USB 3.0 及以上规格的读卡器）。

上述两款软件由同一位开发者开发，但其[官方网站](https://crystalmark.info/en/) 包含较多广告内容，可能导致用户误下载非官方文件。

请从 **[这里](https://sourceforge.net/projects/crystaldiskinfo)** 下载 CrystalDiskInfo；请从 **[这里](https://sourceforge.net/projects/crystaldiskmark/files/)** 下载 CrystalDiskMark；

因此不建议直接访问其官方网站，因为最终下载链接仍会跳转至上述页面。

在撰写本文时，笔者下载使用的是 `CrystalDiskInfo9_3_2Shizuku.exe` 和 `CrystalDiskMark8_0_5Shizuku.exe`。由于界面配色不同，如不需要额外的视觉效果，可分别选择“CrystalDiskInfo9_3_2.exe”、“CrystalDiskMark8_0_5.exe”代替之。

>**注意**
>
>在选购固态硬盘时，不能一味地看读写速度，这没有意义，因为市面上的固态读写速度都大同小异。更重要的是要看固态的主控、NVMe 协议版本及支持状态。
>
>比如大多数杂牌固态都不会支持 ASPM（Active State Power Management，活动状态电源管理）技术。此技术能在保证固态运行效率的情况下尽可能地对固态进行降温，在实际测试中可使硬盘温度降低约 20 ℃。而一些杂牌固态，因为无法很好地适配，开启后就会掉盘，于是主动对该技术在固态的固件中予以关闭。
>
>还有一些杂牌固态仍在使用 NVMe 1.4 协议版本。甚至存在多块硬盘使用相同序列号的情况，而硬盘序列号的重要性不亚于网卡的 MAC 地址，原则上不应重复，否则可能导致系统无法正确识别多块硬盘。

### 使用 CrystalDiskInfo 查看梵想 S690（1TB）NVMe SSD PCIe4.0 硬盘参数

![梵想 S690（1TB）NVMe SSD PCIe4.0](../.gitbook/assets/pciessd3.png)


### 使用 CrystalDiskMark 测试梵想 S690（1TB）NVMe SSD PCIe4.0 读写速率

![梵想 S690（1TB）NVMe SSD PCIe4.0 读写速率](../.gitbook/assets/pcie4ssd2.png)

![梵想 S690（1TB）NVMe SSD PCIe4.0 读写速率](../.gitbook/assets/pcie4ssd1.png)


### 使用 CrystalDiskMark 测试雷克沙 1066x A2 U3 128GB 存储卡读写速率（使用 USB 3.0 读卡器）


![雷克沙 1066x A2 U3 128GB 存储卡读写速率](../.gitbook/assets/lkssd2.png)

![雷克沙 1066x A2 U3 128GB 存储卡读写速率](../.gitbook/assets/lkssd1.png)

可以明显地看到，雷克沙 1066x A2 U3 128GB 存储卡实际测试与页面标称严重不符：标称 A2，应达到读 4000 IOPS，写 2000 IOPS。实际上，无论随机读还是随机写都只有一半；连续读写更是无稽之谈。这是为什么？

#### 标称速度超过 104 MB/s 的 microSD 存储卡在常规使用场景下意义有限

这是为什么？一方面因为使用的不是超频读卡器（即雷克沙配套的读卡器，用于支持其自定义协议），因为 UHS-I 协议的理论速度上限为 104 MB/s（SDR104）。任何存储卡在理论上无法超越，除非使用 UHS-II（两排金手指），但是对于 microSD 来说，几乎没有使用 UHS-II 的，只有标准大小的 SD 卡才有（相机使用）。因此，市面上无论是三星还是闪迪，只要其标称速度超过 UHS-I 的理论上限且并非 UHS-II 产品，通常都是通过非标准协议实现的。**这种非标准协议只有他们的官方读卡器才能支持（售价极高且一般捆绑销售）。其他设备都是不支持这种速率的，故没有意义。**

### 使用 CrystalDiskMark 测试三星 BAR 升级版 + USB3.1 闪存盘 64G 读写速率

即金属款。

![三星 BAR 升级版 + USB3.1 闪存盘 64G 读写速率](../.gitbook/assets/san1.png)

![三星 BAR 升级版 + USB3.1 闪存盘 64G 读写速率](../.gitbook/assets/san2.png)

## 参考文献

- [Raspberry Pi 树莓派中文文档](https://rpicn.bsdcn.org)
- [Inside the Raspberry Pi: The story of the $35 computer that changed the world](https://www.techrepublic.com/article/inside-the-raspberry-pi-the-story-of-the-35-computer-that-changed-the-world/)
- [SD 卡和 microSD 卡类型指南](https://www.kingston.com/cn/blog/personal-storage/microsd-sd-memory-card-guide)
- [SD 卡 和 microSD 卡速度等级指南](https://www.kingston.com/cn/blog/personal-storage/memory-card-speed-classes)
- [了解 SD 卡和 microSD 卡的命名惯例和标签](https://www.kingston.com/cn/blog/personal-storage/microsd-sd-memory-card-naming-conventions)
- [電腦概論中的考古題，關於光碟機的倍數是指什麼](https://www.mobile01.com/topicdetail.php?f=300&t=2126605&p=3)
- [移速（MOVE SPEED）64GB TF（MicroSD）存储卡测试](https://www.bilibili.com/read/mobile?id=21681916)
- [移速这个卡虚标了，速度只有标注的二分之一](https://post.m.smzdm.com/talk/p/az6o8zkr/)
- [Mvespeed 移速 400G 内存卡简单测评](https://post.m.smzdm.com/p/arq759g7/)
- [移速 TF 卡翻不翻车？看来没翻（附游戏测试）](https://post.m.smzdm.com/p/awzqn9z4/)
- [闪迪至尊超极速移动 ™ microSDXC™ UHS-I 存储卡 - 128GB](https://www.westerndigital.com/zh-cn/products/memory-cards/sandisk-extreme-pro-uhs-i-microsd?sku=SDSQXCY-128G-ZN6MA)（参见注释 8：“采用专利技术”）
- [存储卡也超频？实测结果非常意外](https://mp.weixin.qq.com/s/CMioVrUx0YJbF_v7zvQMRA)
- [BAR 升级版 + USB3.1 闪存盘](https://www.samsung.com.cn/memory-storage/usb-flash-drive/usb-3-1-flash-drive-bar-plus-64gb-titanium-gray-muf-64be4-cn/)

