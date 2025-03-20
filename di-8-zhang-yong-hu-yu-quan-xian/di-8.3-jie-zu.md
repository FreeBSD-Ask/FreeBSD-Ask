# 第 8.3 节 组

## `pw` 命令

在 FreeBSD 中，用户和组可以用 `pw` 命令管理：

- 创建 `admin` 分组，并添加 `ykla` 和 `root` 两位用户：

```sh
# pw groupadd admin
# pw groupmod admin -m ykla root
```

- 创建 `wheel` 组，只添加 `root` 用户：

```sh
# pw groupadd wheel
# pw groupmod wheel -m root
```

- 从 `admin` 组里移除用户 `ykla`：

```sh
# pw groupmod admin -d ykla
```

- 删除 `admin` 组：

```sh
# pw groupdel admin
```

---

`admin` 和 `wheel` 权限的区别：

- `admin`，具有管理系统的权限（sudo 的默认配置如此），可以使用 `sudo` 命令。
- `wheel`，超级管理员权限，可以任意修改系统（该名称来源于俚语 big wheel，即大人物）。


## `useradd` 命令

用于新建用户

示例：

```sh
# pw useradd test1 #创建用户 test1，uid 系统默认，test1 组，登陆环境/bin/sh，主目录未创建
# pw useradd test2 -u 1200 -m -d /tmp/test -g test1 -G wheel -s csh -c test2 #创建用户 test2，uid 为 1200，创建主目录，主目录为/tmp/test，test1 组，有管理员权限，登陆环境/bin/csh，全名 test2
# echo password | pw useradd test3 -h 0 #创建用户 test3，同时设置密码为 password
```

## `usermod` 命令

用于修改用户信息，常用参数：

`-l`，为用户改名 其他参数参考 useradd 子命令。

示例：

```sh
# pw usermod test1 -G wheel #为用户 test1 增加管理员权限
# pw usermod test1 -l myuser #用户 test1 改名为 myuser
# echo password | pw usermod test2 -h 0 #修改用户 test2 密码为 password
```

## `userdel` 命令

用于删除用户，常用参数：

`-r`，删除用户同时删除用户主目录及所有相关信息，不使用该参数则信息保留，仅删除用户

示例：

```sh
# pw userdel test2 -r
```

## `usershow` 命令

用于显示用户信息，

示例：

```sh
# pw usershow test2
```

## `usernext` 命令

可返回下一个可用的 uid，

示例：

```sh
# pw usernext
```

## `lock` 命令

锁定账号，锁定后账号无法登录使用，

示例：

```sh
# pw lock test2
```

## `unlock` 命令

解锁账号，解锁后账号可以正常使用，

示例：

```sh
# pw unlock test2
```

## `groupadd` 命令

用于新建组，常用参数：

```sh
-g，指定 gid，不指定则由操作系统根据已存在的 `gid` 自动生成

-M，指定组成员列表，多个用户用逗号隔开
```

示例：

```sh
# pw groupadd test -g 1200 #创建组 test，gid 为 1200，注意，gid 与 uid 不是一回事
# pw groupadd test5 -M test1,test2 #创建组 test5，成员有 test1 和 test2
```

## `groupmod` 命令

用于修改组信息，常用参数：

`-g`，指定新的 `gid`

`-l`，为组改名

`-M`，替换现有组成员列表，多个用逗号隔开

`-m`，为现有组成员列表增加新的成员

其他参数参考 `groupadd` 命令。

示例：

```sh
# pw groupmod test -g 1300 #修改 test 组的 gid 为 1300
# pw groupmod test -l mygroup 组 test 改名为 mygroup
# pw groupmod test5 -M test1 #设置组 test5 的成员为 test1
# pw groupmod test5 -m test3 #为组 test5 增加成员 test3
```

## `groupdel` 命令

用于删除组，

示例：

```sh
# pw groupdel mygroup
```

## `groupshow` 命令

用于显示组信息，

示例：

```sh
# pw groupshow test
```

## `groupnext` 命令

可返回下一个可用的 `gid`，

示例：

```sh
# pw groupnext
```

## 其他用户管理命令

- `adduser` 命令，用于新建用户，与 `pw` 相比，`useradd` 的区别在于该命令是交互式的，安装操作系统时自建的用户，就是基于该命令创建的。
- `rmuser` 命令，用于删除用户，与 `adduser` 命令一样，也是交互式的。不过该命令有 `-y` 参数，且能列出用户列表，

示例：

```sh
# rmuser -y test1 test2 #同时删除用户 test1 和 test2，
```

\-y 参数用于省略询问步骤

- `chpass` 命令，以 `vi` 编辑器方式打开并修改指定用户信息，如不指定用户则默认为当前用户。

常用参数：`-s`，用于登录环境

示例：

```sh
# chpass -s csh test1 # 更换用户 test1 的登陆环境为 /bin/csh
# chpass # 以 vi 方式打开当前用户信息进行修改
# passwd # 修改用户密码，如不指定用户则默认为当前用户。
```

示例： `passwd 用户名` 

回车后根据系统提示设置用户密码。


