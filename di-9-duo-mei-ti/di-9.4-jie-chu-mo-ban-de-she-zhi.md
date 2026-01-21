# 9.4 触摸板与键盘鼠标

在默认情况下，FreeBSD 支持 I²C 和 USB 触摸板。

## 触摸板

### 关闭触摸板

查找触摸板：

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

Apple Magic Trackpad 触摸板系列因压感带来的舒适操作体验而闻名。

FreeBSD 支持苹果妙控板，但需要加载 `bcm5974` 内核模块才能正常使用：

```sh
# kldload bcm5974
```

如果测试妙控板可以正常使用，那么接下来将内核模块 `bcm5974` 加入开机加载列表：

```sh
# sysrc kld_list+="bcm5974"
```

该触摸板需要配合 `libinput` 使用，在加载内核模块之后，通常在 Wayland 桌面环境下可以开箱即用。目前暂不支持通过蓝牙方式使用。

## 附录：解决 15.0 及更高版本中键鼠无法驱动的问题

如果你的 USB 键鼠或触摸板在 15.0 以下的旧版本中工作正常，但在更新到 15.0 后发生故障，可以参考下文：

在 `/boot/loader.conf` 或 `/boot/loader.conf.local` 中加入如下一行：

```ini
hw.usb.usbhid.enable="0"
```

禁用 USB HID 设备，随后重启即可。

问题分析：ums 驱动始终存在于与具体机器无关的内核中，而 usbhid 目前位于 amd64 架构相关的内核选项中。在 15.0 之后，usbhid 驱动成为默认，其优先级高于传统的 ums 驱动。但两者均为直接编译进内核的驱动，而非以模块形式加载。usbhid 驱动引入内核始于 [conf: Add hkbd and hms to GENERIC\* kernel configs](https://reviews.freebsd.org/D45658) [备份](https://web.archive.org/web/20260120211221/https://reviews.freebsd.org/D45658)，而替代 ums 的过程发生在 [Enable usbhid by default](https://reviews.freebsd.org/D45659) [备份](https://web.archive.org/web/20260120211156/https://reviews.freebsd.org/D45659)。该变更最早出现在 13.0 版本，并从 15.0 起成为默认行为。此问题仍需读者进一步研究原因，并向 FreeBSD 项目提交 Bug 报告，因为项目计划在日后彻底移除 ums 支持。具体可参见 FreeBSD 期刊 2021/0708 期。

## 附录：Fn 键设置

- [Adjusting acpi_video brightness increments on FreeBSD](https://www.davidschlachter.com/misc/freebsd-acpi_video-thinkpad-display-brightness) [备份](https://web.archive.org/web/20260120211035/https://www.davidschlachter.com/misc/freebsd-acpi_video-thinkpad-display-brightness)
