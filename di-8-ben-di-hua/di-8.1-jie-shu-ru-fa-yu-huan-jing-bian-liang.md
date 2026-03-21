# 8.1 本地化环境变量

## 可生效的配置文件路径

在 FreeBSD 系统中，本地化环境变量可以在不同的配置文件中进行配置，其具体生效路径取决于所使用的登录管理器（Display Manager）和用户 Shell 环境。

### 登录管理器配置路径

1. SDDM、LightDM、GDM 可以在 `~/.xprofile` 中写入
2. LightDM、GDM 可以在 `~/.profile` 中写入
3. SDDM 可以在用户登录 shell 的配置文件中写入

### Shell 配置路径

- sh: `~/.profile`
- bash: `~/.bash_profile` 或 `~/.profile`
- zsh: `~/.zprofile`
- csh: `~/.cshrc`

## 本地化相关的环境变量

在明确了配置文件的路径选择后，需要进一步掌握与系统本地化（Localization）相关的环境变量体系。下述变量均用于控制系统环境的本地化行为，且大部分变量由 POSIX（Portable Operating System Interface）标准规范定义。

`LC_*` 系列变量是 UNIX 及类 UNIX 操作系统中用于实现国际化（Internationalization）与本地化（Localization）的核心环境变量。这些变量系统性地控制文本字符编码、日期时间格式、货币符号、界面语言等多个维度的本地化行为。其中常见的变量包括：

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

特别说明：

- `LC_ALL`：通过设置该变量，可同时覆盖所有其他 `LC_*` 变量的值。
- `LANG`：用于设置默认的语言和字符集（可通过用户级配置文件代替直接设置该变量）。它通常用于在没有其他 `LC_*` 变量设置时提供区域设置信息。如果同时设置了 `LANG` 和 `LC_*` 变量，`LC_*` 变量将覆盖 `LANG` 变量中相应的设置。
- `LANGUAGE`：主要用于为 GNU gettext 等本地化库指定界面消息（例如命令行提示、错误信息、菜单文本等）的首选语言。它一般不会影响日期、数字、货币等格式，这些格式类本地化仍由相应的 `LC_TIME`、`LC_NUMERIC`、`LC_MONETARY` 等 `LC_*` 变量或 `LANG` 控制。若未设置 `LANGUAGE`，程序通常会回退到 `LC_MESSAGES` 或其他区域设置变量来确定界面消息语言。

通过组合使用这些变量，用户可灵活调整操作系统的语言、界面消息以及本地化相关设置，以适应不同的地域和语言环境。

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

- 因此，实现中文化的方式可以有所不同：

1. 单纯的界面中文化只要设置 `LC_MESSAGES` 为 `"zh_CN.UTF-8"`（在 SDDM/Xfce 下验证）。
2. 较常见的将 `LANG`、`LC_ALL`、`LANGUAGE` 三个环境变量都设为 `"zh_CN.UTF-8"`。
3. 在纯英文环境下，同时使用中文输入法

---

为什么要将 `LANG`、`LC_ALL`、`LANGUAGE` 三个环境变量都设置为 `"zh_CN.UTF-8"`？这是由于不同软件实现可能对本地化变量的读取优先级存在差异，为确保最大程度的系统兼容性而采用此配置策略。

---

第一种设置只影响界面和提示信息，而对其他格式的输出无影响（参考 `LC_*` 系列变量概述），例如在 sh 下：

```sh
$ locale	# 显示当前系统的本地化设置
LANG=C.UTF-8
LC_CTYPE="C.UTF-8"
LC_COLLATE="C.UTF-8"
LC_TIME="C.UTF-8"
LC_NUMERIC="C.UTF-8"
LC_MONETARY="C.UTF-8"
LC_MESSAGES=zh_CN.UTF-8
LC_ALL=
$ date	# 显示时间和日期
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

## 课后习题

1. 在 FreeBSD 系统中配置不同 Shell（sh、bash、zsh、csh）的本地化环境变量，分别验证 `date` 命令在英文和中文环境下的输出。
2. 构建一个仅设置 `LC_MESSAGES=zh_CN.UTF-8` 的环境，测试多个常用命令（如 ls、pkg、man）的中文提示可用性。
3. 设计一个脚本在执行特定任务前临时切换 `LC_TIME` 变量值，验证脚本执行期间的时间格式变化，并分析环境变量的作用域与生命周期机制。
