# 贡献指南与开放任务

## 为什么不去建设《FreeBSD 手册》

FreeBSD 项目拒绝（表现为长期搁置）任何实质上的 PR，除了季度报告。事实上，纵观提交数据，freebsd doc 项目已经死亡十余年：

使用 [统计分析 git 项目](https://gist.github.com/ykla/6c3df44c371d37fc3196ddf5fa87ce5f) 对 freebsd-doc 进行分析的结果参见 [freebsd-doc-2025 分析报告](https://gist.github.com/ykla/363bf922d0785d0b02dd43f8289368db)。

- 2005-2006 年：第一次显著下滑
- 2015-2016 年：第二次大幅下滑

项目结构复杂且混乱。维护者自己都看不懂。比如在翻译时的某些数据引用是否可复用。

由于其安全报告的文件名在 Windows 下是非法字符（有英文冒号 `:`），因此导致整个项目无法在 Windows 下被正常拉取：

```powershell
PS C:\Users\ykla> git clone https://github.com/freebsd/freebsd-doc
Cloning into 'freebsd-doc'...
remote: Enumerating objects: 617155, done.
remote: Counting objects: 100% (294/294), done.
remote: Compressing objects: 100% (120/120), done.
remote: Total 617155 (delta 217), reused 219 (delta 174), pack-reused 616861 (from 4)
Receiving objects: 100% (617155/617155), 483.71 MiB | 786.00 KiB/s, done.
Resolving deltas: 100% (358420/358420), done.
error: invalid path 'website/static/security/advisories/FreeBSD-EN-04:01.twe.asc' # 观察 FreeBSD-EN-04:01.twe.asc，该文件名在 Windows 下是非法的
fatal: unable to checkout working tree
warning: Clone succeeded, but checkout failed.
You can inspect what was checked out with 'git status'
and retry with 'git restore --source=HEAD :/'
```

## 贡献指南概述

如果你想让你的教程出现在本书中，你可以这样做：

- 如果你熟悉 GitHub，可以点击电脑端右侧的“编辑此页”，进入项目进行操作。整个项目使用 Markdown 语法 +  Gitbook，简单易上手（具体详见项目 WiKi）；
- 如果以上有困难，你还可以发 PDF、Word 或者 TXT 给我。请将文件发送至电子邮件 `yklaxds@gmail.com`（我将在 3 天内回复。若我没有回复，请换个邮件再发一次，或者提交 issue）；如果有视频教程，以各大云盘链接为宜。

本书现接受以下内容：

- 一切与 BSD 相关（包括不限于 FreeBSD，OpenBSD，NetBSD）以及各种体系结构的教程。你既可以扩充当前教程，也可以新建一节；
- 下方的 ToDo 列表或 GitHub Project；
- 你亦可在文学故事章节分享你与 BSD 的故事，你的个人心得体会。

### 基本原则与方法论

#### 基本原则

- 尽可能详细和基础，不要假定用户有任何使用背景
- 使用大型软件（如 IDE、JAVA）时，请注明软件版本号
- **应注意引用的权威性、时效性和准确性。尽量采用原始文献，次选二手文献，避免三手文献**
- 在引用其他网站内容时，请查证其引用的内容是否真实可信，并且不要直接引用网站内容，而是要尽量查阅一手来源
- 请提交到 main 分支
- 请避免学术不端行为，参见 [高等学校预防与处理学术不端行为办法](https://www.gov.cn/zhengce/2016-07/19/content_5713390.htm)
- 遵守 [FreeBSD 中文社区行为规范](https://docs.bsdcn.org/CODE_OF_CONDUCT)

#### 使之成为“一本书”，而不仅仅是本字典或手册

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

#### 细则

- 非拉丁字符与拉丁字符间应该加空格（中英文/数字间应有一个半角空格），有许多 Markdown 格式化工具可以自动完成。
- 不应该使用 `sudo` 而应该用 `#` 代替，除非特例（如讲解如何使用 `sudo` 本身）；普通用户权限请使用 `$` 表示。
- 安装软件时，给出 pkg 或 ports 两种方法，除非极不建议使用 pkg，如特定内核模块等。
- 请注意版权问题。引用或灵感受到启发时，请备注文章链接出处，必要时可使用互联网档案馆进行快照保存。
- 编辑时尽量以最新的 FreeBSD RELEASE 为基准，绝对避免出现 `pkg_add` 此类过时东西。如有必要，必须予以注明版本。
- 对于编写时长问题，理论上会一直持续下去，跟随每个 FreeBSD 大版本迭代。
- 由于种种原因，无法立即验证所写内容是否正确无误时，请编辑者打上“警告：以下内容为理论，未经实际测试，仅供参考，如果可以使用请提交 issue 以移除本标签。”标签以作区分。
- 不应该对文学故事章节进行除错字排版以外的删减。
- 请勿使用诸如 Gitee 等境内无法确保信息安全与数据稳定的平台（这类平台无法保证留存文件的长久可访问性，不适合存放适用于长期归档的内容，在未来会有极大风险无法获取该文件）。
- 当进行错别字修改时，请务必确证其的确是错别字，可参考《现代汉语词典》第 7 版等资料进行佐证。

## 实用附录

### 如何使用 git 拉取本项目

>**技巧**
>
>理论上你完全可以通过 GitHub 在线完成所有提交。

![](https://img.shields.io/github/repo-size/FreeBSD-Ask/FreeBSD-Ask?style=for-the-badge&label=%E6%9C%AC%E9%A1%B9%E7%9B%AE%E5%AD%98%E5%82%A8%E5%BA%93%E4%BD%93%E7%A7%AF&color=EB0028)


本项目太大，使用 git 拉取时可能会导致缓冲区溢出，可改变 git 配置文件，以实现对缓冲区的扩大：

以下是一个可用的 `~/.gitconfig`（Windows 上的位置为 `C:\Users\你的用户名\.gitconfig`） 的文件示例：

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

- `autocrlf`：配置 Git 自动处理(转换)行结束符的默认行为。参见 [配置 Git 处理行结束符 - Github Docs](https://docs.github.com/zh/get-started/git-basics/configuring-git-to-handle-line-endings)
- `signingkey`：指设置带签名提交时默认使用的签名密钥。signingkey 既可指 GPG Key，亦可指 SSH Key。因为自 Git 2.34 起，Git 支持了 SSH 签名验证功能。参见 [关于提交签名验证 - Github Docs](https://docs.github.com/zh/authentication/managing-commit-signature-verification/about-commit-signature-verification)

拉取命令：

```sh
$ git clone https://github.com/FreeBSD-Ask/FreeBSD-Ask
```

#### 故障排除

- `致命错误:无法访问 'https://github.com/FreeBSD-Ask/FreeBSD-Ask/': Recv failure: 连接被对方重置`

请尝试拉取这个项目 `https://github.com/FreeBSD-Ask/LDWG`。

如果报错类似，说明你的网络有问题。请使用代理。

### 项目简介

本项目是主项目（即 `https://book.bsdcn.org`）托管在 Gitbook；

`https://docs.bsdcn.org` 是社区自行构建的，docs 网站本身的贡献指南参见 [FreeBSD 从入门到跑路 VitePress 镜像项目](https://github.com/FreeBSD-Ask/FreeBSD-Ask.github.io/blob/main/README.md)。

>**技巧**
>
>如果你仅想贡献内容本身，尚无改进网站 docs 的浏览体验与构建优化等等意向，则仅需阅读本文即可。

### 项目结构概览

```sh
>FreeBSD-Ask-main
│  .gitattributes  # 用于让 github 正确识别 markdown，用于在 github 正确高亮，正确显示编程语言（Languages）的统计信息
│  .gitignore # 一些规则，用于阻止 git 上传特定类型的文件或目录，如 node_modules
│  CHANGELOG-ARCHIVE.md # 普通文件，记录既往所有重要变动
│  CHANGELOG.md # 普通文件，记录当前季度的重要变动。当你有新的子章节提交或彻底重写时，请将其记录到此处
│  CODE_OF_CONDUCT.md # 用于合规，行为准则
│  CONTRIBUTING.md # 本贡献指南
│  LICENSE # 许可证
│  mu-lu.md # 由 Github Action mulu.yml 自动同步
│  README.md # 主页
│  SECURITY.md # 用于合规，安全报告策略
│  SUMMARY.md # 目录文件，同时用于生成 vitepress 左侧边栏
│
├─.gitbook # 图片目录
│  └─assets # 图片
│          1-install.png
│          1.png
│          1011.png
│          其他图片从略
│
├─.github  # Github Action 相关
│  │  .autocorrectrc # 由 AutoCorrect.yml 调用
│  │  .markdownlint.json # 由 markdown-lint2.yml 调用
│  │  auto_assign.yml # 由 Auto-Assign.yml 调用
│  │  dependabot.yml # 检查 GitHub Action 调用的 Action 有无更新，并提交 PR
│  │  lychee.toml # 由 links.yml 调用
│  │
│  ├─ISSUE_TEMPLATE  # Github issue、PR 模板
│  │      bug_report.md  # Github issue 模板
│  │      feature_request.md  # Github PR 模板
│  │
│  ├─scripts # Github Action 相关，由相关 yml 脚本调用
│  │      check_images.py # 由 check-images.yml 调用
│  │      update_ga4_readme.py # 由 update-ga4.yml 调用
│  │      update_progress.sh # 由 Update-commit-progress.yml 调用
│  │
│  └─workflows # Github Action，用于自动化处理一些简单任务
│          Auto-Assign.yml # 自动为 issue PR 分配人员进行处理
│          AutoCorrect.yml # markdown 格式修正，会自动提交 PR
│          check-images.yml # 检查图片的调用情况，有无正确引用图片，不正确会生成 issue
│          create-pdf.yml # 用于在 GitHub release 生成电子书 PDF、EPUB 
│          file-name-check.yml # 检查 SUMMARY.md 目录中的文件引用是否正确，不正确会生成 issue
│          links.yml # 链接检查，检查文中调用的 URL 是否能正常访问
│          markdown-lint2.yml # markdown 格式检查
│          md-padding.yml # markdown 空格检查与修复
│          mulu.yml # 从 SUMMARY.md 生成的镜像文件
│          sync-headers.yml # 从 SUMMARY.md 更新所有 markdown 文件的一级标题。如果你要修改 `#` 标题，必须在此处进行修改，否则会被其覆盖
│          Update-commit-progress.yml # 进度检查工具，每 3533 次提交为一个版本，用于插入到 README.md
│          update-ga4.yml # 谷歌统计数据，用于插入到 README.md
│
├─.vitepress # vitepress 相关，详见 FreeBSD-Ask/FreeBSD-Ask.github.io
│  │  config.mts
│  │
│  └─theme # vitepress 相关，详见 FreeBSD-Ask/FreeBSD-Ask.github.io
│          custom.css
│          index.js
│          Layout.vue
│
├─di-1-zhang-zou-jin-freebsd # 第 1 章的章节目录
│      di-1.1-unix.md # 第 1 章的文件
│      di-1.2-dao-lun.md
│      di-1.3-jie-freebsd-jian-shi.md
│      di-1.4-Fiat-Lux.md
│
├─di-10-zhang-vpn-yu-dai-li # 第 10 章的章节目录
│      di-10.1-jie-http-dai-li.md # 第 10 章的文件
│      di-10.2-jie-v2ray.md
│      di-10.3-jie-clash.md
│      di-10.4-jie-openvpn.md
│
└─其他目录和文件从略
│
├─public # vitepress 相关，参见 FreeBSD-Ask/FreeBSD-Ask.github.io
│      favicon.ico
│      logo.svg
│
└─其他目录和文件从略
```

### 如何新建章节

自行操作时参见操作实例 [Commit 6023cc8](https://github.com/FreeBSD-Ask/FreeBSD-Ask/commit/6023cc8d58f3a1b9849ff11fa63bf3980177c370) 和下方 `SUMMARY.md` 结构说明。

如果有困难可发邮件联系 ykla 来操作。

#### `SUMMARY.md` 目录结构

```md
# Table of contents

* [FreeBSD 从入门到跑路](README.md)
* [编辑日志](CHANGELOG.md)
* [贡献指南与开放任务](CONTRIBUTING.md)
* [目录](mu-lu.md)

## 前言

* [前言](qian-yan/qian-yan.md)
* [致读者](qian-yan/zhi-du-zhe.md)
* [致谢](qian-yan/zhi-xie.md)
* [绪论](qian-yan/xu-lun.md)

## 第 1 章 FreeBSD 初见

* [1.1 操作系统的历程：UNIX、BSD 和 Linux](di-1-zhang-zou-jin-freebsd/di-1.1-unix.md)
* [1.2 FreeBSD 导论](di-1-zhang-zou-jin-freebsd/di-1.2-dao-lun.md)
* [1.3 George Berkeley（乔治·贝克莱）与 BSD 命名的文化背景](di-1-zhang-zou-jin-freebsd/di-1.3-jie-freebsd-jian-shi.md)
* [1.4 加州大学伯克利分校和“Fiat Lux”（要有光）](di-1-zhang-zou-jin-freebsd/di-1.4-Fiat-Lux.md)

## 第 2 章 安装 FreeBSD

* [2.1 安装前的准备工作](di-2-zhang-an-zhuang-freebsd/di-2.1-install-pre.md)
* [2.2 使用 bsdinstall 开始安装](di-2-zhang-an-zhuang-freebsd/di-2.2-jie-start-install.md)
* [2.3 键盘布局和主机名](di-2-zhang-an-zhuang-freebsd/di-2.3-jie-use-bsdinstall.md)
* [2.4 选择安装组件](di-2-zhang-an-zhuang-freebsd/di-2.4-jie-select.md)
* [2.5 分配磁盘空间](di-2-zhang-an-zhuang-freebsd/di-2.5-jie-fen-pei-disk.md)
* [2.6 设置 root 密码](di-2-zhang-an-zhuang-freebsd/di-2.6-root-jie.md)
* [2.7 网络设置](di-2-zhang-an-zhuang-freebsd/di-2.7-jie-net.md)
* [2.8 时区、服务、安全、固件和账户](di-2-zhang-an-zhuang-freebsd/di-2.8-jie-more.md)
* [2.9 完成安装](di-2-zhang-an-zhuang-freebsd/di-2.9-end-jie.md)
* [2.10 故障排除](di-2-zhang-an-zhuang-freebsd/di-2.10-jie-eol.md)
* [2.11 将 U 盘启动盘恢复为普通 U 盘（基于 Windows）](di-2-zhang-an-zhuang-freebsd/di-2.11-jie-usb.md)

其他从略
```

可以看到，`SUMMARY.md` 在形式上就是普通的 markdown 文档，并无特殊支持。

但是也有一些注意事项：

- 第一行 `# Table of contents` 是绝对不允许变动的，否则 Gitbook 将无法识别，造成失去同步。
- 我们要求应该形如 `* [2.2 使用 bsdinstall 开始安装](di-2-zhang-an-zhuang-freebsd/di-2.2-jie-start-install.md)`，不允许 `* [2.2 使用 bsdinstall 开始安装](di-3-zhang-ni-hao/di-2.2-jie-start-install.md)`，即你的目录结构和放置的文件位置必须一致。（不一致并不会出错，但是本项目要求你一致）
- 通过 `sync-headers.yml`，将自动同步 `SUMMARY.md` 中的章节标题到具体的 markdown 文件中。因此若你要修改 `di-2.2-jie-start-install.md` 的一级标题 `# 2.2 使用 bsdinstall 开始安装`，必须只能修改 `SUMMARY.md` 中的 `2.2 使用 bsdinstall 开始安装`，否则会被 `sync-headers.yml` 覆盖。当二者不同时，若正好在提交时未触发脚本即构建，那么 Gitbook 将以 `SUMMARY.md` 中的目录为准。

### 预览页面

当你提交 PR 时，会自动生成一个预览的网站。

实际上，所有提交都有对应版本的网站：

![](.gitbook/assets/yu-lan1.png)

你可以通过该链接获取你当前 PR 的实际显示样式：

![](.gitbook/assets/yu-lan2.png)

![](.gitbook/assets/yu-lan3.png)

且每次 push 都会自动更新：

![](.gitbook/assets/yu-lan4.png)

## 开放任务

所有任务的排序都是随机的并无优先级之分，你可以选你喜欢的去做。

### 开源社区

#### 维护百度百科、维基百科相关条目

如增补修订各大 BSD 中文条目。

#### 帮助修订 USTC 镜像脚本

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
- [ ] gbde 相关加密（已从 [源代码](https://github.com/freebsd/freebsd-src/commit/8d2d1d651678178aa7f24f0530347f860423fd9e) 移除）
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
