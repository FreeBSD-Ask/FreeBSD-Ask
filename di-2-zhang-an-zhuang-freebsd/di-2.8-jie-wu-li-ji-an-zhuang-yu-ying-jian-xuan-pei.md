# 第 2.8 节 物理机安装与硬件选配

## 物理机安装

### 我该下载哪个镜像？

> **警告**
>
> **请不要** 问我在安装中应该选用哪个镜像站这类问题，那是因为你的错误操作导致的。
>
> **不要** 选用带有`bootonly`字样的镜像文件，除非你真的知道自己在干什么。
>
> **也不要** 不看图文教程就全选所有的组件，要按照前文教程进行选择。

使用 **U 盘** 安装应该选用 `img` 结尾的镜像，例如

[FreeBSD-13.2-RELEASE-amd64-memstick.img](https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/13.2/FreeBSD-13.2-RELEASE-amd64-memstick.img)

只有当使用 **光盘/虚拟机** 安装时才应选用 `iso` 结尾的镜像。

**FreeBSD 所有安装介质包括不限于虚拟机文件都没有提供图形界面，均需要自行安装。**

> **注意**
>
> 如果要在 VMware 虚拟机使用 UEFI，必须使用 FreeBSD 13.0-RELEASE 及以上，否则启动会花屏。

### 我该如何刻录 FreeBSD 镜像到 U 盘？

刻录工具 Windows 应该选用 **Rufus**，Linux 直接使用 `dd`命令即可。

rufus 下载地址：<https://rufus.ie/zh>

> **警告**
>
> **不建议** 使用 FreeBSD 手册推荐的 win32diskimager，有时会出现校验码错误的情况（实际上文件校验码正常）。
>
> **严禁** 使用 Ventoy 引导实体机安装，有时会报错找不到安装文件。
>
> 请 **老老实实用 rufus。**

## 怎么看我的硬件支持不支持呢？

更多硬件请参考：

[**https://bsd-hardware.info/?d=FreeBSD**](https://bsd-hardware.info/?d=FreeBSD)

<figure><img src="../.gitbook/assets/h1.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/h2.png" alt=""><figcaption></figcaption></figure>

> 如果你也想上传你的数据到该网站上，请：
>
> ```
> # pkg install hw-probe
> # hw-probe -all -upload
> ```
>
> 其他系统见 <https://github.com/linuxhw/hw-probe/blob/master/INSTALL.BSD.md>

### 网卡推荐

> **警告**
>
> 千兆和 2.5G 网卡 **似乎都有时断时续的故障。** 如果你有更好的推荐（稳定不掉网）请联系我们。

|      类型       |                品牌/型号                 |     芯片组/参数      | 售价（¥） |
| :-------------: | :--------------------------------------: | :------------------: | :-------: |
|  USB 无线网卡   |            COMFAST CF-WU810N             | RTL8188EUS 150M 2.4G |    20     |
|  USB 以太网卡   |         绿联 USB 百兆网卡 CR110          |    AX88772A 100M     |    40     |
|  USB 以太网卡   | 绿联 USB 千兆网卡 CM209【\* 不建议购入】 |    AX88179A 1000M    |    79     |
|  USB 以太网卡   |         绿联 USB 2.5G 网卡 CM275         |     RTL8156 2.5G     |    189    |
| Type-C 以太网卡 |       绿联 Type-C 转百兆网卡 30287       |    AX88772A 100M     |    59     |
| Type-C 以太网卡 |       绿联 Type-C 转千兆网卡 CM199       |    AX88179A 1000M    |    99     |
| Type-C 以太网卡 |         绿联 Type-C 转 2.5G 网卡         |     RTL8156 2.5G     |    199    |

> RTL8156 网卡如果时断时续，请安装 `realtek-re-kmod` ？（此处存疑） 见
>
> - [https://www.freshports.org/net/realtek-re-kmod](https://www.freshports.org/net/realtek-re-kmod)
> - [https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=166724](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=166724)

> \* 绿联 USB 千兆网卡 CM209 时断时续。不建议购买：
>
> - <https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=267514>

## 归档内容

1. 小米笔记本 12.5 一代 ：处理器 6Y30 、显卡 HD515 、WIFI intel 8260AC、声卡 ALC 233（实际上是 235）、硬盘 NVME INTEL 600P。
2. 联想 G400 ：处理器 i3-3110M/i5-3230M、显卡 HD4000、WIFI intel N135（联想 G400 网卡白名单支持三种网卡，如果是博通 BCM43142 建议更换为 N135，FUR 料号：04W3783，如果更换后提示不能读取，请先在 BIOS 里停用无线网卡，升级 BIOS 后恢复即可）。

**故障排除：**

Q：联想笔记本无电池如何升级 BIOS？

A：如果找不到电池，请解压缩`78cn25ww.exe`文件（BIOS 文件请自行去联想美国官网获取），用记事本打开`platform.ini`，查找：

```
[AC_Adapter]
Flag=1
BatteryCheck=1
BatteryBound=30
```

将以上所有数值都修改为`0`：

```
[AC_Adapter]
Flag=0
BatteryCheck=0
BatteryBound=0
```

保存后，双击`InsydeFlash.exe`即可。

**如果断电，后果自负**
