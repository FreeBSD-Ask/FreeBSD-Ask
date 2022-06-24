# 第二节 系统安装

自树莓派 3B+ 开始，无需任何改动，系统即可从 U 盘启动，经过测试了 FreeBSD 12/13/14 都是支持的，但是速度非常慢，一方面树莓派使用 USB2.0 极大的限制的总线速度，另一方面可能是玄学问题。（笔者用的是东芝（TOSHIBA）64GB USB3.0 U 盘 U364 高速迷你车载 U 盘）。

因此不建议使用 U 盘启动，慢的我要打年年猫，年年猫是谁？是一只调皮的野生狸花猫而已。

我们所有要准备的有树莓派 4 板子一块，网线一段，存储卡一枚。从 FreeBSD.org 下载适用于树莓派 4 的镜像:

https://download.freebsd.org/ftp/releases/arm64/aarch64/ISO-IMAGES/13.0/FreeBSD-13.0-RELEASE-arm64-aarch64-RPI.img.xz

下载后解压缩。使用 rufus 刻录。插入网线，将存储卡插入树莓派，通电等待约五分钟，查看路由器后台获取 IP 。

**注意：** 刻录完需要挂载 FAT 分区 替换里面的所有文件，否则会启动花屏，替换的文件路径为：

https://github.com/FreeBSD-Ask/FreeBSD-rpi4-firmware

使用 XShell 即可登录树莓派。用户名密码均为 `freebsd` 。root 需要登录后输入 `su`，密码为 `root` 。

可通过更改 `/etc/ssh/sshd_config` 文件来开启 root 账户的 ssh 远程登录权限。

方法：

编辑 `/etc/sh/sshd_config` （注意是 sshd 不是 ssh ！这是两个文件），修改或者加入

```
PermitRootLogin yes #允许 root 登录
PasswordAuthentication yes # 设置是否使用口令验证。
```

（也可以把对应行前面的注释 # 去掉，注意 `PermitRootLogin` 一行默认是 no，去掉后要改成 yes 。即 `PermitRootLogin yes` ）。

然后重启服务：

```
# server sshd restart
```

然后就是时间设置问题，树莓派没有板载的纽扣电池确保 CMOS 时钟准确。所以完全依靠 NTP 服务来校正时间，如果时间不准确，将影响很多服务的运行，比如无法执行 portsnap fetch 命令。

方法很简单：

在 /etc/rc.conf 中加入

```
ntpd_enable="YES"
ntpdate_enable="YES"
ntpdate_program="ntpdate"
ntpdate_flags="0.cn.pool.ntp.org"
```

然后开启时间服务器：

```
# service ntpdate start
```

输入 `# date` 查看时间，完成校时。我国使用 UTC+8 北京时，虽然不更改不会影响软件使用，但看起来不方便，可通过 `# bsdconfig` 命令将地区调整到亚洲 /中国 /上海。

树莓派应该会自动接通互联网，所以不必考虑联网问题。

CPU 频率调整（600MHZ 到 1500MHZ）：

```
# sysrc powerd_enable="YES"
# service powerd restart
```
