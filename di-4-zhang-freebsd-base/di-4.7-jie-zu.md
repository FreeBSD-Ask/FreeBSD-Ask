# 4.7 用户和基本账户管理

## 账户类型

要想访问 FreeBSD，你必须有一个账户，而且所有进程都是以不同账户的名义启动的。

Ports 中的 `sysutils/htop` 提供的 `htop` 命令能够清晰地显示这一点（注意“USER”）：

```sh
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

FreeBSD 中主要有三类账户：系统账户、用户账户，以及超级用户账户。

超级用户账户拥有系统中的最高权限，即 root 账户。

>**技巧**
>
>实际上是内核根据账户的 EUID（有效用户 ID）是否为 `0` 来判定其是否拥有 root 权限。参见 [main/sys/kern/kern_priv.c](https://github.com/freebsd/freebsd-src/blob/main/sys/kern/kern_priv.c) 中的 `if (suser_enabled(cred))` 代码块部分。

系统账户由源代码中的 [main/etc/master.passwd](https://github.com/freebsd/freebsd-src/blob/main/etc/master.passwd) 所定义，总共 27 个。故，`_dhcp`、`ntpd` 都属于系统账户。系统账户是具有受限权限的专用账户，通常用于运行系统服务和守护进程。

`ykla` 是笔者在安装系统时创建的普通用户账户。如果希望通过 `su` 命令切换为 `root` 用户，必须将该用户加入 `wheel` 用户组。而 `messagebus` 是 Port `devel/dbus` 自动创建的普通用户。

需要注意的是，虽然普通用户权限受限，但其运行的软件越多，系统暴露的攻击面也会增加，从而带来潜在的提权风险。这并不意味着账户“自动”变得更危险——用户的权限是固定的，不会因为运行进程增加而发生权限提升。相反，只有在程序存在漏洞或配置不当的情况下，攻击者才可能尝试利用这些进程实现权限提升。

## `adduser` 创建用户

- 创建一个普通用户（用户名为 `ykla`），并将其添加到 `video` 分组：

```sh
# adduser -g video -s sh -w yes
# Username: ykla
```

示例：创建一个名为 test 的用户，并将其添加到 wheel 组，设置其默认 shell 是 sh：

```sh
root@ykla:/ #  adduser
Username: test # 用户名 ①
Full name:  # 全名，可留空
Uid (Leave empty for default): # UID 设置，可留空
Login group [test]: # 登录组
Login group is test. Invite test into other groups? []: wheel # 设置要加入的组，多个用空格隔开，可留空
Login class [default]: # 登录分类，可留空
Shell (sh csh tcsh git-shell bash rbash nologin) [sh]: sh  # 除非手动设置默认 shell，否则 shell 为 sh
Home directory [/home/test]: #指定家目录
Home directory permissions (Leave empty for default): # 指定家目录权限
Enable ZFS encryption? (yes/no) [no]: # 是否使用 zfs 加密
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
OK? (yes/no): yes # 检查有错误否
adduser: INFO: Successfully created ZFS dataset (zroot/home/test).
adduser: INFO: Successfully added (test) to the user database.
Add another user? (yes/no): no # 还需要创建另一个账号吗？
Goodbye!
```

- ①：登录名命名有一些限制，参见 [passwd(5)](https://man.freebsd.org/cgi/man.cgi?query=passwd&sektion=5&format=html)。但是注意，不支持八位编码字符集，如不支持中文（即仅支持特定 ASCII 字符）。

## `rmuser` 删除用户与 `passwd` 密码修改

- `rmuser` 用于删除用户。与 `adduser` 命令一样，也是交互式的。

示例：

```sh
# rmuser -y test1 test2 # 同时删除用户 test1 和 test2
Removing user (test1): mailspool home passwd.
Removing user (test2): home passwd.

```

参数 `-y` 用于跳过确认步骤。

- `chpass` 命令，以 `vi` 编辑器方式打开并修改指定用户信息，如不指定用户则默认为当前用户。

>**技巧**
>
>`export EDITOR=/usr/bin/ee` 可将编辑器换成更简单的 `ee`。

常用参数：`-s`，用于修改登录 shell

示例：

```sh
# chpass -s sh test1 # 修改用户 test1 的登录环境为 /bin/sh
chpass: user information updated
# export EDITOR=/usr/bin/ee 
# chpass # 以 ee 方式打开当前用户信息进行修改
# passwd # 修改用户密码，如不指定用户则默认为当前用户。
```

root 用户可修改所有用户的密码。

## `pw` 命令

在 FreeBSD 中，可以用 `pw` 命令管理用户和组：

- 创建 `admin` 分组，并将用户 `ykla` 同时添加到 `admin` 和 `wheel` 分组：

```sh
# pw groupadd admin
# pw usermod ykla -G admin,wheel
```

验证一下：

```sh
# id ykla
uid=1001(ykla) gid=1001(ykla) groups=1001(ykla),0(wheel),1002(admin)
```

- 创建 `wheel` 组，只添加 `root` 用户：

```sh
# pw groupadd wheel
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

---

`admin` 和 `wheel` 权限的区别：

- `admin`，具有管理系统的权限（sudo 的默认配置如此），可以使用 `sudo` 命令。
- `wheel`，超级管理员权限（该名称来源于俚语 big wheel，即大人物）。


### `pw useradd` 命令

用于新建用户

示例：

```sh
# pw useradd test1 # 创建用户 test1，uid 系统默认，test1 组，登录环境 /bin/sh，未创建主目录
# pw groupadd test2 # 创建主组 test2
# pw useradd test2 -u 1200 -m -d /tmp/test -g test2 -G wheel -s sh -c test2 # 创建用户 test2，uid 为 1200，创建主目录，主目录为 /tmp/test，主组为 test2，有管理员权限（Wheel），登录环境 /bin/sh，全名 test2
# echo password | pw useradd test3 -h 0 # 创建用户 test3，同时设置密码为 password
```

### `pw usermod` 命令

用于修改用户信息，常用参数：

`-l`，为用户改名 其他参数参考 useradd 子命令。

示例：

```sh
# pw usermod test1 -l test2 # 把用户 test1 重命名为 test2
```

### `pw userdel` 命令

用于删除用户，常用参数：

`-r`，删除用户同时删除用户主目录及所有相关信息；若不使用该参数则信息保留，仅删除用户

示例：

```sh
# pw userdel test2 -r
```

### `pw usershow` 命令

用于显示用户信息，示例：

```sh
# pw usershow test2
test2:$6$FkxPcs2y.Y8cxyuj$kVDoV1LC.IWKGlSitll3oLArF18aHQYID0JYE.TUuD0YFgba.c7MbGs3xLnmpCZyu1nVKHhNqW2X7a57qN0xg/:1201:1201::0:0:User &:/home/test2:/bin/sh
```

### `pw usernext` 命令

可返回下一个可用的 UID 和 GID，示例：

```sh
# pw usernext
1202:1202
```

### `pw lock` 命令

锁定账号，锁定后账号无法登录使用，

示例：

```sh
# pw lock test2
```

### `pw unlock` 命令

解锁账号，解锁后账号可以正常使用，

示例：

```sh
# pw unlock test2
```

### `pw groupadd` 命令

用于新建组。

示例：

```sh
# pw groupadd test -g 1200 # 创建组 test。gid 为 1200；gid 与 uid 有所不同
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

### `pw groupshow` 命令

用于显示组信息，

示例：

```sh
# pw groupshow test5
test5:*:1202:test1
```

### `pw groupnext` 命令

可返回下一个可用的 `gid`，

示例：

```sh
# pw groupnext
1301
```

## 参考文献

- [FreeBSD 入门笔记](https://lvv.me/posts/2021/04/19_freebsd_101/)，作者 lvv.me
