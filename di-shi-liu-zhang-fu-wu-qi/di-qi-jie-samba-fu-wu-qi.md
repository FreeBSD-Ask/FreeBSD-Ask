# 第七节 Samba 服务器

## 一、安装samba

```
# pkg search samba
 
p5-Samba-LDAP-0.05_2           Manage a Samba PDC with an LDAP Backend
p5-Samba-SIDhelper-0.0.0_3     Create SIDs based on G/UIDs
samba-nsupdate-9.16.5          nsupdate utility with the GSS-TSIG support
samba410-4.10.18               Free SMB/CIFS and AD/DC server and client for Unix
samba411-4.11.13               Free SMB/CIFS and AD/DC server and client for Unix
samba412-4.12.7                Free SMB/CIFS and AD/DC server and client for Unix
samba413-4.13.0                Free SMB/CIFS and AD/DC server and client for Unix
```

```
# pkg install samba413-4.13.0
```

## 二、启动samba

（1）打开/etc/rc.conf

```
# vi /etc/rc.conf
```

（2）在/etc/rc.conf最后加入如下，并保存：

```
nmbd_enable="YES"
winbindd_enable="YES"
samba_enable="YES"
samba_server_enable="YES"
```

（3）创建/usr/local/etc/smb4.conf，添加如下内容并保存

```
#vi /usr/local/etc/smb4.conf

[root]
    comment = root's stuff
    path = /root
    public = no
    browseable = yes
    writable = yes
    printable = no
    create mask = 0755
```

（4）创建samba root用户：

```
# smbpasswd -a root
```

（5）进入/usr/local/etc

```
# cd /usr/local/etc
```

（6）再执行

```
# service samba_server start //启动命令
```

（7）查看samba状态：

```
service samba_server status
```

（8）在windows下利用\\192.168.253.128访问共享文件夹

```
\\192.168.253.128
```

