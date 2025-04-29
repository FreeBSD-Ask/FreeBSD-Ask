# 第 5.4 节 五笔输入法

## IBus

安装配置 IBus 从略。


### 安装配置 Rime 输入法


```sh
# pkg install zh-ibus-rime
```

或者：

```sh
# cd /usr/ports/chinese/ibus-rime/ 
# make install clean
```

---

然后在终端运行初始化命令 `ibus-setup` 添加 `rime` 输入法：

![](../.gitbook/assets/wubi3.png)

再将 98 五笔码表（`free-bsd-98wubi-tables-master/wubi86.dict.yaml`、`free-bsd-98wubi-tables-master/wubi86.schema.yaml`）复制到 `/usr/local/share/rime-date` 目录下。下载地址：[FreeBSD-98wubi-tables](https://github.com/FreeBSD-Ask/98-input/)

修改 `/usr/local/share/rime-date` 目录下 `default.yaml` 文件：打开 `default.yaml` 找到 `schema_lis`，下面第一行添加 `- schema: wubi98`（注意保持缩进），并删除其他方案，如下所示：

```ini
# Rime default settings
# encoding: utf-8

config_version: '0.40'

schema_list:
  - schema: wubi98

……其余省略……

```

保存退出重新部署 Rime 输入法即可。

![](../.gitbook/assets/wubi3.png)

## Fcitx 5

首先安装并配置好 Fcitx 5。

### 安装 Fcitx 5 及 Rime 输入法

```sh
# pkg install fcitx5 fcitx5-qt5 fcitx5-qt6 fcitx5-gtk2 fcitx5-gtk3 fcitx5-gtk4 fcitx5-configtool-qt5 fcitx5-configtool-qt6 zh-fcitx5-chinese-addons zh-rime-wubi
```

或者：

```
# cd /usr/ports/chinese/rime-wubi/
# make install clean
```

Fcitx 5 配置从略。

### 下载配置所需文件

首先下载所需文件：<https://github.com/FreeBSD-Ask/98-input>。

- 把 `98五笔/98wbx.conf` 文件复制到 `/usr/local/share/fcitx5/inputmethod/` 下面；
- 把 `98五笔/fcitx-98wubi.png` 和 `org.fcitx.Fcitx5.fcitx-98wubi.png` 图标复制到 `/usr/local/share/icons/hicolor/48x48/apps/` 下面；
- 把 `98五笔/98/wbx.main.dict` 词库放到 `/usr/local/share/libime/` 下面。
- 重启 `fcitx5`，在设置中起用 98 五笔即可。

![](../.gitbook/assets/wubi1.png)

![](../.gitbook/assets/wubi2.png)

---

附录：王码 98 五笔生成 `.dict` 库方法，可用下面命令生成：

```sh
$ libime_tabledict 98wbx.txt 98wbx.main.dict
```

## 配置文件目录

五笔输入法已经安装好，rime 的配置文件位置如下：

```sh
$ cd ~/.config/ibus/rime # 对应 ibus
$ cd ~/.local/share/fcitx5/rime # 对应 fcitx5
```

## 五笔 86 输入法

```sh
$ rime_deployer --add-schema wubi86
```

当前已安装的输入法可以用 `ls /usr/local/share/rime-data` 查看，上面命令中 `"wubi86"`，即对应其中的 `wubi86.schema.yaml` 文件。比如目录下有 `terra_pinyin.schema.yaml` 则可以添加地球拼音

```sh
$ rime_deployer --add-schema terra_pinyin
```

这时配置目录下生成 `default.custom.yaml`，这是 rime 的主要配置文件，示例如下

```sh
% cat default.custom.yaml
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
