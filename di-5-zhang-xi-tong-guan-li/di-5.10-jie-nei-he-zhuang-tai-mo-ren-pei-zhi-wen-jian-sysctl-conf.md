# 5.10 内核状态默认配置文件（sysctl.conf）

sysctl 是 FreeBSD 用于查看和修改内核运行时参数的工具。sysctl 命令支持读取和写入内核状态变量，其状态信息使用管理信息库（MIB）风格的 ASCII 名称标识。

`sysctl` 命令的关键选项如下：

| 选项 | 说明 | 备注 |
|------|------|------|
| `-a` | 列出所有当前可用的值 | 排除不透明变量和标记 CTLFLAG_SKIP 的变量 |
| `-d` | 输出变量的描述而非其值 | |
| `-e` | 以 `name=value` 格式输出 | 用于产生可回传给 sysctl 的输出；若指定了 `-N` 或 `-n` 则忽略此选项；注意 sysctl(8) 的 `-e` 与 sysrc(8) 的 `-e` 含义不同 |
| `-h` | 以人类可读格式输出 | |
| `-n` | 仅输出变量值，不输出名称 | 适用于设置 Shell 变量，如 `set psize=$(sysctl -n hw.pagesize)` |
| `-j jail` | 在指定 Jail 中执行操作 | |

在系统进入多用户模式时将读取 `/etc/sysctl.conf` 文件，用于设置内核的默认配置。

在系统启动过程中，`/etc/sysctl.conf` 文件将由 `/etc/rc.d/sysctl` 脚本加载，采用 sysctl(8) 命令的格式，即：

```ini
sysctl_管理信息标识符=值
```

在文件中的注释仍是 `#`。

相关文件结构：

```sh
/
└── etc/
    ├── rc.d/
    │   ├── sysctl               # rc(8) 脚本，处理 sysctl.conf，在系统过渡到多用户模式早期执行
    │   └── sysctl_lastload      # rc(8) 脚本，处理 sysctl.conf，在系统接近多用户模式时执行
    ├── sysctl.conf              # sysctl(8) 的初始设置
    ├── sysctl.conf.local        # 机器特定设置，用于共享 /etc/sysctl.conf 的位置（默认不存在）
    └── sysctl.kld.d/            # 内核模块特定设置，用于通过 rc.subr(8) 加载的模块（默认为空目录）
```

sysctl 的默认源代码在 [/sbin/sysctl/](https://github.com/freebsd/freebsd-src/tree/main/sbin/sysctl)。

> **技巧**
>
> 不建议直接修改 `/etc/sysctl.conf` 文件，如需自定义配置，应使用 `/etc/sysctl.conf.local` 文件进行本地配置扩展，避免系统更新时配置被覆盖。

## 默认读取的配置文件 `/etc/sysctl.conf`

[sysctl.conf(5)](https://man.freebsd.org/sysctl.conf) 是用于配置内核的默认参数，位于 `/etc/sysctl.conf` 文件，对应源代码 [/sbin/sysctl/sysctl.conf](https://github.com/freebsd/freebsd-src/blob/main/sbin/sysctl/sysctl.conf)。

默认的 `/etc/sysctl.conf` 文件实际上是空文件：

```sh
#  此文件在系统进入多用户模式时读取，其内容通过 sysctl 管道传递以调整内核值
#  详情参见 man 5 sysctl.conf


#  取消注释此行可以防止用户查看由其他 UID 运行的进程信息
#security.bsd.see_other_uids=0
```

所有行都被注释，无一生效。

> **技巧**
>
> 建议启用 `security.bsd.see_other_uids=0` 和 `security.bsd.see_other_gids=0` 配置，可降低信息泄露风险，限制用户查看其他用户的进程信息，增强系统安全审计能力。

> **警告**
>
> 虽然 `/etc/sysctl.conf` 文件实质上为空，但这不代表系统默认的 sysctl 参数为空！它们是通过不同的宏（如 `SYSCTL_INT`）注入到系统中的！使用命令 `sysctl -a` 可列出当前系统所有默认的参数值。

## 参考文献

- FreeBSD Project. sysctl(8)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=sysctl&sektion=8>. 内核状态查询与设置工具手册页。
- FreeBSD Project. sysctl.conf(5)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=sysctl.conf&sektion=5>. sysctl 配置文件手册页。

## 课后习题

1. 创建 `/etc/sysctl.conf.local` 文件并设置几个自定义 sysctl 参数，验证其是否覆盖系统默认值。

2. 查找一个 sysctl 参数的源代码实现（如通过 SYSCTL_INT 宏定义），尝试修改该参数并观察系统行为变化。

3. 启用 `security.bsd.see_other_uids=0` 和 `security.bsd.see_other_gids=0`，对比启用前后普通用户能看到的进程信息差异，自行实现一个更为细粒度的 sysctl 选项，将其提交到 FreeBSD 项目。
