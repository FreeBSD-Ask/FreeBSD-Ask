# 4.12 进程与守护进程

## 进程与守护进程概述

FreeBSD 是一个多任务操作系统。任何时刻运行的程序均称为进程。每个运行的命令至少启动一个新进程，此外还有许多由 FreeBSD 运行的系统进程。

每个进程都由一个称为进程 ID（PID）的数字唯一标识。与文件类似，每个进程都有一个所有者和组，所有者和组权限用于确定进程可以打开哪些文件和设备。大多数进程还有一个启动它们的父进程。例如，Shell 是一个进程，在 Shell 中启动的任何命令都是以 Shell 为父进程的进程。例外是一个名为 init(8) 的特殊进程，其始终是系统启动时的首个进程，并且始终具有 PID 1。在 FreeBSD 中，所有进程都是以某个账户的名义启动的。

Port `sysutils/htop` 能够直观地呈现这一点（注意 `△USER` 这列）：

```sh
$ htop
  PID△USER       PRI  NI  VIRT   RES S   CPU% MEM%   TIME+  Command
    1 root        20   0 12724  1324 S    0.0  0.0  0:00.08 /sbin/init
  216 root        20   0 36172  7308 S    0.0  0.1  0:00.77 ├─ /usr/local/bin/vmtoolsd -c /usr/local/share/vmware-tools/to
  400 root        48   0 14188  2684 S    0.0  0.0  0:00.00 ├─ dhclient: system.syslog
  403 root         4   0 14188  2760 S    0.0  0.0  0:00.00 ├─ dhclient: em0 [priv]
  481 _dhcp       20   0 14192  2808 S    0.0  0.0  0:00.01 ├─ dhclient: em0
  596 root        20   0 15444  4204 S    0.0  0.1  0:00.05 ├─ /sbin/devd
  800 root        20   0 13904  2792 S    0.0  0.0  0:00.02 ├─ /usr/sbin/syslogd -s
  867 messagebus  20   0 15188  4492 S    0.0  0.1  0:00.29 ├─ /usr/local/bin/dbus-daemon --system
  870 root        20   0 14120  2456 S    0.0  0.0  0:00.06 ├─ /usr/sbin/moused -p /dev/psm0 -t auto
  898 ntpd        20   0 24564  5848 S    0.0  0.1  0:00.06 ├─ /usr/sbin/ntpd -p /var/db/ntp/ntpd.pid -c /etc/ntp.conf -f
  944 root        68   0 23508  9560 S    0.0  0.1  0:00.00 ├─ sshd: /usr/sbin/sshd [listener] 0 of 10-100 startups
  947 root        20   0 13944  2576 S    0.0  0.0  0:00.02 ├─ /usr/sbin/cron -s
  952 root        20   0 56736 23700 S    0.0  0.3  0:00.04 ├─ /usr/local/bin/sddm
  980 root        20   0  257M  124M S    1.0  1.5  0:04.83 │  ├─ /usr/local/libexec/Xorg -nolisten tcp -background none -
  993 root        23   0 50208 27572 S    0.0  0.3  0:00.02 │  └─ /usr/local/libexec/sddm-helper --socket /tmp/sddm-auth-4
  994 ykla        68   0 19992  4620 S    0.0  0.1  0:00.01 │     └─ /usr/local/bin/ck-launch-session /usr/local/bin/start
 1005 ykla        68   0  128M 67736 S    0.0  0.8  0:00.13 │        └─ /usr/local/bin/startplasma-x11
 1010 ykla        68   0  128M 68184 S    0.0  0.8  0:00.25 │           └─ /usr/local/bin/plasma_session
 1017 ykla        20   0  773M  190M S    0.0  2.3  0:01.33 │              ├─ /usr/local/bin/kded6
 1018 ykla        20   0  676M  262M S    0.0  3.2  0:30.96 │              ├─ /usr/local/bin/kwin_x11
```

有些程序不设计为持续接收用户输入，并在启动后即与终端断开连接。例如，Web 服务器响应 Web 请求而非用户输入，邮件服务器是此类应用程序的另一个例子。这些类型的程序被称为守护进程（daemon）。术语“daemon”来自希腊神话，代表一种非善非恶的实体，它无形中执行有用的任务。正因如此，BSD 的吉祥物被设计为一个穿着运动鞋、手持草叉的快乐守护进程形象。在 Windows 系统中，这类程序被称为“服务”，可在任务管理器中查看。

这些长期在后台运行的服务通常命名为 `xxxd`，例如 `sshd`、`ntpd`，其中的 `d` 表示守护进程（[daemon](https://www.freebsd.org/copyright/daemon/)），这是 UNIX 系统的通用命名约定。例如，BIND 是 Berkeley Internet Name Domain，但实际执行的程序名为 named。Apache Web 服务器程序是 httpd，数据同步 Rsync 进程是 rsyncd。这只是一个命名约定，例如数据库应用程序 MySQL 的守护进程是 mysql-server，而不是 mysqld。

## 查看进程

在某些情况下，带有 `ww` 选项的 `ps` 可能仍然被截断，因为内核中存储的命令行长度有限制。对于内核线程，命令字段可能显示为 `[ ]` 包裹的名称。

FreeBSD 的 `ps` 基于 4.4BSD。特别注意：FreeBSD 的 `-u` 是显示格式选项，用户过滤应使用 `-U`。FreeBSD 支持 `-G` 显示组。

用户只能向自己拥有的进程发送信号，root 用户可以向任何进程发送信号。SIGKILL 和 SIGSTOP 信号不可被捕获或忽略。特殊 PID：`0` 发送到同组所有进程，`-1` 发送到所有进程（root）或自己的所有进程。

要查看系统上运行的进程，可以使用 ps(1) 或 top(1)。

要显示当前运行进程的静态列表（包括它们的 PID、内存使用量和启动命令），使用 ps(1)。要以交互方式显示所有运行进程并每隔几秒更新显示以查看计算机正在做什么，使用 top(1)。

默认情况下，ps(1) 仅显示由当前用户拥有且正在运行的命令：

```sh
$ ps
 PID TT  STAT    TIME COMMAND
1971  0  Is   0:00.03 -sh (sh)
2183  1  Ss   0:00.05 -sh (sh)
2186  1  R+   0:00.00 ps
```

ps(1) 的输出由多列构成：

- PID 列显示进程 ID。PID 从 1 开始分配，上升到 99999，然后回到开头。但是，如果 PID 已被占用，则不会再分配。
- TT 列显示程序运行所在的 tty，STAT 显示程序的状态。
- TIME 是程序在 CPU 上运行的时间量，这通常不是程序启动以来的经过时间，因为大多数程序在需要花费 CPU 时间之前会花大量时间等待事情发生。
- COMMAND 是用于启动程序的命令。

有许多不同的选项可用于更改显示的信息。最有用的选项集之一是 `auxww`，其中：

- `a` 显示所有用户的所有运行进程的信息
- `u` 显示进程所有者的用户名和内存使用量
- `x` 显示守护进程的信息
- `ww` 使 ps(1) 显示每个进程的完整命令行，而不是在太长无法适应屏幕时截断

ps -auxww 示例：

```sh
$ ps -auxww
USER   PID   %CPU %MEM   VSZ   RSS TT  STAT STARTED      TIME COMMAND
root    11 1592.5  0.0     0   256  -  RNL  11:51   648:25.89 [idle]
root     0    0.0  0.1     0  4240  -  DLs  11:51     0:05.08 [kernel]

……省略部分输出……

_dhcp  792    0.0  0.1 14656  3532  -  ICs  11:51     0:00.04 dhclient: em0 (dhclient)
root  1211    0.0  0.1 14652  3156  -  Is   11:51     0:00.00 /usr/sbin/moused -p /dev/input/event5 -t evdev -I /var/run/moused.event5.pid

……省略部分输出……

root  1974    0.0  0.1 14816  3532  0  I    12:04     0:00.01 su
root  1975    0.0  0.1 14872  3728  0  I+   12:04     0:00.03 su (sh)
ykla  2183    0.0  0.1 14872  3728  1  Ss   12:28     0:00.05 -sh (sh)
ykla  2191    0.0  0.1 14956  3576  1  R+   12:31     0:00.00 ps -auxww
```

top(1) 的输出如下：

```sh
$ top
last pid:  2189;  load averages:    0.24,    0.13,    0.04        up 0+00:39:10  12:30:35
30 processes:  1 running, 29 sleeping
CPU:  0.0% user,  0.0% nice,  0.0% system,  0.0% interrupt,  100% idle
Mem: 26M Active, 21M Inact, 260M Wired, 2056K Buf, 3617M Free
ARC: 35M Total, 6321K MFU, 27M MRU, 128K Anon, 407K Header, 1467K Other
     19M Compressed, 52M Uncompressed, 2.76:1 Ratio
Swap: 8192M Total, 8192M Free

  PID USERNAME    THR PRI NICE   SIZE    RES STATE    C   TIME    WCPU COMMAND
 2183 ykla          1   0    0    15M  3728K wait     9   0:00   0.10% sh
 1623 ntpd          2   0    0    26M  7072K select  12   0:00   0.00% ntpd
 1783 root          1   0    0    15M  3708K ttyin    5   0:00   0.00% sh
 2179 root          1   3    0    25M    12M select  12   0:00   0.00% sshd-session
 1714 root          1   0    0    25M    11M select   5   0:00   0.00% sshd
 1756 root          1   1    0    14M  3076K nanslp  14   0:00   0.00% cron
 1496 root          1   0    0    14M  3456K kqread  15   0:00   0.00% syslogd
 1224 root          1   0    0    16M  4668K select   0   0:00   0.00% devd
 1967 root          1   1    0    25M    12M select  11   0:00   0.00% sshd-session
  792 _dhcp         1   0    0    14M  3532K select   1   0:00   0.00% dhclient
 2182 ykla          1   0    0    25M    12M select   4   0:00   0.00% sshd-session
 1970 ykla          1   0    0    25M    12M select   5   0:00   0.00% sshd-session
 1975 root          1   1    0    15M  3728K ttyin    1   0:00   0.00% sh
 1971 ykla          1   9    0    15M  3720K wait     9   0:00   0.00% sh
 1499 root          1   0    0    14M  3276K select  15   0:00   0.00% syslogd
 1638 root          1   0    0    14M  3160K kqread   8   0:00   0.00% moused
 1974 ykla          1   7    0    14M  3532K wait    15   0:00   0.00% su
```

输出分为两个部分。头部（示例命令为前 7 行）显示最后运行的进程的 PID、系统负载平均值（衡量系统繁忙程度的指标）、系统正常运行时间（自上次重启以来的时间）和当前时间。头部中的其他数字与运行中的进程数量、已使用的内存和交换空间数量，以及系统在不同 CPU 状态下花费的时间有关。如果加载了 ZFS 文件系统模块，ARC 行指示从内存缓存而非磁盘读取了多少数据。

头部下方是一系列列，包含与 ps(1) 输出类似的信息，如 PID、用户名、CPU 时间量和启动进程的命令。默认情况下，top(1) 还显示进程占用的内存空间量，分为两列：一列用于总大小，一列用于驻留大小。总大小是应用程序需要的内存量，驻留大小是它当前实际使用的量。top(1) 默认每两秒自动更新显示，可以使用 `-s` 指定不同的间隔，如 `-s4` 将每隔 4 秒刷新一次。

在非常繁忙的系统上，top 可能显示略过时的信息，因为采样需要时间。

## 终止进程

与任何运行中的进程或守护进程通信的一种方式是使用 kill(1) 发送信号。有许多不同的信号；有些具有特定含义，而其他信号在应用程序的文档中描述。用户只能向自己拥有的进程发送信号，向其他人的进程发送信号将导致权限拒绝错误。例外是 root 用户，他可以向任何人的进程发送信号。

操作系统也可以向进程发送信号。如果应用程序编写不当并试图访问不应访问的内存，FreeBSD 将向进程发送“段违规”信号（SIGSEGV）。如果应用程序编写为使用 alarm(3) 系统调用在一段时间后收到警报，它将收到“闹钟”信号（SIGALRM）。

两个信号可用于停止进程：SIGTERM 和 SIGKILL。SIGTERM 是终止进程的礼貌方式，因为进程可以读取信号、关闭可能打开的任何日志文件，并尝试在关闭之前完成正在做的事情。在某些情况下，如果进程正在执行某些无法中断的任务，它可能会忽略 SIGTERM。

SIGKILL 不能被进程忽略。向进程发送 SIGKILL 通常会立即停止该进程。

其他常用的信号是 SIGHUP、SIGUSR1 和 SIGUSR2。由于这些是通用信号，不同的应用程序会有不同的响应。例如，在更改 Web 服务器的配置文件后，需要告诉 Web 服务器重新读取其配置。重启 httpd 会导致 Web 服务器短暂停机。相反，向守护进程发送 SIGHUP 信号。请注意，不同的守护进程会有不同的行为，因此请参阅守护进程的文档以确定 SIGHUP 是否能达到预期的结果。

杀死系统上的随机进程是极其危险的行为。特别是 init(8)，PID 1，是特殊的。不建议使用命令 `/bin/kill -s KILL 1` 关闭系统，将可能造成数据丢失。在按下回车键之前，请务必仔细检查 kill(1) 的参数。

## 让命令位于前台和后台

**Ctrl**+**Z**：将当前进程挂起（暂停），随后可使用 `fg` 命令将其恢复到前台：

```sh
# ping 163.com  # 测试与 163.com 的网络连通性
PING 163.com (59.111.160.244): 56 data bytes
64 bytes from 59.111.160.244: icmp_seq=0 ttl=52 time=27.611 ms
64 bytes from 59.111.160.244: icmp_seq=1 ttl=52 time=27.691 ms
^Z[1] + Suspended               ping 163.com # 注意此处，按下了 Ctrl+Z
# fg # 返回前台
ping 163.com
64 bytes from 59.111.160.244: icmp_seq=3 ttl=52 time=27.465 ms
64 bytes from 59.111.160.244: icmp_seq=4 ttl=52 time=27.586 ms
64 bytes from 59.111.160.244: icmp_seq=5 ttl=52 time=27.522 ms
^C # 按 Ctrl+C 结束命令
--- 163.com ping statistics ---
6 packets transmitted, 6 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 27.465/27.596/27.701/0.085 ms
```

## 附录：系统监控工具 htop

### 安装与配置

htop 是一款功能丰富的交互式系统监控工具，能够以直观的方式实时显示系统资源使用情况。本节介绍 htop 的安装与配置方法。

**使用 pkg 二进制包管理器安装：**

```sh
# pkg install htop
```

**或使用 Port 从源代码构建安装：**

```sh
# cd /usr/ports/sysutils/htop/
# make install clean
```

### htop 配置持久化

htop 的配置可通过界面或配置文件进行持久化设置。需注意：在默认配置下，使用 F10 保存后无法通过 `Ctrl + C` 退出，必须选择 `quit` 选项才能确保配置保存；也可直接通过编辑配置文件进行设置。

编辑用户目录下的 `~/.config/htop/htoprc` 配置文件，添加以下内容以启用 CPU 频率和温度显示功能：

```ini
show_cpu_frequency=1     # 启用 CPU 当前频率显示
show_cpu_temperature=1   # 启用 CPU 温度显示
```

### 参考文献

- htop-dev. Settings are not saved[EB/OL]. [2026-03-25]. <https://github.com/htop-dev/htop/issues/949>. 讨论了 htop 配置保存的常见问题与解决方案。

## 课后习题

1. 使用 `ps aux` 和 `top` 查看系统运行的进程，分析哪些是用户进程，哪些是系统进程（守护进程）。
2. 尝试使用 `nice` 和 `renice` 修改进程优先级，观察进程运行的变化。
3. 配置一个简单的守护进程（可使用脚本或现有软件），使用 `service` 命令对其进行启动、停止和状态查看操作。
