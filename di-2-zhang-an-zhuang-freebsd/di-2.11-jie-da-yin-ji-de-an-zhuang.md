# 第 2.11 节 打印机的安装

本过程环境使用的是 `KDE5` 桌面系统及 `HP LaserJet Pro MFP M126nw` 多功能激光打印机（如果是其它型号的惠普打印机需在添加打印机时能找到对应的型号的驱动就能使用）,并且已连入局域网实现网络打印。

## 安装 CUPS(通用 Unix 打印系统)

```shell-session
# pkg install cups
```

或

```shell-session
# cd /usr/ports/print/cups
# make install clean
```

请在界面中选中 `x11`，此选项可在 kde 5 桌面系统中生成添加和配置打印机的应用。

## 添加服务

```shell-session
# sysrc cupsd_enable="YES"
```

完成后启动 cups 服务，执行如下命令

```shell-session
# service cupsd restart
```

## 安装打印机驱动

```shell-session
# pkg install hplip
```

## 添加打印机

在浏览器中输入 `http://localhost:631`，该地址为该打印机的管理页面。

点击顶部菜单的 `Administration` 进行添加打印机

或者在 kde 5 的系统设置->打印机中添加。
