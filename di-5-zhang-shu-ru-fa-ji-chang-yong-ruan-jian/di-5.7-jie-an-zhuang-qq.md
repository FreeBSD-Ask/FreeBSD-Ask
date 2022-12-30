# 第5.7节 安装 QQ

## Linux QQ 3.x（electron）

> 请先安装 CentOS 兼容层及 Ubuntu 兼容层，具体请看 第五章 第五节。

```
# chroot /compat/ubuntu/ /bin/bash #进入 Ubuntu 兼容层
# wget https://dldir1.qq.com/qqfile/qq/QQNT/64bd2578/linuxqq_3.0.0-565_amd64.deb #此时位于 Ubuntu 兼容层
```

```
# apt install ./linuxqq_3.0.0-565_amd64.deb  #此时位于 Ubuntu 兼容层
```

安装依赖文件和字体：

```
# apt install libgbm-dev libasound2-dev webcamoid-plugins fonts-wqy-microhei  fonts-wqy-zenhei #此时位于 Ubuntu 兼容层
# cp  /usr/lib/x86_64-linux-gnu/avkys/submodules/MultiSink/libffmpeg.so /usr/lib  #此时位于 Ubuntu 兼容层
# ldconfig #此时位于 Ubuntu 兼容层
```

启动 QQ：

```
# /usr/bin/qq #此时位于 Ubuntu 兼容层
```

![](../.gitbook/assets/qq3.0.jpg)


> **注意**
>
> 一旦彻底退出 QQ，那么在本次开机中就再也进不去了。除非重启系统，原因未知，若有人知道请提交报告。
>
> 只能输入英文，中文输入法暂不可用，原因未知，若有人知道请提交报告。（我的环境是 X11 KDE5 FBSD-13.1-RELEASE Fcitx5 ）


**一些可能会用到的信息**

```
root@ykla:/# cp /usr/lib/x86_64-linux-gnu/libgtk2.0-0/gtk-query-immodules-2.0  /usr/bin/
root@ykla:/# cp /usr/lib/x86_64-linux-gnu/libgtk-3-0/gtk-query-immodules-3.0 /usr/bin/
root@ykla:/# echo $XDG_SESSION_TYPE
x11
```
```
root@ykla:/home/ykla # fcitx5-diagnose
# 系统信息:
1.  `uname -a`:

        FreeBSD ykla 13.1-RELEASE FreeBSD 13.1-RELEASE releng/13.1-n250148-fc952ac2212 GENERIC amd64

2.  `lsb_release`:

    `lsb_release` 未找到.

3.  `/etc/lsb-release`:

    `/etc/lsb-release` 未找到.

4.  `/etc/os-release`:

        NAME=FreeBSD
        VERSION="13.1-RELEASE"
        VERSION_ID="13.1"
        ID=freebsd
        ANSI_COLOR="0;31"
        PRETTY_NAME="FreeBSD 13.1-RELEASE"
        CPE_NAME="cpe:/o:freebsd:freebsd:13.1"
        HOME_URL="https://FreeBSD.org/"
        BUG_REPORT_URL="https://bugs.FreeBSD.org/"

5.  桌面环境：
    桌面环境为 `kde`。
6.  Bash 版本：
        BASH_VERSION='5.2.15(0)-release'

# 环境：1.  DISPLAY:

        DISPLAY=':0'


        WAYLAND_DISPLAY=''

2.  键盘布局：
    1.  `setxkbmap`:

            xkb_keymap {
                xkb_keycodes  { include "evdev+aliases(qwerty)" };
                xkb_types     { include "complete"      };
                xkb_compat    { include "complete"      };
                xkb_symbols   { include "pc+us+inet(evdev)"     };
                xkb_geometry  { include "pc(pc104)"     };
            };

    2.  `xprop`:

            _XKB_RULES_NAMES(STRING) = "evdev", "pc104", "us", "", ""

3.  Locale：
    1.  全部可用 locale：
            C
            C.UTF-8
            POSIX
            af_ZA.ISO8859-1
            af_ZA.ISO8859-15
            af_ZA.UTF-8
            am_ET.UTF-8
            ar_AE.UTF-8
            ar_EG.UTF-8
            ar_JO.UTF-8
            ar_MA.UTF-8
            ar_QA.UTF-8
            ar_SA.UTF-8
            be_BY.CP1131
            be_BY.CP1251
            be_BY.ISO8859-5
            be_BY.UTF-8
            bg_BG.CP1251
            bg_BG.UTF-8
            ca_AD.ISO8859-1
            ca_AD.ISO8859-15
            ca_AD.UTF-8
            ca_ES.ISO8859-1
            ca_ES.ISO8859-15
            ca_ES.UTF-8
            ca_FR.ISO8859-1
            ca_FR.ISO8859-15
            ca_FR.UTF-8
            ca_IT.ISO8859-1
            ca_IT.ISO8859-15
            ca_IT.UTF-8
            cs_CZ.ISO8859-2
            cs_CZ.UTF-8
            da_DK.ISO8859-1
            da_DK.ISO8859-15
            da_DK.UTF-8
            de_AT.ISO8859-1
            de_AT.ISO8859-15
            de_AT.UTF-8
            de_CH.ISO8859-1
            de_CH.ISO8859-15
            de_CH.UTF-8
            de_DE.ISO8859-1
            de_DE.ISO8859-15
            de_DE.UTF-8
            el_GR.ISO8859-7
            el_GR.UTF-8
            en_AU.ISO8859-1
            en_AU.ISO8859-15
            en_AU.US-ASCII
            en_AU.UTF-8
            en_CA.ISO8859-1
            en_CA.ISO8859-15
            en_CA.US-ASCII
            en_CA.UTF-8
            en_GB.ISO8859-1
            en_GB.ISO8859-15
            en_GB.US-ASCII
            en_GB.UTF-8
            en_HK.ISO8859-1
            en_HK.UTF-8
            en_IE.ISO8859-1
            en_IE.ISO8859-15
            en_IE.UTF-8
            en_NZ.ISO8859-1
            en_NZ.ISO8859-15
            en_NZ.US-ASCII
            en_NZ.UTF-8
            en_PH.UTF-8
            en_SG.ISO8859-1
            en_SG.UTF-8
            en_US.ISO8859-1
            en_US.ISO8859-15
            en_US.US-ASCII
            en_US.UTF-8
            en_ZA.ISO8859-1
            en_ZA.ISO8859-15
            en_ZA.US-ASCII
            en_ZA.UTF-8
            es_AR.ISO8859-1
            es_AR.UTF-8
            es_CR.UTF-8
            es_ES.ISO8859-1
            es_ES.ISO8859-15
            es_ES.UTF-8
            es_MX.ISO8859-1
            es_MX.UTF-8
            et_EE.ISO8859-1
            et_EE.ISO8859-15
            et_EE.UTF-8
            eu_ES.ISO8859-1
            eu_ES.ISO8859-15
            eu_ES.UTF-8
            fi_FI.ISO8859-1
            fi_FI.ISO8859-15
            fi_FI.UTF-8
            fr_BE.ISO8859-1
            fr_BE.ISO8859-15
            fr_BE.UTF-8
            fr_CA.ISO8859-1
            fr_CA.ISO8859-15
            fr_CA.UTF-8
            fr_CH.ISO8859-1
            fr_CH.ISO8859-15
            fr_CH.UTF-8
            fr_FR.ISO8859-1
            fr_FR.ISO8859-15
            fr_FR.UTF-8
            ga_IE.UTF-8
            he_IL.UTF-8
            hi_IN.ISCII-DEV
            hi_IN.UTF-8
            hr_HR.ISO8859-2
            hr_HR.UTF-8
            hu_HU.ISO8859-2
            hu_HU.UTF-8
            hy_AM.ARMSCII-8
            hy_AM.UTF-8
            is_IS.ISO8859-1
            is_IS.ISO8859-15
            is_IS.UTF-8
            it_CH.ISO8859-1
            it_CH.ISO8859-15
            it_CH.UTF-8
            it_IT.ISO8859-1
            it_IT.ISO8859-15
            it_IT.UTF-8
            ja_JP.SJIS
            ja_JP.UTF-8
            ja_JP.eucJP
            kk_KZ.UTF-8
            ko_KR.CP949
            ko_KR.UTF-8
            ko_KR.eucKR
            lt_LT.ISO8859-13
            lt_LT.UTF-8
            lv_LV.ISO8859-13
            lv_LV.UTF-8
            mn_MN.UTF-8
            nb_NO.ISO8859-1
            nb_NO.ISO8859-15
            nb_NO.UTF-8
            nl_BE.ISO8859-1
            nl_BE.ISO8859-15
            nl_BE.UTF-8
            nl_NL.ISO8859-1
            nl_NL.ISO8859-15
            nl_NL.UTF-8
            nn_NO.ISO8859-1
            nn_NO.ISO8859-15
            nn_NO.UTF-8
            pl_PL.ISO8859-2
            pl_PL.UTF-8
            pt_BR.ISO8859-1
            pt_BR.UTF-8
            pt_PT.ISO8859-1
            pt_PT.ISO8859-15
            pt_PT.UTF-8
            ro_RO.ISO8859-2
            ro_RO.UTF-8
            ru_RU.CP1251
            ru_RU.CP866
            ru_RU.ISO8859-5
            ru_RU.KOI8-R
            ru_RU.UTF-8
            se_FI.UTF-8
            se_NO.UTF-8
            sk_SK.ISO8859-2
            sk_SK.UTF-8
            sl_SI.ISO8859-2
            sl_SI.UTF-8
            sr_RS.ISO8859-2
            sr_RS.ISO8859-5
            sr_RS.UTF-8
            sr_RS.UTF-8@latin
            sv_FI.ISO8859-1
            sv_FI.ISO8859-15
            sv_FI.UTF-8
            sv_SE.ISO8859-1
            sv_SE.ISO8859-15
            sv_SE.UTF-8
            tr_TR.ISO8859-9
            tr_TR.UTF-8
            uk_UA.CP1251
            uk_UA.ISO8859-5
            uk_UA.KOI8-U
            uk_UA.UTF-8
            zh_CN.GB18030
            zh_CN.GB2312
            zh_CN.GBK
            zh_CN.UTF-8
            zh_CN.eucCN
            zh_HK.UTF-8
            zh_TW.Big5
            zh_TW.UTF-8

    2.  当前 locale：
            LANG=zh_CN.UTF-8
            LC_CTYPE="zh_CN.UTF-8"
            LC_COLLATE="zh_CN.UTF-8"
            LC_TIME="zh_CN.UTF-8"
            LC_NUMERIC="zh_CN.UTF-8"
            LC_MONETARY="zh_CN.UTF-8"
            LC_MESSAGES="zh_CN.UTF-8"
            LC_ALL=

4.  目录：
    1.  主目录：
            /root

    2.  `${XDG_CONFIG_HOME}`:

        环境变量 `XDG_CONFIG_HOME` 没有设定。
        `XDG_CONFIG_HOME` 的当前值是 `~/.config` (`/root/.config`)。
    3.  Fcitx5 设置目录：
        当前 fcitx5 设置目录是 `~/.config/fcitx5` (`/root/.config/fcitx5`)。
5.  当前用户：
    脚本作为 root (0) 运行。
    1.  `sudo` 环境变量：
        SUDO_COMMAND 没有设定。
        SUDO_USER 没有设定。
        SUDO_UID 没有设定。
        SUDO_GID 没有设定。
    2.  以管理员运行：
        **你可能以 `root` 或者 `sudo` 登录运行此脚本。这意味着两种情况，要么你有安全问题或该脚本的结果可能不准确。有关更多信息，请参见 [以 root 身份运行不好的原因](https://www.google.com/search?q=以+root+身份运行不好的原因) 或者 [sudo 的环境变量](https://www.google.com/search?q=sudo+的环境变量) 。**

# Fcitx 状态:
1.  可执行文件：
    在 `/usr/local/bin/fcitx5` 找到了 fcitx5。
2.  版本：
    Fcitx 版本: `5.0.11`

3.  进程：
    找到了 1 个 fcitx5 进程：
        1074 fcitx5

4.  `fcitx5-remote`:
/usr/local/bin/fcitx5-diagnose: 第 907 行： 1983 终止陷阱            （核心已转储）fcitx5-remote &> /dev/null

    **无法连接到 fcitx5。**

5.  DBus 界面：
    使用 `dbus-send` 来检查 dbus。
    **找不到 DBus 名称 `org.fcitx.Fcitx5` 的所有者。**

    **找不到 DBus 名称 `org.fcitx.Fcitx5` 的 pid 所有者。**

# Fcitx 配置界面：1.  配置工具封装：
    在 `/usr/local/bin/fcitx5-configtool` 找到了 fcitx5-configtool。
2.  Qt 的配置界面：
    在 `/usr/local/bin/fcitx5-config-qt` 找到了 `fcitx5-config-qt`。
3.  KDE 的配置界面：
    找到了 fcitx5 的 kcm 模块。
        kcm_fcitx5                     - 配置输入法
# 前端设置：## Xim:
1.  `${XMODIFIERS}`:

    环境变量 XMODIFIERS 已经正确地设为了“@im=fcitx”。    从环境变量中获取的 Xim 服务名称为 fcitx.

2.  根窗口上的 XIM_SERVERS：
    Xim 服务的名称与环境变量中设置的相同。
## Qt:
1.  qt4 - `${QT4_IM_MODULE}`:

    环境变量 QT4_IM_MODULE 已经正确地设为了“fcitx”。
2.  qt5 - `${QT_IM_MODULE}`:

    环境变量 QT_IM_MODULE 已经正确地设为了“fcitx”。
3.  Qt 输入法模块文件：
    找到了未知的 fcitx qt 模块：`/usr/local/lib/qt5/plugins/kcms/kcm_fcitx5.so`。    找到了 fcitx5 的 qt5 输入法模块：`/usr/local/lib/qt5/plugins/platforminputcontexts/libfcitx5platforminputcontextplugin.so`。    找到了 fcitx5 qt5 模块：`/usr/local/lib/fcitx5/qt5/libfcitx-quickphrase-editor5.so`。    找到了 fcitx5 的 qt6 输入法模块：`/usr/local/lib/qt6/plugins/platforminputcontexts/libfcitx5platforminputcontextplugin.so`。    **无法找到 Qt4 的 fcitx5 输入法模块。**

## Gtk:
1.  gtk - `${GTK_IM_MODULE}`:

    环境变量 GTK_IM_MODULE 已经正确地设为了“fcitx”。
2.  `gtk-query-immodules`:

    1.  gtk 2:

        在 `/usr/local/bin/gtk-query-immodules-2.0` 找到了 gtk `2.24.33` 的 `gtk-query-immodules`。        版本行：
            # Created by /usr/local/bin/gtk-query-immodules-2.0 from gtk+-2.24.33

        已找到 gtk `2.24.33` 的 fcitx5 输入法模块。
            "/usr/local/lib/gtk-2.0/2.10.0/immodules/im-fcitx5.so" 
            "fcitx" "Fcitx5 (Flexible Input Method Framework5)" "fcitx5" "/usr/local/locale" "ja:ko:zh:*" 
            "fcitx5" "Fcitx5 (Flexible Input Method Framework5)" "fcitx5" "/usr/local/locale" "ja:ko:zh:*" 

    2.  gtk 3:

        在 `/usr/local/bin/gtk-query-immodules-3.0` 找到了 gtk `3.24.34` 的 `gtk-query-immodules`。        版本行：
            # Created by /usr/local/bin/gtk-query-immodules-3.0 from gtk+-3.24.34

        已找到 gtk `3.24.34` 的 fcitx5 输入法模块。
            "/usr/local/lib/gtk-3.0/3.0.0/immodules/im-fcitx5.so" 
            "fcitx" "Fcitx5 (Flexible Input Method Framework5)" "fcitx5" "/usr/local/locale" "ja:ko:zh:*" 
            "fcitx5" "Fcitx5 (Flexible Input Method Framework5)" "fcitx5" "/usr/local/locale" "ja:ko:zh:*" 

3.  Gtk 输入法模块缓存：
    1.  gtk 2:

        在 `/usr/local/lib/gtk-2.0/2.10.0/immodules.cache` 找到了 gtk `2.24.33` 的输入法模块缓存。        版本行：
            # Created by /usr/local/bin/gtk-query-immodules-2.0 from gtk+-2.24.33

        已找到 gtk `2.24.33` 的 fcitx5 输入法模块。
            "/usr/local/lib/gtk-2.0/2.10.0/immodules/im-fcitx5.so" 
            "fcitx" "Fcitx5 (Flexible Input Method Framework5)" "fcitx5" "/usr/local/locale" "ja:ko:zh:*" 
            "fcitx5" "Fcitx5 (Flexible Input Method Framework5)" "fcitx5" "/usr/local/locale" "ja:ko:zh:*" 

    2.  gtk 3:

        在 `/usr/local/lib/gtk-3.0/3.0.0/immodules.cache` 找到了 gtk `3.24.34` 的输入法模块缓存。        版本行：
            # Created by /usr/local/bin/gtk-query-immodules-3.0 from gtk+-3.24.34

        已找到 gtk `3.24.34` 的 fcitx5 输入法模块。
            "/usr/local/lib/gtk-3.0/3.0.0/immodules/im-fcitx5.so" 
            "fcitx" "Fcitx5 (Flexible Input Method Framework5)" "fcitx5" "/usr/local/locale" "ja:ko:zh:*" 
            "fcitx5" "Fcitx5 (Flexible Input Method Framework5)" "fcitx5" "/usr/local/locale" "ja:ko:zh:*" 

    3.  gtk 4:

        **无法找到 gtk 4 的输入法模块缓存**

        **无法在缓存中找到 gtk 4 的 fcitx5 输入法模块。**

4.  Gtk 输入法模块文件：
    1.  gtk 2:

        找到的全部 Gtk 2 输入法模块文件均存在。
    2.  gtk 3:

        找到的全部 Gtk 3 输入法模块文件均存在。
    3.  gtk 4:

        找到的全部 Gtk 4 输入法模块文件均存在。
# 配置:
## Fcitx 插件：1.  插件配置文件目录：
    找到了 fcitx5 的插件配置目录：`/usr/local/share/fcitx5/addon`。
2.  插件列表：
    1.  找到了 28 个已启用的插件：
            Simplified and Traditional Chinese Translation 5.0.8
            Classic User Inteface 5.0.11
            Clipboard 5.0.11
            Cloud Pinyin 5.0.8
            DBus 5.0.11
            DBus Frontend 5.0.11
            Fcitx4 Frontend 5.0.11
            Full width character 5.0.8
            IBus Frontend 5.0.11
            Lua IME API 5.0.5
            Input method selector 5.0.11
            Keyboard 5.0.11
            KDE Input Method Panel 5.0.11
            Lua Addon Loader 5.0.5
            Status Notifier 5.0.11
            Notification 5.0.11
            Pinyin 5.0.8
            Extra Pinyin functionality 5.0.8
            Punctuation 5.0.8
            Quick Phrase 5.0.11
            Rime 5.0.8
            Spell 5.0.11
            Table 5.0.8
            Unicode 5.0.11
            Wayland 5.0.11
            Wayland Input method frontend 5.0.11
            XCB 5.0.11
            X Input Method Frontend 5.0.11

    2.  找到了 0 个被禁用的插件：
3.  插件库: 

    所有插件所需的库都被找到。
4.  用户界面：
    找到了 2 个已启用的用户界面插件：
        Classic User Inteface
        KDE Input Method Panel

## 输入法：1.  `/root/.config/fcitx5/profile`:

    `/profile` 未找到.

# 日志：1.  `date`:

        2022年12月31日 星期六 00时17分47秒 CST

2.  `/root/.config/fcitx5/crash.log`:

    `/crash.log` 未找到.

**警告：fcitx5-diagnose 的输出可能包含敏感信息，包括发行版名称，内核版本，正在运行的程序名称等。**

**尽管这些信息对于开发者诊断问题有帮助，请在公开发送到在线网站前检查并且根据需要移除的对应信息。**
root@ykla:/home/ykla # 
```

## Linux QQ 2.x （GTK2.0）

### **安装 Linux 兼容层：**

> 请先安装 Linux 兼容层，具体请看 第五章 第五节。

```
# pkg install linux-c7-gtk2 linux-c7-libxkbcommon
```

### 下载 Linux QQ

```
# mkdir /home/work
# fetch https://down.qq.com/qqweb/LinuxQQ/linuxqq_2.0.0-b2-1089_x86_64.rpm
```

安装 Linux QQ：

```
# pkg install archivers/rpm4
# cd /compat/linux
# rpm2cpio < /home/work/linuxqq_2.0.0-b2-1089_x86_64.rpm | cpio -id
```

### 下载并安装 Linux QQ 所需依赖

由于未知原因，安装的 Linux QQ 无法输入，需要安装以下依赖才可以输入文字，但是只摸索了 Fcitx 输入法框架下的依赖。

```
# cd /home/work
# fetch http://mirror.centos.org/centos/7/os/x86_64/Packages/gtk2-immodule-xim-2.24.31-1.el7.x86_64.rpm
# fetch https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/f/fcitx-gtk2-4.2.9.6-1.el7.x86_64.rpm
# fetch https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/f/fcitx-4.2.9.6-1.el7.x86_64.rpm
# fetch https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/f/fcitx-libs-4.2.9.6-1.el7.x86_64.rpm
```

然后分别安装以上 4 个包：

```
# cd /compat/linux
# rpm2cpio < /home/work/gtk2-immodule-xim-2.24.31-1.el7.x86_64.rpm | cpio -id
# rpm2cpio < /home/work/fcitx-gtk2-4.2.9.6-1.el7.x86_64.rpm | cpio -id
# rpm2cpio < /home/work/fcitx-4.2.9.6-1.el7.x86_64.rpm | cpio -id
# rpm2cpio < /home/work/fcitx-libs-4.2.9.6-1.el7.x86_64.rpm | cpio -id
```

~~注意：为了方便境内 FreeBSD 用户，可以使用境内的 gitee 同步下载以上 4 个文件；~~

> 经验与教训：
>
> **请远离境内诸如 gitee 等无良企业。**

Github：

[https://github.com/ykla/FreeBSD-Linux-QQ](https://github.com/ykla/FreeBSD-Linux-QQ)

### 刷新 gtk 缓存

`# /compat/linux/usr/bin/gtk-query-immodules-2.0-64 --update-cache`

### 运行 Linux QQ

`$ /compat/linux/usr/local/bin/qq`
