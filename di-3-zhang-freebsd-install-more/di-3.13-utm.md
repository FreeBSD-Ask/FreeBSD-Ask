# 3.13 基于 Apple M1 和 UTM 安装 FreeBSD

首先下载FreeBSD的安装介质镜像。注意自己下载的是 aarch64 的还是 amd64 的，除非有特殊需求，建议下载 aarch64 的，相同架构速度快一些，性能损失小。

![下载安装镜像](../.gitbook/assets/install_bsd_on_utm/0.png)

接下来新建一个虚拟机，点击窗口上的加号。

![新建虚拟机](../.gitbook/assets/install_bsd_on_utm/1.png)

如果你下载的是 aarch64 的镜像，选择“虚拟化”，如果是 amd64 的镜像，选择“模拟”。

![选择虚拟化类型](../.gitbook/assets/install_bsd_on_utm/2.png)

操作系统选择“其他”。

![选择操作系统](../.gitbook/assets/install_bsd_on_utm/3.png)

内存默认的4GB能适应大多数情况，初始状态下 FreeBSD 15 会占用大约 500M 的内存，有需求可以自己增加或者减少内存。CPU 核心按需设置，M1 芯片可以设置成 4 。

![设置内存和处理器核心数](../.gitbook/assets/install_bsd_on_utm/4.png)

启动设备选择 CD/DVD 映像 ，点击“浏览”按钮选择你下载好的安装介质镜像。

![设置启动设备](../.gitbook/assets/install_bsd_on_utm/5.png)

存储空间默认 64GB ，初始状态 FreeBSD 会使用 5GB 左右的空间，可以根据需求调节。

![设置存储空间](../.gitbook/assets/install_bsd_on_utm/6.png)

共享目录可以暂时跳过。

![跳过共享目录](../.gitbook/assets/install_bsd_on_utm/7.png)

以上步骤设置完以后点击存储即可，想要进一步设置可以勾选“打开虚拟机设置”，或者点击存储以后点击右上角设置按钮打开设置。

![结束设置](../.gitbook/assets/install_bsd_on_utm/8.png)

点击大大的播放按钮即可启动虚拟机。

![启动虚拟机](../.gitbook/assets/install_bsd_on_utm/9.png)

![虚拟机启动界面](../.gitbook/assets/install_bsd_on_utm/10.png)

启动 FreeBSD 安装介质镜像，按 Enter 可以跳过三秒的等待时间。

![系统引导界面](../.gitbook/assets/install_bsd_on_utm/11.png)

进入安装程序，鼠标默认可用，可以按下 Control + Option 快捷键捕获鼠标光标，再次按下此快捷键即可解除捕获。

![安装程序界面](../.gitbook/assets/install_bsd_on_utm/12.png)