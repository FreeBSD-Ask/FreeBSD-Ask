# 第 3.9 节 使用 pkgbase 更新 FreeBSD

现在 FreeBSD 的系统更新是与第三方软件更新的分离的（现在使用 `freebsd-update`），pkgbase 是目的就是将其合并起来统一使用 `pkg` 命令进行管理（学习 Linux？）。因为现在只有一级架构的 RELEASE 才有 `freebsd-update` 可用。pkgbase 早在 2016 年就有了，原计划在 FreeBSD 14 就进入系统替代 `freebsd-update`，但是现在推迟到了 15。另外个人感觉 `freebsd-update` 体验非常差，非常慢（网络无关）。

**pkgbase 的设计初衷是为了让 stable、current 和 release（BETA、RC 等）都能使用一种二进制工具进行更新。当下，stable、current 只能通过完全编译源代码的方式来更新。**

目前不清楚是否让系统组件成为可选的部分（比如 cron、ntp 等第三方软件），这样就可以在 `bsdinstall` 安装的时候选择系统组件了。

>**警告**
>
>**存在风险，可能会丢失所有数据！**

## 配置软件源


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

以 FreeBSD 15.0-CURRENT 为例（当下仅支持 14 和 15）

创建文件夹：

```sh
# mkdir -p /usr/local/etc/pkg/repos/
```

编辑配置文件 `/usr/local/etc/pkg/repos/FreeBSD-base.conf`，写入以下内容，保存退出：


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

### FreeBSD 官方镜像站

```sh
FreeBSD-base: {
  url: "pkg+https://pkg.FreeBSD.org/${ABI}/base_latest",
  mirror_type: "srv",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
```

## 第一次安装更新

- 刷新软件源：

```sh
root@ykla:~ #  pkg update 
Updating FreeBSD repository catalogue...
Fetching meta.conf:   0%
FreeBSD repository is up to date.
Updating FreeBSD-base repository catalogue...
Fetching meta.conf: 100%    178 B   0.2kB/s    00:01    
Fetching data.pkg: 100%   40 KiB  40.6kB/s    00:01    
Processing entries: 100%
FreeBSD-base repository update completed. 527 packages processed.
All repositories are up to date.
```

- 安装 pkgbase：
  
```sh
root@ykla:~ # pkg install -r FreeBSD-base -g 'FreeBSD-*' 
Updating FreeBSD-base repository catalogue...
FreeBSD-base repository is up to date.
All repositories are up to date.
Updating database digests format: 100%
The following 527 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
	FreeBSD-acct: 15.snap20240806043323 [FreeBSD-base]

            ……省略一部分……
	FreeBSD-zoneinfo: 15.snap20240806043323 [FreeBSD-base]

Number of packages to be installed: 527

The process will require 5 GiB more space.
1 GiB to be downloaded.

Proceed with this action? [y/N]:
```


## 第一次安装 pkgbase 后的准备工作（仅需这一次，以后可能不再需要）

还原配置文件（**如果不做这一步，你的密码都会被清零**）：

```sh
# cp /etc/ssh/sshd_config.pkgsave /etc/ssh/sshd_config
# cp /etc/master.passwd.pkgsave /etc/master.passwd
# cp /etc/group.pkgsave /etc/group
# pwd_mkdb -p /etc/master.passwd
# service sshd restart
# cp /etc/sysctl.conf.pkgsave /etc/sysctl.conf
```

按照 WIKI，直接删掉旧系统的文件就行：

>**注意**
>
>我测试的是纯净系统，没有任何多余配置及第三方程序（除了 pkg），仅开了 SSH 服务。

```sh
# find / -name \*.pkgsave -delete
# rm /boot/kernel/linker.hints
```


>**警告**
>
>**存在风险，可能会丢失所有数据！**

>**技巧**
>
>**经测试，以后更新直接 `pkg upgrade` 即可，不再需要此节内容**

## 参考文献

- [wiki/PkgBase](https://wiki.freebsd.org/PkgBase)

