# 6.2 shell 基础

本节介绍什么是 Shell，如何修改默认登录环境。

## 概述

shell 是用户与操作系统内核交互的命令解释程序（command interpreter），接受用户输入的命令并传递给内核执行。用户命令在 shell 中运行，通过 shell 与系统交互。shell 提供命令行界面，从输入通道接收命令并执行。许多 shell 提供内置功能以辅助日常任务，如文件管理、文件名通配、命令行编辑、命令宏和环境变量。FreeBSD 基本系统内置多种 shell，包括扩展 POSIX shell（sh(1)）和扩展 C shell（tcsh(1)）。其他 shell 可通过 FreeBSD Ports 获得，例如 Zsh 和 Bash。

shell 在操作系统中的位置如下：

![什么是 shell](../.gitbook/assets/what-is-shell.png)

FreeBSD root 用户默认 shell 为 sh（自 FreeBSD 14 起），但基本系统同时提供 csh/tcsh 作为替代选择。

> **技巧**
>
> csh 与 tcsh 的关系
>
> FreeBSD 中 csh 和 tcsh 是同一个二进制程序，但以不同名称调用时行为有所差异。可通过查看源代码 [https://github.com/freebsd/freebsd-src/blame/main/bin/csh/Makefile](https://github.com/freebsd/freebsd-src/blame/main/bin/csh/Makefile) 及执行 man csh 验证：两者均重定向至 tcsh。

> **注意**
>
> 虽然 csh 与 tcsh 本质上是同一程序，但如果以 csh 的参数调用，则部分 tcsh 扩展会被关闭，因而在使用时存在差异。

## POSIX shell 规范

POSIX（Portable Operating System Interface）是由 IEEE 和 The Open Group 制定的操作系统接口标准，旨在确保应用程序在不同 UNIX 系统间的可移植性。POSIX.1 标准中的 shell 和实用程序规范（Shell Command Language）定义了符合标准的 shell 必须实现的最小功能集，包括命令语法、变量扩展、引号规则、条件表达式、循环结构和内置命令等。当前版本为 POSIX.1-2024（IEEE Std 1003.1-2024）。

POSIX shell 规范的核心要求包括：

- **命令执行**：支持简单命令、管道、列表和复合命令的执行。
- **变量与参数扩展**：支持位置参数、特殊参数和多种变量扩展形式。
- **引号机制**：支持单引号（保留字面值）、双引号（允许变量扩展和命令替换）和反斜杠转义。
- **模式匹配**：支持文件名通配（globbing），包括 `*`、`?` 和方括号表达式。
- **条件与循环**：支持 `if`、`while`、`for`、`case` 等控制结构。
- **内置命令**：必须实现 `cd`、`echo`、`exit`、`export`、`read`、`return`、`set`、`shift`、`trap`、`unset` 等内置命令。

FreeBSD 系统默认采用的 shell 是 sh。FreeBSD 的 **/bin/sh** 并非 Stephen R. Bourne 在贝尔实验室为 UNIX V7 编写的原始 Bourne shell，而是基于 Kenneth Almquist 于 1989 年发布的 Almquist shell（ash），后者旨在作为 Bourne shell 更紧凑、更高效的替代品。4.3BSD-Reno/Net/2 时期（1990—1991 年）将 ash 引入 BSD 世界，NetBSD 随后将其作为默认 /bin/sh，FreeBSD 又从 NetBSD 导入了 ash 实现，在功能上基本符合 POSIX.1-2024 标准中关于 shell 的规范要求。

Linux 中常见的 shell 是 bash（Bourne Again shell，是对“Born Again”即“重生”的双关，意为“重生的 Bourne shell”）。而 macOS 中的默认 shell 通常是 zsh（Z shell）。

Linux 中同样提供 sh，但通常符号链接到其他 shell（如 Debian/Ubuntu 中链接到 dash，部分发行版链接到 bash），它们并不是真正的 sh。

例如 Ubuntu 24.04 LTS 默认的 shell 是 dash：

```bash
lrwxrwxrwx 1 root root 4  2 月 25 23:19 /bin/sh -> dash
$ ls -l /bin/sh # 以长格式查看 /bin/sh 这个文件的详细信息
```

dash 是 NetBSD 版本 ash（Almquist SHell）的直接后裔。

## 快捷键

> **注意**
>
> 以下快捷键的执行不受键盘大小写状态（如 Caps Lock 开启或关闭）的影响。

### 使用 Scroll Lock 键在 TTY 界面上下翻页/翻行

使用 **Scroll Lock** 键（滚动锁定键）：按下 **Scroll Lock** 键后，可以使用上 ↑/下 ↓ 方向键以及 **Page Up**/**Page Down** 键滚动屏幕。

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
# lo # 此时按 Tab 键可查看以 lo 开头的命令列表；继续输入更多字母后再次按 Tab 可进一步筛选
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
$ cp /home/ykla/ # 此处按 Tab 键，随后再重复按一次 Tab 键，观察效果
$ cp /home/ykla/test/1.txt
.cache/                 .login                  bin/                    test2
.config/                .profile                HW_PROBE/               test3
.cshrc                  .sh_history             mine
.gitconfig              .sh_history.Y8RqIDNDIv  mydir/
.k5login                .shrc
```

### 终止命令

如果要终止命令，可以使用 **Ctrl**+**C**：

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

FreeBSD 的 `ping` 合并了原 `ping6` 的功能，通过 `-4`/`-6` 选项区分协议版本（Google Summer of Code 2019 项目）。Linux 支持 `-O` 报告未收到回复；FreeBSD 的 `-O` 含义不同（仅用于 IPv6 的 ICMPv6 Node Information supported query types 查询），不支持报告未收到回复的功能。`ping -y`（ICMPv6 Node Information DNS Name 查询）和 `ping -k`（Node Information Node Addresses 查询）源自 KAME 项目的 ICMPv6 Node Information 实现。

`ping` 使用 ICMP 协议的 ECHO_REQUEST 数据报来触发主机的 ECHO_RESPONSE。IPv4 目标使用 ICMP，IPv6 目标使用 ICMPv6（RFC 4443）。默认数据大小为 56 字节，加上 8 字节 ICMP 头共 64 字节。如果数据空间不小于 8 字节，前 8 字节用于时间戳以计算往返时间。

### 其他

- **Ctrl**+**L**（字母 L）：清空屏幕
- **Ctrl**+**A**：将光标移动到命令行首
- **Ctrl**+**E**：将光标移动到命令行尾

## 配置 csh/tcsh

对于 C shell（csh/tcsh），登录 shell 依次读取 **/etc/csh.cshrc**、**/etc/csh.login**、**~/.tcshrc**（若不存在则读取 **~/.cshrc**）、**~/.login**。

- 在 **~/.cshrc** 文件中加入下行，为 `ls` 命令设置彩色输出。

```sh
alias ls ls -G
```

并重新登录。

- 如何使 FreeBSD 的 csh 像 Bash 那样按 Tab 列出无法补全的候选文件？在 **~/.cshrc** 文件中加入：

```sh
set filec              # 启用命令行文件名补全
set autolist           # 自动显示补全列表
```

重新加载 C shell 配置文件，刷新别名和环境设置：

```sh
# source ~/.cshrc
```

- 如何使 csh 具备类似 zsh 的命令错误修正功能？

例如，使用 emacs 编写 C 语言程序时，输入 `emacs ma` 并按 `Tab` 键再按回车键，会匹配所有以 `ma` 开头的文件。此配置可以忽略部分匹配的文件，即按 `Tab` 时不会列出被忽略的文件，便于编程，不会匹配二进制 `.o` 文件等。

```sh
set correct = cmd        # 启用命令拼写自动纠正功能，提示输入正确命令
# 例：lz/usr/bin tcsh>ls /usr/bin (y|n|e|a)?  # 当检测到命令拼写错误时的提示示例

set fignore = (.o ~)   # 设置文件名忽略模式，用于补全时排除指定文件或模式
```

## 参考文献

- The Open Group. Shell Command Language[EB/OL]. [2026-04-23]. <https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html>.
- Herbert. Dash[EB/OL]. [2026-05-08]. <http://gondor.apana.org.au/~herbert/dash/>. Dash 官网
- Almquist K. ash (Almquist shell)[EB/OL]. (1989-05-30)[2026-04-18]. <https://github.com/dsipher/ash>. FreeBSD 的 **/bin/sh** 基于 ash，而非 Stephen R. Bourne 的原始 Bourne shell。
- Fox B, Ramey C. Bash Reference Manual[M]. Boston: Free Software Foundation, 2022. “Bourne Again shell”是对“Born Again”的双关。

## 课后习题

1. 在 FreeBSD 中编写一个 sh 脚本，实现文件名补全的最小示例，记录 sh 内建补全机制与 Bash 补全的功能差异。
2. 查阅 FreeBSD sh 源代码（**bin/sh/**），分析其行编辑和快捷键处理的实现方式，比较其与 Bash 在交互功能上的差距。
3. 修改 shell 的默认提示符配置（如通过 `PS1` 或 `set prompt`），记录不同 shell（sh、csh、zsh）中提示符定制的语法差异。
