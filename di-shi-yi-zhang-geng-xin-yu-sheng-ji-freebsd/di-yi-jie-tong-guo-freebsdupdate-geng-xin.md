# 第一节 通过 freebsd-update 更新

****

## **故障排除**

### **FreeBSD 升级出错，没有ntp 用户**

终端执行命令

pw groupadd ntpd -g 123\
pw useradd ntpd -u 123 -g ntpd -h - -d /var/db/ntp -s /usr/sbin/nologin -c “NTP Daemon”
