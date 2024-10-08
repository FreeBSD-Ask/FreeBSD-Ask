# 第 2.6 节 普通电脑下载安装哪个镜像，如何刻录镜像？

## 我该下载哪个镜像？

> **警告**
>
> 如果在安装中出现应该选用哪个镜像站这个问题，是因为你全选了组件，请不要这样做。
>
>**请不要** 不看图文教程就全选所有的组件，要按照前文教程进行选择。
>
> **不要** 选用带有`bootonly`字样的镜像文件，除非你真的知道自己在干什么。


使用 **U 盘** 安装应该选用 `img` 结尾的镜像，例如 [FreeBSD-14.1-RELEASE-amd64-memstick.img](https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/14.1/FreeBSD-14.1-RELEASE-amd64-memstick.img)

只有当使用 **光盘/虚拟机** 安装时才应选用 `iso` 结尾的镜像。这是因为 FreeBSD 的 ISO 镜像没做 Hybrid 混合启动，写入 U 盘会产生错误。见 [Bug](https://bugs.freebsd.org/bugzilla/show\_bug.cgi?id=236786)。

> **警告**
>
>iso 镜像并不适用于物理机（普通电脑），物理机（普通电脑）请使用 img 镜像。除非你有光盘，否则一般请不要下 ISO。

>**技巧**
>
>部分机器（如老款神舟电脑）仍然支持 ISO UEFI 启动。但并非所有机器（比如小米就不支持）都如此。

>**技巧**
>
>FreeBSD 14.1 RELEASE 两个 ISO 均在 Ventoy 下测试通过（英特尔三代处理器下的 UEFI）。但是仍不排除出现问题的可能性。如果出现问题，请首先考虑下载 `img` 正常刻录。

> **注意**
>
>**FreeBSD 所有安装介质包括不限于虚拟机文件都没有提供图形界面，均需要自行安装。**

> **注意**
>
> 如果要在 VMware 虚拟机使用 UEFI，必须使用 FreeBSD 13.0-RELEASE 及以上，否则启动会花屏。

### FreeBSD 镜像 BT 种子下载地址

<https://fosstorrents.com/distributions/freebsd/>

## 我该如何刻录 FreeBSD 镜像到 U 盘？

Windows 上的刻录工具应首选 **Rufus**，Linux 直接使用 `dd`命令即可。

rufus 下载地址：[https://rufus.ie/zh](https://rufus.ie/zh)

> **警告**
>
> **不建议** 使用 FreeBSD 手册推荐的 win32diskimager，有时会出现校验码错误的情况（实际上文件校验码正常）。**应仅在 rufus 无效的情况下才应使用 win32diskimager。** 下载地址 <https://sourceforge.net/projects/win32diskimager/files/Archive/>，点击 `win32diskimager-1.0.0-install.exe` 即可下载。



## 存档内容

Q：联想笔记本无电池如何升级 BIOS？

A：如果找不到电池，请解压缩`78cn25ww.exe`文件（BIOS 文件请自行去联想美国官网获取），用记事本打开`platform.ini`，查找：

```sh
[AC_Adapter]
Flag=1
BatteryCheck=1
BatteryBound=30
```

将以上所有数值都修改为`0`：

```sh
[AC_Adapter]
Flag=0
BatteryCheck=0
BatteryBound=0
```

保存后，双击`InsydeFlash.exe`即可。

**如果断电，后果自负**
