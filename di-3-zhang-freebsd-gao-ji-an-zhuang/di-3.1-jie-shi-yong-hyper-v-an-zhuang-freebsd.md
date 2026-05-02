# 3.1 使用 Hyper-V 安装 FreeBSD

Hyper-V 是微软为 Windows 开发的企业级 Type-1 虚拟机监视器，分 Gen 1 与 Gen 2 两种架构。本节记录在 Hyper-V 中安装与配置 FreeBSD 的完整流程。

## Hyper-V 简介

虚拟机监视器是一种创建和运行虚拟机的软件，允许多个操作系统同时运行在同一台计算机上。从虚拟化技术的理论分类来看，Hypervisor 分为 Type-1（裸金属型）和 Type-2（宿主型）两类。Type-1 直接运行于物理硬件之上，Type-2 则运行于宿主操作系统之上。Hyper-V 属于 Type-1 架构，其虚拟化层直接管理硬件资源，提供更高的隔离性和性能。

Hyper-V 是微软公司（Microsoft）为 Windows 和 Windows Server 开发的企业级虚拟机监视器，属于系统内置组件。

Hyper-V 分为 Gen 1（第一代）和 Gen 2（第二代）两种虚拟机架构，两种架构在硬件支持和启动方式上存在技术差异。

Gen 1 与 Gen 2 的区别如下表所示：

| Hyper-V 代系 | 硬盘 | 启动方式 |
| ------------ | ---- | -------- |
| Gen 1 | IDE + SCSI | 仅支持 MBR |
| Gen 2 | 仅 SCSI | 仅支持 UEFI（包含安全启动及 PXE 支持） |

系统快速创建的虚拟机默认为 Gen 2 架构。

> **注意**
>
> 使用 Gen 2 时请关闭安全启动，否则系统无法启动。具体操作步骤为：点击“设置”，选择“安全”，取消勾选“启用安全启动”。FreeBSD 自 14.0 起已支持 UEFI 安全启动，但其引导加载程序未经 Microsoft 签名，因此在 Hyper-V 默认的安全启动配置（使用“Microsoft UEFI 证书颁发机构”模板）下无法通过验证。

| Hyper-V 代系 | FreeBSD 版本 | 鼠标 | 键盘 | 备注 |
| ------------ | ------------ | ---- | ---- | ---- |
| Gen 1 | 13.0 | 支持 | 不支持 | / |
| Gen 2 | 13.0 | [不支持](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=221074) | 支持 | 需修改参数 `sysctl kern.evdev.rcpt_mask=6`（启用 evdev，让 Xorg 正确检测 PS/2 设备） |
| Gen 2 | 14.0 | 支持 | 支持 | 参见：FreeBSD Project. src[EB/OL]. [2026-03-26]. <https://cgit.FreeBSD.org/src/commit/?id=21f4e817fde79d5de79bfbdf180d358ca5f48bf9>. |

FreeBSD 对 Hyper-V 的集成支持通过内核模块实现：

| 模块 | 功能 |
| ---- | ---- |
| `hv_utils` | 提供时间同步、心跳检测、关机通知等集成功能 |
| `hv_vmbus` | 实现 Hyper-V 虚拟总线，是其他 Hyper-V 设备驱动的基础 |
| `hv_netvsc` | 提供网络半虚拟化驱动（高性能网络通信） |
| `hv_storvsc` | 提供存储半虚拟化驱动（虚拟磁盘 I/O 支持） |

## 测试环境

本节基于以下软硬件环境进行测试与演示，实验结果具有一定的环境依赖性。

- Windows 11 23H2 专业版
- FreeBSD 14.1-RELEASE（`FreeBSD-14.1-RELEASE-amd64-disc1.iso`）
- Hyper-V 版本：10.0.22621.4249
- 使用第二代 Hyper-V 虚拟机

## 安装 Hyper-V

> **注意**
>
> Windows 家庭版和家庭中文版不支持 Hyper-V。

在 Windows 系统中启用 Hyper-V 功能组件，需以管理员权限执行以下命令。

![Hyper-V](../.gitbook/assets/hyperv-1.png)

右键单击 Windows 徽标，在弹出的菜单中选择“终端（管理员）”。输入以下命令：

```powershell
PS C:\Users\ykla> Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
是否立即重启计算机以完成此操作?
[Y] Yes  [N] No  [?] 帮助 (默认值为“Y”):
# 此处按回车键确认重启以完成 Hyper-V 的安装
```

## 创建虚拟机

安装完成 Hyper-V 后，创建虚拟机。

![Hyper-V](../.gitbook/assets/hyperv-2.png)

右键单击 Hyper-V 管理器中的主机名，选择“新建”→“虚拟机”。

![Hyper-V](../.gitbook/assets/hyperv-3.png)

点击“下一页”。

![Hyper-V](../.gitbook/assets/hyperv-4.png)

为虚拟机设置名称，然后点击“下一页”。

![Hyper-V](../.gitbook/assets/hyperv-generation-select.png)

选择“第二代”。然后点击“下一页”。

![Hyper-V](../.gitbook/assets/hyperv-5.png)

设置内存大小，然后点击“下一页”。

![Hyper-V](../.gitbook/assets/hyperv-6.png)

设置网络，然后点击“下一页”。

![Hyper-V](../.gitbook/assets/hyperv-7.png)

指定虚拟硬盘的名称、大小及存储位置，然后点击“下一页”。

![Hyper-V](../.gitbook/assets/hyperv-8.png)

点击“浏览”，找到并选中已下载的 `FreeBSD-14.1-RELEASE-amd64-disc1.iso` 文件，然后点击“下一页”。

![Hyper-V](../.gitbook/assets/hyperv-9.png)

点击“完成”。

## 虚拟机配置调整

虚拟机创建完成后，调整部分设置。

![Hyper-V](../.gitbook/assets/hyperv-10.png)

点击“设置”。

![Hyper-V](../.gitbook/assets/hyperv-11.png)

请务必关闭安全启动（见上文注意事项），否则将无法从安装介质启动安装程序。

![Hyper-V](../.gitbook/assets/hyperv-12.png)

请勾选“来宾服务”。来宾服务是 Hyper-V 集成服务的一部分，提供宿主机与虚拟机之间的文件交换、时间同步等集成功能。其作用详见参考文献。

![Hyper-V](../.gitbook/assets/hyperv-16.jpg)

可选择关闭“使用自动检查点”（即关闭自动快照功能），其作用详见参考文献。

## 安装 FreeBSD

虚拟机设置调整完成后，安装 FreeBSD 系统。

![Hyper-V](../.gitbook/assets/hyperv-13.png)

启动该虚拟机。

![Hyper-V](../.gitbook/assets/hyperv-14.png)

按提示开始安装 FreeBSD。

![Hyper-V](../.gitbook/assets/hyperv-15.jpg)

安装完成。

## 桌面环境验证

安装完成后，测试虚拟机基本功能。

鼠标和键盘均可正常工作，可在宿主机和虚拟机间无缝切换，但虚拟机桌面分辨率无法自适应调整。建议检查 Hyper-V 集成服务安装并参考 FreeBSD 文档以获取显示配置指南。

![Hyper-V](../.gitbook/assets/hyperv-summary.jpg)

删除虚拟机前，必须先将其关闭。

## 参考文献

- 微软. 安装 Hyper-V[EB/OL]. (2025-05-23)[2026-04-04]. <https://learn.microsoft.com/zh-cn/windows-server/virtualization/hyper-v/get-started/install-hyper-v?tabs=powershell&pivots=windows>. 指出家庭版并不支持 Hyper-V 虚拟化技术。
- 微软. Windows Server 和 Windows 中的 Hyper-V 虚拟化[EB/OL]. [2026-03-26]. <https://learn.microsoft.com/zh-cn/windows-server/virtualization/hyper-v/overview>. 微软官方对 Hyper-V 的说明，详细介绍了 Hyper-V 虚拟化架构与功能特性。
- 微软. 在 Windows 上安装 Hyper-V[EB/OL]. [2026-03-26]. <https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v>. 微软官方教程，提供了多种 Hyper-V 启用方法。
- 微软. Hyper-V 集成服务[EB/OL]. [2026-03-26]. <https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/reference/integration-services>. 详细说明了 Hyper-V 集成服务的功能与配置方法。
- 微软. 使用检查点将虚拟机恢复到以前的状态[EB/OL]. [2026-03-26]. <https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/user-guide/checkpoints?source=recommendations&tabs=hyper-v-manager%2Cpowershell>. 介绍了 Hyper-V 检查点的创建与使用方法。
- 微软. 在 Hyper-V 中在标准检查点与生产检查点之间进行选择[EB/OL]. [2026-03-26]. <https://learn.microsoft.com/zh-cn/windows-server/virtualization/hyper-v/manage/choose-between-standard-or-production-checkpoints-in-hyper-v>. 对比了标准检查点与生产检查点的差异与适用场景。
- nanorkyo. FreeBSD13 を Hyper-V 環境 にインストールしてみた 所感[EB/OL]. [2026-03-26]. <https://qiita.com/nanorkyo/items/d33e1befd4eb9c004fcd>. 提供了 FreeBSD 在 Hyper-V 环境下的安装经验与技巧。
- FreeBSD Foundation. FreeBSD UEFI Secure Boot[EB/OL]. [2026-04-17]. <https://freebsdfoundation.org/freebsd-uefi-secure-boot/>. FreeBSD 安全启动的技术说明，阐述了引导加载程序签名与 UEFI 固件验证的关系。

## 课后习题

1. 分析 FreeBSD 中 kern.evdev.rcpt_mask 参数控制输入事件分发的机制。
2. 测试 Hyper-V 虚拟化性能优化设置对 FreeBSD 虚拟机 I/O 吞吐量的影响。
3. 比较 Hyper-V 与 bhyve 在 I/O 半虚拟化驱动模型上的设计差异。
