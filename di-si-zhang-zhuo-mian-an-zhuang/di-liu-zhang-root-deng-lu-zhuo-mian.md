# 第六节 root 登录桌面

## FreeBSD 下root 登录 lightdm

`　# pkg install lightdm-gtk-greeter lightdm`

　　写入lightdm\_enable=“YES”到rc.conf

　　编辑`# ee /usr/local/etc/lightdm/lightdm.conf`

　　往下拉，找到greeter-show-manual-login=true 移除前面的#

　　编辑 `# ee /usr/local/etc/pam.d/lightdm`

　　注释account requisite pam\_securetty.so 这一行（往最前面加#）

　　`# service lightdm start`

即可。

## FreeBSD KDE5 SDDM root登录

更改`  /usr/local/etc/pam.d/sddm  `文件\
把include 之后的login，替换成system，一共4个。\
之后就可以以root 登录sddm了！

#### 注意sddm 左下角选项不能为Wayland ，应该是Plasma-X11，选错无法登陆！
