# 第十节 腾讯云轻量云及其他服务器 dd 安装 FreeBSD


**忠告：如果你还不懂什么是 dd，不建议食用本文。这一切超越了您的动手能力和知识储备。此外，不再受安全支持的版本如`9.2`，请参考本文并结合手动安装 FreeBSD 章节操作。**

## 视频教程

{% embed url="http://b23.tv/zcfHa4K" %}

## 文字教程

腾讯云轻量云以及阿里云等机器都没有 FreeBSD 系统的支持，只能通过特殊的的方法自己暴力安装。请注意数据安全，以下教程有一定危险性和要求你有一定的动手能力。

他是一个服务器面板里没有 FreeBSD 镜像 IDC，所以要用奇怪的方法来安装了。因为 FreeBSD 和 Linux 的内核不通用，可执行文件也不通用，所以无法通过 chroot 再删掉源系统的方法安装。安装的方法是先在内存盘中启动 FreeBSD 系统，也就是 [mfsBSD](https://mfsbsd.vx.sk)，再格式化硬盘安装新系统。mfsBSD 是一个完全载入内存的 FreeBSD 系统，类似于 Windows 中的 PE。

我们需要下载 [img 格式的 mfsBSD 镜像](https://mfsbsd.vx.sk/files/images/13/amd64/mfsbsd-se-13.0-RELEASE-amd64.img)，我也不知道 mfsBSD 的服务器在国内连接如何，所以就把文件先传到了另一台国内的文件服务器上。

### 为什么不能直接 dd？（错误示范）

我试了在正常的 Linux 系统内直接把 mfsBSD 的 img dd 到硬盘里，重启之后虽然正常加载 bootloader，但是可能是因为系统又对硬盘进行了写入而无法正常挂载内存盘。

```
# wget https://mfsbsd.vx.sk/files/images/13/amd64/mfsbsd-se-13.0-RELEASE-amd64.img -O- | dd of=/dev/vda
```

这里的 `|` 是管道的意思，将上一个命令的标准输出作为下一个命令的标准输入。`-O-` 指把文件下载输出到标准输出，而 dd 没有指定 if 时会自动从标准输入读取内容。

![](../.gitbook/assets/1.png)

### 真正的 mfsBSD 启动方法

就是因为刚才说的问题，而且 FreeBSD 和一般的 Linux 是不同的生态，我们需要先进入一个 Linux 的内存盘，再在内存中运行的 Linux 里将 mfsBSD 写入硬盘。

就在 mfsBSD 下载位置的下方，有一个 [mfsLinux](https://mfsbsd.vx.sk/files/iso/mfslinux/mfslinux-0.1.9-dd4a135.iso)，就是我们可以用的工具。由于它只有 ISO 格式，没法直接放在当前环境下启动，而它说自己是纯 initrd 类型的，我们就把启动它的 initrd 和内核提取出来，放在硬盘里手动启动。

我们知道在一般的 Linux 系统中，initrd 是一个打包成内存盘的微型但完整的 Linux 根目录，里面有一些比如说加载驱动，挂载硬盘，以及启动初始化程序的必要数据。开机时内核与 initrd 被 Bootloader 加载，initrd 中的脚本进行启动的准备工作并运行硬盘里的初始化程序。

我们先把从那个 ISO 提取出来的内核和 initrd 文件放在根目录比如说 qwq 这个文件夹下，然后重启机器进入 GRUB 的命令行界面（可以在倒计时的时候按`e`进入编辑模式，删掉所有`linux`、`initrd`行原有内容，写完后按'Ctrl X'即可加载），手动启动指定的内核和 initrd（可以用`Tab`键补全路径）。

```
linux (hd0,msdos1)/qwq/vmlinuz
initrd (hd0,msdos1)/qwq/initramfs.igz
boot
```

![](../.gitbook/assets/2.png)

这个特制的 initrd 启动之后并没有加载本地的系统，而是自己连接了网络并打开 ssh 服务器。于是我们就获得了一个运行在内存中的 Linux 系统。

这个时候服务器应该就可以被 ssh 连接上了，并且可以安全的格式化硬盘。

mfsBSD 和 mfsLinux 镜像的 root 密码默认是 `mfsroot`

```
# cd /tmp
# wget https://mfsbsd.vx.sk/files/images/13/amd64/mfsbsd-se-13.0-RELEASE-amd64.img
# dd if=mfsbsd-se-13.0-RELEASE-amd64.img of=/dev/vda
# reboot
```
**提示：建议在此处使用服务器的“快照”功能对服务器进行备份，以防以下教程操作失误重来耽误时间。**

### 安装 FreeBSD

等待系统初始化完成之后就可以 ssh 上去了，不过还需要一个步骤才能正常安装（不然走完安装向导会报错）

我们还需要下载 FreeBSD 的安装清单文件。

```
# mkdir -p /usr/freebsd-dist
# cd /usr/freebsd-dist
# fetch http://ftp.freebsd.org/pub/FreeBSD/releases/amd64/13.0-RELEASE/MANIFEST
```

最后执行 `# bsdinstall` 进行正常的安装即可（最好使用自动 ufs 分区）。请注意大多数服务器如本文的示例腾讯云轻量云，是不支持 UEFI 的，仍然使用传统的 BIOS；另外请使用 ufs，zfs 安装时会出错。

