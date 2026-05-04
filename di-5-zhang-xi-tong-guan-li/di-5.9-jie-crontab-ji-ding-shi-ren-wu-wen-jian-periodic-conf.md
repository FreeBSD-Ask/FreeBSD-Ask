# 5.9 Cron 和 Periodic

## Cron 和 Periodic 的目录结构

periodic.conf(5) 文件包含了每日、每周和每月系统维护任务应如何运行的说明。`periodic` 是 FreeBSD 的系统维护任务框架，负责执行定期的系统维护工作，如日志轮转、安全检查等。这些任务通过 `periodic` 命令执行，由 `cron` 守护进程按预设时间表自动调用。

与 `periodic`、`cron` 有关的配置和路径如下：

```sh
/
├── etc/
│   ├── defaults/                   # 存放一些系统的默认配置文件
│   │   └── periodic.conf           # 默认配置文件，包含所有系统默认变量和值
│   ├── periodic.conf               # 系统特定的变量覆盖文件（常规覆盖，默认不存在）
│   ├── periodic.conf.local         # 额外覆盖文件，用于共享或分发场景（默认不存在）
│   └── periodic/                   # 基本系统的任务脚本目录
│       ├── daily/                  # 每日维护任务脚本
│       ├── weekly/                 # 每周维护任务脚本
│       ├── monthly/                # 每月维护任务脚本
│       └── security/               # 安全相关任务脚本
├── usr/
│   └── local/                      # 第三方软件安装目录
│       └── etc/
│           └── periodic/           # 第三方应用的任务脚本目录
│               ├── daily/          # 每日维护任务脚本
│               ├── weekly/         # 每周维护任务脚本
│               └── security/       # 安全相关任务脚本
└── var/
    └── cron/
        ├── allow                   # 允许使用 crontab 的用户列表（默认不存在）
        ├── deny                    # 禁止使用 crontab 的用户列表（默认不存在）
        └── tabs/                   # 个人 crontab 文件目录
```

periodic.conf(5) 文件位于 **/etc/defaults** 目录下，其部分内容可被 **/etc** 目录下同名文件覆盖，而 **/etc** 下的文件又可被 **/etc/periodic.conf.local** 文件所覆盖。

源代码路径结构：

- 与 periodic 有关的源代码主要位于 [usr.sbin/periodic/](https://github.com/freebsd/freebsd-src/blob/main/usr.sbin/periodic)
- 与 cron 有关的源代码主要位于 [usr.sbin/cron](https://github.com/freebsd/freebsd-src/tree/main/usr.sbin/cron)。
- periodic 脚本的源代码位于 [usr.sbin/periodic/etc/](https://github.com/freebsd/freebsd-src/tree/main/usr.sbin/periodic/etc)。

## Cron

工具 cron(8) 在后台运行，并定期检查 **/etc/crontab** 中的任务，并在 **/var/cron/tabs** 中查找自定义的 crontab 文件。

这些文件用于调度任务，cron 将在指定的时间执行这些任务。

每个 crontab 条目定义一个要执行的任务，称为 **cron 作业**。

使用两种不同类型的配置文件：

- 系统 crontab，不应修改；系统 crontab **/etc/crontab** 包含 `who` 列，这在用户 crontab 中不存在。在系统 crontab 中，cron 将以该列指定的用户身份运行命令。
- 用户 crontab，可以根据需要创建和编辑。在用户 crontab 中，所有命令都以创建该 crontab 的用户身份运行。用户 crontab 允许每个用户调度自己的任务。`root` 用户也可以拥有其用户 **crontab**，用于调度系统 **crontab** 中不存在的任务。

以下示例条目来自系统 crontab **/etc/crontab**：

```sh
# /etc/crontab - system crontab for FreeBSD # 以 `#` 字符开头的行是注释
#
#
SHELL=/bin/sh # ① = 等号字符用于定义环境设置
PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin
#
#minute	hour	mday	month	wday	who	command
#
# Save some entropy so that /dev/random can re-seed on boot.
*/11	*	*	*	*	operator /usr/libexec/save-entropy # ②③
#
# Rotate log files every hour, if necessary.
0	*	*	*	*	root	newsyslog
#
# Perform daily/weekly/monthly maintenance.
1	3	*	*	*	root	periodic daily
15	4	*	*	6	root	periodic weekly
30	5	1	*	*	root	periodic monthly
#
# Adjust the time zone if the CMOS clock keeps local time, as opposed to
# UTC time.  See adjkerntz(8) for details.
1,31	0-5	*	*	*	root	adjkerntz -a
```

- ① 在此示例中，它用于定义 `SHELL` 和 `PATH`。如果省略 `SHELL`，cron 将使用默认的 Bourne shell。如果省略 `PATH`，则必须提供命令或脚本的完整路径。
- ② 这一行定义了系统 crontab 中使用的七个字段：`minute`、`hour`、`mday`、`month`、`wday`、`who` 和 `command`。`minute` 字段是指定命令运行的分钟数，`hour` 是命令运行的小时数，`mday` 是日期，`month` 是月份，`wday` 是星期几。这些字段必须是数字值，表示 24 小时制，或者是 `*`，表示该字段的所有值。`who` 字段仅存在于系统 crontab 中，指定命令应该以哪个用户身份运行。最后一个字段是要执行的命令。
- ③ 这个条目定义了这个 cron 作业的值。`*/11` 后面跟着多个 `*` 字符，表示 `/usr/libexec/save-entropy` 将由 `operator` 在每小时中的第 11 分钟执行一次，每天、每周、每月都如此。命令可以包含多个选项。如果命令跨越多行，必须使用反斜杠 `\` 延续字符。

### 创建用户 Crontab

要创建用户 crontab，可以在编辑模式下调用 `crontab`：

```sh
$ crontab -e
```

这将使用默认文本编辑器打开用户的 crontab。用户第一次运行此命令时，会打开一个空文件。待用户创建了 crontab，此命令将打开该文件进行编辑。

将以下行添加到 crontab 文件顶部以设置环境变量，同时建议保留 crontab 字段说明注释以便参考：

```ini
SHELL=/bin/sh
PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin
# crontab 字段顺序
# 分钟 小时 日期 月份 星期 命令
```

为每个要运行的命令或脚本添加一行，指定运行命令的时间。此示例每天在下午两点运行指定的自定义 Bourne shell 脚本。由于 `PATH` 中未指定脚本的路径，因此给出脚本的完整路径：

```ini
0 14 * * * /home/ykla/bin/自定义脚本.sh
```

> **技巧**
>
> 在使用自定义脚本之前，请确保其可执行性，并在 cron 设置的有限环境变量下进行测试。为了复制将在上述 cron 条目中使用的环境，可以使用：
>
> ```sh
> $ env -i SHELL=/bin/sh PATH=/etc:/bin:/sbin:/usr/bin:/usr/sbin HOME=/home/user LOGNAME=user /home/user/bin/自定义脚本.sh
> ```
>
> 检查脚本在 cron 环境下是否正常运行尤其重要，特别是当脚本包含任何使用通配符删除文件的命令时。

编辑完 crontab 后，保存文件。crontab 将自动安装生效，cron 会读取 crontab 并在指定时间运行 cron 作业。要列出 crontab 中的 cron 作业，可以使用以下命令：

```sh
$ crontab -l
```

输出应类似于以下内容：

```sh
0 14 * * * /home/ykla/bin/自定义脚本.sh
```

要删除用户 crontab 中的所有 cron 作业：

```sh
$ crontab -r
```

输出应类似于以下内容：

```sh
remove crontab for ykla? y
```

## Periodic

FreeBSD 提供了一组系统管理脚本，用于检查各种子系统的状态，执行与安全相关的检查，轮换日志文件等。这些脚本按周期执行：每日、每周或每月。这些任务的管理由 periodic(8) 执行，其配置位于 periodic.conf(5) 中。周期性任务由系统 crontab 中的条目启动，如上所示。

periodic(8) 执行的脚本位于 **/etc/periodic/**（基本工具）和 **/usr/local/etc/periodic/**（第三方软件）中。

它们被组织在 4 个子目录中：**daily**、**weekly**、**monthly** 和 **security**。

### 启用或禁用周期性任务

FreeBSD 默认启用了某些脚本以定期运行。

如要启用 `daily_status_zfs_enable`，将以下内容添加到文件 **/etc/periodic.conf** 中：

```sh
daily_status_zfs_enable="YES"
```

要禁用默认启用的任务，只需将 `YES` 更改为 `NO`。

### 配置周期性任务的输出

在 **/etc/periodic.conf** 文件中，变量 `daily_output`、`weekly_output` 和 `monthly_output` 指定了脚本执行结果的发送位置。

默认情况下，周期性脚本的输出会发送到 root 用户的邮件，因此建议阅读 root 的邮件，或者将 root 的邮件别名为一个被监控的邮箱。

要将结果发送到其他邮件地址，可以在 **/etc/periodic.conf** 文件中添加以空格分隔的邮件地址：

```ini
daily_output="email1@example.com email2@example.com"
weekly_output="email1@example.com email2@example.com"
monthly_output="email1@example.com email2@example.com"
```

如果希望将周期性输出记录到日志文件，而不是通过邮件接收，可以将以下行添加到 **/etc/periodic.conf** 文件中。newsyslog(8) 将在适当的时间轮换这些文件：

```ini
daily_output=/var/log/daily.log
weekly_output=/var/log/weekly.log
monthly_output=/var/log/monthly.log
```

### 附录：`locate` 命令示例分析

以 `locate` 命令所依赖的路径数据库 **/var/db/locate.database** 文件为例，该数据库由 **/etc/periodic/weekly/310.locate** 脚本每周自动更新一次。

如需立即更新数据库，可直接执行该脚本：

```sh
# locate locate.database # 试图寻找 locate.database
locate: the locate database '/var/db/locate.database' does not exist.

To create a new database, please run the following command as root:

  /etc/periodic/weekly/310.locate
# /etc/periodic/weekly/310.locate  # 未找到数据库，按提示刷新

Rebuilding locate database:
# locate locate.database # 再次查找，已找到
/var/db/locate.database
```

## 参考文献

- FreeBSD Project. periodic.conf(5)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=periodic.conf&sektion=5>. 定期任务配置文件手册页。
- FreeBSD Project. crontab(5)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=crontab&sektion=5>. cron 定时任务表手册页。

## 课后习题

1. 创建一个自定义 periodic 脚本放入 **/usr/local/etc/periodic/daily/**，配置 `periodic.conf` 使其运行，分析 periodic 脚本的命名规则与执行顺序机制。
2. 修改 **/etc/crontab** 文件中 periodic 任务的执行时间，对比修改前后系统日志中任务执行时间的变化。
3. 禁用某个默认的 periodic 任务（如 weekly 的 `310.locate`），观察其对 `locate` 命令数据库更新频率的影响。
