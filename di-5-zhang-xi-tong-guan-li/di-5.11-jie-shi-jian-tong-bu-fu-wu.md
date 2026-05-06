# 5.11 时间同步服务

NTP 协议由 David Mills 于 1985 年提出（RFC 958），现行标准为 NTPv4（RFC 5905）。

在 FreeBSD 中，可以使用内置的 ntpd 来同步系统时钟。同时也可通过 Ports 安装 chrony 等替代实现。

## 时区

时间同步首先需正确设置系统时区。

### 全局时区

设置系统时区有两种方式：

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

除了全局时区设置，每个用户也可以单独设置时区。在用户的 Shell 配置文件中设置 `TZ` 变量即可。

#### 对于 sh、Bash、Zsh

```sh
export TZ=CST-8             # 设置时区为中国标准时间（CST-8）
# 或
export TZ=Asia/Shanghai      # 设置时区为上海
```

#### 对于 csh

```sh
setenv TZ CST-8             # 在 Shell 环境中设置时区为中国标准时间（CST-8）
# 或
setenv TZ "Asia/Shanghai"   # 在 Shell 环境中设置时区为上海
```

### Cron 任务中的时区

在 crontab 配置文件中，设置 `CRON_TZ` 变量即可。

在每天 08:00（CST-8 时区）执行 `date` 命令并将输出追加到 **~/date.log** 文件：

```sh
CRON_TZ=CST-8
0 8 * * * date >> ~/date.log
```

### 将 RTC 时间视为地方时

RTC（Real-Time Clock，实时时钟）是计算机主板上的硬件时钟，用于在系统关机后保持时间。

`adjkerntz` 用于维护内核时钟（始终为 UTC）与实时时钟（可能为本地时间）之间的正确关系，并在时区变更时更新内核时区偏移量。

**/etc/wall_cmos_clock** 文件存在则表示将机器的实时时钟视为本地时间（地方时），不存在则表示将实时时钟视为 UTC 时间。

创建 **/etc/wall_cmos_clock** 文件可以兼容 Windows 时间，防止时间相差 8 小时：

```sh
# touch /etc/wall_cmos_clock # 创建当前时区信息文件，空文件
```

重启系统使该设置生效。

查看当前 CMOS 时钟设置：

```sh
# sysctl machdep.wall_cmos_clock
machdep.wall_cmos_clock: 1
```

## NTP 时间服务

时区设置完成后，需要配置和启用时间同步服务。

ntpd 与其网络对等方通过 UDP 数据包进行通信。在计算机与 NTP 对等方之间的任何防火墙必须配置为允许端口 123 上的 UDP 数据包进出。

>**注意**
>
>一些互联网接入提供商和网络设备会阻止较低编号的端口通信，从而导致 NTP 无法正常工作，因为回复无法到达机器。

### 设置 NTP 服务启动时同步

ntpd 读取 **/etc/ntp.conf** 文件来确定要查询的 NTP 服务器。建议选择多个 NTP 服务器，以防其中一个服务器无法访问或其时钟不可靠。ntpd 会根据接收到的响应，优先选择可靠的服务器，而将不可靠的服务器排除。

查询的 `server` 可以是本地网络中的服务器，ISP 提供的服务器，或者从 [公开可访问的 NTP 服务器列表](https://support.ntp.org/Servers/WebHome) 中选择。选择公共 NTP 服务器时，应选择一个地理位置接近的服务器，并查看其使用政策。此外，FreeBSD 提供了一个自身维护的服务器池，`0.freebsd.pool.ntp.org`。

关键字 `pool` 配置从服务器池中选择一个或多个服务器。可以参考 [公开的 NTP 服务器池列表]（https://support.ntp.org/Servers/NTPPoolServers），按地理区域组织。

编辑 **/etc/ntp.conf** 文件，添加附加时钟服务器：

```ini
# 禁止 ntpq 控制/查询访问。仅允许根据此文件中的 pool 和 server 语句添加对等方。
restrict default limited kod nomodify notrap noquery nopeer
restrict source  limited kod nomodify notrap noquery

# 允许来自本地主机的查询和控制访问。
restrict 127.0.0.1
restrict ::1

# 添加特定的服务器。
server time.windows.com iburst        # 配置 Windows 时间服务器
server 0.cn.pool.ntp.org iburst       # 配置中国 NTP 池服务器 0
server 1.cn.pool.ntp.org iburst       # 配置中国 NTP 池服务器 1
server 2.cn.pool.ntp.org iburst       # 配置中国 NTP 池服务器 2
server 3.cn.pool.ntp.org iburst       # 配置中国 NTP 池服务器 3

# 添加 FreeBSD 池服务器，直到有 3 到 6 个有效的服务器。
tos minclock 3 maxclock 6
pool 0.freebsd.pool.ntp.org iburst

# 使用本地的闰秒文件。
leapfile "/var/db/ntpd.leap-seconds.list"
```

以下是对示例中使用的关键字的简要概述。

默认情况下，NTP 服务器对任何网络主机都可访问。

关键字 `restrict` 控制哪些系统可以访问服务器。可以有多个 `restrict` 条目存在，每个条目都会根据前面的声明细化访问限制。示例中的值授予本地系统完全的查询和控制访问权限，同时允许远程系统仅能够查询时间。

关键字 `server` 指定服务器进行查询。该文件可以包含多个 `server` 关键字，每行列出一个服务器。

关键字 `pool` 指定服务器池。ntpd 会根据需要从该池中添加一个或多个服务器，以达到 `tos minclock` 值所指定的对等方数量。

关键字 `iburst` 指示 ntpd 在首次建立联系时与服务器进行八次快速数据包交换，以帮助快速同步系统时间。

关键字 `leapfile` 指定一个文件的位置，该文件包含关于闰秒的信息。该文件会通过 periodic(8) 自动更新。此关键字指定的文件位置必须与 **/etc/rc.conf** 文件中的变量 `ntp_db_leapfile` 所设置的路径匹配。

### 时间信息查看

显示当前系统日期和时间：

```sh
$ date
2025年 3月22日 星期六 15时27分29秒 CST
```

### 设置并启动 NTP 服务

设置 ntpd_enable=YES 以在启动时启动 ntpd。将 ntpd_enable=YES 添加到 /etc/rc.conf 后，可以通过以下命令立即启动 ntpd，而无需重启系统：

```sh
# service ntpd enable
```

启动 NTP 服务

```sh
# service ntpd start
```

允许 ntpd 在启动时一次性调整时钟的一切偏差：

```sh
# sysrc ntpd_sync_on_start="YES"
```

通常，如果时钟偏差超过 1000 秒，ntpd 会记录错误信息并退出。此选项用于绕过此限制，在没有电池支持的实时时钟的系统中尤其有用。

保护 ntpd 守护进程不会因内存不足 (OOM) 而被系统终止:

```sh
# sysrc ntpd_oomprotect="YES"
```

### 手动时间同步命令

在 FreeBSD 上，ntpd 可以作为一个非特权用户启动并运行。这需要 mac_ntpd(4) 策略模块。启动脚本 **/etc/rc.d/ntpd** 首先检查 NTP 配置。如果可能，它会加载 mac_ntpd 模块，然后以非特权用户 ntpd（用户 ID 123）启动 ntpd。为了避免文件和目录访问问题，当配置包含任何与文件相关的选项时，启动脚本不会自动以 ntpd 用户身份启动 ntpd。

首先临时结束现有的 ntpd 服务，以防止阻止时间同步。

```sh
# service ntpd onestop
```

重启后服务会继续运行。

使用 Windows 时间服务器同步系统：

```sh
# ntpd -q -p time.windows.com
```

| 选项 | 作用 |
| ---- | ---- |
| `-q` | 同步一次并退出 |
| `-g` | 允许一次性进行大幅度时间调整 |
| `-p` | 指定 NTP 服务器（例如 `pool.ntp.org`） |

当系统时间与 NTP 服务器偏差超过 1000 秒时，ntpd 默认拒绝修正并退出，必须使用 `-g` 选项强制修正：

```sh
# ntpd -q -g -p pool.ntp.org
```

| 选项 | 作用 |
| ---- | ---- |
| `-g` | 允许大时间偏差修正 |

使用 pool.ntp.org 服务器更新系统时间。


## 参考文献

- FreeBSD Project. adjkerntz(8)[EB/OL]. [2026-04-24]. <https://man.freebsd.org/cgi/man.cgi?query=adjkerntz&sektion=8>.

## 课后习题

1. 对 NTP 服务进行安全加固（如启用认证、限制查询来源），记录加固措施及其对时间同步精度的影响。
2. 配置硬件 RTC 时钟的时区设置（UTC 与本地时间），分析双系统场景下 RTC 时区不一致导致的时间偏移问题。
3. 搭建一个本地 NTP 时间服务器，配置其为局域网内其他设备提供时间同步服务，记录服务器与客户端的配置流程。
