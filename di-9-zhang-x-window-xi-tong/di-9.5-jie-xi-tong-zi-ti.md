# 9.5 系统字体

FreeBSD 默认字体对中文显示效果欠佳。本节介绍图形界面引入 Windows TrueType 字体的方法及控制台字体的替换配置。

## GUI 图形界面字体

首先提取 Windows **C:\Windows\Fonts** 目录下的所有 `.ttf` 和 `.ttc` 字体文件。macOS 字体文件格式虽同为 `.ttf`，仍需特殊处理。

为管理新字体，创建一个目录存放 Windows 字体：

```sh
# mkdir -p /usr/local/share/fonts/WindowsFonts
```

将字体文件复制到 **WindowsFonts** 目录。

字体目录结构：

```sh
/usr/local/share/
└── fonts/
    └── WindowsFonts/ # Windows 字体存放目录
```

设置 Windows 字体目录及其内容的权限为 755：

```sh
# chmod -R 755 /usr/local/share/fonts/WindowsFonts
```

还需刷新字体缓存：

```sh
# fc-cache
```

## 附录：安装 Windows 11 字体（自制包）

该包亦可运行于 Debian 与低版本 Ubuntu 的 FreeBSD 兼容层下。安装方法：

```sh
# apt install git                          # 安装 Git
# git clone https://github.com/ykla/ttf-mswin11-zh-deb   # 克隆字体包仓库
# cd ttf-mswin11-zh-deb                    # 进入字体包目录
# dpkg -i ttf-ms-win11-*.deb               # 安装 Windows 11 中文字体包
```

## 课后习题

1. 从 Windows 系统提取字体文件并在 FreeBSD 中配置，测试多个 GTK 和 Qt 应用程序的字体显示效果。
2. 下载 bdf 或 hex 格式的字体文件，使用 vtfontcvt 工具将其转换为 fnt 格式，在控制台中测试显示效果。
3. 尝试使用第三方工具（如 vt-fnt）生成中文字体的 fnt 文件，验证其在 FreeBSD 控制台中的显示效果。
