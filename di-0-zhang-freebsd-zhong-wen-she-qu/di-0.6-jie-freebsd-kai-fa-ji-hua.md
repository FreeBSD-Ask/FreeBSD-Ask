# 第 0.6 节 FreeBSD 开发计划


> FreeBSD 的生命周期为每个大版本 5 年，小版本是发布新的小版本版后 +3 个月。
>
> FreeBSD 14 开发计划 [https://github.com/bsdjhb/devsummit/blob/main/14.0/planning.md](https://github.com/bsdjhb/devsummit/blob/main/14.0/planning.md)
>
> FreeBSD 15 开发计划 <https://github.com/bsdjhb/devsummit/blob/main/15.0/planning.md>

## FreeBSD 15.0 计划

\# :加粗: 已完成

已提交到代码库的事项。

| 事项 | 负责人 | 提交 / 审查 / 补丁 |
| ---- | ------ | ------------------ |

## :airplane: 已有事项

已存在于代码库之外的事项，可以在接下来的两年内或者在下一个发布版本之前合并进来（可能需要进一步工作以满足合并要求）。

| 事项                                             | 负责人         | 提交 / 审查 / 补丁 |
| ------------------------------------------------ | -------------- | ------------------ |
| 对于 amd64 的 kboot 支持                         | imp            |                    |
| NVMe-oF/TCP                                      | jhb            |                    |
| 在 mv 和 install 中添加 copy_file_range()        | pjd            |                    |
| 更好的 copy_file_range()回退/包装                | pjd            |                    |
| arm64 分支目标标识                               | andrew         |                    |
| arm64 SVE                                        | andrew         |                    |
| amd64/arm64 救援内核                             | markj / Klara  |                    |
| arm64 bhyve                                      | andrew         |                    |
| iovec 包装器                                     | brooks         |                    |
| 在 bhyve 中支持单步执行 AMD CPU                  | jhb Bojan      |                    |
| 在 bhyve 客户机中支持硬件监视点                  | jhb Bojan      |                    |
| DDB 通过 CTF 进行漂亮打印                        | jhb Bojan      |
| 整合来自我的谷歌代码之夏学生代码的加载器命令行编辑功能 | imp            | 需要协助           |
| 使用 dtrace 进行内联函数追踪                     | markj Christos |                    |
| 谷歌代码之夏：squashfs                                   | chuck          |                    |

## 💸 需要

在接下来的两年内，某些人需要支持产品或服务的事项。

| 事项                             | 负责人                        | 提交 / 审查 / 补丁 / 状态                                           |
| -------------------------------- | ----------------------------- | ------------------------------------------------------------------- |
| 新的 ELF 内核转储格式            | jhb markj                     |                                                                     |
| 完成 pkgbase                     | emaste                        |                                                                     |
| Poudriere 支持无需工具链的 jail | allanjude brd                 |                                                                     |
| 外部工具链支持                   | brooks                        |                                                                     |
| 预提交 CI（代码库、文档）        | lwhsu imp bofh                |                                                                     |
| 预提交 CI（Port）                | lwhsu 将与 bapt 和 decke 核实 |                                                                     |
| 本地和云开发者 CI                | bofh lwhsu                    |                                                                     |
| 其他 CI 改进                     | lwhsu                         |                                                                     |
| 通用闪存存储驱动                 | loos                          | 目前在一些嵌入式部署中需要，未来可能更加通用。即将支持 Intel 平台。 |

## 🥺 想要

这些是希望有但不是必要的事项。

| 事项                                                                        | 负责人                  | 提交 / 审查 / 补丁 / 状态                                                                                         |
| --------------------------------------------------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------- |
| TPM 支持（GELI，ZFS）                                                       | allanjude               | --                                                                                                                |
| smbfs 替代（v2 或更好）                                                     | emaste jhixson          | --                                                                                                                |
| 9pfs 客户端                                                                 | bkumara，khng / Juniper | --                                                                                                                |
| overlayfs                                                                   | thj / Klara             |                                                                                                                   |
| 关于 syscall 表生成的更新（makesyscalls.lua 的库化）                        | imp                     |                                                                                                                   |
| 简化的安装程序（单盘，更好的默认值，例如按 Enter 键完成）                   | emaste brd              |                                                                                                                   |
| 每个文件的 nullfs                                                           | dfr                     |                                                                                                                   |
| 更多的容器支持                                                              | emaste                  | 合作学生                                                                                                          |
| MINIMAL 内核                                                                | imp                     |                                                                                                                   |
| 启动加载程序支持 devmatch                                                   | imp manu                |                                                                                                                   |
| 重写 config(8)（使用 Lua？）                                                | imp kevans              |                                                                                                                   |
| 跨 kldxref                                                                  | brooks / jhb            | （kevans 有一种有些混乱的原型或两种）                                                                             |
| 合并 devmatch 和 devd（库化）                                               | imp                     | meena 愿意协助                                                                                                    |
| 调度器和 VFS 文档覆盖范围                                                   | mhorne                  |                                                                                                                   |
| 减少 GIANT 的修改                                                           | jhb imp                 |                                                                                                                   |
| vt(4)的更好 i18n 支持（CJK 字体，Unicode 字体显示（例如表情符号），输入法） | fanchung                | 在 GSoC'21 有一个[IME PoC](https://wiki.freebsd.org/SummerOfCode2021Projects/InputMethodInFreeBSDVirtualTerminal) |
| 以 tarfs 为根目录                                                           | imp                     |                                                                                                                   |
| 内核中对 Rust 的支持                                                        | brooks                  |                                                                                                                   |
| 用户空间中对 Rust 的支持                                                    | brooks                  |                                                                                                                   |
| 用于 ZFS 的 netlink（zfsd/zed）                                             | allanjude               |                                                                                                                   |
| 用 netlink 替代 devd 套接字                                                 | bapt                    | 内核部分已完成                                                                                                    |
| 将 login.conf 转为 UCL 格式                                                 | meena                   | allanjude 已有一些补丁：[D25365](https://reviews.freebsd.org/D25365)                                              |
| 剩余网络工具的改进（lixo）                                                  | meena                   |                                                                                                                   |
| 层次化动态登录类别                                                          | ngor，meena             |                                                                                                                   |

## 🗑️ 候选删除项 🪓

这些是我们可能希望弃用的事项。可能需要进一步讨论以达成共识。

| 事项                                                                                                  | 负责人          | 提交 / 审查 / 补丁                                                                        |
| ----------------------------------------------------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------------- |
| Firewire 🔥                                                                                           | imp             |                                                                                           |
| armv6                                                                                                 | imp/manu        |                                                                                           |
| SoC 支持审查                                                                                          | imp/manu/mhorne |                                                                                           |
| ftpd                                                                                                  | allanjude       |                                                                                           |
| 删除 DES 的相关模块                                                                                   | des?            |                                                                                           |
| sendmail                                                                                              | bapt?           |                                                                                           |
| bootloader 中的 forth 支持 🔪                                                                         | imp/stevek      |                                                                                           |
| NIS 服务器组件                                                                                        | des?            |                                                                                           |
| publicwkey(5)                                                                                         | manu            | [D30683](https://reviews.freebsd.org/D30683)、[D30682](https://reviews.freebsd.org/D30682) |
| targ(4) CAM 目标驱动程序                                                                              | imp             |                                                                                           |
| fingerd                                                                                               | ??              | meena 愿意自愿负责                                                                        |
| 3dfx(4)和`*_isa`                                                                                      | jhb             |                                                                                           |
| syscons(4)（至少弃用）                                                                                | emaste / manu   |                                                                                           |
| 审查以太网驱动程序（100Mbps、少见的 1/10Gbps）                                                        | brooks          |                                                                                           |
| 审查 CAM 驱动程序（pms(4)等）                                                                         | imp             |                                                                                           |
| ACPI 安全定时器                                                                                       | cperciva        |                                                                                           |
| freebsd-update                                                                                        | cperciva        | 如果 pkgbase 准备好                                                                       |
| 32 位平台（内核，保留 compat32）                                                                      | jhb             |                                                                                           |
| arm\*soft 移除（支持构建完整的软件系统，在删除 libsoft hack 构建和 ld.so 支持后，这是唯一剩下的部分） | imp             |                                                                                           |

## 图例

| 符号 | 含义           |
| ---- | -------------- |
| ??   | 状态有问题     |
| !!   | 需要新的负责人 |
