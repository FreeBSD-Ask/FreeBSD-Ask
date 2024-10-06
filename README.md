# FreeBSD 从入门到跑路

~~为了拯救即将归档（Archived）的 FreeBSD.....决定写一本书~~

## 贡献指南

如果你想让你的教程出现在本书中，你可以这样做：

- 如果你熟悉 GitHub，可以点击电脑端右侧的“编辑此页”，进入项目进行操作。整个项目使用 Markdown 语法 +  Gitbook，简单易上手（具体详见项目 WiKi）；
- 如果以上有困难，你还可以发 PDF、Word 或者 TXT 给我。请将文件发送至 `yklaxds@gmail.com`；如果有视频教程，以各大云盘链接为宜。

本书现接受以下内容：

- 一切与 BSD 相关（包括不限于 FreeBSD，OpenBSD，NetBSD）以及各种体系结构的教程。你既可以扩充当前教程，也可以新建一节；
- 下方的 ToDo 列表；
- 你亦可在文学故事章节分享你与 BSD 的故事，你的个人心得体会。

你为什么要这样做？

- **可访问性**：随处可见，无需再到处寻找；
- **可复现性**：任何人都能轻松复现成果，显著提高工作和学习效率；
- **规模化测试**：可以对教程进行系统化测试，找出最优解；
- **社区支持**：社区将持续维护教程的可用性，并定期更新软件和教程版本；
- **节省时间**：当本教程内容愈加丰富，你花在网络索引上的无效时间就会越少；
- **互惠互利**：合并教程践行了开源哲学，惠及着无穷的远方，无数的人们；
- **增强协作**：促进 FreeBSD 在中国乃至亚洲、全世界的发展；
- **便于反馈**：快速迭代教程，并验证每一步骤的正确性与合理性；
- **易于分享**：本项目既支持在线浏览亦支持 PDF 文档导出，宽松的许可证、简单的项目结构允许自由部署。

唯一要注意的是，你的教程会以本项目的开源许可证（BSD）进行发布。

### 意见反馈

由于编写者水平所限，书中缺点和谬误之处自不可免，希望大家随时提出批评意见，以便修正。你可以利用 Github 提交 Issue 或者发邮件至 `yklaxds@gmail.com`。

## 现成的虚拟机镜像体验（本书自制）

具体详情请参见第 2 章节。

```json
14.1  磁力链接  magnet:?xt=urn:btih:496C343387D74457E441CAFA93B302E791F62924

15.0  磁力链接  magnet:?xt=urn:btih:CBD49C71E87BC0B1406710A437E7135EF3D8C155
```
## ToDo

### 需要

- [ ] 整合现有的上游 FreeBSD 社区文章
- [ ] `pkg autoremove`（会把整个系统都带走）及 `pkg delete`（破坏依赖）都不是正经的卸载软件及孤包依赖的方法，`pkg-rmleaf` 亦已过时无法使用。需要找到正常合理的卸载软件包的方法。`pkg_rmleaves` 似乎可以
- [X] 补充一些 WinSCP、XShell 的替代工具，避免单一来源
  - [ ] 找到一款我认为能替代二者的工具
- [X] 将全书主观性文字转换为思考题供读者自行思考与判断
- [ ] 删除重写部分来源于网络的错误内容
  - [ ] 防火墙
  - [ ] jail
  - [ ] 用户与权限
  - [ ] geom 合并到第 6 章
  - [ ] 删除无实际内容的 DTrace 章节
- [ ] 完全面向新手介绍 FreeBSD
  - [ ] 对比 Linux、Windows、MacOS、Android 和 IOS 等常见操作系统
  - [ ] 客观化论证
    - [ ] 删除冗余，精简论证
    - [X] 补充参考文献
    - [ ] 客观陈述不足，面对现实
- [X] 重写第一章，考虑加入硬件常识，整合现有的树莓派章节相关内容
- [ ] 文学故事章节需要重写
  - [ ] 说明真实看法，避免曲解和误导，旨在强调对 Linux 和开源没有恶意
  - [ ] 删除冗余，精简论证
  - [ ] 客观化
    - [ ] 名人名言
    - [ ] 图片
    - [ ] 视频
    - [X] 参考文献
    - [ ] 说明各大 Linux 操作系统的优势
- [ ] 补充一些实验
  - [ ] 我的世界（服务器、客户端）


### 也许需要

- [X] 将小说诗歌杂记等与 FreeBSD 无关内容下线
- [ ] 参照 FreeBSD handbook、鸟哥的 Linux 私房菜服务器篇改写服务器相关章节
- [ ] KDE6
  - [ ] 基于 Xorg
  - [ ] 基于 Wayland

## PDF 文档

> **PDF 文档导出流程**
>
> - 使用由 [safreya](https://github.com/safreya) 提供的脚本：
>   
>> 　　<https://github.com/FreeBSD-Ask/gitbook-pdf-export> 用于导出本书的 PDF 文档。该脚本使用 Python 3 编写，仅在 Windows 10、FreeBSD 14 上测试过。
>> 
>> 具体使用方法见该项目的 README.

## 概述

FreeBSD 从入门到跑路诞生于 2021 年 12 月 19 日。

本书定位：编写一本 FreeBSD 版本的《鸟哥的 Linux 私房菜：基础学习篇》&《鸟哥的 Linux 私房菜：服务器架设篇》。

**编辑指南概要**：我们欢迎所有支持 FreeBSD 的人进行编写，并会将其列入贡献者名单。

## 资源

QQ 群：787969044（须答题验证）

微信公众号: rpicn2025 （扫码关注）

![](./.gitbook/assets/qr.png)

Telegram 群组：[https://t.me/oh_my_BSD](https://t.me/oh_my_BSD)

Skype: [https://join.skype.com/xktkQtXZopfv](https://join.skype.com/xktkQtXZopfv)

FreeBSD 需要兼容层才能运行 QQ；Telegram 可原生运行；Skype 可使用 pidgin+ 插件 [net-im/pidgin-skypeweb](https://forums.freebsd.org/threads/skype.66115/)

HandBook 翻译：[https://handbook.bsdcn.org](https://handbook.bsdcn.org/)

FreeBSD Port 开发者手册翻译：[https://porters-handbook.bsdcn.org](https://porters-handbook.bsdcn.org/)

FreeBSD 入门书籍：[https://book.bsdcn.org](https://book.bsdcn.org/)

FreeBSD 中文 man 手册：[https://man.bsdcn.org](https://man.bsdcn.org/)

## 内容提要

《FreeBSD 从入门到跑路》 由 FreeBSD 中文社区发起。我们尝试从 0 开始，和所有人一同徜徉 FreeBSD 世界。

**开源维护与捐赠**：

![](.gitbook/assets/proud_donor.png)

[点此捐赠 FreeBSD 基金会](https://freebsdfoundation.org/donate)

~~为了能够更好地维护本书，我们采用了 GitBook 平台来进行协作，并使用 Vuepress 来呈现本书。我们目前的服务器约 5 美元一个月，如果你想为我们提供捐助，请加入我们的 [TG 群](https://t.me/oh_my_BSD) 或者 QQ 群 787969044。如果你也想参与编写，具体请参考 [WIKI](https://github.com/FreeBSD-Ask/FreeBSD-Ask/wiki/%E3%80%8AFreeBSD-%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E8%B7%91%E8%B7%AF%E3%80%8B%E7%BC%96%E8%BE%91%E6%8C%87%E5%8D%97)。~~ 由于没人出钱，故已退回 GitBook。这也没什么问题，能够更加专注于内容，而不是每天都在改没有意义的目录和各种配置文件。有多的钱请捐给 FreeBSD 基金会吧。

