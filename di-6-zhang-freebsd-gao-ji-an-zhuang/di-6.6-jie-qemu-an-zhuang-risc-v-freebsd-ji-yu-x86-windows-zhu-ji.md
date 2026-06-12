# 6.6 QEMU 安装 RISC-V FreeBSD（基于 x86 Windows 主机）

QEMU（Quick Emulator 的缩写）是一个开源的通用机器模拟器与虚拟化器（machine emulator and virtualizer）。

本节实验环境基于 Windows 11 24H2（宿主机，x86-64 架构）、FreeBSD 14.2-RELEASE（虚拟机，RISC-V 架构）以及 QEMU 20241220，所有操作步骤均已在此环境下验证通过。

## 下载 Windows 端 QEMU

请访问 QEMU 官方下载页面 [https://www.qemu.org/download/](https://www.qemu.org/download/#windows)，下载并安装适用于 Windows 主机的 QEMU 安装程序（64 位版本）。

具体 QEMU 下载地址：

[QEMU Binaries for Windows (64 bit)](https://qemu.weilnetz.de/w64/)，请下载列表中最新的安装程序。本节撰写时，最新版本为 `qemu-w64-setup-20241220.exe`，大小为 174 MB。

下载后在 Windows 上安装 QEMU。

## RISC-V FreeBSD 磁盘镜像

QEMU 安装完成后，需要下载 RISC-V 架构的 FreeBSD 磁盘镜像。

RISC-V FreeBSD 磁盘镜像（以 FreeBSD 14.2-RELEASE 为例）：

<https://download.freebsd.org/releases/VM-IMAGES/14.2-RELEASE/riscv64/Latest/FreeBSD-14.2-RELEASE-riscv-riscv64-zfs.raw.xz>

下载后解压缩以备后续使用。

## 相关文件结构

安装完成后，相关文件分布在以下目录结构中。

```sh
/usr/
└── local/
    └── share/
        ├── opensbi/
        │   └── lp64/
        │       └── generic/
        │           └── firmware/
        │               └── fw_jump.elf # OpenSBI 固件
        └── u-boot/
            └── u-boot-qemu-riscv64/
                └── u-boot.bin # U-Boot 引导加载程序
```

## OpenSBI

获取 OpenSBI（RISC-V Open Source Supervisor Binary Interface，RISC-V 开源监督者二进制接口），其功能类似于启动固件，在 RISC-V 启动流程中负责 M 模式固件的工作。

### 安装 OpenSBI

以下命令需要在 FreeBSD 系统上执行（可以是另一台 FreeBSD 机器、虚拟机或 WSL 中的 FreeBSD），安装后将固件文件复制到 Windows 主机上使用。

使用 pkg 安装：

```sh
# pkg install opensbi
```

或者使用 Ports 安装：

```sh
# cd /usr/ports/sysutils/opensbi/
# make install clean
```

### 提取 `fw_jump.elf`

```sh
# /etc/periodic/weekly/310.locate # 刷新 locate 数据库
# locate fw_jump.elf
/usr/local/share/opensbi/lp64/generic/firmware/fw_jump.elf
```

提取 `fw_jump.elf` 到 Windows 下备用。

## U-Boot

在 FreeBSD 系统中获取 U-Boot（Universal Boot Loader），其功能类似于 GRUB 2。

### 安装 U-Boot

使用 pkg 安装：

```sh
# pkg install u-boot-qemu-riscv64
```

或者使用 Ports 安装：

```sh
# cd /usr/ports/sysutils/u-boot-qemu-riscv64/
# make install clean
```

### 提取 `u-boot.bin` 文件

```sh
# /etc/periodic/weekly/310.locate # 刷新数据库
# locate u-boot.bin
/usr/local/share/u-boot/u-boot-qemu-riscv64/u-boot.bin
```

提取 `u-boot.bin` 到 Windows 下备用。

## 配置 QEMU

在桌面新建一个文本文件 `qemu.bat`，写入以下内容：

```batch
cd /d "C:\Program Files\qemu"
.\qemu-system-riscv64.exe ^
    -machine virt ^
    -smp 4 ^
    -cpu rv64 ^
    -m 4G ^
    -device virtio-blk-device,drive=hd ^
    -drive file="C:\Users\ykla\Desktop\FreeBSD-14.2-RELEASE-riscv-riscv64-zfs.raw",if=none,id=hd ^
    -device virtio-net-device,netdev=net ^
    -netdev user,id=net,hostfwd=tcp::8022-:22 ^
    -bios "C:\Users\ykla\Desktop\fw_jump.elf" ^
    -kernel "C:\Users\ykla\Desktop\u-boot.bin" ^
    -append "root=LABEL=rootfs" ^
    -nographic
```

参数说明：

| 参数 | 说明 |
| ---- | ---- |
| `^` | Windows 批处理脚本续行符，可将一条长命令拆成多行书写 |
| `smp` | CPU 数量 |
| `cpu` | CPU 架构 |
| `m` | 内存大小 |
| `hostfwd=tcp::8022-:22` | 将宿主机的 8022 端口转发至虚拟机的 22 端口（SSH） |

以上示例中，请将 **C:\Users\ykla\Desktop\** 替换为实际路径。

保存文件后双击运行该脚本。

![Qemu 安装 FreeBSD](../.gitbook/assets/qemu1.png)

输入用户名 `root` 后直接登录，默认无密码。

无论使用 PowerShell 还是 CMD，输出均会出现乱码（例如执行 `ee` 命令或按下 **Tab 键**）。

此外，该镜像默认未为普通用户配置 SSH 服务，因此无法直接通过 SSH 连接 FreeBSD 设备。

创建普通用户（如尚未创建，注意将其加入 wheel 组）：

```sh
# adduser
```

## 配置 sshd 服务

配置 sshd 服务如下：

```sh
# service sshd enable # 添加启动项
# service sshd start # 启动 sshd 服务
```

此后即可在 Windows 上通过 SSH 连接（IP 为 `localhost`）：

```powershell
ssh -p 8022 ykla@localhost
```

即可通过端口 8022（由文件 `qemu.bat` 指定）以 SSH 连接至本机的 ykla 用户。

## 故障排除与未竟事宜

### 无法显示图形界面

当前版本尚不支持图形界面，相关内容有待补充。

## 参考文献

- zg. Create FreeBSD virtual machine using qemu. Run the VM using xhyve.[EB/OL]. [2026-03-26]. <https://gist.github.com/zg/38a3afa112ddf7de4912aafc249ec82f>. 提供了 QEMU 下 FreeBSD 虚拟机扩容的技术方法。
- Nativus. 在 QEMU for Windows x64 上搭建 RISC-V 环境（Debian Linux）[EB/OL]. (2022-10-12)[2026-03-26]. <https://naiv.fun/Ops/83.html>. 提供了 RISC-V 环境搭建的概念解释与整体框架。
- smist08. RISC-V Emulation Revisited[EB/OL]. (2023-04-28)[2026-03-26]. <https://smist08.wordpress.com/2023/04/28/risc-v-emulation-revisited>. 详细介绍了 QEMU 中 RISC-V 虚拟化的各种配置参数与实现细节。
