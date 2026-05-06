# 5.10 sysctl 工具

sysctl(8) 实用程序用于修改正在运行的 FreeBSD 系统。本节涵盖 sysctl 命令用法与 sysctl.conf 的配置方法。

sysctl(8) 工具可以检索内核状态，并为具有适当权限的进程设置内核状态。

## 读取内核状态变量

sysctl 命令支持读取和写入内核状态变量。要查看所有可读取的变量：

```sh
$ sysctl -a
```

输出类似如下内容：

```sh
kern.ostype: FreeBSD
kern.osrelease: 16.0-CURRENT
kern.osrevision: 199506
kern.version: FreeBSD 16.0-CURRENT #0 main-n285005-e9fc0c538264: Mon Apr 13 12:44:54 UTC 2026
    root@releng3.nyi.freebsd.org:/usr/obj/usr/src/amd64.amd64/sys/GENERIC

kern.maxvnodes: 184403
kern.maxproc: 9428
kern.maxfiles: 129441
kern.argmax: 524288
kern.securelevel: -1
kern.hostname: ykla
kern.hostid: 4270621168
kern.clockrate: { hz = 100, tick = 10000, profhz = 8128, stathz = 127 }

……省略其他输出……
```

要读取特定变量，指定其名称：

```sh
$ sysctl kern.maxproc
```

输出类似于以下内容：

```sh
kern.maxproc: 9428
```

### 使用管理信息库表读取内核状态变量

sysctl 基于管理信息库（MIB）风格的 ASCII 名称标识。

**管理信息库表**

| sysctl | 说明 |
| ------ | ---- |
| kern | 内核功能和特性 |
| vm | 虚拟存储器 |
| vfs | 文件系统 |
| net | 网络 |
| debug | 调试参数 |
| hw | 硬件 |
| machdep | 机器相关 |
| user | 用户空间 |
| p1003_1b | POSIX 1003.1B |

管理信息库（MIB）是分层的，因此指定特定前缀将列出它下面的所有节点：

```sh
$ sysctl net
```

输出类似于以下内容：

```sh
net.local.stream.recvspace: 65536
net.local.stream.sendspace: 65536
net.local.dgram.recvspace: 16384
net.local.dgram.maxdgram: 8192
net.local.seqpacket.recvspace: 65536
net.local.seqpacket.maxseqpacket: 65536
net.local.sockcount: 19
net.local.taskcount: 9

……省略其他输出……
```

## sysctl 工具相关文件结构

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

在系统启动过程中，**/etc/sysctl.conf** 文件将由 **/etc/rc.d/sysctl** 脚本加载。

sysctl 的默认源代码在 [/sbin/sysctl/](https://github.com/freebsd/freebsd-src/tree/main/sbin/sysctl)。

sysctl.conf 的源代码位于 [/sbin/sysctl/sysctl.conf](https://github.com/freebsd/freebsd-src/blob/main/sbin/sysctl/sysctl.conf)。

> **技巧**
>
> 不建议直接修改 **/etc/sysctl.conf** 文件，如需自定义配置，应使用 **/etc/sysctl.conf.local** 文件扩展本地配置，避免系统更新时配置被覆盖。

## 配置文件

在系统进入多用户模式时将读取 **/etc/sysctl.conf** 文件，用于设置内核的默认配置。格式看起来类似于 **/etc/rc.conf**。

基本系统默认的 **/etc/sysctl.conf** 文件实际上是空文件：

```sh
#  此文件在系统进入多用户模式时读取，其内容通过 sysctl 管道传递以调整内核值
#  详情参见 man 5 sysctl.conf


#  取消注释此行可以防止用户查看由其他 UID 运行的进程信息
#security.bsd.see_other_uids=0
```

在文件中的注释仍是 `#`。因此上述所有行都被注释，无一生效。

> **技巧**
>
> 建议启用 `security.bsd.see_other_uids=0` 和 `security.bsd.see_other_gids=0` 配置，可限制用户查看其他用户的进程信息。

> **警告**
>
> 虽然 **/etc/sysctl.conf** 文件实质上为空，但这不代表系统默认的 sysctl 参数为空。它们是通过不同的宏（如 `SYSCTL_INT`）注入到系统中的！使用命令 `sysctl -a` 可列出当前系统所有默认的参数值。

## 设置内核状态变量

要设置特定变量，使用语法 **变量**=**值**。

```ini
sysctl 管理信息标识符=值
```

示例：

```sh
# sysctl kern.maxfiles=9500
```

> **注意**
>
> 指定的值会在系统进入多用户模式后设置。并非所有变量都可以在此模式下设置。

输出类似于以下内容：

```sh
kern.maxfiles: 9428 -> 9500
```

> **注意**
>
> 为了在重启后保持配置，必须将这些变量添加到 **/etc/sysctl.conf** 文件中。

例如，要关闭致命信号退出的日志记录，并防止用户查看其他用户启动的进程，可以在 **/etc/sysctl.conf** 文件中设置以下参数：

```ini
# 不记录致命信号退出（例如，sig 11）
kern.logsigexit=0

# 防止用户查看由其他 UID 启动的进程信息。
security.bsd.see_other_uids=0
```

## 参考文献

- FreeBSD Project. sysctl(8)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=sysctl&sektion=8>. 内核状态查询与设置工具手册页。
- FreeBSD Project. sysctl.conf(5)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=sysctl.conf&sektion=5>. sysctl 配置文件手册页。

## 课后习题

1. 创建 **/etc/sysctl.conf.local** 文件并设置几个自定义 sysctl 参数，验证其是否覆盖系统默认值，分析 sysctl 配置文件的加载顺序。
2. 查阅一个 sysctl 参数的源代码实现（如通过 `SYSCTL_INT` 宏定义），分析其读写权限控制与值域校验的实现机制。
3. 启用 `security.bsd.see_other_uids=0` 和 `security.bsd.see_other_gids=0`，对比启用前后普通用户能看到的进程信息差异，分析该安全策略在进程可见性控制层面的实现原理。
