# 4.9 用户和基本账户管理

用户账户管理是操作系统安全模型的核心组成部分。通过为不同用户分配适当的权限和资源访问范围，系统可以实现细粒度的访问控制和安全隔离。由于对 FreeBSD 系统的所有访问都是通过账户实现的，且所有进程都由用户运行，因此用户和账户管理至关重要。

FreeBSD 提供了多种用户管理工具。`adduser` 命令以交互方式添加新用户，自动完成创建 passwd 条目、构建新用户主目录、从 `/usr/share/skel` 复制默认配置文件等操作。

adduser(8) 是一个 Bourne shell 脚本，内部调用 pw(8) 完成实际的用户数据库操作。adduser(8) 是 FreeBSD 特有工具。

`pw` 命令是更底层的用户和组管理工具，支持非交互式批量操作，可直接修改系统用户数据库文件。

用户账户信息存储于 [master.passwd(5)](https://man.freebsd.org/cgi/man.cgi?query=master.passwd&sektion=5) 文件中，该文件包含用户名、加密密码、UID、GID、登录类、密码过期时间、账户过期时间、GECOS 信息、主目录和登录 Shell 等字段。

## 账户类型

要想登录 FreeBSD，必须有一个账户。

在 FreeBSD 中，所有进程都是以某个账户的名义启动的。`sysutils/htop` 能够直观地呈现这一点（注意 `△USER` 这列）：

```sh
$ htop
  PID△USER       PRI  NI  VIRT   RES S   CPU% MEM%   TIME+  Command
    1 root        20   0 12724  1324 S    0.0  0.0  0:00.08 /sbin/init
  216 root        20   0 36172  7308 S    0.0  0.1  0:00.77 ├─ /usr/local/bin/vmtoolsd -c /usr/local/share/vmware-tools/to
  400 root        48   0 14188  2684 S    0.0  0.0  0:00.00 ├─ dhclient: system.syslog
  403 root         4   0 14188  2760 S    0.0  0.0  0:00.00 ├─ dhclient: em0 [priv]
  481 _dhcp       20   0 14192  2808 S    0.0  0.0  0:00.01 ├─ dhclient: em0
  596 root        20   0 15444  4204 S    0.0  0.1  0:00.05 ├─ /sbin/devd
  800 root        20   0 13904  2792 S    0.0  0.0  0:00.02 ├─ /usr/sbin/syslogd -s
  867 messagebus  20   0 15188  4492 S    0.0  0.1  0:00.29 ├─ /usr/local/bin/dbus-daemon --system
  870 root        20   0 14120  2456 S    0.0  0.0  0:00.06 ├─ /usr/sbin/moused -p /dev/psm0 -t auto
  898 ntpd        20   0 24564  5848 S    0.0  0.1  0:00.06 ├─ /usr/sbin/ntpd -p /var/db/ntp/ntpd.pid -c /etc/ntp.conf -f
  944 root        68   0 23508  9560 S    0.0  0.1  0:00.00 ├─ sshd: /usr/sbin/sshd [listener] 0 of 10-100 startups
  947 root        20   0 13944  2576 S    0.0  0.0  0:00.02 ├─ /usr/sbin/cron -s
  952 root        20   0 56736 23700 S    0.0  0.3  0:00.04 ├─ /usr/local/bin/sddm
  980 root        20   0  257M  124M S    1.0  1.5  0:04.83 │  ├─ /usr/local/libexec/Xorg -nolisten tcp -background none -
  993 root        23   0 50208 27572 S    0.0  0.3  0:00.02 │  └─ /usr/local/libexec/sddm-helper --socket /tmp/sddm-auth-4
  994 ykla        68   0 19992  4620 S    0.0  0.1  0:00.01 │     └─ /usr/local/bin/ck-launch-session /usr/local/bin/start
 1005 ykla        68   0  128M 67736 S    0.0  0.8  0:00.13 │        └─ /usr/local/bin/startplasma-x11
 1010 ykla        68   0  128M 68184 S    0.0  0.8  0:00.25 │           └─ /usr/local/bin/plasma_session
 1017 ykla        20   0  773M  190M S    0.0  2.3  0:01.33 │              ├─ /usr/local/bin/kded6
 1018 ykla        20   0  676M  262M S    0.0  3.2  0:30.96 │              ├─ /usr/local/bin/kwin_x11
```

可以看到系统中存在 `ykla`、`root`、`_dhcp`、`messagebus`、`ntpd` 这几个用户账户。

FreeBSD 中主要有三类账户：系统账户、普通用户账户，以及超级用户账户。

### 系统账户

系统账户用于运行 DNS、邮件和 Web 服务器等服务。使用系统账户的原因在于安全性：如果所有服务都以超级用户身份运行，它们将不受限制地操作。

系统账户由源代码中的 [main/etc/master.passwd](https://github.com/freebsd/freebsd-src/blob/main/etc/master.passwd) 文件定义，写作时总计 27 个。因此，`_dhcp`、`ntpd` 都属于系统账户。系统账户是具有受限权限的专用账户，通常用于运行系统服务和守护进程。

`nobody` 是通用的非特权系统账户，但使用 `nobody` 的服务越多，该用户关联的文件和进程就越多，该用户实际上就越具有特权。因此，最佳实践是为每个服务分配独立的系统账户，而非共用 `nobody`。

### 普通用户账户

普通用户账户分配给真实的人，用于登录和使用系统。每个访问系统的人都应拥有唯一的用户账户。这使管理员能够了解谁在做什么，并防止用户互相干扰彼此的设置。

`ykla` 是在安装系统时创建的普通用户账户。如果希望通过 `su` 命令切换为 `root` 用户，必须将该用户加入 `wheel` 用户组。而 `messagebus` 是 Port `devel/dbus` 自动创建的系统用户。

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

超级用户账户，通常称为 root，用于无限制地管理系统。超级用户与普通用户账户不同，可以不受限制地操作，超级用户账户的误用可能导致灾难性的后果。普通用户账户无法因误操作而破坏操作系统，因此建议以用户账户登录，仅在命令需要额外特权时才成为超级用户。

实际上是内核根据账户的 EUID（有效用户 ID）是否为 `0` 来判定某账户是否拥有 root 权限。参见：main/sys/kern/kern_priv.c[EB/OL]. [2026-03-26]. <https://github.com/freebsd/freebsd-src/blob/main/sys/kern/kern_priv.c> 中的 `if (suser_enabled(cred))` 代码块部分。

获取超级用户特权有多种方式。虽然可以直接以 root 登录，但这种做法极不推荐。推荐使用 `su(1)` 命令切换为超级用户。

## 组管理

组是用户的列表。组由其组名和 GID 标识。在 FreeBSD 中，内核使用进程的 UID 和它所属的组列表来确定进程被允许做什么。大多数情况下，用户或进程的 GID 通常指列表中的第一个组。

组名到 GID 的映射列在 `/etc/group` 中。这是一个纯文本文件，有四个以冒号分隔的字段。第一个字段是组名，第二个是加密密码，第三个是 GID，第四个是以逗号分隔的成员列表。有关语法的完整描述，请参阅 group(5)。

超级用户可以使用文本编辑器修改 `/etc/group`，但首选使用 vigr(8) 编辑组文件，因为它可以捕获一些常见错误。或者，可以使用 pw(8) 添加和编辑组。

使用 `operator` 组时必须小心，因为可能会授予意外的类似超级用户的访问权限，包括但不限于关机、重启和访问 `/dev` 中的所有项目。

### 添加组

使用 pw(8) 添加组：

```sh
# pw groupadd ykla2
# pw groupshow ykla2
ykla2:*:1002:
```

在此示例中，1100 是 ykla2 的 GID。此时，ykla2 没有成员。

### 向组中添加用户

使用 pw(8) 将用户添加到组中：

```sh
# pw groupmod ykla2 -M ykla
# pw groupshow ykla2
ykla2:*:1002:ykla
```

`-M` 的参数是要添加到新（空）组或替换现有组成员的以逗号分隔的用户列表。对用户而言，此组成员身份与密码文件中列出的用户主组不同且是额外的。这意味着当使用 pw(8) 的 groupshow 时，用户不会显示为成员，但当通过 id(1) 或类似工具查询信息时会显示。当 pw(8) 用于将用户添加到组时，它仅操作 `/etc/group`，不会尝试从 `/etc/passwd` 读取额外数据。

向现有组追加新成员：

```sh
# pw groupmod ykla2 -m root
# pw groupshow root
ykla2:*:1002:ykla,root
```

在此示例中，`-m` 的参数是要添加到组中的以逗号分隔的用户列表。与上一个示例不同，这些用户被追加到组中，不会替换组中的现有用户。

使用 id(1) 确定组成员身份：

```sh
% id ykla
uid=1001(ykla) gid=1001(ykla) groups=1001(ykla),0(wheel),1002(ykla2)
```

在此示例中，ykla 是组 ykla、wheel 和 ykla2 的成员。

有关此命令和 `/etc/group` 格式的更多信息，请参阅 pw(8) 和 group(5)。

## `adduser` 创建用户

- 创建一个普通用户（用户名为 `ykla`），并将其添加到 `video` 组：

```sh
# adduser -g video -s sh -w yes
# Username: ykla
```

示例：创建一个名为 test 的用户，并将其添加到 wheel 组，设置其默认 shell 为 sh：

```sh
# adduser
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
Lock out the account after creation? [no]: # 锁定账号？
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
Add another user? (yes/no): no # 还需要创建另一个账号吗？
Goodbye!
```

- ① 登录名命名有一些限制，参见 passwd(5)[EB/OL]. [2026-03-26]. <https://man.freebsd.org/cgi/man.cgi?query=passwd&sektion=5&format=html>。但请注意，登录名不支持八位编码字符集，例如不支持中文（即仅支持特定 ASCII 字符）。

## `rmuser` 删除用户与 `passwd` 修改密码

- `rmuser` 用于删除用户。与 `adduser` 命令一样，也是交互式的。

示例：

```sh
# rmuser -y test1 test2 # 同时删除用户 test1 和 test2
Removing user (test1): mailspool home passwd.
Removing user (test2): home passwd.
```

参数 `-y` 用于跳过确认步骤。

删除用户时，若主目录为 ZFS 数据集且已清空，pw(8) 会自动销毁该数据集，但不处理数据集内的子数据集和快照。

- `chpass` 命令以 `vi` 编辑器方式打开并修改指定用户信息，如不指定用户则默认为当前用户。

> **技巧**
>
> `export EDITOR=/usr/bin/ee` 可将编辑器改为更简单的 `ee`。

常用参数：`-s`，用于修改登录 shell

示例：

```sh
# chpass -s sh test1 # 修改用户 test1 的登录环境为 /bin/sh
chpass: user information updated
# export EDITOR=/usr/bin/ee  # 将编辑器改为更简单的 `ee` 编辑器
# chpass # 使用 ee 编辑器打开当前用户信息进行修改
# passwd # 修改用户密码，如不指定用户则默认为当前用户。
```

root 用户可以修改所有用户的密码。FreeBSD 的 `passwd` 选项与 Linux 不同。FreeBSD 没有 `-u`（解锁）、`-e`（过期）、`-d`（删除密码）等选项。锁定/解锁账户请使用 `pw lock/unlock`。

## `pw` 命令

在 FreeBSD 中，可以使用 `pw` 命令管理用户和组：

- 创建 `admin` 组，并将用户 `ykla` 同时添加到 `admin` 和 `wheel` 组：

```sh
# pw groupadd admin
# pw usermod ykla -G admin,wheel
```

验证如下：

```sh
# id ykla
uid=1001(ykla) gid=1001(ykla) groups=1001(ykla),0(wheel),1002(admin)
```

- 将用户 `root` 添加到 `wheel` 组（`wheel` 组为系统默认组，无需创建）：

```sh
# pw groupmod wheel -m root
```

- 从 `admin` 组里移除用户 `ykla`：

```sh
# pw groupmod admin -d ykla
```

- 删除 `admin` 组：

```sh
# pw groupdel admin
```

### `pw useradd` 命令

用于新建用户。

示例：

```sh
# pw useradd test1 # 创建用户 test1，uid 系统默认，test1 组，登录环境 /bin/sh，未创建主目录
# pw groupadd test2 # 创建主组 test2
# pw useradd test2 -u 1200 -m -d /tmp/test -g test2 -G wheel -s sh -c test2 # 创建用户 test2，uid 为 1200，创建主目录，主目录为 /tmp/test，主组为 test2，有管理员权限（Wheel），登录环境 /bin/sh，全名 test2
# echo password | pw useradd test3 -h 0 # 创建用户 test3，同时设置密码为 password
```

### `pw usermod` 命令

用于修改用户信息，常用参数：

`-l`，为用户改名；其他参数参考 `useradd` 子命令。

示例：

```sh
# pw usermod test1 -l test2 # 将用户 test1 重命名为 test2
```

### `pw userdel` 命令

用于删除用户，常用参数：

`-r`，删除用户同时删除用户主目录及所有相关信息；若不使用该参数则信息保留，仅删除用户。

示例：删除用户 test2 及其主目录。

```sh
# pw userdel -r test2
```

### `pw usershow` 命令

用于显示用户信息，示例：

```sh
# pw usershow test2  # 显示用户 test2 的详细信息
test2:$6$FkxPcs2y.Y8cxyuj$kVDoV1LC.IWKGlSitll3oLArF18aHQYID0JYE.TUuD0YFgba.c7MbGs3xLnmpCZyu1nVKHhNqW2X7a57qN0xg/:1201:1201::0:0:User &:/home/test2:/bin/sh
```

### `pw groupadd` 命令

用于新建组。

示例：

```sh
# pw groupadd test -g 1200 # 创建组 test。gid 为 1200；gid 与 uid 不同
# pw groupadd test5 -M test1,test2 # 创建组 test5。成员有 test1 和 test2
```

### `pw groupmod` 命令

用于修改组信息，常用参数：

`-g`，指定新的 `gid`

`-l`，重命名组名

`-M`，替换现有组成员列表，多个用逗号隔开

`-m`，为现有组成员列表增加新的成员

其他参数参考 `groupadd` 命令。

示例：

```sh
# pw groupmod test -g 1300 # 修改 test 组的 gid 为 1300
# pw groupmod test -l test2 # test 组重命名为 test2
# pw groupmod test5 -M test1 # 设置组 test5 的成员为 test1，原有成员会被删除！
# pw groupmod test5 -m test3 # 为组 test5 新增成员 test3
```

### `pw groupdel` 命令

用于删除组。

示例：

```sh
# pw groupdel test5
```


## 参考文献

- FreeBSD Project. pw(8)[EB/OL]. [2026-03-26]. <https://man.freebsd.org/cgi/man.cgi?pw>. man 页，介绍了用户和组管理命令。

## 课后习题

1. 修改 FreeBSD 源代码，使操作的用户名支持 UTF-8 编码。
2. 查看 FreeBSD 中 pw 命令的源代码实现，使其更加现代化。
