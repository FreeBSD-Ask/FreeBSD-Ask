# 2.4 将 U 盘启动盘恢复为普通 U 盘（基于 Windows）

>**警告**
>
>本文所述操作具有高风险性，可能会损坏部分或全部的数据。除非你已经明确可接受的最坏结果、做好完整可验证的备份、并有可用的回滚方案，否则不要执行。你已经被警告过了。
>
>如果你无力解决，可以尝试在电商平台购买有偿服务来解决。

当使用 Rufus、win32diskimager 等软件制作了 U 盘启动盘用于安装系统后，你会发现 U 盘的可见容量可能只有 31.9 MB（即 EFI）。

![使用 Rufus 制作的 U 盘启动盘](../.gitbook/assets/usb-efi.png)

这是一款 64G 的 U 盘，因此我们往往需要恢复还原 U 盘。

## 使用 diskgenius 恢复 U 盘启动盘

DiskGenius 官网：<https://www.diskgenius.cn/>，该软件有收费功能，但是免费功能已足够用。

### 下载 DiskGenius

在下载时，大部分人应该 [下载](https://www.diskgenius.cn/download.php) 64 位。

下载后，发现是个 zip 压缩包。

![下载的 DiskGenius](../.gitbook/assets/usb-diskgenius.png)

需要在桌面新建文件夹 `1`（即 `C:\Users\ykla\Desktop\1`），全选压缩包内所有文件，提取至新建的文件夹 `1`（即 `C:\Users\ykla\Desktop\1\DiskGenius`）。

![下载的 DiskGenius](../.gitbook/assets/usb-diskgenius2.png)

验证结果：

![验证 DiskGenius 解压结果](../.gitbook/assets/usb-diskgenius3.png)

### 启动 DiskGenius

启动 DiskGenius，需要点击 `DiskGenius.exe`（即 `C:\Users\ykla\Desktop\1\DiskGenius\DiskGenius.exe`，你那里可能是 `DiskGenius`）才能启动。

![DiskGenius](../.gitbook/assets/usb-diskgenius4.png)

同意许可证：

![DiskGenius](../.gitbook/assets/usb-diskgenius5.png)

### 判断哪个是 U 盘

判断哪个是你的 U 盘，一般我们可以通过 U 盘容量来判断。如果你不记得自己的 U 盘容量，可以查询你的购买记录或拔下来 U 盘看一下，上面一般有标记。

- 通过容量判断：64G U 盘一般在 Windows/Linux 中显示为 58G（macOS 中为 64G）。
- 通过盘符判断：在下图中，你也可以通过“EFISYS(E:)”来判断（E 盘），这就是使用 Rufus 制作的 U 盘启动盘。
- 通过 DiskGenius 显示的接口判断：在下图中，你从顶部的“硬盘 1 接口:USB”中的“USB”也可以看出这是 USB 设备，即可能是 U 盘。

![DiskGenius](../.gitbook/assets/usb-diskgenius6.png)

### 恢复 U 盘

在确认了哪个是 U 盘后，右键单击，选中“删除所有分区”。

![DiskGenius](../.gitbook/assets/usb-diskgenius7.png)

在确认后才选择“是”。

![DiskGenius](../.gitbook/assets/usb-diskgenius8.png)

删除后的 U 盘状态：

![DiskGenius](../.gitbook/assets/usb-diskgenius9.png)

鼠标放到顶部空白区，右键单击，点击“建立新分区”。


![DiskGenius](../.gitbook/assets/usb-diskgenius10.png)

设置如下：文件系统我们选择 `exFAT`（具有通用性，一般操作系统都能读写，且不存在单文件不能大于 4GB 的限制），底下选择对齐到 4096 扇区（4K 对齐）。

![DiskGenius](../.gitbook/assets/usb-diskgenius11.png)

点击左上角的“保存更改”。

![DiskGenius](../.gitbook/assets/usb-diskgenius12.png)

在确认后才选择“是”。

![DiskGenius](../.gitbook/assets/usb-diskgenius13.png)

在确认后才选择“是”。

![DiskGenius](../.gitbook/assets/usb-diskgenius14.png)

最后结果：

![DiskGenius](../.gitbook/assets/usb-diskgenius15.png)

打开资源管理器：

![DiskGenius](../.gitbook/assets/usb-diskgenius16.png)

恢复完成。


## 使用傲梅分区助手恢复 U 盘启动盘

使用思路基本同上。

### 下载安装傲梅分区助手

傲梅分区助手官网：<https://www.disktool.cn/>

我们 [下载](https://www.disktool.cn/download.html)“绿色版”（免安装，可直接运行）。我们需要花点时间找到“PartAssist.exe”（你那里可能是 `PartAssist`）。右键单击，点击打开。

![傲梅分区助手](../.gitbook/assets/aomei1.png)

>**技巧**
>
>专业版会提示需要使用码，但是 **无需** 关注其微信公众号，在使用码框中填入数字“1122”即可。参见 [傲梅分区助手常见问题解答](https://www.disktool.cn/faq/partition-assistant.html)，“分区助手使用码：1122”。
>
>![傲梅分区助手专业版使用码](../.gitbook/assets/aomei2.png)

### 判断 U 盘设备

你可以通过以下信息判断是否是 U 盘（看不见的话，用鼠标往下滑）：

![傲梅分区助手](../.gitbook/assets/aomei3.png)

打开“属性与健康”：

![傲梅分区助手](../.gitbook/assets/aomei4.png)

观察接口：

![傲梅分区助手](../.gitbook/assets/aomei5.png)

### 还原 U 盘启动盘

#### 删除所有分区

选中 U 盘设备，右键单击“删除所有分区”

![傲梅分区助手](../.gitbook/assets/aomei6.png)

“删除所有分区”，在确认后点击“确定”

![傲梅分区助手](../.gitbook/assets/aomei7.png)

然后显示如下，点击左上角“提交”，确认上述修改。

![傲梅分区助手](../.gitbook/assets/aomei8.png)

点击“执行”

![傲梅分区助手](../.gitbook/assets/aomei9.png)

确认。

![傲梅分区助手](../.gitbook/assets/aomei9-1.png)

分区删除完毕。

![傲梅分区助手](../.gitbook/assets/aomei10.png)


#### 创建新分区

点击底部的 U 盘，右键单击，选择“创建分区”

![傲梅分区助手](../.gitbook/assets/aomei11.png)

将文件系统改为“exFAT”，确定，

![傲梅分区助手](../.gitbook/assets/aomei12.png)

然后点击左上角的提交。

![傲梅分区助手](../.gitbook/assets/aomei13.png)

进一步确认：

![傲梅分区助手](../.gitbook/assets/aomei14.png)

执行：

![傲梅分区助手](../.gitbook/assets/aomei15.png)


可以看到，已经自动分配了盘符“E”，现在 U 盘是 E 盘。

![傲梅分区助手](../.gitbook/assets/aomei16.png)

## 通过命令 diskpart 恢复

打开 powershell：右键单击 Windows 图标，选中 Windows PowerShell（管理员）。

### MBR 分区表

```powershell
PS C:\WINDOWS\system32> diskpart # 进入 diskpart

Microsoft DiskPart 版本 10.0.26100.1150

Copyright (C) Microsoft Corporation.
在计算机上: DESKTOP-M5P610N

DISKPART> list disk # 列出所有磁盘，下图磁盘 1 没有 Gpt 标识，代表这可能是 MBR 分区表的磁盘

  磁盘 ###  状态           大小     可用     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  磁盘 0    联机              931 GB    41 MB        *
  磁盘 1    联机               57 GB  5120 KB

DISKPART> sel disk 1 # 选中磁盘 1

磁盘 1 现在是所选磁盘。

DISKPART> clean # 清除磁盘 1 所有分区

DiskPart 成功地清除了磁盘。 

DISKPART> cre part pri # 在磁盘 1 创建主分区

DiskPart 成功地创建了指定分区。

DISKPART> list part # 列出磁盘 1 的所有主分区

  分区 ###       类型              大小     偏移量
  -------------  ----------------  -------  -------
* 分区      1    主要                  57 GB  1024 KB

DISKPART> sel part 1 # 选中主分区 1

分区 1 现在是所选分区。

DISKPART> for fs=exfat quick # 快速将主分区 1 格式化为 exfat

  100 百分比已完成

DiskPart 成功格式化该卷。

DISKPART> active # 设置主分区 1 为活动分区

DiskPart 将当前分区标为活动。

DISKPART> ass letter=E # 挂载到 E 盘，你也可以拔出来再插进去

DiskPart 成功地分配了驱动器号或装载点。
```

### GPT 分区表


```powershell
PS C:\WINDOWS\system32> diskpart

Microsoft DiskPart 版本 10.0.26100.1150

Copyright (C) Microsoft Corporation.
在计算机上: DESKTOP-M5P610N

DISKPART> list disk # 列出磁盘

  磁盘 ###  状态           大小     可用     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  磁盘 0    联机              931 GB    41 MB        *
  磁盘 1    联机               57 GB      0 B

DISKPART> sel disk 1 # 选中磁盘 1

磁盘 1 现在是所选磁盘。

DISKPART> list disk # 当前选中的磁盘前会有标记 *

  磁盘 ###  状态           大小     可用     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  磁盘 0    联机              931 GB    41 MB        *
* 磁盘 1    联机               57 GB      0 B


DISKPART> clean # 清空磁盘

DiskPart 成功地清除了磁盘。

DISKPART> con gpt # 将磁盘转为 GPT 分区表
 
DiskPart 已将所选磁盘成功地转更换为 GPT 格式。

DISKPART> list disk # 列出所有磁盘

  磁盘 ###  状态           大小     可用     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  磁盘 0    联机              931 GB    41 MB        *
* 磁盘 1    联机               57 GB    57 GB        *

DISKPART> cre part pri # 创建主分区

DiskPart 成功地创建了指定分区。

DISKPART> list par # 列出磁盘 1 的所有分区

  分区 ###       类型              大小     偏移量
  -------------  ----------------  -------  -------
* 分区      1    主要                  57 GB  1024 KB

DISKPART> for fs=exfat quick # 快速格式化磁盘 1 的分区 1 为 exfat

  100 百分比已完成

DiskPart 成功格式化该卷。

DISKPART> ass letter=E # 将 U 盘分配到 E 盘符

DiskPart 成功地分配了驱动器号或装载点。
```


