# 第 4.9 节 主题与美化

**FreeBSD** 安装桌面环境后，同其它 **类 Unix** 系统一样，很多时候扑面而来的，是简单朴素的色调。这种未加修饰的设定，可能一时会让新用户无法接受。其实它背后的逻辑也很简单：一来是为了系统的稳定，二来众口难调，桌面系统的美化，涉及个人的审美。为了系统的美观，我们将在这一节学习添加 **主题** 和 **图标**。

## 安装软件包

- [ ] 新手任务 ： 从以下软件包中，各选一款主题和图标来安装。

**注：本节仅涉及了 `GTK` 库的桌面主题，囊括了 `Gnome`、`XFCE`、`MATE`、`Cinnamon` 和 `LXDE` 等桌面环境。**

以下仅收录了部分图标和主题，想要获取更多资源，可访问 [FreshPorts](https://www.freshports.org)。

### 主题

- matcha 主题： `# pkg install matcha-gtk-themes`
- Qogir 主题： `# pkg install qogir-gtk-themes`
- Pop 主题：`# pkg install pop-gtk-themes`
- Flat 主题：`# pkg install flat-remix-gtk-themes`
- Numix 主题： `# pkg install numix-gtk-theme`
- Sierra 主题：`# pkg install sierra-gtk-themes`
- Yaru 主题： `# pkg install yaru-gtk-themes`
- Canta 主题：`# pkg install canta-gtk-themes`

### 图标

- papirus 图标： `# pkg install papirus-icon-theme`
- Qogir 图标： `# pkg install qogir-icon-themes`
- Pop 图标： `# pkg install pop-icon-theme`
- Flat 图标：`# pkg install flat-remix-icon-themes`
- Numix 图标： `# pkg install numix-icon-theme`
- Numix 圆形图标： `# pkg install numix-icon-theme-circle`
- Yaru 图标：`# pkg install yaru-icon-theme`
- Canta 图标：`# pkg install canta-icon-theme`

## 终端模式安装

_提示： 新接触 Unix 的用户可略过本节_

- [ ] 高阶任务：为 KDE 或 Gnome 安装一款仿 MacOS 系统样式的主题和图标。
- [x] 提前任务 1 安装 bash：`# pkg install bash`
- [x] 提前任务 2 安装 plank：`# pkg install plank`
- [x] 提前任务 3 安装 git： `# pkg install git`

### KDE 主题美化

我们要安装的是 [WhiteSur](https://www.pling.com/p/1398840/) 主题。

1. 下载主题源码包： `git clone https://github.com/vinceliuice/WhiteSur-kde`
2. 进入主题包目录： `cd WhiteSur-kde`
3. 修改 shebang： `ee install.sh`，修改第一行为 `#!/usr/local/bin/bash`，然后保存。
4. 执行安装： `bash install.sh`

### Gnome 主题美化

同样我们要安装的是 [WhiteSur](https://www.pling.com/p/1403328/) 主题。

1. 下载主题源码包： `git clone https://github.com/vinceliuice/WhiteSur-gtk-theme`
2. 进入主题包目录： `cd WhiteSur-gtk-theme`
3. 修改 shebang： `ee install.sh`，修改第一行为 `#!/usr/local/bin/bash`，然后保存。
4. 执行安装： `bash install.sh`

### [图标](https://www.pling.com/p/1405756/)

1. 下载图标： `git clone https://github.com/vinceliuice/WhiteSur-icon-theme`
2. 进入软件目录： `cd WhiteSur-icon-theme`
3. 修改 shebang： `ee install.sh`，修改第一行为 `#!/usr/local/bin/bash`，然后保存。
4. 执行安装： `bash install.sh`

### [光标](https://www.pling.com/p/1355701/)

1. 下载光标： `git clone https://github.com/vinceliuice/McMojave-cursors`
2. 进入软件目录： `cd McMojave-cursors`
3. 修改 shebang： `ee install.sh`，修改第一行为 `#!/usr/local/bin/bash`，然后保存。
4. 执行安装： `bash install.sh`

### 背景图片

[下载地址](https://github.com/vinceliuice/WhiteSur-kde/tree/master/wallpaper)

### 课后练习

试着按照下面的步骤，在终端安装 [Papirus 图标](https://www.gnome-look.org/p/1166289/):

```shell-session
git clone https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
cd papirus-icon-theme
./install.sh
```
