# 第 5.1 节 本地化环境变量

## 可生效的配置文件路径

1. sddm lightdm gdm 可以在 `~/.xprofile` 中写入；
2. lightdm gdm 可以在 `~/.profile` 中写入；
3. sddm 可以在用户登录 shell 配置文件中写入；

---

- sh: `~/.profile`
- bash: `~/.bash_profile` 或 `~/.profile`
- zsh: `~/.zprofile`
- csh: `~/.cshrc`

## 本地化相关的变量

下面的变量用于控制环境本地化，这些变量大都是由 POSIX 规范定义的。

`LC_*` 系列变量是 `Unix` 操作系统中用于本地化（即国际化和本地化）的环境变量。这些变量控制了文本字符编码、日期和时间格式、货币符号、语言等方面的设置。其中一些常见的变量如：

- `LC_COLLATE`：定义字符串排序的规则。
- `LC_CTYPE`：定义字符集和字符类型判断规则，例如字母、数字、标点符号等。
- `LC_MONETARY`：定义货币格式和货币符号。
- `LC_MESSAGES`：定义程序运行时输出信息的语言。
- `LC_NUMERIC`：定义数字格式，例如小数点和千位分隔符。
- `LC_TIME`：定义日期和时间格式。
- `LC_ADDRESS`：定义地址的格式。
- `LC_NAME`：定义人名的格式。
- `LC_PAPER`：定义纸张大小和打印格式。
- `LC_TELEPHONE`：定义电话号码的格式。
- `LC_MEASUREMENT`：定义度量单位的格式。
- `LC_IDENTIFICATION`：定义文件特征的格式。

特别的：

- `LC_ALL`：通过设置该变量，可同时覆盖所有其他 `LC_*` 变量的值。
- `LANG`：用于设置默认的语言和字符集。它通常用于在没有其他 `LC_*` 变量设置时提供区域设置信息。如果同时设置了 `LANG` 和 `LC_*` 变量：`LC_*` 变量将覆盖 `LANG` 变量中相应的设置。
- `LANGUAGE`：用于设置当前系统的语言环境，它影响了许多程序的行为，如日期格式、数字格式、字符编码等。具体地说，这个环境变量通常会被一些程序自动读取，并根据其值来确定应该使用哪种语言和本地化设置。若未设置该变量，则程序可能会使用默认的系统语言环境或其他环境变量（如 `LC_ALL`、`LC_MESSAGES` 等）来确定语言环境。

通过使用这些变量，用户可轻松地调整操作系统的语言和本地化设置以适应不同的地域和语言环境。

- 可以使用 `locale` 命令确定以上变量的当前值，如：

```sh
$ locale
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

1. 单纯的界面中文化只要设置 `LC_MESSAGES` 为 `"zh_CN.UTF-8"`（在 SDDM/Xfce 下验证）。
2. 较常见的将 `LANG`、`LC_ALL`、`LANGUAGE` 三个环境变量都设为 `"zh_CN.UTF-8"`。
3. 纯英文环境，加上中文输入法。

---

为何要将 `LANG`、`LC_ALL`、`LANGUAGE` 三个环境变量都设为 `"zh_CN.UTF-8"`？主要是开发人员在写程序的时候各自用了不同的变量，为了更大的兼容性才如此。

---

第一种设置只影响界面、提示等，但对其他的格式输出等无响影（参考 `LC_*` 系列变量概述）如（sh）。

```sh
$ locale
LANG=C.UTF-8
LC_CTYPE="C.UTF-8"
LC_COLLATE="C.UTF-8"
LC_TIME="C.UTF-8"
LC_NUMERIC="C.UTF-8"
LC_MONETARY="C.UTF-8"
LC_MESSAGES=zh_CN.UTF-8
LC_ALL=
$ date
Fri Apr 21 21:14:43 UTC 2023
$ export LC_TIME=zh_CN.UTF-8
$ date
2023年 4月21日 星期五 21时15分07秒 UTC
```

在默认情况下：

- `LC_TIME` 环境变量值为 `C.UTF-8`；
- `date` 命令输出 `Fri Apr 21 21:14:43 UTC 2023`；
- `LC_TIME` 环境变量值设置为 `zh_CN.UTF-8`；
- `date` 命令输出为 `2023年 4月21日 星期五 21时15分07秒 UTC`。

>**注意**
>
>维持 `date` 命令的英文输出对一些脚本有时很重要（这仅是其中一种情况，还有其它特殊的需求等）。这样的情况亦同样存在于其它由 `LC_*` 变量控制的信息中。
