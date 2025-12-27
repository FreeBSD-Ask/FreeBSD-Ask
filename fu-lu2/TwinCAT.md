# TwinCAT/BSD 导论

## TwinCAT/BSD 简介

TwinCAT/BSD 是由倍福公司（Beckhoff）开发的基于 FreeBSD 的 PLC（Programmable Logic Controller，可编程逻辑控制器）控制操作系统。在不使用商业功能时，个人用户完全可以免费使用。倍福支持第三方硬件安装，但许可证费用按顶配 PLC 收取：倍福的许可证费用根据硬件性能而定，一般 PLC 标准为 P40/P50。例如，一个基本许可证价格为 1500 元，而第三方硬件按 P90 收费，同样功能约为 6000 元。

更多内容请参考：

- [GPU 直通](https://github.com/FreeBSD-Ask/freebsd-journal-cn/blob/main/2023-0304/GPU%20Passthrough.md)
- [TwinCAT/BSD for Industrial PCs](https://www.beckhoff.com/en-en/products/ipc/software-and-tools/twincat-bsd/)


## 下载 TwinCAT/BSD

<https://www.beckhoff.com/en-us/search-results/?q=bsd>

![TCBSD](../.gitbook/assets/tcbsd.png)

点击 `↓ ZIP` 即可下载。**注意：需要注册才能下载。**

首先解压缩 ZIP，将“TCBSD-x64-13-92446.iso”解压缩出来。

## 创建虚拟硬盘并写入镜像

TCBSD 官方镜像是使用 `dd` 工具制作的，实际上对应 FreeBSD 的 img 镜像，因此虚拟机无法直接识别。需要通过创建虚拟 VHD 硬盘的方式，将镜像写入硬盘后再挂载到虚拟机进行安装。


首先右键单击“这台电脑”，选择管理--磁盘管理--操作--创建 VHD。

![TCBSD](../.gitbook/assets/t1.png)

硬盘大小设置为 1GB 即可，过大无实际必要，该硬盘仅用于写入镜像。其他配置可以参考示例设置。

![TCBSD](../.gitbook/assets/t2.png)

可以看到新增了一个 `磁盘 2`，右键单击左侧区域，选择“初始化磁盘”。（​**注意：文中示例中已有两块硬盘，分别为 `磁盘 0` 和 `磁盘 1`。**​）

![TCBSD](../.gitbook/assets/t3.png)

选择默认参数即可。用 GPT 分区表格式化磁盘 2。

![TCBSD](../.gitbook/assets/t4.png)

右键单击右侧区域，点击“新建简单卷”，其他保持默认配置即可。

![TCBSD](../.gitbook/assets/t5.png)

可以看到出来了一个 `新加卷 F`：

![TCBSD](../.gitbook/assets/t6.png)

![TCBSD](../.gitbook/assets/t7.png)

打开 Rufus 工具，程序会自动识别新加卷 F。选择解压出的镜像 `TCBSD-x64-13-92446.iso`，点击“开始”即可。在刷新分区表的最后一步可能需要较长时间，请耐心等待。

![TCBSD](../.gitbook/assets/t8.png)

返回磁盘管理，选择“操作”--重新扫描磁盘。**否则下面虚拟机无法加载出磁盘 2。**

![TCBSD](../.gitbook/assets/t9.png)

可以看到磁盘 2 已经被写入镜像了：

![TCBSD](../.gitbook/assets/t10.png)

## 通过 VMware Workstation 安装 TwinCAT/BSD

我们先以正常方法创建一个空白的虚拟机模板，然后点击“虚拟机设置”--“添加”--“硬盘”。点击下一步：

![TCBSD](../.gitbook/assets/t11.png)

保持默认即可：

![TCBSD](../.gitbook/assets/t12.png)

选择第三项“使用物理磁盘”：

![TCBSD](../.gitbook/assets/t13.png)

这里选择磁盘 2，并使用整个分区：

![TCBSD](../.gitbook/assets/t14.png)

保持默认即可：

![TCBSD](../.gitbook/assets/t15.png)

检查磁盘的大小、名称是否符合，选错了就无法启动。

![TCBSD](../.gitbook/assets/t16.png)

开启 UEFI：

![TCBSD](../.gitbook/assets/t17.png)

保存以上配置后开机：

![TCBSD](../.gitbook/assets/t18.png)

开始安装：

![TCBSD](../.gitbook/assets/t19.png)

选择磁盘进行安装，看大小就能判断选择哪个：

![TCBSD](../.gitbook/assets/t20.png)

选择“Yes”开始安装：

![TCBSD](../.gitbook/assets/t21.png)

输入 `Administrator` 的密码：

![TCBSD](../.gitbook/assets/t22.png)

再次输入 `Administrator` 的密码：

![TCBSD](../.gitbook/assets/t23.png)

开始安装了：

![TCBSD](../.gitbook/assets/t24.png)

提示安装完成：

![TCBSD](../.gitbook/assets/t25.png)

选择“reboot”重启进入安装后的系统：

![TCBSD](../.gitbook/assets/t26.png)


## 用户账户

默认用户名是 `Administrator`，他的密码是你在安装时设置的。倍福其他 PLC 默认密码都是 `1`。

首先使用 doas 提升权限修改 root 用户密码

```sh
$ doas passwd root
```

然后就可以使用 doas 提升权限为超级用户（root），进入 root Shell

```sh
$ doas su
```

## Web 界面登录

网络连接方式使用 NAT，经测试桥接模式无法访问。

使用 `ifconfig` 查看当前 IP，然后打开主机的浏览器输入 `ifconfig` 命令输出的 IP 内容！

示例中，`ifconfig` 显示的 IP 为 `192.168.245.138`，则访问地址为 `https://192.168.245.138`。（注意使用 ​**https**​，而非 *​http*​，后者无法访问）

输入用户名 `Administrator` 和密码即可登录：

![TCBSD](../.gitbook/assets/tcbsd1.png)

![TCBSD](../.gitbook/assets/tcbsd2.png)


## 故障排除与未竟事宜

### 设置静态 IP 后，网卡存在两个 IP

为网卡设置静态 IP 后，该网卡可能会出现两个 IP：一个为静态 IP，另一个由 DHCP 服务分配。这是由于倍福系统开机自动启动的 dhcpcd 服务导致的，可以通过修改 `/etc/rc.conf` 文件来解决：


修改或加入：

```ini
dhcpcd_flags="--denyinterfaces igb0"
```

即将 `dhcpcd_flags` 的值由 `--waitip` 改为 `--denyinterfaces igb0`（配置 dhcpcd，禁止在指定网卡 `igb0` 上自动获取 DHCP 地址）。`igb0` 为需要配置静态 IP 的网卡名，请根据实际情况更改。


## 换源

使用 `doas` 执行脚本，将 pkg 仓库切换为中国镜像：

```sh
$ doas sh /usr/local/share/examples/bhf/pkgrepo-set.sh china
```

使用 doas 提升权限，先更新 pkg 仓库索引，再升级已安装的软件包：

```sh
$ doas pkg update && doas pkg upgrade
```

## 安装 Beckhoff 提供开发工具包


使用 doas 安装操作系统通用用户空间开发工具包：

```sh
$ doas pkg install os-generic-userland-devtools
```

该操作将安装由 Beckhoff 维护的 LLVM、C/C++ 头文件、C/C++ 库以及 TwinCAT SDK。

## 启用 FreeBSD 源

默认情况下，pkg 只能安装 Beckhoff 维护的包。若需安装 FreeBSD 官方维护的包，需要手动启用相关源。

使用 doas 提升权限，用 ee 编辑器修改 FreeBSD pkg 仓库配置文件：

```sh
$ doas ee /usr/local/etc/pkg/repos/FreeBSD.conf
```

将配置文件中 `FreeBSD: {enabled: no}` 的 `no` 修改为 `yes` 即可。

