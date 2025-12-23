# 5.9 使用 ZFS 启动环境更新 FreeBSD 并实现多版本共存


## 创建启动环境 15.0-RELEASE

- 使用工具 bectl 创建启动环境 `15.0-RELEASE`：

```sh
# bectl create 15.0-RELEASE
```

>**注意**
>
>我们只是将其命名为 15.0，实际上系统仍然是 14.3-RELEASE。

- 使用 bectl 检查启动环境：

```sh
$ bectl list # 显示所有启动环境
BE           Active Mountpoint Space Created
15.0-RELEASE -      -          176K  2025-12-05 22:27
default      NR     /          10.6G 2025-01-14 20:36
```

Active 字段解释（来自 [bectl(8) 手册页](https://man.freebsd.org/cgi/man.cgi?bectl)）:

- “N”：表示该启动环境当前是否处于活动状态（当前是否位于此环境中）
- “R”：在重启时是否处于活动状态（下次是否选中，用于固定选项）
- “T”：是否会在下次启动时生效（且仅下次，用于一次性选项）
- “NRT”：这些标识（N / R / T）理论上可以组合出现（但实际不会出现，该组合在语义上存在矛盾）

- 列出系统中所有 ZFS 文件系统及其属性：

```sh
# zfs list
NAME                      USED  AVAIL  REFER  MOUNTPOINT

……其他省略……

zroot/ROOT/15.0-RELEASE     8K  83.8G  10.6G  /

……其他省略……
```

注意 `zroot/ROOT/15.0-RELEASE     8K  83.8G  10.6G  /` 这一行是刚刚创建的。

## 将启动环境中的系统版本更新到 15.0-RELEASE

### 挂载启动环境 15.0-RELEASE

- 创建一个临时目录用于更新启动环境 15.0-RELEASE 中的 FreeBSD 系统

```sh
# mkdir /mnt/upgrade
```

- 将启动环境（实际上是一个数据集）15.0-RELEASE 挂载到上面的路径中

```sh
# bectl mount 15.0-RELEASE /mnt/upgrade
/mnt/upgrade
```

- 显示已挂载文件系统的磁盘使用情况：

```sh
# df
Filesystem              1K-blocks     Used    Avail Capacity  Mounted on

……其他省略……

zroot/ROOT/15.0-RELEASE  99036272 11132688 87903584    11%    /mnt/upgrade

……其他省略……
```

可以看到，已经成功将启动环境 15.0-RELEASE 挂载到了指定路径。


### 验证当前 FreeBSD 版本

目前 15.0-RELEASE 实际上仍是 14.3-RELEASE。虽然这是已知事实，但仍可使用命令 `freebsd-version` 进行验证。

在 `/mnt/upgrade` 环境中运行 `freebsd-version`：

```sh
# chroot /mnt/upgrade freebsd-version -kru
14.3-RELEASE
14.3-RELEASE
14.3-RELEASE
```

`freebsd-version` 参数解释（摘自手册页 [freebsd-version(1)](https://man.freebsd.org/cgi/man.cgi?freebsd-version)）：

- `-k`：打印已安装内核的版本和补丁级别。与 [uname(1)](https://man.freebsd.org/uname(1)) 不同的是，如果新的内核已经安装但系统尚未重启，`freebsd-version` 会打印新内核的版本和补丁级别。
- `-r`：打印正在运行中的内核的版本和补丁级别。与 [uname(1)](https://man.freebsd.org/uname(1)) 不同的是，`freebsd-version` 不受环境变量影响。
- `-u`：打印已安装用户态的版本和补丁级别。这些信息在构建过程中会被写入程序 `freebsd-version` 中。


### 使用 pkgbase 将启动环境中的 14.3-RELEASE（系统版本）转换到 pkgbase

pkgbase 的设计初衷是为了让 stable、current 和 release（包括 BETA、RC 等）都能使用统一的二进制工具进行更新。之前，stable 和 current 只能通过完整编译源代码的方式进行更新。

>**注意**
>
>仅 FreeBSD 14.0-RELEASE 及更高版本才能直接被转换为 pkgbase。旧版仍需要通过 `freebsd-update` 进行更新（运行时 pkgbasify 会提示 `Unsupported FreeBSD version`，即 FreeBSD 版本不受支持）。

>**警告**
>
>**存在风险，可能会丢失所有数据！建议在操作之前做好备份。**

- `在 /mnt/upgrade` 环境中锁定 pkg 软件包，防止被升级或修改：

```sh
# pkg -c /mnt/upgrade lock pkg
pkg-2.4.2_1: lock this package? [y/N]: y # 输入 y 按回车键确认锁定 pkg
Locking pkg-2.4.2_1
```

- 下载 pkgbase 转换脚本

```sh
# fetch -o /mnt/upgrade https://raw.githubusercontent.com/FreeBSDFoundation/pkgbasify/main/pkgbasify.lua
```

- 使用 pkgbasify 进行转换

>**警告**
>
>在接受 `Do you accept this risk and wish to continue? (y/n)` 这个风险提示后就没有其他二次确认了！

```sh
# chroot /mnt/upgrade /usr/libexec/flua pkgbasify.lua
Running this tool will irreversibly modify your system to use pkgbase.
This tool and pkgbase are experimental and may result in a broken system.
It is highly recommended to backup your system before proceeding.
Do you accept this risk and wish to continue? (y/n) y # 这里是风险提示，确认
Updating FreeBSD repository catalogue...

……此处省略……

The following 370 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
        FreeBSD-acct: 14.3p6 [FreeBSD-base]
        FreeBSD-acct-man: 14.3p6 [FreeBSD-base]
        FreeBSD-acpi: 14.3p6 [FreeBSD-base]
        FreeBSD-acpi-man: 14.3p6 [FreeBSD-base]

……此处省略……

Conversion finished.

Please verify that the contents of the following critical files are as expected:
/etc/master.passwd
/etc/group
/etc/ssh/sshd_config

After verifying those files, restart the system.
```

- 检查启动环境 15.0-RELEASE 中的系统版本
  
```sh
# chroot /mnt/upgrade freebsd-version -kru
14.3-RELEASE-p6
14.3-RELEASE
14.3-RELEASE-p6
```

可以看到，pkgbasify 已将系统更新到最新的补丁版本，并完成了向 pkgbase 的转换。

### 使用 pkgbase 将启动环境中的系统版本更新到 15.0-RELEASE

- 创建 pkgbase 软件源目录

```sh
# mkdir -p /mnt/upgrade/usr/local/etc/pkg/repos/
```

- 编辑 `/mnt/upgrade/usr/local/etc/pkg/repos/FreeBSD-base.conf`，添加 pkgbase 源

```ini
FreeBSD-base {
    url = "https://pkg.freebsd.org/${ABI}/base_release_${VERSION_MINOR}";
    enabled = yes;
}
```

>**警告**
>
>请检查 `FreeBSD-base.conf` 的内容，尤其是 **不应该** 在里面手动硬编码写入指定任何具体的版本（如 `base_release_3`）。

>**技巧**
>
>需要换源的用户可以将 `url` 这行改成 `url = "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_release_${VERSION_MINOR}";`。而对于那些优先考虑安全性的读者应该维持默认设置。

- 刷新软件源

```sh
# pkg -c /mnt/upgrade update -r FreeBSD-base
```

- 使用 pkgbase 将 14.3-RELEASE 更新到 15.0-RELEASE（即将 ABI 指定为 15）

```sh
# env ABI=FreeBSD:15:amd64 pkg-static -c /mnt/upgrade upgrade -r FreeBSD-base	# 在 /mnt/upgrade 环境中使用指定 ABI 升级 FreeBSD 基础系统包
pkg-static: Setting ABI requires setting OSVERSION, guessing the OSVERSION as: 1500000
pkg-static: Warning: Major OS version upgrade detected.  Running "pkg bootstrap -f" recommended
Updating FreeBSD-base repository catalogue...
pkg-static: Repository FreeBSD-base has a wrong packagesite, need to re-create database
Fetching meta.conf: 100%    179 B   0.2kB/s    00:01    
Fetching data.pkg: 100%   80 KiB  81.6kB/s    00:01    
Processing entries:   0%
Newer FreeBSD version for package FreeBSD-zlib-dbg:
To ignore this error set IGNORE_OSVERSION=yes
- package: 1500068
- running userland: 1500000
Ignore the mismatch and continue? [y/N]: y # 此处输入 y 后继续
Processing entries: 100%
FreeBSD-base repository update completed. 496 packages processed.
FreeBSD-base is up to date.
Checking for upgrades (230 candidates): 100%
Processing candidates (230 candidates): 100%
The following 290 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
        FreeBSD-atf: 15.0 [FreeBSD-base]
        FreeBSD-atf-dev: 15.0 [FreeBSD-base]
        FreeBSD-atf-lib: 15.0 [FreeBSD-base]

        ……此处省略一部分…

        FreeBSD-zoneinfo: 14.3p6 -> 15.0 [FreeBSD-base]

Number of packages to be installed: 61
Number of packages to be upgraded: 229

The operation will free 100 MiB.
473 MiB to be downloaded.

Proceed with this action? [y/N]: y # 此处输入 y 后继续
```

>**技巧**
>
>如果检查不到任何更新，请检查你当前是否已成功转换为 pkgbase，并确认软件源配置是否正确


- 检查启动环境 15.0-RELEASE 中的系统版本
  
```sh
# chroot /mnt/upgrade freebsd-version -kru
15.0-RELEASE
14.3-RELEASE
15.0-RELEASE
```

这里 `r` 显示为 14.3-RELEASE 并无异常，说明当前运行的仍是 14.3。结合其他参数，可知重启后才会变成 15.0-RELEASE。

- 解锁 pkg

```sh
# chroot /mnt/upgrade pkg unlock pkg
pkg: Warning: Major OS version upgrade detected.  Running "pkg bootstrap -f" recommended
pkg-2.4.2_1: unlock this package? [y/N]: y
Unlocking pkg-2.4.2_1
```

- 将所有第三方软件包的 ABI 更新到 FreeBSD 15.0

```sh
# chroot /mnt/upgrade pkg upgrade
```

更新过程中需要多次确认才能完成。

### 启动到启动环境 15.0-RELEASE

- 在下次启动时进入启动环境 15.0-RELEASE

```sh
# bectl activate -t 15.0-RELEASE
Successfully activated boot environment 15.0-RELEASE
for next boot
```

- 验证设置是否成功。列出系统中所有 ZFS 启动环境：

```sh
$ bectl list
BE                             Active Mountpoint   Space Created
15.0-RELEASE                   T      /mnt/upgrade 8.75G 2025-12-05 23:22
default                        NR     /            10.9G 2025-01-14 20:36
```

注意，这是一次性的（`T`），此处仅用于验证其是否能够正常启动。我们还需要回到目前的主系统 14.3-RELEASE 来更新 ZFS。

- 重启以进入启动环境 15.0-RELEASE

```sh
# reboot
```

- 验证版本：

```sh
$ freebsd-version -kru
15.0-RELEASE
15.0-RELEASE
15.0-RELEASE
$ bectl list
BE                             Active Mountpoint Space Created
15.0-RELEASE                   N      /          8.75G 2025-12-05 23:22
default                        R      -          10.9G 2025-01-14 20:36
```

可以看到，我们已经成功将启动环境 15.0-RELEASE 中的 FreeBSD 系统升级到了 15.0-RELEASE。现在名副其实了。

并且 `R` 意味着我们再次重启就会回到启动环境 `default`（14.3-RELEASE）。

## 附录：永久性使用 15.0-RELEASE

如果读者不需要多版本共存，并且验证过目前的环境满足需要，也可以将启动环境 15.0-RELEASE 设置为永久的：

```sh
# bectl activate 15.0-RELEASE
```

随后，读者也可以销毁不再需要的启动环境：

```sh
# bectl destroy 启动环境
```

将参数 `启动环境` 替换为命令 `bectl list` 输出中 `BE` 列对应的启动环境名称即可将其销毁。

## 将基本系统中的 ZFS 替换为 Ports 版本

通常，在 FreeBSD 大版本之间，ZFS 池版本和特性都会发生变化，例如从 13 到 14 时 zpool 就有所变动。

可通过 Ports 中的 OpenZFS 实现 13、14、15 等多个系统版本的共存。

>**警告**
>
>如不按照下方进行设置就强行升级 ZFS 池/特性，将无法访问旧版系统。

那些有意愿实现多版本共存的读者可以直接重启，进入启动环境 `default`（14.3-RELEASE）。

### 验证当前系统版本

我们需要确定我们的确在启动环境 `default`（14.3-RELEASE）中。

```sh
$ bectl list
BE                             Active Mountpoint Space Created
15.0-RELEASE                   -      -          8.75G 2025-12-05 23:22
default                        NR     /          10.9G 2025-01-14 20:36
$ freebsd-version -kru
14.3-RELEASE
14.3-RELEASE
14.3-RELEASE
```

可以看到，我们已经回来了。


### 查看内置的 OpenZFS 版本

显示当前 ZFS 工具和内核模块的版本信息：

```sh
# zfs --version
zfs-2.2.7-FreeBSD_ge269af1b3
zfs-kmod-2.2.7-FreeBSD_ge269af1b3
```

目前 FreeBSD 基本系统内置的是 OpenZFS 2.2.7（即来自 <https://github.com/openzfs/zfs/commit/e269af1b3>）

### 安装 filesystems/openzfs

- 使用 pkg 安装

```sh
# pkg ins openzfs
```

- 使用 ports 安装：

```sh
# cd /usr/ports/filesystems/openzfs/ 
# make install clean
```

### 编辑 `/boot/loader.conf`

为了防止系统加载基本系统内置的 ZFS 版本，需要在 `zfs_load=YES` 前加上注释 `#`，取消其开机自动加载。

形如：

```ini
# zfs_load=YES	# 禁用内置 ZFS 模块加载
```

再新增下列数行：

```ini
zfs_load=NO        # 禁用内置 ZFS 模块加载
openzfs_load=YES   # 启用 OpenZFS 模块加载
```

完成后重启系统。

### 检查 ZFS 版本

在重启后，检查 ZFS 版本：

```sh
# zfs --version
zfs-2.2.7-FreeBSD_ge269af1b3
zfs-kmod-2.3.5-1
```

随后即可更新其他存储池或启用新的特性。

>**警告**
>
>考虑到基本系统中的 OpenZFS 版本不一定是最新的，所以你最好对所有版本都使用 Ports 中的版本以期达到统一。换言之，建议读者也在 15.0-RELEASE 中按照相同方法替换 ZFS。

## 附录：给 pkgbasify 脚本换源

### 修改示例（使用 USTC）

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

将这个函数修改如下，其中在 `return` 部分指定了镜像站：

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

>**警告**
>
>请删除 `return "pkg+https://"` 这行里面的 `pkg+`，否则会报错。

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

>**注意**
>
>对于那些优先考虑安全性的读者应该保持默认设置。

### 南京大学开源镜像站 NJU

```ini
https://mirrors.nju.edu.cn/freebsd-pkg/
```


### 网易开源镜像站 163

```ini
https://mirrors.163.com/freebsd-pkg/
```

## 附录：配置软件源

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

以上表格中的时间已转换为北京时间（东八区），对应 FreeBSD 官方镜像站的发布时间。

若官方源下载速度慢，可以考虑换成国内镜像。只需要替换 `https://pkg.freebsd.org` 这部分。

## 参考文献

- [ZFS Boot Environments Explained](https://vermaden.wordpress.com/2025/11/25/zfs-boot-environments-explained/)，指出可以手动安装 openzfs 来达到旧系统使用新 zfs 池的目的
- [wiki/BootEnvironments](https://wiki.freebsd.org/BootEnvironments)，维基
- man [bectl(8)](https://man.freebsd.org/cgi/man.cgi?bectl)
