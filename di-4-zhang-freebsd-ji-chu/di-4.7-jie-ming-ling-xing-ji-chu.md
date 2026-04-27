# 4.7 命令行基础

命令行界面（Command Line Interface, CLI）作为类 UNIX 系统的核心交互方式，提供了直接、高效的系统操作手段。

命令行的基本语法结构遵循 POSIX Shell Command Language 规范（IEEE Std 1003.1），其一般形式为：

```sh
命令 [选项] [参数]
```

其中，选项（option）通常以 `-`（短选项）或 `--`（长选项）开头，用于修改命令的行为；参数（argument）是命令操作的对象。多个短选项可合并书写，如 `-a -l` 等价于 `-al`。命令执行后返回退出状态码（exit status）：0 表示成功，非 0 表示失败，可通过 `$?` 变量查看（IEEE. POSIX.1-2017, Shell Command Language[EB/OL]. [2026-04-26]. ，<https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html>.）

Shell 还提供了管道（pipe）、重定向（redirection）和通配符（globbing）三种核心组合机制：管道通过 `|` 将一个命令的输出连接到另一个命令的输入；重定向通过 `>`、`<`、`>>` 改变命令的标准输入/输出方向；通配符通过 `*`、`?`、`[]` 匹配文件名模式。

## 我是谁？

- 查看当前登录系统的用户名：

```sh
$ whoami
ykla
```

>**技巧**
>
>`whoami` 已被 id(1) 替代，等价于 `id -un`。

- 查看当前登录用户所属用户组的信息。

```sh
$ id
uid=1001(ykla) gid=1001(ykla) groups=1001(ykla),0(wheel)
```

- 查看当前用户登录的终端及本次登录时间。

```sh
$ who
root             pts/0        Mar 19 15:00 (3413e8b6b43f)
```

BSD who 与 GNU/Linux 的 `who` 差异较大；FreeBSD 的 `who` 不支持 Linux 的 `-d`（死进程）、`-p`（init 活动进程）、`--lookup`、`--ips` 等选项。

## 我从哪里来？

展示当前有哪些用户已登录，以及他们正在做什么：

```sh
$ w
 3:02PM  up 21:52, 1 user, load averages: 0.01, 0.01, 0.00
USER       TTY      FROM           LOGIN@  IDLE WHAT
root       pts/0    3413e8b6b43f   3:00PM     - w
```

BSD `w` 与 GNU/Linux 的 `w` 差异较大；FreeBSD 的 `w` 不支持 Linux `w` 的 `-f`（省略 FROM 列）、`-s`（短格式）、`-u`（省略 USER 列）等选项。

## 我在哪？

- 查看当前所在路径。

`pwd` 即 `print working directory`，用于打印当前工作目录。

```sh
$ pwd
/usr/ports/editors/vscode
```

BSD `pwd` 与 POSIX 标准兼容；与 GNU/Linux 的 `pwd` 基本兼容。

## 我究竟是谁？

账户切换与退出登录：

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

- ① 使用 `su空格用户名` 可以切换到用户 ykla。若从 root 切换到 ykla，则不需要输入 ykla 的密码：
  - `root@ykla:/`：
  - `root`：当前用户是 root
  - `@`：“谁”在“xx”主机上
  - `ykla`：这里是主机名，和用户 ykla 无关。可以随便起不一样的主机名
  - `:/`：代表当前位于 `/` 路径下
- ② 注意到提示符号的变化没有？root 是 `#`，普通用户是 `$`（csh 是 `%`）
- ③ 如果仅输入 `su` 并回车，命令的含义是从当前用户切换到 root 账户（如果已经是 root，则不会有任何变化）。非 wheel 组成员不能直接 `su` 到 root，否则会报错 `sorry`，但可以 `su` 到其他用户。
- ④ 从普通用户切换到 root，需要 root 账户的登录密码。
- ⑤ 输入 `exit` 可退出当前用户，如果是唯一登录的用户，将退出登录到 TTY。

> **思考题**
>
> ⑥、⑦ 分别切换到了哪些用户或执行了哪些操作？

`su` 命令只能切换到在 `/etc/shells` 中列出的 shell。`su -` 或 `su -l` 不仅切换用户，还会将工作目录切换到目标用户的主目录，并重置环境变量。

BSD 与 GNU `su` 行为比较：

| 项目 | FreeBSD `su` 行为 | Linux `su` 行为 |
| ---- | ----------------- | --------------- |
| `-c` | 指定 login class（登录类） | 执行指定命令（command） |
| `-s` | 设置 MAC label（强制访问控制标签） | 指定登录 shell |
| 执行命令方式 | 将命令作为参数传递给目标用户 shell 执行 | 使用 `-c` 直接执行命令 |

## 我要去哪里？

`cd` 命令，即“change the working directory”，切换当前工作目录。

```sh
ykla@ykla:~ $ pwd
/home/ykla
ykla@ykla:~ $ cd .
ykla@ykla:~ $ pwd
/home/ykla
ykla@ykla:~ $ cd ..
ykla@ykla:/home $ pwd
/home
ykla@ykla:/home $ cd ..
ykla@ykla:/ $ pwd
/
ykla@ykla:/ $ cd /home/ykla
ykla@ykla:~ $ cd ../..
ykla@ykla:/ $ pwd
/
```

根据上面的输出，请读者思考：上面的 `.` 和 `..` 分别代表什么？

>**技巧**
>
>在 FreeBSD 的 sh(1) 中，`cd` 的行为由 POSIX 标准规定。

## 命令行格式

大部分命令行命令的名称都具有明确含义，例如 `ls` 即 `list`（列出）、`wget` 即通过 web（网络）来 `get`（下载）；也存在少量见名不知义的命令，例如 `thefuck` 命令（用于自动纠正拼写错误）。

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

其中，`ls`（L 小写）意味着列出当前目录或指定目录下的文件；选项 `-l`（L 小写）意味着打印详细信息，输出长（*long*）格式。

目前，大多数命令均遵循上述形式（细节有所省略）。这是 [POSIX.1-2024](https://pubs.opengroup.org/onlinepubs/9799919799/) 规范所规定的。

需要注意中英文书写习惯的差异：中文行文不使用空格分隔，而英文单词必须使用空格加以区分。因此，命令行中各个组成部分之间应使用空格分隔 ` `。空格的数量一般不受限制，但最少应该为一个，即 ` `。

> **思考题**
>
> 如果不使用空格或某种方式（例如其他符号）对命令行进行分隔，那么软件该如何理解整个句子？
>
> 如果不加空格，从自然语言角度，从人类视角看这句话 `Whatwelovedeclarespubliclywhoexactlyweare.` 会是怎样的体验？
>
> 再看：`ls-l/home/ykla/tmp`、`ls/` 呢？
>
> ```sh
> # ls-l/home/ykla/tmp
> -sh: ls-l/home/ykla/tmp: not found
> # ls/
> -sh: ls/: not found
> ```
>
> 可以看到，shell 会将整个字符串当作一个可执行命令来解析和执行。

还需要注意，命令行本身不具备自动纠错功能，即使仅拼错一个字母或少输入一个字符，命令也无法正确执行。

```sh
# LS # 试试全大写
-sh: LS: not found
# Ls # 一大一小呢
-sh: Ls: not found
# ls /hom1 # 实为 /home
ls: /hom1: No such file or directory
# ls -z /home # 不存在选项 -z
ls: invalid option -- z
usage: ls [-ABCFGHILPRSTUWZabcdfghiklmnopqrstuvwxy1,] [--color=when] [-D format] [--group-directories=] [file ...]
```

> **技巧**
>
> Windows 不仅对文件名大小写不敏感，对命令名称的大小写也不敏感。
>
>```powershell
> PS C:\Users\ykla> cd C:\ # 这里 cd 是小写
> PS C:\> CD D:\ # 这里 CD 是大写
> PS D:\> CD c:\ # 这里 C 盘是小写
> PS C:\> dir # 小写 dir，列出目录，等于 ls
>
>     目录：C:\
>
> ……省略一部分……
>
> PS C:\Users\ykla> TREE # 大写 tree，显示路径关系
> 文件夹 PATH 列表
> 卷序列号为 2A90-E989
> C:.
> ├─.android
> ├─.cache
> │ ├─selenium
> ……省略一部分……
>```

> **技巧**
>
> 命令前面的 `#` 表示什么意思？`#` 在 shell 当中一般是起注释作用（由 [POSIX.1-2024](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html) 规定），相当于 C 语言中的 `//`。意味着后边的文字只起到说明作用，不起实际作用。
>

## 命令的执行与中断

与 Windows 及图形化界面软件不同，绝大多数命令行程序在执行过程中不会显示进度提示。通常只有以下两种结果：

- 成功执行：

```sh
# cp test /root/mydir/


```

- 执行中断：

```sh
# cp test9 /root/mydir/
cp: test9: No such file or directory
```

执行中断有很多可能的情形，以上只是其中一种（指定的文件或目录不存在）。

可以看到，只有当执行中断时，命令行才会有提示；若执行完毕，是不会有任何提示的。这种 UNIX 设计哲学旨在保证终端输出的简洁性。

## shell 命令的来源

### Linux

在 Linux 中，大多数常用命令来自 GNU 等用户空间软件包，Linux 内核本身并不提供用户级命令。来验证这一点：

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

列出所有 shell 内置命令：

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

在 FreeBSD 中，除了上述 shell 内置命令外（参见：sh(1)[EB/OL]. [2026-03-26]. <https://man.freebsd.org/cgi/man.cgi?sh(1)>），常用命令都是基本系统自带的，不属于任何一个包。比如 `ls` 命令，其源代码位于 `freebsd-src/bin/ls/`[EB/OL]. [2026-03-26]. <https://github.com/freebsd/freebsd-src/tree/main/bin/ls>。可见 FreeBSD 系统是一个有机整体，而非由不同人员或团队维护的软件包简单拼凑而成。

如果配置了 pkgbase，则输出类似：

```sh
# pkg which /bin/ls # 查询 /bin/ls 所属的软件包
/bin/ls was installed by package FreeBSD-runtime-15.snap20250313173555
```

如果缺少了哪个命令，一般可以通过安装相应的软件包来获取，比如 `lspci` 命令，来自软件包 `sysutils/pciutils`。但是也有很多命令存在 Linux 主义问题，不兼容其他操作系统，比如 `ip` 命令，来自软件包 iproute2。

## 常用命令

### `cd` 命令

`cd`（change working directory，更改工作目录）

切换到 `/home`：

```sh
$ cd /home # 切换到 `/home`
$ pwd # 看看现在在哪
/home
```

### `ls` 命令

`ls`（list，列出）命令的基本用法前文已经介绍，下面演示如何让 `ls` 以人类易读的方式显示文件大小：

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

在 UNIX 系统中，以 `.` 开头的文件或目录（如上面的 `.Xauthority`）都是隐藏的。Android 手机也是一样的——可以通过 [MT 文件管理器](https://mt2.cn/) 自行查看。

选项 `-a` 可用于显示隐藏的目录和文件：

```sh
$ ls -a
.		.cshrc		.login		.profile	公共		视频
..		.dbus		.login_conf	.sh_history	图片		音乐
.Xauthority	.face		.mail_aliases	.shrc		文档
.cache		.icons		.mailrc		.themes		桌面
.config		.local		.mozilla	下载		模板
```

试试不加选项 `-a` 呢？

```sh
ykla@ykla:~ $ ls
下载	公共	图片	文档	桌面	模板	视频	音乐
```

则不会显示隐藏文件。

> **技巧**
>
> 请以普通用户进行测试，因为 FreeBSD 的 root shell 总是显示隐藏文件。

### `touch` 创建文件命令

`touch` 的字面含义为“触碰”，表示对文件时间戳进行轻微变动。

FreeBSD 的 `touch` 与 POSIX 标准兼容，来源于 4.3BSD。

创建一个文件，命名为 `test`：

```sh
$ touch test
```

> **技巧**
>
> 可以看到上述命令创建的是 `test`，而非 `test.txt`、`test.word`、`test.pdf` 之类的。事实上，`.txt` 这一部分称为文件后缀名，主要用于提示用户文件类型，而非供系统识别。许多我们以为，清楚明白的事物真的如我们所认为的那般吗？
>
> 即使去掉相应的后缀名，在类 UNIX 系统中也可以识别文件的类型，这是根据文件幻数（magic numbers）确定的：
>
>```sh
> $ file book
> book: PDF document, version 1.7
>```

`file` 命令通过三组测试依次判定文件类型：文件系统测试（基于 stat(2)）、幻数测试（基于 `/usr/share/misc/magic.mgc` 中的固定格式标识）和语言测试（基于文本模式匹配）。其中“幻数”（magic number）概念源于 UNIX 可执行文件格式，文件头部特定偏移量处存储的固定标识用于指示文件类型。

FreeBSD 的 `file` 来自 file 软件包（与 GNU/Linux 采用相同的上游源码），因此基本兼容。主要差异在于魔法数据库文件路径可能不同。

可以一次性使用多个参数创建多个文件（类似用法几乎是通用的，不再赘述）：

```sh
$ touch test test1 test2 test3
```

### `mkdir` 创建目录

`mkdir` 即 `make directories`，创建目录

创建一个目录，命名为 ykla。

```sh
$ mkdir -v ykla # -v 选项可以帮我们看到文件的变动，是 verbose 的缩写，即“啰嗦”一些，意为输出详细信息
ykla
```

如果文件已存在：

```sh
$ mkdir ykla
mkdir: ykla: File exists # 提示该目录已存在。
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

FreeBSD 的 `mkdir` 与 GNU/Linux 的 `mkdir` 基本兼容。

### `rm` 删除命令

> **警告**
>
> FreeBSD 命令行界面是没有回收站的，所有命令一经执行不可撤销。命令行操作 `rm` 是比较危险的。

`rm` 即英文 `remove` 的缩写，意为删除。

---

删除文件 `test`

```sh
$ rm test
```

若不存在一个名称为 `test` 的文件：

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

使用参数 `-r`（recursively）递归，参数 `-f`（force）强制删除：

> **技巧**
>
> 什么是递归？
>
> “从前有座山，山上有座庙，庙里有个老和尚在给小和尚讲故事。老和尚说：‘从前有座山，山上有座庙……’”这就是递归的实例。
>
> 在该操作中，其含义是先进入 `/home/ykla/test/` 下最深层的子目录（如存在），删除其中的文件和子目录本身，然后向上逐层重复该过程。直至删除 `/home/ykla/test/`。即使用深度优先搜索算法（Depth-First-Search，DFS）。

```sh
$ rm -rf /home/ykla/test/
```

> **警告**
>
> 使用 `rm -rf` 是相当危险的操作，是不可撤销的。若命令中误输入空格，如将 `/home/ykla/test/` 打错成 `/home/ykla /test/`，会导致删除路径错误：
>
>```sh
> # rm -rf /home/ykla /test
> # ls /home/ykla
> ls: /home/ykla: No such file or directory # 发现已经不存在 ykla 这个目录了
>```

> **警告**
>
> 网上经常有人说使用 `sudo rm -rf /*` 是某某命令可以 xxx，误导他人对系统造成不可挽回的灾难性破坏。该命令实质上是以 root 权限（~~还好 FreeBSD 默认没有 sudo~~），删除 `/` 及其子目录下的一切存在。现在展示一下结果：
>
>```sh
> # rm -rf /*
> rm: /boot/efi: Device busy
> rm: /boot: Directory not empty
> rm: /dev/reroot: Operation not supported
> rm: /dev/input: Operation not supported
> rm: /dev/fd: Operation not supported
> ……省略一部分……
> #
>```
>
> ![引导错误](../.gitbook/assets/noefi.png)
>
> 重启后即可发现引导项丢失。
>
>> **思考题**
>>
>> 你是否对上面“root 是 UNIX 中的最高权限”这句话有了更深刻的体会？这是否说明了权力和责任的一致性？如果滥用权力，不仅会伤害他人，最后也会导致自己失去存在的现实性。

### `mv` 移动/重命名命令

`mv` 即英文 `move` 的缩写，意为移动。

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

末尾的 `/` 很重要，如果缺少了末尾的 `/`，且子目录 ykla 不存在，`test` 将被重命名为 `ykla`（ykla 在设想中本应是个目录）：

```sh
$ cp test /home/ykla/
cp: directory /home/ykla does not exist # 若加上 /，会提示目录不存在
```

若缺少了末尾的 `/`：

```sh
$ cp -v test /home/ykla # -v 选项可以帮我们看到文件的变动，是 verbose 的缩写，即“啰嗦”一些，意为输出详细信息
test -> /home/ykla
```

> **思考题**
>
> 其他命令有没有类似的问题？请试一试。

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

可见直接复制是不可行的，提示是目录不是文件。

因此还需要选项 `-r`。`r` 是英文 `recursively`（递归）的意思：

```sh
$ cp -vr /usr/ports/editors/vscode /home/ykla
/usr/ports/editors/vscode -> /home/ykla/vscode
/usr/ports/editors/vscode/distinfo -> /home/ykla/vscode/distinfo
……省略一部分……
```

### 通配符 `*`

有时操作需要全选，可以使用通配符 `*`。

- 删除所有文件名以 `test` 开头的文件：

```sh
$ rm test*
rm: test: is a directory
rm: test4: is a directory
```

可以看到，不会处理目录。

- 删除所有文件名以 `test` 开头的文件和 **目录**：

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

`&&`（逻辑与，AND）：只有 `&&` 之前的命令执行成功了，才会执行后续的命令；否则如果 `&&` 之前的命令执行失败，后面的命令就不会执行。

简单理解：得先做饭才能吃饭，然后才能刷锅 → 做饭 `&&` 吃饭 `&&` 刷锅。如果没有做饭，自然谈不上吃饭，更遑论刷锅了。

使用场景：执行一连串有依赖关系的命令。比如得先刷新软件源才能更新系统，然后才能重启。以 Ubuntu 为例：`sudo apt update -y && sudo apt upgrade -y && sudo reboot`。只有前面的命令执行成功，才会执行后面的命令。

### 逻辑运算符 `||`

`||`（逻辑或，OR）：只有 `||` 之前的命令执行失败时，后边的命令才会执行；如果 `||` 之前的命令执行成功，后面的命令就不会执行。

简单理解：要么做饭，要么点外卖，要么出去吃——> 做饭 `||` 点外卖 `||` 出去吃。如果不会做饭，就只能点外卖，如果外卖没有好吃的，就只能出去吃。

使用场景：如果一个命令一直执行失败，但偏要它一直执行。就可以写很多 `||`，防止一次失败后反复手动再次执行该命令，比如：

```sh
make BATCH=yes install || make BATCH=yes install || make BATCH=yes install || make BATCH=yes install
```

当一次 `make BATCH=yes install` 失败后，仍然会执行下一个 `make BATCH=yes install`。即之前的命令执行失败，转而执行后面的命令。

> **技巧**
>
> `&&` 和 `||` 的优先级相同，且按从左到右的顺序进行求值。

> **思考题**
>
> `touch a.txt && touch b.txt || touch c.txt || reboot` 是什么意思？
>
> 如果 `touch a.txt` 失败会执行后面的哪个操作？

## 进程与守护进程

FreeBSD 是一个多任务操作系统。每个在任何时刻运行的程序都称为进程。每个运行的命令至少启动一个新进程，此外还有许多由 FreeBSD 运行的系统进程。

每个进程都由一个称为进程 ID（PID）的数字唯一标识。与文件类似，每个进程都有一个所有者和组，所有者和组权限用于确定进程可以打开哪些文件和设备。大多数进程还有一个启动它们的父进程。例如，Shell 是一个进程，在 Shell 中启动的任何命令都是以 Shell 为父进程的进程。例外是一个名为 init(8) 的特殊进程，它始终是启动时第一个启动的进程，并且始终具有 PID 1。

有些程序不设计为持续接收用户输入，并在第一次机会时与终端断开连接。例如，Web 服务器响应 Web 请求而非用户输入，邮件服务器是此类应用程序的另一个例子。这些类型的程序被称为守护进程（daemon）。术语“daemon”来自希腊神话，代表一种既非善也非恶的实体，它无形中执行有用的任务。这就是 BSD 吉祥物是那个穿着运动鞋和拿着草叉的快乐守护进程的原因。

有一种命名约定，即通常作为守护进程运行的程序名称以字母“d”结尾。例如，BIND 是 Berkeley Internet Name Domain，但实际执行的程序名为 named。Apache Web 服务器程序是 httpd，行式打印机假脱机守护进程是 lpd。这只是一个命名约定，例如 Sendmail 应用程序的主要邮件守护进程是 sendmail，而不是 maild。

### 查看进程

在某些情况下，带有 `ww` 选项的 `ps` 可能仍然被截断，因为内核中存储的命令行长度有限制。对于内核线程，命令字段可能显示为 `[ ]` 包裹的名称。

FreeBSD 的 `ps` 基于 4.4BSD。特别注意：FreeBSD 的 `-u` 是显示格式选项，用户过滤应使用 `-U`。FreeBSD 支持 `-G` 显示组。

用户只能向自己拥有的进程发送信号，root 用户可以向任何进程发送信号。SIGKILL 和 SIGSTOP 信号不可被捕获或忽略。特殊 PID：`0` 发送到同组所有进程，`-1` 发送到所有进程（root）或自己的所有进程。

要查看系统上运行的进程，使用 ps(1) 或 top(1)。要显示当前运行进程的静态列表（包括它们的 PID、内存使用量和启动命令），使用 ps(1)。要以交互方式显示所有运行进程并每隔几秒更新显示以查看计算机正在做什么，使用 top(1)。

默认情况下，ps(1) 仅显示由当前用户拥有且正在运行的命令：

```sh
% ps
 PID TT  STAT    TIME COMMAND
8203  0  Ss   0:00.59 /bin/csh
8895  0  R+   0:00.00 ps
```

ps(1) 的输出组织为多个列。PID 列显示进程 ID。PID 从 1 开始分配，上升到 99999，然后回到开头。但是，如果 PID 已在使用中，则不会重新分配。TT 列显示程序运行所在的 tty，STAT 显示程序的状态。TIME 是程序在 CPU 上运行的时间量，这通常不是程序启动以来的经过时间，因为大多数程序在需要花费 CPU 时间之前会花大量时间等待事情发生。最后，COMMAND 是用于启动程序的命令。

有许多不同的选项可用于更改显示的信息。最有用的选项集之一是 `auxww`，其中 `a` 显示所有用户的所有运行进程的信息，`u` 显示进程所有者的用户名和内存使用量，`x` 显示守护进程的信息，`ww` 使 ps(1) 显示每个进程的完整命令行，而不是在太长无法适应屏幕时截断。

top(1) 的输出类似：

```sh
% top
last pid:  9609;  load averages:  0.56,  0.45,  0.36              up 0+00:20:03  10:21:46
107 processes: 2 running, 104 sleeping, 1 zombie
CPU:  6.2% user,  0.1% nice,  8.2% system,  0.4% interrupt, 85.1% idle
Mem: 541M Active, 450M Inact, 1333M Wired, 4064K Cache, 1498M Free
ARC: 992M Total, 377M MFU, 589M MRU, 250K Anon, 5280K Header, 21M Other
Swap: 2048M Total, 2048M Free

  PID USERNAME    THR PRI NICE   SIZE    RES STATE   C   TIME   WCPU COMMAND
  557 root          1 -21  r31   136M 42296K select  0   2:20  9.96% Xorg
 8198 dru           2  52    0   449M 82736K select  3   0:08  5.96% kdeinit4
 8311 dru          27  30    0  1150M   187M uwait   1   1:37  0.98% firefox
```

输出分为两个部分。头部（前五六行）显示最后运行的进程的 PID、系统负载平均值（衡量系统繁忙程度的指标）、系统正常运行时间（自上次重启以来的时间）和当前时间。头部中的其他数字与运行中的进程数量、已使用的内存和交换空间数量，以及系统在不同 CPU 状态下花费的时间有关。如果已加载 ZFS 文件系统模块，ARC 行指示从内存缓存而非磁盘读取了多少数据。

头部下方是一系列列，包含与 ps(1) 输出类似的信息，如 PID、用户名、CPU 时间量和启动进程的命令。默认情况下，top(1) 还显示进程占用的内存空间量，分为两列：一列用于总大小，一列用于驻留大小。总大小是应用程序需要的内存量，驻留大小是它当前实际使用的量。top(1) 默认每两秒自动更新显示，可以使用 `-s` 指定不同的间隔。

在非常繁忙的系统上，top 可能显示略过时的信息，因为采样需要时间。

### 终止进程

与任何运行中的进程或守护进程通信的一种方式是使用 kill(1) 发送信号。有许多不同的信号；有些具有特定含义，而其他信号在应用程序的文档中描述。用户只能向自己拥有的进程发送信号，向其他人的进程发送信号将导致权限拒绝错误。例外是 root 用户，他可以向任何人的进程发送信号。

操作系统也可以向进程发送信号。如果应用程序编写不当并试图访问不应访问的内存，FreeBSD 将向进程发送“段违规”信号（SIGSEGV）。如果应用程序编写为使用 alarm(3) 系统调用在一段时间后收到警报，它将收到“闹钟”信号（SIGALRM）。

两个信号可用于停止进程：SIGTERM 和 SIGKILL。SIGTERM 是终止进程的礼貌方式，因为进程可以读取信号、关闭可能打开的任何日志文件，并尝试在关闭之前完成正在做的事情。在某些情况下，如果进程正在执行某些无法中断的任务，它可能会忽略 SIGTERM。

SIGKILL 不能被进程忽略。向进程发送 SIGKILL 通常会立即停止该进程。

其他常用的信号是 SIGHUP、SIGUSR1 和 SIGUSR2。由于这些是通用信号，不同的应用程序会有不同的响应。例如，在更改 Web 服务器的配置文件后，需要告诉 Web 服务器重新读取其配置。重启 httpd 会导致 Web 服务器短暂停机。相反，向守护进程发送 SIGHUP 信号。请注意，不同的守护进程会有不同的行为，因此请参阅守护进程的文档以确定 SIGHUP 是否能达到预期的结果。

杀死系统上的随机进程是一个坏主意。特别是 init(8)，PID 1，是特殊的。运行 `/bin/kill -s KILL 1` 是一种快速但不推荐的关闭系统的方法。在按下回车键之前，务必仔细检查 kill(1) 的参数。

## 设备与设备节点

设备是系统中主要用于与硬件相关活动的术语，包括磁盘、打印机、显卡和键盘。当 FreeBSD 启动时，大多数启动消息都与正在检测的设备有关。启动消息的副本保存在 `/var/run/dmesg.boot` 中。

每个设备都有一个设备名称和编号。例如，`ada0` 是第一个 SATA 硬盘，而 `kbd0` 代表键盘。

FreeBSD 中的大多数设备必须通过称为设备节点的特殊文件访问，这些文件位于 `/dev` 目录中。

在 FreeBSD 中，设备节点由 devfs(5) 文件系统自动管理。devfs 是一个虚拟文件系统，在系统启动时由内核自动挂载到 `/dev`，并根据当前系统中存在的硬件设备动态创建和删除设备节点。这与传统 UNIX 系统需要手动使用 `mknod` 命令创建设备节点的做法不同。devfs 确保了 `/dev` 目录中只包含当前系统实际存在的设备节点，避免了设备节点的冗余。

设备节点分为两种类型：字符设备（character device）和块设备（block device）。字符设备以字节流方式访问数据，如终端（`/dev/ttyv0`）和串口；块设备以固定大小的块为单位访问数据，如磁盘（`/dev/ada0`）。在 `ls -l` 的输出中，字符设备的类型标识为 `c`，块设备的类型标识为 `b`。

设备命名遵循一定的约定：SATA 硬盘以 `ada` 开头（如 `ada0`、`ada1`），SCSI 硬盘和 USB 存储设备以 `da` 开头（如 `da0`），NVMe 存储以 `nvd` 或 `nda` 开头，CD-ROM 驱动器以 `cd` 开头。编号从 0 开始。GPT 分区在设备名后附加 `p` 加分区号（如 `ada0p1`），MBR 切片附加 `s` 加切片号（如 `ada0s1`）。

`dmesg` 显示的是内核消息缓冲区的内容，该缓冲区大小有限，旧消息可能被新消息覆盖。系统启动时的 `dmesg` 输出副本自动保存至 `/var/run/dmesg.boot`。可通过 sysctl 变量 `kern.msgbuf_show_timestamp` 控制时间戳显示：`0` 为不显示，`1` 为秒级精度，`2` 为微秒级精度。

## 手册页

FreeBSD 上最全面的文档以手册页的形式存在。系统上几乎每个程序都附带一份简短的参考手册，解释基本操作和可用参数。这些手册可以使用 man 命令查看：

```sh
% man command
```

其中 `command` 是要了解的命令名称。例如，要了解更多关于 ls(1) 的信息，输入：

```sh
% man ls
```

手册页分为多个节，代表主题的类型。在 FreeBSD 中，以下章节可用：

1. 用户命令。
2. 系统调用和错误编号。
3. C 库中的函数。
4. 设备驱动程序。
5. 文件格式。
6. 游戏和其他娱乐。
7. 杂项信息。
8. 系统维护和操作命令。
9. 系统内核接口。

在某些情况下，同一主题可能出现在在线手册的多个节中。例如，既有 chmod 用户命令，也有 chmod() 系统调用。要告诉 man(1) 显示哪个节，指定节号：

```sh
% man 1 chmod
```

这将显示用户命令 chmod(1) 的手册页。在书面文档中，对在线手册特定节的引用传统上放在括号中，因此 chmod(1) 指的是用户命令，chmod(2) 指的是系统调用。

如果不知道手册页的名称，使用 `man -k` 搜索手册页描述中的关键词：

```sh
% man -k mail
```

此命令显示描述中包含关键词“mail”的命令列表。这等效于使用 apropos(1)。

要阅读 `/usr/sbin` 中所有命令的描述，输入：

```sh
% cd /usr/sbin
% man -f * | more
```

或：

```sh
% cd /usr/sbin
% whatis * | more
```

## BSD 风格的 make/grep/sed/awk

### make(1) 命令

make(1) 命令选项：

| 选项 | 说明 | 备注 |
| ---- | ---- | ---- |
| `-f <Makefile>` | 指定 Makefile 文件名 | 默认查找 makefile 或 Makefile |
| `-j <作业数>` | 并行执行的作业数 | 并行构建；指定 CPU 核心数 |
| `-n` | 不执行，仅打印命令 | 显示会执行什么但不实际执行 |
| `-k` | 出错时继续构建其他目标 | 即使某个目标失败也尽可能继续 |
| `-s` | 静默模式，不打印命令 | 简洁输出 |
| `-C <目录>` | 切换到目录后执行 | 先进入指定目录 |

FreeBSD 的 make（bmake）与 GNU make（gmake）在语法和内置变量上有显著差异。FreeBSD make 不支持 GNU make 的许多高级特性，如 `$(wildcard ...)` 的某些用法、条件语句语法等。FreeBSD make 使用 `.include` 而 GNU make 使用 `include`；变量赋值语法 `?=`、`:=` 的行为也不同。在 FreeBSD 上，可安装 devel/gmake 以获得 GNU make。

### sed(1) 命令

FreeBSD sed 基于 4.4BSD lite sed，与 GNU sed 在正则表达式语法、一些扩展命令（如 `\l`、`\u`、`\L`、`\U`）、地址范围语法上存在差异。GNU sed 支持 `\w`、`\W`、`\b`、`\B` 等字符类，而 FreeBSD sed 需要使用 `[[:alnum:]]` 等 POSIX 类。

sed(1) 命令命令选项：

| 选项 | 说明 | 备注 |
| ---- | ---- | ---- |
| `-i <后缀>` | 原地编辑文件 | 备份文件使用指定后缀；空后缀不备份 |
| `-e <脚本>` | 添加脚本到执行列表 | 可多次使用，按顺序执行 |
| `-n` | 不自动打印行 | 仅在使用 `p` 命令时输出 |
| `-f <文件>` | 从文件读取脚本 | 替代 `-e` |
| `-E` | 使用扩展正则表达式 | 同 GNU sed 的 `-r` 选项 |
| `-r` | 同上，兼容性别名 | |

与 GNU sed 最显著的差异是 `-i` 选项语法：FreeBSD sed 的 `-i` 必须有后缀参数，即使是空字符串（`-i ''`），而 GNU sed 的 `-i` 后缀是可选的（`-i[SUFFIX]`）。这是最常见的跨平台兼容性问题。

示例：

```sh
sed -i '' 's/quarterly/latest/g' /etc/pkg/FreeBSD.conf
```

必须提供一个空参数 `''`，且不能省略。

### awk(1) 命令

awk(1) 命令选项：

| 选项 | 说明 | 备注 |
| ---- | ---- | ---- |
| `-F <分隔符>` | 指定字段分隔符 | 可以是正则表达式；同 `FS` 变量 |
| `-v <var>=<val>` | 在执行前设置变量 | 可多次使用 |
| `-f <文件>` | 从文件读取脚本 | 替代命令行脚本 |
| `-W <选项>` | 扩展选项（兼容 GNU awk） | FreeBSD awk 部分支持 |

FreeBSD 默认的 awk 是 nawk（New AWK），基于 Aho、Kernighan、Weinberger 的原始实现，与 GNU awk（gawk）有许多差异。GNU awk 有大量扩展，如：多维数组、网络操作、时间函数、`length(array)`、`gensub()`、`strftime()` 等，这些在 FreeBSD nawk 中不可用。在 FreeBSD 上，可安装 lang/gawk 获得 GNU awk。

### grep(1) 命令

grep(1) 命令选项：

| 选项 | 说明 | 备注 |
| ---- | ---- | ---- |
| `-r` | 递归搜索目录 | |
| `-i` | 忽略大小写 | |
| `-n` | 显示行号 | |
| `-l` | 仅显示包含匹配的文件名 | 不显示匹配内容 |
| `-v` | 反转匹配，显示不匹配的行 | |
| `-E` | 使用扩展正则表达式 | 等同于 `egrep` |
| `-c` | 仅显示匹配行数 | |

FreeBSD 基本系统的 grep 是 BSD grep（基于 GNU grep 2.0 的旧版分支），与 Linux 上的 GNU grep 在正则表达式语法和选项上基本兼容；但 BSD grep 不支持 GNU grep 的 `-P`（Perl 正则表达式）选项，需安装 `textproc/gnugrep` 以获得 PCRE 支持。

## 关机与重启

`reboot`、`halt`、`poweroff` 在 FreeBSD 中是同一个程序的不同名称，行为不同；而在 Linux 中，这些命令可能是 systemd 的符号链接，行为也不同。

FreeBSD 的设计更接近传统 UNIX 的行为。

关机：

- 使用 `shutdown now` 将不会关机，而是切换到“单用户模式”，将提示：`Enter full pathname of shell or RETURN for /bin/sh :` 回车后进入单用户模式；
- 使用 `shutdown -h now` 将不会彻底断电，只会停止系统的运行，提示：`The operating system has halted. Please press any key to reboot.` 此处按任意键可重启系统；
- 正确的关机并断电命令是 `poweroff`，等同于命令 `shutdown -p now`。

重启：

- 重启命令和 Linux 一致，都是 `reboot`，但是参数不通用。
- 在 FreeBSD 下 `reboot` 等同于 `shutdown -r now`

>**技巧**
>
> 当使用上述命令关闭 FreeBSD 时，系统将调用 shell 脚本 `/etc/rc.shutdown`。该脚本按 *rc.d* 脚本列表的逆序依次执行，以关闭系统服务。（参见 FreeBSD Project. rc.shutdown[EB/OL]. (2026-04-09)[2026-04-09]. <https://github.com/freebsd/freebsd-src/blob/main/libexec/rc/rc.shutdown>）

> **注意**
>
> 在 FreeBSD 下，关机与重启操作都只有 root 用户和 operator 组成员可以执行。

## 附录：拼写自动纠正工具

### 安装与配置

FreeBSD 可使用 `sysutils/thefuck` 工具实现命令拼写自动纠正功能。该工具可自动检测并纠正命令输入错误。

使用 pkg 安装：

```sh
# pkg install thefuck
```

或使用 Ports 构建：

```sh
# cd /usr/ports/misc/thefuck/
# make install clean
```

### 配置 thefuck

查看安装后的配置信息

```sh
# fuck
Seems like fuck alias isn't configured!
More details - https://github.com/nvbn/thefuck#manual-installation
```

打开网页浏览。发现要将 `eval $(thefuck --alias)` 加入到 `~/.bash_profile`（bash shell）、`~/.bashrc`（bash shell）或 `~/.zshrc`（zsh shell）。

FreeBSD 默认使用的是 sh，因此将下行：

```sh
eval $(thefuck --alias)
```

在 FreeBSD 默认 sh 环境中，需将以下配置写入 `~/.shrc` 文件：

```sh
# . ~/.shrc
# fuck
No fucks given
```

> **技巧**
>
> 根据作者信息，若不喜欢输入 `fuck`，还可以使用其他别名：若更改为 `eval $(thefuck --alias abc)`，则下方所有 `fuck` 命令都会被换为 `abc`。
>
>```sh
> # abc
> Nothing found
> # plg install gimp
>-sh: plg: not found
> # abc
> pkg install gimp [enter/↑/↓/ctrl+c]
> ……省略一部分……
>```

### 使用示例

```sh
# ls-l /home/ykla/ # 先输入一遍错误的试试
-sh: ls-l: not found
# fuck
ls -l /home/ykla/ [enter/↑/↓/ctrl+c] # 上下箭头切换可能的命令，回车确认，Ctrl+C 中断
total 317
……省略一部分……
drwxr-xr-x  2 ykla ykla        2 Mar  9 20:45 下载
drwxr-xr-x  2 ykla ykla        2 Mar  9 20:45 桌面
```

再试试：

```sh
# plg install gimp
-sh: plg: not found
# fuck
pkg install gimp [enter/↑/↓/ctrl+c]
Updating FreeBSD repository catalogue...
FreeBSD repository is up to date.
……省略一部分……
```

## 参考文献

- FreeBSD Project. make -- maintain program groups[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=make&sektion=1>. BSD make 手册页，描述构建工具语法与用法。
- FreeBSD Project. grep -- file pattern searcher[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=grep&sektion=1>. 文本搜索工具手册页。
- FreeBSD Project. sed -- stream editor[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=sed&sektion=1>. 流编辑器手册页。

## 课后习题

1. 尝试进行对 BSD 风格的 sed/awk/grep 命令选项进行优化，使其兼容 GNU 语法。
2. 查看 FreeBSD 中 ls 命令的源代码实现，并与 GNU 的实现进行比较。
