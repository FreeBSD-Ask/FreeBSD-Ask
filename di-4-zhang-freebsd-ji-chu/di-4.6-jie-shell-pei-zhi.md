# 4.6 Shell 配置

Shell 的配置体系通过一系列初始化文件（initialization files）实现。

不同 Shell 的初始化文件加载顺序存在差异：

对于 Bourne Shell 及其兼容 Shell（sh、bash、zsh），登录 Shell 依次读取 `/etc/profile`、`~/.profile`（或 `~/.bash_profile`、`~/.zprofile`），交互式非登录 Shell 读取 `~/.bashrc`（bash）或 `~/.zshrc`（zsh）；

对于 C Shell（csh/tcsh），登录 Shell 读取 `/etc/csh.cshrc`、`/etc/csh.login`、`~/.cshrc`、`~/.login`。

理解这一加载顺序对于正确配置环境变量和 Shell 别名至关重要。

## Zsh

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

- 使用 ports 安装：

```sh
# cd /usr/ports/shells/zsh/ && make install clean
# cd /usr/ports/shells/zsh-completions && make install clean
# cd /usr/ports/shells/zsh-autosuggestions/ && make install clean
# cd /usr/ports/shells/zsh-syntax-highlighting/ && make install clean
```

### 查看安装信息

```sh
# pkg info -D zsh
zsh-5.9_5:
On install:
==========================================================

By default, zsh looks for system-wide defaults in
/usr/local/etc.

If you previously set up /etc/zprofile, /etc/zshenv, etc.,
either move them to /usr/local/etc or rebuild zsh with the
ETCDIR option enabled.

==========================================================
默认情况下，zsh 会在 /usr/local/etc 中查找系统范围的默认设置。

如果你之前设置了 /etc/zprofile、/etc/zshenv 等，
要么将它们移到 /usr/local/etc，要么在启用 ETCDIR 选项的情况下重新构建 zsh。

==========================================================
```

```sh
# pkg info -D zsh-autosuggestions
zsh-autosuggestions-0.7.1:
On install:
Add the line below to your .zshrc to enable auto suggestions.

source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh
安装时：
将以下行添加到你的 .zshrc 文件中以启用自动建议。

source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh

zsh-syntax-highlighting-0.8.0,1:
On install:
Add the line below to *the end of* your .zshrc to enable highlighting.

source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
安装时：
将以下行添加到你的 .zshrc 文件 *末尾* 以启用语法高亮。

source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
```

### 配置 Zsh

将当前用户的默认登录 Shell 修改为 Zsh：

```sh
# chsh -s /usr/local/bin/zsh # 切换 shell 至 zsh
chsh: user information updated
```

> **注意**
>
>`chsh`、`chfn`、`chpass` 是同一个程序，通过不同名称调用。非超级用户只能将 Shell 更改为 `/etc/shells` 中列出的标准 Shell；从非标准 Shell 更改或更改为非标准 Shell 均被拒绝。编辑器由 `EDITOR` 环境变量决定，默认使用 vi(1)。修改完成后需要通过 pwd_mkdb(8) 更新用户数据库。

编辑 `~/.zshrc` 文件，添加下面几行：

```ini
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

#### 使用主题美化

除了基本配置外，还可以通过主题让 Shell 界面更加美观。Powerlevel10k 是一个非常流行的 Zsh 主题，下面是安装和配置方法：

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

回答几个问题即可完成配置。重启后完成配置。

##### 参考文献

- romkatv. Powerlevel10k[EB/OL]. [2026-03-26]. <https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#installation>. 主题项目官网。
- FreeBSD Project. csh -- a shell with C-like syntax[EB/OL]. [2026-04-17]. <https://man.freebsd.org/cgi/man.cgi?query=csh&sektion=1>. C 风格语法 Shell 手册页。

## Bash

Bash（Bourne Again SHell）是 GNU 项目开发的 Shell 程序，作为 Bourne Shell（sh）的增强替代品。Bash 兼容 sh 语法，并集成了 csh 和 ksh 的有用特性，包括命令行编辑、命令历史、可编程补全和作业控制等功能。Bash 是多数 Linux 发行版的默认 Shell，但在 FreeBSD 中并非基本系统组件。

### 安装 Bash

- 使用 pkg 安装：

```sh
# pkg install bash bash-completion-freebsd bash-completion-zfs
```

软件包说明：

| 程序 | 说明 |
| ---- | ---- |
| `bash` | Bash shell 主程序 |
| `bash-completion-freebsd` | 针对 FreeBSD 的 Bash 补全库扩展，安装时会自动安装 shells/bash-completion 作为依赖 |
| `bash-completion-zfs` | 针对 OpenZFS 的 Bash 补全库扩展 |

- 使用 ports 安装：

```sh
# cd /usr/ports/shells/bash/ && make install clean
# cd /usr/ports/shells/bash-completion-freebsd/ && make install clean
# cd /usr/ports/shells/bash-completion-zfs/ && make install clean
```

### 查看安装后配置

```sh
# pkg info -D bash-completion # 作为依赖安装的
bash-completion-2.14.0,2:
On install:
To enable the bash completion library, add the following to
your .bashrc file:

[[ $PS1 && -f /usr/local/share/bash-completion/bash_completion.sh ]] && \
	source /usr/local/share/bash-completion/bash_completion.sh

See /usr/local/share/doc/bash-completion/README.md for more information.
安装时：
要启用 bash 补全库，请将以下内容添加到你的 .bashrc 文件中：

[[ $PS1 && -f /usr/local/share/bash-completion/bash_completion.sh ]] && \
	source /usr/local/share/bash-completion/bash_completion.sh

有关更多信息，请参见 /usr/local/share/doc/bash-completion/README.md。
```

### 配置 Bash

安装完 Bash 及相关补全库后，需要进行配置才能正常使用。

```bash
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

要加载 Bash 补全功能。编辑 `~/.bash_profile` 文件，写入下行：

```bash
[[ $PS1 && -f /usr/local/share/bash-completion/bash_completion.sh ]] && source /usr/local/share/bash-completion/bash_completion.sh
```

立即使用：

```bash
# bash                     # 切换当前 shell 到 Bash
# source ~/.bash_profile    # 重新加载 Bash 配置文件，刷新环境变量
```

## 配置 csh/tcsh

除了 Zsh 和 Bash 外，FreeBSD 基本系统还内置了 csh 和 tcsh。csh（C shell，灵感来自 C 语言，语法也类似，作者是 Bill Joy）是 FreeBSD 基本系统内置的 shell，以前是 root 用户的默认 shell。FreeBSD 默认 Shell 为 sh（自 FreeBSD 14 起），但基本系统同时提供 csh/tcsh 作为替代选择。

> **技巧**
>
> csh 与 tcsh 的关系
>
> 需要注意的是，FreeBSD 中 csh 和 tcsh 是同一个二进制程序，但以不同名称调用时行为有所差异。可以通过查看源代码 [https://github.com/freebsd/freebsd-src/blame/main/bin/csh/Makefile](https://github.com/freebsd/freebsd-src/blame/main/bin/csh/Makefile) 以及执行 man csh 来验证，都会重定向至 tcsh，提供 csh 与 tcsh 关系的源代码佐证。

> **注意**
>
> 虽然 csh 与 tcsh 本质上是同一程序，但在使用时存在差异，如果以 csh 的参数调用，则部分 tcsh 扩展会被关闭。

> **注意**
>
> [FreeBSD 14 中的 shell 被统一为 sh](https://github.com/freebsd/freebsd-src/commit/d410b585b6f00a26c2de7724d6576a3ea7d548b7)，记录 FreeBSD 14 默认 shell 变更的提交记录。

- 在 `~/.cshrc` 文件中加入下行，为 `ls` 命令设置彩色输出。

```sh
alias ls ls -G
```

并重新登录即可。

- 如何让 FreeBSD 的 csh 像 Bash 那样按 Tab 列出无法补全的候选文件？在 `~/.cshrc` 文件中加入：

```ini
set filec              # 启用命令行文件名补全
set autolist           # 自动显示补全列表
```

重新加载 C shell 配置文件，刷新别名和环境设置：

```sh
# source ~/.cshrc
```

- 如何让 csh 像 zsh 那样具有命令错误修正功能呢？

例如，当使用 emacs 编写 C 语言程序时，输入 `emacs ma` 并按 `Tab` 键再按回车键，会匹配所有以 `ma` 开头的文件。此配置可以忽略部分匹配的文件，即按 `Tab` 时不会列出被忽略的文件，便于编程，不会匹配二进制 `.o` 文件等。

```ini
set correct = cmd        # 启用命令拼写自动纠正功能，提示输入正确命令
# 例：lz/usr/bin tcsh>ls /usr/bin (y|n|e|a)?  # 当检测到命令拼写错误时的提示示例

set fignore = (.o ~)   # 设置文件名忽略模式，用于补全时排除指定文件或模式
```

## 课后习题

1. 配置 Zsh 环境，安装 Powerlevel10k 主题，并编写一个自定义 Shell 函数用于自动化 FreeBSD 系统更新。
2. 对比 csh/tcsh 与 sh 在 FreeBSD 基本系统中的实现差异，分析为何 csh 曾作为默认 root Shell。
3. 为 csh 添加一些现代 Shell 应有的功能。
