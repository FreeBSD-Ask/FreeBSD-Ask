# 第一节 FTP 服务器

FTP 意为文件传输协议。使用 FTP 服务搭建服务器可以快速传输文件。

## proftpd 

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

使用`pw`命令添加访问 ftp 服务器用户组：

```
# pw groupadd -n ftp
```

给 ftp 服务器设立主目录，名字可以随便写，本文以`youftp`为例：

```
# mkdir /youftp
```

在服务器真正可用之前，我们还需要编辑服务器自身的配置文件

```
# ee /usr/local/etc/proftpd.conf
```

`proftpd.conf`(部分)解析如下

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

阻止用户组`students`上传文件,重命名,删除目录 在   /usr/local/homework  中
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

使用`ftp`命令可以快速连接到 FTP 服务器。

用法: 

`ftp [选项] [URL]`

选项：

`-4` 强制使用 IPv4 协议连接

`-6`强制使用 IPv6 协议连接

`-a` 使用匿名登录

`-q [quittime]` 在设定时间后连接失败则自动放弃连接

`-r [wait]` 每隔`wait`秒发送一次连接请求

`-A` 强制使用主动模式

`-d` 开启调试模式

`-v`开启啰嗦模式

`-V` 关闭啰嗦模式

#### 登录后的命令：

`account [passwd]` 提交补充密码

`append [locol-file] [remote-file]` 以`remote-file`为文件名向服务器上传本地文件`local-file`

`ascii` 将FTP文件传送类型设置为`ASCII`模式

`bell` 在文件传送完后发出提示音

`bye` 结束与服务器的会话

`cd`切换目录

`cdup` 退回父目录

`delete`删除文件

`dir` 显示该目录下的文件及文件夹

`features` 显示该服务器支持的功能

`get remote-fil` 下载服务器上的 remote-file


