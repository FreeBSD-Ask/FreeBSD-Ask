# 第一节 通过 freebsd-update 更新

>注意：只有一级架构的 release 版本才提供该源。也就是说 current 和 stable 是没有的。
关于架构的支持等级说明请看：
><https://www.freebsd.org/platforms>


>前排提示：阿里云用户请注意，目前不支持从 12.1 升级到任一版本，因为
><https://reviews.freebsd.org/D27262>

## 更新系统

FreeBSD 提供了实用工具 `freebsd-update` 来安装系统更新，包括升级到大版本。

常规的安全更新：

```
# freebsd-update fetch
# freebsd-update install
```

小版本或者大版本更新，`13.1` 是要更新到的版本号：

```
# freebsd-update upgrade -r 13.1-RELEASE
# freebsd-update install
```

安装后需要重启系统：

```
# reboot
```

然后再继续完成安装：

```
# freebsd-update install
```

## **故障排除**

### **FreeBSD 升级出错，没有 ntp 用户**

终端执行命令

```
# pw groupadd ntpd -g 123
# pw useradd ntpd -u 123 -g ntpd -h - -d /var/db/ntp -s /usr/sbin/nologin -c "NTP Daemon"
```
