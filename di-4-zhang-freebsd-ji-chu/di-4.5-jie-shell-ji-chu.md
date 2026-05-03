# 4.5 Shell 基础

## Shell 的概念与定位

![什么是 Shell](../.gitbook/assets/what-is-shell.png)

shell 是用户与操作系统内核进行交互的命令解释器（command interpreter），它接受用户输入的命令并将其传递给内核执行。用户的命令运行在 shell 中，并通过 shell 与系统进行交互。shell 提供命令行界面用于与操作系统交互，从输入通道接收命令并执行。许多 shell 提供内置功能以辅助日常任务，如文件管理、文件名通配、命令行编辑、命令宏和环境变量。FreeBSD 基本系统内置多种 shell，包括扩展 POSIX Shell（sh(1)）和扩展 C Shell（tcsh(1)）。其它 shell 可通过 FreeBSD Ports 获得，例如 Zsh 和 Bash。

### Shell 的架构角色

从操作系统架构的角度看，Shell 位于用户空间与内核空间之间，充当命令解释与进程管理的中间层。shell 的核心功能包括：

- **命令解释**：解析用户输入的命令行，将其分解为命令名、选项和参数，然后通过系统调用（如 `execve(2)`）请求内核创建新进程执行相应程序。
- **进程控制**：管理进程的创建、前台/后台调度、信号传递和作业控制。shell 是用户管理进程生命周期的首要工具。
- **环境管理**：维护环境变量（如 `PATH`、`HOME`、`TERM`），这些变量构成了进程的执行上下文。环境变量是存储在 shell 环境中的键值对，任何由 shell 调用的程序都可以读取该环境，因此其中包含大量程序配置信息。
- **I/O 重定向与管道**：通过文件描述符操作实现标准输入（stdin）、标准输出（stdout）和标准错误（stderr）的重定向，以及通过管道（pipe）机制将一个进程的输出直接传递给另一个进程的输入。UNIX 管道操作符 `|` 允许将一个命令的输出直接传递给另一个程序，管道将一个命令的标准输出作为另一个命令的标准输入传递。
- **脚本编程**：shell 本身也是一种编程语言，支持变量、条件判断、循环、函数等控制结构，可用于编写自动化脚本。

### Shell 的历史演化与分类

shell 的演化反映了 UNIX 系统半个多世纪的发展历程。按语法族系划分，shell 可分为两大谱系：

- **Bourne Shell 谱系**：以 Stephen R. Bourne 于 1977 年为 Unix V7 编写的 Bourne Shell（sh）为始祖。该谱系的 shell 采用较为简洁的语法，以 `$` 作为默认提示符。后续演化包括 Almquist Shell（ash，1989 年）、KornShell（ksh，1983 年）、Bourne Again Shell（bash，1989 年）、Z Shell（zsh，1990 年）等。
- **C Shell 谱系**：以 Bill Joy 于 1978 年为 2BSD 编写的 C Shell（csh）为始祖。该谱系的 shell 语法更接近 C 语言，以 `%` 作为默认提示符。后续演化包括 TENEX C Shell（tcsh，1983 年）等。

### POSIX Shell 规范

POSIX（Portable Operating System Interface）是由 IEEE 和 The Open Group 制定的操作系统接口标准，旨在确保应用程序在不同 UNIX 系统间的可移植性。POSIX.1 标准中的 Shell 和实用程序规范（Shell Command Language）定义了符合标准的 shell 必须实现的最小功能集，包括命令语法、变量扩展、引号规则、条件表达式、循环结构和内置命令等。当前版本为 POSIX.1-2024（IEEE Std 1003.1-2024）（来源：The Open Group. Shell Command Language[EB/OL]. [2026-04-23]. <https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html>.）

POSIX Shell 规范的核心要求包括：

- **命令执行**：支持简单命令、管道、列表和复合命令的执行。
- **变量与参数扩展**：支持位置参数、特殊参数和多种变量扩展形式。
- **引号机制**：支持单引号（保留字面值）、双引号（允许变量扩展和命令替换）和反斜杠转义。
- **模式匹配**：支持文件名通配（globbing），包括 `*`、`?` 和方括号表达式。
- **条件与循环**：支持 `if`、`while`、`for`、`case` 等控制结构。
- **内置命令**：必须实现 `cd`、`echo`、`exit`、`export`、`read`、`return`、`set`、`shift`、`trap`、`unset` 等内置命令。

FreeBSD 系统默认采用的 shell 是 sh。FreeBSD 的 **/bin/sh** 并非 Stephen R. Bourne 在贝尔实验室为 Unix V7 编写的原始 Bourne Shell，而是基于 Kenneth Almquist 于 1989 年发布的 Almquist Shell（ash），后者是作为 Bourne Shell 的更紧凑、更高效的替代品而设计的。BSD 系列自 4.4BSD 起便采用 ash 衍生的 sh，在功能上基本符合 POSIX.1-2024 标准中关于 shell 的规范要求。

Linux 中常见的 shell 通常是 bash（Bourne Again Shell，是对“Born Again”即“重生”的双关，意为“重生的 Bourne Shell”）。而 macOS 中的默认 shell 通常是 zsh（Z Shell）。

> **注意**
>
> Linux 中同样提供 sh，但通常被软链接到其他 shell（如 Debian/Ubuntu 中链接到 dash，部分发行版链接到 bash），它们并不是真正的 sh。
>
>- Ubuntu 24.04 LTS 默认的 shell：
>
>```bash
> lrwxrwxrwx 1 root root 4  2 月 25 23:19 /bin/sh -> dash
> $ ls -l /bin/sh # 以长格式查看 /bin/sh 这个文件的详细信息
>```

## 快捷键

> **注意**
>
> 以下快捷键的执行不受键盘大小写状态（如 Caps Lock 开启或关闭）的影响。

### 使用 Scroll Lock 键在 TTY 界面上下翻页/翻行

使用 **Scroll Lock** 键（滚动锁定键）：按下 **Scroll Lock** 键后，可以使用上 ↑/下 ↓ 方向键以及 **Page Up**/**Page Down** 键对屏幕进行操作。

不同点：

- 上 ↑/下 ↓ 方向键：使 TTY 界面上下滚动一行
- **Page Up**/**Page Down** 键：使 TTY 界面上下滚动一页

再次按下 **Scroll Lock** 键将退出此模式。

> **技巧**
>
> SL 键在 **HOME** 键的上方，PS 截图键 **Print Screen** 的右侧，PB 键 **Pause/Break** 的左侧。

从历史角度来看，**Scroll Lock** 键即为此类用途而设计，它能在文本界面中滚动而不影响光标位置。

### 使用 Shift 组合键在 TTY 界面上下翻页/翻行

使用 **Shift** 快捷键：

- **Shift** + 上 ↑/下 ↓ 方向键——使 TTY 界面上下滚动一行
- **Shift** + **Page Up**/**Page Down** 键——使 TTY 界面上下滚动一页

### 补全命令或目录

可使用 **Tab** 键补全命令或目录；上箭头 **↑** 用于查看上一条命令，下箭头 **↓** 用于查看下一条命令。

- 补全命令

```sh
# lo # 若此时按 Tab 键，输出如下。可继续输入一个字母后再次按 Tab 键以查看更多匹配项
local                    localedef                login
local-unbound            locate                   logins
local-unbound-anchor     lock                     logname
local-unbound-checkconf  lockf                    look
local-unbound-control    lockstat                 lorder
local-unbound-setup      locktest                 lowntfs-3g
locale
```

- 补全文件目录或文件名

```sh
$ cp /home/ykla/ # 此处按 Tab 键，然后再重复按一次 Tab 键，观察效果
$ cp /home/ykla/test/1.txt
.cache/                 .login                  bin/                    test2
.config/                .profile                HW_PROBE/               test3
.cshrc                  .sh_history             mine
.gitconfig              .sh_history.Y8RqIDNDIv  mydir/
.k5login                .shrc
```

### 终止命令

若要终止命令，可以使用 **Ctrl**+**C**：

```sh
# ping 163.com  # 测试与 163.com 的网络连通性
PING 163.com (59.111.160.244): 56 data bytes
64 bytes from 59.111.160.244: icmp_seq=0 ttl=52 time=27.672 ms
64 bytes from 59.111.160.244: icmp_seq=1 ttl=52 time=27.580 ms
^C # 注意这里，^C 表示此处按下了 Ctrl+C 的组合键，随后命令被终止
--- 163.com ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 27.580/27.626/27.672/0.046 ms
```

FreeBSD 的 `ping` 自 15.0 起合并了原 `ping6` 的功能，通过 `-4`/`-6` 选项区分协议版本（Google Summer of Code 2019 项目）。（如 Linux 支持 `-O` 报告未收到回复，FreeBSD 不支持）。FreeBSD 特有 `ping -y`（ICMPv6 Node Information DNS Name 查询）和 `ping -k`（Node Information Node Addresses 查询）。

`ping` 使用 ICMP 协议的 ECHO_REQUEST 数据报来触发主机的 ECHO_RESPONSE。IPv4 目标使用 ICMP，IPv6 目标使用 ICMPv6（RFC 2463）。默认数据大小为 56 字节，加上 8 字节 ICMP 头共 64 字节。若数据空间不小于 8 字节，前 8 字节用于时间戳以计算往返时间。

### 其他

- **Ctrl**+**L**（字母 L）：清空屏幕
- **Ctrl**+**A**：将光标移动到命令行首
- **Ctrl**+**E**：将光标移动到命令行尾

## 参考文献

- Almquist K. ash (Almquist Shell)[EB/OL]. (1989-05-30)[2026-04-18]. <https://github.com/dsipher/ash>. FreeBSD 的 **/bin/sh** 基于 ash，而非 Stephen R. Bourne 的原始 Bourne Shell。
- Fox B, Ramey C. Bash Reference Manual[M]. Boston: Free Software Foundation, 2022. “Bourne Again Shell”是对“Born Again”的双关。

## 课后习题

1. 在 FreeBSD 中编写一个 sh 脚本，实现文件名补全的最小示例，记录 sh 内建补全机制与 Bash 补全的功能差异。
2. 查阅 FreeBSD sh 源代码（`bin/sh/`），分析其行编辑和快捷键处理的实现方式，比较其与 Bash 在交互功能上的差距。
3. 修改 shell 的默认提示符配置（如通过 `PS1` 或 `set prompt`），记录不同 shell（sh、csh、zsh）中提示符定制的语法差异。
