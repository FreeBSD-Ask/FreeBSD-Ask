# 第二节 开启 DTrace

## FreeBSD 11 以后

`# kldload dtraceall`

即可开启

## 对于 FreeBSD 9/10

FreeBSD 内核默认没有开启 DTrace 这项功能。要开启本功能必须加入参数重新编译内核。

建议先阅读第二十章 内核。

编辑内核配置文件加入：



```
options         KDTRACE_HOOKS
options         DDB_CTF
makeoptions	DEBUG=-g
makeoptions	WITH_CTF=1
```

如果是64 位操作系统：



```
options         KDTRACE_FRAME
```

