

## 以太网卡设置

![](../.gitbook/assets/ins17.png)

`请选择一个网络接口进行配置`

即选择网卡。按 **方向键** 可切换，按 **回车键** 可选定。

![](../.gitbook/assets/ins18.png)

`你希望为此接口配置 IPv4 吗？`

配置 IPv4。按 **回车键** 可选定。

![](../.gitbook/assets/ins19.png)

`你希望使用 DHCP 配置此接口吗？`

配置使用 DHCP。按 **回车键** 可选定。

![](../.gitbook/assets/ins20.png)

`你希望为此接口配置 IPv6 吗？`

配置 IPv6。因本教程未使用 IPv6，故选 `No`，按 **回车键** 可选定。如有需要可自行配置 IPv6。

![](../.gitbook/assets/ins21.png)

`配置解析器`

一般保持 DHCP 获取的 DNS 即可，也可以使用其他 DNS。此处使用了阿里 DNS `223.5.5.5`。按 **方向键** 可切换，按 **回车键** 可选定。

## 无线网卡/ WiFi 设置

>**注意**
>
>博通网卡请安装后再参照 WiFi 章节进行处理。

![](../.gitbook/assets/ins-w1.png)

`请选择网络接口进行配置`



![](../.gitbook/assets/ins-w2.png)

`更改地区/国家（FCC/US）？`

修改 WiFi 区域码，按回车确认。

![](../.gitbook/assets/ins-w3.png)

`选择你的区域码`

我们应该选 `NONE ROW`。


![](../.gitbook/assets/ins-w4.png)

`选择你的地区`

选择区域：

![](../.gitbook/assets/ins-w5.png)

`等待 5 秒钟，正在扫描无线网络……`

扫描。

>**技巧**
>
>只要能识别出来网卡，肯定就是能用的，但是在安装系统的时候不一定能够正确搜索出 WiFi。请你置空，安装完成后重启到新系统，再参照 WiFi 章节进行处理。

在列表中找寻你的 WiFi，找不到的话请你换下路由器的信道。

![](../.gitbook/assets/ins-w6.png)

`选择你要链接的无线网络`

输入 WiFi 密码即可链接：

![](../.gitbook/assets/ins-w7.png)

![](../.gitbook/assets/ins18.png)

`你想要为此接口配置 IPv4 吗`

配置 IPv4。按 **回车键** 可选定。

![](../.gitbook/assets/ins19.png)

`你希望使用 DHCP 配置此接口吗？`

配置使用 DHCP。按 **回车键** 可选定。

![](../.gitbook/assets/ins20.png)

`你希望为此接口配置 IPv6 吗？`

配置 IPv6。因本教程未使用 IPv6，故选 `No`，按 **回车键** 可选定。如有需要可自行配置 IPv6。

![](../.gitbook/assets/ins21.png)

`配置解析器`

一般保持 DHCP 获取的 DNS 即可，也可以使用其他 DNS。此处使用了阿里 DNS `223.5.5.5`。按 **方向键** 可切换，按 **回车键** 可选定。

### 参考文献

- [Regulatory Domain Support](https://wiki.freebsd.org/WiFi/RegulatoryDomainSupport)
- [regdomain.xml --	802.11 wireless	regulatory definitions](https://man.freebsd.org/cgi/man.cgi?query=regdomain&sektion=5)，对应编码请参考系统中的 `/etc/regdomain.xml` 文件。
- [阿里公共 DNS](https://www.alidns.com/)
