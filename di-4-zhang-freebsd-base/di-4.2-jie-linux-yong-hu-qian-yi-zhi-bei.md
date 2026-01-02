# 4.2 Linux 用户迁移指南

## 遗失的世界

许多流行于 Linux 中的常见概念，其最初的提出者实际上是 BSD：

- 例如“容器”的概念（可参考 [什么是 Linux 容器？](https://www.redhat.com/zh/topics/containers/whats-a-linux-container)）；
- “发行版”的概念（参见 [《FreeBSD：原始操作系统发行版的火炬传承者》](https://book.bsdcn.org/fan-yi-wen-zhang-cun-dang/2025-nian-1-yue/bsd)）；
- Gentoo 的 Ports 方法源于 BSD；
- 乃至开源理念本身，也是 BSD 最早提出的，世界上第一款开源许可证即 BSD 许可证。在这个意义上，BSD 是世界上第一款真正自由开源的操作系统。

>**思考题**
>
>>“一切真历史都是当代史”（克罗齐. 历史学的理论和历史[M]. 田时纲译. 北京: 中国社会科学出版社, 2018）
>
>读者如何理解这句话？如何定义“真”与“非真”。

## FreeBSD 与 Linux 不同之处

### init

FreeBSD 仍然使用 BSD init 而非 systemd；BSD init 与传统的 SysVinit 也有所不同——BSD 没有运行级别（runlevel），也没有 `/etc/inittab`，均由 rc 系统控制。

当以用户进程身份运行 init 时，可以模拟 AT&T System V UNIX 的行为——即超级用户可以在命令行中指定所需的运行级别：该 init 进程会向原始的（PID 为 1 的）init 进程发送特定信号，以执行相应操作，实现类似功能。参见 [init(8)](https://man.freebsd.org/cgi/man.cgi?query=init&sektion=8&manpath=freebsd-release-ports)。例如，在 FreeBSD 中执行 `init 0` 仍然表示关机。

| 运行级别 | 信号       | 操作说明                             |
|:----------:|:------------|:--------------------------------------|
| 0        | SIGUSR1    | 停止系统运行。                       |
| 0        | SIGUSR2    | 停止系统运行并关闭电源。             |
| 0        | SIGWINCH   | 停止系统运行，关闭电源，然后重新启动。 |
| 1        | SIGTERM    | 进入单用户模式。                     |
| 6        | SIGINT     | 重启计算机。                         |
| c        | SIGTSTP    | 阻止进一步的登录。                   |
| q        | SIGHUP     | 重新扫描终端设备文件（ttys(5)）。   |

### shell

FreeBSD 所有用户的默认 shell 均为 sh（14 之前 root 默认为 csh），而非 bash（如有需要亦可切换）；

### 基本系统去 GNU 化

FreeBSD 基本系统几乎不包含任何与 BSD 协议不兼容的软件；

### 容器技术

许多 Linux 的常用概念最初源于 BSD，例如容器和发行版的概念。

—— [什么是 Linux 容器？](https://www.redhat.com/zh/topics/containers/shenmeshi-linux-rongqi)

我们现在称为容器技术的概念最初出现在 2000 年，当时称为 FreeBSD jail，这种技术可将 FreeBSD 系统分区为多个子系统（也称为 Jail）。Jail 是作为安全环境而开发的，系统管理员可与企业内部或外部的多个用户共享这些 Jail。2001 年，通过 Jacques Gélinas 的 VServer 项目，隔离环境的实施进入了 Linux 领域。在完成了这项针对 Linux 中多个受控制用户空间的基础性工作后，Linux 容器开始逐渐成形并最终发展成了现在的模样。2008 年，Docker 项目通过 dotCloud 平台推出其同名的容器技术并进入公众视野。

### 参考文献

- [浅析 Linux 初始化 init 系统，第 1 部分：sysvinit 第 2 部分：UpStart 第 3 部分：Systemd](https://www.cnblogs.com/MYSQLZOUQI/p/5250336.html)，为存档，原文已佚
- [init -- process control initialization](https://man.freebsd.org/cgi/man.cgi?query=init)
- [Comparison of init systems](https://wiki.gentoo.org/wiki/Comparison_of_init_systems)，各大 init 对比图
- [GPL Software in FreeBSD Base](https://wiki.freebsd.org/GPLinBase)，FreeBSD 基本系统中的 GPL 软件

## 基本对比

|   操作系统   |                           发布/生命周期（主要版本）                           |                          主要包管理器（命令）                          |                        许可证（主要）                        | 工具链 |   shell    |     桌面     |
| :----------: | :---------------------------------------------------------------------------: | :--------------------------------------------------------------------: | :----------------------------------------------------------: | :----: | :--------: | :----------: |
|    Ubuntu    |             [2 年/10 年](https://ubuntu.com/about/release-cycle)              |        [apt](https://ubuntu.com/server/docs/package-management)        | [GNU](https://ubuntu.com/legal/intellectual-property-policy) |  gcc   |    bash    |    Gnome     |
| Gentoo Linux |                                   滚动更新                                    |       [Portage（emerge）](https://wiki.gentoo.org/wiki/Portage)        |                             GNU                              |  gcc   |    bash    |     可选     |
|  Arch Linux  |                                   滚动更新                                    |           [pacman](https://wiki.archlinux.org/title/pacman)            |                             GNU                              |  gcc   |    bash    |     可选     |
|     RHEL     | [3/最长 12 年](https://access.redhat.com/zh_CN/support/policy/updates/errata) | [RPM（yum、dnf）](https://www.redhat.com/sysadmin/how-manage-packages) |                             GNU                              |  gcc   |    bash    |    Gnome     |
|   FreeBSD    |               [约 2/4 年](https://www.freebsd.org/security/)                |                               pkg/ports                                |                             BSD                              | clang  |   csh/sh   |     可选     |
|   Windows    |       [不固定](https://docs.microsoft.com/zh-cn/lifecycle/faq/windows)        |                                  可选                                  |                             专有                             |  可选  | PowerShell | Windows 桌面 |
|    macOS     |                                 1 年/约 5 年                                  |                                   无                                   |           [专有](https://www.apple.com/legal/sla/)           | clang  |    zsh     |     Aqua     |


由于 Linux 广泛使用 GNU 工具，因此理论上只要不依赖特定的 Linux 函数库，这些工具都可以在 FreeBSD 上运行。

| Linux 命令/GNU 软件 | BSD Port/命令 |      作用说明      |                                                                                  备注                                                                                   |
| :-----------------: | :-------------------: |  :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        `lsusb`        |          `sysutils/usbutils`  |   显示 USB 信息    |                                                                            粗略地可以用 `cat /var/run/dmesg`                                                                             |
|        `lspci`        |        `sysutils/pciutils` |    显示 PCI 信息    |                                                                            粗略地可以用 `cat /var/run/dmesg`                                                                             |
|        `lsblk`        |         `sysutils/lsblk`    |  显示磁盘使用情况  |                                                                                            /                                                                                             |
|        `free`        |     `sysutils/freecolor` |  显示内存使用情况  | FreeBSD 未提供 `free` 命令，因为该命令依赖 Linux 特性，通常由 `procps` 包提供。如确实需要 `free`，可使用 `https://github.com/j-keck/free`，其他替代命令包括 `vmstat` |
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


## 附录：GNU/Linux 发行版比较

由于 GNU 开源运动的大规模开展和 Linux 的蓬勃发展，大部分人对于开源的理解被囿于 GPL 协议与 Linux 系统，对 FreeBSD 等 BSD 世界则接触较少。一些以开源为旗号的社区组织，其活动也主要围绕 Linux 领域展开，鲜有超越这一范畴的探索。

当然，这并不是指这部分用户或团体本身有任何问题。无可指摘，“时来天地皆同力，运去英雄不自由”。李白永远无法成为盛唐的政治家，他自幼喜剑道，好修仙，年少时意欲成为“十步杀一人，千里不留行”的江湖侠客；后又想成为匡扶社稷的朝廷重臣。但太白终究“剑非万人敌，文窃四海声”。操作系统的命运和时代发展的脉搏紧密相连，市场的需求也在不断地塑造着我们今天习以为常的那些功能和交互模式。


>**思考题**
>
>>心知不得语，却欲栖蓬瀛。
>>
>>弯弧惧天狼，挟矢不敢张。
>>
>>揽涕黄金台，呼天哭昭王。
>>
>>无人贵骏骨，騄耳空腾骧。
>>
>>乐毅倘再生，于今亦奔亡。
>
>读者如何理解李白与 FreeBSD 项目及相关社区、人员在经历上的相似点。读者是否有一刻也曾感慨个人在时代面前的无力感。

本附录旨在对主流 GNU/Linux 发行版进行对比分析，帮助读者更全面地了解不同的 GNU/Linux 发行版。

### 何以成为 GNU/Linux 发行版

不同的操作系统/发行版，不同的世界观。对“发行版”给出一个精确而统一的定义并不容易。

>**思考题**
>
>如何理解“不同的操作系统/发行版，不同的世界观”这句话？

曾有人指出，“看似纷繁复杂的 Linux 发行版，仅仅是一个假象罢了。它们甚至可能缺乏独立的自主决策权。例如，若上游采用 systemd 初始化系统，发行版通常也会跟进。否则可能无法继续使用部分第三方软件，而后果就是你本身也被消灭了。Linux 发行版从未真正存在过。”

>**思考题**
>
>“Linux 发行版从未真正存在过。”这种说法固然存在一定的局限性，但它向我们提供了一个重要启示，怎样理解？

常见的 Linux 发行版以及一些基于 Linux 的国产操作系统，其维护工作的重点和范围主要体现在哪些方面？它们通常并非文件系统、Linux 内核、GNU C 库（glibc）、systemd、桌面环境等上游项目的原始维护者，对于大量第三方软件包，也往往以集成和适配为主。即使是包管理器和软件源，也大多是在上游工具和社区资源的基础上进行配置与管理。

在长期支持与稳定性方面，红帽企业 Linux（Red Hat Enterprise Linux，RHEL）投入了大量资源，这是其区别于许多其他发行版的重要特征。RHEL 通过保证应用二进制接口（Application Binary Interface，ABI）和内核应用二进制接口（Kernel Application Binary Interface，kABI）的长期稳定性，提供了最长可达十年的支持周期，这与许多其他发行版的支持策略存在明显差异。相关参考如下：

- [Red Hat Enterprise Linux 10: Application Compatibility Guide](https://access.redhat.com/articles/rhel10-abi-compatibility)
- [What is Kernel Application Binary Interface (kABI)?](https://access.redhat.com/solutions/444773)。

许多发行版并不直接维护或对上述软件和工具进行全面测试，也不一定为其持续编写补丁或文档。直接将修改回溯并贡献至上游的发行版相对较少，Ubuntu 是其中较为典型的例子。此外，即使发行版维护者有意向向上游贡献代码，也可能面临补丁被接受的挑战，因为其并不对上游项目拥有直接的决策权。

许多商业发行版（如 RHEL）确实向上游项目（例如 Linux 内核）贡献了大量代码，这是客观事实。然而，这并未完全解决基础工具维护资源不足的广泛问题。此外，一些基于提交量的分析表明，商业公司在代码贡献中占据较大比重，红帽是其中的重要贡献者之一。这反映出社区与商业组织在项目贡献与治理上的结构性变化，也揭示着开源社区对开源项目主导权的实质性转移。这一现象常被以 Xorg 项目作为讨论案例，目前其维护和发展方向主要由少数核心维护者和相关组织主导，项目整体重心逐步转向 Wayland 等新的显示技术路线。可以看到，商业发行版对 Linux 生态的影响并非在所有情况下都具有积极效果，其商业目标与部分开源项目的发展方向之间可能存在张力——在这一背景下，GPL 的制度设计产生了自我消解的效果。

>**思考题**
>
>>严肃的商业发行版力求稳定压倒一切，要求集中式的统一管理；而大多数 Linux 基础工具都强调敏捷开发策略，稳定性往往不是最高优先级，并且这些工具的控制权是极度分散的。
>
>你认为商业发行版对开源项目的贡献，根本上看，是为了发展项目，还是为了彻底消灭项目？为什么？

表面上用户似乎有多种发行版可选，但在兼容性、依赖和生态约束下，实际的可选范围可能比表面更为有限。在某些场景下，甚至没有任何选择的余地。用户所做出的选择表面上是自主的，但可供选择的选项往往由他人预先设定。大多数读者也有能力或正在维护自己的发行版，那么究竟在维护什么？从技术实质上看，几乎不存在任何可独立维护的组成部分。这是当前生态结构所决定的现实情况。

>**思考题**
>
>>你的自由意志和上帝的预定并不冲突。这和你的信仰无关，这是一个逻辑问题。
>
>请读者讨论个人选择与社会生产力的制约关系。
>
>分析：为什么说，看似自由的选择，其实也可能完全是被“预定”的。

### Ubuntu

部分用户反馈 Ubuntu 系统中会出现“[内部错误（internal error）](https://www.google.com/search?q=internal+error+ubuntu+site:askubuntu.com)”提示。有观点认为这是 Ubuntu 对错误信息的统一提示方式。需要注意的是，Ubuntu 在开发过程中会阶段性引入 Debian SID（不稳定分支）的软件包。这可能导致其稳定性在特定阶段存在不确定性（无论普通版本还是 LTS）。例如，在跨大版本或小版本升级时，部分用户反馈存在升级失败的风险，即使在初始环境较为干净的系统上也可能会出现。

以下命令可用于查询 Ubuntu 24.04 与 Debian 版本的关联信息：

```bash
ykla@ykla-ubuntu:~$ cat /etc/debian_version
trixie/sid # trixie 即 Debian 13。在当前时间点，Debian 最新的稳定版本是 12 bookworm
ykla@ykla-ubuntu:~$ cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=24.04
DISTRIB_CODENAME=noble
DISTRIB_DESCRIPTION="Ubuntu 24.04 LTS"
```

在 VMware Workstation 17 Pro 虚拟机上对 Ubuntu 24.04 LTS 版本（发布于伦敦当地时间 2024 年 4 月 25 日）进行测试时，发现其整体使用体验相较于之前版本有所下降。安装过程中即出现报错，且后续使用中遇到了窗口显示异常、鼠标光标消失、输入框无法获取焦点等问题。安装完成后，系统在开机后频繁弹出“内部错误”提示。

![Ubuntu 24.04 内部错误](../.gitbook/assets/nbcw.jpg)

![Ubuntu 24.10](../.gitbook/assets/ubuntu24.10.png)


### Fedora Linux

Fedora 在部分社区中存在较为戏谑的称呼“[地沟油](https://zh.moegirl.org.cn/zh-hans/Fedora%E5%A8%98)”。

Fedora 是基于 Red Hat Enterprise Linux（RHEL）的上游发行版，其定位侧重于技术验证和前沿特性测试，根本目的是为 RHEL 系统的新设计和新架构提供试验平台（[该社区由 Red Hat 红帽公司完全主导](https://docs.fedoraproject.org/en-US/council/)）。待特性稳定后，会引入到 RHEL 中。

因此，稳定性并非该发行版的主要设计目标。Fedora 官方的直接跨大版本升级失败率较高。这意味着长期使用后，用户可能需要进行全新安装并重新配置环境。用户难以在该发行版上获得长期的稳定性支持。与基于 Debian 的发行版不同，Fedora 不同大版本之间的软件源通常无法通用，因为软件依赖关系变动频繁。其各版本在定位上更接近于持续迭代的开发分支。其所有版本均包含大量新特性，稳定性表现与持续集成的 [nightly](https://openqa.fedoraproject.org/nightlies.html) 版本较为接近，差异不大。其稳定性特征与滚动更新发行版有相似之处。在部分测试场景下，其稳定性表现可能不及 Ubuntu。例如，在关闭屏幕保护与锁屏休眠功能后，进行长时间的高负载编译任务。在特定测试中，Fedora 系统可能在数小时后出现界面无响应，而在相同条件下，Ubuntu 系统运行正常。

由此可见，部分开源软件项目采用“社区测试，成熟后进入商业或企业级产品”的开发路径，例如 Wine 与 CrossOver。


>**思考题**
>
>你如何看待这种始终由开源社区进行测试和反馈，待稳定后引入其商业产品，同时再引入新一轮待测试项目或组件的开发模式？你认为这是一种形式主义的开源吗，即开源社区付出了实质性劳动力，但成果却被资本擢取，社区用户得到的始终是残次品。并且得不到任何报酬和荣誉。商业公司通过该模式将应承担的测试和客服等成本都转嫁给了开源社区。

近年来，Fedora 对系统资源的需求有所提升。在 VMware 虚拟机环境中，仅分配 4 GB 内存可能无法顺利完成安装，需要分配 6 GB 至 8 GB 内存才能避免安装过程停滞。

### CentOS/Rocky Linux/RHEL

CentOS 已从原先基于 RHEL 源代码重建的稳定发行版，转变为 RHEL 的中游开发与测试分支（即 CentOS Stream），其定位与 Fedora 有相似之处。其替代品较多，其中包括获得 UNIX 认证的欧拉（openEuler）操作系统。Rocky Linux 也是其中一个备受关注的替代方案。

这类系统在服务器领域被广泛部署，其特点是以牺牲软件版本的新颖性来换取稳定性，因此所包含的软件版本通常较为陈旧。同样，它们通常不支持直接跨大版本升级，并且在安全更新策略上相对保守。

### Debian

![Debian Logo，图片来自 https://www.debian.org/](../.gitbook/assets/debian.png)

Debian 的名称及 Logo 在中文语境中偶有基于谐音的非正式调侃“大便”（[谐音](https://www.debian.org/intro/about)“/ˈde.bi.ən/”）。

一个值得注意的[现象](https://lists.debian.org/debian-cd/2020/02/msg00000.html)是，如果在 Debian 安装过程中设置了 root 密码，系统默认可能不会安装 sudo 工具。这一设计通常被认为是出于安全性方面的考虑。但这可能与 GNOME 等桌面环境及大多数登录管理器默认禁止 root 账户直接登录的惯例存在张力。

此外，在部分版本（如 Debian 12.6）中，虽然会安装 sudo，但创建的第一个普通用户默认未被加入 `sudo` 组。这在实际使用中会带来不便，例如该普通用户无法直接通过 sudo 命令重启网络服务。用户需要切换到 tty 控制台登录 root 账户进行操作，这在一定程度上降低了图形界面（GUI）默认安装环境下的使用便利性。

> ```sh
> ykla@debian:~$ sudo su
> [sudo]ykla 的密码：
> ykla 不是 sudoers 文件。
> ykla@debian:~$ id
> uid=1000(ykla) gid=1000(ykla) 组=1000(ykla),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),100(users),106(netdev),111(bluetooth),113(Lpadmin),116(scanner)
> ykla@debian:~$ hostnamectl
> Static hostname: debian
>       Icon name: computer-vm
>         Chassis: vm
>      Machine ID: 9b3107b788dd461f94ca93150474946e
>         Boot ID: 081c39d5ac4748fa9ec0b2157c9a5beb
>  Virtualization: vmware
> Operating System: Debian GNU/Linux 12(bookworm)
>          Kernel: Linux 6.1.0-22-amd64
>    Architecture: x86-64
> Hardware Vendor: VMware, Inc.
>  Hardware Model: VMware Virtual Platform
> Firmware Version: 6.00
> ```

上述问题在实际安装和使用过程中较为明显。例如，安装程序在配置软件源时可能不会同步更新 `debian-security` 源，却默认尝试连接网络进行系统更新（此问题在 Ubuntu 中也存在。鲜为人知的是，在 Debian 高级安装中可绕过该问题），这有时会导致安装失败。

另外，其网络管理工具 [NetworkManager](https://wiki.debian.org/NetworkManager) 与 systemd 在部分功能的集成上可能存在冲突。类似的设计在实际使用中容易引发用户困扰。

对于普通用户而言，向 Debian 社区提交 Bug 报告并获取及时反馈的流程可能较为复杂。Debian 的 [Bug 报告流程](https://www.debian.org/Bugs/Reporting)相对于一些更注重用户友好性的开源项目而言，对普通用户门槛较高。

Debian Stable 发行版的软件包策略以稳定为主，大部分软件在发布后，其主版本号在生命周期内通常不会升级，软件版本会被锁定，因此应将 Stable 同时理解为“稳定”与“固定”。若用户需要获取更新的软件版本，则需要切换到 Testing 或 Unstable（Sid）分支，但这会牺牲系统的整体稳定性。

综上所述，Debian Stable 发行版以系统稳定著称，同时其软件包版本也相对较旧。在追求稳定性和软件包陈旧度方面，它与 RHEL 有相似之处。

### openSUSE

在物理机上安装完整的 openSUSE 后，部分用户反馈系统会出现卡顿现象。相关性能问题可能与默认使用的 Btrfs 文件系统的某些特性或配置有关。在多台不同代际的英特尔平台物理机上进行测试，均观察到了卡顿现象。安装后短时间内可能出现系统响应迟缓的情况。因此，不同用户对其使用体验的评价可能存在分歧。有用户通过将根文件系统从 Btrfs 切换为 Ext4 来规避此问题。在网络上搜索“openSUSE btrfs hang”可以发现类似反馈，表明这可能并非个别现象。

openSUSE 因其 Logo 形象，在社区中被昵称为“大蜥蜴”。

其版本号命名曾有一段趣事：为纪念英国作家道格拉斯·亚当斯在《银河系漫游指南》中提到的数字“42”（被誉为“生命、宇宙以及一切事物的终极答案”），openSUSE 将版本号从 13.x 跳跃至 42.x，随后又下调回 15.x。这导致了版本号逻辑上的一个现象：由于 42 大于 15，在特定条件下，从 15.x 升级可能会错误地指向 **更低** 的 42.x 版本。这种版本号跳跃再跌落现象在发行版中实属罕见。

openSUSE 有时会在稳定版本的软件包中引入实验性功能，且可能没有明确的提示。这可能导致用户将其视为软件缺陷（Bug）进行反馈。用户可能需要提交问题报告后，才能从维护者处得知该行为是实验性功能所致。

>**思考题**
>
>你认为在严肃的商业发行版中，允许出现此类版本异动和未经用户明确批准的测试行为吗？
>
>这是否可以用以论述，社区发行版仅仅是企业发行版的试验田。

openSUSE 原生的包管理器是 `zypper`。有用户将其与 Fedora 的 `dnf` 进行对比，认为 `zypper` 在交互响应速度或某些场景下的性能表现有待优化 ~~比如你数数这有几个字母？~~，`zypper` 相比 `dnf` 存在明显的卡顿和延迟。

### Gentoo Linux

Gentoo [自称](https://www.gentoo.org/get-started/about/)是“元发行版（*Metadistribution*）”。其传统安装方式是从源代码 **编译** 所有软件。虽然近年提供了[官方二进制包](https://www.gentoo.org/news/2023/12/29/Gentoo-binary.html)支持，但在依赖管理方面仍有一定复杂性，且二进制包通用性极为有限。

Gentoo 包管理系统的缺点在于，若某个软件包编译失败，则无法安装，且编译失败的情况时有发生。如果系统长时间不更新，再次更新时可能会遇到复杂的 **循环依赖** 问题。此外，Gentoo 难以进行大规模标准化部署，在服务器环境中的应用也相对较少。

此外，Gentoo 的 Portage 包管理器主要由 [Python](https://github.com/gentoo/portage) 语言编写。在进行大规模软件集（如 KDE 桌面环境）的依赖计算时，可能会耗费较长时间。在性能有限的处理器上，此计算过程可能需要数分钟至数小时不等，性能开销较为明显。由于可能存在循环依赖等问题，依赖解析过程往往需要多次迭代计算，有时甚至无法自动解决，导致安装操作失败。随着系统中安装的软件包数量增加，包管理操作（如依赖计算）所花费的时间将明显呈几何增长。

Gentoo 的包管理器设计理念独特，但学习曲线较为陡峭，对普通用户而言使用门槛较高。~~Gentoo 的包管理器好玩但是不好用——这应该是最好玩的包管理器了。~~

简而言之，Gentoo 高度灵活的 USE 标记系统和从源码编译的机制，在给予用户极大控制权的同时，也带来了较高的复杂性。依赖问题（包括循环依赖）可能影响系统稳定性，并使得软件安装、升级和卸载变得困难。

Gentoo 的高度定制化哲学要求用户投入更多精力进行系统管理和维护。

如果说 Arch Linux 可能在滚动更新中遇到问题，那么 Gentoo 则可能因为依赖冲突等问题，导致更新过程本身难以进行。如果系统长时间未更新，再次尝试更新时可能会因依赖地狱而无法继续进行任何软件包管理操作。复杂的 USE 标记系统，以至于即使是经验丰富的 Gentoo 用户也每天都在和这套哲学体系搏斗。依赖问题的解决是 Gentoo 社区中常见的技术讨论话题。

Gentoo 哲学和 C++ 哲学有异曲同工之妙：

>“C++ 是一种语言，而不是一个完整的系统。为每种应该支持的风格提供全面支持，**不试图去强迫别人做什么。**”

>“如果工具 **强迫用户** 按照特定的方式操作，那么工具实际上是在与用户对抗，而不是为用户服务。**我们都经历过工具强加自己意愿的情况。** 这是错误的，违背了 Gentoo 的哲学。”

正如世界上无人敢声称自己熟练掌握 C++ 一样，Gentoo 亦如此。自由的选择固然是人类向往的本性，但也带给人们无尽的焦虑和抑郁。

>**思考题**
>
>强迫自由究竟是实现自由的一种可行手段，还是一种形式主义和法西斯主义？
>
>在此基石上，请读者再理解 GPL 许可证与 BSD 许可证。

Gentoo 平台的 Bug 跟踪与反馈流程可能对普通用户不够友好。在个别情况下，相关问题可能在较长时间后，随着软件被移除而被标记为不再适用。其 Bug 报告平台的搜索与使用体验有待优化。有时通过外部搜索引擎（如 Google）使用“site:bugs.gentoo.org”语法进行搜索，可能比直接使用平台内搜索更有效。[高级搜索](https://bugs.gentoo.org/query.cgi)功能的使用也较为复杂。

### Deepin/UOS/中标麒麟

UOS 和 Deepin 的关系类似于 Red Hat Enterprise Linux（RHEL）与 Fedora 的关系，前者基于后者的社区版本进行商业化和深度定制。

Deepin 系统经常因部分更新包[测试不充分](https://bbs.deepin.org/post/218041)而饱受用户批评。有反馈称，某些存在问题的更新在推送后未及时撤回，官方仅通过发布修复教程进行处理。这种处理方式影响了用户体验。例如，有用户反馈在全新安装系统后立即升级，便遭遇了系统崩溃。

早期版本中，Deepin 系统在执行如复制文件等基础桌面操作时，曾出现界面卡顿或无响应的情况。

类似更新测试不充分的情况，在 UOS 系统中也有用户反馈。此类情况并非偶发。此外，用户曾遇到 UOS 更新服务器宕机或配置错误导致客户端异常（如浏览器无限弹窗打开几十上百个 UOS 主页）的情况，而官方状态通告有时不够及时。

UOS 服务器承载能力有限，因此 UOS 对镜像下载方式存在过限制，使得普通人无法使用迅雷下载。有用户测试反馈，其下载服务器带宽有限，且某些网络运营商（如中国移动）的用户可能难以连接。

问题在于 UOS 的许多系统功能（如开发者模式激活）需要在线账户登录并与服务器交互，若服务器连接不稳定，则会直接影响这些功能的使用。从技术角度来看，通过采用更高效的镜像分发方式（如 BitTorrent），有可能改善下载体验。官方也偶尔提供了百度网盘供用户使用。~~这就看你是选择 100K/s 还是 101K/s 啦……~~

>**思考题**
>
>>“从技术角度来看，通过采用更高效的镜像分发方式（如 BitTorrent），有可能改善下载体验。”明明有更高效的分发方式（发生在 PCDN 投毒之前），为何难以推动技术兑现？
>
>你如何理解现代企业中，个人对企业是否存在一种虚无的责任感和职业道德？
>
>>归根结底，二者只是雇佣关系。职业道德，荣誉光环究竟是虚伪的面纱，还是人类文明不可或缺的自我欺骗。但是若将一切拉平，反而有悖于常识。
>
>你怎样理解？

从默认配置策略也可观察到这一问题：UOS 早期版本的默认安装方案仅为系统盘分配约 20 GB 空间，对于日常使用而言容易快速耗尽。用户只能自学成才，在拿到电脑没几周后就被迫重装系统，学习如何自定义分区。而剩下 50% 的其余未分配空间被设计用于系统备份与还原功能，其机制更接近于完整的系统镜像恢复。若用户采用自定义分区方案，则可能失去原厂提供的系统还原功能。这是一个两难选择。后续版本虽已支持调整系统分区大小，但默认安装方案在较长时期内仍未改变。

中标麒麟系统曾因未及时修复诸如 ZIP 压缩包解压乱码等常见基础问题而受到用户批评。

一个现实问题是，对于需要离线部署的内网机器，及时安装[安全补丁](https://src.uniontech.com/#/security_advisory_detail?utsa_id=UTSA-2024-003941)可能存在困难。由于 Linux 系统更新（尤其是涉及底层库时）常存在复杂的依赖关系，在内网固定版本环境中单独安装某个安全补丁，可能会遇到依赖不满足的问题。这是离线环境软件维护中普遍存在的挑战，在现有依赖管理模式下较难彻底规避。其安全漏洞公告页面的呈现格式经过多次迭代才趋于规范。

> **思考题**
>
> 什么是 Linux 操作系统根社区？
>
> - 从 Linux kernel 和其他开源组件而构建，不依赖上游发行版社区
>
> - 采用开源社区运行模式，有大量的外部个人贡献者与企业参与
>
> - 被广泛认可，衍生出不同分支或下游社区
>
> - 与各开源组件社区沟通畅通，并持续回馈自己的能力
>
>   ——[[社区新闻] 深度社区全新规划：打造中国主导的桌面系统根社区！](https://bbs.deepin.org/post/237175)
>
> > ① 如果一个操作系统，长得像 Debian，运行的软件也都来自 Debian，内核也一模一样，那么你凭什么说他是 Ubuntu？
> >
> > ② 根社区的“根”到底在哪？他们究竟维护着什么“根”？他们的“根”遵循 GPL 了吗？

### Arch Linux/Manjaro

Arch Linux 在中文社区中存在一些非正式的社区戏称：“**[邪教](https://zh.moegirl.org.cn/zh-hans/Arch_Linux%E5%A8%98) 和 [洗发水](https://bbs.archlinuxcn.org/viewtopic.php?id=694)**”。这是一个以滚动更新模式著称的 Linux 发行版，因其高度的可定制性和软件的新颖度吸引了许多用户。

然而，滚动更新模式也意味着系统可能面临更高的不稳定风险。随着系统中安装的软件包数量增加，因依赖冲突或版本不兼容导致问题的概率也可能上升。有观点认为，通过仔细阅读官方更新公告可以规避多数问题。但这要求用户具备较高的主动维护意识和排查能力。

Arch Linux 的主要优势在于软件包版本非常新。但并非所有软件都如此，部分特定领域的工具包（如某些 R 语言包）可能不如其他发行版（如 FreeBSD）更新及时。Arch Linux 在技术社区中拥有很高的知名度。

Arch Linux 官方仓库（Official Repository）的软件包数量有限，用户通常需要启用 Arch 用户软件仓库（Arch User Repository，AUR）来获取更丰富的软件。而 AUR 源是[未经过任何代码审查的](https://wiki.archlinux.org/title/Arch_User_Repository)（`Warning: AUR packages are user-produced content. These PKGBUILDs are completely unofficial and have not been thoroughly vetted. Any use of the provided files is at your own risk.`，`警告： AUR 中的软件包是由其他用户编写的，这些 PKGBUILD 完全是非官方的，未经彻底审查。使用这些文件的风险由您自行承担。`）实际上缺乏系统性的集中审查机制：恶意或高风险脚本经常被提交其中。虽然构建过程在受限环境中进行，但无法保证生成的软件包本身是安全的。这类似于任何未经严格审核的软件来源（包括部分官方应用商店）都可能存在恶意软件。

这并非危言耸听，AUR 中确实曾[发现](https://www.linuxuprising.com/2018/07/malware-found-on-arch-user-repository.html?m=1)存在恶意软件包。

正如 FreeBSD 开发者 Warner Losh 所说，“如今，在开源项目处于日益恶劣的工作环境下，一些看似多余的步骤却往往是必要的。”

### NixOS

首先，读者不必被 NixOS 提出的一系列术语所困扰，其中部分概念在实际使用中容易被误解。

其核心理念并非简单的“OS as Code”，其包管理与配置方式在某些方面与 Node.js 的依赖管理有相似之处。 ~~它并不是什么“OS as Code”，而是“OS as Node.js”~~

对于熟悉声明式配置和函数式包管理理念的用户（尤其是有 Node.js 生态经验者），这个系统使用起来比大多数 Linux 发行版都要简单得多，而不一定如部分宣传中所描述的那样晦涩难用。

本质上，NixOS 将声明式和函数式的依赖管理范式应用到了整个操作系统层面。~~NixOS 就是把 Node.js 做成了一款系统~~

NixOS 强调可重现的系统构建。其配置文件（如 `/etc/nixos/configuration.nix`）、依赖锁定（如 `flake.lock` 文件）等机制，在理念上与 Node.js 的 `package.json` 和 `package-lock.json` 有相通之处：在某些情况下，错误提示并不能直观反映问题本身，例如将依赖缺失提示为语法错误。

- **声明式配置**：系统的所有配置集中在一个声明式文件中（如 `/etc/nixos/configuration.nix`），类似于 Node.js 项目中的 `package.json`。
- **Flakes**：这是一个实验性功能，提供了更可重现的依赖管理和项目结构，其锁定文件（`flake.lock`）的作用类似于 `package-lock.json`。
- **可重现性**：基于声明的配置和锁定的依赖，可以精确地复现整个系统环境。
- **无依赖冲突**：通过为每个依赖创建独立存储路径来避免冲突。但这可能导致存储占用较大，且旧版本包需要手动清理。~~存在较多类似 node_modules 的冗余存储，清理成本较高~~
- **可回滚**：每次系统更新（通过 `nixos-rebuild switch`）都会生成新的系统代际（Generation，即新的启动选项），允许用户轻松回滚到任意历史版本。切换后通常需要重启以完全生效。

Node.js 的依赖存储在 `node_modules` 目录，而 Nix/NixOS 的所有包则存储在 `/nix/store` 目录下。

与 Node.js 生态存在多个包管理器（如 npm、yarn、bun、pnpm）类似，Nix 生态中也出现了不同的工具和前端（如 Nix、NixOS with Flakes、Nix with Home Manager），带来了选择的多样性，也可能造成一定的生态碎片化。~~并且从现状看，NixOS 正在重走 Node.js 的老路~~

~~因此，喜欢 Node.js 的人肯定很喜欢这个系统，讨厌 Node.js 的人自然也喜欢不起来 NixOS。~~

### 参考文献

- [Benefits of Gentoo](https://wiki.gentoo.org/wiki/Benefits_of_Gentoo)
- [The philosophy of Gentoo](https://www.gentoo.org/get-started/philosophy/)，Gentoo 设计哲学
- [Arch compared to other distributions](https://wiki.archlinux.org/title/Arch_compared_to_other_distributions)，翻译[在这里](https://wiki.archlinuxcn.org/wiki/Arch_%E4%B8%8E%E5%85%B6%E4%BB%96%E5%8F%91%E8%A1%8C%E7%89%88%E7%9A%84%E6%AF%94%E8%BE%83)
- 《C++ 语言的设计和演化》，[美] Bjarne Stroustrup，译者：裘宗燕，人民邮电出版社，ISBN 9787115497116
