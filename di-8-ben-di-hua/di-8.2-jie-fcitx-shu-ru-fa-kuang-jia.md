# 8.2 Fcitx 输入法框架

输入法框架和输入法本身是不同的概念，切不可混淆。输入法依赖输入法框架。即使在 Windows 上也是如此： [TSF 管理器](https://learn.microsoft.com/zh-cn/windows/win32/tsf/text-services-framework)。

fcitx 是“小企鹅输入法”，其英文名称为“A flexible input method framework（一款灵活的输入法框架）”。关于其英文命名来源，请参见 [历史](https://fcitx-im.org/wiki/History/zh-cn)。

>**技巧**
>
>视频教程见 [006-FreeBSD14.2 安装 fcitx5 及其输入法](https://www.bilibili.com/video/BV13ji2YLE3m)


> **注意**
>
> 在 FreeBSD-CURRENT 中可能会出现许多不可预料的怪异 bug：fcitx5 诊断信息英文乱码，输入法显示出奇怪的汉字，fcitx5-qt5 环境不能正常加载……

## 安装 Fcitx5

- 使用 pkg 安装：

```sh
# pkg install fcitx5 fcitx5-qt5 fcitx5-qt6 fcitx5-gtk2 fcitx5-gtk3 fcitx5-gtk4 fcitx5-configtool-qt5 fcitx5-configtool-qt6 zh-fcitx5-chinese-addons
```

- 或者使用 Ports 安装：

```
# cd /usr/ports/textproc/fcitx5/ && make install clean # 主程序
# cd /usr/ports/textproc/fcitx5-qt/ && make install clean  # 同时包含 QT 5 和 QT 6
# cd /usr/ports/textproc/fcitx5-gtk/ && make install clean # 同时包含 gtk 2、3、4
# cd /usr/ports/textproc/fcitx5-configtool/ && make install clean # fcitx5 的图形配置工具。同时包含 QT 5 和 QT 6
# cd /usr/ports/chinese/fcitx5-chinese-addons/ && make install clean # 输入法
```


经测试，在 SLiM 窗口下可能会提示找不到 IBus，这可能是一个 bug，也可能是配置问题。

### Fcitx 5.X 开启自启

```sh
$ mkdir -p ~/.config/autostart/ # 创建自启动路径。如果使用其他用户，需要在该用户的命令行下执行
$ cp /usr/local/share/applications/org.fcitx.Fcitx5.desktop ~/.config/autostart/  # 设置 Fcitx 5 开启启动
```

## 配置 Fcitx 环境变量

### X11

根据所使用的桌面管理器及 shell，选择适合的方式进行配置：

- 登录管理器配置路径

1. SDDM、LightDM、GDM 都可以在 `~/.xprofile` 中写入 A 组配置
2. LightDM、GDM 可以在 `~/.profile` 中写入 A 组配置
3. SDDM 可以在用户登录 shell 的配置文件中写入配置

- Shell 配置路径

1. sh: `~/.profile` 写入 A 组配置
2. bash: `~/.bash_profile` 或 `~/.profile` 写入 A 组配置
3. zsh: `~/.zprofile` 写入 A 组配置
4. csh: `~/.cshrc` 写入 B 组配置

>**注意**
>
>如果登录桌面的用户账户不是 root，则不能使用 root 身份进行设置：必须切换到该用户，并在不使用 sudo 的情况下进行配置。

- A 组（sh/bash/zsh）

```ini
export LANG=zh_CN.UTF-8            # 设置系统语言为中文
export LANGUAGE=zh_CN.UTF-8       # 设置优先语言为中文
export LC_ALL=zh_CN.UTF-8         # 设置所有本地化环境变量为中文
export XMODIFIERS='@im=fcitx'    # 设置 X 输入法模块为 fcitx
export GTK_IM_MODULE=fcitx        # 设置 GTK 应用使用 fcitx 输入法
export QT_IM_MODULE=fcitx         # 设置 QT 应用使用 fcitx 输入法
```

- B 组（csh）

```ini
setenv LANG zh_CN.UTF-8
setenv LC_ALL zh_CN.UTF-8
setenv LANGUAGE zh_CN.UTF-8
setenv XMODIFIERS @im=fcitx
setenv GTK_IM_MODULE fcitx
setenv QT_IM_MODULE fcitx
```

### Wayland

在 Wayland 下，不应设置 `GTK_IM_MODULE` 与 `QT_IM_MODULE`。Wayland 提供了输入法相关的协议（`text-input` 和 `input-method`），这些协议已得到广泛支持，因此不依赖 GTK 和 Qt 的输入法模块也能正常使用输入法。设置 `GTK_IM_MODULE` 或 `QT_IM_MODULE` 可能会产生反效果，例如输入候选框与光标位置间距离异常。

运行在 XWayland 下的程序，输入法由环境变量 `XMODIFIERS='@im=fcitx'` 配置。

- A 组（sh/bash/zsh）：

```ini
export LANG=zh_CN.UTF-8            # 设置系统语言为中文
export LANGUAGE=zh_CN.UTF-8       # 设置优先语言为中文
export LC_ALL=zh_CN.UTF-8         # 设置所有本地化环境变量为中文
export XMODIFIERS='@im=fcitx'    # 设置 X 输入法模块为 fcitx
```

- B 组（csh）

```ini
setenv LANG zh_CN.UTF-8
setenv LC_ALL zh_CN.UTF-8
setenv LANGUAGE zh_CN.UTF-8
setenv XMODIFIERS @im=fcitx
```

## 附录：安装 RIME 中州韵输入法

- 使用 pkg 安装：

```sh
# pkg install zh-fcitx5-rime zh-rime-essay
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/chinese/fcitx5-rime/ && make install clean
# cd /usr/ports/chinese/rime-essay/ && make install clean
```

>**注意**
>
>`chinese/rime-essay` 是必要的，是 Rime 的共享词汇与语言模型，没有这个 Port，你的 RIME 输入法只会显示一团乱码。

如果 rime 未被自动添加到输入法，请手动添加完成初始化（程序里找到 fcitx 配置工具，添加 rime 输入法即可）。

对于普通用户，如果配置未生效，请检查所使用的 shell 是否按照教程进行了设置。同时，请将该用户加入 wheel 组。

## 故障排除与未竟事宜

遇到问题，请先运行 `fcitx` 故障诊断，但该输出仅针对 `bash` 的环境变量配置。也就是说，输出的环境变量仅适用于 `bash`、`sh` 和 `zsh` 等 shell，不适用于 `csh`。`csh` 的环境变量配置请参考上文。

如果提示 `bash` 字样且无法输出诊断信息，则需要先安装 `bash`：`# pkg install bash`。

运行 Fcitx5 输入法诊断工具，检查配置和环境问题：

```sh
# fcitx5-diagnose
```

对于 Fcitx 5.x 来说，找不到 `fcitx qt 4` 的支持是正常现象

