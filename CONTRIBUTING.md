# 贡献指南与开放任务

细节参见 <https://github.com/FreeBSD-Ask/FreeBSD-Ask/wiki>。

## 为什么不去建设《FreeBSD 手册》

我们意识到在现有框架内推动《FreeBSD 手册》的全面现代化改进存在较大困难。笔者提交的多个 PR 往往需要经历一年甚至更长时间才被接受，提交者普遍缺乏时间感和动力。在这样沉重的阻力下，传统路径难以奏效。

因此，我们决定探索一种更开放、高效的协作模式，创造一本更贴近用户需求、更新及时且易于维护的 FreeBSD 文档。这本书的出现，正是为了填补这一空白，服务更广泛的 FreeBSD 用户和社区。

### 方法论

使之成为“一本书”，而不仅仅是本字典或手册：

- 如果某一技术在最新版本被移除，则应及时移除其在本书的对应位置内容
- 使全书语气温柔而坚定
- 在最大化减少原文引用的前提下，重写各章节内容，删除冗余。
- 现代化、简化 BSD 中文文档协作方式：
  - 自动化（CI 检查、预览、生成 HTML/PDF）
  - 仅用最基础的 Markdown 语法，避免复杂扩展和繁琐流程
  - 技术和选材与时俱进，确保内容现代化。
- 严格验证每一部分：
  - 参考文献：不仅要求来源可查，而且要求来源可信：
  - 原理性内容：
    - 追溯到具体 FreeBSD 源码文件、提交记录或函数；
    - 具体到相关标准、规范、法律文件等
    - 分析其设计哲学与开发思路
  - 操作性内容：在 FreeBSD 环境中亲自试验，确保可复现
- 审视原作者的开发哲学与理念，评价其合理性，并尝试简单参与相关项目。
- 指出并修正上游官方手册中的错误或已过时内容。
- 生成英文版本

## 贡献指南

如果你想让你的教程出现在本书中，你可以这样做：

- 如果你熟悉 GitHub，可以点击电脑端右侧的“编辑此页”，进入项目进行操作。整个项目使用 Markdown 语法 +  Gitbook，简单易上手（具体详见项目 WiKi）；
- 如果以上有困难，你还可以发 PDF、Word 或者 TXT 给我。请将文件发送至电子邮件 `yklaxds@gmail.com`（我将在 3 天内回复。若我没有回复，请换个邮件再发一次，或者提交 issue）；如果有视频教程，以各大云盘链接为宜。

本书现接受以下内容：

- 一切与 BSD 相关（包括不限于 FreeBSD，OpenBSD，NetBSD）以及各种体系结构的教程。你既可以扩充当前教程，也可以新建一节；
- 下方的 ToDo 列表；
- 你亦可在文学故事章节分享你与 BSD 的故事，你的个人心得体会。

### 如何使用 git 拉取本项目

本项目太大，拉取时可能会导致缓冲区溢出，可改变 git 配置文件，以实现对缓冲区的扩大：

以下是一个可用的 `~/.gitconfig`（Windows 位置为 `C:\Users\你的用户名\.gitconfig`） 的文件示例：

```ini
[filter "lfs"]
	required = true
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
	process = git-lfs filter-process
[user]
	name = # 你的用户名
	email = # 你的邮箱
	signingkey = # 你的密钥 ID，使用密钥签名时需要
[commit]
	gpgsign = true # 使用密钥签名时需要
[core]
	autocrlf = true # 自动调整末尾回车与换行
[http]
	proxy = http://localhost:7890 # 设置使用 http 代理
	postBuffer = 1048576000 # 扩大缓冲区，约 1 GB
	maxRequestBuffer = 1048576000 # 扩大缓冲区，约 1 GB
```

名词解释：

- `autocrlf`：配置 Git 自动处理(转换)行结束符的默认行为。参见[配置 Git 处理行结束符 - Github Docs](https://docs.github.com/zh/get-started/git-basics/configuring-git-to-handle-line-endings)
- `signingkey`：指设置带签名提交时默认使用的签名密钥。signingkey 既可指 GPG Key，亦可指 SSH Key。因为自 Git 2.34 起，Git 支持了 SSH 签名验证功能。参见[关于提交签名验证 - Github Docs](https://docs.github.com/zh/authentication/managing-commit-signature-verification/about-commit-signature-verification)

拉取命令：

```sh
$ git clone https://github.com/FreeBSD-Ask/FreeBSD-Ask
```

#### 故障排除

- `致命错误:无法访问 'https://github.com/FreeBSD-Ask/FreeBSD-Ask/': Recv failure: 连接被对方重置`

请尝试拉取这个项目 `https://github.com/FreeBSD-Ask/LDWG`。

如果报错类似，说明你的网络有问题。请使用代理。

## 开放任务

所有任务的排序都是随机的并无优先级之分，你可以选你喜欢的去做。

### 开源社区

#### 维护百度百科、维基百科相关条目

如增补修订各大 BSD 中文条目。

#### 帮助修订 UTSC 镜像脚本

- <https://github.com/ustclug/ustcmirror-images/blob/master/freebsd-pkg/sync.sh>
- <https://github.com/ustclug/ustcmirror-images/blob/master/freebsd-ports/sync-ports.sh>

### FreeBSD ToDo

**不再需要** 的内容（请 **不要** 撰写下列条目）：

- [ ] 9.6.图像扫描仪（谁有？而且谁支持 FreeBSD？）
- [ ] 18.7.在 MAC Jail 中运行 Nagios（过时，不写。请用其他案例代替）
- [ ] 第 11 章 打印（本节对中英文均无意义，不引入）
- [ ] 24.8.基于 FreeBSD 的 Xen™ 虚拟机（过时、支持差。真的支持 Windows 11 吗？10 也行。Xen 真难用，而且删除了 PV 支持）
- [ ] 31.4.Sendmail（过时，用 Postfix 等代替）
- [ ] 32.2.inetd 超级服务器（过时。谁在用？）
- [ ] 32.4.网络信息系统（NIS）（过时，用 SSSD-LADP 代替）
- [ ] 30.5.使用 ATM 上的 PPP (PPPoA)（过时）
- [ ] 29.4.拨入服务（过时）
- [ ] gbde 相关加密（已从[源代码](https://github.com/freebsd/freebsd-src/commit/8d2d1d651678178aa7f24f0530347f860423fd9e)移除）
- [ ] 29.5.拨出服务（过时）
- [ ] 30.2.配置 PPP（过时）
- [ ] 31.3.DragonFly 邮件代理（DMA）（过时，用 Postfix 等代替）
- [ ] 20.10.文件系统快照（UFS）（UFS 快照？？？）
- [ ] 21.8.通过 GEOM 实现 UFS 日志（无意义）

 **Just for fun**（没有也行无关紧要）

- [ ] 20.7.创建和使用软盘（谁还有这种东西？2024，日本政府决定全面淘汰软盘）（无意义，但勉强可以写，若有光驱和软盘 *Just for fun*）
- [ ] 20.6.创建和使用 DVD（无意义，但勉强可以写，若有光驱和光盘 *Just for fun*）
- [ ] 20.5.创建和使用 CD（无意义，但勉强可以写，若有光驱和光盘 *Just for fun*）
- [ ] 16.9.Kerberos（谁在用？）

**需要重写** 的内容（请撰写这些内容）：

参见 [Projects](https://github.com/FreeBSD-Ask/FreeBSD-Ask/projects)。

### NetBSD ToDo

参见 [Projects](https://github.com/FreeBSD-Ask/FreeBSD-Ask/projects)。

### DragonFlyBSD ToDo

参见 [Projects](https://github.com/FreeBSD-Ask/FreeBSD-Ask/projects)。
