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
Password: 	# 此处输入密码，然后按回车键
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

## 虚拟控制台

虽然系统控制台可用于与系统交互，但在 FreeBSD 系统键盘前使用命令行工作的用户通常会登录到虚拟控制台而非系统控制台。这是因为系统消息默认配置为在系统控制台上显示，这些消息会覆盖在用户正在处理的命令或文件之上，影响用户集中注意力。

默认情况下，FreeBSD 配置了多个虚拟控制台用于输入命令。每个虚拟控制台都有自己的登录提示符和 Shell，在虚拟控制台之间切换非常方便。这本质上提供了在图形环境中同时打开多个窗口的命令行等效功能。

FreeBSD 保留了 Alt+F1 至 Alt+F8 的组合键用于在虚拟控制台之间切换。使用 Alt+F1 切换到系统控制台（ttyv0），Alt+F2 访问第一个虚拟控制台（ttyv1），Alt+F3 访问第二个虚拟控制台（ttyv2），依此类推。当使用 Xorg 作为图形控制台时，组合键变为 Ctrl+Alt+F1 以返回基于文本的虚拟控制台。

从一个控制台切换到另一个时，FreeBSD 管理屏幕输出，结果是产生拥有多个虚拟屏幕和键盘的错觉，可以用来输入命令让 FreeBSD 执行。在一个虚拟控制台中启动的程序不会因为用户切换到另一个虚拟控制台而停止运行。

在 FreeBSD 中，可用虚拟控制台的数量在 `/etc/ttys` 文件的以下部分中配置：

```sh
# name    getty                         type  status comments
#
ttyv0   "/usr/libexec/getty Pc"         xterm   on  secure
# Virtual terminals
ttyv1   "/usr/libexec/getty Pc"         xterm   on  secure
ttyv2   "/usr/libexec/getty Pc"         xterm   on  secure
ttyv3   "/usr/libexec/getty Pc"         xterm   on  secure
ttyv4   "/usr/libexec/getty Pc"         xterm   on  secure
ttyv5   "/usr/libexec/getty Pc"         xterm   on  secure
ttyv6   "/usr/libexec/getty Pc"         xterm   on  secure
ttyv7   "/usr/libexec/getty Pc"         xterm   on  secure
ttyv8   "/usr/X11R6/bin/xdm -nodaemon"  xterm   off secure
```

要禁用某个虚拟控制台，在该虚拟控制台对应行的开头加上注释符号 `#`。例如，要将可用虚拟控制台的数量从八个减少到四个，在代表虚拟控制台 ttyv5 至 ttyv8 的最后四行开头加上 `#`。不要注释掉系统控制台 ttyv0 的行。注意，最后一个虚拟控制台（ttyv8）用于访问图形环境（如果已安装并配置了 Xorg）。

有关此文件中每列的详细描述和虚拟控制台的可用选项，请参阅 ttys(5)。

## 单用户模式

FreeBSD 启动菜单提供了一个标记为\u201cBoot Single User\u201d的选项。如果选择此选项，系统将启动进入一种称为\u201c单用户模式\u201d的特殊模式。此模式通常用于修复无法启动的系统，或在不知道 root 密码时重置 root 密码。

在单用户模式下，网络和其他虚拟控制台不可用。但是，可以获得完整的 root 访问权限，并且默认情况下不需要 root 密码。由于这些原因，需要物理访问键盘才能启动进入此模式，因此在保护 FreeBSD 系统安全时，确定谁拥有键盘的物理访问权是需要考虑的重要因素。

控制单用户模式的设置位于 `/etc/ttys` 文件的以下部分：

```sh
# name  getty                           type  status  comments
#
# If console is marked "insecure", then init will ask for the root password
# when going to single-user mode.
console none                            unknown  off  secure
```

默认情况下，状态设置为 `secure`。这假设谁拥有键盘的物理访问权要么不重要，要么由物理安全策略控制。如果将此设置更改为 `insecure`，则假设环境本身是不安全的，因为任何人都可以访问键盘。当此行更改为 `insecure` 时，FreeBSD 将在用户选择启动进入单用户模式时提示输入 root 密码。

将此设置更改为 `insecure` 时要小心！如果忘记了 root 密码，仍然可以启动进入单用户模式，但对于不熟悉 FreeBSD 启动过程的人来说可能会比较困难。

## 更改控制台显示模式

FreeBSD 控制台的默认显示模式可以调整为 1024x768、1280x1024 或图形芯片和显示器支持的任何其他大小。要使用不同的显示模式，加载 VESA 模块：

```sh
# kldload vesa
```

要确定硬件支持哪些显示模式，使用 vidcontrol(1)。

`vidcontrol` 用于设置 syscons(4) 或 vt(4) 控制台驱动的选项。

不同行数模式需要不同尺寸的字体文件。

```sh
# vidcontrol -i mode
```

此命令的输出列出了硬件支持的显示模式。要选择新的显示模式，以 root 用户身份使用 vidcontrol(1) 指定模式：

```sh
# vidcontrol MODE_279
```

如果新的显示模式可以接受，可以通过将其添加到 `/etc/rc.conf` 来在启动时永久设置：

```sh
allscreens_flags="MODE_279"
```

### 参考文献

- ItsFOSS. What is TTY in Linux?[EB/OL]. [2026-03-25]. <https://itsfoss.com/what-is-tty-in-linux/>. 详细介绍 TTY 概念与历史

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

## 课后习题

1. 在 FreeBSD 中切换多个虚拟控制台（ttyv0-ttyv3），分别在不同控制台登录不同用户，使用 w 命令验证并记录结果。
2. 查找 FreeBSD 内核中 TTY 子系统的核心源代码，使其具有现代操作系统应有的功能。
3. 修改 FreeBSD 中 motd（Message of the Day）的默认显示行为，验证其变化。
