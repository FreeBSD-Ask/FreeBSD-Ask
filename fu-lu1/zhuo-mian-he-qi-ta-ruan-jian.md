# 桌面和其他软件

本节介绍 OpenBSD 上常用桌面环境的安装与配置，以及一些实用工具的使用方法，为用户提供完整的桌面系统搭建指南。

## MATE

MATE 是一个基于传统 GNOME 2 的桌面环境，提供了简洁、稳定的用户体验，适合追求系统稳定性和传统桌面操作模式的用户。

### 安装 MATE 桌面环境

以 `root` 用户登录终端，并运行以下命令，安装 MATE 桌面环境及其工具和附加组件：

```sh
# pkg_add mate mate-utils mate-extras
```

编辑 `/etc/rc.conf.local` 文件，添加如下配置：

```ini
pkg_scripts=messagebus avahi_daemon   # 系统启动时自动启动的服务列表，包括 messagebus 和 avahi_daemon
apmd_flags=-A                           # APM（高级电源管理）守护进程启动参数，-A 表示启用所有事件监控
multicast=YES                           # 启用多播功能
```

在终端输入以下命令，安装中文字体包，包括 Noto CJK 和文泉驿正黑字体：

```sh
# pkg_add noto-cjk zh-wqy-zenhei-ttf
```

退出 `root` 账号，并以普通用户账号重新登录桌面即可。

### 配置 MATE 桌面环境

安装完成后，需要进行一些基本配置才能正常使用 MATE 桌面环境。

将以下内容添加到 `~/.xsession` 文件（用于 `xenodm` 登录）或 `~/.xinitrc` 文件（用于控制台登录）：

```ini
. ~/.profile             # 加载用户环境配置文件
. ~/.kshrc               # 加载 KornShell 配置文件
/usr/local/bin/mate-session   # 启动 MATE 桌面会话
```

配置完成后，重新登录账户，或在控制台运行 `startx` 即可进入 MATE 桌面环境。

### 安装 Fcitx 5 输入法及中文界面

本节介绍 Fcitx 5 输入法的安装和配置方法。

安装 Fcitx 5 输入法框架及相关图形配置工具、GTK/Qt 支持和中文输入法插件：

```sh
# pkg_add fcitx fcitx-configtool-qt fcitx-gtk fcitx-qt fcitx-chinese-addons
```

随后请在 Fcitx 5 设置中手动添加中文输入法。

编辑 `~/.profile` 文件，添加以下文本：

```ini
export LANG="zh_CN.UTF-8"       # 设置系统语言环境为中文 UTF-8
export LC_ALL="zh_CN.UTF-8"     # 设置所有本地化环境变量为中文 UTF-8
export XIM_PROGRAM=fcitx         # 指定 XIM 输入法程序为 fcitx
export XIM=fcitx                 # 指定 XIM 输入法
export XMODIFIERS="@im=fcitx"   # 设置 XIM 修饰符，使用 fcitx
export QT_IM_MODULE=XIM          # 指定 Qt 输入法模块为 XIM
export GTK_IM_MODULE=XIM         # 指定 GTK 输入法模块为 XIM
```

用户主目录配置文件结构：

```sh
~/
├── .xsession
├── .xinitrc
├── .profile
└── .kshrc
```

## Xfce

Xfce 是一个轻量级的桌面环境，适合资源有限的计算机使用。

### 安装 Xfce

在终端运行以下命令，安装 Xfce 桌面环境及其附加组件：

```sh
# pkg_add xfce xfce-extras
```

编辑 `/etc/rc.conf.local` 文件，添加以下几行：

```ini
pkg_scripts=messagebus avahi_daemon   # 系统启动时自动启动的服务，包括 messagebus 和 avahi_daemon
apmd_flags=-A                           # 高级电源管理（APM）守护进程参数，-A 表示启用所有事件监控
multicast=YES                           # 启用网络多播功能
```

启用 `messagebus` 和 `avahi_daemon` 服务，使其在系统启动时自动运行：

```sh
# rcctl enable messagebus avahi_daemon
```

安装中文字体包，包括 Noto CJK 和文泉驿正黑字体：

```sh
# pkg_add noto-cjk zh-wqy-zenhei-ttf
```

退出 `root` 账号，以普通账号登录。

### 配置 Xfce

Xfce 安装完成后，需要进行简单配置才能正常使用。

将以下内容添加到 `~/.xsession` 文件（用于 `xenodm` 登录）或 `~/.xinitrc` 文件（用于控制台登录）：

```ini
. ~/.profile                 # 加载用户环境配置文件
. ~/.kshrc                   # 加载 KornShell 配置文件
/usr/local/bin/startxfce4    # 启动 Xfce 桌面会话
```

配置完成后，重新登录账户，或在控制台运行 `startx` 即可进入 Xfce 桌面环境。

### 安装 Fcitx 5 输入法及中文界面

与 MATE 类似，在 Xfce 中也可以安装 Fcitx 5 输入法以支持中文输入。

安装 Fcitx 5 输入法框架及相关工具、GTK/Qt 支持和中文输入法插件：

```sh
# pkg_add fcitx fcitx-configtool-qt fcitx-gtk fcitx-qt fcitx-chinese-addons
```

随后请在 Fcitx 5 设置中手动添加中文输入法。

编辑 `~/.profile` 文件，添加以下文本：

```ini
export LANG="zh_CN.UTF-8"       # 设置系统语言环境为中文 UTF-8
export LC_ALL="zh_CN.UTF-8"     # 设置所有本地化环境变量为中文 UTF-8
export XIM_PROGRAM=fcitx         # 指定 XIM 输入法程序为 fcitx
export XIM=fcitx                 # 指定 XIM 输入法
export XMODIFIERS="@im=fcitx"   # 设置 XIM 修饰符，使用 fcitx
export QT_IM_MODULE=XIM          # 指定 Qt 输入法模块为 XIM
export GTK_IM_MODULE=XIM         # 指定 GTK 输入法模块为 XIM
```

## GNOME

GNOME 是一个现代化、功能丰富的桌面环境，提供了直观的用户界面和丰富的应用程序。

### 安装 GNOME

打开终端，输入以下命令安装 GNOME 桌面环境及其附加组件：

```sh
# pkg_add gnome gnome-extras
```

然后运行以下命令：

```sh
# rcctl disable xenodm                     # 禁用 xenodm 显示管理器服务
# rcctl enable messagebus gdm avahi_daemon # 启用 messagebus、GDM 和 avahi_daemon 服务，使其开机自启动
```

重启系统后，即可登录 GNOME 桌面环境。

### 中文字体

为了在 GNOME 中正常显示中文，需要安装中文字体包。

安装中文字体包，包括 Noto CJK 和文泉驿正黑字体：

```sh
# pkg_add noto-cjk zh-wqy-zenhei-ttf
```

### 中文界面

安装完字体后，还需要配置系统语言以显示中文界面。

编辑 `/etc/gdm/locale.conf` 文件，修改文本为如下内容：

```ini
LC_CTYPE="zh_CN.UTF-8"
LC_MESSAGES="zh_CN.UTF-8"
```

将系统消息的本地化语言设置为中文 UTF-8。

重启系统后，即可进入中文界面。

### 主题和图标

用户可以根据个人喜好自定义 GNOME 的外观，包括主题和图标。

以下仅举两个实例，[Qogir](https://www.gnome-look.org/p/1230631/) 主题和 [Tela](https://www.gnome-look.org/p/1279924/) 图标。

可访问 [相关网站](https://www.gnome-look.org/) 自行选择并安装所需的主题和图标。

#### 提前准备

在安装主题和图标前，需要先准备一些必要的工具。

执行命令，安装 Git 版本控制工具和 Bash Shell：

```sh
# pkg_add git bash
```

#### 安装主题

准备工作完成后，就可以开始安装主题了。

克隆 Qogir 主题仓库并切换到该目录：

```sh
$ git clone https://github.com/vinceliuice/Qogir-theme && cd Qogir-theme
```

编辑 `install.sh` 文件，将文件的第一行修改为 `#!/usr/local/bin/bash`。

之后使用 Bash 执行 Qogir 主题安装脚本：

```sh
$ bash ./install.sh
```

#### 安装图标

除了主题外，用户也可以更换系统图标以获得更好的视觉效果。

克隆 Tela 图标主题仓库并切换到该目录：

```sh
$ git clone https://github.com/vinceliuice/Tela-icon-theme && cd Tela-icon-theme
```

编辑 `install.sh` 文件，将文件的第一行修改为 `#!/usr/local/bin/bash`。

之后使用 Bash 执行 Tela 图标主题安装脚本：

```sh
$ bash ./install.sh
```

## KDE 6

KDE Plasma 6 是 KDE 社区最新推出的桌面环境，提供了现代化的用户界面和丰富的功能。

> **警告**
>
> 在 VMware 17 UEFI 环境下，该桌面存在问题（窗口显示为灰色，仅鼠标可操作）。在 BIOS 模式下，`root` 用户也会遇到相同问题，而普通用户可正常使用。物理机下 UEFI 模式运行正常。

### 安装 KDE 6

使用命令，安装 KDE 桌面环境、D-Bus 服务及 Plasma 桌面和附加组件：

```sh
# pkg_add kde dbus kde-plasma kde-plasma-extras
```

### 启动服务

KDE 6 安装完成后，需要配置并启动一些必要的系统服务。

编辑 `/etc/rc.conf.local` 文件，添加如下几行：

```ini
pkg_scripts=messagebus avahi_daemon   # 系统启动时自动启动的服务，包括 messagebus 和 avahi_daemon
apmd_flags=-A                           # 高级电源管理（APM）守护进程参数，-A 表示启用所有事件监控
multicast=YES                           # 启用网络多播功能
```

启用 `messagebus` 和 `avahi_daemon` 服务，使其开机自启动：

```sh
# rcctl enable messagebus avahi_daemon
```

### startx

服务配置完成后，需要配置启动 KDE Plasma 桌面环境。

以下是两个配置选项，可任选其一。

**选项一：使用 ConsoleKit**

将以下内容添加到文件 `~/.xsession`（用于 `xenodm` 登录，需启用 `xenodm`）或 `~/.xinitrc`（用于控制台登录）：

```ini
. ~/.profile                             # 加载用户环境配置文件
export QT_FORCE_STDERR_LOGGING=1         # 强制 Qt 将日志输出到标准错误
export XDG_CURRENT_DESKTOP=KDE           # 设置当前桌面环境为 KDE
export DESKTOP_SESSION=plasma            # 设置桌面会话为 Plasma
ck-launch-session startplasma-x11        # 使用 ConsoleKit 启动 Plasma X11 会话
```

**选项二：使用 XDG_RUNTIME_DIR**

或者写入如下行：

```ini
export XDG_RUNTIME_DIR=/tmp/run/$(id -u)   # 使用当前用户 UID 创建专属运行时目录，用于进程间通信

# 如果运行时目录不存在，则创建，并设置权限为仅当前用户可访问
if [ ! -d $XDG_RUNTIME_DIR ]; then
    mkdir -m 700 -p $XDG_RUNTIME_DIR
fi

# 启用 Qt 的标准错误日志输出，便于调试 Qt 应用程序
export QT_FORCE_STDERR_LOGGING=1

# 设置当前桌面环境为 KDE，用于兼容桌面应用和服务
export XDG_CURRENT_DESKTOP=KDE

# 设置当前桌面会话为 plasma，标识 KDE Plasma 桌面环境
export DESKTOP_SESSION=plasma

# 启动 KDE Plasma X11 会话，并将标准输出和错误日志保存到 ~/.startplasma-x11.log
/usr/local/bin/startplasma-x11 > ~/.startplasma-x11.log 2>&1
```

配置完成后，重新登录账户，或在控制台运行 `startx` 即可进入 KDE 桌面环境。

### 故障排除

在使用 KDE 6 中可能会遇到一些问题，本节介绍常见问题的解决方法。

#### KDE 无声音

若使用 `pkg_add` 安装软件包，在 `/etc/pulse/client.conf` 文件中将 `autospawn = yes` 改为 `autospawn = no`。阻止开机加载 pulseaudio。

若使用 Ports 构建 KDE，请在构建前于 `/etc/make.conf` 中添加以下设置：

```ini
OPTIONS_UNSET+=PULSE      # 禁用 PulseAudio 支持
OPTIONS_UNSET+=PULSEAUDIO # 禁用 PulseAudio 支持（可选重复声明）
OPTIONS_SET+=SNDIO        # 启用 sndio 音频后端支持
```

系统配置文件结构：

```sh
/etc/
├── rc.conf.local
├── gdm/
│   └── locale.conf
├── pulse/
│   └── client.conf
└── make.conf
```

### 参考文献

- OpenBSD Project. The meta/kde,-plasma port[EB/OL]. (2024-03-25)[2026-03-25]. <https://openports.pl/path/meta/kde,-plasma>. 官方 Ports 包说明，提供 KDE Plasma 安装与配置参考。
- YouTube. Install KDE Plasma on OpenBSD 7.5[EB/OL]. (2024-03-25)[2026-03-25]. <https://www.youtube.com/watch?v=Gmj6O07QmRI>. 视频教程，详细演示 KDE Plasma 在 OpenBSD 上的安装流程。
- Sadowski R. KDE6 on OpenBSD[EB/OL]. (2024-05-20)[2026-03-25]. <https://rsadowski.de/posts/2024-05-20-kde6-on-openbsd/>. 技术博客，介绍 KDE6 在 OpenBSD 上的部署经验。
- Sadowski R. OpenBSD KDE Plasma Desktop[EB/OL]. (2024-01-09)[2026-03-25]. <https://rsadowski.de/posts/2024-01-09-openbsd-kde/>. 技术博客，提供 KDE Plasma 桌面环境安装指南。
- OpenBSD Ports. NEW: KDE Plasma (x11/kde-plasma)[EB/OL]. (2024-03-25)[2026-03-25]. <https://marc.info/?l=openbsd-ports&m=169391479324962&w=2>. 邮件列表公告，记录了 KDE Plasma 初次移植成功的里程碑。
- PulseAudio Project. Autospawning[EB/OL]. (2024-03-25)[2026-03-25]. <https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Running/>. PulseAudio 官方文档，说明如何控制音频服务的自动启动行为。

## Firefox

本节介绍如何在 OpenBSD 中安装 Firefox 浏览器。

安装 Firefox ESR 浏览器和 FFmpeg 多媒体处理工具：

```sh
# pkg_add firefox-esr ffmpeg
```

> **注意**
>
> 如果未安装 FFmpeg，将无法提供解码器，导致无法正常播放视频。

## 查看实时流量

除了桌面环境和浏览器外，OpenBSD 还提供了许多实用工具，本节介绍网络流量监控工具的使用方法。

bwm-ng 的使用示例：

```sh
# pkg_add bwm-ng   # 安装 bwm-ng 网络带宽监控工具
# bwm-ng           # 启动 bwm-ng，动态显示实时网络流量
  bwm-ng v0.6.3 (probing every 0.500s), press 'h' for help
  input: getifaddrs type: rate
  /         iface                   Rx                   Tx                Total
  ==============================================================================
              lo0:           0.00 KB/s            0.00 KB/s            0.00 KB/s
             bse0:         396.59 KB/s           12.80 KB/s          409.39 KB/s
           pflog0:           0.00 KB/s            0.00 KB/s            0.00 KB/s
  ------------------------------------------------------------------------------
            total:         396.59 KB/s           12.80 KB/s          409.39 KB/s
```
