# 关系型数据库基础

关系型数据库是一种基于关系模型的数据库。它使用表格来存储数据，通过表与表之间的关联来实现数据的管理和查询。

关系型数据库管理系统（RDBMS）通过 SQL 语言提供数据定义、数据操作和数据控制功能，并使用事务机制确保数据的一致性和完整性。

本部分将介绍关系型数据库的基本操作和 SQL 语法。

## 在 UNIX 系统中连接数据库并执行 SQL 脚本

在 UNIX 或类 UNIX 系统中，可以通过命令行连接数据库并执行 SQL 脚本。数据库客户端程序通过网络协议（如 MySQL 的 TCP/IP 协议）与数据库服务器通信，发送 SQL 语句并接收结果。

以下命令用于连接 MySQL 数据库并执行 SQL 脚本：

```sh
# mysql -u root -p          # 以 root 用户登录 MySQL，-u 指定用户名，-p 表示需要密码验证
# source FileName.sql       # 在 MySQL 交互式界面中执行指定的 SQL 文件，source 命令读取文件内容并逐条执行 SQL 语句
```

## 建立数据库

在关系型数据库中，创建数据库是使用数据库的第一步。数据库是存储相关数据表的容器，每个数据库有独立的权限控制和存储空间。可以通过 SQL 语句来创建新的数据库，数据库管理系统会在磁盘上分配空间并创建系统表来管理数据库元数据。

```sql
create database db_name;
```

- `db_name`：数据库名，用于标识数据库。数据库名在数据库实例中必须唯一。

## 数据库重命名

```sql
rename database old_name to new_name;
```

- `old_name`：旧数据库名，要重命名的数据库当前名称
- `new_name`：新数据库名，重命名后的数据库名称

在 MySQL 中，`RENAME DATABASE` 语句在早期版本中存在，但在 MySQL 5.1.23 之后被移除，因为该操作存在安全风险。现代 MySQL 版本中，重命名数据库需要通过导出、创建新数据库、导入数据的方式实现。

## 查看数据库

```sql
show databases;
```

## 进入数据库

```sql
use db_name;
```

- `db_name`：数据库名

## 删除数据库

```sql
drop database db_name;
```

- `db_name`：数据库名

## 更改数据库字符集

```sql
alter database xxx
default character set utf8mb4;
```

- `xxx`：数据库名
- `utf8mb4`：字符集名称，指定数据库的默认字符集

## SQL 数据类型

SQL 数据类型定义了表中列可以存储的数据种类和格式。正确选择数据类型对于数据存储效率和查询性能至关重要。

- `tinyint` (1B), `smallint` (2B), `mediumint` (3B), `int` (4B), `bigint` (8B)
- `float` (4B), `double` (8B), `decimal(整体位数, 小数点后位数)`
- `char` 是字符类型，想存字符串用 `char(字符数)`
- `unsigned + 数据类型` 可设置为无符号的数据类型

## 建立表

```sql
create table table_name (
  column_name data_type,
  column_name data_type,
  column_name data_type
);
```

- `table_name`：表名
- `column_name`：列名
- `data_type`：数据类型

## 表重命名

```sql
alter table old_name rename to new_name;
```

- `old_name`：旧表名
- `new_name`：新表名

## 查看数据库中有哪些表

```sql
show tables;
```

## 展示表结构

```sql
desc table_name;
```

## 显示表全部信息（select * from 表名）

```sql
select * from table_name;
```

## SQL 语法：注释

单行注释：

```sql
-- 这是单行注释：注释不会被执行，用于说明 SQL 语句的用途或注意事项
```

多行注释：

```sql
/* 
   这里是多行注释
   可以跨越多行，用于描述复杂的业务逻辑或临时禁用代码块
*/
```

在脚本中添加注释是一种最佳实践，可以提高代码的可读性和可维护性。注释应当说明代码的意图、业务逻辑或特殊处理，而不是简单重复代码本身的功能。

## 主键、唯一约束、非空约束与自动编号

```sql
create table 表名
(
  -- 主键
  列名 数据类型 primary key,
  -- 唯一
  列名 char(20) unique,
  -- 不允许为空
  列名 数据类型 not null,
  -- 自动编号
  列名 数据类型 auto_increment