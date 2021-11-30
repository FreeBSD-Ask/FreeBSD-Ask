# 第四节 禁用 Sendmail

FreeBSD系统中的sendmail一直默认启动，对于大多数人来说是无用的，这个可以在安装时禁止，详见安装说明。



编辑 `/etc/rc.conf` ，加入以下几行：

```
sendmail_enable="NO"
sendmail_submit_enable="NO"
sendmail_outbound_enable="NO"
sendmail_msp_queue_enable="NO"
```

编辑 `/etc/periodic.conf` ，加入以下几行，关闭某些Sendmail才会用到的设定。

```
daily_clean_hoststat_enable="NO"
daily_status_mail_rejects_enable="NO"
daily_status_include_submit_mailq="NO"
daily_submit_queuerun="NO"
```
