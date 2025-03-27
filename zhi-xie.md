# 致谢

~~本书初版架构基于贴吧用户“Smile_Zheng”《操作系统笔记》分享的[早期版本](https://tieba.baidu.com/p/7424071955)。主要引用了防火墙章节、用户与权限。~~

据查，其主要引用自《FreeBSD 技术内幕》（*[FreeBSD Unleashed](https://www.amazon.com/FreeBSD-Unleashed-2nd-Brian-Tiemann/dp/0672324563)*），ISBN 9787111102010，机械工业出版社，2002，作者是 Brian Tiemann、Michael Urban，真实译者不详（智慧东方工作室）。

## 致歉

目前，在本项目中某些章节还引用了或完全就是网络上其他作者的教程。

由于历史问题和对许可证的非标准引用（主要是认识不足），没能按要求作者的要求注明来源及作者。再此表示歉意。如果您对此有不同看法或要求，请联系 `yklaxds@gmail.com`。

作为项目目标的一部分，我们会尽快重写所有相关部分内容及对作者和项目进行规范化标注。

## 项目部署与维护

《FreeBSD 从入门到跑路》项目早期发起人为 [clean-master 清理大师](https://github.com/clean-master)。他自费创建了域名 `freebsdcn.org`（已不再使用）以及目前仍在使用的 <https://bsdcn.org> 主页。他鼓励 ykla 创建一个项目来维护相关的 FreeBSD 教程。

[Roberta Wheeler](https://github.com/rowheel) 自费部署维护过《FreeBSD 从入门到跑路》项目使用的服务器（目前已切换至免费的 GitBook），并撰写了部分文章。

[safreya](https://github.com/safreya) 曾撰写过 2 款用于导出本项目 PDF 的开源工具（目前仍在使用），并撰写了大量文章。

Ubuntu 吧前吧主 Simple 曾建议修改项目的章节文件名与许可协议，这提高了本项目的可维护性。

目前《FreeBSD 从入门到跑路》项目的主要非技术维护者为 [Voosk](https://github.com/MilkGolium)，他也撰写了部分文章。

目前《FreeBSD 从入门到跑路》项目的主要技术维护者为  [ykla](https://github.com/ykla)。

## 文档贡献者名单

>**注意**
>
>如果缺少了你的信息或者不想被列出，请发起 Issue。

按 A-Z 排序：

- [5gura](https://github.com/5gura)  
- Alex6357 [(GitHub)](https://github.com/Alex6357)  
- April Simone🍥  
- [bduath](https://github.com/bduath)  
- [blu10ph](https://github.com/blu10ph)  
- [bsdwiki](https://github.com/bsdwiki)  
- [Dedicatus5457](https://github.com/Dedicatus5457)  
- DogeW  
- [dongdigua](https://github.com/dongdigua)  
- [fanyang1997](https://github.com/fanyang1997)  
- [fjh1997](https://github.com/fjh1997)  
- freyr  
- gua-leopard [(GitHub)](https://github.com/gua-leopard)  
- hangyongcong  
- heguru5  
- isNijikawa  
- Jack  
- kuntop  
- [李大鹏](https://dapeng.li/)  
- liguangsheng [(GitHub)](https://github.com/liguangsheng)  
- livrth  
- [凌莞](https://clansty.com)  
- [柳离枝](https://github.com/liulitchi)  
- matatabi-wang  
- 墨子  
- [mxdyeah / mxdabc](https://mxdyeah.top/)  
- [nerdroychan](https://github.com/nerdroychan)  
- [number201724](https://github.com/number201724)  
- [orzyyyy](https://github.com/orzyyyy)  
- [peiyafei](https://github.com/peiyafei)  
- [pengxingwei](https://github.com/pengxingwei)  
- [puffinjiang](https://github.com/puffinjiang)  
- 清和 [(GitHub)](https://github.com/qinghecyn)  
- 清热解毒口服液  
- [Rintim](https://github.com/Rintim)  
- [ruur](https://github.com/ruur)  
- [Sayunosyjou](https://github.com/Sayunosyjou)  
- 施主  
- [Suyun114](https://github.com/Suyun114)  
- [tergel93](https://github.com/tergel93)  
- [tomblackwhite](https://github.com/tomblackwhite)  
- 艳阳天  
- [wyathou](https://github.com/wyathou)  
- X-Ray  
- 心即理物即心  
- 仰望天空  
- [Zomby7e](https://github.com/Zomby7e)  
- 地铁卡  
- 兜率  
- 极品盗号  
- [魔王酱](https://github.com/maou-sama-desu)  
- 🎀🌸星不萌🌸🎀（贴吧账户）  
- 雨天
  
## 开源项目

本项目还使用了以下相关的 Github Action 自动化工具或项目，我们对其作者表示感谢：

- [actions/checkout](https://github.com/actions/checkout)，用于 Git 检出项目
- [actions/setup-node](https://github.com/actions/setup-node)，用于配置 Node.js 环境
- [peter-evans/create-pull-request](https://github.com/peter-evans/create-pull-request)，用于创建 PR
- [lycheeverse/lychee-action](https://github.com/lycheeverse/lychee-action)，用于检查失效链接及文件
- [peter-evans/create-issue-from-file](https://github.com/peter-evans/create-issue-from-file)，用于创建 Issue
- [DavidAnson/markdownlint-cli2-action](https://github.com/DavidAnson/markdownlint-cli2-action)，用于 Markdown 规范化
- [tj-actions/changed-files](https://github.com/tj-actions/changed-files)，用于检查文件变动
- [autocorrect](https://github.com/huacnlee/autocorrect)，用于 Markdown 规范化，主要是加空格
- [md-padding](https://github.com/harttle/md-padding)，用于 Markdown 规范化，主要是加空格

---

本项目主要托管在 [GitHub](https://GitHub.com)。

本项目还受到了 [GitBook 开源计划](https://www.gitbook.com/solutions/open-source)的赞助。本项目的网站由其提供。


