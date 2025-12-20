# 3.2 使用 VMware Workstation Pro 安装 FreeBSD


## 视频教程

- [001-Windows 11 安装 VMware 17](https://www.bilibili.com/video/BV1Qji2YLEgS)

## 镜像下载

>**提示**
>
>虚拟机也可以使用 FreeBSD 官方构建的 [虚拟机镜像](https://download.freebsd.org/releases/VM-IMAGES/14.2-RELEASE/amd64/Latest/)，需要手动扩容，文件系统可选 UFS 与 ZFS。
>
>虚拟机一般使用 `FreeBSD-14.2-RELEASE-amd64-disc1.iso` 等类似文件名和后缀的镜像，但是，`FreeBSD-14.2-RELEASE-amd64-memstick.img` 也并非只能用于 U 盘刻录，虚拟机也是可以用的，使用方法参考第 31.2 节。


## 配置虚拟机



![VMware 安装 FreeBSD](../.gitbook/assets/vm1.png)


![VMware 安装 FreeBSD](../.gitbook/assets/vm2.png)

![VMware 安装 FreeBSD](../.gitbook/assets/vm3.png)

请务必选择“稍后安装操作系统”，否则启动会出问题。

![VMware 安装 FreeBSD](../.gitbook/assets/vm4.png)

请选择“其他”，然后选择 FreeBSD。

>**技巧**
>
>这一步其实无意义。甚至选择 Windows 也能顺利启动。但是对于低版本的 FreeBSD，虚拟机增强工具没有开源，可能会出问题。

![VMware 安装 FreeBSD](../.gitbook/assets/vm5.png)

虚拟机占用磁盘空间极大。若你不想 C 盘被占满，请自行调整存储位置。

![VMware 安装 FreeBSD](../.gitbook/assets/vm6.png)

请调整最大磁盘大小。默认值不合理。若要安装桌面，最小要大于 20 G。

![VMware 安装 FreeBSD](../.gitbook/assets/vm7.png)

![VMware 安装 FreeBSD](../.gitbook/assets/vm8.png)

![VMware 安装 FreeBSD](../.gitbook/assets/vm9.png)

默认值 256 M 能够启动。但是不建议这么做。实在不行给 512 M 也行。

![VMware 安装 FreeBSD](../.gitbook/assets/vm10.png)

默认值 1 CPU 能够启动。但是不合理。

![VMware 安装 FreeBSD](../.gitbook/assets/vm11.png)

在“使用 ISO 映像文件”中，点击浏览找到，并选中你下载的 `-RELEASE-amd64-disc1.iso` 文件。

![VMware 安装 FreeBSD](../.gitbook/assets/vm12.png)


>**技巧**
>
> 经过测试，FreeBSD 也可以支持驱动 UEFI 下 VMware 的显卡。——2025.3.24


> **警告**
>
> 由于 [Bug 250580 - VMware UEFI guests crash in virtual hardware after r366691](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=250580)，FreeBSD 11/12 在 VMware 的 UEFI 环境下可能无法启动。经测试 13.0 正常启动。



![VMware 安装 FreeBSD](../.gitbook/assets/vm13.png)

![VMware 安装 FreeBSD](../.gitbook/assets/vm14.png)

![VMware 安装 FreeBSD](../.gitbook/assets/vm15.png)


## 网络设置

请使用 NAT 模式（默认），如果不能与宿主机（物理机）互通，请打开 VMware 编辑 - 虚拟网络管理器，“还原默认设置”，直至出现类似下图的配置：

>**注意**
>
>经过测试，桥接的虚拟机在与主机传递文件时，网速极慢。

>**技巧**
>
>如果“还原默认设置”不起作用，始终只有单个某模式，请按照下图手动配置。

>**警告**
>
>NAT 模式“名称”是与你主机的 `控制面板\网络和 Internet\网络连接` 中的 `VMware Network Adapter VMnet8` 绑定的，默认绑定的是 `8`：换言之，`NAT 模式` “名称”默认必须指定为下图的 `VMnet8`，指定为其他名称虚拟机不会有网络！
>
>![vmware network on freebsd](../.gitbook/assets/VMnat8.png)


![vmware network on freebsd](../.gitbook/assets/net1.png)

以上请不要手动设置，如果虚拟机内部一直提示 `no link`，请重启物理机，再打开虚拟机：VMware 编辑 - 虚拟网络管理器，“还原默认设置”，直至出现上述配置。（请不要尝试手动配置，那是无效的）

如果没有网络请设置 DNS 为 `223.5.5.5`。请看本章其余章节。

如果配置桥接后始终无法 DHCP 到 IP，可尝试手动将“已桥接至 自动”改为你当前使用的网卡。

![vmware network on freebsd](../.gitbook/assets/net2.png)

## 虚拟机增强工具与显卡驱动

安装显卡驱动和虚拟机增强工具，即：

```sh
# pkg install xf86-video-vmware open-vm-tools xf86-input-vmmouse open-vm-kmod
```

或者

```sh
# cd /usr/ports/x11-drivers/xf86-video-vmware/  && make install clean
# cd /usr/ports/emulators/open-vm-tools/ && make install clean
# cd /usr/ports/x11-drivers/xf86-input-vmmouse/  && make install clean
# cd /usr/ports/emulators/open-vm-kmod/ && make install clean
```

>**注意**
>
>若你不使用桌面还可以这样（仍然是 Port `emulators/open-vm-tools`）：
>
>```sh
># pkg install open-vm-tools-nox11
>```

安装完毕后无需任何多余配置即可实现屏幕自动缩放。

>**注意**
>
>Wayland 下也需要安装该驱动。

>**技巧**
>
> 如果屏幕显示不正常（过大），请尝试：编辑虚拟机设置——> 硬件、设备——> 显示器——> 监视器、指定监视器设置——> 任意监视器的最大分辨率，设置为主机的分辨率或者略低于主机分辨率均可。


### 鼠标集成（主机虚拟机鼠标自由切换）

请先安装显卡驱动和虚拟机增强工具。

```sh
# service moused enable
# Xorg -configure
# mv /root/xorg.conf.new /usr/local/share/X11/xorg.conf.d/xorg.conf
```

编辑 `/usr/local/share/X11/xorg.conf.d/xorg.conf` 修改以下段落为（其他部分不需要动，保留原样即可）：

```ini
Section "ServerLayout"
        Identifier     "X.org Configured"
        Screen          0  "Screen0" 0 0
        InputDevice    "Mouse0" "CorePointer"
        InputDevice    "Keyboard0" "CoreKeyboard"
        Option          "AutoAddDevices" "Off"  # 添加此行到此处
EndSection

…………此处省略一部分…………

Section "InputDevice"
      Identifier  "Mouse0"
      Driver      "vmmouse"  # 修改 mouse 为 vmmouse
      Option      "Protocol" "auto"
      Option      "Device" "/dev/sysmouse"
      Option      "ZAxisMapping" "4 5 6 7"
EndSection

…………此处省略一部分…………
```

### 共享文件夹

请先安装虚拟机增强工具。

#### 在物理机设置共享文件夹

![FreeBSD VMware 共享文件夹](../.gitbook/assets/hgfs1.png)

>**注意**
>
>不必疑惑虚拟机的名字是 Windows 11，因为这是 Windows 11 和 BSD 双系统虚拟机。

在 FreeBSD 虚拟机中查看设置的文件夹：

```sh
# vmware-hgfsclient
123pan
```

#### 加载 fuse 模块

加载 fuse，将下文写入 `/boot/loader.conf`：

```sh
fusefs_load="YES"
```

#### 挂载

##### 手动挂载

>**注意**
>
>请将 `123pan` 换成你自己的路径。

```sh
# vmhgfs-fuse .host:/123pan /mnt/hgfs
```

##### 自动挂载

编辑 `/etc/fstab`：写入：

>**注意**
>
>请将 `123pan` 换成你自己的路径。

```sh
.host:/123pan      /mnt/hgfs    fusefs  rw,mountprog=/usr/local/bin/vmhgfs-fuse,allow_other,failok 0 0
```

检查（请务必执行，否则若写错了会卡在开机处）：

```sh
# mount -al # 若无输出则正常
```

#### 查看共享文件夹

```sh
# ls /mnt/hgfs/
Downloads
# ls /mnt/hgfs/Downloads/
零跑
```

![FreeBSD VMware 共享文件夹](../.gitbook/assets/hgfs2.png)

文件内容一致。

#### 参考文献

- [解决 vmware 上 Ubuntu 共享文件夹（2022 年 7 月）](https://www.cnblogs.com/MaRcOGO/p/16463460.html)，整体方法参考此处
- [fuse: failed to open fuse device](https://forums.freebsd.org/threads/fuse-failed-to-open-fuse-device.44544/)，解决 `fuse: failed to open fuse device: No such file or directory` 的问题
- [VMware shared folders](https://forums.freebsd.org/threads/vmware-shared-folders.10318/)，挂载方法参考此处


## 故障排除与未尽事宜

> **注意**
>
> 在使用 Windows 远程桌面或者其他 XRDP 工具远程另一台 Windows 桌面，并使用其上面运行的 VMware 虚拟机操作 FreeBSD 时，鼠标通常会变得难以控制。这是正常的！

- 每次进入图形界面，窗口都会异常扩大。

调整虚拟机的最大分辨率即可。

![VMware 安装 FreeBSD](../.gitbook/assets/vm16.png)

硬件——显示——监视器——任意监视器的最大分辨率 (M)，将其由默认最大的 `2560 x 1600`（2K）改成其他较小值即可，亦可自定义数值。

- 没有声音

加载声卡后若仍然没有声音，请将音量拉满到 100% 再看一下。因为默认声音几乎微不可闻。

## 附录：博通（Broadcom）账号相关

>**警告**
>
>博通官网频繁变动，无法始终提供一致的解决方案，请读者领会大意，自行操作，实在不会，请加入中文社区聊天群。

### 博通（broadcom）账号注册

VMware 已被博通收购。**故目前下载任何博通产品均须先注册、登录博通账号。** 目前任何非此域名（`broadcom.com`）教程均无效。

>**博通（broadcom）账号的注册流程**
>
>- 打开 <https://support.broadcom.com/>
>
> ![打开 <https://support.broadcom.com/>](../.gitbook/assets/Register.png)
>
>- 点击右上角的“Register”（注册）（或者直接打开 <https://profile.broadcom.com/web/registration>）
>>
>>在页面“Email Address”（电子邮件）处输入你的电子邮箱。如果没有的话，可以用你的 QQ 号，然后直接加上一个 `@qq.com`——比如你的 QQ 号是 `1212111111`，那么你的 QQ 邮箱则为 `1212111111@qq.com`
>>
>>在页面“Enter text from image”（输入图片上的文本）处输入图片上的文本信息（实际上是验证码）。如果看不清或者不认识，可以点 `Enter text from image` 右侧的 🔁
>>点击“Next”（继续）
>>
>>如果你使用的是 QQ 号生成的邮箱，请打开 <https://wx.mail.qq.com/>。其他邮箱请在各自网站打开，如果不知道，请使用 QQ 邮箱。
>
>![注册](../.gitbook/assets/Register2.png)
>
>- 把第五步得到的“Verification Code: 972980”，中的 972980（你的和我不一样，找你自己的）填到“Enter text from image”里面。
>
>![邮箱验证码](../.gitbook/assets/mail.png)
>
>- 点击“Verify & Continue”（确认并继续）
>
>![输入邮箱验证码](../.gitbook/assets/Verify.png)
>
>- 完成注册
>
>![完成注册](../.gitbook/assets/comreg.png)
>
>- 结束注册流程
>  
>![结束注册](../.gitbook/assets/dolater.png)


### 博通（broadcom）账号登录

>**博通（broadcom）账号登录流程**
>
>- 打开 <https://support.broadcom.com/>
>>
>>点击右上角的“Login”（登录）（或者直接打开 <https://support.broadcom.com/c/portal/login>）
>
>![登录](../.gitbook/assets/loginbcm.png)
>
>- Username（用户名）就是你注册时候的邮箱。然后点“Next”（下一步）
>
>![登录](../.gitbook/assets/loginbcm2.png)
>
>- 点击下一步
>
>![点击下一步](../.gitbook/assets/loginbcm3.png)
>
>- 点击登录
>
>![点击登录](../.gitbook/assets/loginbcm4.png)
>
>- 登录完成
>
>![登录后界面](../.gitbook/assets/afterlogin.png)

### VMware Workstation Pro 下载（推荐）

>**VMware Workstation Pro 下载流程**
>
>- 点击右上角对应图标（名字左侧第一个），选择“VMware Cloud Foundation”（VMware 云计算基础架构）
>  
>![](../.gitbook/assets/downbcm1.png)
>
>- 点击右侧的“My Downloads”（我的下载）
>
>![](../.gitbook/assets/downbcm0.png)
>
>- 往下翻，点击“VMware Workstation Pro“
>
>![点击“VMware Workstation Pro“](../.gitbook/assets/downbcm2.png)
>
>- 点击“Release”（发行版），选择最顶部的那个，你看到的不一定和我一样。
>
>![点击“Release”（发行版）](../.gitbook/assets/downbcm3.png)
>
>**或者跳过上述步骤，直接打开 <https://support.broadcom.com/group/ecx/free-downloads>**
>
>![下载主页](../.gitbook/assets/downbcm4.png)
>
>- 把红色的 `*` 项目填写完成，不会写的自己编，最好不要抄我的。
>  
>![补充信息](../.gitbook/assets/downbcm5.png)
>
>- 勾选“I agree to Terms and Conditions”（我同意条款及条件）左侧的方框 ⬜，让他变成 🟦。（必须先点击“Terms and Conditions”弹窗新页面，再回来就能勾选了）
>  
>![同意许可协议](../.gitbook/assets/downbcm6.png)
>
>- 点击右侧箭头的云朵图片 ☁️ 即可下载
>  
>![下载](../.gitbook/assets/downbcm7.png)


VMware Workstation Pro 目前对于个人用户来说是 **免费下载、免费使用、免费授权的。** **请勿从任何第三方站点下载。** 否则会造成一些未知的后果——90% 的问题都是由此产生的。


### 博通开源/社区产品

博通所有开源/社区产品都被整合到了这里进行下载。

如：Community Network Driver for ESXi、ESXi Arm Edition 等。

访问地址：<https://community.broadcom.com/flings/home>。目前任何非此域名教程（`community.broadcom.com`）均无效。

### VMware Workstation Player（已弃用，不要用）

VMware Workstation Player 目前已弃用。且功能相对 VMware Workstation Pro 非常有缺失。不建议使用，非要下载，请点击 <https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20Workstation%20Player>。目前所有包含该软件的教程均为旧教程。
