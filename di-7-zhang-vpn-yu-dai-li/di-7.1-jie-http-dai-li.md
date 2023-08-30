# 第 7.1 节 HTTP 代理

示例：V2ray 或 clash 开启允许局域网连接。然后按照具体配置可能如下：

首先查看使用的 shell
```shell
$ echo $SHELL
```

>**注意**
>
>**本文中的 `192.168.X.X:7890` 均非实际参数，以实际为准，复制粘贴是不会生效的！**

## HTTP_PROXY 代理

- 如果使用的是 `sh`, `bash`, `zsh`
  
**环境变量 HTTP_PROXY 一定要是大写！小写不生效！**
  
设置：
```shell
# export HTTP_PROXY=http://192.168.X.X:7890
```

取消：
```shell
# unset HTTP_PROXY
```


- 如果使用的是 `csh`

设置：
```shell
# setenv http_proxy http://192.168.X.X:7890
```

取消：
```shell
# unsetenv http_proxy
```
## Git 代理

- 如果使用的是 `sh`, `bash`, `zsh`：

设置：
```shell
# git config --global http.proxy http://192.168.X.X:7890
# git config --global https.proxy http://192.168.X.X:7890
```
取消：

```shell
# git config --global --unset http.proxy
# git config --global --unset https.proxy
```

