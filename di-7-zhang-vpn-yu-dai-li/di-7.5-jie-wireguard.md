# 第 7.5 节 Wireguard

WireGuard 是一个极其简单而又快速的现代 VPN，采用了最先进的加密技术。它的目标是比 IPsec 更快、更简单、更精简、更有用，同时避免了大量的头痛问题。它打算比 OpenVPN 的性能要好得多。WireGuard 被设计成一个通用的 VPN，可以在嵌入式接口和超级计算机上运行，适合于许多不同的情况。它最初是为 Linux 内核发布的，现在是跨平台的（Windows、macOS、BSD、iOS、Android），可广泛部署。它目前正在大力发展，但已经被认为是业内最安全、最容易使用和最简单的 VPN 解决方案。但不适合国内情况。

推荐 FreeBSD 13，安装：

```shell-session
# pkg install wireguard
```
