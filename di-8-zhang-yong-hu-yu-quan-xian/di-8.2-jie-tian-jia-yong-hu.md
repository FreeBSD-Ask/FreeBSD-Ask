# 第 8.2 节 添加用户

示例：创建一个普通用户（用户名为 `ykla`），并将其添加到 `video` 分组：

```shell-session
# adduser -g video -s sh -w yes
# Username: ykla
```

示例：创建一个名为 test 的用户，并添加其到 video 组，设置其默认 shell 是 csh：

```shell-session
root@ykla:/ #  adduser
Username: test #用户名
Full name:  #全名，可留空
Uid (Leave empty for default): # UID 设置，可留空
Login group [test]: #登录组
Login group is test. Invite test into other groups? []: video #设置要加入的组，多个用空格隔开，可留空
Login class [default]: #登录分类，可留空
Shell (sh csh tcsh git-shell bash rbash nologin) [sh]: csh  #手动设置默认 shell，否则 shell 为 sh
Home directory [/home/test]: #指定家目录
Home directory permissions (Leave empty for default): #指定家目录权限
Use password-based authentication? [yes]:  #是否使用密码
Use an empty password? (yes/no) [no]:   #是否空密码
Use a random password? (yes/no) [no]:   #是否随机密码
Enter password: #输入密码
Enter password again: #重复输入密码
Lock out the account after creation? [no]: #锁定账号？
Username   : test
Password   : *****
Full Name  :
Uid        : 1002
Class      :
Groups     : test video
Home       : /home/test
Home Mode  :
Shell      : /bin/csh
Locked     : no
OK? (yes/no): yes #检查有错误否
adduser: INFO: Successfully added (test) to the user database.
Add another user? (yes/no): no #还需要创建另一个账号吗？
Goodbye!
```
