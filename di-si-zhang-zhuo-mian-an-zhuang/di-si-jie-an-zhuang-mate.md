# 第四节 安装 Mate 桌面

FreeBSD 安装 mate 桌面环境

## 安装开始（主要程序）

`# pkg install -y mate xorg`

在文件 `/etc/rc.conf` 中加入下面的行

```
moused_enable="YES"
dbus_enable="YES"
```

## 安装登陆管理器

Slim 和 Lightdm 任选其一，因为前者已经停止开发，故推荐使用 Lightdm。

### 安装 Lightdm

- `# pkg install lightdm lightdm-gtk-greeter`

- 在`/etc/rc.conf` 中加入一行：`lightdm_enable="YES"`

- 在主目录`.xinitrc` 文件内加入下面的行:

`exec mate-session`


### 安装 Slim

- `# pkg install -y slim`

- 在`/etc/rc.conf` 中加入一行：`slim_enable="YES"`


## 显示中文桌面环境

默认是 csh，在 `.cshrc` 中添加如下内容：

```
setenv LANG zh_CN.UTF-8
setenv LC_CTYPE zh_CN.UTF-8
```

## 输入法

`# pkg install zh-ibus-libpinyin`（安装好运行初始化命令 `ibus-setup`）

设置输入法变量:

`# ee .xinitrc`

文件添加以下内容

```
export GTK_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export QT_IM_MODULE=ibus
ibus &
```

## 安装软件/安装字体

```
# pkg install -y noto-sc
# pkg install -y firefox
# pkg install -y networkmgr
# pkg install -y zh_CN-libreoffice
```
