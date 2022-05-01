# 第十二节 安装 i3wm

本篇写给诸位希望在 FreeBSD 上使用 i3wm 的用户们.

[i3 使用手册](https://www.freebsd.org/cgi/man.cgi?query=i3&apropos=0&sektion=1&manpath=freebsd-ports&format=html)

## 准备在前

1. 安装显卡驱动, 相关教程请移步至[第二章第九节](../di-er-zhang-an-zhuang-freebsd/di-jiu-jie-wu-li-ji-xia-xian-ka-de-pei-zhi)

2. 更新系统

    ```sh
    $ pkg update
    $ pkg upgrade
    ```

3. 安装 xorg

    ```sh
    $ pkg install xorg
    ```

## 安装 i3wm 与必要的配置

1. 安装 i3wm

    ```sh
    $ pkg install -y i3
    ```

2. 安装完成后, 请在用户主目录 /usr/home/你的用户名/ 下创建 .xinitrc 文件以便使用 startx 命令启动 i3wm:

    ```sh
    $ echo "/usr/local/bin/i3" >> /usr/home/你的用户名/.xinitrc
    $ chown 你的用户名 /usr/home/你的用户名/.xinitrc
    ```

3. 重启计算机

    ```sh
    $ reboot
    ```

4. 重启完成后, 在 tty 界面登录用户, 并使用 startx 命令启动 i3wm.

    ```sh
    $ startx
    ```

5. 若一切顺利, 你已经可以看到一个 i3 界面了

    ![i3wmpreview](https://raw.githubusercontent.com/isNijikawa/isNijikawa/main/asset/i3wm_preview.png)

## 参考

+ <http://bottlenix.wikidot.com/installing-i3wm>
+ <https://unixsheikh.com/tutorials/how-to-setup-freebsd-with-a-riced-desktop-part-3-i3.html#xterm>
+ <https://forums.freebsd.org/threads/how-to-install-i3.62305/>
+ <https://www.freebsd.org/cgi/man.cgi?query=i3&apropos=0&sektion=1&manpath=freebsd-ports&format=html>
