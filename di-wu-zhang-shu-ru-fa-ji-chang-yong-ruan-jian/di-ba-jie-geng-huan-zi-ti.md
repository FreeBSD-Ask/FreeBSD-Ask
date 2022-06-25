# 第八节 更换字体

首先提取 `C:\Windows\Fonts` 里所有的 `.ttf` 和 `.ttc` 字体文件。

为新字体新建一个目录便于管理：

`# mkdir -p /usr/local/share/fonts/WindowsFonts`

将字体文件复制进 `WindowsFonts` 即可。

```
# chmod -R +755 /usr/local/share/fonts/WindowsFonts #刷新权限
# fc-cache 
```

即可。
