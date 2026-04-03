# 3.4 安装双系统（先安装 FreeBSD）

本节介绍在同一物理设备上部署 FreeBSD 与 Windows 多操作系统的技术方案，本小节聚焦于先安装 FreeBSD、再安装其他操作系统的场景。

> **注意**
>
> 本文要求先安装 FreeBSD，再安装 Windows 或其他操作系统，请遵循此顺序进行操作。

## 安装 FreeBSD 14.2 RELEASE

首先按照以下步骤安装 FreeBSD 14.2 RELEASE 系统，本文未特别说明之处，均采用默认设置与参数，以确保系统的稳定性。

![FreeBSD 安装界面](../.gitbook/assets/shuang1.png)

![FreeBSD 安装界面](../.gitbook/assets/shuang2.png)

> **技巧**
>
> 如果在此处设置 `P Partition Scheme` 为 `GPT (UEFI)` 而非其他（只有老电脑才需要 `GPT (BIOS+UEFI)` 等选项），后续分区与系统更新过程会更加简单，也能实现 4 K 对齐。

![分区方案选择](../.gitbook/assets/shuang3.png)

这里需要设置一个大的临时交换分区，该数值表示计划中的交换分区与 Windows 系统分区容量之和。这样设置是为了后续安装 Windows 时能够直接使用这部分空间，避免额外的分区操作。在本文中，交换分区（Swap）大小为 8 GB，其余 200 GB 空间预留给 Windows。请修改 `S Swap Size` 的大小。

![交换分区大小设置](../.gitbook/assets/shuang4.png)

列出系统磁盘分区情况：

```sh
# gpart show
=>     9  639659  cd0  MBR  (1.2G)
       9  639659       - free -  (1.2G)

=>     9  639659  iso9660/14_2_RELEASE_AMD64_CD  MBR  (1.2G)
       9  639659                                 - free -  (1.2G)

=>       40  629145520  nda0 GPT  (300G)
         40     532480    1  efi  (260M)
     532520       1024    2  freebsd-boot  (512K)
     533544        984       - free -  (492K)
     534528  436207616    3  freebsd-swap  (208G)
  436742144  192401408    4  freebsd-zfs  (92G)
  629143552       2008       - free -  (1.0M)
  
```

显示交换分区和交换文件的使用情况（单位为 MB/GB）：

```sh
# swapinfo -mh
Device              Size     Used    Avail Capacity
/dev/nda0p3          208G       0B     208G     0%
```

可以看到交换分区的大小是我们所设定的 208 GB（其中 200 GB 预留给 Windows 操作系统）。

编辑 `/etc/fstab`，在 swap 对应行的行首添加 `#` 字符将其注释，本例中该行是第三行，这样可以避免系统在启动时不挂载这个大的交换分区，为后续安装 Windows 作准备：

```sh
# Device                Mountpoint      FStype  Options         Dump    Pass#
/dev/gpt/efiboot0               /boot/efi       msdosfs rw              2       2
#/dev/nda0p3             none    swap    sw              0       0
```

## 安装 Windows 11

FreeBSD 安装完成后，接下来安装 Windows 系统。

插入 Windows 启动盘，设置 BIOS 从该启动盘启动，开始安装 Windows。此时系统会识别到这块硬盘上的现有分区结构，我们只需要使用之前预留的空间。

![Windows 安装分区界面](../.gitbook/assets/shuang5.png)

在分区时，删除（Delete Partition）整个 208 GB 的交换分区（本例中为“磁盘 0 分区 3”），因为这部分空间正是我们为 Windows 预留的。

![删除交换分区](../.gitbook/assets/shuang6.png)

然后点击创建分区（Create Partition），如果提示出错，点击刷新（Refresh）即可。Windows 安装程序会自动在未分配空间上创建它需要的分区，包括 MSR 分区、系统分区和恢复分区。

然后选中 208 G 的“磁盘 0 未分配空间”，点击“下一步”进行安装。

![选择未分配空间安装 Windows](../.gitbook/assets/shuang7.png)

## 还原交换分区（Swap）

Windows 安装完成后，需要为 FreeBSD 还原交换分区。我们分配了 208 GB 空间，其中有 8 GB 是为交换分区预留的。现在需要将其还原。需要用到工具 [DiskGenius](https://www.diskgenius.com/)。

![DiskGenius 主界面](../.gitbook/assets/shuang8.png)

打开 DiskGenius，压缩 C 盘，腾出 8 GB 的未分配空间。Windows 系统安装完成后，C 盘占用了我们之前预留的大部分空间，我们只需要从 C 盘末尾压缩出 8 GB 即可。

![压缩 C 盘](../.gitbook/assets/shuang9.png)

将这 8 GB 空间格式化为 `FreeBSD Swap partition` 类型，然后点击“保存更改”。这一步操作是将新创建的交换分区标记为 FreeBSD 可以识别的类型。

![格式化交换分区](../.gitbook/assets/shuang10.png)

![保存分区更改](../.gitbook/assets/shaung11.png)

回到 FreeBSD，查看磁盘分区情况：

```sh
# gpart show
=>       34  629145533  nda0  GPT  (300G)
         34          6        - free -  (3.0K)
         40     532480     1  efi  (260M)
     532520       1024     2  freebsd-boot  (512K)
     533544        984        - free -  (492K)
     534528      32768     3  ms-reserved  (16M)
     567296  417953792     4  ms-basic-data  (199G)
  418521088   16777216     5  freebsd-swap  (8.0G)
  435298304    1441792     6  ms-recovery  (704M)
  436740096       2048        - free -  (1.0M)
  436742144  192401408     7  freebsd-zfs  (92G)
  629143552       2015        - free -  (1.0M)

```

可以看到，`nda0p5`（分区 5）即是我们新建的交换分区。测试一下，立刻启用指定交换分区 `/dev/nda0p5`：

```sh
# swapon /dev/nda0p5
```

没有报错，也没有任何提示，说明正常，系统已经可以正常识别并使用这个新的交换分区。

编辑 `/etc/fstab`，在 swap 一行最前面删去注释符号 `#`，并将分区改为正确的值，在本例中如下第三行：

```sh
# Device                Mountpoint      FStype  Options         Dump    Pass#
/dev/gpt/efiboot0               /boot/efi       msdosfs rw              2       2
/dev/nda0p5             none    swap    sw              0       0
```

重启再查看一下既有的交换分区情况：

```sh
# swapinfo -mh
Device              Size     Used    Avail Capacity
/dev/nda0p5         8.0G       0B     8.0G     0%
```

列出系统中所有 ZFS 池及其状态：

```sh
# zpool list
NAME    SIZE  ALLOC   FREE  CKPOINT  EXPANDSZ   FRAG    CAP  DEDUP    HEALTH  ALTROOT
zroot  91.5G   922M  90.6G        -         -     0%     0%  1.00x    ONLINE  -
# zfs list
NAME                 USED  AVAIL  REFER  MOUNTPOINT
zroot                922M  87.8G    96K  /zroot
zroot/ROOT           919M  87.8G    96K  none
zroot/ROOT/default   919M  87.8G   919M  /
zroot/home           224K  87.8G    96K  /home
zroot/home/ykla      128K  87.8G   128K  /home/ykla
zroot/tmp            104K  87.8G   104K  /tmp
zroot/usr            288K  87.8G    96K  /usr
zroot/usr/ports       96K  87.8G    96K  /usr/ports
zroot/usr/src         96K  87.8G    96K  /usr/src
zroot/var            668K  87.8G    96K  /var
zroot/var/audit       96K  87.8G    96K  /var/audit
zroot/var/crash       96K  87.8G    96K  /var/crash
zroot/var/log        188K  87.8G   188K  /var/log
zroot/var/mail        96K  87.8G    96K  /var/mail
zroot/var/tmp         96K  87.8G    96K  /var/tmp
```

## 课后习题

1. 研究 FreeBSD 安装程序的分区算法，尝试设计一种无需预先预留大空间、也无需后期压缩 Windows 分区的双系统安装方案，并在虚拟机环境中验证其可行性。

2. 分析 GPT 分区表中各分区类型标识的历史演变，对比 freebsd-swap 与 Linux swap 分区的实现差异，修改 swap 分区类型标识并观察系统行为变化。

3. 尝试修改 Windows 安装过程，使其在不破坏 FreeBSD ZFS 分区的情况下完成安装。
