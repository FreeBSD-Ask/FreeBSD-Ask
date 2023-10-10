# 第 9.1 节 jail 与 docker 的比较

前文提及过 “Jail 与 byhve 虚拟化，不必配置底层虚拟化，节约系统资源。” FreeBSD 的 docker 处于破损状态，需要志愿者来维护。

## FreeBSD docker 现状

FreeBSD 的 docker 上次开发还是在 2015 年。后来在 2019 年 3 月 docker-freebsd 由于编译不通过而在 2020 年 1 月初被移除。当时 docker 还没有易名为 moby。docker 改名的原因和百度云改名百度网盘是一样的。

<https://www.freshports.org/sysutils/docker-freebsd/>

当时项目地址：<https://github.com/kvasdopil/docker>

当时的 docker 依赖 zfs 与 jail。似乎还利用了 Linux ABI。

在 docker 2015 编译错误后再无人接盘开发。此后有一些人尝试，但是终究没有成功。直到今年 2 月初有人重新接盘自己以前的努力开始继续。

大步骤计划：

- 从一个基于 moby 的新 port 开始（已完成）
- hack 它以使它能编译 (已完成)
- 运行时测试（“某些东西工作”）。
- 清理补丁/同步上游

目前的工作情况：

- 运行 FreeBSD docker 容器
- 建立 FreeBSD docker 容器（通过 docker 文件）。
- 桥接网络（使用 vnet，自动创建 docker0 桥，分配 IP 并设置 PF nat 规则，很可能还需要很多测试，IP 冲突等等）。

最有可能的是，在我的测试中，除了“尝试是否启动，运行一些命令，退出”之外，没有更多的问题了。

以上的计划和工作情况是该项目作者在两年前写就的。目前该项目被迁移到了 <https://codeberg.org/decke/ports> 而不再使用 Github。

该作者似乎没有对项目进行进一步说明，所以编译起来会有很多问题，详见 <https://codeberg.org/decke/ports/issues/18>

至于该项目在 FreeBSD 开发平台的链接则为 <https://reviews.freebsd.org/D21570>

最后希望有力者能够继续接盘帮助开发。
