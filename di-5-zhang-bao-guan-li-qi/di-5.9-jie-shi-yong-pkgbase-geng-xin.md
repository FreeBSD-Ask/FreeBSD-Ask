# 5.9 使用 pkgbase 更新 FreeBSD


## （可选）配置软件源

FreeBSD 官方源的 pkgbase 信息如下：

| **分支** | **更新频率** | **URL 地址** |
| :---: | :---: | :--- |
| main（16.0-CURRENT） | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_latest> |
| main（16.0-CURRENT） | 每周一次：星期日 20:00 | <https://pkg.freebsd.org/${ABI}/base_weekly> |
| stable/14 | 每天两次：08:00、20:00  | <https://pkg.freebsd.org/${ABI}/base_latest> |
| stable/14 | 每周一次：星期日 20:00 | <https://pkg.freebsd.org/${ABI}/base_weekly> |
| releng/14.0（RELEASE） | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_release_0> |
| releng/14.1（RELEASE） | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_release_1> |
| releng/14.2（RELEASE） | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_release_2> |
| releng/14.3（RELEASE） | 每天两次：08:00、20:00 | <https://pkg.freebsd.org/${ABI}/base_release_3> |

**以上表格的时间已转换为北京时间，即东八区时间，均为 FreeBSD 官方镜像站的时间。**

若官方源下载速度慢，可以考虑换成国内镜像。

找到 Lua 脚本中的 `create_base_repo_conf` 函数：

```lua
local function base_repo_url()
	local major, minor, branch = freebsd_version()
	if math.tointeger(major) < 14 then
		fatal("Unsupported FreeBSD version: " .. raw)
	end
	if branch == "RELEASE" or branch:match("^BETA") or branch:match("^RC") then
		return "pkg+https://pkg.FreeBSD.org/${ABI}/base_release_" .. minor
	elseif branch == "CURRENT" or
		branch == "STABLE" or
		branch == "PRERELEASE" or
		branch:match("^ALPHA")
	then
		return "pkg+https://pkg.FreeBSD.org/${ABI}/base_latest"
	else
		fatal("Unsupported FreeBSD version: " .. raw)
	end
end
```

将这部分函数中修改如下，其中 `url` 指定了镜像站：

```lua
local function base_repo_url()
	local major, minor, branch = freebsd_version()
	if math.tointeger(major) < 14 then
		fatal("Unsupported FreeBSD version: " .. raw)
	end
	if branch == "RELEASE" or branch:match("^BETA") or branch:match("^RC") then
		return "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_release_" .. minor
	elseif branch == "CURRENT" or
		branch == "STABLE" or
		branch == "PRERELEASE" or
		branch:match("^ALPHA")
	then
		return "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_latest"
	else
		fatal("Unsupported FreeBSD version: " .. raw)
	end
end
```


再找到下面的函数 `create_base_repo_conf`

```lua
local function create_base_repo_conf(path)
	assert(os.execute("mkdir -p " .. path:match(".*/")))
	local f <close> = assert(io.open(path, "w"))
	if math.tointeger(freebsd_version()) >= 15 then
		assert(f:write(string.format([[
%s: {
  enabled: yes
}
]], options.repo_name)))
	else
		assert(f:write(string.format([[
%s: {
  url: "%s",
  mirror_type: "srv",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
]], options.repo_name, base_repo_url())))
	end
end
```

修改如下（删除了 srv 相关数行）：

```lua
local function create_base_repo_conf(path)
	assert(os.execute("mkdir -p " .. path:match(".*/")))
	local f <close> = assert(io.open(path, "w"))
	if math.tointeger(freebsd_version()) >= 15 then
		assert(f:write(string.format([[
%s: {
  enabled: yes
}
]], options.repo_name)))
	else
		assert(f:write(string.format([[
%s: {
  url: "%s",
  enabled: yes
}
]], options.repo_name, base_repo_url())))
	end
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

