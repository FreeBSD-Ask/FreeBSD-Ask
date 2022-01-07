# 第一节 Fcitx 输入法框架

fcitx 5 相比前一代，增加了对 Wayland 的支持，据说更加流畅。

#### 注意，在 FreeBSD-14.0-Current 中会出现许多不可预料的奇怪的 bug（fcitx5 诊断信息英文乱码，输入法显示出奇怪的汉字，Fcitx5-qt5 环境不能正常加载……），如果条件允许应该在 FreeBSD-Release 中参考使用本文。

## FreeBSD 4.X

#### 注意：该教程仅在 KDE 5 下测试通过。

`# pkg install zh-fcitx zh-fcitx-configtool fcitx-qt5 fcitx-m17n zh-fcitx-libpinyin`

在`.cshrc` 和`/etc/csh.cshrc` 中添加如下配置，此配置可以解决部分窗口 fcitx 无效的问题。

```
setenv QT4_IM_MODULE fcitx
setenv GTK_IM_MODULE fcitx
setenv QT_IM_MODULE fcitx
setenv GTK2_IM_MODULE fcitx
setenv GTK3_IM_MODULE fcitx
setenv XMODIFIERS @im=fcitx
```

在`.cshrc`和`/etc/csh.cshrc` 中添加下面两行配置可以解决终端无法输入中文和无法显示中文的问题。

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

## Fcitx 5.X

#### 注意：该教程仅在 KDE 5 下测试通过。

`# pkg install fcitx5 fcitx5-qt fcitx5-gtk fcitx5-configtool zh-fcitx5-rime zh-rime-essay zh-fcitx5-chinese-addons`

　　也可通过 ports 安装。环境变量取决于你的窗口管理器和桌面以及 shell 。经测试不支持 slim，可能是配置问题。sddm 可用。

　　自动启动：

`# cp /usr/local/share/applications/org.fcitx.Fcitx5.desktop ~/.config/autostart/`

　　在 `.cshrc` 和 `/etc/csh.cshrc` 中进行如下配置，此配置可以解决部分窗口 fcitx 无效以及无法输入显示中文的问题。

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

　　在 root 用户下 rime 不会自动被添加到输入法，需要手动添加完成初始化（程序里找到 fcitx 配置工具，添加 rime 输入法即可）！对于普通用户如果未生效，请检查自己的 shell，应该是 csh，如果不是请将该用户加入 wheel 组。对于其他 shell 请自行更正为对应 shell 的环境变量。

　　SLIM 窗口下会提示 IBUS 找不到……疑似bug。
  
  ## 普通用户设置
  
  普通用户的默认 shell 一般不是 `csh`，为了方便配置，需要把默认 shell 改成 csh。然后其余配置方法同上所述。
  
  先看看现在是什么 shell:
  ```
  # echo $0
  ```

如果输出不是`csh`，尝试修改成`csh`：

```
# chsh -s /bin/csh
```

退出当前账号，重新登录，查看 shell 是否变为 `csh`：

  ```
  # echo $0
  ```
  
  如果输出`csh`，代表配置成功。然后其余环境变量配置方法同上所述。
  
  #### 提示：如果不想使用 csh，把 `setenv`等环境变量改为`export`形式亦可。
