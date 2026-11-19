# AGENTS.md

本文件面向 AI 代理与自动化协作者，规定在本仓库中读取、修改、校验与提交的方式。人类贡献者的完整规范见 CONTRIBUTING.md。执行写作或批量修改之前，须先阅读 CONTRIBUTING.md 与 .github/workflows/ 中相关的工作流配置；本文件与二者冲突时，以其为准，并向维护者报告，不得自行取舍。

## 仓库定位

《FreeBSD 从入门到跑路》的正文仓库，Markdown 编写，GitBook 渲染（book.bsdcn.org）。VitePress 站点由 FreeBSD-Ask/FreeBSD-Ask.github.io 单独维护，本仓库只提供内容。收录一切与 FreeBSD 及各体系架构相关的教程，既可扩充既有章节，也可新建章节；文学故事章节接受个人经历与心得。

CI 承担格式检查、目录同步、链接与图片校验、字数统计与 PDF/EPUB 生成。正文只使用基础 Markdown 语法，避免复杂扩展，以保证 GitBook 兼容。

## 目录与命名

- 章节目录为 `di-<章号>-zhang-<拼音>`，章节文件为 `di-<章号>.<节号>-jie-<拼音>.md`，两者的章号必须一致
- 另有 qian-yan（前言）、fu-lu1、fu-lu2（附录）、hou-ji（后记）、public（VitePress 资源）、.gitbook/assets（正文图片）
- 文件名只用 ASCII 小写拼音与连字符，不用中文、空格与大写字母
- 新增章节须同时在 SUMMARY.md 登记，登记路径与实际存放位置必须一致
- 临时脚本与中间产物置于 script/ 或 scripts/（已被 .gitignore 忽略，且不在 lint 范围内）；根目录除书稿与既有配置外不新增文件与目录

## 会被自动覆盖的文件

| 文件 | 维护方式 | 禁止事项 |
| ---- | -------- | -------- |
| SUMMARY.md | 人工维护，目录与一级标题的唯一真源 | 改首行 `# Table of contents`；条目路径与文件位置不一致 |
| mu-lu.md | 由 mulu.yml 从 SUMMARY.md 生成 | 手工编辑 |
| 各章节一级标题 | 由 sync-headers.yml 按 SUMMARY.md 覆盖 | 只改文件内 H1 而不改 SUMMARY.md |
| README.md 的 GA_STATS、GA_BADGES、CHINESE_CHAR_COUNT 标记块 | 由 update-ga4.yml、count-chinese.yml 覆写 | 手工编辑块内文字 |
| CHANGELOG.md | 人工维护，create-pdf.yml 取其全文作 Release 说明 | 删除历史条目或结构性重排 |

## 本地校验

CI 的格式检查均不构成合并门禁，提交前须在本地自查。

| 工具 | 本地版本 | 作用 |
| ---- | -------- | ---- |
| markdownlint-cli2 | v0.24.1（markdownlint v0.42.1） | 语法、空行、表格结构，`--fix` 可修复多数问题 |
| md-padding | 1.10.0 | 在 CJK 与拉丁字符之间补空格 |
| autocorrect | 未纳入本地依赖 | 空格与全角标点；CI 以 yarn 临时安装，仓库无 package.json |

```sh
# 检查
markdownlint-cli2 "**/*.md" "!en/**" "!.github/**" "!.gitbook/**" "!node_modules/**" "!script/**" --config .github/.markdownlint.json

# 修复
markdownlint-cli2 "**/*.md" "!en/**" "!.github/**" "!.gitbook/**" "!node_modules/**" "!script/**" --config .github/.markdownlint.json --fix
```

markdown-lint2.yml 在 CI 中使用无排除的 `**/*.md`；本地排除 .github/ 以免改动工作流与其配置，en/ 为英文版预留、当前不存在。全库 `--fix` 之后必须复核 diff，避免无关文件被夹带修改。

## 表格格式（MD060）

`.github/.markdownlint.json` 对 MD060 启用 `compact` 与 `aligned_delimiter`：单元格与管道符之间恰有一个空格，分隔行的管道符须与表头按显示宽度对齐。`--fix` 只补管道符两侧空格，对齐部分须手算。

计宽方式为 CJK 字符按 2、ASCII 按 1。设表头某列内容显示宽度为 W，单元格内宽为 W + 2，分隔行内宽须与之一致，故 dash 数为：

- 无对齐冒号（`---`）：W
- 左对齐或右对齐（`:---`、`---:`）：W − 1
- 居中（`:---:`）：W − 2

表头 `| FreeBSD 版本 | 支持情况 |` 的两列 W 分别为 12 与 8，无冒号时分隔行为 `| ------------ | -------- |`，居中时写作 `| :----------: | :------: |`。

正文行的管道符不参与对齐检查，只须保持单空格；空单元格写作 `| |`。表头声明几列，数据行就必须有几列（MD056）。

## 其他须遵守的 markdownlint 规则

- MD041、MD025、MD003：首个非空行为唯一的一级标题，用 ATX 风格 `#`
- MD022、MD031、MD032、MD058：标题、代码块、列表、表格前后各留一个空行
- MD040：围栏代码块须标注语言
- MD047、MD012、MD009：文件以单个换行结尾，不出现连续空行，行尾不留空格
- MD034：裸 URL 写作 `<https://example.com>` 形式
- MD049、MD050：强调用 `*斜体*` 与 `**粗体**`
- MD013 关闭，段落按一段一行书写，不做硬换行；MD033 关闭，允许内联 HTML；MD036 关闭，不检查以强调代替标题
- 行尾由 .gitattributes 强制为 LF，Windows 本地编辑须避免写入 CRLF

## CI 全景

| 工作流 | 触发 | 行为 |
| ------ | ---- | ---- |
| markdown-lint2.yml | 仅 workflow_dispatch | markdownlint 检查并以 fix 回写，失败时建 PR |
| AutoCorrect.yml | repository_dispatch、workflow_dispatch | autocorrect 修正空格与全角标点，建 PR |
| md-padding.yml | repository_dispatch、workflow_dispatch | md-padding 补 CJK 空格，建 PR |
| links.yml | 每月 15 日 18:00（UTC）、手动 | lychee 检查全库链接，失败时建 issue |
| file-name-check.yml | push（`**/*.md`） | 校验 SUMMARY.md 条目所指文件存在，缺失时建 issue（label summary-check） |
| check-images.yml | push（`.gitbook/assets/**`） | check_images.py 比对图片引用与实存，缺失或未使用时建 issue |
| mulu.yml | push（SUMMARY.md） | 生成 mu-lu.md 并自动提交 |
| sync-headers.yml | push、mulu.yml 完成后 | 按 SUMMARY.md 覆盖各文件一级标题并自动提交 |
| count-chinese.yml | 每月 1 日 20:10（UTC） | 统计字数写入 README 标记块并提交 |
| update-ga4.yml | 每月 1 日 15:10（UTC） | GA4 数据写入 README 标记块并提交 |
| create-pdf.yml | 每周日 15:30（UTC） | 打 YYYY.MM.DD 标签，构建 PDF/EPUB 并发布 Release |
| Auto-Assign.yml | issue、PR 事件 | 自动指派 ykla |
| dependabot.yml | 每日 | 检查 Action 版本并提 PR |

由此产生三项约束：格式问题不会在 PR 上被自动拦截；涉及 README、mu-lu.md、一级标题的改动须从源头文件驱动；工作流的自动提交会改写工作区，避免与之并发修改同一文件。

## 提交与 PR

- 一律提交至 main 分支；PR 自动指派 ykla，并生成 GitBook 预览站点，每次 push 自动更新
- 新增子章节、彻底重写或删除章节时，在 CHANGELOG.md 当季分节下记录，格式为 `- YYYY.M.D` 加二级缩进条目，写明改动与原因
- 提交信息以中文陈述改动，可附 PR 编号，如 `增补 (#2368)`、`第 13.9 节改用 Budgie 替代 CDE (#2364)`；`CI:`、`chore:` 前缀属自动提交，人工提交不加
- 格式修正与内容改动分开提交，避免全库 `--fix` 掩盖内容 diff
- 仓库体积较大，clone 或 pull 失败时按 CONTRIBUTING.md 调整 http.postBuffer 与网络代理

## 内容规范

引用与考据：

- 引用优先级为原始文献、二手文献、三手文献；须核实一手来源，不直接转引网站内容
- 引用或受启发之处注明链接；需要长期留存时使用互联网档案馆快照
- 原理性内容溯源到具体源码文件、提交记录或函数，并引用相关标准、规范或法律文件；操作性内容须在真实 FreeBSD 环境验证可复现
- 指出并修正上游官方手册的错误与过时内容；已从 FreeBSD 移除的技术，其对应章节一并删除

写作：

- 面向零基础读者，不假定任何使用背景；介绍大型软件时注明版本号
- 以最新 FreeBSD RELEASE 为基准，禁止 `pkg_add` 等过时内容，必要处标注版本
- 安装软件同时给出 pkg 与 Ports 两种方法，除非明确不建议使用 pkg（如部分内核模块）
- 提示符 root 用 `#`、普通用户用 `$`，不以 sudo 代替，讲解 sudo 本身时除外
- 中文与拉丁字符、数字之间加半角空格
- 未实测内容加标签：“警告：以下内容为理论，未经实际测试，仅供参考，如可使用请提交 issue 以移除本标签。”
- 减少原文引用，改写并删除冗余；全书语气温和而坚定
- 文学故事章节除错别字与排版外不得删减
- 修改错别字须确证，依据《现代汉语词典》第 7 版等资料
- 不使用 Gitee 等无法保证长期可访问的境内平台链接

AIGC：

- 一切 AIGC 内容须经人工二次确认，核实原始出处与来源可靠性后方可提交，纯翻译除外
- 提交者对内容自行负责，无论是否由 AIGC 生成
- 遵守 FreeBSD 中文社区行为规范与学术不端相关规定

## 文档风格

- 不带选项与参数的裸命令（如 mv、cp）不加反引号；带选项、参数或路径时加反引号
- 命令块用 `sh`，配置文件按实际语法标注；示例输出与命令分开

## 参考资料

- CONTRIBUTING.md：收录范围、基本原则、细则、开放任务
- README.md、SECURITY.md、CODE_OF_CONDUCT.md：项目说明、安全策略、行为准则
- .github/workflows/、.github/.markdownlint.json、.github/.autocorrectrc、.github/lychee.toml：CI 行为的唯一依据
