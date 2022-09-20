# 第五节 使用 bhyve 安装 Windows 11

## 基本思路

首先，完全可行，已经有人实现（见参考资料）。其次，Windows 11 与 Windows 10 的不同之处在于前者对硬件的设备的要求更高，要求强制的 TPM 模块（受信任的平台）。并且强制要求使用 UEFI GPT。所以需要对镜像做一些额外的修改才可以加载使用（参考资料似乎不需要这些）。最后，其他的应该和 Windows 10 是相同的。

## 参考资料

 - <https://github.com/churchers/vm-bhyve/wiki/Running-Windows>
 - <https://twitter.com/bhyve_dev/status/1446404943020056581>
 - <https://forums.freebsd.org/threads/windows-11-on-bhyve.82371/>
 - <https://dadv.livejournal.com/209650.html>
 - <https://wiki.freebsd.org/bhyve/Windows>

