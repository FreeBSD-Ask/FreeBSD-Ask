# 4.4 认识 shell

## 什么是 shell

![](../.gitbook/assets/you-shell.png)

我们的命令运行在 shell 中，并通过 shell 与系统进行交互。

FreeBSD 默认的 shell 是 sh（Bourne shell，原作者为 Stephen R. Bourne）。该实现已被重写，目前基本符合 [POSIX.1-2024](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html) 中对 shell 的规范。

Linux 中常见的 shell 一般是 bash（Bourne Again Shell，即“又一个 Bourne shell”）。而 macOS 中的默认 shell 通常是 zsh（Z shell）。

>**注意**
>
>Linux 中也存在 sh，但通常被软链接到 bash 或其他 shell，它们并不是真正的 sh。
>
>- Ubuntu 24.04 LTS 的默认 shell：
>
>```bash
>$ ls -l /bin/sh  # 以长格式查看 /bin/sh 这个文件的详细信息
>lrwxrwxrwx 1 root root 4  2 月 25 23:19 /bin/sh -> dash
>```

## 快捷键

>**注意**
>
>以下快捷键不一定必须在小写状态下才能执行，在大写状态下同样可以执行。

### 在 TTY 界面上下翻页/翻行

### 使用 Scroll Lock 键在 TTY 界面上下翻页/翻行

使用 **Scroll Lock** 键（滚动锁定键）：按下 **Scroll Lock** 键后，可以使用上 ↑/下 ↓ 方向键以及 **Page Up**/**Page Down** 键对屏幕进行操作。

不同点：

- 上 ↑/下 ↓ 方向键：使 TTY 界面上下滚动一行
- **Page Up**/**Page Down** 键：使 TTY 界面上下滚动一页

再次按下 **Scroll Lock** 键将退出此模式。

>**技巧**
>
>SL 键在 **HOME** 键上方，PS 截图键 **Print Screen** 右侧，PB 键 **Pause break** 左侧。

事实上，从历史角度来看，**Scroll Lock** 键正是为此类用途而设计的。


### 使用 Shift 组合键在 TTY 界面上下翻页/翻行

使用 **Shift** 快捷键：

- **Shift** + 上 ↑/下 ↓ 方向键——使 TTY 界面上下滚动一行
- **Shift** + **Page Up**/**Page Down** 键——使 TTY 界面上下滚动一页

### 补全命令或目录

一般可以使用 **Tab** 键补全命令或目录；上箭头 **↑** 用于查看上一条命令，下箭头 **↓** 用于查看下一条命令。


- 补全命令
  
```sh
# lo # 若此时按 TAB 键，输出如下。可以再输一个字母再按一次 TAB 键看看
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
$ cp /home/ykla/ # 此处按 TAB 键，然后再重复按一次 TAB 键，看看效果
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
^C # 注意这里，^C 即代表你在此处按下了 ctrl + c 的组合键，随后命令被终止
--- 163.com ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 27.580/27.626/27.672/0.046 ms
```

### 命令后台前台

**Ctrl**+**Z**：将当前进程挂起到后台，随后可使用 `fg` 命令将其恢复到前台：

```sh
# ping 163.com  # 测试与 163.com 的网络连通性
PING 163.com (59.111.160.244): 56 data bytes
64 bytes from 59.111.160.244: icmp_seq=0 ttl=52 time=27.611 ms
64 bytes from 59.111.160.244: icmp_seq=1 ttl=52 time=27.691 ms
^Z[1] + Suspended               ping 163.com # 注意此处，按下了 ctrl + z
# fg # 返回前台
ping 163.com
64 bytes from 59.111.160.244: icmp_seq=3 ttl=52 time=27.465 ms
64 bytes from 59.111.160.244: icmp_seq=4 ttl=52 time=27.586 ms
64 bytes from 59.111.160.244: icmp_seq=5 ttl=52 time=27.522 ms
^C # 按 ctrl + c 结束命令
--- 163.com ping statistics ---
6 packets transmitted, 6 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 27.465/27.596/27.701/0.085 ms
```

### 其他

- **Ctrl**+**L**（字母 L）：清空屏幕
- **Ctrl**+**A**：将光标移动到命令行首
- **Ctrl**+**E**：将光标移动到命令行尾
