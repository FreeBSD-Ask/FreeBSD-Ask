# 第一节 Fcitx 输入法框架

## FreeBSD Fcitx 输入法框架设置（4.X）

#### 注意：该教程仅在KDE5 下测试通过。 <a href="zhu-yi-gai-jiao-cheng-jin-zai-kde5-xia-ce-shi-tong-guo" id="zhu-yi-gai-jiao-cheng-jin-zai-kde5-xia-ce-shi-tong-guo"></a>

在.cshrc 和/etc/csh.cshrc 中进行如下配置，此配置可以解决部分窗口fcitx 无效的问题。

```
setenv QT4_IM_MODULE fcitx
setenv GTK_IM_MODULE fcitx
setenv QT_IM_MODULE fcitx
setenv GTK2_IM_MODULE fcitx
setenv GTK3_IM_MODULE fcitx
setenv XMODIFIERS @im=fcitx
```

在.cshrc 和/etc/csh.cshrc 中进行下面两行配置可以解决终端无法输入中文和无法显示中文的问题。

```
setenv LANG zh_CN.UTF-8
setenv MM_CHARSET zh_CN.UTF-8
```

接Fcitx 输入法补充：

```
#要想终端不乱码还需要添加：
setenv LANG zh_CN.UTF-8
setenv LC_CTYPE zh_CN.UTF-8
setenv LC_ALL zh_CN.UTF-8
```

## Fcitx5.X

#### 注意：该教程仅在KDE5 下测试通过。 <a href="zhu-yi-gai-jiao-cheng-jin-zai-kde5-xia-ce-shi-tong-guo" id="zhu-yi-gai-jiao-cheng-jin-zai-kde5-xia-ce-shi-tong-guo"></a>

textproc/fcitx5

textproc/fcitx5-qt

textproc/fcitx5-gtk

textproc/fcitx5-configtool

chinese/fcitx5-rime

…

　　可通过 ports 安装。环境变量取决于你的窗口管理器和桌面以及 shell 。经测试不支持 slim，可能是配置问题。sddm 可用。

　　自动启动：

`# cp /usr/local/share/applications/fcitx.desktop ~/.config/autostart/`

　　在 .cshrc 和 /etc/csh.cshrc 中进行如下配置，此配置可以解决部分窗口 fcitx 无效以及无法输入显示中文的问题。

```
setenv QT4_IM_MODULE fcitx
setenv GTK_IM_MODULE fcitx
setenv QT_IM_MODULE fcitx
setenv GTK2_IM_MODULE fcitx
setenv GTK3_IM_MODULE fcitx
setenv XMODIFIERS @im=fcitx
setenv LANG zh_CN.UTF-8
setenv MM_CHARSET zh_CN.UTF-8
```

　　在 root 用户下 rime 不会自动被添加到输入法，需要手动添加完成初始化！对于普通用户如果未生效，请检查自己的 shell，应该是 csh，如果不是请将该用户加入 wheel 组。对于其他 shell 请自行更正为对应 shell 的环境变量。

　　SLIM 窗口下会提示IBUS 找不到……疑似bug。
