# 第5.5节 安装 金山 WPS

> 请勿使用 ports 中的金山 WPS，因为无人更新。推荐自行构建兼容层安装使用。

## 故障排除

* KDE5 下 WPS 可能会无法启动。

因为 WPS 启动文件调用的是 bash shell。所以安装 bash 后就可以正常启动了：

```
# pkg install bash
