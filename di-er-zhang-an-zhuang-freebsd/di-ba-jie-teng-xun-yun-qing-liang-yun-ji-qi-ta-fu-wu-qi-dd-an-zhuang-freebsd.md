# 第八节 腾讯云轻量云及其他服务器 dd 安装 FreeBSD

之前给云服务器刷了 Arch Linux，现在感觉 Arch 维护太麻烦了，因为包更新比较快，虽然没有滚炸，但是更新之后也会因为需要重启而无法使用一些功能。听说 FreeBSD 稳如大黄狗，所以今天打算给服务器安装 FreeBSD。

又是一个服务器面板里没有镜像的系统，又要用奇怪的方法来安装了。因为 FreeBSD 和 Linux 的内核不通用，可执行文件也不通用，所以无法通过 chroot 再删掉源系统的方法安装。安装的方法是先在内存盘中启动 FreeBSD 系统，也就是 [mfsBSD](https://mfsbsd.vx.sk)，再格式化硬盘安装新系统。mfsBSD 是一个完全载入内存的 FreeBSD 系统，类似于 Windows 中的 PE。

我们需要下载 [img 格式的 mfsBSD 镜像](https://mfsbsd.vx.sk/files/images/13/amd64/mfsbsd-se-13.0-RELEASE-amd64.img)，我也不知道 mfsBSD 的服务器在国内连接如何，所以就把文件先传到了另一台国内的文件服务器上。

### 踩坑

我试了在正常的 Linux 系统内直接把 mfsBSD 的 img dd 到硬盘里，重启之后虽然正常加载 bootloader，但是可能是因为系统又对硬盘进行了写入而无法正常挂载内存盘。

```bash
wget https://mfsbsd.vx.sk/files/images/13/amd64/mfsbsd-se-13.0-RELEASE-amd64.img -O- | dd of=/dev/vda
```

这里的 `|` 是管道的意思，将上一个命令的标准输出作为下一个命令的标准输入。`-O-` 指把文件下载输出到标准输出，而 dd 没有指定 if 时会自动从标准输入读取内容。

![](../.gitbook/assets/1.png)

### 真正的 mfsBSD 启动方法

就是因为刚才说的问题，而且 FreeBSD 和一般的 Linux 是不同的生态，我们需要先进入一个 Linux 的内存盘，再在内存中运行的 Linux 里将 mfsBSD 写入硬盘。

就在 mfsBSD 下载位置的下方，有一个 [mfsLinux](https://mfsbsd.vx.sk/files/iso/mfslinux/mfslinux-0.1.9-dd4a135.iso)，就是我们可以用的工具。由于它只有 ISO 格式，没法直接放在当前环境下启动，而它说自己是纯 initrd 类型的，我们就把启动它的 initrd 和内核提取出来，放在硬盘里手动启动。

我们知道在一般的 Linux 系统中，initrd 是一个打包成内存盘的微型但完整的 Linux 根目录，里面有一些比如说加载驱动，挂载硬盘，以及启动初始化程序的必要数据。开机时内核与 initrd 被 Bootloader 加载，initrd 中的脚本进行启动的准备工作并运行硬盘里的初始化程序。

我们先把从那个 ISO 提取出来的内核和 initrd 文件放在根目录比如说 qwq 这个文件夹下，然后重启机器进入 GRUB 的命令行界面，手动启动指定的内核和 initrd。

```
linux (hd0,msdos1)/qwq/vmlinuz
initrd (hd0,msdos1)/qwq/initramfs.igz
boot
```

这个特制的 initrd 启动之后并没有加载本地的系统，而是自己连接了网络并打开 ssh 服务器。于是我们就获得了一个运行在内存中的 Linux 系统。

这个时候服务器应该就可以被 ssh 连接上了，并且可以安全的格式化硬盘。

（mfsBSD 和 mfsLinux 镜像的 root 密码默认是 `mfsroot`

```bash
cd /tmp
wget https://mfsbsd.vx.sk/files/images/13/amd64/mfsbsd-se-13.0-RELEASE-amd64.img
dd if=mfsbsd-se-13.0-RELEASE-amd64.img of=/dev/vda
reboot
```

![](../.gitbook/assets/2.png)

### 安装 FreeBSD

等待系统初始化完成之后就可以 ssh 上去了，不过还需要一个步骤才能正常安装（不然走完安装向导会报错）

我们需要下载 FreeBSD 的安装清单文件。

其实直接在自己电脑上[下载](http://ftp.freebsd.org/pub/FreeBSD/releases/amd64/12.0-RELEASE/MANIFEST)之后把内容贴上去

```bash
mkdir -p /usr/freebsd-dist
ee /usr/freebsd-dist/MANIFEST
```

ee 是 FreeBSD 中自带的文本编辑器，有点像 nano，总之上手就会用的。

最后执行 `bsdinstall` 进行正常的安装即可。
