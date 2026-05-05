# 4.1 Windows 用户迁移指南

操作系统迁移涉及文件系统概念、字符编码、换行符规范、时区处理等多维度差异。从 Windows 迁移至 FreeBSD 的用户，须先理解这些差异，方可顺利过渡。

## 文件系统基础

首先，观察以下两幅图像：

![文件系统基础](../.gitbook/assets/filesystem-bamboo-2.jpg)

![文件系统基础](../.gitbook/assets/filesystem-bamboo-3.jpg)

前一幅图像展示的是竹子（Bambusoideae），后一幅图像展示的是若干棵行道树。

亚里士多德认为种子之所以能长成大树，是因为种子蕴含一种潜能，环境条件具备时便可能长成一棵树（参见《形而上学》IX.7, 1049b）。人与器物的差别，在于人没有固定不变的潜能——这契合了儒家“君子不器”（何晏，注；邢昺，疏. 论语注疏[M]. 北京：中国致公出版社，2016. ISBN: 978-7-5145-0846-8.）和萨特“存在先于本质”之说（参见 Sartre J P. 萨特哲学论文集[M]. 潘培庆，等，译. 合肥：安徽文艺出版社，1998. ISBN: 7-5396-1632-6.）。由此观之，理解 UNIX 目录与 Windows 目录的异同，便能洞悉操作系统设计与实现的逻辑。

![文件系统基础](../.gitbook/assets/filesystem-bamboo.png)

竹子的生长发育常被用作经典生物学案例：竹子（Bambusoideae）开花，往往预示大片竹林将随之死亡。原因在于，许多看似茂密繁盛的竹林，很可能只有一棵竹子真实存活——它们均从同一地下根系长出，看似多棵独立个体，实则同属一个整体。植物学称此现象为**克隆生长**（clonal growth），这也是“雨后春笋”的由来。无论竹子之间相隔多远，仍旧一荣俱荣、一损俱损。

这正是 UNIX 目录的写照：系统中的所有目录均依托根目录（root）。根（**/**）是一切目录的起点，构成**单一层次的目录树结构**（single-rooted directory hierarchy）。例如 **/home/ykla/nihao**、**/bin/sh**、**/etc/fstab**，追根溯源，均从根目录出发。换言之，删除 **/** 即意味着删除整个系统，所有设备上的目录均将一并删除。

![文件系统基础](../.gitbook/assets/windows-file-explorer.png)

行道树则不同，每棵均独立生长。即便两树紧邻而立，也仍然是独立的个体。行道树正如 Windows 目录，盘符各自独立——`C:\Program Files (x86)\Google\Update`、`D:\BaiduNetdiskDownload\工具列表`、`E:\123\app`：`C`、`D`、`E` 盘彼此隔离、互不干扰。格式化 `D` 盘，不影响 `E` 盘中存储的文件。即便在 PE 中格式化 `C` 盘（可能不会显示为 `C` 盘），`E` 盘文件亦不受影响。

Windows 的“盘符”并非固定存在。在 PE 环境中，`C` 盘可能显示为其他盘符（如 `X`）；运行中的 Windows 亦可任意分配盘符。

Windows 判断分区与盘符的对应关系，依据的是 GPT 分区类型 UUID（如 Windows 数据分区类型 UUID 为 `EBD0A0A2-B9E5-4433-87C0-68B6B72699C7`，即 Microsoft Basic Data 类型，适用于所有 Windows 数据分区，而非仅限 C 盘）以及分区的唯一 GUID（相关配置由 Windows 装入管理器 Mount Manager 写入注册表 `HKLM\SYSTEM\MountedDevices`），而非依靠盘符自身。

查看盘符和卷的映射关系：

```powershell
PS C:\WINDOWS\system32> Get-ItemProperty -Path "HKLM:\SYSTEM\MountedDevices"


\DosDevices\C:                          : {68, 77, 73, 79...}   # C: 盘符映射项，对应某个磁盘卷的二进制标识（Volume GUID/卷结构数据）
#{6dc6b5e1-fff0-11f0-bf73-b0416f0b5119} : {68, 77, 73, 79...}   # 卷 GUID（唯一卷标识符），表示某个物理分区；右侧为该卷的内部二进制数据
\DosDevices\D:                          : {68, 77, 73, 79...}   # D: 盘符映射项，对应另一个磁盘卷的标识数据
PSPath
                                 :
……省略其他输出……
```

盘符是一种抽象映射，本身并无固定不变的物理意义。这也解释了为何在其他操作系统中（包括 Windows 双系统环境）均看不到 `C` 盘——根本原因在于，文件系统中并不存在硬编码的 `C` 盘标识。只有实际启动系统后，Windows 才能确定哪个分区对应 `C` 盘，并写入注册表。其他盘符的分配则存在不确定性，`D` 盘变为 `E` 盘的情形也屡见不鲜，例如某虚拟光驱可能在开机时被自动加载。

> **思考题**
>
> 阅读《深入解析 Windows 操作系统（第 7 版）（卷 2）》（978-7-115-61974-7，人民邮电出版社）及其他相关文献资料，回答问题：在传统的 BIOS + MBR 引导下，Windows 如何识别 `C` 盘？

### 挂载的概念与机制

![如何理解挂载](../.gitbook/assets/mount-concept.png)

从园艺角度看，通常需要从树 A 剪取一段枝条，斜插至树 B 上并加以包裹，待愈合后二者便成为一体：例如苹果树（UNIX）上可结出桃子（挂载 Windows 的 `C` 盘）。

这种方法称为“嫁接”。其实质是将树 A 的枝条（文件系统）挂载到树 B 上（嫁接点即挂载点，终究依托根目录 **/**）。

就操作系统技术层面而言，挂载（mount）是指将文件系统附加到系统目录树已有目录（挂载点）上的操作。文件系统可视作以 **/** 为根的树形结构，一个文件系统必须挂载到另一文件系统中的某目录上。文件系统 B 挂载至目录 A 后，B 的根目录取代 A，B 所含目录随之显现；A 中原有文件则暂时隐藏，直至 B 从 A 卸载后方重新出现。

工具 mount 调用 nmount(2) 系统调用，将一个特殊设备或远程节点（rhost:path）映射并嫁接到文件系统树中的节点（node）位置。系统维护一个当前已挂载文件系统的列表。如果不带任何参数调用 mount，将打印此列表。

> **注意**
>
>FreeBSD 的 `mount` 源于 4.4BSD，与 Linux 的 `mount` 在选项语法上基本兼容，但 FreeBSD 使用的是 nmount(2) 系统调用而非 Linux 的 mount(2)。FreeBSD 的 `mount` 会根据文件系统类型自动调用 **/sbin/mount_type** 程序（如 `mount_nfs`、`mount_msdosfs`）。

### 卸载的概念与机制

![如何理解卸载](../.gitbook/assets/unmount-concept.png)

熟悉园艺的读者，对“扦插”这种植物培育方法应不陌生：

将一棵树新发的侧枝剪下，插入土中。悉心照料一段时间后，即可获得一株新的幼苗。

这与卸载的原理相通：将某个文件系统（如 **/mnt/test**）从完整的根（**/**）上卸下，即解除其与目录树的关联。

就技术层面而言，卸载（unmount）是挂载的逆操作，它将已挂载的文件系统从系统目录树中分离。文件系统 B 从 A 卸载后，A 中原有文件重新出现。

### fstab 文件

在启动过程中，系统将自动挂载 **/etc/fstab** 文件中列出的文件系统（标注 `noauto` 选项的条目除外）。

该文件中的条目格式如下：

```sh
设备       /挂载点 文件系统     选项      转储     fsck 检查顺序
```

说明：

- `设备`：现有设备名。
- `挂载点`：现有的目录，用于挂载文件系统。
- `文件系统`：传递给 mount(8) 的文件系统类型。
- `选项`：`rw` 表示读写文件系统，`ro` 表示只读文件系统，可跟其他选项。常用选项包括 `noauto`，表示启动时不挂载此文件系统。
- `转储`：供 dump(8) 判断哪些文件系统需要备份。缺省时视为 0。
- `fsck 检查顺序`：决定在重启后，哪些文件系统应由 fsck(8) 检查，以及检查顺序。应跳过的文件系统设置为 0。根文件系统应优先检查，设为 1，其他文件系统应设为大于 1 的值。若多个文件系统具有相同的 `passno`，fsck(8) 会尝试并行检查。

示例：标准 ZFS 安装下的 **/etc/fstab** 文件。

```sh
# Device		Mountpoint	FStype	Options		Dump	Pass#
/dev/gpt/efiboot0		/boot/efi	msdosfs	rw		2	2	# EFI 分区
/dev/nda0p2		none	swap	sw		0	0	# 交换分区
```

>**注意**
>
>ZFS 并不使用 **/etc/fstab** 文件。因此如果在该文件中不存在任何 ZFS 文件系统（**/**），是符合预期的。

示例：标准 UFS 安装下的 **/etc/fstab** 文件。

```sh
# Device	Mountpoint	FStype	Options	Dump	Pass#
/dev/nda0p2	/		ufs	rw	1	1	# 根分区
/dev/nda0p1	/boot/efi		msdosfs	rw	2	2	# EFI 分区
/dev/nda0p3	none		swap	sw	0	0	# 交换分区
```

### 参考文献

- 微软. PARTITION_INFORMATION_GPT[EB/OL]. [2026-04-18]. <https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ns-winioctl-partition_information_gpt>. GPT 分区类型 GUID 定义，其中 Microsoft Basic Data 类型为 EBD0A0A2-B9E5-4433-87C0-68B6B72699C7。
- 微软. Supporting Mount Manager Requests in a Storage Class Driver[EB/OL]. [2026-04-18]. <https://learn.microsoft.com/en-us/windows-hardware/drivers/storage/supporting-mount-manager-requests-in-a-storage-class-driver>. Windows 装入管理器将盘符与分区的映射关系持久化存储于注册表 `HKLM\SYSTEM\MountedDevices`。
- GBIF. Bambusoideae Luerss.[EB/OL]. [2026-04-18]. <https://www.gbif.org/species/113642445>. 竹亚科许多物种具有群体开花（gregarious flowering）特性，开花后常因资源耗竭而死亡；竹子通过地下根茎系统进行克隆生长（clonal growth），同一克隆的个体共享资源。
- Aristotle. Metaphysics[M]. Translated by W. D. Ross. Oxford: Clarendon Press, 1908. Book IX (Theta), Chapter 7, 1049b. 亚里士多德论潜能与现实：种子之所以能长成大树，是因为种子暗含着一种潜能。

## 文件名规范的差异

### 非法字符

许多在 FreeBSD 中合法的文件名或路径，在 Windows 中均属非法（即包含非法字符）。在 Windows 上使用 Git 拉取项目时，此类情形较为常见。

以下仅列举部分典型情况：

- 文件或文件夹名称中不能包含英文冒号 `:`。

![非法字符](../.gitbook/assets/windows-invalid-char-1.png)

- 无法将文件或文件夹命名为 `con`。

![非法字符](../.gitbook/assets/windows-invalid-char-2.png)

更多要求参见：微软. 命名文件、路径和命名空间[EB/OL]. [2026-03-26]. <https://learn.microsoft.com/zh-cn/windows/win32/fileio/naming-a-file>.

> **技巧**
>
> 可在 Windows 下使用 git 工具拉取 [freebsd-doc](https://github.com/freebsd/freebsd-doc) 项目验证兼容性问题。相关 Bug 报告：[The colon in the file name of the security report of the FreeBSD doc is not compatible with Microsoft Windows](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=267636)

### 大小写敏感性

FreeBSD 的 ZFS 和 UFS 均**区分大小写（大小写敏感）**。而 macOS 的 HFS+（默认不区分大小写）、APFS（默认不区分大小写）以及 Windows 的 FAT32 文件系统均**不区分大小写（大小写不敏感）**。NTFS 本身为大小写保留文件系统，但 Windows 的 Win32 子系统默认以大小写不敏感方式处理文件名（Windows 10 1803 以后可通过 `fsutil.exe file queryCaseSensitiveInfo <路径>` 按目录启用大小写敏感，主要用于 WSL 兼容）。

- Windows 下 **大小写不敏感**

![大小写敏感](../.gitbook/assets/windows-case-sensitive.png)

在 Windows 中，`abc` 和 `ABC` 被视为同一文件，无法共存。

> **技巧**
>
> 判断网站服务器类型的简易方法：若 `https://example.com/path` 和 `https://example.com/PATH` 均可访问且内容相同，则该网站可能运行在 Windows 操作系统上。

- FreeBSD 下 **大小写敏感**

```sh
$ touch ABC    # 创建名为 ABC 的文件
$ touch abc    # 创建名为 abc 的文件
$ ls           # 列出当前目录内容（区分文件名大小写）
abc    ABC
```

在 FreeBSD 中，`abc` 和 `ABC` 是两个独立文件，可以共存。

#### 参考文献

- 微软. 调整区分大小写[EB/OL]. [2026-03-26]. <https://learn.microsoft.com/en-us/windows/wsl/case-sensitivity>. Windows 文件系统支持使用属性标志按目录设置区分大小写，提供跨平台文件兼容性支持。
- 微软. FAT32 File System[EB/OL]. [2026-04-18]. <https://learn.microsoft.com/en-us/previous-versions/aa364047(v=vs.85)>. FAT 文件系统卷不区分大小写。
- Apple. File system formats available in Disk Utility[EB/OL]. [2026-04-18]. <https://support.apple.com/guide/disk-utility/file-system-formats-dsku19ed921c/mac>. APFS 和 HFS+ 默认均不区分大小写，但可在格式化时选择区分大小写变体。

## 换行符差异

回车（Carriage Return，CR）和换行（Line Feed，LF）是不同的概念，均起源于电传打字机（真实 TTY）时代。

- 回车 CR：将光标移动到当前行开头；
- 换行 LF：将光标移动到下一行。

可见，在早期二者各自独立，否则 CRLF 会使当前行“下沉”一行。

Windows 操作系统默认的文本换行符为 CRLF（即 `\r\n`，0x0D 0x0A，`^M$`），而 UNIX 默认使用 LF（即 `\n`，0x0A，`$`），Classic Mac OS 则使用 `\r`（0x0D）。

时至今日，这两种符号通常见于每行末尾。

二者互不兼容。将使用 Windows 换行符的文件置于 UNIX 系统，可能导致每行末尾多出 `^M` 字符；某些工具会因此产生识别错误，而对 FreeBSD Port 相关文件而言，则可能将多行识别为单行。

然而两种换行符可以互相转换。在 FreeBSD 下可使用 Port `converters/dos2unix` 来实现，该软件包含 2 个命令：`dos2unix`（Windows 换行符到 UNIX）、`unix2dos`（UNIX 换行符到 Windows）。基本用法是 `$ dos2unix -n a.txt b.txt`，如果不需要保留源文件，可直接 `$ dos2unix a.txt b.txt c.txt`（一次转换多个文件）。可使用命令 `file a.txt` 来判断文件的换行符类型：

- 使用普通的 UNIX 换行符文本文件

```sh
$ file a.txt  # 查看文件类型
a.txt: Unicode text, UTF-8 text
```

- 使用 Windows 换行符的文本文件

```sh
$ file b.txt  # 查看文件类型
b.txt: Unicode text, UTF-8 text, with very long lines (314), with CRLF line terminators
```

### 参考文献

- IETF. RFC 2046: Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types[EB/OL]. [2026-04-18]. <https://datatracker.ietf.org/doc/html/rfc2046>. 规定文本类型的规范行结束符为 CRLF（0x0D 0x0A）。
- IETF. RFC 20: ASCII format for network interchange[EB/OL]. [2026-04-18]. <https://www.rfc-editor.org/rfc/rfc20.html>. ASCII 字符编码标准，定义 7 位 128 个字符的编码，其中 0x41 为大写字母 A；标准定义 CR 为 0x0D（第 13 号控制字符），LF 为 0x0A（第 10 号控制字符），二者均源自电传打字机时代的物理操作。
- Wasserburger E. dos2unix / unix2dos - Text file format converters[EB/OL]. [2026-04-18]. <https://dos2unix.sourceforge.io/>. dos2unix 与 unix2dos 命令行工具，用于在 CRLF（Windows）与 LF（UNIX）换行格式之间转换；FreeBSD Port 路径为 converters/dos2unix。基本系统版本与 Port 版本为不同程序。Port 为增强版本，支持更多选项。

## 字符编码差异

计算机只识别 `0` 和 `1`，因此字符编码是将字符转换为数字表示的规则体系。字符可为屏幕上可见的文字，也可为不可见的控制标记，如换行符（LF）、回车符（CR）等，涵盖数字、Emoji 表情符号、汉字、拉丁字母等文本常见元素。编码过程即为这些字符分配唯一数字标识（通常为整数），即代码点（code point）。

例如，ASCII（American Standard Code for Information Interchange，ANSI X3.4）编码中，`0x41`（二进制 `0100 0001`）代表大写字母 `A`。ASCII 仅支持英文字母、数字和常见标点，共 128 个字符。

而在 Unicode 编码体系中，“你”这个汉字的代码点是 U+4F60。在 UTF-8（8-bit Unicode Transformation Format，8 位 Unicode 转换格式）编码方式下，其编码后为字节序列 `0xE4 0xBD 0xA0`（二进制为 `11100100 10111101 10100000`）。UTF-8 编码涵盖的字符范围远超 GBK（国标扩展），其中甚至含有埃及圣书体，如果当前屏幕上能看到 𓀀 𓃕 𓌊 这三个字符，则很可能正在使用 UTF-8 编码（若使用 UTF-8 编码但仍无法显示这些字符，很可能是字体不支持这些字符集，而非编码问题）。

程序如何识别文本编码？某些文件会在开头使用特定字节序列（即 BOM，byte order mark，字节顺序标记）标明编码。例如 UTF-8 的 BOM 是 `0xEF 0xBB 0xBF`。但许多文本文件并无 BOM，读取程序需通过上下文猜测编码格式，这往往导致乱码。虽然通过程序分析文本内容（如统计字符分布或抽取字符计算）可猜测编码，但此法未必可靠。编码问题，根本原因在于系统间默认编码不同或未明确指定编码。

Windows 默认使用 GBK（在简体中文环境下，为 GB2312 的超集），而 Linux 或 UNIX 通常使用 UTF-8。

- Windows 11 24H2 查看当前控制台代码页：

```powershell
PS C:\Users\ykla> chcp
活动代码页: 936 # GBK 编码
```

- Ubuntu 24.04/FreeBSD 输出当前区域设置（locale）的字符编码：

```sh
root@ykla:/home/ykla# locale charmap
UTF-8
```

此外，也可将 Windows 10 及后续版本的系统字符编码设置为 UTF-8。然而，如此设置往往只会引入更多编码问题，无助于解决问题。

FreeBSD 的编码在 [main/usr.bin/login/login.conf](https://github.com/freebsd/freebsd-src/blob/main/usr.bin/login/login.conf) 文件中设置，编译后路径为 **/etc/login.conf**。

### 参考文献

- 微软. Code pages[EB/OL]. [2026-03-26]. <https://learn.microsoft.com/en-us/globalization/encoding/code-pages>. 微软官方称，936 即是 GBK，用于中文简体字符编码；代码页 936 最初覆盖 GB 2312 字符集，后扩展为 GBK。
- Unicode Consortium. UTF-8, UTF-16, UTF-32 BOM[EB/OL]. [2026-04-18]. <https://www.unicode.org/faq/utf_bom.html>. UTF-8 的 BOM 为字节序列 0xEF 0xBB 0xBF。
- 微软. Use UTF-8 code pages in Windows apps[EB/OL]. [2026-04-18]. <https://learn.microsoft.com/en-us/windows/apps/design/globalizing/use-utf8-code-page>. Windows 10 及后续版本可通过系统区域设置启用 UTF-8 支持（Beta 功能），但可能导致旧应用程序兼容性问题。
- FreeBSD Project. login.conf(5)[EB/OL]. [2026-04-18]. <https://man.freebsd.org/cgi/man.cgi?query=login.conf&sektion=5>. FreeBSD 登录类能力数据库，源文件位于 `usr.bin/login/login.conf`，编译后路径为 **/etc/login.conf**，用于设置字符编码等用户环境。

## 时间与时区差异

中国统一使用东八区，即 UTC+8。UTC（Coordinated Universal Time，协调世界时）在日常使用中与 GMT（Greenwich Mean Time，格林尼治时间）几乎等同。UTC 以国际原子时（temps atomique international，TAI）的秒长为基础（二者并不完全一致）：取铯（Cs）频率 ΔνCs——即铯 133 原子不受干扰的基态超精细跃迁频率——以 Hz（s⁻¹）表示时的固定数值 9,192,631,770 定义秒，此后又对国际原子时进行了多项修正。

有过 Windows 和 UNIX 双系统安装经验的用户会发现，Windows 和 UNIX 的时间总相差 8 小时。现代计算机主板通常配备一颗由纽扣电池供电的 RTC（Real-time clock，实时时钟芯片），用于在系统断电后维持计时。

计算机操作系统开机时读取 RTC 时间以设定系统时间。RTC 时间未标注时区。

Windows 直接读取 RTC 的值，并视为本地时间（Local Time，地方时）；UNIX 则将 RTC 数据视为 UTC 时间，双系统时间由此相差 8 小时。

例如，设 RTC 时间为 2025 年 6 月 6 日中午 12:00（UTC+8）。Windows 下显示为 2025 年 6 月 6 日中午 12:00（UTC+8）；UNIX 下则显示为 2025 年 6 月 6 日晚上 20:00——原因在于 UNIX 将 RTC 中的 12:00 视为 UTC，加上 UTC+8 偏移量后得 12+8=20。由于 UNIX 将 RTC 视为 UTC 而非本地时间，其显示时间比 Windows 快 8 小时。

对于现代计算机网络来说，时间准确性至关重要，通过一个简单实验可验证：将时间调慢 5 分钟，打开浏览器，即可发现绝大部分网站无法访问（HTTPS）。

计算机中的时区是由 IANA 时区数据库规范的，历史悠久。

中华民国二十八年（1939），民国政府将中国划分为五个时区，当时称为长白时区（UTC+8:30）、中原标准时区（UTC+8）、陇蜀时区（UTC+7）、新藏时区（UTC+6）和昆仑时区（UTC+5:30）。在 IANA 时区数据库中，这些时区分别对应 `Asia/Harbin`、`Asia/Shanghai`、`Asia/Chongqing`、`Asia/Urumqi` 和 `Asia/Kashgar`。

从实际地理时区看，新疆属于东六区（虽全国统一使用北京时间）。北京地区若在北京时间五点日出，新疆则要到北京时间七点方见日出。

在时区数据库 2025b 中，`Asia/Harbin`、`Asia/Chongqing`、`Asia/Shanghai` 均等同于北京时间。`Asia/Urumqi` 和 `Asia/Kashgar` 则均为 `UTC+6`（东六区时间）。

在 FreeBSD 中，北京时间同样为 `Asia/Shanghai`（东八区）。部分国产操作系统自行定义 `Asia/Beijing` 时区，此举不符合国际标准与规范，可能造成严重后果——例如导致时间回退至 UTC。

> **注意**
>
> 北京（东经 116°）的地方时并不完全等于 UTC+8。北京时间不是北京的地方时，而是东经 120 度（上海东经 120°）的地方时。

> **技巧**
>
> 中国也曾实行过夏令时（在夏季将时钟调快一个小时，因夏季日出较早）。

> **思考题**
>
> 外太空（飞船，星球等）用什么时区？为什么？

### 参考文献

- 中国计量科学研究院. 秒的定义[EB/OL]. [2026-03-26]. <https://www.nim.ac.cn/520/node/4.html>. 秒的定义，基于铯原子超精细跃迁频率。
- BIPM. SI base unit: second[EB/OL]. [2026-04-18]. <https://www.bipm.org/en/si-base-units/second>. 国际计量局秒的 SI 定义，铯 133 原子不受干扰的基态超精细跃迁频率取固定数值 9,192,631,770 Hz。
- IANA. Time Zone Database[EB/OL]. [2026-03-26]. <https://www.iana.org/time-zones>. 时区数据库，提供全球时区信息标准化。
- IANA. tzdata release 2025b NEWS[EB/OL]. [2026-04-18]. <https://data.iana.org/time-zones/tzdb-2025b/NEWS>. 时区数据库 2025b 版本变更说明，Asia/Urumqi 的 1980 年向 UTC+8 的转换已被移除，现为 UTC+6；Asia/Kashgar 为 Asia/Urumqi 的向后兼容链接。
- 微软. Why does Windows keep your BIOS clock on local time?[EB/OL]. [2026-04-18]. <https://devblogs.microsoft.com/oldnewthing/20040902-00/?p=37983>. Windows 默认将硬件时钟（RTC）视为本地时间而非 UTC 的历史原因。
- 中国科学院紫金山天文台. 历书基本术语简介[EB/OL]. [2026-03-26]. <http://www.pmo.cas.cn/xwdt2019/kpdt2019/202203/t20220314_6389637.html#b4>. 本节所涉术语，可参考此处的精确解释。
- 新华网. “北京时间”是怎么来的[EB/OL]. [2026-04-18]. <http://www.xinhuanet.com/politics/2015-10/28/c_1116958394.htm>. 北京时间并非北京（东经 116.4°）地方时，而是东经 120° 经线的区时；中国曾于 1986—1991 年实行夏令时。
- IETF. RFC 5246: The Transport Layer Security (TLS) Protocol Version 1.2[EB/OL]. [2026-04-18]. <https://www.rfc-editor.org/rfc/rfc5246>. TLS 协议规定证书包含 notBefore 与 notAfter 有效期字段，客户端验证时将系统时间与证书有效期比对，时钟偏移可导致握手失败。
- IETF. RFC 6557: Procedures for Maintaining the Time Zone Database[EB/OL]. [2026-04-18]. <https://www.rfc-editor.org/rfc/rfc6557>. IANA 时区数据库维护程序（BCP 175），该数据库自 20 世纪 70 年代末由 Arthur David Olson 开发，2011 年起由 IANA 维护。

## 深入阅读

### Windows

以下书籍可供读者进一步研究 Windows 操作系统设计与实现：

- Russinovich M, Solomon D, Ionescu A, 等. 深入解析 Windows 操作系统：第7版. 卷1[M]. 刘晖，译. 北京：人民邮电出版社，2021. ISBN: 978-7-115-55694-3. 微软官方教材，系统阐述 Windows 内核架构。
- Russinovich M, Solomon D, Ionescu A, 等. 深入解析 Windows 操作系统：第7版. 卷2[M]. 刘晖，译. 北京：人民邮电出版社，2024. ISBN: 978-7-115-61974-7. 微软官方教材，详解 Windows 系统组件。

### 天文历法

- 中国科学院紫金山天文台. 2026 年中国天文年历[M]. 北京：科学出版社，2025. ISBN: 978-7-03-082584-1. 注：每年一版。一般日历会写潮起潮落太阳东升西落的时间，该书则是大全，提供精确的天文数据。
- 胡中为. 天文学教程（上）[M]. 上海：上海交通大学出版社，2019. ISBN: 978-7-3132-1655-7. 天文学历史悠久，这是本现代天文学入门书籍，本科生教材，系统介绍天文学基础。
- 胡中为. 天文学教程（下）[M]. 上海：上海交通大学出版社，2020. ISBN: 978-7-3132-3572-5. 天文学是一级学科，深入讲解天体物理与宇宙学。
- Dodelson S, Schmidt F. 现代宇宙学[M]. 于浩然，译. 第2版. 北京：科学出版社，2024. ISBN: 978-7-03-078693-7. 该书用数学和物理学描述宇宙宏观整体而非具体天体行星，提供现代宇宙学理论框架。
- 卢央. 中国古代星占学[M]. 北京：中国科学技术出版社，2013. ISBN: 978-7-5046-6140-1. 中国古代天文学入门，星占学即用哲学或神秘学解释天文学，梳理古代星占文化。
- Carroll B W, Ostlie D A. 当代天体物理学导论[M]. 姜碧沩，李庆康，高健，等，译. 第2版. 北京：科学出版社，2023. ISBN: 978-7-03-076666-3. 天体物理学即用物理学解释天文学，是现代天文学的核心（还有一些测量、分类、天文历法等不属于此范畴），提供天体物理系统介绍。

> **思考题**
>
>> 对于描述世界，我们有太多种方法。正如马克思所述，“哲学家们只是用不同的方式解释世界……”（《关于费尔巴哈的提纲》第十一条：马克思主义哲学的使命）
>
> 你认为通过数学和物理学解释世界的优点是什么？如果排除实用主义、实证主义和经验主义，那么还能剩下什么？
>
> 你认为通过哲学和神秘学/宗教神学解释世界的缺点是什么？如果排除实用主义和经验主义，那么还能剩下什么？
>
>>马克思还认为只有必要的自由时间才能确保真正的自由（邓晓芒. 马克思论“存在与时间”[J]. 哲学动态，2000(6): 11-14）：
>>
>>“必须将感性的时间从强制性的、社会一般的抽象时间中解放出来。”
>>
>>“实践也不能被曲解为异化了的生产活动，即类似于动物性的筋肉活动、体力的支出，至少不能将异化劳动当作马克思本来意义上的实践活动。”
>
> 你怎样理解这样一个事实：我们 **显然拥有充足的** 自由时间，但是我们仍然 **无法拥有** 所谓的 **“自由”时间** 去了解一些“无意义”的东西（非学术目的），比如天文学？
>
> 我们在不断地刷短视频阅读网络小说所花费的精力，是否在某种程度上也构成了 **生产活动**？所花费的时间是否在某种意义上构成了 **社会一般（平均）劳动时间**？换言之，这种自由时间的放松，究竟是真正的自由还是一种资本化的假象（实际上仍是另一种形式的工作）？这种自由时间往往被视为对工作的放松，是为了更好地工作，而非单纯实现自由时间；并且我们通过平台获取的快乐和 **工资** 远低于平台从用户获取的算法，个性化数据，内容主体，广告等带来的价值。你如何看待这种对自由时间的资本化异化？

## 课后习题

1. 在 FreeBSD 中挂载一个 Windows NTFS 分区，使用 `converters/dos2unix` 批量转换包含 Windows 换行符的文本文件，编写 shell 脚本实现自动化处理。
2. 查阅 FreeBSD 内核源代码中 UFS/ZFS 文件系统处理大小写敏感的逻辑，分析其实现机制与 Windows NTFS 大小写不敏感设计的差异。
3. 修改 Windows 注册表使其将硬件时钟视为 UTC，记录修改前后 FreeBSD 与 Windows 双系统时间显示的差异。
