# 第六节 root 登录桌面

## FreeBSD 下 root 登录 lightdm

`　# pkg install lightdm-gtk-greeter lightdm`

　　写入`lightdm_enable="YES"`到rc.conf

　　编辑`# ee /usr/local/etc/lightdm/lightdm.conf`

　　往下拉，找到`greeter-show-manual-login=true`移除前面的`#`

　　编辑 `# ee /usr/local/etc/pam.d/lightdm`

　　注释`account requisite pam_securetty.so`这一行（往最前面加`#`）

　　`# service lightdm start`

即可。

## FreeBSD KDE5 SDDM root登录

更改`/usr/local/etc/pam.d/sddm`文件
把`include`之后的`login`，替换成`system`，一共4个。
之后就可以以 root 登录 sddm了！

#### 注意 sddm 左下角选项不能为 Wayland ，应该是 Plasma-X11，目前 KDE 5 不支持 wayland，选错无法登陆！
