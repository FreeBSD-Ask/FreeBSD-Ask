# 第 5.7 节 更换字体

首先提取 Windows `C:\Windows\Fonts` 里所有的 `.ttf` 和 `.ttc` 字体文件。（MacOS 中的字体需要特殊处理，虽然看起来格式都是 `.ttf`）

为新字体新建一个目录便于管理：

```sh
# mkdir -p /usr/local/share/fonts/WindowsFonts
```

将字体文件复制进 `WindowsFonts` 即可。

```sh
# chmod -R 755 /usr/local/share/fonts/WindowsFonts #刷新权限
# fc-cache
```
