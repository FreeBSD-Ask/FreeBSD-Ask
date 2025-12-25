# 8.1 本地化环境变量

## 可生效的配置文件路径

### 登录管理器配置路径

1. SDDM、LightDM、GDM 可以在 `~/.xprofile` 中写入
2. LightDM、GDM 可以在 `~/.profile` 中写入
3. SDDM 可以在用户登录 shell 的配置文件中写入

### Shell 配置路径

- sh: `~/.profile`
- bash: `~/.bash_profile` 或 `~/.profile`
- zsh: `~/.zprofile`
- csh: `~/.cshrc`

## 本地化相关的变量

下面的变量用于控制环境本地化，这些变量大都是由 POSIX 规范定义的。

`LC_*` 系列变量是 UNIX 操作系统中用于本地化（国际化和本地化）的环境变量。这些变量控制了文本字符编码、日期和时间格式、货币符号、语言等方面的设置。其中一些常见的变量如：

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

- `LC_ALL`：通过设置该变量，可同时覆盖所有其他 `LC_*` 变量的值
- `LANG`：用于设置默认的语言和字符集（可通过用户级配置文件代替直接设置该变量）。它通常用于在没有其他 `LC_*` 变量设置时提供区域设置信息。如果同时设置了 `LANG` 和 `LC_*` 变量：`LC_*` 变量将覆盖 `LANG` 变量中相应的设置
- `LANGUAGE`：用于设置当前系统的语言环境，影响程序的行为，例如日期格式、数字格式和字符编码等。该变量通常会被程序自动读取，并根据其值确定使用的语言和本地化设置。若未设置此变量，程序可能会使用默认的系统语言环境或其他环境变量（如 `LC_ALL`、`LC_MESSAGES`）来确定语言环境

通过使用这些变量，用户可轻松地调整操作系统的语言和本地化设置以适应不同的地域和语言环境。

- 可以使用 `locale` 命令确定以上变量的当前值，如：

```sh
$ locale  # 显示当前系统的本地化设置
LANG=C.UTF-8
LC_CTYPE="C.UTF-8"
LC_COLLATE="C.UTF-8"
LC_TIME="C.UTF-8"
LC_NUMERIC="C.UTF-8"
LC_MONETARY="C.UTF-8"
LC_MESSAGES="C.UTF-8"
LC_ALL=
```

- 因此，实现中文化的方式可以有所不同

1. 单纯的界面中文化只要设置 `LC_MESSAGES` 为 `"zh_CN.UTF-8"`（在 SDDM/Xfce 下验证）。
2. 较常见的将 `LANG`、`LC_ALL`、`LANGUAGE` 三个环境变量都设为 `"zh_CN.UTF-8"`。
3. 在纯英文环境下，同时使用中文输入法

---

为什么要将 `LANG`、`LC_ALL`、`LANGUAGE` 三个环境变量都设置为 `"zh_CN.UTF-8"`？这是因为开发人员在编写程序时可能使用不同的变量，为了提高兼容性才采用此设置

---

第一种设置只影响界面和提示信息，而对其他格式的输出无影响（参考 `LC_*` 系列变量概述），例如在 sh 下：

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
>保持 `date` 命令的英文输出在某些脚本中可能非常重要（这只是其中一种情况，还有其他特殊需求）。类似情况也存在于由其他 `LC_*` 变量控制的信息中。
