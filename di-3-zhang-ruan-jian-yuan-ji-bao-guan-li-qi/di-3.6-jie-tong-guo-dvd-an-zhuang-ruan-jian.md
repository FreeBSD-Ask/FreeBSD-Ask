# 第 3.6 节 通过 DVD 安装软件

## 挂载 DVD 到 /dist 目录:

- 若直接挂载本地 ISO：

```shell-session
# mdconfig FreeBSD-13.1-RELEASE-amd64-dvd1.iso
# mkdir -p /dist
# mount -t cd9660 /dev/md0 /dist #不能直接挂载 ISO，会显示错误 block device required
```

- 若直接使用 DVD 设备（如虚拟机直接挂载 ISO 镜像）：

```shell-session
# mkdir -p /dist
# mount -t cd9660 /dev/cd0 /dist
```

> **故障排除**
>
> **/dist** 目录若改为其他则使用环境变量方法无效，因为 `packages/repos/FreeBSD_install_cdrom.conf` 写死了路径且无法修改。

### 使用环境变量【可选】

#### 安装软件

测试安装：

```shell-session
# env REPOS_DIR=/dist/packages/repos pkg install xorg
```

要列出看 DVD 中的可用软件：

```shell-session
# env REPOS_DIR=/dist/packages/repos pkg rquery "%n"
```

### 换源为 DVD【可选】

#### 创建源

```shell-session
# cp /dist/packages/repos/FreeBSD_install_cdrom.conf /etc/pkg/
```

测试安装：

```shell-session
# pkg install xorg
```

##

参考资料：

- [Product Details](https://www.freebsdmall.com/cgi-bin/fm/bsddvd10.1)
- [HOWTO: Install binary package without internet acces](https://forums.freebsd.org/threads/howto-install-binary-package-without-internet-acces.60723/)
