# 4.4 虚拟控制台和终端

虚拟控制台（Virtual Console）是 FreeBSD 提供的多终端机制，允许用户在同一物理显示器和键盘上同时使用多个独立的登录会话。每个虚拟控制台拥有自己的登录提示符和 shell，用户可通过 Alt+F1 至 Alt+F8 键组合在它们之间切换。

终端（Terminal）的概念源于早期计算机系统中用于与主机通信的物理设备（电传打字机 TTY），在现代系统中演变为软件模拟的终端设备。FreeBSD 的虚拟控制台设备名称为 ttyv0 至 ttyv7，其中 ttyv0 为系统控制台（System Console），系统消息默认输出到该控制台。虚拟控制台的数量由 `/etc/ttys` 文件配置。

## 登录到 FreeBSD

当 FreeBSD 系统安装完成并正常启动后，用户将在屏幕上看到以下系统提示符界面：

```sh
FreeBSD/amd64 (ykla) (ttyv0)

login:
```

这一屏幕界面在计算机技术史上被称为 TTY（teletypewriter，电传打字机），也可称为物理终端。TTY 作为用户与操作系统内核进行交互的早期接口形式，在图形用户界面（GUI）普及之前构成了主要的人机交互（HCI）手段，是计算机人机交互历史发展进程中的重要阶段。

解释：

- `FreeBSD` 是操作系统名称；
- `amd64` 是体系架构，一般英特尔和 AMD 处理器使用的都是 amd64，即 x86-64；
- `ykla` 是主机名，是在安装系统时用户自行设置的；
- `ttyv0` 是指首个 TTY，计算机中许多事物的编号序列都是以 0 打头的；
- `login:` 指示用户登录。

输入用户名和密码，登录系统：

```sh
FreeBSD/amd64 (ykla) (ttyv0)

login: root # 此处输入用户名，然后按回车键 ①
Password: # 此处输入密码，然后按回车键
Last login: Tue Mar 18 17:24:48 2025 from 3413e8b6b43f
FreeBSD 15.0-CURRENT (GENERIC) main-n275981-b0375f78e32a

Welcome to FreeBSD!

Release Notes, Errata: https://www.FreeBSD.org/releases/
Security Advisories:   https://www.FreeBSD.org/security/
FreeBSD Handbook:      https://www.FreeBSD.org/handbook/
FreeBSD FAQ:           https://www.FreeBSD.org/faq/
Questions List:        https://www.FreeBSD.org/lists/questions/
FreeBSD Forums:        https://forums.FreeBSD.org/

Documents installed with the system are in the /usr/local/share/doc/freebsd/
directory, or can be installed later with:  pkg install en-freebsd-doc
For other languages, replace "en" with a language code like de or fr.

Show the version of FreeBSD installed:  freebsd-version ; uname -a
Please include that output and any error messages when posting questions.
Introduction to manual pages:  man man
FreeBSD directory layout:      man hier

To change this login announcement, see motd(5).
```

祝贺你！你已经成功登录到 FreeBSD 操作系统。

> **注意**
>
> 密码并不会被回显打印到屏幕上。一般情况下，输入密码时，屏幕上会显示 `******`。但在 FreeBSD 中，凡是涉及密码的地方大都不会有任何显示，即使输入了密码，屏幕上也仍然是空白的，与没有任何输入时的状态相同，直接输入后按回车即可。

- ①：root 是 UNIX 系统中的超级用户账户，拥有最高权限。常说的 Android root、Apple 越狱、Kindle 越狱等，都是为了获取这一 root 权限。


### 故障排除与未竟事宜

- 若用户名正确，但密码不正确：

```sh
login: root
Password:
Login incorrect # 表示登录信息不正确
login:
```

- 若用户名和密码都不正确：

```sh
login: test # 当前系统中不存在该用户
Password:
Login incorrect
login:
```

如果读者连用户名都无从得知，建议找回 `root` 密码后，查看系统中有哪些用户账户，或者直接重装系统会更方便。

### 参考文献

- ItsFOSS. What is TTY in Linux?[EB/OL]. [2026-03-25]. <https://itsfoss.com/what-is-tty-in-linux/>. 详细介绍 TTY 概念与历史

## 虚拟控制台

虽然系统控制台可用于与系统交互，但在 FreeBSD 系统键盘前使用命令行工作的用户通常会登录到虚拟控制台而非系统控制台。这是因为系统消息默认配置为在系统控制台上显示，这些消息会覆盖在用户正在处理的命令或文件之上，影响用户集中注意力。

默认情况下，FreeBSD 配置了多个虚拟控制台用于输入命令。每个虚拟控制台都有自己的登录提示符和 Shell，在虚拟控制台之间切换非常方便。这本质上提供了在图形环境中同时打开多个窗口的命令行等效功能。

FreeBSD 保留了 Alt+F1 至 Alt+F8 的组合键用于在虚拟控制台之间切换。使用 Alt+F1 切换到系统控制台（ttyv0），Alt+F2 访问第一个虚拟控制台（ttyv1），Alt+F3 访问第二个虚拟控制台（ttyv2），依此类推。当使用 Xorg 作为图形控制台时，组合键变为 Ctrl+Alt+F1 以返回基于文本的虚拟控制台。

从一个控制台切换到另一个时，FreeBSD 管理屏幕输出，结果是产生拥有多个虚拟屏幕和键盘的错觉，可以用来输入命令让 FreeBSD 执行。在一个虚拟控制台中启动的程序不会因为用户切换到另一个虚拟控制台而停止运行。

在 FreeBSD 中，可用虚拟控制台的数量在 `/etc/ttys` 文件的以下部分中配置：

```ini
……其他省略……

# name	getty				type	status		comments
#
# If console is marked "insecure", init will ask for the root password
# when going to single-user mode.
console	none				unknown	off insecure
#
ttyv0	"/usr/libexec/getty Pc"		xterm	onifexists secure
# Virtual terminals
ttyv1	"/usr/libexec/getty Pc"		xterm	onifexists secure
ttyv2	"/usr/libexec/getty Pc"		xterm	onifexists secure
ttyv3	"/usr/libexec/getty Pc"		xterm	onifexists secure
ttyv4	"/usr/libexec/getty Pc"		xterm	onifexists secure
ttyv5	"/usr/libexec/getty Pc"		xterm	onifexists secure
ttyv6	"/usr/libexec/getty Pc"		xterm	onifexists secure
ttyv7	"/usr/libexec/getty Pc"		xterm	onifexists secure
ttyv8	"/usr/local/bin/xdm -nodaemon"	xterm	off secure

……其他省略……
```

要禁用某个虚拟控制台，在该虚拟控制台对应行的开头加上注释符号 `#`。例如，要将可用虚拟控制台的数量从八个减少到四个，在代表虚拟控制台 ttyv5 至 ttyv8 的最后四行开头加上 `#`：

```ini
……其他省略……

#ttyv5	"/usr/libexec/getty Pc"		xterm	onifexists secure
#ttyv6	"/usr/libexec/getty Pc"		xterm	onifexists secure
#ttyv7	"/usr/libexec/getty Pc"		xterm	onifexists secure
#ttyv8	"/usr/local/bin/xdm -nodaemon"	xterm	off secure

……其他省略……
```

> **技巧**
>
>如果操作失误，但是配置了 SSHD 服务，仍可通过 SSH 远程连接 FreeBSD 系统，将生成一个 pts(4) 伪终端 `/dev/pts/n`。
>
>```sh
>$ w
>10:22PM  up 27 mins, 3 users, load averages: 0.03, 0.04, 0.00
>USER       TTY      FROM            LOGIN@  IDLE WHAT
>ykla       pts/0    192.168.179.1   9:55PM     4 su (sh)
>ykla       pts/1    192.168.179.1  10:22PM     - w
>```


注意，最后一个虚拟控制台（ttyv8）用于访问图形环境（如果已安装并配置了 Xorg）。

有关此文件中每列的详细描述和虚拟控制台的可用选项，请参阅 ttys(5)。

## 单用户模式

FreeBSD 启动菜单提供了一个标记为“Boot Single User”的选项。如果选择此选项，系统将启动进入一种称为“单用户模式”的特殊模式。此模式通常用于修复无法启动的系统，或在不知道 root 密码时重置 root 密码。

在单用户模式下，网络和其他虚拟控制台不可用。但是，可以获得完整的 root 访问权限，并且默认情况下不需要 root 密码。由于这些原因，需要物理访问键盘才能启动进入此模式，因此在保护 FreeBSD 系统安全时，确定谁拥有键盘的物理访问权是需要考虑的重要因素。

控制单用户模式的设置位于 `/etc/ttys` 文件的以下部分：

```ini
……以上省略……

# name	getty				type	status		comments
#
# If console is marked "insecure", init will ask for the root password
# when going to single-user mode.
console	none				unknown	off secure	# 注意此行
#

……以下省略……
```

默认情况下，状态设置为 `secure`（安全）。这假设谁拥有键盘的物理访问权要么不重要，要么由物理安全策略控制。

如果将此设置更改为 `insecure`（不安全），则假设物理环境本身是不安全的，因为任何人都可以访问键盘。当此行中的 `secure` 更改为 `insecure` 后，即：

```ini
console	none				unknown	off insecure
```

FreeBSD 将在用户选择启动进入单用户模式时提示输入 root 密码：

```sh
Enter root password, or ^D to go multi-user
Password:
```

将此设置更改为 `insecure` 时要小心！如果忘记了 root 密码，仍然可以借助安装介质启动进入单用户模式，但对于不熟悉 FreeBSD 启动过程的人来说可能会比较困难。

## 调整引导界面和 TTY 分辨率

### 修改“gop”（通用方法）

在出现 FreeBSD 菜单时，按 **ESC** 键退出引导，出现提示符 `OK`。输入 `gop list` 可查看所有支持的分辨率列表：

```sh
OK gop list
mode 0: 1920x1080x32, stride=1920   # 显示模式 0，分辨率 1920x1080，颜色深度 32 位，行跨度 1920
mode 1: 640x480x32, stride=640       # 显示模式 1，分辨率 640x480，颜色深度 32 位，行跨度 640
mode 2: 800x600x32, stride=800       # 显示模式 2，分辨率 800x600，颜色深度 32 位，行跨度 800
mode 3: 1024x768x32, stride=1024     # 显示模式 3，分辨率 1024x768，颜色深度 32 位，行跨度 1024
mode 4: 1280x720x32, stride=1280     # 显示模式 4，分辨率 1280x720，颜色深度 32 位，行跨度 1280
mode 5: 1280x1024x32, stride=1280    # 显示模式 5，分辨率 1280x1024，颜色深度 32 位，行跨度 1280
```

此处选择 `mode 0` 进行效果测试：

```sh
OK gop set 0
```

效果会立即显示。

确认效果合适后，继续引导：

```sh
OK menu
```

该命令表示操作确认或进入菜单界面。

将该配置写入 `/boot/loader.conf` 文件，设置 GOP 模式为 0：

```ini
exec="gop set 0"
```

### `efi_max_resolution`（UEFI）或 `vbe_max_resolution`（BIOS）

也可以通过配置文件设置 UEFI 或 BIOS 下的分辨率。根据文档 [LOADER.CONF(5)](https://man.freebsd.org/cgi/man.cgi?loader.conf(5))，这两个变量可接受以下值：

```sh
值	           分辨率
480p	        640x480
720p	        1280x720
1080p	       1920x1080
1440p	       2560x1440
2160p	       3840x2160
4k	          3840x2160
5k	          5120x2880
宽 x 高        宽 x 高
```

本节测试使用 `efi_max_resolution` 变量：将 `efi_max_resolution="1080p"` 写入 `/boot/loader.conf` 文件，重启后效果与 gop 方法一致。

### 参考文献

- FreeBSD Project. loader.conf(5)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?loader.conf(5)>.
- FreeBSD Forums. gop set < mode > being ignored in /boot/loader.conf[EB/OL]. [2026-03-26]. <https://forums.freebsd.org/threads/gop-set-mode-being-ignored-in-boot-loader-conf.77779/>. 讨论 loader.conf 中 GOP 模式设置未生效的原因与解决思路。
- FreeBSD Forums. How to find the valid values of efi_max_resolution[EB/OL]. [2026-03-26]. <https://forums.freebsd.org/threads/how-to-find-the-valid-values-of-efi_max_resolution.84840/>. 探讨查询 efi_max_resolution 有效取值的方法。



## 课后习题

1. 在 FreeBSD 中切换多个虚拟控制台（ttyv0-ttyv3），分别在不同控制台登录不同用户，使用 w 命令验证并记录结果。
2. 查找 FreeBSD 内核中 TTY 子系统的核心源代码，使其具有现代操作系统应有的功能。
3. 修改 FreeBSD 中 motd（Message of the Day）的默认显示行为，验证其变化。
