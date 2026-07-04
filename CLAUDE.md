# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.


## Lint 配置

- 不带选项和参数的裸命令，如 mv cp 等，一般不加反引号 “`”，即不进行包裹。

- **markdownlint**（`.github/.markdownlint.json`）：本地已安装 `markdownlint-cli2 v0.22.1`（基于 `markdownlint v0.40.0`），可在本地直接运行检查与修复
  - **本地运行命令**（在仓库根目录执行）：

    ```sh
    # 检查全部中文 .md（排除 en/、.github/、.gitbook/、node_modules/、script/）
    markdownlint-cli2 "**/*.md" "!en/**" "!.github/**" "!.gitbook/**" "!node_modules/**" "!script/**" --config .github/.markdownlint.json

    # 自动修复可修复的问题（MD012 多余空行、MD047 末尾换行、MD034 裸 URL 等）
    markdownlint-cli2 "**/*.md" "!en/**" "!.github/**" "!.gitbook/**" "!node_modules/**" "!script/**" --config .github/.markdownlint.json --fix
    ```

  - **MD060 表格列风格规则（重要）**：配置为 `"style": "compact"` + `"aligned_delimiter": true`
    - **compact 风格**：管道符两侧各保留**单个空格**，例如 `| cell1 | cell2 |`；空单元格写作 `| |`（不是 `||` 或 `|  |`）
    - **aligned_delimiter**：分隔行 `|---|` 的管道符位置必须与表头行的管道符位置对齐
    - **CJK 显示宽度**：markdownlint 按**显示宽度**计算列位置，**每个中文字符按 2 宽度**计算（与英文 1 宽度不同）。因此含 CJK 的列宽 = CJK 字符数 × 2 + ASCII 字符数 × 1
    - **分隔行 dash 数量公式**：若某列内容显示宽度为 W，则分隔行该列总宽（含两侧空格）也应为 W，dash 数量 = W − 4（减去前后各 1 空格 + 前后各 1 冒号）。例如列内容 `FreeBSD 版本` 显示宽度 = 7+1+4 = 12，分隔行应为 ` :--------: `（8 个 dash）
    - **常见错误修复**：当 markdownlint 报 `MD060/table-column-style [Table pipe does not align with header for option "aligned_delimiter"]` 时，需手动扩展分隔行 dash 数量，使管道符位置与表头按显示宽度对齐；`--fix` 无法自动修复此类问题
  - **MD056 表格列数规则**：表头声明几列，所有数据行都必须有几列；末尾缺空单元格时需补 `| |`，而非省略管道符
- **textlint**（`.textlintrc`）：仅启用 `ja-space-between-half-and-full-width` 规则，用于 CJK/英文空格检查
