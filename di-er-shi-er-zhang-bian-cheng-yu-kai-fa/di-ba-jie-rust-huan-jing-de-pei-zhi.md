# 第八节 Rust 环境的配置

## 安装

以下安装方式二选其一

### FreeBSD 打包

`#pkg install rust`

### Rust 官方打包

- 安装：`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`

- 升级： `cd ~` `./.cargo/bin/rustup update`

- 删除： `./cargo/bin/rustup self uninstall` 


安装成功后，输入 `rustc --version` 或 `cargo --version` 查看软件版本
