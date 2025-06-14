# 贡献指南与开放任务

细节参见 <https://github.com/FreeBSD-Ask/FreeBSD-Ask/wiki>。


## 贡献指南

如果你想让你的教程出现在本书中，你可以这样做：

- 如果你熟悉 GitHub，可以点击电脑端右侧的“编辑此页”，进入项目进行操作。整个项目使用 Markdown 语法 +  Gitbook，简单易上手（具体详见项目 WiKi）；
- 如果以上有困难，你还可以发 PDF、Word 或者 TXT 给我。请将文件发送至电子邮件 `yklaxds@gmail.com`（我将在 3 天内回复。若我没有回复，请换个邮件再发一次，或者提交 issue）；如果有视频教程，以各大云盘链接为宜。

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

所有任务的排序都是随机的并无优先级之分，你可以选你喜欢的去做。

### FreeBSD ToDo

#### 季度常规任务

- [ ] 规范用户配置文件与系统文件
  - [ ] sysctl：不应直接修改 `/etc/sysctl.conf`，而应改为 `/etc/sysctl.conf.local`，后者会覆盖全局的 `/etc/sysctl.conf` 参数。参见 [sysctl.conf(5)](https://man.freebsd.org/cgi/man.cgi?sysctl.conf(5))
  - [ ] 启动引导参数：不应直接修改 `/boot/loader.conf`，建议改为 `/boot/loader.conf.local`，后者会覆盖全局的 `/boot/loader.conf` 参数。参见 [loader.conf(5)](https://man.freebsd.org/cgi/man.cgi?loader.conf(5))
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
  - [ ] 基于 Wayland
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


#### 重写 FreeBSD 社区手册

大部分内容其实已有，待整合。

- [ ] 第 1 章 简介
  - [ ] FreeBSD 项目宗旨
  - [ ] FreeBSD 哲学理念
  - [ ] FreeBSD 开发模式（组织结构）
- [ ] 第 2 章 安装 FreeBSD
  - [ ] FreeBSD Live CD 用法（USB img 无法挂载以进行重置密码登操作，因为文件系统是只读的，需要解决）
  - [ ] PXE 安装 FreeBSD
- [ ] 第 3 章 FreeBSD 基础
  - [ ] 3.2.虚拟控制台和终端
  - [ ] 3.3.用户和基本账户管理
  - [ ] 3.4.权限
  - [ ] 3.5.目录结构
  - [ ] 3.6.磁盘结构
  - [ ] 3.8.进程和守护进程
  - [ ] Emacs 编辑器基础用法
- [ ] 第 4 章 安装应用程序：软件包和 Ports
  - [ ] 4.6.使用 Poudriere 构建软件包
- [ ] 第 5 章 X Window 系统
  - [ ] 5.5.在 X11 中使用字体（重点引入中文字体）
- [ ] 第 6 章 FreeBSD 中的 Wayland
  - [ ] 设计哲学
  - [ ] 与 x11 对比，如何在 wayland 下实现原有 x11 的功能
  - [ ] 将所有常见桌面 wayland 化
  - [ ] 引入新的桌面相关软件
  - [ ] 远程连接
- [ ] 第 7 章 网络
  - [ ] ADSL 拨号上网
  - [ ] 7.4.无线网络（引入高级加密等）
- [ ] 第 9 章 多媒体
  - [ ] 9.2.设置声卡
  - [ ] 9.5.视频会议
  - [ ] 9.6.图像扫描仪
- [ ] 第 10 章 配置 FreeBSD 内核
  - [ ] 交叉编译
  - [ ] 修改内核配置
  - [ ] 翻译内核参数
- [ ] 第 11 章 打印（本节对中文无意义，不引入）
- [ ] 第 13 章 WINE
  - [ ] Wine x86 程序
- [ ] 第 14 章 配置与优化
  - [ ] 列举 `/etc` 目录的单个配置文件及说明作用
  - [ ] 14.4.Cron 和 Periodic
  - [ ] 14.6.电源和资源管理
  - [ ] 14.5.配置系统日志（可结合列举 `/etc` 目录的单个配置文件及说明作用该步骤）
- [ ] 第 15 章 FreeBSD 的引导过程
  - [ ] UEFI
  - [ ] BIOS
- [ ] 第 16 章 安全
  - [ ] 计算机安全基础与哲学
  - [ ] 16.3.账户安全
  - [ ] 16.4.入侵检测系统（IDS）
  - [ ] 16.5.安全等级
  - [ ] 16.6.文件标志位
  - [ ] 16.9.Kerberos
  - [ ] 16.11.访问控制列表（ACL）
  - [ ] 16.12.Capsicum
  - [ ] 16.13.进程记账
  - [ ] 16.14.资源限制（资源配额）
- [ ] 第 17 章 jail 与容器
  - [ ] 17.4.传统 jail（厚 jail）
  - [ ] 17.5.瘦 jail
  - [ ] 17.6.管理 jail
  - [ ] 17.7.更新 jail
  - [ ] 17.8.jail 资源限制
  - [ ] 17.9.jail 管理器与容器
- [ ] 第 18 章 强制访问控制
  - [ ] 18.3.了解 MAC 标签
  - [ ] 18.4.规划安全配置
  - [ ] 18.5.可用的 MAC 策略
  - [ ] 18.6.用户锁定
  - [ ] 18.7.MAC Jail 中的 Nagios
  - [ ] 18.8.MAC 框架的故障排除
- [ ] 第 19 章 安全事件审计
  - [ ] 19.3.审计配置
  - [ ] 19.4.使用审计跟踪
- [ ] 第 20 章 存储
  - [ ] 20.6.创建和使用 DVD
  - [ ] 20.5.创建和使用 CD
  - [ ] 20.10.文件系统快照（UFS）
  - [ ] 20.11.磁盘配额
  - [ ] 20.12.加密磁盘分区
  - [ ] 20.13.加密交换分区
  - [ ] 20.14.高可用性存储（HAST）     
- [ ] 第21章 GEOM: 模块化磁盘转换框架
  - [ ] 21.2.RAID0——条带
  - [ ] 21.3.RAID1——镜像
  - [ ] 21.4.RAID3——带有专用奇偶校验的字节级条带
  - [ ] 21.5.软件 RAID 设备
  - [ ] 21.6.GEOM Gate 网络设备
  - [ ] 21.7.为磁盘设备添加卷标
- [ ] 第 22 章 Z 文件系统（ZFS）
  - [ ] ZFS 设计哲学
  - [ ] 22.6.高级主题
  - [ ] 拆分 zfs、zpool（池）管理
- [ ] 第 24 章 虚拟化
  - [ ] 24.8.基于 FreeBSD 的 Xen™ 虚拟机
  - [ ] 24.6.使用 FreeBSD 上的 QEMU 虚拟化
- [ ] 第 26 章 FreeBSD 更新与升级
  - [ ] 26.7.多台机器的追踪
  - [ ] 26.8.在非 FreeBSD 主机上进行构建
- [ ] 第 27 章 DTrace
  - [ ] 27.2.实现上的差异
  - [ ] 27.3.开启 DTrace 支持
  - [ ] 27.4.启用内核外部模块 DTrace
  - [ ] 27.5.使用 DTrace
- [ ] 第 31 章 电子邮件
- [ ] 第 32 章 网络服务器
  - [ ] 32.2.inetd 超级服务器
  - [ ] 32.4.网络信息系统（NIS）
  - [ ] 32.6.动态主机设置协议（DHCP）
  - [ ] 32.7.域名系统（DNS）
  - [ ] 32.8.零配置网络（mDNS/DNS-SD）
  - [ ] 32.13.iSCSI target 和 initiator 的配置
- [ ] 第 33 章 防火墙
  - [ ] 33.6.Blacklistd
- [ ] 第 34 章 高级网络
  - [ ] 34.2.网关和路由
  - [ ] 34.3.虚拟主机
  - [ ] 34.4.无线高级身份验证
  - [ ] 34.5.无线自组织（Ad-hoc）模式
  - [ ] 34.7.蓝牙
  - [ ] 34.8.桥接
  - [ ] 34.9.链路聚合与故障转移
  - [ ] 34.10.使用 PXE 进行无盘操作
  - [ ] 34.11.共用地址冗余协议（CARP）
  - [ ] 34.12.VLAN
- [ ] - 术语表
      
### OpenBSD ToDo

- [x] KDE5
- [ ] QQ？可能吗？
- [ ] 微信？可能吗？
- [ ] 规范用户配置文件与系统文件
- [ ] Wine 可能吗？
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

- [ ] NetBSD 调优
- [ ] 桌面
  - [ ] 火狐浏览器
  - [ ] Chromium
  - [x] KDE 4
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
  

- [ ] DragonFlyBSD 调优
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

