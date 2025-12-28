# 8.10 微信（Linux 版本）

## 基于 Rocky Linux 兼容层（FreeBSD Ports）

请先参照本书其他章节，先行安装 Rocky Linux 兼容层（FreeBSD Ports）。

### 安装 RPM 工具

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

官方下载地址：[微信 Linux 测试版](https://linux.weixin.qq.com/)

```sh
# fetch https://dldir1v6.qq.com/weixin/Universal/Linux/WeChatLinux_x86_64.rpm	# 写作本文时链接如此，请自行获取最新的微信下载链接
```

### 安装微信

```sh
root@ykla:/ # cd /compat/linux/	# 切换到兼容层路径
root@ykla:/compat/linux # rpm2cpio < WeChatLinux_x86_64.rpm  | cpio -id	# 读者请将 WeChatLinux_x86_64.rpm 的路径改成自己的
1393412 blocks
```

### 解决依赖问题

查看依赖关系：

```bash
# /compat/linux/usr/bin/bash	# 切换到兼容层的 shell
bash-5.1# ldd /opt/wechat/wechat	# 使用 ldd 检查微信的依赖库是否完整
	libatomic.so.1 => not found
	libbz2.so.1.0 => not found
	libxkbcommon-x11.so.0 => not found
	libxcb-icccm.so.4 => not found
	libxcb-image.so.0 => not found
	libxcb-render-util.so.0 => not found
	libxcb-keysyms.so.1 => not found
		……其他省略……
```

- 安装缺少的依赖库 `libatomic.so.1`。

使用 pkg 安装：

```sh
# pkg install linux-rl9-libatomic
```

或者使用 ports 安装：

```sh
# cd /usr/ports/devel/linux-rl9-libatomic/ 
# make install clean
```

- 为缺少的依赖库 `libbz2.so.1.0` 创建符号链接：

```sh
# ln -s /compat/linux/lib64/libbz2.so.1.0.8 /compat/linux/lib64/libbz2.so.1.0 # 创建所需的符号链接
```

>**技巧**
>
>`libbz2.so.1` 这个库本身已存在，但文件名不同。如果找不到，可以输入 `ls /compat/linux/lib64/libbz2`，然后按 **TAB** 键补全，查看实际文件名。


- 安装依赖库 `libxkbcommon-x11.so.0`：

```sh
# fetch https://dl.rockylinux.org/pub/rocky/9/devel/x86_64/os/Packages/l/libxkbcommon-x11-1.0.3-4.el9.x86_64.rpm	# 下载所需的依赖库
# cd /compat/linux/
root@ykla:/compat/linux # rpm2cpio < libxkbcommon-x11-1.0.3-4.el9.x86_64.rpm  | cpio -id 	# 解压安装该依赖库
82 blocks
```

>**技巧**
>
>当找不到 Rocky Linux 的某个库时，可以到 <https://rockylinux.pkgs.org/> 搜索。FreeBSD Ports 已经打包了一部分，可以参照 pkg 章节使用 `pkg-provides` 搜索一下。


- 解决依赖库 `libxcb-icccm.so.4`：

```sh
# fetch https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/x/xcb-util-wm-0.4.1-22.el9.x86_64.rpm	# 下载所需的依赖库
# cd /compat/linux/
root@ykla:/compat/linux #  rpm2cpio < xcb-util-wm-0.4.1-22.el9.x86_64.rpm  | cpio -id 	# 解压安装该依赖库 
175 blocks
```

- 解决其他与 xcb 库相关的依赖。

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

在命令行中启动微信。

```sh
$ /compat/linux/opt/wechat/wechat
```

### 创建软件图标

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

设置 `wechat.desktop` 文件权限为 `755`，使其可执行：

```sh
# chmod 755 ~/.local/share/applications/wechat.desktop
```

重启系统后，即可在系统菜单中找到微信。

功能正常：

![FreeBSD 微信](../.gitbook/assets/wechat1.png)

![FreeBSD 微信](../.gitbook/assets/wechat2.png)

![FreeBSD 微信](../.gitbook/assets/wechat3.png)

### 中文输入法问题

如果以 root 权限运行 Rocky Linux 兼容层中的应用，输入法可能会出现问题。

![FreeBSD 微信](../.gitbook/assets/wechat4.png)
