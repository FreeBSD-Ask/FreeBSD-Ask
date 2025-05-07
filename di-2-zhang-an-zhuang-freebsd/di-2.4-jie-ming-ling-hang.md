# 第 2.4 节 命令行基础（新手入门版本）

## 登录到 FreeBSD

当你安装 FreeBSD 后，若一切正常，你应该会在屏幕上看到以下内容：

```sh
FreeBSD/amd64 (ykla) (ttyv0)

login:
```

我们将这个屏幕上呈现的界面称为 TTY（teletypewriter，电传打字机）或物理终端。

解释：

- `FreeBSD` 是操作系统名称；
- `amd64` 是体系架构，一般英特尔和 AMD 处理器都是 amd64，即 x86-64；
- `ykla` 是主机名，是在安装系统时你自己设置的；
- `ttyv0` 是指首个 TTY，你会发现计算机中大部分事物的序列都是以 0 打头的；
- `login:` 指示用户登录。

我们输入用户名和密码，以登录到系统：

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
root@ykla:~ #

```

祝贺你！你已经成功地登录到了 FreeBSD 操作系统。

>**注意**
>
>密码并不会被回显打印到屏幕上：一般我们输入密码时，屏幕上会显示 `******`。但是在 FreeBSD 中，凡是涉及密码的地方大都不会有任何显示，即使输入了密码屏幕上也是空白的，和没有任何输入是一个状态，就是什么也没有，输入后回车即可。

- ①：root 是 UNIX 中的最高权限。我们常说的安卓 root，苹果越狱，Kindle 越狱等等都是为了获取这个 root 权限权限。

### 参考文献

- [What is TTY in Linux?](https://itsfoss.com/what-is-tty-in-linux/)，翻译在 [Linux 黑话解释：TTY 是什么？](https://linuxstory.org/linux-blackmail-explained-what-is-tty/)。


### 故障排除与未竟事宜

- 若用户名正确，但密码不正确：
  
```sh
login: root
Password:
Login: incorrect # 即不正确的意思
login: 
```

- 若用户名和密码都不正确：

```sh
login: test # 当前系统中不存在该用户
Password:
Login: incorrect
login: 
```

如果你连用户名都不知道，建议你找回 root 密码后看看系统中有哪些用户账户或者重装系统比较快。

## 我是谁？

- 查看当前登录系统的用户名：

```sh
$ whoami
ykla
```

- 查看当前登录用户用户组相关

```sh
$ id
uid=1001(ykla) gid=1001(ykla) groups=1001(ykla),0(wheel)
```

- 查看当前用户登录的中断及本次登录时间

```sh
$ who
root             pts/0        Mar 19 15:00 (3413e8b6b43f)
```

- 展示当前有哪些用户已登录，并且他们在干什么

```sh
$ w
 3:02PM  up 21:52, 1 user, load averages: 0.01, 0.01, 0.00
USER       TTY      FROM           LOGIN@  IDLE WHAT
root       pts/0    3413e8b6b43f   3:00PM     - w
```

- 查看当前所在路径

`pwd` 即 `print work directory`，打印工作目录

```sh
$ pwd
/usr/ports/editors/vscode
```


## 账户切换与退出登录

```sh
root@ykla:/ # su ykla ①
ykla@ykla:/ $ ②
ykla@ykla:/ $ su ③
Password: ④
root@ykla:/ #
root@ykla:/ # exit ⑤
ykla@ykla:/ $ exit ⑥
root@ykla:/ # exit ⑦

FreeBSD/amd64 (ykla) (ttyv0)

login:
```

- ① 使用  `su空格用户名` 可以切换到用户 ykla，从 root 切换的话，不需要输入 ykla 的密码：
  - `root@ykla:/`：
    - `root`：当前用户是 root
    - `@` “谁” `在` “xx”主机上
    - `ykla`：这里是主机名，和用户 ykla 无涉。你可以随便起不一样的主机名
    - `:/`：代表当前在 `/` 路径下
- ② 注意到提示符号的变化没有？root 是 `#`，普通用户是 `$`（csh 是 `%`）
- ③ 如果只是单纯 `su` 回车，命令的意思是从当前用户切换到 root 账户（如果已经是 root，则不会有任何反应）。但是你必须是 wheel 组的成员才能进行此操作，否则会报错 `sorry`。
- ④ 从普通用户切换到 root，要输入的密码是 root 账户的登录密码。
- ⑤ 输入 `exit` 可退出当前用户，如果是唯一登录的用户，将退出登录到 TTY

>**思考题**
>
>⑥、⑦ 分别切换到了哪些用户或执行了哪些操作？

## 命令行格式

大部分命令行命令都应是有意义的，例如 `ls` 即 `list`（列出来）、`wget` 即通过 web（网络）来 `get`（下载）；罕有一些见名不知意的命令，比如 `fuck` 命令（可自动纠正拼写错误的命令）。

```sh
# 命令 选项  参数 1       参数 2
# ls   -l   /home/ykla /tmp
/home/ykla:
total 317
  ……有所省略……
drwxr-xr-x  2 ykla ykla        2 Mar  9 20:45 下载
drwxr-xr-x  2 ykla ykla        2 Mar  9 20:45 
桌面

/tmp:
total 6
drwxrwxrwt  2 root    wheel  3 Mar 18 17:23 .ICE-unix
-r--r--r--  1 root    wheel 11 Mar 18 17:10 .X0-lock
```


其中，`ls`（L 小写）意味着列出当下目录或指定目录下的文件；选项 `-l`（L 小写）意味着打印详细信息，输出长（*long*）的格式。

现在，大部分命令均应遵从上面的方式（有所省略）。这是 [POSIX.1-2024](https://pubs.opengroup.org/onlinepubs/9799919799/) 规范所规定的。

我们需要注意英文和中文是不同的，中文行文间不使用空格进行分割，而英文单词必须使用空格以示分别。故，命令行的每个部分中间应该有空格，即 ``。空格的数量一般不受限制，但最少应该为一个，即``。

>**思考题**
>
>如果不使用空格或某种方式（例如其他符号）对命令行进行分隔，那么软件该如何理解整个句子？
>
>如果不加空格，从自然语言角度，从人类视角看这句话 `Whatwelovedeclarespubliclywhoexactlyweare.` 会是怎样的体验？
>
>换成：`ls-l/home/ykla/tmp`、`ls/` 呢？
>
>```sh
>root@ykla:~ # ls-l/home/ykla/tmp
>-sh: ls-l/home/ykla/tmp: not found
>root@ykla:~ # ls/
>-sh: ls/: not found
>```
>
>可以看到，shell 会将整个句子当成一个可执行的命令去执行。

我们还需要知道，命令是不具有自动纠错功能的，哪怕只是打错了一个字母，少了一个数字，命令也绝不会执行成功：

```sh
root@ykla:~ # LS # 试试全大写
-sh: LS: not found
root@ykla:~ # Ls # 一大一小呢
-sh: Ls: not found
root@ykla:~ # ls /hom1 # 实为 /home
ls: /hom1: No such file or directory
root@ykla:~ # ls -z /home # 不存在选项 -z
ls: invalid option -- z
usage: ls [-ABCFGHILPRSTUWZabcdfghiklmnopqrstuvwxy1,] [--color=when] [-D format] [--group-directories=] [file ...]
```


> **技巧**
>
> 命令后面 `#` 是什么意思？`#` 在 shell 当中一般是起注释作用（由 [POSIX.1-2024](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html) 规定），相当于 C 语言里面的 `//`。意味着后边的文字只起到说明作用，不起实际作用。

>**思考题**
>
>本文已经将日常所需的命令和选项都列出来了。
>
>一个命令的选项或参数可能有几十上百个，而字典或文档（man 也好 info 也罢）是用来查的不是用来背的。
>
>你怎么看“吾生也有涯，而知也无涯。以有涯随无涯，殆已”？

### thefuck：自动纠正错误拼写的命令

#### 安装 thefuck

使用 pkg

```sh
# pkg ins thefuck
```

或者 ports

```sh
# cd /usr/ports/misc/thefuck/
# make install clean
```

#### 配置 thefuck

查看安装后配置信息

```sh
root@ykla:~ # fuck
Seems like fuck alias isn't configured!
More details - https://github.com/nvbn/thefuck#manual-installation
```

我们打开网页浏览。发现要把 `eval $(thefuck --alias)` 加入到 `~/.bash_profile`（bash shell）、`~/.bashrc`（bash shell）或 `~/.zshrc`（zsh shell）。

我们 FreeBSD 默认使用的是 sh，故将：

```sh
eval $(thefuck --alias) 
```

写入 `~/.shrc`，请勿使用 `>>` 重定向，请手动编辑加入。

刷新环境变量：

```sh
root@ykla:~ # . ~/.shrc
root@ykla:~ # fuck
No fucks given
```

>**技巧**
>
>根据作者信息，若不喜欢输入 `fuck`，还可以使用其他别名：若更改为 `eval $(thefuck --alias abc)`，则下方所有 `fuck` 命令都会被换成 `abc`。
>
>```sh
>root@ykla:~ # abc
>Nothing found
>root@ykla:~ # plg install gimp
>-sh: plg: not found
>root@ykla:~ # abc
>​​​​​​​​​​pkg install gimp [enter/↑/↓/ctrl+c]​​​​​​​​​​
>……省略一部分……
>```


#### 测试使用 thefuck

```sh
root@ykla:~ # ls-l /home/ykla/ # 先输入一遍错误的试试
-sh: ls-l: not found
root@ykla:~ # fuck
​​​​​​​​​​ls -l /home/ykla/ [enter/↑/↓/ctrl+c] # 上下箭头切换可能的命令，回车确认，ctrl c 中断​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
total 317
……省略一部分……
drwxr-xr-x  2 ykla ykla        2 Mar  9 20:45 下载
drwxr-xr-x  2 ykla ykla        2 Mar  9 20:45 桌面
```

再试试：

```sh
root@ykla:~ # plg install gimp
-sh: plg: not found
root@ykla:~ # fuck
​​​​​​​​​​pkg install gimp [enter/↑/↓/ctrl+c]​​​​​​​​​​
Updating FreeBSD repository catalogue...
FreeBSD repository is up to date.
……省略一部分……
```

## 命令的执行与中断

与 Windows 以及图形化界面的软件不同，绝大部分命令行程序在执行中是不会有任何进度提示的。通常只有以下两个结果：

- 成功执行：

```sh
root@ykla:~ # cp test /root/mydir/
root@ykla:~ #

```

- 执行中断：

```sh
root@ykla:~ # cp test9 /root/mydir/
cp: test9: No such file or directory
```

执行中断有很多可能的情形，以上只是其中一种（指定的文件或目录不存在）。

可以看到，只有当执行中断时，命令行才会有提示；若执行完毕，是不会有任何提示的。这种 Unix 设计哲学旨在保证终端输出的简洁性。

## Shell

我们的命令是运行在 shell 中的，通过 shell 与系统进行交互。

FreeBSD 默认的 shell 是 sh（Bourne shell，原作者名为 Stephen R. Bourne）。目前已经重写过了，现基本符合 [POSIX.1-2024](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html) 中对 shell 的规范。

Linux 中常见的 shell 一般是 bash（Bourne Again SHell，即“又一个 Bourne shell”）。而 macOS 中的默认 shell 通常是 zsh（Z shell）。

>**注意**
>
>Linux 中也存在 sh，但是一般都是被软链接到了 bash 或其他 shell，她们都不是真正的 sh。
>
>- Ubuntu 24.04 LTS 的默认 shell：
>
>```bash
>$ ls -l /bin/sh
>lrwxrwxrwx 1 root root 4  2 月 25 23:19 /bin/sh -> dash
>```

### 快捷键

>**注意**
>
>以下快捷键不一定非要是小写状态才能执行，大写状态下一样可以执行。

#### 在 TTY 界面上下翻页/翻行

#### 使用 Scroll Lock 键在 TTY 界面上下翻页/翻行

使用 **Scroll Lock** 键（滚动键）：按下 **Scroll Lock** 键后，你可以使用上 ↑/下 ↓ 方向键、**Page Up**/**Page Down** 键来对屏幕进行操作。

不同点：

- 上 ↑/下 ↓ 方向键：使 TTY 界面上下滚动一行
- **Page Up**/**Page Down** 键：使 TTY 界面上下滚动一页

再次按下 **Scroll Lock** 键将退出此模式。

>**技巧**
>
>SL 键在 **HOME** 键上方，PS 截图键 **Print Screen** 右侧，PB 键 **Pause break** 左侧。

事实上，在历史上 **Scroll Lock** 这个按键就是为此而设计的。

#### 使用 Shift 组合键在 TTY 界面上下翻页/翻行

使用 **Shift** 快捷键：

- **Shift** + 上 ↑/下 ↓ 方向键——使 TTY 界面上下滚动一行
- **Shift** + **Page Up**/**Page Down** 键——使 TTY 界面上下滚动一页

#### 补全命令或目录

一般可以用 **Tab** 键补全命令或目录。上箭头 **↑** 是查看上一条命令，下箭头 **↓** 是查看下一条命令。

- 补全命令
  
```sh
root@ykla:~ # lo # 若此时按 TAB 键，输出如下。可以再输一个字母再按一次 TAB 键看看
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

#### 终止命令

若想终止命令，可以用 **ctrl**+**c**：

```sh
root@ykla:~ # ping 163.com
PING 163.com (59.111.160.244): 56 data bytes
64 bytes from 59.111.160.244: icmp_seq=0 ttl=52 time=27.672 ms
64 bytes from 59.111.160.244: icmp_seq=1 ttl=52 time=27.580 ms
^C # 注意这里，^C 即代表你在此处按下了 ctrl + c 的组合键，随后命令被终止
--- 163.com ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 27.580/27.626/27.672/0.046 ms
```

#### 命令后台前台

**ctrl**+**z**: 把当前进程放到后台，然后用 `fg` 命令可回到前台：

```sh
root@ykla:~ # ping 163.com
PING 163.com (59.111.160.244): 56 data bytes
64 bytes from 59.111.160.244: icmp_seq=0 ttl=52 time=27.611 ms
64 bytes from 59.111.160.244: icmp_seq=1 ttl=52 time=27.691 ms
^Z[1] + Suspended               ping 163.com # 注意此处，按下了 ctrl + z
root@ykla:~ # fg # 返回前台
ping 163.com
64 bytes from 59.111.160.244: icmp_seq=3 ttl=52 time=27.465 ms
64 bytes from 59.111.160.244: icmp_seq=4 ttl=52 time=27.586 ms
64 bytes from 59.111.160.244: icmp_seq=5 ttl=52 time=27.522 ms
^C # 按 crtl + c 结束命令
--- 163.com ping statistics ---
6 packets transmitted, 6 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 27.465/27.596/27.701/0.085 ms
```

#### 其他

- **ctrl**+**l**（L 的小写）：清空屏幕
- **ctrl**+**a**：移动光标到命令行首
- **ctrl**+**a**: 移动光标到命令行尾

## 命令的来源

### Linux

在 Linux 中，所有命令基本上都是来自 GNU 软件包的，Linux 内核没有任何命令。我们来验证这一点：

```bash
$ dpkg -S /bin/mv 
coreutils: /bin/mv
$ dpkg -S /bin/cp
coreutils: /bin/cp
$ dpkg -S /bin/ls
coreutils: /bin/ls
$ dpkg -S /bin/pwd
coreutils: /bin/pwd
$ dpkg -S /bin/cat
coreutils: /bin/cat
$ dpkg -S /usr/sbin/chroot
coreutils: /usr/sbin/chroot
$ dpkg -S /bin/kill
procps: /bin/kill
$ dpkg -S /usr/bin/free
procps: /usr/bin/free
$ dpkg -S /bin/su
util-linux: /bin/su
```

可见在 Linux 中，这些常见命令一般出自 GNU 软件 coreutils、util-linux 或 procps。这些软件在历史上是 GNU 计划对 UNIX 软件的再实现。

同时，shell 本身也内置了一些命令：

```bash
$ type cd
cd 是 shell 内建
```

列出所有 shell 内置的命令：

```bash
$ compgen -b
.
:
[
alias
bg
bind
break
builtin
caller
cd
command
compgen
……省略一部分……
ulimit
umask
unalias
unset
wait
```

### FreeBSD

```sh
$ type cd
cd is a shell builtin
```

在 FreeBSD 中，除了上述 shell 内置命令外（参见 [sh(1)](https://man.freebsd.org/cgi/man.cgi?sh(1))），常用命令都是基本系统自带的，不属于任何一个包。比如 `ls` 命令，其源代码位于 [freebsd-src/bin/ls/](https://github.com/freebsd/freebsd-src/tree/main/bin/ls)。可见 FreeBSD 系统是一个有机整体。并非由不同人员或团队维护的软件包拼凑而成的。

如果你配置了 pkgbase，则输出类似：

```sh
# pkg which /bin/ls
/bin/ls was installed by package FreeBSD-runtime-15.snap20250313173555

```


如果缺少了哪个命令，一般可以通过安装相应的软件包来获取，比如 `lspci` 命令，来自软件包 `sysutils/pciutil`。但是也有很多命令存在 Linux 主义问题，不兼容其他操作系统，比如 ip 命令，来自 GNU 软件包 iproute2。

## `ee` 编辑器基本用法

`ee` 是 FreeBSD 基本系统内置的编辑器。

`ee` 的用法比 [nano](https://www.redhat.com/zh/blog/getting-started-nano)（一款 GNU 编辑器）还要简单上许多，你从其名字“easy editor”（简单的编辑器）就能看出来。

比如

```sh
# ee a.txt
```

可以直接编辑，就和 `nano` 或 Windows 记事本一样。

按 **ESC 键**，会显示提示框，按两次 **回车键** 即可保存。

## `vi` 编辑器基本用法

FreeBSD 还有一款内置的编辑器是 `vi`，用法较为复杂。有别于大多数类 UNIX 操作系统将 `vi` 链接到了 `vim` 的做法，BSD 系统内是真正的 `vi`（实际上是 `nvi`，即新 vi，4.4BSD 再实现）。

- macOS 下的 `vi`

```sh
$ ls -al /usr/bin/vi   
lrwxr-xr-x  1 root  wheel  3  4 12 13:16 /usr/bin/vi -> vim
```

打开 BSD 的 `vi` 后默认处于“命令模式”，此时输入 `i`，可以进入到“文本模式”，这时候就可以顺利编辑文本了。需要注意的是，**删除键（退格键）** 不起作用，或者说和 **Insert 键** 表现的一样。要删除文本的话，需要按 **Delete 键**。

```sh
bc123
~      
~
~
```

>**技巧**
>
>空行会显示为 `~`。

编辑完成后，按 **ESC 键** 即可从从文本模式退回到命令模式。

在命令模式下，输入 `:`，即可输入命令，例如：`:q` 是退出不保存、`:wq` 是保存并退出、`:wq!` 是强制保存、`:q!` 是强制退出。


```sh
ABC
~
~
:wq
```

## 常用命令

### `cd` 命令

`cd`（change working directory，更改工作目录）

切换到 `/home`

```
$ cd /home
$ pwd # 看看现在在哪
/home
```

### `ls` 命令

`ls`（list，列出）命令的基本用法上面已经介绍过了，下面试着让 ls 以人类易读的方式列出文件大小：

选项 `-h`，即 `human`（人类），须与 `-l`（`long` 长输出）结合使用。

```sh
# ls -hl /home/ykla
total 326 KB
-rw-------  1 ykla ykla   50B Mar 18 17:23 .Xauthority
drwx------  6 ykla ykla    6B Mar 10 16:21 .cache
drwx------  9 ykla ykla   12B Mar 19 15:01 .config
-rw-r--r--  1 ykla ykla  1.0K Feb 24 12:18 .shrc
drwxr-xr-x  2 ykla ykla    2B Mar  9 23:48 .themes
-rw-r--r--  1 root ykla    0B Mar 19 15:13 abc.TXT
drwxr-xr-x  3 root ykla    7B Mar 19 15:17 vscode
-rw-------  1 ykla ykla   17M Mar 18 17:09 xrdp-chansrv.core
drwxr-xr-x  2 ykla ykla    2B Mar  9 20:45 下载
……省略一部分……
```

在 UNIX 系统中，以 `.` 开头的文件或目录（如上面的 `.XIM-unix`）都是隐藏的。你的安卓手机也是一样的——你可以通过 [MT 文件管理器](https://mt2.cn/) 自行查看一下。

而选项 `-a` 可以显示出来隐藏的目录或文件：

```sh
ykla@ykla:~ $ ls -a
.		.cshrc		.login		.profile	公共		视频
..		.dbus		.login_conf	.sh_history	图片		音乐
.Xauthority	.face		.mail_aliases	.shrc		文档
.cache		.icons		.mailrc		.themes		桌面
.config		.local		.mozilla	下载		模板
```

>**思考题**
>
>```sh
>ykla@ykla:~ $ pwd
>/home/ykla
>ykla@ykla:~ $ cd .
>ykla@ykla:~ $ pwd
>/home/ykla
>ykla@ykla:~ $ cd ..
>ykla@ykla:/home $ pwd
>/home
>ykla@ykla:/home $ cd ..
>ykla@ykla:/ $ pwd
>/
>ykla@ykla:/ $ cd /home/ykla
>ykla@ykla:~ $ cd ../..
>ykla@ykla:/ $ pwd
>/
>```
>
>根据上面的输出，思考：上面的 `.`、`..` 分别代表什么？

试试不加选项 `-a` 呢？

```sh
ykla@ykla:~ $ ls
下载	公共	图片	文档	桌面	模板	视频	音乐
```

则不会显示隐藏文件。

>**技巧**、
>
>请以普通用户进行测试，因为 FreeBSD 的 root shell 总是显示隐藏文件的。

### `touch` 创建文件命令

`touch` 即触碰，意为轻微变动。

创建一个文件，叫 `test`：

```sh
$ touch test
```

>**技巧**
>
>你可以看到我是创建了 `test`，而不是叫什么 `test.txt`、`test.word`、`test.pdf` 之类的。事实上，`.txt` 这部分我们称为后缀名，此部分主要是给人看的，并非机器。许多我们以为的清楚明白的事物真的如我们所认为的那般吗？
>
>即使我们去掉相应的后缀名，在类 UNIX 中也可以识别文件的类型，这是根据文件幻数（magic numbers）确定的：
>
>```sh
>$ file book
>book: PDF document, version 1.7
>```

可以一次性使用多个参数创建多个文件（类似用法几乎是通用的，不再赘述）：

```
$ touch test test1 test2 test3
```

### `mkdir` 创建目录

`mkdir` 即 `make directories`，创建目录

创建一个目录，叫 ykla

```sh
$ mkdir -v ykla # -v 选项可以帮我们看到文件的变动，是 verbose 的缩写，即“啰嗦”一些，意为输出详细信息
ykla
```

如果文件已存在

```sh
$ mkdir ykla
mkdir: ykla: File exists # 提示已经有了该目录了！
```

---

如果要创建目录 `ykla/ykla1/ykla2/ykla3` 呢？

```sh
$ mkdir ykla/ykla1/ykla2/ykla3
mkdir: ykla/ykla1/ykla2: No such file or directory
```

报错如上，此时需要参数 `-p`，`p` 是英文 `parents`（父）的意思，即若上级目录不存在，则一并创建之。

```sh
$ mkdir -vp  ykla/ykla1/ykla2/ykla3
ykla/ykla1
ykla/ykla1/ykla2
ykla/ykla1/ykla2/ykla3
```

### `rm` 删除命令

>**警告**
>
>FreeBSD 命令行界面是没有回收站的，所有命令一经执行不可撤销。命令行操作 `rm` 是比较危险的。

`rm` 即英文 `remove` 的缩写，即删除。

---

删除文件 `test`

```sh
$ rm test
```

若不存在一个叫 `test` 的文件：

```sh
$ rm test
rm: test: No such file or directory # 报错指定的文件或目录不存在
```

---  

删除路径 `/home/ykla/test`

- 若目录为空（不含任何文件，只是空目录）

```sh
$ rm /home/ykla/test
$ 
```

还可以用命令 `rmdir`（remove directory，即删除目录，且只能删除空目录）：

```sh
$  rmdir /home/ykla/test
$ 
```

- 若目录不为空

```sh
$ rm /home/ykla/test/
rm: /home/ykla/test/: is a directory # 提示我们 /home/ykla/test/ 是个目录
```

使用参数 `-r`（recursively）递归、和参数 `-f`（force）强制删除：

>**技巧**
>
>什么是递归？
>
>“从前有座山，山上有座庙，庙里有个老和尚在给小和尚讲故事。老和尚说：“从前有座山，山上有座庙……”这就是递归的实例。
>
>在该操作中，意为先进入 `/home/ykla/test/` 下的最深层的子目录（如有），删除其文件和子目录自身；然后向上重复操作。直至删除 `/home/ykla/test/`。即使用深度优先搜索算法（Depth-First-Search，DFS）。

```sh
$ rm -rf /home/ykla/test/
```

>**警告**
>
>使用 `rm -rf` 是相当危险的操作，是不可撤销的。试想，上述命令若 `/home/ykla/test/` 打错成了 `/home/ykla /test/`（多了个空格），会造成什么后果？
>
>```sh
>root@ykla:~ # rm -rf /home/ykla /test
>root@ykla:~ # ls /home/ykla
>ls: /home/ykla: No such file or directory # 发现已经不存在 ykla 这个目录了
>```

>**警告**
>
>网上经常有人说使用 `sudo rm -rf /*` 是某某命令可以 xxx，误导他人对系统造成不可挽回的灾难性破坏。该命令实质上是以 root 权限（~~还好 FreeBSD 默认没有 sudo~~），删除 `/` 及其子目录下的一切存在。让我来展示一下：
>
>```sh
>root@ykla:/ # rm -rf /*
>rm: /boot/efi: Device busy
>rm: /boot: Directory not empty
>rm: /dev/reroot: Operation not supported
>rm: /dev/input: Operation not supported
>rm: /dev/fd: Operation not supported
>……省略一部分……
>root@ykla:/ # 
>```
>
>![](../.gitbook/assets/noefi.png)
>
>重启后你会发现连引导都没了。
>
>>**思考题**
>>
>>你是否对上面“root 是 UNIX 中的最高权限”这句话有了更深刻的体会？这是否说明了权力和责任的一致性？如果滥用权力，不仅会伤害他人，最后也会致使自己失去存在的现实性。

### `mv` 移动/重命名命令

`mv` 即英文 `move` 的缩写，即移动。

---

将文件 `test` 移动到 `/home/ykla`：

```sh
$ mv -v test /home/ykla # -v 选项可以帮我们看到文件的变动，是 verbose 的缩写，即“啰嗦”一些，意为输出详细信息
test -> /home/ykla/test
```

将目录及子目录移动到 `/home/ykla`

---

- 重命名

将 `test5.pdf` 重命名为 `test5.txt`

```sh
$ mv -v  test5.pdf test5.txt
test5.pdf -> test5.txt
```

将 `test2` 重命名为 `test2.pdf`

```sh
$ mv -v test2 test2.pdf 
test2 -> test2.pdf
```

### `cp` 复制命令

`cp` 即英文 `copy` 的缩写，意为复制。

---

将文件 `test` 复制到 `/home/ykla`

```sh
$ cp test /home/ykla/
```

末尾的 `/` 很重要，如果缺少了末尾的 `/`，且子目录 ykla 不存在的话， `test` 会被重命名为 `ykla`（ykla 在设想中本应是个目录）：

```sh
$ cp test /home/ykla/
cp: directory /home/ykla does not exist # 若加上 /，会提示目录不存在
```

若缺少了末尾的 `/`：

```sh
$ cp -v test /home/ykla # -v 选项可以帮我们看到文件的变动，是 verbose 的缩写，即“啰嗦”一些，意为输出详细信息
test -> /home/ykla
```

>**思考题**
>
>其他命令有没有类似的问题？请你试一试。

---

在复制文件的同时修改其文件名及后缀：

```sh
$ cp -v test /home/ykla/abc.TXT
test -> /home/ykla/abc.TXT
```

该命令通常用于备份配置文件。

---

复制目录及子目录：

```sh
$ cp -v /usr/ports/editors/vscode /home/ykla
cp: /usr/ports/editors/vscode is a directory (not copied).
```

可见直接复制是不行的，提示是目录不是文件。

我们需要选项 `-r`。`r` 是英文 `recursively`（递归）的意思：

```sh
$ cp -vr /usr/ports/editors/vscode /home/ykla
/usr/ports/editors/vscode -> /home/ykla/vscode
/usr/ports/editors/vscode/distinfo -> /home/ykla/vscode/distinfo
……省略一部分……
```

### 正则表达式 `*`

有时操作需要全选，可以使用正则 `*`。

- 删除所有文件名以 `test` 打头的文件：

```sh
$ rm test*
rm: test: is a directory
rm: test4: is a directory
```

可以看到，不会处理目录。

- 删除所有文件名以 `test` 打头的文件和 **目录**：

```sh
$ ls test*  # 确认匹配的文件
$ rm -rf test*
```

- 删除所有文件和 **目录**：

```sh
$ ls *  # 确认匹配的文件
$ rm -rf *
```

### 逻辑运算符 `&&`

`&&`（逻辑与，AND）：只有 `&&`之前的命令执行成功了，后边的命令才会执行；否则如果 `&&` 之前的命令执行失败了，后面的命令就不会执行。

简单理解：你得先做饭才能吃饭，然后才能刷锅——> 做饭 `&&` 吃饭 `&&` 刷锅。如果你没有做饭，自然谈不上怎么吃饭，更遑论刷锅了。

使用场景：执行一连串有依赖关系的命令。比如你得先刷新软件源才能更新系统，然后才能重启。以 Ubuntu 为例：`sudo apt update -y && sudo apt upgrade -y && sudo reboot`。只有前面的命令执行成功，方才会执行后面的命令

### 逻辑运算符 `||`

`||`（逻辑或，OR）：只有 `||` 之前的命令执行错误了，后边的命令才会执行；否则如果 `||` 之前的命令执行成功了，后面的命令就不会执行。

简单理解：你要么做饭，要么点外卖，要么出去吃——> 做饭 `||` 点外卖 `||` 出去吃。如果你不会做饭，你就只能点外卖了，如果外卖没有好吃的，你就只能出去吃了。

使用场景：如果一个命令一直执行失败，但是你偏要他一直执行。你就可以写很多的 `||`，防止一次失败后反复手动再次执行该命令，比如：

```sh
make BATCH=yes install || make BATCH=yes install || make BATCH=yes install || make BATCH=yes install
```

当一次 `make BATCH=yes install` 失败后仍然会执行下一个 `make BATCH=yes install`。即之前的命令执行失败了，转而执行后面的命令……

>**技巧**
>
>`&&` 和 `||` 的优先级相同，并且从左到右执行。

>**思考题**
>
>`touch a.txt && touch b.txt || touch c.txt || reboot` 是什么意思？
>
>如果 `touch a.txt` 失败了会执行后面的哪个操作？

## BSD 风格的 make/grep/sed/awk

FreeBSD 的 [make](https://www.freebsd.org/cgi/man.cgi?query=make&apropos=0&sektion=0&manpath=FreeBSD+13.1-RELEASE+and+Ports&arch=default&format=html)/[grep](https://www.freebsd.org/cgi/man.cgi?query=grep&sektion=&n=1)/[sed](https://www.freebsd.org/cgi/man.cgi?query=sed&apropos=0&sektion=0&manpath=FreeBSD+13.1-RELEASE+and+Ports&arch=default&format=html)/[awk](https://www.freebsd.org/cgi/man.cgi?query=awk&apropos=0&sektion=0&manpath=FreeBSD+13.1-RELEASE+and+Ports&arch=default&format=html) 与 GNU 那套有所不同。详见 man 手册。

示例：

```sh
sed -i '' 's/quarterly/latest/g' /etc/pkg/FreeBSD.conf
```

必须加一个空的参数''，不能省略。



## 关机与重启

​FreeBSD 和 Linux 的 shutdown 命令在语法和行为上有一些重大差异，如果你有使用 Linux 的经验，那么是不能照抄的。

FreeBSD 的设计更接近传统 UNIX 的行为。

关机：

- 使用 `shutdown now` 将不会关机，而是切换到“单用户模式”，将提示：`Enter full pathname of shell or RETURN for /bin/sh :` 回车后进入单用户模式；
- 使用 `shutdown -h now` 将不会彻底断电，只会停止系统的运行，将提示：`The operating system has halted. Please press any key to reboot.` 此处按任意键可重启系统；
- 正确的关机并断电命令是 `poweroff`，等同于命令 `shutdown -p now`。

重启：

- 重启命令和 Linux 一致，都是 `reboot`，但是参数不通用。
- 在 FreeBSD 下 `roboot` 等同于 `shutdown -r now`

>**注意**
>
>关机与重启都需要 root 权限才能执行。

