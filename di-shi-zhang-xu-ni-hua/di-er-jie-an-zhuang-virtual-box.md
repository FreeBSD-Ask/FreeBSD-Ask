# 第二节 安装 Virtual Box

pkg 安装安装的 Virtual Box 会出现若干问题，比如无法加载 `vboxdrv` 模块等。

因此建议使用 ports 进行安装：

```
# cd /usr/ports/emulators/virtualbox-ose 
# make BATCH=yes install clean
```
