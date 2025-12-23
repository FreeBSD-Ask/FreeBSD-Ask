# 8.7 更换字体

首先提取 Windows `C:\Windows\Fonts` 目录下的所有 `.ttf` 和 `.ttc` 字体文件。对于 macOS 的字体，需要进行特殊处理，尽管其文件格式也为 `.ttf`。

为便于管理新字体，创建一个目录存放 Windows 字体：

```sh
# mkdir -p /usr/local/share/fonts/WindowsFonts
```

将字体文件复制到 `WindowsFonts` 目录即可：


```sh
# chmod -R 755 /usr/local/share/fonts/WindowsFonts   # 设置 Windows 字体目录及其内容的权限为 755
# fc-cache                                           # 刷新字体缓存
```
