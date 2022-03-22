# 第一节 FTP 服务器



FTP 意为文件传输协议。使用 FTP 服务搭建服务器可以快速传输文件。

## pure-ftpd（以 MySQL 支持为例）

>**注意：本示例以 mysql 5.x 为例。**

### 安装

由于 pkg 包不带有数据库支持功能，所以需要通过 ports 来安装该软件:

```
# /usr/ports/ftp/pure-ftpd
# make config-recursive
```
选中 mysql，其余保持默认选项回车即可

sjshhhhh此处插入图片jskkdd


```
# make install clean
```

>**注意：关于 mysql 的基本设置请看 第十七章**

### 配置 /usr/local/etc/pure-ftpd.conf 文件

#### 生成配置文件：

```
# cp /usr/local/etc/pure-ftpd.conf.sample /usr/local/etc/pure-ftpd.conf
# cp /usr/local/etc/pureftpd-mysql.conf.sample /usr/local/etc/pureftpd-mysql.conf
```

编辑配置文件并增加 mysql 的支持：
```
#兼容 ie 等非正规化的 ftp 客户端

BrokenClientsCompatibility yes

# 被动连接响应的端口范围。
PassivePortRange 30000 50000

# 认证用户允许登陆的最小组 ID（UID） 。
MinUID 2000

# 仅允许认证用户进行 FXP 传输。
AllowUserFXP yes

# 用户主目录不存在的话，自动创建。
CreateHomeDir yes

# MySQL configuration file (see README.MySQL)

MySQLConfigFile /usr/local/etc/pureftpd-mysql.conf
```

### 配置 mysql

#### 创建数据库

```
create database pureftp;
use pureftp;
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
`User` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
`Password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
`Uid` int(11) NOT NULL DEFAULT -1 COMMENT '用户ID',
`Gid` int(11) NOT NULL DEFAULT -1 COMMENT '用户组ID',
`Dir` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
`quotafiles` int(255) NULL DEFAULT 500,
`quotasize` int(255) NULL DEFAULT 30,
`ulbandwidth` int(255) NULL DEFAULT 80,
`dlbandwidth` int(255) NULL DEFAULT 80,
`ipaddress` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT
'*',
`comment` int(255) NULL DEFAULT NULL,
`status` tinyint(4) NULL DEFAULT 1,
`ulratio` int(255) NULL DEFAULT 1,
`dlratio` int(255) NULL DEFAULT 1,
PRIMARY KEY (`User`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT =
Dynamic;
INSERT INTO `users` VALUES ('demo', 'demo&2022*', 2002, 2000, '/home/www/demo', 500, 30,
80, 80, '*', NULL, NULL, 1, 1);
```

#### 创建登录数据库用户及设置密码

```
grant select,insert,update,delete on pureftp.* to pftp@localhost identified by
"Ab123456&";
```

### 配置 /usr/local/etc/pureftpd-mysql.conf

```

##############################################
# #
# Sample Pure-FTPd Mysql configuration file. #
# See README.MySQL for explanations. #
# #
##############################################


# Optional : MySQL server name or IP. Don't define this for unix sockets.

# MYSQLServer 127.0.0.1
MYSQLServer localhost


# Optional : MySQL port. Don't define this if a local unix socket is used.

MYSQLPort 3306


# Optional : define the location of mysql.sock if the server runs on this host.

MYSQLSocket /var/run/mysqld/mysqld.sock


# Mandatory : user to bind the server as.

MYSQLUser pftp


# Mandatory : user password. You must have a password.

MYSQLPassword Ab123456&


# Mandatory : database to open.

MYSQLDatabase pureftpd


# Mandatory : how passwords are stored
Valid values are : "cleartext", "argon2", "scrypt", "crypt", "sha1", "md5",
assword" and "any"

# ("password" = MySQL password() function, which is sha1(sha1(password)))

#MYSQLCrypt scrypt
MYSQLCrypt cleartext


# In the following directives, parts of the strings are replaced at
# run-time before performing queries :
#
# \L is replaced by the login of the user trying to authenticate.
# \I is replaced by the IP address the user connected to.
# \P is replaced by the port number the user connected to.
# \R is replaced by the IP address the user connected from.
# \D is replaced by the remote IP address, as a long decimal number.
#
# Very complex queries can be performed using these substitution strings,
# especially for virtual hosting.

# Query to execute in order to fetch the password

MYSQLGetPW SELECT Password FROM users WHERE User='\L'


# Query to execute in order to fetch the system user name or uid
MYSQLGetUID SELECT Uid FROM users WHERE User='\L'


# Optional : default UID - if set this overrides MYSQLGetUID

MYSQLDefaultUID 2000


# Query to execute in order to fetch the system user group or gid

MYSQLGetGID SELECT Gid FROM users WHERE User='\L'


# Optional : default GID - if set this overrides MYSQLGetGID

MYSQLDefaultGID 2000


# Query to execute in order to fetch the home directory

MYSQLGetDir SELECT Dir FROM users WHERE User='\L'


# Optional : query to get the maximal number of files
# Pure-FTPd must have been compiled with virtual quotas support.

# MySQLGetQTAFS SELECT QuotaFiles FROM users WHERE User='\L'


# Optional : query to get the maximal disk usage (virtual quotas)
# The number should be in Megabytes.
# Pure-FTPd must have been compiled with virtual quotas support.

# MySQLGetQTASZ SELECT QuotaSize FROM users WHERE User='\L'


# Optional : ratios. The server has to be compiled with ratio support.

# MySQLGetRatioUL SELECT ULRatio FROM users WHERE User='\L'
# MySQLGetRatioDL SELECT DLRatio FROM users WHERE User='\L'


# Optional : bandwidth throttling.
# The server has to be compiled with throttling support.
# Values are in KB/s .

# MySQLGetBandwidthUL SELECT ULBandwidth FROM users WHERE User='\L'
# MySQLGetBandwidthDL SELECT DLBandwidth FROM users WHERE User='\L'


# Enable ~ expansion. NEVER ENABLE THIS BLINDLY UNLESS :
# 1) You know what you are doing.
# 2) Real and virtual users match.

# MySQLForceTildeExpansion 1


# If you're using a transactionnal storage engine, you can enable SQL
# transactions to avoid races. Leave this commented if you are using the
# traditional MyIsam engine.

# MySQLTransactions On
```
### 添加 ftp 组和用户

```
# pw groupadd ftpgroup -g 2000
# pw useradd ftpuser -u 2001 -g 2000
```
或

```
# pw useradd ftpuser -u 2001 -g 2000 -s /sbin/nologin -w no -d /home/vftp -c "VirtualUser Pure-FTPd" -m
```

### 配置 FTP 目录

```
# mkdir /home/www/pureftp
# chown -R ftpuser /home/www/
# chgrp -R ftpgroup /home/www/
```

### 状态操作

```
# sysrc pureftpd_enable="YES"
# service pure-ftpd start   #启动服务器
# service pure-ftpd stop    #停止服务
# service pure-ftpd restart #重启服务
```


## proftpd

> **警告：该教程仍在进行测试，请略过。**
> 
### 安装 proftpd

```
# pkg install proftpd
```
### 服务器操作

```
# sysrc  proftpd_enable="YES"

# service proftpd start #启动服务器

# service proftpd stop #停止服务

# service proftpd restart #重启服务
```

### 编辑配置文件

设置启动：

```
# touch /var/run/proftpd/proftpd.scoreboard
```

使用 `pw` 命令添加访问 ftp 服务器用户组：

```
# pw groupadd -n ftp
```

给 ftp 服务器设立主目录，名字可以随便写，本文以 `youftp` 为例：

```
# mkdir /youftp
```

在服务器真正可用之前，我们还需要编辑服务器自身的配置文件

```
# ee /usr/local/etc/proftpd.conf
```

`proftpd.conf` (部分)解析如下

```
ServerName          "youftp" #服务器名 自行修改
Port           21 #ftp端口
UseIPv6         on #是否使用IPv6
Umask           022 #掩码
MaxInstances        30 #最大允许线程数（连接次数）
User              nobody
Group           nobody   #设置服务器用户及用户组
DefaultRoot        /youftp #用户默认根目录
AllowOverwrite        on #允许覆盖文件
<Limit SITE_CHMOD>DenyAll</Limit> #是否允许用户改变文件权限
```

### <Anonymous ~ftp>部分

该部分设置匿名登录。若不希望匿名登录服务器，请将此部分注释掉。

```
User         ftp
Group        ftp #用户及用户组管理
MaxClients        10 #允许匿名登录的用户最高数量
DisplayLogin     welcome.msg #服务器欢迎信息
DisplayFirstChdir     .message #用户改变目录时显示信息
<Limit WRITE>DenyAll</Limit> #是否允许写入
```

### 权限设置

```
<directory [PATH]> #设置[PATH]文件夹的权限
   <limit [OPTIONS]> #限制选项
      denygroup [GROUPNAME] #用户组
      DenyAll #所有用户
   </limit>
</directory>
```
#### [OPTIONS]命令介绍:
```
     ALL 除了 LOGIN 命令外的所有命令
     DIRS
          CDUP 返回上层目录
          CWD 改变目录
          LIST 展示目录
          PWD 查看目录
          STAT 显示文件状态
          MLSD 展示信息
     READ
          RETR 下载文件
          SIZE 查看大小
     WRITE
          APPE 上传并覆盖文件
          STOR 上传文件
          RNTO 重命名
          MKD 建立目录
          RMD 删除目录
     SITE_CHMOD 改变权限 
    
```
#### 举例

阻止用户组 `students` 上传文件、重命名、删除目录 在 `/usr/local/homework`  中
```
<directory /usr/local/homework>
   <limit APPE RNTO RMD>
      denygroup students
   </limit>
   AllowOverwrite on
   AllowRetrieveRestart on
   AllowStoreRestart on
</directory>
```

## **连接到 FTP 服务器**

使用 `ftp` 命令可以快速连接到 FTP 服务器。

用法: 

```
ftp [选项] [URL]
```

选项：

`-4` 强制使用 IPv4 协议连接

`-6` 强制使用 IPv6 协议连接

`-a` 使用匿名登录

`-q` [quittime] 在设定时间后连接失败则自动放弃连接

`-r` [wait] 每隔 `wait` 秒发送一次连接请求

`-A` 强制使用主动模式

`-d` 开启调试模式

`-v` 开启啰嗦模式

`-V` 关闭啰嗦模式


#### 登录后的命令：

```
account [passwd] 提交补充密码

append [locol-file] [remote-file] 以 remote-file 为文件名向服务器上传本地文件 local-file

ascii 将FTP文件传送类型设置为 ASCII 模式

bell 在文件传送完后发出提示音

bye 结束与服务器的会话

cd 切换目录

cdup 退回父目录

delete 删除文件

dir 显示该目录下的文件及文件夹

features 显示该服务器支持的功能

get remote-fil 下载服务器上的 remote-file
```

