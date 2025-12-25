# 8.9 压缩和解压

## zip

在使用 zip 压缩中文或非英文字符时出现乱码是正常现象，因为编码方式不同。一般国产操作系统（如 UOS、Ubuntu Kylin）通过打补丁解决了此问题。关于该补丁未提交到上游的原因，如有了解者可提交 PR。

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

### zip 压缩

```sh
$ zip test.zip test # 压缩成 zip 文件
```


### zip 解压

zip 文件解压时，系统通常自带 `unzip` 工具，无需额外安装。

```sh
$ unzip test.zip # 解压 zip 文件到当前路径
$ unzip test.zip -d /home/ykla/test # 解压到指定路径，-d 即 directory，目录的意思
```

## tar

基本系统自带 `tar`，不用安装。

tar 是“tape archive”（磁带归档）的缩写，最初用于在磁带上进行文件存储。

>**思考题**
>
>>归档文件包是指压缩率为 `0` 的文件集合，即将多个文件或目录打包成单一文件以便存储。单纯使用 `tar` 只进行打包而不压缩。压缩的本质是通过算法减小文件占用的存储空间，而不是针对目录本身。因此，常见压缩软件通常先将目录归档为文件，然后再进行压缩。
>
>如何理解归档与压缩的关系？

### tar 压缩
  
```sh
$ tar -cvf test.tar test # 压缩成 tar 格式文件。-c 即 Create，创建
$ tar -zcvf test.tar.gz test # 压缩成 gzip 格式文件。-z 即 gzip
$ tar -jcvf test.tar.bz2 test # 压缩成 bzip2 格式文件。参数 -j 即 bzip2，请注意大小写
$ tar -Jcvf test.tar.xz test # 压缩成 xz 格式文件。参数 -J 即 xz，请注意大小写
```

### tar 解压

```sh
$ tar -xvf test.tar.其他压缩格式 # 解压 tar 格式文件，可支持如 test.tar.bz2、test.tar.gz、test.tar.xz 等格式
$ tar -xvf test.tar -C /home/ykla/mytest # 解压 test.tar 到指定路径
```

选项说明：

- `x`：Extract 解压的意思
- `v`：verbose 输出详细信息模式
- `f`：file 指定文件
- `C`：`cd` 的意思，即指定路径

## xz

基本系统自带 `xz`、`unxz`，同样也不用安装。

### `xz` 压缩

```sh
$ xz -k test.txt  # 压缩并保留原文件
$ xz test.pdf     # 压缩并删除原文件
```

### `unxz` 解压

```sh
$ unxz -k test.tar.xz  # 解压并保留原文件，参数 -k 即 keep（保留），下同
$ unxz test.tar.xz     # 解压并删除原文件
```

## 7z

在 FreeBSD 操作系统中，7z 命令可通过安装 `archivers/7-zip` 包使用。

### 安装 7-zip

- 使用 pkg：

```sh
# pkg install 7-zip
```

- 通过 Ports：

```sh
# cd /usr/ports/archivers/7-zip/
# make install clean
```

### 7z 压缩
  
```sh
$ 7z a test.7z test # 将 test 文件压缩成 7z 文件。
```

`-a` 表示 add，将要压缩的文件添加到 test.7z。

### 7z 解压

```
$ 7z x test.7z # 解压 7z 文件
$ 7z x test.7z -o/home/ykla/下载/test # 将 test.7z 解压到指定路径
```

`-o` 即 Output，指定输出路径。

>**警告**
>
>`-o/home/ykla/下载/test` 中 `-o` 与路径之间没有空格，这并非拼写错误，而是 7z 命令的设计方式。如有意者可提交 PR 改进。


## rar

rar 是 Windows 上常见的压缩工具。

### 安装 rar

- 通过 pkg 安装：

```sh
# pkg ins rar unrar
```

- 通过 Ports：

```sh
# cd /usr/ports/archivers/rar/ && make install clean
# cd /usr/ports/archivers/unrar/ && make install clean
```


### rar 压缩

```sh
$ rar a archive.rar test
```

`-a` 表示 add（添加），将文件添加到 `archive.rar`。

### rar 解压

```sh
$ unrar x archive.rar # 解压到当前路径。参数 -x 即 Extract，解压的意思
$ unrar x archive.rar /home/ykla/桌面/test/ # 解压缩到指定目录
```

## zstd

基本系统内置 zstd，无需安装。参见 [Add support for zstd-compressed user and kernel core dumps.](https://svnweb.freebsd.org/base?view=revision&revision=329240)

### zstd 压缩

- 使用 zstd 压缩单个文件

```sh
$ zstd test.pdf
```

- 使用 zstd 压缩文件夹
  
zstd 不直接支持压缩文件夹（参见 [How can I compress a directory?](https://github.com/facebook/zstd/issues/1526)），因此需要先将文件夹打包为 tar 文件。

>**思考题**
>
>zstd 为什么不支持压缩文件夹？有哪些可能性。

```sh
$ tar -cf test.tar /home/ykla/test/ # 先压缩成 tar。参数 -f 即 file（文件）
```

再将 `test.tar` 压缩成 `test.tar.zst`

```sh
$ zstd -o test.tar.zst test.tar # 参数 -o 代表 file，用于指定输出文件
```

### zstd 解压

#### 解压到当前路径

```sh
$ zstd -d test.tar.zst
```

>**注意**
>
>这样解压出来的是 `test.tar`，还需要再使用 `tar` 解压一遍。

#### 解压到指定路径

```sh
$ zstd -d test.tar.zst -o /home/ykla/mytest # 参数 -d 表示 decompress（解压缩）
```

>**注意**
>
>这样解压出来的是 `test.tar`，还需要再使用 `tar` 解压一遍。
