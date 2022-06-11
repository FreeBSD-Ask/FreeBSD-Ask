# FreeBSD 从入门到跑路
## FreeBSD 中文社区（CFC）版权所有 2022

## 概述

请注意，PDF 等电子书版本仅供参考，且存在这样或那样的问题，应该以在线版本为主。

### 格言

恪守古老的法则，追寻真正的自由。

### 本书定位

我们的目标并非是 Handbook 的翻译，而是编写一本类似于《鸟哥的 Linux 私房菜：基础学习篇》+《鸟哥的 Linux 私房菜：服务器架设篇》二合一的基于 FreeBSD 的教程。也就说我们是 Handbook 的超集。

### 编辑指南概要

我们欢迎所有支持 FreeBSD 的人进行编写，并会将你添加到贡献者名单当中。

[详细的编辑指南，点击此处](https://github.com/FreeBSD-Ask/FreeBSD-Ask/wiki)。

## 前言

### FreeBSD 从入门到跑路

本书诞生于 2021 年 12 月 19 日。编写目的是为了 Make FreeBSD Great Again。编写内容为 FreeBSD 的基础与高阶知识。对于章节安排，如果你有一定的 UNIX 基础可以跳过第 一 章，如果你对 FreeBSD 有一定认识，欢迎你加入我们一起编写本书，贡献自己的力量。

### 内容提要

本书是由 ykla 发起，并由 FreeBSD 中文社区的一些群成员参与编写的《FreeBSD 从入门到跑路》。我们尝试从 0 开始，带领普通人走进 FreeBSD 世界，充分参考了 FreeBSD Handbook，构建了一个完整、科学的目录体系。本书不是一个教程的大杂烩亦或者是大集合，而是为了构建一个自成体系的一本开源书籍。全书共分三十章，既强调了学习 FreeBSD 的必要基础也提供了内核设计与实现等专业性较强的教程。本书可作为高等学校“FreeBSD 操作系统”课程的本科生教材，同时也适合相关专业研究生或计算机技术人员参考阅读。

### 开源维护与捐赠

![](./.gitbook/assets/proud_donor.gif)

[点此捐赠 FreeBSD 基金会](https://freebsdfoundation.org/donate)。

为了能够更好地维护本书，我们采用了 Gitbook 平台来进行协作，并使用 Vuepress 来呈现本书。对于无法直接从 GitBook 导出为 PDF 的问题（我们提供了 PDF 的参考版本于 release）以及访问速度慢等问题，我们深感抱歉。我们目前的服务器约 10 美元一个月，如果你想为我们提供捐助，请加入我们的 [TG 群](https://t.me/freebsdba) 或者 QQ 群 319271312。 如果你也想参与编写，具体请参考 [WIKI](https://github.com/FreeBSD-Ask/FreeBSD-Ask/wiki/%E3%80%8AFreeBSD-%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E8%B7%91%E8%B7%AF%E3%80%8B%E7%BC%96%E8%BE%91%E6%8C%87%E5%8D%97)，关于贡献者名单请参考 第一章 第九节。

**捐赠者:**

【FreeBSD 2022 捐赠名单】

<https://docs.qq.com/doc/DSXZ1Q1JOenRzUkp4>

### 激励计划

【FreeBSD 中文社区 2022 教程 激励计划】

<https://docs.qq.com/doc/DSUJsUFBHTnVWQmtS>

### 意见反馈

由于编写者水平所限，书中缺点和谬误之处自不可免，希望同志们随时提出批评意见，以便修正。你可以利用 Github 的各种交互功能与我们联系：提交 Issue、Pull request 或者加入 QQ 群或 TG 群直接联系（yklaxds AT gmail DOT com）等。

### TODO / Wishlist

后续还有很多需要完善的工作，包括不限于:

- FreeBSD 14 统一 shell 为`sh`，教程需要针对其进行统一
- 整理和上传配置文件和环境
- 对教程的格式目录进行优化调整
- 完善目前的空白章节，并对已有内容进行测试校验
- 积极对外宣传并寻求正式出版
- 删改外部引用文字/图片等内容或给出规范化的引用声明
- 因为博通收购 VMware 并作出了诸多商业上的改变，考虑提升 Virtual Box 虚拟机在本文中的地位
- 考虑删除过于主观性或者没有具体根据的个人观点

### 许可证

本书采用 [BSD-3-Clause License](LICENSE/) 许可证开源。我们在编写过程吸收了一些现有的研究成果，在此表示感谢。引用本书内容时，请务必留下我们的原地址——https://book.bsdcn.org 及署名——FreeBSD 中文社区（CFC）。

### 其他

[FreeBSD Handbook 2022 中文翻译项目](https://handbook.bsdcn.org)

微信公众号: freebsdzh （扫码关注）

![](./.gitbook/assets/qrcode_for_gh_3b263cc9b20b_258.jpg)

## 关于

### FreeBSD 中文社区的愿景

我们成立于 2018年3月17日，由贴吧——FreeBSD 吧发展到了 QQ 群（主群 319271312），Telegram 群，乃至于微信群。

我们的成员具有非常大的广泛性和普遍性，能够代表绝大多数 FreeBSD 用户的平均水平：可能根本没有听说过何为 FreeBSD，但这并不影响我们的交流与沟通。也许有人觉得这是浪费时间，但是没有新生力量的培养，何来 FreeBSD 的明天呢？谁不知道新人可能有很多坏习惯呢。

同鲁迅先生说的那样，但愿每个人都是一束光，照亮 FreeBSD 在中国大陆地区前进的光荣的荆棘路。也希望，你可以加入我们，共同组成漫天星光亦或者是星星之火。

无穷的远方，无数的人们，都和我有关。

我曾无数次眺望远山，想要找到一汪清泉，天总是不随人愿，还是没有找到。

我是谁，我们是谁？这个问题永远也不会有结果。

我们选择 FreeBSD，是因为想选择一个清晰、明了、可靠、稳固的一个操作系统在工作上给我们带来收益以及在生活中给我们带来乐趣。当然 FreeBSD 还存在很多问题，有待大家积极发现、探讨、完善，社会在进步，技术在进步，热情丝毫不减在持续，未来越来越美好。
