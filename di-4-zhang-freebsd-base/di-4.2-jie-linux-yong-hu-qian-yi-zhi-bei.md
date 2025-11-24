# 4.2 Linux 用户迁移指南

## 历史

许多流行于 Linux 中的常见概念，其真正的提出者其实是 BSD：

- 比如“容器”的概念（可参考 [什么是 Linux 容器？](https://www.redhat.com/zh/topics/containers/whats-a-linux-container)）；
- “发行版”的概念（参见 [《FreeBSD：原始操作系统发行版的火炬传承者》](https://book.bsdcn.org/fan-yi-wen-zhang-cun-dang/2025-nian-1-yue/bsd)）；
- Gentoo Ports 的方法源于 BSD；
- 乃至于开源的理念，也是 BSD 首先提出的，世界上第一款开源许可证就是 BSD 许可证。在这个意义上，BSD 是世界上第一款真正自由开源的操作系统。

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


- FreeBSD 所有用户 shell 默认均是 sh（14 之前 root 为 csh），而非 bash（若你喜欢，亦可切换）；
- FreeBSD 基本系统几乎不包含任何与 BSD 协议不兼容的软件；

### 参考文献

- [浅析 Linux 初始化 init 系统，第 1 部分：sysvinit 第 2 部分：UpStart 第 3 部分：Systemd](https://www.cnblogs.com/MYSQLZOUQI/p/5250336.html)，为存档，原文已佚
- [init -- process control initialization](https://man.freebsd.org/cgi/man.cgi?query=init)
- [Comparison of init systems](https://wiki.gentoo.org/wiki/Comparison_of_init_systems)，各大 init 对比图
- [GPL Software in FreeBSD Base](https://wiki.freebsd.org/GPLinBase)，FreeBSD 基本系统中的 GPL 软件

许多 Linux 的常用概念其实最初源于 BSD，比如容器、发行版的概念。

—— [什么是 Linux 容器？](https://www.redhat.com/zh/topics/containers/shenmeshi-linux-rongqi)

我们现在称为容器技术的概念最初出现在 2000 年，当时称为 FreeBSD jail，这种技术可将 FreeBSD 系统分区为多个子系统（也称为 Jail）。Jail 是作为安全环境而开发的，系统管理员可与企业内部或外部的多个用户共享这些 Jail。2001 年，通过 Jacques Gélinas 的 VServer 项目，隔离环境的实施进入了 Linux 领域。在完成了这项针对 Linux 中多个受控制用户空间的基础性工作后，Linux 容器开始逐渐成形并最终发展成了现在的模样。2008 年，Docker 公司凭借与公司同名的容器技术通过 dotCloud 登上了舞台。

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
