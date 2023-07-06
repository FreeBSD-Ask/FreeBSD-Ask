# 第5.5节 安装 金山 WPS

> 请勿使用 ports 中的金山 WPS，因为无人更新。推荐自行构建兼容层安装使用。

## 基于 ArchLinux 兼容层

```
# fetch http://book.bsdcn.org/arch.sh #下载脚本构建兼容层
# sh arch.sh #运行脚本
# chroot /compat/arch/ /bin/bash #进入 Arch兼容层
# passwd #为 Arch 的 root 设置一个密码
# su test # 此时位于 Arch 兼容层！切换到普通用户才能使用 aur，脚本已经创建过该用户了！
$ yay -S linuxqq # 此时位于 Arch 兼容层！此时用户为 test
# exit # 此时位于 Arch 兼容层！此时用户恢复为 root
```

## 故障排除

* KDE5 下 WPS 可能会无法启动。

因为 WPS 启动文件调用的是 bash shell。所以安装 bash 后就可以正常启动了：

```
# pkg install bash
