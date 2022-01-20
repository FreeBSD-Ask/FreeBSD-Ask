# 第二节 安装 KDE 5

## 安装

`# pkg install -y xorg sddm kde5 wqy-fonts`

## 配置

`# ee /etc/fstab`
添加内容如下:

`proc /proc procfs rw 0 0`

然后

```
# ee /etc/rc.conf
#添加：
dbus_enable="YES"
sddm_enable="YES"

#然后
# echo "exec ck-launch-session startplasma-x11" > ~/.xinitrc
```



提示：hal 已经被删除。**不需要**再添加~~hald_enable="YES",~~ 见：

{% embed url="https://www.freshports.org/sysutils/hal" %}


**注意：如果 sddm 登录闪退到登录界面，请检查左下角是不是 plasma-X11，闪退的一般都是 Wayland！因为目前 FreeBSD 上的 KDE 5 尚不支持 Wayland。**

## 中文化

点击开始->System Settings->Regional Settings 在`Language`项的`Available Language`栏中找到“简体中文”单击“>”将其加到`Preferrred Languages`栏中，然后单击Apply按钮；再到`Formats`项，将`Region`文本框中的内容修改为“中国-简体中文(zh-CN)，单击`Apply`按钮，logout（注销）后重新登录，此时系统语言将变为中文。
