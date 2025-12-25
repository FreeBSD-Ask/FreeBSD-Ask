# 4.3 虚拟控制台和终端

## 登录到 FreeBSD

当你安装 FreeBSD 后，若一切正常，你应该会在屏幕上看到以下内容：

```sh
FreeBSD/amd64 (ykla) (ttyv0)

login:
```

我们将这个屏幕上呈现的界面称为 TTY（teletypewriter，电传打字机），也称为物理终端。

解释：

- `FreeBSD` 是操作系统名称；
- `amd64` 是体系架构，一般英特尔和 AMD 处理器使用的都是 amd64，即 x86-64；
- `ykla` 是主机名，是在安装系统时你自己设置的；
- `ttyv0` 是指首个 TTY，你会发现计算机中许多事物的编号序列都是以 0 打头的；
- `login:` 指示用户登录。

我们输入用户名和密码，登录到系统：

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

>**注意**
>
>密码并不会被回显打印到屏幕上：一般情况下，我们输入密码时，屏幕上会显示 `******`。但在 FreeBSD 中，凡是涉及密码的地方大都不会有任何显示，即使输入了密码，屏幕上也仍然是空白的，与没有任何输入时的状态相同，直接输入后按回车即可。

- ①：root 是 UNIX 中的最高权限。我们常说的 Android root、苹果越狱、Kindle 越狱等，都是为了获取这一 root 权限。

### 参考文献

- [What is TTY in Linux?](https://itsfoss.com/what-is-tty-in-linux/)，翻译在 [Linux 黑话解释：TTY 是什么？](https://linuxstory.org/linux-blackmail-explained-what-is-tty/)。


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

如果读者连用户名都无从得知，建议找回 root 密码后，再查看系统中有哪些用户账户，或者直接重装系统会更方便。
