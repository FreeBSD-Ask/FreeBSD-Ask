# 第 9.2 节 jail 配置

## 创建 jail 目录

### 放入 FreeBSD 基本系统

方案一

```sh
# cd /usr/src
# make buildworld                      # 编译基本系统
# make installworld DESTDIR=/usr/jail/ # 安装到 jail
# make distribution DESTDIR=/usr/jail/ # 或者用
```

方案二

下载 `base.txz` 或者从 iso 提取 `baes.txz`，然后解压到 jail

```sh
# tar -xvf base.txz -C /usr/jail/
```

挂载 devfs 文件系统。(不是必须)

```sh
# mount -t devfs devfs /usr/jail/dev
```

### 写入 `/etc/rc.conf`

```sh
# sysrc jail_enable="YES"
```

创建 `jail.conf` 文件（可以写进 `rc.conf` 但这样便于管理）

```sh
www {
host.hostname =www.example.org;         # 主机名
ip4.addr = 192.168.0.10;                # IP 地址
path ="/usr/jail";                      # jail 位置
devfs_ruleset = "www_ruleset";          # devfs ruleset
mount.devfs;                            # 挂载 devfs 文件系统到 jail
exec.start = "/bin/sh /etc/rc";         # 启动命令
exec.stop = "/bin/sh /etc/rc.shutdown"; # 关闭命令
}
```

## 管理

用 `jls` 查看在线 jail 信息列表

```sh
JID IP Address    Hostname   Path
3   192.168.0.10  www       /usr/jail/www
```

中英对照

|    英语    |   中文    |
| :--------: | :-------: |
|    JID     |  jail ID  |
| IP Address |  IP 地址  |
|  Hostname  |  主机名   |
|    Path    | jail 路径 |

## 启动与停止 jail

```sh
# service jail start www
# service jail stop www
```

## 登录 jail

```sh
# jexec 1 tcsh
```

## 干净关闭 jail

```sh
# jexec 3 /etc/rc.shutdown
```

## 升级 jail

```sh
# freebsd-update -b /here/is/the/jail fetch
# freebsd-update -b /here/is/the/jail install
```

## ping 与网络

### 开启 ping

写入 `/etc/jail.conf`

```sh
allow.raw_sockets=1;
allow.sysvipc=1;
```

配置完毕请重启 jail。

- 示例：

```sh
# jail -rc test
```

### 网络

创建 `/etc/resolv.conf`,并编辑

```sh
search lan
nameserver 223.5.5.5 #不要写路由器地址
nameserver 223.6.6.6 #不要写路由器地址
```

## 故障排除

- 删除文件没有权限

```sh
# chflags -R noschg directory
```

- `Certificate verification failed for /C=US/O=Let's Encrypt/CN=E6
0020C1CD593C0000:error:16000069:STORE routines:ossl_store_get0_loader_int:unregistered`

经检查，时间正常。一般发生在 FreeBSD 14.1、14.2 RELEASE 中。

```sh
# pkg
The package management tool is not yet installed on your system.
Do you want to fetch and install it now? [y/N]: y
Bootstrapping pkg from pkg+https://pkg.FreeBSD.org/FreeBSD:14:amd64/latest, please wait...
Certificate verification failed for /C=US/O=Let's Encrypt/CN=E6
0020C1CD593C0000:error:16000069:STORE routines:ossl_store_get0_loader_int:unregistered scheme:/usr/src/crypto/openssl/crypto/store/store_register.c:237:scheme=file
0020C1CD593C0000:error:80000002:system library:file_open:No such file or directory:/usr/src/crypto/openssl/providers/implementations/storemgmt/file_store.c:267:calling stat(/etc/ssl/certs/4042bcee.0)
0020C1CD593C0000:error:16000069:STORE routines:ossl_store_get0_loader_int:unregistered scheme:/usr/src/crypto/openssl/crypto/store/store_register.c:237:scheme=file
0020C1CD593C0000:error:80000002:system library:file_open:No such file or directory:/usr/src/crypto/openssl/providers/implementations/storemgmt/file_store.c:267:calling stat(/etc/ssl/certs/4042bcee.0)
0020C1CD593C0000:error:0A000086:SSL routines:tls_post_process_server_certificate:certificate verify failed:/usr/src/crypto/openssl/ssl/statem/statem_clnt.c:1890:
Certificate verification failed for /C=US/O=Let's Encrypt/CN=E6
0020C1CD593C0000:error:16000069:STORE routines:ossl_store_get0_loader_int:unregistered scheme:/usr/src/crypto/openssl/crypto/store/store_register.c:237:scheme=file
0020C1CD593C0000:error:80000002:system library:file_open:No such file or directory:/usr/src/crypto/openssl/providers/implementations/storemgmt/file_store.c:267:calling stat(/etc/ssl/certs/4042bcee.0)
0020C1CD593C0000:error:16000069:STORE routines:ossl_store_get0_loader_int:unregistered scheme:/usr/src/crypto/openssl/crypto/store/store_register.c:237:scheme=file
0020C1CD593C0000:error:80000002:system library:file_open:No such file or directory:/usr/src/crypto/openssl/providers/implementations/storemgmt/file_store.c:267:calling stat(/etc/ssl/certs/4042bcee.0)
0020C1CD593C0000:error:0A000086:SSL routines:tls_post_process_server_certificate:certificate verify failed:/usr/src/crypto/openssl/ssl/statem/statem_clnt.c:1890:
Certificate verification failed for /C=US/O=Let's Encrypt/CN=E6
0020C1CD593C0000:error:16000069:STORE routines:ossl_store_get0_loader_int:unregistered scheme:/usr/src/crypto/openssl/crypto/store/store_register.c:237:scheme=file
0020C1CD593C0000:error:80000002:system library:file_open:No such file or directory:/usr/src/crypto/openssl/providers/implementations/storemgmt/file_store.c:267:calling stat(/etc/ssl/certs/4042bcee.0)
0020C1CD593C0000:error:16000069:STORE routines:ossl_store_get0_loader_int:unregistered scheme:/usr/src/crypto/openssl/crypto/store/store_register.c:237:scheme=file
0020C1CD593C0000:error:80000002:system library:file_open:No such file or directory:/usr/src/crypto/openssl/providers/implementations/storemgmt/file_store.c:267:calling stat(/etc/ssl/certs/4042bcee.0)
0020C1CD593C0000:error:0A000086:SSL routines:tls_post_process_server_certificate:certificate verify failed:/usr/src/crypto/openssl/ssl/statem/statem_clnt.c:1890:
Certificate verification failed for /C=US/O=Let's Encrypt/CN=E6
0020C1CD593C0000:error:16000069:STORE routines:ossl_store_get0_loader_int:unregistered scheme:/usr/src/crypto/openssl/crypto/store/store_register.c:237:scheme=file
0020C1CD593C0000:error:80000002:system library:file_open:No such file or directory:/usr/src/crypto/openssl/providers/implementations/storemgmt/file_store.c:267:calling stat(/etc/ssl/certs/4042bcee.0)
0020C1CD593C0000:error:16000069:STORE routines:ossl_store_get0_loader_int:unregistered scheme:/usr/src/crypto/openssl/crypto/store/store_register.c:237:scheme=file
0020C1CD593C0000:error:80000002:system library:file_open:No such file or directory:/usr/src/crypto/openssl/providers/implementations/storemgmt/file_store.c:267:calling stat(/etc/ssl/certs/4042bcee.0)
0020C1CD593C0000:error:0A000086:SSL routines:tls_post_process_server_certificate:certificate verify failed:/usr/src/crypto/openssl/ssl/statem/statem_clnt.c:1890:
Certificate verification failed for /C=US/O=Let's Encrypt/CN=E6
0020C1CD593C0000:error:16000069:STORE routines:ossl_store_get0_loader_int:unregistered scheme:/usr/src/crypto/openssl/crypto/store/store_register.c:237:scheme=file
0020C1CD593C0000:error:80000002:system library:file_open:No such file or directory:/usr/src/crypto/openssl/providers/implementations/storemgmt/file_store.c:267:calling stat(/etc/ssl/certs/4042bcee.0)
0020C1CD593C0000:error:16000069:STORE routines:ossl_store_get0_loader_int:unregistered scheme:/usr/src/crypto/openssl/crypto/store/store_register.c:237:scheme=file
0020C1CD593C0000:error:80000002:system library:file_open:No such file or directory:/usr/src/crypto/openssl/providers/implementations/storemgmt/file_store.c:267:calling stat(/etc/ssl/certs/4042bcee.0)
0020C1CD593C0000:error:0A000086:SSL routines:tls_post_process_server_certificate:certificate verify failed:/usr/src/crypto/openssl/ssl/statem/statem_clnt.c:1890:
Certificate verification failed for /C=US/O=Let's Encrypt/CN=E6
0020C1CD593C0000:error:16000069:STORE routines:ossl_store_get0_loader_int:unregistered scheme:/usr/src/crypto/openssl/crypto/store/store_register.c:237:scheme=file
0020C1CD593C0000:error:80000002:system library:file_open:No such file or directory:/usr/src/crypto/openssl/providers/implementations/storemgmt/file_store.c:267:calling stat(/etc/ssl/certs/4042bcee.0)
0020C1CD593C0000:error:16000069:STORE routines:ossl_store_get0_loader_int:unregistered scheme:/usr/src/crypto/openssl/crypto/store/store_register.c:237:scheme=file
0020C1CD593C0000:error:80000002:system library:file_open:No such file or directory:/usr/src/crypto/openssl/providers/implementations/storemgmt/file_store.c:267:calling stat(/etc/ssl/certs/4042bcee.0)
0020C1CD593C0000:error:0A000086:SSL routines:tls_post_process_server_certificate:certificate verify failed:/usr/src/crypto/openssl/ssl/statem/statem_clnt.c:1890:
pkg: Attempted to fetch https://pkg.FreeBSD.org/FreeBSD:14:amd64/latest/Latest/pkg.pkg
pkg: Attempted to fetch https://pkg.FreeBSD.org/FreeBSD:14:amd64/latest/Latest/pkg.txz
pkg: Error: Authentication error
A pre-built version of pkg could not be found for your system.
Consider changing PACKAGESITE or installing it from ports: 'ports-mgmt/pkg'
```

解决：

```sh
# certctl rehash
```

重新执行 `pkg` 即可。

原因未知，参见

- [Bug 280031 - Cannot install `pkg` due to 404 on pkg.freebsd.org](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=280031)
- [Cannot fetch (and install) `pkg`](https://forums.freebsd.org/threads/cannot-fetch-and-install-pkg.93976/)
