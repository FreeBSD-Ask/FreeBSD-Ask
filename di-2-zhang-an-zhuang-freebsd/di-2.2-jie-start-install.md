# 2.2 使用 bsdinstall 开始安装

>**技巧**
>
>视频教程见 [FreeBSD 14.2 基础安装配置教程](https://www.bilibili.com/video/BV1STExzEEhh)（物理机）、[002-VMware17 安装 FreeBSD14.2](https://www.bilibili.com/video/BV1gji2YLEoC)（虚拟机）。

---

以下安装说明基于 `FreeBSD-14.2-RELEASE-amd64-disc1.iso`。`-dvd1.iso` 和 `-memstick.img` 大同小异。

>**警告**
>
>本文基于 VMware 17 进行演示（使用 UEFI）。
>
>若是物理机，请考虑使用 [rufus](https://rufus.ie/zh/) + [img 镜像](https://download.freebsd.org/ftp/releases/ISO-IMAGES/14.1/FreeBSD-14.1-RELEASE-amd64-memstick.img)。


> **警告**
>
> 如果要在 VMware 虚拟机使用 UEFI，必须使用 FreeBSD 13.0-RELEASE 及以上，否则启动会花屏。

## 启动安装盘

![](../.gitbook/assets/ins1.png)

此界面无需任何操作，等待十秒，可自动进入 `1. Boot Installer [Enter]`；亦可以直接按 **回车键** 进入。

按 **空格键** 可暂停，可选定以下选项。

>**技巧**
>
>如果按其他任意键盘会进入提示符 `OK`，可输入 `menu` 再按 **回车键** 返回菜单。

以下操作：按最开头的数字可进行选定。`on` 代表已开启，`off` 代表已关闭。

|     选项     |                                   解释                                    |
| :----------: | :----------------------------------------------------------------------- |
|`1. Boot Installer [Enter]`|用于安装系统|
| `2. Boot Single user` |  单用户模式，找回 root 密码和修复磁盘时会用到 |
|  `3.Escape to loader prompt`   |           离开菜单，进入命令模式，进入后输入 `reboot` 回车可重启                                |
| `4.Reboot`  |        重启                      |
|  `5. Cons: Video`    |    选择输出模式：视频（`Video`）、串口（`Serial`）、同时输出，但串口优先（`Dual (Serial primary)`、同时输出，但视频优先（`Dual (Video primary)` 可选）                         |
|`6. Lernel: default/kernal (1 of 1)`|选择要启动的内核|

![](../.gitbook/assets/ins2.png)

|**`7. Boot Options`**|启动参数|
| :----------: | :----------------------------------------------------------------------- |
|`1. Back to main menu [Backspace]`|按 **删除键** 可返回上级菜单 |
|`2. Load System Defaults`|恢复默认配置|
|`3. ACPI`|高级配置和电源接口|
|`4. Safe Mode`|安全模式|
|`5. Single user`|单用户模式|
|`6. Verbose`|啰嗦模式，增加更多调试信息输出|


![](../.gitbook/assets/ins3.png)

欢迎菜单。

`欢迎使用 FreeBSD！你想要开始安装还是使用 Live 系统？`

选中 `install`，按下 **回车键** 可进行安装。中间 `Shell` 是命令行，左右侧 `Live System` 是 LiveCD 模式。

>**技巧**
>
>以下若无特别说明，按 **TAB 键** 或者 **方向键** 可选择不同条目；按 **回车键** 可以选定高亮条目；

>**技巧**
>
>注意观察图片中的红色加粗大写首字母，如 `Install`、`Shell` 和 `Live System` 中的 **`I`**、**`S`**、**`L`** 分别是红色加粗大写的。若你直接按键盘上面的对应按键（无论大小写），均会选定并直接进入该界面。


>**警告**
>
>无论在任何步骤，按 **ESC 键** 均 **不能** 返回上一菜单，都会直接跳到下一步直至退出安装或结束安装。
