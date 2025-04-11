# 第 1.4 节 Linux 用户迁移指南

## FreeBSD 与 Linux 不同之处

- FreeBSD 仍然使用古老的 BSD init 而非 systemd；BSD init 与传统的 SysVinit 也不大相同——BSD 没有运行级别（runlevel），也没有 `/etc/inittab`，均由 rc 控制。

当以用户进程身份运行 init 时，可模拟 AT&T System V UNIX 的行为——即超级用户可以在命令行中指定所需的运行级别：init 会向原始的（PID 为 1 的）init 进程发送特定信号，以执行相应的操作，实现类似的功能。参见 [init](https://man.freebsd.org/cgi/man.cgi?query=init&sektion=8&manpath=freebsd-release-ports)。例如在 FreeBSD 中执行 `init 0` 仍然是关机。

| 运行级别 | 信号       | 操作说明                             |
|:----------:|:------------|:--------------------------------------|
| 0        | SIGUSR1    | 停止系统运行。                       |
| 0        | SIGUSR2    | 停止系统运行并关闭电源。             |
| 0        | SIGWINCH   | 停止系统运行，关闭电源，然后重新启动。 |
| 1        | SIGTERM    | 进入单用户模式。                     |
| 6        | SIGINT     | 重启计算机。                         |
| c        | SIGTSTP    | 阻止进一步的登录。                   |
| q        | SIGHUP     | 重新扫描终端设备文件（ttys(5)）。   |


- FreeBSD 所有用户 shell 默认均是 sh（14 之前 root 为 csh，普通用户为 sh），而非 bash（如果你喜欢，亦可切换为 bash 或 zsh）；

- FreeBSD 基本系统几乎不包含任何与 BSD 协议不兼容的软件（你可以自己安装）。

>**思考题**
>>
>>- FreeBSD 致力于去 GNU 化，这意味着基本系统不使用 glibc、GCC 等软件。
>
>你认为是 BSD 一直在去 GNU 化，还是 Linux 一直在 GNU 化？

- FreeBSD 的用户配置文件和系统配置文件严格分离，即内核和基本系统与第三方应用程序是完全分离的；
- FreeBSD 项目是作为一个完整的操作系统维护的，而非内核与 userland 单独维护；也就是说如果你要使用 FreeBSD，那么就只有一个 FreeBSD 可选；
- FreeBSD 没有 free 命令也不支持安装这个包（FreeBSD 已不使用 procfs），FreeBSD 基本系统自带的文本编辑器有 `ee` 和 `vi`（不是软链接到 vim 的 vi，是真实的 nvi）；没有预装 `wget`，而是 `etch`。


### 参考文献

- [浅析 Linux 初始化 init 系统，第 1 部分：sysvinit 第 2 部分：UpStart 第 3 部分：Systemd](https://www.cnblogs.com/MYSQLZOUQI/p/5250336.html)，为存档，原文已佚
- [init -- process control initialization](https://man.freebsd.org/cgi/man.cgi?query=init)
- [Comparison of init systems](https://wiki.gentoo.org/wiki/Comparison_of_init_systems)，各大 init 对比图
- [GPL Software in FreeBSD Base](https://wiki.freebsd.org/GPLinBase)，FreeBSD 基本系统中的 GPL 软件


## FreeBSD 的缺陷

- FreeBSD 无论社区还是开发者都秉持着“慢就是快，快就是慢”的哲学思想。正因为秉持这一思想，让很多事物不被匆忙对待，有更多的时间来审视一切。但这是一个后工业化的时代，很多人认为“欲速则不达”只是一种落伍的软件工程理论，而更偏好于敏捷开发。~~我们的确需要花些时间慢下来，审视自己的一切，无论知识还是自我。花些时间在路旁的花朵石子上面，也许并不是浪费时间，无所事事。~~
- FreeBSD 系统总体上不够现代化，缺乏现代操作系统应有的实现。与其他系统相比，在嵌入式方面差距非常大。
- FreeBSD 没有为用户提供带桌面的基本系统；
- FreeBSD 的驱动水平较差；
- FreeBSD 的开发者非常少，这意味着你的 Bug 可能很久都无法得到解决，不是所有软件包都能时刻保持最新版；
- FreeBSD 的资料相对较少；
- 由于 Systemd 不兼容 Linux 以外的操作系统，导致很多软件比如 NetworkManager 无法移植，桌面环境的组件也无法完善；
- 由于 FreeBSD 项目的基本目标和设计问题，FreeBSD 基本系统不包含一般 Linux 中常用的一些软件和命令，比如没有 `lspci`、`free`。有些可以自己安装，有些则不行；
- FreeBSD 的两个文件系统 ZFS 与 UFS 都只能扩大不能缩小，一个奇怪的设计；
- FreeBSD 缺乏上层应用软件设计，即使底层有类似 docker 的技术 jail 也没能发展起来；FreeBSD 的虚拟化技术 Byhve 也很难用：没有一个前端的 GUI 来控制，设定参数也缺乏一个统一的教程。

> 我们现在称为容器技术的概念最初出现在 2000 年，当时称为 FreeBSD jail，这种技术可将 FreeBSD 系统分区为多个子系统（也称为 Jail）。Jail 是作为安全环境而开发的，系统管理员可与企业内部或外部的多个用户共享这些 Jail。2001 年，通过 Jacques Gélinas 的 VServer 项目，隔离环境的实施进入了 Linux 领域。在完成了这项针对 Linux 中多个受控制用户空间的基础性工作后，Linux 容器开始逐渐成形并最终发展成了现在的模样。2008 年，Docker 公司凭借与公司同名的容器技术通过 dotCloud 登上了舞台。—— [什么是 Linux 容器？](https://www.redhat.com/zh/topics/containers/shenmeshi-linux-rongqi)

## 基本对比

|   操作系统   |                           发布/生命周期（主要版本）                           |                          主要包管理器（命令）                          |                        许可证（主要）                        | 工具链 |   shell    |     桌面     |
| :----------: | :---------------------------------------------------------------------------: | :--------------------------------------------------------------------: | :----------------------------------------------------------: | :----: | :--------: | :----------: |
|    Ubuntu    |             [2 年/10 年](https://ubuntu.com/about/release-cycle)              |        [apt](https://ubuntu.com/server/docs/package-management)        | [GNU](https://ubuntu.com/legal/intellectual-property-policy) |  gcc   |    bash    |    Gnome     |
| Gentoo Linux |                                   滚动更新                                    |       [Portage（emerge）](https://wiki.gentoo.org/wiki/Portage)        |                             GNU                              |  gcc   |    bash    |     可选     |
|  Arch Linux  |                                   滚动更新                                    |           [pacman](https://wiki.archlinux.org/title/pacman)            |                             GNU                              |  gcc   |    bash    |     可选     |
|     RHEL     | [3/最长 12 年](https://access.redhat.com/zh_CN/support/policy/updates/errata) | [RPM（yum、dnf）](https://www.redhat.com/sysadmin/how-manage-packages) |                             GNU                              |  gcc   |    bash    |    Gnome     |
|   FreeBSD    |               [约 2/4 年](https://www.freebsd.org/security/)                |                               pkg/ports                                |                             BSD                              | clang  |   csh/sh   |     可选     |
|   Windows    |       [不固定](https://docs.microsoft.com/zh-cn/lifecycle/faq/windows)        |                                  可选                                  |                             专有                             |  可选  | powershell | Windows 桌面 |
|    MacOS     |                                 1 年/约 5 年                                  |                                   无                                   |           [专有](https://www.apple.com/legal/sla/)           | clang  |    zsh     |     Aqua     |


## 命令替代/软件替代

因为 Linux 广泛使用的也是 GNU 工具，因此只要理论上不是依赖于特定的 Linux 函数库，该工具都可以在 FreeBSD 上运行。

| Linux 命令/GNU 软件 | BSD Port/命令 |      作用说明      |                                                                                  备注                                                                                   |
| :-----------------: | :-------------------: |  :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        `lsusb`        |          `sysutils/usbutils`  |   显示 USB 信息    |                                                                            粗略地可以用 `cat /var/run/dmesg`                                                                             |
|        `lspci`        |        `sysutils/pciutils` |    显示 PCI 信息    |                                                                            粗略地可以用 `cat /var/run/dmesg`                                                                             |
|        `lsblk`        |         `sysutils/lsblk`    |  显示磁盘使用情况  |                                                                                            /                                                                                             |
|        `free`        |     `sysutils/freecolor` |  显示内存使用情况  | FreeBSD 未提供 `free` 命令，因为其依赖 Linux 特性，由包 `procps` 提供。如确需要 `free`，可用 `https://github.com/j-keck/free` 其他替代命令是 `vmstat` |
|        `lscpu`        |        `sysutils/lscpu`    |   显示处理器信息   |                                                                                            /                                                                                             |
|        glibc        |        bsdlibc        |                   C 库        |                                                                                            /                                                                                             |
|         GCC         |     LLVM + Clang      |            编译器、编译链工具 |                                                                              非要用也可以安装 `devel/gcc`                                                                               |
|         `vim`         |            `editors/vim/`    |     文本编辑器     |                                                                  FreeBSD 的 `vi` 不是软连接到 `vim`，而是早期的 `nvi`                                                                   |
|        `wget`         |          `ftp/wget`    |       下载器       |                                                                               系统默认的下载工具是 `fetch`                                                                                |
|        bash         |           `shells/bash`   |       shell        |                                              系统默认的 shell 是 `sh`（非软连接）。你可以自己改。                                             |
|   NetworkManager    |      `net-mgmt/networkmgr`  |    网络连接工具    |                                                                        NetworkManager 依赖 `systemd` 无法直接移植                                                                        |
|`lsmod`|	`kldstat`|列出已加载的内核模块|/|
|`strace`|	`truss`|跟踪系统调用|/|
|`modprobe`|	加载内核模块：`kldload`；卸载内核模块：`kldunload` |加载内核模块、卸载内核模块|/|
