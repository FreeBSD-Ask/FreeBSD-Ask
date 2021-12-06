# 第七节 Samba 服务器

## 1、内核优化

编辑 /etc/sysctl.conf，添加如下内容

```
kern.maxfiles=25600
kern.maxfilesperproc=16384
net.inet.tcp.sendspace=65536
net.inet.tcp.recvspace=65536
```

编辑 /boot/loader.conf，添加

```
aio_load="YES"
```

## 2、安装

1、查找相关包

```
# pkg search samba
```

2、选择要安装的版本

```
# pkg install samba413
```

3、配置 /usr/local/etc/smb4.conf (默认没这个文件，请自行新建)

```
[global]
workgroup = WORKGROUP
server string = Samba Server %v
netbios name = NAS
security = user
create mode = 0644
force create mode = 0644
directory mode = 0755
force directory mode = 0755
load printers = no
printing = bsd
printcap name = /dev/null
show add printer wizard = no
disable spoolss = yes
server multi channel support=yes
max protocol = SMB3
#############
[pub]
path = /YOUR_PATH  #此处写文件共享路径
browsable = yes
writable = yes
```

4、自启动设置

```
# sysrc samba_server_enalbe="YES"
# service samba_server start
```

5、添加 samba 用户

```
# pdbedit -a -u username #此处应根据实际填写
```
