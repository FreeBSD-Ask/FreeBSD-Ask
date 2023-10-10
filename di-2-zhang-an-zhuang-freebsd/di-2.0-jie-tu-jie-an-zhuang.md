# 第 2.0 节 图解安装

以下为 `FreeBSD-14.0-ALPHA2-amd64-20230818-77013f29d048-264841-disc1.iso` 的安装说明。DVD 请自行研究，大同小异。

![](../.gitbook/assets/安装1.png)

推荐等待十秒即可自动进入，也可以直接回车进入。

|     选项     |                                   解释                                    |
| :----------: | :-----------------------------------------------------------------------: |
| ACPI Support | ACPI 支持。有很多教程说有问题就关闭他，实际上是胡扯。关闭了反而问题会更多 |
|  Safe Mode   |                                 安全模式                                  |
| Single User  |               单用户模式，找回 root 密码或修复磁盘时会用到                |
|   Verbose    |                          啰嗦模式，显示更多输出                           |

![](../.gitbook/assets/安装2.png)

选择 `install`,按下`回车键`进行安装。

![](../.gitbook/assets/安装3.png)

这里是设置键盘，直接回车即可。

![](../.gitbook/assets/安装4.png)

此处是设置主机名。**严禁直接回车，设置主机名为空，否则后果自负。**

![](../.gitbook/assets/安装5.png)

推荐：只选 `src` 以及 `lib32`。部分显卡驱动或其他程序需要 `src`，经测试 `lib32` 后天安装无效。不推荐选 `ports`，因为太老了，还不如直接从源里拉取最新的。

**严禁全选，全选部分组件会使用网络进行安装。**

|    选项    |                                 解释                                  |
| :--------: | :-------------------------------------------------------------------: |
|  base-dbg  |                 激活调试符号的基础工具，如 cat、ls 等                 |
| kernel-dbg |                       激活内核和模块的调试符号                        |
| lib32-dbg  | 用于在激活调试符号的 64 位版本的 FreeBSD 上运行 32 位应用程序的兼容库 |
|   lib32    |        用于在 64 位版本的 FreeBSD 上运行 32 位应用程序的兼容库        |
|   ports    |                                 ports                                 |
|    src     |                              系统源代码                               |
|   tests    |                               测试工具                                |

![](../.gitbook/assets/安装6.png)

推荐：文件分区详解在第 6 章。这里推荐选择 auto ZFS/UFS，一般来说内存小于 8GB 的应该选择 UFS，内存 8G 及以上的应该选用 ZFS。允许手动分区解压 txz 文件以自定义。

> 注意：如果使用手动分区一直提示分区表损坏（corrupted）或类似字样，请先退出重启进入 shell 模式，刷新分区表：
>
> ```shell-session
> # gpart recover ada0
> ```
>
> 你在手动安装的时候可以判断是哪块硬盘，以确定 ada0 这个参数是多少。
>
> 刷新后，输入 `bsdinstall` 即可进入安装模式。
>
> 原因详情见 [FreeBSD 手册](https://handbook.bsdcn.org/di-18-zhang-cun-chu/18.3.-tiao-zheng-he-zeng-jia-ci-pan-da-xiao.html)，但是我认为这是一个 bug。

![](../.gitbook/assets/安装7.png)

现代计算机应该选择 GPT+UEFI。较老的计算机（比如 2013 年以前的）应该选择保持与图片一致的选项（GPT(BIOS)）。

![](../.gitbook/assets/安装8.png)

![](../.gitbook/assets/安装8.1.png)

![](../.gitbook/assets/安装8.2.png)

![](../.gitbook/assets/安装9.png)

![](../.gitbook/assets/安装10.png)

![](../.gitbook/assets/安装11.png)

![](../.gitbook/assets/安装11.1.png)


此处输入 root 密码，密码不会显示在屏幕上，且要求重复输入两次以确认一致性。密码强度默认无要求。



![](../.gitbook/assets/安装12.png)

![](../.gitbook/assets/安装13.png)

![](../.gitbook/assets/安装14.png)

![](../.gitbook/assets/安装15.png)

![](../.gitbook/assets/安装16.png)

![](../.gitbook/assets/安装17.png)

保持 DHCP 获取的 DNS 即可，也可以使用其他 DNS。

![](../.gitbook/assets/安装18.png)

![](../.gitbook/assets/安装19.png)

![](../.gitbook/assets/安装20.png)

![](../.gitbook/assets/安装21.png)

![](../.gitbook/assets/安装22.png)

![](../.gitbook/assets/安装23.png)

![](../.gitbook/assets/installbsd.png)

**严禁全选**

不要选`local_unbound`，会影响 DNS，见 [https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=262290](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=262290)。

虚拟机不需要选 `powerd`。

|     选项      |                                                                                  解释                                                                                   |
| :-----------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| local_unbound | 启用 DNS 本地非绑定。这是基本系统预置的 unbound，仅用于本地缓存转发解析器使用。注意：如果开启，你的系统将不会正确联网，需要手动配置 DNS。如果你不知道这是什么不建议开启 |
|     sshd      |                                                                              开启 ssh 服务                                                                              |
|    moused     |                                                                           在 tty 界面显示鼠标                                                                           |
|    ntpdate    |                                                                      启用启动时的自动时钟同步功能                                                                       |
|     ntpd      |                                                              用于自动时钟同步的网络时间协议（NTP）守护程序                                                              |
|    powerd     |                                                                                电源管理                                                                                 |
|    dumpdev    |                                                                       启用崩溃转储，用于调试系统                                                                        |

![](../.gitbook/assets/安装25.png)

推荐选择：这里是安全增强选择，应该选择 `disable_sendmail`，如果不禁止这个服务会使你在每次开机的时候卡上几分钟，而且这个服务本身没什么用，发邮件用的。

**在 FreeBSD 14 中已不存在该选项，可跳过此步骤。**

![](../.gitbook/assets/安装26.png)

![](../.gitbook/assets/安装26.2.png)

**如果你要创建普通用户，务必将其加入到 wheel 组中。**

这个菜单选项是用来创建普通用户的。root 敢死队可以无视之。其他参数可以保持默认设置不变。在 FreeBSD 14 及以后，所有用户的 shell 都被统一为了 sh。

![](../.gitbook/assets/安装27.png)

![](../.gitbook/assets/安装28.png)

![](../.gitbook/assets/安装29.png)

