# 编辑日志

仅列出当下季度的编辑日志。其他存档在项目的 [CHANGELOG-ARCHIVE.md](https://docs.bsdcn.org/CHANGELOG-ARCHIVE) 文件中。

## 2025 年第三季度

- 2025.9.19
  - “1.2 FreeBSD 导论”——“选择 FreeBSD 的技术性原因”新增“安全原因”
- 2025.9.15
  - 新增“22.15 在 Ubuntu 上构建 FreeBSD” 
- 2025.9.10
  - 重写“9.1 音频设备配置”
  - 新增“6.16 KDE6（Wayland）”
- 2025.8.31
  - 目前将无线电（WiFi）区域码设置为 `CN NONE`（`create_args_wlan0="country CN regdomain NONE"`）是不正确的，因为 FreeBSD 的文件没有得到维护，实际上会导致无法协商到 WiFi5（FreeBSD 为 VHT40），速率始终是 11a，不是应有的 11ac；并且对于 DFS，配置写的也不正确。已经报告 Bug 至 [Missing CN regulatory domain and 11ac/DFS support in regdomain.xml ](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=289202)。临时解决方案：如果你的信道 > 48，需要专门在 `/etc/rc.conf` 中修改或写入 `create_args_wlan0="country HR regdomain ETSI"`；如果你的信道 <= 48，且存在 `create_args_wlan0="country CN regdomain NONE"`，请将其删除，因为默认的 FCC US 配置可支持其 WiFi5 协议。经过测试，即使是 WiFi 6 路由器，开启 WPA3、160MHz，也是受支持的。按照以上临时方案进行配置，Intel AX200 网卡在 FreeBSD 14.3-RELEASE 上可成功协商至 11ac。
  - 因 budgie 主要维护者 Olivier Duchateau 称已对此项目不感兴趣，放弃维护。且无人主动维护，目前核心组件 Port `sysutils/budgie-control-center` [被标记为](https://www.freshports.org/sysutils/budgie-control-center/) `broken`（破损）。考虑在日后删除 6.10 Budgie。如果 6 个月内仍未得到修复将建议上游删除此项目，并从本书中移除此节。
- 2025.8.24
  - 新增：“12.5 无线网络环境下使用 bhyve”
  - “4.2 Linux 用户迁移指南”新增“历史”
- 2025.8.20
  - 新增“3.10 云服务器安装 FreeBSD（基于 KVM、QEMU 等平台）”
- 2025.8.18
  - “2.1 安装前的准备工作”新增：最高硬件支持
- 2025.8.17
  - 3.9 云服务器安装 FreeBSD（基于腾讯云轻量云）：测试了多种替代方案均失败
- 2025.8.14
  - 将“1.2 欢迎来到 FreeBSD”、“1.3 关于 FreeBSD 项目”合并为“1.2 FreeBSD 导论”，原有章节从标题看不知道是作何用的
  - 将“窗口管理器”、“FreeBSD 高级安装”前置便于使用
- 2025.8.13
  - 增补 2.2 使用 bsdinstall 开始安装：补充有关 ACPI 的警告、引入 bsdinstall 介绍
  - 将本书的组织结构、本书中使用的一些约定合并入绪论
  - 合并三篇序言到前言
- 2025.8.7
  - 重写：本书的组织结构
- 2025.7.31
  - 新增：附录 2 UEFI/BIOS 注解（基于 AMI BIOS）
- 2025.7.30
  - 之前 KDE 在 Wayland 下，启动后桌面右键单击黑屏的问题已得到解决。参见 <https://old.reddit.com/r/freebsd/comments/1m9popo/kde_mini_review/n5dv1uk/> 和 <https://github.com/freebsd/freebsd-ports/pull/431>。目前已安装的只需要 `make reinstall` Port `graphics/qt6-wayland` 和 `/x11/plasma6-layer-shell-qt` 即可。或者等几天通过 `pkg upgrade`、安装的也应该不会有黑屏问题了。
- 2025.7.23
  - 恢复书名《FreeBSD 从入门到跑路》
- 2025.7.7
  - 17.7 OpenList 新增：本机存储的多属主权限管理
  - 17.7 OpenList 新增：影视刮削
- 2025.7.6
  - 新增：17.7 OpenList
  - 6.2 Fcitx 输入法框架：已经把安装 RIME 中州韵输入法（可选）作为独立子节，并强调了 chinese/rime-essay 的必要性
  - 20.1 Renpy 游戏与 Godot 游戏：删除五分钟游戏。都是些桌面自带的游戏，列举无意义
  - 新增：20.4 Steam
- 2025.7.5
  - 重写：6.6 QQ（Linux 版）。在所有兼容层中，Fcitx5 输入法框架均测试通过，可以正常输入汉字
- 2025.7.4
  - 新增：6.11 Wine
