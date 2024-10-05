# 第 2.4 节 安装 FreeBSD——基于 Hyper-V

## Hyper-V 简介

Hyper-V 是微软为 Windows 开发的虚拟机，分为 `Gen 1` 和 `Gen 2`。

Hyper-V 不支持家庭版。

`Gen 1` 和 `Gen 2` 区别如下：

| Hyper-V 代数 |    硬盘    |             启动引导              |
| :----------: | :--------: | :-------------------------------: |
|    Gen 1     | IDE + SCSI |              仅 MBR               |
|    Gen 2     |  仅 SCSI   | 仅 UEFI + 安全启动支持 + PXE 支持 |

系统快速创建的为 `Gen 2`。

>**注意：**
>
>使用 Gen 2 时请关闭安全启动，否则系统无法启动！点击设置： 点击“安全”——>取消勾选“启用安全启动。

| Hyper-V 代数 | FreeBSD 版本 |                                鼠标                                |  键盘  |                                              备注                                              |
| :----------: | :----------: | :----------------------------------------------------------------: | :----: | :--------------------------------------------------------------------------------------------: |
|    Gen 1     |     13.0     |                                支持                                | 不支持 |                                               /                                                |
|    Gen 2     |     13.0     | [不支持](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=221074) |  支持  |                          需要修改参数`sysctl kern.evdev.rcpt_mask=6`                           |
|    Gen 2     |     14.0     |                                支持                                |  支持  | 参见[源代码](https://cgit.FreeBSD.org/src/commit/?id=21f4e817fde79d5de79bfbdf180d358ca5f48bf9) |


## 测试环境：

- Windows 11 23H2 专业版
- FreeBSD 14.1-RELEASE（`FreeBSD-14.1-RELEASE-amd64-disc1.iso`）
- Hyper-V 版本: 10.0.22621.4249

## 安装 Hyper-V

![Hyper-V](../.gitbook/assets/hp1.png)

右键单击 Windows 徽标，在弹出窗口中右键单击“终端管理员”：输入以下内容

```batch
PS C:\Users\ykla> Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All                             是否立即重启计算机以完成此操作?
[Y] Yes  [N] No  [?] 帮助 (默认值为“Y”): #此处按回车键确定重启完成 Hyper-V 的安装
```

## 准备 Hyper-V 虚拟机

![Hyper-V](../.gitbook/assets/hp2.png)

右键单击这台主机的主机名，选择“新建”——>“虚拟机”。

![Hyper-V](../.gitbook/assets/hp1.png)

![Hyper-V](../.gitbook/assets/hp2.png)

![Hyper-V](../.gitbook/assets/hp3.png)

![Hyper-V](../.gitbook/assets/hp4.png)

![Hyper-V](../.gitbook/assets/hp5.png)

![Hyper-V](../.gitbook/assets/hp6.png)

![Hyper-V](../.gitbook/assets/hp7.png)

![Hyper-V](../.gitbook/assets/hp8.png)

![Hyper-V](../.gitbook/assets/hp9.png)

![Hyper-V](../.gitbook/assets/hp10.png)

![Hyper-V](../.gitbook/assets/hp11.png)

![Hyper-V](../.gitbook/assets/hp12.png)

![Hyper-V](../.gitbook/assets/hp13.png)

## 安装 FreeBSD

![Hyper-V](../.gitbook/assets/hp14.png)

![Hyper-V](../.gitbook/assets/hp15.png)



### 参考文献

- [在 Windows 上安装 Hyper-V](https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v)，微软官方教程，还有多种方法可选
- [Hyper-V 集成服务](https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/reference/integration-services)，对各种 Hyper-V 服务进行了详细说明
- [使用检查点将虚拟机恢复到以前的状态](https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/user-guide/checkpoints?source=recommendations&tabs=hyper-v-manager%2Cpowershell)
- [在 Hyper-V 中在标准检查点与生产检查点之间进行选择](https://learn.microsoft.com/zh-cn/windows-server/virtualization/hyper-v/manage/choose-between-standard-or-production-checkpoints-in-hyper-v)
