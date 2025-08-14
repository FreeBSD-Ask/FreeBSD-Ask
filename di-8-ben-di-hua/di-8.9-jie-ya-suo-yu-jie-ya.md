# 6.9 压缩和解压

## zip

>**技巧**
>
>zip 中文或非英文字符乱码是很正常的一件事。因为编码不同，而一般国产操作系统（如 UOS、UbuntuKylin）之所以不乱码是打了补丁的。至于为什么这个补丁没有提交到上游，有知道的人欢迎 PR。

### 安装 zip

- 使用 pkg

```sh
# pkg install zip
```

- 使用 ports

```sh
# cd /usr/ports/archivers/zip/
# make install clean
```

### zip 压缩与解压



- 解压 zip

zip 解压的话，基本系统自带 `unzip`，不用安装。

```sh
$ zip test.zip test # 压缩成 zip 文件
```

- 压缩成 zip

```
$ unzip test.zip # 解压 zip 文件到当前路径
$ unzip test.zip -d /home/ykla/test # 解压到指定路径，-d 即 directory，目录的意思
```

## tar

基本系统自带 `tar`，不用安装。

tar 即“tape archive”（磁带归档），最早是为了在磁带上进行存储的。

>**思考题**
>
>>归档文件包就是压缩率为 `0` 的文件集合（将多个文件/目录打包成一个单一文件便于存储）。单纯的 `tar` 操作仅打包，不压缩。而压缩的本质是通过某种算法缩减文件所占用的体积，而非针对目录。所以常见压缩软件本质上是先将目录归档成为文件，然后再将其压缩。
>
>如何理解归档与压缩的关系？

### 解压 tar



```sh
$ tar -xvf test.tar # 解压 tar 格式文件、包括不限于 test.tar.bz2、test.tar.gz、test.tar.xz：
$ tar -xvf test.tar -C /home/ykla/mytest # 解压到指定路径
```

- `x`：Extract 解压的意思
- `v`：verbose 啰嗦模式即输出详细信息
- `f`：file 指定文件
- `C`：`cd` 的意思，即指定路径

### 压缩成 tar
  
```sh
$ tar -cvf test.tar test # 压缩成 tar 格式文件。-c 即 Create，创建；
$ tar -zcvf test.tar.gz test # 压缩成 gzip 格式文件。-z 即 gzip
$ tar -jcvf test.tar.bz2 test # 压缩成 bzip2 格式文件。参数 -j 即 bzip2，请注意大小写
$ tar -Jcvf test.tar.xz test # 压缩成 xz 格式文件。参数 -J 即 xz，请注意大小写
```

## xz

基本系统自带 `xz`、`unxz`，同样也不用安装。

### 解压缩 `unxz`

```sh
$ unxz -k test.tar.xz  # 解压并保留原文件，参数 -k 即 keep（保留），下同
$ unxz test.tar.xz     # 解压并删除原文件
```

### 压缩成 `xz`

```sh
$ xz -k test.txt  # 压缩并保留原文件
$ xz test.pdf     # 压缩并删除原文件
```

## 7z

FreeBSD 操作系统下，7z 命令通过下载 `archivers/7-zip` 使用。

### 安装 7-zip

- 使用 pkg：

```
# pkg install 7-zip
```

- 通过 Ports：

```
# cd /usr/ports/archivers/7-zip/
# make install clean
```

### 示例

- 压缩成 7z
  
```sh
$ 7z a test.7z test # 压缩成 7z 文件。-a 就是 add，即把要压缩的文件添加到 test.7z
```

- 解压缩 7z

```
$ 7z x test.7z # 解压 7z 文件
$ 7z x test.7z -o /home/ykla/下载/test # 解压到指定路径。-o 即 Output，指定输出路径
```

## rar

rar 是 Windows 上常见的压缩工具。

### 安装 rar

- 通过 pkg;

```sh
# pkg ins rar unrar
```

- 通过 Ports：

```sh
# cd /usr/ports/archivers/rar/ && make install clean
# cd /usr/ports/archivers/unrar/ && make install clean
```

### 使用 rar

- 压缩成 rar

```
$ rar a archive.rar test # -a 即 add，把文件添加到 archive.rar 的意思
```

- 解压 rar

```sh
$ unrar x archive.rar # 解压到当前路径。参数 -x 即 Extract，解压的意思
$ unrar x archive.rar /home/ykla/桌面/test/ # 解压缩到指定目录
```

## zstd

基本系统内置 zstd，无需安装。参见 [Add support for zstd-compressed user and kernel core dumps.](https://svnweb.freebsd.org/base?view=revision&revision=329240)

### 压缩成 zstd

- 使用 zstd 压缩单个文件

```sh
$ zstd test.pdf
```

- 使用 zstd 压缩文件夹
  
zstd 不支持压缩文件夹（参见 [How can I compress a directory?](https://github.com/facebook/zstd/issues/1526)），故需要先打包成 tar：

>**思考题**
>
>zstd 为什么不支持压缩文件夹？有哪些可能性。

```sh
$ tar -cf test.tar /home/ykla/test/ # 先压缩成 tar。参数 -f 即 file（文件）
```

再把 `test.tar` 压缩成 `test.tar.zst`

```sh
$ zstd -o test.tar.zst test.tar # 参数 -o 代表 file，文件
```

### 解压 zstd

- 解压到当前路径

```sh
$ zstd -d test.tar.zst
```

>**注意**
>
>这样解压出来的是 `test.tar`，还需要再使用 `tar` 解压一遍。

- 解压到指定路径

```sh
$ zstd -d test.tar.zst -o /home/ykla/mytest # 参数 -d 即 decompress（解压缩）
```

>**注意**
>
>这样解压出来的是 `test.tar`，还需要再使用 `tar` 解压一遍。
