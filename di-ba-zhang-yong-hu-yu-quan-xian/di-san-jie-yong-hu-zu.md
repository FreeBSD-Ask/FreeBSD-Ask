# 第三节 用户组



创建一个 `admin` 分组，并添加 `ykla` 和 `root` 两位用户：

```
# pw groupadd admin
# pw groupmod admin -m ykla root
```

创建一个 `wheel` 分组，只添加 `root` 用户：

```
# pw groupadd wheel
# pw groupmod wheel -m root
```

从 `admin` 组里移除用户 `ykla`：

```
# pw groupmod admin -d ykla
```

删除 `admin` 用户组：

```
# pw groupdel admin
```

`admin` 和 `wheel` 权限的区别：

* `admin`，具有管理系统的权限（sudo 的默认配置如此），可以使用 `sudo` 命令。
* `wheel`，超级管理员权限，可以任意修改系统（该名称来源于俚语 big wheel，意为大人物）。
