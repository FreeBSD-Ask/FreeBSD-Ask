# 第二节 Ibus 输入法框架

#### 注意：该教程仅在XFCE 桌面下测试通过。不适用于KDE5。
　　ibus 输入法框架配置`.xinitrc`中增加

```
XIM=ibus;export XIM
GTK_IM_MODULE=ibus;export GTK_IM_MODULE
QT_IM_MODULE=xim; export QT_IM_MODULE
XMODIFIERS='@im=ibus'; export XMODIFIERS
XIM_PROGRAM="ibus-daemon"; export XIM_PROGRAM
XIM_ARGS="–daemonize –xim"; export XIM_ARGS
```

　　`.cshrc` 中增加

```
setenv LANG zh_CN.UTF-8
setenv LC_CTYPE zh_CN.UTF-8
setenv LC_ALL zh_CN.UTF-8
setenv XMODIFIERS @im=ibus
```

　　`.profile` 中添加
`export LC_ALL=zh_CN.UTF-8`
