# 8.7 更换字体

首先提取 Windows `C:\Windows\Fonts` 目录下的所有 `.ttf` 和 `.ttc` 字体文件。对于 macOS 的字体，需要进行特殊处理，尽管其文件格式也为 `.ttf`。

为便于管理新字体，可以创建一个专用目录：

```sh
# mkdir -p /usr/local/share/fonts/WindowsFonts
```

将字体文件复制到 `WindowsFonts` 目录即可：


```sh
# chmod -R 755 /usr/local/share/fonts/WindowsFonts  # 刷新权限
# fc-cache
```
