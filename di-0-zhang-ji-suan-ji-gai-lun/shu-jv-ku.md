# MySQL

修改用户密码

```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'your_new_password';
```

UNIX 连接 MySQL

```shell
# mysql -u root -p
```

在修改完用户、权限或主机以后，使用 `FLUSH PRIVILEGES;` 命令刷新是个好习惯，可以确保更改生效。

设置用户可以被某个特定主机连接， `Host = 'xxx'` 是指定能连接的 IP， `%` 就是随意一个主机都能连接。

```sql
UPDATE mysql.user SET Host = '%' WHERE User = 'root';
FLUSH PRIVILEGES;
```

## 建立数据库

```sql
create database xxx;
```

或者

```sql
create database if not exists xxx;
```

## 数据库命名

数据库名称区分大小写。  
数据库名称最长 64 个字符，别名（alias）最长 256 字符。  
数据库名不能使用数据库的关键字。

## 查看数据库

```sql
show databases;
```

输出的表格：

```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| jimmy_db           |
| mysql              |
| performance_schema |
| sys                |
| vskdb              |
+--------------------+
6 rows in set (0.00 sec)
```

## 进入数据库

`use xxx;`
再进入其他数据库重复上面语句。

## 删除数据库

```sql
drop database xxx;
```

注意不能删除系统数据库：

- Information_schema
- Mysql
- Performance_schema
- Test

GBK: 国家标准扩展码（Guo-Biao Kuozhan）  
BIG5：大五码，繁体中文社区最常用的电脑汉字字符集标准。

## 数据库重命名

```sql
rename database xxx xxxx;
```

MySQL 会报错，因为某版本以后不允许改名。SQL 语法写的没问题，别的数据库仍可能支持重命名。

## 更改数据库字符集

```sql
alter database xxx
default character set UTF-8;
```

## 数据类型

范围视有符号和无符号而定，无符号范围更大。根据实际要存储的数据选择合适的数据类型。

**数字类型**：

- TINYINT，1 字节
- SMALLINT，2 字节
- MEDIUMINT，3 字节
- INT，4 字节
- BIGINT，8 字节

- FLOAT，4 字节，
- DOUBLE，8 字节
  DECIMAL：  
  P 是表示有效数字数的精度。 P 范围是 1 到 65。  
  D 是表示小数点后的位数。 D 的范围是 0 到 30。D 肯定是要小于或等于(<=)P 的。

想要数据库类型为无符号，请添加 UNSIGNED 属性。

## 建立表格

```sql
create table if not exists <table_name>
(
  sid tinyint,
  sage tinyint
);
```

输出：

```
mysql> create table if not exists MyTable
    -> (
    ->   sid tinyint,
    ->   sage tinyint
    -> );
Query OK, 0 rows affected (0.06 sec)
```

==注意！表格是放在数据库里面的，进入 MySQL 解释器以后必须使用 use 命令进入你的数据库==

## 查看数据表

```sql
show tables;
```

此时可以看到表格已经被创建：

```
mysql> show tables;
+-----------------+
| Tables_in_vskdb |
+-----------------+
| MyTable         |
+-----------------+
1 row in set (0.00 sec)
```

## 查看表结构

```sql
desc <table_name>;
```

输出的表格：

```
mysql> desc MyTable;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| sid   | tinyint | YES  |     | NULL    |       |
| sage  | tinyint | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
2 rows in set (0.01 sec)
```

Null：是否允许为空  
Extra: 对于该列的备注

## 表约束

### 主键

不能为空，并且唯一。例如姓名就不是主键，因为可以重复。身份证号可以是主键，每个人都不一样。

```sql
create table if not exists stu_table
(
  stu_id tinyint primary key,
  stu_name char(20) unique,
  stu_age tinyint not null
)
```

上面代码：
stu_id 被设置为主键，  
stu_name 被设置为唯一，  
stu_age 被设置为禁止为空。

## 如何执行 MySQL 脚本

在命令行中执行：

```sql
# mysql -u root -p 密码 < SQL脚本路径
```

数据库中执行：

```sql
mysql> source test.sql
```
