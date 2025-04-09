# 第 5.1 节 输入法与环境变量


在“可生效配置文件”中写入配置内容即可。配置内容分 A、B 组两组。

## A 组

### sh/bash/zsh：fcitx/fcitx5

```sh
export LANG=zh_CN.UTF-8
export LANGUAGE=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8

export XMODIFIERS='@im=fcitx'
export GTK_IM_MODULE=fcitx/xim
export QT_IM_MODULE=fcitx
```

### sh/bash/zsh：ibus

```sh
export LANG=zh_CN.UTF-8
export LANGUAGE=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8

export XIM=ibus
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export XIM_PROGRAM="ibus-daemon"
export XIM_ARGS="--daemonize --xim"
```

## B 组

### csh：fcitx5

```sh
setenv LANG zh_CN.UTF-8
setenv LC_ALL zh_CN.UTF-8
setenv LANGUAGE zh_CN.UTF-8
setenv XMODIFIERS @im=fcitx
setenv GTK_IM_MODULE fcitx/xim
setenv QT_IM_MODULE fcitx
```

### csh：ibus

```sh
setenv LANG zh_CN.UTF-8
setenv LC_ALL zh_CN.UTF-8
setenv LANGUAGE zh_CN.UTF-8
setenv XIM ibus
setenv GTK_IM_MODULE ibus
setenv QT_IM_MODULE ibus
setenv XMODIFIERS @im=ibus
setenv XIM_PROGRAM ibus-daemon
setenv XIM_ARGS "--daemonize --xim"
```

## 配置文件路径

根据自己使用的桌面管理器择一使用：

1. sddm lightdm gdm 可以在 `~/.xprofile` 中写入 A 组配置
2. lightdm gdm 可以在 `~/.profile` 中写入 A 组配置
3. sddm 可以在用户登录 shell 配置文件中写入配置

- sh: `~/.profile` 写入 A 组配置
- bash: `~/.bash_profile` 或 `~/.profile` 写入 A 组配置
- zsh: `~/.zprofile` 写入 A 组配置
- csh: `~/.cshrc` 写入 B 组配置

## 本地化相关的变量

下面的变量用于控制环境本地化，这些变量大都是由 POSIX 规范定义的。

`LC_*` 系列变量是 `Linux` 和 `Unix` 操作系统中用于本地化（即国际化和本地化）的环境变量。这些变量控制了文本字符编码、日期和时间格式、货币符号、语言等方面的设置。其中一些常见的变量包括：

- `LC_COLLATE`: 定义字符串排序的规则。
- `LC_CTYPE`: 定义字符集和字符类型判断规则，例如字母、数字、标点符号等。
- `LC_MONETARY`: 定义货币格式和货币符号。
- `LC_MESSAGES`: 定义程序运行时输出信息的语言。
- `LC_NUMERIC`: 定义数字格式，例如小数点和千位分隔符。
- `LC_TIME`: 定义日期和时间格式。
- `LC_ADDRESS`: 定义地址的格式。
- `LC_NAME`: 定义人名的格式。
- `LC_PAPER`: 定义纸张大小和打印格式。
- `LC_TELEPHONE`: 定义电话号码的格式。
- `LC_MEASUREMENT`: 定义度量单位的格式。
- `LC_IDENTIFICATION`: 定义文件特征的格式。

特别的：

- `LC_ALL`: 通过设置该变量，可以同时覆盖所有其他 `LC_*` 变量的值。
- `LANG`: 用于设置默认的语言和字符集。它通常用于在没有其他 `LC_*` 变量设置时提供区域设置信息。如果同时设置了 `LANG` 和 `LC_*` 变量，`LC_*` 变量将覆盖 `LANG` 变量中相应的设置。
- `LANGUAGE`: 用于设置当前系统的语言环境，它影响了许多程序的行为，如日期格式、数字格式、字符编码等。具体地说，这个环境变量通常会被一些程序自动读取，并根据其值来确定应该使用哪种语言和本地化设置。如果未设置该变量，则程序可能会使用默认的系统语言环境或其他环境变量（如 `LC_ALL`、`LC_MESSAGES` 等）来确定语言环境。

使用这些变量，用户可以轻松地调整操作系统的语言和本地化设置以适应不同的地域和语言环境。

- 可以使用 `locale` 命令确定以上变量的当前值，如：

```sh
jk@freebsd:~ $ locale
LANG=C.UTF-8
LC_CTYPE="C.UTF-8"
LC_COLLATE="C.UTF-8"
LC_TIME="C.UTF-8"
LC_NUMERIC="C.UTF-8"
LC_MONETARY="C.UTF-8"
LC_MESSAGES="C.UTF-8"
LC_ALL=
```

- 所以中文化其实也可以不同。

1. 单纯的界面中文化只要设置 `LC_MESSAGES` 为 `"zh_CN.UTF-8"`（在 sddm/xfce 下验证）。
2. 较常见的将 `LANG`、`LC_ALL`、`LANGUAGE` 三个环境变量都设为 `"zh_CN.UTF-8"`。
3. 纯英文环境，加上中文输入。

---

为什么要将 `LANG`、`LC_ALL`、`LANGUAGE` 三个环境变量都设为 `"zh_CN.UTF-8"`？主要是开发人员在写程序的时候各自用了不同的变量，为了更大的适应性，就全部进行设置。

---

第一种设置只影响界面、提示等，但对其他的格式输出等没有响影（参考 `LC_*` 系列变量概述）如（sh）。

```sh
jk@freebsd:~ $ locale
LANG=C.UTF-8
LC_CTYPE="C.UTF-8"
LC_COLLATE="C.UTF-8"
LC_TIME="C.UTF-8"
LC_NUMERIC="C.UTF-8"
LC_MONETARY="C.UTF-8"
LC_MESSAGES=zh_CN.UTF-8
LC_ALL=
jk@freebsd:~ $ date
Fri Apr 21 21:14:43 UTC 2023
jk@freebsd:~ $ export LC_TIME=zh_CN.UTF-8
jk@freebsd:~ $ date
2023年 4月21日 星期五 21时15分07秒 UTC
```

默认情况 `LC_TIME` 环境变量值为 `C.UTF-8`。`date` 命令输出 `Fri Apr 21 21:14:43 UTC 2023`。`LC_TIME` 环境变量值设置为 `zh_CN.UTF-8`。`date` 命令输出 `2023年 4月21日 星期五 21时15分07秒 UTC`。维持 `date` 命令的英文输出对一些脚本编写者有时很重要（这只是一种情况，还有其它特殊的需求等）。这样的情况也存在于其它一样 `LC_*` 变量控制的信息中。

## 时区设置

每个用户可以设置自己的时区，在用户的 shell 配置文件中设置 `TZ` 变量即可。

- sh、bash、zsh

```sh
export TZ=CST-8 
# 或
export TZ=Asia/Shanghai
```

- csh

```sh
setenv TZ CST-8
# 或
setenv TZ "Asia/Shanghai"
```

- 在 crontab 配置文件中，设置 `CRON_TZ` 变量即可：

```sh
CRON_TZ=CST-8
0 8 * * * date >> ~/date.log
```

## 安装输入法的 Shell 脚本

用户可以通过脚本快速安装，shell 脚本内容如下。可能已经过时不再能使用了。

<https://gist.github.com/ykla/b10c7da5382543e288f79f9f446bcc9e>
