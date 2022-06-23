# 第九节 Csh 与其他 Shell

>注意：该文章可能不再具有现实意义，因为 FreeBSD 14 中的 shell 被统一为了 sh。
## FreeBSD csh shell 配置

在 `/etc/csh.cshrc` 里面加入：

`alias ls ls –G`

并重新登录

问：如何让 FreeBSD 的 csh 像 bash 那样按 Tab 列出列出无法补齐的候选文件？

答：标准的方法是按 `Ctrl+D`。

但如果一定要用 `Tab` 的话，在 `/etc/csh.cshrc`中加入：`set autolist`

## FreeBSD 如何让 csh 像 zsh 那样具有命令错误修正呢

比如你用 emacs 写 c 语言程序，但你输完 `emacs ma` 按 `Tab` 回车是，他会匹配所有 `ma` 开头的文件，而这个是忽略掉，也就是按 `Tab` 时不会在有你忽略的东西，对编程之类的友好，不用再匹配到二进制。`.o` 之类的文件，

```
　set correct = cmd lz/usr/bin tcsh>ls /usr/bin (y|n|e|a)?
　set fignore = (.o ~) emacs ma[^D] main.c main.c~ main.o emacs ma[tab] emacs main.c
```

## 更换默认 shell

警告：切换默认 `Shell` 会导致 **恢复模式无法正常启动加载命令行环境**。

例如切换到 zsh：

```
# pkg install zsh zsh-autosuggestions zsh-syntax-highlighting
# chsh -s /usr/local/bin/zsh
# touch ~/.zshrc
# ee ~/.zshrc #添加下面几行
source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/.p10k.zsh
```

切换到 bash：

```
# pkg install bash
# chsh -s /usr/local/bin/bash
# ee ~/.bash_profile
```
