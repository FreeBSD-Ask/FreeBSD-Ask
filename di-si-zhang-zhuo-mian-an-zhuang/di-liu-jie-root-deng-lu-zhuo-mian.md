# 第六节 root 登录桌面

## lightdm

安装与配置：

```
# pkg install lightdm-gtk-greeter lightdm
```

首先设置启动服务：

```
　　# sysrc lightdm_enable="YES"
```
然后修改配置文件：

　　编辑`# ee /usr/local/etc/lightdm/lightdm.conf`

　　往下拉，找到`greeter-show-manual-login=true`移除前面的`#`

　　编辑 `# ee /usr/local/etc/pam.d/lightdm`

　　注释`account requisite pam_securetty.so`这一行（往最前面加`#`）

重启服务

```
# service lightdm restart`
```

即可。

## sddm

安装

```
# pkg install sddm
# sysrc sddm_enable="YES"
```

更改`/usr/local/etc/pam.d/sddm`文件:

把`include`之后的`login`，替换成`system`，一共4个。

重启服务

```
# service sddm restart
```

之后就可以 root 登录 sddm了！

#### 注意 sddm 左下角选项不能为 Wayland ，应该是 Plasma-X11，目前 KDE 5 不支持 wayland，选错无法登陆！
