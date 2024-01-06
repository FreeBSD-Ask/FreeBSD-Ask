# FreeBSD 从入门到跑路

### 概述

格言：恪守古老的法则，追寻真正的自由\
本书定位：入门到跑路这本书的目标，并非是对HandBook的翻译，而是编写一本类似《鸟哥的Linux私房菜：基础学习篇》&《鸟哥的Linux私房菜：服务器假设篇》二合一的FreeBSD文档。本书是HandBook的超集。\
**编辑指南概要**：我们欢迎所有支持FreeBSD的人进行编写，并会将他们陈列在贡献者名单中。\
FreeBSD 从入门到跑路诞生于12月19日2021年。目的是复兴FreeBSD。编写内容为FreeBSD的基础和进阶知识。如果你有一定的Unix基础，可以跳过第一章。如果你对FreeBSD有一定的认识，欢迎你加入我们，一起编写本书，贡献自己的力量，让FreeBSD在中国越走越远！

### 资源

QQ群：787969044\
Telegram群组：[https://t.me/oh_my_BSD](https://t.me/oh_my_BSD)\
微信群：需要通过QQ群\
HandBook最新翻译：[https://handbook.bsdcn.org](https://handbook.bsdcn.org/)\
FreeBSD Port开发者手册 最新翻译：[https://porters-handbook.bsdcn.org](https://porters-handbook.bsdcn.org/)\
FreeBSD入门书籍：[https://book.bsdcn.org](https://book.bsdcn.org/)\
FreeBSD 中文 man 手册：[https://man.bsdcn.org](https://man.bsdcn.org/)

### 社区愿景

我们成立于 2018 年 3 月 17 日，由贴吧——FreeBSD 吧发展到了 QQ 群，Telegram 群，至于微信群。 我们的成员具有非常大的广泛性和普遍性，能够代表绝大多数 FreeBSD 用户的平均水平：他们可能根本没有听说过何为 FreeBSD，但这并不影响我们的交流与沟通。也许有人觉得这是浪费时间，但是没有新生力量的培养，何来 FreeBSD 的明天呢？谁不知道新人可能有很多坏习惯呢。 同鲁迅先生说的那样，但愿每个人都是一束光，照亮 FreeBSD 在中国大陆地区前进的光荣的荆棘路。也希望，你可以加入我们，共同组成漫天星光亦或者是莹莹之火。 无穷的远方，无数的人们，都和我有关。 我曾无数次眺望远山，想要找到一汪清泉，天总是不遂人愿，仍旧是没有找到。 我们是谁？我们从何而来？我们将去往何方？这些问题永远也不会有结果。 我们选择 FreeBSD，是因为想选择一个清晰、明了、可靠、稳固的一个操作系统在工作上给我们带来收益以及在生活中给我们带来乐趣。当然 FreeBSD 还存在很多问题，有待大家积极发现、探讨、完善，社会在进步，技术在进步，热情丝毫不减在持续，未来越来越美好。 我们必须团结起来做些什么事情，无论大小，哪怕只是谈谈自己的学习体会（但并非出于炫耀）。否则如果只是夸夸其谈的话，我们和那些只会吹牛逼的、只会键政的、互称大佬的群或社区有任何区别吗？如果没有区别，那就没有任何意义，那么我宁愿这个社区不再存在。如果大家有时间有精力的话可以考虑翻译文档，如果会编程的话可以考虑移植软件到 BSD，如果能力更高甚至可以参与系统开发。

### 内容提要

本书是由 ykla 发起，并由 FreeBSD 中文社区的一些群成员参与编写的《FreeBSD 从入门到跑路》。我们尝试从 0 开始，带领普通人走进 FreeBSD 世界。本书充分参考了 FreeBSD HandBook，构建了一个完整、科学的目录体系。本书不是一个大杂烩或是大集合，而是为了构建一个自成体系的一本开源书籍。全书共分 31 章，既强调了学习 FreeBSD 的必要基础也提供了内核设计与实现等专业性较强的教程。本书可作为高等学校“FreeBSD 操作系统”课程的本科生教材，同时也适合相关专业研究生或计算机技术人员参考阅读。

**开源维护与捐赠**：&#x20;

![](.gitbook/assets/proud\_donor.png)\
[点此捐赠 FreeBSD 基金会](https://freebsdfoundation.org/donate)

为了能够更好地维护本书，我们采用了 GitBook 平台来进行协作，并使用 Vuepress 来呈现本书。我们目前的服务器约 5 美元一个月，如果你想为我们提供捐助，请加入我们的 [TG 群](https://t.me/freebsdba) 或者 QQ 群 787969044。如果你也想参与编写，具体请参考 [WIKI](https://github.com/FreeBSD-Ask/FreeBSD-Ask/wiki/%E3%80%8AFreeBSD-%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E8%B7%91%E8%B7%AF%E3%80%8B%E7%BC%96%E8%BE%91%E6%8C%87%E5%8D%97)，关于贡献者名单请参考第 1.17 节。

**贡献者名单**：[https://book.bsdcn.org/di-1-zhang-zou-jin-freebsd/di-1.17-jie-can-kao-zi-liao-yu-gong-xian-zhe-ming-dan](https://book.bsdcn.org/di-1-zhang-zou-jin-freebsd/di-1.17-jie-can-kao-zi-liao-yu-gong-xian-zhe-ming-dan) \
&#x20;**捐赠者名单**：​[https://docs.qq.com/doc/DSXZ1Q1JOenRzUkp4](https://docs.qq.com/doc/DSXZ1Q1JOenRzUkp4) ​

### 意见反馈

由于编写者水平所限，书中缺点和谬误之处自不可免，希望大家随时提出批评意见，以便修正。你可以利用 Github 的各种交互功能与我们联系：Github上提交 Issue、Pull request 或者加入QQ群或Telegram群。\
**网站部署**：Shengyun\
黑名单与社区失信名单：[http://chinafreebsd.org/](http://chinafreebsd.org/)\
_待解决：BiliBili、微信公众号、自动化入群验证与成员管理系统、重修黑名单_

2024 FreeBSD 中文社区 版权所有
