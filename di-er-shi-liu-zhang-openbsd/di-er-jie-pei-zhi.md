# 第二节 配置

##  初次登录

### 获取驱动

第一次进入系统后，OpenBSD 会自动检测无线、显卡和声卡，并下载相关驱动。静等几分钟，待其自行更新。由于国外网站连接比较慢，如果等待时间过长，可 `Ctrl` + `C` 取消，待进入系统后运行 `# fw_update` 重新获取驱动。

新版 7.1 出现了变动，下载驱动时会遇到超时错误（GFW）。如此则在运行`fw_update` 后，记住获取失败的驱动名，而后直接访问[官方驱动站](http://firmware.openbsd.org/firmware/7.1/)来手动获取。解压驱动包，将内部驱动文件复制到`/etc/firmware/`文件夹内，之后重启。

如`inteldrm-firmware-xxx.tgz`为 intel 的显卡驱动，解压该驱动后，发现驱动 firmware 目录下有 i915 的目录。可执行以下操作（操作需要权限）：

```
cd /etc/firmware/
mkdir i915
cp -r /$PATH/inteldrm-firmware-xxx/firmware/i915/* /etc/firmware/i915/
```

同理`amdgpu-firmware-xxx.tgz`为 amd 的显卡驱动，解压该驱动后，发现驱动 firmware 目录下有 amdgpu 的目录。可执行以下操作（操作需要权限）：

```
cd /etc/firmware/
mkdir amdgpu
cp -r /$PATH/amdgpu-firmware-xxx/firmware/amdgpu/* /etc/firmware/amdgpu/
```
其它驱动与此类同。

### 桌面支持(新版请忽略此项)

旧版本安装时，可能会遇到是否启用 X 的选项。若是不小心屏蔽了，我们可以重新开启。打开 `/etc/sysctl.conf`，添加一行 `machdep.allowaperture=2` 。

### 修改软件源

打开 `/etc/installurl` ，将默认源注释掉，改为 `https://mirrors.bfsu.edu.cn/OpenBSD` 。此处我们选择了北外源，用户也可选择 [清华镜像源](https://mirrors.tuna.tsinghua.edu.cn/OpenBSD)、 [阿里镜像源](https://mirrors.aliyun.com/openbsd)、 及[南京大学源](https://mirror.sjtu.edu.cn/OpenBSD) 等。

## 系统更新

### 普通账号获取权限

以 root 账号登录系统，而后新建 `/etc/doas.conf` 文本，打开`doas.conf`，添加一行 `permit persist :wheel`

### 内核更新

内核更新：`# syspatch`

驱动升级：`# fw_update`

软件升级：`# pkg_add -u`

修改shell： `chsh`
 
示例：`# chsh -s /usr/local/bin/bash $USER`

## 软件管理

- 查找软件： `# pkg_info -Q foo`

- 安装软件： `# pkg_add foo`

- 升级软件： `# pkg_add -iu foo`


## 挂载可移动磁盘

### 新建挂载点

```
$ cd ~
$ mkdir media
$ cd media
# mkdir usb1 usb2 usb3 usb4
```
### 查看盘符

使用 `dmesg` 命令来查看新插入的盘符，如格式为 fat32 的 U盘，可能在 OpenBSD 系统里盘符为 `sd1` 。

### 检查分区

如插入的盘符为 `sd1`，则输入 `disklabel sd1` 查看分区情况。如下

```
#                size           offset  fstype [fsize bsize   cpg]
 c:         60062500                0  unused                    
 i:         60062244              256   MSDOS    
```

### 挂载

由上则可知分区为 `i` ，使用以下命令挂载：

`# mount /dev/sd1i /$USER/media/usb1` ，`$USER` 替换为当前用户名。

### 其它格式

OpenBSD 可挂载的外接硬盘格式有 NTFS（需要安装软件包`ntfs_3g`）、ext2/ext3 以及 CD 磁盘等，具体命令可参考如下：

```
# mount /dev/sd3i /$USER/media/usb1   # fat32
# mount_ntfs /dev/sd2k /$USER/media/usb2  # NTFS
# mount /dev/sd1l /$USER/media/usb3   # ext2/ext3
# mount /dev/cd0a /$USER/media/usb4   # CD
```

### 卸载磁盘

`# umount /$USER/media/usb1`

## 无线测试

OpenBSD 里的无线网络，配置文件通常是 `hostname.if` ，其中 `if` 为无线驱动名称+序号。如一台笔记本无线型号为 rtl8188cu ，OpenBSD 下驱动为 rtwn ，序号从 0 开始。为了让系统自动加载无线，可打开 `/etc/hostname.rtwn0` 文件 ，而后添加：

```
dhcp 
join 无线名称 wpakey 无线密码
```
保存后即可。

## 补遗

### 加载触摸板

打开 `/etc/wsconsctl.conf`， 添加一行 `mouse.tp.tapping=1` 。

### 加载多线程

打开 `/etc/sysctl.conf`，添加一行 `hw.smt=1` 。

### 相关资料

- OpenBSD FAQ  推荐

- Absolute OpenBSD 补充

_如果觉得 Firefox 运行缓慢，试试 Epiphany (Gnome 浏览器) 。_
