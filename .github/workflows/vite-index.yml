name: 🔗 从 README.md 更新 Vitepress 首页

on:
  push:
    # 当根目录下的 README.md 被修改时触发工作流
    paths:
      - 'README.md'
  workflow_dispatch:
jobs:
  update-mu-lu:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v5
        with:
          # 获取完整历史记录，便于后续提交操作
          fetch-depth: 0

      - name: Delete existing index.md if exists
        run: |
          if [ -f index.md ]; then
            echo "Deleting existing index.md..."
            rm index.md
          else
            echo "index.md not found, skipping deletion."
          fi

      - name: Copy README.md to index.md
        run: |
          cp README.md index.md
          echo "Copied README.md to index.md"

      - name: Commit and push changes
        uses: stefanzweifel/git-auto-commit-action@v7
        with:
          commit_message: "从 README.md 更新 index.md [skip ci]"
          file_pattern: "index.md"
