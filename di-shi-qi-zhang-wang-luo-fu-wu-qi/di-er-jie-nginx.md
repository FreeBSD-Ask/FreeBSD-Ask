# 第二节 Nginx

## 1.安装 <a href="#1-an-zhuang" id="1-an-zhuang"></a>

* ports: `# make -C /usr/ports/www/nginx install`
* pkg: `# pkg install nginx`

### 查找相关的软件包

* ports: `$ ls /usr/ports/www/ | grep nginx`
* pkg: `$ pkg search -o nginx`

## 2.配置 <a href="#2-pei-zhi" id="2-pei-zhi"></a>

配置教程可参阅[官方文档](https://nginx.org/en/docs/)与[官方百科](https://wiki.nginx.org/Configuration)。

本文仅简单说明FreeBSD中如何启动Nginx及Nginx的配置文件。

### 2.1 启动 <a href="#2.1-qi-dong" id="2.1-qi-dong"></a>

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

改成你想要的目录位置，例如`root /path/to/new/webroot;`

## 3.示例文件（Nginx +  Typecho 伪静态 + SSL）

```
#user  nobody;
worker_processes  1;

# This default error log path is compiled-in to make sure configuration parsing
# errors are logged somewhere, especially during unattended boot when stderr
# isn't normally logged anywhere. This path will be touched on every nginx
# start regardless of error log location configured here. See
# https://trac.nginx.org/nginx/ticket/147 for more info. 
#
#error_log  /var/log/nginx/error.log;
#

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    server {
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   /usr/local/www/nginx;
            index  index.html index.htm index.php;
if (-f $request_filename/index.html){
rewrite (.*) $1/index.html break;
}
if (-f $request_filename/index.php){
rewrite (.*) $1/index.php;
}
if (!-f $request_filename){
rewrite (.*) /index.php;}       
 }

 
location ~ .*\.php(\/.*)*$ {
            root           /usr/local/www/nginx;
            fastcgi_pass   127.0.0.1:9000;
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME $request_filename;
            include        fastcgi_params;
        }





  #location ~ .*\.php(\/.*)*$ {
   #         include fastcgi_params;
    #        fastcgi_pass  127.0.0.1:9000;
     #   }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /usr/local/www/nginx-dist;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        location ~ .*\.php(\/.*)*$ {
            root           /usr/local/www/nginx;
            fastcgi_pass   127.0.0.1:9000;
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME $request_filename;
            include        fastcgi_params;
        }

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    server {
       listen       443;
       server_name  localhost;

        ssl_certificate      /usr/local/etc/nginx/fbxs.crt;
      ssl_certificate_key   /usr/local/etc/nginx/fbxs.key;

      ssl on;
        ssl_certificate fbxs.crt;
        ssl_certificate_key fbxs.key;
        ssl_session_timeout 5m;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2; #按照这个协议配置
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;#按照这个套件配置
        ssl_prefer_server_ciphers on;
location ~ .*\.php(\/.*)*$ {
            root           /usr/local/www/nginx-dist;
            fastcgi_pass   127.0.0.1:9000;
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME $request_filename;
            include        fastcgi_params;
        }
        location / {
            root   /usr/local/www/nginx-dist;
            index  index.php;    
 }
      }

}
```
