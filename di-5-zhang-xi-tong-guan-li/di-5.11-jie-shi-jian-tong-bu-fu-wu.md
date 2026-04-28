# 5.11 时间同步服务

时间同步的准确性直接关系到系统安全与数据一致性。在分布式系统中，时间不一致可能导致认证失败、日志分析困难、数据库事务冲突等严重问题。

本节详细介绍 FreeBSD 系统的时区配置与网络时间协议（Network Time Protocol，NTP）时间同步服务的部署与管理。NTP 协议由 David Mills 于 1985 年提出（RFC 958），现行标准为 NTPv4（RFC 5905）。FreeBSD 基本系统内置 ntpd(8) 服务，同时也可通过 Ports 安装 chrony 等替代实现。

## 调整时区

时间同步首先需正确设置系统时区。

### 全局时区设置

设置系统时区有两种方式：一是通过图形化工具，二是通过命令行。

- 使用 `bsdconfig` 工具设置时区
- 使用命令行设置系统时区为上海时间：

```sh
# cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

### 时间服务文件结构

```sh
/
├── usr
│   └── share
│       └── zoneinfo
│           └── Asia
│               └── Shanghai           # 上海时区文件
└── etc
    ├── localtime                     # 系统本地时间文件
    ├── wall_cmos_clock               # RTC 时钟设置标记
    └── ntp.conf                       # NTP 服务配置文件
```

### 用户级时区

除了全局时区设置，每个用户也可以单独设置时区。在用户的 shell 配置文件中设置 `TZ` 变量即可。

#### 对于 sh、bash、zsh

```sh
export TZ=CST-8             # 设置时区为中国标准时间（CST-8）
# 或
export TZ=Asia/Shanghai      # 设置时区为上海
```

#### 对于 csh

```sh
setenv TZ CST-8             # 在 shell 环境中设置时区为中国标准时间（CST-8）
# 或
setenv TZ "Asia/Shanghai"   # 在 shell 环境中设置时区为上海
```

### 定时计划

在 crontab 配置文件中，设置 `CRON_TZ` 变量即可。

在每天 08:00（CST-8 时区）执行 `date` 命令并将输出追加到 `~/date.log` 文件：

```sh
CRON_TZ=CST-8
0 8 * * * date >> ~/date.log
```

### 将 RTC 时间视为地方时

RTC（Real-Time Clock，实时时钟）是计算机主板上的硬件时钟，用于在系统关机后保持时间。

`adjkerntz` 用于维护内核时钟（始终为 UTC）与实时时钟（可能为本地时间）之间的正确关系，并在时区变更时更新内核时区偏移量。

`/etc/wall_cmos_clock` 文件存在则表示将机器的实时时钟视为本地时间（地方时），不存在则表示将实时时钟视为 UTC 时间。

创建 `/etc/wall_cmos_clock` 文件可以兼容 Windows 时间，防止时间相差 8 小时：

```sh
# touch /etc/wall_cmos_clock # 创建当前时区信息文件，空文件
```

重启系统使该设置生效：

```sh
# reboot
```

查看当前 CMOS 时钟设置：

```sh
# sysctl machdep.wall_cmos_clock
machdep.wall_cmos_clock: 1
```

#### 参考文献

- FreeBSD Project. adjkerntz(8)[EB/OL]. [2026-04-24]. <https://man.freebsd.org/cgi/man.cgi?query=adjkerntz&sektion=8>.

## 时间服务

时区设置完成后，需要配置和启用时间同步服务。网络时间协议（Network Time Protocol，NTP）是常用的时间同步协议，用于通过网络同步计算机系统时间。

FreeBSD 与 Linux 时间服务比较：

| 特性 | FreeBSD | Linux |
| ---- | ------- | ----- |
| 默认 NTP 客户端 | NTP Classic（ISC ntpd 分支） | chrony 或 systemd-timesyncd |
| NTS（Network Time Security） 支持 | 不支持，需安装 Port `net/chrony` | 支持（chrony 或 systemd-timesyncd） |
| 启动时同步 | 通过 rc.conf 变量 `ntpd_sync_on_start` 控制 | chrony 默认在启动时同步 |
| 内核时钟调整 | 使用 sysctl `kern.ntp` | 使用系统调用 `adjtimex()` |

### 设置并启动 NTP 服务

设置 NTP 服务在系统启动时自动启动：

```sh
# service ntpd enable
```

### 设置 NTP 服务启动时同步

设置 NTP 服务在启动时自动同步时间：

```sh
# sysrc ntpd_sync_on_start="YES"
```

编辑 `/etc/ntp.conf` 文件，添加附加时钟服务器：

```ini
server time.windows.com        # 配置 Windows 时间服务器
server 0.cn.pool.ntp.org       # 配置中国 NTP 池服务器 0
server 1.cn.pool.ntp.org       # 配置中国 NTP 池服务器 1
server 2.cn.pool.ntp.org       # 配置中国 NTP 池服务器 2
server 3.cn.pool.ntp.org       # 配置中国 NTP 池服务器 3
```

### NTP 服务

- 启动 NTP 服务

```sh
# service ntpd start
```

- 重启 NTP 服务

```sh
# service ntpd restart
```

### 时间信息查看

显示当前系统日期和时间：

```sh
$ date
2025年 3月22日 星期六 15时27分29秒 CST
```

### 手动时间同步

ntpd 是 FreeBSD 系统的默认 NTP 守护进程，用于持续同步系统时间。

使用 Windows 时间服务器同步系统：

```sh
# ntpd -q time.windows.com
```

| 选项 | 作用 |
| ---- | ---- |
| `-q` | 同步一次并退出 |

当系统时间与 NTP 服务器偏差超过 1000 秒时，ntpd 默认拒绝修正并退出，必须使用 `-g` 选项强制修正：

```sh
# ntpd -q -g pool.ntp.org
```

| 选项 | 作用 |
| ---- | ---- |
| `-g` | 允许大时间偏差修正 |

使用 pool.ntp.org 服务器更新系统时间。

## 课后习题

1. 对时间服务进行安全加固，使之适用于生产环境。总结并提交 PR 至本节。

2. 配置硬件 RTC 时钟。

3. 建立时间服务器。
