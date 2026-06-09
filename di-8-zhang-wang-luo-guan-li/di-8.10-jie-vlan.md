# 8.10 VLAN

VLAN（虚拟局域网）是将网络虚拟划分为多个子网络的一种方式，也称为网络分段。每个段将拥有自己的广播域，并与其他 VLAN 隔离。

在 FreeBSD 上，VLAN 必须由网络卡驱动程序支持。要查看哪些驱动程序支持 VLAN，请参阅 [vlan(4)](https://man.freebsd.org/cgi/man.cgi?query=vlan&sektion=4&format=html) 手册页。

在配置 VLAN 时，需要知道几个信息。首先，哪个网络接口？其次，VLAN 标签是什么？

## 定义 VLAN 

假设使用的网卡为 `em0`，VLAN 标签为 `5`，则命令如下：

```sh
# ifconfig em0.5 create vlan 5 vlandev em0 inet 192.168.20.20/24
```

> **注意**
>
> 请注意，接口名称包括了网卡驱动程序名称和 VLAN 标签，并通过点号分隔开来。这是最佳实践，尤其在机器上配置了多个 VLAN 时，能方便地管理 VLAN 配置。

> **注意**
>
> 在定义 VLAN 时，确保父网络接口也被配置和启用。上面的示例中，最小配置为：
>
> ```sh
> # ifconfig em0 up
> ```

要在启动时配置 VLAN，必须更新 **/etc/rc.conf**。要复制上面的配置，需添加以下内容：

```sh
vlans_em0="5"
ifconfig_em0_5="inet 192.168.20.20/24"
```

可以通过简单地将标签添加到 `vlans_em0` 字段，并为该 VLAN 标签的接口配置网络来添加更多 VLAN。

> **注意**
>
> 在 **/etc/rc.conf** 中定义 VLAN 时，请确保父网络接口也被配置和启用。上面的示例中，最简配置为：
>
> ```ini
> ifconfig_em0="up"
> ```

## 为接口指定符号名称

为接口指定符号名称是很有用的，这样当更换关联的硬件时，只需要更新少数几个配置变量。例如，安全摄像头需要在 `em0` 上运行 VLAN 1。如果以后将 `em0` 卡替换为使用 [ixgb(4)](https://man.freebsd.org/cgi/man.cgi?query=ixgb&sektion=4&format=html) 驱动程序的网卡，那么就不需要再将所有指向 `em0.1` 的引用改为 `ixgb0.1`。

要在网卡`em0` 上配置 VLAN `5`，并为接口指定名称 `cameras`，为其分配 IP 地址 `192.168.20.20/24`，使用以下命令：

```sh
# ifconfig em0.5 create vlan 5 vlandev em0 name cameras inet 192.168.20.20/24
```

如果接口名为 `video`，则使用以下命令：

```sh
# ifconfig video.5 create vlan 5 vlandev video name cameras inet 192.168.20.20/24
```

在 **/etc/rc.conf** 中添加以下内容以在启动时应用更改：

```sh
vlans_video="cameras"
create_args_cameras="vlan 5"
ifconfig_cameras="inet 192.168.20.20/24"
```