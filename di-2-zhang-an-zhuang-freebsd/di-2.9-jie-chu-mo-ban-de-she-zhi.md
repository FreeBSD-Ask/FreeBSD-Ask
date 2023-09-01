# 第 2.9 节 触摸板的设置

默认情况下支持 i2c 和 USB 触摸板。

## 关闭触摸板

查找触摸板：

```shell-session
ykla@ykla-mi:~ $ xinput list
⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
⎜   ↳ Windows pointer                         	id=6	[slave  pointer  (2)]
⎣ Virtual core keyboard                   	id=3	[master keyboard (2)]
    ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
    ↳ Windows keyboard                        	id=7	[slave  keyboard (3)]
```

可以看到 `6` 是触摸板，关闭：（最后 1 为开启）

```shell-session
ykla@ykla-mi:~ $ xinput set-prop 6 "Device Enabled" 0
```

参考文献：

- [FreeBSDタッチパッドをoffにする](https://qiita.com/fygar256/items/35100d43b096470631d6)

