# 第三节 磁盘扩容

### 扩容方法

1、gpart show
```
# gpart show
=> 63 209715137 vtbd0 MBR (100G)
63 1 - free - (512B)
64 62914496 **1** freebsd [active] (30G)
62914560 146800640 - free - (70G)
```
查看系统盘大小只有 30G，显示 1 只有这一个盘。

2、执行扩容命令，vtbd0 从 gpart show 执行后查看
```
# gpart resize -i 1 vtbd0
vtbd0s1 resized
```

3、启动 growfs 服务，自动完成扩展
```
# service growfs onestart

Growing root partition to fill device
vtbd0s1 resized
gpart: arg0 'ufsid/62b5826d': Invalid argument
super-block backups (for fsck_ffs -b #) at:
64112192 65394432 66676672 67958912 69241152 70523392
```
4、用 df -h 命令查看结果。
```
# df -h
Filesystem Size Used Avail Capacity Mounted on
/dev/ufsid/62b5826d 97G 15G 75G 16% /
devfs 1.0K 1.0K 0B 100% /dev
```
