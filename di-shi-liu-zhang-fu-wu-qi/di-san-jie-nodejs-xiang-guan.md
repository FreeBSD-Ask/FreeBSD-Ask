# 第三节 Nodejs 相关

## 在 FreeBSD 13 上的安装

`node` 依赖 `/lib/libcrypto.so.111` 的某个特定版本，而这意味着如果你需要在 FreeBSD 上使用 NodeJS，你必须留意 FreeBSD 本身的版本，尤其是当你的 pkg 配置使用了 latest 源时。

一般而言，如果想要在 FreeBSD 13上 安装 node /w yarn，请这么做：

```
# freebsd-update fetch install
# pkg install yarn
```

如果你跳过了 FreeBSD 的升级而直接做第二步，在 FreeBSD 13 上，你可能会碰到这样子错误：

```
# pkg install yarn
% node
ld-elf.so.1: /lib/libcrypto.so.111: version OPENSSL_1_1_1e required by /usr/local/bin/node not found
```

所以还是老老实实地照着教程走吧。。
