# 第三节 Nodejs 相关

## 在 FreeBSD 13 上的安装

`nodejs` 依赖 `/lib/libcrypto.so.111` 的某个特定版本，而这意味着如果你需要在 FreeBSD 上使用 NodeJS，你必须留意 FreeBSD 本身的版本，尤其是当你的 pkg 配置使用了 latest 源时。

一般而言，如果想要在 FreeBSD 13.1 上安装 node+yarn，请这么做：

```
# freebsd-update fetch install #必须先更新基本系统
# pkg install yarn             #会自动安装对应版本的 nodejs
```

安装 npm：

```
# pkg install npm
```

>如果你跳过了 FreeBSD 的升级直接安装软件，那么在 FreeBSD 13 上，你将会遇到以下错误：
>
>```
># pkg install yarn
>% node
>ld-elf.so.1: /lib/libcrypto.so.111: version OPENSSL_1_1_1e required by /usr/local/bin/node not found
>```


