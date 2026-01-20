# 3.5 手动安装双系统（后安装 FreeBSD）

本文以 `FreeBSD-14.2-RELEASE-amd64-disc1.iso` 为例，演示了如何在 UEFI 环境下，安装 FreeBSD 14.2 RELEASE 与 Windows 11 24H2 双系统。

>**技巧**
>
>本文示例要求先安装其他操作系统（如 Windows），再安装 FreeBSD。

## 简单方法（无众多数据集）

> **注意**
>
> 以此部分所述方法，在使用 ZFS 时，只会创建一个名为 `zroot` 的存储池（zpool），并在其中创建一个直接挂载到 `/` 的名为 `root` 的数据集。不会像自动安装那样创建 `zroot/ROOT/default` 以及众多的数据集。你可以在安装后创建数据集并进行替换操作，但若希望初始布局就与自动安装相同，请跳转至本节“Shell 分区”部分。

首先需要在硬盘上为 FreeBSD 预留空间。该空间不一定位于硬盘末尾，中间位置亦可，因为典型的 Windows 安装中最后一个分区（本例为 `nda0p4`）通常是恢复分区。

分区完成后，在 FreeBSD 下查看磁盘分区情况，结果如下：

```sh
# gpart show
=>       34  419430333  nda0  GPT  (200G)
         34       2014        - free -  (1.0M)
       2048     204800     1  efi  (100M) # EFI 分区
     206848      32768     2  ms-reserved  (16M) # MSR 分区
     239616  207992832     3  ms-basic-data  (99G) # 此为 C 盘（NTFS 数据分区）。此处已为其后的 FreeBSD 预留了约 100G 空间。
  417947648    1478656     4  ms-recovery  (722M) # 恢复分区
  419426304       4063        - free -  (100G)
```

你应关闭安全启动和快速启动。或者，也可通过 Windows 设置 → 更新与安全 → 恢复 → 高级启动，选择从 U 盘设备启动。然后正常引导 FreeBSD 安装程序，直至进入分区选择界面。

![](../.gitbook/assets/shuangxitong1.png)

此处选择 `Manual`

>**技巧**
>
>其实这里调用的是软件 `sade`（sysadmins disk editor，系统管理员磁盘编辑器），`bsdconfig` 中的分区模块亦调用此工具。

此处可查看硬盘分区情况。图中仅有一块硬盘，包含一个 300M 的 EFI 系统分区、一个 16M 的 MSR 分区、一个 64G 的 Windows 系统分区（即 C 盘）以及未显示的空闲空间。直接选择 `Create`（创建）。

![](../.gitbook/assets/shuangxitong2.png)

此处在第一行输入分区类型（即下方会列出的 `Filesystem type`）。如需添加 swap 分区，请在此步骤首先添加，后添加难以控制分区大小。在添加 UFS 或 ZFS 分区时，需在 `Mountpoint` 处填写 `/`，表示将该分区挂载到根目录。`Label` 是 FreeBSD 的卷标（gptlabel），用于方便识别分区，可根据需要填写或留空。此处使用 ZFS，不添加 swap 分区，并且填入卷标 `zroot`。

![](../.gitbook/assets/shuangxitong3.png)

使用 **Tab 键** 将焦点移动到 `OK`，然后按回车键确认。

![](../.gitbook/assets/shuangxitong4.png)

此处会警告 ZFS 分区可能无法启动，但经实测可以正常启动。选择 `Yes` 忽略此警告：

![](../.gitbook/assets/shuangxitong5.png)

>**注意**
>
>请将 Windows 创建的 300M EFI 系统分区的挂载点设置为 `/boot/efi`。

选择 `Finish`（完成）

![](../.gitbook/assets/shuangxitong6.png)

选择 `Commit`（确认）

![](../.gitbook/assets/shuangxitong7.png)


之后会进入正常安装的流程。安装完成后列出系统中所有 ZFS 池及其状态：

```sh
# zfs list
NAME  USED   AVAIL  REFER  MOUNTPOINT
root  534M    130G   534M  none
```

进入系统后可以看到，仅有一个 `root` 数据集。可以手动将数据集改为自动安装的样子，亦可参照下文在安装时进入 shell 进行分区。

## Shell 分区

仍进行到分区选择界面，此时选择 `Shell`

![](../.gitbook/assets/shuangxitong9.png)

之后将进入终端（TTY）：

![](../.gitbook/assets/shuangxitong10.png)

执行以下命令。

### 加载 ZFS 内核模块

默认的安装镜像可能未默认启用 ZFS，让我们现在就加载 ZFS 内核模块：

```sh
# kldload zfs
```

### 配置 ZFS 对齐方式（只影响新创建的硬盘分区）

强制 ZFS 文件系统使用 4K 对齐：

```sh
# sysctl vfs.zfs.vdev.min_auto_ashift=12
vfs.zfs.vdev.min_auto_ashift: 9 -> 12
```

>**技巧**
>
> 参数 `12` 表示 2^12 = 4096 字节（4KB）的扇区大小。默认参数（可通过命令 `sysctl vfs.zfs.vdev.min_auto_ashift` 查看）是 `9`，即 2^9 = 512 字节。

>**思考题**
>
>若使用 NVMe 硬盘，新装系统（UEFI+GPT，无 freebsd-boot 分区）的该默认参数通常为 12。但 4K 对齐究竟对齐的是什么？因为 SSD 并无传统机械硬盘的物理扇区概念。

### 创建交换分区

在 nda0 磁盘上创建 4GB，4K 对齐的 FreeBSD 交换分区，并将其标记为 swap：

```sh
# gpart add -a 4k -l swap -s 4G -t freebsd-swap nda0
```

选项说明：

- `-t` 指定类型
- `-l` 指定卷标
- `-s` 指定大小
- `-a` 指定对齐

请注意根据实际情况替换 `nda0` 为实际硬盘编号。


### 创建 ZFS 分区

在 nda0 磁盘上创建 4K 对齐的 FreeBSD ZFS 分区，并标记为 zroot：

```sh
# gpart add -a 4k -l zroot -t freebsd-zfs nda0
```

将设置使用全部空余空间，请注意替换 nda0 为实际硬盘编号。

#### 查看分区情况

显示系统磁盘分区情况：

```sh
# gpart show
=>       34  419430333  nda0  GPT  (200G)
         34       2014        - free -  (1.0M)
       2048     204800     1  efi  (100M)
     206848      32768     2  ms-reserved  (16M)
     239616  207992832     3  ms-basic-data  (99G)
  208232448    8388608     5  freebsd-swap  (4.0G)
  216621056  201326592     6  freebsd-zfs  (96G)
  417947648    1478656     4  ms-recovery  (722M)
  419426304       4063        - free -  (2.0M)
```

### 挂载临时文件系统准备安装

挂载一个临时文件系统（tmpfs）：
  
```sh
# mount -t tmpfs tmpfs /mnt
```

### 创建 ZFS 池

创建 ZFS 池 zroot：

```sh
# zpool create -f -o altroot=/mnt -O compress=lz4 -O atime=off -m none zroot /dev/gpt/zroot
```

该命令将设置 zroot 池的挂载点为 `/mnt`，启用 LZ4 压缩，关闭访问时间记录。

选项说明如下：

- `-o altroot=/mnt` 将其临时挂载至 /mnt；
- `-O compress=lz4` 启用 lz4 压缩（可换为 zstd 等）；
- `-O atime=off` 关闭访问时间记录；
- `-m none` 不设置挂载点；
- `/dev/gpt/zroot` 为刚创建的分区。

### 创建 ZFS 数据集

以下数据集的设置参照 FreeBSD 源代码中的 [usr.sbin/bsdinstall/scripts/zfsboot](https://github.com/freebsd/freebsd-src/blob/main/usr.sbin/bsdinstall/scripts/zfsboot) [备份](https://web.archive.org/web/20260120012933/https://github.com/freebsd/freebsd-src/blob/main/usr.sbin/bsdinstall/scripts/zfsboot) 进行创建，因为 FreeBSD 本身的开发是持续不断的，所以 FreeBSD 不同版本间的 ZFS 数据集也有所差异。读者在创建数据集时若希望创建与默认安装相同的数据集结构，应参照对应分支的 `usr.sbin/bsdinstall/scripts/zfsboot` 文件。


- 创建根数据集

```sh
# zfs create -o mountpoint=none zroot/ROOT
```

将创建数据集 `zroot/ROOT`，不设置挂载点（`mountpoint=none`）。

此类无具体挂载点的数据集通常作为系统根数据集的容器，其下将创建具体用于挂载的子数据集或起到排除作用。


- 创建默认根数据集

```sh
# zfs create -o mountpoint=/ zroot/ROOT/default
```

将创建数据集 `zroot/ROOT/default`，将其挂载到根目录 `/`。此数据集将作为系统的默认根文件系统。


- 创建 `/home` 数据集

```sh
# zfs create -o mountpoint=/home zroot/home
```

将创建数据集 `zroot/home`，并将其挂载到 `/home`，通常用于存储用户主目录。

- 创建 `/tmp` 数据集

```sh
# zfs create -o mountpoint=/tmp -o exec=on -o setuid=off zroot/tmp
```

创建数据集 `zroot/tmp`，并将其挂载到 `/tmp`，允许执行文件（`exec=on`），但禁用 setuid（`setuid=off`）防止该目录中的文件使用 setuid 提升权限。

- 创建 `zroot/usr` 数据集

```sh
# zfs create -o mountpoint=/usr -o canmount=off zroot/usr
```

将创建 `zroot/usr` 数据集，`canmount` 即禁止自动挂载。


- 创建 `/usr/ports` 数据集

```sh
# zfs create -o setuid=off zroot/usr/ports
```

将创建 `/usr/ports` 数据集，禁用 setuid（`setuid=off`）。

- 为 ports 下的部分文件夹关闭压缩功能

```sh
# zfs create -o compress=off zroot/usr/ports/distfiles
# zfs create -o compress=off zroot/usr/ports/packages
```

在 ZFS 上创建数据集 `zroot/usr/ports/distfiles` 和 `zroot/usr/ports/packages`。

参数 `-o compress=off` 表示关闭压缩功能，因为存储的文件本身已是经过压缩的。


- 创建 `/usr/src` 数据集

```sh
# zfs create zroot/usr/src
```

将创建 `/usr/src` 数据集。

- 创建 `/var` 数据集

```sh
# zfs create -o mountpoint=/var -o canmount=off zroot/var
```

将创建 `/var` 数据集，`canmount` 意味着不会自动挂载。


- 创建 `/var/audit` 数据集

```sh
# zfs create -o exec=off -o setuid=off zroot/var/audit
```

将创建 `/var/audit` 数据集，禁用执行（`exec=off`），同时禁用 setuid（`setuid=off`）。

- 创建 `/var/crash` 数据集

```sh
# zfs create -o exec=off -o setuid=off zroot/var/crash
```

将创建 `/var/crash` 数据集，禁用执行（`exec=off`），同时禁用 setuid（`setuid=off`）。

- 创建 `/var/log` 数据集

```sh
# zfs create -o exec=off -o setuid=off zroot/var/log
```

将创建 `/var/log` 数据集，禁用执行（`exec=off`），同时禁用 setuid（`setuid=off`）。

- 创建 `/var/tmp` 数据集

```sh
# zfs create -o setuid=off zroot/var/tmp
```

将创建 `/var/tmp` 数据集，同时禁用 setuid（`setuid=off`）。

- 创建 `/var/mail` 数据集

```sh
# zfs create -o atime=on zroot/var/mail
```

将创建 `zroot/var/mail` 数据集，并启用访问时间记录（`atime=on`），通常用于存放邮件数据。


>**技巧**
>
>上述参数参考自 [bsdinstall(8)](https://man.freebsd.org/cgi/man.cgi?bsdinstall(8)) 的默认配置。安装后，也可通过命令 `zfs get exec,setuid,mountpoint` 查看相关属性。具体代码位于 `/usr/src/usr.sbin/bsdinstall/scripts/zfsboot`。

### 修改文件夹权限

将 `/mnt/tmp` 和 `/mnt/var/tmp` 的权限设置为 `1777`（粘滞位），以确保临时目录权限正确：

```sh
# chmod 1777 /mnt/tmp        # 设置 /mnt/tmp 目录为粘滞位，可读写
# chmod 1777 /mnt/var/tmp    # 设置 /mnt/var/tmp 目录为粘滞位，可读写
```

### 设置交换分区到 `fstab`

将交换分区 `/dev/nda0p5` 添加到临时的 fstab 文件：

```sh
# printf "/dev/nda0p5\tnone\tswap\tsw\t0\t0\n" >> /tmp/bsdinstall_etc/fstab
```

注意将 `/dev/nda0p5` 替换为实际的交换分区设备名，可使用 `gpart show nda0` 命令进行确认。

>**技巧**
>
>`\t` 是制表符（Tab）的转义字符（意味着按了一下 **TAB** 键），用于对齐字段，使用空格亦可达到相同效果。也可使用 `ee /tmp/bsdinstall_etc/fstab` 命令手动编辑该文件并写入如下格式的行：
>
>```sh
>/dev/nda0p5  none  swap  sw  0  0
>```
>
>下同。

### 设置启动项与 UEFI

- 设置 ZFS 池的引导文件系统（bootfs）为 `zroot/ROOT/default`：

```sh
# zpool set bootfs=zroot/ROOT/default zroot
```

- 配置系统在启动时启用 ZFS 服务。

```sh
# printf 'zfs_enable="YES"\n' >> /tmp/bsdinstall_etc/rc.conf
```

`\n` 代表 Unix/Linux 系统中的换行符。

Windows 文本文件的行尾通常是 `\r\n`（回车 + 换行）。

此命令效果等同于使用 `ee /tmp/bsdinstall_etc/rc.conf` 编辑该文件并添加一行 `zfs_enable="YES"`。

- 挂载现有的 EFI 系统分区：

```sh
# mount -t msdosfs /dev/nda0p1 /media
```

注意将 `/dev/nda0p1` 替换为实际的 EFI 分区设备名。

- 在 EFI 系统分区中为 FreeBSD 创建启动目录

```sh
# mkdir -p /media/efi/freebsd
```


- 将 FreeBSD 的 EFI 启动文件复制到启动目录

```sh
# cp /boot/loader.efi /media/efi/freebsd/
```

- 使用 efibootmgr 工具向主板 UEFI 固件添加启动项 “FreeBSD”。

```
# efibootmgr --create --activate --label "FreeBSD" --loader "/media/efi/freebsd/loader.efi"
```


- 卸载 EFI 系统分区

```sh
# umount /media
```


- 退出 Shell

```sh
# exit  
```

安装程序将自动继续后续流程。


### 完成

至此，我们便手动创建了一套与自动安装程序基本相同的 ZFS 数据集结构（自动安装通常还会创建独立的 `/home/用户名` 数据集，此处未包含）。

显示安装后系统的 ZFS 文件系统状态：

```sh
# zfs list
NAME                 USED  AVAIL  REFER  MOUNTPOINT
zroot                921M  91.6G    96K  none
zroot/ROOT           919M  91.6G    96K  none
zroot/ROOT/default   919M  91.6G   919M  /
zroot/home           128K  91.6G   128K  /home
zroot/tmp            104K  91.6G   104K  /tmp
zroot/usr            288K  91.6G    96K  /usr
zroot/usr/ports       96K  91.6G    96K  /usr/ports
zroot/usr/src         96K  91.6G    96K  /usr/src
zroot/var            636K  91.6G    96K  /var
zroot/var/audit       96K  91.6G    96K  /var/audit
zroot/var/crash       96K  91.6G    96K  /var/crash
zroot/var/log        156K  91.6G   156K  /var/log
zroot/var/mail        96K  91.6G    96K  /var/mail
zroot/var/tmp         96K  91.6G    96K  /var/tmp
```


## 参考文献

- [How to manually install FreeBSD on a remote server (with UFS, ZFS, encryption...)](https://stanislas.blog/2018/12/how-to-install-freebsd-server/) [备份](https://web.archive.org/web/20260117184103/https://stanislas.blog/2018/12/how-to-install-freebsd-server/)
- [RootOnZFS/GPTZFSBoot](https://wiki.freebsd.org/RootOnZFS/GPTZFSBoot) [备份](https://web.archive.org/web/20251202034128/https://wiki.freebsd.org/RootOnZFS/GPTZFSBoot)
