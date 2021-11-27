# 第三节 Gitup 的用法（FreeBSD 13.0及以后）

在 FreeBSD 13.0，FreeBSD 官方将 portsnap 移除了，转而使用 gitup，换用 git 方式获取系统源代码和 ports 打包套件。
```
#pkg install gitup #安装 gitup
#gitup ports #获取 ports
#gitup release #获取 release 版本的源代码
```
## 故障排除：速度太慢

设置 HTTP 代理&#x20;

gitup 的代理不取决于系统代理，而是由其配置文件单独决定。

`# ee /usr/local/etc/gitup.conf`

示例（先删去前边的 # 再改）
```
"proxy_host" : "192.168.27.1",
"proxy_port" : 7890,
```