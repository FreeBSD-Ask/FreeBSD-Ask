# 4.3 虚拟控制台和终端

## 登录到 FreeBSD

当 FreeBSD 系统安装完成并正常启动后，用户将在屏幕上看到以下系统提示符界面：

```sh
FreeBSD/amd64 (ykla) (ttyv0)

login:
```

这一屏幕界面在计算机技术史上被称为 TTY（teletypewriter，电传打字机），也可称为物理终端。TTY 作为用户与操作系统内核进行交互的早期接口形式，在图形用户界面（GUI）普及之前构成了主要的人机交互（HCI）手段，是计算机人机交互历史发展进程中的重要阶段。

解释：

- `FreeBSD` 是操作系统名称；
- `amd64` 是体系架构，一般英特尔和 AMD 处理器使用的都是 amd64，即 x86-64；
- `ykla` 是主机名，是在安装系统时用户自行设置的；
- `ttyv0` 是指首个 TTY，计算机中许多事物的编号序列都是以 0 打头的；
- `login:` 指示用户登录。

我们输入用户名和密码，登录系统：

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
```

祝贺你！你已经成功登录到 FreeBSD 操作系统。

> **注意**
>
> 密码并不会被回显打印到屏幕上。一般情况下，我们输入密码时，屏幕上会显示 `******`。但在 FreeBSD 中，凡是涉及密码的地方大都不会有任何显示，即使输入了密码，屏幕上也仍然是空白的，与没有任何输入时的状态相同，直接输入后按回车即可。

- ①：root 是 UNIX 系统中的超级用户账户，拥有最高权限。我们常说的 Android root、苹果越狱、Kindle 越狱等，都是为了获取这一 root 权限。

### 参考文献

- ItsFOSS. What is TTY in Linux?[EB/OL]. [2026-03-25]. <https://itsfoss.com/what-is-tty-in-linux/>. 详细介绍 TTY 概念与历史

### 故障排除与未竟事宜

- 若用户名正确，但密码不正确：
  
```sh
login: root
Password:
Login: incorrect # 表示登录信息不正确
login: 
```

- 若用户名和密码都不正确：

```sh
login: test # 当前系统中不存在该用户
Password:
Login: incorrect
login: 
```

如果读者连用户名都无从得知，建议找回 `root` 密码后，查看系统中有哪些用户账户，或者直接重装系统会更方便。

## 课后习题

1. 在 FreeBSD 中切换多个虚拟控制台（ttyv0-ttyv3），分别在不同控制台登录不同用户，使用 w 命令验证并记录结果。
2. 查找 FreeBSD 内核中 TTY 子系统的核心源码，使其具有现代操作系统应有的功能。
3. 修改 FreeBSD 中 motd（Message of the Day）的默认显示行为，验证其变化。
