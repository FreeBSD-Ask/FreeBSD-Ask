# 第五节 常用软件 与 SSH 配置

## WinSCP 下载

WinSCP 是对 `scp` 命令的图形化封装，同时支持 FTP 等多种协议。可以快捷的传输文件与 Windows 系统和 Linux 或 BSD 之间。

下载地址：

{% embed url="https://winscp.net/eng/download.php" %}

## X shell 下载

Xshell 是 Windows 平台上的强大的 shell 工具，不建议使用苦难哲学的 putty 。

下载地址（输入用户名和邮件即可）：

{% embed url="https://www.netsarang.com/zh/free-for-home-school" %}

## 配置SSH

```
# ee /etc/ssh/sshd_config #（删去前边的 #，并将 yes 或 no 修改为如下）
PermitRootLogin yes          #允许 root 登录 
PasswordAuthentication yes   # 设置是否使用口令验证 
```

>提示：删去前边的`#`是什么意思？`#`在 UNIX 当中一般是起到一个注释作用，相当于 C 语言里面的`//`。意味着后边的文字只起到说明作用，不起实际作用。

## 开启SSH 服务

```
# service sshd restart
```

如果提示找不到`sshd`,请执行下一命令:

```
# sysrc sshd_enable="YES"
```

然后再

```
# service sshd restart
```

## 保持 SSH 在线

服务端设置：

编辑 `# ee /etc/ssh/sshd_config`，调整 `ClientAlive` 的设置：

```
ClientAliveInterval 10
ClientAliveCountMax 3
```

10 秒给客户端发一次检测，客户端如果 3 次都不回应，则认为客户端已断开连接。

`ClientAliveInterval` 默认是 `0`，表示禁用检测。

客户端设置：

全局用户生效：`# ee /etc/ssh/ssh_config` ，仅对当前用户生效：`~/.ssh/config`。

```
Host *
ServerAliveInterval 10
ServerAliveCountMax 3
```

或者在连接的时候使用 `-o` 指定参数：

```
# ssh user@server -p 22 -o ServerAliveInterval=10 -o ServerAliveCountMax=3
```

客户端和服务端任一开启检测即可。
