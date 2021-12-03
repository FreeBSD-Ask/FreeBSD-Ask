# 第八节 Rust/Go 环境的配置

## 安装 Rust 语言

以下安装方式二选一

### FreeBSD 打包

`#pkg install rust`

### Rust 官方打包（不建议）

* 安装：`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
* 升级： `cd ~` `./.cargo/bin/rustup update`
* 删除： `./cargo/bin/rustup self uninstall`


安装成功后，输入 `rustc --version` 或 `cargo --version` 查看软件版本。


## 安装 Go 语言

以下安装方式二选一

### FreeBSD 打包

`#pkg install go`

### Golang 官方打包（不建议）：

* 下载二进制包：
> 去[下载地址](https://golang.google.cn/dl/) 选择 `goXXX.freebsd-amd64.tar.gz` 或 `goXXX.freebsd-386.tar.gz` 。

* 解压二进制包：以 amd64 为例 
>`tar -C /usr/local -xzf https://golang.google.cn/dl/go1.17.4.freebsd-amd64.tar.gz`

* 添加环境变量： 
> 文本模式打开`.profile`， 添加一行 `export PATH=$PATH:/usr/local/go/bin`

安装成功后，输入 `go version` 查看软件版本。
