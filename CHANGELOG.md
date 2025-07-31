# 编辑日志

仅列出当下季度的编辑日志。其他存档在项目的 [CHANGELOG-ARCHIVE.md](https://docs.bsdcn.org/CHANGELOG-ARCHIVE) 文件中。

## 2025 年第三季度

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
