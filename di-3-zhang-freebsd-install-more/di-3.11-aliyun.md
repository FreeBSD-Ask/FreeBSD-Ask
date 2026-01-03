# 阿里云

```sh
[root@iZuf6796zmyoxqo7fzn665Z ~]# df -Th
Filesystem     Type      Size  Used Avail Use% Mounted on
devtmpfs       devtmpfs  4.0M     0  4.0M   0% /dev
tmpfs          tmpfs     447M     0  447M   0% /dev/shm
tmpfs          tmpfs     179M  2.8M  176M   2% /run
efivarfs       efivarfs  256K  7.4K  244K   3% /sys/firmware/efi/efivars
/dev/vda3      xfs        30G  3.4G   27G  12% /
/dev/vda2      vfat      100M  7.1M   93M   8% /boot/efi
tmpfs          tmpfs      90M     0   90M   0% /run/user/0
```

```sh
[root@iZuf6796zmyoxqo7fzn665Z ~]# cat /etc/fstab

#
# /etc/fstab
# Created by anaconda on Mon May 26 09:36:59 2025
#
# Accessible filesystems, by reference, are maintained under '/dev/disk/'.
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info.
#
# After editing this file, run 'systemctl daemon-reload' to update systemd
# units generated from this file.
#
UUID=a1a902bf-090a-4942-b533-c016a4e1c142 /                       xfs     defaults0 0
UUID=638D-9E50          /boot/efi               vfat    defaults,uid=0,gid=0,umask=077,shortname=winnt 0 2
```

```sh
[root@iZuf6796zmyoxqo7fzn665Z ~]# hostnamectl
 Static hostname: iZuf6796zmyoxqo7fzn665Z
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: 37ef1ea9b706405ea6df432d1348dc03
         Boot ID: 33fa5e31444449efb3888ceca163022e
  Virtualization: kvm
Operating System: Rocky Linux 9.5 (Blue Onyx)
     CPE OS Name: cpe:/o:rocky:rocky:9::baseos
          Kernel: Linux 5.14.0-503.40.1.el9_5.x86_64
    Architecture: x86-64
 Hardware Vendor: Alibaba Cloud
  Hardware Model: Alibaba Cloud ECS
Firmware Version: 0.0.0
```

```sh
[root@iZuf6796zmyoxqo7fzn665Z ~]# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group defaultqlen 1000
    link/ether 00:16:3e:45:bc:81 brd ff:ff:ff:ff:ff:ff
    altname enp0s5
    altname ens5
    inet 172.24.0.80/18 brd 172.24.63.255 scope global dynamic noprefixroute eth0
       valid_lft 1892159248sec preferred_lft 1892159248sec
    inet6 fe80::216:3eff:fe45:bc81/64 scope link
       valid_lft forever preferred_lft forever
```

```sh
[root@iZuf6796zmyoxqo7fzn665Z ~]# ip route show
default via 172.24.63.253 dev eth0 proto dhcp src 172.24.0.80 metric 100
172.24.0.0/18 dev eth0 proto kernel scope link src 172.24.0.80 metric 100
```


```sh
[root@iZuf6796zmyoxqo7fzn665Z ~]# lspci
00:00.0 Host bridge: Intel Corporation 440FX - 82441FX PMC [Natoma] (rev 02)
00:01.0 ISA bridge: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II]
00:01.1 IDE interface: Intel Corporation 82371SB PIIX3 IDE [Natoma/Triton II]
00:01.2 USB controller: Intel Corporation 82371SB PIIX3 USB [Natoma/Triton II] (rev 01)
00:01.3 Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 03)
00:02.0 VGA compatible controller: Cirrus Logic GD 5446
00:03.0 Communication controller: Red Hat, Inc. Virtio console
00:04.0 SCSI storage controller: Red Hat, Inc. Virtio block device
00:05.0 Ethernet controller: Red Hat, Inc. Virtio network device
00:06.0 Unclassified device [00ff]: Red Hat, Inc. Virtio memory balloon
```


```sh
# wget https://mirrors.nju.edu.cn/github-release/ventoy/Ventoy/Ventoy%201.1.10%20release/ventoy-1.1.10-linux.tar.gz

```
