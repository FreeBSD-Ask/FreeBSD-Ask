# 4.6 文本编辑器

## `ee` 编辑器基本用法

>**注意**
>
>`ee` 编辑器不支持中文。已经报告 Bug [Bug 291279 - [Feature Request] Add UTF-8 Support to ee(1)](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=291279)。

`ee` 是 FreeBSD 基本系统内置的编辑器。

`ee` 的用法比 [nano](https://www.redhat.com/zh/blog/getting-started-nano)（一款 GNU 编辑器）还要简单许多，从其名字“easy editor”（简单的编辑器）即可看出。

比如使用 ee 编辑器打开 `a.txt` 文件：

```sh
# ee a.txt
```

可以直接进行编辑，用法与 `nano` 或 Windows 记事本类似。

按 **ESC 键** 会显示提示框，再按两次 **回车键** 即可保存。


## `vi` 编辑器基本用法

FreeBSD 还内置了一款编辑器 `vi`，其用法较为复杂。有别于大多数类 UNIX 操作系统将 `vi` 链接到 `vim` 的做法，BSD 系统中提供的是真正的 `vi`（实际上是 `nvi`，即 New vi，是 4.4BSD 的重新实现）。

### macOS 下的 `vi`

显示 macOS 中 `/usr/bin/vi` 的详细文件信息：

```sh
$ ls -al /usr/bin/vi
lrwxr-xr-x  1 root  wheel  3  4 12 13:16 /usr/bin/vi -> vim
```

### FreeBSD 下的  `vi`

打开 BSD 的 `vi` 后默认处于“命令模式”，此时输入 `i` 可以进入“文本模式”，从而进行文本编辑。需要注意的是，**删除键（退格键）** 在该模式下不起作用，其行为与 **Insert 键** 相同。若要删除文本，需要使用 **Delete 键**。


```sh
bc123
~      
~
~
```

>**技巧**
>
>空行会显示为 `~`。

编辑完成后，按 **ESC 键** 即可从文本模式返回命令模式。

在命令模式下输入 `:` 可进入命令输入状态，例如：`:q` 表示不保存退出，`:wq` 表示保存并退出，`:wq!` 表示强制保存，`:q!` 表示强制退出。


```sh
ABC
~
~
:wq
```

## microsoft-edit

microsoft-edit 是微软开源的文本编辑器，原生支持中文，交互界面简单，并支持鼠标操作。

- 使用 pkg 安装：

```sh
# pkg ins microsoft-edit
```

- 还可以使用 Ports 安装：

```sh
# cd /usr/ports/editors/microsoft-edit/ 
# make install clean
```

使用 msedit 编辑器打开 `abc.txt` 文件：

```sh
$ msedit abc.txt
```

![](../.gitbook/assets/msedit1.png)

![](../.gitbook/assets/msedit2.png)

操作较为简单，此处不再展开说明。
