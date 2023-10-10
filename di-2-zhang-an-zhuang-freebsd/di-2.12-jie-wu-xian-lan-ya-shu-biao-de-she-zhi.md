# 第 2.12 节 无线蓝牙鼠标的设置

> 本文基于 FreeBSD 13.0，并使用罗技 m337。

```shell-session
# sysrc hcsecd_enable="YES"
# sysrc bthidd_enable="YES"
# service hcsecd start
# service bthidd start
```

使用`bluetooth-config`工具添加蓝牙设备即可。

蓝牙鼠标调到配对模式，运行`# bluetooth-config scan`，按提示信息进行添加：

```shell-session
#  bluetooth-config scan
Scanning for new Bluetooth devices (Attempt 1 of 5) ... done.
Found 1 new bluetooth device (now scanning for names):
[ 1] 34:88:5d:12:34:56  "Bluetooth Mouse M336/M337/M535" (Logitech-M337)
Select device to pair with [1, or 0 to rescan]: 1

This device provides human interface device services.
Set it up? [yes]:
```

> 注意： logitech m337 配对连接后会自动断开。解决方案：删除`/var/db/bthidd.hids`文件中对应鼠标的`bd_addr`行`xx:xx:xx:xx:xx`，重启 bthidd 服务 `# service bthidd restart`
