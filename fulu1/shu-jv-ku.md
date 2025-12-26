# 关系型数据库基础

## UNIX 中连接到数据库、执行 SQL 脚本

```sh
# mysql -u root -p
# source FileName.sql
```

## 建立数据库

```sql
create database db_name;
```

- `db_name`：数据库名

数据库命名区分大小写，最长 64 字符，别名最长 256 字符，不能使用数据库关键字。

## 数据库重命名

```sql
rename database old_name to new_name;
```

- `old_name`：旧数据库名
- `new_name`：新数据库名


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
default character set UTF-8;
```

## SQL 数据类型

- `tinyint` (1B), `smallint` (2B), `mediumint` (3B), `int` (4B), `bigint` (8B)  
- `float` (4B), `double` (8B), `decimal(整体位数，小数点后位数)`  
- `char` 是字符类型，想存字符串用 `char(字符数)`  
- `unsigned + 数据类型` 可以设置为无符号的数据类型。

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

## 查看数据库有哪些表

```sql
show tables;
```


## 展示表结构

```sql
desc tables;
```


## 显示表全部信息（select 后面细说）

```sql
select * from tables;
```

## SQL 语法：注释

```sql
-- 注释不会被执行
```

写脚本加注释是一个好习惯，防止你过一段时间不知道自己写的什么...

## 主键、唯一、不许为空、自动编号

```sql
create table 表名
(
  -- 主键
  列名 数据类型 primary key,
  -- 唯一
  列名 char(20) unique,
  -- 不许为空
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
alter table 表名 drop 列名;
```

## 表修改列数据类型

```sql
alter table table_name modify column col_name new_data_type;
```

- `new_data_type`：新数据类型


## 表添加主键

```sql
alter table table_name
add primary key (col_name);
```

- `col_name`：新列名

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

### 表添加外键

```sql
ALTER TABLE table_name
ADD CONSTRAINT fk_column_name
FOREIGN KEY (fk_column)
REFERENCES tstu(sid);
```

- `fk_column_name`：外键名
- `fk_column`：外部表格列名

### 表删除外键

```sql
alter table table_name
drop foreign key fk_name;
```

- `table_name`：子表名
- `fk_name`：外键名

### 外键的概念


- 父表：外键引用的表。父表中的被引用列通常是主键（PRIMARY KEY）或唯一键（UNIQUE）。例如上面的黄色表。
- 子表：包含外键的表。子表中的外键列指向父表中的主键或唯一键。例如上面的绿色表。

### 删除父表数据时失败

- 原因：子表中存在引用该数据的记录。
- 解决：使用 `ON DELETE CASCADE` 或先删除子表中的记录。
- `ON DELETE CASCADE` 又是一堆内容，先略过。看 [往下数三个章节](##自动维护父表和子表之间的参照完整性)。

### 下面是一个父、子表格和外键的示例

```sql
-- 创建父表 customers
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

## 修改列数据类型

```
ALTER TABLE 表名
MODIFY COLUMN 列名 新数据类型;

-- 例如（重设数据类型并不许为空、设置默认值）
ALTER TABLE book_table
MODIFY COLUMN BookName CHAR(100) NOT NULL DEFAULT "《书名》";

-- 如果修改的列是外键，必须先删除外键约束，然后修改数据类型，再重新添加外键
alter table 子表格 drop FOREIGN KEY 外键名;
alter table 子表格 modify column 列名 新数据类型;
alter table 子表格 add constraint 外键名 FOREIGN KEY (列名) REFERENCES 父表名(父列名);
```

## 修改表信息、删除行

```
-- 修改表信息
update 表名
set 列名 = 新的值
where 条件;
```

注：set 你选择了一整列，想修改单个或多个位置的值，就需要 where 的条件来限定，你是要修改整列，还是其中哪个。类似横竖交叉定位一个坐标点。

```sql
-- 删除行
DELETE FROM book_table
WHERE BookNumber < 200;
```

下面给几个示例：

```sql
update book_table
set Price = Price * 1.2
where Publisher = "人民邮电出版社";
```

翻译成人话：将表 `book_table` 中 `Publisher` 值为 `"人民邮电出版社"` 的行，Price 值全乘以 `1.2`（就是增加 20%）

```sql
DELETE FROM book_table
WHERE BookNumber < 200;

DELETE FROM book_table
WHERE author IN ('王阳', '刘天洋');
```

### “Where 子句”


```
...(update 或 delete)
where Price < 50;
...(update 或 delete)
WHERE author = '王阳' or author = '刘天洋';
...(update 或 delete)
WHERE name in ('张三', '李四');
```

1. 如果 `Price` 值小于 50，就...
2. 如果 `author` 值是王阳或者刘天洋，就...
3. 如果 `name` 值是张三或者李四，就...
   where 接收写在后面的表达式，表达式会运算出一个布尔值。

### 这里就需要一个知识：SQL 运算符

#### 算术运算符

- `+` 加法运算符
- `-` 减法运算符
- `*` 乘法运算符
- `/` 除法运算符
- `%` 取模运算符

#### 比较运算符

- `=` 等于（也是赋值运算符）
- `!=` 不等于
- `<` 小于
- `>` 大于
- `<=` 小于等于
- `>=` 大于等于
- `<=>` NULL 安全等于，NULL <=> NULL，返回结果是 TRUE

#### 逻辑运算符

- `and` 两条件都为真才返回真，否则为假
- `or` 两条件有一个为真就是真，全是假才为假
- `not` 反转真假
- `xor` 仅一个条件为真才返回真，否则返回假。

#### 特殊运算符

- `in` ：“值在列表中”运算符，用来筛选符合条件的表项，并对符合的项返回一个“真”的布尔值，交给前面 update 或者 delete 进行操作。例如 `5 in (1, 3, 5)` 返回真。
- `between` 范围匹配：例如 `5 between 1 and 10` 返回真。
- `like` 模式匹配：`'abc' like 'a%'` 返回真。百分号在这里类似 sh 的通配符。
- `IS NULL` ”判断表项是否为 NULL“：`NULL IS NULL` 返回 TRUE。  
  例子：查看书名有没有叫《xxx 设计 xxx》的

```sql
select * from book_table
where BookName like '%设计%';

select * from book_table
where BookName like '_____';
-- 五个下划线代表五个字，返回长度为 5 个字的书名。
```

在一个书籍管理库中会返回类似《mysql 数据库设计》的书名。

这样一来，上面 where 后面的东西不就能看懂了？

## 自动维护父表和子表之间的参照完整性

- **CASCADE** 级联操作：父表记录删除/更新时，子表中相关记录也被删除/更新。  
- **SET NULL** 将子表中的外键列设置为 NULL（要求外键列允许 NULL）。  
- **RESTRICT** 拒绝操作：不允许删除/更新父表中被引用的记录（立即返回错误）。  
- **NO ACTION** 类似 RESTRICT，但延迟到事务结束时才检查完整性。  
- **SET DEFAULT** 设置为默认值，MySQL 不支持。

## SELECT 语句

select 后面是列名，写上 `*` 则是选择所有列

```sql
select * from student_table
where age=(select max(age) from student_table;);
```

显示 student_table 中，年龄为“student_table 中‘年龄为最大值’的条目”

### 升序输出和降序输出

ASC 升序，DESC 降序。

```sql
SELECT student_name FROM student_table DESC;
```

`LIMIT a, b` 截取内容。a 是索引，从 0 开始，b 是偏移量，写几就偏移几。

```sql
SELECT * from `学生表`
ORDER BY `学号` desc
LIMIT 0,3;
```

### 怎么将别的表给带上（连接查询）

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

显然隐式连接更加简洁，所以这里推荐大家使用。
