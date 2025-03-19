# 第 8.4 节 用户权限

## 权限

首先观察以下命令输出：

```sh
root@ykla:~ # ls -al /home/ykla
total 74
drwxr-xr-x  17 ykla ykla    27 Mar 19 17:57 .
drwxr-xr-x   3 root wheel    4 Mar 19 16:05 ..
-rw-------   1 ykla ykla    50 Mar 18 17:23 .Xauthority
drwx------   6 ykla ykla     6 Mar 10 16:21 .cache
drwx------   9 ykla ykla    12 Mar 19 15:01 .config
-rw-r--r--   1 ykla ykla   950 Feb 24 12:18 .cshrc
drwx------   3 ykla ykla     3 Mar  9 20:44 .dbus
-rw-r--r--   1 ykla ykla  6858 Mar  9 23:46 .face
drwxr-xr-x   2 ykla ykla     2 Mar  9 23:48 .icons
drwxr-xr-x   3 ykla ykla     3 Mar  9 20:44 .local
-rw-r--r--   1 ykla ykla   311 Feb 24 12:18 .login
-rw-r--r--   1 ykla ykla    79 Feb 24 12:18 .login_conf
-rw-------   1 ykla ykla   289 Feb 24 12:18 .mail_aliases
-rw-r--r--   1 ykla ykla   255 Feb 24 12:18 .mailrc
drwx------   4 ykla ykla     4 Mar 10 16:21 .mozilla
-rw-r--r--   1 ykla ykla   966 Feb 24 12:18 .profile
-rw-------   1 ykla ykla   200 Mar 19 17:57 .sh_history
-rw-r--r--   1 ykla ykla  1003 Feb 24 12:18 .shrc
drwxr-xr-x   2 ykla ykla     2 Mar  9 23:48 .themes
drwxr-xr-x   2 ykla ykla     2 Mar  9 20:45 下载
drwxr-xr-x   2 ykla ykla     2 Mar  9 20:45 公共
drwxr-xr-x   2 ykla ykla     2 Mar  9 20:45 图片
drwxr-xr-x   2 ykla ykla     2 Mar  9 20:45 文档
drwxr-xr-x   2 ykla ykla     2 Mar  9 20:45 桌面
drwxr-xr-x   2 ykla ykla     2 Mar  9 20:45 模板
drwxr-xr-x   2 ykla ykla     2 Mar  9 20:45 视频
drwxr-xr-x   2 ykla ykla     2 Mar  9 20:45 音乐
```

再观察：

```sh
----------   1 root wheel         0 Mar 19 22:26 test
```

FreeBSD 文件访问权限可以用 10 个标志位来说明（数一数第一列是不是 10 位），而这 10 个标志位由 4 部分组成：

第一部分是第 1 位，用 `d` 表示目录，`-` 表示普通文件，`l` 表示链接文件，`b` 表示块设备文件，`p` 表示管道文件，`c` 表示字符设备文件，`s` 表示套接字文件；

第二部分是第 2-4 位，用于标识文件所属用户对文件的访问权限，用 `rwx` 表示读、写、 执行（对于目录来说即访问，如  `ls`、`cd` 目录的权限）权限，无权限就写成 `-`；

第三部分是第 5-7 位，用于标识文件所属组成员对文件的访问权限。

第四部分是第 8-10 位，用于标识文件其他用户对文件的访问权限。

读、写、执行除了用 `rwx` 表示，也可以对应成数字 4、2、1，无权限即 0，每部分的数字相加后，组合在一起，就是 3 位数字的表示方式。（记忆口诀：“读 4 写 2 执行 1”）

如：

| 字符标识权限 | 数字标识权限 |   说明 |
| :----------: | :----------: | :-----: |
|  -rwxrwxrwx  |     777      |                         所有人都可读、写、执行的普通文件       |
|  -rwxr-xr-x  |     755      | 这是一个普通文件，所属用户有读、写、执行权限；同组用户和其他用户只能读取或执行，不可写入 |

>**思考题**
>
>>`drw-------`，即 `600` 这是一个目录，只有所属用户可以读、写。
>
>上面的说法正确吗，有意义吗，为什么？

## chmod 命令

可修改文件访问权限，有两种操作方式：

- 操作符方式，如：

```
$ chmod a+x test.sh
``` 

在 `a+x` 中:

第一位表示操作对象，`u` 是所属用户，`g` 是所属组，`o` 是其他用户，`a` 则表示所有用户，不写按系统默认操作;

第二位是操作符，`+` 是添加权限，`-` 是去除权限;

第三位是权限模式，`rwx` 分别表示读、写、执行，还有 `s`表示文件执行时把进程属主或组置成与文件属主或组一致。

- 数字方式，如： 

```sh
$ chmod 750 test.sh
```

其中 7 表示所属用户拥有读、写、执行的权限，同组用户有读和执行的权限，其他用户则没有任何权限，这种方式使用起来比较方便。

选项 `-R`，递归赋权

示例：

```sh
# chmod -R 777 /tmp # 允许任何用户读、写、执行 /tmp 目录下所有文件
# chmod -R a+rwx /tmp # 允许任何用户读、写、执行 /tmp 目录下所有文件
```

## `chown` 命令

了修改文件的属主，包括所属用户和所属组。


选项 `-R`，递归赋权

示例：

```sh
# chown test1 t.sh # 修改 t.sh 属主为用户 test1
# chown test1:test t.sh # 修改 t.sh 属主为用户 test1、组 test
# chown -R test1:test /tmp # 修改/tmp 目录下所有文件的属主为用户 test1、组 test
```
