# 第一节 安装与配置

## 中文化


`/etc/csh.cshrc`中添加如下内容:
```
setenv LANG "zh_CN.UTF-8"
```

在`/etc/profile`文件中添加:

```
export LANG=zh_CN.UTF-8
export LC_ALL="en_US.ISO8859-1"
export LANG="en_US.ISO8859-1"
export LC_CTYPE="en_US.ISO8859-1"
export LANG=zh_CN.eucCN
```
