# 第一节 网络参数配置命令



#### 系统设置工具 bsdconfig

`# bsdconfig` 是 FreeBSD 提供的系统配置实用工具，是个 Shell 界面。

#### 安全的操作 rc 文件

`# sysrc` 是 FreeBSD 提供的 rc 文件实用工具，代替手动编辑 `rc.conf`。

#### 作为网关服务器

打开 IP 转发功能：

```
# sysrc gateway_enable="YES"
# sysrc ipv6_gateway_enable="YES"
```

打开防火墙，开启 NAT：

```
# sysrc firewall_enable="YES"
# sysrc firewall_script="/etc/ipfw.rules"
# sysrc firewall_nat_enable="YES"
```

设置默认接受连接： `# ee /boot/loader.conf`

```
net.inet.ip.fw.default_to_accept=1
```

#### 手动设置 resolv.conf

手动编辑 resolv.conf 后，重启系统又会被重置，因为 DHCP 会重写这个文件。

防止 `resolvconf` 服务覆盖 resolv.conf：`# ee /etc/resolvconf.conf`

```
resolv_conf="/dev/null"
```

再编辑 resolv.conf 就可以了。

#### 查看网卡速率

每 `1` 秒刷新一次：

```
# systat -if 1
```
