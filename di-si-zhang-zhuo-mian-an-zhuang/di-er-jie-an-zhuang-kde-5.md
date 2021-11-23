# 第二节 安装 KDE 5

## 1.安装 <a href="1-an-zhuang" id="1-an-zhuang"></a>

`#pkg install -y xorg sddm kde5 wqy-fonts`

## 2.配置

`#ee /etc/fstab`\
添加内容如下:

`proc /proc procfs rw 0 0`

然后
```
#ee /etc/rc.conf
#添加：
dbus_enable=”YES”
hald_enable=”YES”
sddm_enable=”YES”
echo “exec /usr/local/bin/startkde” > ~/.xinitrc
```


## 中文化

点击开始->System Settings->Regional Settings 在Language项的Available Language栏中找到“简体中文”单击“>”将其加到 Preferrred Languages栏中，然后单击Apply按钮；再到Formats项，将Region文本框中的内容修改为“中国-简体中文(zh-CN)，单击Apply按钮，logout（注销）后重新登录，此时系统语言将变为中文。

