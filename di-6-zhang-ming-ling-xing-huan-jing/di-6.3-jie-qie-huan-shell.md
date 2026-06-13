# 6.3 切换 shell

永久更改默认 shell 的最简单方法是使用 chsh。运行此命令会打开由 EDITOR 环境变量配置的编辑器，默认情况下为 vi(1)。

## Zsh

Zsh 是 Kali Linux 和 macOS 的默认 shell。Zsh 不仅是一款为交互式使用而设计的 Shell，它还是一种强大的脚本语言。zsh 整合了 bash、ksh 和 tcsh 等绝大多数主流 shell 的许多实用特性，同时还加入了大量原创特性。

### 安装 Zsh

- 使用 pkg 安装：

```sh
# pkg install zsh zsh-completions zsh-autosuggestions zsh-syntax-highlighting
```

软件包说明：

| 程序 | 说明 |
| ---- | ---- |
| `zsh` | Zsh shell |
| `zsh-completions` | 自动补全 |
| `zsh-autosuggestions` | 类 Fish shell 的 Zsh 自动补全 |
| `zsh-syntax-highlighting` | 类 Fish shell 的 Zsh 语法高亮 |

- 使用 Ports 安装：

```sh
# cd /usr/ports/shells/zsh/ && make install clean
# cd /usr/ports/shells/zsh-completions && make install clean
# cd /usr/ports/shells/zsh-autosuggestions/ && make install clean
# cd /usr/ports/shells/zsh-syntax-highlighting/ && make install clean
```

- 查看 Zsh 安装信息

```sh
# pkg info -D zsh
```

### 配置 Zsh

将当前用户的默认登录 shell 修改为 Zsh：

```sh
# chsh -s /usr/local/bin/zsh # 切换 shell 至 zsh
chsh: user information updated
```

在提示符下输入你的密码并按下 **回车键** 即可更改 shell。注销并重新登录后即可开始使用新 shell。

> **注意**
>
> `chsh`、`chfn`、`chpass` 是同一个程序，通过不同名称调用。非超级用户只能将 shell 更改为 **/etc/shells** 中列出的标准 shell；从非标准 shell 更改或更改为非标准 shell 均会拒绝。编辑器由 `EDITOR` 环境变量决定，默认使用 vi(1)。信息验证后，chpass 会自动调用 pwd_mkdb(8) 更新用户数据库。

编辑 **~/.zshrc** 文件，添加下面几行：

```sh
source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh   # 加载 Zsh 自动建议插件
source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh   # 加载 Zsh 语法高亮插件
fpath+=/usr/local/share/zsh/site-functions/   # 将自定义函数目录添加到 Zsh 函数搜索路径
```

目录结构：

```sh
~/
└── .zshrc # Zsh 配置文件
/usr/local/
└── share/
    ├── zsh-autosuggestions/
    │   └── zsh-autosuggestions.zsh # Zsh 自动建议插件
    ├── zsh-syntax-highlighting/
    │   └── zsh-syntax-highlighting.zsh # Zsh 语法高亮插件
    └── zsh/
        └── site-functions/ # Zsh 自定义函数目录
```

立即使用：

```sh
# zsh                        # 切换当前 shell 到 Zsh
# source ~/.zshrc            # 重新加载 Zsh 配置文件，刷新环境变量
# rm -f ~/.zcompdump         # 删除 Zsh 补全缓存文件
# autoload -Uz compinit       # 加载 compinit 函数
# compinit                   # 初始化补全系统并强制重建缓存
```

### 使用主题美化

除了基本配置外，还可以通过主题美化 shell 界面。Powerlevel10k 是广泛使用的 Zsh 主题，安装和配置方法如下：

```sh
$ git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k   # 克隆 Powerlevel10k 主题仓库到主目录
$ echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc                    # 将 Powerlevel10k 主题加载命令追加到 ~/.zshrc
```

目录结构：

```sh
~/
├── .zshrc # Zsh 配置文件
└── powerlevel10k/ # Powerlevel10k 主题目录
    └── powerlevel10k.zsh-theme # Powerlevel10k 主题文件
```

重新加载 Zsh 配置文件，使 Powerlevel10k 主题生效：

```sh
# source ~/.zshrc
```

按照提示回答若干问题以完成配置，重启后生效。

### 参考文献

- romkatv. Powerlevel10k[EB/OL]. [2026-03-26]. <https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#installation>. 主题项目官网。
- FreeBSD Project. csh -- a shell with C-like syntax[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=csh&sektion=1>. C 风格语法 shell 手册页。

## Bash

Bash（Bourne Again shell）是 GNU 项目开发的 shell 程序，作为 Bourne shell（sh）的增强替代品。Bash 兼容 sh 语法，并集成了 csh 和 ksh 的有用特性，包括命令行编辑、命令历史、可编程补全和作业控制等功能。Bash 是多数 Linux 发行版的默认 shell，但在 FreeBSD 中并非基本系统组件。

### 安装 Bash

- 使用 pkg 安装：

```sh
# pkg install bash bash-completion-freebsd bash-completion-zfs
```

- 使用 Ports 安装：

```sh
# cd /usr/ports/shells/bash/ && make install clean
# cd /usr/ports/shells/bash-completion-freebsd/ && make install clean
# cd /usr/ports/shells/bash-completion-zfs/ && make install clean
```

软件包说明：

| 程序 | 说明 |
| ---- | ---- |
| `bash` | Bash shell 主程序 |
| `bash-completion-freebsd` | 针对 FreeBSD 的 Bash 补全库扩展，作为依赖自动安装 |
| `bash-completion-zfs` | 针对 OpenZFS 的 Bash 补全库扩展 |

- 查看安装后配置

```sh
# pkg info -D bash-completion # 查看作为依赖安装的 bash-completion 的配置说明
```

### 配置 Bash

安装完 Bash 及相关补全库后，需要配置才能正常运作。

```sh
chsh -s /usr/local/bin/bash   # 将当前用户的默认登录 Shell 切换为 Bash
touch ~/.bash_profile         # 创建 ~/.bash_profile 文件，用于配置 Bash 环境变量
```

相关文件结构：

```sh
~/
└── .bash_profile # Bash 配置文件
/usr/local/
└── share/
    └── bash-completion/
        ├── bash_completion.sh # Bash 补全脚本
        └── README.md # Bash 补全说明文档
```

为加载 Bash 补全功能，编辑 **~/.bash_profile** 文件，写入下行：

```bash
[[ $PS1 && -f /usr/local/share/bash-completion/bash_completion.sh ]] && source /usr/local/share/bash-completion/bash_completion.sh
```

立即使用：

```bash
# bash                     # 切换当前 shell 到 Bash
# source ~/.bash_profile    # 重新加载 Bash 配置文件，刷新环境变量
```
