# 第二节 Nginx

## 1.安装 <a href="1-an-zhuang" id="1-an-zhuang"></a>

- ports: `# make -C /usr/ports/www/nginx install`
- pkg: `# pkg install nginx`

## 2.配置

```
# sysrc nginx_enable="yes"
# service nginx start
```

此时你可以通过`# sockstat -4 | grep nginx`检查nginx是否启动并正常运行。
