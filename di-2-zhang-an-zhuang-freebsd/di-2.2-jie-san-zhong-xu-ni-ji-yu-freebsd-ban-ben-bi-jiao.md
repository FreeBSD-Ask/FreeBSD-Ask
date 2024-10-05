# 第 2.2 节 三种虚拟机与 FreeBSD 版本比较

## FreeBSD 版本比较

已知 FreeBSD 有如下版本： alpha、rc、beta、release、current、stable。

release 是可以日常/服务器使用的，一般意义上的稳定版或者说是 LTS。而 **stable** 和 current 都是开发分支，都是 **不稳定的**。

>**注意**
>
>FreeBSD 的 ***stable*** 与一般发行版的“稳定版”的概念并不一致，反而是一种 **不稳定** 的“开发版”。

alpha 是 current 进入 release 的第一步。具体过程是 current --> alpha（进入 stable 分支）--> beta --> rc --> release。

current 相对稳定后会推送到 stable，但是不保证二者没有大的 bug。stable 仅确保其 ABI 与所对应的大版本兼容。

### FreeBSD 版本选择

其中 rc 和 beta 都是测试版本。

日常使用应该选择 release 版本，当有多个 release 版本时，应该选择最新的一个；

如果硬件比较新或者需要进行某些测试，应该选择 current 版本，它是滚动地开发版。

>**注意**
>
>只有 rc、beta 和 release（[且是一级架构](https://www.freebsd.org/platforms/)）才能使用命令 `freebsd-update` 更新系统，其余版本系统均需要通过源代码编译的方式（或使用二进制的 pkgbase）更新系统。



## 参考链接：

- [SystemTuning](https://wiki.freebsd.org/SystemTuning)
- [FreeBSD13 を Hyper-V 環境にインストールしてみた所感](https://qiita.com/nanorkyo/items/d33e1befd4eb9c004fcd)

