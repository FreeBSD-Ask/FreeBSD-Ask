# 第 2.8 节 常用软件 与 SSH 配置

## WinSCP 下载

WinSCP 是对 `scp` 命令的图形化封装的软件，并同时支持 FTP 等多种协议。可以快捷的传输文件与 Windows 系统和 Linux 或 BSD 之间。

下载地址：

[https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)

## Xshell 下载

Xshell 是 Windows 平台上的强大的 shell 工具，不建议使用苦难哲学的 putty。

下载地址（输入用户名和邮件即可）：

[https://www.netsarang.com/zh/free-for-home-school](https://www.netsarang.com/zh/free-for-home-school)

## 配置 SSH

### 允许 root ssh

```shell-session
# ee /etc/ssh/sshd_config    #（删去前边的 #，并将 yes 或 no 修改为如下）
PermitRootLogin yes          #允许 root 登录
PasswordAuthentication yes   #（可选）设置是否使用普通密码验证，如果不设置此参数则使用 PAM 认证登录，安全性更高
```

> 提示：删去前边的 `#` 是什么意思？`#` 在 UNIX 当中一般是起到一个注释作用，相当于 C 语言里面的 `//`。意味着后边的文字只起到说明作用，不起实际作用。

> **故障排除**
>
> 如果你实在是找不到 `PasswordAuthentication no`，请你看看你改的究竟是 `/etc/ssh/`ssh\_**d**\_`_config` 还是 `/etc/ssh/`**ssh**`_config`。**sshd** 才是我们真正要改的文件。

### 开启 SSH 服务

```shell-session
# service sshd restart
```

如果提示找不到 `sshd`,请执行下一命令:

```shell-session
# sysrc sshd_enable="YES"
```

然后再

```shell-session
# service sshd restart
```

### 保持 SSH 在线

服务端设置：

编辑 `# ee /etc/ssh/sshd_config`，调整 `ClientAlive` 的设置：

```shell-session
ClientAliveInterval 10
ClientAliveCountMax 3
```

10 秒给客户端发一次检测，客户端如果 3 次都不回应，则认为客户端已断开连接。

`ClientAliveInterval` 默认是 `0`，表示禁用检测。

客户端设置：

全局用户生效：`# ee /etc/ssh/ssh_config`，仅对当前用户生效：`~/.ssh/config`。

```shell-session
Host *
ServerAliveInterval 10
ServerAliveCountMax 3
```

或者在连接的时候使用 `-o` 指定参数：

```shell-session
# ssh user@server -p 22 -o ServerAliveInterval=10 -o ServerAliveCountMax=3
```

客户端和服务端任一开启检测即可。

## SSH 密钥登录

### 生成密钥

```shell-session
# ssh-keygen
```

> OpenSSH 7.0 及以上版本默认禁用了 ssh-dss(DSA) 公钥算法。FreeBSD 13.0 采用 OpenSSH\_7.9。因此使用默认值即可。

```shell-session
root@ykla:~ # ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): #此处回车
Created directory '/root/.ssh'.
Enter passphrase (empty for no passphrase):    #此处输入密码（为了安全建议设置密码）
Enter same passphrase again:     #此处重复输入密码
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:MkcEjGhWCv6P/8y62JfbpEws9OnRN1W0adxmpceNny8 root@ykla
The key's randomart image is:
+---[RSA 2048]----+
|.  o.o...      ..|
|..+.. ..      o+*|
| +.     .     o*B|
|  .    .      o=.|
|   . .o S    . ..|
|    + o+o   .   .|
|   . o *.o o  E .|
|    + Bo= . .  . |
|   . ==O..       |
+----[SHA256]-----+
root@ykla:~ #
```

### 配置密钥

检查权限（默认创建的权限如下）：

```shell-session
drwx------  2 root  wheel   512 Mar 22 18:27 /root/.ssh #权限为 700
-rw-------  1 root  wheel  1856 Mar 22 18:27 /root/.ssh/id_rsa  #私钥，权限为 600
-rw-r--r--  1 root  wheel  391 Mar 22 18:27 /root/.ssh/id_rsa.pub #公钥，权限为 644
```

生成验证公钥：

```shell-session
# cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys
-rw-r--r--  1 root  wheel  391 Mar 22 18:39 /root/.ssh/authorized_keys #检查权限 644
```

使用 winscp 把私钥和公钥保存到本地后，删除服务器上的多余文件：

```shell-session
# rm /root/.ssh/id_rsa*
```

### 修改 /etc/ssh/sshd\_config

```shell-session
# ee /etc/ssh/sshd_config
```

修改配置如下（删去前边的 #，并将 yes 或 no 修改为如下）：

```shell-session
PermitRootLogin yes                          #允许 ROOT 用户直接登陆系统
AuthorizedKeysFile     .ssh/authorized_keys  #修改使用用户目录下密钥文件，默认已经正确配置，请检查
PasswordAuthentication no                    #不允许用户使用密码方式登录
ChallengeResponseAuthentication no           #禁止密码登录验证
PermitEmptyPasswords no                      #禁止空密码的用户进行登录
```

### 重启服务

```shell-session
# service sshd restart
```

使用 xshell 登录即可，输入密钥密码，导入私钥`id_rsa`，即可登录。

> 如果使用其他 ssh 软件无法登陆请自行转换密钥格式。

## 使用 screen 保持 SSH 不断线

安装：

```shell-session
# pkg install screen
```

使用方法：

```shell-session
# screen -S xxx
```

使用 `-S` 可以指定 `xxx` 为名字，方便找到。

然后就可以进行 ssh 连接了，后续可以关闭这个窗口或软件，不影响 ssh。

查看有哪些正在运行的 screen？

```shell-session
root@ykla:/ # screen -ls
There are screens on:
	18380.pts-0.ykla	(Attached)
	70812.xxx	(Detached)
	67169.pts-0.ykla	(Detached)
3 Sockets in /tmp/screens/S-root.
```

`Detached` 的可以直接 `-r` 恢复。

```shell-session
screen -r xxx
```

`Attached` 的必须先离线再恢复：

```shell-session
root@ykla:/ # screen -d 18380
[18380.pts-0.ykla detached.]

root@ykla:/ # screen -r 18380
```

