# 编辑日志

仅列出当下季度的编辑日志。其他存档在项目的 `CHANGELOG-ARCHIVE.md` 文件中。

## 2025 年第二季度

- 2025.4.9
  - 使用 <https://gist.github.com/ykla/adf011fea43f5f4b91aa6f065ac09da2> 对全书过长（> 30 行）的代码块进行整理。
- 2025.4.8
  - “第 27.2 节 NetBSD 安装图解”更新至 NetBSD 10.1
  - “桌面与中文环境常用软件”更新至 NetBSD 10.1
  - “桌面与中文环境常用软件”新增输入法
  - “桌面与中文环境常用软件”新增中文环境
  - NetBSD KDE 4 UEFI 下测试失败，还是黑屏，报错见 <https://gnats.netbsd.org/57554>
  - “第 16.5 节 Wildfly”测试失败，见 [Bug 285956 - java/wildfly: service start fail, illegal group name](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=285956)
- 2025.4.7
  - 全译现有所有安装后说明
  - 从 2024.8 开始，目前对全书已重写 94%（按 Commit 数）
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
  -  测试“第 20.2 节 音视频播放器”：尝试播放电视剧《人民公仆》、尝试播放动漫《败犬女主太多了！》，测试通过
- 2025.4.1
  - <https://mirrors.aliyun.com/freebsd-pkg/> 看起来早就失去同步。还是 2 月我提交 kmod 源以前的内容，故不写入
