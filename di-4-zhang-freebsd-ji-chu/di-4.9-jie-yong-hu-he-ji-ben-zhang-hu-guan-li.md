# 4.9 用户和基本账户管理

FreeBSD 系统的所有访问均通过账户实现，所有进程均由用户运行，因此用户与账户管理是系统安全的基础。

FreeBSD 提供了多种用户管理工具。`adduser` 命令以交互方式添加新用户，自动完成创建 passwd 条目、构建新用户主目录、从 `/usr/share/skel` 复制默认配置文件等操作。

adduser(8) 是一个 Bourne Shell 脚本，内部调用 pw(8) 完成实际的用户数据库操作。adduser(8) 是 FreeBSD 特有工具。

`pw` 命令是更底层的用户和组管理工具，支持非交互式批量操作，可直接修改系统用户数据库文件。

用户账户信息存储于 [master.passwd(5)](https://man.freebsd.org/cgi/man.cgi?query=master.passwd&sektion=5) 文件中，该文件包含用户名、加密密码、UID、GID、登录类、密码过期时间、账户过期时间、GECOS 信息、主目录和登录 Shell 等字段。

## 账户类型

要登录 FreeBSD，必须有一个账户。

以下直接通过密码文件 `/etc/master.passwd` 观察用户：

```ini
root:$6$huh5iMfeueumGM3B$ycd9HsGOzKfFq6hbWMxceNBRCLibbSj5Ofjv/ed6Kq60M2F.syaGaxfdfYMqB79DZzqyhQlIiRZ4.D9ST90Gv/:0:0::0:0:Charlie &:/root:/bin/sh
toor:*:0:0::0:0:Bourne-again Superuser:/root:
daemon:*:1:1::0:0:Owner of many system processes:/root:/usr/sbin/nologin
operator:*:2:5::0:0:System &:/:/usr/sbin/nologin

……省略一部分……

www:*:80:80::0:0:World Wide Web Owner:/nonexistent:/usr/sbin/nologin
ntpd:*:123:123::0:0:NTP Daemon:/var/db/ntp:/usr/sbin/nologin
nobody:*:65534:65534::0:0:Unprivileged user:/nonexistent:/usr/sbin/nologin
ykla:$6$SqMJXrv5aC6Wq.by$nmbZs078aHNBVyh9noLFouJsGHyFSvQIzH0W4zpdfXuPtGtt.FHgWfXDHVBa.g9P0eZ32UwfByzRKdVnTaO7W.:1001:1001::0:0:User &:/home/ykla:/bin/sh
```

可以看到系统中存在若干用户账户。

FreeBSD 中主要有三类账户：系统账户、普通用户账户，以及超级用户账户。

### 系统账户

系统账户用于运行 DNS、邮件和 Web 服务器等服务。使用系统账户的原因在于安全性：如果所有服务均以超级用户身份运行，其操作将不受限制。

系统账户由源代码中的 [main/etc/master.passwd](https://github.com/freebsd/freebsd-src/blob/main/etc/master.passwd) 文件定义，截至写作时共计 27 个。因此，`_dhcp`、`ntpd` 都属于系统账户。系统账户是具有受限权限的专用账户，通常用于运行系统服务和守护进程。

`nobody` 是通用的非特权系统账户，但使用 `nobody` 的服务越多，该用户关联的文件和进程就越多，该用户实际上就越具有特权。因此，最佳实践是为每个服务分配独立的系统账户，而非共用 `nobody`。

### 普通用户账户

普通用户账户分配给实际使用者，用于登录和使用系统。每个访问系统的人都应拥有唯一的用户账户，这使管理员能够追踪用户操作，并防止用户互相干扰彼此的设置。

`ykla` 是在安装系统时创建的普通用户账户。如果希望通过 `su` 命令切换为 `root` 用户，必须将该用户加入 `wheel` 用户组。此外，部分用户账户是 Port 自动创建的系统用户。

每个用户账户在 FreeBSD 系统上都关联着若干属性信息：

- **用户名**：在 `login:` 提示符处输入的名称，每个用户必须拥有唯一的用户名。`passwd(5)` 中记载了创建有效用户名的规则。建议使用八个或更少的全部小写字符作为用户名，以保持向后兼容性。
- **密码**：每个账户都有一个关联的密码。
- **用户 ID（UID）**：用于在 FreeBSD 系统中唯一标识用户的数字。建议使用小于 65535 的 UID，因为较高的值可能导致某些软件的兼容性问题。
- **组 ID（GID）**：用于唯一标识用户所属主组的数字。建议使用 65535 或更低的 GID。
- **登录类**：组机制的扩展，在为不同用户定制系统时提供额外的灵活性。
- **密码更改时间**：默认情况下密码不会过期，但可以按用户启用密码过期。
- **账户过期时间**：默认情况下 FreeBSD 不会使账户过期。
- **用户全名**：用户名唯一标识 FreeBSD 的账户，但不一定反映用户的真实姓名。
- **家目录**：用户登录时的起始目录。常见约定是将所有用户家目录放在 `/home/username` 或 `/usr/home/username` 下。
- **用户 Shell**：Shell 提供用户与系统交互的默认环境。

需要注意的是，虽然普通用户权限受限，但其运行的软件越多，系统暴露的攻击面也会增加，从而带来潜在的提权风险。用户本身的权限是固定的，不会因为运行进程增加而直接获得更多权限；然而，运行更多软件意味着存在更多可能被攻击者利用的漏洞入口，因此提权风险确实会随之增大。只有在程序存在漏洞或配置不当的情况下，攻击者才可能利用这些进程实现权限提升。

### 超级用户账户

超级用户账户，通常称为 root，用于无限制地管理系统。超级用户与普通用户账户不同，可以不受限制地操作，超级用户账户的误用可能导致灾难性的后果。普通用户账户无法因误操作而破坏操作系统，因此建议以普通用户账户登录，仅在命令需要额外特权时方切换为超级用户。

实际上，内核根据账户的 EUID（有效用户 ID）是否为 `0` 来判定某账户是否拥有 root 权限。参见：main/sys/kern/kern_priv.c[EB/OL]. [2026-03-26]. <https://github.com/freebsd/freebsd-src/blob/main/sys/kern/kern_priv.c> 中的 `if (suser_enabled(cred))` 代码块部分。

获取超级用户特权有多种方式。虽然可以直接以 root 登录，但这种做法极不推荐，推荐使用 `su(1)` 命令切换为超级用户。

## 账户管理

FreeBSD 提供了多种不同的命令来管理用户账户。

**管理用户账户的工具**

| 命令 | 概要 |
| ---- | ---- |
| [adduser(8)](https://man.freebsd.org/cgi/man.cgi?query=adduser&sektion=8&format=html) | 推荐用于添加新用户的命令行应用程序。 |
| [rmuser(8)](https://man.freebsd.org/cgi/man.cgi?query=rmuser&sektion=8&format=html) | 推荐用于删除用户的命令行应用程序。 |
| [chpass(1)](https://man.freebsd.org/cgi/man.cgi?query=chpass&sektion=1&format=html) | 用于更改用户数据库信息的灵活工具。 |
| [passwd(1)](https://man.freebsd.org/cgi/man.cgi?query=passwd&sektion=1&format=html) | 用于更改用户密码的命令行工具。 |
| [pw(8)](https://man.freebsd.org/cgi/man.cgi?query=pw&sektion=8&format=html) | 可修改用户账户所有方面的强大灵活工具。 |
| [bsdconfig(8)](https://man.freebsd.org/cgi/man.cgi?query=bsdconfig&sektion=8&format=html) | 带有账户管理支持的系统配置工具。 |

### adduser 创建用户

推荐使用的添加新用户的程序是脚本文件 [adduser(8)](https://man.freebsd.org/cgi/man.cgi?query=adduser&sektion=8&format=html)。添加新用户时，此程序会自动更新 `/etc/passwd` 和 `/etc/group`。

adduser 还会为新用户创建 home 目录，从 `/usr/share/skel` （源代码路径为 `share/skel`）复制默认配置文件。`adduser` 的源代码路径为 `usr.sbin/adduser/adduser.sh`。

[adduser(8)](https://man.freebsd.org/cgi/man.cgi?query=adduser&sektion=8&format=html) 是交互式的，会逐步引导创建新用户账户。如下所示，输入所需信息或按 **回车键** 接受方括号中的默认值。

在此示例中，用户被邀请加入 `wheel` 组，使其可以通过 [su(1)](https://man.freebsd.org/cgi/man.cgi?query=su&sektion=1&format=html) 成为超级用户。

完成后，该工具会提示是创建另一个用户还是退出。

示例：创建普通用户 `ykla`，并将其添加到 `video` 组：

```sh
# adduser -g video -s sh -w yes
# Username: ykla
```

示例：创建用户 test，并将其添加到 wheel 组，设置其默认 Shell 为 sh：

```sh
# adduser # 此工具必须由超级用户运行
Username: test # 用户名 ①
Full name:  # 全名，可留空
Uid (Leave empty for default): # UID 设置，可留空
Login group [test]: # 登录组
Login group is test. Invite test into other groups? []: wheel # 设置要加入的组，多个用空格隔开，可留空
Login class [default]: # 登录分类，可留空
Shell (sh csh tcsh git-shell bash rbash nologin) [sh]: sh  # 除非手动设置默认 shell，否则 shell 为 sh
Home directory [/home/test]: # 指定家目录
Home directory permissions (Leave empty for default): # 指定家目录权限
Enable ZFS encryption? (yes/no) [no]: # 是否使用 ZFS 加密
Use password-based authentication? [yes]:  # 是否使用密码
Use an empty password? (yes/no) [no]:   # 是否空密码
Use a random password? (yes/no) [no]:   # 是否随机密码
Enter password: # 输入密码
Enter password again: # 重复输入密码
Lock out the account after creation? [no]: # 锁定账户？
Username   : test
Password   : *****
Full Name  :
Uid        : 1002
ZFS dataset : zroot/home/test
Class      :
Groups     : test wheel
Home       : /home/test
Home Mode  :
Shell      : /bin/sh
Locked     : no
OK? (yes/no): yes # 检查是否有错误
adduser: INFO: Successfully created ZFS dataset (zroot/home/test).
adduser: INFO: Successfully added (test) to the user database.
Add another user? (yes/no): no # 还需要创建另一个账户吗？
Goodbye!
```

> **注意**
>
> 由于输入密码时不会打印在屏幕上也不会显示为掩码 `*`，请在创建用户账户时小心不要输错密码。

- ① 登录名命名有一些限制，参见 passwd(5)[EB/OL]. [2026-03-26]. <https://man.freebsd.org/cgi/man.cgi?query=passwd&sektion=5&format=html>。但请注意，登录名不支持八位编码字符集，例如不支持中文（即仅支持特定 ASCII 字符）。

只有 root 才能使用此命令，否则将报错如下：

```sh
$ adduser test
adduser: ERROR: you must be the super-user (uid 0) to use this utility.
```

提示只有 UID 0 的用户（通常是 root）才能调用 adduser 命令。

### rmuser 删除用户

`rmuser` 用于删除用户，与 `adduser` 命令一样，也是交互式的脚本。`rmuser` 源代码路径是 `usr.sbin/adduser/rmuser.sh`。

示例：删除用户 test1 test2。

```sh
# rmuser -y test1 test2 # 同时删除用户 test1 和 test2
Removing user (test1): mailspool home passwd.
Removing user (test2): home passwd.
```

参数 `-y` 用于跳过确认步骤。

### chpass 更改用户信息

所有用户都可以使用 [chpass(1)](https://man.freebsd.org/cgi/man.cgi?query=chpass&sektion=1&format=html) 更改其默认 shell 和账户的个人信息。chpass 源代码位于 `usr.bin/chpass`。

示例：普通用户使用 nvi 文本编辑器打开当前用户信息进行修改。

```sh
$ chpass ykla	# 修改 ykla 的账户信息数据库
#Changing user information for ykla.
Shell: /bin/sh	# 用户 Shell
Full Name: User &	# 用户全名
Office Location:	# 办公地点
Office Phone:	# 办公电话
Home Phone:	# 家庭电话
Other information:	# 其他信息
~
~
~
/etc/pw.ogzb33: unmodified: line 1
```

root 可以用此工具更改任意用户的额外账户信息。

```sh
# chpass ykla	# 修改 ykla 的账户信息数据库
#Changing user information for ykla.
Login: ykla	# 指定 ykla 
Password: $6$SqMJXrv5aC6Wq.by$nmbZs078aHNBVyh9noLFouJsGHyFSvQIzH0W4zpdfXuPtGtt.FHgWfXDHVBa
.g9P0eZ32UwfByzRKdVnTaO7W.	# 用户密码
Uid [#]: 1001
Gid [# or name]: 1001
Change [month day year]:	# 密码更改日期
Expire [month day year]:	# 账户过期日期
Class:	# 用户分级
Home directory: /home/ykla	# 用户家目录
Shell: /bin/sh
Full Name: User &
Office Location:
Office Phone:
Home Phone:
Other information:
~
~
~
/etc/pw.mDp9q3: unmodified: line 1
```

示例：修改用户 test1 的登录环境为 `/bin/sh`。

```sh
# chpass -s sh test1 # 
chpass: user information updated
```

常用参数：`-s`，用于修改登录 Shell。

> **技巧**
>
> [chfn(1)](https://man.freebsd.org/cgi/man.cgi?query=chfn&sektion=1&format=html) 与 [chsh(1)](https://man.freebsd.org/cgi/man.cgi?query=chsh&sektion=1&format=html) 是 [chpass(1)](https://man.freebsd.org/cgi/man.cgi?query=chpass&sektion=1&format=html) 的链接命令，[ypchpass(1)](https://man.freebsd.org/cgi/man.cgi?query=ypchpass&sektion=1&format=html)、[ypchfn(1)](https://man.freebsd.org/cgi/man.cgi?query=ypchfn&sektion=1&format=html) 和 [ypchsh(1)](https://man.freebsd.org/cgi/man.cgi?query=ypchsh&sektion=1&format=html) 也是。由于 NIS 支持是自动的，无需在命令前加 `yp`。这一点可以从源代码 `usr.bin/chpass/Makefile` 进行推断：
>
> ```makefile
>SYMLINKS=	chpass ${BINDIR}/chfn
>SYMLINKS+=	chpass ${BINDIR}/chsh
>.if ${MK_NIS} != "no"	# 如果系统启用了 NIS
>SYMLINKS+=	chpass ${BINDIR}/ypchfn
>SYMLINKS+=	chpass ${BINDIR}/ypchpass
>SYMLINKS+=	chpass ${BINDIR}/ypchsh
>.endif
>
>MLINKS=	chpass.1 chfn.1 chpass.1 chsh.1
>.if ${MK_NIS} != "no"
>MLINKS+= chpass.1 ypchpass.1 chpass.1 ypchfn.1 chpass.1 ypchsh.1
>.endif
> ```


### passwd 更改用户密码

修改用户密码，如不指定用户则默认为当前用户。普通用户只能修改自己的密码，否则将报错如下：

```sh
$ passwd test
passwd: permission denied
```

示例：使用 ykla 更改自己的密码。

```sh
$ passwd ykla
Changing local password for ykla
Old Password:	# 输入旧密码
New Password:	# 输入新密码
Retype New Password:	# 再次输入新密码
```

root 用户可以修改所有用户的密码，且无需旧密码。

示例：使用 root 更改用户 ykla 的密码。

```sh
# passwd ykla
Changing local password for ykla
New Password:	# 输入新密码
Retype New Password:	# 再次输入新密码
```

> **技巧**
>
> FreeBSD 的 `passwd` 选项与 Linux 不同，锁定/解锁账户请使用 `pw lock/unlock`。

## 组管理

组是用户的列表。组由其组名和 GID 标识。在 FreeBSD 中，内核使用进程的 UID 和其所属的组列表来确定进程可执行的操作范围。大多数情况下，用户或进程的 GID 通常指列表中的第一个组。

组名到 GID 的映射列在 `/etc/group` 中。`/etc/group` 是纯文本文件，有四个以冒号分隔的字段。

```sh
# cat /etc/group
wheel:*:0:root,ykla	# 
operator:*:5:root

……省略部分输出……

ykla:*:1001:
test:*:1002:
```

可以看到 `/etc/group` 的格式形如 `组名:加密后的密码:GID:成员列表`，通过英文冒号分隔。

超级用户可以使用文本编辑器修改 `/etc/group`，但不建议，因为可能会因编辑错误导致严重后果。建议使用 pw(8) 添加和编辑组。

在使用 `operator` 组时请务必小心，因为可能会授予意外的类似超级用户的访问权限，包括但不限于关机、重启和访问 `/dev` 中的所有项目。

在 FreeBSD 中，可以使用 `pw` 命令管理用户和组：它是系统用户和组文件的前端。[pw(8)](https://man.freebsd.org/cgi/man.cgi?query=pw&sektion=8&format=html) 提供了非常强大的命令行选项，适合用于 shell 脚本，但对于新用户来说可能比本节中的其他命令更复杂。

### 添加组

使用 pw(8) 添加组：

```sh
# pw groupadd ykla2
# pw groupshow ykla2
ykla2:*:1002:
```

在此示例中，1002 是 ykla2 的 GID。此时，ykla2 没有成员。

### 向组中添加用户

使用 pw(8) 将用户添加到组中。

示例：设置组 test5 的成员为 test1。

```sh
# pw groupmod test5 -M test1 # 原有成员会被删除！
```

示例：将用户 `ykla` 同时添加到 `ykla2` 和 `wheel` 组：

```sh
# pw usermod ykla -G ykla2,wheel
```

`-G` 组列表，逗号分隔。

验证如下：

```sh
# id ykla
uid=1001(ykla) gid=1001(ykla) groups=1001(ykla),0(wheel),1002(ykla2)
```

示例：将用户 `test` 添加到 `wheel` 组（`wheel` 组为系统默认组，无需创建）：

```sh
# pw groupmod wheel -m test
```

在这个例子中，传递给 `-m` 的参数是用户列表（逗号分隔），这些用户将被追加进组中，并不会替换已有用户。

### 删除组

示例：删除 `admin` 组：

```sh
# pw groupdel admin
```

### 删除组中的用户

示例：从 `admin` 组里移除用户 `ykla`：

```sh
# pw groupmod admin -d ykla
```

### 添加用户

`pw useradd` 命令用于新建用户。

示例：创建用户 test1。

```sh
# pw useradd test1 # uid 系统默认，test1 组，登录环境 /bin/sh，未创建主目录
```

示例：创建用户 test2。

```sh
# pw useradd test2 -u 1200 -m -d /tmp/test -g test2 -G wheel -s sh -c test2 # 创建用户 test2，uid 为 1200，创建主目录，主目录为 /tmp/test，主组为 test2，有 wheel 权限，登录环境 /bin/sh，全名 test2
```

### 修改用户信息

`pw usermod` 命令用于修改用户信息。

示例：

```sh
# pw usermod test1 -l test2 # 将用户 test1 重命名为 test2
```

选项 `-l` 修改用户名。

### 删除用户

`pw userdel` 命令用于删除用户。

示例：删除用户 test2 及其主目录。

```sh
# pw userdel -r test2
```

常用参数：`-r` 删除用户同时删除用户主目录及所有相关信息；若不使用该参数则信息保留，仅删除用户。若主目录为 ZFS 数据集且已清空，pw(8) 会自动销毁该数据集，但不会处理数据集内的子数据集和快照。

### 显示用户信息

`pw usershow` 命令用于显示用户信息。

示例：显示用户 test2 的详细信息。

```sh
# pw usershow test2
test2:$6$FkxPcs2y.Y8cxyuj$kVDoV1LC.IWKGlSitll3oLArF18aHQYID0JYE.TUuD0YFgba.c7MbGs3xLnmpCZyu1nVKHhNqW2X7a57qN0xg/:1201:1201::0:0:User &:/home/test2:/bin/sh
```

### 修改组信息

`pw groupmod` 命令用于修改组信息。

示例：修改 test 组的 gid 为 1300。

```sh
# pw groupmod test -g 1300
```

示例：将 test 组重命名为 test2。

```sh
# pw groupmod test -l test2
```

## 参考文献

- FreeBSD Project. pw(8)[EB/OL]. [2026-03-26]. <https://man.freebsd.org/cgi/man.cgi?pw>. man 页，介绍了用户和组管理命令。

## 课后习题

1. 修改 FreeBSD 源代码，使操作的用户名支持 UTF-8 编码。
2. 查看 FreeBSD 中 pw 命令的源代码实现，使其更加现代化。
