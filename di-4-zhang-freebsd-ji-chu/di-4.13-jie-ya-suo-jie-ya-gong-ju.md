# 4.13 压缩解压工具

压缩和解压工具是计算机文件管理中的基础工具。数据压缩利用信息的统计冗余性，通过编码算法减少数据表示所需的存储空间。根据是否允许信息丢失，压缩算法可分为无损压缩（lossless compression）和有损压缩（lossy compression）两大类。本节所涉及的工具均采用无损压缩算法，即解压后的数据与原始数据完全一致。

常见的无损压缩算法包括：DEFLATE（结合 LZ77 与 Huffman 编码，用于 zip/gzip）、LZMA/LZMA2（用于 xz）、LZ4（高速压缩）、Zstandard（兼顾速度与压缩率，用于 zstd）以及 bzip2（基于 Burrows-Wheeler 变换）。这些算法在压缩率与压缩/解压速度之间存在不同的权衡点，用户可根据实际场景选择。

本节将介绍 FreeBSD 系统上常用的压缩解压工具的安装和使用方法。

## zip

zip 格式是 PKZIP 归档格式的实现，由 Info-ZIP 项目维护。zip 是一种压缩和文件打包工具，兼容 PKZIP（Phil Katz 的 ZIP for MSDOS 系统），zip 3.0 版本兼容 PKZIP 2.04 并支持 Zip64 扩展（允许归档和文件超过 2 GB 限制）。zip 使用 deflation 作为默认压缩方法，也可存储不压缩的文件，并自动为每个文件选择更优的方式。

zip 格式是 Windows 上最常用的格式，但对 Unicode 文件名支持有限（取决于 zip 工具版本和压缩设置）。在跨平台交换文件时建议使用 tar.xz 或 tar.zst 格式。

> **技巧**
>
>在使用 zip 压缩中文或非英文字符时出现乱码是正常现象，因为编码方式不同。zip 3.0 在支持 Unicode 的平台上编译时，会额外存储路径的 UTF-8 翻译，以改善跨平台文件名兼容性。一般国产操作系统（如 UOS、Ubuntu Kylin）通过打补丁解决了此问题。关于该补丁未提交到上游的原因，如有了解者可提交 PR。

### 安装 zip

- 使用 pkg

```sh
# pkg install zip
```

- 使用 Ports

```sh
# cd /usr/ports/archivers/zip/
# make install clean
```

### zip 压缩

```sh
$ zip test.zip test # 压缩成 zip 文件
```

### zip 解压

zip 文件解压时，需要安装 `unzip` 工具（FreeBSD 基本系统自带的 `unzip` 基于 libarchive，功能有限；如需完整功能，可通过 `pkg install unzip` 安装 Info-ZIP 版本）。

```sh
$ unzip test.zip # 解压 zip 文件到当前路径
$ unzip test.zip -d /home/ykla/test # 解压到指定路径，-d 即 directory（目录）
```

unzip 的 `-d` 选项后面跟目录名，可以有空格（如 `-d /path`），也可以紧贴（如 `-d/path`）。

## tar

基本系统自带 `tar`，无需安装。

tar 是“tape archive”（磁带归档）的缩写，最初用于在磁带上进行文件存储。FreeBSD 的 tar 实现基于 libarchive 库（即 bsdtar），首次随 FreeBSD 5.4 发布（2005 年 5 月），替代了早期版本中使用的 GNU tar。该实现可从 tar、pax、cpio、zip、jar、ar、xar、rar、rpm、7-zip 及 ISO 9660 光盘镜像中提取文件，并可创建 tar、pax、cpio、ar、zip、7-zip 和 shar 格式的归档。

bsdtar 的 `-l` 选项遵循 ISO/IEC 9945-1:1996（“POSIX.1”）的定义（检查链接）。

GNU tar 支持自动识别多种压缩格式；bsdtar 支持 tar、pax、cpio、zip 等多种格式，GNU tar 仅支持 tar 相关格式。

> **思考题**
>
>> 归档文件包是指压缩率为 `0` 的文件集合，即将多个文件或目录打包成单一文件以便存储。单纯使用 `tar` 只进行打包而不压缩。压缩的本质是通过算法减小文件占用的存储空间，而不是针对目录本身。因此，常见压缩软件通常先将目录归档为文件，然后再进行压缩。
>
> 如何理解归档与压缩的关系？

### tar 压缩

```sh
$ tar -cvf test.tar test # 打包成 tar 格式文件。-c 即 Create，创建
$ tar -zcvf test.tar.gz test # 压缩成 gzip 格式文件。-z 即 gzip
$ tar -jcvf test.tar.bz2 test # 压缩成 bzip2 格式文件。参数 -j 即 bzip2，请注意大小写
$ tar -Jcvf test.tar.xz test # 压缩成 xz 格式文件。参数 -J 即 xz，请注意大小写
$ tar --zstd -cvf test.tar.zst test # 压缩成 zstd 格式文件
```

### tar 解压

```sh
$ tar -xvf test.tar.其他压缩格式 # 解压 tar 格式文件，可支持如 test.tar.bz2、test.tar.gz、test.tar.xz、test.tar.zst 等格式
$ tar -xvf test.tar -C /home/ykla/mytest # 解压 test.tar 到指定路径
```

选项说明：

- `x`：Extract，解压
- `v`：verbose，输出详细信息模式
- `f`：file，指定文件
- `C`：即 cd，指定路径

## xz

基本系统自带 `xz`、`unxz`，同样无需安装。xz 格式是当前压缩率最高的格式之一，特别适合大文件归档。

### `xz` 压缩

默认压缩后会删除原文件，建议加 `-k` 选项保留原文件。

```sh
$ xz -k test.txt
```

压缩并删除原文件：

```sh
$ xz test.pdf
```

### `unxz` 解压

unxz 实际上是 xz 的符号链接，使用 `xz -d` 或直接 `unxz` 效果相同。

```sh
$ unxz -k test.tar.xz  # 解压并保留原文件，参数 -k 即 keep（保留），下同
$ unxz test.tar.xz     # 解压并删除原文件
```

## 7z

7z 格式具有极高的压缩率，特别适合大文件归档。

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

`a` 表示 add，将要压缩的文件添加到 test.7z。

### 7z 解压

```sh
$ 7z x test.7z # 解压 7z 文件
$ 7z x test.7z -o/home/ykla/下载/test # 将 test.7z 解压到指定路径
```

`-o` 即 Output，指定输出路径。

> **警告**
>
>`-o/home/ykla/下载/test` 中 `-o` 与路径之间 **不能有空格**，这并非拼写错误，而是 7z 命令的设计方式。欢迎提交 PR 改进。

## rar

rar 是 Windows 上最流行的格式之一，但在 Unix 世界使用率较低；rar 有较好的恢复记录和分卷功能，适合大文件传输。

rar 格式是专有格式，未在基本系统内置。

### 安装 rar

- 通过 pkg 安装：

```sh
# pkg install rar unrar
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

`a` 表示 add（添加），将文件添加到 `archive.rar`。

### rar 解压

```sh
$ unrar x archive.rar # 解压到当前路径。命令 `x` 即 Extract，解压
$ unrar x archive.rar /home/ykla/桌面/test/ # 解压到指定目录
```

## zstd

zstd 是 Facebook 开发的快速压缩算法，兼顾压缩速度和压缩率，是现代系统首选的压缩格式。

zstd 是 FreeBSD 12+ 基本系统内置的压缩工具，Linux 发行版通常也预装 zstd；zstd 支持多种预设级别，从最快（`-1`）到极限压缩（`--ultra -22`）。参见：FreeBSD Project. Add support for zstd-compressed user and kernel core dumps.[EB/OL]. [2026-03-26]. <https://svnweb.freebsd.org/base?view=revision&revision=329240>. 该修订记录了 zstd 压缩转储支持的实现细节。

### zstd 压缩

- 使用 zstd 压缩单个文件

```sh
$ zstd test.pdf
```

zstd 不直接支持压缩目录，需要先将目录打包成 tar 文件再压缩。

- 使用 zstd 压缩文件夹。

zstd 不直接支持压缩文件夹（参见：GitHub. How can I compress a directory?[EB/OL]. [2026-03-26]. <https://github.com/facebook/zstd/issues/1526>.）。该 Issue 讨论了 zstd 不支持直接压缩目录的技术原因与替代方案，因此需要先将文件夹打包为 tar 文件。

> **思考题**
>
> zstd 为什么不支持压缩文件夹？有哪些可能性？

```sh
$ tar -cf test.tar /home/ykla/test/ # 先打包成 tar。参数 -f 即 file（文件）
```

将 `test.tar` 压缩成 `test.tar.zst`

```sh
$ zstd -o test.tar.zst test.tar # 参数 -o 代表 file，用于指定输出文件
```

此外，也可直接使用 tar 的 `--zstd` 选项一步完成打包与压缩：

```sh
$ tar --zstd -cvf 输出文件 -C 起点目录 相对路径
```

示例：

```sh
$ tar --zstd -cvf test.tar.zst -C /home/ykla/ test # 打包并压缩成 zstd 格式
a test
```

查看结果：

```sh
$ ykla@ykla:~ $ ls -al
drwxr-xr-x  2 ykla ykla     2 Apr 16 11:53 test
-rw-r--r--  1 ykla ykla    98 Apr 16 11:58 test.tar.zst
```

文件结构图：

```sh
当前工作目录（命令执行所在位置，如 ~）
│
├── test.tar.zst   ← 输出文件（始终在“当前目录”生成）
│
└── （选项 -C 将在添加后续文件之前切换目录）
     ↓
     切换到：/home/ykla/
                │
                └── test   ← 被打包的对象
```

### zstd 解压

#### 解压到当前路径

```sh
$ zstd -d test.tar.zst
```

> **注意**
>
> 这样解压出来的是 `test.tar`，还需要再用 `tar` 解压一次。

#### 解压到指定路径

```sh
$ zstd -d test.tar.zst -o /home/ykla/mytest # 参数 -d 表示 decompress（解压缩）
```

> **注意**
>
> 同上，解压出来的是 `test.tar`，还需要再用 `tar` 解压一次。

## 课后习题

1. 使用 zip、tar、xz、7z、rar、zstd 等工具分别压缩和解压包含中文文件名的文件，对比各工具对 UTF-8 编码的处理方式，分析不同压缩格式在国际化支持上的设计差异。
2. 使用不同压缩算法（gzip、bzip2、xz、zstd）压缩同一组文件，对比压缩率、压缩时间和解压时间，分析各算法在压缩效率与计算性能之间的权衡策略。
3. 查阅 zip 格式规范中关于文件名编码的条款，分析中文文件名乱码问题的根源，评估现有补丁方案的适用范围。
