# TwinCAT/BSD 系统导论

## TwinCAT/BSD 简介

TwinCAT/BSD 是一款针对工业控制领域优化的操作系统，基于 FreeBSD 开发，由倍福公司（Beckhoff）推出。

TwinCAT/BSD 作为基于 FreeBSD 的 PLC（Programmable Logic Controller，可编程逻辑控制器）控制操作系统，专为工业自动化场景设计。

PLC 是一种专用于工业自动化控制的计算设备，用于监控和控制生产设备。

个人用户可以免费使用 TwinCAT/BSD 的非商业功能。

关于硬件兼容性与授权策略：倍福支持第三方硬件安装，但许可证费用按硬件性能分级收取。一般 PLC 标准为 P40/P50 级别。P40/P50 是倍福定义的硬件性能等级，P 后面的数字越大表示硬件性能越强。例如，一个基本许可证价格为 1500 元，而第三方硬件按 P90 级别收费，同等功能约为 6000 元。

更多内容请参考：

- TwinCAT/BSD for Industrial PCs[EB/OL]. [2026-03-25]. <https://www.beckhoff.com/en-en/products/ipc/software-and-tools/twincat-bsd/>. 倍福官方 TwinCAT/BSD 产品说明，涵盖技术规格与授权信息。

## 下载 TwinCAT/BSD

了解 TwinCAT/BSD 的基本信息后，可开始准备安装。首先需获取系统安装镜像，下载地址如下：

<https://www.beckhoff.com/en-us/search-results/?q=bsd>

![TCBSD](../.gitbook/assets/tcbsd.png)

点击 `↓ ZIP` 即可下载。**注意：需要注册才能下载。**

首先解压 ZIP，得到 `TCBSD-x64-13-92446.iso` 文件

## 创建虚拟硬盘并写入镜像

下载完成后，需对镜像进行特殊处理才能用于虚拟机安装。TCBSD 官方镜像是使用 `dd` 工具制作的，实际上对应 FreeBSD 的 img 镜像，因此虚拟机无法直接识别。dd 是一个用于复制和转换文件的命令行工具，常用于制作磁盘镜像。需要通过创建虚拟 VHD 硬盘的方式，将镜像写入硬盘后再挂载到虚拟机进行安装。VHD 是虚拟硬盘格式，用于在虚拟机中模拟物理硬盘。

首先右键单击“这台电脑”，依次选择“管理”→“磁盘管理”→“操作”→“创建 VHD”。

![TCBSD](../.gitbook/assets/t1.png)

硬盘大小设置为 1 GB 即可，过大无实际必要，该硬盘仅用于写入镜像。其他配置可参考示例设置。

![TCBSD](../.gitbook/assets/t2.png)

可以看到新增了一个 `磁盘 2`，右键单击左侧区域，选择“初始化磁盘”。（**注意：文中示例中已有两块硬盘，分别为 `磁盘 0` 和 `磁盘 1`。**）

![TCBSD](../.gitbook/assets/t3.png)

选择默认参数即可。用 GPT 分区表格式化磁盘 2。GPT 是 GUID 分区表，是一种现代的磁盘分区标准。

![TCBSD](../.gitbook/assets/t4.png)

右键单击右侧区域，点击“新建简单卷”，其他保持默认配置即可。

![TCBSD](../.gitbook/assets/t5.png)

可以看到出现了一个 `新加卷 F`：

![TCBSD](../.gitbook/assets/t6.png)

![TCBSD](../.gitbook/assets/t7.png)

打开 Rufus 工具，程序会自动识别新加卷 F。选择解压出的镜像 `TCBSD-x64-13-92446.iso`，点击“开始”即可。在刷新分区表的最后一步可能需要较长时间，请耐心等待。

![TCBSD](../.gitbook/assets/t8.png)

返回磁盘管理，选择“操作”→“重新扫描磁盘”。**否则下面虚拟机无法加载磁盘 2。**

![TCBSD](../.gitbook/assets/t9.png)

可以看到磁盘 2 已被写入镜像：

![TCBSD](../.gitbook/assets/t10.png)

## 通过 VMware Workstation 安装 TwinCAT/BSD

虚拟硬盘准备完成后，可以开始通过 VMware Workstation 进行系统安装。以下介绍通过 VMware Workstation 安装 TwinCAT/BSD 的步骤。先以正常方法创建一个空白的虚拟机模板，然后点击“虚拟机设置”→“添加”→“硬盘”。点击下一步：

![TCBSD](../.gitbook/assets/t11.png)

保持默认即可：

![TCBSD](../.gitbook/assets/t12.png)

选择第三项“使用物理磁盘”：

![TCBSD](../.gitbook/assets/t13.png)

这里选择磁盘 2，并使用整个分区：

![TCBSD](../.gitbook/assets/t14.png)

保持默认即可：

![TCBSD](../.gitbook/assets/t15.png)

检查磁盘的大小和名称是否正确，选择错误将导致无法启动。

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

开始安装：

![TCBSD](../.gitbook/assets/t24.png)

提示安装完成：

![TCBSD](../.gitbook/assets/t25.png)

选择“reboot”重启进入安装后的系统：

![TCBSD](../.gitbook/assets/t26.png)

## 用户账户

系统安装完成后，需要了解系统的用户账户配置。默认用户名是 `Administrator`，其密码是在安装时设置的。倍福其他 PLC 默认密码通常是 `1`，但 TwinCAT/BSD 的密码由用户自定义。

首先使用 doas 提升权限修改 root 用户密码：

```sh
$ doas passwd root
```

然后就可以使用 doas 提升权限为超级用户（root），进入 root Shell：

```sh
$ doas su
```

## Web 界面登录

TwinCAT/BSD 提供了 Web 管理界面，方便用户进行系统配置和管理。网络连接方式使用 NAT，经测试桥接模式无法访问。NAT 是网络地址转换，是一种将私有 IP 地址转换为公网 IP 地址的技术。

使用 `ifconfig` 查看当前 IP，然后打开主机的浏览器，输入 `ifconfig` 命令输出的 IP 地址。

示例中，`ifconfig` 显示的 IP 为 `192.168.245.138`，则访问地址为 `https://192.168.245.138`。（注意使用 **https**，而非 *http*，后者无法访问）

输入用户名 `Administrator` 和密码即可登录：

![TCBSD](../.gitbook/assets/tcbsd1.png)

![TCBSD](../.gitbook/assets/tcbsd2.png)

## 故障排除与未竟事宜

在使用 TwinCAT/BSD 的过程中，可能会遇到问题。以下是常见问题的解决方法。

### 设置静态 IP 后，网卡存在两个 IP

为网卡设置静态 IP 后，该网卡可能会出现两个 IP：一个为静态 IP，另一个由 DHCP 服务分配。这是由于倍福系统开机自动启动的 dhcpcd 服务导致的。dhcpcd 是一个 DHCP 客户端守护进程，用于自动获取 IP 地址。可以通过修改 `/etc/rc.conf` 文件来解决：

修改或加入：

```ini
dhcpcd_flags="--denyinterfaces igb0"
```

即将 `dhcpcd_flags` 的值由 `--waitip` 改为 `--denyinterfaces igb0`（配置 dhcpcd，禁止在指定网卡 `igb0` 上自动获取 DHCP 地址）。`igb0` 为需要配置静态 IP 的网卡名，请根据实际情况更改。

## 修改软件源

软件源结构：

```sh
/usr/local/
├── share/
│   └── examples/
│       └── bhf/
│           └── pkgrepo-set.sh  # pkg 仓库设置脚本
└── etc/
    └── pkg/
        └── repos/
            └── FreeBSD.conf  # FreeBSD pkg 仓库配置文件
```

为了提高软件安装和更新的速度，可以将 pkg 仓库切换为中国镜像。以下介绍如何将 pkg 仓库切换为中国镜像。使用 `doas` 执行脚本，将 pkg 仓库切换为中国镜像：

```sh
$ doas sh /usr/local/share/examples/bhf/pkgrepo-set.sh china
```

使用 doas 提升权限，先更新 pkg 仓库索引，再升级已安装的软件包：

```sh
$ doas pkg update && doas pkg upgrade
```

## 安装 Beckhoff 开发工具包

如果需要进行开发工作，可以安装 Beckhoff 提供的开发工具包。使用 doas 安装操作系统通用用户空间开发工具包：

```sh
$ doas pkg install os-generic-userland-devtools
```

该操作将安装由 Beckhoff 维护的 LLVM、C/C++ 头文件、C/C++ 库以及 TwinCAT SDK。

## 启用 FreeBSD 源

TwinCAT/BSD 默认只提供 Beckhoff 维护的软件包。如果需要使用更多 FreeBSD 官方维护的软件包，可以手动启用相关源。

```sh
/usr/local/
├── share/
│   └── examples/
│       └── bhf/
│           └── pkgrepo-set.sh  # pkg 仓库设置脚本
└── etc/
    └── pkg/
        └── repos/
            └── FreeBSD.conf  # FreeBSD pkg 仓库配置文件
```

编辑 `/usr/local/etc/pkg/repos/FreeBSD.conf` 文件，将配置文件中 `FreeBSD: {enabled: no}` 的 `no` 修改为 `yes` 即可。

## 课后习题

1. 查找 TwinCAT/BSD 中 dhcpcd 服务的实现，分析其为何在设置静态 IP 后仍会分配 DHCP 地址，重构最小化的网络配置方案并验证。

2. 在 TwinCAT/BSD 系统中同时启用 Beckhoff 源和 FreeBSD 官方源，尝试安装一个来自 FreeBSD 源的软件包（如 nginx）。
