# 关系型数据库基础

关系型数据库是一种基于关系模型的数据库系统，采用二维表格形式存储数据，并通过表与表之间的关联关系实现数据的组织、管理与查询。

关系型数据库管理系统（Relational Database Management System, RDBMS）通过结构化查询语言（Structured Query Language, SQL）提供数据定义、数据操作和数据控制功能，并利用事务机制保障数据的一致性与完整性。

本部分介绍关系型数据库的基本操作与 SQL 语法。

## 在 UNIX 系统中连接数据库并执行 SQL 脚本

在 UNIX 或类 UNIX 系统中，可通过命令行连接数据库并执行 SQL 脚本。数据库客户端程序通过网络协议（如 MySQL 的 TCP/IP 协议）与数据库服务器通信，发送 SQL 语句并接收执行结果。

以下命令用于连接 MySQL 数据库并执行 SQL 脚本：

```sh
# mysql -u root -p          # 以 root 用户登录 MySQL，-u 指定用户名，-p 表示需要密码验证
# source FileName.sql       # 在 MySQL 交互式界面中执行指定的 SQL 文件，source 命令读取文件内容并逐条执行 SQL 语句
```

## 建立数据库

在关系型数据库中，创建数据库是使用数据库的第一步。数据库是存储相关数据表的容器，每个数据库具有独立的权限控制机制与存储空间。

可通过 SQL 语句创建新的数据库。数据库管理系统将在磁盘上分配空间并创建系统表以管理数据库元数据。

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

在 MySQL 中，`RENAME DATABASE` 语句存在于早期版本中，但在 MySQL 5.1.23 之后已被移除，原因是该操作存在安全风险。

现代 MySQL 版本中，重命名数据库需通过导出数据、创建新数据库、导入数据的方式实现。

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

- `tinyint`（1B）、`smallint`（2B）、`mediumint`（3B）、`int`（4B）、`bigint`（8B）
- `float`（4B）、`double`（8B）、`decimal(整体位数, 小数点后位数)`
- `char` 是字符类型，若要存储字符串需使用 `char(字符数)`
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

在脚本中添加注释是一种推荐实践，可提高代码的可读性与可维护性。注释应说明代码的意图、业务逻辑或特殊处理，而非简单重复代码本身的功能。

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
);
```

## 信息写入表

```sql
insert into table_name (col1, col2) values (123, "李明");
```

- `col1`：列名 1
- `col2`：列名 2

## 表新增列

```sql
alter table table_name
add column new_col data_type;
```

- `new_col`：新列名
- `data_type`：数据类型

## 表删除列

```sql
alter table 表名 drop column 列名;
```

## 修改表列数据类型

```sql
alter table table_name modify column col_name new_data_type;
```

- `new_data_type`：新数据类型

## 表添加主键

```sql
alter table table_name
add primary key (col_name);
```

- `col_name`：作为主键的列名（通常为已存在的列）

## 表删除主键

```sql
alter table table_name drop primary key;
```

## 唯一性约束

### 表添加唯一性约束

```sql
alter table table_name
add constraint constraint_name unique (col_name);
```

- `constraint_name`：唯一约束名
- `col_name`：列名

### 表删除唯一性约束

```sql
alter table table_name
drop index constraint_name;
```

## 外键

### 添加外键

```sql
ALTER TABLE table_name
ADD CONSTRAINT fk_column_name
FOREIGN KEY (fk_column)
REFERENCES tstu(sid);
```

- `fk_column_name`：外键名
- `fk_column`：子表中的外键列名

### 删除外键

```sql
alter table table_name
drop foreign key fk_name;
```

- `table_name`：子表名
- `fk_name`：外键名

### 外键的概念

外键是用于建立并强制两个表之间关联关系的一列或多列。它指向另一个表的主键或唯一键，以确保数据的一致性与完整性。数据库管理系统在外键约束上维护参照完整性，确保子表中的外键值必须存在于父表的主键或唯一键中，或者为 NULL（如果允许）。

- 父表：外键引用的表。父表中的被引用列通常是主键（PRIMARY KEY）或唯一键（UNIQUE）。例如上文示例中的父表。
- 子表：包含外键的表。子表中的外键列指向父表中的主键或唯一键。例如上文示例中的子表。

### 父表数据删除失败

- 原因：子表中存在引用该数据的记录。数据库管理系统会阻止删除操作以维护参照完整性。
- 解决：使用 `ON DELETE CASCADE` 自动删除子表中的相关记录，或先手动删除子表中的记录，再删除父表中的记录。
- `ON DELETE CASCADE` 是外键约束的一个选项，当父表记录被删除时，数据库自动删除子表中所有引用该记录的行。这个机制在“自动维护父表和子表之间的参照完整性”一节中有详细说明。

### 父子表和外键示例

```sql
-- 创建父表 customers，包含以下列：
CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY, -- 主键，自动编号
    name VARCHAR(100) NOT NULL,        -- 客户名
    email VARCHAR(150) UNIQUE          -- 唯一的电子邮件
);

-- 创建子表 orders
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY, -- 主键，订单编号
    order_date DATE NOT NULL,                -- 订单日期
    customer_id INT,                         -- 外键列，关联客户 ID
    amount DECIMAL(10,2),                    -- 订单金额
    FOREIGN KEY (customer_id) REFERENCES customers(id) -- 定义外键
    ON DELETE CASCADE -- 当父表记录被删除时，级联删除子表相关记录
    ON UPDATE CASCADE -- 当父表主键更新时，子表外键自动更新
);
```

1. 创建父表 customers：
   包含列：
   id：主键，用于唯一标识客户。
   name：客户姓名。
   email：唯一约束，用于防止重复的电子邮件地址。
2. 创建子表 orders：
   order_id：主键，用于唯一标识订单。
   order_date：记录订单日期。
   customer_id：外键列，用于关联客户。
   amount：订单金额。
3. 设置外键：
   `FOREIGN KEY (customer_id) REFERENCES customers(id)` 表示子表的 customer_id 列引用父表的 id 列。
   `ON DELETE CASCADE` 删除父表记录时，子表中引用该记录的行也会被删除。
   `ON UPDATE CASCADE` 更新父表主键时，子表外键列会自动更新。

## 修改列的数据类型

```sql
ALTER TABLE 表名
MODIFY COLUMN 列名 新数据类型;

-- 例如（重设数据类型并不允许为空、设置默认值）
ALTER TABLE book_table
MODIFY COLUMN BookName CHAR(100) NOT NULL DEFAULT "《书名》";

-- 如果修改的列是外键，必须先删除外键约束，然后修改数据类型，最后重新添加外键约束
alter table 子表 drop FOREIGN KEY 外键名;
alter table 子表 modify column 列名 新数据类型;
alter table 子表 add constraint 外键名 FOREIGN KEY (列名) REFERENCES 父表名(父列名);
```

## 修改表信息、删除行

```sql
-- 修改表信息
update 表名
set 列名 = 新值
where 条件;
```

SET 子句用于指定需要修改的列。如果仅希望修改部分记录，需通过 WHERE 子句限定条件，以明确修改范围。

```sql
-- 删除行
DELETE FROM book_table
WHERE BookNumber < 200;
```

下面给出几个示例：

```sql
update book_table
set Price = Price * 1.2
where Publisher = "人民邮电出版社";
```

该示例将表 `book_table` 中 `Publisher` 值为“人民邮电出版社”的记录，其 `Price` 值统一乘以 `1.2`，即在原价基础上增加 20%。

```sql
DELETE FROM book_table
WHERE BookNumber < 200;

DELETE FROM book_table
WHERE author IN ('王阳', '刘天洋');
```

### WHERE 子句

WHERE 子句是 SQL 语句中的重要组成部分，用于指定筛选条件，仅对符合条件的记录进行操作。

```sql
...(update 或 delete)
where Price < 50;
...(update 或 delete)
WHERE author = '王阳' or author = '刘天洋';
...(update 或 delete)
WHERE name in ('张三', '李四');
```

1. 如果 `Price` 值小于 50，就...
2. 如果 `author` 值是王阳或者刘天洋，就...
3. 如果 `name` 值是张三或李四，就...

WHERE 子句用于指定条件表达式，该表达式会计算并返回一个布尔值。

### SQL 运算符

运算符是 SQL 语句中用于进行数据计算和比较的符号，分为算术运算符、比较运算符、逻辑运算符和特殊运算符等几类。

#### 算术运算符

- `+` 加法运算符
- `-` 减法运算符
- `*` 乘法运算符
- `/` 除法运算符
- `%` 取模运算符

#### 比较运算符

- `=` 等于（在 SQL 中用于比较，而非赋值）
- `!=` 不等于
- `<` 小于
- `>` 大于
- `<=` 小于等于
- `>=` 大于等于
- `<=>` NULL 安全等于，NULL <=> NULL，返回结果是 TRUE

#### 逻辑运算符

- `and` 两条件都为真时才返回真，否则为假
- `or` 两条件有一个为真时就是真，全为假时才为假
- `not` 反转真假
- `xor` 仅一个条件为真时才返回真，否则返回假

#### 特殊运算符

- `in`：“值在列表中”运算符，用于筛选符合条件的记录，并返回布尔结果，供 update 或 delete 语句使用。例如 `5 in (1, 3, 5)` 返回真。
- `between` 范围匹配：例如 `5 between 1 and 10` 返回真。
- `like` 模式匹配：`'abc' like 'a%'` 返回真。百分号在这里类似 sh 的通配符。
- `IS NULL`“判断表项是否为 NULL”：`NULL IS NULL` 返回 TRUE。
示例：查看书名条目是否存在 `《xxx 设计 yyy》`。

```sql
select * from book_table
where BookName like '%设计%';

select * from book_table
where BookName like '_____';
-- 五个下划线代表五个字，返回长度为 5 个字的书名。
```

在一个书籍管理库中，使用 LIKE '%设计%' 会返回类似《MySQL 数据库设计》的书名。这展示了模式匹配在查询中的应用。通过上述说明，可以更好地理解 WHERE 子句中条件表达式的含义以及如何构建有效的查询条件。

## 自动维护父表和子表之间的参照完整性

参照完整性是数据库的重要特性，它确保相关表之间数据的一致性。当父表中的数据发生变化时，子表中的相关数据也需相应调整。

- **CASCADE** 级联操作：父表记录删除/更新时，子表中相关记录也被删除/更新。
- **SET NULL** 将子表中的外键列设置为 NULL（要求外键列允许 NULL）。
- **RESTRICT** 拒绝操作：不允许删除/更新父表中被引用的记录（立即返回错误）。
- **NO ACTION** 类似 RESTRICT。在 MySQL 中，二者完全等价，均立即拒绝违反参照完整性的操作。在 SQL 标准中，NO ACTION 在语句结束时检查完整性，而非延迟到事务结束。
- **SET DEFAULT** 设置为默认值，MySQL 不支持。

## SELECT 语句

SELECT 语句是 SQL 中最常用的查询语句，用于从数据库中检索数据。SELECT 语句执行时，数据库管理系统解析查询语法，生成查询执行计划，访问存储引擎获取数据，应用过滤条件，最后返回结果集给客户端。

SELECT 关键字后指定要查询的列名，使用 `*` 表示选择所有列。SELECT 语句的基本语法包括 SELECT 子句（指定要返回的列）、FROM 子句（指定数据源表）、WHERE 子句（指定过滤条件）、GROUP BY 子句（分组聚合）、HAVING 子句（分组过滤）和 ORDER BY 子句（结果排序）。

```sql
select * from student_table
where age = (select max(age) from student_table);
```

该查询用于显示 student_table 中年龄等于该表最大年龄值的记录。这是一个嵌套查询示例：内部子查询 `(select max(age) from student_table)` 首先执行，返回表中的最大年龄值；外部查询使用 WHERE 子句过滤出年龄等于该最大值的所有记录。数据库管理系统可能优化此类查询，使用索引加速最大值的查找。

### 升序输出和降序输出

排序是查询的重要功能，通过 ORDER BY 子句可以指定查询结果的排序方式。

ASC 升序，DESC 降序。

```sql
SELECT student_name FROM student_table ORDER BY student_name DESC;
```

`LIMIT a, b` 用于限制查询结果的数量，其中 a 表示起始位置（从 0 开始），b 表示返回的记录条数。

```sql
SELECT * from `学生表`
ORDER BY `学号` desc
LIMIT 0,3;
```

### 连接查询

连接查询是关系型数据库的核心功能之一，它允许从多个相关联的表中同时获取数据。

#### 显式连接

```sql
SELECT name, score --name 来自学生表，score 来自分数表
FROM stu_table -- 表一
JOIN score_table -- 表二
ON stu_table.stu_id = score_table.s_id; -- 连接条件
WHERE name = 'Jack' -- 筛选条件，后面还可以接上 AND 或 OR。
```

`name` 取自 `stu_table`
`score` 取自 `score_table`

#### 隐式连接

```sql
SELECT name, score
FROM stu_table, score_table
WHERE stu_table.stu_id = score_table.s_id
AND name = 'Jack';
```

虽然隐式连接语法较为简洁，但在实际开发中更推荐使用显式连接，以提高可读性和可维护性。显式连接使用明确的 JOIN 关键字，清晰地表达了表之间的连接关系，而隐式连接将连接条件放在 WHERE 子句中，可能导致代码意图不够清晰。

## 课后习题

1. 在 FreeBSD 系统上部署 PostgreSQL 数据库，创建包含外键约束的父子表，并验证其参照完整性机制。
2. 选取 MySQL 的外键约束机制，设计一组不使用外键的等价方案。
3. 修改数据库的默认隔离级别，执行并发读写操作并观察数据一致性变化。
