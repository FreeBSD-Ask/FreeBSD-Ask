# 编辑日志

仅列出当下季度的编辑日志。其他存档在项目的 [CHANGELOG-ARCHIVE.md](https://docs.bsdcn.org/CHANGELOG-ARCHIVE) 文件中。

## 2025 年第二季度

- 2025.4.22
  - 《FreeBSD 从入门到跑路》恢复旧名《FreeBSD 艺术科学哲学导论》
- 2025.4.22
  - 第 5.2 节 Fcitx 输入法框架：重新排版
  - 从“第 4.1 节 显卡驱动”拆分出“第 4.1 节 显卡驱动（英特尔、AMD）”、“第 4.2 节 显卡驱动（NVIDIA）”
  - 第 9.3 节 使用 Qjail 管理 Jail：重新排版
- 2025.4.21
  - “第 5.6 节 QQ（Linux 版）”新增：解决 fcitx 中文输入法在 QQ 中不能使用的问题
  
---

- 2024.8.1-2025.4.20：《FreeBSD 从入门到跑路》第二版完成（TAG 2025.4.20）

---

- 2025.4.20
  - 格式化全书
  - 对全书初版重写达 100%
- 2025.4.19
  - 第 4 章 桌面环境：新增软件解释
  - 对全书删除冗余，重新排版
- 2025.4.18
  - “第 2.2 节 命令行基础（新手入门版本）”新增：关机、重启、`&&`、`||`
- 2025.4.17
  - 重写：第 16.7 节 Samba 服务器中的安装 Samba 部分，其余部分无条件测试
  - 重写：第 16.6 节 rsync 同步服务
- 2025.4.16
  - 格式化：第 14.2 节 WiFi
  - “第 27.4 节 桌面与中文环境常用软件”：重写引入：KDE 4。因为物理机测试成功。
  - 从“第 1.1 节 操作系统的历程：UNIX、Unix-like、Linux & FreeBSD”拆分出“第 1.2 节 FreeBSD 简史”
  - 重写：第 2.6 节 云服务器安装 FreeBSD（基于腾讯云轻量云）
  - 拆分序言
  - 引入 GitHub Action：🔗 从 SUMMARY.md 更新一级标题。用于检查 SUMMARY 标题和对应文件的一级标题的符合情况
- 2025.4.15
  - 格式化：第 5.6 节 QQ（Linux 版）
  - 第 4.20 节 远程桌面：删除剩余的“VNC 与 RPD（XRDP）对比”部分
- 2025.4.14
  - 目前对全书初版已重写 96.57%（按 Commit 数）
  - 格式化“第 11.5 章 MySQL 数据库”
  - 删减占用篇幅较大的无用图片
- 2025.4.13
  - “第 16.5 节 WildFly”测试基本成功，但是注意补丁仍未合并到主线，详见 [Bug 285956 - java/wildfly: service start fail, illegal group name](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=285956)。
  - 新增“第 24.3 节 配置 DragonFly BSD”
  - 重写“第 24.2 节 安装 DragonFly BSD”
- 2025.4.11
  - 通过段落间距调整，PDF 页数从 1209 到 1084，减少了 10.34% 的页面占用。
- 2025.4.10
  - 测试、改写“第 2.8 节 手动安装双系统（后安装 FreeBSD）”
  - NetBSD 10.1 在 VMware 虚拟机中无论 UEFI 与否，进入 kde 4  都会黑屏。
- 2025.4.9
  - 使用 <https://gist.github.com/ykla/adf011fea43f5f4b91aa6f065ac09da2> 对全书过长（> 30 行）的代码块进行整理。
  - 孤行控制，删除冗余。
  - 从 1238 页到 1209 页，减少了 2.34% 的无效页面。
- 2025.4.8
  - “第 27.2 节 NetBSD 安装图解”更新至 NetBSD 10.1
  - “桌面与中文环境常用软件”更新至 NetBSD 10.1
  - “桌面与中文环境常用软件”新增输入法
  - “桌面与中文环境常用软件”新增中文环境
  - NetBSD KDE 4 UEFI 下测试失败，还是黑屏，报错见 <https://gnats.netbsd.org/57554>
  - “第 16.5 节 Wildfly”测试失败，见 [Bug 285956 - java/wildfly: service start fail, illegal group name](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=285956)
- 2025.4.7
  - 全译现有所有安装后说明
  - 从 [2024.8-3533 次](https://github.com/FreeBSD-Ask/FreeBSD-Ask/commit/c4d657fb586f91e9f8664ee1181a2711f7350d17) 开始，目前对全书初版已重写 94%（按 Commit 数），下同
  - 删除“第 11.3 节 散热器、风扇、鼓风机”，可能包含错误内容
- 2025.4.6
  - “第 17.8 节 PostgreSQL 与 pgAdmin4”新增“深入 PostgreSQL 服务管理”
  - “第 4.21 节 FreeBSD 桌面发行版”补图
- 2025.4.5
  - 初步重写第 15.4 节 ipfirewall（IPFW）
  - 格式化第 15.2 节 PF
  - 格式化第 15.3 节 IPFilter（IPF）
  - 新增“第 4.21 节 FreeBSD 桌面发行版”
- 2025.4.4
  - 从各个章节拆分出“第 6 章 多媒体与外设”
  - 格式化“第 5.1 节 输入法与环境变量”
  - 格式化“第 21.12 节 Linux 兼容层与 Jail”
  - mihomo（原 Clash），需要重写相关章节，我们需要一个 GUI 界面！
- 2025.4.3
  - 从“第 20.1 节 游戏”拆分出“第 20.6 节 我的世界（Minecraft）”
  - 将“第 20.2 节 音视频播放器与剪辑”拆分为“第 20.2 节 音频播放器”、“第 20.3 节 视频播放器”、“第 20.4 节 音视频剪辑与图像处理”、
  - 测试“第 20.5 节 科研与专业工具”，并新增“Calibre 文档管理（epub、mobi、azw3 等格式）”
  - “第 20.5 节 科研与专业工具”补图
  - “第 20.1 节 游戏”：重写“Renpy 游戏”
- 2025.4.2
  - 测试“第 20.2 节 音视频播放器”：尝试播放电视剧《人民公仆》、尝试播放动漫《败犬女主太多了！》，测试通过
- 2025.4.1
  - <https://mirrors.aliyun.com/freebsd-pkg/> 看起来早就失去同步。还是 2 月我提交 kmod 源以前的内容，故不写入
