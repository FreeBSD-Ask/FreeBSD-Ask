# 第一节 网络参数配置命令



#### 系统设置工具 bsdconfig <a href="xi-tong-she-zhi-gong-ju-bsdconfig" id="xi-tong-she-zhi-gong-ju-bsdconfig"></a>

`bsdconfig` 是 FreeBSD 提供的系统配置实用工具，是个 Shell 界面。

#### 安全的操作 rc 文件 <a href="an-quan-de-cao-zuo-rc-wen-jian" id="an-quan-de-cao-zuo-rc-wen-jian"></a>

`sysrc` 是 FreeBSD 提供的 rc 文件实用工具，代替手动编辑 `rc.conf`。

#### 作为网关服务器 <a href="zuo-wei-wang-guan-fu-wu-qi" id="zuo-wei-wang-guan-fu-wu-qi"></a>

打开 IP 转发功能：

```
sysrc gateway_enable="YES"
sysrc ipv6_gateway_enable="YES"
```

打开防火墙，开启 NAT：

```
sysrc firewall_enable="YES"
sysrc firewall_script="/etc/ipfw.rules"
sysrc firewall_nat_enable="YES"
```

设置默认接受连接： `vi /boot/loader.conf`

```
net.inet.ip.fw.default_to_accept=1
```

#### 手动设置 resolv.conf <a href="shou-dong-she-zhi-resolvconf" id="shou-dong-she-zhi-resolvconf"></a>

手动编辑 resolv.conf 后，重启系统又会被重置，因为 DHCP 会重写这个文件。

防止 `resolvconf` 服务覆盖 resolv.conf：`ee /etc/resolvconf.conf`

```
resolv_conf="/dev/null"
```

再编辑 resolv.conf 就可以了。

#### 查看网卡速率 <a href="cha-kan-wang-ka-su-lv" id="cha-kan-wang-ka-su-lv"></a>

每 `1` 秒刷新一次：

```
systat -if 1
```
