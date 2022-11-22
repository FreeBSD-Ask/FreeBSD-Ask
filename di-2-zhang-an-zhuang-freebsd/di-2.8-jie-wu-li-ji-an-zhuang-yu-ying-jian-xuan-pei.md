# 第2.8节 物理机安装与硬件选配

## 物理机安装添加

> 注意：请不要问我在安装中应该选用哪个镜像站这类问题，那是因为你的错误操作导致的。 不要选用带有`bootonly`字样的镜像文件，除非你真的知道自己在干什么。

使用 **光盘** 安装应选用 `iso` 结尾的镜像。

使用 **U盘** 安装应该选用 `img` 结尾的镜像，例如

[https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/13.0/FreeBSD-13.0-RELEASE-amd64-memstick.img](https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/13.0/FreeBSD-13.0-RELEASE-amd64-memstick.img)

**FreeBSD 所有安装介质包括不限于虚拟机文件都没有提供图形界面，需要自行安装。**

**注意：如果要在 vmware 虚拟机使用 UEFI，必须使用 FreeBSD 13.0 及以上，否则启动会花屏。**

刻录工具 Windows 应该选用 Rufus，Linux 直接使用 `dd`命令即可。

https://rufus.ie/zh

**注意：不建议使用 Handbook 推荐的 win32diskimager，有时会出现校验码错误的情况（实际上文件校验码正常）。也不要使用 ventory 引导实体机安装，有时会报错找不到安装文件。老老实实 rufus。**

## 硬件选配（以下硬件均正常运行）

更多硬件请参考：

[https://bsd-hardware.info/?d=FreeBSD](https://bsd-hardware.info/?d=FreeBSD)

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

### 网卡推荐

> 以下无利益关系。

|      类型     |         品牌/型号         |        芯片组/参数        | 售价（¥） |
| :---------: | :-------------------: | :------------------: | :---: |
|   USB 无线网卡  |   COMFAST CF-WU810N   | RTL8188EUS 150M 2.4G |   20  |
|   USB 以太网卡  |   绿联 USB 百兆网卡 CR110   |     AX88772A 100M    |   40  |
|   USB 以太网卡  |   绿联 USB 千兆网卡 CM209   |    AX88179A 1000M    |   79  |
|   USB 以太网卡  |  绿联 USB 2.5G 网卡 CM275 |     RTL8156 2.5G     |  189  |
| Type-C 以太网卡 | 绿联 Type-C 转百兆网卡 30287 |     AX88772A 100M    |   59  |
| Type-C 以太网卡 | 绿联 Type-C 转千兆网卡 CM199 |    AX88179A 1000M    |   99  |
| Type-C 以太网卡 |  绿联 Type-C 转 2.5G 网卡  |     RTL8156 2.5G     |  199  |

> RTL8156 网卡如果时断时续，请安装 `realtek-re-kmod`。？（此处存疑） 见
>
> * [https://www.freshports.org/net/realtek-re-kmod](https://www.freshports.org/net/realtek-re-kmod)
> * [https://bugs.freebsd.org/bugzilla/show\_bug.cgi?id=166724](https://bugs.freebsd.org/bugzilla/show\_bug.cgi?id=166724)
