# 3.11 配置 rEFInd（双系统用）

在 BIOS 来回切换确实很麻烦，我们可以借助 [rEFInd](https://www.rodsbooks.com/refind/) 实现类似 Clover 的效果，在开机时选择我们要进入的操作系统。

`rEFInd` 复刻自 `rEFIt`，源自对“refind”（改进、完美）和“EFI”（Extensible Firmware Interface，可扩展固件接口）两个词的组合，即修改 UEFI。

打开下载页面 [Getting rEFInd from Sourceforge](https://www.rodsbooks.com/refind/getting.html)，点击 `A binary zip file` 即可自动开始下载。写作本文使用到了 `refind-bin-0.14.2.zip`。

该文件中只有一部分是有用的启动文件。我们只需要其中的 `refind` 文件夹，其他的不需要。

在 `refind` 文件夹中只有一部分是有用的启动文件。所有带 `aa64`、`ia32` 字样的均可删除。

所有用到的文件如下图所示。

![](../.gitbook/assets/shuang12.png)

我们将 `refind.conf-sample` 复制一份，并重命名为 `refind.conf`。


>**技巧**
>
>一般来说无需手动配置。但事有例外，若无法识别现有的操作系统，请按以下方法操作：
>
>打开 `refind.conf`，在任意空白行加入：
>
>```ini
>menuentry "FreeBSD" { 
>	icon \EFI\refind\icons\os_freebsd.png 
>	volume "FreeBSD"
>	loader \EFI\freebsd\loader.efi 
>}
>
>menuentry "Windows 10" { 
>	icon \EFI\refind\icons\os_win.png
>	volume "Windows 10"  
>	loader \EFI\Microsoft\Boot\bootmgfw.efi 
>}
>```

使用 [diskgenius](https://www.diskgenius.com/) 将 `refind` 文件夹复制到 EFI 文件系统下的 efi 文件夹下。

![](../.gitbook/assets/shaung13.png)

## 添加启动项

使用 [diskgenius](https://www.diskgenius.com/) 创建启动项。

![](../.gitbook/assets/shuang14.png)

点击“工具”——"设置 UEFI BIOS 启动项"。

![](../.gitbook/assets/shuang15.png)

点击“添加”。选中“refind_x64.efi”。

![](../.gitbook/assets/shaung16.png)

将其移动至顶部，设置为第一启动项。重启后测试效果。

![](../.gitbook/assets/shuang16-2.png)

![](../.gitbook/assets/shuang17.png)


两个选项都能进入。

## 附录：rEFInd 主题

rEFInd 有多款主题可选。

本例采用 Matrix-rEFInd（电影《黑客帝国》）进行说明。

项目地址：[Matrix-rEFInd](https://github.com/Yannis4444/Matrix-rEFInd/)

将项目下载下来解压缩 `Matrix-rEFInd-master.zip`。将解压出的文件夹 `Matrix-rEFInd-master` 重命名为 `Matrix-rEFInd`。

再新建目录 `themes`，将 `Matrix-rEFInd` 放到 `themes` 里面。

将 `themes` 复制到 EFI 分区的 efi 文件夹下的 `refind` 文件夹中。

再编辑 `refind.conf`（无法直接编辑可先复制到桌面，编辑后再覆盖回去），在此文件的最后一行加入 `include themes/Matrix-rEFInd/theme.conf`。

重启：

![](../.gitbook/assets/shuang18.jpg)

>**技巧**
>
>如果你在虚拟机复现本实验，受制于虚拟机（VMware、VirtualBox）的 UEFI 屏幕分辨率，你可能只能看到一个操作系统，可通过按钮切换而非上图中的两个。物理机是正常的。
