# 第八节 PostgreSQL

PostgreSQL 是一款自由的对象-关系型数据库，最早发布于 1989 年 6 月，国内某些数据 库据说也是由此发展而来。 

FreeBSD 的软件源有提供 PostgreSQL 的安装包，版本 12.2，可以通过命令安装： 
```
pkg install -y postgresql12-server postgresql12-client 
```
安装后会在系统中生成 postgresql 服务，可以用 service 命令管理

。但此刻启动服务只会报 错，这是因为 PostgreSQL 尚未初始化，故此还需要执行命令： 
```
su postgres -c "pg\_ctl -D /var/db/postgres/data12 initdb" 
```
会将数据目录创建完成，接下来再用 service 命令管理 postgresql 服务。

如： 
```
service postgresql enable 
service postgresql start
```
PostgreSQL 已经正常启动了。
