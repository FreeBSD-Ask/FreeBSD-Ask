# 第5.6节 安装 金山 WPS

> 注意，该 port 的维护者已经放弃维护，不再更新。请谨慎使用。可能需要新的志愿者对 WPS 进行维护。

金山 WPS 提供两个版本一是国际版，另一个是国内版本。**国际版无中文支持。**

二者的使用都需要先安装 Linux 兼容层、字体问题见本书其余章节。

## 国内版

linux-wps-office-zh\_CN

安装，目前只能通过 ports 安装：

```
# cd /usr/ports/chinese/linux-wps-office-zh_CN/ && make install clean #如要默认请添加 BATCH=yes
```

## 国际版

linux-wps-office

请注意：国际版的服务器在境外，境内下载速度非常慢，请参考 第七章 第一节

安装，目前只能通过 ports 安装：

```
# cd /usr/ports/editors/linux-wps-office/ && make install clean #如要默认请添加 BATCH=yes
```

## 故障排除

* KDE5 下 WPS 可能会无法启动。

因为 WPS 启动文件调用的是 bash shell。所以安装 bash 后就可以正常启动了：

```
# pkg install bash
```

* fcitx 5 在 WPS 下无法使用

这是 WPS 的一个已知 bug：

参考：

[https://bbs.archlinuxcn.org/viewtopic.php?id=10984](https://bbs.archlinuxcn.org/viewtopic.php?id=10984)

[https://github.com/fcitx/fcitx5/issues/83](https://github.com/fcitx/fcitx5/issues/83)

[https://plumz.me/archives/12331/](https://plumz.me/archives/12331/)

* 点击设置会闪退

Linux 版本同样如此。
