# 凡例

## 目标平台

目前版本兼容 FreeBSD 14.2-RELEASE 及 FreeBSD 15.0-CURRENT，并尽量向下兼容。

主要面向 X86、AArch64 架构，并支持尽可能多的架构。

Windows 测试环境为 Windows 10、11，并尽量使用最新版本的 Windows。

## pkg 与 ports

因为 FreeBSD 有两种安装软件的方式（但并非所有软件都支持 pkg 的安装方式），因此为了方便，在本跑路教程中已经尽可能地列出了两种方式的安装说明。但希望大家明白，只是为了方便，而并非不能使用 ports 或者 pkg 进行安装或必须使用二者其一进行安装。

>**请注意**
>
> ports 一般是 HEAD 分支，你的 pkg 最好与 ports 保持在同一主线上，即都选择 `latest`。


示例：

要安装软件 `yyy`，`yyy` 在 ports 里是 `xxx/yyy`，即路径是 `/usr/ports/xxx/yyy`。

- 那么首先可以通过 pkg 安装二进制软件包，和绝大多数 Linux 用法一样，下同：

```sh
# pkg install yyy
```

还可以这样：

```sh
# pkg install xxx/yyy
```

或者这样简写：

```sh
# pkg ins yyy
```

- 那么还可以通过 Ports 编译安装：

```sh
# cd /usr/ports/xxx/yyy
# make install clean
```

将会不断地弹出来窗口询问你怎么选。如果是使用默认选项，请这样做，则：

```sh
# cd /usr/ports/xxx/yyy
# make BATCH=yes install clean
```

如果你想一次性完成所有配置：

```sh
# cd /usr/ports/xxx/yyy
# make config-recursive # 会一直问你，直到结束依赖
# make install clean
```


### 本书中命令前的符号含义

`#` 代表 `root` 下的操作，基本等同 `sudo`。

`$`、`%` 代表普通用户账户权限。

## 对用户的要求

以高等院校计算机科学与技术学科一般本科毕业生所能达到的及格或及格以上水平为编写难度基准。如未能达到要求，请自行学习。

## 本书定位

本书旨在敉平新手与进阶之间的台阶。

## 参考书目

相关书籍：新的变化也不是很大。不像 Linux 有这么多入门书籍。出于历史上的原因，看 UNIX 相关书籍即可。


> **技巧**
>
> 以下有多本书籍可通过微信读书免费阅读。

|                                                     封面                                                    |                书名                |                             作者                             |      ISBN     |       出版社       |                                         原版书名                                        |                     说明                    |
| :-------------------------------------------------------------------------------------------------------: | :------------------------------: | :--------------------------------------------------------: | :-----------: | :-------------: | :---------------------------------------------------------------------------------: | :---------------------------------------: |
| ![Absolute FreeBSD, 3rd Edition: The Complete Guide to FreeBS](./.gitbook/assets/AbsoluteBSD.png) |    _**Absolute FreeBSD 3rd**_    |                      Michael W. Lucas                      | 9781593278922 | No Starch Press |                                          /                                          | 英文版，目前没有译文。词汇包括内容都非常基础。**有计算机基础的人不需要阅读。** |
|                             ![Unix & Linux大学教程](./.gitbook/assets/unix3.png)                             |        《Unix & Linux 大学教程》       |                         Harley Hahn                        | 9787302209560 |     清华大学出版社     |                     _**Harley Hahn's Guide to Unix and Linux**_                     |                   命令行基础                   |
|                         ![UNIX/Linux 系统管理技术手册（第5版）](./.gitbook/assets/unix4.png)                         |   《UNIX/Linux 系统管理技术手册（第 5 版）》   | Evi Nemeth、Garth Snyder、Trent R.Hein、Ben Whaley、Dan Mackin | 9787115532763 |     人民邮电出版社     |           _**UNIX and Linux System Administration Handbook 5th Edition**_           |               命令行进阶与 UNIX 基础              |
|                       ![FreeBSD 操作系统设计与实现（原书第二版）](./.gitbook/assets/freebsd2rd.png)                      |   《FreeBSD 操作系统设计与实现（原书第 2 版）》   |  Marshall McKusick、George Neville-Neil、Robert N.M. Watson  | 9787111689973 |     机械工业出版社     |         _**Design and Implementation of the FreeBSD Operating System, 2nd**_        |                  主要讲解了内核。轻型纸，居然还有几个章节要自己在网络自己下载？                 |
|                            ![UNIX 传奇：历史与回忆](./.gitbook/assets/unixchuanqi.png)                           |         《UNIX 传奇——历史与回忆》         |                      Brian W Kernighan                     | 9787115557179 |     人民邮电出版社     |                          _**UNIX: A History and a Memoir**_                         |             主要讲解了 UNIX 的发展历史。写的比较粗略。             |
|                               ![UNIX 编程艺术](./.gitbook/assets/s11345267.png)                              |            《UNIX 编程艺术》           |                        Eric Raymond                        | 9787121176654 |     电子工业出版社     | _**The Art of UNIX Programming (The Addison-Wesley Professional Computng Series)**_ |          主要讲解了 UNIX 的设计哲学与软件工程理论。         |
|                                ![大教堂与集市](./.gitbook/assets/dajiaotang.png)                               |             《大教堂与集市》             |                       Eric S. Raymond                      | 9787111452478 |     机械工业出版社     |                           _**The Cathedral & the Bazaar**_                          |               主要介绍了开源运动的发展史。              |
|                              ![4.4BSD 操作系统设计与实现](./.gitbook/assets/4BSD.png)                             |        《4.4BSD 操作系统设计与实现》        |                   Marshall Kirk McKusick                   | 9787111366478 |     机械工业出版社     |          _**The Design and Implementation of the 4.4BSD Operating System**_         |              4.4BSD 操作系统设计与实现             |
|                          ![深入理解 FreeBSD 设备驱动程序开发](./.gitbook/assets/qudong.png)                          |      《深入理解 FreeBSD 设备驱动程序开发》     |                         Joseph Kong                        | 9787111411574 |     机械工业出版社     |                _**FreeBSD Device Drivers: A Guide for the Intrepid**_               |              FreeBSD 设备驱动程序开发             |
|                              ![UNIX环境高级编程（第3版）](./.gitbook/assets/unix.png)                              |       《UNIX 环境高级编程（第 3 版）》       |              W.Richard Stevens、Stephen A.Rago              | 9787115352118 |     人民邮电出版社     |          _**Advanced Programming in the UNIX Environment, Third Edition**_          |          深入了解驱动 UNIX 内核的编程接口的实用知识         |
|                       ![UNIX 网络编程 卷 1：套接字联网 API（第3版）](./.gitbook/assets/unix1.png)                       | 《UNIX 网络编程 卷 1：套接字联网 API（第 3 版）》 |       W. Richard Stevens、Bill Fenner、Andrew M. Rudoff      | 9787115367198 |     人民邮电出版社     | _**UNIX Network Programming, Volume 1: The Sockets Networking API, Third Edition**_ |             如何使用套接字 API 进行网络编程            |
|                         ![UNIX 网络编程 卷 2：进程间通信（第2版）](./.gitbook/assets/unix2.png)                         |   《UNIX 网络编程 卷 2：进程间通信（第 2 版）》   |                     W. Richard Stevens                     | 9787115367204 |     人民邮电出版社     |  _**UNIX Network Programming,Vovum 2：Interprocess Communications,Second Edition**_  |    深入了解各种进程间通信形式。**这书原作者没出第 3 版，不用再找了**   |
| ![深入理解 UNIX 系统内核](./.gitbook/assets/unixinternals.png)|《深入理解 UNIX 系统内核》|Uresh Vahalia|9787111491453|机械工业出版社|***UNIX Internals: The New Frontiers***|UNIX 内核基础|
