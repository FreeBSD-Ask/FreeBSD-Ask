# 4.9 使用 pkgbase 更新 FreeBSD

现在 FreeBSD 的系统更新是与第三方软件更新的分离的（现在使用 `freebsd-update`），pkgbase 是目的就是将其合并起来统一使用 `pkg` 命令进行管理（学习 Linux？）。因为现在只有一级架构的 RELEASE 才有 `freebsd-update` 可用。pkgbase 早在 2016 年就有了，原计划在 FreeBSD 14 就进入系统替代 `freebsd-update`，但是现在推迟到了 15。另外个人感觉 `freebsd-update` 体验非常差，非常慢（网络无关）。

**pkgbase 的设计初衷是为了让 stable、current 和 release（BETA、RC 等）都能使用一种二进制工具进行更新。当下，stable、current 只能通过完全编译源代码的方式来更新。**

>**警告**
>
>**存在风险，可能会丢失所有数据！建议在操作之前做好备份。**

## 下载 `pkgbasify` 脚本

在 [Github 仓库](https://github.com/FreeBSDFoundation/pkgbasify)下载 `pkgbasify.lua` 脚本文件：

```sh
$ fetch https://github.com/FreeBSDFoundation/pkgbasify/raw/refs/heads/main/pkgbasify.lua
```

## （可选）配置软件源

FreeBSD 官方源的 pkgbase 信息如下：

| **分支** | **更新频率** | **URL 地址** |
| :---: | :---: | :--- |
| main（15.0-CURRENT） | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_latest> |
| main（15.0-CURRENT） | 每周一次：星期日 20:00 | <https://pkg.freebsd.org/${ABI}/base_weekly> |
| stable/14 | 每天两次：08:00、20:00  | <https://pkg.freebsd.org/${ABI}/base_latest> |
| stable/14 | 每周一次：星期日 20:00 | <https://pkg.freebsd.org/${ABI}/base_weekly> |
| releng/14.0（RELEASE） | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_release_0> |
| releng/14.1（RELEASE） | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_release_1> |
| releng/14.2（RELEASE） | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_release_2> |

**以上表格的时间已转换为北京时间，即东八区时间。为 FreeBSD 官方镜像站时间。**

若官方源下载速度慢，可以考虑换成国内镜像。

修改 Lua 脚本中的 `create_base_repo_conf` 函数：

```lua
function create_base_repo_conf(path)
	assert(os.execute("mkdir -p " .. path:match(".*/")))
	local f <close> = assert(io.open(path, "w"))
	assert(f:write(string.format([[
FreeBSD-base: {
  url: "%s",
  mirror_type: "srv",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
]], base_repo_url())))
end
```

将软件源信息替换为下列镜像站中的任何一个，例如：

```lua
function create_base_repo_conf(path)
	assert(os.execute("mkdir -p " .. path:match(".*/")))
	local f <close> = assert(io.open(path, "w"))
	assert(f:write([[
FreeBSD-base: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_latest",
  enabled: yes
}
]]))
end
```


### 南京大学开源镜像站 NJU

```sh
FreeBSD-base: {
  url: "https://mirrors.nju.edu.cn/freebsd-pkg/${ABI}/base_latest",
  enabled: yes
}
```

### 中国科学技术大学开源镜像站 USTC

```sh
FreeBSD-base: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_latest",
  enabled: yes
}
```

### 网易开源镜像站 163

```sh
FreeBSD-base: {
  url: "https://mirrors.163.com/freebsd-pkg/${ABI}/base_latest",
  enabled: yes
}
```

## 运行 `pkgbasify.lua`

```sh
# chmod +x pkgbasify.lua
# ./pkgbasify.lua
```

>**注意**
>
>我测试的是纯净系统，没有任何多余配置及第三方程序（除了 pkg），仅开了 SSH 服务。


>**警告**
>
>**存在风险，可能会丢失所有数据！**

## 参考文献

- [wiki/PkgBase](https://wiki.freebsd.org/PkgBase)

