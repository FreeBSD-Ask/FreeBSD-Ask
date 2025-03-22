# 第 6.7 节 ZFS 磁盘加解密

## ZFS 加密后——挂载磁盘

如果在安装 FreeBSD 的时候选择了 ZFS 磁盘加密，那么如何挂载该磁盘呢？

磁盘结构（FreeBSD 11 以后）

|     分区类型      | 挂载点 |             设备              |
| :---------------: | :----: | :---------------------------: |
| freebsd-boot /EFI |        |          /dev/ada0p1          |
|    freebsd-zfs    |   /    | /dev/ada0p2/、/dev/ada0p2.eli |
|   freebsd-swap    |        | /dev/ada0p3、/dev/ada0p3.eli  |

>**技巧**
>
>`ada` 即 SATA 硬盘。

很简单，也不需要密钥。执行命令

```sh
# geli attach /dev/ada0p3
```

然后输入正确的密码即可通过 `# zfs mount zroot/ROOT/default` 命令导入磁盘。

## 使用 GELI 加密 ZFS 卷

- 创建块设备：

```sh
# zfs create -V 256M zroot/test
```

- 查看（已忽略其他无用信息）：

```sh
# zfs list
NAME                 USED  AVAIL  REFER  MOUNTPOINT
zroot/test           262M  83.7G    56K  -
```

- 创建一个随机生成的、4K 大小的 key:

```sh
# dd if=/dev/random of=/tmp/test.key bs=4k count=1
1+0 records in
1+0 records out
4096 bytes transferred in 0.000083 secs (49072111 bytes/sec)
```

- 初始化并加载加密磁盘

```sh
# geli init -K /tmp/test.key /dev/zvol/zroot/test
Enter new passphrase: # 输入密码，密码不显示为 ***，就是什么也没有
Reenter new passphrase: # 重复输入密码，密码不显示 ***，就是什么也没有

Metadata backup for provider /dev/zvol/zroot/test can be found in /var/backups/zvol_zroot_test.eli
and can be restored with the following command:

	# geli restore /var/backups/zvol_zroot_test.eli /dev/zvol/zroot/test
```

- 使用指定的密钥文件解锁、挂载 GELI 加密的 zvol 设备

```sh
# geli attach -k /tmp/test.key /dev/zvol/zroot/test
Enter passphrase: # 输入刚才设置的密码
```

- 发现设备

```sh
# ls /dev/zvol/zroot/test.eli
/dev/zvol/zroot/test.eli
```

- 我们可以在该设备上创建一个新的文件分区

```sh
# zpool create -m /tmp/ztest ztest /dev/zvol/zroot/test.eli
```

- 查看设备

```
# geli list
Geom name: zvol/zroot/test.eli
State: ACTIVE
EncryptionAlgorithm: AES-XTS
KeyLength: 128
Crypto: accelerated software
Version: 7
UsedKey: 0
Flags: AUTORESIZE
KeysAllocated: 1
KeysTotal: 1
Providers:
1. Name: zvol/zroot/test.eli
   Mediasize: 268434944 (256M)
   Sectorsize: 512
   Mode: r1w1e1
Consumers:
1. Name: zvol/zroot/test
   Mediasize: 268435456 (256M)
   Sectorsize: 512
   Stripesize: 16384
   Stripeoffset: 0
   Mode: r1w1e1
```


## 参考文献

- [GELI — Disk Encryption in FreeBSD](https://bsd-pl.org/assets/talks/2018-11-15_0_Micha%C5%82-Borysiak_GELI-Disk-encryption-in-FreeBSD.pdf)，本文主要来自此处。没有写的部分是因为测试失败了。
