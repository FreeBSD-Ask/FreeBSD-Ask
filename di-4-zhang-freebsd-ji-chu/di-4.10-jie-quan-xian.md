# 4.10 权限

文件系统权限机制是类 UNIX 系统安全架构的基石。

在 FreeBSD 中，每个文件和目录都关联一组权限，有多种工具可用于查看和修改这些权限。

权限决定了用户能够访问哪些文件，以及能否修改或执行不属于自身的文件。

基本的 UNIX 权限使用三种访问类型分配：读、写和执行。这些访问类型用于确定文件所有者、组和其他人（其他所有人）的文件访问权限。

本节讨论的是 FreeBSD 中使用的传统 UNIX® 权限，不涉及细粒度的权限。

## 自主访问控制（DAC）模型

FreeBSD 采用的传统 UNIX 权限模型属于自主访问控制（Discretionary Access Control，DAC）范畴。DAC 的核心特征是：客体的所有者（owner）有权自主决定将访问权限授予其他主体，或撤销其他主体的访问权限。在 UNIX 系统中，文件的所有者可以自行修改文件的权限位，决定其他用户对该文件的访问能力。这种模型被称为“自主的”（discretionary），因为访问控制决策由客体所有者而非系统管理员集中做出。

DAC 模型的理论基础可追溯至 20 世纪 60—70 年代的多用户操作系统安全研究。美国国防部于 1985 年发布的《可信计算机系统评估准则》（Trusted Computer System Evaluation Criteria，TCSEC，又称“橘皮书”）将 DAC 定义为：一种基于主体身份和/或所属组来限制对客体访问的访问控制机制，客体的所有者可以自行指定或修改访问权限（来源：Department of Defense. DoD 5200.28-STD: Trusted Computer System Evaluation Criteria[S]. Washington, D.C.: Department of Defense, 1985.）。

传统 UNIX DAC 模型具有以下特征与局限：

- **粗粒度控制**：仅区分所有者、所属组和其他用户三类主体，无法对单个用户或多个组进行细粒度授权。
- **权限传播**：文件所有者可以将权限授予任意用户，包括将写权限授予非信任用户，这可能导致权限泄露。
- **超级用户绕过**：root 用户不受 DAC 约束，可以访问任何文件。这种设计在提供管理便利性的同时，也构成了潜在的安全风险，一旦 root 权限被非法获取，整个系统的安全防线将被突破。

为弥补传统 DAC 模型的不足，FreeBSD 提供了以下增强机制：

- **访问控制列表（ACL）**：基于 POSIX.1e 草案标准的 ACL 机制，允许对单个用户或组设置细粒度的访问权限，突破了传统 DAC 仅支持三类主体的限制。
- **强制访问控制（MAC）**：TrustedBSD MAC 框架提供了基于安全策略的强制访问控制能力，包括 Biba 完整性模型、MLS 多级安全模型等。与 DAC 不同，MAC 的访问控制决策由系统安全策略强制执行，客体所有者无法自行修改。
- **文件标志（File Flags）**：FreeBSD 支持通过 [chflags(1)](https://man.freebsd.org/cgi/man.cgi?query=chflags&sektion=1) 设置文件标志，如 `schg`（系统不可变标志）和 `sappnd`（系统仅追加标志），即使 root 用户也无法修改带有这些标志的文件（除非先移除标志）。文件标志增加了额外的安全和控制层级，即使 root 也可以被阻止删除或修改文件。
- **Capsicum 沙盒框架**：通过能力（capability）机制限制进程可访问的系统资源范围，实现最小权限原则。

## 权限表达式

首先，观察以下 `ls` 命令的输出示例，以理解权限表达式的构成：

```sh
# ls -al /home/ykla  # 显示 /home/ykla 目录下的详细文件列表
total 74
drwxr-xr-x  17 ykla ykla    27 Mar 19 17:57 .
drwxr-xr-x   3 root wheel    4 Mar 19 16:05 ..
drwx------   4 ykla ykla     4 Mar 10 16:21 .mozilla
-rw-r--r--   1 ykla ykla   966 Feb 24 12:18 .profile
-rw-------   1 ykla ykla   200 Mar 19 17:57 .sh_history
-rw-r--r--   1 ykla ykla  1003 Feb 24 12:18 .shrc
drwxr-xr-x   2 ykla ykla     2 Mar  9 23:48 .themes
drwxr-xr-x   2 ykla ykla     2 Mar  9 20:45 桌面
```

再观察：

```sh
----------   1 root wheel         0 Mar 19 22:26 test
```

FreeBSD 文件访问权限可以用 10 个标志位来表示（请读者核实第一列是否为 10 位），而这 10 个标志位由 4 个部分组成：

用斜杠分隔：`-/---/---/---`

```sh
- / --- / --- / ---
|   |     |     |
|   |     |     └─── 第四部分：其他用户权限（others）
|   |     └───────── 第三部分：同组用户权限（group）
|   └─────────────── 第二部分：所有者权限（owner）
└─────────────────── 第一部分：文件类型 / 设备类型
```

第一部分是第 1 位，用 `d` 表示目录，`-` 表示普通文件，`l` 表示符号链接文件，`b` 表示块设备文件，`p` 表示管道文件，`c` 表示字符设备文件，`s` 表示套接字文件。

第二部分是第 2、3、4 位，用于表示文件所属用户对文件的访问权限，用 `rwx` 表示读、写、执行权限（对于目录来说即访问权限，如 `ls`、`cd`），无权限则写成 `-`。

第三部分是第 5、6、7 位，用于标识文件所属组成员对文件的访问权限。

第四部分是第 8、9、10 位，用于标识其他用户对文件的访问权限。

读、写、执行权限除了用 `rwx` 表示外，也可分别对应数字 4、2、1，无权限即 0。每三位权限对应的数字相加后组合，即形成 3 位数字的表示方式（记忆口诀：“读 4 写 2 执行 1”）。

可能的数字与字母组合方式如下。

**UNIX® 权限**

| 值 | 权限说明 | 目录列表 |
| -- | -------- | -------- |
| 0 | 无读、无写、无执行权限 | `---` |
| 1 | 无读、无写、有执行权限 | `--x` |
| 2 | 无读、有写、无执行权限 | `-w-` |
| 3 | 无读、有写、有执行权限 | `-wx` |
| 4 | 有读、无写、无执行权限 | `r--` |
| 5 | 有读、无写、有执行权限 | `r-x` |
| 6 | 有读、有写、无执行权限 | `rw-` |
| 7 | 有读、有写、有执行权限 | `rwx` |

关于上面数字代表权限的代码可以在 [main/sys/sys/stat.h](https://github.com/freebsd/freebsd-src/blob/main/sys/sys/stat.h) 找到，由 IEEE Std 1003.1 规范定义：

```c
#define	S_IRWXU	0000700			/* 拥有者的读、写、执行（RWX）权限掩码 */
#define	S_IRUSR	0000400			/* 拥有者的读（Read）权限 */
#define	S_IWUSR	0000200			/* 拥有者的写（Write）权限 */
#define	S_IXUSR	0000100			/* 拥有者的执行（Execute）权限 */
```

系统控制设备权限的机制基于传统的 UNIX 哲学“一切皆文件”，即将大多数硬件设备视为文件，程序可对其进行打开、读写操作。这些特殊的设备文件存储在 `/dev/` 目录中。

典型的 `/dev/` 目录：

```sh
$ ls /dev
acpi		efi		mixer0		pci		ttyv6
apm		fd		mlx5ctl		pfil		ttyv7
apmctl		fido		nda0		psm0		ttyv8
atkbd0		full		nda0p1		pts		ttyv9
audit		geom.ctl	nda0p2		random		ttyva
auditpipe	gpt		nda0p3		reroot		ttyvb
bpf		hpet0		netdump		sndstat		ufssuspend
bpf0		input		netmap		stderr		ugen0.1
bpsm0		io		null		stdin		ugen0.2
cd0		iso9660		nvd0		stdout		ugen0.3
console		kbd0		nvd0p1		sysmouse	ugen1.1
consolectl	kbd1		nvd0p2		tcp_log		uinput
ctty		kbdmux0		nvd0p3		ttyv0		urandom
devctl		klog		nvme0		ttyv1		usb
devctl2		kmem		nvme0n1		ttyv2		usbctl
devstat		log		nvme0ns1	ttyv3		xpt0
dsp0		mdctl		pass0		ttyv4		zero
dumpdev		mem		pass1		ttyv5		zfs
```

> **思考题**
>
>>`drw-------`，即 `600`，这是一个目录，只有所属用户可以读、写。
>
> 这种说法正确吗，有意义吗，为什么？读者如何理解这种设计上的逻辑悖论？

目录也被视为文件进行相同的处理，同样具有读、写和执行权限。目录的可执行位与文件略有不同，当目录被设置为可执行时，表示可以使用 `cd` 命令切换进入该目录。

这也意味着要访问该目录中的文件，前提是文件本身的权限允许访问：

```sh
$ cd test/
cd: test/: Permission denied	# 提示权限不足
$ ls -ld test/	# 浏览目录权限
drw-------  2 ykla ykla 2 Apr 28 00:24 test/
```

如果要列出目录内容，该目录必须具有读权限。如果要删除已知名称的文件，则必须对该文件所在的目录同时具有写权限和执行权限。

此外还存在额外的权限位，主要用于特殊场景，例如 setuid 可执行文件和 sticky 目录。

## 符号权限

符号权限使用字符而非八进制值来为文件或目录分配权限，其语法为 `(对象)(操作)(权限)`，其中可用的值如下：

| 选项 | 字母 | 代表 |
| ---- | ---- | ---- |
| 对象 | u | 用户（User） |
| 对象 | g | 组所有者（Group owner） |
| 对象 | o | 其他（Other） |
| 对象 | a | 所有（ALL） |
| 操作 | + | 添加权限 |
| 操作 | - | 移除权限 |
| 操作 | = | 显式设置权限 |
| 权限 | r | 读（Read） |
| 权限 | w | 写（Write） |
| 权限 | x | 执行（Execute） |
| 权限 | t | 粘滞位（Sticky bit） |
| 权限 | s | 设置 UID 或 GID |

> **注意**
>
>chmod(1) 符号模式中的 `t`（sticky bit, 粘滞位）不在 POSIX.2 标准中。对“其他”权限（`o`）单独操作 `s`（设置 UID 或 GID）或 `t` 标志（粘滞位）时将被忽略。设置粘滞位应使用 `+t` 或 `a+t`，而非 `o+t`。

这些值与 chmod(1) 一起使用，但使用字母而非数字。例如，以下命令将阻止与 test 关联的组成员和所有其他用户访问 test：

```sh
% chmod go= test
```

~~这里的 go 并不是代表“前进”，而是“组所有者”和“其他”。并且等于号后面的空格是必要的。~~

当需要对文件进行多组更改时，可以提供逗号分隔的列表。例如，以下命令移除 test 的组和“world”写权限，并为所有用户添加执行权限：

```sh
% chmod go-w,a+x test
```

> **技巧**
>
>chmod(1) 符号模式中 `X` 权限仅在文件已是可执行或为目录时才设置执行位，常用于 `chmod =rw,+X` 保留已有执行权限。

### 操作符方式

赋予所有用户对 test.sh 脚本的执行权限：

```sh
$ chmod a+x test.sh
```

在 `a+x` 中：

- `a` 表示操作对象为所有用户。可选项还有：`u` 表示所属用户，`g` 表示所属组，`o` 表示其他用户，若省略则依照系统默认对象操作；
- `+` 是操作符，意为增加权限；可选项 `-` 则为移除权限；
- `rwx` 是权限模式。`r` 表示读、`w` 表示写、`x` 表示执行。可选项 `s` 表示在文件执行时将进程的属主或属组设置为文件的属主或属组。

### 数字方式

设置 `test.sh` 的权限为所有者可读写执行、组用户可读执行、其他用户无权限：

```sh
$ chmod 750 test.sh
```

其中：

- `7`：所属用户拥有读、写、执行的权限
- `5`：同组用户有读和执行的权限
- `0`：其他用户没有任何权限

此处，选项 `-R` 可递归修改权限。

示例：

```sh
# chmod -R 777 /tmp # 允许任何用户读、写、执行 /tmp 目录下所有文件
# chmod -R a+rwx /tmp # 允许任何用户读、写、执行 /tmp 目录下所有文件
```

## umask：文件创建掩码

在 UNIX 系统中，当进程调用 `open(2)`、`mkdir(2)` 等系统调用创建文件或目录时，内核使用文件创建掩码（umask）来确定最终权限。umask 是一个进程级属性，指定在文件创建时应被屏蔽（移除）的权限位。umask 机制确保新创建的文件不会意外地拥有过于宽松的权限。

事实上，权限数值是八进制，而非十进制。将八进制 755 转为二进制则为：111 101 101。具体计算过程：

```sh
7
= 4 + 2 + 1
= 1×2² + 1×2¹ + 1×2⁰
= 111₂

5
= 4 + 0 + 1
= 1×2² + 0×2¹ + 1×2⁰
= 101₂

5
= 4 + 0 + 1
= 1×2² + 0×2¹ + 1×2⁰
= 101₂

合并（最后数字 = Σ (数字 × 进制数^位置)，位置从 0 开始，从右到左，Σ 代表总和）：

111 101 101₂
```

> **技巧**
>
>一般来说，任何非零数的 0 次方都等于 1。

具体而言，新文件的初始权限由创建请求中的模式参数与 umask 取反后进行按位与运算得出：

```sh
最终权限 = 请求模式 & ~umask
```

> **技巧**
>
>按位与 `&`：
>
>| 位 1 | 位 2 | 结果 |
>| ---- | ---- | ---- |
>| 1 | 1 | 1 |
>| 1 | 0 | 0 |
>| 0 | 1 | 0 |
>| 0 | 0 | 0 |
>
>按位取反：
>
>```sh
>umask:   000 010 010   （022）
>~umask:  111 101 101   （755）
>```

例如，当进程请求以模式 `0666`（所有用户读写）创建文件，而当前 umask 为 `0022` 时：

```sh
  110 110 110   (0666)
& 111 101 101   (~0022)
--------------
  110 100 100
```

则最终权限为 `0666 & ~0022 = 0644`（所有者读写、组和其他用户只读）。

```sh
  111 111 111   (0777)
& 111 101 101   (~0022)
--------------
  111 101 101
```

对于目录，通常的请求模式为 `0777`，在 umask 为 `0022` 时结果为 `0755`。

FreeBSD 的默认 umask 为 `0022`，可通过 [umask(2)](https://man.freebsd.org/cgi/man.cgi?query=umask&sektion=2) 系统调用或 Shell 内建的 `umask` 命令查看和设置：

```sh
% umask      # 显示当前 umask（八进制）
0022
% umask -S   # 以符号方式显示
u=rwx,g=rx,o=rx
% umask 027  # 设置 umask 为 027（请勿在生产环境执行）
```

| umask 值 | 新文件权限（请求 0666） | 新目录权限（请求 0777） | 备注 |
| -------- | ----------------------- | ----------------------- | ---- |
| `0022` | `0644`（rw-r--r--） | `0755`（rwxr-xr-x） | 默认值 |
| `0027` | `0640`（rw-r-----） | `0750`（rwxr-x---） | 更严格，禁止其他用户访问 |
| `0077` | `0600`（rw-------） | `0700`（rwx------） | 最严格，仅所有者可访问 |

umask 在 Shell 启动文件（如 `~/.profile` 或 `~/.cshrc`）中设置。在 csh/tcsh 中使用 `umask 022`，在 sh/bash 中同样使用 `umask 022`。

> **注意**
>
> - umask 仅影响文件创建时的初始权限，不会修改已存在文件的权限。
> - 在 Jail 容器中，umask 继承自主机系统的进程环境，不受 Jail 配置的直接影响。

## `chown` 命令

[chown(8)](https://man.freebsd.org/cgi/man.cgi?query=chown&sektion=8) 命令用于修改文件的属主，包括所属用户和所属组。只有文件所有者或超级用户（root）才能修改文件的属主。

> **注意**
>
> 符号表示法：`用户:组` 同时修改属主和属组；`:组` 仅修改属组；`用户:` 修改属主并将属组设为指定用户的登录组。

示例：修改 `t.sh` 的属主为 `test1`。

```sh
# chown test1 t.sh
```

示例：修改 `t.sh` 的属主为用户 `test1`、组 `test`。

```sh
# chown test1:test t.sh
```

示例：修改 `/tmp` 目录下所有文件的属主为用户 `test1`、组 `test`。

```sh
# chown -R test1:test /tmp
```

此处，选项 `-R` 可递归修改属主。

## 特殊权限位：setuid、setgid 与 sticky bit

除基本的读、写、执行权限外，UNIX 系统还定义了三种特殊权限位，这些设置提供了通常不授予普通用户的功能。要理解这些权限位，必须注意实际用户 ID（real user ID）与有效用户 ID（effective user ID）之间的区别：实际用户 ID 是拥有或启动进程的 UID，而有效 UID 是进程运行时所采用的 UID。

### setuid（设置用户 ID）

当可执行文件设置了 setuid 位后，无论哪个用户执行该文件，进程的有效用户 ID（EUID）都将被设置为文件所有者的 UID，而非执行者的 UID。这一机制使得普通用户可以临时获得文件所有者的权限来执行特定操作。

setuid 位在权限表达式中以所有者执行位上的 `s` 表示（如 `-r-sr-xr-x`）。

setuid 最典型的应用场景是 `passwd(1)` 命令。

```sh
# ls -al /usr/bin/passwd
-r-sr-xr-x  1 root wheel 8368 Apr 13 12:38 /usr/bin/passwd
```

普通用户修改密码时需要更新 `/etc/master.passwd` 文件，而该文件只有 root 才有写权限。通过 setuid 机制，`passwd` 命令以 root 的 EUID 运行，从而获得修改密码文件的权限。`passwd(1)` 以普通用户的实际用户 ID 运行，但为了更新密码数据库，该命令以 root 用户的有效 ID 运行，使用户能够更改密码而不会遇到“Permission Denied”错误。

setuid 位数字表示法中在三位权限码前加 `4`（如 `4555`），使用命令显示完整权限（含类型和特殊位，八进制）：

```sh
# stat -f "%p" /usr/bin/passwd
104555
```

> **注意**
>
> setuid 机制是一把双刃剑。如果 setuid 程序存在安全漏洞，攻击者可能利用该程序以文件所有者（通常是 root）的权限执行任意代码。因此，系统管理员应尽量减少 setuid 程序的数量，并定期审计系统中的 setuid 文件。`nosuid` 挂载选项将导致此类二进制文件静默失败而不通知用户，但该选项并非完全可靠。

### setgid（设置组 ID）

setgid 的作用与 setuid 类似，但作用于组而非用户。当可执行文件设置了 setgid 位后，进程的有效组 ID（EGID）将被设置为文件所属组的 GID。当目录设置了 setgid 位后，在该目录中创建的新文件将继承目录的所属组，而非创建者的主组。

setgid 位在权限表达式中以所属组执行位上的 `s` 表示（如 `-r-xr-sr-x`）：

```sh
# stat -f "%Sp" /usr/libexec/dma
-r-xr-sr-x
```

数字表示法中在三位权限码前加 `2`（如 `2555`）:

```sh
# stat -f "%p" /usr/libexec/dma
102555
```

### sticky bit（粘滞位）

sticky bit 最初用于将可执行文件的代码段“粘滞”在交换空间中以提高重复启动速度，但在现代系统中这一用途已不再相关。当前，sticky bit 主要用于目录：当目录设置了 sticky bit 后，只有文件的所有者（或 root）才能删除或重命名该目录下的文件，即使其他用户对该目录拥有写权限。

sticky bit 最常见的应用场景是 `/tmp` 目录。该目录对所有用户开放写权限，但通过 sticky bit 防止用户删除他人的临时文件。当目录设置了 sticky bit 时，仅文件所有者可以删除该目录下的文件，这对于防止公共目录中非文件所有者删除文件非常有用。

sticky bit 在权限表达式中以其他用户执行位上的 `t` 表示（如 `drwxrwxrwt`）：

```sh
# ls -ald /tmp
drwxrwxrwt  6 root wheel 6 Apr 27 21:55 /tmp
```

数字表示法中在三位权限码前加 `1`（如 `1777`）:

```sh
# stat -f "%p" /tmp
41777
```

## FreeBSD 文件标志

除了文件权限外，FreeBSD 还支持使用“文件标志”。这些标志增加了额外的安全和控制层级，适用于文件和目录，通过文件标志甚至可以阻止 root 删除或修改文件。

常用标志如下：

| 标志 | 说明 | 备注 |
| ---- | ---- | ---- |
| `schg` / `schange` / `simmutable` | 系统不可变标志 | 仅超级用户可设置；在安全级别（securelevel）大于 0 时无法清除 |
| `sappnd` / `sappend` | 系统仅追加标志 | 仅超级用户可设置；同受安全级别限制 |
| `uchg` / `uchange` / `uimmutable` | 用户不可变标志 | 文件所有者或超级用户可设置；不受安全级别限制 |
| `uappnd` / `uappend` | 用户仅追加标志 | 文件所有者或超级用户可设置 |
| `nodump` | 不转储标志 | 文件所有者或超级用户可设置；dump(8) 将跳过此类文件 |
| `sunlnk` / `sunlink` | 系统不可删除标志 | 仅超级用户可设置 |
| `uunlnk` / `uunlink` | 用户不可删除标志 | 文件所有者或超级用户可设置 |

> **注意**
>
> - 标志前加 `no` 可清除该标志，如 `nouchg` 清除用户不可变标志。
> - 某些标志的修改能力取决于当前内核安全级别（securelevel），参见 security(7)。
> - 仅有限数量的工具支持 chflags 标志，包括 ls(1)、cp(1)、find(1)、install(1)、dump(8)、restore(8)；目前 pax(1) 不支持 chflags。

使用 chflags(1) 可修改文件标志。chflags(1) 首次出现于 4.4BSD，是 BSD 系统特有的功能，Linux 不原生支持（需通过 `chattr` 命令和 `lsattr` 命令实现类似功能）。查看文件的标志可使用 ls(1) 的 `-lo` 选项：

```sh
# ls -lo test
-rwx--x--x  1 ykla ykla uarch 0 Apr 16 12:44 test
```

> **注意**
>
>如果使用 ZFS 文件系统，所有文件都可能拥有归档标志 `uarch`，这是符合预期的。

例如，要在文件 `test` 上启用系统不可删除标志，执行以下命令：

```sh
# chflags sunlink test
```

执行后，查看文件：

```sh
# ls -lo test
-rwx--x--x  1 ykla ykla sunlnk,uarch 0 Apr 16 12:44 test
```

要禁用系统不可删除标志，在 sunlink 前面加上“no”：

```sh
# chflags nosunlink test
```

文件标志通常只能由 root 用户添加或移除：

```sh
$ ls -lo
-rwx--x--x  1 ykla ykla     0 Apr 16 12:44 test
$ chflags sunlink test
chflags: test: Operation not permitted
```

否则系统将返回操作不被允许的错误。

### 参考文献

- FreeBSD Forums. File flag defaults on ZFS[EB/OL]. (2020-09-22)[2026-04-27]. <https://forums.freebsd.org/threads/file-flag-defaults-on-zfs.77088/>.

## 课后习题

1. 查看 FreeBSD 内核中权限检查的核心源代码，尝试使其更加细粒度。
2. 修改一个系统目录（如 `/var/tmp`）的默认权限配置，记录修改后对该目录下文件创建和进程访问行为的影响。
