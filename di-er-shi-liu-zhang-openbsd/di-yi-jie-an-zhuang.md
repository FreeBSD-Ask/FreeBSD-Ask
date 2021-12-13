# 第一节 安装

下载镜像

访问 [链接](https://mirrors.bfsu.edu.cn/OpenBSD/7.0/amd64/) ，下载系统镜像。若是刻录 U盘 安装，就下载 installXX.img ；若是虚拟机体验，请下载 installXX.iso 。（注：截止 OpenBSD 7.0 时，请不要使用 ventory 引导安装。）

## 自定义安装

这里推荐大家使用**自定义安装**，不要使用系统推荐的方式。因为为了安全考虑，**OpenBSD**默认大量分区。新用户初次遇到，会一头雾水，极不适应。

### 推荐分区

对于尝鲜的朋友，假设有 32GB 的容量，推荐两个分区： swap 2GB ，/ 为剩下的全部容量。

如果有 128GB 容量，推荐分区： / 32GB ，swap 4GB ，/home 为剩下的全部容量。

对于更大的容量，可依自己喜好，进一步细化分区配置。

### 安装过程

> Welcome to the OpenBSD/amd64 7.0 installation program.
> (I)nstall, (U)pgrade or (S)hell? `i`

选择 i 进行安装

> System hostname? (short form, e.g. 'foo') `XiaoMing`

系统主机名，可以选择一个字母少的，将来会显示`XiaoMing.DHCP`这样的主机名。

> Available network interfaces are: em0 rtwn0.\n
> Which one do you wish to configure? (or 'done') [em0]

这一步选择网络连接。为免去不必要麻烦，请尽量选择有线网络。本例中 `em0` 为有线网络，`rtwn0` 为无线网络。

后续配置直接**回车键**确认即可。

> Password for root account? (will not echo)

设置根账号密码，输入后回车确认（密码不会在屏幕上显示）。

> Password for root account? (again)

再次输入一遍根账号密码，回车键确认。

后续配置回车确认。

> Do you expect to run the X Window System? [yes] `no`

图形窗口界面，这一步选择 `no`，后续我们会安装自己需要的桌面环境。

> Setup a user? (enter a lower-case loginname, or 'no') [no] `XiaoMing`

设置一个用户名。

> Full user name for XiaoMing?

用户全名，可随意输入。

> Password for XiaoMing account? (will not echo)

为该账号设置密码（密码不会显示在屏幕上）。

> Password for XiaoMing account? (again)

再次输入该用户名的密码。

后续配置回车确认。

> What timezone are you in? ('?' for list) [US/Eastern] ?

时区选择，`？` 列出所有选项。依次进入 `Asia/Shanghai`

What timezone are you in? ('?' for list)

时区选择，找到 `Beijing` 选择北京时区。

> Available disks are: sd0, sd1, sd2.
> Which one is the root disk? (or 'done') [sd0] `?`

这一步是选择要将系统安装在哪一块硬盘。按 `？` 列出识别的所有硬盘。请务必记住所有的盘符：所要安装系统的盘符，以及我们的U盘 盘符。然后输入需要安装的位置，如 `sd0` 。

再次提醒：请确认好目标硬盘，否则悔之晚矣！

> Use DUIDs rather than device names in fstab? [yes]

回车确认默认选择。

> Use (W)hole disk, use the (O)penBSD area, or (E)dit the MBR? [whole]

是否选择全部硬盘空间，回车选择全部。

> Use (A)uto layout, (E)dit auto layout, or create (C)ustom layout? [a] `C`

这一步一定要选择 `C` ，即`自定义设置` 。

> `p m`

输入 `p m` 来显示硬盘。其它选项如下表：

| 代码  | 作用  |
| --- | --- |
| p m | 查看分区大小 |
| a   | 增加分区 |
| d   | 删除分区 |
| q   | 确认分区 |

以下假设一块 64 GB 硬盘，分区为：/ 20GB ， swap 4GB ，然后剩下的空间全部划分给 /home 。

> \> `a`
> 
> partition: [a]
>
> offset: [64]
> size: [xxxxxxxx] `20g`
> Rounding size to cylinder (bbbbb sectors): yyyyyyyy
> FS type: [4.2BSD]
> mount point: [none] `/`
> Rounding size to bsize (w sectors): zzzzzzz
> 
> \>

这里设置了 20GB 的 / 分区，`阴影框`为我们输入的设置，其余的皆为回车键默认选择。

> \> a
> partition: [b]
> offset: []
> size: [xxxxxxxxxx] 4g
> Rounding size to cylinder (w sectors): zzzzzz
> FS type: [swap]
> 
> \>

这里设置了 4GB 的 swap 分区，`阴影框` 为我们输入的设置，其余的皆为回车键默认选择。

> \> `a`
> partition: [h]
> offset: [aaaaaaaaa]
> size: [ASDFGHJKL]
> FS type: [4.2BSD]
> mount point: [none] `/home`
> Rounding size to bsize (w sectors): zzzzzzzz
> 
> \>

注意 `size` 一栏里我们并未输入数值，而是直接回车，意味着上步余下的全部容量都给了该分区，即 `/home` 分区。

配置完毕，记得输入 `q` 确认。

> \> `q`

以上，分区完毕。

> Let's install the sets!
> Location of sets? (cd disk ftp http or 'done') [cd] `disk`

软件地址，选择`disk` 。
