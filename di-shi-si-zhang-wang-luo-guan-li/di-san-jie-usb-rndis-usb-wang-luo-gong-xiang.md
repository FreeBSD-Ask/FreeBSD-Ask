# 第九节 USB RNDIS (USB 网络共享)

该教程在小米手机上测试通过，理论上同时支持 Android 和 IOS。

首先加载内核模块：

```
# kldload if_urndis #安卓 Android 
# kldload if_ipheth #苹果 IOS
# kldload if_cdce   #其他设备
```

启动时开机加载：写入到

```
if_urndis_load="YES"
if_cdce_load="YES"
if_ipheth_load="YES"
```
