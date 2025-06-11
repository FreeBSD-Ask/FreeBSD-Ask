# 第 6.4 节 触摸板

在默认情况下 FreeBSD 支持 i2c 和 USB 触摸板。

## 关闭触摸板

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

## Apple Magic Trackpad

Apple Magic Trackpad 是一个触摸板系列，因压感带来的舒适操作体验而闻名。FreeBSD 支持苹果妙控板，但需要加载 `bcm5974` 内核模块。

```sh
kldload bcm5974
```

可以在 `rc.conf` 中永久化这一配置：

```
sysrc kld_list+="bcm5974"
```

该触摸板需要配合 `libinput` 使用，在加载内核模块之后，通常 Wayland 桌面环境可以开箱即用。目前暂不支持蓝牙功能。

### 参考文献

- [FreeBSD タッチパッドを off にする](https://qiita.com/fygar256/items/35100d43b096470631d6)

## Fn 键设置


- [Adjusting acpi_video brightness increments on FreeBSD](https://www.davidschlachter.com/misc/freebsd-acpi_video-thinkpad-display-brightness)
