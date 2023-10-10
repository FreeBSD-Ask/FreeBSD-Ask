# 第 1.14节 FreeBSD 安全公告


## FreeBSD 安全公告 FreeBSD-SA-23:11.wifi

- **主题:** Wi-Fi 加密绕过
- **分类:** 核心
- **模块:** net80211
- **公告日期:** 2023 年 09 月 06 日
- **贡献者** 请参阅参考部分中链接的论文
- **受影响版本:** 所有受支持的 FreeBSD 版本
- **修复日期:**
  - 2023 年 06 月 26 日 12:02:00 UTC (stable/13, 13.2-STABLE)
  - 2023 年 09 月 06 日 17:13:25 UTC (releng/13.2, 13.2-RELEASE-p3)
  - 2023 年 06 月 26 日 12:30:23 UTC (stable/12, 12.4-STABLE)
  - 2023 年 09 月 06 日 17:38:34 UTC (releng/12.4, 12.4-RELEASE-p5)
- **CVE 名称:** CVE-2022-47522

有关 FreeBSD 安全公告的一般信息，包括上述字段的描述、安全分支和以下部分，请访问<https://security.FreeBSD.org/>。

### I. 背景

FreeBSD 的 net80211 内核子系统提供了 IEEE 802.11 无线（Wi-Fi）通信的基础设施和驱动程序。Wi-Fi 通信依赖于单播和多播密钥来保护传输。

### II. 问题描述

在单播密钥被删除的情况下，net80211 子系统会退回到多播密钥以处理单播流量。这将导致缓冲的单播流量暴露给具有多播密钥访问权限的任何站点。

### III. 影响

正如《Framing Frames: Bypassing Wi-Fi Encryption by Manipulating Transmit Queues》（绕过 Wi-Fi 加密通过操作传输队列）论文中所述，攻击者可以诱使访问点为客户端缓冲帧，断开客户端的连接（导致从访问点删除单播密钥），然后刷新缓冲的帧，这些帧现在使用多播密钥进行加密。这将使攻击者能够访问数据。

### IV. 解决方法

没有可用的解决方法。不使用 Wi-Fi 的系统不受影响。

### V. 解决方案

升级您的受影响系统到受支持的 FreeBSD  STABLE 版本或 RELEASE/安全分支（releng），日期在纠正日期之后，并重新启动。

执行以下操作之一：

1. 通过二进制补丁更新您的受影响系统：

在 amd64、i386 或（在 FreeBSD 13 及以后）arm64 平台上运行 FreeBSD RELEASE 版本的系统可以通过 freebsd-update(8) 工具进行更新：

```
# freebsd-update fetch
# freebsd-update install
# shutdown -r +10min "Rebooting for a security update"
```

2. 通过源代码补丁更新您的受影响系统：

以下补丁已被验证可适用于适用的 FreeBSD 发布分支。

a) 从以下位置下载相关补丁，并使用您的 PGP 工具验证分离的 PGP 签名。

```
# fetch https://security.FreeBSD.org/patches/SA-23:11/wifi.patch
# fetch https://security.FreeBSD.org/patches/SA-23:11/wifi.patch.asc
# gpg --verify wifi.patch.asc
```

b) 应用补丁。以 root 用户身份执行以下命令：

```
# cd /usr/src
# patch < /path/to/patch
```

c) 根据 <https://www.FreeBSD.org/handbook/kernelconfig.html> 中说明的方式重新编译内核并重新启动系统。

### VI. 修复详细信息

此问题通过以下 STABLE 和 RELEASE 分支中的相应 Git 提交哈希或 Subversion 修订号来纠正：

| 分支/路径    | 哈希         | 修订号              |
| ------------ | ------------ | ------------------- |
| stable/13/   | 6c9bcecfb296 | stable/13-n255680   |
| releng/13.2/ | 7f34ee7cc56b | releng/13.2-n254632 |
| stable/12/   |              | r373115             |
| releng/12.4/ |              | r373187             |

对于 FreeBSD 13 及更高版本：

运行以下命令以查看特定提交修改的文件：

```
# git show --stat <commit hash>
```

或访问以下 URL，替换 NNNNNN 为哈希值：

<https://cgit.freebsd.org/src/commit/?id=NNNNNN>

要确定工作树中的提交计数（用于与上表中的 nNNNNNN 进行比较），运行：

```
# git rev-list --count --first-parent HEAD
```

对于 FreeBSD 12 及更早版本：

运行以下命令以查看特定修订号修改的文件，替换 NNNNNN 为修订号：

```
# svn diff -cNNNNNN --summarize svn://svn.freebsd.org/base
```

或访问以下 URL，替换 NNNNNN 为修订号：

<https://svnweb.freebsd.org/base?view=revision&revision=NNNNNN>

### VII. 参考资料

<https://papers.mathyvanhoef.com/usenix2023-wifi.pdf>

<https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47522>


## FreeBSD 安全公告 FreeBSD-SA-23:10.pf


- **主题:** pf 在处理多个 IPv6 分片头时出现错误
- **分类:** 核心
- **模块:** pf
- **公告日期:** 2023 年 09 月 06 日
- **贡献者** Enrico Bassetti bassetti@di.uniroma1.it (罗马大学的 NetSecurityLab)
- **受影响版本:** 所有受支持的 FreeBSD 版本
- **修复日期:**
  - 2023 年 08 月 04 日 14:08:05 UTC (stable/13, 13.2-STABLE)
  - 2023 年 09 月 06 日 16:58:39 UTC (releng/13.2, 13.2-RELEASE-p3)
  - 2023 年 08 月 04 日 14:14:08 UTC (stable/12, 12.4-STABLE)
  - 2023 年 09 月 06 日 17:38:31 UTC (releng/12.4, 12.4-RELEASE-p5)
- **CVE 名称:** CVE-2023-4809

有关 FreeBSD 安全公告的一般信息，包括上述字段的描述、安全分支和以下部分，请访问 <https://security.FreeBSD.org/>。

### I. 背景

pf 是最初为 OpenBSD 编写的 Internet 协议数据包过滤器。pf 可以重新组装分段的 IPv6 数据包以便对重新组装后的数据包应用规则。这使得 pf 可以基于上层协议（例如 TCP、UDP）信息进行过滤。

IPv6 数据包可能会被原始节点分段，并且将包含一个分段扩展头。一个 IPv6 数据包通常只包含一个分段扩展头。

### II. 问题描述

使用'scrub fragment reassemble'规则，包含多个 IPv6 分片头的数据包将被重新组装，然后立即处理。也就是说，包含多个分段扩展头的数据包不会被识别为正确的最终有效载荷。而是，多个 IPv6 分片头的数据包将意外地被解释为分段数据包，而非实际有效载荷是什么。

### III. 影响

IPv6 分段可能会绕过基于所有分段已被重新组装的假设编写的防火墙规则，并因此被主机转发或处理。

### IV. 解决方法

没有可用的解决方法，但不使用 pf 防火墙的系统不受影响。

### V. 解决方案

升级您的受影响系统到支持的 FreeBSD  STABLE 版本或 RELEASE/安全分支（releng），日期在纠正日期之后，并重新启动。

执行以下操作之一：

1. 通过二进制补丁更新您受影响的系统：

在 amd64、i386 或（在 FreeBSD 13 及以后）arm64 平台上运行 FreeBSD RELEASE 版本的系统可以通过 freebsd-update(8)工具进行更新：

```
# freebsd-update fetch
# freebsd-update install
# shutdown -r +10min "Rebooting for a security update"
```

2. 通过源代码补丁更新您的受影响系统：

以下补丁已被验证可适用于适用的 FreeBSD 发布分支。

a) 从以下位置下载相关补丁，并使用您的 PGP 工具验证分离的 PGP 签名。

[FreeBSD 13.2]

```
# fetch https://security.FreeBSD.org/patches/SA-23:10/pf.13.patch
# fetch https://security.FreeBSD.org/patches/SA-23:10/pf.13.patch.asc
# gpg --verify pf.13.patch.asc
```

[FreeBSD 12.4]

```
# fetch https://security.FreeBSD.org/patches/SA-23:10/pf.12.patch
# fetch https://security.FreeBSD.org/patches/SA-23:10/pf.12.patch.asc
# gpg --verify pf.12.patch.asc
```

b) 应用补丁。以 root 用户身份执行以下命令：

```
# cd /usr/src
# patch < /path/to/patch
```

c) 根据 <https://www.FreeBSD.org/handbook/kernelconfig.html> 中说明的方式重新编译内核并重新启动系统。

### VI. 更正详情

此问题通过以下 Stable 和 Release 分支中的相应 Git 提交哈希或 Subversion 修订号来纠正：

| 分支/路径    | 哈希         | 修订号              |
| ------------ | ------------ | ------------------- |
| stable/13/   | 3a0461f23a4f | stable/13-n255953   |
| releng/13.2/ | 41b7760991ef | releng/13.2-n254631 |
| stable/12/   |              | r373157             |
| releng/12.4/ |              | r373186             |

对于 FreeBSD 13 及更高版本：

运行以下命令以查看特定提交修改的文件：

```
# git show --stat <commit hash>
```

或访问以下 URL，替换 `NNNNNN` 为哈希值：

<https://cgit.freebsd.org/src/commit/?id=NNNNNN>

要确定工作树中的提交计数（用于与上表中的 nNNNNNN 进行比较），运行：

```
# git rev-list --count --first-parent HEAD
```

对于 FreeBSD 12 及更早版本：

运行以下命令以查看特定修订号修改的文件，替换 NNNNNN 为修订号：

```
# svn diff -cNNNNNN --summarize svn://svn.freebsd.org/base
```

或访问以下 URL，替换 NNNNNN 为修订号：

<https://svnweb.freebsd.org/base?view=revision&revision=NNNNNN>

## VII. 参考资料

<https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4809>

## FreeBSD 安全公告 FreeBSD-SA-23:09.pam_krb5

- **主题：** pam_krb5 通过网络身份验证攻击

- **类别：** 核心
- **模块：** pam_krb5
- **发布日期：** 2023 年 8 月 1 日
- **受影响版本：** 所有受支持的 FreeBSD 版本
- **修复日期：**
  - 2023 年 7 月 8 日 05:44:29 UTC (stable/13, 13.2-STABLE)
  - 2023 年 8 月 1 日 19:50:30 UTC (releng/13.2, 13.2-RELEASE-p2)
  - 2023 年 8 月 1 日 19:48:09 UTC (releng/13.1, 13.1-RELEASE-p9)
  - 2023 年 7 月 8 日 05:44:51 UTC (stable/12, 12.4-STABLE)
  - 2023 年 8 月 1 日 19:46:53 UTC (releng/12.4, 12.4-RELEASE-p4)
- **CVE 编号：** CVE-2023-3326

有关 FreeBSD 安全公告的一般信息，包括上述字段的描述、安全分支和以下部分，请访问 <URL:https://security.FreeBSD.org/>。

**I. 背景**

Kerberos 5 (krb5) 是一种基于票据的计算机网络身份验证协议，它允许通过票证在非安全网络上通信的节点以安全的方式相互验证身份。

PAM（可插拔认证模块）库提供了一个灵活的用户身份验证和会话设置/拆除框架。

pam_krb5 是一个 PAM 模块，允许使用 Kerberos 密码对用户进行身份验证。 在默认的 FreeBSD 安装中，pam_krb5 被禁用。

pam_krb5 使用密码进行身份验证，这与 Kerberos 本机协议（如 GSSAPI）不同，后者允许在不交换密码的情况下进行登录。 GSSAPI 不受此问题影响。

**II. 问题描述**

FreeBSD-SA-23:04.pam_krb5 中详细描述的问题在该公告的补丁后仍存在。

**III. 影响**

在 FreeBSD-SA-23:04.pam_krb5 中描述的影响仍然存在。

**IV. 解决方法**

如果您压根不使用 Kerberos，请确保系统中不存在 `/etc/krb5.conf` 这个文件。 此外，请确保将 pam_krb5 从 PAM 配置中注释掉，位置如 pam.conf(5) 中所述，通常在 `/etc/pam.d`。 请注意，在默认的 FreeBSD PAM 配置中已注释掉了 pam_krb5。

如果您使用 Kerberos，但不使用 pam_krb5，请确保将 pam_krb5 从 PAM 配置中注释掉，位置如 pam.conf(5) 中所述，通常在 `/etc/pam.d`。 请注意，在默认的 FreeBSD PAM 配置中已注释掉了 pam_krb5。

如果您使用 pam_krb5，请确保您的系统上有一个由 Kerberos 管理员提供的密钥表（keytab）。

**V. 解决方案**

将易受攻击的系统升级为支持的 FreeBSD STABLE 或 RELEASE 安全分支（releng），日期在修正日期之后。

执行以下操作之一：

1. 通过二进制补丁更新易受攻击的系统：

在 amd64、i386 或（在 FreeBSD 13 及更高版本上）arm64 平台上运行 RELEASE 版本的 FreeBSD 系统可以使用 freebsd-update(8)工具进行更新：
```shell-session
# freebsd-update fetch
# freebsd-update install
```
2. 通过源代码补丁更新易受攻击的系统：

以下补丁已经验证适用于适用的 FreeBSD 发行版分支。

a) 从以下位置下载相关补丁，并使用您的 PGP 工具验证已分离的 PGP 签名。
```shell-session
# fetch https://security.FreeBSD.org/patches/SA-23:09/pam_krb5.patch
# fetch https://security.FreeBSD.org/patches/SA-23:09/pam_krb5.patch.asc
# gpg --verify pam_krb5.patch.asc
```
b) 应用补丁。 以 root 用户执行以下命令：
```shell-session
# cd /usr/src
# patch < /path/to/patch
```
c) 如 <URL:https://www.FreeBSD.org/handbook/makeworld.html> 中所述，重新编译您的操作系统，并重新启动使用 PAM 模块的所有守护进程，或重新启动系统。

**VI. 修正细节**

此问题通过以下 STABLE 和 RELEASE 分支中的相应 Git 提交哈希或 Subversion 修订号来进行修正：

|分支/路径| 哈希| 修订号|
|---|---|---|
|stable/13/ d295e418ae7e stable/13-n255792|
|releng/13.2/| 9b45d8eddfac| releng/13.2-n254622|
|releng/13.1/| 140f65a20533| releng/13.1-n250188|
|stable/12/ ||r373127|
|releng/12.4/|| r373150|

对于 FreeBSD 13 及更高版本：

运行以下命令以查看特定提交修改了哪些文件：
```shell-session
# git show --stat <提交哈希>
```
或访问以下 URL，将 `NNNNNN` 替换为哈希：

<URL:https://cgit.freebsd.org/src/commit/?id=NNNNNN>

要在工作树中确定提交计数（用于与上表中的 `nNNNNNN` 进行比较），运行：
```shell-session
# git rev-list --count --first-parent HEAD
```
对于 FreeBSD 12 及更早版本：

运行以下命令以查看特定修订修改了哪些文件，将 `NNNNNN` 替换为修订号：
```shell-session
# svn diff -cNNNNNN --summarize svn://svn.freebsd.org/base
```
或访问以下 URL，将 `NNNNNN` 替换为修订号：

<URL:https://svnweb.freebsd.org/base?view=revision&revision=NNNNNN>

**VII. 参考**

<URL:https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3326>

此安全公告的最新修订版可在以下 URL 上获取：
<URL:https://security.FreeBSD.org/advisories/FreeBSD-SA-23:09.pam_krb5.asc>

## FreeBSD 安全公告 FreeBSD-SA-23:07.bhyve

- **主题:**           bhyve 特权客户机通过 fwctl 实现逃逸

- **类别:**          核心
- **模块:**          bhyve
- **发布日期:**      2023-08-01
- **致谢：**        来自微软的 Omri Ben Bassat 和 Vladimir Eli Tokarev
- **影响版本:**       FreeBSD 13.1 和 13.2
-**修复日期:**
  - 2023-08-01 19:48:53 UTC (stable/13, 13.2-STABLE)
  - 2023-08-01 19:50:47 UTC (releng/13.2, 13.2-RELEASE-p2)
  - 2023-08-01 19:48:26 UTC (releng/13.1, 13.1-RELEASE-p9)
- **CVE 编号:**      CVE-2023-3494

有关 FreeBSD 安全公告的一般信息，包括上述字段的描述、安全分支，以及以下各部分，请访问 [FreeBSD Security Advisories](https://security.FreeBSD.org/)。

I.   背景

bhyve(8) 的 fwctl 接口为客户机固件提供了一种查询虚拟机信息的机制。当以 "-l bootrom" 选项运行 bhyve 时，该 fwctl 接口对客户机可用，例如在 UEFI 模式下启动客户机时使用。

bhyve 目前仅支持在 amd64 平台上运行。

II.  问题描述

fwctl 驱动程序实现了一个状态机，当客户机访问特定的 x86 I/O 端口时执行该状态机。该接口允许客户机将字符串复制到驻留在 bhyve 进程内存中的缓冲区中。状态机实现中的一个错误可能导致在复制此字符串时发生缓冲区溢出。

III. 影响

在客户机虚拟机中运行的恶意特权软件可以利用缓冲区溢出，在 bhyve 用户空间进程中实现对主机的代码执行，通常该进程以 root 权限运行。请注意，bhyve 在 Capsicum 沙盒中运行，因此恶意代码受到 bhyve 进程可用能力的限制。

IV.  解决方法

目前没有可用的解决方法。未使用 `-l bootrom` 参数执行的 bhyve 客户机不受影响。

V.   解决方案

将您的受影响系统升级到支持的 FreeBSD  stable 或 RELEASE/安全分支（releng），升级日期应在修正日期之后。

执行以下操作之一：

1) 通过二进制补丁更新您的受影响系统：

在 amd64、i386 或 (FreeBSD 13 及更高版本) arm64 平台上运行 RELEASE 版本的 FreeBSD 系统可以使用 `freebsd-update(8)` 工具进行更新：

```shell-session
freebsd-update fetch
freebsd-update install
```


重新启动所有受影响的虚拟机。

2) 通过源代码补丁更新您的受影响系统：

以下补丁已经过验证，适用于相应的 FreeBSD RELEASE 分支。

a) 从下方的位置下载相关补丁，并使用您的 PGP 工具验证分离的 PGP 签名。

**FreeBSD 13.2**
```shell-session
fetch https://security.FreeBSD.org/patches/SA-23:07/bhyve.13.2.patch
fetch https://security.FreeBSD.org/patches/SA-23:07/bhyve.13.2.patch.asc
gpg --verify bhyve.13.2.patch.asc
```


**FreeBSD 13.1**
```shell-session
fetch https://security.FreeBSD.org/patches/SA-23:07/bhyve.13.1.patch
fetch https://security.FreeBSD.org/patches/SA-23:07/bhyve.13.1.patch.asc
gpg --verify bhyve.13.1.patch.asc
```


b) 应用补丁。以 root 身份执行以下命令：
```shell-session
cd /usr/src
patch < /path/to/patch
```


c) 使用 `buildworld` 和 `installworld` 重新编译操作系统，如 [FreeBSD 手册 - Building and Installing](https://www.FreeBSD.org/handbook/makeworld.html) 中所述。

重新启动所有受影响的虚拟机。

VI.  修正详情

此问题通过以下 STABLE 和 RELEASE 分支中相应的 Git 提交哈希或 Subversion 修订号进行修正：

|分支/路径   |                          哈希        |             修订号|
|---|---|---| 
| stable/13/     |                          9fe302d78109 |    stable/13-n255918| 
| releng/13.2/      |                       2bae613e0da3 |  releng/13.2-n254625| 
| releng/13.1/     |                        87702e38a4b4 |  releng/13.1-n250190| 


运行以下命令查看特定提交修改了哪些文件：

```shell-session
git show --stat <commit hash>
```


或访问以下 URL，在其中将 `NNNNNN` 替换为哈希：

[FreeBSD Commit](https://cgit.freebsd.org/src/commit/?id=NNNNNN)

要确定工作树中的提交数（以与上表中的 `nNNNNNN` 进行比较），运行：

```shell-session
git rev-list --count --first-parent HEAD
```

VII. 参考文献

[CVE-2023-3494](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3494)


此安全公告的最新修订版可在以下 URL 上获取：

[FreeBSD-SA-23:07.bhyve.asc](https://security.FreeBSD.org/advisories/FreeBSD-SA-23:07.bhyve.asc)

## FreeBSD 安全公告 FreeBSD-SA-23:06.ipv6

- **主题：** IPv6 片段重组中的远程拒绝服务

- **类别：** 核心
- **模块：** ipv6
- **发布日期：** 2023 年 8 月 1 日
- **致谢：** Kunlun Lab 的 Zweig
- **受影响版本：** 所有受支持的 FreeBSD 版本
- **修复日期：**
  - 2023 年 8 月 1 日 19:49:07 UTC (stable/13, 13.2-STABLE)
  - 2023 年 8 月 1 日 19:51:27 UTC (releng/13.2, 13.2-RELEASE-p2)
  - 2023 年 8 月 1 日 19:49:52 UTC (releng/13.1, 13.1-RELEASE-p9)
  - 2023 年 8 月 1 日 20:05:08 UTC (stable/12, 12.4-STABLE)
  - 2023 年 8 月 1 日 20:05:42 UTC (releng/12.4, 12.4-RELEASE-p4)
- **CVE 编号：** CVE-2023-3107

有关 FreeBSD 安全公告的一般信息，包括上述字段的描述、安全分支和以下部分，请访问 <URL:https://security.FreeBSD.org/>。

**I. 背景**

IPv6 数据包可能会被分片以适应源主机和目标主机之间的网络路径的最大传输单元（MTU）。 FreeBSD 内核会跟踪接收到的数据包片段，并在接收到所有片段后重新组装原始数据包，然后对数据包进行正常处理。

**II. 问题描述**

IPv6 数据包的每个片段都包含一个片段头，指定相对于原始数据包的片段偏移，并且每个片段在 IPv6 头中指定其长度。 在重新组装数据包时，内核会计算完整的 IPv6 有效载荷长度。有效载荷长度必须适合 IPv6 头中的 16 位字段。

由于内核中的一个错误，一组精心构造的数据包可以触发重新组装数据包的有效载荷长度字段的整数溢出。

**III. 影响**

如果 IPv6 数据包被重新组装，内核将继续处理其内容。 它会假设分片层已验证了构造的 IPv6 头的所有字段。 该漏洞违反了这些假设，并可被利用以触发远程内核 panic，导致拒绝服务。

**IV. 解决方法**

禁用不受信任的网络接口上的 IPv6 的用户不受影响。 这些接口将在 ifconfig(8) 中设置 IFDISABLED nd6 标志。

可以通过将 sysctl `1net.inet6.ip6.maxfrags` 设置为 0 来配置内核以丢弃所有 IPv6 片段。 这样做将阻止漏洞被触发，但正常的 IPv6 片段将被丢弃。

如果启用了 pf(4) 防火墙，并且在不受信任的接口上启用了 scrubbing 和片段重组，则无法触发此漏洞。 这是启用了 pf(4) 的默认设置。

**V. 解决方案**

将易受攻击的系统升级为支持的 FreeBSD STABLE 或 RELEASE/安全分支（releng），日期在修正日期之后，并重新启动。

执行以下操作之一：

1. 通过二进制补丁更新易受攻击的系统：

在 amd64、i386 或（在 FreeBSD 13 及更高版本上）arm64 平台上运行 RELEASE 版本的 FreeBSD 系统可以使用 freebsd-update(8) 工具进行更新：

```shell-session
# freebsd-update fetch
# freebsd-update install
# shutdown -r +10min "Rebooting for a security update"
```

2. 通过源代码补丁更新易受攻击的系统：

以下补丁已经验证适用于适用的 FreeBSD 发行版分支。

a) 从以下位置下载相关补丁，并使用您的 PGP 工具验证已分离的 PGP 签名。

```shell-session
# fetch https://security.FreeBSD.org/patches/SA-23:06/ipv6.patch
# fetch https://security.FreeBSD.org/patches/SA-23:06/ipv6.patch.asc
# gpg --verify ipv6.patch.asc
```
b) 应用补丁。 以 root 用户执行以下命令：
```shell-session
# cd /usr/src
# patch < /path/to/patch
```
c) 如 <URL:https://www.FreeBSD.org/handbook/kernelconfig.html> 中所述，重新编译您的内核，并重新启动系统。

**VI. 修正细节**

此问题通过以下 STABLE 和 RELEASE 分支中的相应 Git 提交哈希或 Subversion 修订号来进行修正：

|分支/路径 |哈希 |修订|
|---|---|---|
|stable/13/ |9515f04fe3b1 |stable/13-n255919|
|releng/13.2/ |da38eaca4a22| releng/13.2-n254626|
|releng/13.1/ |4e548c72914a| releng/13.1-n250191|
|stable/12/| |r373149|
|releng/12.4/ ||r373152|

对于 FreeBSD 13 及更高版本：

运行以下命令以查看哪些文件被特定提交修改：

```shell-session
# git show --stat <commit 哈希>
```

或访问以下 URL，将 `NNNNNN` 替换为哈希：

<URL:https://cgit.freebsd.org/src/commit/?id=NNNNNN>

要确定工作树中的提交计数（用于与上表中的 `nNNNNNN` 进行比较），运行：
```shell-session
# git rev-list --count --first-parent HEAD
```
对于 FreeBSD 12 及更早版本：

运行以下命令以查看特定修订号修改的文件，将 `NNNNNN` 替换为修订号：
```shell-session
# svn diff -cNNNNNN --summarize svn://svn.freebsd.org/base
```


或访问以下 URL，将 `NNNNNN` 替换为修订号：

<URL:https://svnweb.freebsd.org/base?view=revision&revision=NNNNNN>

**VII. 参考**

<URL:https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3107>

此安全公告的最新修订版可在以下 URL 上获取：
<URL:https://security.FreeBSD.org/advisories/FreeBSD-SA-23:06.ipv6.asc>

## FreeBSD 安全公告 FreeBSD-SA-23:08.ssh

- **主题：** 潜在的通过 ssh-agent 转发进行远程代码执行

- **类别：** 贡献
- **模块：** OpenSSH
- **发布日期：** 2023 年 8 月 1 日
- **致谢：** Qualys
- **受影响版本：** 所有受支持的 FreeBSD 版本
- **修复日期：** 
  - 2023 年 7 月 21 日 14:41:41 UTC (stable/13, 13.2-STABLE)
  - 2023 年 8 月 1 日 19:50:47 UTC (releng/13.2, 13.2-RELEASE-p2)
  - 2023 年 8 月 1 日 19:48:26 UTC (releng/13.1, 13.1-RELEASE-p9)
  - 2023 年 7 月 21 日 16:25:51 UTC (stable/12, 12.4-STABLE)
  - 2023 年 8 月 1 日 19:47:00 UTC (releng/12.4, 12.4-RELEASE-p4)
- **CVE 编号：** CVE-2023-38408

有关 FreeBSD 安全公告的一般信息，包括上述字段的描述、安全分支和以下部分，请访问<URL:https://security.FreeBSD.org/>。

**I. 背景**

ssh-agent 是用于 OpenSSH 公钥身份验证的私钥持有程序。 可以使用 ssh 的-A 选项从更远的远程主机转发到 ssh-agent。 将 ssh-agent 连接转发到的服务器可能会导致 ssh-agent 进程加载（和卸载）操作系统提供的共享库以支持添加和删除 PKCS#11 密钥。

**II. 问题描述**

服务器可能会导致 ssh-agent 加载除 PKCS#11 支持所需的共享库之外的其他共享库。 这些共享库可能会在加载和卸载（dlopen 和 dlclose）时产生副作用。

**III. 影响**

拥有访问接受转发 ssh-agent 连接的服务器的攻击者可能能够在运行 ssh-agent 的机器上执行代码。请注意，此攻击依赖于操作系统提供的库的属性。 在其他操作系统上已经证明了这一点；尚不清楚是否可以使用 FreeBSD 安装提供的库进行此攻击。

**IV. 解决方法**

避免使用 ssh-agent 转发，或使用空的 PKCS#11/FIDO 允许列表启动 ssh-agent（ssh-agent -P''），或配置一个仅包含特定提供程序库的允许列表。

**V. 解决方案**

将易受攻击的系统升级为支持的 FreeBSD STABLE 或 RELEASE/安全分支（releng），日期在修正日期之后，并重新启动使用 ssh-agent 转发的任何 ssh 会话。

执行以下操作之一：

1. 通过二进制补丁更新易受攻击的系统：

在 amd64、i386 或（在 FreeBSD 13 及更高版本上）arm64 平台上运行 RELEASE 版本的 FreeBSD 系统可以使用 freebsd-update(8) 工具进行更新：

```shell-session
# freebsd-update fetch
# freebsd-update install
```
2. 通过源代码补丁更新易受攻击的系统：

以下补丁已经验证适用于适用的 FreeBSD 发行版分支。

a) 从以下位置下载相关补丁，并使用您的 PGP 工具验证已分离的 PGP 签名。

**FreeBSD 13.2**
```shell-session
# fetch https://security.FreeBSD.org/patches/SA-23:08/ssh.13.2.patch
# fetch https://security.FreeBSD.org/patches/SA-23:08/ssh.13.2.patch.asc
# gpg --verify ssh.13.2.patch.asc
```
**FreeBSD 13.1**
```shell-session
# fetch https://security.FreeBSD.org/patches/SA-23:08/ssh.13.1.patch
# fetch https://security.FreeBSD.org/patches/SA-23:08/ssh.13.1.patch.asc
# gpg --verify ssh.13.1.patch.asc
```
**FreeBSD 12.4**
```shell-session
# fetch https://security.FreeBSD.org/patches/SA-23:08/ssh.12.4.patch
# fetch https://security.FreeBSD.org/patches/SA-23:08/ssh.12.4.patch.asc
# gpg --verify ssh.12.4.patch.asc
```
b) 应用补丁。 以 root 用户执行以下命令：
```shell-session
# cd /usr/src
# patch < /path/to/patch
```
c) 如 <URL:https://www.FreeBSD.org/handbook/makeworld.html> 中所述，重新编译您的操作系统，并重新启动使用 ssh-agent 转发的所有 ssh 会话，或重新启动系统。

**VI. 修正细节**

此问题通过以下 STABLE 和 RELEASE 中的相应 Git 提交哈希或 Subversion 修订号来进行修正：

|分支/路径| 哈希| 修订号|
 |---|---|---|
 |stable/13/  |d578a19e2cd3 | stable/13-n255848 |
 |releng/13.2/ | 20bcfc33d3f2 | releng/13.2-n254624 |
 |releng/13.1/  |3d3a1cbfd7a2 | releng/13.1-n250189 |
 |stable/12/ | | r373142 |
 |releng/12.4/  | |r373151 |

对于 FreeBSD 13 及更高版本：

运行以下命令以查看特定提交修改了哪些文件：
```shell-session
# git show --stat <提交哈希>
```
或访问以下 URL，将 `NNNNNN` 替换为哈希：

<URL:https://cgit.freebsd.org/src/commit/?id=NNNNNN>

要在工作树中确定提交计数（用于与上表中的 `nNNNNNN` 进行比较），运行：
```shell-session
# git rev-list --count --first-parent HEAD
```
对于 FreeBSD 12 及更早版本：

运行以下命令以查看特定修订修改了哪些文件，将 `NNNNNN` 替换为修订号：
```shell-session
# svn diff -cNNNNNN --summarize svn://svn.freebsd.org/base
```
或访问以下 URL，将 `NNNNNN` 替换为修订号：

<URL:https://svnweb.freebsd.org/base?view=revision&revision=NNNNNN>

**VII. 参考**

<URL:https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38408>

此安全公告的最新修订版可在以下 URL 上获取：
<URL:https://security.FreeBSD.org/advisories/FreeBSD-SA-23:08.ssh.asc>


