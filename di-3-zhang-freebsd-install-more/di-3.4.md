# 3.4 手动安装双系统（先安装 FreeBSD）

>**注意**
>
>本文要求先安装 FreeBSD，再安装 Windows 或其他操作系统。

## 安装 FreeBSD 14.2 RELEASE

本文未特别说明的，皆为正常设置与参数。

![](../.gitbook/assets/shuang1.png)

![](../.gitbook/assets/shuang2.png)

>**技巧**
>
>如果在此处设置 `P Partition Scheme` 为 `GPT (UEFI)` 而非其他（只有老电脑才需要 `GPT (BIOS+UEFI)` 等选项），后续分区与系统更新过程会更加简单，也能实现 4K 对齐。


![](../.gitbook/assets/shuang3.png)

在这一步修改 `S Swap Size` 的大小（计算方法为 swap 大小 + Windows 大小）。

本文中，交换分区（Swap）占 8G，其他的 200G 留给 Windows。

![](../.gitbook/assets/shuang4.png)


查看磁盘分区：

```sh
root@ykla:/home/ykla # gpart show
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

查看交换分区：

```sh
root@ykla:/home/ykla # swapinfo -mh
Device              Size     Used    Avail Capacity
/dev/nda0p3          208G       0B     208G     0%
```

可以看到交换分区的大小是我们所设定的 208GB。

编辑 `/etc/fstab`，在 swap 一行最前面加上 `#`，在本例中如下第三行：

```sh
# Device                Mountpoint      FStype  Options         Dump    Pass#
/dev/gpt/efiboot0               /boot/efi       msdosfs rw              2       2
#/dev/nda0p3             none    swap    sw              0       0
```

## 安装 Windows 11

插入 Windows 启动盘，设置 BIOS 从中启动，开始安装 Windows。

![](../.gitbook/assets/shuang5.png)

在分区时，删除（Delete Partition）整个 208G 的交换分区（本例中为“磁盘 0 分区 3”）。

![](../.gitbook/assets/shuang6.png)

然后点击创建分区（Create Partition），如果提示出错，请点击刷新（Refresh）即可。

然后选中 208G 的“磁盘 0 未分配空间”，点击“下一步”进行安装。

![](../.gitbook/assets/shuang7.png)

## 还原交换分区（Swap）

我们设置了 208G，很明显有 8G 是为 swap 创设的。现在需要将其还原。需要用到 [diskgenius](https://www.diskgenius.com/)。

![](../.gitbook/assets/shuang8.png)

打开 diskgenius，压缩 C 盘，空出 8G 剩余空间。

![](../.gitbook/assets/shuang9.png)


将这 8G 剩余空间格式化为 `FreeBSD Swap partition`，然后点击“保存更改”。

![](../.gitbook/assets/shuang10.png)

![](../.gitbook/assets/shaung11.png)

回到 FreeBSD，查看磁盘：

```sh
root@ykla:/home/ykla # gpart show
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

可以看到，nda0p5（分区 5）是我们新的 swap。测试一下：

```sh
root@ykla:/home/ykla # swapon /dev/nda0p5
```

没有报错，也没有任何提示，说明正常。

编辑 `/etc/fstab`，在 swap 一行最前面去掉 `#`，并将分区改为正确的，在本例中如下第三行：

```sh
# Device                Mountpoint      FStype  Options         Dump    Pass#
/dev/gpt/efiboot0               /boot/efi       msdosfs rw              2       2
/dev/nda0p5             none    swap    sw              0       0
```

重启测试一下：

```sh
root@ykla:/home/ykla # swapinfo -mh
Device              Size     Used    Avail Capacity
/dev/nda0p5         8.0G       0B     8.0G     0%
```

查看 ZFS 卷：

```sh
root@ykla:/home/ykla # zpool list
NAME    SIZE  ALLOC   FREE  CKPOINT  EXPANDSZ   FRAG    CAP  DEDUP    HEALTH  ALTROOT
zroot  91.5G   922M  90.6G        -         -     0%     0%  1.00x    ONLINE  -
root@ykla:/home/ykla # zfs list
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

