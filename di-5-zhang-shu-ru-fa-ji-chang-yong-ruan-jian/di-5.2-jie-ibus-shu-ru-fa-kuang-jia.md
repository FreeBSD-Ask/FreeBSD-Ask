# 第 5.2 节 Ibus 输入法框架

## ibus

基本安装

```shell-session
# pkg install ibus zh-ibus-pinyin
```

其中 `zh-ibus-pinyin` 为拼音输入法

可选的还有

- `zh-ibus-cangjie` 仓颉输入法
- `zh-ibus-chewing` 酷音输入法
- `zh-ibus-rime` rime 输入法引擎（另述）
- `zh-ibus-table-chinese` 包含五笔、仓颉等多种输入法

## 环境变量配置

1. sddm lightdm gdm 都可以在 `~/.xprofile` 中写入 A 组配置
2. lightdm gdm 可以在 `~/.profile` 中写入 A 组配置
3. sddm 可以在用户登录 shell 配置文件中写入配置

- sh: `~/.profile` 写入 A 组配置
- bash: `~/.bash_profile` 或 `~/.profile` 写入 A 组配置
- zsh: `~/.zprofile` 写入 A 组配置
- csh: `~/.cshrc` 写入 B 组配置

注销后登录，直接点击 ibus 图标加入自己的输入法后，即可使用,不需配置,不须中文化设置（测试环境 sddm/xfce/freebsd 13.2/sh）。但是 ibus 提示应当在相应的 shell 文件(具体文件另述）中加入以下内容

A 组：

```shell-session
#A 组 在 sh、bash、zsh 中
export XIM=ibus
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export XIM_PROGRAM="ibus-daemon"
export XIM_ARGS="--daemonize --xim"
```

或 B 组：

```shell-session
#B组 在 csh 中
setenv XIM ibus
setenv GTK_IM_MODULE ibus
setenv QT_IM_MODULE ibus
setenv XMODIFIERS @im=ibus
setenv XIM_PROGRAM ibus-daemon
setenv XIM_ARGS "--daemonize --xim"
```

这里，建议按 ibus 的建议加入相应内容，以确保在更多的程序中使用时的兼容性。

以前是要配置的现在默认可以不配置，这里我注意到 FreeBSD 13 中 `LC_*`,及`LANG`环境变量的默认值为`"C.UTF-8"`,原来这些环境变量的默认值是`"C"`,这个变化从 FreeBSD 12 开始(chatgpt 查询所得)。所以现在的情况下默认已指定字符编码为`UTF-8`,这可能是 ibus 不需要设置的原因。之前没注意到，或是因为不作汉化使用输入法的情况是很少见的，或是因为来自于 FreeBSD 12 之前的习惯做了环境变量设置而未意识到，或者是之前 ibus 对环境变量的要求比与现在有区别。这里以 lightdm/mate/ibus/rime 环境,`LANG`,`LANGUAGE`,`LC_ALL`设置为`"fr_Fr.UTF-8"`，维持字符编码为`UTF-8`，仍可以正常输入中文，可见 ibus 对编码设置有要求，但对区域设置并无要求

![ibus](../.gitbook/assets/ibus-fr-ch-ok.png)

