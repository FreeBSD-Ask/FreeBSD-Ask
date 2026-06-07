# 5.6 shell

本节介绍什么是 Shell，如何修改默认登录环境。

## 概述

![什么是 shell](../.gitbook/assets/what-is-shell.png)

shell 是用户与操作系统内核交互的命令解释程序（command interpreter），接受用户输入的命令并传递给内核执行。用户命令在 shell 中运行，通过 shell 与系统交互。shell 提供命令行界面，从输入通道接收命令并执行。许多 shell 提供内置功能以辅助日常任务，如文件管理、文件名通配、命令行编辑、命令宏和环境变量。FreeBSD 基本系统内置多种 shell，包括扩展 POSIX shell（sh(1)）和扩展 C shell（tcsh(1)）。其他 shell 可通过 FreeBSD Ports 获得，例如 Zsh 和 Bash。

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

Linux 中同样提供 sh，但通常软链接到其他 shell（如 Debian/Ubuntu 中链接到 dash，部分发行版链接到 bash），它们并不是真正的 sh。

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
# lo # 如果此时按 Tab 键，输出如下。可继续输入一个字母后再次按 Tab 键以查看更多匹配项
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

FreeBSD 的 `ping` 合并了原 `ping6` 的功能，通过 `-4`/`-6` 选项区分协议版本（Google Summer of Code 2019 项目）。Linux 支持 `-O` 报告未收到回复；FreeBSD 的 `-O` 含义不同（仅用于 IPv6 的 ICMPv6 Node Information supported query types 查询），不支持报告未收到回复的功能。`ping -y`（ICMPv6 Node Information DNS Name 查询）和 `ping -k`（Node Information Node Addresses 查询）源自 KAME 项目的 ICMPv6 Node Information 实现，在 KAME 衍生系统（FreeBSD、NetBSD、OpenBSD、macOS 等）中均可用，Linux 的 iputils-ping 不支持这些选项。

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

## 切换 shell

永久更改默认 shell 的最简单方法是使用 chsh。运行此命令会打开由 EDITOR 环境变量配置的编辑器，默认情况下为 vi(1)。

### 切换 shell 为 Zsh

#### 安装 Zsh

- 使用 pkg 安装：

```sh
# pkg install zsh zsh-completions zsh-autosuggestions zsh-syntax-highlighting
```

软件包说明：

| 程序 | 说明 |
| ---- | ---- |
| `zsh` | Zsh shell |
| `zsh-completions` | 自动补全 |
| `zsh-autosuggestions` | 类 Fish shell 的 Zsh 自动补全 |
| `zsh-syntax-highlighting` | 类 Fish shell 的 Zsh 语法高亮 |

- 使用 Ports 安装：

```sh
# cd /usr/ports/shells/zsh/ && make install clean
# cd /usr/ports/shells/zsh-completions && make install clean
# cd /usr/ports/shells/zsh-autosuggestions/ && make install clean
# cd /usr/ports/shells/zsh-syntax-highlighting/ && make install clean
```

- 查看 Zsh 安装信息

```sh
# pkg info -D zsh
```

#### 配置 Zsh

将当前用户的默认登录 shell 修改为 Zsh：

```sh
# chsh -s /usr/local/bin/zsh # 切换 shell 至 zsh
chsh: user information updated
```

在提示符下输入你的密码并按下 **回车键** 即可更改 shell。注销并重新登录后即可开始使用新 shell。

> **注意**
>
> `chsh`、`chfn`、`chpass` 是同一个程序，通过不同名称调用。非超级用户只能将 shell 更改为 **/etc/shells** 中列出的标准 shell；从非标准 shell 更改或更改为非标准 shell 均会拒绝。编辑器由 `EDITOR` 环境变量决定，默认使用 vi(1)。信息验证后，chpass 会自动调用 pwd_mkdb(8) 更新用户数据库。

编辑 **~/.zshrc** 文件，添加下面几行：

```sh
source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh   # 加载 Zsh 自动建议插件
source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh   # 加载 Zsh 语法高亮插件
fpath+=/usr/local/share/zsh/site-functions/   # 将自定义函数目录添加到 Zsh 函数搜索路径
```

目录结构：

```sh
~/
└── .zshrc # Zsh 配置文件
/usr/local/
└── share/
    ├── zsh-autosuggestions/
    │   └── zsh-autosuggestions.zsh # Zsh 自动建议插件
    ├── zsh-syntax-highlighting/
    │   └── zsh-syntax-highlighting.zsh # Zsh 语法高亮插件
    └── zsh/
        └── site-functions/ # Zsh 自定义函数目录
```

立即使用：

```sh
# zsh                        # 切换当前 shell 到 Zsh
# source ~/.zshrc            # 重新加载 Zsh 配置文件，刷新环境变量
# rm -f ~/.zcompdump         # 删除 Zsh 补全缓存文件
# autoload -Uz compinit       # 加载 compinit 函数
# compinit                   # 初始化补全系统并强制重建缓存
```

#### 使用主题美化

除了基本配置外，还可以通过主题美化 shell 界面。Powerlevel10k 是广泛使用的 Zsh 主题，安装和配置方法如下：

```sh
$ git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k   # 克隆 Powerlevel10k 主题仓库到主目录
$ echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc                    # 将 Powerlevel10k 主题加载命令追加到 ~/.zshrc
```

目录结构：

```sh
~/
├── .zshrc # Zsh 配置文件
└── powerlevel10k/ # Powerlevel10k 主题目录
    └── powerlevel10k.zsh-theme # Powerlevel10k 主题文件
```

重新加载 Zsh 配置文件，使 Powerlevel10k 主题生效：

```sh
# source ~/.zshrc
```

按照提示回答若干问题以完成配置，重启后生效。

#### 参考文献

- romkatv. Powerlevel10k[EB/OL]. [2026-03-26]. <https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#installation>. 主题项目官网。
- FreeBSD Project. csh -- a shell with C-like syntax[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=csh&sektion=1>. C 风格语法 shell 手册页。

### Bash

Bash（Bourne Again shell）是 GNU 项目开发的 shell 程序，作为 Bourne shell（sh）的增强替代品。Bash 兼容 sh 语法，并集成了 csh 和 ksh 的有用特性，包括命令行编辑、命令历史、可编程补全和作业控制等功能。Bash 是多数 Linux 发行版的默认 shell，但在 FreeBSD 中并非基本系统组件。

#### 安装 Bash

- 使用 pkg 安装：

```sh
# pkg install bash bash-completion-freebsd bash-completion-zfs
```

- 使用 Ports 安装：

```sh
# cd /usr/ports/shells/bash/ && make install clean
# cd /usr/ports/shells/bash-completion-freebsd/ && make install clean
# cd /usr/ports/shells/bash-completion-zfs/ && make install clean
```

软件包说明：

| 程序 | 说明 |
| ---- | ---- |
| `bash` | Bash shell 主程序 |
| `bash-completion-freebsd` | 针对 FreeBSD 的 Bash 补全库扩展，作为依赖自动安装 |
| `bash-completion-zfs` | 针对 OpenZFS 的 Bash 补全库扩展 |

- 查看安装后配置

```sh
# pkg info -D bash-completion # 作为依赖安装的
```

#### 配置 Bash

安装完 Bash 及相关补全库后，需要配置才能正常运作。

```sh
chsh -s /usr/local/bin/bash   # 将当前用户的默认登录 Shell 切换为 Bash
touch ~/.bash_profile         # 创建 ~/.bash_profile 文件，用于配置 Bash 环境变量
```

相关文件结构：

```sh
~/
└── .bash_profile # Bash 配置文件
/usr/local/
└── share/
    └── bash-completion/
        ├── bash_completion.sh # Bash 补全脚本
        └── README.md # Bash 补全说明文档
```

为加载 Bash 补全功能，编辑 **~/.bash_profile** 文件，写入下行：

```bash
[[ $PS1 && -f /usr/local/share/bash-completion/bash_completion.sh ]] && source /usr/local/share/bash-completion/bash_completion.sh
```

立即使用：

```bash
# bash                     # 切换当前 shell 到 Bash
# source ~/.bash_profile    # 重新加载 Bash 配置文件，刷新环境变量
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
