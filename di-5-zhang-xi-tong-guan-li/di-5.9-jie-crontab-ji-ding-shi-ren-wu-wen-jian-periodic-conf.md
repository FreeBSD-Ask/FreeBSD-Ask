# 5.9 crontab 及定时任务文件（periodic.conf）

## periodic.conf 的功能与目录结构

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

periodic.conf(5) 文件位于 `/etc/defaults` 目录下，其部分内容可被 `/etc` 目录下同名文件覆盖，而 `/etc` 下的文件又可被 `/etc/periodic.conf.local` 文件所覆盖。

源代码路径结构：

- 与 periodic 有关的源代码主要位于 [usr.sbin/periodic/](https://github.com/freebsd/freebsd-src/blob/main/usr.sbin/periodic)
- 与 cron 有关的源代码主要位于 [usr.sbin/cron](https://github.com/freebsd/freebsd-src/tree/main/usr.sbin/cron)。
- periodic 脚本的源代码位于 [usr.sbin/periodic/etc/](https://github.com/freebsd/freebsd-src/tree/main/usr.sbin/periodic/etc)。

## 附录：示例分析

以 `locate` 命令所依赖的路径数据库 `/var/db/locate.database` 文件为例，该数据库由 `/etc/periodic/weekly/310.locate` 脚本每周自动更新一次。

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

crontab: `cron` 配置，位于 `/etc/crontab`，可参阅 crontab(5))。

## 参考文献

- FreeBSD Project. periodic.conf(5)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=periodic.conf&sektion=5>. 定期任务配置文件手册页。
- FreeBSD Project. crontab(5)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=crontab&sektion=5>. cron 定时任务表手册页。

## 课后习题

1. 创建一个自定义 periodic 脚本放入 `/usr/local/etc/periodic/daily/`，配置 `periodic.conf` 使其运行，分析 periodic 脚本的命名规则与执行顺序机制。
2. 修改 `/etc/crontab` 文件中 periodic 任务的执行时间，对比修改前后系统日志中任务执行时间的变化。
3. 禁用某个默认的 periodic 任务（如 weekly 的 `310.locate`），观察其对 `locate` 命令数据库更新频率的影响。
