# 第二节 安装 KDE 5

>以下教程适用于 shell 为 csh/tcsh 的用户。
>
>首先看看现在自己的 shell 是不是 csh/tcsh
>
>`# echo  $0`
>
>如果是 csh/tcsh 其中之一，请继续。

## 安装

```
# pkg install xorg sddm kde5 wqy-fonts xdg-user-dirs
```


>上面的命令分别安装了桌面、窗口管理器和中文字体以及创建用户目录的工具。

## 配置

`# ee /etc/fstab`

添加内容如下:

```
proc            /proc           procfs  rw      0       0
```

>添加 proc 挂载这一步是非常必要的，如果不添加会导致桌面服务无法正常运行，部分组件无法加载！

然后


```
sysrc dbus_enable="YES"
sysrc sddm_enable="YES"
```

然后

`# echo "exec ck-launch-session startplasma-x11" > ~/.xinitrc`

>如果你在 root 下已经执行过了，那么新用户仍要再执行一次才能正常使用（无需 root 权限或 sudo 等）。

提示：hal 已经被删除。**不需要**再添加~~hald_enable="YES",~~ 见：

https://www.freshports.org/sysutils/hal


**注意：如果 sddm 登录闪退到登录界面，请检查左下角是不是 plasma-X11，闪退的一般都是 Wayland！因为目前 FreeBSD 上的 KDE 5 尚不支持 Wayland。**

## 中文化

点击开始-> System Settings -> Regional Settings 在 `Language` 项的 `Available Language` 栏中找到 “简体中文” 单击 `>` 将其加到 `Preferrred Languages` 栏中，然后单击 `Apply` 按钮；再到 `Formats` 项，将 `Region` 文本框中的内容修改为 “中国-简体中文(zh-CN)”，单击 `Apply` 按钮，logout（注销）后重新登录，此时系统语言将变为中文。
