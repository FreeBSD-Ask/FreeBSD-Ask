# 3.6 安装故障排除

安装过程中最常见的阻断性问题包括无法进入安装界面、分区表错误与引导丢失。本节逐一给出排查步骤与恢复方法。

## 无法进入安装界面

如果无法进入安装界面，首先区分虚拟机环境与物理机环境，而后分别排查。

如果是虚拟机，请检查虚拟机配置。

如果是物理机，请依次检查如下项目：

- 电脑是否为标准个人计算机？
- 处理器品牌是否为 Intel 或 AMD？
- 是否已关闭 BIOS 中的安全启动（Secure Boot）？
- 镜像是否从 <https://www.freebsd.org> 下载？
- 是否下载了最新版本的 RELEASE 镜像？
- 下载的镜像文件扩展名是否为 `img`（USB 设备）或 `iso`（光盘镜像）？
- 镜像校验（SHA-256）是否通过？
- 下载的镜像是否带有 `amd64`（标准个人计算机）字样？
  - 请确认是 `amd64`（适用于标准 x86 个人计算机）**而非** `arm64`（适用于 ARM 架构设备，如树莓派等嵌入式平台）。
- U 盘是否为扩容盘（伪造容量产品）？
- 是否使用了 Ventoy 工具？
  - 如果使用 Ventoy - 多系统启动 USB 启动盘制作工具 <https://www.ventoy.net/cn/index.html> 无法启动，可尝试改用 Rufus - Create bootable USB drives the easy way <https://rufus.ie/zh/> 刻录。

如果仍出现问题，请先在 FreeBSD 官方论坛 <https://forums.freebsd.org/> 以英语提问；如未获解答，可按其他章节指引提交 Bug。

## 重启后又进入了安装界面

安装完成后重启系统时，可能再次进入安装界面，此时需要检查引导设备。

如果是虚拟机，请手动弹出或断开虚拟 DVD 光驱的自动连接，而后重启。如果是物理机，请拔出 U 盘或弹出安装光盘后重启。

## 启动时输出若干 ACPI 字样的错误信息

> **警告**
>
> 某些文章建议关闭 ACPI。该做法在现代硬件上已缺乏技术依据，关闭 ACPI 可能导致系统无法正常启动或功能受限。ACPI 与电源状态管理、设备节能、多处理器支持等功能密切相关，关闭 ACPI 的选项应视为遗留功能。

如果出现 ACPI 错误提示，大多数情况下不影响正常运行。通常可通过更新主板 BIOS 或固件解决。少数情况下可能需要修补 SSDT（Secondary System Description Table，次级系统描述表）和 DSDT（Differentiated System Description Table，差异化系统描述表）。

部分制造商建议仅在必要时升级主板 BIOS/固件。升级过程 **可能** 出现问题（如意外断电），造成 BIOS 固件不完整，导致计算机无法正常工作。

## 启动时停滞于某项服务

旧版本安装时，系统启动可能长时间停留在 sendmail 等服务；需要配置静态 IP 地址时，系统却可能持续尝试 DHCP。

此时可尝试按下 **Ctrl** + **C** 组合键中断该服务，从而继续启动系统。

### 参考文献

- FreeBSD Project. FreeBSD 14.0-RELEASE Release Notes[EB/OL]. [2026-04-17]. <https://www.freebsd.org/releases/14.0R/relnotes/>. FreeBSD 14.0 起将默认邮件传输代理（MTA）从 sendmail 替换为 dma（Dragonfly Mail Agent），sendmail 不再默认启动，解决了旧版本启动卡顿问题。
