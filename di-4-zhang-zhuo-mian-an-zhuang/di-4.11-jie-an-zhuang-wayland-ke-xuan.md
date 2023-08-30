# 第 4.11 节 安装 Wayland （可选）

目前安装 xorg 会自动安装 Wayland。

Wayland 是 Xorg 的下一代替代品，使用上的不同就是相比 xorg，前者界面渲染效果更好，更加流畅；触控板效果更加接近 macOS。但是 Wayland 设计上更加反人类，甚至不为应用程序提供接口，导致远程软件都无法开发。

FreeBSD 已经正式支持 wayland。但是经过测试目前暂不支持 kde5 gnome 等桌面。但是支持了 bspwm wayfire——参见 Handbook。
