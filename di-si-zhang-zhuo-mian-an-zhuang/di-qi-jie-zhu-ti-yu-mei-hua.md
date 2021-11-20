# 第七节 主题与美化

**FreeBSD**安装桌面环境后，同其它**类Unix**系统一样，很多时候扑面而来的，是一种朴素的色调。这种未加修饰设定，一来是为了系统的稳定，二来众口难调，桌面系统的美化，涉及个人的审美。因此为了提升系统的美观，我们在这一节学习添加 **主题** 和 **图标**。

~~我们常用的图形界面，基本分为了两大工具包：`GTK` 和 `Qt`。使用`GTK`的桌面有`Gnome`、`XFCE`、`Mate`和`LXDE`等；使用`Qt`的桌面有`KDE` 和 `Lxqt`等.~~

## 直接安装软件包

- [ ] 新手任务 ： 从以下软件包中，各选一款主题和图标来安装。

### 主题

- matcha 主题： `pkg install matcha-gtk-themes`

- Qogir 主题： `pkg install qogir-gtk-themes`

- Pop 主题：`pkg install pop-gtk-themes`

- Flat 主题：`pkg install flat-remix-gtk-themes`

- Numix 主题： `pkg install numix-gtk-theme`


### 图标

- papirus 图标： `pkg install papirus-icon-theme`

- Qogir 图标： `pkg install qogir-icon-themes`

- Pop 图标： `pkg install pop-icon-theme`

- Flat 图标：`pkg install flat-remix-icon-themes`

- Numix 图标： `pkg install numix-icon-theme`

- Numix 圆形图标： `pkg install numix-icon-theme-circle`


## 终端安装

*提示：刚接触 Unix 的用户可略过本节*

- [ ] 高阶任务：为 KDE 或 Gnome 安装一款仿 MacOS 系统样式的主题和图标。

- [x] 提前任务1：安装bash `pkg install bash` 

- [x] 提前任务2：安装plank ``

### KDE 主题美化

我们要安装的是 [WhiteSur](https://github.com/vinceliuice/WhiteSur-kde) 主题。

- 1. 下载主题源码包： `git clone https://github.com/vinceliuice/WhiteSur-kde`

- 2. 进入主题包目录： `cd WhiteSur-kde`

- 3. 修改 shebang： `vim install.sh`，修改第一行为 `/usr/local/bin/bash`，然后保存。

- 4. 执行安装： `bash install.sh`

### Gnome 主题美化

同样我们要安装的是 [WhiteSur](https://github.com/vinceliuice/WhiteSur-gtk-theme) 主题。

- 1. 下载主题源码包： `git clone https://github.com/vinceliuice/WhiteSur-gtk-theme`

- 2. 进入主题包目录： `cd WhiteSur-gtk-theme`

- 3. 修改 shebang： `vim install.sh`，修改第一行为 `/usr/local/bin/bash`，然后保存。

- 4. 执行安装： `bash install.sh`


### 图标

- 1. 下载图标： `git clone https://github.com/vinceliuice/WhiteSur-icon-theme`

- 2. 进入主题包目录： `cd WhiteSur-icon-theme`

- 3. 修改 shebang： `vim install.sh`，修改第一行为 `/usr/local/bin/bash`，然后保存。

- 4. 执行安装： `bash install.sh`

### 光标

- 1. 下载光标： `git clone https://github.com/vinceliuice/McMojave-cursors`

- 2. 进入主题包目录： `cd McMojave-cursors`

- 3. 修改 shebang： `vim install.sh`，修改第一行为 `/usr/local/bin/bash`，然后保存。

- 4. 执行安装： `bash install.sh`

### 背景图片[下载地址](https://github.com/vinceliuice/WhiteSur-kde/tree/master/wallpaper)

### 课后练习

试按照下述步骤，自己在终端安装[Papirus 图标](https://www.gnome-look.org/p/1166289/)

```
git clone https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
cd papirus-icon-theme
./install.sh
```
