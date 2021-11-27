# 第一节 System INIT 管理服务

## 服务管理系统 <a href="fu-wu-guan-li-xi-tong" id="fu-wu-guan-li-xi-tong"></a>

FreeBSD 使用 BSD INIT 管理系统服务。

* 启动一个服务：`# service XXX start`
* 停止一个服务：`# service XXX stop`
* 重启一个服务：`# service XXX restart`

出于安全性考虑，服务安装以后默认是禁用状态，以上命令是无法执行的，需要先开启服务：

```
#ee /etc/rc.conf
```

添加一行，`XXX_enable="YES"`，`XXX` 表示服务名称（这里只是举例，实际上可以是nginx samba等），这是固定格式：

```
XXX_enable="YES"
```

服务所对应的脚本路径是： `/usr/local/etc/rc.d/`
