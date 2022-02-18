# 第一节 Apache

## 安装

以下二选一

```
# cd /usr/ports/www/apache24/ && make install clean
```

或者

```
# pkg install apache24
```

## 启动服务

```
# 添加服务开机自启
# sysrc apache24_enable=YES

# 启动服务
# service apache24 start

# 查看状态
# service apache24 status
```

按理来说，apache 服务已经启动了，现在可以打开网址 `localhost` 看一下。
