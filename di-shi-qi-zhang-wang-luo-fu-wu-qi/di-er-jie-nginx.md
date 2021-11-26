# 第二节 Nginx

## 1.安装 <a href="1-an-zhuang" id="1-an-zhuang"></a>

- ports: `# make -C /usr/ports/www/nginx install`
- pkg: `# pkg install nginx`

### 查找相关的软件包

- ports: `$ ls /usr/ports/www/ | grep nginx`
- pkg: `$ pkg search -o nginx`

## 2.配置 <a href="2-pei-zhi" id="2-pei-zhi"></a>

配置教程可参阅[官方文档](https://nginx.org/en/docs/)与[官方百科](https://wiki.nginx.org/Configuration)。

本文仅简单说明FreeBSD中如何启动Nginx及Nginx的配置文件。

### 2.1 启动 <a href="2.1-qi-dong" id="2.1-qi-dong"></a>

```
# service nginx onestart
```

你可以通过`$ sockstat -4 | grep nginx`检查nginx是否启动并正常运行。

#### 开机自启动

```
# sysrc nginx_enable="yes"
```

此时你应该通过`# service nginx start`启动Nginx而不是`# service nginx onestart`

### 2.2 配置文件

FreeBSD中，Nginx的配置文件位于`/usr/local/etc/nginx/`中，而主要的配置文件则在`/usr/local/etc/nginx/nginx.conf`

默认配置中Nginx的根目录为`/usr/lccal/www/nginx/`，如果需要更改目录位置，请将`/usr/local/etc/nginx/nginx.conf`中的

```
root	/usr/lccal/www/nginx;
```

改成你想要的目录位置，例如`root    /path/to/new/webroot;`