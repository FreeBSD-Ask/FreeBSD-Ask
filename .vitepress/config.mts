import { defineConfig } from "vitepress";
import autoNav from "vite-plugin-vitepress-auto-nav";
import type MarkdownIt from "markdown-it";
import footnote from "markdown-it-footnote";
import taskLists from "markdown-it-task-checkbox";
import {
    chineseSearchOptimize,
    pagefindPlugin,
} from "vitepress-plugin-pagefind";
import lightbox from "vitepress-plugin-lightbox";
import { RSSOptions, RssPlugin } from "vitepress-plugin-rss";

const baseUrl = 'https://docs.bsdcn.org'
const RSS: RSSOptions = {
  title: 'FreeBSD 从入门到跑路',
  baseUrl,
  copyright: 'Copyright (c) 2021-present, FreeBSD 中文社区',
  language: 'zh-cn',
  favicon: 'https://docs.bsdcn.org/favicon.ico',
}

export default defineConfig({
    sitemap: {
        hostname: "https://docs.bsdcn.org",
    },
    lang: "zh-CN",
    lastUpdated: true,
    title: "FreeBSD 从入门到跑路",
    description: "FreeBSD 从入门到跑路",
    cleanUrls: true, // 在 URL 中去掉 .html 后缀
    metaChunk: true, // 参见 https://vitepress.dev/zh/reference/site-config#metachunk
    markdown: {
        image: {
        // 开启图片懒加载
        lazyLoading: true
        },
        lineNumbers: true, // 启用行号于代码块
        math: true, // 数学公式
        config: (md) => {
            // 使用 lightbox plugin
            md.use(lightbox, {});
            const MAX_LEVEL = 6; // 支持的最大标题层级
            const counters = new Array<number>(MAX_LEVEL + 1).fill(0); // 索引 1~6 对应 H1~H6，0 未使用
            let h1Prefix = "";
            let skipNumbering = false; // 是否跳过编号的标志

            md.core.ruler.push("auto_heading_number", (state) => {
                counters.fill(0);
                h1Prefix = "";
                skipNumbering = false;

                for (let i = 0; i < state.tokens.length; i++) {
                    const tok = state.tokens[i];
                    if (tok.type !== "heading_open") continue;

                    const level = +tok.tag.slice(1);
                    const inline = state.tokens[i + 1];
                    if (!inline || inline.type !== "inline") continue;

                    // H1 处理：解析数字前缀，决定是否对子标题编号
                    if (level === 1) {
                        const textNode = inline.children.find(
                            (t) => t.type === "text",
                        );
                        if (textNode) {
                            const m =
                                textNode.content.match(/^(\d+\.\d+)\s+(.*)$/);
                            if (m) {
                                // 包含数字前缀的 H1
                                h1Prefix = m[1];
                                textNode.content = `${h1Prefix} ${m[2]}`;
                                skipNumbering = false;
                                counters.fill(0, 2); // 重置 H2~H6 计数器
                            } else {
                                // 不包含数字前缀的 H1（如“前言”）
                                h1Prefix = "";
                                skipNumbering = true;
                            }
                        }
                        continue;
                    }

                    // 处于跳过编号状态时直接跳过
                    if (skipNumbering) continue;

                    // 仅处理 H2~H6
                    if (level < 2 || level > MAX_LEVEL) continue;

                    // 自增当前层级计数器，并重置所有更深层级计数器
                    counters[level]++;
                    for (let l = level + 1; l <= MAX_LEVEL; l++) {
                        counters[l] = 0;
                    }

                    // 数据驱动构造编号：按需拼接 h1Prefix 与 H2~当前层级的计数
                    const parts: string[] = [];
                    if (h1Prefix) parts.push(h1Prefix);
                    for (let l = 2; l <= level; l++) {
                        parts.push(String(counters[l]));
                    }
                    const prefix = parts.join(".");

                    if (prefix) {
                        // 创建编号文本节点并插入到标题开头
                        const numToken = new state.Token("text", "", 0);
                        numToken.content = `${prefix} `;
                        inline.children.unshift(numToken);
                    }
                }
            });

            // —— 插件加载 ——
            md.use(footnote);
            md.use(taskLists, {
                disabled: true,
                divWrap: false,
                divClass: "checkbox",
                idPrefix: "cbx_",
                ulClass: "task-list",
                liClass: "task-list-item",
            });

            // 修改脚注样式
            md.renderer.rules.footnote_anchor = (
                tokens,
                idx,
                options,
                env,
                slf,
            ) => {
                let id =
                    slf.rules.footnote_anchor_name?.(
                        tokens,
                        idx,
                        options,
                        env,
                        slf,
                    ) || "";
                if (tokens[idx].meta.subId > 0)
                    id += ":" + tokens[idx].meta.subId;
                return ` <a href="#fnref${id}" class="footnote-backref">🔼</a>`;
            };

            // 为行内 code 添加 v-pre
            const defaultInline = md.renderer.rules.code_inline;
            md.renderer.rules.code_inline = (
                tokens,
                idx,
                options,
                env,
                self,
            ) => {
                tokens[idx].attrSet("v-pre", "");
                return defaultInline(tokens, idx, options, env, self);
            };
        },
    },
    head: [
        [
            "script",
            {},
            `import('/pagefind/pagefind.js')
        .then((module) => {
          window.__pagefind__ = module
          module.init()
        })
        .catch(() => {
          // console.log('not load /pagefind/pagefind.js')
        })`,
        ],
        [
            "link",
            {
                rel: "icon",
                href: "/favicon.ico",
            },
        ],
        [
            "meta",
            {
                name: "keywords",
                content: "",
            },
        ],
        [
            "script",
            {
                async: "",
                src: "https://www.googletagmanager.com/gtag/js?id=G-GKTJ5MJJ58",
            },
        ],
        [
            "script",
            {},
            `window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-31WQ8W3FF6');`,
        ],
    ],
    themeConfig: {
        socialLinks: [],
        siteTitle: "FreeBSD 中文社区",
        langMenuLabel: "多语言",
        returnToTopLabel: "回到顶部",
        darkModeSwitchLabel: "主题",
        lightModeSwitchTitle: "切换到浅色模式",
        darkModeSwitchTitle: "切换到深色模式",
        docFooter: {
            prev: "上一页",
            next: "下一页",
        },
        //自定义 404 页面
        notFound: {
            title: "页面未找到",
            quote: "哎呀，抱歉！您访问的页面好像去“捉迷藏”了，没找着呀！", // set to '' to hide
            linkLabel: "go to home", // aria-label
            linkText: "返回首页",
            code: "404 - 页面未找到",
        },
        logo: {
            src: "/logo.svg",
            width: 24,
            height: 24,
        },
        nav: [
            {
                text: "QQ 群 787969044",
                link: "https://qm.qq.com/q/cX5mpJ36gg",
            },
            {
                text: "FreeBSD 中文社区",
                link: "https://bsdcn.org",
            },
            {
                text: "回到主站",
                link: "https://book.bsdcn.org",
            },
            {
                text: "目录",
                link: "mu-lu.md",
            },
            {
                text: "视频教程Ⅰ",
                link: "https://www.bilibili.com/video/BV1Qji2YLEgS/",
            },
            {
                text: "视频教程Ⅱ",
                link: "https://www.bilibili.com/video/BV12m4y1w7FS/",
            },
        ],
        base: "/",
        editLink: {
            text: "在 GitHub 上编辑此页面",
            pattern:
                "https://github.com/FreeBSD-Ask/FreeBSD-Ask/edit/main/:path",
        },
        outline: {
            label: "此页目录",
            level: "deep",
        },
        sidebarMenuLabel: "目录",
        lastUpdated: {
            text: "最后更新于",
            formatOptions: {
                dateStyle: "full",
                timeStyle: "full",
            },
        },
    },

    vite: {
        plugins: [
            pagefindPlugin({
                customSearchQuery: chineseSearchOptimize,
                btnPlaceholder: "搜索",
                placeholder: "搜索文档",
                emptyText: "空空如也",
                heading: "共: {{searchResult}} 条结果",
                excludeSelector: ["img", "a.header-anchor"],
            }),
            RssPlugin(RSS),
            autoNav({
                summary: {
                    target: "docs/SUMMARY.md",
                    collapsed: false,
                },
            }),
        ],
    },
});
