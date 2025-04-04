# 前言

## 目标平台

目前版本兼容 FreeBSD 14.2-RELEASE 及 FreeBSD 15.0-CURRENT，并尽量向下兼容。

主要面向 x86-64（amd64）、AArch64（arm64），并尽可能多的支持其他体系平台。

Windows 测试环境为 Windows 10、11，并尽量使用最新版本的 Windows。

## pkg 与 ports

因为 FreeBSD 有两种安装软件的方式（但个别软件不支持 pkg 安装）：因此为了方便，在本教程中已经尽可能地列出了两种方式的安装说明。但希望大家明白，只是为了方便，而并非不能使用 ports 或者 pkg 进行安装或必须使用二者其一进行安装。

>**请注意**
>
> ports 一般是 HEAD 分支，你的 pkg 最好与 ports 保持在同一主线上，即都选择 `latest`。

---

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


### 本书中命令及符号含义

`#` 代表 `root` 下的操作，基本等同 `su`、`sudo` 和 `doas`。

`$`、`%` 代表普通用户账户权限。

---

>**注意**
>
>提示一些注意事项。

>**技巧**
>
>提示一些技巧。

>**警告**
>
>如果不知道、不做就无法完成或造成重大危害的事项。

---

章节：

```
故障排除与未竟事宜
```

旨在将现存的问题和改进的方向/建议或谜团留置其中，以期后人的智慧。

## 对用户的要求

以高等院校计算机科学与技术学科一般本科毕业生所能达到的及格或及格以上水平为编写难度基准。你可以通过以下问题来判断：

- 科学在本质上是正确的还是错误的？科学与真理的区别是什么？（请勿套用马哲课本上的话，你是棵会思想的蒹葭）
- 尝试根据本书提供的线索，独立证明小学数学 `1+2=3` 以及证明其中 `+`，`=` 符号。
- 你可以自圆其说地向一位目前仍把屏幕认作主机（非一体机）的人解释为什么手机屏幕碎了而截图是完整的。
- 你可以按照本书的视频和文字图片教程独立完成在 VMware 虚拟机中的 FreeBSD 14.2-RELEASE 安装（在 Windows 11 环境下）；并配置好 KDE6 以及中文输入法。
- 在网络上找到本书下面所列的所有书籍的 PDF 或电子文件。（不得付费，独立完成）
- 当上面一条出现错误时清楚明白这是为什么？以及如何解决。并且有想要解决此问题的决心与信心。
- 在九个月内回答以上问题。

或：

- 向本书提交 PR 在实质上改进章节内容。
- 在毕业论文中使用或重点提及 FreeBSD

## 本书定位

本书旨在敉平新手与进阶之间的台阶。

## 参考书目

相关书籍：新的变化也不是很大。不像 Linux 有这么多入门书籍。出于历史上的原因，看 UNIX 相关书籍即可。


> **技巧**
>
> 以下有多本书籍可通过微信读书免费阅读。


| 封面 | 书名 | 作者 | ISBN | 出版社 | 说明 |
| :---: | :---: | :---: | :---: | :---: | :---: | 
|![FreeBSD 技术内幕](./.gitbook/assets/Unleashed.png) | 《FreeBSD 技术内幕》 | Brian Tiemann、Michael Urban | 9787111102010 | 机械工业出版社 |  2002 年的书，居然还能用。你该说 BSD 没有发展，还是该说他稳定？本书推荐选读第 1、4、8、9、10、11、12、13 章|
| ![Unix & Linux 大学教程](./.gitbook/assets/unix3.png) | 《Unix & Linux 大学教程》 | Harley Hahn | 9787302209560 | 清华大学出版社 | 命令行基础 |
| ![UNIX/Linux 系统管理技术手册（第 5 版）](./.gitbook/assets/unix4.png) | 《UNIX/Linux 系统管理技术手册（第 5 版）》 | Evi Nemeth、Garth Snyder、Trent R.Hein、Ben Whaley、Dan Mackin | 9787115532763 | 人民邮电出版社 |命令行进阶与 UNIX 基础 |
| ![FreeBSD 操作系统设计与实现（原书第二版）](./.gitbook/assets/freebsd2rd.png) | 《FreeBSD 操作系统设计与实现（原书第 2 版）》 | Marshall McKusick、George Neville-Neil、Robert N.M. Watson | 9787111689973 | 机械工业出版社 |  主要讲解了内核。轻型纸，居然还有几个章节要自己在网络自己下载？ |
| ![UNIX 编程艺术](./.gitbook/assets/s11345267.png) | 《UNIX 编程艺术》（TAOUP） | Eric Raymond | 9787121176654 | 电子工业出版社 | 主要讲解了 UNIX 的设计哲学与软件工程理论。 |
| ![大教堂与集市](./.gitbook/assets/dajiaotang.png) | 《大教堂与集市》 | Eric S. Raymond | 9787111452478 | 机械工业出版社 | 主要介绍了开源运动的发展史。 |
| ![4.4BSD 操作系统设计与实现](./.gitbook/assets/4BSD.png) | 《4.4BSD 操作系统设计与实现》 | Marshall Kirk McKusick | 9787111366478 | 机械工业出版社 | 4.4BSD 操作系统设计与实现 |
| ![深入理解 FreeBSD 设备驱动程序开发](./.gitbook/assets/qudong.png) | 《深入理解 FreeBSD 设备驱动程序开发》 | Joseph Kong | 9787111411574 | 机械工业出版社 |  FreeBSD 设备驱动程序开发 |
| ![UNIX 环境高级编程（第 3 版）](./.gitbook/assets/unix.png) | 《UNIX 环境高级编程（第 3 版）》 | W. Richard Stevens、Stephen A. Rago | 9787115352118 | 人民邮电出版社 |  深入了解驱动 UNIX 内核的编程接口的实用知识 |
| ![UNIX 网络编程 卷 1：套接字联网 API（第 3 版）](./.gitbook/assets/unix1.png) | 《UNIX 网络编程 卷 1：套接字联网 API（第 3 版）》 | W. Richard Stevens、Bill Fenner、Andrew M. Rudoff | 9787115367198 | 人民邮电出版社 | 如何使用套接字 API 进行网络编程 |
| ![UNIX 网络编程 卷 2：进程间通信（第 2 版）](./.gitbook/assets/unix2.png) | 《UNIX 网络编程 卷 2：进程间通信（第 2 版）》 | W. Richard Stevens | 9787115367204 | 人民邮电出版社 | 深入了解各种进程间通信形式。**这书原作者没出第 3 版，不用再找了** |
| ![深入理解 UNIX 系统内核](./.gitbook/assets/unixinternals.png) | 《深入理解 UNIX 系统内核》 | Uresh Vahalia | 9787111491453 | 机械工业出版社 | UNIX 内核基础 |


### 选读书目

| 封面 | 书名 | 作者 | ISBN | 出版社 |说明 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| ![UNIX 传奇：历史与回忆](./.gitbook/assets/unixchuanqi.png) | 《UNIX 传奇——历史与回忆》 | Brian W Kernighan | 9787115557179 | 人民邮电出版社 | 主要讲解了 UNIX 的发展历史。写的比较粗略。 |
| ![Absolute FreeBSD, 3rd Edition: The Complete Guide to FreeBS](./.gitbook/assets/AbsoluteBSD.png) | ***Absolute FreeBSD 3rd*** | Michael W. Lucas | 9781593278922 | No Starch Press |英文版，目前没有译文。词汇包括内容都非常基础。切记，有计算机基础的人不需要阅读。 |
