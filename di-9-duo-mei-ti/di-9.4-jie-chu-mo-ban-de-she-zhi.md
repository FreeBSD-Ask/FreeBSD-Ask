# 9.4 触摸板与键鼠

在默认情况下 FreeBSD 支持 i2c 和 USB 触摸板。

## 触摸板

### 关闭触摸板

查找触摸板：

```sh
ykla@ykla-mi:~ $ xinput list
⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
⎜   ↳ Windows pointer                         	id=6	[slave  pointer  (2)]
⎣ Virtual core keyboard                   	id=3	[master keyboard (2)]
    ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
    ↳ Windows keyboard                        	id=7	[slave  keyboard (3)]
```

可以看到 `6` 是触摸板，关闭：（最后 `1` 为开启；`0` 关闭）

```sh
ykla@ykla-mi:~ $ xinput set-prop 6 "Device Enabled" 0
```

#### 参考文献

- [FreeBSD タッチパッドを off にする](https://qiita.com/fygar256/items/35100d43b096470631d6)

### Apple Magic Trackpad

Apple Magic Trackpad 触摸板系列，因压感带来的舒适操作体验而闻名。FreeBSD 支持苹果妙控板，但需要加载 `bcm5974` 内核模块。

```sh
kldload bcm5974
```

可以在 `rc.conf` 中永久化这一配置：

```
sysrc kld_list+="bcm5974"
```

该触摸板需要配合 `libinput` 使用，在加载内核模块之后，通常 Wayland 桌面环境可以开箱即用。目前暂不支持蓝牙功能。

## 附录：解决 15.0 及更高版本键鼠无法驱动

如果你的 USB 键鼠或触摸板在 15.0 以下的旧版本中均正常。更新到 15.0 后发生故障，可参考下文：

在 `/boot/loader.conf` 或 `/boot/loader.conf.local` 中加入如下一行：

```ini
hw.usb.usbhid.enable="0"
```

随后重启即可。

问题分析：ums 在机器无关的内核里始终存在，usbhid 现在位于 amd64 机器相关内核选项里。15.0 后 usbhid 驱动成为默认，优先级高于传统的 ums 驱动。但都是编译进内核的不是模块。usbhid 引入内核自 [conf: Add hkbd and hms to GENERIC* kernel configs](https://reviews.freebsd.org/D45658)，替代 ums 发生在 [Enable usbhid by default](https://reviews.freebsd.org/D45659)。最早出现在 13.0，从 15.0 成为默认。**此问题仍需读者进一步研究原因并提出 Bug 到 FreeBSD 项目，因为项目计划日后彻底移除 ums 支持。** 具体参见 FreeBSD 期刊 2021/0708 号。

## 附录：Fn 键设置

- [Adjusting acpi_video brightness increments on FreeBSD](https://www.davidschlachter.com/misc/freebsd-acpi_video-thinkpad-display-brightness)
