# FreeBSD 从入门到跑路

## FreeBSD 中文社区 版权所有 2023

> **域名部署**
>
> **当前网站部署的域名为** [**https://book.bsdcn.org**](https://book.bsdcn.org)**，如果当前使用的不是这个域名，请切换到该域名。其他域名不保证可用性。**
>
> **For the English version, please visit** [**https://mfga.bsdcn.org**](https://mfga.bsdcn.org)**. The English version book is a stub. Please help out by expanding it.**

> **PDF 文档**
>
> - 方案① 点击 [https://freebsd.gitbook.io/book/](https://freebsd.gitbook.io/book/)，选择右上角的“导出为 PDF”（需要代理软件）。
> - 方案② 社区成员提供的脚本：
>   
>> 　　https://github.com/safreya/tobook 用于导出跑路的pdf，打印的话比gitbook导出的应该要好点。该脚本运行于 FreeBSD。
>> 
>> 　　先安装需要的东西：
>> ```
>> # pkg install git graphicsmagick
>> ```
>>　　 如需设置 git 代理请按跑路教程提前设置以免无法拉取项目。具体使用方法见该项目的 README.

## 概述

### 格言

恪守古老的法则，追寻真正的自由。

### 本书定位

我们的目标并非是 Handbook 的翻译，而是编写一本类似于《鸟哥的 Linux 私房菜：基础学习篇》+《鸟哥的 Linux 私房菜：服务器架设篇》二合一的基于 FreeBSD 的教程。也即本书是 Handbook 的超集。

### 编辑指南概要

我们欢迎所有支持 FreeBSD 的人进行编写，并会将其添加到贡献者名单当中。

[详细的编辑指南，点击此处](https://github.com/FreeBSD-Ask/FreeBSD-Ask/wiki)

## 前言

### FreeBSD 从入门到跑路

本书诞生于 2021 年 12 月 19 日。编写目的是 Make FreeBSD Great Again。编写内容为 FreeBSD 的基础与进阶知识。对于章节安排，如果你有一定的 UNIX 基础可以跳过第 1 章，如果你对 FreeBSD 有一定认识，欢迎你加入我们一起编写本书，贡献自己的力量。

### 内容提要

本书是由 ykla 发起，并由 FreeBSD 中文社区的一些群成员参与编写的《FreeBSD 从入门到跑路》。我们尝试从 0 开始，带领普通人走进 FreeBSD 世界，充分参考了 FreeBSD Handbook，构建了一个完整、科学的目录体系。本书不是一个教程的大杂烩亦或者是大集合，而是为了构建一个自成体系的一本开源书籍。全书共分 32 章，既强调了学习 FreeBSD 的必要基础也提供了内核设计与实现等专业性较强的教程。本书可作为高等学校“FreeBSD 操作系统”课程的本科生教材，同时也适合相关专业研究生或计算机技术人员参考阅读。

### 开源维护与捐赠

![](./.gitbook/assets/proud_donor.gif)

[点此捐赠 FreeBSD 基金会](https://freebsdfoundation.org/donate)

为了能够更好地维护本书，我们采用了 GitBook 平台来进行协作，并使用 Vuepress 来呈现本书。我们目前的服务器约 5 美元一个月，如果你想为我们提供捐助，请加入我们的 [TG 群](https://t.me/freebsdba) 或者 QQ 群 787969044。如果你也想参与编写，具体请参考 [WIKI](https://github.com/FreeBSD-Ask/FreeBSD-Ask/wiki/%E3%80%8AFreeBSD-%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E8%B7%91%E8%B7%AF%E3%80%8B%E7%BC%96%E8%BE%91%E6%8C%87%E5%8D%97)，关于贡献者名单请参考第 1.9 节。

**捐赠者:**

【FreeBSD 2022 捐赠名单】

[https://docs.qq.com/doc/DSXZ1Q1JOenRzUkp4](https://docs.qq.com/doc/DSXZ1Q1JOenRzUkp4)

### 意见反馈

由于编写者水平所限，书中缺点和谬误之处自不可免，希望同志们随时提出批评意见，以便修正。你可以利用 Github 的各种交互功能与我们联系：提交 Issue、Pull request 或者加入 QQ 群或 TG 群直接联系（ykla AT bsdcn DOT org）等。

### TODO / Wishlist

后续还有很多需要完善的工作，包括不限于:

- FreeBSD 14 shell 被统一为 `sh`，教程需要针对其进行统一
- 整理和上传配置文件和环境
- 对教程的格式目录进行优化调整
- 完善目前的空白章节，并对已有内容进行测试校验
- 积极对外宣传并寻求正式出版
- 删改外部引用文字/图片等内容或给出规范化的引用声明避免版权问题
- ~~因为博通收购 VMware 并作出了诸多商业上的改变，考虑提升 Virtual Box 虚拟机在本文中的地位~~ （VB 虚拟机太难用了，本条作废。）
- 对于过于主观性或者没有根据的观点需要进行删除或补充例证

### 许可证

本书采用 BSD-3-Clause License 许可证开源。我们在编写过程吸收了一些现有的研究成果，在此表示感谢。引用本书内容时，请务必留下我们的原地址——[https://book.bsdcn.org](https://book.bsdcn.org) 及署名——FreeBSD 中文社区（CFC）。

## 关于

### 为什么要编写此书？

本书是为了活跃 FreeBSD 中文社区、助力 FreeBSD 系统生态发展。我们争取做到人人都可以写教程、参与开源协作。没有人强迫您阅读本书，所以也请您不要诋毁我们。FreeBSD 中国境内的社区这几年一本教程都没有，这不是我们想看到的。请不做事的人不要去嘲讽正在做事的。感谢您的体谅！

### FreeBSD 中文社区的愿景

我们成立于 2018 年 3 月 17 日，由贴吧——FreeBSD 吧发展到了 QQ 群（主群 787969044），Telegram 群，至于微信群。

我们的成员具有非常大的广泛性和普遍性，能够代表绝大多数 FreeBSD 用户的平均水平：他们可能根本没有听说过何为 FreeBSD，但这并不影响我们的交流与沟通。也许有人觉得这是浪费时间，但是没有新生力量的培养，何来 FreeBSD 的明天呢？谁不知道新人可能有很多坏习惯呢。

同鲁迅先生说的那样，但愿每个人都是一束光，照亮 FreeBSD 在中国大陆地区前进的光荣的荆棘路。也希望，你可以加入我们，共同组成漫天星光亦或者是莹莹之火。

无穷的远方，无数的人们，都和我有关。

我曾无数次眺望远山，想要找到一汪清泉，天总是不遂人愿，仍旧是没有找到。

我们是谁？我们从何而来？我们将去往何方？这些问题永远也不会有结果。

我们选择 FreeBSD，是因为想选择一个清晰、明了、可靠、稳固的一个操作系统在工作上给我们带来收益以及在生活中给我们带来乐趣。当然 FreeBSD 还存在很多问题，有待大家积极发现、探讨、完善，社会在进步，技术在进步，热情丝毫不减在持续，未来越来越美好。

### 其他

|               资源               |                                      链接                                      |
| :------------------------------: | :----------------------------------------------------------------------------: |
|           Telegram 群            |                [https://t.me/freebsdba](https://t.me/freebsdba)                |
|              QQ 群               |                                   787969044                                    |
|        Handbook 最新翻译         |            [https://handbook.bsdcn.org](https://handbook.bsdcn.org)            |
| FreeBSD Port 开发者手册 最新翻译 |    [https://porters-handbook.bsdcn.org](https://porters-handbook.bsdcn.org)    |
|         FreeBSD 入门书籍         |                [https://book.bsdcn.org](https://book.bsdcn.org)                |
|         BiliBili【B 站】         | [https://space.bilibili.com/2120246893](https://space.bilibili.com/2120246893) |
|            微信公众号            |                                   freebsdzh                                    |

微信公众号: freebsdzh （扫码关注）

![](./.gitbook/assets/qrcode_for_gh_3b263cc9b20b_258.jpg)

### 网站部署&维护

Shengyun

### 黑名单与社区失信名单

见 [http://chinafreebsd.org/](http://chinafreebsd.org/)。
