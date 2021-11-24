# 第八节 TCP BBR

TCP BBR 是一种拥塞控制算法。作用有两个，

1. **在有一定丢包率的网络链路上充分利用带宽。**
2. **降低网络链路上的 buffer 占用率，从而降低延迟。**

一般来说，如果你使用了代理软件，建议开启TCP BBR 功能，在速度和稳定性上会有十分显著的作用。该项目在 FreeBSD 中，由 Netflix 团队协助开发。最低系统版本支持：r363032，也即推荐 FreeBSD 13.0。

**修改内核配置**

`# cd /usr/src/sys/amd64/conf`

如果安装FreeBSD时没有选择安装内核源码，建议阅读 第二十章。

`# cp GENERIC GENERIC-bbr`

`# ee GENERIC-bbr`

调整配置，修改`ident`的值为`GENERIC-bbr`，在`ident`这一项下面加入以下项目：

```
options TCPHPTS
options RATELIMIT
options WITH_EXTRA_TCP_STACKS=1
```

新建`/etc/src.conf`，内容为:

```
KERNCONF=GENERIC-bbr
MALLOC_PRODUCTION=yes
```

**编译并安装内核**
```
# /usr/sbin/config GENERIC-BBR
# cd ../compile/GENERIC-BBR
# make cleandepend && make depend
# make -jN+1
```

其中`N`建议为`CPU核心数`。

`# make install`

安装内核，完成后重启使用新内核。

`# uname -a`

如果显示出`GENERIC-bbr`，则表示 TCP BBR 内核编译并安装成功。

**配置和加载BBR模块**

`# sysrc kld_list+="tcp_rack tcp_bbr"`

启动时加载 BBR 模块。

`# echo 'net.inet.tcp.functions_default=bbr' >> /etc/sysctl.conf`

设置默认使用 BBR，重启。

`# sysctl net.inet.tcp.functions_default`

如果结果是`net.inet.tcp.functions_default: bbr`，则启用 TCP BBR 成功。

**注意：**故障排除等事宜请参考 [https://github.com/netflix/tcplog_dumper](https://github.com/netflix/tcplog_dumper)
