# 第一节 System INIT 管理服务

## 基础 <a href="fu-wu-guan-li-xi-tong" id="fu-wu-guan-li-xi-tong"></a>

FreeBSD 使用 BSD INIT 管理系统服务。

* 启动一个服务：`#service XXX start`
* 停止一个服务：`#service XXX stop`
* 重启一个服务：`#service XXX restart`

出于安全性考虑，服务安装以后默认是禁用状态，以上命令是无法执行的，需要先开启服务：

```
#ee /etc/rc.conf
```

添加一行，`XXX_enable="YES"`，`XXX` 表示服务名称（这里只是举例，实际上可以是nginx samba等），这是固定格式：

```
XXX_enable="YES"
```

服务所对应的脚本路径是： `/usr/local/etc/rc.d/`

当然也可以直接调用 `/etc/rc.d/` 和 `/usr/local/etc/rc.d/` 下的那些脚本`。`

* `/usr/local/etc/rc.d/XXX reload`
* `/usr/local/etc/rc.d/XXX stop`

如果 rc.conf 中并没有启用某项服务，但想临时启动它，那么可以这样：

* `service XXX onestart`
* `service XXX onestop`

## 进阶

rc.conf 掌管着所有系统服务。与之相关的文件和路径如下：

1. 默认的配置位于 `/etc/defaults/rc.conf`。尽量不要对其进行修改。
2. 用户自定义的配置位于 `/etc/rc.conf`。例如，如果想让系统自动启动 ssh、ipfw、nginx 等服务，就要修改本文件。**注意，如果某项配置与默认的配置有冲突，则以本文件为准。**
3. 基系统的服务脚本位于 `/etc/rc.d/`。第三方应用的服务脚本位于 `/usr/local/etc/rc.d/`。当遇到问题时，通过查阅配置文件，找出问题所在。

### periodic.conf <a href="periodicconf" id="periodicconf"></a>

FreeBSD 默认有一些周期执行的任务，它们是通过 `periodic` 命令执行的，由 `cron` 自动调用。与 `periodic` 有关的配置和路径如下：

1. 默认的配置位于 `/etc/defaults/periodic.conf`。
2. 用户自定义的配置位于 `/etc/periodic.conf`。
3. 基系统的任务脚本位于 `/etc/periodic/`。
4. 第三方应用的任务脚本位于 `/usr/local/etc/periodic/`。

以 `locate` 命令的所依赖的路径数据库 `/var/db/locate.database` 为例，\
该数据库由 `/etc/periodic/weekly/310.locate` 这个脚本每周更新一次。\
如果你要立即更新，也可以直接执行这个脚本。

### &#x20;其他配置文件 <a href="qi-ta-pei-zhi-wen-jian" id="qi-ta-pei-zhi-wen-jian"></a>

* crontab: `cron` 配置，位于 `/etc/crontab`，请参考 `man crontab`。
* syslog.conf: 系统日志配置，位于 `/etc/syslog.conf`，请参考 `man syslog.conf`。
* loader.conf: 系统启动配置，位于 `/boot/loader.conf`，请参考 `man loader.conf`。
* sysctl.conf: 内核参数配置，位于 `/etc/sysctl.conf`，请参考 `man sysctl.conf`。
