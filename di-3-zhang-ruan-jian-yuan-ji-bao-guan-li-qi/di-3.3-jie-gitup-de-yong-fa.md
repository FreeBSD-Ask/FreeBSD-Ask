# 第3.3节 gitup 的用法

> 在 FreeBSD 13.0，FreeBSD 官方准备将 `portsnap` 移除（但 13.1 仍可使用），转而使用 `gitup`，换用 git 方式获取系统源代码和 ports 打包套件。但是目前尚不清楚这一替代是否会生效。

```
# pkg install gitup #安装 gitup
# gitup ports #获取 ports
# gitup release #获取 release 版本的源代码
```

## 境内 Git 镜像站

<https://git.freebsd.cn>

## 故障排除：速度太慢

设置 HTTP 代理

`gitup` 的代理不取决于系统代理，而是由其配置文件单独决定。

`# ee /usr/local/etc/gitup.conf`

示例（先删去前边的 # 再改）

```
"proxy_host" : "192.168.27.1",
"proxy_port" : 7890,
```

参考链接：

[https://www.freebsd.org/cgi/man.cgi?query=gitup\&sektion=1\&manpath=freebsd-release-ports](https://www.freebsd.org/cgi/man.cgi?query=gitup\&sektion=1\&manpath=freebsd-release-ports)

[https://www.freshports.org/net/gitup](https://www.freshports.org/net/gitup)

[https://github.com/johnmehr/gitup](https://github.com/johnmehr/gitup)
