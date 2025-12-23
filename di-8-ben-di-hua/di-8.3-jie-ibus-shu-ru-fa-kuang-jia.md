# 8.3 IBus 输入法框架

IBus 即“Intelligent Input Bus”（智能输入总线）。

## IBus

- 使用 pkg 安装：

```sh
# pkg install ibus zh-ibus-pinyin
```

- 或者使用 Ports 安装：

```sh
# cd /usr/ports/textproc/ibus/ && make install clean
# cd /usr/ports/chinese/ibus-libpinyin/ && make install clean
```

其中 `zh-ibus-pinyin` 是拼音输入法。

可选的输入法还包括：

- `chinese/ibus-cangjie` 仓颉输入法
- `chinese/ibus-chewing` 酷音输入法
- `chinese/ibus-rime` Rime 输入法引擎（后文另行说明）
- `chinese/ibus-table-chinese` 包含五笔、仓颉等多种输入法

## 配置环境变量

- 登录管理器配置路径

1. SDDM、LightDM、GDM 都可以在 `~/.xprofile` 中写入 A 组配置
2. LightDM、GDM 可以在 `~/.profile` 中写入 A 组配置
3. SDDM 可以在用户登录 shell 的配置文件中写入配置

- Shell 配置路径

1. sh: `~/.profile` 写入 A 组配置
2. bash: `~/.bash_profile` 或 `~/.profile` 写入 A 组配置
3. zsh: `~/.zprofile` 写入 A 组配置
4. csh: `~/.cshrc` 写入 B 组配置

注销后重新登录，点击 IBus 图标添加所需输入法，即可使用，无需进行中文化设置（测试环境为 SDDM/Xfce/FreeBSD 13.2/sh）或其他额外配置。建议在相应的 shell 配置文件中加入以下内容以确保 IBus 正常运行：

- A 组（在 sh、bash、zsh 中）

```ini
export XIM=ibus                     # 设置 X 输入法为 IBus
export GTK_IM_MODULE=ibus           # 设置 GTK 应用使用 IBus 输入法
export QT_IM_MODULE=ibus            # 设置 QT 应用使用 IBus 输入法
export XMODIFIERS=@im=ibus          # 设置 X 输入法修饰符为 IBus
export XIM_PROGRAM="ibus-daemon"    # 指定 XIM 程序为 ibus-daemon
export XIM_ARGS="--daemonize --xim" # 设置 XIM 启动参数为守护进程模式并启用 XIM
```

- B 组（在 csh 中）

```ini
setenv XIM ibus
setenv GTK_IM_MODULE ibus
setenv QT_IM_MODULE ibus
setenv XMODIFIERS @im=ibus
setenv XIM_PROGRAM ibus-daemon
setenv XIM_ARGS "--daemonize --xim"
```

## IBus 设置

- IBus 设置：

```sh
$ ibus-setup
```

- 编码：

IBus 要求使用 UTF-8 编码，但对区域设置（如 `C.UTF-8` 或 `zh_CN.UTF-8`）没有限制。

![ibus](../.gitbook/assets/ibus-fr-ch-ok.png)

