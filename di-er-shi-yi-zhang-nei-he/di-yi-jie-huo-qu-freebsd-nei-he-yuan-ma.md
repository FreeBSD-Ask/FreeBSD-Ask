# 第一节 获取 FreeBSD 内核源码

FreeBSD 项目在 2021 年从 SVN 全面迁移到了 Git，即

https://git.freebsd.org

所以获取源代码的方式也产生了变化。

## 从 Git 获取源代码

```
# pkg install -y gitup 
# gitup release # 具体版本需要参考当前 gitup 配置 https://github.com/johnmehr/gitup/blob/main/gitup.conf
# gitup current # 获取 current 源代码
```

## 从压缩包获取源代码(推荐)

该方法比较简单快捷。

以 FreeBSD 13.0 为例：

```
# fetch https://download.freebsd.org/ftp/releases/amd64/13.0-RELEASE/src.txz
# tar xvzfp src.txz  -C /
```
>如果速度慢可以切换到 <https://mirror.bjtu.edu.cn/freebsd/releases/amd64/13.0-RELEASE/lib32.txz>
