# 第五节 SWAP 交换分区的设置

如果在安装系统的时候并未设置 swap 即交换分区，那么后期只能通过 dd 一个交换分区的文件来实现了。因为无论是 UFS 还是 ZFS 都是不支持缩小文件分区的……

dd 一个 大小为 1GB 的 swap 文件

`# dd if=/dev/zero of=/usr/swap0 bs=1M count=1024`

设置权限为 600，即只有拥有者有读写权限。

`# chmod 0600 /usr/swap0`

如果要立即使用

`# mdconfig -a -t vnode -f /usr/swap0 -u 0 && swapon /dev/md0`

为了重启后仍然有效，还需要往`/etc/rc.conf`中加入

`swapfile="/usr/swap0"`
