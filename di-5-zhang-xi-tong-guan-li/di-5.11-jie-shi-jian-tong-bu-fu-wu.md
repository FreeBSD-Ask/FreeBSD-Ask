# 5.11 时间同步服务

时间同步的准确性直接关系到系统安全与数据一致性。在分布式系统中，时间不一致可能导致认证失败、日志分析困难、数据库事务冲突等严重问题。

本节详细介绍 FreeBSD 系统的时区配置与网络时间协议（Network Time Protocol，NTP）时间同步服务的部署与管理。

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

RTC（Real-Time Clock，实时时钟）是计算机主板上的硬件时钟，用于在系统关机后保持时间。创建 `/etc/wall_cmos_clock` 文件可以兼容 Windows 时间，防止差 8 小时：

```sh
# touch /etc/wall_cmos_clock         # 创建当前时区信息文件，空文件
```

该文件存在则表示将机器的实时时钟视为本地时间（地方时），不存在则表示将实时时钟视为 UTC 时间。

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

- FreeBSD. adjkerntz -- adjust real-time clock (RTC) and kernel timezone offset[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?adjkerntz(8)>. 调整实时时钟 (RTC) 与内核时区偏移，该手册页详细说明了系统时区调整机制。

## 时间服务

时区设置完成后，需要配置和启用时间同步服务。网络时间协议（Network Time Protocol，NTP）是常用的时间同步协议，用于通过网络同步计算机系统时间。

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
# ntpd -q -p time.windows.com
```

| 选项 | 作用 |
| ---- | ---- |
| `-q` | 同步一次并退出 |
| `-p` | 指定 NTP 服务器 |

当时间相差较大时（超过 1000 秒）必须使用该命令，其他命令不会生效：

```sh
# ntpd -q -g -p pool.ntp.org
```

| 选项 | 作用 |
| ---- | ---- |
| `-g` | 允许大时间偏差修正 |

使用 pool.ntp.org 服务器更新系统时间。

## 课后习题

1. 对时间服务进行安全加固，使之适用于生产环境。总结并提交 PR 至本节。

2. 配置硬件 RTC 时钟。

3. 建立时间服务器。
