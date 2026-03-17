# 2.4 安装故障排除


## 无法进入安装界面

若是虚拟机，请检查虚拟机配置。

若是物理机：

>请依次检查如下项目：
>
> - 电脑是否为普通家用计算机？
> - 处理器品牌是否为 Intel 或 AMD？
> - 是否已关闭 BIOS 中的安全启动（Secure Boot）？
> - 镜像是否从 <https://www.freebsd.org> 下载？
> - 是否下载了最新版本的 RELEASE 镜像？
> - 下载的镜像文件扩展名是否为 `img`？
> - 镜像校验（SHA256）是否通过？
> - 下载的镜像是否带有 `amd64`（普通家用电脑）字样？
>   - 请确认是 `amd64`（适用于普通电脑）**而非** `arm64`（适用于开发板）。
> - U 盘是否为扩容盘（假冒产品）？
> - 是否使用了 Ventoy 工具？
>   - 建议使用 [Rufus](https://rufus.ie/zh/) [备份](https://web.archive.org/web/20260115142915/https://rufus.ie/zh/) 进行刻录，而非 [Ventoy](https://www.ventoy.net/cn/index.html) [备份](https://web.archive.org/web/20260116224411/https://www.ventoy.net/cn/index.html)。

若仍出现问题，请先在 [官方论坛](https://forums.freebsd.org/) [备份](https://web.archive.org/web/20260119051244/https://forums.freebsd.org/) 使用英语询问；若无果，可按其他章节指引提交 Bug。

## 重启后又进入了安装界面

若是虚拟机，请手动弹出或断开 DVD 的开机自动连接，然后重启。若是物理机，请拔出 U 盘或弹出安装光盘后重启。

## 卡在某项服务

在旧版本安装过程中，系统启动时可能长时间卡在 sendmail 等服务，或者在需要配置静态 IP 地址时，系统却持续尝试 DHCP。

此时可尝试按下 **Ctrl** + **C** 组合键中断该服务，从而继续启动系统。
