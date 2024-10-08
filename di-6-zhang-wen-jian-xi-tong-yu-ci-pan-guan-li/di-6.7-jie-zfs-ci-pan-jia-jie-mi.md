# 第 6.7 节 ZFS 磁盘加解密

## ZFS 加密后-挂载磁盘

如果在安装的时候选择了 ZFS 磁盘加密，那么如何挂载该磁盘呢？

磁盘结构（FreeBSD 11 以后）

|     分区类型      | 挂载点 |             设备              |
| :---------------: | :----: | :---------------------------: |
| freebsd-boot /EFI |        |          /dev/ada0p1          |
|    freebsd-zfs    |   /    | /dev/ada0p2/、/dev/ada0p2.eli |
|   freebsd-swap    |        | /dev/ada0p3、/dev/ada0p3.eli  |

很简单，也不需要密钥。

执行命令 `# geli attach /dev/ada0p3`

然后输入正确的密码即可通过 `zfs mount zroot/ROOT/default` 命令导入磁盘。

## 使用 GELI 加密 ZFS 卷

```sh
# 创建一个块设备
# zfs create -V 256M zroot/test
# 创建一个随机生成的、4K 大小的 key
# dd if=/dev/random of=/tmp/test.key bs=4k count=1
# 初始化并加载加密磁盘
# geli init -K /tmp/test.key /dev/zvol/zroot/test
# geli attach -k /tmp/test.key /dev/zvol/zroot/test
# 发现一个新设备
# ls /dev/zvol/zroot/test.eli
# 我们可以在该设备上创建一个新的文件分区
# zpool create -m /tmp/ztest ztest /dev/zvol/zroot/test.eli
```

## GELI 数据备份和恢复

```sh
# 备份 GELT 数据
# geli backup /dev/zvol/zroot/test /tmp/test.eli
# 清空 GELT 数据
# geli clear /dev/zvol/zroot/test
# GELI尝试挂载 GELT设备，但无法做到，因为找不到他的 GELT 数据
# geli attach -k /tmp/test.key /dev/zvol/zroot/test
# 恢复 GELT 数据
# geli restore /tmp/test.eli /dev/zvol/zroot/test
# 现在我们可以挂载设备并导入池了
# geli attach -k /tmp/test.key /dev/zvol/zroot/test
# zpool import
```

## 调整 GELI 磁盘大小

```sh
# 调整 ZFS 卷
# zfs set volsize=512M zroot/test
# 现在还不能挂载 GELT 设备，因为 GELT 找不到数据
# geli attach /dev/zvol/zroot/test
# 我们需要告诉 GELT 以前设备的存储大小
# geli resize -s 256M /dev/zvol/zroot/test
# 现在我们可以挂载设备并导入池了
# geli attach -k /tmp/test.key /dev/zvol/zroot/test
# zpool import
```

## 参考文献

- [GELI — Disk Encryption in FreeBSD](https://bsd-pl.org/assets/talks/2018-11-15_0_Micha%C5%82-Borysiak_GELI-Disk-encryption-in-FreeBSD.pdf)，本文主要来自此处。
