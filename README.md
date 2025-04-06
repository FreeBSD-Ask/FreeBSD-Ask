# FreeBSD 从入门到跑路

~~[为了拯救即将归档（Archived）的 FreeBSD······我们决定写一本书。](https://mzh.moegirl.org.cn/%E4%B8%BA%E4%BA%86%E4%BF%9D%E6%8A%A4%E6%88%91%E4%BB%AC%E5%BF%83%E7%88%B1%E7%9A%84ooo%E2%80%A6%E2%80%A6%E6%88%90%E4%B8%BA%E5%81%B6%E5%83%8F%EF%BC%81)~~

FreeBSD 是真正自由（Liberty）的**操作系统**，在这波谲云诡的世界中仍然坚守 BSD UNIX 哲学——恪守古老的法则，追寻真正的自由。

内容提要：本书旨在敉平入门到进阶之间的台阶，与你一道进入这片开源世界。

## 关于

本书官方部署站点：

- <https://book.bsdcn.org>，使用 GitBook，并集成了其他相关页面
- <https://docs.bsdcn.org>，使用 VitePress，仅本书

### 加入 FreeBSD 中文社区（CFC）

- **首要**联系方式为 **QQ 群**：787969044

  - 微信群：出于微信的封闭性，你须先加入 QQ 群，再联系 QQ 群主方可加入

---

- Discord：<https://discord.gg/n5wu65Z6tw>（需要代理。可直接通过网页使用，无需安装任何软件）

- Telegram：[https://t.me/oh_my_BSD](https://t.me/oh_my_BSD)（需要代理）

### 历史

《FreeBSD 从入门到跑路》诞生于 2021 年 3 月 14 日（依据 [clean-master/freebsdcn](https://github.com/clean-master/freebsdcn/graphs/contributors) 项目的创建时间，其同天产生了此书原型），由 FreeBSD 中文社区（CFC）[clean-master 清理大师](https://github.com/clean-master)发起，[ykla](https://github.com/ykla) 在翌日夜间完成了教程的初步整理与发布。

### 意见反馈

由于编写者水平所限，书中缺点和谬误之处自不可免。

如遇本站直接相关问题：请直接发送邮件至 `yklaxds@gmail.com`（优先）或联系 QQ 群群主。如果可以的话，欢迎 PR。在桌面端网页右下方或底部左下方有当前页面的 GitHub 编辑地址。

## ToDo 待办事项

### 贡献指南与开放任务

参见 [贡献指南与开放任务](https://freebsd.gitbook.io/cfc/she-qu-jian-she/renwu)

### 2025 年第二季度 ToDo List

- [ ] 在每节最后嵌入（或与故障排除合并为）“故障排除与未竟事宜”，将现存的问题和改进的方向/建议或谜团留置其中，以期后人的智慧。
- [ ] 解释全书所有命令和选项
  - [ ] 含义
  - [ ] 历史（如必要）
  - [ ] 艺术（如必要）
  - [ ] 哲学（如必要）
- [ ] 重写“第 3.2 节 FreeBSD 换源方式”
- [ ] 重写“第 4.1 节 Xorg & 显卡驱动”
- [ ] 重写“第 5.7 节 更换字体”
- [ ] 重写第 20 章
  - [X] 尝试播放电视剧、动漫（10bit）
  - [X] 尝试播放 ac4（m4a）、flac 音乐
  - [ ] 命令行播放音乐
  - [ ] 命令行播放视频
  - [X] 测试全章
  - [X] 全章补图
- [ ] 重写防火墙相关章节（尽力而为，我不熟）
  - [ ] PF
  - [ ] IPF
  - [ ] IPFW
- [X] 格式化“第 5.1 节 输入法与环境变量”
- [X] 格式化“第 21.12 节 高级教程：Linux 兼容层与 Jail”
- [ ] 撰写一篇文章，主题为“UNIX 哲学”
- [X] 测评各种尚存的桌面版本 FreeBSD ~~也许没必要？已有 [FreeBSD 桌面发行版](https://freebsd-journal-cn.bsdcn.org/20200506-wang-luo-xing-neng/desktop)~~ 这篇文章实在无诚意和实质性内容
  - [X] [GhostBSD](https://www.ghostbsd.org/)
  - [X] [NomadBSD](https://nomadbsd.org/)
  - [X] [helloSystem](https://hellosystem.github.io/docs/)
  - [X] [MidnightBSD](https://www.midnightbsd.org/)
- [ ] 基础知识
  - [ ] 登出账号
  - [ ] 命令行关机
  - [ ] 命令行重启
- [ ] 给出更多有意义和价值的参考文献，不局限于计算机科学

## PDF 文档导出

可使用由 [safreya](https://github.com/safreya) 编写的[脚本](https://github.com/FreeBSD-Ask/gitbook-pdf-export)来导出本书的 PDF 文档。

此外，还会每天通过 GitHub Action 导出 PDF 于 [releases](https://github.com/FreeBSD-Ask/FreeBSD-Ask/releases)（也许需要代理）。

## 捐赠

资金有余力者请捐给 FreeBSD 基金会吧！如果你觉得有帮助，可以给 [GitHub 项目](https://github.com/FreeBSD-Ask)加颗 ⭐。

---

![](.gitbook/assets/proud_donor.png)

[点此捐赠 FreeBSD 基金会](https://freebsdfoundation.org/donate)

需要你有 VISA 信用卡：请使用捐赠页面“Click & Pledge”下的 `Amazon Pay` 或 `Google Pay`，经测试均可以顺利支付。

## 授权许可

本项目使用《CC BY 4.0 署名 4.0 协议国际版》，具体细则参见[本项目](https://github.com/FreeBSD-Ask)下的 `LICENSE.md` 文件。

![CC BY](.gitbook/assets/by.png)

---

![](.gitbook/assets/ai.png)

[Not By AI](https://notbyai.fyi/cn/)
