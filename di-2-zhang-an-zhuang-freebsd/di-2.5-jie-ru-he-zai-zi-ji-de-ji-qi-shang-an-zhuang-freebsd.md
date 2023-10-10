# 第 2.5 节 如何在自己的机器上安装 FreeBSD

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

只有当使用 **光盘/虚拟机** 安装时才应选用 `iso` 结尾的镜像。这是因为 FreeBSD 的 ISO 镜像没做 Hybrid 混合启动，写入 U 盘会产生错误。见 [Bug](https://bugs.freebsd.org/bugzilla/show\_bug.cgi?id=236786)。

**FreeBSD 所有安装介质包括不限于虚拟机文件都没有提供图形界面，均需要自行安装。**

> **注意**
>
> 如果要在 VMware 虚拟机使用 UEFI，必须使用 FreeBSD 13.0-RELEASE 及以上，否则启动会花屏。

### 我该如何刻录 FreeBSD 镜像到 U 盘？

刻录工具 Windows 应该选用 **Rufus**，Linux 直接使用 `dd`命令即可。

rufus 下载地址：[https://rufus.ie/zh](https://rufus.ie/zh)

> **警告**
>
> **不建议** 使用 FreeBSD 手册推荐的 win32diskimager，有时会出现校验码错误的情况（实际上文件校验码正常）。**只有在 rufus 无效的情况下才应使用 win32diskimager。** 下载地址 <https://sourceforge.net/projects/win32diskimager/files/Archive/>,点击 `win32diskimager-1.0.0-install.exe` 即可下载。
>
> **严禁** 使用 Ventoy 引导实体机安装，有时会报错找不到安装文件。
>
> 请 **老老实实用 rufus。**

##

