# 第四节 FreeBSD 与其他操作系统

## 什么是 FreeBSD？

　 FreeBSD 不是 Linux，不是国产操作系统，不兼容 Systemd，不能吃鸡，亦不是 UNIX 。目前在 BSD 系中，FreeBSD 的用户是最多的。一些 Linux 下的软件基本上在 FreeBSD 中都能够被找到，即使找不到的也可以通过 CentOS 兼容层运行，你也可以自己通过 debootstrap 构建一个 debian 或者 ubuntu 的 / 系统。

![](../.gitbook/assets/图片3.png) **FreeBSD 不是Linux，亦不是UNIX。**

UNIX -> Networking Release 1->Networking Release 2  ->386BSD -> FreeBSD 1.0

386BSD -> 诉讼（1991-1994） -> 4.4 BSD-Lite -> FreeBSD 2.0

Linus“I have never even checked 386BSD out; when I started on Linux it wast available”

![](../.gitbook/assets/图片2.png)

## FreeBSD or Others  <a href="#freebsd-or-others" id="freebsd-or-others"></a>

　　①Linux

　　首先大概许多人是从 Linux 跑过来的，这样说我也没什么统计依据，不过姑且这样说罢。如果你发现在哪本书是举例提到 FreeBSD 是一种 Linux 发行版，那么我个人是不建议你继续看下去的，这属于误人子弟，我也曾在某些慕课网站上看到过类似行为。

　　严格来说 Linux 是指 Linux kernel，只是个内核而非操作系统。而 FreeBSD 是个操作系统。FreeBSD 采用 BSD 授权许可（见 [_https://www.freebsd.org/zh_CN/copyright/freebsd-license.html_](https://www.freebsd.org/zh_CN/copyright/freebsd-license.html) __ ）。FreeBSD 驱动方面一直是个大 Bug，不如 Linux 。

　　②Mac OS & iOS

　　 Mac OS & iOS 在一定程度上来说，都基于 FreeBSD 。可见 FreeBSD 的 GUI 并不是搞不好，只是 xorg 和开发方向有问题。

　 首先 mac os 和 iOS 某种程度上都基于 FreeBSD 。但是这时候就要说易用性了。FreeBSD 和 Linux 还都是那套 Xorg 。很明显不行，但是本着你行你上的观点我也上不去。。。图形界面才是第一 x3 。

　　到底是苹果成就了 mac os iOS 还是反过来 二者成就了苹果呢？举例来说，买 Mbp 装 Windows 。当然这是个人喜好，没有任何值得批评的地方。假设 iOS 预装 Android 。这么举例可能不恰当。但是相当一部分纯果粉应该是接受不了的。

　　生态环境。这个见 Windows Phone 。那么为什么选择 Apple 就不是 1% 的生活了？成功的商业化运作起着很大的用处。就像在这个贴吧里总有人看我不爽但又骂不过我一样，逞得口舌之利都不如我。FreeBSD 在大陆镜像站都没有，甚至因为 free 这个英文单词连官网都被电信屏蔽过。这个生态环境相比可知了。而且现在 UNIX 认证很宽容，所谓什么血统那是扯淡。好不好用自己心里没数吗？资本家之所以是资本家就在于产出再投入。对于这里而言，苹果的软件多就是因为用的人多。这个初期是怎么积累的？ FreeBSD 一场官司，初期就没有得到很好的发展，不然就没有 Linux 了，这话是 linus 说的。

　　国民素质有待提高。这个不是看不起嘲讽。这是客观事实。很多大学生甚至不知道什么是 Android，还有人说万物基于 MIUI 。这和术业有专攻这句话已经完全无关了。当然不是说用水果就是素质低，这么理解的人语文有毛病。

　　水果摆脱了开源界所谓的苦难哲学。

　　③ Microsoft Windows

　　微软非常重视用户体验，而一些社区可能完全忽视了这一点。直接的结果就是需要自己动手解决的地方略多。有人认为 Windows 简单因为都是图形化界面。事实上这是一种非常错误的说法，Windows 非常复杂。举例来说，你精通注册表否？知道每个选项什么意思吗？

　　至于安全性，很多人认为 UNIX-like 不需要杀毒软件，但是事实上这种观点是不正确的，当你发现自己中毒的时候，已经成为了病毒的培养基。但是目前来说，FreeBSD 远比 Windows 安全。

　　至于游戏什么的，已知 steam 运行。运行 Minecraft 这种 java 软件也没毛病。
