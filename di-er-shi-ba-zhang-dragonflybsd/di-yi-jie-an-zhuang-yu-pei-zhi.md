# 第一节 安装与配置

## 换源

```
# ee /usr/local/etc/pkg/repos/df-latest.conf
```

找到国内源，把`no`改成`yes`，把之前的源改为`no`。

## 中文化


`/etc/csh.cshrc`中添加:

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

## i915kms 显卡支持

```
# kldload drm
```
