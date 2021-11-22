# 第三节 FreeBSD 中文 TTY 控制台

FreeBSD 新型终端VT，支持cjk，所以丢个字体进去，就能显示中文了\
1，首先你没有改过控制台程序，使用的是默认的……\
2，最新版本，本说明是以FreeBSD 12.1 release\
字体格式为.fnt\
命令:vidcontrol -f ABC.fnt\
系统提供了一个工具，可用于讲bdf,hex 转换为fnt

vtfontcvt \[ -h 高度 ] \[ -v ] \[ -w 宽度] \[字体]\
命令一般都是临时的，，永久生效是，将东西加入rc.conf\
示例：font8x8=abc
