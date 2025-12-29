# FreeBSD 桌面发行版评述


## GhostBSD

GhostBSD 始于 2010 年。

GhostBSD 官网为 [https://www.ghostbsd.org](https://www.ghostbsd.org)。其口号为“A simple, elegant desktop BSD Operating System”，意为“简洁而优雅的 BSD 桌面操作系统”。

GhostBSD 曾基于 TrueOS（另一款消逝的桌面发行版），也曾使用 GNOME 作为桌面。GhostBSD 这一名称与早期 Windows 平台上常用的 Ghost 软件并无任何关联，其含义为“(G)nome (host)ed by Free(BSD)”（由 FreeBSD 驱动的 GNOME 桌面），而当前所使用的 MATE 桌面环境亦源自 GNOME 项目。GhostBSD 默认配置了 Linux 兼容层，但其使用方式与常规目录结构不同，且无法通过 chroot 直接进入，对 deb、rpm 文件的处理也无明显反馈。GhostBSD 使用 FreeBSD 的 pkg（默认软件源为 GhostBSD 镜像站）和 Ports，同时也提供了官方的图形化软件管理工具及自有的二进制软件包。

GhostBSD 的下载地址为 <https://www.ghostbsd.org/download>。GhostBSD 官方仅提供基于 MATE 桌面环境的安装镜像，社区则提供了基于 Xfce 的版本。GhostBSD 是一款滚动发行版，但更新节奏相对缓慢，基于 FreeBSD 最新的 STABLE 分支。常见问题文档在 [FAQ](https://ghostbsd-documentation-portal.readthedocs.io/en/latest/user/FAQ.html)。可以看到系统默认未安装编译工具，需要通过命令 `sudo pkg install -g 'GhostBSD*-dev'` 进行安装。

GhostBSD 至少需要 4 GB 内存才能完成安装，因为系统启动后会以内存盘方式运行。

![](../.gitbook/assets/GhostBSD1.png)

在从 ISO 启动时即可验证这一点，在将文件复制到内存盘的过程中需要等待较长时间。

开始安装：

![](../.gitbook/assets/GhostBSD2.png)

GhostBSD 默认使用的 shell 是与 POSIX 不兼容的 [fish shell](https://fishshell.com/)。

![](../.gitbook/assets/GhostBSD3.png)


## NomadBSD

NomadBSD 始于 2018 年。“Nomad”意为“游牧者、经常迁移的人”，对应其面向 U 盘的即插即用设计理念。

NomadBSD 的官网为 [https://nomadbsd.org](https://nomadbsd.org)。NomadBSD 基于 FreeBSD 最新的 RELEASE 版本，2 GB 内存即可运行，主要设计用于 LiveCD 场景，以测试 FreeBSD 的硬件兼容性。

NomadBSD 的下载地址为 [https://nomadbsd.org/download.html](https://nomadbsd.org/download.html)（页面右侧的 MANIFEST 文件列出了预装的软件）。

NomadBSD 默认采用 Xfce 桌面。

![](../.gitbook/assets/nomadbsd1.png)

  从界面来看，系统似乎支持对默认 Shell 进行自定义配置。

![](../.gitbook/assets/nomadbsd2.png)

输入法功能存在异常。

![](../.gitbook/assets/nomadbsd3.png)

## MidnightBSD

MidnightBSD 的官网为 [https://www.midnightbsd.org](https://www.midnightbsd.org)。MidnightBSD 也是一款基于 Xfce 桌面环境的发行版。~~起个名字真是太难了，而创始人的第一只猫叫 Midnight（即午夜，可能因为是只黑猫），所以就叫 MidnightBSD 啦。~~

MidnightBSD 始于 2006 年，拥有自己的二进制软件包系统——[mports](https://www.midnightbsd.org/documentation/mports/index.html)，安装过程中该选项默认启用。

MidnightBSD 的安装界面与 FreeBSD 基本一致，采用经典的蓝底白字文本界面。普通用户的默认 Shell 为 [mksh](https://github.com/MirBSD/mksh)

![](../.gitbook/assets/midnightbsd1.png)

![](../.gitbook/assets/midnightbsd2.png)

系统在首次启动时需要回答较多配置问题，例如镜像服务器所在地区、隐私数据收集选项、硬件信息提交、是否安装特定组件以及是否启用图形化桌面等。（你可以看其 ISO 镜像里的 `/etc/rc.d/firstboot` 文件）系统默认启用了 IPFW 防火墙。

若选择启用图形化桌面，系统会在安装过程中联网下载 midnightbsd-desktop 软件包，即使配置了代理，下载速度仍然较慢。pkg 命令在该系统中不可用，其功能由 mport 命令替代。通过用户级别设置更改系统语言的方法未能生效。

![](../.gitbook/assets/midnightbsd3.png)

![](../.gitbook/assets/midnightbsd4.png)


## helloSystem

helloSystem 始于 2021 年。helloSystem 在设计理念上类似于 Linux 生态中的 [Pear OS](https://pearos.xyz)。

helloSystem 项目的开发进度在一段时间内较为停滞。该项目团队甚至并未注册 helloSystem.org 域名。

helloSystem 的官网为 <https://hellosystem.github.io/docs>，同时也是他们的文档网站。下载地址位于 [GitHub Releases 页面](https://github.com/helloSystem/ISO/releases)。

helloSystem 的设计原则主要面向 macOS 用户，可概括为“桌面风格 Mac 化的 FreeBSD”。设计哲学是“少而精”。

helloSystem 基于 FreeBSD `RELEASE` 版本。默认 Shell 是 zsh。安装了 sudo。

helloSystem 运行时通常需要 4～8 GB 内存。helloSystem 在界面设计和交互逻辑上与传统发行版存在明显差异，例如在终端中，快捷键 Ctrl+C 用于复制而非中断程序，Caps Lock 键默认无效，只能通过 Shift 键输入大写字母。屏幕缩放功能也存在明显限制，无法自定义缩放比例。

![](../.gitbook/assets/hellosystem1.png)

![](../.gitbook/assets/hellosystem2.png)

![](../.gitbook/assets/hellosystem3.png)

系统无法正常设置界面语言，基于用户级别的语言设置同样未生效。

![](../.gitbook/assets/hellosystem4.png)
