# 第 2.9 节 虚拟机预安装镜像

## 环境

- 虚拟机版本：VMware® Workstation 17 Pro 17.5.2 build-23775571
- 主机版本：Windows 10 企业版 21H2
- BIOS+UEFI
- DNS：`223.5.5.5`
- 主机名：`ykla`
- 用户名：`root`、`ykla`
- 密码：`root`、`ykla` 均为 `z`
- pkg 源已经配置为 latest 版本的 NJU Mirror（南京大学开源镜像站），如不喜欢可以删除自定义文件 `/usr/local/etc/pkg/repos/ustc.nju`，即可切换回官方源。
- 推荐内存 4-8G；CPU 4。
- 已经安装虚拟机工具，屏幕可自由拖动缩放，鼠标可无缝切换。
- 已经关闭锁屏，可以到设置中自行开启。
- 已经设置 KDE5 为中文，可以到设置中自行修改。
- 已经允许 root ssh，但未允许 root 登录 ssdm，如有需要可参照其他章节教程自行修改。
- 预设置了 `/etc/make.conf`，可自行查看内容。已经配置了多线程编译，使用 USTC 的 Port 源。
- 预拉取了 USTC 镜像站的的 ports，如需使用，请先更新：`cd /usr/ports/ && git pull`
- 安装了火狐浏览器和 fcitx5 输入法框架及输入法（输入法已为 `root` 用户进行配置）


## 预装软件

预装软件一览表（不含依赖包）：

|软件|备注|
|pkg||
|xorg||
|sddm||
|kde5||
| plasma5-sddm-kcm||
|wqy-fonts||
|xdg-user-dirs||
|xf86-video-vmware||
| open-vm-tools||
| xf86-input-vmmouse||
|git||
|firefox-esr||
|fcitx5||
| fcitx5-qt5 ||
|fcitx5-qt6||
| fcitx5-gtk2 ||
|fcitx5-gtk3 ||
|fcitx5-gtk4||
| fcitx5-configtool ||
|zh-fcitx5-chinese-addons||
|||
|||
|||
|||
|||
|||


   
