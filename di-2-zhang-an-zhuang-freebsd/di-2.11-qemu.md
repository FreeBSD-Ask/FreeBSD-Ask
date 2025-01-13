# 第 2.11 节 Qemu 安装 RISC-V FreeBSD（基于 x86 Windows）

Qemu 是一款纯软件模拟的开源虚拟机，支持模拟不同的体系结构。

## 下载软件与镜像

本文基于 Windows 11 24H2（物理机）X86-64，FreeBSD 14.2 RELEASE RISC-V（虚拟机），qemu 20241220。

### Qemu 

Qemu 下载地址：

[QEMU Binaries for Windows (64 bit)](https://qemu.weilnetz.de/w64/)，点击最下方倒数第二个文件即可。写作文本时，为 `qemu-w64-setup-20241220.exe`。大小为 174M。

下载后在 Windows 上安装 Qemu。

### RISC-V FreeBSD 磁盘镜像

RISC-V FreeBSD 磁盘镜像（以 FreeBSD 14.2 RELEASE 为例）：

<https://download.freebsd.org/releases/VM-IMAGES/14.2-RELEASE/riscv64/Latest/FreeBSD-14.2-RELEASE-riscv-riscv64-zfs.raw.xz>

下载后解压缩备用。

### OpenSBI

获取 OpenSBI（RISC-V Open Source Supervisor Binary Interface），类似于 BIOS：

安装 OpenSBI：

```sh
# pkg install opensbi
```

或者：

```sh
# cd /usr/ports/sysutils/opensbi/ 
# make install clean
```

看看 `fw_jump.elf` 在哪：

```sh
# /etc/periodic/weekly/310.locate # 刷新数据库
# locate fw_jump.elf
/usr/local/share/opensbi/lp64/generic/firmware/fw_jump.elf
```

提取 `fw_jump.elf` 到 Windows 下备用。

### U-Boot

获取 U-Boot，类似于 Grub2：

安装：

```sh
# pkg install u-boot-qemu-riscv64
```

或者：

```sh
# cd /usr/ports/sysutils/u-boot-qemu-riscv64/ 
# make install clean
```

查看 `u-boot` 位置：

```sh
# /etc/periodic/weekly/310.locate # 刷新数据库
# locate u-boot.bin
root@ykla:/home/ykla # locate u-boot.bin
/usr/local/share/u-boot/u-boot-qemu-riscv64/u-boot.bin
```

提取 `u-boot.bin` 到 Windows 下备用。

## 配置 Qemu

在桌面新建一个文本文件 `qemu.bat`，

写入

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
    -append “root=LABEL=rootfs” ^
    -nographic
```

概述：

- `^` 相当于 Windows 下的反斜杠。
- `smp` 为 CPU 数量
- `cpu` 指定 CPU 架构
- `m` 指定内存大小

以上，请将 `C:\Users\ykla\Desktop\` 替换为你自己的路径。

运行脚本即可。

![Qemu 安装 FreeBSD](../.gitbook/assets/qemu1.png)

输入用户名 `root` 回车即可，默认没有密码。

## 故障排除

- 在 PowerShell 和 CMD 中运行都会产生各种乱码（比如 `ee` 命令，或按 **TAB 键**）。

待解决

- 图形化无法显示

待解决

## 参考文献

- [Create FreeBSD virtual machine using qemu. Run the VM using xhyve.](https://gist.github.com/zg/38a3afa112ddf7de4912aafc249ec82f)，有一些扩容方法
- [在 QEMU for Windows x64 上搭建 RISC-V 环境（Debian Linux）](https://naiv.fun/Ops/83.html)，有一些概念解释和整体框架
- [RISC-V Emulation Revisited](https://smist08.wordpress.com/2023/04/28/risc-v-emulation-revisited/)，各种参数来自此处。