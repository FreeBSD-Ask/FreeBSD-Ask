# 第 7.2 节 V2ray

## 安装 v2ray

执行命令：

```shell-session
# pkg install v2ray
```

也可安装 xray-core：

```shell-session
# pkg install xray-core
```

这两个代理配置基本相同，配置文档可以在各自的官方文档找到，xray 完全可以参考 v2ray 的配置方法。

## 启动软件

如果事先有代理客户端可以把客户端节点的配置导出来，复制到 FreeBSD，假设导出的文件名为 `config.json` 然后执行：

```shell-session
$ v2ray -c config.json
```

如果用 xray-core，可执行：

```shell-session
$ xray -c config.json
```

这个时候软件应该启动成功了。

## 配置软件代理

这个时候可打开`config.json`,找到对应的`inbounds`属性，`inbounds`是一个数组，里面每个元素代表了入站接口配置，有地址和端口号，代理方式。在需要代理的软件内部设置成这里对应的地址和端口号。

比如其中一个入站接口`protocol`是 `http`，`listen` 是`127.0.0.1`, `port`是`10809`，假如这里需要火狐浏览器走代理，可以在浏览器设置里找到，网络-代理服务器，设置 http 代理地址就设置为`127.0.0.1`,端口为`10809`。同理 socks 代理也可以参考此方法设置。

大部分软件代理设置方式不同。比较混乱，对于桌面软件需要自行设置对应的代理服务器。终端命令，如果需要走代理就比较简单了。大部分终端命令，都会寻找`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY` 这三个环境变量，根据这三个环境变量的值设置对应代理。

下面的命令适用于 sh、bash、zsh：

```shell-session
$ export HTTP_PROXY="http://127.0.0.1:10809" #设置 http 代理
$ export HTTPS_PROXY="http://127.0.0.1:10809"
$ export ALL_PROXY="socks5://127.0.0.1:10808" #设置 socks 代理
```

设置完成后，在火狐浏览器中浏览网页，观察 v2ray 输出的日志，就可以看到浏览器流量走了代理。终端命令也走了代理，但是一些命令根据环境变量设置代理，请自行查找对应软件的设置方法。

## 代理分流

有些网址是不需要走代理服务器的，比如境内的网站，本地网站之类的。这个需要对流量做一个分流，一部分流量需要代理，一部分流量需要走直连等方式。

打开 config.json，找到对应的 routing 属性，下面有个 rules 子属性，这里面就用来配置 v2ray 的流量分流方式。rules 里面可以配置不同的规则，每个规则有个 ip 属性，或者 domain 属性。代理的流量，是有网址，和 ip 的，如果 ip 或者网址匹配了其中一个规则，v2ray 会根据 outboundTag 属性，把流量转发到对应的 outbounds 位置，比如 outbonds 中，有 tag 为 proxy（代理）, direct（直连）, block。所以就可以把想要分流的网址 ip 写到对应的规则里就行了。这里可参考对应的 v2ray 文档。实际上在 v2ray 客户端上导出配置文件时，也默认导出了对应的分流规则。

v2ray 也事先给了`geosite.dat`、`geoip.dat`,两个资源文件，`geosite.dat`里面分类保存而来各个网址，`geoip.dat`分类保存了各个 ip。资源文件路径，可以通过 `V2RAY_LOCATION_ASSET` 环境变量设置，v2ray 可以自动查找路径下的`geosite.dat`和`geosite.ip`文件。对于 xray 是使用这个`XRAY_LOCATION_ASSET`环境变量设置资源路径。

比如直连规则下面配置可设置 geosite 中 cn 网址直连：

```shell-session
      {
        "domain": [
          "geosite:cn"
        ],
        "outboundTag": "direct",
        "type": "field"
      },
```

v2ray 社区给的 cn 网址直连网址不太全，分类也比较少，可自行在 github 上找社区整理的 geosite, geoip 文件，里面也详细的说明了白名单配置模式，黑名单配置模式。
