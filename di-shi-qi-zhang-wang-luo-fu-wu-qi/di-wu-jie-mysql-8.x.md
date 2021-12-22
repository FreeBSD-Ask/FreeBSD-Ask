# 第五节 MySQL 8.X

## mysql 80

### 安装 （以下二选一）

```
# pkg install mysql80-server

```
或者

```
# cd /usr/ports/databases/mysql80-server/ && make install clean
```

### 启动服务

```
# sysrc mysql_enable=YES
# service  mysql-server start
```

### 登录

mysql 8.0 默认密码是空，直接回车即可。

```
root@ykla:~ # mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or g.
Your MySQL connection id is 8
Server version: 8.0.27 Source distribution

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or 'h' for help. Type 'c' to clear the current input statement.

root@localhost [(none)]> 

```

### 修改密码

设置密码为`z`，然后刷新权限。

```
root@localhost [(none)]> alter user 'root'@'localhost' identified by 'z';
Query OK, 0 rows affected (0.02 sec)

root@localhost [(none)]> flush privileges;
Query OK, 0 rows affected (0.00 sec)
```
重新登录：

```
root@localhost [(none)]> quit;
Bye
root@ykla:~ # mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or g.
Your MySQL connection id is 9
Server version: 8.0.27 Source distribution

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or 'h' for help. Type 'c' to clear the current input statement.

root@localhost [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.01 sec)

root@localhost [(none)]> 
```
