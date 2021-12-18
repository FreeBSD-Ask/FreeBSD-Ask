# 第八节 PostgreSQL

PostgreSQL 是一款自由的对象-关系型数据库，最早发布于 1989 年 6 月。在FreeBSD 上，提供了 9.6、10、11、12、13、14共计6个大版本可选。

## postgresql 安装示例，6个版本都如此。

### 安装：二选一

```
# pkg install -y postgresql96-server
```
或者

```
cd /usr/ports/databases/postgresql96-server/ && make install clean
```
### 加入启动项
```
# sysrc postgresql_enable=YES
```

### 初始化数据库
```
/usr/local/etc/rc.d/postgresql initdb
```
示例输出：
```
root@ykla:~ # /usr/local/etc/rc.d/postgresql initdb
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locales
  COLLATE:  C
  CTYPE:    C.UTF-8
  MESSAGES: C.UTF-8
  MONETARY: C.UTF-8
  NUMERIC:  C.UTF-8
  TIME:     C.UTF-8
The default text search configuration will be set to "english".

Data page checksums are disabled.

creating directory /var/db/postgres/data96 ... ok
creating subdirectories ... ok
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default timezone ... PRC
selecting dynamic shared memory implementation ... posix
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok
syncing data to disk ... ok

WARNING: enabling "trust" authentication for local connections
You can change this by editing pg_hba.conf or using the option -A, or
--auth-local and --auth-host, the next time you run initdb.

Success. You can now start the database server using:

    /usr/local/bin/pg_ctl -D /var/db/postgres/data96 -l logfile start

root@ykla:~ # 
```
### 登录使用

Postgresql 默认是没有 root 用户的，需要使用其创建的 postgres 用户登录。

示例输出:

```
root@ykla:~ # psql
psql: FATAL:  role "root" does not exist
```
正确用法：
```
# 切换用户
root@ykla:~ # su - postgres  

#启动服务
$ /usr/local/bin/pg_ctl -D /var/db/postgres/data96 -l logfile start

#创建新用户 ykla，并设置密码
$ createuser -sdrP ykla
Enter password for new role: 
Enter it again: 
$ 
# 创建数据库
$ createdb new_db
#登录进数据库并将数据库权限赋予用户 ykla。
$ psql
psql (9.6.24)
Type "help" for help.

postgres=# ALTER USER ykla WITH ENCRYPTED PASSWORD 'password';
ALTER ROLE
postgres=# 
postgres=# GRANT ALL PRIVILEGES ON DATABASE new_db TO ykla;
GRANT
#退出数据库
postgres=# \q
$
```
