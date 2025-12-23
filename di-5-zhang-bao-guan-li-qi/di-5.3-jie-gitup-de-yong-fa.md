# 5.3 Gitup 的用法

>**技巧**
>
>FreeBSD 14.0 已经删除了 portsnap，转而使用 Git，如本文所述可以使用 gitup 替代 portsnap。

`gitup` 是用于更新 Git 仓库的工具。

## 安装 gitup

- 使用 pkg 安装：

```sh
# pkg install gitup 
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/net/gitup/
# make install clean
```

## 使用 gitup

```sh
# gitup ports 	# 获取 latest 分支的 Ports
# gitup release # 获取 release 版本的源代码
```

## 境内 Git 镜像站

```sh
# cp /usr/local/etc/gitup.conf.sample /usr/local/etc/gitup.conf
```

编辑 `/usr/local/etc/gitup.conf`，修改内容如下（有 ①②③ 共计三处需要修改）：

```ini
# $FreeBSD$
#
# Default configuration options for gitup.conf.
{
	"defaults" : {
		"host"           : "mirrors.ustc.edu.cn",  #①改动成这样
		"port"           : 443,
#		"proxy_host"     : "",
#		"proxy_port"     : 0,
#		"proxy_username" : "",
#		"proxy_password" : "",
#		"source_address" : "",
		"low_memory"     : false,
		"display_depth"  : 0,
		"verbosity"      : 1,
		"work_directory" : "/var/db/gitup",
	},

	"ports" : {
		"repository_path"  : "/freebsd-ports/ports.git",  #②改动成这样
		"branch"           : "main",
		"target_directory" : "/usr/ports",
		"ignores"          : [],
	},

	"quarterly" : {
		"repository_path"  : "/freebsd-ports/ports.git",  #③改动成这样
		"branch"           : "quarterly",
		"target_directory" : "/usr/ports",
		"ignores"          : [],
	},

	"release" : {
		"repository_path"  : "/src.git",
		"branch"           : "releng/13.2",
		"target_directory" : "/usr/src",
		"ignores"          : [
			"sys/[^\/]+/conf",
		],
	},

	"stable" : {
		"repository_path"  : "/src.git",
		"branch"           : "stable/13",
		"target_directory" : "/usr/src",
		"ignores"          : [
			"sys/[^\/]+/conf",
		],
	},

	"current" : {
		"repository_path"  : "/src.git",
		"branch"           : "main",
		"target_directory" : "/usr/src",
		"ignores"          : [
			"sys/[^\/]+/conf",
		],
	}
}
```

拉取 ports：

```sh
# gitup ports
```

## 故障排除与未竟事宜

### 速度太慢（若不使用镜像站）

需要设置 HTTP 代理：`gitup` 不使用系统代理，而是由其配置文件 `/usr/local/etc/gitup.conf` 单独决定代理设置。


示例（先删去前面的 `#` 再修改）：

```sh
"proxy_host": "192.168.27.1",  # 设置代理服务器地址
"proxy_port": 7890              # 设置代理服务器端口
```

### 详细调试输出

以详细模式更新 ports 树到最新版本：

```sh
# gitup -v2 ports
```

### 报错 `build_repair_command: There are too many files to repair -- please re-clone the repository: Argument list too long`
  
```sh
# rm -rf /usr/ports/*
# gitup ports
```

清空目录后重新拉取即可，可以忽略 `rm: /usr/ports/: Device busy` 提示。

## 参考链接

- [gitup --A minimalist, dependency-free program to clone/pull Git repos-itories.](https://www.freebsd.org/cgi/man.cgi?query=gitup&sektion=1&manpath=freebsd-release-ports)，man 手册
- [net/gitup](https://www.freshports.org/net/gitup)
- [johnmehr/gitup](https://github.com/johnmehr/gitup)，开发者官网
