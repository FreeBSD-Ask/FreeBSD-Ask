# 第二节 如何提交一个软件包

建议阅读 [FreeBSD Porter's Handbook](https://docs.freebsd.org/en/books/porters-handbook/) 。

>**注意**
>
>我们正在尽力翻译该文档，如果你愿意参加，请点击 <https://github.com/FreeBSD-Ask/porter-handbook>。

FreeBSD 的软件是以 port 提供的，开发者不需要考虑如何打包成二进制软件包等问题，port 里面也不包含软件的源代码，类似于 Gentoo（Gentoo 的 portage 脱胎于 ports) ，所以理论上移植难度并不是很高。

当你移植完成后，可以提交一个 bug 到 bug 报告系统请求合并，具体格式可以在列表看看别的软件。如果长时间没人理会，请发邮件到邮件列表询问是否有人能够帮助提交。如果还是没有人，请隔一周再发一遍。

可能用到的资源：

 - FreeBSD 的镜像构建状态网页：<https://ci.freebsd.org/>。
 - FreeBSD 的 pkg 二进制软件包构建状态网页：<https://pkg-status.freebsd.org/>。


