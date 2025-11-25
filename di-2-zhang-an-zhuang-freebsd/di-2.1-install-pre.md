# 2.1 安装前的准备工作


## 硬件支持情况

### 最低硬件需求

针对 AMD64 架构，14.2-RELEASE 在虚拟机上测得：

- 硬盘：
  - 仅基本系统（安装后）：550MB
  - KDE 桌面（pkg 安装后）：15G
- 内存：
  - UEFI 下，最小内存为 128M
  - BIOS 下，最小内存为 64M

### 实测硬件支持


| 受支持的硬件类别  | 系列        | 实测型号                                         | 备注                                                                                                          |
| --------- | ------------ | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| CPU       | Intel 大小核    | i7-1260P、N100                                | 实测可支持，但无法合理调度，睿频上限受限                                                                                               |
| NVMe 固态硬盘 | M.2 接口       | 英睿达 P310，Intel 600P，梵想 S530Q、S500Pro、S542PRO | 正常工作                                                                                                        |
| 无线网卡      | Intel AX 系列  | AX200                                        | WiFi 5 速率与 Windows 11 IoT Enterprise 24H2 相当（使用 iperf2 测得）                                                                     |
| 有线网卡      | Realtek 2.5G | RTL8125B                                     | 需要额外安装驱动，参见全书附录                                                                                             |
| 有线网卡      | Intel 2.5G   | i226-V                                       | 正常工作                                                                                                        |
| 英特尔/AMD 显卡        | 英特尔、AMD 近十多年的显卡        |   英特尔锐炬 ® Xe 显卡、Intel HD Graphics 4000       | 支持水平与 drm 移植进度相关；写作本文时相当于 Linux 内核 6.6，最新状态参见 [freebsd/drm-kmod](https://github.com/freebsd/drm-kmod/pulls) |
| NVIDIA 显卡 | 近十多年的显卡   | GTX 850M  | 受 NVIDIA 官方显卡驱动支持     |

>**注意**
>
>FreeBSD 不支持 [安全启动](https://wiki.freebsd.org/SecureBoot)，在安装 FreeBSD 前请务必关闭安全启动（SecureBoot）；FreeBSD 也不支持 Fake RAID（伪 RAID），请将其控制器修改为 AHCI。
>
>操作方法请咨询购机厂商技术售后。

### 特定硬件支持情况查询

更多硬件请参考：

[Hardware for BSD](https://bsd-hardware.info/?view=search)

![](../.gitbook/assets/h1.png)

![](../.gitbook/assets/h2.png)

>**注意**
>
>推荐还是实际测试看看，因为该网站也会出现一些错误，比如将 LPDDR5 误认为 LPDDR4。

## 下载 FreeBSD 镜像

首先我们打开 FreeBSD 项目官网：<https://www.freebsd.org/>：

![FreeBSD 项目官网](../.gitbook/assets/do1.png)

我们点击黄底红字 `Download FreeBSD`，会跳转如下：

![下载 FreeBSD](../.gitbook/assets/do2.png)

>**技巧**
>
>随着岁月的流逝，在读者下载的时候，已经没有 14.2 了。你只需要选择最顶部的一个 `FreeBSD-X.Y-RELEASE`（这是推荐用于生产环境的版本）即可。其中，现在在读者面前的 `X.Y` 应是比 `14.2` 大的值。

>**警告**
>
>使用非 RELEASE 的用户应有意愿有时间关注实时的开发动态，浏览邮件列表与 Bug 列表，如：[freebsd-src/UPDATING](https://github.com/freebsd/freebsd-src/blob/main/UPDATING) 及 [freebsd-src/RELNOTES](https://github.com/freebsd/freebsd-src/blob/main/RELNOTES) 等等信息。并且要求用户具备一定的探索能力和动手意愿，否则建议读者使用 RELEASE 版本。

|Installer|VM|SD Card|Documentation|
|:---:|:---:|:---:|:---:|
|安装镜像 | 虚拟机预安装镜像 | 存储卡镜像 | 文档|
|一般安装使用 | 需要自己扩容 | 单板机/嵌入式用 | 就是文档|

>**技巧**
>
>如果你不知道选哪个，请你选择 `Installer`（普通家用电脑，苹果除外）。

>**技巧**
>
>如果你不知道 `amd64` `i386` `aarch64` `armv7` 是什么意思，请你选择 `amd64`（普通家用电脑，苹果除外）。

![FreeBSD 镜像](../.gitbook/assets/do3.png)


```sh
File Name                                          File Size      Date                 
Parent directory/                                  -              -                     
CHECKSUM.SHA256-FreeBSD-14.2-RELEASE-amd64         1171           2024-Nov-29 14:11     
CHECKSUM.SHA512-FreeBSD-14.2-RELEASE-amd64         1811           2024-Nov-29 14:09     
FreeBSD-14.2-RELEASE-amd64-bootonly.iso            459491328      2024-Nov-29 13:04     
FreeBSD-14.2-RELEASE-amd64-bootonly.iso.xz         100595956      2024-Nov-29 13:04     
FreeBSD-14.2-RELEASE-amd64-disc1.iso               1310040064     2024-Nov-29 13:05     
FreeBSD-14.2-RELEASE-amd64-disc1.iso.xz            855850608      2024-Nov-29 13:05     
FreeBSD-14.2-RELEASE-amd64-dvd1.iso                4826406912     2024-Nov-29 13:05     
FreeBSD-14.2-RELEASE-amd64-dvd1.iso.xz             3812250832     2024-Nov-29 13:05     
FreeBSD-14.2-RELEASE-amd64-memstick.img            1559351808     2024-Nov-29 13:05     
FreeBSD-14.2-RELEASE-amd64-memstick.img.xz         867177260      2024-Nov-29 13:05     
FreeBSD-14.2-RELEASE-amd64-mini-memstick.img       564220416      2024-Nov-29 13:04     
FreeBSD-14.2-RELEASE-amd64-mini-memstick.img.xz    107445036      2024-Nov-29 13:04     
```

以上：第一列代表文件名，第二列是文件大小，第三列是发布日期。

|首列 | 说明|
|:---|:---|
|Parent directory/	-	-|点击后返回上级目录|
|CHECKSUM.SHA256-FreeBSD-14.2-RELEASE-amd64	  | 本页所有镜像的 SHA256 校验值 |
|CHECKSUM.SHA512-FreeBSD-14.2-RELEASE-amd64   |  本页所有镜像的 SHA512 校验值 |
|FreeBSD-14.2-RELEASE-amd64-bootonly.iso	      | 网络安装镜像，安装时需联网 |
|FreeBSD-14.2-RELEASE-amd64-bootonly.iso.xz	    | 压缩的网络安装镜像，安装时需联网|
|FreeBSD-14.2-RELEASE-amd64-disc1.iso	 | cd 镜像    |
|FreeBSD-14.2-RELEASE-amd64-disc1.iso.xz	|  压缩的 cd 镜像 |
|FreeBSD-14.2-RELEASE-amd64-dvd1.iso	 | dvd 镜像，相比 cd 镜像多了一些没用的 pkg 包    |
|FreeBSD-14.2-RELEASE-amd64-dvd1.iso.xz	  | 压缩的 dvd 镜像，相比 cd 镜像多了一些没用的 pkg 包  |
|FreeBSD-14.2-RELEASE-amd64-memstick.img	| U 盘用的镜像（可以使用 Rufus 制作 U 盘启动盘）   |
|FreeBSD-14.2-RELEASE-amd64-memstick.img.xz	 | 压缩的 U 盘用的镜像（无需解压缩，可以使用 Rufus 制作 U 盘启动盘）   |
|FreeBSD-14.2-RELEASE-amd64-mini-memstick.img	 | U 盘用的网络安装镜像，安装时需联网 |
|FreeBSD-14.2-RELEASE-amd64-mini-memstick.img.xz|压缩的 U 盘用的网络安装镜像，安装时需联网 |

>**技巧**
>
>网络是随时波动的，因此下载的文件时而会与源文件有差异，产生错误。~~百度网盘就经常这样~~。因此我们需要一种机制确保你获取的文件与 FreeBSD 项目发布的镜像是完全一致的。就需要用到 **校验值**。Windows 10、11 均自带命令行工具 `CertUtil`，无需额外的软件。你还可以参考 [如何确定用于安全应用程序的文件 SHA-256 哈希](https://www.dell.com/support/kbdoc/en-bs/000130826/%E5%A6%82%E4%BD%95-%E7%A1%AE%E5%AE%9A-%E7%94%A8%E4%BA%8E-%E9%98%B2-%E7%97%85%E6%AF%92-%E5%92%8C-%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6-%E9%98%B2%E6%8A%A4-%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F-%E7%9A%84-%E6%96%87%E4%BB%B6-sha-256-%E5%93%88%E5%B8%8C?lang=zh) 这篇文章。


> **注意**
>
>FreeBSD 所有安装介质包括不限于虚拟机文件都没有提供图形界面（DVD 有 pkg 包，但是会出问题），均需要自行安装。

>**技巧**
>
>FreeBSD 镜像 BT 种子下载地址
>
><https://fosstorrents.com/distributions/freebsd/>

- RELEASE 正式版镜像下载地址
  - 虚拟机用：<https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/14.2/FreeBSD-14.2-RELEASE-amd64-disc1.iso>
  - 物理机用：<https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/14.2/FreeBSD-14.2-RELEASE-amd64-memstick.img>
- CURRENT 开发版下载地址（仅限专业用户）
  - 虚拟机用：[https://download.freebsd.org/snapshots/amd64/amd64/ISO-IMAGES/15.0/](https://download.freebsd.org/snapshots/amd64/amd64/ISO-IMAGES/15.0/)
  - 物理机下载 `-amd64-memstick.img` 或 `-amd64-memstick.img.xz` 结尾的文件

旧版本 FreeBSD 下载地址：

- 5.1-9.2 <http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/old-releases/amd64/ISO-IMAGES>
- 9.3-最新 <http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/old-releases/ISO-IMAGES/>


## 刻录 FreeBSD 镜像

>**技巧**
>
>FreeBSD 14.1 RELEASE 两个 ISO 均在 Ventoy 下测试通过（英特尔三代处理器下的 UEFI）。但是仍不排除出现问题的可能性。如果出现问题，请首先考虑下载 `img` 正常刻录。15.0 实测无法引导。


>**技巧**
>
>U 盘安装最好使用 `-img` 或 `-img.xz`。因为 `.iso` 镜像没做 Hybrid 混合启动，写入 U 盘会产生错误。见 [FreeBSD -.iso files not support written to USB drive](https://bugs.freebsd.org/bugzilla/show\_bug.cgi?id=236786)。
>
>
>只有当使用 **光盘/虚拟机** 安装时才应选用 `iso` 结尾的镜像。
>
>但事无绝对，某些机器使用 `.iso` 刻录 U 盘启动盘，仍然可以顺利进入安装界面。部分机器（如老款神舟电脑）就支持 ISO 下的 UEFI 启动。但并非所有机器（比如小米就不支持）都如此。

- 我该如何刻录 FreeBSD 镜像到 U 盘？

Windows 上的刻录工具应首选 **Rufus**，Linux 直接使用 `dd` 命令即可。rufus 下载地址：[https://rufus.ie/zh](https://rufus.ie/zh)

> **警告**
>
> **不建议** 使用 FreeBSD 手册推荐的 win32diskimager，有时会出现校验码错误的情况（实际上文件校验码正常）。**应仅在 rufus 无效的情况下才使用 win32diskimager。** win32diskimager 下载地址 <https://sourceforge.net/projects/win32diskimager/files/Archive/>，点击 `win32diskimager-1.0.0-install.exe` 即可下载。


>**技巧**
>
>rufus 刻录镜像时，无需解压缩，直接选择 `-img.xz` 亦可进行启动盘制作的过程。
>
>![rufus](../.gitbook/assets/rufus.png)

## 附录：上传自己的硬件数据

如果你也想上传你的数据到 <https://bsd-hardware.info>，请：

### 安装 hw-probe

- 使用 pkg 安装：

 ```sh
 # pkg install hw-probe
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/sysutils/hw-probe/
# make install clean
```

### 上传数据

命令行执行：

```sh
# hw-probe -all -upload
Probe for hardware ... Ok
Reading logs ... Ok
Uploaded to DB, Thank you!

Probe URL: https://bsd-hardware.info/?probe=f64606c4b1
```

打开上面的链接，即可看到你的设备。笔者上传的是 Radxa x4 的配置信息。

其他操作系统见 [INSTALL HOWTO FOR BSD](https://github.com/linuxhw/hw-probe/blob/master/INSTALL.BSD.md)


