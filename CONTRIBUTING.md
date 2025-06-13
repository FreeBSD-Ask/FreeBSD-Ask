# 贡献指南与开放任务

细节参见 <https://github.com/FreeBSD-Ask/FreeBSD-Ask/wiki>。

## 贡献指南
如果你想让你的教程出现在本书中，你可以这样做：


- 如果你熟悉 GitHub，可以点击电脑端右侧的“编辑此页”，进入项目进行操作。整个项目使用 Markdown 语法 +  Gitbook，简单易上手（具体详见项目 WiKi）；
- 如果以上有困难，你还可以发 PDF、Word 或者 TXT 给我。请将文件发送至电子邮件 `yklaxds@gmail.com`；如果有视频教程，以各大云盘链接为宜。

本书现接受以下内容：

- 一切与 BSD 相关（包括不限于 FreeBSD，OpenBSD，NetBSD）以及各种体系结构的教程。你既可以扩充当前教程，也可以新建一节；
- 下方的 ToDo 列表；
- 你亦可在文学故事章节分享你与 BSD 的故事，你的个人心得体会。

### 如何使用 git 拉取本项目

本项目太大，拉取时可能会导致缓冲区溢出，可改变 git 配置文件，以实现对缓冲区的扩大：

以下是一个可用的 `.gitconfig` 的文件示例：

```ini
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
	autocrlf = true # 自动调整末尾回车与换行
[http]
	proxy = http://localhost:7890 # 设置使用 http 代理
	postBuffer = 1048576000 # 扩大缓冲区，约 1 GB
	maxRequestBuffer = 1048576000 # 扩大缓冲区，约 1 GB
```

## 开放任务

### 总体目标

使之成为“一本书”，确保每个部分都是经过实际验证的：如果是原理性内容，要找出最原始的出处；如果是可操作内容，必须自己试一试。

### FreeBSD ToDo

- [ ] Vagrant FreeBSD
  - [ ] ZFS
  - [ ] 预置 GUI
  - [ ] 兼容 VM、VB 虚拟机
  - [ ] 兼容 FreeBSD、Linux、Windows 宿主机
- [ ] [security/sudo-rs](https://www.freshports.org/security/sudo-rs/)：RUST 重构的 sudo 和 su
- [ ] GUI 代理软件
  - [ ] 基于 mihomo
- [ ] 为所有涉及的开源项目列出可行的捐款渠道（如有），鼓励捐赠或贡献代码，做些力所能及之事
- [ ] 整合现有的上游 FreeBSD 社区文章
- [X] fail2ban（须适配自带的几种防火墙）
- [ ] 删除或重写“第 9.2 节 jail 更新”
- [ ] 使用关键字 `enable`、`disable`、`delete` 替代旧式 sysrc 写法。不能完全替代遇到了 Bug [rc keywords: enable, disable, delete cannot manage certain built-in rc startup items.](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=285543)
- [X] 介绍伯克利大学与校训思想
- [ ] 从 FreeBSD 期刊引入 IPv6  教程
- [ ] Makefile
- [X] 从 FreeBSD 期刊引入 Zabbix 教程
- [X] gitlab-ee
- [ ] 为所有需要额外配置的文件，使用命令 `pkg info -D` 列出正文如此配置之原因
  - [ ] 翻译 `pkg info -D` 重要输出
- [X] 重写“第 4.1 节 安装显卡驱动及 Xorg（必看）”，尤其是 N 卡驱动部分，目前是无效的，必须重写
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
  - [] 基于 Wayland
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
- [ ] Port 移植
  - [X] QQ（上游没人管，放在了[这里](https://github.com/FreeBSD-Ask/QQ-Port/tree/main/net-im/qq)， ）
  - [ ] 微信
  - [ ] WPS


### OpenBSD ToDo

- [ ] OpenBSD
  - [X] KDE5
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
    - [ ] HTTPD
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

### NetBSD ToDo
  
- [ ] NetBSD
  - [ ] NetBSD 调优
  - [ ] 桌面
    - [ ] 火狐浏览器
    - [ ] Chromium
    - [X] KDE 4
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



### DragonFlyBSD ToDo
  
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
