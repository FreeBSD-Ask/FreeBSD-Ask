# 8.8 制作 FreeBSD 二进制包（pkg）

本节介绍如何自行制作 pkg 二进制包。此前各节讨论的都是从软件源安装现成的包，自制包则适用于两类场景：把自行编译的软件分发到其他机器，以及把上游只提供 Linux 版本或源码的软件在 FreeBSD 上构建后打包分发。

## pkg 包的结构与本地数据库

pkg 包是一个经过压缩的 tar 归档，扩展名为 `.pkg`，默认使用 zstd 压缩（`pkg create` 也支持 txz、tbz、tgz 以及不压缩的 tar）。可以直接用 `tar` 查看其内容：

```sh
$ tar --zstd -tf hello-1.0.pkg
+COMPACT_MANIFEST
+MANIFEST
/usr/local/bin/hello
```

`+MANIFEST` 是 JSON 格式的包元数据，记录包名、版本、依赖、安装前缀等信息；`+COMPACT_MANIFEST` 是同一份元数据的精简形式。其余条目就是包所携带的文件，其路径为安装后的绝对路径。

需要注意 pkg(8) 的本地数据库位置。它是一个 SQLite 数据库文件 **/var/db/pkg/local.sqlite**，并不存在逐包的 `/var/db/pkg/<包名>-<版本>/+MANIFEST` 目录。因此读取已安装包的元数据应使用 `pkg query`，而不是到数据库目录下翻找文件：

```sh
# pkg query -e '%n = nginx' '%n %v %o'
nginx 1.28.0_1,3 www/nginx
```

`pkg query` 的第二个参数是格式串，`%n`、`%v`、`%o` 依次表示包名、版本与来源（origin，即 Ports 中的 `分类/目录` 形式）。完整的格式说明符列表见 pkg-query(8)。

> **技巧**
>
> 本节示例除安装与卸载包需要 `root` 权限外，其余步骤均可在普通用户下完成。

## 制作一个 pkg 包

制作过程分三步：准备一个与安装后目录结构一致的暂存目录，编写元数据，然后调用 `pkg create`。

下面以制作一个安装 `/usr/local/bin/hello` 的包为例。先建立暂存目录，其内部结构与安装后的最终位置一致：

```sh
$ mkdir -p ~/hello-pkg/stage/usr/local/bin
$ mkdir -p ~/hello-pkg/meta
```

写入要打包的文件：

```sh
$ cat > ~/hello-pkg/stage/usr/local/bin/hello << 'EOF'
#!/bin/sh
echo "hello from a pkg package"
EOF
$ chmod 755 ~/hello-pkg/stage/usr/local/bin/hello
```

在 `meta` 目录中编写 `+MANIFEST`：

```json
{
  "name": "hello",
  "version": "1.0",
  "origin": "misc/hello",
  "comment": "A minimal example package",
  "desc": "A minimal example package used to demonstrate pkg create.",
  "maintainer": "you@example.com",
  "www": "https://example.com/",
  "prefix": "/usr/local",
  "deps": {}
}
```

字段含义见 pkg-create(8)。`name` 与 `version` 共同决定包的文件名；`origin` 沿用 Ports 的 `分类/目录` 形式；`comment` 是一行简介，`desc` 是较长的描述；`prefix` 是安装前缀，常规取值为 **/usr/local**。

`pkg create` 只打包 plist 中列出的文件，因此还需要生成一份 plist。plist 就是文件路径的列表，以 `/` 开头的路径按绝对路径处理，否则视为相对于 `prefix`。注意符号链接也要列入：`-type f` 只匹配普通文件，若暂存目录中含有符号链接，需同时匹配 `-type l`，否则这些链接不会被打包。

```sh
$ cd ~/hello-pkg
$ find stage \( -type f -o -type l \) | sed 's|^stage||' > meta/files.plist
$ cat meta/files.plist
/usr/local/bin/hello
```

随后执行 `pkg create`。`-r` 指定暂存目录，`-p` 指定 plist，`-m` 指定元数据目录，`-o` 指定输出目录：

```sh
$ pkg create -r stage -p meta/files.plist -m meta -o out
$ ls out
hello-1.0.pkg
```

> **技巧**
>
> 若软件是通过 Ports 安装的，可以直接用 `pkg create <包名>` 从已安装的包重建出二进制包，例如 `pkg create nginx`，无需再准备暂存目录与元数据。

## 在包中声明依赖

`+MANIFEST` 的 `deps` 字段用于声明运行期依赖，取值是一个以依赖包名为键的关联数组，每项记录其来源与版本：

```json
  "deps": {
    "xdg-utils": {
      "origin": "devel/xdg-utils",
      "version": "1.2.1"
    }
  }
```

`deps` 中必须包含程序在运行期真正需要的每一个包。判断依据是它链接了哪些共享库、这些库由哪个包提供——`pkg info -d` 在列出直接依赖之后，会接着列出所需的共享库及其提供者：

```sh
# pkg info -d curl
curl-8.22.0:
	brotli-1.2.0,1
	libidn2-2.3.8
	libnghttp2-1.69.0
	……
	brotli-1.2.0,1 (libbrotlidec.so.1)
	FreeBSD-clibs-15.1 (libc.so.7)
	libnghttp2-1.69.0 (libnghttp2.so.14)
	……
```

括号中是共享库的文件名，其前面的包就是该库的提供者。

若要沿用一个已安装包在构建时所链接的那组依赖，可以直接从它的元数据中读出这份依赖表：

```sh
# pkg query -e '%n = curl' '%dn %do %dv'
brotli archivers/brotli 1.2.0,1
libidn2 dns/libidn2 2.3.8
libnghttp2 www/libnghttp2 1.69.0
……
```

`%dn`、`%do`、`%dv` 分别表示依赖包的包名、来源与版本，正好对应 `deps` 所需的三个字段。需要注意，查询得到的是被查询包自身的依赖，其中并不包含被查询包自己；若程序依赖的正是被查询包提供的文件（例如链接了它安装的共享库），必须把该包本身也一并写入 `deps`。

把上文 `hello` 的 `+MANIFEST` 中的 `deps` 改为声明一个依赖，重新执行 `pkg create` 并安装后，即可看到效果：

```sh
# pkg info -d hello
hello-1.0:
	xdg-utils-1.2.1
# pkg check -d hello
Checking hello: . done
```

## 安装与卸载脚本

元数据目录中还可以放置安装与卸载脚本，pkg(8) 会在相应阶段执行它们（见 pkg-script(5)）。文件名与执行时机如下：

| 文件名 | 执行时机 |
| ------ | -------- |
| `+PRE_INSTALL` | 安装文件之前 |
| `+POST_INSTALL` | 安装文件之后 |
| `+PRE_DEINSTALL` | 删除文件之前 |
| `+POST_DEINSTALL` | 删除文件之后 |

脚本需要可执行权限。桌面应用的包常用 `+POST_INSTALL` 刷新桌面数据库与图标缓存：

```sh
#!/bin/sh
# 无桌面环境的系统上这两个工具可能不存在，任何一种情况都不应让安装失败
if command -v update-desktop-database >/dev/null 2>&1; then
    update-desktop-database -q /usr/local/share/applications || true
fi
if command -v gtk-update-icon-cache >/dev/null 2>&1; then
    gtk-update-icon-cache -q -t -f /usr/local/share/icons/hicolor || true
fi
```

## 安装、校验与卸载

制作出的包可以直接用 `pkg install` 安装，用 `pkg delete` 卸载，二者都需要 `root` 权限：

```sh
# pkg install ./out/hello-1.0.pkg
# hello
hello from a pkg package
# pkg delete -y hello
```

若只想查看包的内容而不安装，可以用 `pkg info -F` 读取包文件的元数据，或用 `tar` 直接查看：

```sh
$ pkg info -F out/hello-1.0.pkg
hello-1.0
Name           : hello
Version        : 1.0
Origin         : misc/hello
Prefix         : /usr/local
……
$ tar --zstd -tvf out/hello-1.0.pkg
```

## 在 GitHub Actions 中为 FreeBSD 构建

GitHub 提供的托管运行器没有 FreeBSD 系统，无法直接在其中构建 FreeBSD 包。vmactions/freebsd-vm 这个 Action 会在 Ubuntu 运行器上以 QEMU 启动一台 FreeBSD 虚拟机，把工作区同步进去，并在其中执行指定的命令：

```yaml
name: Build FreeBSD package

on: [push]

permissions:
  contents: read

jobs:
  package:
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@v6
        with:
          persist-credentials: false

      - name: 在 FreeBSD 虚拟机中构建
        uses: vmactions/freebsd-vm@v1
        with:
          release: '15.1'
          arch: x86_64
          mem: 8192
          cpu: 4
          envs: 'VERSION'
          run: |
            set -eu
            sh ./build-freebsd.sh
        env:
          VERSION: '1.0'

      - uses: actions/upload-artifact@v7
        with:
          name: freebsd-pkg
          path: out/*.pkg
```

其中 `release` 指定虚拟机的 FreeBSD 版本，`envs` 列出需要传入虚拟机的环境变量，`run` 中的命令在虚拟机内执行。虚拟机是每次运行临时启动的，构建脚本应当自行完成依赖安装（`pkg install`）等准备工作。

需要注意凭据问题。`actions/checkout` 默认会把仓库凭据写入工作区 `.git` 的配置中，而虚拟机动作会把整个工作区（含 `.git`）同步进虚拟机；一旦构建脚本或其调用的代码被篡改，虚拟机内即可读出该凭据。因此上面用 `persist-credentials: false` 关闭凭据写入，并用 `permissions` 把工作流令牌限制为只读。

## 移植与打包时的注意事项

### 构建脚本中的命令被同名程序遮蔽

若构建树中某个目录（例如 Node.js 项目的 `node_modules/.bin`）排在 `PATH` 前面，且其中存在与系统命令同名的可执行文件，脚本调用的就不再是系统命令。典型例子是 Node.js 生态中的打包工具 `pkg`，它与 FreeBSD 的包管理器 pkg(8) 同名。此时应使用绝对路径调用系统工具：

```sh
# /usr/sbin/pkg query -e '%n = nginx' '%n %v'
```

### 桌面条目与图标的安装位置

打包桌面应用时，桌面条目应安装到 **/usr/local/share/applications/<名称>.desktop**，图标应安装到 **/usr/local/share/icons/hicolor/<尺寸>x<尺寸>/apps/**，其中 `<尺寸>` 为图标的像素边长（如 48x48、256x256）。安装到这两处之外的位置，桌面环境不会识别。

### 上游源码中的平台判断

从源码构建时，上游代码可能把平台条件写死为 Linux，例如用 `#ifdef __linux__` 圈定某段实现。这类代码在 FreeBSD 上会走到另一分支，导致编译失败或行为异常，需要在移植时把 FreeBSD 一并纳入条件。此外，若上游不发布 FreeBSD 的预编译产物，本地原生模块需要从源码编译，构建环境须具备相应的编译工具链。

## 参考文献

- FreeBSD Project. pkg-create -- a utility for creating software package distributions[EB/OL]. [2026-10-18]. <https://man.freebsd.org/cgi/man.cgi?query=pkg-create&sektion=8>. 本文中 `pkg create` 的参数、`+MANIFEST` 字段与 plist 格式均以此为准。
- FreeBSD Project. pkg-query -- query information from the local package database[EB/OL]. [2026-10-18]. <https://man.freebsd.org/cgi/man.cgi?query=pkg-query&sektion=8>. `pkg query` 的格式说明符列表。
- FreeBSD Project. pkg -- package manager[EB/OL]. [2026-10-18]. <https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=8>. 本地包数据库位于 SQLite 数据库文件 /var/db/pkg/local.sqlite。
- FreeBSD Project. pkg-script -- shell scripts that are run by pkg(8)[EB/OL]. [2026-10-18]. <https://man.freebsd.org/cgi/man.cgi?query=pkg-script&sektion=5>. 安装与卸载脚本的执行阶段。
- vmactions. freebsd-vm[EB/OL]. [2026-10-18]. <https://github.com/vmactions/freebsd-vm>. 在 GitHub Actions 中启动 FreeBSD 虚拟机。

## 课后习题

1. 制作一个包，使其在安装与卸载时分别输出一条消息，并用 `pkg info -F` 检查包内是否包含这些脚本。
2. 用 `pkg query` 列出某个已安装包的完整依赖，并说明其输出与 `+MANIFEST` 中 `deps` 字段的对应关系。
3. 为某个自行编译的软件制作一个 pkg 包，并在另一台 FreeBSD 上用 `pkg install` 安装验证。
