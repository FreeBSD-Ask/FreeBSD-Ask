# 5.8 设备资源提示文件（device.hints）

设备资源提示文件（device.hints）是 FreeBSD 引导过程中的关键配置文件。该文件在系统启动时由 boot loader(8) 读取，其内容传递给内核，用于控制内核的引导行为，但也可包含任何内核可调参数值。设备提示变量主要用于设备驱动程序设置设备，最常用于 ISA 设备驱动程序指定探测位置和所需资源。

## device.hints 的功能与结构

[device.hints(5)](https://man.freebsd.org/cgi/man.cgi?device.hints) 相关文件结构：

```sh
/
├── boot/ 操作系统引导过程中使用的程序和配置文件
│    └── device.hints 设备资源提示文件
└── sys/
     └── ARCH/ 某架构，具体参见内核
          └── conf/ 内核配置相关文件
               ├── GENERIC.hints GENERIC 内核的设备资源提示示例
               └── NOTES 关于内核配置文件和设备资源提示的说明
```

根据源代码分析，[sys/amd64/conf/GENERIC.hints](https://github.com/freebsd/freebsd-src/blob/main/sys/amd64/conf/GENERIC.hints) 即为 amd64 架构默认的 device.hints 文件。

该文件的默认内容根据架构的不同而变化，其每条格式为（`#` 代表注释）：

```ini
hint.设备驱动名称.单元编号.关键字="值"
```

为驱动的某单元编号设备实例指定资源或属性。

```ini
# 下面的驱动大多数已经被现代计算机所淘汰，或在个人 PC 上较为罕见

# AT 键盘控制器驱动 atkbdc(4) AT 机，1980 年代产物
hint.atkbdc.0.at="isa"  # at：指定设备所连接的总线
hint.atkbdc.0.port="0x060"  # port：即指定设备将使用的 I/O Port 起始地址
hint.atkbd.0.at="atkbdc"
hint.atkbd.0.irq="1"  # irq：要使用的中断线路编号

# PS/2 外设 IBM 兼容鼠标驱动 psm(4)，1980 年代产物

#isa
# └── atkbdc0
#       ├── atkbd0
#       └── psm0

hint.psm.0.at="atkbdc"
hint.psm.0.irq="12"

# syscons(4) 传统控制台驱动
hint.sc.0.at="isa"
hint.sc.0.flags="0x100"  # flags：为设备设置标志位

# 串口驱动 uart(4)
hint.uart.0.at="acpi"  # 即设置 COM1
hint.uart.0.port="0x3F8"
hint.uart.0.flags="0x10"
hint.uart.1.at="acpi"  # 即设置 COM2
hint.uart.1.port="0x2F8"

# RTC 驱动（实时时钟 atrtc(4)）
hint.atrtc.0.at="isa"
hint.atrtc.0.port="0x70"
hint.atrtc.0.irq="8"

# i8254 可编程间隔定时器（AT 定时器）驱动 attimer(4)
hint.attimer.0.at="isa"
hint.attimer.0.port="0x40"
hint.attimer.0.irq="0"

# 禁用 ACPI CPU throttle 驱动，参见 cpufreq(4)
hint.acpi_throttle.0.disabled="1"  # disabled：设置为 “1” 意味着禁用该设备

# 禁用 Pentium 4 热控制，参见 cpufreq(4)
hint.p4tcc.0.disabled="1"
```

文件版本：[amd64 GENERIC: Switch uart hints from "isa" to "acpi"](https://github.com/freebsd/freebsd-src/commit/9cc06bf7aa2846c35483de567779bb8afc289f53)

解释：

```sh
hint.atkbdc.0.at="isa"
```

将驱动 [atkbdc](https://man.freebsd.org/cgi/man.cgi?query=atkbdc&sektion=4)（AT 键盘控制器）的设备实例号 0 附加（attach）到 ISA 总线上，即指定第 0 个 atkbdc 设备位于 ISA 总线上。

## 参考文献

- FreeBSD Project. device.hints(5)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=device.hints&sektion=5>. 设备资源提示文件手册页。
- FreeBSD Project. loader(8)[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=loader&sektion=8>. 系统引导加载程序手册页。
- FreeBSD Project. atkbdc -- AT keyboard controller driver[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=atkbdc&sektion=4>. AT 键盘控制器驱动手册页。

## 课后习题

1. 查找并分析 device.hints 中某个已禁用设备（如 hint.acpi_throttle.0.disabled）的源代码实现。

2. 创建一个自定义 device.hints 文件，为某个虚拟设备设置资源提示，验证其是否被内核正确读取。

3. 对比 device.hints 文件和 loader.conf 文件中内核可调参数的加载时机差异，尝试在两个文件中设置同一参数并观察哪个生效。
