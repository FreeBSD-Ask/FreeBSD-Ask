# 8.12 CDE

## CDE 桌面环境概述

CDE（Common Desktop Environment，通用桌面环境）是 20 世纪 90 年代商业 UNIX 系统的标准桌面环境，曾广泛应用于 Solaris、HP-UX 和 AIX 等商业发行版。

## 安装 CDE 桌面环境

如果您需要使用中文环境，请从源代码编译安装。

### 常规方法

#### - 使用 pkg 安装：

```sh
# pkg install xorg cde wqy-fonts xdg-user-dirs
```

#### - 或使用 Ports 安装：

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11/cde/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean
```

#### 软件包说明

|包名|作用说明|
|---|---|
|`xorg`|X 窗口系统|
|`cde`|提供传统的 CDE 桌面环境|
|`wqy-fonts`|文泉驿中文字体|
|`xdg-user-dirs`|管理用户目录，如"桌面""下载"等|

### 源代码编译

#### 前置准备与关键警告

1. 系统环境要求：请确认系统语言已设置为中文（`zh_CN.UTF-8` 或 `zh_TW.UTF-8`），否则中文编译适配将失效。

2. 架构依赖说明：aarch64 架构设备无适配的 `shells/ksh93` 二进制包，`ksh2020` 无法替代（缺少 CDE 必需的 libAST 依赖），该架构设备暂无法完成中文源码编译安装。

CDE 官方源码包已经自带 `zh_CN.UTF-8` 和 `zh_TW.UTF-8` 的翻译文件（app-defaults、msg、config、palettes、types、backdrops 等），但缺少构建系统集成——没有 `configure` 选项、没有 Makefile.am、没有 Autoconf 模板。`build_zh.sh` 预处理脚本负责补齐这些缺失的部分。

#### 安装编译依赖

源代码编译需提前安装全部依赖组件，执行以下 pkg 安装命令：

```sh
# pkg install -y autoconf automake libtool gmake gcc git \
  shells/ksh93 x11-toolkits/open-motif fontconfig \
  xorg libX11 libXext libXft libXinerama libXmu libXpm libXrandr \
  libXrender libXtst openjdk11 jpeg-turbo png bzip2 textproc/opensp \
  tk86 tcl86 bdftopcf wqy-fonts xdg-user-dirs perl5
```

#### 源码准备与预处理

解压源码包，下载专属预处理脚本并放置到源码根目录：

```sh
# git clone https://git.code.sf.net/p/cdesktopenv/code cde
# cd cde
# wget https://raw.githubusercontent.com/lqy306/cde-zh/refs/heads/main/preprocessing_freebsd.sh
```

执行预处理脚本（仅修复构建系统配置，不执行编译操作）：

```sh
# sh ./preprocessing_freebsd.sh
```

#### 编译与安装

执行标准 Autotools 编译流程，开启中文适配参数并屏蔽系统编译告警：

```sh
# sh ./autogen.sh
# ./configure --with-tcl=/usr/local/lib/tcl8.6 --enable-chinese --enable-chinese-tw --disable-docs \
    CFLAGS="-Wno-incompatible-function-pointer-types" \
    CXXFLAGS="-Wno-register"
# gmake -j$(nproc)
# sudo gmake install
```

`--enable-chinese` 启用简体中文（zh_CN.UTF-8），`--enable-chinese-tw` 启用繁体中文（zh_TW.UTF-8），按需开启。`--disable-docs` 可跳过文档编译以节省时间。`CFLAGS`/`CXXFLAGS` 用于抑制 FreeBSD 14 下 Clang 的编译警告。

#### 启动桌面

源代码编译的 CDE 安装到 `/usr/dt/`（而非 pkg/ports 版本的 `/usr/local/dt/`）。

> **重要：首次启动前请确保主机名可解析。**
> CDE 的 ToolTalk（`ttsession`）和桌面消息系统必须在启动时解析本地主机名，若 `hostname` 返回的主机名不在 `/etc/hosts` 中，会直接导致 CDE 启动失败。
>
> 验证方法：
>
> ```sh
> $ hostname
> vmware
> $ grep "$(hostname)" /etc/hosts
> ```
>
> 如果 `grep` 没有输出，先添加主机名到 `/etc/hosts`（替换 `vmware` 为你实际的主机名）：
>
> ```sh
> # sed -i '' 's/127.0.0.1[[:blank:]]*localhost/127.0.0.1\tvmware localhost/' /etc/hosts
> ```
>
>

从现有 X11 会话启动完整 CDE 桌面：

```sh
$ /usr/dt/bin/Xsession
```

或通过 `startx` 启动：

```sh
$ echo "/usr/dt/bin/Xsession" > ~/.xinitrc
$ startx
```

也可以单独启动 CDE 窗口管理器（接替当前窗口管理器）：

```sh
$ /usr/dt/bin/dtwm
```

如需配置 dtlogin 显示管理器守护进程（提供图形登录界面），先创建 Xwrapper.config：

```sh
# echo "allowed_users=anybody" > /etc/X11/Xwrapper.config
```

然后启动 dtlogin：

```sh
# /usr/dt/bin/dtlogin -daemon
```

如需开机自启 dtlogin，将其添加到 `/etc/rc.conf`：

```sh
# sysrc dtlogin_enable=YES
```

#### 注意：路径差异

- **pkg/ports 安装**：CDE 安装在 `/usr/local/dt/`

- **源代码编译安装**：CDE 安装在 `/usr/dt/`

本手册服务配置部分以源代码编译安装的 `/usr/dt/` 路径为例。若为 pkg/ports 安装，请将路径中的 `/usr/dt/` 替换为 `/usr/local/dt/`。

#### 原理说明

CDE 源码中已包含中文翻译文件，但缺少构建系统集成。`build_zh.sh` 预处理脚本做了以下工作：

1. 在 `configure.ac` 中添加 `--enable-chinese` / `--enable-chinese-tw` 选项

2. 在 `configure.ac` 中注册 `zh_CN.UTF-8` / `zh_TW.UTF-8` 下各子目录的 Makefile

3. 在 `programs/localized/Makefile.am` 中添加 CHINESE / CHINESE_TW 条件编译

4. 创建 LANG 模板文件（`Chinese.am` / `Chinese_TW.am`）

5. 为各子目录（app-defaults、config、backdrops、types、palettes、msg、appmanager）创建 Makefile.am

6. 补全缺失的翻译文件占位符，修复繁体中文翻译中的格式问题

完成预处理后，中文翻译文件就能被 Autotools 构建系统识别并编译到 CDE 中。

### 查看安装后的信息

```sh
# pkg info -D cde
cde-2.5.2_4:
On install:
CDE - The Common Desktop Environment is an X Windows desktop environment
that was commonly used on commercial UNIX variants such as Sun Solaris,
HP-UX, and IBM AIX. Developed between 1993 and 1999, it has now been
released under an Open source license by The Open Group.
# CDE（通用桌面环境）是早期 X Windows 的桌面环境，曾广泛用于商用 UNIX 系统如 Solaris、HP-UX 和 AIX。
# 开发时间大致为 1993–1999 年，现由 The Open Group 以开源协议发布。

Common Desktop Environment requires the Subprocess Control Service,
dtcms, and the inetd super server to fully function.
# 要完整运行 CDE，需启用子进程控制服务（dtspc）、日历管理服务（dtcms）以及 inetd 超级服务器进程。

First, add the following line to /etc/inetd.conf:

dtspc	stream	tcp	nowait	root	 /usr/local/dt/bin/dtspcd	/usr/local/dt/bin/dtspcd
# 第一步，在 /etc/inetd.conf 中添加 dtspcd 服务行。

Second, add the following line to /etc/services:

dtspc		6112/tcp # CDE Subprocess Control Service
# 第二步，在 /etc/services 中注册 dtspc 服务端口。

# sysrc rpcbind_enable=YES
# sysrc dtcms_enable=YES
# sysrc inetd_enable=YES
# service rpcbind start && service dtcms start && service inetd start
# 启用并启动 rpcbind、dtcms 和 inetd 服务，这是 CDE 所依赖的组件。

Finally, make sure to add /usr/local/dt/bin to your path.
# 最后，请将 /usr/local/dt/bin 添加到当前 PATH 环境变量中。

To start the Common Desktop Environment:
% env LANG=C startx /usr/local/dt/bin/Xsession
# 使用上述命令启动 CDE 桌面环境，设置环境变量 LANG=C 避免本地化问题。

Alternatively, if you want to use the Login Manager as well, create
/usr/local/etc/X11/Xwrapper.config and add this line:

allowed_users=anybody
# 如需启用图形显示管理器（Login Manager），请创建 Xwrapper.config 并添加 allowed_users=anybody。

To start the Common Desktop Enviroment Login Manager:

% /usr/local/dt/bin/dtlogin -daemon

# 使用 dtlogin -daemon 命令启动 CDE 显示管理器（守护进程模式）。
```

### 配置服务与文件

以下命令以源代码编译安装（`/usr/dt/`）为例。若为 pkg/ports 安装，将路径中的 `/usr/dt/` 替换为 `/usr/local/dt/`。

#### 1. 主机名与网络配置

CDE 依赖主机名解析，`hostname` 返回的名称必须在 `/etc/hosts` 中有对应条目：

```sh
# 确认当前主机名
$ hostname
vmware

# 检查主机名是否在 /etc/hosts 中
$ grep "$(hostname)" /etc/hosts

# 若没有输出，添加主机名到 localhost 行
# sed -i '' 's/127.0.0.1[[:blank:]]*localhost/127.0.0.1\tvmware localhost/' /etc/hosts
```

#### 2. 配置 CDE 服务

CDE 需要 rpcbind、dtcms（日历服务）和 inetd（承载 dtspcd 子进程服务）：

```sh
# 启用并启动 rpcbind
# sysrc rpcbind_enable=YES
# service rpcbind start

# 注册 dtspc 服务端口
# grep -q '^dtspc' /etc/services || \
  echo 'dtspc		6112/tcp # CDE Subprocess Control Service' >> /etc/services

# 注册 dtspcd 到 inetd
# grep -q 'dtspc' /etc/inetd.conf || \
  echo 'dtspc	stream	tcp	nowait	root	/usr/dt/bin/dtspcd	/usr/dt/bin/dtspcd' >> /etc/inetd.conf

# 启用并启动 inetd
# sysrc inetd_enable=YES
# service inetd start
```

dtcms（日历管理守护进程）对于完整 CDE 功能是必需的：

```sh
# 手动启动 dtcms（源代码编译无 rc 脚本，直接运行二进制文件）
# /usr/dt/bin/dtcm_daemon &

# 如需开机自启，将上面这行添加到 /etc/rc.local
```

#### 3. 配置 X 服务器与显示管理器

```sh
# 允许任意用户启动 X
# echo "allowed_users=anybody" > /etc/X11/Xwrapper.config

# 为当前用户创建 Xsession 符号链接
$ ln -s /usr/dt/bin/Xsession ~/.xinitrc

# 如需 dtlogin（图形登录界面）开机自启
# sysrc dtlogin_enable=YES
```

### 中文配置

编辑 **/etc/login.conf** 文件：找到 `default:\` 部分，将 `:lang=C.UTF-8` 修改为 `:lang=zh_CN.UTF-8`。

根据 **/etc/login.conf** 文件生成能力数据库使配置生效：

```sh
# cap_mkdb /etc/login.conf
```

## 桌面欣赏

![dtlogin](../.gitbook/assets/cde2.png)

![FreeBSD 安装 CDE](../.gitbook/assets/cde4.png)

每次启动时均会在此阶段暂停数分钟。

![FreeBSD 安装 CDE](../.gitbook/assets/cde1.png)

![终端](../.gitbook/assets/cde3.png)

## 参考文献

- FreshPorts. cde Common Desktop Environment[EB/OL]. [2026-03-25]. <https://www.freshports.org/x11/cde/>. FreshPorts 提供的 CDE 桌面环境 Port 详情与安装指南。

- FreeBSD Project. Setting up Common Desktop Environment for modern use[EB/OL]. [2026-03-25]. <https://forums.freebsd.org/threads/setting-up-common-desktop-environment-for-modern-use.69475/>. 详细配置可参考 FreeBSD 论坛相关讨论。

- CDE Project. CDE - Common Desktop Environment Wiki[EB/OL]. [2026-03-25]. <https://sourceforge.net/p/cdesktopenv/wiki/FreeBSDBuild/>. CDE 项目官方 Wiki 提供的 FreeBSD 平台构建与配置指南。

## 课后习题

1. 安装并启动 CDE 桌面环境，记录在 FreeBSD 上的使用体验。

2. 对比 CDE 与当代桌面环境（如 KDE）在系统资源占用上的差异。
   
