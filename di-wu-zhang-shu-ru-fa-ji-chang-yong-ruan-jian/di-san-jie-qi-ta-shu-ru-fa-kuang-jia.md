# 第三节 五笔输入法

## FreeBSD 使用 98 五笔输入法教程

**注意：以下全部教程可能仅适用于 GNOME 桌面**

以下教程二选一。

### ibus

`# pkg install zh-ibus-rime`

#### 配置

环境变量配置：安装好运行初始化命令 `ibus-setup`，将 98 五笔码表（`wubi86.dict.yaml`、`wubi86.schema.yaml`）复制到`/usr/local/share/rime-date` 目录下，修改 rime-date 目录下default.yaml 文件:

打开 `default.yaml` 找到`schema_lis`：

下面第一行添加 `- schema: wubi98` 保存退出重新加载 ibus 输入法即可。

#### 98 五笔码表 下载地址

~~https://gitee.com/ykla/free-bsd-98wubi-tables/tree/master~~

>经验与教训：
>
>**请远离国内打着开源旗号实则封闭的无良企业与其创造的所谓的开源社区。**

### fcitx5


首先下载所需文件：https://github.com/FreeBSD-Ask/98-input

把 `98wbx.conf` 文件复制到 `/usr/local/share/fcitx5/inputmethod/`（`inputmethod` 目录）下面
把 `fcitx-98wubi.png` 和 `org.fcitx.Fcitx5.fcitx-98wubi.png` 图标复制到 `/usr/local/share/icons/hicolor/48x48/apps/`（apps目录）下面
把 `98wbx.main.dict` 词库放到 `/usr/local/share/libime/`（`libime`目录）下面
重启 `fcitx5`，在 `fcitx5-configtool` 起用98五笔即可

提示：王码 98 五笔生成 `.dict` 库方法，直接用下面命令生成：

```
$ libime_tabledict 98wbx.txt 98wbx.main.dict
```
