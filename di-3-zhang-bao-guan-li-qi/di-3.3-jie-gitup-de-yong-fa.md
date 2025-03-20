# 第 3.3 节 gitup 的用法

>**技巧**
>
>FreeBSD 14.0 已经删除了 portsnap，转而使用 git，如本文所述可以使用 gitup 替代之。

`gitup`，即更新 git 的意思。

## 安装 gitup

使用 pkg

```sh
# pkg install gitup 
```

或者

```sh
# cd /usr/ports/net/gitup/
# make install clean
```

## 使用 gitup

```sh
# gitup ports # 获取 latest 的 ports
# gitup release # 获取 release 版本的源代码
```

## 境内 Git 镜像站

```sh
# cp /usr/local/etc/gitup.conf.sample /usr/local/etc/gitup.conf
```

```sh
# ee /usr/local/etc/gitup.conf
```

内容如下（有 ①②③ 共计三个需要修改的地方）：

```sh
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

## 故障排除：

- 速度太慢（若不使用镜像站）：设置 HTTP 代理

`gitup` 的代理不取决于系统代理，而是由其配置文件 `/usr/local/etc/gitup.conf` 单独决定。

示例（先删去前边的 `#` 再改）：

```sh
"proxy_host" : "192.168.27.1",
"proxy_port" : 7890,
```

- 详细调试输出：

```sh
# gitup -v2 ports
```

- gitup: `build_repair_command: There are too many files to repair -- please re-clone the repository: Argument list too long`
  
```sh
# rm -rf /usr/ports
# gitup ports
```

清空目录重新拉取即可，可以无视 `rm: /usr/ports/: Device busy` 这个提示。

## 参考链接

- [gitup --A minimalist, dependency-free program to clone/pull Git repos-itories.](https://www.freebsd.org/cgi/man.cgi?query=gitup&sektion=1&manpath=freebsd-release-ports)，man 手册
- [net/gitup](https://www.freshports.org/net/gitup)
- [johnmehr/gitup](https://github.com/johnmehr/gitup)，开发者官网
