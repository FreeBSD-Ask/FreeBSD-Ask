# 第一节 三种虚拟机与 FreeBSD 版本比较

## FreeBSD 版本比较

已知 FreeBSD 有以下版本：rc、beta、release、current、stable。

release 是绝对的 stable，而 stable 和 current 都是开发分支，不太稳定。

Current 相对稳定后会推送到 stable，但是不保证 stable 没有大的 Bug，只是确保其 ABI 兼容。

### FreeBSD 版本选择

其中 rc 和 beta 都是测试版本；

日常使用应该选择 release 版本，当有多个 release 版本时，应该选择最新的一个；

如果硬件比较新或者需要测试 ax200 网卡，应该选择 current 版本，是滚动开发版。

注意：只有 rc、beta 和 release 才能使用 freebsd-update 命令更新系统（且是一级架构），其余系统均需要通过源代码编译的方式更新系统。

## 三种虚拟机比较

个人计算机上常用的虚拟机有两种，一是 Virtual Box，另一个是 Vmware Workstation Pro。

一般来说，在 Windows 系统上建议使用Vmware Workstation Pro （以下简称 VM），在Linux 系统上建议使用 Virtual Box（以下简称 VB）。

VM 是闭源的由商业公司提供的，是需要付费的，可用免费试用，也有免费版本 _VMware Workstation Player_；VB 是 Oracle 公司的开源产物，是免费的。

就个人而已，VM 在实际使用中 Bug 会比 VB 少一些：VB 会有一些奇奇怪怪的问题（详见 VB 章节），且很花时间去排除解决。但是为了给与大家更多自由，我们将两种虚拟机的安装使用方法都提供给大家。

