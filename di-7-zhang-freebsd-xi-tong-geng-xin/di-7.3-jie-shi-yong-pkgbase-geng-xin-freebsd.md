# 7.3 使用 PkgBase 更新 FreeBSD

借助 ZFS 启动环境，可在同一台机器上保留多个独立的系统版本，升级失败时无需重新安装即可回滚到先前状态，从而实现原子更新、多系统并存与快速回滚。本节所述方法仅适用于使用 ZFS 文件系统的系统。

> **警告**
>
> PkgBase 与 freebsd-update **不可混用**。一旦将系统转换为 PkgBase，所有系统更新均应通过 pkg 包管理器进行，不得再使用 freebsd-update，否则可能导致系统组件冲突、文件损坏或系统无法启动。

## 创建启动环境 15.0-RELEASE

ZFS 启动环境（Boot Environment，BE）允许在系统中创建多个独立的系统环境，实现不同版本的共存与安全切换。以下操作将创建启动环境 15.0-RELEASE。

- 使用工具 bectl 创建启动环境 `15.0-RELEASE`：

```sh
# bectl create 15.0-RELEASE
```

> **注意**
>
> 此处启动环境命名为 15.0-RELEASE，但当前系统仍为 14.3-RELEASE。

- 使用 bectl 检查启动环境：

```sh
$ bectl list # 显示所有启动环境
BE           Active Mountpoint Space Created
15.0-RELEASE -      -          176K  2025-12-05 22:27
default      NR     /          10.6G 2025-01-14 20:36
```

- 列出系统中所有 ZFS 文件系统及其属性：

```sh
# zfs list
NAME                      USED  AVAIL  REFER  MOUNTPOINT

……其他省略……

zroot/ROOT/15.0-RELEASE     8K  83.8G  10.6G  /

……其他省略……
```

其中 `zroot/ROOT/15.0-RELEASE` 一行即为新创建的启动环境。

## 将启动环境中的系统版本更新到 15.0-RELEASE

创建启动环境后，需要更新到目标版本。操作分为挂载、验证版本、转换为 PkgBase、升级四个步骤。

### 挂载启动环境 15.0-RELEASE

操作启动环境前，需先将其挂载至文件系统。首先创建临时目录：

- 创建一个临时目录，用于更新启动环境 15.0-RELEASE 中的系统

```sh
# mkdir /mnt/upgrade
```

```sh
/mnt/
└── upgrade/ # 启动环境挂载目录
    └── usr/
        └── local/
            └── etc/
                └── pkg/
                    └── repos/
                        └── FreeBSD-base.conf # PkgBase 源配置文件
```

- 将启动环境（实际上是一个数据集）15.0-RELEASE 挂载到指定路径

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

### 验证当前 FreeBSD 版本

该启动环境（ZFS 数据集）15.0-RELEASE 当前实际仍为 14.3-RELEASE，可使用 `freebsd-version` 验证：

在 **/mnt/upgrade** 环境中运行 `freebsd-version`：

```sh
# chroot /mnt/upgrade freebsd-version -kru
14.3-RELEASE
14.3-RELEASE
14.3-RELEASE
```

`freebsd-version` 参数解释：

| 参数 | 说明 |
| ---- | ---- |
| `-k` | 打印已安装内核的版本和补丁级别。不同于 uname(1)，如果新的内核已经安装但系统尚未重启，`freebsd-version` 会打印新内核的版本和补丁级别 |
| `-r` | 打印正在运行中的内核的版本和补丁级别。不同于 uname(1)，`freebsd-version` 不受环境变量影响 |
| `-u` | 打印已安装用户态的版本和补丁级别。这些信息在构建过程中会写入程序 `freebsd-version` 中 |

### 使用 PkgBase 将启动环境中的 14.3-RELEASE（系统版本）转换为 PkgBase

升级之前，需将传统的 FreeBSD 系统转换为 PkgBase 格式。PkgBase 是 FreeBSD 官方提供的基本系统打包方式，使用 pkg 包管理器管理系统组件。

PkgBase 的设计目标是使 stable、current 与 release（包括 BETA、RC 等）分支均能使用统一的二进制工具进行更新。此前，stable 与 current 分支仅能通过编译源代码进行更新。

> **注意**
>
> 仅 FreeBSD 14.0-RELEASE 及更高版本才能直接转换为 PkgBase。旧版仍需要通过 `freebsd-update` 更新（运行时 pkgbasify 会提示 `Unsupported FreeBSD version`，即 FreeBSD 版本不受支持）。

> **警告**
>
> **存在风险，可能会丢失所有数据！建议在操作前做好备份。**

- 在 **/mnt/upgrade** 环境中锁定 pkg 软件包，防止升级或修改：

```sh
# pkg -c /mnt/upgrade lock pkg  # 在 /mnt/upgrade 环境中锁定 pkg 软件包
pkg-2.4.2_1: lock this package? [y/N]: y # 输入 y 按回车键确认锁定 pkg
Locking pkg-2.4.2_1
```

- 下载 PkgBase 转换脚本

```sh
# fetch -o /mnt/upgrade https://raw.githubusercontent.com/FreeBSDFoundation/pkgbasify/main/pkgbasify.lua  # 下载 PkgBase 转换脚本
```

- 使用 pkgbasify 转换

> **警告**
>
> 确认 `Do you accept this risk and wish to continue? (y/n)` 风险提示后便无二次确认步骤！

```sh
# chroot /mnt/upgrade /usr/libexec/flua pkgbasify.lua  # 使用 pkgbasify 转换
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

### 使用 PkgBase 将启动环境中的系统版本更新到 15.0-RELEASE

转换为 PkgBase 后，即可使用 pkg 包管理器升级系统。下面配置 PkgBase 源并执行升级。

软件源结构：

```sh
/usr/local/etc/pkg/
└── repos/ # pkg 仓库配置目录
    └── FreeBSD-base.conf # PkgBase 源配置文件
```

- 创建 PkgBase 软件源目录

```sh
# mkdir -p /mnt/upgrade/usr/local/etc/pkg/repos/  # 创建 PkgBase 软件源目录
```

- 编辑 **/mnt/upgrade/usr/local/etc/pkg/repos/FreeBSD-base.conf** 文件，添加 PkgBase 源

```ini
FreeBSD-base {
    url: "pkg+https://pkg.FreeBSD.org/${ABI}/base_release_${VERSION_MINOR}",
    mirror_type: "srv",
    signature_type: "fingerprints",
    fingerprints: "/usr/share/keys/pkgbase-${VERSION_MAJOR}",
    enabled: yes
}
```

> **警告**
>
> 请检查 `FreeBSD-base.conf` 的内容，尤其是 **不应该** 在其中手动硬编码任何具体的版本（如 `base_release_3`）。
>
> 由于 FreeBSD 15.0 使用了新的签名密钥，从 14.x 升级到 15.0 时必须将 `fingerprints` 路径从 pkgbasify 默认生成的 `/usr/share/keys/pkg` 改为 `/usr/share/keys/pkgbase-${VERSION_MAJOR}`，并确保已安装 pkgbase-15 密钥（可通过 `pkg add -f https://pkg.freebsd.org/FreeBSD:15:$(uname -p)/base_release_0/FreeBSD-pkg-bootstrap-15.0.pkg` 安装）。

> **技巧**
>
> 需要切换软件源的用户可将 `url` 这行改为 `url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_release_${VERSION_MINOR}",`。注重安全性的读者应维持默认设置。

- 刷新软件源

```sh
# pkg -c /mnt/upgrade update -r FreeBSD-base  # 刷新软件源
```

- 使用 PkgBase 将 14.3-RELEASE 更新到 15.0-RELEASE（即将 ABI 指定为 15）

```sh
# env ABI=FreeBSD:15:amd64 pkg-static -c /mnt/upgrade upgrade -r FreeBSD-base  # 在 /mnt/upgrade 环境中使用指定 ABI 升级 FreeBSD 基本系统包
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

> **技巧**
>
> 如果检查不到任何更新，请确认当前是否已成功转换为 PkgBase，并检查软件源配置是否正确。

- 检查启动环境 15.0-RELEASE 中的系统版本

```sh
# chroot /mnt/upgrade freebsd-version -kru
15.0-RELEASE
14.3-RELEASE
15.0-RELEASE
```

其中 `r` 显示为 14.3-RELEASE 并无异常，表明当前运行的仍是 14.3-RELEASE。结合其他参数，可知重启后才会切换至 15.0-RELEASE。

- 解锁 pkg

```sh
# chroot /mnt/upgrade pkg unlock pkg  # 解锁 pkg
pkg: Warning: Major OS version upgrade detected.  Running "pkg bootstrap -f" recommended
pkg-2.4.2_1: unlock this package? [y/N]: y
Unlocking pkg-2.4.2_1
```

- 将所有第三方软件包的 ABI 更新至 FreeBSD 15.0

```sh
# chroot /mnt/upgrade pkg upgrade  # 将所有第三方软件包的 ABI 更新到 FreeBSD 15.0
```

更新过程中需要多次确认才能完成。

### 启动到启动环境 15.0-RELEASE

完成所有更新操作后，启动到新的启动环境验证结果。

- 在下次启动时进入启动环境 15.0-RELEASE

```sh
# bectl activate -t 15.0-RELEASE  # 在下次启动时进入启动环境 15.0-RELEASE
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

注意，这是一次性的（`T`），此处仅用于验证其是否能够正常启动。还需要回到当前的主系统 14.3-RELEASE 来更新 ZFS。

- 重启以进入启动环境 15.0-RELEASE

```sh
# reboot  # 重启以进入启动环境 15.0-RELEASE
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

由输出可知，已成功将启动环境 15.0-RELEASE 中的 FreeBSD 系统升级到 15.0-RELEASE，此时启动环境名称与实际版本一致。

`R` 意味着再次重启将回到启动环境 `default`（14.3-RELEASE）。

## 附录：永久性使用 15.0-RELEASE

前面已通过一次性启动环境完成验证。如果验证通过并且不需要再保留旧版本，可以将新环境设置为永久默认。

如果读者不需要多版本共存，并且验证过目前的环境满足需要，也可以将启动环境 15.0-RELEASE 设置为永久的：

```sh
# bectl activate 15.0-RELEASE
```

随后，读者也可以销毁不再需要的启动环境：

```sh
# bectl destroy 要销毁的启动环境名称
```

将参数 `要销毁的启动环境名称` 替换为命令 `bectl list` 输出中 `BE` 列对应的启动环境名称即可销毁。

## 将基本系统中的 ZFS 替换为 Ports 版本

需实现多版本共存的读者可直接重启，进入启动环境 `default`（14.3-RELEASE），升级 14.3-RELEASE 中的 OpenZFS 版本。升级细节参照其他相关章节。

> **警告**
>
> 如不更新为 Ports 版本强行升级 ZFS 池/特性，将无法访问旧版系统。

## 附录：给 pkgbasify 脚本切换软件源

对于网络环境受限制的用户，可能需要为 pkgbasify 脚本配置国内镜像源以提高下载速度。下面介绍如何修改脚本中的源地址。

### 修改示例（使用 USTC）

中国科学技术大学（USTC）提供了 FreeBSD 的镜像服务，可以修改 pkgbasify 脚本来使用这个镜像源。首先需要找到脚本中的相关函数。

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

> **警告**
>
> 请删除 `return "pkg+https://"` 这行中的 `pkg+`，否则会报错。

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

> **技巧**
>
> 注重安全性的读者应保持默认设置。

其他开源镜像站参见软件源章节。

## 参考文献

- vermaden. ZFS Boot Environments Explained[EB/OL]. [2026-03-25]. <https://vermaden.wordpress.com/2025/11/25/zfs-boot-environments-explained/>. 详细阐释 ZFS 启动环境的原理与实践，包含跨版本 ZFS 池兼容方案。
- FreeBSD Project. BootEnvironments[EB/OL]. [2026-03-25]. <https://wiki.freebsd.org/BootEnvironments>. FreeBSD 官方关于启动环境的 Wiki。
- FreeBSD Project. bectl(8)[EB/OL]. [2026-03-25]. <https://man.freebsd.org/cgi/man.cgi?query=bectl&sektion=8>. ZFS 启动环境管理工具的官方技术规范。
