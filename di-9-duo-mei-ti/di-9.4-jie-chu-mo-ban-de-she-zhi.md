# 9.4 人机输入设备

在默认情况下，FreeBSD 操作系统原生支持 I²C（Inter-Integrated Circuit，集成电路总线）和 USB（Universal Serial Bus，通用串行总线）接口的触摸板。本章将介绍触摸板的相关配置方法与技术细节。

## 触摸板

### 关闭触摸板

要关闭触摸板功能，首先需要查找触摸板在 X Window 系统中的设备标识：

```sh
$ xinput list
⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
⎜   ↳ Windows pointer                         	id=6	[slave  pointer  (2)]
⎣ Virtual core keyboard                   	id=3	[master keyboard (2)]
    ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
    ↳ Windows keyboard                        	id=7	[slave  keyboard (3)]
```

可以看到，`6` 是触摸板，关闭方式如下（其中 `1` 表示开启，`0` 表示关闭）：

```sh
$ xinput set-prop 6 "Device Enabled" 0    # 禁用 ID 为 6 的输入设备
```

#### 参考文献

- [FreeBSD タッチパッドを off にする](https://qiita.com/fygar256/items/35100d43b096470631d6) [备份](https://web.archive.org/web/20260120211042/https://qiita.com/fygar256/items/35100d43b096470631d6)

### Apple Magic Trackpad

Apple Magic Trackpad（苹果妙控板）触摸板系列因其压力感应技术带来的精确舒适操作体验而闻名。

FreeBSD 操作系统支持苹果妙控板硬件，但需要加载 `bcm5974` 内核模块才能正常启用其功能：

```sh
# kldload bcm5974
```

如果测试妙控板可以正常使用，那么接下来将内核模块 `bcm5974` 加入系统开机自动加载列表，以确保每次启动后都能自动加载该驱动：

```sh
# sysrc kld_list+="bcm5974"
```

该触摸板需要配合 `libinput` 输入库使用，在加载内核模块之后，通常在 Wayland 桌面环境下可以开箱即用。目前暂不支持通过蓝牙无线方式使用。

## 附录：解决 15.0 及更高版本中键鼠无法驱动的问题

如果你的 USB 键盘、鼠标或触摸板在 15.0 以下的旧版本中工作正常，但在系统更新到 15.0 后发生驱动故障，可以参考以下解决方案：

在系统启动配置文件 `/boot/loader.conf` 或 `/boot/loader.conf.local` 中加入如下一行配置：

```ini
hw.usb.usbhid.enable="0"
```

该配置将禁用 USB HID 设备驱动，随后重启系统即可。

问题分析：ums（USB Mouse/Keyboard）驱动始终存在于与具体硬件架构无关的通用内核中，而 usbhid 驱动目前位于 amd64 架构相关的内核选项中。在 15.0 版本之后，usbhid 驱动成为默认选择，其优先级高于传统的 ums 驱动。需要注意的是，两者均为直接编译进内核的驱动，而非以可加载模块形式存在。usbhid 驱动引入内核的过程始于 [conf: Add hkbd and hms to GENERIC\* kernel configs](https://reviews.freebsd.org/D45658) [备份](https://web.archive.org/web/20260120211221/https://reviews.freebsd.org/D45658)，而替代 ums 作为默认驱动的变更发生在 [Enable usbhid by default](https://reviews.freebsd.org/D45659) [备份](https://web.archive.org/web/20260120211156/https://reviews.freebsd.org/D45659)。该变更最早出现在 13.0 版本，并从 15.0 起成为系统默认行为。此问题仍需读者进一步研究其根本原因，并向 FreeBSD 项目提交 Bug 报告，因为项目计划在未来版本中彻底移除 ums 驱动支持。具体可参见 FreeBSD 期刊 2021/0708 期的相关报道。

## 附录：Fn 键设置

- [Adjusting acpi_video brightness increments on FreeBSD](https://www.davidschlachter.com/misc/freebsd-acpi_video-thinkpad-display-brightness) [备份](https://web.archive.org/web/20260120211035/https://www.davidschlachter.com/misc/freebsd-acpi_video-thinkpad-display-brightness)
