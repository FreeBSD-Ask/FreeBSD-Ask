# 第 1.10 节 FreeBSD 的不足之处

- FreeBSD 没有为用户提供一个带 GUI 的基本系统，甚至显卡驱动都需要自己通过 ports 编译安装；
- FreeBSD 的驱动很差劲，直到最近才将将完美地支持 WIFI 6 的网卡，比如 AX210；
- FreeBSD 的开发者非常少，这意味着你的 bug 可能很久都无法得到解决，不是所有软件包都像 ARCH 那样时刻保持最新版；
- FreeBSD 的资料相对较少，中文资料更少，除了本文以外的简体中文资料几乎为 0；
- 由于 systemd 不兼容 Linux 以外的操作系统，导致很多软件比如 NetworkManager 无法移植，桌面环境的组件也无法完善；
- FreeBSD 的菊苣们比 Linux 的还要更加高傲，他们不在意你到底会不会换源会不会设置代理，需不需要境内的官方镜像站；
- 由于 FreeBSD 项目的基本目标和设计问题，FreeBSD 基本系统不包含一般 Linux 中常用的一些软件和命令，比如没有 `lspci`,`free`。有些可以自己安装，有些则不行；
- FreeBSD 的两个文件系统 ZFS 与 UFS 都只能扩大不能缩小，一个奇怪的设计；
- FreeBSD 缺乏上层应用软件设计，即使底层有类似 docker 的技术 jail 也没能发展起来；FreeBSD 的虚拟化技术 Byhve 也很难用，没有一个前端的 GUI 来控制，设定参数也缺乏一个统一的教程。

> 我们现在称为容器技术的概念最初出现在 2000 年，当时称为 FreeBSD jail，这种技术可将 FreeBSD 系统分区为多个子系统（也称为 Jail）。Jail 是作为安全环境而开发的，系统管理员可与企业内部或外部的多个用户共享这些 Jail。2001 年，通过 Jacques Gélinas 的 VServer 项目，隔离环境的实施进入了 Linux 领域。在完成了这项针对 Linux 中多个受控制用户空间的基础性工作后，Linux 容器开始逐渐成形并最终发展成了现在的模样。2008 年，Docker 公司凭借与公司同名的容器技术通过 dotCloud 登上了舞台。—— [什么是 Linux 容器？](https://www.redhat.com/zh/topics/containers/whats-a-linux-container)
