# 第一节 概述

### FreeBSD中的磁盘加密功能

GBDE (基于 GEOM 的磁盘加密)

内核中的 GEOM 模块 gbde(4)

用户空间工具 gbde(8)

创建后缀为 `.bde` 的新设备

GELI (GEOM eli)

内核中的 GEOM 模块

用户空间工具 geli(8)

创建后缀为`.eli`的新设备

在扇区级操作

创建新的设备以允许对数据进行纯文本访问

### GEOM 框架

访问存储层的标准化方式

GEOM 类的集合

类可以以任何顺序自由堆叠

I/O 请求转换的抽象化

变换：条带化、镜像、分区、加密

提供者和消费者

自动发现

### GBDE

主密钥（2048 个随机位）位于 GEOM 设备的一个随机位置在 GEOM 设备上，其位置存储在一个锁文件中。

锁定文件使用用户密码进行加密，并且应该 应单独存储

最多可以有 4 个独立的用户秘密(锁定扇区)

每个扇区使用 `AES-CBC-128` 和一个随机的扇区密钥进行加密。扇区密钥

扇区密钥使用从主密钥和扇区号中提取的密钥进行加密。扇区密钥使用由主密钥和扇区编号衍生的密钥进行加密

存储每个扇区密钥的磁盘空间开销

非原子性的磁盘更新，因为扇区密钥是与数据分开存储的 因为扇区密钥与数据分开存储

不支持在/文件系统中安装加密的设备系统中的加密设备

### GELI

简单的扇区对扇区加密

为了对扇区进行对称加密，选择一个随机的主密钥

主密钥使用用户密钥进行加密，并存储在 GEOM 设备的最后一个扇区中

主密钥的最多两个加密副本可以存储在扇区中

用户密钥由最多两个部分组成：一个用户口令和一个密钥文件

口令使用 PKCS #5：基于密码的密码学规范 2.0(Password-Based Cryptography Specification 2.0)来加强

加密技术规范 2.0 (RFC 2898)

可以对数据完整性进行验证

由于利用了 crypto(9)框架，自动利用硬件加速加密操作的优势

支持多种加密算法（AES-XTS,AES-CBS, Blowfish-CBC, Camellia-CBC, 3DES-CBC）和不同的密钥长度。不同的密钥长度

允许在/文件系统中挂载加密的设备

自 FreeBSD 11 支持从加密的分区启动

## GEOM 模块化磁盘变换框架及其他磁盘管理常用命令： 

```
# fdisk -s /dev/da0 #打印磁盘对象汇总信息。其中/dev/da0 即磁盘对象，表示本机的第一块硬盘，如果不写 默认显示启动盘信息。还可以写成分片或分区，如/dev/da0s1 和/dev/da0s1a，其中硬盘用 da 表示，从 0 起算，分片用 s 表示，从 1 起算，分区则用字母 a-h 表示，/dev/da0s1a 即表示第一块硬盘第一个分片的 第一个分区，这是 MBR 的表示方法。GPT 由于没有分片的概念，直接就是分区，因此用 p 表示分区， 从 1 起算，/dev/da0p1 即表示第一块硬盘的第一个分区 

# dd if=/dev/zero of=/dev/da1 bs=1k count=1 #清理磁盘信息 

# fdisk -BI /dev/da1 #初始化磁盘，默认 MBR 模式 bsdlabel -w /dev/da1s1 #写入 bsdlabel 

# bsdlabel -e /dev/da1s1 #用 vi 编辑器编辑 

# bsdlabel geom -t #树状结构显示磁盘对象关系

# geom disk lsit #列表显示已使用的物理磁盘 

# geom disk status #显示已使用的物理磁盘状态信息 

# gpart list | geom part list #列表显示已创建的分片和分区 

# gpart status | geom part status #显示已创建的分片和分区状态信息 

# gpart show /dev/da1 #显示已使用的硬盘信息 

# gpart create -s GPT /dev/da1 #为磁盘/dev/da1 创建分区表，本例为 GPT 模式，还可以设置 MBR、APM、 BSD、BSD64、LDM、VTOC8 

# gpart add -b 64 -s 2048m -t freebsd-ufs -i 2 -l root0 /dev/da1 #在磁盘/dev/da1 上创建新分区。-b 表示起始位 置；-s 表示分配空间；-t 为分区格式，分片时可以用 freebsd，还有 freebsd-boot、freebsd-swap、freebsdzfs 等类型；-i 表示索引，本例为 2，即新分区名为/dev/da1p2；-l 为标签 newfs /dev/da1p2 #格式化分区 

# gpart modify -i 2 -t freebsd-zfs -l myroot /dev/da1 #在磁盘/dev/da1 上修改索引为 2 的分区，分区格式和标签均可修改 

# gpart resize -i 2 -s 4g /dev/da1 #在磁盘/dev/da1 上调整索引为 2 的分区大小，单位可以用 k、m、g、t。注 意，如果要缩小分区，则分区不能处于使用状态，这意味着系统分区默认情况下无法缩小；如果要扩大 分区，则分区后面必须是空闲空间，而不能有其他分区，这意味着系统分区默认情况下也无法扩展。因 此在创建 FreeBSD 虚机时，应充份考虑可能使用系统盘的情况，或尽量避免使用系统盘 

# gpart bootcode -b /boot/mbr /dev/da1 #写入启动代码，常用的还有/boot/gptboot 和/boot/boot 

# gpart set -a active -i 1 /dev/da0 #设置活动分片。分区表为 MBR 时，bsdinstall 和 sade 会自动把新建的分片设置为活动分片，从而导致操作系统重启时无法正确加载启动分区，故需要重设 

# gpart delete -i 2 /dev/da1 #在磁盘/dev/da1 上删除索引为 2 的分区 

# gpart destroy -F /dev/da1 #销毁磁盘/dev/da1 上的信息，-F 参数表示强制 

# mount /dev/da1p1 /data #将分区/dev/da1p1 挂载到/data 目录，挂载后注意用 chown 命令设置归属，若希望重启后自动挂载，请在终端执行命令：
# printf "/dev/da1p1t/datattufstrwt0t0n" >> /etc/fstab 
# umount /data #卸载/data 目录上的挂载 
```


下面再给出四组示例，谨供参考： 

```
#1.MBR 在系统盘扩展分片后新建分区(假设已为系统盘增加 50G 磁盘空间) 

# gpart resize -i 1 -s 149g /dev/da0 #调整分片/dev/da0s1 的空间为 149G。尽管磁盘的大小为 150G，但由于技术原因，实际可使用的空间并没有那么多 

# gpart add -t freebsd-ufs /dev/da0s1 #在分片/dev/da0s1 上添加分区，类型 freebsd-ufs。不指定-s 参数时，表示将 剩余空间都分配给该分区 

# newfs /dev/da0s1d #格式化新分区。这里注意新分区名称，由于 a 是启动分区，b 是 swap 分区，c 已经被分 片本身占用，因此新分区默认分配为 d 
# mkdir /data 
# mount /dev/da0s1d /data 
# printf "/dev/da0s1dt/datattufstrwt2t2n" >> /etc/fstab
```

```
#2.MBR 在系统盘新建分片后再建分区(假设已为系统盘增加 50G 磁盘空间) 

# gpart add -t freebsd /dev/da0 #在次跑/dev/da0 上添加分片，类型 freebsd。不指定-s 参数时，表示将剩余空间都 分配给该分片 

# gpart create -s BSD /dev/da0s2 #设置分片生效 gpart add -t freebsd-ufs /dev/da0s2 #在分片/dev/da0s2 上添加分区，类型 freebsd-ufs。不指定-s 参数时，表示将 剩余空间都分配给该分区 

# newfs /dev/da0s2a #格式化新分区。由于当前分区是当前分片上的第一个分区，因此系统默认分配为 a 

# gpart set -a active -i 1 /dev/da0 #设置活动分片。若用 bsdinstall 或 sade 创建新分片，则此步骤为必须 
# mkdir /data mount /dev/da0s2a /data 
# printf "/dev/da0s2at/datattufstrwt2t2n" >> /etc/fstab
```
```
#3.GPT 在系统盘新建分区(假设已为系统盘增加 50G 磁盘空间) 

# gpart add -t freebsd-ufs /dev/da0 #在磁盘/dev/da0 上添加分区，GPT 中没有分片的概念 

# newfs /dev/da0p4 #格式化新分区。这里注意新分区名称，p1 是 boot 分区，p2 是系统分区，p3 是 swap 分区，因此新分区默认为 p4 
# mkdir /data mount /dev/da0p4 /data 
# printf "/dev/da0p4t/datattufstrwt2t2n" >> /etc/fstab 
```
```
#4.GPT 创建数据分区 

# gpart create -s GPT /dev/da1 #为磁盘/dev/da1 设置分区表。若想用 MBR 分区，则将-s 参数的值改为 MBR 

# gpart add -t freebsd-ufs /dev/da1 #在磁盘/dev/da1 上添加分区，类型 freebsd-ufs 
# newfs /dev/da1p1 #格式化新分区。由于当前分区是当前分片上的第一个分区，因此系统默认分配为 p1 
# mkdir /data mount /dev/da1p1 /data 
# printf "/dev/da1p1t/datattufstrwt2t2n" >> /etc/fstab
```
