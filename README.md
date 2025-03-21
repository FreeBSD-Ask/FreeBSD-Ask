# FreeBSD 从入门到跑路

~~为了拯救即将归档（Archived）的 FreeBSD······我们决定写一本书。[^1]~~

FreeBSD 是真正自由（Liberal）的**操作系统**，在这个大流变的世界中仍然坚守 BSD UNIX 哲学——恪守古老的法则，追寻真正的自由。

## 关于

**首要**联系方式：**QQ 群**：787969044

微信群：出于微信的封闭性，你须先加入 QQ 群，再联系 QQ 群主方可加入

Discord (Non-Chinese users, please join this group.)：<https://discord.gg/n5wu65Z6tw>（需要代理。可直接通过网页使用，无需安装任何软件）

Telegram：[https://t.me/oh_my_BSD](https://t.me/oh_my_BSD)（需要代理）

## 历史

《FreeBSD 从入门到跑路》诞生于 2021 年 12 月 19 日，由 FreeBSD 中文社区（CFC）ykla 发起。

## 内容提要

本书旨在敉平入门到进阶之间的台阶，与你一道进入这片开源世界。

## 贡献指南

如果你想让你的教程出现在本书中，你可以这样做：

<details> 
<summary>点击此处展开贡献指南详情</summary>

- 如果你熟悉 GitHub，可以点击电脑端右侧的“编辑此页”，进入项目进行操作。整个项目使用 Markdown 语法 +  Gitbook，简单易上手（具体详见项目 WiKi）；
- 如果以上有困难，你还可以发 PDF、Word 或者 TXT 给我。请将文件发送至电子邮件 `yklaxds@gmail.com`；如果有视频教程，以各大云盘链接为宜。

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

唯一要注意的是，你的教程会以本项目的开源许可证（CC BY 4.0）进行发布。


### 如何使用 git 拉取本项目

本项目太大，拉取时可能会导致缓冲区溢出，可改变 git 配置文件，以实现对缓冲区的扩大：

以下是一个可用的 `.gitconfig` 的文件示例：

```json
[filter "lfs"]
	required = true
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
	process = git-lfs filter-process
[user]
	name = # 你的用户名
	email = # 你的邮箱
	signingkey = # 你的密钥 ID，使用密钥签名时需要
[commit]
  gpgsign = true # 使用密钥签名时需要
[core]
	autocrlf = true
[http]
	proxy = http://localhost:7890 # 设置使用 http 代理
	postBuffer = 1048576000 # 扩大缓冲区，约 1 GB
	maxRequestBuffer = 1048576000 # 扩大缓冲区，约 1 GB
```

</pre> </details>

### 意见反馈

由于编写者水平所限，书中缺点和谬误之处自不可免。

如遇本站直接相关问题：如错别字、过时、网站配色、错误、投稿、翻译等问题，请直接发送邮件至 `yklaxds@gmail.com`（优先）或联系 QQ 群群主。如果可以的话，欢迎 PR。在桌面端网页右侧有当前页面的 GitHub 编辑地址。


## ToDo

### 本季度任务

- [ ] 重写“第 1.4 节 Linux 用户迁移指南”
- [ ] 重写“第 3.2 节 FreeBSD 换源方式”
- [ ] 重写“第 4.1 节 Xorg & 显卡驱动”
- [ ] 格式化“第 5.1 节 输入法与环境变量”
- [ ] 格式化“第 5.4 节 五笔输入法”
- [ ] 重写“第 5.7 节 更换字体”
- [ ] 测试“第 6.7 节 ZFS 磁盘加解密”
- [ ] 格式化“第 15.1 节 网络参数配置命令”
- [ ] 格式化“第 14.4 节 蓝牙”
- [ ] 测试“第 16.2 节 MinIO 对象存储服务”
- [ ] 格式化“第 16.4 节 时间服务”
- [ ] 格式化“第 16.8 节 NFS 服务器”
- [ ] 重写“第 6.6 节 Ext 2/3/4 等文件系统”
- [ ] 更新“第 16.1 节 FTP 服务器”（可能性不大，我不懂）
- [ ] 测试“第 17.7 节 Telegraf+InfluxDB+Grafana 监控平台”（仅测试）
- [ ] 整理第 18 章
  - [ ] 将“第 18.4 节 USB 网卡与 WiFi”删除或合并
  - [ ] 精简章节
- [ ] 格式化“第 21.12 节 高级教程：Linux 兼容层与 Jail”
- [ ] 整理“第 22.12 节 安装 code-server 和 clangd”

### 开放任务

<details> 
<summary>点击此处展开 FreeBSD ToDo</summary>

- [ ] 整合现有的上游 FreeBSD 社区文章
- [ ] fail2ban（须适配自带的几种防火墙）
- [ ] 删除或重写“第 9.2 节 jail 更新”
- [ ] 使用关键字 `enable`、`disable`、`delete` 替代旧式 sysrc 写法
- [X] 介绍伯克利大学与校训思想
- [ ] 从 FreeBSD 期刊引入 IPv6  教程
- [ ] Makefile
- [X] 从 FreeBSD 期刊引入 Zabbix 教程
- [X] gitlab-ee
- [ ] 为所有需要额外配置的文件，使用命令 `pkg info -D` 列出正文如此配置之原因
- [ ] 重写“第 4.1 节 安装显卡驱动及 Xorg（必看）”，尤其是 N 卡驱动部分，目前是无效的，必须重写
- [X] `pkg autoremove`（会把整个系统都带走）及 `pkg delete`（破坏依赖）都不是正经的卸载软件及孤包依赖的方法，`pkg-rmleaf` 亦已过时无法使用。需要找到正常合理的卸载软件包的方法。`pkg_rmleaves` 似乎可以
- [X] 补充一些 WinSCP、XShell 的替代工具，避免单一来源
  - [ ] 找到一款我认为能替代二者的工具
- [X] 将全书主观性文字转换为思考题供读者自行思考与判断
- [ ] 更新“第 16.7 节 Samba 服务器”
- [ ] steam
- [ ] Wayland 化桌面
- [ ] Bhyve
  - [ ] `sysutils/bhyvemgr` GUI
  - [X] Windows 11
  - [ ] ~~Windows XP ?~~
  - [X] Ubuntu
  - [X] FreeBSD
  - [ ] ~~MacOS ?~~
- [ ] 删除重写部分来源于网络的错误内容
  - [ ] 防火墙
  - [ ] jail
  - [ ] 用户与权限
  - [ ] GEOM
  - [ ] DTrace
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
  - [X] 我的世界（服务器、客户端）
- [ ] ZFS（可以参考 [Oracle Solaris 管理：ZFS 文件系统](https://docs.oracle.com/cd/E26926_01/html/E25826/index.html)）
  - [ ] ZFS 共享
  - [ ] ZFS 加密
  - [ ] ZFS 调优
  - [ ] ZFS iSCSI
  - [ ] 补充 ZFS 委托管理
  - [ ] 归档快照和根池恢复
  - [ ] ZFS 故障排除
  - [ ] ZFS 克隆
  - [ ] ZFS 与 ACL
  - [ ] ZFS 高级主题
  - [ ] ZFS 池管理
  - [ ] ZFS 与 RAID
- [X] 将小说诗歌杂记等与 FreeBSD 无关内容下线
- [ ] 参照 FreeBSD handbook、鸟哥的 Linux 私房菜服务器篇改写服务器相关章节
  - [ ] BSD 常用网络命令
  - [ ] 链路聚合
  - [ ] IPv6 配置
    - [ ] WiFi
    - [ ] 以太网
  - [ ] DNS
  - [ ] DHCP
  - [ ] 更新：第 17.8 节 PostgreSQL 与 pgAdmin4
  - [ ] NTP
  - [ ] Redis
  - [ ] NFS
  - [ ] iSCSI
  - [ ] Postfix
  - [ ] LDAP（OpenLDAP，也许可以参考 [WiKi LDAP/Setup](https://wiki.freebsd.org/LDAP/Setup)）
- [X] NextCloud（最好基于 PostgreSQL）
- [ ] KDE6
  - [X] 基于 Xorg
  - [X] 基于 Wayland（部分完成）
- [ ] Wayland
  - [ ] 远程软件
  - [ ] KDE6
  - [ ] Gnome
  - [ ] 经典登录管理器
  - [ ] 窗口管理器
  - [ ] 基础知识
- [ ] FreeBSD 路由器
- [ ] Wine
  - [ ] 填充实质性内容
  - [ ] 64 位 Windows 程序（64 位 Wine？）
- [ ] FreeBSD 安全加固（可参照 [FreeBSD 14 CIS 基准](https://www.cisecurity.org/cis-benchmarks)，[阿里云盘](https://www.alipan.com/s/9Vced5R3Wit)）
  - [ ] 云服务器
  - [ ] 路由器
  - [ ] 小主机
  - [ ] 桌面用户
  - [ ] 虚拟机
  - [ ] 限制端口
  - [ ] 防火墙
- [X] 微信
  - [ ] 微信双开
- [X] WPS
  - [X] 解决 fcitx、fcitx5 输入法不能输入的问题
- [ ] HTTP代理
  - [ ] 测试 [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev) 能否在 FreeBSD 上正常运行
  - [ ] 测试 [V2raya](https://github.com/v2rayA/v2rayA) 能否在 FreeBSD 上正常运行
- [ ] 浏览器
  - [X] Google Chrome / Chromium Google 账号同步



</pre> </details>

<details> 
<summary>点击此处展开 OpenBSD ToDo</summary>
  
- [ ] OpenBSD
  - [ ] KDE5（现在 UEFI 下进入桌面黑屏）
  - [ ] QQ？原生可能吗
  - [ ] 微信？原生可能吗
  - [ ] Wine
  - [ ] OpenBSD 调优
  - [ ] OpenBSD 安全加固
  - [ ] 网络
    - [ ] DNS
    - [ ] FTP
    - [ ] NTP
    - [ ] DHCP
    - [ ] 各式代理
    - [ ] 邮件服务器
    - [ ] PF 等防火墙
    - [ ] IPv6
    - [ ] 常用网络命令
  - [ ] OpenBSD 路由器（可参考 [OpenBSD 路由器指南](https://translated-articles.bsdcn.org/2023-nian-9-yue/openbsd-router-guide)）
    - [ ] WiFi
    - [ ] 链路聚合
    - [ ] 路由表
    - [ ] 默认路由
  - [ ] OpenBSD 基础知识
    - [ ] 版本概况
    - [ ] 开发宗旨与项目目标
    - [ ] 性能参数
    - [ ] 注意事项
    - [ ] 跟踪新版本
    - [ ] pkgsrc
  - [ ] 嵌入式

</pre> </details>

<details> 
<summary>点击此处展开 NetBSD ToDo</summary>
  
- [ ] NetBSD
  - [ ] NetBSD 调优
  - [ ] 桌面
    - [ ] 火狐浏览器
    - [ ] Chromium
    - [ ] KDE 4（现在进入桌面黑屏）
    - [ ] QQ
    - [ ] 微信
    - [ ] Wine
  - [ ] 树莓派 4 & 5
  - [ ] NetBSD 安全加固
  - [ ] NetBSD 基础知识
    - [ ] 版本概况
    - [ ] 开发宗旨与项目目标
    - [ ] 注意事项
    - [ ] 跟踪新版本
    - [ ] pkgsrc
  - [ ] 嵌入式  
  - [ ] 网络
    - [ ] DNS
    - [ ] FTP
    - [ ] NTP
    - [ ] DHCP
    - [ ] 各式代理
    - [ ] 邮件服务器
    - [ ] PF 等防火墙
    - [ ] IPv6
    - [ ] 常用网络命令
  - [ ] NetBSD 路由器
    - [ ] WiFi
    - [ ] 链路聚合
    - [ ] 路由表
    - [ ] 默认路由

</pre> </details>

<details> 
<summary>点击此处展开 DragonFlyBSD ToDo</summary>
  
- [ ] DragonFlyBSD
  - [ ] DragonFlyBSD调优
  - [ ] 桌面
    - [ ] KDE5
    - [ ] Gnome
    - [ ] QQ
    - [ ] 微信
    - [ ] Wine
    - [ ] XFCE
    - [ ] 火狐浏览器
    - [ ] Chromium
  - [ ] DragonFlyBSD 安全加固
  - [ ] DragonFlyBSD 基础知识
    - [ ] 版本概况
    - [ ] 开发宗旨与项目目标
    - [ ] 注意事项
    - [ ] 跟踪新版本
    - [ ] pkgsrc
    - [ ] FreeBSD Ports
  - [ ] 换源与包管理器

</pre> </details>


## PDF 文档导出流程

可使用由 [safreya](https://github.com/safreya) 编写的脚本：<https://github.com/FreeBSD-Ask/gitbook-pdf-export> 来导出本书的 PDF 文档。

该脚本使用 Python3 编写，仅在 Windows 10、FreeBSD 14.2 上测试过。具体使用方法见该项目的 README。


## 捐赠

资金有余力者请捐给 FreeBSD 基金会吧！

FreeBSD 基金会（501(c)(3)）日常年份收到的捐款仅有 Linux 基金会（501(c)(6)）的千分之五。因此亦十分需要个人捐款。

![](.gitbook/assets/proud_donor.png)

[点此捐赠 FreeBSD 基金会](https://freebsdfoundation.org/donate)

需要你有 Visa 信用卡：若直接提交无法支付，请使用捐赠页面的 `Amazon Pay` 或 `Google Pay`，经测试均可以顺利支付。

## 授权许可

本项目使用《CC BY 4.0 署名 4.0 协议国际版》，具体细则参见 <https://github.com/FreeBSD-Ask/FreeBSD-Ask> 项目下的 `LICENSE.md` 文件。

![CC BY](.gitbook/assets/by.png)

[^1]: 参见 [为了保护我们心爱的ooo……成为偶像！](https://mobile.moegirl.org.cn/%E4%B8%BA%E4%BA%86%E4%BF%9D%E6%8A%A4%E6%88%91%E4%BB%AC%E5%BF%83%E7%88%B1%E7%9A%84ooo%E2%80%A6%E2%80%A6%E6%88%90%E4%B8%BA%E5%81%B6%E5%83%8F%EF%BC%81)
---

![](.gitbook/assets/ai.png)

[Not By AI](https://notbyai.fyi/cn/)
