# 第十三节 Wildfly

## 安装

>目前提供  wildfly10、wildfly11、wildfly12、wildfly13、wildfly14、wildfly15、wildfly16、wildfly17、wildfly18、wildfly24、wildfly25、wildfly26 等多个版本。

在此以 wildfly26 为例：

```
# pkg install wildfly26
```

## 配置


在 `/etc/hosts` 增加以下代码，其中 `server02` 为本机 `hostname`（主机名，安装时设置的）。

```
127.0.0.1               server02
```

还需要一些其他设置：

```
# sysrc wildfly26_enable="yes"
# sysrc wildfly26_args="-Djboss.bind.address=0.0.0.0 -Djboss.bind.address.management=0.0.0.0"
# sysrc wildfly26_log_stdout="/dev/null"
# sysrc wildfly26_log_stderr="/dev/null"
```

然后启动服务：

```
# service wildfly26 start
```

打开 `http://127.0.0.1:8080` 即可检验服务状态。


>**可选**
>
>还可以用 `/usr/local/wildfly26/bin/add-user.sh ` 生成管理员账户，


# 故障排除

如果服务无法正常启动，可以通过 `/usr/local/wildfly26/standalone/log/server.log` 查看错误日志。

