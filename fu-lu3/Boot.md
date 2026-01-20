# Boot（启动）


![](../.gitbook/assets/image-20250726132126-uafgj13.png)

## Setup Prompt Timeout（设置 Setup 提示超时时间）

值：

0–65535 秒

说明：

Setup 提示超时设置，用于设置等待 Setup 激活键的时间，最大值为 65535 秒，表示无限等待。

## Bootup NumLock State（启动时 NumLock 状态）

选项：

On（开）

Off（关）

说明：

选择键盘 NumLock 状态（锁定或解锁数字小键盘）。设备启动后，可将数字小键盘设置为开启（On，用于数字输入）或关闭（Off，用于导航功能）。导航功能指通过数字键实现界面上下左右移动。

## Quiet Boot（静默启动）

选项：

Enabled（启用）

Disabled（禁用）

说明：

用于设置是否启用静默启动模式。

设置为 Enabled 时，开机将显示制造商提供的 Logo；设置为 Disabled 时，开机画面为文本模式的 POST 界面。在自检（POST）期间，启用（Enabled）时显示启动徽标，禁用（Disabled）时以文本模式显示启动信息。

## Fast Boot（快速启动）

选项：

Enabled（启用）

Disabled（禁用）

说明：

用于启用或禁用在启动过程中仅初始化启动活动选项所需的最小设备集合。该设置对 BBS 启动选项（非 UEFI 启动选项）无效。如果使用外置显卡，则其 VBIOS 需要支持 UEFI GOP。

警告：开启此选项后可能无法再次进入 BIOS，因为启用快速启动后，系统在启动阶段会忽略所有 USB 设备（如键盘）。通常可通过重置 CMOS，或使用 Windows 的高级启动功能进入 UEFI 固件设置。参见 [Windows 11/10 如何进入 BIOS 设置界面](https://www.asus.com.cn/support/faq/1008829/) [备份](https://web.archive.org/web/20260119181725/https://www.asus.com.cn/support/faq/1008829/)。需要注意的是，此方法并非对所有主板均有效，部分主板仍无法通过该方式进入 BIOS。

## SATA Support（SATA 支持）

选项：

Last Boot SATA Devices Only（仅最后启动的 SATA 设备）

All SATA Devices（全部 SATA 设备）

说明：

如果选择“仅最后启动的 SATA 设备”，则在 POST 过程中仅检测并显示上一次启动时使用的 SATA 设备。

如果选择“全部 SATA 设备”，则所有 SATA 设备都会在 POST 过程中被检测，并在操作系统中可用。

## NVMe Support（NVMe 支持）

选项：

Enabled（启用）

Disabled（禁用）

说明：

若禁用，NVMe 设备将被跳过。M.2 固态硬盘通常使用该协议。

## USB Support（USB 支持）

选项：

Disabled（禁用）

Full Initial（完全初始化）

Partial Initial（部分初始化）

说明：

如果禁用，所有 USB 设备（包括键盘、鼠标等）在操作系统启动前均不可用。

>**警告**
>
>在部分机器上，该选项一旦关闭可能无法再次启用，具体请参考 BIOS 右上角的提示信息。由于现代设备通常不再提供 PS/2 接口，可能会导致系统无法正常操作。

如果选择部分初始化，则 USB 大容量存储设备（如 U 盘）以及部分 USB 端口或设备在操作系统启动前不可用。

如果启用，所有 USB 设备在操作系统和启动自检（POST）过程中均可用。

## PS2 Devices Support（PS/2 设备支持）

选项：

Enabled（启用）

Disabled（禁用）

说明：

若禁用，PS/2 设备将被跳过。较早期的鼠标、键盘或摇杆设备使用该协议，该接口大约在 2009 年前后逐渐被淘汰。现代设备通常不再提供 PS/2 接口，因此该选项在多数情况下意义不大。

## Network Stack Driver Support（网络协议栈驱动支持）

选项：

Enabled（启用）

Disabled（禁用）

说明：

该功能为 PXE 启动所必需。若禁用，网络协议栈驱动将被跳过。

## Redirection Support（重定向支持）

选项：

Enabled（启用）

Disabled（禁用）

说明：

若禁用，重定向功能将被跳过。

## Boot Option #1（启动选项 1）

选项：

Hard Disk0（硬盘 0）

Hard Disk1（硬盘 1）

eMMC（嵌入式 eMMC）

CD/DVD（光学介质/光盘）

SD（存储卡）

USB Device（USB 设备，如 U 盘）

Network（网络启动）

Other Device（其他设备）

Disabled（禁用）

说明：

用于设置系统的启动顺序。

## Boot Option #2（启动选项 2）

同上。

## Boot Option #3（启动选项 3）

同上。

## Boot Option #4（启动选项 4）

同上。

## Boot Option #5（启动选项 5）

同上。

## Boot Option #6（启动选项 6）

同上。

## Boot Option #7（启动选项 7）

同上。

## Boot Option #8（启动选项 8）

同上。

## Boot Option #9（启动选项 9）

同上。

## UEFI EMMC Drive BBS Priorities（UEFI EMMC 驱动 BBS 优先级）

用于指定来自可用 UEFI eMMC 设备的启动优先顺序。

## UEFI SD Drive BBS Priorities（UEFI SD 驱动 BBS 优先级）

指定来自可用 UEFI SD 驱动的启动设备优先顺序。
