# 第 5.4 节 五笔输入法

## 安装 rime 输入法

rime 输入法引擎仅是输入法，还需要输入法面板 "ibus/fcitx" 才能使用。所以使用 rime 的前提是先正确配置 ibus/fcitx。

下面的择其一，进行安装。

```sh
# pkg install zh-fcitx5-rime
```

```
# pkg install zh-ibus-rime
```

或者：

```
# cd /usr/ports/chinese/fcitx5-rime/ && make install clean
# cd /usr/ports/chinese/ibus-rime/ && make install clean
```

## ibus


如果使用 ibus，环境变量配置：安装好运行初始化命令 `ibus-setup`，将 98 五笔码表（`wubi86.dict.yaml`、`wubi86.schema.yaml`）复制到 `/usr/local/share/rime-date` 目录下。

修改 `rime-date` 目录下 `default.yaml` 文件：打开 `default.yaml` 找到 `schema_lis` 看，下面第一行添加 `- schema: wubi98` 保存退出重新加载 ibus 输入法即可。


## fcitx 5

### 下载配置所需文件

首先下载所需文件：<https://github.com/FreeBSD-Ask/98-input>

把 `98wbx.conf` 文件复制到 `/usr/local/share/fcitx5/inputmethod/` 下面。把 `fcitx-98wubi.png` 和 `org.fcitx.Fcitx5.fcitx-98wubi.png` 图标复制到 `/usr/local/share/icons/hicolor/48x48/apps/` 下面 把 `98wbx.main.dict` 词库放到 `/usr/local/share/libime/` 下面 重启 `fcitx5`，在 `fcitx5-configtool` 起用 98 五笔即可。

王码 98 五笔生成 `.dict` 库方法，直接用下面命令生成：

```sh
$ libime_tabledict 98wbx.txt 98wbx.main.dict
```

### 安装五笔输入法

安装完成选择 rime 输入法即可，rime 默认输入法为朗月拼音（我也不知道是什么）。可以使用 `pkg search zh-rime` 查找支持的输入法：

```sh
# pkg install zh-rime-wubi
```

或者：

```
# cd /usr/ports/chinese/rime-wubi/
# make install clean
```


### 配置文件目录

五笔输入法已经安装好，在开始之前记住两个目录，第一个对应 ibus，第二个对应 fcitx5，都是 rime 的配置文件位置：

```sh
~/.config/ibus/rime             # ${XDG_CONFIG_HOME}/ibus/rime
~/.local/share/fcitx5/rime      # ${XDG_DATA_HOME}/fcitx5/rime
```

其实两者都尊循 XDG 基本目录规范，但 FreeBSD 中没有定义这两个环境变量，写在这里只是作个介绍。开始设置前 **先进入正确的配置目录**

```sh
$ cd ~/.config/ibus/rime
$ cd ~/.local/share/fcitx5/rime
```

### 启用五笔 86 输入法

```sh
$ rime_deployer --add-schema wubi86
```

当前已安装的输入法可以用 `ls /usr/local/share/rime-data` 查看，上面命令中 `"wubi86"`, 即对应其中的 `wubi86.schema.yaml` 文件。比如目录下有 `terra_pinyin.schema.yaml` 则可以添加地球拼音

```sh
$ rime_deployer --add-schema terra_pinyin
```

这时配置目录下生成 `default.custom.yaml`，这是 rime 的主要配置文件，示例如下

```sh
kamixp% cat default.custom.yaml
patch:
  schema_list:
    - {schema: wubi86}%
```

### 修改候选字为 9 行

#### 方法 ①

```sh
$ rime_patch default menu
page_size: 9
^D
patch applied.
```

其中：

- `default` 对应 `default.custom.yaml` 文件
- `menu` 对应一级选项，`page_size` 对应二级选项
- `^D` 空行按下 ctrl+D 表示结束，命令反馈输出“patch applied”

#### 方法 ②

```sh
$ rime_patch default menu/page_size
9
^D
patch applied.
```

这里推荐使用形式二进行设置，形式一在复杂一点的设置中要求对配置文件格式有一定了解

### 默认英文输出

```sh
$ rime_patch wubi86 'switches/@1/reset'
1
^D
patch applied.
```

这里把 patch 应用到 wubi86 输入法上（写入 `wubi86.custom.yaml`)，大部分的选项都是和输入法相关的，只有少部分选项是全局的（写入 `default.custom.yaml`）

具体的可用的设定选项参考下面两个链接：

- [LEOYoon-Tsaw/Rime_collections/](https://github.com/LEOYoon-Tsaw/Rime_collections/blob/master/Rime_description.md)
- [rime/CustomizationGuide](https://github.com/rime/home/wiki/CustomizationGuide)

## 98 五笔码表下载地址

[FreeBSD-98wubi-tables](https://github.com/FreeBSD-Ask/98-input/tree/main/free-bsd-98wubi-tables-master)

