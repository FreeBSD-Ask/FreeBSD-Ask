# 第 2.10 节 FreeBSD 硬件选择

## 怎么看我的硬件支持不支持呢？

更多硬件请参考：

[Hardware for BSD](https://bsd-hardware.info/?view=search)

<figure><img src="../.gitbook/assets/h1.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/h2.png" alt=""><figcaption></figcaption></figure>

> 如果你也想上传你的数据到该网站上，请：
>
> ```shell-session
> # pkg install hw-probe
> # hw-probe -all -upload
> ```
>
> 其他系统见 [INSTALL HOWTO FOR BSD](https://github.com/linuxhw/hw-probe/blob/master/INSTALL.BSD.md)


## 归档内容

* 联想 G400 ：处理器 i3-3110M/i5-3230M、显卡 HD4000、WIFI intel N135（联想 G400 网卡白名单支持三种网卡，如果是博通 BCM43142 建议更换为 N135，FUR 料号：04W3783，如果更换后提示不能读取，请先在 BIOS 里停用无线网卡，升级 BIOS 后恢复即可）。

**故障排除：**

Q：联想笔记本无电池如何升级 BIOS？

A：如果找不到电池，请解压缩`78cn25ww.exe`文件（BIOS 文件请自行去联想美国官网获取），用记事本打开`platform.ini`，查找：

```shell-session
[AC_Adapter]
Flag=1
BatteryCheck=1
BatteryBound=30
```

将以上所有数值都修改为`0`：

```shell-session
[AC_Adapter]
Flag=0
BatteryCheck=0
BatteryBound=0
```

保存后，双击`InsydeFlash.exe`即可。

**如果断电，后果自负**

