# 第 2.1 节 三种虚拟机与 FreeBSD 版本比较

## FreeBSD 版本比较

已知 FreeBSD 有以下版本： alpha、rc、beta、release、current、stable。

release 是绝对的“stable”，是可以日常/服务器使用的稳定版。而 stable 和 current 都是开发分支，都是不稳定的。所以 FreeBSD 的 stable 与其他发行版的“稳定版”的概念并不一致，反而是一种“开发版”。

alpha 是 current 进入 release 的第一步。具体是 current --> alpha（进入 stable 分支）--> beta --> rc --> release。

stable 相对稳定后会推送到 current，但是不保证二者没有大的 bug，只是 stable 确保其 ABI 是兼容与大版本的。

### FreeBSD 版本选择

其中 rc 和 beta 都是测试版本；

日常使用应该选择 release 版本，当有多个 release 版本时，应该选择最新的一个；

如果硬件比较新或者需要进行某些测试，应该选择 current 版本，是滚动开发版。

注意：只有 rc、beta 和 release 才能使用 freebsd-update 命令更新系统（[且是一级架构](https://www.freebsd.org/platforms/)），其余系统均需要通过源代码编译的方式更新系统。

## 三种虚拟机比较

### Virtual Box 与 VMware Workstation Pro

个人计算机上常用的虚拟机有两种，一是 Virtual Box，另一个是 VMware Workstation Pro。

一般来说，在 Windows 系统上建议使用 VMware Workstation Pro （以下简称 VM），在 Linux 系统上建议使用 Virtual Box（以下简称 VB）。

VM 是闭源的由商业公司提供的，是需要付费的，可用免费试用，也有免费版本 _VMware Workstation Player_；VB 是 Oracle 公司的开源产物，是免费的。

就个人而言，VM 在实际使用中 Bug 会比 VB 少一些：VB 会有一些奇奇怪怪的问题（详见 VB 章节），且很花时间去排除解决：对于我自己来说，VB 唯一好处就是支持 FreeBSD 的鼠标集成功能，不需要按键使虚拟机里的鼠标来回切换。但是 vb  不堪重用，休眠/恢复虚拟机往往需要几分钟的时间，而同样的操作，vm 只需要 3 秒钟。在忍无可忍的状态下，我恢复了 vm 的使用，卸载了 vb 虚拟机。

但是为了给与大家更多自由，我们将两种虚拟机的安装使用方法都提供给大家。

### Hyper-V

Hyper-V 是微软为 Windows 开发的虚拟机，分为 `Gen 1` 和 `Gen 2`。

`Gen 1` 和 `Gen 2` 区别如下：

| Hyper-V 代数 |    硬盘    |             启动引导              |
| :----------: | :--------: | :-------------------------------: |
|    Gen 1     | IDE + SCSI |              仅 MBR               |
|    Gen 2     |  仅 SCSI   | 仅 UEFI + 安全启动支持 + PXE 支持 |

系统快速创建的为 `Gen 2`。

>**注意：**
>
>使用 Gen 2 时请关闭安全启动，否则系统无法启动！点击设置： 点击“安全”——>取消勾选“启用安全启动。

| Hyper-V 代数 | FreeBSD 版本 |                                鼠标                                |  键盘  |                                              备注                                              |
| :----------: | :----------: | :----------------------------------------------------------------: | :----: | :--------------------------------------------------------------------------------------------: |
|    Gen 1     |     13.0     |                                支持                                | 不支持 |                                               /                                                |
|    Gen 2     |     13.0     | [不支持](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=221074) |  支持  |                          需要修改参数`sysctl kern.evdev.rcpt_mask=6`                           |
|    Gen 2     |     14.0     |                                支持                                |  支持  | 参见[源代码](https://cgit.FreeBSD.org/src/commit/?id=21f4e817fde79d5de79bfbdf180d358ca5f48bf9) |

### 使用 virtio 技术半虚拟化的虚拟机

> **注意：以下内容仅供参考，有待测试。如果你测试通过，请告知我们！**

根据反馈，在 VMware EXSI 等半虚拟化平台上安装或升级 FreeBSD 会遇到故障（如阿里云 virtio-blk 驱动会出问题），需要在开机时按`ESC`,然后输入 `set kern.maxphys=65536` 回车，再输入 `boot` 即可正常启动。安装好后需要在 `/boot/loader.conf` 加入 `kern.maxphys=65536` 以免每次开机重复操作。阿里云升级完成后可能会因为此类问题卡在引导界面，此时需要重启并进 VNC 再进行上述操作。

## 参考链接：

- [SystemTuning](https://wiki.freebsd.org/SystemTuning)
- [FreeBSD13 を Hyper-V 環境にインストールしてみた所感](https://qiita.com/nanorkyo/items/d33e1befd4eb9c004fcd)

