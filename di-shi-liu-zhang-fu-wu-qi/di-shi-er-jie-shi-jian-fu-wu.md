# 第十二节 时间服务

- 配置时区
- 同步时间

## 选择正确时区

### 安装操作系统的时候选择正确的时区

### 配置时区

```
# cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

## 配置同步时间

### 设置 ntp 服务可用

```
# sysrc ntpd_enable="YES"
```

### 设置 ntp 服务开机时候启动

```
# sysrc ntpd_sync_on_start="YES"
```

### 编辑 `ntp.conf文件`

```
# ee /etc/ntp.conf
```

添加附加时钟服务器

```
server time.windows.com
server 0.cn.pool.ntp.org
server 1.cn.pool.ntp.org
server 2.cn.pool.ntp.org
server 3.cn.pool.ntp.org
```

### 设置 ntp 服务开机自启动（上面已设置，此处可选）

```
# /etc/rc.d/ntpd enable 
或
# service ntpd enable
```

### 启动 ntp 服务

```
# /etc/rc.d/ntpd start
或
# service ntpd start 
```

### 重启 ntp 服务

```
# /etc/rc.d/ntpd restart
或
# service ntpd restart
```

### 显示当前时间

```
# date
```

### 手动同步时间（可选）

```
# ntpdate time.windows.com
```
