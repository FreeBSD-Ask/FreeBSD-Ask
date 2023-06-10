# 第5.1节 Fcitx 输入法框架

> **注意**
>
> 在 FreeBSD-14.0-Current 中可能会出现许多不可预料的奇怪的 bug（fcitx5 诊断信息英文乱码，输入法显示出奇怪的汉字，fcitx5-qt5 环境不能正常加载……），如果条件允许应该在 FreeBSD-Release 中参考使用本文。

## Fcitx 4.X

> **注意**
>
> 该教程仅在 KDE 5/csh 下测试通过。

`# pkg install zh-fcitx zh-fcitx-configtool fcitx-qt5 fcitx-m17n zh-fcitx-libpinyin`

在 `.cshrc` 和 `/etc/csh.cshrc` 中添加如下配置，此配置可以解决部分窗口 fcitx 无效的问题。

```
setenv QT4_IM_MODULE fcitx
setenv GTK_IM_MODULE fcitx
setenv QT_IM_MODULE fcitx
setenv GTK2_IM_MODULE fcitx
setenv GTK3_IM_MODULE fcitx
setenv XMODIFIERS @im=fcitx
```

在 `.cshrc` 和 `/etc/csh.cshrc` 中添加下面几行配置可以解决终端无法输入中文和无法显示中文的问题。

```
setenv LANG zh_CN.UTF-8
setenv MM_CHARSET zh_CN.UTF-8
setenv LC_CTYPE zh_CN.UTF-8
setenv LC_ALL zh_CN.UTF-8
```

自动启动：

`# cp /usr/local/share/applications/fcitx.desktop ~/.config/autostart/`

## Fcitx 5.X

fcitx 5 相比前一代，增加了对 Wayland 的支持，据说更加流畅。

`# pkg install fcitx5 fcitx5-qt5 fcitx5-qt6 fcitx5-gtk2 fcitx5-gtk3 fcitx5-gtk4 fcitx5-configtool zh-fcitx5-chinese-addons`

也可通过 ports 安装。环境变量取决于你的窗口管理器和桌面以及 shell。经测试不支持 slim，可能是配置问题。sddm 可用。

> **可选**
>
> 你还可以选择安装 rime，`#pkg install zh-fcitx5-rime zh-rime-essay`。rime 不会自动被添加到输入法，需要手动添加完成初始化（程序里找到 fcitx 配置工具，添加 rime 输入法即可），这个输入法我不知道配置文件在哪，有意者可以自行安装。而且经常切换到繁体，即使你选择了简体，BUG 比较多，原因未知。对于普通用户如果未生效，请检查自己的 shell 是否选择了对应教程进行设置。另外请将该用户加入 wheel 组。

SLIM 窗口下会提示 IBUS 找不到……疑似 bug。

自动启动：

```
# mkdir -p ~/.config/autostart/ #若使用其他用户则需要在其命令行下再执行之。
# cp /usr/local/share/applications/org.fcitx.Fcitx5.desktop ~/.config/autostart/
```

### 根据 Shell 设置环境变量

#### 如何查看修改当前 shell

先看看现在的 shell 是什么: `# echo $0`。

例：尝试将当前 shell 修改成 `csh`：

```
# chsh -s /bin/csh
```

退出当前账号，重新登录，查看 shell 是否变为 `csh`：

```
# echo $0
```

如果输出`csh`，代表配置成功。然后其余环境变量配置方法同上所述。

#### Shell 是 csh 或 tcsh

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

#### Shell 是 sh/bash/zsh

编辑或者新建 `~/.xprofile`，加入：

```
export XIM=fcitx5
export XIM_PROGRAM=fcitx5
export QT_IM_MODULE=fcitx5
export GTK_IM_MODULE=fcitx5
export XMODIFIERS="@im=fcitx5"
```

注意，需要提前在 KDE5 设置里把 KDE5 修改为简体中文。

## 故障排除

遇到问题，请先运行 `fcitx` 故障诊断，但是该输出仅对 `bash` 做了环境变量的配置。 也就是说他输出的环境变量仅适用于 `bash`、`sh`和`zsh` 等 SHELL，而不适用于 `csh`。于 `csh` 的环境变量配置需要参考上文。

如果提示 `bash` 字样且无法输出诊断信息，则需要先安装 `bash`：`# pkg install bash`

### fcitx 4.x

```
# fcitx-diagnose
```

对于 fcitx 4.x 来说，找不到 `GTK 4` 的支持是正常的。

### fcitx 5.x

```
# fcitx5-diagnose
```

对于 fcitx 5.x 来说，找不到 `fcitx qt 4` 的支持是正常的。
