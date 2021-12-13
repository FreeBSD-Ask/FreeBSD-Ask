# 第二节 配置

## 1. 准备工作

### 获取驱动

第一次进入系统后，OpenBSD 会自动检测无线、显卡和声卡，并下载相关驱动。静等几分钟，待其自行更新。由于国外网站连接比较慢，如果等待时间过长，可 `Ctrl` + `C` 取消待进入系统后运行 `fw_update` 重新获取驱动。

### 开启桌面支持

上一节安装时，我们屏蔽了桌面选项。这一步我们重新开启。打开 `/etc/sysctl.conf`，添加一行` machdep.allowaperture=2` 。

### 修改软件源

打开 `/etc/installurl` ，将默认源注释掉，改为 `https://mirrors.bfsu.edu.cn/OpenBSD` 。此处我们选择了北外源，用户也可选择 [清华镜像源](https://mirrors.tuna.tsinghua.edu.cn/OpenBSD)、 [阿里镜像源](https://mirrors.aliyun.com/openbsd)、 及[南京大学源](https://mirror.sjtu.edu.cn/OpenBSD) 等。

