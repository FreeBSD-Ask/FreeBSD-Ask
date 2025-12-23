# 5.7 使用 freebsd-update 更新 FreeBSD

> **注意：**
>
> 只有一级架构的 RELEASE 版本才提供该更新源。也就是说，CURRENT 和 STABLE 不提供该源。关于架构的支持等级说明请参见： [Supported Platforms](https://www.freebsd.org/platforms)

>**注意**
>
>ZFS 相关升级请参见 ZFS 章节。

## 历史

FreeBSD 提供了实用工具 `freebsd-update`，用于安装系统更新，包括升级到新的大版本。`freebsd-update` 在 FreeBSD 7.0-RELEASE 中获得了正式支持。

### 参考文献

- [FreeBSD 7.0-RELEASE Announcement](https://www.freebsd.org/releases/7.0R/announce/) 指出 freebsd-update(8) 是官方支持的二进制更新方式，不仅可用于升级到新版本，还可用于安全修复和勘误补丁的更新。

## 将默认文本编辑器替换为较简单的编辑器

### bash、zsh 或 sh（14.0 及以上版本）

```sh
# export EDITOR=/usr/bin/ee # 切换 vi 为 ee，默认为 nvi 
# export VISUAL=/usr/bin/ee # 切换 vi 为 ee
```

### csh（14.0 以下版本）

```sh
# setenv EDITOR /usr/bin/ee # 切换 vi 为 ee，默认为 nvi 
# setenv VISUAL /usr/bin/ee # 切换 vi 为 ee
```

### 检查与验证

- 查看当前终端默认文本编辑器：

```sh
# echo $EDITOR
/usr/bin/ee
```

- 查看当前终端可视化文本编辑器：

```sh
# echo $VISUAL
/usr/bin/ee
```

## 常规补丁/安全更新（`X.Y-RELEASE`——>`X.Y-RELEASE-pN`）

>**警告**
>
>无论是大版本更新、点版本更新还是常规更新，都应该先执行一次该流程。不可绕过，否则可能会出现不可预料的后果。

### FreeBSD 版本检查

```sh
# freebsd-version -kru
14.3-RELEASE
14.3-RELEASE
14.3-RELEASE
```

### 进行更新

- 获取更新

```sh
# freebsd-update fetch
```

当出现类似如下信息时：

```sh
usr/include/c++/vl/trllvector usr/include/c++/vl/trllversion usr/include/c++/v1/trl/wchar.h usr/include/c++/v1/tr1/wctype.h usr/include/c++/v1/unwind-armh
usr/include/c++/v1/unwind-itaniumh usr/include/c++/v1/unwindh
usr/include/crypto/ cryptodevh usr/include/crypto/cbcmac.h usr/include/crypto/deflate.h usr/include/crypto/gfmult.h usr/include/crypto/gmac.h
usr/include/crypto/rijndael.h usr/include/crypto/rmd160.h usr/include/crypto/xform.h
usr/lib/clang/11.0.1/include
: q # 这里输入 q 再按回车键

上面列出的路径仅为示例输出，实际系统中的路径名称和数量可能会略有不同，以你自己机器上的实际显示为准。

这里列出的是发生变动的文件，你只需要在确认后输入字母 q（代表“quit”，退出）并按回车键即可。

然后安装更新：

```sh
# freebsd-update install
```

### FreeBSD 版本检查

- 查看更新后的 FreeBSD 版本：

```sh
# freebsd-version -kru
14.3-RELEASE-p5
14.3-RELEASE
14.3-RELEASE-p6
```

> **注意：**
>
> 有时候补丁不涉及内核，内核版本就不会变，用 `uname -r` 无法体现，但用户空间版本会发生变化。因此你可能会看到两个版本号，应以较高者为准。

重启系统：

```sh
# reboot
```

再查看 FreeBSD 版本：

```sh
# freebsd-version -kru
14.3-RELEASE-p5
14.3-RELEASE-p5
14.3-RELEASE-p6
```

## 大版本更迭（`X.Z-RELEASE-pN`——>`A.0-RELEASE`）

>**注意**
>
>`freebsd-update` 下载慢不是因为其更新源在境外（你使用境外服务器更新一样慢；并且在 freebsdcn 境内源还生效的那些日子里，亦如此）。这可能与其设计缺陷有关，`freebsd-update` 是一个由数千行组成的纯 shell 脚本。[这是一个始终普遍存在的问题](https://freebsd-questions.freebsd.narkive.com/xjVoetUM/why-is-freebsd-update-so-horrible-slow)。

**以 FreeBSD 14.3-RELEASE 升级至 15.0-RELEASE 为例**

### 检查版本

```sh
# freebsd-version -kru
14.3-RELEASE-p5
14.3-RELEASE-p5
14.3-RELEASE-p6
```

>**警告**
>
>由于大版本间的变动，可能影响 `freebsd-update` 更新工具本身，所以一定要：
>
>先更新到当前版本最新的补丁版本（如 `X.Y-RELEASE-pN`），然后再更新到最新的点版本（如 `X.Z-RELEASE`）.
>
>接下来：更新到最新的点版本及该点版本上最新的补丁版本（如 `X.Z-RELEASE-pN`）
>
>最后：进行大版本（`X.Z-RELEASE-pN`——>`A.0-RELEASE`）的更迭。
>
>参见 [libsys.so.7 not found when upgrading userland with legacy freebsd-update](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=289769)。

### 更新到 15.0-RELEASE

升级系统到 FreeBSD 15.0-RELEASE 版本：

```sh
# freebsd-update upgrade -r 15.0-RELEASE

……当出现类似于下列信息时，按照下方提示操作……

src component not installed, skipped
Looking up update.FreeBSD.org mirrors... 3 mirrors found.
Fetching metadata signature for 14.3-RELEASE from update1.freebsd.org... done.
Fetching metadata index... done.
Fetching 2 metadata patches.. done.
Applying metadata patches... done.
Fetching 1 metadata files... done.
Inspecting system... done.

The following components of FreeBSD seem to be installed:
kernel/generic kernel/generic-dbg world/base world/lib32

The following components of FreeBSD do not seem to be installed:
world/base-dbg world/lib32-dbg

Does this look reasonable (y/n)? y # 在这里输入 y，然后回车即可，在检查基本组件的安装情况。

Fetching metadata signature for 15.0-RELEASE from update1.freebsd.org... done.
Fetching metadata index... done.
Fetching 1 metadata patches. done.
Applying metadata patches... done.
Fetching 1 metadata files... done.
Inspecting system...

…………这里在检查系统，从上面的回车到这里需要等待约 10 分钟…………

Fetching metadata signature for 15.0-RELEASE from update1.freebsd.org... done.
Fetching metadata index... done.
Fetching 1 metadata patches. done.
Applying metadata patches... done.
Fetching 1 metadata files... done.
Inspecting system... done.
Fetching files from 14.3-RELEASE for merging... done.
Preparing to download files... done.

…………这里在准备要下载的文件，需要等待约 15 分钟…………

Fetching 6735 patches.....10....20....30....40....50....60....70....80....90.
 
………………下面需要等待约 30 分钟。注意，当跨大版本更新时，有时候需要等待 5 小时或更长时间，这都是正常的。………………

....100....110....120....130....140....150....160....170....180....190....200

…………中间省略………………

20....6630....6640....6650....6660....6670....6680....6690....6700....6710....6720....6730.. done.
Applying patches... 

………………打补丁，需要等待约 5 分钟………………

Applying patches... done.
Fetching 880 files... ....10....20....30....4

………………省略一部分进度条………………

0....880 done.
Attempting to automatically merge changes in files... done.

The following file could not be merged automatically: /etc/pkg/FreeBSD.conf
Press Enter to edit this file in /usr/bin/ee and resolve the conflicts
manually...

……这里提示我们按回车键编辑一些无法自动合并需要手动编辑的文件……

The following changes, which occurred between FreeBSD 14.3-RELEASE and
FreeBSD 15.0-RELEASE have been merged into /etc/login.conf:
--- current version
+++ new version

……此处列出的是发生变动的文件，省略一部分输出……

 #site:\
-#      :ignoretime:\
 #      :passwordtime@:\
 #      :refreshtime@:\
 #      :refreshperiod@:\
 #      :sessionlimit@:\
 #      :autodelete@:\
Does this look reasonable (y/n)? # 输入 y 回车，这里在确认系统文件的变动

The following changes, which occurred between FreeBSD 14.3-RELEASE and
FreeBSD 15.0-RELEASE have been merged into /etc/pkg/FreeBSD.conf:
--- current version
+++ new version

……此处列出的是发生变动的文件，省略一部分输出……

Does this look reasonable (y/n)?  # 输入 y 回车，这里在确认系统文件的变动

The following changes, which occurred between FreeBSD 14.3-RELEASE and
FreeBSD 15.0-RELEASE have been merged into /etc/ssh/sshd_config:
--- current version
+++ new version

……此处列出的是发生变动的文件，省略一部分输出……

 # override default of no subsystems
Does this look reasonable (y/n)? # 输入 y 回车，这里在确认系统文件的变动

The following files are affected by updates. No changes have
been downloaded, however, because the files have been modified
locally:
/etc/ssl/cert.pem
(END) # 这里是发生变动的文件，你只需要在确认后输入字母 `q`（代表“quit”，退出）再按回车键即可。

# 上面列出的路径仅为示例输出，实际系统中的路径名称和数量可能会略有不同，以你自己机器上的实际显示为准。

The following files will be removed as part of updating to
15.0-RELEASE-p0:
/.cshrc
/.profile
/boot/kernel/callout_test.ko
/boot/kernel/geom_bde.ko
/boot/kernel/geom_vinum.ko

…………中间省略，这些是将被删除的文件………………

/usr/share/examples/sound/sndstat_nv.c
: # 这里输入 q，确认变动，直至没有新内容出现

…………中间省略………………

The following files will be added as part of updating to
15.0-RELEASE-p0:
/boot/firmware/iwm3160fw
/boot/firmware/iwm3168fw
/boot/firmware/iwm7260f

…………中间省略这些是新增的文件………………

/boot/kernel/nvmf_tcp.ko
/boot/kernel/nvmf_transport.ko
/boot/kernel/nvmft.ko
/boot/kernel/p9fs.ko
: # 这里输入 q，确认变动，直至没有新内容出现

The following files will be updated as part of updating to
15.0-RELEASE-p0:
/COPYRIGHT
/bin/[
/bin/cat

…………中间省略这些是新增的文件………………

/bin/kenv
/bin/kill
/bin/link
/bin/ln
/bin/ls
/bin/mkdir
/bin/mv
/bin/nproc
To install the downloaded upgrades, run 'freebsd-update [options] install'.
```

运行 `freebsd-update install` 以安装更新：

```sh
# freebsd-update install
src component not installed, skipped
Creating snapshot of existing boot environment... done.
Installing updates...
Kernel updates have been installed.  Please reboot and run
'freebsd-update [options] install' again to finish installing updates.
```

内核更新已经安装：

```sh
# freebsd-version -kru
15.0-RELEASE
14.3-RELEASE-p5
14.3-RELEASE-p6
```

可以看到，当前已安装内核的版本和补丁级别是 15.0-RELEASE。但用户空间和当前正在运行的系统仍是 14.3-RELEASE，因此需要按照 `freebsd-update` 的提示进行重启：


```sh
# reboot
```

运行 `freebsd-update install` 安装用户空间的更新部分：

```sh
# freebsd-update install
src component not installed, skipped
Creating snapshot of existing boot environment... done.
Installing updates...
Restarting sshd after upgrade
Performing sanity check on sshd configuration.
Stopping sshd.
Waiting for PIDS: 906.
Performing sanity check on sshd configuration.
Starting sshd.

Completing this upgrade requires removing old shared object files.
Please rebuild all installed 3rd party software (e.g., programs
installed from the ports tree) and then run
'freebsd-update [options] install' again to finish installing updates.
```


重新安装 `pkg` 本身，将其 ABI 更新到 15.0-RELEASE：

```sh
# pkg bootstrap -f
The package management tool is not yet installed on your system.
Do you want to fetch and install it now? [y/N]: y # 此处输入 y 后回车
Bootstrapping pkg from pkg+https://pkg.FreeBSD.org/FreeBSD:15:amd64/quarterly, please wait...
Verifying signature with trusted certificate pkg.freebsd.org.2013102301... done
Installing pkg-2.4.2...
package pkg is already installed, forced install
Extracting pkg-2.4.2: 100%
```

将第三方程序的 ABI 一并更新到 15.0-RELEASE：

```sh
# pkg upgrade
Updating nju repository catalogue...
Fetching meta.conf:   0%
Fetching data.pkg: 100%    7 MiB   7.6MB/s    00:01    
Processing entries: 100%
nju repository update completed. 35765 packages processed.
All repositories are up to date.
Updating database digests format: 100%
Checking for upgrades (215 candidates): 100%
Processing candidates (215 candidates): 100%
The following 223 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
	ceres-solver: 2.2.0_10

…………中间省略………………

The process will require 45 MiB more space.
687 MiB to be downloaded.

Proceed with this action? [y/N]:  # 此处输入 y 再回车即可

…………中间省略………………

Proceed with this action? [y/N]:  # 此处输入 y 再回车即可，可能会出现多次，下同
```

第三方程序的更新至此完成。

再次执行 `freebsd-update` 以结束更新流程。


```sh
# freebsd-update install
src component not installed, skipped
Creating snapshot of existing boot environment... done.
Installing updates... done.
```

验证操作系统版本：

```sh
# freebsd-version -kru
15.0-RELEASE
15.0-RELEASE
15.0-RELEASE
```

系统更新完成。

## 更新 EFI 引导

### 背景介绍

>**警告**
>
>对于使用 EFI 引导的系统，EFI 系统分区（ESP）上有引导加载程序的副本，用于固件引导内核。如果根文件系统是 ZFS，则引导加载程序必须得能读取 ZFS 引导文件系统。在系统升级后，且执行 `zpool upgrade` 前，必须先更新 ESP 上的引导加载程序，否则系统可能无法引导。虽然不是强制性的，但在 UFS 作为根文件系统时亦应如此。

可以使用命令 `efibootmgr -v` 来确定当前引导加载程序的位置。`BootCurrent` 显示的值是用于引导系统的当下引导配置的编号。输出的相应条目以 `+` 开头，如

```sh
# efibootmgr -v
Boot to FW : false
BootCurrent: 0004
BootOrder  : 0004, 0000, 0001, 0002, 0003
+Boot0004* FreeBSD HD(1,GPT,f83a9e2f-bd87-11ef-95b7-000c29761cd2,0x28,0x82000)/File(\efi\freebsd\loader.efi) # 就是这条
                      nda0p1:/efi/freebsd/loader.efi (null)
 Boot0000* EFI VMware Virtual NVME Namespace (NSID 1) PciRoot(0x0)/Pci(0x15,0x0)/Pci(0x0,0x0)/NVMe(0x1,00-00-00-00-00-00-00-00)
 Boot0001* EFI VMware Virtual IDE CDROM Drive (IDE 1:0) PciRoot(0x0)/Pci(0x7,0x1)/Ata(Secondary,Master,0x0)
 Boot0002* EFI Network PciRoot(0x0)/Pci(0x11,0x0)/Pci(0x1,0x0)/MAC(000c29761cd2,0x0)
 Boot0003* EFI Internal Shell (Unsupported option) MemoryMapped(0xb,0xbeb4d018,0xbf07e017)/FvFile(c57ad6b7-0515-40a8-9d21-551652854e37)


Unreferenced Variables:
```

ESP 通常已经挂载到了 **/boot/efi**。如果没有，可手动挂载之，使用 `efibootmgr` 输出中列出的分区（本例为 `nda0p1`）：`mount_msdosfs /dev/nda0p1 /boot/efi`。有关另一则示例，请参阅 [loader.efi(8)](https://man.freebsd.org/cgi/man.cgi?query=loader.efi&sektion=8&format=html)。

在 `efibootmgr -v` 输出的 `File` 字段中的值，如 `\efi\freebsd\loader.efi`，是 EFI 上正在使用的引导加载程序的位置。若挂载点是 **/boot/efi**，则此文件为 `/boot/efi/efi/freebsd/loader.efi`。（在 FAT32 文件系统上大小写不敏感；FreeBSD 使用小写）`File` 的另一个常见值可能是 `\EFI\boot\bootXXX.efi`，其中 `XXX` 是 amd64（即 `x64`）、aarch64（即 `aa64`）或 riscv64（即 `riscv64`）；如未配置，则为默认引导加载程序。应将 **/boot/loader.efi** 复制到 **/boot/efi** 中的正确路径来更新已配置及默认的引导加载程序。

### 更新方法


在版本更新后，在启动菜单出现之前，可能出现下面的画面

>**注意**
>
>该界面出现的时间非常短暂，约只有 20 毫秒。可用相机拍摄观察。

![loader 更新提示界面](../.gitbook/assets/loader.png)

即

```sh
**************************************************************
**************************************************************
*****                                                    *****   
*****      BOOT LOADER IS TOO OLD, PLEASE UPGRADE.       *****
*****                                                    *****
**************************************************************
************************************************************** 
```

这表明 loader 需要更新。还可以使用命令进行版本验证：

```sh
# strings /boot/efi/efi/freebsd/loader.efi | grep FreeBSD | grep EFI  # 查看 EFI 引导加载器版本
DFreeBSD/amd64 EFI loader, Revision 1.1

# strings /boot/loader.efi | grep FreeBSD | grep EFI  # 查看 /boot/loader.efi 的 EFI 引导加载器版本
DFreeBSD/amd64 EFI loader, Revision 3.0
```

此处命令参考了手册 [loader.efi](https://man.freebsd.org/cgi/man.cgi?query=loader.efi) 中的例子。`/boot/efi/efi/freebsd/loader.efi` 为当前正在使用的 loader（版本确实较旧）。

将 `/boot/loader.efi` 复制到 EFI 系统分区的 FreeBSD 目录下进行更新：

```sh
# cp /boot/loader.efi /boot/efi/efi/freebsd/
```

>**警告**
>
>请先更新 loader，再更新 ZFS 版本！

>**重要**
>
>非 EFI、bootcode、ZFS 等相关更新请自行查阅相关章节。


## 故障排除与未竟事宜

### 回滚更新

回滚最近一次系统更新：

```sh
# freebsd-update rollback
```

### pkg 找不到 `.so` 文件

终端执行命令强制初始化 pkg 包管理器：

```sh
# pkg bootstrap -f
```

### FreeBSD 升级出错，缺少 ntp 用户

终端执行命令：

```sh
# pw groupadd ntpd -g 123  # 创建 ntpd 用户组，GID 为 123
# pw useradd ntpd -u 123 -g ntpd -h - -d /var/db/ntp -s /usr/sbin/nologin -c "NTP Daemon"  # 创建 ntpd 用户，UID 为 123，主目录 /var/db/ntp，禁止登录，仅用于 NTP 守护进程
```
