# 第 6.2 节 Fcitx 输入法框架

输入法框架和输入法本身是两码事，切不可混为一谈，输入法依赖输入法框架。即使在 Windows 上亦如此：Windows 目前其使用 [TSF 管理器](https://learn.microsoft.com/zh-cn/windows/win32/tsf/text-services-framework)。

fcitx 即“A flexible input method framework（一款灵活的输入法框架）”小企鹅输入法。关于其英文命名来源参见[历史](https://fcitx-im.org/wiki/History/zh-cn)。

>**技巧**
>
>视频教程见 [006-FreeBSD14.2 安装 fcitx5 及其输入法](https://www.bilibili.com/video/BV13ji2YLE3m)


> **注意**
>
> 在 FreeBSD-CURRENT 中可能会出现许多不可预料的怪异 bug：fcitx5 诊断信息英文乱码，输入法显示出奇怪的汉字，fcitx5-qt5 环境不能正常加载……

## 安装 Fcitx

### 安装 Fcitx 4.X

> **注意**
>
> 该教程仅在 KDE 5/csh 下测试通过。

- 使用 pkg 安装：


```sh
# pkg install zh-fcitx zh-fcitx-configtool fcitx-qt5 fcitx-m17n zh-fcitx-libpinyin
```

- 或者使用 Ports 安装：

```
# cd /usr/ports/chinese/fcitx/ && make install clean # 输入法框架
# cd /usr/ports/chinese/fcitx-configtool/ && make install clean # 输入法图形化配置工具
# cd /usr/ports/textproc/fcitx-qt5/ && make install clean # 支持 qt5 软件
# cd /usr/ports/textproc/fcitx-m17n/ && make install clean # 多语种支持
# cd /usr/ports/chinese/fcitx-libpinyin/ && make install clean # 拼音输入法
```


#### 开机自启 Fcitx 4.X

```sh
$ mkdir -p ~/.config/autostart/ # 若使用其他用户则需要在其命令行下再执行之
$ cp /usr/local/share/applications/fcitx.desktop ~/.config/autostart/
```

### 安装 Fcitx 5.X

fcitx 5 相比前一代，增加了对 Wayland 的支持，据说更加流畅。

---

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


经测试 SLIM 窗口下会提示 IBus 找不到……疑似 bug。也可能是配置问题。

> **技巧**
>
> 你还可以选择安装 rime：
>
>```
># pkg install zh-fcitx5-rime zh-rime-essay
>```
>
>或者：
>
>```
># cd /usr/ports/chinese/fcitx5-rime/ && make install clean
># cd /usr/ports/chinese/rime-essay/ && make install clean
>```
>
> rime 不会自动添加到输入法，需要手动添加完成初始化（程序里找到 fcitx 配置工具，添加 rime 输入法即可），这个输入法我不知道配置文件在哪，有意者可以自行安装。而且经常切换到繁体，即使你选择了简体，BUG 比较多，原因未知。对于普通用户如果未生效，请检查自己的 shell 是否选择了对应教程进行设置。另外请将该用户加入 wheel 组。


#### 开启自启 Fcitx 5.X

```sh
$ mkdir -p ~/.config/autostart/ # 若使用其他用户则需要在其命令行下再执行之
$ cp /usr/local/share/applications/org.fcitx.Fcitx5.desktop ~/.config/autostart/
```


## 配置 Fcitx4/5 环境变量

根据自己使用的桌面管理器及 shell 择一使用：

1. sddm lightdm gdm 都可以在 `~/.xprofile` 中写入 A 组配置
2. lightdm gdm 可以在 `~/.profile` 中写入 A 组配置
3. sddm 可以在用户登录 shell 配置文件中写入配置

---

- sh: `~/.profile` 写入 A 组配置
- bash: `~/.bash_profile` 或 `~/.profile` 写入 A 组配置
- zsh: `~/.zprofile` 写入 A 组配置
- csh: `~/.cshrc` 写入 B 组配置

>**注意**
>
>如果登录桌面的用户账户不是 root，就不能使用 root 身份进行设置：必须切换到该用户且在不使用 sudo 的情况下进行配置。

- A 组（sh/bash/zsh）：

```sh
export LANG=zh_CN.UTF-8
export LANGUAGE=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8
export XMODIFIERS='@im=fcitx'
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
```

- B 组（csh）

```sh
setenv LANG zh_CN.UTF-8
setenv LC_ALL zh_CN.UTF-8
setenv LANGUAGE zh_CN.UTF-8
setenv XMODIFIERS @im=fcitx
setenv GTK_IM_MODULE fcitx
setenv QT_IM_MODULE fcitx
```


## 故障排除与未竟事宜

遇到问题，请先运行 `fcitx` 故障诊断，但是该输出仅对 `bash` 做了环境变量的配置。也就是说他输出的环境变量仅适用于 `bash`、`sh` 和 `zsh` 等 SHELL，而不适用于 `csh`。于 `csh` 的环境变量配置需要参考上文。

如果提示 `bash` 字样且无法输出诊断信息，则需要先安装 `bash`：`# pkg install bash`

### fcitx 4.x

```sh
# fcitx-diagnose
```

对于 fcitx 4.x 来说，找不到 `GTK 4` 的支持是正常的。

### fcitx 5.x

```sh
# fcitx5-diagnose
```

对于 fcitx 5.x 来说，找不到 `fcitx qt 4` 的支持是正常的。

