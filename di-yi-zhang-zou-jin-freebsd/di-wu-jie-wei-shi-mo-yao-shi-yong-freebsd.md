# 第五节 为什么要使用 FreeBSD

## 选择 FreeBSD 的一般原因 <a href="#xuan-ze-freebsd-de-yi-ban-yuan-yin" id="xuan-ze-freebsd-de-yi-ban-yuan-yin"></a>

　　从道家来讲，你爱选不选，太长不看，不用？左转 Linux , Windows 吧，不谢。

　　从佛教来说，因为缘分。万物缘起性空，我们有缘相聚，又会者定离。万般诸相皆如此。

　　从基督教来讲，这是主的指引。就像出埃及记一样，你看上去是自己的选择，实在上都是主的安排。

　　从辩证唯物主义来讲，是因为联系。FreeBSD 是 UNIX 直接后裔，而 Linux 只是仿制品，而很多协议又离不开 UNIX，所以你注定了要来到这里。

　　按照我个人观点而言，追求软件的稳定和新，既要有二进制源，又要能编译安装。除了 FreeBSD 之外我找不到 Linux 系统。

　　 BSD 三则授权协议：并允许自由分发。GPL 与 BSD 协议，究竟何者是真正的自由？

　　远离碎片化的 Linux 发行版，使得选择困难症用户免受痛苦。

　　 BSD 是一个完整的 OS，而不是内核。内核和基本系统作为一个项目来整体维护。

## 选择 FreeBSD 的技术性原因

　　系统配置文件与第三方软件配置文件分离。/etc 与 /usr/local/etc 等

　　文档齐全，所有涉及一般性的问题 Handbook 手册都有记述。

　　安全漏洞相比于 linux 较少。

　　接近2.5 年的版本发布周期，赋予了 FreeBSD 稳定性。

　　 Ports 可以编译安装软件，进行自由配置。

　　 ZFS 文件系统可以被配置为 root 分区。ZFS 被誉为最强大的文件系统。

　　 Jail 与 byhve 虚拟化，不必配置底层虚拟化，节约系统资源。

　　传统的 BSD INIT 引导，使你免受 systemd 迫害。

　　 DTrace 框架与 GEOM 存储框架。

　　 Linux CentOS 二进制兼容层，可运行 Linux 软件，只要其支持 CentOS 。

　　安全事件审计。
