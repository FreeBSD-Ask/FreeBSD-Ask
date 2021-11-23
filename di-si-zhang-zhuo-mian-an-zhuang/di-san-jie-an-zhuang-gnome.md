# 第三节 安装 Gnome

#### ！注意：以下配置：使用英特尔核显+N卡！ <a href="zhu-yi-yi-xia-pei-zhi-shi-yong-ying-te-er-he-xiannka" id="zhu-yi-yi-xia-pei-zhi-shi-yong-ying-te-er-he-xiannka"></a>

## 1.依赖准备

`#pkg install -y xorg gnome3`

## 2.配置

\#ee /etc/fstab\
添加内容如下:\
`proc /proc procfs rw 0 0`

`#ee /etc/rc.conf`\
添加：
```
dbus_enable=”YES”
hald_enable=”YES”
gdm_enable=”YES”
gnome_enable=”YES”
cupsd_enable=”YES”
snd_hda=”YES”
moused_enable=”YES”
linux_enable=”YES”
kld_list=”/boot/modules/i915kms.ko”
```
输入以下指令（或者在.xinitrc文件加入“”内容）\
`% echo “/usr/local/bin/gnome-session” > ~/.xinitrc`

## 安装显卡驱动
```
#pkg install drm-fbsd12.0-kmod
#pkg install nvidia-driver
#ee /boot/loader.conf
#添加下面一行代码：
#nvidia_load=”YES”
```
## 中文化GNOME
```
#ee locale.conf 文件添加(/usr/local/etc/gdm/ 目录)添加以下内容
LANG=”zh_CN.UTF-8”
LC_CTYPE=”zh_CN.UTF-8”
LC_MESSAGES=”zh_CN.UTF-8”
LC_ALL=”zh_CN.UTF-8”
```
## 安装输入法

`#pkg install zh-ibus-libpinyin`（安装好运行初始化命令ibus-setup）

## 安装字体

`#pkg install wqy-fonts`

## 终端显示中文(文件用户根目录)

添加以下内容
```
#ee .cshrc
setenv LANG zh_CN.UTF-8
setenv LC_CTYPE zh_CN.UTF-8
setenv LC_ALL zh_CN.UTF-8`
```
## 优化系统

gnome-tweaks

##
