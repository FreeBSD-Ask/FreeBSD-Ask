# 8.10 微信（Linux 版本）

## 基于 Rocky Linux 兼容层（FreeBSD Port）

>**注意**
>
>请先参照本书其他章节先行安装 Rocky Linux 兼容层（FreeBSD Port）

### 安装 rpm 工具

- 使用 pkg 安装

```sh
# pkg install rpm4
```

- 或者使用 Ports 安装：

```
# cd /usr/ports/archivers/rpm4/ 
# make install clean
```

### 下载微信

官方地址：[微信 Linux 测试版](https://linux.weixin.qq.com/)

```sh
# fetch https://dldir1v6.qq.com/weixin/Universal/Linux/WeChatLinux_x86_64.rpm # 写作本文时链接如此，请自行获取最新的微信下载链接
```

### 安装微信

```sh
root@ykla:/ # cd /compat/linux/	# 切换到兼容层路径
root@ykla:/compat/linux # rpm2cpio < WeChatLinux_x86_64.rpm  | cpio -id # 读者请将 WeChatLinux_x86_64.rpm 的路径改成自己的
1393412 blocks
```

### 解决依赖问题

查看依赖：

```bash
root@ykla:/compat/linux # /compat/linux/usr/bin/bash # 切换到兼容层的 shell
bash-5.1# ldd /opt/wechat/wechat # 使用 ldd 检查微信的依赖库是否完整
	libatomic.so.1 => not found
	libbz2.so.1.0 => not found
	libxkbcommon-x11.so.0 => not found
	libxcb-icccm.so.4 => not found
	libxcb-image.so.0 => not found
	libxcb-render-util.so.0 => not found
	libxcb-keysyms.so.1 => not found
		……其他省略……
```

- 安装缺少的依赖 `libatomic.so.1` 库。

使用 pkg 安装：

```sh
# pkg install linux-rl9-libatomic
```

或者使用 ports 安装：

```sh
# cd /usr/ports/devel/linux-rl9-libatomic/ 
# make install clean
```

- 再链接缺少的依赖 `libbz2.so.1.0` 库：

```sh
# ln -s /compat/linux/lib64/libbz2.so.1.0.8 /compat/linux/lib64/libbz2.so.1.0 # 重命名所需的库
```

>**技巧**
>
>`libbz2.so.1` 这个库本来就有，但是名字不一样，你找不到的话，自己输入 `ls /compat/linux/lib64/libbz2` 然后按一下 **TAB** 补全看一下你的名字是什么。

- 安装依赖库 `libxkbcommon-x11.so.0`:

```sh
# fetch https://dl.rockylinux.org/pub/rocky/9/devel/x86_64/os/Packages/l/libxkbcommon-x11-1.0.3-4.el9.x86_64.rpm	# 下载所需的依赖库
# cd /compat/linux/
root@ykla:/compat/linux # rpm2cpio < libxkbcommon-x11-1.0.3-4.el9.x86_64.rpm  | cpio -id 	# 解压安装该依赖库
82 blocks
```

>**技巧**
>
>当找不到 Rocky Linux 的某某库时，可以到 <https://rockylinux.pkgs.org/> 搜索。FreeBSD Ports 已经打包了一部分，可以参照 pkg 章节使用 `pkg-provides` 搜索一下。


- 解决依赖 `libxcb-icccm.so.4`：

```sh
# fetch https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/x/xcb-util-wm-0.4.1-22.el9.x86_64.rpm	# 下载所需的依赖库
# cd /compat/linux/
root@ykla:/compat/linux #  rpm2cpio < xcb-util-wm-0.4.1-22.el9.x86_64.rpm  | cpio -id 	# 解压安装该依赖库 
175 blocks
```

- 解决其他 xcb 库相关依赖。

使用 pkg 安装：

```sh
# pkg install linux-rl9-xcb-util
```

或者使用 ports 安装：

```sh
# cd /usr/ports/x11/linux-rl9-xcb-util/ 
# make install clean
```

### 启动微信

在命令行启动微信。

```sh
$ /compat/linux/opt/wechat/wechat
```

### 软件图标

在路径 `~/.local/share/applications` 下新建文本文件 `wechat.desktop`，写入：

```ini
[Desktop Entry]
Name=WeChat
Comment=微信
Exec=/compat/linux/opt/wechat/wechat
Terminal=false
Type=Application
Encoding=UTF-8
Icon=/compat/linux/opt/wechat/icons/wechat.png
Path=
StartupNotify=false
Categories=Network
```

重启系统，即可在系统菜单中找到微信。

功能正常：

![FreeBSD 微信](../.gitbook/assets/wechat1.png)

![FreeBSD 微信](../.gitbook/assets/wechat2.png)

![FreeBSD 微信](../.gitbook/assets/wechat3.png)

### 中文输入法

如果以 root 权限运行 RockyLinux 中的兼容层应用，则输入法会有问题。请以普通用户权限运行之。

![FreeBSD 微信](../.gitbook/assets/wechat4.png)
