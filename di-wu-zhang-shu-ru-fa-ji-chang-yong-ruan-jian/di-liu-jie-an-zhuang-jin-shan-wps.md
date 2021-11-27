# 第六节 安装 金山 WPS

金山 WPS 提供两个版本一是国际版，一是国内版本。国际版无中文支持。

二者的使用都需要先安装 Linux 兼容层，见[ 第六节](di-wu-jie-linux-jian-rong-ceng.md)。字体问题见 [第八节](di-ba-jie-geng-huan-zi-ti.md)

## 1、国内版&#x20;

linux-wps-office-zh_CN

安装，目前只能通过 ports 安装：

```
# cd /usr/ports/chinese/linux-wps-office-zh_CN/ && make install clean #如要默认请添加 BATCH=yes
```


## 2、国际版

linux-wps-office

请注意：国际版的服务器在境外，境内下载速度非常慢，请参考 [第七章 第一节](../di-qi-zhang-vpn-yu-dai-li/di-yi-jie-http-dai-li.md)

安装，目前只能通过 ports 安装：

```
# cd /usr/ports/editors/linux-wps-office/ && make install clean #如要默认请添加 BATCH=yes
```
