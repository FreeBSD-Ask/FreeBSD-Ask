# 第 5.9 节 压缩与解压

## zip

安装 zip 压缩文件 `# pkg install zip`，基本系统自带 `unzip`。

```shell-session
# zip test.zip test # 打包 zip 格式文件

# unzip test.zip # 释放 zip 格式文件
```

## tar/xz

```shell-session
# tar -cvf test.tar test # 打包 tar 格式文件

# tar -xvf test.tar # 释放 tar 格式文件

# tar -zcvf test.tar.gz test # 打包 gzip 格式文件

# tar -zxvf test.tar.gz # 释放 gzip 格式文件

# tar -jcvf test.tar.bz2 test # 打包 bzip2 格式文件

# tar -jxvf test.tar.bz2 # 释放 bzip2 格式文件

# tar -Jcvf test.tar.xz test # 打包 xz 格式文件

# tar -Jxvf test.tar.xz # 释放 xz 格式文件

# xz -z -k test.tar # 打包 xz 格式文件，如不加 -k 参数，命令执行完原文件将被删除

# xz -d -k test.tar.xz # 释放 xz 格式文件，如不加 -k 参数，命令执行完 xz 文件将被删除
```

## 7z/7za

FreeBSD 操作系统下，7z 和 7za 命令均通过`# pkg install -y 7-zip`获取，别安装成了 `p7zip`。

示例如下：

```shell-session
# 7z a test.7z test # 7z 打包文件
# 7z x test.7z # 7z 释放文件
# 7za a test.7z test # 7za 打包文件
# 7za x test.7z # 7za 释放文件
```
