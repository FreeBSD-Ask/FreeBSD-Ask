# 第二节 安装 CDE

>**未经测试，仅供参考。**


## 开始安装

```
# pkg install -y iconv bdftopcf libXScrnSaver ksh93 open-motif tcl86 xorg-fonts xorg-fonts-100dpi cde
```
## 开启各项服务

```
# sysrc rpcbind_enable="YES"
# sysrc dtspc_enable=="YES"
# sysrc dtcms_enable=="YES"
# ln -s /usr/local/dt/bin/Xsession ~/.Xsession 
```
